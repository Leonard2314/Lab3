import employee_info as info
def test_get_employee_by_age_range():
    min_age=22
    max_age=33
    names=["John","Jane","Mary","Mike"]
    results=info.get_employees_by_age_range(min_age,max_age)
    assert results==names

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