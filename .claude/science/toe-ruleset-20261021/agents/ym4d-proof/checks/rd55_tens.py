# rd55_tens.py -- H(4)-invariants in Sym^k(R^4), k <= 4, exact. Criteria: checks/rd55_tens_criteria.md.
from itertools import permutations, product
from fractions import Fraction

def cycles(p):
    seen, out = [False]*4, []
    for i in range(4):
        if not seen[i]:
            c, j = [], i
            while not seen[j]:
                seen[j] = True; c.append(j); j = p[j]
            out.append(c)
    return out

def series_coeffs(p, s, kmax=4):
    # product over cycles of 1/(1 - eps t^len) = product of sum_m eps^m t^{m len}
    poly = [1] + [0]*kmax
    for c in cycles(p):
        eps = 1
        for i in c: eps *= s[i]
        L = len(c)
        fac = [0]*(kmax+1)
        m = 0
        while m*L <= kmax:
            fac[m*L] = eps**m; m += 1
        new = [0]*(kmax+1)
        for a in range(kmax+1):
            if poly[a]:
                for b in range(kmax+1-a):
                    new[a+b] += poly[a]*fac[b]
        poly = new
    return poly

def mat(p, s):
    M = [[0]*4 for _ in range(4)]
    for i in range(4): M[p[i]][i] = s[i]
    return M

def tr(M): return sum(M[i][i] for i in range(4))
def mul(X, Y): return [[sum(X[i][k]*Y[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

ok_ctrl, counts = True, [0]*5
for p in permutations(range(4)):
    for s in product((1, -1), repeat=4):
        co = series_coeffs(p, s)
        M = mat(p, s)
        if co[2] != (tr(M)**2 + tr(mul(M, M)))//2: ok_ctrl = False
        for k in range(5): counts[k] += co[k]
inv = [Fraction(c, 384) for c in counts]
print(f"T0 control k=2 character identity: {'PASS' if ok_ctrl else 'BROKEN'}")
print(f"T1 H(4)-invariant counts in Sym^k, k=0..4: {[str(x) for x in inv]} -> {'PASS' if [int(x) for x in inv[1:]] == [0,1,0,2] and all(x.denominator == 1 for x in inv) else 'FAIL'}")
