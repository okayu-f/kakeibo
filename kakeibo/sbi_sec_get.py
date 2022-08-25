import time
from config import pw
from util import ex_driver


def sbi_sec_get(username, password, driver=None):
    if not driver:
        driver = ex_driver.set_driver()

    wait = ex_driver.set_wait(driver)
    driver.get("https://www.sbisec.co.jp/")

    ex_driver.send_key_name(driver, username, "user_id")
    ex_driver.send_key_name(driver, password, "user_password")
    ex_driver.wait_click_name(wait, "ACT_login")  # ログインボタン
    driver.get("https://site2.sbisec.co.jp/ETGate/?_ControlID=WPLETsmR001Control&_PageID=WPLETsmR001Sdtl12&_DataStoreID=DSWPLETsmR001Control&sw_page=WNS001&sw_param1=deposit&sw_param2=detail&cat1=home&cat2=none&getFlg=on")
    ex_driver.wait_click_css(wait, "#detailInquiryForm > p > a")

    time.sleep(3)

    return driver


def add_get_foreign_currency(driver):
    driver.get("https://site2.sbisec.co.jp/ETGate/?_ControlID=WPLETsmR001Control&_PageID=WPLETsmR001Sdtl12&_DataStoreID=DSWPLETsmR001Control&sw_page=BondFx&sw_param2=02_605&cat1=home&cat2=none&getFlg=on&OutSide=on")
    wait = ex_driver.set_wait(driver)
    ex_driver.wait_click_css(wait, "div.dpst-form-01-btn > p > a")
    time.sleep(3)

    return driver


if __name__ == '__main__':
    driver = sbi_sec_get(pw.sbi_sec_name, pw.sbi_sec_pass)
    add_get_foreign_currency(driver)
    driver.close()
