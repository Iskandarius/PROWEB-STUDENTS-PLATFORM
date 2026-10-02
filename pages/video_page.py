from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import wait_for_write
import time

class VideoPage:
    def __init__(self, driver):
        self.driver = driver

        # Локаторы
        self.btn_play = (
            By.CSS_SELECTOR,
            "#app > div > div.videolesson > div > div:nth-child(2) > div > "
            "div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > "
            "div.video-player-proweb__controlls > div.video-player-proweb__controllers > "
            "div.video-player-proweb__controllers-left > button > span",
        )
        self.btn_fullscreen = (
            By.CSS_SELECTOR,
            "#app > div > div.videolesson > div > div:nth-child(2) > div > "
            "div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > "
            "div.video-player-proweb__controlls > div.video-player-proweb__controllers > "
            "div.video-player-proweb__controllers-right > button:nth-child(3) > span",
        )

        self.btn_pause = (
            By.CSS_SELECTOR,
            "#app > div > div.videolesson > div > div:nth-child(2) > div > "
            "div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > "
            "div.video-player-proweb__controlls > div.video-player-proweb__controllers > "
            "div.video-player-proweb__controllers-left > button > span",
        )
        self.btn_collapse = (
            By.CSS_SELECTOR,
            "#app > div > div.videolesson > div > div:nth-child(2) > div > "
            "div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > "
            "div.video-player-proweb__controlls > div.video-player-proweb__controllers > "
            "div.video-player-proweb__controllers-right > button:nth-child(3) > span",
        )

        self.btn_leave = (
            By.CSS_SELECTOR,
            "#app > div > div.videolesson > div > div:nth-child(2) > div > "
            "div:nth-child(1) > button",
        )
        self.logo_home = (
            By.CSS_SELECTOR,
            "#app > div > div.header > nav > div.header__logo > div > a",
        )

        self.fullscreen_fire = (By.CSS_SELECTOR, ".baseavatar_fullscreen")
        self.screen_collapse_fire = (
            By.CSS_SELECTOR,
            ".baseavatar_fullscreen-exit",
        )

    def click_btn_play(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_play)).click()

    def click_btn_fullscreen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen)).click()

    def click_btn_pause(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_pause)).click()

    def click_btn_collapse(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_collapse)).click()

    def is_video_paused(self):
        try:
            return self.driver.execute_script(
                "let v = document.querySelector('video'); return v ? v.paused : null;"
            )
        except Exception:
            return None

    def resume_if_paused(self):
        if self.is_video_paused():
            self.click_btn_play()

    def click_fullscreen_fire(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.fullscreen_fire)).click()

    def click_screen_collapse_fire(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.screen_collapse_fire)
        ).click()

    def click_btn_leave(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.btn_leave))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
            element,
        )
        time.sleep(1.5)
        wait.until(EC.element_to_be_clickable(self.btn_leave)).click()

    def click_logo_home(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.logo_home)).click()