"""Utilidades compartidas: creación del driver y capturas de evidencia."""
import os
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

BASE_URL = os.environ.get("SAUCE_URL", "https://www.saucedemo.com")
EVIDENCIAS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "evidencias")


def crear_driver(headless=None):
    """Crea Chrome. HEADLESS=1 (variable de entorno) activa el modo sin ventana (CI)."""
    if headless is None:
        headless = os.environ.get("HEADLESS", "0") == "1"

    options = Options()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1366,900")
    # Evita el aviso de Chrome "cambiar contraseña" que tapa la página
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver_path = os.environ.get("CHROMEDRIVER_PATH")
    service = Service(driver_path) if driver_path else Service()
    return webdriver.Chrome(options=options, service=service)


def capturar(driver, nombre):
    """Guarda una captura en evidencias/<nombre>.png y devuelve la ruta."""
    os.makedirs(EVIDENCIAS, exist_ok=True)
    limpio = re.sub(r"[^A-Za-z0-9_.-]+", "_", nombre)
    ruta = os.path.join(EVIDENCIAS, f"{limpio}.png")
    driver.save_screenshot(ruta)
    return ruta
