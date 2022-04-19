from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import pw


def sbi_bank_get(username, password):

    driver = webdriver.Chrome("/usr/local/bin/chromedriver")

    driver.get("https://www.netbk.co.jp/contents/pages/wpl010101/i010101CT/DI01010210")

    wait = WebDriverWait(driver, 10)

    user_name = driver.find_element_by_name("userName")
    user_name.send_keys(username)

    user_pass = driver.find_element_by_id("loginPwdSet")
    user_pass.send_keys(password)

    btn = driver.find_element_by_css_selector("button")
    btn.click()

    bs_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "span.m-icon-ps_details")))
    bs_btn.click()

    select_term = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div.m-formWrap-data > ul > li:nth-child(5)")))
    select_term.click()
    # うまく動かないから美しくないが指定している。

    display_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div.m-sortMeisai div.m-formWrapPlural.search-btn a")))
    display_btn.click()

    older = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div.details-sort.ng-tns-c3-3.ng-star-inserted li.ng-tns-c3-3.ng-star-inserted.notActive")))
    older.click()

    download = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "dl.details-download a.details-iconExcel")))
    download.click()

    time.sleep(3)
    driver.close()


if __name__ == '__main__':
    sbi_bank_get(pw.sbi_bank_b_user, pw.sbi_bank_b_pass)
