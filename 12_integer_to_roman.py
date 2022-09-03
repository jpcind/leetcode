class Solution:
    def intToRoman(self, num: int) -> str:
        mylist = []

        if num // 1000 > 0:
            for i in range(num//1000):
                mylist.append("M")
                num = num - ((num // 1000) * 1000)
        if num // 900 > 0:
            for i in range(num//900):
                mylist.append("CM")
                num = num - ((num // 900) * 900)
        if num // 500 > 0:
            for i in range(num//500):
                mylist.append("D")
                num = num - ((num // 500) * 500)
        if num // 400 > 0:
            for i in range(num//400):
                mylist.append("CD")
                num = num - ((num // 400) * 400)
        if num // 100 > 0:
            for i in range(num//100):
                mylist.append("C")
                num = num - ((num // 100) * 100)
        if num // 90 > 0:
            for i in range(num//90):
                mylist.append("XC")
                num = num - ((num // 90) * 90)
        if num // 50 > 0:
            for i in range(num//50):
                mylist.append("L")
                num = num - ((num // 50) * 50)
        if num // 40 > 0:
            for i in range(num//40):
                mylist.append("XL")
                num = num - ((num//40)*40)
        if num // 10 > 0:
            for i in range(num//10):
                mylist.append("X")
                num = num - ((num // 10) * 10)
        if num // 9 > 0:
            for i in range(num//9):
                mylist.append("IX")
                num = num - ((num // 9) * 9)
        if num // 5 > 0:
            for i in range(num//5):
                mylist.append("V")
                num = num - ((num // 5) * 5)
        if num // 4 > 0:
            for i in range(num//4):
                mylist.append("IV")
                num = num - ((num // 4) * 4)
        if num // 1 > 0:
            for i in range(num//1):
                mylist.append("I")

        return(''.join(mylist))

def main():
    for i in range(1, 4000):
        print("{}: {}".format(i, int_to_roman(i)))

if __name__ == '__main__':
    main()
