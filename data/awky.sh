"Site 8743 ":    "39.2463171,-94.5808637",
#'Site 1': '31.336968, -109.560959',
awk -F' ' '{print "        " "\"" "Site "  NR " \"" ":" " ","  \""$1","$2"\"""\,"}' latlon
