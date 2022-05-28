import time
from config import pw
from util import ex_driver


def rakuten_c_get(username, password):
    driver = ex_driver.set_driver()
    wait = ex_driver.set_wait(driver)
    driver.get("https://www.rakuten-card.co.jp/e-navi/")

    ex_driver.wait_send_key_name(wait, username, "u")
    ex_driver.send_key_name(driver, password, "p")
    ex_driver.wait_click_css(wait, "#loginButton")
    time.sleep(3)

    driver.get("https://www.rakuten-card.co.jp/e-navi/members/statement/index.xhtml?tabNo=0")  # 0...最新月
    driver.get("https://www.rakuten-card.co.jp/e-navi/members/statement/index.xhtml?downloadAsCsv=1")

    time.sleep(3)
    return driver


if __name__ == '__main__':
    driver = rakuten_c_get(pw.rakuten_c_mail, pw.rakuten_c_pass)
    driver.close()
