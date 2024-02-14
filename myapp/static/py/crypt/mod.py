a = (16 * 19) % 18
б = (12 * 30) % 9
в = (3 * 5 * 36) % 7
г = 3 ** 15 % 10
д = 4 ** 10 % 14
е = (25 * 6) % 8
ж = (5 ** 6) ** 2 % 15

print('а) ' ' (16 * 19) % 18 =', (16 * 19), '% 18' ' = ', a)
print('б) ' ' (12 * 30) % 9 =', (12 * 30), '% 9'' = ', б)
print('в) ' ' (3 * 5 * 36) % 7 =', (3 * 5 * 36), '% 7'' = ', в)
print('г) ' ' 3**15 % 10 =', 3 ** 15, '% 10'' = ', г)
print('д) ' ' 4 ** 10 % 14 =', 4 ** 10, '% 14'' = ', д)
print('е) ' ' (25 * 6) % 8 =', (25 * 6), '% 8'' = ', е)
print('ж) ' ' (5 ** 6) ** 2 % 15 =', (5 ** 6) ** 2, '% 15'' = ', ж)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


pairs = [("а", 56, 15), ("б", 275, 198)]

for pair in pairs:
    label, x, y = pair

    gcd_result = gcd(x, y)

    print(f'{label}) НСД для ({x}, {y}):')
    print(f'   {x} = {x // gcd_result} * {gcd_result}')
    print(f'   {y} = {y // gcd_result} * {gcd_result}')
    print(f'   НСД = {gcd_result}')
    print()


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


num1 = 24
num2 = 45

lcm_result = lcm(num1, num2)
gcd_result = gcd(num1, num2)
print("НСК для чисел", num1, "і", num2, "дорівнює", lcm_result)
print("Обчислення НСК використовуючи НСД:")
print(f'   {num1} = {num1 // gcd_result} * {gcd_result}')
print(f'   {num2} = {num2 // gcd_result} * {gcd_result}')
print("   НСД(", num1, ",", num2, ") =", gcd(num1, num2))
print("   НСК(", num1, ",", num2, ") = (", num1, "*", num2, ") / НСД(", num1, ",", num2, ") =", lcm_result)
