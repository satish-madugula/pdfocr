import re
lst = ["a par_1_2","par_1_test","par_test_test","par_1_a","par_2_1","par_3_12"]
pat = "\w[par]\w[_]\d{1,3}[_]\d{1,3}"
for l in lst:
    res = re.match(pat,l)
    print(res)