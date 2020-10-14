from selenium import webdriver
import pytest
from time import sleep


@pytest.fixture(scope="class")
def setupBrowser(request):
    driver = webdriver.Chrome(executable_path='C://Users//Yago//Desktop//chromedriver.exe')
    driver.get('http://localhost:5000')
    request.cls.driver = driver