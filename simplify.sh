#!/bin/sh

for h_skel in `find include -name "*.orig"`
do
  h_simple=`echo ${h_skel} | sed 's|.orig||'`
  echo "# writing "${h_simple}
  ./ifdef-pp/ifdef-pp.py \
    --list-macros-undefine=undefine.txt \
    --apple-libc=remove \
    < "${h_skel}" > "${h_simple}"
done
