import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

def crawldata_bds():
    print(" Bắt đầu thu thập dữ liệu lúc 6h sáng")

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://batdongsan.so/')
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="hnp"]/div[2]/div[1]/form/div/div[5]/select/option[4]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="hnp"]/div[2]/div[1]/form/div/div[4]/select/option[2]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="hnp"]/div[2]/div[1]/form/div/div[3]/button').click()
    time.sleep(4)

    data = []
    page = 1

    while True:
        print(f" Đang thu thập dữ liệu trang {page}...")
        time.sleep(2)

        danh_sach_bai = driver.find_elements(By.XPATH, '//*[@id="main"]/div/div/section/div/div[1]/article')

        if not danh_sach_bai:
            print(" Không còn bài viết nào.")
            break

        links = []
        for bai in danh_sach_bai:
            try:
                link = bai.find_element(By.XPATH, './div[1]/h3/a').get_attribute('href')
                links.append(link)
            except:
                continue

        for link in links:
            driver.execute_script("window.open(arguments[0]);", link)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)

            try:
                tieu_de = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/section[1]/h1').text.strip()
            except:
                tieu_de = "Không có tiêu đề"

            try:
                mo_ta = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/section[1]/div[2]/div[3]').text.strip()
            except:
                mo_ta = "Không có mô tả"

            try:
                gia = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/section[1]/div[1]/div[2]/div[2]').text.strip()
            except:
                gia = "Không có giá"

            try:
                dien_tich = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/section[1]/div[2]/ul/li[1]').text.strip()
            except:
                dien_tich = "Không có diện tích"

            try:
                dia_chi = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/section[1]/div[2]/div[2]').text.strip()
            except:
                dia_chi = "Không có địa chỉ"

            data.append([tieu_de, mo_ta, gia, dien_tich, dia_chi])

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(5)

        try:
            next_button = driver.find_element(By.LINK_TEXT, '»')
            next_button.click()
            page += 1
            time.sleep(5)
        except:
            print(" Không tìm thấy nút Trang tiếp theo. Đã lấy hết dữ liệu!")
            break

    driver.quit()

    df = pd.DataFrame(data, columns=['Tiêu đề', 'Mô tả', 'Giá', 'Diện tích', 'Địa chỉ']) 
    df.to_csv('btl_alonhadat_danang.csv', index=False, encoding='utf-8-sig')
    print(f" Hoàn thành! Đã lưu {len(data)} bài viết.")

schedule.every().day.at("06:00").do(crawldata_bds)

print(" Đang chờ đến 6h sáng mỗi ngày để thu thập dữ liệu")
while True:
    schedule.run_pending()
    time.sleep(60)
