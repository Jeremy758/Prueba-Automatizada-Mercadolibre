from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

# Crear carpeta para guardar screenshots
if not os.path.exists("report"):
    os.makedirs("report")

def take_screenshot(step_name):
    filename = f"report/{step_name}.png"
    driver.save_screenshot(filename)
    print(f"📸 Captura guardada: {filename}")

# Inicializar Chrome
driver = webdriver.Chrome()
driver.maximize_window()

wait_time = 1.5  # cada acción ahora espera 1.5 seg

# 1. Abrir Mercado Libre
print("🌐 Abriendo MercadoLibre...")
driver.get("https://www.mercadolibre.com/")
time.sleep(wait_time)
take_screenshot("01_home")

# 2. Seleccionar México
try:
    mexico = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "MX"))
    )
    mexico.click()
    print("✅ País seleccionado: México")
except:
    print("⚠️ Ya estabas en MercadoLibre México")
time.sleep(wait_time)
take_screenshot("02_mexico")

# 3. Cerrar banner cookies
try:
    aceptar_cookies = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Entendido')] | //button[contains(., 'Aceptar')]"))
    )
    aceptar_cookies.click()
    print("✅ Banner de cookies cerrado")
except:
    print("⚠️ No apareció banner de cookies")
time.sleep(wait_time)
take_screenshot("03_cookies")

# 4. Buscar Playstation 5
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "as_word"))
)
search_box.send_keys("playstation 5")
search_box.send_keys(Keys.RETURN)
print("🔍 Buscando 'playstation 5'...")
time.sleep(wait_time)
take_screenshot("04_search")

# 5. Filtrar por Nuevo
try:
    nuevo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Nuevo']"))
    )
    nuevo.click()
    print("✅ Filtro aplicado: Nuevo")
except:
    print("⚠️ No encontré el filtro 'Nuevo'")
time.sleep(wait_time)
take_screenshot("05_nuevo")

# 6. Filtrar por ubicación CDMX
try:
    cdmx = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Ciudad de México')] | //span[contains(text(),'CDMX')] | //span[contains(text(),'Distrito Federal')]"))
    )
    cdmx.click()
    print("✅ Filtro aplicado: CDMX")
except:
    print("⚠️ No encontré el filtro de ubicación CDMX")
time.sleep(wait_time)
take_screenshot("06_cdmx")

# 7. Ordenar por Mayor precio
try:
    order_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'andes-dropdown__trigger')]"))
    )
    order_dropdown.click()
    print("✅ Desplegado menú de ordenamiento")
    time.sleep(wait_time)

    mayor_precio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li//span[contains(text(),'Mayor') and contains(text(),'precio')]"))
    )
    mayor_precio.click()
    print("✅ Ordenado por Mayor precio")
except:
    print("⚠️ No encontré la opción de 'Mayor precio'")
time.sleep(wait_time)
take_screenshot("07_mayor_precio")

# 8. Obtener productos
productos = []
try:
    nombres = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//h2[contains(@class,'title')]"))
    )
    precios = driver.find_elements(By.XPATH, "//span[@class='andes-money-amount__fraction']")

    for i in range(5):
        nombre = nombres[i].text
        precio = precios[i].text if i < len(precios) else "N/D"
        productos.append((nombre, precio))
        print(f"{i+1}. {nombre} - ${precio}")
except:
    print("⚠️ No se pudieron obtener los productos")
time.sleep(wait_time)
take_screenshot("08_resultados")

driver.quit()

# 9. Crear reporte HTML
with open("report/reporte.html", "w", encoding="utf-8") as f:
    f.write("<html><head><title>Reporte MercadoLibre</title></head><body>")
    f.write("<h1>Reporte de ejecución - MercadoLibre</h1>")
    pasos = [
        "01_home", "02_mexico", "03_cookies", "04_search",
        "05_nuevo", "06_cdmx", "07_mayor_precio", "08_resultados"
    ]
    for paso in pasos:
        f.write(f"<h2>{paso}</h2><img src='{paso}.png' width='600'><br>")
    f.write("<h2>Resultados</h2><ul>")
    for p in productos:
        f.write(f"<li>{p[0]} - ${p[1]}</li>")
    f.write("</ul></body></html>")

print("📄 Reporte generado en: report/reporte.html")

