#!/bin/sh

git submodule update --init ifdef-pp

git submodule update --init Libc-825.24
git submodule update --init --reference Libc-825.24 Libc-498.1.7
git submodule update --init --reference Libc-825.24 Libc-498

git submodule update --init Libm-292.4

git submodule update --init xnu-1456.1.26
git submodule update --init --reference xnu-1456.1.26 xnu-1228.15.4
git submodule update --init --reference xnu-1456.1.26 xnu-1228
