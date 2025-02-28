import time
import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


def datas_to_csv(data,path_output):
    df = pd.DataFrame(data)
    df.columns=['product_name','mount','article','width','height','depth']
    df.to_csv(path_output, index=False)

def scraper(data,driver):
    for product_id in range(1, 13):
        products = driver.find_elements(By.XPATH, "//*[@id='"'main_block'"']/div/div[3]/div[" + str(
            product_id) + "]/div/div/h6/a")

        product_name = products[0].text
        driver.execute_script("arguments[0].click();", products[0])
        time.sleep(1)

        price = driver.find_elements(By.XPATH, "//*[@id='"'product_amount'"']")[0].text
        article = driver.find_elements(By.XPATH,"//*[@id='"'sku'"']")[0].text
        width = driver.find_elements(By.XPATH,"//*[@id='"'characteristics'"']/tbody/tr[1]/td[2]")[0].text
        height = driver.find_elements(By.XPATH, "//*[@id='"'characteristics'"']/tbody/tr[2]/td[2]")[0].text
        depth = driver.find_elements(By.XPATH, "//*[@id='"'characteristics'"']/tbody/tr[3]/td[2]")[0].text

        data.append([product_name,price,article,width,height,depth])
        driver.back()
    return data

def main(path_output):

    chrome_option = webdriver.ChromeOptions()
    chrome_option.page_load_strategy = "normal"

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service)
    driver.maximize_window()
    driver.get('https://parsemachine.com/sandbox/')

    driver.find_element(By.XPATH,"//*[@id='"'main_block'"']/div/div[2]/div/div/div[1]/div/h2/a").click()

    data = []
    for _ in range(2):
        data = data + scraper(data,driver)
        next_page_link = driver.find_element(By.XPATH, "//*[@id='"'pagination'"']/p/a[3]")
        driver.execute_script("arguments[0].click();", next_page_link)
    datas_to_csv(data,path_output)

if __name__=="__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Arguments is not correct")