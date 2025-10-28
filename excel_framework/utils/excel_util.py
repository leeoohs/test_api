import os

import openpyxl

from excel_framework.config.setting import DATA_PATH


def get_row_values(file_name, sheet_name, row_num):
    file_path = os.path.join(DATA_PATH, file_name)
    # file_path = DATA_PATH / file_name
    print("实际读取的文件路径：", file_path)
    # 加载excel数据文件
    workbook = openpyxl.load_workbook(file_path)
    # 具体某一sheet
    sheet = workbook[sheet_name]
    data = []
    # 行数
    cloumns = sheet.max_column
    for i in range(1, cloumns + 1):
        cell = sheet.cell(row=row_num, column=i)
        data.append(cell.value)
    return data


def get_test_data(file_name, sheet_name):
    file_path = os.path.join(DATA_PATH, file_name)
    # file_path = DATA_PATH / file_name
    # 加载excel数据文件
    workbook = openpyxl.load_workbook(file_path)
    # 具体某一sheet
    sheet = workbook[sheet_name]
    data = []
    # 行数
    rows = sheet.max_row

    for j in range(1, rows + 1):
        data.append(get_row_values(file_name, sheet_name, j))
    return data


if __name__ == '__main__':
    print(get_row_values('d.xlsx', 'add', 1))
    try:
        # 正确写法：调用函数并打印返回值
        row_data = get_row_values('d.xlsx', 'add', 1)
        print("第1行数据：", row_data)  # 打印函数返回的行数据
    except Exception as e:
        print("执行错误：", e)  # 打印异常信息（而非路径）