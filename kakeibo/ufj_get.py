from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.common.action_chains import ActionChains
import pw
import time


def ufj_get(username, password):

    driver = webdriver.Chrome("/usr/local/bin/chromedriver")

    driver.get("https://entry11.bk.mufg.jp/ibg/dfw/APLIN/loginib/login?_TRANID=AA000_001")

    wait = WebDriverWait(driver, 10)

    # user_name = driver.find_element_by_css_selector("#tx-contract-number")
    user_name = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#tx-contract-number")))
    user_name.send_keys(username)

    user_pass = driver.find_element_by_name("PASSWORD")
    user_pass.send_keys(password)

    login_btn = driver.find_element_by_css_selector("button.gonext")
    login_btn.click()

    # detail_btn = driver.find_element_by_css_selector("div.detail")
    detail_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div.detail")))
    detail_btn.click()

    term_btn = driver.find_element_by_css_selector("#appoint")
    term_btn.click()

    # view_btn = driver.find_element_by_css_selector("div.item.last_item button")
    view_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div.item.last_item button")))
    view_btn.click()

    # download_link = driver.find_element_by_css_selector("div.data_footer td.first_child")
    download_link = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div.data_footer td.first_child")))
    download_link.click()

    csv_download = driver.find_element_by_css_selector("div.admb_l > button")
    csv_download.click()

    time.sleep(3)
    driver.close()


if __name__ == '__main__':
    ufj_get(pw.ufj_username, pw.ufj_password)
