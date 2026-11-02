"""Fase 2 - Esperas explícitas (Explicit Waits).  Ejecutar: python robust_test.py"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import BASE_URL, capturar, crear_driver


def ejecutar():
    driver = crear_driver()
    wait = WebDriverWait(driver, 10)  # espera máxima de 10 s
    try:
        # --- CASO 1: Login seguro ---
        driver.get(BASE_URL)
        user_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        user_input.send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.url_contains("inventory.html"))
        capturar(driver, "fase2_caso1_login")

        # --- CASO 2: Agregar al carrito con verificación de clic ---
        btn_add = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        btn_add.click()
        badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        print(f"Prueba exitosa: Carrito tiene {badge.text} producto(s).")
        capturar(driver, "fase2_caso2_carrito")

        # --- CASO 3: Validación de error de bloqueo ---
        driver.delete_all_cookies()
        driver.get(BASE_URL)
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        error_container = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        )
        print(f"Validación de error correcta: {error_container.text}")
        capturar(driver, "fase2_caso3_error_bloqueo")
    finally:
        driver.quit()


if __name__ == "__main__":
    ejecutar()
