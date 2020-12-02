with open('day2_input.txt', 'r') as f:
    POLICY_TO_PASSWORDS = tuple(x.strip().split(": ") for x in f.readlines())


def count_valid(policy_to_passwords):
    valid = 0
    for policy, password in policy_to_passwords:
        valid += is_valid(password, policy)
    return valid


def is_valid(password, policy):
    _range, char = policy.split()
    a, b = _range.split('-')
    return password.count(char) in range(int(a), int(b)+1)


if __name__ == '__main__':
    print(count_valid(POLICY_TO_PASSWORDS))
