from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def extract_downloads(url):
    # تنظیمات کروم
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    
    driver = webdriver.Chrome(options=chrome_options)

    try:
        print(f"Opening URL: {url}")
        driver.get(url)

        # انتظار برای لود صفحه
        print("Waiting for page to load...")
        
        # انتظار برای وجود body
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # اسکرول به پایین برای لود کامل محتوا
        driver.execute_script("window.scrollTo(0, 800);")
        time.sleep(3)
        
        # روش 1: گرفتن تمام spanها با این کلاس و انتخاب دومین مورد
        try:
            all_spans = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.mw-css-81vkv1"))
            )
            
            if len(all_spans) >= 2:
                second_span = all_spans[1]  # دومین عنصر (ایندکس 1)
                print("✅ Found second span with class mw-css-81vkv1")
                print("Content:", second_span.text)
                return second_span.text
            else:
                print(f"❌ Only found {len(all_spans)} spans, need at least 2")
                return None
                
        except:
            # روش 2: استفاده از XPath برای انتخاب دومین span
            print("Trying XPath method for second span...")
            second_span = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//span[@class='mw-css-81vkv1'])[2]"))
            )
            print("✅ Found second span using XPath")
            print("Content:", second_span.text)
            return second_span.text

    except Exception as e:
        print("❌ Error:", str(e))
        
        # دیباگ: بررسی تعداد spanهای موجود
        try:
            all_spans = driver.find_elements(By.CSS_SELECTOR, "span.mw-css-81vkv1")
            print(f"Found {len(all_spans)} spans with class 'mw-css-81vkv1':")
            for i, span in enumerate(all_spans):
                print(f"  Span {i+1}: '{span.text}'")
                
        except Exception as debug_e:
            print("Debug error:", debug_e)
            
        driver.save_screenshot("debug_screenshot.png")
        print("Screenshot saved for debugging")
        
    finally:
        driver.quit()

# تست
url = "https://makerworld.com/en/models/707208-clicker-fidget-print-in-place#profileId-637253"
result = extract_downloads(url)
print("Final result:", result)
