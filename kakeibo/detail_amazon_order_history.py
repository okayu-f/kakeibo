import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import pandas as pd
from bs4 import BeautifulSoup
from config import pw
from util import ex_driver


log_in_email = pw.amazon_email
log_in_pass = pw.amazon_pass
order_nums_columns = []
sub_nums = []
order_dates = []
shipment_dates = []
descs = []
quantities = []
unit_prices = []
prices = []


def login_view_history(driver=None):
    if not driver:
        driver = ex_driver.set_driver()
    wait = ex_driver.set_wait(driver)

    driver.get("https://www.amazon.co.jp/")
    ex_driver.wait_click_css(wait, "#nav-orders")  # 注文履歴ボタン
    ex_driver.wait_send_key_css(wait, log_in_email, "#ap_email")
    ex_driver.wait_click_css(wait, "#continue")
    ex_driver.wait_send_key_css(wait, log_in_pass, "#ap_password")
    ex_driver.wait_click_css(wait, "#auth-signin-button")
    input("2段階認証待ち。完了したらenterを")
    # ex_driver.wait_click_css(wait, "#a-autoid-1-announce")  # 注文期間
    # ex_driver.wait_click_css(wait, "#time-filter_2")  # 当年を選択

    time.sleep(3)
    return driver


def get_order_nums(driver, already_got_num=None, skip_order_nums=[]):
    order_nums = []
    wait = WebDriverWait(driver, 5)
    while True:
        order_num_elems = driver.find_elements(By.CSS_SELECTOR, 'div.yohtmlc-order-id > span:nth-child(2)')
        for elem in order_num_elems:
            order_num = elem.text
            if order_num == already_got_num:
                return order_nums
            if order_num in skip_order_nums:
                continue
            order_nums.append(elem.text)
        try:
            next_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "li.a-last > a")))
            next_btn.click()
            time.sleep(1)
        except TimeoutException:
            break
    return order_nums


def history_to_df():
    data = dict(order_nums=order_nums_columns, sub_nums=sub_nums, order_dates=order_dates, shipment_dates=shipment_dates, descs=descs, quantities=quantities, unit_prices=unit_prices, prices=prices)
    df = pd.DataFrame(data=data)
    df['order_dates'] = pd.to_datetime(df['order_dates'], format='%Y年%m月%d日')
    df.sort_values('order_dates', inplace=True, kind='mergesort')
    return df


def get_invoice_html(order_num, driver):
    if order_num[0] == 'D':
        URL = 'https://www.amazon.co.jp/gp/digital/your-account/order-summary.html/ref=oh_aui_ajax_dpi?ie=UTF8&orderID=' + order_num + '&print=1'
    else:
        URL = 'https://www.amazon.co.jp/gp/css/summary/print.html/ref=oh_aui_ajax_invoice?ie=UTF8&orderID=' + order_num
    driver.get(URL)
    invoice_html = driver.page_source.encode('utf-8')
    return invoice_html


def order_detail_get(html, num):
    soup = BeautifulSoup(html, 'html.parser')
    order_date = ''
    order_date_row = soup.select_one("body > table:nth-child(7) > tbody > tr > td > table:nth-child(1) > tbody > tr:nth-child(2) > td")
    if order_date_row:
        order_date = order_date_row.get_text(strip=True).replace('注文日：', '').replace('「定期おトク便」のご注文が確定しました', '')

    order_tables = soup.select("body > table:nth-child(7) > tbody > tr > td > table > tbody > tr > td > table")
    sub_num = 0
    for order_table in order_tables[:-1]:
        sub_num += 1
        shipment_date = ''
        shipment_date_elem = order_table.select_one("center")
        if shipment_date_elem:
            shipment_date = shipment_date_elem.get_text(strip=True).replace('に発送済み', '')

        desc_tags = order_table.select("i")
        for desc_tag in desc_tags:
            desc = desc_tag.get_text(strip=True)
            descs.append(desc)
            order_nums_columns.append(num)
            sub_nums.append(sub_num)
            order_dates.append(order_date)
            shipment_dates.append(shipment_date)

        order_products = order_table.select("table:nth-child(2) tr td:nth-child(2)")[1:]
        for order_product in order_products:
            order_text = order_product.get_text(strip=True)
            word_count_unit = order_text.index('点')
            if 'g' in order_text[0:word_count_unit]:
                quantity = 1 # グラム売りは1点として記録する
            else:
                quantity = int(order_text[0:word_count_unit])
            quantities.append(quantity)

        price_tags = order_table.select("tr:nth-child(2) td:nth-child(3)")
        for price_tag in price_tags:
            unit_price = price_tag.get_text(strip=True).replace('￥', '').replace(' ', '').replace(',', '')
            if 'g' in unit_price:
                unit_price = unit_price.split("\n")[-1] # グラム売りは総額を単価として記録する
            unit_price = int(unit_price)
            unit_prices.append(unit_price)

    payment_informations = order_tables[-1].select("tbody tbody tbody tbody tbody tbody tr")
    for payment_information in payment_informations:
        tds = payment_information.select("td")
        if (tds[0].get_text(strip=True) == '商品の小計：'
                or tds[0].get_text(strip=True) == '注文合計：'
                or tds[0].get_text(strip=True) == 'ご請求額：'
                or tds[1].get_text(strip=True) == '-----'):
            continue
        order_nums_columns.append(num)
        sub_nums.append('-')
        order_dates.append(order_date)
        shipment_dates.append('-')
        descs.append(tds[0].get_text(strip=True).replace('：', ''))
        quantities.append(1)
        unit_prices.append(int(tds[1].get_text(strip=True).replace('￥', '').replace(' ', '').replace(',', '')))


def digital_order_detail_get(html, num):
    soup = BeautifulSoup(html, 'html.parser')
    order_date = ''
    order_date_row = soup.select_one("body div.orderSummary > table:nth-child(1) tr:nth-child(2) > td")
    if order_date_row:
        order_date = order_date_row.get_text(strip=True).replace('注文日：', '')

    sub_num = 1
    shipment_date = "-"
    quantity = 1

    desc_tags = soup.select("div.orderSummary a")
    for desc_tag in desc_tags:
        desc = desc_tag.get_text(strip=True)
        descs.append(desc)
        order_nums_columns.append(num)
        sub_nums.append(sub_num)
        order_dates.append(order_date)
        shipment_dates.append(shipment_date)
        quantities.append(quantity)

    price_tags = soup.select("body > div.orderSummary td:nth-child(2)")[2:]
    for price_tag in price_tags:
        unit_price = int(price_tag.get_text(strip=True).replace('￥', '').replace(' ', '').replace(',', ''))
        unit_prices.append(unit_price)

    payment_informations = soup.select("div.a-column.a-span5.pmts-amount-breakdown.a-span-last > div")
    for payment_information in payment_informations[1:-2]:
        order_nums_columns.append(num)
        sub_nums.append('-')
        order_dates.append(order_date)
        shipment_dates.append('-')
        desc = payment_information.select_one("div.a-column.a-span8")
        if desc:
            descs.append(desc.get_text(strip=True).replace('：', ''))
        quantities.append(1)
        unit_price = payment_information.select_one("div.a-column.a-span4.a-text-right.a-span-last")
        if unit_price:
            unit_prices.append(int(unit_price.get_text(strip=True).replace('￥', '').replace(' ', '').replace(',', '')))


def fetch(latest_order_num=None, driver=None, skip_order_nums=[]):
    invoice_htmls = []

    driver = login_view_history(driver)
    order_nums = get_order_nums(driver, latest_order_num, skip_order_nums)
    for order_num in order_nums:
        time.sleep(1)
        invoice_html = get_invoice_html(order_num, driver)
        invoice_htmls.append(invoice_html)
    time.sleep(3)
    driver.close()

    for sourse, num in zip(invoice_htmls, order_nums):
        print(num)
        if num[0] == 'D':
            digital_order_detail_get(sourse, num)
        else:
            order_detail_get(sourse, num)
    for x, y in zip(quantities, unit_prices):
        price = x * y
        prices.append(price)


if __name__ == '__main__':
    latest_order_num = '249-3377026-0559031'
    fetch(latest_order_num)
    df = history_to_df()
    df.to_csv('.data//history_csv_out.csv', encoding='utf-8')
    print('done')
