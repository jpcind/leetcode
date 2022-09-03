class Solution:
    # def isPalindrome(self, x: int) -> bool:
    def isPalindrome(self, x):
        x = str(x)

        x = list(x)
        number2 = x[::-1]
        if x == number2:
            return True
        return False


def main():
    x = 12321
    y = 39984
    my_sol = Solution()
    print(my_sol.isPalindrome(x))
    print(my_sol.isPalindrome(y))

main()
