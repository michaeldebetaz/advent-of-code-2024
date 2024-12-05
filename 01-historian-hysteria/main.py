def main():
    filename = "input.txt"
    lines: list[str] = []

    with open(filename) as f:
        lines = f.readlines()

    # [
    #  "1000   2000",
    #  "3000   4000",
    #   ...
    # ]

    # [[1000, 30000, ...] [2000, 4000, ...]]
    
    col_1: list[int] = []
    col_2: list[int] = []

    for line in lines:
        first, second = line.split("   ")
        col_1.append(int(first))
        col_2.append(int(second))

    col_1.sort()
    col_2.sort()
    
    result_1 = 0

    for val_1, val_2 in zip(col_1, col_2):
        distance = abs(val_1 - val_2)
        result_1 += distance
    
    print(f"Col 1: {col_1[0:5]}")
    print(f"Col 2: {col_2[0:5]}")
    print(f"RESULT 1: {result_1}")

    counts: dict[int, int] = {}

    for val_1 in col_1:
        if val_1 not in counts:
            count = 0
            for val_2 in col_2:
                if val_1 == val_2:
                    count += 1
            counts[val_1] = count

    result_2 = 0
    for val_1 in col_1:
        similarity_coeff = counts[val_1]
        result_2 += val_1 * similarity_coeff

    print(f"RESULT 2: {result_2}")


if __name__ == '__main__':
    main()
