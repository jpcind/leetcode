def most_water(my_list):
    max_value = 0
    if len(my_list) == 2:
        return min(my_list)
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if i == j:
                continue
            if my_list[i] <= my_list[j]:
                distance = abs(i - j)
                value = my_list[i] * distance
                if value > max_value:
                    max_value = value
    return max_value


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    anotherheight = [1, 8, 6, 2, 5, 4, 8, 3]
    height2 = [1, 1]
    height3 = [2, 4, 3, 5]
    height4 = [8]
    print(most_water(anotherheight))


if __name__ == '__main__':
    main()
