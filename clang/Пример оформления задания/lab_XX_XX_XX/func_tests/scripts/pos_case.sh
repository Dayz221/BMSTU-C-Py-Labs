#!/bin/bash

# Коды возврата:
# 0 - тест пройден успешно
# 1 - тест не пройден
# 2 - неверное количество аргументов
# 3 - файл не найден

verbose=0

if [[ $# -ne 2 ]]; then
    # неверное количество аргументов
	exit 2
fi

if [[ ! -f $1 || ! -f $2 ]]; then
    # файл не найден
	exit 3
fi

basename=$(basename $1)
test_name=${basename%_in.txt}
sctipt_dir=$(dirname "$(realpath "$0")")

"$sctipt_dir/../../app.exe" < $1 > "$test_name.tmp"
result_app=$?

"$sctipt_dir/comparator.sh" "$test_name.tmp" $2
result_comparator=$?

summ=$(($result_app+$result_comparator))
if [[ $summ -eq 0 ]]; then
    exit 0
else
    exit 1
fi