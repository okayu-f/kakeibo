from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time
from config import pw


def orico_get(username, password):

    driver = webdriver.Chrome("/usr/local/bin/chromedriver")

    driver.get("https://my.orico.co.jp/eorico/login.do")

    wait = WebDriverWait(driver, 10)

    user_name = driver.find_element_by_name("LoginId")
    user_name.send_keys(username)

    user_pass = driver.find_element_by_name("Pwd")
    user_pass.send_keys(password)

    login_btn = driver.find_element_by_css_selector("#base tr > td > a > img")
    login_btn.click()

    token = input("画像認証のひらがな3文字を入力してください：")
    token_form = driver.find_element_by_name("token")
    token_form.send_keys(token)

    login_btn = driver.find_element_by_css_selector("#base input[type=image]")
    login_btn.click()

    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element_by_css_selector("#gnavi1 > a > img")).perform()
    # Invoice_link = driver.find_element_by_css_selector("#subnavi1 p:nth-child(1) a")
    Invoice_link = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#subnavi1 p:nth-child(1) a")))
    Invoice_link.click()

    card_link = driver.find_element_by_css_selector("table:nth-child(4) a")
    card_link.click()

    csv_download = driver.find_element_by_partial_link_text("CSV")
    csv_download.click()

    time.sleep(3)
    driver.close()


if __name__ == '__main__':
    orico_get(pw.orico_username, pw.orico_password)
