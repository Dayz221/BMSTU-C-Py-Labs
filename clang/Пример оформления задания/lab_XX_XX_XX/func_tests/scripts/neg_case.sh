#!/bin/bash

# Коды возврата:
# 0 - негативный тест пройден успешно (код возврата 1)
# 1 - негативный тест не пройден
# 2 - неверное количество аргументов
# 3 - файл не найден

verbose=0

if [[ $# -ne 1 ]]; then
    # неверное количество аргументов
	exit 2
fi

if [[ ! -f $1 ]]; then
    # файл не найден
	exit 3
fi

sctipt_dir=$(dirname "$(realpath "$0")")

"$sctipt_dir/../../app.exe" < $1 > /dev/null
result_app=$?

if [[ $result_app -eq 0 ]]; then
    exit 1
else
    exit 0
fi