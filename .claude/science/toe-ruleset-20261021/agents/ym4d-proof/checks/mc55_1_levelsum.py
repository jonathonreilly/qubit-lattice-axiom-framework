# mc55_1 -- exact check of the level-sum bookkeeping in MINCB55 Proposition DENS (b).
# Criteria: checks/mc55_1_criteria.md (written before this script). Exact rationals only.
from fractions import Fraction as F

def Lpow(L, e):
    # L^e for rational e with denominator 1 or 2 is needed only as L^(-2 sigma m) with sigma in {1, 1/2}:
    # exponents used below are always integers; assert that.
    assert e.denominator == 1, e
    e = int(e)
    return F(L) ** e

def A_k(sigma, L, k, d=4):
    s = F(0)
    for m in range(k):
        e = F(d * m) - 2 * (2 + sigma) * m
        s += 4 * Lpow(L, e)
    return s

def bound(sigma, L):
    return F(4) / (1 - Lpow(L, -2 * sigma))

ok = True
report = []
# G1 and G2
for L in (3, 5):
    for sigma in (F(1), F(1, 2)):
        B = bound(sigma, L)
        prev = None
        g1 = True
        s = F(0)
        for k in range(1, 201):
            e = F(4 * (k - 1)) - 2 * (2 + sigma) * (k - 1)
            s += 4 * Lpow(L, e)
            if not (s <= B):
                g1 = False
            if prev is not None and not (s > prev):
                g1 = False
            prev = s
        g2 = all(Lpow(L, F(4 * m)) * Lpow(L, -2 * (2 + sigma) * m) == Lpow(L, -2 * sigma * m) for m in range(61))
        report.append(f"G1 L={L} sigma={sigma}: {'PASS' if g1 else 'FAIL'} (A_200 = {float(s):.12g} <= B = {B} = {float(B):.12g})")
        report.append(f"G2 L={L} sigma={sigma}: {'PASS' if g2 else 'FAIL'}")
        ok = ok and g1 and g2
# G4
for L in (3, 5):
    g4 = all(6 * F(L) ** (4 * k) * (F(L) ** (-2 * k)) ** 2 == 6 for k in range(1, 61))
    report.append(f"G4 L={L}: {'PASS' if g4 else 'FAIL'}")
    ok = ok and g4
# C1: sigma = 0 must FAIL "A_k <= 400 for all k <= 200"
s = F(0); c1_holds = True
for k in range(1, 201):
    s += 4 * F(3) ** (4 * (k - 1)) * F(3) ** (-2 * 2 * (k - 1))
    if not (s <= 400):
        c1_holds = False
report.append(f"C1 sigma=0 L=3 gate 'A_k<=400 for k<=200': {'holds (control did NOT fire)' if c1_holds else 'FAILS (control fired)'}; A_200 = {s}")
# C2: d = 5 mutant with sigma = 1/2, L = 3 must FAIL "A_k <= B(1/2,3)"
B = bound(F(1, 2), 3); s = F(0); c2_holds = True
for k in range(1, 201):
    e = F(5 * (k - 1)) - 2 * (2 + F(1, 2)) * (k - 1)
    s += 4 * Lpow(3, e)
    if not (s <= B):
        c2_holds = False
report.append(f"C2 d=5 mutant sigma=1/2 L=3 gate 'A_k<=B={B}': {'holds (control did NOT fire)' if c2_holds else 'FAILS (control fired)'}; A_200 = {s}")
controls_fired = (not c1_holds) and (not c2_holds)
verdict = 'PASS' if (ok and controls_fired) else 'FAIL'
for line in report:
    print(line)
print(f"VERDICT mc55_1: {verdict} (gates {'all hold' if ok else 'NOT all hold'}; controls {'both fired' if controls_fired else 'NOT both fired'})")
