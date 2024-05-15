import price_info as info

def test_cost_of_fruits():
    result=8.4
    answer=info.cost_of_fruits('orange',6)
    assert(round(answer,1)==result)

def test_total_cost_shopping():
    print(dict.values(info.price_list))
    info.price_list["orange"] = 2
    print(dict.values(info.price_list))
    print(dict.values(info.quantity_list))
    info.quantity_list["orange"] = 10
    print(dict.values(info.quantity_list))
    result = []
    result = info.total_cost_shopping()
    assert(result==59.75)