from datetime import datetime
import serial
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# coba-110@buoyant-equator-244810.iam.gserviceaccount.com

scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

list_sheet = [
  client.open_by_key("1VNhxS0nKTh530JSieb6J0tfNXjAqrswl9moTqTsIoGE").worksheet("Sheet1"),
  client.open_by_key("17H-KuJlRJRXEFUg1-oxpd0SKxZTHl2Rg1j0G6E_eBR8").worksheet("Sheet1"),
  client.open_by_key("18gPNc2PmoRsGtaRu5gTE2nN5VN5lDZNM9eSY6iPdfnA").worksheet("Sheet1"),
  client.open_by_key("16o91jUEa5h5FRA1Ta2MGzqgKUestfFp27We51ZxzubU").worksheet("Sheet1")
]

ser = serial.Serial(
  port='/dev/ttyAMA3',
  baudrate=9600,
  bytesize=serial.EIGHTBITS,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  timeout=5
)

def read_sensor():
  ser.write(b'\x01\x03\x00\x00\x00\x01\x84\x0A')
  response = ser.read(14)
  value = int.from_bytes(response[3:5])
  if value > 0x8000:
    value -= 0x10000  # Convert to signed 16-bit integer

  return value / 10

while True:
    print("Waiting for the next minute to read temperature...")
    now = datetime.now()
    wait_until = (10 - now.second) % 10
    time.sleep(wait_until)
    try:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Reading temperature...")
        current_time = datetime.now()
        temperature = read_sensor()
        print(f"Temperature: {temperature} °C")
        for sheet in list_sheet:
          sheet.append_row([current_time.strftime('%Y-%m-%d %H:%M:%S'), temperature])
        time.sleep(1)  # Sleep until the next minute
    except Exception as e:
        print(f"Error reading temperature: {e}")

