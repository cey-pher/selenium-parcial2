"""Fase 1 - Automatización básica (script).  Ejecutar: python test_practico.py"""
from selenium.webdriver.common.by import By

from utils import BASE_URL, capturar, crear_driver


def ejecutar_pruebas():
    driver = crear_driver()
    driver.implicitly_wait(10)
    try:
        # --- CASO 1: Login exitoso ---
        print("Ejecutando Caso 1: Login...")
        driver.get(BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert "inventory.html" in driver.current_url
        capturar(driver, "fase1_caso1_login_exitoso")
        print("OK Caso 1 completado con éxito.")

        # --- CASO 2: Agregar al carrito ---
        print("Ejecutando Caso 2: Agregar producto...")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert badge == "1"
        capturar(driver, "fase1_caso2_agregar_carrito")
        print("OK Caso 2 completado con éxito.")

        # --- CASO 3: Login fallido (usuario bloqueado) ---
        print("Ejecutando Caso 3: Login fallido...")
        driver.delete_all_cookies()  # limpiar sesión
        driver.get(BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        # By.DATA_TEST no existe en Selenium: se usa un selector CSS por atributo
        error_msg = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        assert "Sorry, this user has been locked out" in error_msg
        capturar(driver, "fase1_caso3_login_fallido")
        print("OK Caso 3 completado con éxito.")
    except Exception as e:
        print(f"ERROR durante la ejecución: {e}")
        capturar(driver, "fase1_error")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    ejecutar_pruebas()
