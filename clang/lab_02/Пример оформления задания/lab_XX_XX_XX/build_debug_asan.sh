#!/bin/bash

clang -std=c99 -Wall -Werror -fsanitize=address -fno-omit-frame-pointer -g -o debug_asan.exe main.c -lm