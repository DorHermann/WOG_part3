from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_scores_service(url):
    driver_chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver_chrome.get(url)

    score = driver_chrome.find_element(By.XPATH, "/html/body/div").text
    # print(score)
    # Close the browser window
    driver_chrome.quit()

    if not score.isdigit():
        return False

    if 1 <= int(score) <= 1000:
        return True
    else:
        return False


def main_function():
    if not test_scores_service(r'http://127.0.0.1:5000/score'):
        exit(-1)  # Tests failed
    exit()  # Tests passed
