def runge_kutta_third_order(f, a, b, y0, h, n):
    x_values = [a + i * h for i in range(n + 1)]
    y_values = [0] * (n + 1)
    y_values[0] = y0

    for i in range(n):
        k1 = h * f(x_values[i], y_values[i])
        k2 = h * f(x_values[i] + h / 2, y_values[i] + k1 / 2)
        k3 = h * f(x_values[i] + h / 2, y_values[i] + k2 / 2)

        y_values[i + 1] = y_values[i] + (k1 + 2 * k2 + k3) / 6

    return x_values, y_values

def runge_kutta_fourth_order(f, a, b, y0, h, n):
    x_values = [a + i * h for i in range(n + 1)]
    y_values = [0] * (n + 1)
    y_values[0] = y0

    for i in range(n):
        k1 = h * f(x_values[i], y_values[i])
        k2 = h * f(x_values[i] + h / 2, y_values[i] + k1 / 2)
        k3 = h * f(x_values[i] + h / 2, y_values[i] + k2 / 2)
        k4 = h * f(x_values[i] + h, y_values[i] + k3)

        y_values[i + 1] = y_values[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return x_values, y_values

def main():
    print("Wybierz postać funkcji:")
    print("1. F(x, y) = a · x + b · y")
    print("2. F(x, y) = a · x − b · y")
    print("3. F(x, y) = a · x · b · y")
    print("4. F(x, y) = a·x/b·y")

    choice = int(input("Podaj numer wybranej funkcji (1-4): "))

    if choice not in range(1, 5):
        print("Niepoprawny numer funkcji.")
        return

    a = float(input("Podaj wartość stałej a (różna od zera): "))
    b = float(input("Podaj wartość stałej b (różna od zera): "))

    if choice == 1:
        f = lambda x, y: a * x + b * y
    elif choice == 2:
        f = lambda x, y: a * x - b * y
    elif choice == 3:
        f = lambda x, y: a * x * b * y
    elif choice == 4:
        f = lambda x, y: a * x / (b * y)

    a_input = float(input("Podaj początek przedziału (a): "))
    b_input = float(input("Podaj koniec przedziału (b): "))
    y0_input = float(input("Podaj warunek początkowy (y(a)): "))
    h_input = float(input("Podaj krok (h): "))
    n = int((b_input - a_input) / h_input)

    x_third, y_third = runge_kutta_third_order(f, a_input, b_input, y0_input, h_input, n)
    x_fourth, y_fourth = runge_kutta_fourth_order(f, a_input, b_input, y0_input, h_input, n)

    print("\nWyniki dla metody Rungego-Kuty rzędu trzeciego:")
    for x, y in zip(x_third, y_third):
        print(f"x = {x}, y = {y}")

    print("\nWyniki dla metody Rungego-Kuty rzędu czwartego:")
    for x, y in zip(x_fourth, y_fourth):
        print(f"x = {x}, y = {y}")

if __name__ == "__main__":
    main()