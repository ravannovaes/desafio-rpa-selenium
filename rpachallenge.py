#Importação da biblioteca pandas, e do webdriver do Selenium.
import pandas as pd 
from selenium import webdriver

#Leitura do arquivo challenge.xlsx com o pandas.
tabela = pd.read_excel("challenge.xlsx")

#Site aberto pelo navegador Chrome utilizando o webdriver e a função GET para a url.
navegador = webdriver.Chrome()
navegador.get("https://www.rpachallenge.com/")

#Laço for com index da tabela, com o método iloc do pandas é possivel acessar dados da linha, de cada coluna a cada iteração.
for indice in tabela.index:
    first_name = tabela.iloc[indice,0]
    last_name = tabela.iloc[indice, 1]
    company_name= tabela.iloc[indice, 2]
    rolo_in_company = tabela.iloc[indice, 3]
    andress = tabela.iloc[indice, 4]
    email = tabela.iloc[indice, 5]
    phone_number = tabela.iloc[indice, 6]
    
#Linhas de código Utilizadas para escrever na página com o método send_keys do campo identificado com o Seletor CSS: find_element_by_css_selector.
    navegador.find_element_by_css_selector("input[ng-reflect-name='labelFirstName']").send_keys(first_name)
    navegador.find_element_by_css_selector("input[ng-reflect-name='labelLastName']").send_keys(last_name)
    navegador.find_element_by_css_selector("input[ng-reflect-name='labelCompanyName']").send_keys(company_name)
    navegador.find_element_by_css_selector("input[ng-reflect-name='labelRole']").send_keys(rolo_in_company)
    navegador.find_element_by_css_selector("input[ng-reflect-name='labelAddress']").send_keys(str(andress))
    navegador.find_element_by_css_selector("input[ng-reflect-name='labelPhone']").send_keys(str(phone_number))
    navegador.find_element_by_css_selector("input[ng-reflect-name='labelEmail']").send_keys(email)
    navegador.find_element_by_css_selector("input[class='btn uiColorButton']").click()
