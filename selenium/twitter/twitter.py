from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def scroll_to_bottom():
    script = """
    window.scrollTo(0, document.body.scrollHeight); 
    var lenOfPage = document.body.scrollHeight;
    return lenOfPage;
    """
    len_of_page = driver.execute_script(script)
    load_more = True
    while load_more:
        last_len = len_of_page
        time.sleep(3)
        len_of_page = driver.execute_script(script)
        if last_len == len_of_page:
            load_more = False


inp_user = input("Please enter your username: ")
inp_pass = input("Please enter your password: ")

chrome_driver_path = "C:/MITO/robot/chromedriver-85.exe"
url = "https://twitter.com/login"

driver = webdriver.Chrome(chrome_driver_path)
driver.get(url)
time.sleep(5)

username = driver\
    .find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")

password = driver\
    .find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")

login_button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div")

username.send_keys(inp_user)
password.send_keys(inp_pass)
login_button.click()

time.sleep(10)

search_field = driver\
    .find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")

search_field.send_keys("#ericssonbiketheextramile")
search_field.send_keys(Keys.ENTER)

time.sleep(5)
scroll_to_bottom()
time.sleep(5)

buttons = driver.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1777fci.r-11cpok1.r-1ny4l3l.r-bztko3.r-lrvibr")
like_buttons = [button for button in buttons if button.get_attribute("data-testid") == "like"]

for like_button in like_buttons:
    try:
        like_button.click()
        time.sleep(3)
    except Exception as e:
        print(e)



