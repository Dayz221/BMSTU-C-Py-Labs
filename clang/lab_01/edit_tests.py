i = 1
while True:
    in_data = input(f"Введите входные позитивные данные {i} теста: ")
    if in_data == "":break

    out_data = input(f"Введите выходные позитивные данные {i} теста: ")

    with open(f"func_tests/data/pos_{i:02}_in.txt", "w") as in_file, open(f"func_tests/data/pos_{i:02}_out.txt", "w") as out_file:
        in_file.write(in_data)
        out_file.write(out_data)

    i += 1

i = 1
while True:
    in_data = input(f"Введите входные негативные данные {i} теста: ")
    if in_data == "":break

    out_data = input(f"Введите выходные негативные данные {i} теста: ")

    with open(f"func_tests/data/neg_{i:02}_in.txt", "w") as in_file, open(f"func_tests/data/neg_{i:02}_out.txt", "w") as out_file:
        in_file.write(in_data)
        out_file.write(out_data)

    i += 1