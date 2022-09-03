class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        my_arr = []
        num = 1
        for i in range(1,n+1):
            if i % 15 == 0:
                my_arr.append("FizzBuzz")
                num += 1
                continue
            elif i % 3 == 0:
                my_arr.append("Fizz")
                num += 1
                continue
            elif i % 5 == 0:
                my_arr.append("Buzz")
                num += 1
                continue

            my_arr.append(str(num))
            num += 1
        return my_arr
