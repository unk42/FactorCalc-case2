import math
import sys

sys.set_int_max_str_digits(0)

def get_positive_integer():
    while True:
        try:
            num = int(input("Введите положительное целое число: "))
            if num <= 0:
                print("Ошибка: Введите положительное число.")
            else:
                return num
        except ValueError:
            print("Ошибка: Введите целое число.")

def calculate_factorial(n):
    return math.factorial(n)

def main():
    num = get_positive_integer()
    factorial = calculate_factorial(num)
    print(f"Факториал числа {num} равен {factorial}")

if __name__ == "__main__":
    main()