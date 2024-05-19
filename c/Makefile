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