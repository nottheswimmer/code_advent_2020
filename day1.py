YEAR = 2020
with open('day1_input.txt', 'r') as f:
    EXPENSE_REPORT = [int(x) for x in f.readlines()]


def sum_year(nums, year):
    seen = set()
    for a in nums:
        b = year - a
        if b in seen:
            return a * b
        seen.add(a)


if __name__ == '__main__':
    print(sum_year(EXPENSE_REPORT, 2020))
