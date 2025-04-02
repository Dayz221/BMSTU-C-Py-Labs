#!/bin/bash

# Компиляция
gcc -std=c99 -Wall -Werror -c -o app.o main.c -lm

# Компановка
gcc app.o -o app.exe