
def make_script(course_name, index):
    assignments = courses[course_name]
    script_text = """
                    var table = document.querySelector('.table.table-sm.table-hover.table-striped tbody');
                    var rows = table.querySelectorAll('tr');
                """
    assignment_list = ""
    for assignment in assignments:
        assignment_list += f"<li>{assignment['assignment_name']}</li>"
    script_text += f"""
                            var row = table.insertRow({index}.insertCell(0);
                            cell.textConte);
                            var cell = rownt = '{course_name}';
                            var ul = document.createElement('ul');
                            ul.innerHTML = '{assignment_list}';
                            cell.appendChild(ul);
                            row.classList.add('new-row');
                        """
    index += 1
    script_text2 = """
                    var style = document.createElement('style');
                    style.innerHTML = '.new-row td { padding-left: 20px; font-size: 75%; }';
                    document.head.appendChild(style);
                """
    driver.execute_script(script_text)
    driver.execute_script(script_text2)



'''
#links[][] look like this:
[('/pl/course_instance/130633', ['CS 225', ' Data Structures and Algorithms, Spring 2023']), ('/pl/course_instance/130040', ['CS 361', ' P
robability and Statistics for Computer Science, Spring 2023']), ('/pl/course_instance/130110', ['MATH 257', ' Linear Algebra with Computat
ional Applications, MATH 257 - Spring 2023']), ('/pl/course_instance/130303', ['CS 233', ' Computer Architecture, Spring 2023'])]
'''
driver.get("https://us.prairielearn.com")
html = driver.page_source
parsed_html = BeautifulSoup(html, 'html.parser')
tds = parsed_html.find_all('td')
index = -1
for td in tds:
    link = td.find('a')
    if link:
        index = index + 2
        text = link.text.strip()
        text = (text.split(":"))[0]
        make_script(text, index)
