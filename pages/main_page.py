from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import wait_for_write
import time


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.watch_again = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div.container.container_mobile > div > div.home-eduV2__watched > div.home-eduV2__watched-segments > div > button:nth-child(2)")
        self.lsn_7 = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div.container.container_mobile > div > div.home-eduV2__watched > div.w100.hidden.relative > div > div:nth-child(4)")

        self.homeworks = (By.CSS_SELECTOR, "#tabbar > div > div > div.tab-header__wrapper > div:nth-child(2)")

        self.profile_icon = (By.CSS_SELECTOR, ".header__avatar")
        self.logout_btn = (By.CSS_SELECTOR, "#app > div > div.user-container.user-container_change > div > div > div.relative.w100p > div.flex.column.gap15.w100p.relative > div:nth-child(6) > div")
        self.exit_confirm = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")


    def click_watch_again(self):
        wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.presence_of_element_located(self.logout_btn))
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        # time.sleep(1.5)
        wait.until(EC.element_to_be_clickable(self.watch_again)).click()

    def click_lsn_7(self):
        wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.presence_of_element_located(self.logout_btn))
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        # time.sleep(1.5)
        wait.until(EC.element_to_be_clickable(self.lsn_7)).click()

    def click_homeworks(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.homeworks)).click()

    def click_profile_icon(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.profile_icon)).click()

    def click_logout_btn(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.logout_btn))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        time.sleep(1.5)
        wait.until(EC.element_to_be_clickable(self.logout_btn)).click()

    def click_exit_confirm(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.exit_confirm)).click()
