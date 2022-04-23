import time
from config import pw
from util import ex_driver


def aeon_c_get(username, password, expiration_month, expiration_year, security_code):
    driver = ex_driver.set_driver()
    wait = ex_driver.set_wait(driver)
    driver.get("https://www.aeon.co.jp/app/")

    ex_driver.wait_send_key_name(wait, username, "username")
    ex_driver.send_key_name(driver, password, "password")
    ex_driver.wait_click_css(wait, "div.m-buttoncontainer")  # ログインボタン

    driver.get("https://www.aeon.co.jp/app/details/download/")
    ex_driver.wait_send_key_name(wait, expiration_month, "expiration_month")
    ex_driver.wait_send_key_name(wait, expiration_year, "expiration_year")
    ex_driver.wait_send_key_name(wait, security_code, "securityCode")
    ex_driver.click_css(driver, "div.m-buttoncontainer_primary button")  # 認証ボタン
    ex_driver.wait_click_css(driver, "div:nth-child(4) > div > label > div")  # CSVのチェックボックス
    ex_driver.click_css(driver, "div.m-buttoncontainer_primary button")  # ダウンロードボタン

    return driver


if __name__ == '__main__':
    driver = aeon_c_get(pw.aeon_c_username, pw.aeon_c_password, pw.aeon_c_expiration_month, pw.aeon_c_expiration_year, pw.aeon_c_security_code)
    time.sleep(3)
    driver.close()
