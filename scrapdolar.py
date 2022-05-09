from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions() # Creacion del objeto
options.add_argument('--headless') # Para que corra Chrome en 2do plano
options.add_argument('--disable-extensions') # Sin Extensiones para que no cause problemas

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options) # Inicializacion del Driver


# Se declara la URL con la cual vamos a trabajar
driver.get('https://www.cotizacioneshoy.com.ar/cotizaciones')

# Se pasa como parametro el Full Xpath del elemento que queremos Scrapear
precio_compra = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section[1]/div[2]/table/tbody/tr[1]/td[2]')
precio_venta = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section[1]/div[2]/table/tbody/tr[1]/td[3]')

# Se transforman a tipo texto los datos obtenidos
compra = precio_compra.text
venta = precio_venta.text

driver.quit() # Se cierra el proceso y luego ya podemos almacenar o trabajar los datos obtenidos desde el Scrapeo
