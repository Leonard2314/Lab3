import employee_info as info
def test_get_employee_by_age_range():
    result=info.get_employees_by_age_range(22,24)
    assert result==[{"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]

def test_calculate_average_salary():
    for x in info.employee_data:
        if x["salary"]<=65000:
            x["salary"]=0
    average=11666.7
    assert average==round(info.calculate_average_salary(),1)

def test_get_employee_by_dept():
    depart="Marketing"
    users=["Jane","Mary"]
    assert users==info.get_employees_by_dept(depart)