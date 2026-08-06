@echo off
echo ================================
echo   BẮT ĐẦU BUILD ImageInfoViewer
echo ================================
echo Cài đặt thư viện...
pip install -r requirements.txt
pip install pyinstaller
echo ----------------
echo Đang build EXE...
pyinstaller --noconsole --onefile --icon=assets/app_icon.ico main.py
echo ----------------
echo Build hoàn tất! File .exe nằm trong thư mục dist/
echo ================================
pause
