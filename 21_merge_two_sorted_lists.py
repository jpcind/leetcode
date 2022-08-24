def mergeTwoLists(list1, list2):
    list3 = []
    for i in list1:
        list3.append(i)
    for i in list2:
        list3.append(i)
    list3.sort()
    return list3



print(mergeTwoLists([1,2,3],[1,3,4]))
