"""Fase 3 - Test con Page Object Model.

Con pytest:       pytest test_pom.py
Como script:      python test_pom.py
"""
from login_page import LoginPage
from utils import BASE_URL, capturar, crear_driver


def test_ejecucion_pom(driver):
    driver.get(BASE_URL)

    login = LoginPage(driver)  # instanciamos la página
    # Caso de uso: login fallido
    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()

    mensaje = login.obtener_error()
    print(f"Resultado de la prueba: {mensaje}")
    capturar(driver, "fase3_pom_login_fallido")
    assert "locked out" in mensaje


if __name__ == "__main__":
    d = crear_driver()
    try:
        test_ejecucion_pom(d)
    finally:
        d.quit()
