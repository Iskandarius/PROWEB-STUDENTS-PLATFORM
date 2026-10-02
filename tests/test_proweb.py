import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException


from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.video_page import VideoPage
from pages.homeworks_page import HomeworkPage


def test_my_proweb_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in?q=/home")
    login_page = LoginPage(driver_chrome)
    login_page.change_lang_ru()
    time.sleep(3)
    login_page.enter_input_login("my@proweb.uz")
    time.sleep(3)
    login_page.click_btn_enter()
    time.sleep(3)
    login_page.enter_input_password("proweb3106632")
    time.sleep(3)
    login_page.click_btn_login()
    time.sleep(3)
    try:
        login_page.click_device_1()
        time.sleep(3)
        login_page.click_finish_1()
        time.sleep(3)
    except (TimeoutException, NoSuchElementException):
        pass


    main_page = MainPage(driver_chrome)
    main_page.click_watch_again()
    time.sleep(3)
    main_page.click_lsn_7()
    time.sleep(3)

    video_page = VideoPage(driver_chrome)
    video_page.click_btn_play()
    time.sleep(3)
    video_page.click_btn_fullscreen()
    time.sleep(15)
    video_page.resume_if_paused()
    time.sleep(3)
    video_page.click_btn_pause()
    time.sleep(3)
    video_page.click_btn_collapse()
    time.sleep(3)
    video_page.click_btn_leave()
    time.sleep(3)
    video_page.click_logo_home()
    time.sleep(3)

    main_page.click_homeworks()
    time.sleep(10)

    homeworks_page = HomeworkPage(driver_chrome)
    homeworks_page.click_btn_group()
    time.sleep(3)
    homeworks_page.click_last_homework()
    time.sleep(3)
    homeworks_page.click_btn_question()
    time.sleep(3)
    homeworks_page.enter_input_text("test")
    time.sleep(5)
    homeworks_page.click_btn_send()
    time.sleep(3)

    main_page.click_profile_icon()
    time.sleep(3)
    main_page.click_logout_btn()
    time.sleep(3)
    main_page.click_exit_confirm()
    time.sleep(3)


def test_invalid_my_proweb_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in?q=/home")
    login_page = LoginPage(driver_chrome)
    login_page.change_lang_ru()
    time.sleep(3)
    login_page.enter_input_login("my@proweb.uz")
    time.sleep(3)
    login_page.click_btn_enter()
    time.sleep(3)
    login_page.enter_input_password("qwerty123")
    time.sleep(3)
    login_page.click_btn_login()
    time.sleep(3)


def test_my_proweb_edge(driver_edge):
    driver_edge.get("https://my.proweb.uz/log-in?q=/home")
    login_page = LoginPage(driver_edge)
    login_page.change_lang_ru()
    time.sleep(3)
    login_page.enter_input_login("my@proweb.uz")
    time.sleep(3)
    login_page.click_btn_enter()
    time.sleep(3)
    login_page.enter_input_password("proweb3106632")
    time.sleep(3)
    login_page.click_btn_login()
    time.sleep(3)
    try:
        login_page.click_device_1()
        time.sleep(3)
        login_page.click_finish_1()
        time.sleep(3)
    except (TimeoutException, NoSuchElementException):
        pass


    main_page = MainPage(driver_edge)
    main_page.click_watch_again()
    time.sleep(3)
    main_page.click_lsn_7()
    time.sleep(3)

    video_page = VideoPage(driver_edge)
    video_page.click_btn_play()
    time.sleep(3)
    video_page.click_btn_fullscreen()
    time.sleep(15)
    video_page.resume_if_paused()
    time.sleep(3)
    video_page.click_btn_pause()
    time.sleep(3)
    video_page.click_btn_collapse()
    time.sleep(3)
    video_page.click_btn_leave()
    time.sleep(3)
    video_page.click_logo_home()
    time.sleep(3)

    main_page.click_homeworks()
    time.sleep(10)

    homeworks_page = HomeworkPage(driver_edge)
    homeworks_page.click_btn_group()
    time.sleep(3)
    homeworks_page.click_last_homework()
    time.sleep(3)
    homeworks_page.click_btn_question()
    time.sleep(3)
    homeworks_page.enter_input_text("test")
    time.sleep(5)
    homeworks_page.click_btn_send()
    time.sleep(3)

    main_page.click_profile_icon()
    time.sleep(3)
    main_page.click_logout_btn()
    time.sleep(3)
    main_page.click_exit_confirm()
    time.sleep(3)
    main_page.click_homeworks()
    time.sleep(10)
    main_page.click_profile_icon()
    time.sleep(3)
    main_page.click_logout_btn()
    time.sleep(3)
    main_page.click_exit_confirm()
    time.sleep(3)


def test_invalid_my_proweb_edge(driver_edge):
    driver_edge.get("https://my.proweb.uz/log-in?q=/home")
    login_page = LoginPage(driver_edge)
    login_page.change_lang_ru()
    time.sleep(3)
    login_page.enter_input_login("my@proweb.uz")
    time.sleep(3)
    login_page.click_btn_enter()
    time.sleep(3)
    login_page.enter_input_password("qwerty123")
    time.sleep(3)
    login_page.click_btn_login()
    time.sleep(3)