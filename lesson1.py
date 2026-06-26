# Ожидание заполнения шкалы до 75%

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 60, 0.25)

text_to_be = "75"

driver.get("http://uitestingplayground.com/progressbar")

driver.find_element(By.CSS_SELECTOR, "#startButton").click()

waiter.until(
    EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, "#progressBar"), "aria-valuenow", text_to_be)
)

driver.find_element(By.CSS_SELECTOR, "#stopButton").click()

driver.quit()