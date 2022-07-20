class Solution:
    def __init__(self):
        pass

    def rom_to_int(self, roman_num:str):
        rom_num_list = list(roman_num)
        int_list = []
        for i in range(len(rom_num_list)):
            if rom_num_list[i] == "I":
                int_list.append(1)
            elif rom_num_list[i] == "V":
                if rom_num_list[i-1] == "I":
                    if i-1 == -1:
                        int_list.append(5)
                    else:
                        int_list.append(3)
                else:
                    int_list.append(5)
            elif rom_num_list[i] == "X":
                if rom_num_list[i-1] == "I":
                    if i-1 == -1:
                        int_list.append(10)
                    else:
                        int_list.append(8)
                else:
                    int_list.append(10)
            elif rom_num_list[i] == "L":
                if rom_num_list[i-1] == "X":
                    if i-1 == -1:
                        int_list.append(50)
                    else:
                        int_list.append(30)
                else:
                    int_list.append(50)
            elif rom_num_list[i] == "C":
                if rom_num_list[i-1] == "X":
                    if i-1 == -1:
                        int_list.append(100)
                    else:
                        int_list.append(80)
                else:
                    int_list.append(100)
            elif rom_num_list[i] == "D":
                if rom_num_list[i-1] == "C":
                    if i-1 == -1:
                        int_list.append(500)
                    else:
                        int_list.append(300)
                else:
                    int_list.append(500)
            elif rom_num_list[i] == "M":
                if rom_num_list[i-1] == "C":
                    if i-1 == -1:
                        int_list.append(1000)
                    else:
                        int_list.append(800)
                else:
                    int_list.append(1000)
            else:
                return "Invalid"
        return sum(int_list)


def main():
    x = Solution()
    s = "".upper()

    print(x.rom_to_int(s))

if __name__ == '__main__':
    main()
