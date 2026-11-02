"""Fase 5 - Fallo forzado para ver la captura automática en el reporte.

Ejecutar desde la raíz del proyecto:
    pytest demo_fallo/test_fallo.py --html=reporte_fallos.html --self-contained-html
Este test FALLA a propósito (el texto "Bienvenido" no existe en saucedemo.com).
"""
from login_page import LoginPage
from utils import BASE_URL


def test_fallo_forzado(driver):
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()
    assert "Bienvenido" in driver.page_source
