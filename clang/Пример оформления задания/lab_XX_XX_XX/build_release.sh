#!/bin/bash

# Компиляция
gcc -std=c99 -Wall -Werror -c -o app.o main.c

# Компановка
gcc app.o -o app.exe