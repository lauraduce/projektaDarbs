import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook, load_workbook
print("Ievadiet valamas lietas nosaukumu un kvalitati:")
item= input()
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
urlDM = "https://dmarket.com/ingame-items/item-list/csgo-skins"
driver.get(urlDM)
time.sleep(2)
SearchDM = driver.find_element(By.CLASS_NAME, "o-filter__searchInput")
SearchDM.clear()
SearchDM.send_keys(item)
time.sleep(2)


priceFindDM = driver.find_element(By.CLASS_NAME, "c-asset__priceNumber")
priceDM = priceFindDM.get_attribute('innerText')

print(priceDM)