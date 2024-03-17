import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import safsarX_selling_Tickets.data_of_elements.data


def enter_inputs(actions, my_dict, *value):
    # my_dict = {'element name':(By.NAME, 'firstName') }
    list_of_elements = []
    index = 0
    for key in my_dict.values():
        element = actions.find_element(key)
        dropdown = actions.get_attribute(element, 'aria-haspopup')
        isradio = actions.get_attribute(element, 'type')
        if isradio != 'radio' and isradio != 'checkbox':
            actions.send_keys(element, value[index])
            list_of_elements.append(element)
            if dropdown == "listbox":
                time.sleep(2)
                actions.send_keys(element, Keys.RETURN)
        elif isradio == 'radio' or isradio == 'checkbox':
            actions.click_element(element)
            index = index - 1

        index = index + 1
    return list_of_elements


def find_all_buttons(actions):
    buttons = actions.find_elements((By.TAG_NAME, 'button'))
    return buttons


def find_all_h2_titles(actions):
    # Find all h2 title elements
    h2_titles = actions.find_elements((By.TAG_NAME, 'h2'))
    return h2_titles


def find_all_paragraphs(actions):
    # Find all p text elements
    paragraphs = actions.find_elements((By.TAG_NAME, 'p'))

    return paragraphs


def click_on(actions, text_button):
    button = actions.find_element((By.XPATH, f"//button[text()='{text_button}']"))
    actions.click_element(button)


def page_start_screeen(actions):
    selling_tickets_button = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.selling_tickets_button)
    actions.click_element(selling_tickets_button)
    page = []
    registr_button = actions.find_element((By.XPATH, "//button[text()='הרשמה']"))
    page.append(registr_button.text)
    sign_in_button = actions.find_element((By.XPATH, ' //*[@id="root"]/main/div/div[2]/div[2]/button[2]'))
    page.append(sign_in_button.text)
    title = actions.find_element((By.XPATH, "//h2[contains(text(), 'מכירת כרטיסים')]"))
    page.append(title.text)
    subtitle = actions.find_element((By.XPATH, "//p[contains(text(), 'שנתחיל בלהכיר')]"))
    page.append(subtitle.text)
    print(page)
    return page


def navigation_to_selling_tickets(actions):
    selling_tickets_button = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.selling_tickets_button)
    actions.click_element(selling_tickets_button)
    click_on(actions, 'יש לי חשבון')


def log_in(actions, phone):
    my_dict = {'phone_filed': (safsarX_selling_Tickets.data_of_elements.data.phone_filed)}
    enter_inputs(actions, my_dict, phone)
    enter_button = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.enter_button)
    actions.click_element(enter_button)
    time.sleep(17)
    # wait for enter code
    submit_button = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.submit_button)
    actions.click_element(submit_button)


def success_sell_page(actions):
    back_to_home = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.back_to_home)
    actions.click_element(back_to_home)


def register_page(actions, email, first_name, last_name, phone, isnumber):
    click_on(actions, 'הרשמה')
    my_dict = {'email_field': (By.XPATH, '//*[@id="root"]/main/div[2]/div/div/form/input')}
    enter_inputs(actions, my_dict, email)

    click_on(actions, 'הרשמה')

    enter_inputs(actions, safsarX_selling_Tickets.data_of_elements.data.user_info_fields, first_name, last_name, phone,
                 isnumber)

    check_box = actions.find_element((By.XPATH, '//*[@id="root"]/main/div/div[2]/div/form/div[3]/div[1]/label/input'))
    check_box.click()
    click_on(actions, 'כניסה')


def page_verification_screeen(actions, xpathHeader, xpath_Title, xpath_subtitle, xpath_Text_field, xpath_button):
    selling_tickets_button = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.selling_tickets_button)
    actions.click_element(selling_tickets_button)
    page = []
    header = actions.find_element((xpathHeader))
    page.append(header.text)
    title = actions.find_element((xpath_Title))
    page.append(title.text)
    subtitle = actions.find_element((xpath_subtitle))
    page.append(subtitle.text)
    text_field = actions.find_element((xpath_Text_field))
    page.append(text_field.text)
    button = actions.find_element((xpath_button))
    page.append(button.text)
    return page


def page1_event_info(actions, category_name, artist_name, day, eventLocation, time):
    enter_inputs(actions, safsarX_selling_Tickets.data_of_elements.data.page1_1, category_name, artist_name)

    actions.find_element(safsarX_selling_Tickets.data_of_elements.data.page1.get("date")).click()
    actions.find_element((By.XPATH, f".//div[text()={day}]")).click()

    enter_inputs(actions, safsarX_selling_Tickets.data_of_elements.data.page1_2, eventLocation, time)


def page1_event_info_sport(actions, category_name, subCategory, gameName, playingTeam, againstTeam, day, eventLocation,
                           time):
    enter_inputs(actions, safsarX_selling_Tickets.data_of_elements.data.pagr1_sport, category_name, subCategory,
                 gameName, playingTeam, againstTeam)

    actions.find_element(safsarX_selling_Tickets.data_of_elements.data.page1.get("date")).click()
    actions.find_element((By.XPATH, f".//div[text()={day}]")).click()

    enter_inputs(actions, safsarX_selling_Tickets.data_of_elements.data.page1_2, eventLocation, time)


def page2_ticket_info(actions, event_type, ticket_quantity, ticket_price):
    enter_inputs(actions, safsarX_selling_Tickets.data_of_elements.data.page2, event_type, ticket_quantity,
                 ticket_price)
    # wait to file
    time.sleep(20)


def page3_summary(actions, fullName, bankName, branchNumber, accountNumber):
    enter_inputs(actions, safsarX_selling_Tickets.data_of_elements.data.page3, fullName, bankName, branchNumber,
                 accountNumber)

# elements = actions.find_element((By.ID, 'ID_NAME'))
# actions.send_keys(bankName, text)
#
# elements = actions.find_element((By.ID, 'ID_NAME'))
# actions.send_keys(bankName, text)
#
# elements = actions.find_element((By.ID, 'ID_NAME'))
# actions.send_keys(bankName, text)
#
# elements = actions.find_element((By.ID, 'ID_NAME'))
# actions.send_keys(bankName, text)
#
# elements = actions.find_element((By.ID, 'ID_NAME'))
# actions.send_keys(bankName, text)
