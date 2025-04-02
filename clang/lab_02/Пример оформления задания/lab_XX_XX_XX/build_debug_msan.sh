#!/bin/bash

clang -std=c99 -Wall -Werror -fsanitize=memory -fPIE -pie -fno-omit-frame-pointer -g -o debug_msan.exe main.c -lm