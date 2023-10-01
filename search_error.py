from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

base_url = 'https://stackoverflow.com'
file_path = "answer.txt"

def search_error(error):
  search_query = 'python 3 ' + error

  driver.get(base_url)
  driver.fullscreen_window()

  form = driver.find_element(By.ID, value="search")
  input_search = form.find_element(By.TAG_NAME, value='input')
  input_search.send_keys(search_query)
  input_search.submit()

  consent_button = driver.find_element(By.CLASS_NAME, value='js-accept-cookies')
  consent_button.click()

  first_link = driver.find_element(By.CLASS_NAME, value='answer-hyperlink')
  first_link.click()

  accepted_answer_container = driver.find_element(By.XPATH, value='//div[@itemprop="acceptedAnswer"]')
  answer_cell = accepted_answer_container.find_element(By.CLASS_NAME, value='js-post-body')

  with open(file_path, "w") as file:
    file.write(answer_cell.text)

  driver.quit()