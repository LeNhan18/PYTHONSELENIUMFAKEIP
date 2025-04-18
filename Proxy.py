import zipfile
import os
import undetected_chromedriver as uc

# ======= Thay bằng proxy của bạn =======
proxy_host = "123.123.123.123"    # IP proxy
proxy_port = "8080"               # Port
proxy_user = "nhan1811"      # Username proxy
proxy_pass = "nhan1811"      # Password proxy
# =======================================

# === Tạo extension Chrome cho proxy auth ===
plugin_file = 'proxy_auth_plugin.zip'
manifest_json = """
{
  "version": "1.0.0",
  "manifest_version": 2,
  "name": "ProxyAuthExtension",
  "permissions": [
    "proxy",
    "tabs",
    "unlimitedStorage",
    "storage",
    "<all_urls>",
    "webRequest",
    "webRequestBlocking"
  ],
  "background": {
    "scripts": ["background.js"]
  },
  "minimum_chrome_version":"22.0.0"
}
"""

background_js = f"""
var config = {{
    mode: "fixed_servers",
    rules: {{
      singleProxy: {{
        scheme: "http",
        host: "{proxy_host}",
        port: parseInt({proxy_port})
      }},
      bypassList: ["localhost"]
    }}
  }};

chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});

function callbackFn(details) {{
    return {{
        authCredentials: {{
            username: "{proxy_user}",
            password: "{proxy_pass}"
        }}
    }};
}}

chrome.webRequest.onAuthRequired.addListener(
    callbackFn,
    {{urls: ["<all_urls>"]}},
    ['blocking']
);
"""

with zipfile.ZipFile(plugin_file, 'w') as zp:
    zp.writestr("manifest.json", manifest_json)
    zp.writestr("background.js", background_js)

# === Setup Chrome options ===
options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_extension(plugin_file)

# === Mở trình duyệt với proxy đã cài sẵn ===
driver = uc.Chrome(options=options)
driver.get("https://api.ipify.org?format=json")  # Kiểm tra IP

# === Giữ trình duyệt mở để xem ===
input("Nhấn Enter để thoát...")

driver.quit()
os.remove(plugin_file)  # Xoá plugin sau khi chạy
