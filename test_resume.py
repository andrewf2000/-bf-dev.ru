import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestResume():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_resume(self):
    self.driver.get("http://test.qahunter.ru/")
    self.driver.set_window_size(1865, 1018)
    element = self.driver.find_element(By.LINK_TEXT, "Войти/зарегистрироваться")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "Войти/зарегистрироваться").click()
    self.driver.find_element(By.ID, "formInput#text").click()
    self.driver.find_element(By.ID, "formInput#text").send_keys("fandrew")
    self.driver.find_element(By.ID, "formInput#passowrd").click()
    self.driver.find_element(By.ID, "formInput#passowrd").send_keys("dthjybrf1")
    self.driver.find_element(By.CSS_SELECTOR, ".btn--lg").click()
    self.driver.find_element(By.LINK_TEXT, "Резюме").click()
    self.driver.find_element(By.ID, "formInput#search").click()
    self.driver.find_element(By.ID, "formInput#search").send_keys("fandrew")
    self.driver.find_element(By.CSS_SELECTOR, ".btn--lg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card__body").click()
    self.driver.find_element(By.LINK_TEXT, "Мой аккаунт").click()
    self.driver.find_element(By.LINK_TEXT, "Изменить данные").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn--lg").click()
    self.driver.find_element(By.LINK_TEXT, "Резюме").click()
    self.driver.find_element(By.ID, "formInput#search").click()
    self.driver.find_element(By.ID, "formInput#search").send_keys("fandrew")
    self.driver.find_element(By.CSS_SELECTOR, ".btn--lg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dev__meta > h3").click()
    self.driver.find_element(By.LINK_TEXT, "Выйти").click()
  
