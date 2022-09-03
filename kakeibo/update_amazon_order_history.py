import detail_amazon_order_history
import latest_copy
from openpyxl import load_workbook


def execute(wb, sheet_name, order_num_column=0, date_column=2, date_fmt='%Y-%m-%d'):
    ws = wb[sheet_name]
    latest_row = latest_copy.get_latest_row(ws)
    print(f'latest_row={latest_row}')
    latest_order_num = ws.cell(latest_row, order_num_column + 1).value
    print(f'latest_order_num={latest_order_num}')
    detail_amazon_order_history.fetch(latest_order_num)
    df = detail_amazon_order_history.history_to_df()
    latest_copy.update_data(ws, date_column, latest_row, df, date_fmt, index=True)


if __name__ == '__main__':
    wb = load_workbook("./data/ama_his_test.xlsx")
    execute(wb, 'Ama履歴')
    wb.save("./ama_his_test_update.xlsx")

    print('done')
