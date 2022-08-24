def twoSum(nums, target):
    mylist = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                if i == j:
                    continue


            mylist2 = []
            if nums[i] + nums[j] == target:
                mylist2.append(i)
                mylist2.append(j)
                mylist.append(mylist2)
                # print("Index of {} is at {}".format(nums[i], i))
                # print("Index of {} is at {}".format(nums[j], j))
    return mylist


myl = [5, 3, 6, 4, 4, 2, 1, 7]
two_d_list = twoSum(myl, 8)

for i in two_d_list:
    print(i)
