def phone_dict():
    phone_dictionary = {'2': ['a', 'b', 'c'],
                        '3': ['d', 'e', 'f'],
                        '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'],
                        '6': ['m', 'n', 'o'],
                        '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'],
                        '9': ['w', 'x', 'y', 'z'],
                        }
    return phone_dictionary


def digits(str_of_numbers) -> list:
    phone_dictionary = phone_dict()
    list_of_dictionary_values = []
    list_of_numbers = list(str_of_numbers)
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] == '2':
            list_of_dictionary_values.append(phone_dictionary['2'])
        if list_of_numbers[i] == '3':
            list_of_dictionary_values.append(phone_dictionary['3'])
        if list_of_numbers[i] == '4':
            list_of_dictionary_values.append(phone_dictionary['4'])
        if list_of_numbers[i] == '5':
            list_of_dictionary_values.append(phone_dictionary['5'])
        if list_of_numbers[i] == '6':
            list_of_dictionary_values.append(phone_dictionary['6'])
        if list_of_numbers[i] == '7':
            list_of_dictionary_values.append(phone_dictionary['7'])
        if list_of_numbers[i] == '8':
            list_of_dictionary_values.append(phone_dictionary['8'])
        if list_of_numbers[i] == '9':
            list_of_dictionary_values.append(phone_dictionary['9'])
    return list_of_dictionary_values


def main():
    x = "864"
    my_list = []
    for i in range(len(digits(x)[0])):
        for j in range(len(digits(x)[1])):
            for k in range(len(digits(x)[2])):
                my_list2 = [digits(x)[0][i],
                            digits(x)[1][j],
                            digits(x)[2][k]]
                my_list.append(my_list2)
    for i in range(1, len(my_list)):
        my_list[i] = ''.join(my_list[i])
        print("{}: \"{}\"".format(i, my_list[i]))



if __name__ == '__main__':
    main()
