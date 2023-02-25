from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://us.prairielearn.com/pl/login")
time.sleep(2)
driver.find_element("link text", "University of Illinois at Urbana-Champaign (UIUC)").click()
time.sleep(2)
get_url = driver.current_url
driver.get(get_url)
time.sleep(2)
driver.find_element("name", "loginfmt").send_keys("neel4@illinois.edu")
time.sleep(2)
driver.find_element("id", "idSIButton9").click()
time.sleep(2)
driver.find_element("name", "passwd").send_keys("EagleSky4032")
driver.find_element("id", "idSIButton9").click()
time.sleep(2)
driver.get("https://us.prairielearn.com/pl/course_instance/130110/assessments")
content = driver.find_elements(By.CLASS_NAME, "content")
html = driver.page_source
parsed_html = BeautifulSoup(html, 'html.parser')
table = parsed_html.find("table")
rows = table.find_all("tr")
for row in rows:
    cells = row.find_all("td")
    for cell in cells:
        print(cell.text.strip())
driver.quit()
