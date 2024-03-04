from selenium.webdriver.common.by import By

# first process in selling
selling_tickets_button = (By.XPATH, "//p[text()='מכירת כרטיסים']")
next_button = (By.XPATH, "//button[text()='הבא']")

category_filed = (By.ID, "//*[@id='eventInfoForm_category']")
artistName_filed = (By.ID, "//*[@id='eventInfoForm_artistName']")
eventDate_filed = (By.ID, "//*[@id='eventInfoForm_eventDate']")
eventTime_filed = (By.ID, "//*[@id='eventInfoForm_eventTime']")

checkbox_locator = (By.XPATH, "//label[text()='כמה אמנים']/preceding-sibling/input[@type='radio']")
one_artist_radio_locator = (By.XPATH, "//label[text()='אמן אחד']/preceding-sibling/input[@type='radio']")

# second process in selling

back_button = (By.XPATH, "//button[text()='חזרה']")
next_button = (By.XPATH, "//button[text()='הבא']")

sitting_details_filed = (By.ID, "eventInfoForm_typeDescription")
ticket_type_field = (By.ID, "eventInfoForm_ticketType")  # Using ID for better stability
ticket_quantity_field = (By.ID, "eventInfoForm_ticketQuantity")
ticket_price_field = (By.ID, "eventInfoForm_ticketPrice")

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