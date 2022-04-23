from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def set_driver():
    return webdriver.Chrome("/usr/local/bin/chromedriver")


def set_wait(driver):
    return WebDriverWait(driver, 10)


def click_css(driver, css_selector):
    link = driver.find_element_by_css_selector(css_selector)
    link.click()


def wait_click_css(wait, css_selector):
    link = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    link.click()


def send_key_by_name(driver, key, name):
    user_pass = driver.find_element_by_name(name)
    user_pass.send_keys(key)
