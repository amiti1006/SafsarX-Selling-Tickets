import time
from selenium.webdriver.common.by import By

import safsarX_selling_Tickets
from safsarX_selling_Tickets.data_of_elements import data
from safsarX_selling_Tickets.selling_tickets_page.driver import webdriver_instance, Actions
from safsarX_selling_Tickets.selling_tickets_page.funcs import page_start_screeen, \
    navigation_to_selling_tickets, register_page, page_verification_screeen, page1_event_info, \
    page2_ticket_info, click_on, page3_summary, find_page_elements, page1_event_info_sport
import pytest

base_url = "https://portal-dev.safsarglobal.link/"
my_driver = webdriver_instance()
my_driver.get(base_url)
actions = Actions(my_driver)


# elements = page_start_screeen(actions)


def test_sent_to_login_register_page():
    my_driver.get(base_url)
    selling_tickets_button = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.selling_tickets_button)
    actions.click_element(selling_tickets_button)
    assert actions.driver.current_url == 'https://portal-dev.safsarglobal.link/start-ticket-sell'


@pytest.mark.parametrize("expected_text", ['הרשמה', 'יש לי חשבון', 'מכירת כרטיסים\nבראש שקט', 'שנתחיל בלהכיר ?'])
def test_navigation(expected_text):
    assert all(expected_text in elements for element in elements)
    my_driver.get(base_url)


def test_success_screen():  # לא נבדק
    my_driver.get(base_url)
    page_start_screeen(actions)
    register_page(actions, 'youuppiiiik@gmail.com', 'שדג', 'דשגשדג', '0544425781', '545879541')

    subtitle = actions.find_element((By.XPATH, "//p[contains(text(), 'אחרי שתמלאו את כל הפרטים')]"))
    assert subtitle
    my_driver.get(base_url)


def test_existing_user_move_to_sign_in():
    my_driver.get(base_url)
    navigation_to_selling_tickets(actions, '0547675277')
    category_name_field = actions.find_element((By.XPATH, '//*[@id="eventInfoForm"]/div[1]/div/label'))
    assert category_name_field.text == 'באיזו קטגוריה הכרטיסים?'
    my_driver.get(base_url)


def test_moveTicket_sale_verification():
    my_driver.get(base_url)
    navigation_to_selling_tickets(actions, '0547675277')
    selling_tickets_button = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.selling_tickets_button)
    actions.click_element(selling_tickets_button)
    assert actions.driver.current_url == 'url of this page'


@pytest.mark.parametrize("expected_text", ['Header', 'Title & subtitle', 'Text field', 'כניסה'])
def test_Verification_Screen_structure(expected_text):
    test_moveTicket_sale_verification()
    elements = page_verification_screeen(actions, 'xpathHeader', 'xpath_Title', 'xpath_subtitle', 'xpath_Text_field',
                                         'xpath_button')
    assert all(expected_text in elements for element in elements)
    my_driver.get(base_url)


def test_full_process_selling():
    navigation_to_selling_tickets(actions, '0533363708')
    page1_event_info(actions, 'ילדים', 'מאיר בנאי', '17', 'היכל התרבות רחובות', '10:59AM')
    click_on(actions, 'הבא')
    page2_ticket_info(actions, 'רגיל', 'כרטיס בודד', '100')
    click_on(actions, 'הבא')
    page3_summary(actions, 'עמית', '11 דיסקונט', '12', '789456')
    click_on(actions, 'הבא')
    time.sleep(20)

    buttons, h2_titles, paragraphs = find_page_elements(actions)
    for x in paragraphs:
        print(x)
    assert any('מכירת הכרטיסים שלך נשלחה לאישור' in paragraph for paragraph in paragraphs)


# test 1
@pytest.mark.parametrize("price,expected_price", [('jhgjh', '₪0')])
def test_price_is_valid(price, expected_price):
    navigation_to_selling_tickets(actions, '0533363708')
    page1_event_info(actions, 'ילדים', 'מאיר בנאי', '17', 'היכל התרבות רחובות', '10:59AM')
    click_on(actions, 'הבא')
    page2_ticket_info(actions, 'רגיל', 'כרטיס בודד', price)
    display_price = actions.find_element((By.XPATH, '//*[@id="eventInfoForm"]/div[5]/div[2]/p')).text
    try:
        assert display_price == expected_price
    except ValueError as e:
        print(display_price, 'לא זהים', e)


# test 2
@pytest.mark.parametrize("actual_input,expected_price", [('!', '')])
def test_invalid_input(actual_input,expected_price):
    navigation_to_selling_tickets(actions, '0533363708')
    page1_event_info_sport(actions, 'ספורט', 'כדורגל','ליגת העל בישראל',actual_input,actual_input, 17, 'גריי מודיעין', '10:59AM')
    playingTeam = actions.find_element( safsarX_selling_Tickets.data_of_elements.data.pagr1_sport.get('playingTeam')).text
    againstTeam = actions.find_element( safsarX_selling_Tickets.data_of_elements.data.pagr1_sport.get('againstTeam')).text
    try:
        assert playingTeam == expected_price
    except ValueError as e:
        print(playingTeam, 'מקבל גם ערכים שגויים', e)

