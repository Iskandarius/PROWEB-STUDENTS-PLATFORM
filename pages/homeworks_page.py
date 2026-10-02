from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import wait_for_write
import time

class HomeworkPage:
    def __init__(self,driver):
        self.driver = driver
        self.btn_group = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div.home-homeworkV2__header.subscription-top-padding > div > div:nth-child(6)")
        self.last_homework = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div.lazyscroll.h100 > div > div.home-homeworkV2__content-months > div:nth-child(1) > div.home-homeworkV2__content-months-month-works.md3-list > a")
        self.btn_question = (By.CSS_SELECTOR, r"#\33  > div.homework-task__left.flex.column > div.homework-task__left-top.p20 > div.pt20.flex.gap10.wrap > button.material-filled-button.homework-task__left-top-questionbutton")
        self.input_text = (By.CSS_SELECTOR, r"#\33  > div.homework-comments__bottom > div.homework-comments__bottom-input > div > div.list-tile__leading-box.grow > div > label > textarea")
        self.btn_send = (By.CSS_SELECTOR, r"#\33  > div.homework-comments__bottom > div.homework-comments__bottom-input > button")

    def click_btn_group(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_group)).click()

    def click_last_homework(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.last_homework)).click()

    def click_btn_question(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_question)).click()

    def enter_input_text(self, input_text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.input_text)).send_keys(input_text)

    def click_btn_send(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_send)).click()


