def longest_com_pre(list_of_strings):
    list_of_common_letters = []
    # for i in list_of_strings[0]:
    #     for j in list_of_strings[1]:
    #         if i == j:
    #             list_of_common_letters.append(j)
    # return list_of_common_letters

    for i in range(len(list_of_strings[0])):
        if list_of_strings[0][i] == list_of_strings[1][i] == list_of_strings[2][i]:
            list_of_common_letters.append(list_of_strings[0][i])
        else:
            break
        return list_of_common_letters




def main():
    my_list = ["flower", "flow", "flight"]
    print(''.join(longest_com_pre(my_list)))




main()
