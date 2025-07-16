def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if n == 0:
        return "zero"
    
    result = []
    
    if n >= 1000:
        result.append(ones[n // 1000] + " thousand")
        n %= 1000
    
    if n >= 100:
        result.append(ones[n // 100] + " hundred")
        n %= 100
    
    if n >= 20:
        result.append(tens[n // 10])
        n %= 10
    
    if n >= 10:
        result.append(teens[n - 10])
        n = 0
    
    if n > 0:
        result.append(ones[n])
    
    return " ".join(result)

T = int(input())
for _ in range(T):
    N = int(input())
    print(number_to_words(N))


"""
class Solution(object):
    def numberToWords(self, num):
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if num == 0:
            return "Zero"

        result = []

        if num >= 1000000000:
            result.append(self.numberToWords(num // 1000000000) + " Billion")
            num %= 1000000000

        if num >= 1000000:
            result.append(self.numberToWords(num // 1000000) + " Million")
            num %= 1000000

        if num >= 1000:
            result.append(self.numberToWords(num // 1000) + " Thousand")
            num %= 1000

        if num >= 100:
            result.append(ones[num // 100] + " Hundred")
            num %= 100

        if num >= 20:
            result.append(tens[num // 10])
            num %= 10
    
        if num >= 10:
            result.append(teens[num - 10])
            num = 0

        if num > 0:
            result.append(ones[num])

        return " ".join(result)
"""
