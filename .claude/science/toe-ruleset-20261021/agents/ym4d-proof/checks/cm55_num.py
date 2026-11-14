# cm55_num.py -- rigorous rational arithmetic for the size of m_Y and the weight factors of COFM55.md.
# Criteria: checks/cm55_criteria.md (Part B, items N1-N6 and controls C5-C6; Amendment A2 for N1).
# Exact Fractions / integers only; ln 2 by a rational enclosure; no floats in any verdict.
from fractions import Fraction as F

results = []
controls = []


def report(name, ok, detail):
    results.append((name, ok))
    print(f"{name}: {'PASS' if ok else 'FAIL'}  {detail}")


def control(name, claim_holds, detail):
    fires = not claim_holds
    controls.append((name, fires))
    print(f"{name}: {'FIRES' if fires else 'DOES NOT FIRE'}  {detail}")


def sci(x, digits=6):
    """decimal string of a Fraction for display only (never used in a verdict)."""
    if x == 0:
        return "0"
    sign = "-" if x < 0 else ""
    x = abs(x)
    e = 0
    while x >= 10:
        x /= 10
        e += 1
    while x < 1:
        x *= 10
        e -= 1
    q = int(x * 10 ** digits)
    s = str(q)
    return f"{sign}{s[0]}.{s[1:]}e{e}"


# N1: ln 2 = 2 atanh(1/3) = 2 sum_{j>=0} (1/3)^(2j+1)/(2j+1); tail after N terms <= 2 (1/3)^(2N+1)/((2N+1)(1-1/9))
N = 60
x = F(1, 3)
S = F(0)
for j in range(N):
    S += x ** (2 * j + 1) / (2 * j + 1)
lo = 2 * S
tail = 2 * x ** (2 * N + 1) / ((2 * N + 1) * (1 - x * x))
hi = lo + tail
trunc = F(6931471805599453, 10 ** 16)
report("N1 (ln 2 enclosure)", (0 < hi - lo < F(1, 10 ** 40)) and (0 <= lo - trunc < F(1, 10 ** 16)),
       f"width = {sci(hi - lo)}, lo - 0.6931471805599453 = {sci(lo - trunc)}")

# N2: m_Y <= ln2/(16 L^c) <= ln2/4160 (L^c >= 260)
mY_hi = hi / 4160
mY_lo = lo / 4160
report("N2 (m_Y <= ln2/4160 <= 1.67e-4)", mY_hi <= F(167, 10 ** 6), f"ln2/4160 in [{sci(mY_lo, 8)}, {sci(mY_hi, 8)}]")
control("C5 (claim ln2/4160 <= 1.66e-4)", mY_hi <= F(166, 10 ** 6), f"lo/4160 = {sci(mY_lo, 8)}")

# N3: explicit-part weight: 4(L^c+4) <= 4.1 L^c at L^c = 260 and 2^(264/1040) <= 6/5
ok3a = F(260) * F(41, 10) >= 4 * 264
ok3b = 6 ** 1040 >= 2 ** 264 * 5 ** 1040
report("N3 (e^{4m(L^c+4)} <= 2^(264/1040) <= 6/5 for L^c >= 260, m <= ln2/(16L^c))", ok3a and ok3b,
       f"4.1*260 = {F(260) * F(41, 10)} >= 1056: {ok3a}; (6/5)^1040 >= 2^264: {ok3b}")
control("C6 (claim 4(L^c+4) <= 4.1 L^c at L^c = 100)", 4 * (100 + 4) <= F(41, 10) * 100, "416 vs 410")

# N4: Lemma BW coefficient: (1/4) 2^(4.2/16) <= 1/2  <=  4.2/16 <= 1
report("N4 (BW coefficient <= 1/2 at m_Y)", F(42, 160) <= 1, "exponent 42/160 <= 1")

# N5: which branch of m_Y = min(m'/2, ln2/(16L^c)) binds, m' = m_*'/3, for the tabulated strip widths
tab = [F(273, 10 ** 4), F(384, 10 ** 4), F(306, 10 ** 4), F(140, 10 ** 4), F(226, 10 ** 4), F(216, 10 ** 4)]
mins = min(tab) / 6
report("N5 (ln-2 branch binds for all tabulated m_*')", mins > mY_hi,
       f"min m_*'/6 = {sci(mins, 6)} > ln2/4160 = {sci(mY_hi, 6)}")

# N6 (informational): e^{40 m} at m = ln2/4160 via e^x <= 1/(1-x), 0 <= x < 1
xx = 40 * mY_hi
ub = 1 / (1 - xx)
print(f"N6 (informational): e^(40 m_Y) <= 1/(1 - 40*ln2/4160) = {sci(ub, 8)}")

allpass = all(ok for _, ok in results)
allfire = all(f for _, f in controls)
print()
if allpass and allfire:
    print(f"VERDICT cm55_num: ALL PASS (all controls fired) [{len(results)} criteria, {len(controls)} controls]")
else:
    print("VERDICT cm55_num: FAILURES:",
          [n for n, ok in results if not ok], "controls not firing:", [n for n, f in controls if not f])
