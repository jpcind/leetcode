def majority_element(nums_list):
    my_dict = {}
    for i in range(len(nums_list)-1):
        my_dict[nums_list[i]] = nums_list.count(nums_list[i])
    print(my_dict)
    my_key = list(my_dict.keys())
    my_values = list(my_dict.values())
    maj_ele = my_key[my_values.index(max(my_values))]
    return maj_ele
