LIPO ?= powerpc64-apple-darwin9-lipo
CC   ?= powerpc64-apple-darwin9-base-gcc
SRCS  = libSystem-PD9.c Libc+xnu_sym-with-dollar.c

libSystem.B.dylib: libSystem.m32.dylib libSystem.m64.dylib
	$(LIPO) -create -output $@ $^

libSystem.m32.dylib: $(SRCS)
	$(CC) -m32 $(SRCS) -dynamiclib -o $@ \
		-install_name /usr/lib/libSystem.B.dylib \
		-compatibility_version 1.0.0 \
		-current_version 111.1.4

libSystem.m64.dylib: $(SRCS)
	$(CC) -m64 $(SRCS) -dynamiclib -o $@ \
		-install_name /usr/lib/libSystem.B.dylib \
		-compatibility_version 1.0.0 \
		-current_version 111.1.4

libSystem-PD9.c: libSystem-PD9.txt
	awk -f nm2c.awk < $< > $@

Libc+xnu_sym-with-dollar.c:
	find Libc xnu -name "*.h" | ./scan-symbol-with-suffix.py > $@

