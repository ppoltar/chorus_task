import pytest, logging, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="class")
def chrome_driver(request):
    logging.info("Setting up driver for test chorus site.")
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    logging.info("Closing the window of the chorus site.")
    chrome_driver.close()

@pytest.fixture(scope="class")
def title_name():
    title_name = {
        "login_page" : "Chorus",
        "test_page"  :'Chorus.ai'
    }
    return title_name

@pytest.fixture(scope="class")
def url_path():
    url_path = {
        "login_page" : "https://hello.chorus.ai/login?next=http:%2F%2Fchorus.ai%2Fmeeting%2F3519739%3Ftab%3Dsummary%26call%3D07373DE47C6246A1B39F62311C156162",
        "test_page"  : "https://chorus.ai/meeting/3519739?tab=summary&call=07373DE47C6246A1B39F62311C156162"
    }
    return url_path

@pytest.fixture(scope="class")
def certification():
    certification = {
        "Username": "barashek11@chorus-auto.com",
        "Password": "qmZGj267Sy!"

    }
    return certification

