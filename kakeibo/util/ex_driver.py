from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def set_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--lang=ja-JP')
    options.add_argument('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    prefs = {'profile.password_manager_enabled': False,
             'credentials_enable_service': False}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver", options=options)
    return driver


def set_wait(driver):
    return WebDriverWait(driver, 10)


def click_css(driver, css_selector):
    link = driver.find_element_by_css_selector(css_selector)
    link.click()


def send_key_css(driver, key, css_selector):
    form = driver.find_element_by_css_selector(css_selector)
    form.send_keys(key)


def send_key_name(driver, key, name):
    form = driver.find_element_by_name(name)
    form.send_keys(key)


def wait_click_css(wait, css_selector):
    link = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    link.click()


def wait_click_name(wait, name):
    link = wait.until(expected_conditions.element_to_be_clickable((By.NAME, name)))
    link.click()


def wait_send_key_css(wait, key, css_selector):
    form = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
    form.send_keys(key)


def wait_send_key_name(wait, key, name):
    form = wait.until(expected_conditions.visibility_of_element_located((By.NAME, name)))
    form.send_keys(key)


def hover_css(driver, css_selector):
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element_by_css_selector(css_selector)).perform()
