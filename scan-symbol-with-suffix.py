#!/usr/bin/env python3
import argparse
import sys
import re

parser = argparse.ArgumentParser(
  formatter_class = argparse.RawTextHelpFormatter
)
parser.add_argument("--include-non-cancellable", action = "store_true",
                    help = "Include $NOCANCEL version (default is not)")
args, rest = parser.parse_known_args()


# see xnu/bsd/sys/cdefs.h
SUF_UNIX03          = "$UNIX2003"
SUF_INODE64         = "$INODE64"
SUF_1050            = "$1050"
SUF_NON_CANCELLABLE = "$NOCANCEL"
SUF_EXTSN           = "$DARWIN_EXTSN"
SUF_LDBL128         = "$LDBL128"

# exclude preprocessor macro definition
regex_PP_DEFINE = re.compile(r"^\s*#\s*define")

# see xnu/bsd/sys/cdefs.h
regex_DARWIN_ALIAS        = re.compile(r"__DARWIN_ALIAS\s*\(\s*(\w+)\s*\)")
regex_DARWIN_ALIAS_C      = re.compile(r"__DARWIN_ALIAS_C\s*\(\s*(\w+)\s*\)")
regex_DARWIN_ALIAS_I      = re.compile(r"__DARWIN_ALIAS_I\s*\(\s*(\w+)\s*\)")
regex_DARWIN_INODE64      = re.compile(r"__DARWIN_INODE64\s*\(\s*(\w+)\s*\)")

regex_DARWIN_1050         = re.compile(r"__DARWIN_1050\s*\(\s*(\w+)\s*\)")
regex_DARWIN_1050ALIAS    = re.compile(r"__DARWIN_1050ALIAS\s*\(\s*(\w+)\s*\)")
regex_DARWIN_1050ALIAS_C  = re.compile(r"__DARWIN_1050ALIAS_C\s*\(\s*(\w+)\s*\)")
regex_DARWIN_1050ALIAS_I  = re.compile(r"__DARWIN_1050ALIAS_I\s*\(\s*(\w+)\s*\)")
regex_DARWIN_1050INODE64  = re.compile(r"__DARWIN_1050INODE64\s*\(\s*(\w+)\s*\)")

regex_DARWIN_EXTSN        = re.compile(r"__DARWIN_EXTSN\s*\(\s*(\w+)\s*\)")
regex_DARWIN_EXTSN_C      = re.compile(r"__DARWIN_EXTSN_C\s*\(\s*(\w+)\s*\)")

regex_DARWIN_LDBL_COMPAT  = re.compile(r"__DARWIN_LDBL_COMPAT\s*\(\s*(\w+)\s*\)")
regex_DARWIN_LDBL_COMPAT2 = re.compile(r"__DARWIN_LDBL_COMPAT2\s*\(\s*(\w+)\s*\)")

## see Libc/include/sys/cdefs.h
#regex_LIBC_ALIAS   = re.compile(r"LIBC_ALIAS\s*\(\s*(\w+)\s*\)")
#regex_LIBC_ALIAS_C = re.compile(r"LIBC_ALIAS_C\s*\(\s*(\w+)\s*\)")
#regex_LIBC_ALIAS_I = re.compile(r"LIBC_ALIAS_I\s*\(\s*(\w+)\s*\)")
#regex_LIBC_INODE64 = re.compile(r"LIBC_INODE64\s*\(\s*(\w+)\s*\)")
#
#regex_LIBC_1050        = re.compile(r"LIBC_1050\s*\(\s*(\w+)\s*\)")
#regex_LIBC_1050ALIAS   = re.compile(r"LIBC_1050ALIAS\s*\(\s*(\w+)\s*\)")
#regex_LIBC_1050ALIAS_C = re.compile(r"LIBC_1050ALIAS_C\s*\(\s*(\w+)\s*\)")
#regex_LIBC_1050ALIAS_I = re.compile(r"LIBC_1050ALIAS_I\s*\(\s*(\w+)\s*\)")
#regex_LIBC_1050INODE64 = re.compile(r"LIBC_1050INODE64\s*\(\s*(\w+)\s*\)")
#
#regex_LIBC_EXTSN       = re.compile(r"LIBC_EXTSN\s*\(\s*(\w+)\s*\)")
#regex_LIBC_EXTSN_C     = re.compile(r"LIBC_EXTSN_C\s*\(\s*(\w+)\s*\)")


regex_suffix = [
#  {"regex": regex_LIBC_ALIAS, "suffixes": [SUF_UNIX03]},
#  {"regex": regex_LIBC_ALIAS_C, "suffixes": [SUF_NON_CANCELLABLE, SUF_UNIX03]},
#  {"regex": regex_LIBC_ALIAS_I, "suffixes": [SUF_INODE64, SUF_UNIX03]},
#  {"regex": regex_LIBC_INODE64, "suffixes": [SUF_INODE64]},
#
#  {"regex": regex_LIBC_1050, "suffixes": [SUF_1050]},
#  {"regex": regex_LIBC_1050ALIAS, "suffixes": [SUF_1050, SUF_UNIX03]},
#  {"regex": regex_LIBC_1050ALIAS_C, "suffixes": [SUF_1050, SUF_NON_CANCELLABLE, SUF_UNIX03]},
#  {"regex": regex_LIBC_1050ALIAS_I, "suffixes": [SUF_1050, SUF_INODE64, SUF_UNIX03]},
#  {"regex": regex_LIBC_1050INODE64, "suffixes": [SUF_1050, SUF_INODE64]},
#
#  {"regex": regex_LIBC_EXTSN, "suffixes": [SUF_EXTSN]},
#  {"regex": regex_LIBC_EXTSN_C, "suffixes": [SUF_EXTSN, SUF_NON_CANCELLABLE]},

  # see xnu/bsd/sys/cdefs.h
  {"regex": regex_DARWIN_ALIAS, "suffixes": [SUF_UNIX03]},
  {"regex": regex_DARWIN_ALIAS_C, "suffixes": [SUF_NON_CANCELLABLE, SUF_UNIX03]},
  {"regex": regex_DARWIN_ALIAS_I, "suffixes": [SUF_INODE64, SUF_UNIX03]},
  {"regex": regex_DARWIN_INODE64, "suffixes": [SUF_INODE64]},

  {"regex": regex_DARWIN_1050, "suffixes": [SUF_1050]},
  {"regex": regex_DARWIN_1050ALIAS, "suffixes": [SUF_1050, SUF_UNIX03]},
  {"regex": regex_DARWIN_1050ALIAS_C, "suffixes": [SUF_1050, SUF_NON_CANCELLABLE, SUF_UNIX03]},
  {"regex": regex_DARWIN_1050ALIAS_I, "suffixes": [SUF_1050, SUF_INODE64, SUF_UNIX03]},
  {"regex": regex_DARWIN_1050INODE64, "suffixes": [SUF_1050, SUF_INODE64]},

  {"regex": regex_DARWIN_EXTSN, "suffixes": [SUF_EXTSN]},
  {"regex": regex_DARWIN_EXTSN_C, "suffixes": [SUF_EXTSN, SUF_NON_CANCELLABLE]},

  {"regex": regex_DARWIN_LDBL_COMPAT, "suffixes": [SUF_LDBL128]},
  {"regex": regex_DARWIN_LDBL_COMPAT2, "suffixes": [SUF_LDBL128]},
]

headers = sys.stdin.readlines()

def create_entry(fp, idx, header_line, m, suffixes, suffixes_exclude):
  suffixes_selected = [sfx for sfx in suffixes if sfx not in suffixes_exclude]
  found_macro = m.group(0)
  sym_name = m.group(1)
  sym_name_with_suffix = sym_name + "".join(suffixes_selected)
  d = {}
  d["file"] = fp
  d["line"] = {
    "index": idx,
    "content": header_line,
    "found_macro": found_macro
  }
  d["stem"] = sym_name
  d["suffixes"] = suffixes_selected
  return sym_name_with_suffix, d

syms_with_suffix = {}

for fp in headers:
  fp = fp.strip()
  sys.stderr.write(f"# scan {fp}...")
  with open(fp, "r", encoding = "latin-1") as fh:
    for idx, header_line in enumerate(fh.readlines()):
      header_line = header_line.strip()

      if regex_PP_DEFINE.match(header_line):
        continue

      for dic in regex_suffix:
        rgx  = dic["regex"]
        if m := rgx.search(header_line):
          # print(f"{header_line}")
          s, d = create_entry(fp, idx, header_line, m,
                              dic["suffixes"], [SUF_NON_CANCELLABLE])
          if s not in syms_with_suffix:
            syms_with_suffix[s] = d

          if args.include_non_cancellable and SUF_NON_CANCELLABLE in dic["suffixes"]:
            s, d = create_entry(fp, idx, header_line, m,
                                dic["suffixes"], [])
            if s not in syms_with_suffix:
              syms_with_suffix[s] = d

  sys.stderr.write("\n")

print(f"/* {len(syms_with_suffix.keys())} stub symbols with special suffixes */\n")
for s in sorted(syms_with_suffix.keys()):
  d = syms_with_suffix[s]
  f = d["file"]
  l = d["line"]["index"]
  m = d["line"]["found_macro"]
  sa = d["stem"] + "".join( sfx.replace("$", "_").lower() for sfx in d["suffixes"] )
  print(f"/* {f}:{l} \"{m}\" */")
  print(f"void {sa}(void) __asm__(\"_{s}\");")
  print(f"void {sa}(void) {{}}")
  print("")
