from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # creates a wait
from selenium.webdriver.support import expected_conditions as EC  # alias to use as expected_conditions is too long
from selenium.webdriver.chrome.options import Options


def webdriver_instance():
    options = Options()
    service = ChromeService(ChromeDriverManager().install())

    options.add_argument('start-maximized')
    options.add_argument('disable-extensions')
    my_driver = webdriver.Chrome(service=service, options=options)
    return my_driver


class Actions:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, tupel_selector):
        my_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(tupel_selector))
        return my_element

    def click_element(self, element):
        element.click()

    def send_keys(self, element, value):
        element.send_keys(value)

    def get_attribute(self, element, attribute):
        requested_attribute = element.get_attribute(attribute)
        return requested_attribute

    def find_text(self, tupel_selector):
        text_post_login_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(tupel_selector))
        element_text = text_post_login_element.get_attribute('innerText')
        return element_text

    def find_elements(self, tuple_selector):
        my_elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(tuple_selector))
        return my_elements
