CFLAGS=-g -O0 -Wall -std=c99 -Wno-format -march=native -funroll-loops -fomit-frame-pointer -ffunction-sections -fdata-sections -msse -maes -msse4

ifdef MPAR
	CFLAGS += -DMPAR=$(MPAR)
endif

haraka: haraka.c
	$(CC) $(CFLAGS) -fPIC -c -o $@.o $<
	$(CC) $(CLFAGS) -shared -o lib$@.so $@.o

.PHONY: haraka
