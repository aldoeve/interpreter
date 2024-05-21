#-----------------------------------------------------------------#
#  Developer: Aldo Vera-Espinoza                  ___     _______ #
#  Date: Tue May 21 15:51:15 2024                / \ \   / / ____|#
#                                               / _ \ \ / /|  _|  #
#  Project Name: Makefile for Cinterpreter     / ___ \ V / | |___ #
#  Description:                               /_/   \_\_/  |_____|#
#    Makefile for Cinterpreter.                                   #
#-----------------------------------------------------------------#

CFLAGS = -Wextra -Wall -Wshadow -Wundef -O3

all: test.out

main.cpp: common.h

test.out: main.c
	$(CC) $(CFLAGS) -o $@ $^

run:
	@echo "Running"
	@echo "---------------------------------------------------------"
	@./test

clean:
	rm -f test.out