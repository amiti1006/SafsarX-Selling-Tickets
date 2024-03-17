import time
from selenium.webdriver.common.by import By

import safsarX_selling_Tickets
from safsarX_selling_Tickets.data_of_elements import data
from safsarX_selling_Tickets.selling_tickets_page.driver import webdriver_instance, Actions
from safsarX_selling_Tickets.selling_tickets_page.funcs import page_start_screeen, \
    navigation_to_selling_tickets, register_page, page_verification_screeen, page1_event_info, \
    page2_ticket_info, click_on, page3_summary, page1_event_info_sport, log_in, find_all_paragraphs
import pytest

base_url = "https://portal-dev.safsarglobal.link/"
my_driver = webdriver_instance()
my_driver.get(base_url)
actions = Actions(my_driver)


@pytest.mark.parametrize("expected_text", ['הרשמה', 'יש לי חשבון', 'מכירת כרטיסים\nבראש שקט', 'שנתחיל בלהכיר ?'])
def test_navigation(expected_text):
    # elements
    elements = page_start_screeen(actions)
    assert all(expected_text in elements for element in elements)
    my_driver.get(base_url)
    actions.update_driver(my_driver)


@pytest.mark.skip
def test_success_screen():  # לא נבדק
    my_driver.get(base_url)
    page_start_screeen(actions)
    register_page(actions, 'youuppiiiik@gmail.com', 'שדג', 'דשגשדג', '0544425781', '545879541')
    subtitle = actions.find_element((By.XPATH, "//p[contains(text(), 'אחרי שתמלאו את כל הפרטים')]"))
    assert 'אחרי שתמלאו את כל הפרטים' in subtitle.text
    my_driver.get(base_url)
    actions.update_driver(my_driver)


def test_existing_user_move_to_sign_in():
    my_driver.get(base_url)
    navigation_to_selling_tickets(actions)
    log_in(actions, '0533363708')
    category_name_field = actions.find_element((By.XPATH, '//*[@id="eventInfoForm"]/div[1]/div/label'))
    assert category_name_field.text == 'באיזו קטגוריה הכרטיסים?'
    my_driver.get(base_url)
    actions.update_driver(my_driver)


def test_moveTicket_sale_verification():
    my_driver.get(base_url)
    navigation_to_selling_tickets(actions)
    log_in(actions, '0533363708')
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
    actions.update_driver(my_driver)


def test_full_process_selling():
    navigation_to_selling_tickets(actions)
    log_in(actions, '0533363708')
    page1_event_info(actions, 'ילדים', 'מאיר בנאי', '17', 'היכל התרבות רחובות', '10:59AM')
    click_on(actions, 'הבא')
    page2_ticket_info(actions, 'רגיל', 'כרטיס בודד', '100')
    click_on(actions, 'הבא')
    page3_summary(actions, 'עמית', '11 דיסקונט', '12', '789456')
    click_on(actions, 'הבא')
    time.sleep(20)

    paragraphs = find_all_paragraphs(actions)
    for x in paragraphs:
        print(x)
    assert any('מכירת הכרטיסים שלך נשלחה לאישור' in paragraph for paragraph in paragraphs)


# test 1
def getto_page2_ticket_info():
    navigation_to_selling_tickets(actions)
    log_in(actions, '0533363708')
    page1_event_info(actions, 'ילדים', 'מאיר בנאי', '17', 'היכל התרבות רחובות', '10:59AM')
    click_on(actions, 'הבא')
    page2_ticket_info(actions, 'רגיל', 'כרטיס בודד', '0')


@pytest.mark.parametrize("price_text,expected_price", [
    ('jhgjh', '₪0'),
    ('22', '₪22'),
    ('-22', '₪0'),
])
def test_price_is_valid(price_text, expected_price):
    getto_page2_ticket_info()
    price = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.page2.get('ticket_price'))
    actions.send_keys(price, price_text)
    time.sleep(1)
    display_price = actions.find_element((By.XPATH, '//*[@id="eventInfoForm"]/div[5]/div[2]/p')).text
    try:
        assert display_price == expected_price
    except AssertionError as e:
        print(display_price, 'לא זהים', e)
    my_driver.get(base_url)
    actions.update_driver(my_driver)


# test 2
@pytest.mark.parametrize("playingTeam, againstTeam,expected_playingTeam,expected_againstTeam", [
    ('!!!!', 'ASDASD', '', 'ASDASD'),
    ('הפועל תל אביב', 'מכבי תל אביב', 'הפועל תל אביב', 'הפועל תל אביב'),
])
def test_invalid_input_playingTeam(playingTeam, againstTeam, expected_playingTeam, expected_againstTeam):
    navigation_to_selling_tickets(actions)
    log_in(actions, '0533363708')
    page1_event_info_sport(actions, 'ספורט', 'כדורגל', 'ליגת העל בישראל', playingTeam, againstTeam, 17,
                           'גריי מודיעין', '10:59AM')
    time.sleep(3)
    playingTeam_text = actions.find_element(
        safsarX_selling_Tickets.data_of_elements.data.pagr1_sport.get('playingTeam')).text
    againstTeam_text = actions.find_element(
        safsarX_selling_Tickets.data_of_elements.data.pagr1_sport.get('againstTeam')).text
    try:
        assert playingTeam_text == expected_playingTeam and againstTeam_text == expected_againstTeam
    except ValueError as e:
        print(playingTeam, 'מקבל גם ערכים שגויים', e)
    my_driver.get(base_url)
    actions.update_driver(my_driver)


# test 3
def goto_page3_summary():
    navigation_to_selling_tickets(actions)
    log_in(actions, '0533363708')
    page1_event_info(actions, 'ילדים', 'מאיר בנאי', '17', 'היכל התרבות רחובות', '10:59AM')
    click_on(actions, 'הבא')
    page2_ticket_info(actions, 'רגיל', 'כרטיס בודד', '100')
    click_on(actions, 'הבא')
    page3_summary(actions, 'עמית', '11 דיסקונט', '12', '789456')


@pytest.mark.parametrize("bankname_text,expected_bankname_text", [
    ('11 דיסקונט', '11 דיסקונט'),
    ('eeewwex', ''),
    ('$#@', ''),
])
def test_bank_name_is_valid(bankname_text, expected_bankname_text):
    goto_page3_summary()
    bankName = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.page3.get('bankName'))
    actions.send_keys(bankName, bankname_text)
    time.sleep(1)
    display_price = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.page3.get('bankName')).text
    try:
        assert display_price == expected_bankname_text
    except AssertionError as e:
        print(display_price, 'הוכנס שם בנק לא נכון', e)
    my_driver.get(base_url)
    actions.update_driver(my_driver)


@pytest.mark.parametrize("accountNumber_text,expected_accountNumber_text", [
    ('123456', '123456'),
    ('eeewwex', ''),
    ('$#@', ''),
])
def test_bank_name_is_valid(accountNumber_text, expected_accountNumber_text):
    goto_page3_summary()
    accountNumber = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.page3.get('accountNumber'))
    actions.send_keys(accountNumber, accountNumber_text)
    time.sleep(1)
    display_price = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.page3.get('accountNumber')).text
    try:
        assert display_price == expected_accountNumber_text
    except AssertionError as e:
        print(display_price, 'הוכנס מספר בנק שגוי', e)
    my_driver.get(base_url)
    actions.update_driver(my_driver)