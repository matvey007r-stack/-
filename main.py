matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

even_count = 0

print("Матриця:")

for i in range(3):
    row_sum = 0

    for j in range(3):
        number = matrix[i][j]
        print(number, end=" ")
        row_sum += number

        if number % 2 == 0:
            even_count += 1

    print()
    print(f"Сума рядка {i + 1}: {row_sum}")

print(f"\nПарних елементів: {even_count}")