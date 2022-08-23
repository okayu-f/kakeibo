import time
from config import pw
from util import ex_driver


def ufj_get(username, password, driver=None):
    if not driver:
        driver = ex_driver.set_driver()

    wait = ex_driver.set_wait(driver)
    driver.get("https://entry11.bk.mufg.jp/ibg/dfw/APLIN/loginib/login?_TRANID=AA000_001")

    ex_driver.wait_send_key_css(wait, username, "#tx-contract-number")
    ex_driver.wait_send_key_name(wait, password, "PASSWORD")
    ex_driver.click_css(driver, "button.gonext")  # ログインボタン
    ex_driver.wait_click_css(wait, "div.detail")  # 明細ボタン
    ex_driver.click_css(driver, "#appoint")  # 期間ボタン
    ex_driver.wait_click_css(wait, "div.item.last_item button")  # 表示ボタン
    ex_driver.wait_click_css(wait, "div.data_footer td.first_child")  # ダウンロードリンク
    ex_driver.click_css(driver, "div.admb_l > button")  # ダウンロードボタン

    time.sleep(3)

    time.sleep(3)
    return driver


if __name__ == '__main__':
    driver = ufj_get(pw.ufj_username, pw.ufj_password)
    driver.close()
