import time
from config import pw
from util import ex_driver


def orico_get(username: str, password: str, driver=None):
    '''
    username,passwordを引数にして、CSVをダウンロードする
    '''
    if not driver:
        driver = ex_driver.set_driver()

    driver.get("https://my.orico.co.jp/eorico/login.do")

    ex_driver.send_key_name(driver, username, "LoginId")
    ex_driver.send_key_name(driver, password, "Pwd")
    ex_driver.click_css(driver, "#base tr > td > a > img")  # login_button
    print("画像認証のひらがな3文字を入力し、手動で進めてください。")
    input("ログインに成功したらenterを押してください。")
    driver.get("https://my.orico.co.jp/eorico/KAL1B10003.do?SelIndex=0")
    driver.get("https://my.orico.co.jp/eorico/KAL1B10013.do?SelIndex=0")

    time.sleep(3)
    return driver


if __name__ == '__main__':
    driver = orico_get(pw.orico_username, pw.orico_password)
    driver.close()
