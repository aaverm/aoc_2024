import itertools


def parse_file(file_path):
    test_values, numbers = [], []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        value, nums = line.split(':')
        test_values.append(int(value))
        numbers.append([int(x) for x in nums.split() if x])

    return test_values, numbers

def generate_operator_permutations_p1(num_operators):
    operators = ['+', '*']
    return itertools.product(operators, repeat=num_operators)


def evaluate_operations_p1(nums, ops):
    result = nums[0]
    for num, op in zip(nums[1:], ops):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
    return result

def generate_operator_permutations_p2(num_operators):
    operators = ['+', '*', '||']
    return itertools.product(operators, repeat=num_operators)


def evaluate_operations_p2(nums, ops):
    result = nums[0]
    for num, op in zip(nums[1:], ops):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif op == '||':
            result = int(str(result) + str(num))
    return result

def find_valid_test_values_p1(numbers, test_values):
    valid_values = []

    for i, nums in enumerate(numbers):
        test_value = test_values[i]
        num_operators = len(nums) - 1
        operator_permutations = generate_operator_permutations_p1(num_operators)

        for ops in operator_permutations:
            result = evaluate_operations_p1(nums, ops)
            if result == test_value:
                valid_values.append(test_value)
                break

    return valid_values


def find_valid_test_values_p2(numbers, test_values):
    valid_values = []

    for i, nums in enumerate(numbers):
        test_value = test_values[i]
        num_operators = len(nums) - 1
        operator_permutations = generate_operator_permutations_p2(num_operators)

        for ops in operator_permutations:
            result = evaluate_operations_p2(nums, ops)
            if result == test_value:
                valid_values.append(test_value)
                break 

    return valid_values


if __name__ == "__main__":
    input_file = "input.txt"
    test_values, numbers = parse_file(input_file)
    valid_values_p1 = find_valid_test_values_p1(numbers, test_values)
    valid_values_p2 = find_valid_test_values_p2(numbers, test_values)
    print(sum(valid_values_p1), sum(valid_values_p2))