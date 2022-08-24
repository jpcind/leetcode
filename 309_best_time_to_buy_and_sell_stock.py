def stock(prices):
    my_list = []
    for i in range(len(prices)):
        for j in range(len(prices)):
            if j <= i or prices[i] > prices[j]:
                continue
            my_list.append(prices[j] - prices[i])
    if not my_list:
        return 0
    return max(my_list)




def main():
    my_prices = [7, 1, 5, 3, 6, 4]
    my_prices2 = [4, 11, 12, 8, 2, 9, 1, 4, 10]
    my_prices3 = [7, 6, 4, 3, 1]
    my_prices4 = [7, 4, 5, 3, 6, 8, 9,5, 2, 4, 1, 21, 13, 6, 4, 7, 5]
    print(stock(my_prices4))

main()
