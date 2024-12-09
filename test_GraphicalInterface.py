"""from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_options = Options()
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/NASA")

element1 = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/a/img')
print(element1.value_of_css_property("width") == "160px")
print(element1.value_of_css_property("height") == "160px")

element2 = driver.find_element(By.XPATH, '/html/body')
print(element2.value_of_css_property("color") == "#000000")

element3 = driver.find_element(By.CLASS_NAME, "wikitable")
print(element3.value_of_css_property("box-sizing") == "border-box")

element4 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/nav")
print(element3.value_of_css_property("font-family") == "sans-serif")
print(element3.value_of_css_property("box-sizing") == "12.6px")

time.sleep(5)"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Fixture - WebDriver yaradılması və bağlanması
@pytest.fixture
def driver():
    chrome_options = Options()
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver  # Testdən sonra bağlanacaq
    driver.quit()

# Test 1: Logo ölçülərinin yoxlanılması
def test_logo_dimensions(driver):
    driver.get("https://en.wikipedia.org/wiki/NASA")
    element1 = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/a/img')
    assert element1.value_of_css_property("width") == "160px", "Logo genişliyi səhvdir"
    assert element1.value_of_css_property("height") == "160px", "Logo hündürlüyü səhvdir"

# Test 2: Səhifə rənginin yoxlanılması
def test_page_color(driver):
    driver.get("https://en.wikipedia.org/wiki/NASA")
    element2 = driver.find_element(By.XPATH, '/html/body')
    assert print(element2.value_of_css_property("color") == "#000000")
    

# Test 3: Cədvəl CSS xüsusiyyətinin yoxlanılması
def test_table_css(driver):
    driver.get("https://en.wikipedia.org/wiki/NASA")
    element3 = driver.find_element(By.CLASS_NAME, "wikitable")
    assert element3.value_of_css_property("box-sizing") == "border-box"

# Test 4: Font xassələrinin yoxlanılması
def test_font_family(driver):
    driver.get("https://en.wikipedia.org/wiki/NASA")
    element4 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/nav")
    assert element4.value_of_css_property("font-family") == "sans-serif"
    #assert element4.value_of_css_property("box-sizing") == "12.6px"

#python -m pytest --html=report.html