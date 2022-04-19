from openpyxl.reader.excel import load_workbook
from ufj_get import ufj_get
from aeon_c_get import aeon_c_get
from latest_copy import latest_copy_depck, latest_copy, latest_csv_move_to
import os
import datetime
from sbi_bank_get import sbi_bank_get
from orico_get import orico_get
import pw
# from aeon_c_get import aeon_c_get

now = datetime.datetime.now()
today = now.strftime('%Y%m%d')
os.makedirs(today, exist_ok=True)

print('start driver...')
orico_get(pw.orico_username, pw.orico_password)
csv_path = latest_csv_move_to(today)

sheet_name = 'orico'
csv_file = csv_path
csv_date_column_name = 'ご利用日'
csv_date_fmt = '%Y年%m月%d日'
date_column = 0
key_column1 = 1
key_column2 = 8
csv_skiprows = 9

print('opening excel...')
wb = load_workbook('★家計簿190429.xlsx')

latest_copy(wb, sheet_name, csv_file, csv_date_column_name, csv_date_fmt, date_column, key_column1, key_column2, csv_skiprows)

sbi_bank_get(pw.sbi_bank_a_name, pw.sbi_bank_a_pass)
sbi_bank_get(pw.sbi_bank_b_user, pw.sbi_bank_b_pass)

csv_path = latest_csv_move_to(today)

sheet_name = '裕SBI'
csv_file = csv_path
csv_date_column_name = '日付'
csv_date_fmt = '%Y/%m/%d'
date_column = 0
key_column1 = 1
key_column2 = 4
csv_skiprows = 0

latest_copy_depck(wb, sheet_name, csv_file, csv_date_column_name, csv_date_fmt, date_column, key_column1, key_column2, csv_skiprows)

csv_path = latest_csv_move_to(today)

sheet_name = 'ひさSBI'
csv_file = csv_path
csv_date_column_name = '日付'
csv_date_fmt = '%Y/%m/%d'
date_column = 0
key_column1 = 1
key_column2 = 4
csv_skiprows = 0

latest_copy_depck(wb, sheet_name, csv_file, csv_date_column_name, csv_date_fmt, date_column, key_column1, key_column2, csv_skiprows)

aeon_c_get(pw.aeon_c_username, pw.aeon_c_password, pw.aeon_c_expiration_month, pw.aeon_c_expiration_year, pw.aeon_c_security_code)
csv_path = latest_csv_move_to(today)


sheet_name = 'AEON'
csv_file = csv_path
csv_date_column_name = 'ご利用日'
csv_date_fmt = '%y%m%d'
date_column = 0
key_column1 = 2
key_column2 = 6
csv_skiprows = 7
csv_footerrows = 3

latest_copy(wb, sheet_name, csv_file, csv_date_column_name, csv_date_fmt, date_column, key_column1, key_column2, csv_skiprows, csv_footerrows)


ufj_get(pw.ufj_username, pw.ufj_password)
csv_path = latest_csv_move_to(today)

sheet_name = 'UFJ'
csv_file = csv_path
csv_date_column_name = '日付'
csv_date_fmt = '%Y/%m/%d'
date_column = 0
key_column1 = 2
key_column2 = 5
csv_skiprows = 0

latest_copy_depck(wb, sheet_name, csv_file, csv_date_column_name, csv_date_fmt, date_column, key_column1, key_column2, csv_skiprows)


wb.save('new_kakeibo_test.xlsx')

print('done!')
