#!/bin/bash

sctipt_dir=$(dirname "$(realpath "$0")")

pos_tests=$(find "$sctipt_dir/../data/" -type f -name "pos_??_in.txt" | sort)
echo -e "Количество позитивных тестов: $(echo "$pos_tests" | wc -l)"

neg_tests=$(find "$sctipt_dir/../data/" -type f -name "neg_??_in.txt" | sort)
echo -e "Количество позитивных тестов: $(echo "$neg_tests" | wc -l)"

cnt_ok=0
cnt_err=0
for pos_test in $pos_tests; do
    basename=$(basename "$pos_test")
    test_name=${basename%_in.txt}

    "$sctipt_dir/pos_case.sh" "$pos_test" "$sctipt_dir/../data/${test_name}_out.txt"
    result=$?

    if [[ result -eq 0 ]]; then
        echo "Тест $test_name пройден!"
        cnt_ok=$(($cnt_ok+1))
    else
        echo "Тест $test_name НЕ пройден!"
        cnt_err=$(($cnt_err+1))
    fi
done

echo "Всего пройдено $cnt_ok/$(echo "$pos_tests" | wc -l) позитивных тестов!"

cnt_ok=0
for neg_test in $neg_tests; do
    basename=$(basename "$neg_test")
    test_name=${basename%_in.txt}

    "$sctipt_dir/neg_case.sh" "$neg_test"
    result=$?

    if [[ result -eq 0 ]]; then
        echo "Тест $test_name пройден!"
        cnt_ok=$(($cnt_ok+1))
    else
        echo "Тест $test_name НЕ пройден!"
        cnt_err=$(($cnt_err+1))
    fi
done

echo "Всего пройдено $cnt_ok/$(echo "$neg_tests" | wc -l) негативных тестов!"

exit $cnt_err