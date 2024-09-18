import time
print("Đang đợi API khởi động; Bạn hãy đợi khoảng 40s")
time.sleep(65)
import threading
from craw import fuc_craw
from fastapi import FastAPI,HTTPException,Query
from datetime import datetime
from callapi import *
import os


app = FastAPI()
@app.get("/craw")
async def craw():
    api_url = os.environ.get('API_URL')
    urlPost = api_url+"/countries/truncate"
    reset_table(urlPost)
    time.sleep(5)
    fuc_craw()
    return "Đã craw thành công"   


def crawDaily(hourDaily,minuteDaily):
    print(hourDaily)
    print(minuteDaily)
    nam_vua_cao = None
    ngay_vua_cao = None
    thang_vua_cao =  None
    # Lấy thời gian hiện tại
    while(True):
        current_time = datetime.now()
        hour = current_time.hour
        minute = current_time.minute
        day = current_time.day
        month = current_time.month
        year = current_time.year
        if (hour == hourDaily) & (minuteDaily == minute) & (nam_vua_cao != year) & (thang_vua_cao != month) & (ngay_vua_cao != day):
            api_url = os.environ.get('API_URL')
            if api_url:
                print(f"Đã lấy URL của API: {api_url}")
            else:
                print("Không thể tìm thấy biến môi trường API_URL.")
            urlTruncate = api_url+"/countries/truncate"
            reset_table(urlTruncate)
            time.sleep(5)
            fuc_craw()
            nam_vua_cao = year
            ngay_vua_cao = day
            thang_vua_cao =  month
      
fuc_craw()
print("Đã craw thành công")

            
# Tạo một luồng mới để chạy hàm crawDaily trong nền
craw_thread = threading.Thread(target=crawDaily, args=(14, 34))
craw_thread.daemon = True
craw_thread.start()



