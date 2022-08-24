def three_sums_list(nums):
    list1 = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i == j or i == k or j == k:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    list2 = [nums[i], nums[j], nums[k]]
                    list2.sort()
                    list1.append(list2)
    list1 = unique(list1)
    return list1


def unique(my_list):
    unique_list = []
    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


def main():
    my_list = [-1, 0, 1, 2, -1, -4]
    my_list2 = [0, 0, 0]
    my_list3 = [4, 5, 6, 3, 2, 1, -1, -5, -7, -3]
    print("List of numbers that when added up equals 0:")
    for i in three_sums_list(my_list3):
        print(i)


if __name__ == '__main__':
    main()
