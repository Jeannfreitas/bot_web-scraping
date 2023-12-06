from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl


drive = webdriver.Chrome()
drive.get('https://www.kabum.com.br/promocao/MENU_PCGAMER')

titulo = drive.find_elements(By.XPATH,"//span[@class='sc-d79c9c3f-0 nlmfp sc-cdc9b13f-16 eHyEuD nameCard']")

preços = drive.find_elements(By.XPATH,"//span[@class='sc-620f2d27-2 bMHwXA priceCard']")

workbook = openpyxl.Workbook()

workbook.create_sheet('produtos')

sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'produto'
sheet_produtos['b1'].value = 'preço'


for a,b in zip(titulo,preços):
   sheet_produtos.append([a.text,b.text])
   
workbook.save('produtos.xlsx')  
   