from datetime import datetime
import pytz
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
driver.get("https://us.prairielearn.com/pl/login")
time.sleep(1)
driver.find_element("link text", "University of Illinois at Urbana-Champaign (UIUC)").click()
time.sleep(1)
driver.find_element("name", "loginfmt").send_keys("dodich3@illinois.edu")
time.sleep(1)
driver.find_element("id", "idSIButton9").click()
time.sleep(1)
driver.find_element("name", "passwd").send_keys("xBnb4mti?4mti")
driver.find_element("id", "idSIButton9").click()
time.sleep(1)

html = driver.page_source
parsed_html = BeautifulSoup(html, 'html.parser')
tds = parsed_html.find_all('td')
index = -1
for td in tds:
    link = td.find('a')
    if link:
        index = index + 2
        text = link.text.strip()
        scriptTxt3 = """
        var style = document.createElement('style');
        style.innerHTML = '.new-row td { padding-left: 20px; font-size: 75%; }';
        document.head.appendChild(style);
        """
        scriptTxt = f"""
                var table = document.querySelector('.table.table-sm.table-hover.table-striped tbody');
                var row = table.insertRow({index});
                var cell = row.insertCell(0);
                var ul = document.createElement('ul');
                var li1 = document.createElement('li');
                li1.textContent = '{text}';
                ul.appendChild(li1);
                cell.appendChild(ul);
                row.classList.add('new-row');
                """
        driver.execute_script(scriptTxt)
        driver.execute_script(scriptTxt3)




time.sleep(60)
