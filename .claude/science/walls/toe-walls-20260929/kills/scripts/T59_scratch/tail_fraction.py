import re, math, numpy as np
src = open('kill_checks.py').read().split("# ---------------- K1")[0]
exec(src)
eps = 0.02
def resp(mask_fun, XM=1e7):
    up = run(LAM, 2.0, 5.0, 1.0, xmax=XM, fun=lambda x: 1.0/(1.0+eps*mask_fun(x)))
    dn = run(LAM, 2.0, 5.0, 1.0, xmax=XM, fun=lambda x: 1.0/(1.0-eps*mask_fun(x)))
    return (up-dn)/(2*eps)
tot = resp(lambda x: 1.0)
print("total response (x from 5 to 1e7):", round(tot,4))
for X in [100, 200, 300, 500, 1000]:
    r = resp(lambda x, X=X: 1.0 if x > X else 0.0)
    print(f"  fraction of response from x>{X}: {r/tot:.3f}")
lo = resp(lambda x: 1.0 if x < 1.0 else 0.0) if False else 0.0
