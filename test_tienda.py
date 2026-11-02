"""Fase 4 - Pruebas estilo pytest.

Ejecutar:  pytest test_tienda.py --html=reporte_pruebas.html --self-contained-html
El fixture `driver` y la captura automática están en conftest.py (Fase 5).
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from login_page import LoginPage
from utils import BASE_URL


def test_login_exitoso(driver):
    """Prueba de login correcto."""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()
    assert "inventory.html" in driver.current_url


def test_agregar_al_carrito(driver):
    """Agregar un producto y verificar el contador del carrito."""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert badge.text == "1"


def test_login_fallido(driver):
    """Prueba de usuario bloqueado."""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()
    assert "locked out" in login.obtener_error()
