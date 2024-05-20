CPPFLAGS = -std=gnu++20 -Wall -Wextra -Werror -Wshadow -Wconversion

all: stamper.out

stamper.out:stamper.cpp
	$(CXX) $(CPPFLAGS) -o $@ $^

clean:
	rm -f stamper.out