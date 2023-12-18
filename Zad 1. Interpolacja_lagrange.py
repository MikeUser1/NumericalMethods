def interpolacja_lagrange(x, y):
    n = len(x)

    # Funkcja pomocnicza dla interpolacji Lagrange'a
    def lagrange_basis_polynomial(i):
        def basis_polynomial(x_value):
            result = 1.0
            for j in range(n):
                if j != i:
                    result *= (x_value - x[j]) / (x[i] - x[j])
            return result

        return basis_polynomial

    # Tworzenie wielomianu interpolacyjnego
    def wielomian_interpolacyjny(x_value):
        result = 0.0
        for i in range(n):
            result += y[i] * lagrange_basis_polynomial(i)(x_value)
        return result

    return wielomian_interpolacyjny

# Przykładowe dane dla 10 punktów
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 5, 10, 17, 26, 37, 50, 65, 82, 101]

# Wywołanie funkcji interpolacji
interpolacja = interpolacja_lagrange(x, y)

# Przykładowe wartości x, dla interpolacji
x_values = [1.5, 2.5, 6.5, 8.5]

# Wyświetlanie wyniku
for x_val in x_values:
    y_val = interpolacja(x_val)
    print(f'Interpolacja dla x = {x_val}: y = {y_val}')
