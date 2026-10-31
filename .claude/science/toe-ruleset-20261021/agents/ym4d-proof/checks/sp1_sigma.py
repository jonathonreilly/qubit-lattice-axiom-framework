#!/usr/bin/env python3
# sp1 — exact bookkeeping gates for target T55-R.  Criteria: checks/sp1_criteria.md (written first).
# Exact Fraction / int arithmetic only.  No numpy, no BLAS.  No numeric lock needed (rule 6).
from fractions import Fraction as F

out = []
def say(s):
    out.append(s); print(s)

def Lpow(L, e):
    """L**e for rational e where it is exact; returns Fraction or None."""
    if e.denominator == 1:
        return F(L) ** e.numerator
    r = round(L ** (1.0 / e.denominator))
    if r ** e.denominator != L:
        return None
    return F(r) ** e.numerator

# ---------------- sp1-A : the Step 3 exponent identity -------------------------------
def gateA(coef_m=4):
    bad = []
    n = 0
    for k in range(1, 13):
        for l in range(0, k):
            for m in range(l + 1, k + 1):
                n += 1
                E = -3 * (k - l) + coef_m * (m - l) - 2 * (k - l) + 4 * (k - m)
                if E != -(k - l):
                    bad.append((k, l, m, E, -(k - l)))
    return n, bad

n, bad = gateA(4)
say("sp1-A  triples=%d  violations=%d  -> %s" % (n, len(bad), "PASS" if not bad else "FAIL"))

# sp1-A' : sigma-shifted identity
sigmas = [F(1), F(3, 4), F(1, 2), F(1, 4), F(1, 8)]
badp = []
for s in sigmas:
    for k in range(1, 13):
        for l in range(0, k):
            for m in range(l + 1, k + 1):
                lhs = F(-3 * (k - l) + 4 * (m - l) - 2 * (k - l) + 4 * (k - m)) + (1 - s) * (m - l)
                rhs = F(-(k - l)) + (1 - s) * (m - l)
                if lhs != rhs:
                    badp.append((s, k, l, m))
say("sp1-A' sigmas=%d  violations=%d  -> %s" % (len(sigmas), len(badp), "PASS" if not badp else "FAIL"))

# sp1-F : designed-FAIL control, mutate the constant 4 -> 3
n2, bad2 = gateA(3)
fired_F = len(bad2) > 0
say("sp1-F  CONTROL (coef 4->3): violations=%d  -> %s" % (len(bad2), "FIRED" if fired_F else "DID NOT FIRE"))

# ---------------- sp1-B : closed form of the double sum ------------------------------
def Theta(L, s, t):
    """sum_{j=0}^{t-1} L^{(1-s)j} as an exact Fraction (requires L^{(1-s)} exact)."""
    x = Lpow(L, 1 - s)
    assert x is not None
    tot = F(0); cur = F(1)
    for _ in range(t):
        tot += cur; cur *= x
    return tot

def gateB(L, s, Tmax=60):
    ls = Lpow(L, s)
    if ls is None:
        return None
    closed = F(1) / ((L - 1) * (1 - F(1) / ls))
    partial = F(0)
    for t in range(1, Tmax + 1):
        partial += Theta(L, s, t) * F(1, L ** t)
    # exact tail bound
    if s == 1:
        tail = F(Tmax + 2, L ** Tmax) * F(L, (L - 1) ** 2)
    else:
        x = Lpow(L, 1 - s)
        tail = (F(1) / ls) ** Tmax * (F(1) / ls) / ((x - 1) * (1 - F(1) / ls))
    err = abs(partial - closed)
    return closed, partial, err, tail, err <= tail

say("")
cases = [(3, F(1)), (9, F(1, 2)), (16, F(3, 4)), (16, F(1, 4)), (81, F(1, 4)), (4, F(1, 2))]
allB = True
for L, s in cases:
    r = gateB(L, s)
    if r is None:
        say("sp1-B  L=%d sigma=%s  SKIPPED (L^sigma irrational)" % (L, s)); allB = False; continue
    closed, partial, err, tail, ok = r
    allB = allB and ok
    say("sp1-B  L=%-3d sigma=%-4s closed=%-22s err=%s tail=%s -> %s"
        % (L, s, str(closed), str(err), str(tail), "PASS" if ok else "FAIL"))
say("sp1-B  OVERALL -> %s" % ("PASS" if allB else "FAIL"))

# ---------------- sp1-C : convergence of the CO-B_sigma Holder sum --------------------
def Esig(L, s, t):
    return F(t + 1) * Theta(L, s, t + 1)

def gateC(L, alpha, s, Tmax=40):
    y = Lpow(L, 1 - alpha)
    assert y is not None
    terms = []
    for t in range(1, Tmax + 1):
        terms.append(Esig(L, s, t) / (y ** t))
    S = [F(0)]
    for x in terms:
        S.append(S[-1] + x)
    worst = F(0); okratio = True
    for T in range(10, Tmax + 1):
        num = S[T] - S[T - 1]
        den = S[T - 1] - S[T - 2]
        r = num / den
        if r > worst:
            worst = r
        if r > F(9, 10):
            okratio = False
    return S[Tmax], worst, okratio and S[Tmax] <= 10 ** 6

say("")
pairs = [(F(1, 4), F(1, 2)), (F(1, 8), F(1, 4)), (F(1, 16), F(1, 8)), (F(1, 4), F(1)), (F(1, 2), F(3, 4))]
allC = True
for a, s in pairs:
    # need L^{1-alpha} and L^{1-sigma} exact: pick L a high power
    L = 2 ** 16
    Sv, worst, ok = gateC(L, a, s)
    allC = allC and ok
    say("sp1-C  L=2^16 alpha=%-5s sigma=%-4s S(40)=%.6g  worst ratio=%.6f -> %s"
        % (a, s, float(Sv), float(worst), "PASS" if ok else "FAIL"))
say("sp1-C  OVERALL -> %s" % ("PASS" if allC else "FAIL"))

# ---------------- sp1-D : designed-FAIL control, sigma = 0 ---------------------------
say("")
s0 = F(0)
# (i) closed form singular
L = 3
sing = (1 - F(1) / Lpow(L, s0)) == 0
# (ii) the Holder sum diverges
L = 2 ** 16
Sv, worst, ok = gateC(L, F(1, 4), s0)
fired_D = sing and (not ok) and Sv > 10 ** 6
say("sp1-D  CONTROL sigma=0: closed-form denominator zero = %s ; S(40)=%.6g worst ratio=%.6f gate=%s"
    % (sing, float(Sv), float(worst), "PASS" if ok else "FAIL"))
say("sp1-D  CONTROL -> %s" % ("FIRED" if fired_D else "DID NOT FIRE"))

# ---------------- sp1-E : designed-FAIL control, alpha = sigma -----------------------
say("")
fired_E = True
for s in [F(1, 2), F(1, 4)]:
    L = 2 ** 16
    Sv, worst, ok = gateC(L, s, s)
    fired_E = fired_E and (not ok)
    say("sp1-E  CONTROL alpha=sigma=%-4s S(40)=%.6g worst ratio=%.6f -> %s"
        % (s, float(Sv), float(worst), "FAIL (as designed)" if not ok else "PASS (control did NOT fire)"))
say("sp1-E  CONTROL -> %s" % ("FIRED" if fired_E else "DID NOT FIRE"))

say("")
say("SUMMARY: A=%s A'=%s B=%s C=%s | controls D=%s E=%s F=%s"
    % ("PASS" if not bad else "FAIL", "PASS" if not badp else "FAIL",
       "PASS" if allB else "FAIL", "PASS" if allC else "FAIL",
       "FIRED" if fired_D else "NOT FIRED", "FIRED" if fired_E else "NOT FIRED",
       "FIRED" if fired_F else "NOT FIRED"))

import sys
open(sys.argv[1], "w").write("\n".join(out) + "\n") if len(sys.argv) > 1 else None
