from openpyxl.reader.excel import load_workbook
# from ufj_get import ufj_get
from aeon_c_get import aeon_c_get
from latest_copy import latest_copy_depck, latest_copy, latest_csv_move_to
import os
import datetime
import json
from sbi_bank_get import sbi_bank_get
from orico_get import orico_get
from try_get import try_get
from config import pw

now = datetime.datetime.now()
today = now.strftime('%Y%m%d')
data_path = './data/' + today
os.makedirs(data_path, exist_ok=True)

with open('config/config.json') as f:
    config = json.load(f)

print('start driver...')
try_get(orico_get, pw.orico_username, pw.orico_password)
csv_path = latest_csv_move_to(data_path)

print('opening excel...')
wb = load_workbook(config["target_file"])

latest_copy(wb, csv_path, **config["orico"])

print('sbi_bank_get1...')
try_get(sbi_bank_get, pw.sbi_bank_a_name, pw.sbi_bank_a_pass)

csv_path = latest_csv_move_to(data_path)

latest_copy_depck(wb, csv_path, **config["sbi1"])

print('sbi_bank_get2...')
try_get(sbi_bank_get, pw.sbi_bank_b_name, pw.sbi_bank_b_pass)

csv_path = latest_csv_move_to(data_path)

latest_copy_depck(wb, csv_path, **config["sbi2"])

try_get(aeon_c_get, pw.aeon_c_username, pw.aeon_c_password, pw.aeon_c_expiration_month, pw.aeon_c_expiration_year, pw.aeon_c_security_code)
csv_path = latest_csv_move_to(data_path)

latest_copy(wb, csv_path, **config["AEON"])

# print('ufj_get...')
# try_get(ufj_get, pw.ufj_username, pw.ufj_password)
# csv_path = latest_csv_move_to(data_path)

# latest_copy_depck(wb, csv_path, **config["ufj"])

print('save excel...')
wb.save(config["save_name"])

print('done!')
