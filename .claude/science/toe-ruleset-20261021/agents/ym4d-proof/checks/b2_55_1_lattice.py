# b2_55_1 — exact check for B2_55 (criteria: checks/b2_55_1_criteria.md, written first).
# Plain python, fractions only; rigorous rational enclosures for exp and ln 2; no floats in verdicts.
from fractions import Fraction as F
import sys

K = 256
SC = 1 << K

def rdown(x):
    return F((x.numerator * SC) // x.denominator, SC)

def rup(x):
    return F(-((-x.numerator * SC) // x.denominator), SC)

def exp_neg(x):
    """Rigorous enclosure [lo, hi] of e^{-x} for rational x >= 0."""
    x = F(x)
    assert x >= 0
    if x == 0:
        return F(1), F(1)
    s = 0
    while x / (1 << s) > F(1, 2):
        s += 1
    y = x / (1 << s)
    # alternating partial sums: S_{2m+1} <= e^{-y} <= S_{2m} for 0 <= y <= 1/2
    term = F(1)
    S = F(1)
    sums = [S]
    for i in range(1, 32):
        term = term * y / i
        S = S - term if i % 2 == 1 else S + term
        sums.append(S)
    hi = sums[30]
    lo = sums[31]
    assert 0 < lo <= hi
    lo, hi = rdown(lo), rup(hi)
    for _ in range(s):
        lo, hi = rdown(lo * lo), rup(hi * hi)
    assert 0 < lo <= hi
    return lo, hi

def dT(z, T):
    z = z % T
    return min(z, T - z)

results = {}
out = []

# ---------------- Gate A ----------------
mus = [F(1, 10000), F(1, 100), F(1, 7), F(1), F(3)]
hs = [F(1), F(1, 3), F(1, 9), F(1, 27)]
Ts = [3, 4, 5]
A_ok = True
A_ctl = False
ctl_cases = []
ncase = 0
for mu in mus:
    for h in hs:
        for T in Ts:
            n_pts = F(T) / h
            assert n_pts.denominator == 1
            n_pts = int(n_pts)
            for a in [F(0), h / 3, h / 2, 2 * h / 3]:
                ncase += 1
                Slo = F(0); Shi = F(0)
                for n in range(n_pts):
                    d = dT(a + n * h, T)
                    lo, hi = exp_neg(mu * d)
                    Slo += lo; Shi += hi
                t0 = a % h
                l1, u1 = exp_neg(mu * t0)
                l2, u2 = exp_neg(mu * (h - t0))
                l3, u3 = exp_neg(mu * h)
                assert u3 < 1
                Plo = (l1 + l2) / (1 - l3)
                Phi = (u1 + u2) / (1 - u3)
                B1lo = 2 / (1 - l3)
                B1hi = 2 / (1 - u3)
                B2 = 2 * (1 + 1 / (mu * h))
                ok = (Shi <= Plo) and (Phi <= B1lo) and (B1hi <= B2)
                if not ok:
                    A_ok = False
                    out.append("A FAIL case mu=%s h=%s T=%s a=%s" % (mu, h, T, a))
                if Slo > 1 + 1 / (mu * h):
                    A_ctl = True
                    ctl_cases.append((str(mu), str(h), T, str(a), float(Slo), float(1 + 1 / (mu * h))))
out.append("A: %d cases; all inequalities S <= P <= 2/(1-e^{-mu h}) <= 2(1+1/(mu h)) hold: %s" % (ncase, A_ok))
out.append("A-ctl (false bound S <= 1 + 1/(mu h)) violated in %d cases; fired: %s" % (len(ctl_cases), A_ctl))
for c in ctl_cases[:6]:
    out.append("   A-ctl witness mu=%s h=%s T=%s a=%s : S >= %.6f > %.6f" % c)
results['A'] = A_ok
results['A-ctl fired'] = A_ctl

# ---------------- Gate D ----------------
N = 60
ln2_part = sum(F(1, n * (1 << n)) for n in range(1, N + 1))
ln2_hi = ln2_part + F(1, (N + 1) * (1 << N))
ln2_lo = ln2_part
assert ln2_lo < ln2_hi
mbar = ln2_hi / 4160
D_val = (1 + 1 / mbar) ** 2
D_ok = D_val >= 36000000
out.append("D: ln2 in [%.12f, %.12f]; m_Y <= mbar = %.6e; (1+1/mbar)^2 >= %.1f ; >= 3.6e7: %s"
           % (float(ln2_lo), float(ln2_hi), float(mbar), float(D_val), D_ok))
D_rounded = (1 + 1 / F(167, 1000000)) ** 2
D_ctl = not (D_rounded >= 36000000)
out.append("D-ctl: with 1.67e-4, (1+1/mu)^2 = %.1f ; '>= 3.6e7' is FALSE (control fires): %s" % (float(D_rounded), D_ctl))
results['D'] = D_ok
results['D-ctl fired'] = D_ctl

# ---------------- Gate E ----------------
cases = [(3, F(1), F(3)), (5, F(1), F(5)), (7, F(1), F(7)), (9, F(1, 2), F(3))]
E_ok = True
E_ctl1 = True
for (Lv, sig, Ls) in cases:
    Lf = F(Lv)
    bound_mis = Lf ** 2 / (1 - 1 / Ls)
    for k in range(1, 61):
        lhs = sum(Lf ** (-2 * (k - 1 - j)) * Ls ** (-(k - 1 - j)) * Lf ** (2 * (k - j)) for j in range(k))
        rhs = Lf ** 2 * sum(Ls ** (-q) for q in range(k))
        printed = sum(Lf ** (-2 * (k - j)) * Ls ** (-(k - j)) * Lf ** (2 * (k - j)) for j in range(k))
        cert = sum(Lf ** (-2 * (k - j)) * Lf ** (k - j) for j in range(k))
        eta2 = sum(Lf ** (-3 * (k - j)) * Lf ** (2 * (k - j)) for j in range(k))
        e1 = (lhs == rhs) and (lhs <= bound_mis)
        e2 = (printed * Lf ** 2 * Ls == lhs)
        e3 = (cert <= 1 / (Lf - 1)) and (eta2 <= 1 / (Lf - 1))
        if not (e1 and e2 and e3):
            E_ok = False
            out.append("E FAIL L=%s sigma=%s k=%d e1=%s e2=%s e3=%s" % (Lv, sig, k, e1, e2, e3))
        # control 1: weight L^{(1+sigma/2)(k-j)} -> squared weight L^{2(k-j)} * Ls^{(k-j)}
        mis_a = sum(Lf ** (-2 * (k - 1 - j)) * Ls ** (-(k - 1 - j)) * Lf ** (2 * (k - j)) * Ls ** (k - j) for j in range(k))
        if mis_a != k * Lf ** 2 * Ls:
            E_ctl1 = False
    mis60 = 60 * Lf ** 2 * Ls
    ratio = mis60 / bound_mis
    if not ratio >= 30:
        E_ctl1 = False
    out.append("E case L=%d sigma=%s: E1/E2/E3 over k=1..60 ok so far: %s; ctl1 ratio at k=60 = %s" % (Lv, sig, E_ok, ratio))
spin = [F(9) ** k for k in range(1, 61)]
E_ctl2 = any(s > 10 ** 6 for s in spin)
first = next(k for k in range(1, 61) if F(9) ** k > 10 ** 6)
out.append("E-ctl2: 9^k > 1e6 first at k = %d; fired: %s" % (first, E_ctl2))
results['E'] = E_ok
results['E-ctl1 fired'] = E_ctl1
results['E-ctl2 fired'] = E_ctl2

overall = A_ok and D_ok and E_ok and A_ctl and D_ctl and E_ctl1 and E_ctl2
out.append("RESULTS: %s" % results)
out.append("OVERALL: %s" % ("PASS" if overall else "FAIL"))
print("\n".join(out))
