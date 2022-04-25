import time
from config import pw
from util import ex_driver


def orico_get(username: str, password: str):
    '''
    username,passwordを引数にして、CSVをダウンロードする
    '''

    driver = ex_driver.set_driver()
    driver.get("https://my.orico.co.jp/eorico/login.do")

    ex_driver.click_css(driver, "#datasign_cmp__cmp_close_button")  # cookie agreement close button
    ex_driver.send_key_name(driver, username, "LoginId")
    ex_driver.send_key_name(driver, password, "Pwd")
    ex_driver.click_css(driver, "#base tr > td > a > img")  # login_button
    token = input("画像認証のひらがな3文字を入力してください:")
    ex_driver.send_key_name(driver, token, "token")
    ex_driver.click_css(driver, "#base input[type=image]")  # login_button
    driver.get("https://my.orico.co.jp/eorico/KAL1B10003.do?SelIndex=0")
    driver.get("https://my.orico.co.jp/eorico/KAL1B10013.do?SelIndex=0")

    return driver


if __name__ == '__main__':
    driver = orico_get(pw.orico_username, pw.orico_password)
    time.sleep(3)
    driver.close()
