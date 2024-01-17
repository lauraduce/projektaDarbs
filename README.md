# Projekta Darbs

# **Counter-Strike 2 Virtuālo Priekšmetu Cenu Salīdzinātājs**

## **Uzdevuma apraksts**

Pēdējos gados virtuālo priekšmetu (turpmāk tekstā- In-game item) iegāde ir kļuvusi ar vien populārāka. Daži cilvēki to dara vienkārši tāpēc, lai izbaudītu estētisko izskatu spēlē, bet citi izvēlas ieguldīt, cerot uz to, ka In-game item cena laika gaitā pieaugs. Protams, visiem ir aktuāli atrast vēlamo In-game item par izdevīgāko cenu. Izveidotā programma ļauj salīdzināt vēlāmā In-game item cenu trīs populārās tīmekļa vietnēs (DMarket, GamerPay, SkinBaron).

Programmas mērķis ir sniegt lietotājam iespēju vienkārši un efektīvi salīdzināt In-game item cenas, lai noteiktu, kur ir visizdevīgāk iegādāties vēlamo In-game item. 

Lietotājam tiek prasīts ievadīt vēlāmā In-game item nosaukumu un kvalitāti. Pēc ievades programma automātiski pārbauda cenu tīmekļa vietnēs, kas, ja nepieciešams, izmantojot Eiropas Centrālās bankas kursu, tiek pārveidotas no dolāriem uz eiro. Rezultātos tiek iekļauta informācija par In-game item cenu, komisijas lielumu, kā arī aprēķināta cena ar komisiju. Tāpāt tiek sniegta informācija par to, vai In-game item iekļaujas vai izkrīt no attiecīgās mājaslapas depozīta diapazona. Visi rezultāti tiek saglabāti Excel datnē, nodrošinot lietotājus ar pārskatāmu informāciju par labākajiem piedāvājumiem.

[Saite uz programmas testu un rezultātu.](https://www.youtube.com/watch?v=rG6ZBmdNeJQ)

## **Python bibliotēku apraksts**

- import selenium - bāze programmai, kas ļauj automatizēt timekļa pārlūkošanu. Tā tiek izmantota, lai meklētu un iegūtu datus no tīmekļa vietnēm.

- from selenium.webdriver.common.by import By - rīks tiek izmantots, lai ērti identificētu tīmekļa vietnes elementus. To izmanto, piemēram, lai norādītu, kā atrast konkrētu elementu tīmekļa lapā.

- from selenium.webdriver.support.ui import WebDriverWait - rīks nodrošina dažādas gaidīšanas nosacījumu funkcijas, ko izmanto, lai definētu, kad darbības var turpināties pēc gaidīšanas perioda.

- from selenium.webdriver.support import expected_conditions as EC - nodrošina papuldu rīkus un metodes, lai veiktu dažādus uzdevumus.

- from selenium.webdriver.common.keys import Keys - ļauj darboties ar tastatūras taustiņiem tīmekļa pārlūkošanas procesā. 

- import time - ļauj aizkavēt noteiktas darbības. Piemēram, pagaidīt, kamēr tīmekļa lapa ielādējas, pirms tiek veikta nākamā darbība.

- import re - piedāvā regulāro izteiksmju apstrādes iespējas. To izmanto, piemēram, teksta analīzei un datu iegūšanai.

- from openpyxl import Workbook, load_workbook - Bibliotēka, kas ļauj veikt darbības ar Excel datnēm. Piemēram, pievienot vai nolasīt datus no Excel datnēm.

## **Metožu apraksts**

### 1. Webdriver inicialiizācija Python:

- Inicializē Google Chrome pārlūkprogrammu, izmantojot Selenium WebDriver.
- Izmanto papildu komponentes, piemēram, Service un ChromeOptions

### 2. Ievade:

- Tiek lūgts lietotājam ievadīt priekšmeta nosaukumu un kvalitāti.

### 3. Tīmekļa vietņu atvēršana un satura meklēšana:

- Programma izmanto WebDriver, lai atvērtu tīmekļa vietnes.

- Izmantojot get() metodi, tiek atvērtas katra tīmekļa vietne, un automātiski tiek veikta meklēšana pēc vajadzīgajiem elementiem un informācijas.

    - Valūtas kursa meklēšana
    - Cenu meklēšana salīdzināšanai:
        - Ja ir nepieciešams programma apstiprina sīkdatnes.
        - Tālāk programma meklē ievades lauku jeb "Search Bar", kurā tiek ierakstīts lietotāja vēlāmais priekšmets.
        - Tā kā zināms, ka atbilstoša priekšmeta izdevīgākais piedāvājums atradīsies pats pirmais mājaslapas kreisajā pusē, tā elementa iekšējais teksts tiek nolasīts.

- Meklēšanai tika izmantots "By.CLASS_NAME", "By.XPATH", "By.ID" un "By.CSS_SELECTOR"
- Nolasīšanai tika izmantots get_attribute()

### 4. Datu apstrāde:

- Katrai tīmekļa vietnei tike izveidots saraksts, kurā tiks saglabāti visi dati.

- Dati tiek pārveidoti par "float" un tiek noņemtas liekās zīmes, lai ar tiem varētu veikt matemātiskos aprēķinus. Piem. (float(re.sub('[^0-9.]', '', priceGetSB)))

- Iegūtie cenu dati tiek apstrādāti izmantojot formulas, kas tika izveidotas atbilstoši komisiju makasas lielumam un valūtai.

- Tiek pārbaudīts, vai cena ir noteiktajā depozīta diapazona. 

- Izmantojot extend() visi dati tiek salikti sarakstos.

### 5. Datu ievietošana Excel datnē

- Tiek izveidots saraksts ar virsrakstiem.

- Imantojot openpyxl, tiek izveidota jauna datne.

- Visi saraksti tiek ievietoti Excel datnē izmantojot append().


