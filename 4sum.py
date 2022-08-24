def four_sums_list(nums, target):
    list1 = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                for l in range(len(nums)):
                    if i == j or i == k or i == l or j == k or j == l or k == l:
                        continue
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        list2 = [nums[i], nums[j], nums[k], nums[l]]
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
    nums = [1, 0, -1, 0, -2, 2]
    nums2 = [2, 2, 2, 2]
    print(four_sums_list(nums2, 8))


if __name__ == '__main__':
    main()
