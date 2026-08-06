# ImageInfoViewer

Ứng dụng desktop Python giúp quét thư mục, hiển thị thông tin kích thước ảnh và preview nhanh.

## Tính năng

- Chọn thư mục và quét đệ quy tất cả file
- Hiển thị tên file + kích thước (width × height) nếu là ảnh
- Preview ảnh khi click vào danh sách (có viền trắng)
- Xuất danh sách ra CSV hoặc Excel
- Copy toàn bộ thông tin vào clipboard
- Build thành file `.exe` độc lập (không cần Python)

---

## 1. Tạo môi trường ảo (khuyến nghị)

Mở **Command Prompt** hoặc **PowerShell** tại thư mục dự án:

```bash
# Tạo virtual environment
python -m venv .venv

# Kích hoạt môi trường ảo
# Windows (CMD):
.venv\Scripts\activate

# Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Linux / macOS:
source .venv/bin/activate
```

Sau khi kích hoạt, bạn sẽ thấy `(.venv)` ở đầu dòng lệnh.

---

## 2. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

Nếu muốn build `.exe`, cài thêm PyInstaller:

```bash
pip install pyinstaller
```

---

## 3. Chạy ứng dụng (chế độ development)

```bash
python main.py
```

---

## 4. Build file .exe

### Cách 1: Dùng file `build_exe.bat` (nhanh nhất)

Chỉ cần double-click hoặc chạy:

```bash
build_exe.bat
```

Script sẽ tự động:
1. Cài đặt các thư viện cần thiết
2. Cài PyInstaller
3. Build file `.exe` (onefile, không hiện console)
4. File kết quả nằm trong thư mục `dist/`

### Cách 2: Build thủ công

```bash
pyinstaller --noconsole --onefile --icon=assets/app_icon.ico main.py
```

Sau khi build xong:
- File `ImageInfoViewer.exe` (hoặc `main.exe`) nằm trong thư mục **`dist/`**
- Bạn có thể copy file `.exe` này sang máy khác và chạy độc lập (không cần cài Python)

> **Lưu ý**: Đảm bảo file icon `assets/app_icon.ico` tồn tại. Nếu không có icon, bỏ tham số `--icon=...`.

---

## Cấu trúc dự án

```
ImageInfoViewer/
├── main.py              # Điểm khởi chạy ứng dụng
├── ui.py                # Giao diện chính
├── file_utils.py        # Quét thư mục & lấy thông tin ảnh
├── preview_utils.py     # Hiển thị preview ảnh
├── export_utils.py      # Xuất CSV / Excel
├── requirements.txt
├── build_exe.bat        # Script build .exe tự động
├── assets/
│   └── app_icon.ico     # Icon ứng dụng (dùng khi build)
└── README.md
```

---

## Cách sử dụng

1. Nhấn **Chọn Folder** → chọn thư mục chứa ảnh
2. Click vào một dòng trong danh sách để xem preview bên phải
3. Xuất dữ liệu:
   - **Xuất CSV** → `output/image_info.csv`
   - **Xuất Excel** → `output/image_info.xlsx`
4. **Copy Info** → copy toàn bộ danh sách vào clipboard

---

## Ghi chú

- Chỉ file ảnh hợp lệ mới hiển thị kích thước; file khác sẽ hiện `(Not an image)`
- Preview được resize tối đa 300×300 pixel và có viền trắng
- Thư mục `output/` sẽ được tạo tự động khi xuất file
- Theme mặc định là `darkly` (có thể đổi trong `main.py`)

---

## Yêu cầu hệ thống

- Windows 10/11 (khuyến nghị)
- Python 3.8 trở lên (chỉ cần khi chạy source hoặc build)
```