import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# 1. Autentikasi ke Google Sheets
scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# 2. Buka spreadsheet dan worksheet
spreadsheet = client.open_by_key("1VNhxS0nKTh530JSieb6J0tfNXjAqrswl9moTqTsIoGE")
sheet = spreadsheet.worksheet("Sheet1")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
sheet.append_row([now, "Data baru"])
