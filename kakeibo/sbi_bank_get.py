import time
from config import pw
from util import ex_driver


def sbi_bank_get(username, password):
    driver = ex_driver.set_driver()
    wait = ex_driver.set_wait(driver)
    driver.get("https://www.netbk.co.jp/contents/pages/wpl010101/i010101CT/DI01010210")

    ex_driver.send_key_name(driver, username, "userName")
    ex_driver.send_key_css(driver, password, "#loginPwdSet")
    ex_driver.click_css(driver, "button")  # ログインボタン
    ex_driver.wait_click_css(wait, "span.m-icon-ps_details")
    ex_driver.wait_click_css(wait, "div.m-formWrap-data > ul > li:nth-child(5)")
    ex_driver.wait_click_css(wait, "div.m-sortMeisai div.m-formWrapPlural.search-btn a")
    ex_driver.wait_click_css(wait, "div.details-sort.ng-tns-c3-3.ng-star-inserted li.ng-tns-c3-3.ng-star-inserted.notActive")
    ex_driver.wait_click_css(wait, "dl.details-download a.details-iconExcel")

    time.sleep(3)
    return driver


if __name__ == '__main__':
    driver = sbi_bank_get(pw.sbi_bank_b_name, pw.sbi_bank_b_pass)
    driver.close()
