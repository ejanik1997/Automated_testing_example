from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe")
    driver.implicitly_wait(5)

    driver.get('https://allegro.pl/')
    driver.find_element(By.XPATH, '/html/body/div[2]/div[8]/div/div/div/div/div[2]/div[2]/button[1]').click()

    product = 'whey protein isolate'
    some_other_product = 'creatine monohydrate'
    search = driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/header/div/div/div[1]/div/form/input')
    search.send_keys(product, Keys.ENTER)

    result = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div/h1').text
    assert product == result, f'Error, expected: ' + product + ', while result should be: ' + result
    assert some_other_product == result, f'Error, expected: ' + product + ', while result should be: ' + result

    driver.quit()