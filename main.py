from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class scraper:
     def __init__(self,url):
          self.driver = webdriver.Chrome()
          self.url = url
          self.currency_list = []
     
     def scrap_currencys(self) :
          self.driver.get(self.url)
          time.sleep(5)
          currency_table = self.driver.find_element(By.CLASS_NAME,"kurlarTablo")
          titles = currency_table.find_element(By.TAG_NAME,"thead").find_elements(By.TAG_NAME,"strong")
          rows = currency_table.find_element(By.TAG_NAME,"tbody").find_elements(By.TAG_NAME,"tr")
          for row in rows:
               currency_code = row.find_element(By.CLASS_NAME,"para.kurkodu").text
               unit = row.find_element(By.CLASS_NAME,"para.birim").text
               currency = row.find_element(By.CLASS_NAME,"para").text
               forex_buy = row.find_elements(By.CLASS_NAME,"deger")[0].text
               forex_sell = row.find_elements(By.CLASS_NAME,"deger")[1].text
               self.currency_list.append([currency_code,unit,currency,forex_buy,forex_sell])

     
     def print_currency_table(self):
          for sub in self.currency_list :
               print("currency code =",sub[0])
               print("unit =",sub[1])
               print("currency =",sub[2])
               print("forex buy =",sub[3])
               print("forex sell =",sub[4])


         





#bagımsız
obje = scraper(url="https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+page+site+area/bugun")
obje.scrap_currencys()
obje.print_currency_table()
x = obje.currency_list