from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def set_driver():
    return webdriver.Chrome("/usr/local/bin/chromedriver")


def set_wait(driver):
    return WebDriverWait(driver, 10)


def click_css(driver, css_selector):
    link = driver.find_element_by_css_selector(css_selector)
    link.click()


def send_key_name(driver, key, name):
    form = driver.find_element_by_name(name)
    form.send_keys(key)


def wait_click_css(wait, css_selector):
    link = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    link.click()


def wait_click_name(wait, name):
    link = wait.until(expected_conditions.element_to_be_clickable((By.NAME, name)))
    link.click()


def wait_send_key_name(wait, key, name):
    form = wait.until(expected_conditions.visibility_of_element_located((By.NAME, name)))
    form.send_keys(key)


def hover_css(driver, css_selector):
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element_by_css_selector(css_selector)).perform()
