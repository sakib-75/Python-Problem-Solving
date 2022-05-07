def all_equal(list_):
    first_element = list_[0]
    check = True
    for element in list_:
        if first_element != element:
            check = False
            break
    return check


print(all_equal([1, 1, 1]))
