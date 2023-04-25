import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es',help="Choose browser language: es, fr, en, ru")

@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    browser = None
    s=Service('C:\\Users\\s.andreyuk\\python environments\\selenium_cource_hw\\chromedriver_win32\\chromedriver.exe')
    options = Options()
    if language_name == "es":
        options.add_experimental_option('prefs', {'intl.accept_languages': "es"})
        print("\nbrowser will start in espaniol...")
        browser = webdriver.Chrome(service=s, options=options)
    elif language_name == "fr":
        options.add_experimental_option('prefs', {'intl.accept_languages': "fr"})
        print("\nbrowser will start in french...")
        browser = webdriver.Chrome(service=s, options=options)
    elif language_name == "en":
        options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
        print("\nbrowser will start in english...")
        browser = webdriver.Chrome(service=s, options=options)
    elif language_name == "ru":
        options.add_experimental_option('prefs', {'intl.accept_languages': "ru"})
        print("\nbrowser will start in russian...")
        browser = webdriver.Chrome(service=s, options=options)
    else:
        raise pytest.UsageError("--language should be es, fr, en or ru")
    yield browser
    print("\nquit browser..")
    browser.quit()
