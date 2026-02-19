# ppc-libsystem-stub

## What is this?

This is an APSL compatible libSystem.dylib stub,
to be usable as a substitution of a `MacOSX.10.5.sdk`
in `osxcross` building for PowerPC platform.

## Why?

The redistribution and reverse engineering (like
disassembling) of genuine MacOSX SDK is prohibited
by MacOSX SDK EULA. Thus it is not hard to build
cross compilers on non-Apple computers. It means
that it is hard to apply CI/CD procedure to it,
because the resource of CI/CD infrastructure for
macOS is not popular.

Fortunately, the symbols required by `libgcc_s.dylib`,
`libstdc++.dylib`, `libobjc-gnu.dylib` etc are quite
limited, they are covered by the symbols provided
by Libc and libSystem components published under APSL.
GCC-based cross compilers like `osxcross` would have
no essential dependency with proprietary frameworks.

However, building Libc or libSystem out of macOS is
not easy. In the past, `PureDarwin` project did it
for Darwin9 kernel on i386 platform (no ppc binaries),
but their building scripts are already lost.

## What this repository provides

### The header files collected from APSL softwares

Even the header files of them include so many `#ifdef`
which are not found in genuine MacOSX SDK.
By `ifdef-pp.py` (a wrapper of `unifdef`), they are
preprocessed to convert them into simplified headers.

### The stub libraries

This project provides 2 stubs: libSystem.B.dylib and
libSystemStubs.a. The latter is an empty library,
providing no symbols to be referred seriously. 

The former is a stub library, providing the void
function entries, and 1024-byte strings. As the first
release, the symbols are gathered from following steps.

1. `PureDarwin 9` iso image had `libSystem.B.dylib`
which was built (for i386) by themselves, and it was
not prohibited to be used for reverse engineering.
Scanning it and get the list of its global symbols.

2. The functions with suffixes (like `printf$UNIX2003`)
scanned by the header files.

Yet we do not have a way to get complete list of the
symbols in genuine libSystem.B.dylib, without violating
MacOSX EULA, but the symbols to build GCC-5.5.0 in
`osxcross` for PowerPC can be covered by this stub.


