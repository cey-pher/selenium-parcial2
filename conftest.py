"""Fase 5 - Configuración de pytest: fixture del navegador y captura automática.

Cada test deja su captura en el reporte HTML (en fallos y también en aciertos,
como evidencia) y en evidencias/<test>.png.
"""
import pytest
import pytest_html

from utils import capturar, crear_driver


@pytest.fixture
def driver():
    """Fixture del navegador (HEADLESS=1 para correr sin ventana)."""
    d = crear_driver()
    d.maximize_window()
    yield d
    d.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Adjunta una captura de pantalla al reporte HTML después de cada test."""
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call":
        driver = item.funcargs.get("driver")
        if driver is not None:
            estado = "FALLO" if report.failed else "OK"
            capturar(driver, f"{item.name}_{estado}")
            png_b64 = driver.get_screenshot_as_base64()
            extras.append(pytest_html.extras.png(png_b64, name=f"Captura ({estado})"))
        report.extras = extras
