from selenium import webdriver
import time

chrome_driver_path = "C:/MITO/robot/chromedriver-85.exe"
url = "https://eksisozluk.com/python--109286"

driver = webdriver.Chrome(chrome_driver_path)
driver.get(url)
time.sleep(5)

elements = driver.find_elements_by_css_selector(".content")
pager = int(driver.find_elements_by_class_name("last")[0])

print(pager.text)

for element in elements:
    print("*" * 100)
    print(element.text)
    print("*" * 100)

driver.close()
