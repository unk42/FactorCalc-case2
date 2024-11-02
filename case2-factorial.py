import math
import sys
import time

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
    if (num >= 100000) and (num < 200000):
        print("Вычисление факториала больших чисел (свыше ста сотен тысяч) может занять некоторое время.")
        time.sleep(1)
        print("Введите 'yes' для продолжения: ")
        continue_calc = input()
        if continue_calc == 'yes':
            factorial = calculate_factorial(num)
            print(f"Факториал числа {num} равен {factorial}")
        else:
            print("Действие отменено. Завершение программы...")
    elif num >= 200000:
        print("Не рекомендуется вычислять факториал очень больших чисел (свыше двух сотен тысяч).")
        print("Возможно процесс вичисления займет много времени.")
        time.sleep(1)
        print("Введите 'yes' для продолжения: ")
        continue_calc = input()
        if continue_calc == 'yes':
            factorial = calculate_factorial(num)
            print(f"Факториал числа {num} равен {factorial}")
        else:
            print("Действие отменено. Завершение программы...")
    elif num == 1 or num == 2:
        print(f"Факториал числа {num} будет равен {num}. Вычисление не требуется.")
    else:
        factorial = calculate_factorial(num)
        print(f"Факториал числа {num} равен {factorial}")

if __name__ == "__main__":
    main()
