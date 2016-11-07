Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

class Solution(object):
    def fizzBuzz(self, n):
        def fb(n):
            if not n%3:
                if not n%5:
                    return "FizzBuzz"
                return "Fizz"
            elif not n%5:
                return "Buzz"
            return str(n)

        return [fb(x) for x in range(1,n+1)]