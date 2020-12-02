from itertools import islice

YEAR = 2020
with open('day1_input.txt', 'r') as f:
    EXPENSE_REPORT = [int(x) for x in f.readlines()]


def two_sum_year(nums, year):
    seen = set()
    for a in nums:
        b = year - a
        if b in seen:
            return a * b
        seen.add(a)

def three_sum_year(nums, year):
    for i, a in enumerate(nums):
        result = two_sum_year(islice(nums, i+1, len(nums)), year-a)
        if result:
            return result*a


if __name__ == '__main__':
    print(two_sum_year(EXPENSE_REPORT, 2020))
    print(three_sum_year(EXPENSE_REPORT, 2020))
