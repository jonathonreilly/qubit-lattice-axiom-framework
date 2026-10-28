#!/usr/bin/env python3
# gt1_price.py -- the carry-through arithmetic of GREENT.md section G3: the cell sum S_T of the Coulomb
# representative's profile, against NLOC.md's T^d (its unconditional route) and c_m (what a true (N-loc)
# would buy at the same rate).  Exact integer shell counts; scalar float elsewhere.  Milliseconds.
# No criterion is evaluated here: this is the arithmetic of a derived formula, reported as COMPUTED.
import math, sys
from fractions import Fraction

d = 4
# shell counts in Z^d, exact:  n(s) = sum_j 2^j C(d,j) C(s-1,j-1)
def comb(n, k):
    if k < 0 or n < 0 or k > n:
        return 0
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r
def nshell(s):
    if s == 0:
        return 1
    return sum((2 ** j) * comb(d, j) * comb(s - 1, j - 1) for j in range(1, d + 1))

def cm(mp):                       # sum_X exp(-mp |X|_1) = coth(mp/2)^d
    return (1.0 / math.tanh(mp / 2.0)) ** d
def cm1(mp):                      # sum_X (|X|_1 + d) exp(-mp |X|_1)
    w = math.exp(-mp)
    return cm(mp) * d * (1.0 + 2.0 * w / (1.0 - w * w))
_XI = {}
def xi_table(mp):
    "suffix sums  Xi(u) = sum_{s>u} n(s) e^{-mp s}, tabulated"
    if mp in _XI:
        return _XI[mp]
    S = int(120.0 / mp) + 20
    vals = [nshell(s) * math.exp(-mp * s) for s in range(S + 2)]
    suf = [0.0] * (S + 3)
    for s in range(S + 1, -1, -1):
        suf[s] = suf[s + 1] + vals[s]
    _XI[mp] = (S, suf)
    return _XI[mp]

def Xi(mp, u):
    S, suf = xi_table(mp)
    k = int(math.floor(u)) + 1
    return suf[k] if k <= S + 1 else 0.0

# Theorem GT-1/GT-2 constants in coarse l^1 form (GREENT.md section G2), rounded UP as reported there
C1l = 429.0
C2l = 27250.0
KS  = 8.0        # sup_N  s_{d-1}(N)/N  for Z^4 (s_3(1)=8, s_3(2)=6, -> 8/3); conservative

def pieces(mp):
    """coefficients of the profile, divided by M (which cancels in every ratio).
    cC  : sup-bound coefficient for the delta_x response (section G2.6)
    qn  : coefficient of D^{-d}          (the first-moment / Coulomb tail)
    qii : coefficient of D^{-(d-1)}Xi(D/2)
    qi  : coefficient of (D+4) e^{-3 mp D/4}"""
    z   = 1.0 + 16.0 * d + cm(mp)
    cC  = 2.0 * (d - 1) ** 2 * C1l * z
    cn  = 2.0 * (4.0 ** d) * d * (d - 1) ** 2 * C2l * cm1(mp)
    cii = (8.0 ** (d - 1)) * d * (d - 1) ** 2 * C1l
    ci  = 2.0 * KS * d * (d - 1) * C1l
    return cC, cn / cC, cii / cC, ci / cC

def cellsum(mp, T, verbose=False):
    cC, qn, qii, qi = pieces(mp)
    N = int(2 * T)                     # the l^1 radius of (Z/T)^d is d*T/2 = 2T at d=4
    s1 = max(int(qn ** (1.0 / d)) + 2, int(120.0 / mp) + 10)
    s1 = min(s1, N)
    def prof(s):
        return min(1.0, qn * max(1.0, float(s)) ** (-d)
                   + qii * max(1.0, float(s)) ** (-(d - 1)) * Xi(mp, s / 2.0)
                   + qi * (s + 4) * math.exp(-0.75 * mp * s))
    near = sum(nshell(s) * prof(s) for s in range(0, s1 + 1))
    sat = next((s for s in range(0, s1 + 1) if prof(s) < 1.0), None)
    g = 0.5772156649015329
    def H(n, p):
        if p == 1:
            return math.log(n) + g + 1.0 / (2.0 * n)
        tot = 0.0
        for i in range(1, min(n, 20000) + 1):
            tot += i ** (-p)
        if n > 20000:
            tot += 1.0 / ((p - 1) * 20000.0 ** (p - 1))
        return tot
    def Hr(a, b, p):
        return H(b, p) - H(a, p) if b > a else 0.0
    # beyond s1 only the power term survives (the exponential parts are < 1e-40 there)
    tail = qn * ((8.0 / 3.0) * (Hr(s1, N, 1) - 6 * Hr(s1, N, 2) + 11 * Hr(s1, N, 3) - 6 * Hr(s1, N, 4))
                 + 16.0 * (Hr(s1, N, 2) - 3 * Hr(s1, N, 3) + 2 * Hr(s1, N, 4))
                 + 24.0 * (Hr(s1, N, 3) - Hr(s1, N, 4)) + 8.0 * Hr(s1, N, 4))
    if verbose:
        print("   mp=%.4f qn=%.4g s_sat=%s s1=%d near=%.5g tail=%.5g" % (mp, qn, sat, s1, near, tail))
    return near + tail, (qn, qii, qi, s1, sat)

def main():
    out = []; P = out.append
    P("gt1_price.py -- GREENT.md section G3 arithmetic.  COMPUTED (exact shell counts, scalar floats).")
    P("Theorem GT-1/GT-2 constants used (coarse l^1 form, as REPORTED in section G2): C_1^(1)=%.0f C_2^(1)=%.0f"
      % (C1l, C2l))
    T0 = 1.2932e7
    P("")
    for mp, lab in ((0.0384, "PROVEN rate m_*' (kappa=1, L=3)"), (1.0, "LOCATED rate (NOT proven)")):
        P("=== %s : m' = %.4f ===" % (lab, mp))
        P("   c_m = sum_X e^{-m'|X|_1} = coth(m'/2)^4            = %.6g" % cm(mp))
        P("   c_m^(1) = sum_X (|X|_1+4) e^{-m'|X|_1}             = %.6g   (ratio to c_m: %.4g)"
          % (cm1(mp), cm1(mp) / cm(mp)))
        S, (qn, qii, qi, s1, sat) = cellsum(mp, T0, verbose=True)
        P("   profile coefficients:  q_n = %.6g   q_ii = %.6g   q_i = %.6g ; profile falls below 1 at shell s = %s" % (qn, qii, qi, sat))
        P("   CELL SUM  S_T  at T = T_0 = 1.2932e7               = %.6g" % S)
        P("   NLOC.md Corollary NL-4 cell sum  T^d               = %.6g" % (T0 ** 4))
        P("   a true (N-loc) at this rate      c_m               = %.6g" % cm(mp))
        P("   GAIN over NLOC's T^d : %.4g      COST over an ideal (N-loc): %.4g"
          % (T0 ** 4 / S, S / cm(mp)))
        # how the cell sum scales with T (is it really a log?)
        for Tt in (1e3, 1e5, 1e7, 1.2932e7, 1e9, 1e12):
            Sx, _ = cellsum(mp, Tt)
            P("     T = %-10.4g  S_T = %-14.6g   S_T / log(2T) = %.6g" % (Tt, Sx, Sx / math.log(2 * Tt)))
        P("")
    txt = "\n".join(out)
    print(txt)
    with open(sys.argv[1] if len(sys.argv) > 1 else "gt1_price_out.txt", "w") as f:
        f.write(txt + "\n")

if __name__ == "__main__":
    main()
