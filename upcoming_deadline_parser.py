# reducing to 4
parsed_courses = []
def get_objects_by_date(data):
    today = datetime.datetime.today().date()
    objects_with_same_date = []
    objects_with_closest_dates = []

    for course_name, assignments in data.items():
        for assignment in assignments:
            if assignment['most_relevant_date'] is not None:
                assignment_date = assignment['most_relevant_date'].date()
                diff = abs(today - assignment_date)

            if diff == datetime.timedelta(days=0):
                objects_with_same_date.append(assignment)
            else:
                objects_with_closest_dates.append((assignment, diff))

    objects_with_closest_dates.sort(key=lambda x: x[1])
    closest_objects = [x[0] for x in objects_with_closest_dates][:4]

    if objects_with_same_date:
        return objects_with_same_date
    else:
        return closest_objects

parsed_courses = get_objects_by_date(scrape.courses)

def make_script(course_name, index):
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

