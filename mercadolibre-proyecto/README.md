# TEST DE JESUS EDUARDO REYES MARTINEZ

# 🛠 Proyecto: Automatización de búsqueda en Mercado Libre

Este proyecto automatiza, mediante **Selenium + Python**, una búsqueda en [Mercado Libre](https://www.mercadolibre.com), aplicando filtros y ordenando resultados.  
Finalmente, genera un **reporte HTML con capturas de pantalla** y muestra en consola los primeros 5 productos encontrados con su nombre y precio.

---

## 📌 Requisitos previos

Antes de ejecutar el proyecto asegúrate de tener instalado:

1. **Python 3.10+** (recomendado 3.12 o 3.13)  
   [Descargar Python](https://www.python.org/downloads/)
2. **Google Chrome** (actualizado a tu versión más reciente)  
   Verifica tu versión en: `Menú > Ayuda > Información de Google Chrome`
3. **ChromeDriver** (compatible con tu versión de Chrome)  
   Descárgalo desde: [chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

   * Extrae el archivo y colócalo en una carpeta, ej: `C:\\\\chromedriver\\\\`
   * Agrega esa carpeta al **PATH** de tu sistema:

     * En Windows:

       * Ve a **Variables de entorno**
       * Edita la variable `Path`
       * Agrega la carpeta (ej: `C:\\\\chromedriver\\\\`)
       * ✅ Importante: no pongas el `.exe`, solo la carpeta.

     * Verifica la instalación abriendo CMD y ejecutando:

```bash
       chromedriver --version
       ```

4. Instalar dependencias de Python (desde la carpeta del proyecto):

```bash
   pip install selenium



# 📌Ejecución



\* Abre una terminal en la carpeta del proyecto:



cd C:\\\\mercadolibre-proyecto



\* Ejecuta el script:



python test.py



# ⚙️ Flujo automatizado del programa



El script realiza los siguientes pasos de forma automática:



1. Abre la página principal de Mercado Libre.
2. Selecciona México como país.
3. Cierra el banner de cookies (si aparece).
4. Busca el término "Playstation 5".
5. Filtra resultados por condición Nuevos.
6. Intenta filtrar ubicación por CDMX (si está disponible).
7. Ordena los resultados de Mayor a menor precio.
8. Obtiene el nombre y precio de los primeros 5 productos.
9. Imprime esos productos en la consola.
10. Genera un reporte HTML con capturas de pantalla de cada paso.
11. El reporte y las capturas se guardan dentro de la carpeta del proyecto.

