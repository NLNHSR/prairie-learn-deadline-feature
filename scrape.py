from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
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
links = []
for td in tds:
    link = td.find('a')
    print(link)
    if link:
        text = link.text.strip()
        href = link.get('href')
        links.append((href, text.split(":")))

# Print the list of hrefs
#print(links)
courses = {}
def course_deadlines(parsed_html, course_name):
    assignments = []
    html = driver.page_source
    parsed_html = BeautifulSoup(html, 'html.parser')
    assessments = parsed_html.find_all('tr')
    for assessment in assessments:
        # extract link and name
        link_tag = assessment.find('a', href=True)
        if link_tag is None:
            continue  # Skip assessments without links
        link = link_tag['href']
        name = assessment.find('a').text.strip()

        # extract deadline table
        try:
            deadline_table = assessment.find('a', {'data-content': True})['data-content']
            deadline_table = BeautifulSoup(deadline_table, 'html.parser')
        except:
            continue

        # find most relevant deadline date
        deadline_rows = deadline_table.find_all('tr')[1:]
        most_relevant = None
        for row in deadline_rows:
            percentage = row.find_all('td')[0].text.strip()
            deadline_str = row.find_all('td')[2].text.strip()
            if deadline_str == '—' or deadline_str == '':
                continue
            if 'CST' in deadline_str:
                deadline_str = deadline_str.replace(' (CST)', '')
            elif 'CDT' in deadline_str:
                deadline_str = deadline_str.replace(' (CDT)', '')
            deadline = datetime.strptime(deadline_str[:-3], '%Y-%m-%d %H:%M:%S')
            #
            if deadline >= datetime.now():
                # check if this deadline is the most relevant so far
                if most_relevant is None or deadline < most_relevant:
                    most_relevant = deadline
                    most_relevant_percentage = percentage

        if most_relevant == "None" or most_relevant is None:
            most_relevant_percentage = "0%"
        assignment = {
            'course_name': course_name,
            'assignment_name': name,
            'link': "https://us.prairielearn.com" + link,
            'most_relevant_date': most_relevant,
            'most_relevant_percentage': most_relevant_percentage
        }
        assignments.append(assignment)
        #print(f'{course_name}: {name}: {link} (deadline: {most_relevant}), percentage: {most_relevant_percentage}')
    courses[course_name] = assignments
for link in links:
    url_to_get = "https://us.prairielearn.com" + link[0]
    driver.get(url_to_get)
    content = driver.find_elements(By.CLASS_NAME, "content")
    course_deadlines(parsed_html, link[1][0])

print(courses)

'''
#links[][] look like this:
[('/pl/course_instance/130633', ['CS 225', ' Data Structures and Algorithms, Spring 2023']), ('/pl/course_instance/130040', ['CS 361', ' P
robability and Statistics for Computer Science, Spring 2023']), ('/pl/course_instance/130110', ['MATH 257', ' Linear Algebra with Computat
ional Applications, MATH 257 - Spring 2023']), ('/pl/course_instance/130303', ['CS 233', ' Computer Architecture, Spring 2023'])]
'''

# my_variable = 'Test'
# script = """
# body = document.getElementById('content');
# element = document.createElement('div');
# text = document.createTextNode('{}');
# element.appendChild(text);
# body.append(element);
# """.format(my_variable)
# driver.get("https://us.prairielearn.com")
# driver.execute_script(script)
# driver.execute_script(script)
time.sleep(30)