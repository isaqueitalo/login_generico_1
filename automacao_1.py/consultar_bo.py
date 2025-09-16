from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time

# Iniciar navegador e aguardar login manual
driver = webdriver.Chrome()
driver.get("https://www.policiaagil.sds.pe.gov.br/pagina-inicial")

input("Faça o login manualmente e clique em ENTRAR. Depois pressione Enter aqui para continuar...")

# Acessar Consulta BOEPM
driver.find_element(By.LINK_TEXT, "Consulta BOEPM").click()
time.sleep(2)

# Preencher data de hoje
data_hoje = datetime.now().strftime("%d/%m/%Y")
driver.find_element(By.NAME, "dataInicial").clear()
driver.find_element(By.NAME, "dataInicial").send_keys(data_hoje)
driver.find_element(By.NAME, "dataFinal").clear()
driver.find_element(By.NAME, "dataFinal").send_keys(data_hoje)

# Selecionar unidade
Select(driver.find_element(By.NAME, "unidade")).select_by_visible_text("6º BPM")

# Clicar em pesquisar
driver.find_element(By.XPATH, "//button[contains(text(), 'Pesquisar')]").click()
time.sleep(3)

# Extrair dados dos BOs (ajuste os seletores conforme o site real)
boletins = driver.find_elements(By.CLASS_NAME, "bo-item")  # Exemplo genérico
for bo in boletins:
    numero = bo.find_element(By.CLASS_NAME, "numero").text
    data = bo.find_element(By.CLASS_NAME, "data").text
    tipo = bo.find_element(By.CLASS_NAME, "tipo").text
    relato = bo.find_element(By.CLASS_NAME, "relato").text
    print(f"BO Nº {numero} | {data} | {tipo}\nRelato: {relato}\n")

input("Pressione Enter para encerrar...")
driver.quit()