from selenium import webdriver
import undetected_chromedriver as uc

# === Cấu hình Proxy ===
proxy = "47.243.180.142:808"  # Đảm bảo proxy bạn sử dụng đang hoạt động

# === Tùy chọn Chrome ===
options = uc.ChromeOptions()
options.add_argument(f'--proxy-server=http://{proxy}')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")  # Mở full cửa sổ trình duyệt
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# === Khởi tạo trình duyệt undetected ===
driver = uc.Chrome(options=options)

# === Kiểm tra IP proxy ===
driver.get("https://api.ipify.org?format=json")  # Kiểm tra IP xem có thay đổi không

# === Mở TikTok ===
driver.get("https://www.tiktok.com/")

# === GIỮ MỞ để bạn kiểm tra ===
input("Nhấn Enter để đóng trình duyệt...")

# === Đóng trình duyệt sau khi xong ===
driver.quit()
