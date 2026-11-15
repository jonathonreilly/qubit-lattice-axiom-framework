# ru55_3: U1 arithmetic (criteria: checks/ru55_3_criteria.md, written first). Fractions; rigorous log enclosures; floats display-only.
from fractions import Fraction as F
from math import isqrt

GRAN = 10 ** 45


def _down(q):
    return F((q.numerator * GRAN) // q.denominator, GRAN)


def _up(q):
    return F(-((-q.numerator * GRAN) // q.denominator), GRAN)


def _ln_m(m, n=48):
    """rigorous enclosure of ln m for a Fraction m in [1, 2]"""
    z = (m - 1) / (m + 1)
    z2 = z * z
    s, p = F(0), z
    for j in range(n):
        s += p / (2 * j + 1)
        p *= z2
    s *= 2
    rem = 2 * p / ((2 * n + 1) * (1 - z2))  # p = z^(2n+1)
    return _down(s), _up(s + rem)


LN2 = _ln_m(F(2))


def ln_enc(x):
    x = F(x)
    assert x > 0
    k = x.numerator.bit_length() - x.denominator.bit_length()
    m = x / F(2) ** k
    while m >= 2:
        m /= 2; k += 1
    while m < 1:
        m *= 2; k -= 1
    lo, hi = _ln_m(m)
    if k >= 0:
        return lo + k * LN2[0], hi + k * LN2[1]
    return lo + k * LN2[1], hi + k * LN2[0]


def idiv(a, b):
    """[a]/[b] with b > 0"""
    (a0, a1), (b0, b1) = a, b
    assert b0 > 0
    c = [a0 / b0, a0 / b1, a1 / b0, a1 / b1]
    return min(c), max(c)


LN10 = ln_enc(10)


def log10_enc(x):
    return idiv(ln_enc(x), LN10)


def disp(iv, nd=6):
    return f"[{float(iv[0]):.{nd}f}, {float(iv[1]):.{nd}f}]"


A_d, n_P = 9, 1296
c_pr = F(1, 640 * 53 ** 2)
eps1 = F(67, 10 ** 41)
DX = F(25, 10 ** 153)  # 2.5e-152, divided by C_Omega below
LAMS = [("3.17e-3", F(317, 10 ** 5)), ("4.23e-3", F(423, 10 ** 5)), ("6.6e-10 [sensitivity: L0-1]", F(66, 10 ** 11))]


def b1(k):
    return n_P + 1200 * k


def entries(N, kappa, lam):
    eq = F(1, 256 * N * A_d)  # eta_q/eps_1
    sig2 = 16 / lam
    aJ = kappa / F(2048 * N)
    afl = 49 * eq ** 2 / (1024 * sig2)
    ag = kappa / F(256 * N * N * b1(kappa))
    return aJ, afl, ag


def solve_t(a, P, lnC, lo=F(10) ** 60, hi=F(10) ** 130, steps=70):
    """geometric bisection on integers for a*t = (P/2) ln t + lnC; returns (t_lo, t_hi) with F(t_lo)<0<=F(t_hi) rigorously"""
    def sign(t):
        l0, l1 = ln_enc(t)
        fhi = a * t - F(P, 2) * l0 - lnC
        flo = a * t - F(P, 2) * l1 - lnC
        if fhi < 0:
            return -1
        if flo >= 0:
            return 1
        return 0
    tl, th = int(lo), int(hi)
    assert sign(tl) == -1 and sign(th) == 1
    for _ in range(steps):
        mid = isqrt(tl * th)
        if mid <= tl or mid >= th:
            break
        s = sign(mid)
        if s == -1:
            tl = mid
        elif s == 1:
            th = mid
        else:
            break
    return F(tl), F(th)


def main():
    ok_all, ctrl = True, True
    print("ru55_3: U1 arithmetic (Fractions; rigorous log enclosures; floats display-only)")
    print(f"K4: ln 10 in {disp(LN10, 20)}; width {float(LN10[1] - LN10[0]):.2e}")
    k4 = LN10[0] <= F(2302585092994045684, 10 ** 18) <= LN10[1] and (LN10[1] - LN10[0]) < F(1, 10 ** 30)
    print(f"K4: contains 2.302585092994045684 and width < 1e-30: {k4}")
    ctrl &= k4
    a_bad = c_pr * eps1 ** 2
    print(f"a_bad = c_pr eps_1^2 = {float(a_bad):.6e} (display)")
    # U1-1, U1-2
    u11 = True
    afl_store = {}
    for N in (2, 3):
        for kappa in (F(1), F(1, 4)):
            for name, lam in LAMS:
                aJ, afl, ag = entries(N, kappa, lam)
                binds = afl < min(aJ, ag)
                u11 &= binds
                afl_store[(N, kappa, name)] = afl
                print(f"U1-1 N={N} kappa={kappa} lam_min={name}: a_J={float(aJ):.4e} a_fl={float(afl):.4e} a_gamma={float(ag):.4e} "
                      f"(units eps_1^2) -> a_fl binds: {binds}; a_ret^PLD/a_bad = {afl / c_pr} (display {float(afl / c_pr):.4e})")
    print(f"U1-1: {'PASS' if u11 else 'FAIL'}")
    ok_all &= u11
    tgt = [((2, F(1), "3.17e-3"), F(4465, 10 ** 16), F(8027, 10 ** 10)), ((2, F(1), "4.23e-3"), F(5958, 10 ** 16), F(1071, 10 ** 9))]
    u12 = True
    for key, t_afl, t_ratio in tgt:
        afl = afl_store[key]
        r1 = abs(afl / t_afl - 1) <= F(1, 1000)
        r2 = abs((afl / c_pr) / t_ratio - 1) <= F(1, 1000)
        u12 &= r1 and r2
        print(f"U1-2 {key}: a_fl/eps^2 = {float(afl):.6e} vs {float(t_afl):.4e}: {r1}; ratio {float(afl / c_pr):.6e} vs {float(t_ratio):.4e}: {r2}")
    l01 = afl_store[(2, F(1), "3.17e-3")] / afl_store[(2, F(1), "6.6e-10 [sensitivity: L0-1]")]
    print(f"U1-2: {'PASS' if u12 else 'FAIL'}; L0-1 factor a_fl(3.17e-3)/a_fl(6.6e-10) = {l01} (display {float(l01):.6e})")
    ok_all &= u12
    # U1-3
    print()
    u13 = True
    for (N, kappa) in ((2, F(1)), (2, F(1, 4)), (3, F(1)), (3, F(1, 4))):
        for name, lam in LAMS:
            afl = afl_store[(N, kappa, name)]
            a_ret = afl * eps1 ** 2
            for COm in (F(1), F(3 * (N * N - 1), 2)):
                t = COm / DX
                B = a_ret * t
                Lt = ln_enc(t)
                Pmax = idiv((2 * B, 2 * B), Lt)
                lnCmax = (B - 6 * Lt[1], B - 6 * Lt[0])
                print(f"U1-3 N={N} kappa={kappa} lam={name} C_Om={COm}: B = a_ret t_DX = {float(B):.4e}; ln t_DX in {disp(Lt, 4)}; "
                      f"P_max(lnC=0) in [{float(Pmax[0]):.4e}, {float(Pmax[1]):.4e}]; lnC_max(P=12) >= {float(lnCmax[0]):.4e}")
    # envelope tests at N=2, kappa=1, C_Om=1
    def holds(lam_name, P, lnC):
        a_ret = afl_store[(2, F(1), lam_name)] * eps1 ** 2
        t = F(1) / DX
        Lt = ln_enc(t)
        cost_hi = lnC + F(P, 2) * Lt[1]
        mono = t >= F(P) / (2 * a_ret)
        return cost_hi <= a_ret * t, mono
    e1 = holds("3.17e-3", 10 ** 58, F(10) ** 60)
    e2 = holds("6.6e-10 [sensitivity: L0-1]", 10 ** 51, F(10) ** 53)
    print(f"U1-3 envelope (i) lam=3.17e-3, (P, lnC) = (1e58, 1e60): holds {e1[0]}, premise t_DX >= P/(2a_ret) {e1[1]}")
    print(f"U1-3 envelope (ii) lam=6.6e-10, (P, lnC) = (1e51, 1e53): holds {e2[0]}, premise {e2[1]}")
    u13 = e1[0] and e1[1] and e2[0] and e2[1]
    k1 = holds("3.17e-3", 10 ** 62, F(0))
    print(f"K1: P = 1e62, lnC = 0, lam=3.17e-3: holds {k1[0]} -> {'FAILS (as designed)' if not k1[0] else 'CONTROL DOES NOT FIRE'}")
    ctrl &= not k1[0]
    print(f"U1-3: {'PASS' if u13 else 'FAIL'}")
    ok_all &= u13
    # U1-4
    print()
    a_ret0 = afl_store[(2, F(1), "3.17e-3")] * eps1 ** 2
    print(f"U1-4: a_ret^PLD(eps_1 = 6.7e-40, N=2, kappa=1, lam=3.17e-3) = {float(a_ret0):.6e} (display)")
    res = {}
    margins_pos = True
    for (p, lnC, lab) in ((6, F(0), "E3"), (6, F(50), "E3"), (12, F(0), "E3"), (12, F(50), "E3"), (702, F(10) ** 5, "ILLUSTRATIVE")):
        tl, th = solve_t(a_ret0, 12 + p, lnC)
        g2 = (1 / th, 1 / tl)
        lg = (log10_enc(g2[0])[0], log10_enc(g2[1])[1])
        marg = (log10_enc(g2[0] / DX)[0], log10_enc(g2[1] / DX)[1])
        margins_pos &= marg[0] > 0
        res[(p, lnC)] = g2
        print(f"U1-4 p(SC)={p} lnC={float(lnC):g} [{lab}]: g^2_delta in [{float(g2[0]):.6e}, {float(g2[1]):.6e}]; log10 {disp(lg, 4)}; "
              f"margin over DX'(C_Om=1) {disp(marg, 4)} decades")
    pld = [F(103, 10 ** 96), F(100, 10 ** 96), F(771, 10 ** 97), F(756, 10 ** 97)]
    mine = [res[(6, F(0))], res[(6, F(50))], res[(12, F(0))], res[(12, F(50))]]
    rep = all(abs((m[0] + m[1]) / 2 / t - 1) <= F(2, 100) for m, t in zip(mine, pld))
    print(f"U1-4 reproduction of PLD p4 E3 (order (6,0),(6,50),(12,0),(12,50)) within 2%: {'PASS' if rep else 'FAIL'}")
    ok_all &= rep
    # U1-5
    print()
    L12800 = ln_enc(12800)
    L43 = ln_enc(F(4, 3))
    D0 = (L12800[0] + 324 * L43[0], L12800[1] + 324 * L43[1])
    D1 = (D0[0] + 38417, D0[1] + 38417)
    thetas = [("1/24 (route iii sup)", F(1, 24)), ("1/15000 (route iv)", F(1, 15000)),
              ("a_ret/a_bad (route ii fallback)", afl_store[(2, F(1), "3.17e-3")] / c_pr)]
    rows = {}
    for tname, th in thetas:
        a = th * a_bad
        for dname, D in (("100 (l.617 form)", (F(100), F(100))), ("B_0=0", D0), ("B_0=1", D1)):
            g2 = (a / D[1], a / D[0])
            marg = (log10_enc(g2[0] / DX)[0], log10_enc(g2[1] / DX)[1])
            margins_pos &= marg[0] > 0
            rows[(tname, dname)] = (g2, marg)
            print(f"U1-5 theta={tname}, D={dname}: g^2_H in [{float(g2[0]):.6e}, {float(g2[1]):.6e}]; margin over DX'(C_Om=1) {disp(marg, 6)} decades")
    m100 = rows[("1/24 (route iii sup)", "100 (l.617 form)")][1]
    rep1 = abs((m100[0] + m100[1]) / 2 - F(63619267, 10 ** 6)) <= F(1, 10 ** 6)
    gB1 = rows[("1/24 (route iii sup)", "B_0=1")][0]
    gB0 = rows[("1/24 (route iii sup)", "B_0=0")][0]
    rep2 = abs(gB1[0] / F(270, 10 ** 93) - 1) <= F(1, 100)
    rep3 = abs(gB0[0] / F(101, 10 ** 90) - 1) <= F(1, 100)
    print(f"U1-5 reproduction: +63.619267 (l.617 form, theta=1/24): {rep1}; 2.70e-91 (B_0=1): {rep2}; 1.01e-88 (B_0=0): {rep3}")
    ok_all &= rep1 and rep2 and rep3
    k2 = (rows[("1/24 (route iii sup)", "B_0=0")][1][0] - rows[("1/24 (route iii sup)", "B_0=1")][1][1]) > 2
    print(f"K2: B_0=0 vs B_0=1 margins differ by > 2 decades: {k2} -> {'as designed' if k2 else 'CONTROL DOES NOT FIRE'}")
    ctrl &= k2
    print(f"sign gate (U1-4 and U1-5 margins all > 0): {'PASS' if margins_pos else 'a NEGATIVE margin exists (finding)'}")
    # U1-6
    print()
    th, lam = F(1, 24), F(1, 2)
    kmin = 256 * th * c_pr / lam
    u16a = kmin == F(1, 84270)
    first, second = lam * F(1) / (256 * c_pr), 6 * th
    u16b = (second < first) and min(first, second) == F(1, 4)
    print(f"U1-6: kappa_min = 256 theta c_pr/lambda = {kmin} == 1/84270: {u16a}; a_A/a_bad at kappa=1: min({first}, {second}) = {min(first, second)} "
          f"(6theta binds: {second < first}) -> {'PASS' if (u16a and u16b) else 'FAIL'}")
    ok_all &= u16a and u16b
    lamK = F(1, 10 ** 6)
    k3 = lamK / (256 * c_pr) < 6 * th
    print(f"K3: lambda = 1e-6: lambda kappa/(256 c_pr) = {lamK / (256 * c_pr)} < 6 theta = {6 * th}: {k3} -> {'flips (as designed)' if k3 else 'CONTROL DOES NOT FIRE'}")
    ctrl &= k3
    print(f"\nGATES: {'all PASS' if ok_all else 'NOT all PASS'}; CONTROLS: {'all as designed' if ctrl else 'NOT all as designed -> UNABLE TO DECIDE'}")


if __name__ == "__main__":
    main()
