from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pw

import time


def aeon_c_get(username, password, expiration_month, expiration_year, security_code):
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")

    driver.get("https://www.aeon.co.jp/app/")

    wait = WebDriverWait(driver, 10)

    user_name = wait.until(expected_conditions.visibility_of_element_located((By.NAME, "username")))
    user_name.send_keys(username)

    user_pass = driver.find_element_by_name("password")
    user_pass.send_keys(password)

    login_btn = driver.find_element_by_css_selector("div.m-buttoncontainer")
    login_btn.click()

    driver.get("https://www.aeon.co.jp/app/details/download/")

    # time.sleep(1)
    # em = driver.find_element_by_name("expiration_month")
    em = wait.until(expected_conditions.visibility_of_element_located((By.NAME, "expiration_month")))
    em.send_keys(expiration_month)

    ey = driver.find_element_by_name("expiration_year")
    ey.send_keys(expiration_year)

    sc = driver.find_element_by_name("securityCode")
    sc.send_keys(security_code)
    # sc = wait.until(expected_conditions.visibility_of_element_located((By.NAME, "securityCode")))

    auth_btn = driver.find_element_by_css_selector("div.m-buttoncontainer_primary button")
    auth_btn.click()

    csv_select = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div:nth-child(4) > div > label > div")))
    csv_select.click()

    download_btn = driver.find_element_by_css_selector("div.m-buttoncontainer_primary button")
    download_btn.click()

    time.sleep(3)
    driver.close()


if __name__ == '__main__':
    aeon_c_get(pw.aeon_c_username, pw.aeon_c_password, pw.aeon_c_expiration_month, pw.aeon_c_expiration_year, pw.aeon_c_security_code)
