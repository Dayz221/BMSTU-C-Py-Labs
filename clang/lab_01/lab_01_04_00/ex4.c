#include <stdio.h>

#define FULL_PRICE 45
#define EMPTY_PRICE 20

int main()
{
    // Ввод входных данных
    int money;

    printf("Enter count of moneys: ");
    scanf("%d", &money);

    // Необходимые вычисления
    int cnt_of_bottles;
    cnt_of_bottles = (money - EMPTY_PRICE) / (FULL_PRICE - EMPTY_PRICE);

    // Вывод результата
    printf("Count of bottles: %d", cnt_of_bottles);

    return 0;
}
