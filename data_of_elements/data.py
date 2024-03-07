from selenium.webdriver.common.by import By

# first process in selling
selling_tickets_button = (By.XPATH, "//p[text()='מכירת כרטיסים']")
next_button = (By.XPATH, "//button[text()='הבא']")

category_field = (By.ID, '//*[@id="category"]/div/div/div/div/div/div')
artistName_field = (By.ID, "//*[@id='eventInfoForm_artistName']")
eventDate_field = (By.ID, "//*[@id='eventInfoForm_eventDate']")
where_event_field = ''
eventTime_field = (By.ID, "//*[@id='eventInfoForm_eventTime']")

its_few_days = ''

artist_radio_locator = (By.XPATH, "//label[text()='כמה אמנים']/preceding-sibling/input[@type='radio']")
one_artist_radio_locator = (By.XPATH, "//label[text()='אמן אחד']/preceding-sibling/input[@type='radio']")

# soccer

which_branch_field = (By.ID, 'eventInfoForm_subCategory')
type_of_game_regular = (By.XPATH, '//*[@id="eventInfoForm_gameType"]/label[1]/span[1]/input')
type_of_game_tournament = (By.XPATH, '//*[@id="eventInfoForm_gameType"]/label[2]/span[1]/input')

# regular & tournament
game_name = (By.ID, 'eventInfoForm_gameName')
playing_team = (By.ID, 'eventInfoForm_playingTeam')
against_team = (By.ID, 'eventInfoForm_againstTeam')

# theater
eventName = (By.ID, 'eventInfoForm_eventName')


# second process in selling

back_button = (By.XPATH, "//button[text()='חזרה']")
next_button = (By.XPATH, "//button[text()='הבא']")

event_style = []

sitting_details_field = (By.ID, "eventInfoForm_typeDescription")
ticket_type_field = (By.ID, "eventInfoForm_ticketType")
ticket_quantity_field = (By.ID, "eventInfoForm_ticketQuantity")
ticket_price_field = (By.ID, "eventInfoForm_ticketPrice")

upload_file = ''

upload_button = (By.XPATH, "//button[text()='העלאת קובץ נוסף']")
delete_buttons = (By.XPATH, "//li/button")

# thread process in selling

back_button = (By.XPATH, "//button[text()='חזרה']")
next_button = (By.XPATH, "//button[text()='הבא']")

full_name_field = (By.ID, "eventInfoForm_fullName")
bank_name_field = (By.ID, "eventInfoForm_bankName")
branch_number_field = (By.ID, "eventInfoForm_branchNumber")
account_number_field = (By.ID, "eventInfoForm_accountNumber")

terms_checkbox = (By.XPATH, "//label[text()='קראתי והסכמתי ל']/preceding-sibling/input[@type='checkbox']")
email_updates_checkbox = (By.XPATH, "//label[text()='קבל עדכונים במייל']/preceding-sibling/input[@type='checkbox']")

# success_page
back_to_home = (By.XPATH, '//*[@id="root"]/main/div[2]/div/a')
succsess_text = (By.XPATH, '//*[@id="root"]/main/div[2]/div/p')
