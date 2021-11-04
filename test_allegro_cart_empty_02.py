from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAllegroCartEmpty:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.get('https://allegro.pl/')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[8]/div/div/div/div/div[2]/div[2]/button[1]').click()

    def test_cart_empty(self):
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/header/div/nav/div[4]/div/div/a/div/img').click()
        result = self.driver.find_element(By.XPATH,
                                          '/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/h2/span').text
        expected = 'Twój koszyk jest pusty'
        assert result == expected, f'Error, expected: ' + expected + ', while result should is: ' + result

    def teardown_method(self):
        self.driver.quit()

