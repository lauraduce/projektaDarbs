import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import re
from openpyxl import Workbook, load_workbook
print("Ievadiet valamas lietas nosaukumu un kvalitati:")
item= input()

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

DMarket=[]
urlDM = "https://dmarket.com/ingame-items/item-list/csgo-skins"
driver.get(urlDM)
time.sleep(2)
SearchDM = driver.find_element(By.CLASS_NAME, "o-filter__searchInput")
SearchDM.clear()
SearchDM.send_keys(item)
time.sleep(2)


priceFindDM = driver.find_element(By.CLASS_NAME, "c-asset__priceNumber")
priceGetDM = priceFindDM.get_attribute('innerText')
priceDM = float(re.sub('[^0-9.]', '', priceGetDM))
print(priceDM)

urlValutasKurss = "https://www.bank.lv/statistika/dati-statistika/valutu-kursi/aktualie"
driver.get(urlValutasKurss)
time.sleep(2)
acceptCookies1 = driver.find_element(By.CLASS_NAME, "status")
acceptCookies1.click()
time.sleep(2)
exchangeRateFind = driver.find_element(By.XPATH, '//*[@id="period2024-01-08"]/div[2]/div/div/div/table/tbody/tr[29]/td[3]')
time.sleep(4)
exchageRateGet = exchangeRateFind.get_attribute('innerText')
exchangeRate = float(exchageRateGet)

commissionDm = "3.85% + 0.27€"

withoutCommissionDM = round((priceDM/exchangeRate), 2)
withCommissionDM = round(((withoutCommissionDM)*1.0385 + 0.27), 2)

minDM = 1/exchangeRate
maxDM = 500/exchangeRate

if minDM<=withoutCommissionDM<=maxDM:
    limitsDM = "+"
else:
    limitsDM = "-"

DMarket.extend([item, withoutCommissionDM, commissionDm, withCommissionDM, limitsDM])

print(DMarket)