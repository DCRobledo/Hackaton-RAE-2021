CC =gcc
CFLAGS = -Wall -g -Werror

SRC = src
OBJ = obj

FILES=$(wildcard $(SRC)/*.c)
OBJS=$(patsubst $(SRC)%.c,$(OBJ)%.o, $(FILES))

LDLIBS = 

out = /bin


all: tool 

tool: $(OBJS)
	$(CC) $(LDLIBS) $^ -o $(out)/$@

clean:
	rm $(OBJ)/*
	rm $(out)/*


$(OBJS)%.o: $(SRC)%.c
	$(CC) $(CFLAGS) $(LDGLAGS) $^ $(LDLIBS) -c -o $@