# Lab14
def check_truth(a, b, c):
    return (a and b) or c
Опис:
Ця функція повертає логічне значення, що визначається виразом (a and b) or c. Якщо a і b обидва True або хоча б одне з них True, то результат буде True. Якщо обидва a і b False, то результат залежить від значення c.

Функція logical_equivalence

def logical_equivalence(a, b):
    return a == b
Опис:
Ця функція перевіряє, чи є два вхідних значення a і b логічно еквівалентними, повертаючи True, якщо вони однакові, і False в іншому випадку.

Функція xor

def xor(a, b):
    return (a or b) and not (a and b)
Опис:
Ця функція реалізує логічну операцію XOR (виключне АБО). Вона повертає True, якщо один з аргументів a або b є True, але не обидва одночасно.

Функція greet

def greet(value):
    return "Hello, World!" if value else "Goodbye, World!"
Опис:
Ця функція повертає рядок з привітанням залежно від вхідного значення value. Якщо value є True, то повертається "Hello, World!", в іншому випадку повертається "Goodbye, World!".

Функція nested_condition

def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y != z != x:
        return "All different"
    else:
        return "Neither"
Опис:
Ця функція перевіряє три числа x, y і z на рівність між собою. Якщо всі три числа рівні, повертається "All same". Якщо всі три числа різні одне від одного, повертається "All different". В іншому випадку повертається "Neither".

Функція count_true

def count_true(bool_list):
    return sum(bool_list)
Опис:
Ця функція рахує кількість значень True у списку bool_list, використовуючи вбудовану функцію sum(), яка конвертує кожен True у 1 і потім сумує ці значення.

Функція parity

def parity(num):
    binary = bin(num)
    ones_count = binary.count('1')
    return ones_count % 2 == 0
Опис:
Ця функція перевіряє парність числа num в двійковому представленні. Вона конвертує число у двійкову форму за допомогою bin(num), після чого рахує кількість одиниць (у бінарному представленні) і перевіряє, чи це число парне (повертає True), якщо кількість одиниць парна, інакше повертає False.

Функція majority_vote

def majority_vote(a, b, c):
    return sum([a, b, c]) > 1
Опис:
Ця функція перевіряє, чи є більше одного True серед вхідних аргументів a, b, c. Якщо два або більше з них є True, то результат буде True, інакше - False.

Функція switch

def switch(value):
    return not value
Опис:
Ця функція виконує інверсію логічного значення value. Якщо value є True, то повертається False, і навпаки.

Функція ternary_check

def ternary_check(condition, if_true, if_false):
    return if_true if condition else if_false
Опис:
Ця функція реалізує тернарний оператор в Python. Якщо condition є True, то повертається if_true, в іншому випадку повертається if_false.

Функція validate

def validate(x, y, z):
    return x or (y and z)
Опис:
Ця функція перевіряє умову, використовуючи логічний оператор or і and. Повертає True, якщо x або обидва y і z є True.

Функція chain_check

def chain_check(x, y, z):
    if x < y < z:
        return "Increasing"
    elif x > y > z:
        return "Decreasing"
    else:
        return "Neither"
Опис:
Ця функція перевіряє послідовність чисел x, y і z. Якщо вони зростають послідовно (x < y < z), повертає "Increasing". Якщо вони спадають послідовно (x > y > z), повертає "Decreasing". Якщо ні одне з цих умов не виконується, повертає "Neither".

Функція filter_true

def filter_true(bool_list):
    return [item for item in bool_list if item]
Опис:
Ця функція фільтрує список bool_list, залишаючи лише значення True. Використовується спискове включення для створення нового списку, що містить тільки елементи, які є True.

Функція multiplexer

def multiplexer(a, b, c, num):
    if a:
        return num * 2
    elif b:
        return num * 3
    elif c:
        return num - 5
    else:
        return num
Опис:
Ця функція реалізує логіку мультиплексора, вибираючи операцію в залежності від значень a, b і c. Якщо a є True, повертає num * 2. Якщо b є True, повертає num * 3. Якщо c є True, поверта








