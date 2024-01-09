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

urlExchangeRate = "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html"
driver.get(urlExchangeRate)
time.sleep(2)
exchangeRateFind = driver.find_element(By.XPATH, '//*[@id="main-wrapper"]/main/div[3]/div[2]/div/div/table/tbody/tr[1]/td[3]/a/span')
time.sleep(4)
exchageRateGet = exchangeRateFind.get_attribute('innerText')
exchangeRate = float(exchageRateGet)

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

CSFloat = []

urlCSFloat = "https://csfloat.com/"

driver.get(urlCSFloat)
time.sleep(2)
changeCurrencyCSFloat = driver.find_element(By.XPATH, '//*[@id="mat-select-0"]/div/div[2]/div')
changeCurrencyCSFloat.click()
CurrencyCSFloatToUSD = driver.find_element(By.XPATH, '//*[@id="mat-option-0"]/span')
CurrencyCSFloatToUSD.click()
searchCSFloat = driver.find_element(By.ID, "mat-input-0")
time.sleep(2)
searchCSFloat.clear()
searchCSFloat.send_keys(item)
searchCSFloat.send_keys(Keys.ENTER)
time.sleep(2)

priceFindCSFloat = driver.find_element(By.CLASS_NAME, "price.ng-star-inserted")
priceGetCSFloat = priceFindCSFloat.get_attribute('innerText')
priceCSFloat = float(re.sub('[^0-9.]', '', priceGetCSFloat))

commissionCSFloat = "2.8% + 0.27€"

withoutCommissionCSFloat = round((priceCSFloat/exchangeRate),2)
withCommissionCSFloat = round(((withoutCommissionCSFloat)*1.028 + 0.27),2)

minCSFloat = 5/exchangeRate
maxCSFloat = 10000/exchangeRate

if minCSFloat<=withoutCommissionCSFloat<=maxCSFloat:
    limitsCSFloat = "+"
else:
    limitsCSFloat = "-"

CSFloat.extend([item, withoutCommissionCSFloat, commissionCSFloat, withCommissionCSFloat, limitsCSFloat])

print(CSFloat)