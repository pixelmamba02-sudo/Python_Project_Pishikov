def check_palindrome():
    print("--- Задание 1: Палиндром ---")
    while True:
        number = input("Введите четырёхзначное число: ")
        if not number.isdigit() or len(number) != 4:
            print("Ошибка: нужно ввести ровно четыре цифры.")
            continue

        if number == number[::-1]:
            print("Истина: число читается одинаково.")
        else:
            print("Ложь: число не палиндром.")
        break


def check_rook_move():
    print("\n--- Задание 2: Ход ладьи ---")
    while True:
        try:
            x1 = int(input("Введите x1 (1-8): "))
            y1 = int(input("Введите y1 (1-8): "))
            x2 = int(input("Введите x2 (1-8): "))
            y2 = int(input("Введите y2 (1-8): "))

            if not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
                print("Ошибка: координаты от 1 до 8.")
                continue

            if x1 == x2 or y1 == y2:
                print("Истина: ладья может так сходить.")
            else:
                print("Ложь: ладья так не ходит.")
            break

        except ValueError:
            print("Ошибка: вводите только целые числа.")


if __name__ == "__main__":
    check_palindrome()
    check_rook_move()