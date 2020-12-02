with open('day2_input.txt', 'r') as f:
    POLICY_TO_PASSWORDS = tuple(x.strip().split(": ") for x in f.readlines())


def count_valid(policy_to_passwords, validator):
    valid = 0
    for policy, password in policy_to_passwords:
        valid += validator(password, policy)
    return valid


def validator_1(password, policy):
    _range, char = policy.split()
    a, b = _range.split('-')
    return password.count(char) in range(int(a), int(b)+1)

def validator_2(password, policy):
    pos, char = policy.split()
    a, b = pos.split('-')
    try:
        return (password[int(a)-1] == char) ^ (password[int(b)-1] == char)
    except IndexError:
        return False

if __name__ == '__main__':
    print(count_valid(POLICY_TO_PASSWORDS, validator=validator_1))
    print(count_valid(POLICY_TO_PASSWORDS, validator=validator_2))
