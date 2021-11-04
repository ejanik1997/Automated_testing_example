import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestSearch():
    search_words = ('whey protein isolate',
                    'creatine monohydrate',
                    'vitamin D')
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe")
        self.driver.implicitly_wait(5)

        self.driver.get('https://allegro.pl/')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[8]/div/div/div/div/div[2]/div[2]/button[1]').click()

    @pytest.mark.parametrize('search_query', search_words)
    def test_search(self, search_query):
        search = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/header/div/div/div[1]/div/form/input')
        search.send_keys(search_query, Keys.ENTER)
        expected = search_query
        result = self.driver.find_element(By.XPATH,
                                     '/html/body/div[2]/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div/h1').text
        assert expected == result, f'Error, expected: ' + expected + ', while result is: ' + result

    def teardown_method(self):
        self.driver.quit()
