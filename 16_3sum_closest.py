def return_2dlist(my_list):
    new_list = []
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            for k in range(len(my_list)):
                if i == j or i == k or j == k:
                    continue
                new_list2 = [my_list[i], my_list[j], my_list[k]]
                new_list.append(new_list2)
    return new_list


def unique_2dlist(my_list):
    unique_list = []
    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


def add_values_in_list(my_list):
    sum_list = []
    for i in my_list:
        sum_list.append(sum(i))
    return sum_list


def small_difference(my_list, target):
    difference_dictionary = {}
    difference_list = []
    for i in my_list:
        my_difference = i - target
        difference_dictionary[i] = abs(my_difference)
        # difference_list.append(abs(my_difference))
    return min(difference_dictionary, key=difference_dictionary.get)


def main():
    list1 = [-1, 2, 1, -4]
    list2 = [0, 0, 0]
    list3 = [1, -1, 3, -5, 0, 2]

    target = -11

    my_unique2d_list = unique_2dlist(return_2dlist(list3))
    sums_list = add_values_in_list(my_unique2d_list)
    print(small_difference(sums_list, target))


if __name__ == '__main__':
    main()
