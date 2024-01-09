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
searchDM = driver.find_element(By.CLASS_NAME, "o-filter__searchInput")
searchDM.clear()
searchDM.send_keys(item)
time.sleep(2)


priceFindDM = driver.find_element(By.CLASS_NAME, "c-asset__priceNumber")
priceGetDM = priceFindDM.get_attribute('innerText')
priceDM = float(re.sub('[^0-9.]', '', priceGetDM))
print(priceDM)

commissionDm = "3.85% + €0.27"

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

urlCSF = "https://csfloat.com/"

driver.get(urlCSF)
time.sleep(2)
changeCurrencyCSF = driver.find_element(By.XPATH, '//*[@id="mat-select-0"]/div/div[2]/div')
changeCurrencyCSF.click()
CurrencyCSFToUSD = driver.find_element(By.XPATH, '//*[@id="mat-option-0"]/span')
CurrencyCSFToUSD.click()
searchCSF = driver.find_element(By.ID, "mat-input-0")
time.sleep(2)
searchCSF.clear()
searchCSF.send_keys(item)
searchCSF.send_keys(Keys.ENTER)
time.sleep(2)

priceFindCSF = driver.find_element(By.CLASS_NAME, "price.ng-star-inserted")
priceGetCSF = priceFindCSF.get_attribute('innerText')
priceCSFloat = float(re.sub('[^0-9.]', '', priceGetCSF))

commissionCSF = "2.8% + €0.27"

withoutCommissionCSF = round((priceCSFloat/exchangeRate),2)
withCommissionCSF = round(((withoutCommissionCSF)*1.028 + 0.27),2)

minCSF = 5/exchangeRate
maxCSF = 10000/exchangeRate

if minCSF<=withoutCommissionCSF<=maxCSF:
    limitsCSF = "+"
else:
    limitsCSF = "-"

CSFloat.extend([item, withoutCommissionCSF, commissionCSF, withCommissionCSF, limitsCSF])

print(CSFloat)

GamerPay = []

urlGP = "https://gamerpay.gg/"
driver.get(urlGP)
time.sleep(2)
acceptCookiesGP= driver.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
acceptCookiesGP.click()
time.sleep(2)
searchGP = driver.find_element(By.ID, "searchBar")
time.sleep(2)
searchGP.send_keys(item)
searchGP.send_keys(Keys.ENTER)
time.sleep(8)

priceFindGP = driver.find_element(By.CLASS_NAME, "ItemCardNewBody_pricePrimary__Tpkw7")
priceGetGP = priceFindGP.get_attribute('innerText')
priceGP = float(re.sub('[^0-9.]', '', priceGetGP))

commissionGP = "5% + €0.70"

withoutCommissionGP = priceGP
withCommissionGP = round(((withoutCommissionGP)*1.05 + 0.7),2)

limitsGP = "+"

GamerPay.extend([item,withoutCommissionGP, commissionGP, withCommissionGP, limitsGP])

print(GamerPay)

SkinBaron = []

urlSB = "https://skinbaron.de/en"
driver.get(urlSB)
time.sleep(2)
acceptCookiesSB = driver.find_element(By.ID,"onetrust-accept-btn-handler")
acceptCookiesSB.click()
time.sleep(2)
searchSB = driver.find_element(By.CSS_SELECTOR, 'input[pathtodata="variants"]')
time.sleep(2)
searchSB.send_keys(item)
searchSB.send_keys(Keys.ENTER)
time.sleep(4)

priceFindSB = driver.find_element(By.XPATH, '//*[@id="offer-container"]/ul/li[1]/sb-offer-card/div/div/div[3]/div/div/span[3]')
priceGetSB = priceFindSB.get_attribute('innerText')
priceSB = float(re.sub('[^0-9.]', '', priceGetSB))

commissionSB = "5% + €0.35"

withoutCommissionSB = priceSB
withCommissionSB = round(((withoutCommissionSB)*1.05 + 0.35),2)

minSB = 1
maxSB = 7500

if 1<=withoutCommissionSB<=7500:
    limitsSB = "+"
else:
    limitsSB = "-"

SkinBaron.extend([item, withoutCommissionSB, commissionSB, withCommissionSB, limitsSB])

print(SkinBaron)

