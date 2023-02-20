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

class TestTestauth():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testauth(self):
    self.driver.get("http://test.qahunter.ru/")
    self.driver.set_window_size(1440, 806)
    self.driver.find_element(By.LINK_TEXT, "Войти").click()
    self.driver.find_element(By.LINK_TEXT, "Войти").click()
    self.driver.find_element(By.ID, "formInput#text").click()
    self.driver.find_element(By.ID, "formInput#text").send_keys("ev.nalivayko2")
    self.driver.find_element(By.ID, "formInput#passowrd").click()
    self.driver.find_element(By.ID, "formInput#passowrd").send_keys("azsxdc!2")
    self.driver.find_element(By.CSS_SELECTOR, ".btn--lg").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".dev__name").text == "Евгений"
    assert self.driver.find_element(By.LINK_TEXT, "Курсы").text == "Курсы"
    self.driver.find_element(By.LINK_TEXT, "Выйти").click()

