def linear_approximation(points):
    n = len(points)
    a = (points[-1][1] - points[0][1]) / (points[-1][0] - points[0][0])
    b = points[0][1] - a * points[0][0]
    return a, b

def absolute_error(points, a, b):
    error = 0
    for x, y in points:
        error += abs(y - (a * x + b))
    return error

def draw_line(a, b, start, end):
    x_values = [start[0], end[0]]
    y_values = [a * start[0] + b, a * end[0] + b]
    line = list(zip(x_values, y_values))
    return line

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

    n = int(input("Podaj liczbę punktów do interpolacji: "))
    points = []
    for i in range(n):
        x = float(input(f"Podaj x{i + 1}: "))
        y = float(input(f"Podaj y{i + 1}: "))
        points.append((x, y))

    # Metoda Łamanych
    print("Metoda Łamanych:")
    for i in range(n - 1):
        line = draw_line(0, 0, points[i], points[i + 1])
        print(f"Odcinek {i + 1}: {line}")

    # Pierwsze Ulepszenie
    print("\nPierwsze Ulepszenie:")
    for i in range(n - 1):
        a, b = linear_approximation(points[i:i + 2])
        line = draw_line(a, b, points[i], points[i + 1])
        print(f"Odcinek {i + 1}: {line}")

if __name__ == "__main__":
    main()