import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

class FlaskFormTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location =  os.getenv('CHROME_BIN')

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def tearDown(self):
        self.driver.quit()

    def test_form_submission(self):
        self.driver.get('http://127.0.0.1:5000/')
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.NAME, 'text')))
        text_input = self.driver.find_element(By.NAME, 'text')
        text_input.send_keys('Test text')
        submit_button = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
        submit_button.click()
        submitted_text = self.driver.find_element(By.XPATH, '//p').text
        self.assertEqual(submitted_text, 'You submitted: Test text')

if __name__ == '__main__':
    unittest.main()
