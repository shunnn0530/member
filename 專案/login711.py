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


#程式開始 

#登入

driver = webdriver.Chrome() # 登入網頁
driver.get("https://group.openpoint.com.tw/auth/service/login")

select_element = driver.find_element_by_name("mobileCountry") # 選擇地區
select = Select(select_element)
select.select_by_value("886")

# 登入帳號

worksheet_name = "工作表1"  # 選擇工作表
worksheet = spreadsheet.worksheet(worksheet_name)

start_account = 'A2' # 指定範圍
end_account = 'account7_11'

account_range = worksheet.range(start_account + ':' + end_account) # 取得指定範圍的資料

# 將資料存放到 account7_11 變數中
# 假設每一列的資料格式為 [列1的值, 列2的值, 列3的值, ...]
account_headers = account_range[0::worksheet.col_count]  # 第一列是標題
account_data_rows = account_range[1:]  # 其他列是資料


account_data_dict_list = [dict(zip(account_headers, row)) for row in [account.value for account in account_data_rows]]   # 將資料轉換成字典

account7_11 = account_data_dict_list # 將資料儲存到 account7_11 變數中

#開始輸入帳號
input_mobile = driver.find_element_by_id("mobile")
input_mobile.send_keys(account7_11)

# 登入密碼

worksheet_name = "工作表1"  # 選擇工作表
worksheet = spreadsheet.worksheet(worksheet_name)

start_password = 'B2' # 指定範圍
end_password = 'password7_11'
password_range = worksheet.range(start_password + ':' + end_password) # 取得指定範圍的資料

# 將資料存放到 password7_11 變數中
# 假設每一列的資料格式為 [列1的值, 列2的值, 列3的值, ...]
password_headers = password_range[0::worksheet.col_count]  # 第一列是標題
password_data_rows = password_range[1:]  # 其他列是資料


password_data_dict_list = [dict(zip(password_headers, row)) for row in [password.value for password in password_data_rows]]   # 將資料轉換成字典

password7_11 = password_data_dict_list # 將資料儲存到 password7_11 變數中

#開始輸入密碼
input_password = driver.find_element_by_id("passwd_d")
input_password.send_keys(password7_11)

