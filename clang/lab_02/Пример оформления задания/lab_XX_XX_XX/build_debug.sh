#!/bin/bash

# Компиляция
gcc -std=c99 -Wall -Werror -O0 -g -c -o debug.o main.c -lm

# Компановка
gcc debug.o -o debug.exe