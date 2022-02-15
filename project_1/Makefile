obj-m += jiffies.o

obj-m += seconds.o

KVERSION = $(shell uname -r)

all:
        make -C /lib/modules/$(KVERSION)/build M=$(PWD) modules

clean:
        make -C /lib/modules/$(KVERSION)/build M=$(PWD) clean
~                                                                               
~                                                                  
