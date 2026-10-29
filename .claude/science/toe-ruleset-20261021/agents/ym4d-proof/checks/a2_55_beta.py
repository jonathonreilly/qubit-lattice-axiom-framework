# a2_55_beta.py -- exact integer comparisons (criteria: a2_55_beta_criteria.md, written first)
a = 51447766041
b1 = a**5 < 5**77
cb_fires = not (a**10 < 5**153)
print("B1 (beta = 23/50 certified for L = 5 at n = 5):", "PASS" if b1 else "FAIL")
print("CB (beta = 47/100 NOT certified):", "FIRES" if cb_fires else "does NOT fire")
print("OVERALL:", "PASS" if (b1 and cb_fires) else "FAIL")
