"""Independent check of a line of pinned sources on the 4-torus.

Own 7-point operator and own Green inverse over the rationals.
The author's script is not called. The killing rate is part of the finite model.
"""
import itertools
import sys

from sympy import QQ
from sympy.polys.matrices import DomainMatrix

FAILS = []
L = 4
SITES = [(i, j, k) for i in range(L) for j in range(L) for k in range(L)]
IDX = {s: n for n, s in enumerate(SITES)}
NB = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def want(label, ok):
    if not ok:
        FAILS.append(label)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


def build(kill):
    n = len(SITES)
    w = (QQ(1) - kill) / QQ(7)
    rows = [[QQ(0) for _ in range(n)] for _ in range(n)]
    for s in SITES:
        i = IDX[s]
        rows[i][i] += QQ(1) - w
        for d in NB:
            t = ((s[0] + d[0]) % L, (s[1] + d[1]) % L, (s[2] + d[2]) % L)
            rows[i][IDX[t]] -= w
    return DomainMatrix(rows, (n, n), QQ)


kill = QQ(1, 10)
A = build(kill)
G = A.inv()
g0 = G[0, 0].element
ok = all(A[i, j] == A[j, i] for i in range(0, 64, 5) for j in range(i))
ok = ok and all(G[i, j] == G[j, i] for i in range(0, 64, 5) for j in range(i))
# row sum of A is the killing rate
row = sum(A[0, j].element for j in range(64))
ok = ok and row == kill
want("U1 the Green matrix of the killed 7-point operator is symmetric and A has row sum 1/10", ok)

alpha = QQ(1)
charges = {}
for nsrc in (2, 3, 4):
    S = [(i, 0, 0) for i in range(nsrc)]
    M = DomainMatrix([[G[IDX[S[a]], IDX[S[b]]].element for b in range(nsrc)] for a in range(nsrc)], (nsrc, nsrc), QQ)
    c = M.inv() * DomainMatrix([[alpha] for _ in range(nsrc)], (nsrc, 1), QQ)
    cs = [c[i, 0].element for i in range(nsrc)]
    charges[nsrc] = cs
    rhs = [QQ(0)] * 64
    for i, s in enumerate(S):
        rhs[IDX[s]] = cs[i]
    cvec = DomainMatrix([[rhs[i]] for i in range(64)], (64, 1), QQ)
    mvec = G * cvec
    Am = A * mvec
    pin = all(mvec[IDX[s], 0].element == alpha for s in S)
    off = all(Am[IDX[y], 0].element == 0 for y in SITES if y not in S)
    on = all(Am[IDX[S[i]], 0].element == cs[i] for i in range(nsrc))
    want(f"U2 n={nsrc} pins at 1 and (I-P)m vanishes off the line", pin and off and on)

c3 = charges[3]
ok = c3[0] == c3[2] and c3[1] < c3[0]
want("U3 n=3 is symmetric and the interior charge is strictly smaller than the ends", ok)
c4 = charges[4]
ok = all(c4[i] == c4[0] for i in range(4))
want("U3 n=4 wraps the 4-torus, so all four charges are equal", ok)

iso = alpha / g0
per = {n: sum(charges[n]) / QQ(n) for n in (2, 3, 4)}
tot = {n: sum(charges[n]) for n in (2, 3, 4)}
ok = tot[2] < tot[3] < tot[4]
ok = ok and per[4] < per[3] < per[2] < iso
want("U4 total charge rises with length while charge per source falls below the isolated cost", ok)


def show(q):
    return f"{float(q):.9f}"


quoted = {
    "iso": "0.692647018",
    "c3e": "0.528563241",
    "c3i": "0.447653871",
    "p2": "0.562325833",
    "p3": "0.501593451",
    "p4": "0.439033578",
}
ok = (
    show(iso) == quoted["iso"]
    and show(c3[0]) == quoted["c3e"]
    and show(c3[1]) == quoted["c3i"]
    and show(per[2]) == quoted["p2"]
    and show(per[3]) == quoted["p3"]
    and show(per[4]) == quoted["p4"]
)
want("U4 the printed nine-decimal charges match the exact rationals", ok)

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: fails at " + FAILS[0])
    sys.exit(1)
print(
    "HIT: confirmed - on the 4-torus with killing 1/10, c = M^{-1} alpha pins a collinear line of 2, 3 or 4 sources. "
    "At n=3 the interior charge is strictly below the ends. At n=4 the line wraps and all four charges are equal. "
    "Charge per source falls from the isolated value through n=2, 3 and 4."
)
print(
    "SUMMARY: confirmed the line solve. The numbers are for this killed finite torus, not for Z^3. "
    f"Interior {show(c3[1])} against ends {show(c3[0])}; per source {show(iso)}, {show(per[2])}, {show(per[3])}, {show(per[4])}."
)
