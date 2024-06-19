def check_truth(a, b, c):
    return (a and b) or c

# Example usage:
print(check_truth(True, False, True))  # True

def logical_equivalence(a, b):
    return a == b

# Example usage:
print(logical_equivalence(True, True))  # True

def xor(a, b):
    return (a or b) and not (a and b)

# Example usage:
print(xor(True, False))  # True

def greet(value):
    return "Hello, World!" if value else "Goodbye, World!"

# Example usage:
print(greet(True))  # Hello, World!

def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y != z != x:
        return "All different"
    else:
        return "Neither"

# Example usage:
print(nested_condition(3, 3, 3))  # All same

def count_true(bool_list):
    return sum(bool_list)

# Example usage:
print(count_true([True, False, True, False, True]))  # 3

def parity(num):
    binary = bin(num)
    ones_count = binary.count('1')
    return ones_count % 2 == 0

# Example usage:
print(parity(3))  # False (binary 11)

def majority_vote(a, b, c):
    return sum([a, b, c]) > 1

# Example usage:
print(majority_vote(True, True, False))  # True

def switch(value):
    return not value

# Example usage:
print(switch(True))  # False

def ternary_check(condition, if_true, if_false):
    return if_true if condition else if_false

# Example usage:
print(ternary_check(True, "Yes", "No"))  # Yes

def validate(x, y, z):
    return x or (y and z)

# Example usage:
print(validate(True, False, True))  # True

def chain_check(x, y, z):
    if x < y < z:
        return "Increasing"
    elif x > y > z:
        return "Decreasing"
    else:
        return "Neither"

# Example usage:
print(chain_check(1, 2, 3))  # Increasing

def filter_true(bool_list):
    return [item for item in bool_list if item]

# Example usage:
print(filter_true([True, False, True, False]))  # [True, True]

def multiplexer(a, b, c, num):
    if a:
        return num * 2
    elif b:
        return num * 3
    elif c:
        return num - 5
    else:
        return num

# Example usage:
print(multiplexer(False, False, True, 10))  # 5
