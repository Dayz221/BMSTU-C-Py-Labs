#!/bin/bash

clang -std=c99 -Wall -Werror -fsanitize=undefined -fno-omit-frame-pointer -g -o debug_ubsan.exe main.c