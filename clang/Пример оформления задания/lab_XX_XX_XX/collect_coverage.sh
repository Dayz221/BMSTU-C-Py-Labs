#!/bin/bash

gcc -std=c99 -Wall -Werror --coverage -O0 -o app.exe main.c

./func_tests/scripts/func_tests.sh

result=$(gcov app-main | grep -o -m 1 "[0-9]*.[0-9]*%")
echo "Результат тестирования покрытия: $result"