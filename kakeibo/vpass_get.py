import time
from config import pw
from util import ex_driver


def vpass_get(username, password, driver=None):
    if not driver:
        driver = ex_driver.set_driver()

    # wait = ex_driver.set_wait(driver)
    driver.get("https://www.smbc-card.com/mem/index.jsp")

    ex_driver.send_key_css(driver, username, "#id_input")
    ex_driver.send_key_css(driver, password, "#pw_input")
    print("パズル認証タイム")
    input("ログインに成功したらenterを押してください。")
    # ex_driver.click_css(driver, "input[value='ログイン']")  # ログインボタン

    driver.get("https://www.smbc-card.com/memx/web_meisai/top/index.html")
    time.sleep(3)
    ex_driver.click_css(driver, "#vp-view-VC0502-003_RS0001_U051111_3")  # CSVでダウンロードする ボタン

    time.sleep(3)

    return driver


if __name__ == '__main__':
    driver = vpass_get(pw.vpass_name, pw.vpass_pass)
    driver.close()
