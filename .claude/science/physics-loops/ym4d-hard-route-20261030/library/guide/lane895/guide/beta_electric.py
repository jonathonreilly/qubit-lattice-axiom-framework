# GUIDE only: electric model (row 863 A2). Levels are sums over links of E_j(s) = -log(I_{2j+1}(s)/I_1(s)).
# Computes max over j of -d log E_j/ds on s in [0.36, 3]. Decides nothing.
import math
def logI(n, x, terms=60):
    # log of modified Bessel I_n(x) by the series, in logs to avoid overflow
    logs = [(2*k+n)*math.log(x/2) - math.lgamma(k+1) - math.lgamma(k+n+1) for k in range(terms)]
    m = max(logs)
    return m + math.log(sum(math.exp(l-m) for l in logs))
def E(n, s):  # n = 2j+1, j >= 1/2
    return -(logI(n, s) - logI(1, s))
h = 1e-5
def slope(n, s):
    return -(math.log(E(n, s+h)) - math.log(E(n, s-h)))/(2*h)
for s in (0.36, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0):
    best = max((slope(n, s), n) for n in range(2, 40))
    print(f"s={s:4.2f}  max_j -dlogE_j/ds = {best[0]:.3f} at 2j+1 = {best[1]}   (j=1/2: {slope(2, s):.3f})")
