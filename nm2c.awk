{
  if (2 < NF) {
    sym = $3
    sub(/^_/, "", sym)
    if ($2 == "T" || $2 == "t") print "void " sym "(void) {}";
    else if ($2 ~ /[SDsdBb]/) print "char " sym "[1024];";
  }
}
