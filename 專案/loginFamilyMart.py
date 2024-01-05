from selenium import webdriver
import requests
from selenium.webdriver.support.ui import Select
import gspread

from google.auth.transport.requests import Request #google
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

credentials = Credentials.from_service_account_file('path/to/your/credentials.json', scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']) # 設定 API 金鑰文件的路徑

credentials = Credentials.from_service_account_file('path/to/your/credentials.json', scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']) # 設定 API 金鑰文件的路徑

from oauth2client.service_account import ServiceAccountCredentials


credentials = ServiceAccountCredentials.from_json_keyfile_name('your-credentials.json', ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])# 載入憑證

gc = gspread.authorize(credentials) # 設定 gspread

spreadsheet = gc.open('APP會員帳密儲存庫') # 打開試算表

# 全家

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 程式開始

# 登入

driver = webdriver.Chrome() # 登入網頁
driver.get("https://group.openpoint.com.tw/auth/service/login")

# 登入帳號

worksheet_name = "工作表2"  # 選擇工作表
worksheet = spreadsheet.worksheet(worksheet_name)

start_account = 'A2' # 指定範圍
end_account = 'account_family'

account_range = worksheet.range(start_account + ':' + end_account) # 取得指定範圍的資料

# 將資料存放到 account_family 變數中
# 假設每一列的資料格式為 [列1的值, 列2的值, 列3的值, ...]
account_headers = account_range[0::worksheet.col_count]  # 第一列是標題
account_data_rows = account_range[1:]  # 其他列是資料

account_data_dict_list = [dict(zip(account_headers, row)) for row in [account.value for account in account_data_rows]]   # 將資料轉換成字典

account_family = account_data_dict_list # 將資料儲存到 account_family 變數中

phone_input = driver.find_element(By.ID, "account")
phone_input.send_keys(account_family)

# 登入密碼

worksheet_name = "工作表2"  # 選擇工作表
worksheet = spreadsheet.worksheet(worksheet_name)

start_password = 'B2' # 指定範圍
end_password = 'password_family'
password_range = worksheet.range(start_password + ':' + end_password) # 取得指定範圍的資料

# 將資料存放到 password_family變數中
# 假設每一列的資料格式為 [列1的值, 列2的值, 列3的值, ...]
password_headers = password_range[0::worksheet.col_count]  # 第一列是標題
password_data_rows = password_range[1:]  # 其他列是資料

password_data_dict_list = [dict(zip(password_headers, row)) for row in [password.value for password in password_data_rows]]   # 將資料轉換成字典

password_family = password_data_dict_list # 將資料儲存到 password_family 變數中

#開始輸入密碼

# 偵測是否需要輸入密碼和驗證碼
if "password" in driver.page_source and "captcha" in driver.page_source:

    # 如果需要，填寫密碼和驗證碼
    password_input = driver.find_element(By.ID, "password")
    captcha_input = driver.find_element(By.ID, "captcha")

    # 替換 "YourPassword" 為實際的密碼
    password_input.send_keys(password_family)
    captcha_input.send_keys("YourCaptcha")          #這裡有驗證碼 需參考台大醫那個人的小論文

    # 提交表單
    login_button = driver.find_element(By.ID, "btn_login")
    login_button.click()

else:
    print("電話號碼未註冊")

