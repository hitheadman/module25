import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome()
   # Переходим на страницу авторизации
   driver.get('https://petfriends.skillfactory.ru/login')

   yield driver

   driver.quit()

def test_all_pets(driver):
   # Вводим email
   driver.find_element(By.ID, 'email').send_keys('hitheadman@mail.ru')
   # Вводим пароль
   driver.find_element(By.ID, 'pass').send_keys('EvhbCerf3Hfpf')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   driver.implicitly_wait(5)
   driver.get('https://petfriends.skillfactory.ru/all_pets')
   names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i].text
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
def test_my_pets(driver):
   # Вводим email
   driver.find_element(By.ID, 'email').send_keys('hitheadman@mail.ru')
   # Вводим пароль
   driver.find_element(By.ID, 'pass').send_keys('EvhbCerf3Hfpf')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   driver.get('https://petfriends.skillfactory.ru/my_pets')
   driver.implicitly_wait(5)
   number_of_pets = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
   number_of_pets = len(number_of_pets)
   WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
   number = driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
   num = number[0].text.split('\n')
   num = num[1].split(' ')
   num = int(num[1])
   assert  number_of_pets == num

