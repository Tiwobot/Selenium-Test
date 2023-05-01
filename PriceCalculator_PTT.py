from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import common
from dependencies import ChromeDriverLocation

desiWeight = common.desiKG
desiWidth = common.desiWidth
desiLength = common.desiLength
desiHeight = common.desiHeight
isSMSwanted = common.isSMSwanted

PATH = ChromeDriverLocation
driver = webdriver.Chrome(PATH)
driver.get("https://pttreklamws.ptt.gov.tr/HesapMakinesi/index_tr.html")
driver.implicitly_wait(2)

title = driver.title
print(title)

driver.find_element(By.CSS_SELECTOR, "#menu0f960p0i2im > div").click()
driver.find_element(By.ID, "agirlik").send_keys(desiWeight*1000)
driver.find_element(By.ID, "txt_en").send_keys(desiWidth)
driver.find_element(By.ID, "txt_boy").send_keys(desiLength)
driver.find_element(By.ID, "txt_yuk").send_keys(desiHeight)

driver.find_element(By.ID, "cbx_adrese_teslim").click()
driver.find_element(By.ID, "cbx_teslim_sms").click()

print(driver.find_element(By.ID, "txt_desi").get_attribute("value"))
print(driver.find_element(By.ID, "ucret").get_attribute("value"))