# Parcial #2 - Pruebas funcionales con Selenium (Sauce Demo)

Requisitos: Python 3.9+ y Google Chrome. Selenium Manager descarga el chromedriver solo.

```
pip install -r requirements.txt
```

| Fase | Comando (desde esta carpeta) | Resultado |
|---|---|---|
| 1. Básica | `python test_practico.py` | `evidencias/fase1_*.png` |
| 2. Esperas explícitas | `python robust_test.py` | `evidencias/fase2_*.png` |
| 3. POM | `python test_pom.py` | `evidencias/fase3_*.png` |
| 4. Reporte HTML | `pytest --html=reporte_pruebas.html --self-contained-html` | `reporte_pruebas.html` |
| 5. Captura en fallos | `pytest demo_fallo/test_fallo.py --html=reporte_fallos.html --self-contained-html` | `reporte_fallos.html` (falla a propósito) |
| 6. CI/CD | `git push` a GitHub y revisar la pestaña Actions | artifact `reporte-selenium` |

Variables de entorno opcionales: `HEADLESS=1` (sin ventana), `SAUCE_URL` (URL base, por defecto https://www.saucedemo.com), `CHROMEDRIVER_PATH`.

Correcciones respecto al documento original:
- `By.DATA_TEST` no existe en Selenium: se usa `By.CSS_SELECTOR, "[data-test='error']"`.
- `conftest.py` importa `pytest_html` y usa la API de pytest-html 4 (`report.extras`, `extras.png`).
- La fixture `driver` vive solo en `conftest.py` (antes estaba duplicada).
- El workflow usa `checkout@v4`, `setup-python@v5`, `upload-artifact@v4` y activa `HEADLESS=1`.
