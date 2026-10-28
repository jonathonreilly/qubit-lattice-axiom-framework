#!/usr/bin/env python3
"""r55t_checks.py -- REVIEW55_TENT (batch C7) exact checks.

Criteria: checks/r55t_criteria.md (written and stat'ed BEFORE this file existed).
Exact arithmetic only: fractions.Fraction and ints. No numpy, no BLAS, no floats in any verdict.
Built from the SOURCE definitions (BFT_A l.599, l.1872; LINEAR_PACKAGE §1.2; BFT_B l.2024), not from
any reviewed worker's script (none of tq1/ys1/fb1/gs1/cf1/rev8 was read or run).
Usage: python3 -I r55t_checks.py   (prints a verdict line per clause)
"""
import itertools
import random
from fractions import Fraction as F

L = 3
M = (L - 1) // 2
VERDICTS = []


def verdict(cid, ok, note=""):
    VERDICTS.append((cid, ok))
    print(f"{cid}: {'PASS' if ok else 'FAIL'}  {note}")


def unit(d, mu):
    return tuple(1 if i == mu else 0 for i in range(d))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scal(c, a):
    return tuple(c * x for x in a)


def clean(dct):
    return {k: v for k, v in dct.items() if v != 0}


def accum(dct, key, val):
    dct[key] = dct.get(key, 0) + val


# ---------------- exterior calculus (BFT_A l.1872 conventions) ----------------
def d0(lam, d, sites):
    """(d lambda)(z, mu) = lambda(z + e_mu) - lambda(z), for z in sites (lam: dict, default 0)."""
    out = {}
    for z in sites:
        for mu in range(d):
            v = lam.get(add(z, unit(d, mu)), 0) - lam.get(z, 0)
            if v != 0:
                out[(z, mu)] = v
    return out


def dstar1(v, d):
    """(d* v)(z) = sum_mu [v(z - e_mu, mu) - v(z, mu)]."""
    out = {}
    for (z, mu), a in v.items():
        if a == 0:
            continue
        accum(out, add(z, unit(d, mu)), a)
        accum(out, z, -a)
    return clean(out)


def dstar_plaquette(zp, al, be, d):
    """d* of the unit 2-form delta at plaquette (zp; al<be), G_{al be}(zp) = 1, G_{be al} = -1.
    (d*G)_nu(z) = sum_mu [G_{mu nu}(z - e_mu) - G_{mu nu}(z)]."""
    out = {}
    # nu = be, mu = al: G_{al be}(z - e_al) - G_{al be}(z)
    accum(out, (add(zp, unit(d, al)), be), 1)
    accum(out, (zp, be), -1)
    # nu = al, mu = be: G_{be al}(z - e_be) - G_{be al}(z) = -G_{al be}(z - e_be) + G_{al be}(z)
    accum(out, (add(zp, unit(d, be)), al), -1)
    accum(out, (zp, al), 1)
    return clean(out)


# ---------------- straight average Q_str (BFT_A l.599) ----------------
def qstr(v, d):
    """(Q_str v)(Y, m) = L^{-d} sum_{r in [0,L)^d} sum_{j<L} v(L Y + r + j e_m, m)."""
    out = {}
    w = F(1, L ** d)
    for (z, m), a in v.items():
        for j in range(L):
            zz = sub(z, scal(j, unit(d, m)))
            Y = tuple(c // L for c in zz)  # floor division: r = zz - L*Y in [0, L)
            accum(out, (Y, m), a * w)
    return clean(out)


# ---------------- slice functional h (LINEAR_PACKAGE §1.2) ----------------
def axial_path(c, y, order, d):
    """Links (with signs) of the complete-axial path from c to y moving coordinates in `order`."""
    pos = list(c)
    links = []
    for mu in order:
        while pos[mu] < y[mu]:
            links.append(((tuple(pos), mu), 1))
            pos[mu] += 1
        while pos[mu] > y[mu]:
            pos[mu] -= 1
            links.append(((tuple(pos), mu), -1))
    assert tuple(pos) == tuple(y)
    return links


def h_kernel_rel(d, orders, root_off):
    """Kernel of h at one block, relative to the block corner: block = [0,L)^d, root = root_off*1.
    Returns dict ((site_rel_to_corner), mu) -> coefficient; h(w)(Y) = sum K[(o,mu)] w(L*Y + o, mu)."""
    K = {}
    c = tuple([root_off] * d)
    norm = F(1, len(orders) * L ** d)
    for y in itertools.product(range(L), repeat=d):
        for order in orders:
            for (b, s) in axial_path(c, y, order, d):
                accum(K, b, s * norm)
    return clean(K)


def apply_h(K, w, Y, d):
    corner = scal(L, Y)
    tot = F(0)
    for (o, mu), coef in K.items():
        a = w.get((add(corner, o), mu))
        if a:
            tot += coef * a
    return tot


def off(l, root_off):
    """Level-0 (or level-i) coordinate offset of the root: root_off*(L^l - 1)/(L - 1)."""
    return root_off * (L ** l - 1) // (L - 1)


def funnel_terms(v, k, d, orders, root_off):
    """phi_{i+1} = h_i(Q_str^{(0->i)} v)(Y_{i+1}), Y_{i+1} = level-(i+1) site that is the root of X = 0.
    In level-(i+1) coordinates Y_{i+1} = off(k-i-1)*1, whose root in level-i coords is off(k-i)*1."""
    K = h_kernel_rel(d, orders, root_off)
    terms = []
    w = dict(v)
    for i in range(k):
        Y = tuple([off(k - i - 1, root_off)] * d)
        terms.append(apply_h(K, w, Y, d))
        w = qstr(w, d)
    return terms


ALL4 = list(itertools.permutations(range(4)))
FIX4 = [tuple(range(4))]


def witness(k, d, root_off, normalise=True):
    cx = tuple([off(k, root_off)] * d)
    zp = add(cx, unit(d, 0))
    u = dstar_plaquette(zp, 0, 1, d)
    if normalise:
        u = {key: F(val, 2 * d) for key, val in u.items()}
    return u


def part_A():
    print("=== Part A: funnel, d = 4, L = 3 ===")
    d = 4
    # A1
    t2 = funnel_terms(witness(2, d, M), 2, d, ALL4, M)
    P2 = sum(t2)
    print(f"  order-averaged, k=2: phi = {t2}, Phi_2 = {P2}")
    ok1 = (t2[0] == F(-1, 432) and t2[1] == F(-17, 104976) and P2 == F(-65, 26244))
    verdict("A1", ok1, f"phi_1={t2[0]} phi_2={t2[1]} Phi_2={P2}")
    # A2
    ok2 = True
    for k in (3, 4):
        tk = funnel_terms(witness(k, d, M), k, d, ALL4, M)
        print(f"  order-averaged, k={k}: phi = {tk}, Phi_k = {sum(tk)}")
        ok2 &= (tk[0] == F(-1, 432) and tk[1] == F(-17, 104976)
                and all(t == 0 for t in tk[2:]) and sum(tk) == F(-65, 26244))
    verdict("A2", ok2, "termination phi_i = 0 for i >= 3 at k = 3, 4")
    # A3
    ok3 = True
    for k in (1, 2, 3):
        cx = tuple([off(k, M)] * d)
        v = {}
        for mu in range(d):
            accum(v, (sub(cx, unit(d, mu)), mu), 1)
            accum(v, (cx, mu), -1)
        val = sum(funnel_terms(v, k, d, ALL4, M))
        exp = F(1, 3 ** (4 * k)) - 1
        print(f"  Phi_{k}(d delta_c)(c) = {val}; 3^(-4k)-1 = {exp}")
        ok3 &= (val == exp)
    verdict("A3", ok3, "Phi_k(d delta_c)(c) = 3^{-4k} - 1 (k-dependent)")
    # A4 measurement
    Kav = h_kernel_rel(d, ALL4, M)
    Kfx = h_kernel_rel(d, FIX4, M)
    mav, sav = max(abs(x) for x in Kav.values()), sum(abs(x) for x in Kav.values())
    mfx, sfx = max(abs(x) for x in Kfx.values()), sum(abs(x) for x in Kfx.values())
    print(f"  h_0 kernel order-averaged: max|c| = {mav}, sum|c| = {sav}")
    print(f"  h_0 kernel fixed order    : max|c| = {mfx}, sum|c| = {sfx}")
    print(f"  T6 collision real (max differs): {mav != mfx};  2d*max|c|: avg {2 * d * mav}, fixed {2 * d * mfx}")
    # support check: all kernel links have both endpoints in the block [0,L)^d
    def inblock(K):
        for (o, mu) in K:
            e = add(o, unit(d, mu))
            if not (all(0 <= c < L for c in o) and all(0 <= c < L for c in e)):
                return False
        return True
    print(f"  kernels supported on block-interior links: avg {inblock(Kav)}, fixed {inblock(Kfx)}")
    verdict("A4", sav == F(8, 3) and sfx == F(8, 3), f"sum|c| avg={sav} fixed={sfx}")
    # A5 measurement
    t2f = funnel_terms(witness(2, d, M), 2, d, FIX4, M)
    print(f"  A5 fixed-order (0123), k=2: phi = {t2f}, Phi_2 = {sum(t2f)}; differs from A1: {t2f != t2}")
    # also the k=3 fixed-order value, to see whether the fixed-order funnel terminates too
    t3f = funnel_terms(witness(3, d, M), 3, d, FIX4, M)
    print(f"  A5 fixed-order (0123), k=3: phi = {t3f}, Phi_3 = {sum(t3f)}")
    # A6 controls
    t2c = funnel_terms(witness(2, d, 0), 2, d, ALL4, 0)
    c_a = not (t2c[0] == F(-1, 432) and t2c[1] == F(-17, 104976) and sum(t2c) == F(-65, 26244))
    t2u = funnel_terms(witness(2, d, M, normalise=False), 2, d, ALL4, M)
    c_b = not (t2u[0] == F(-1, 432) and t2u[1] == F(-17, 104976) and sum(t2u) == F(-65, 26244))
    print(f"  A6(a) corner roots: phi = {t2c}, Phi = {sum(t2c)} -> A1 fails: {c_a}")
    print(f"  A6(b) no 1/8: phi = {t2u}, Phi = {sum(t2u)} -> A1 fails: {c_b}")
    verdict("A6", c_a and c_b, "designed-FAIL controls fired" if (c_a and c_b) else "a control did NOT fire")
    # A7 implementation cross-checks
    rnd = random.Random(20261028)
    ok7 = True
    for trial in range(5):
        lam = {z: rnd.randint(-9, 9) for z in itertools.product(range(-1, 2 * L + 1), repeat=d)}
        sites = list(itertools.product(range(-1, 2 * L), repeat=d))
        dl = d0(lam, d, sites)
        for K, lab in ((Kav, "avg"), (Kfx, "fixed")):
            for Y in [tuple([0] * d), unit(d, 0)]:
                lhs = apply_h(K, dl, Y, d)
                corner = scal(L, Y)
                blk = [add(corner, r) for r in itertools.product(range(L), repeat=d)]
                rhs = F(sum(lam[z] for z in blk), L ** d) - lam[add(corner, tuple([M] * d))]
                ok7 &= (lhs == rhs)
        # Q_str(d lambda)(Y, m) = A lambda(Y + e_m) - A lambda(Y) at Y = 0
        qd = qstr(dl, d)
        for m in range(d):
            Y = tuple([0] * d)
            Yp = unit(d, m)
            Al = lambda Yy: F(sum(lam[add(scal(L, Yy), r)] for r in itertools.product(range(L), repeat=d)), L ** d)
            ok7 &= (qd.get((Y, m), 0) == Al(Yp) - Al(Y))
    verdict("A7", ok7, "h_0(d lam) = mean - root value (both operators); Q_str d = d A")
    return t2, t2f


# ---------------- Part B: quintic tents and QFALSE ----------------
def sig5(tau):
    if tau >= 1:
        return F(0)
    return 1 - 10 * tau ** 3 + 15 * tau ** 4 - 6 * tau ** 5


def part_B_case(d, n, scale):
    """scale = tent half-width (n for the real tent, n - 1 for the control)."""
    s = {t: sig5(F(abs(t), scale)) for t in range(-n - 2, n + 3)}
    R = range(-n - 1, n + 2)
    chi = {}
    for z in itertools.product(R, repeat=d):
        p = F(1)
        for c in z:
            p *= s[c]
            if p == 0:
                break
        if p != 0:
            chi[z] = p
    # B1: total variation by brute force over links
    tv = F(0)
    j0 = {}
    for z in itertools.product(range(-n - 1, n + 1), repeat=d):
        cz = chi.get(z, 0)
        for mu in range(d):
            dz = chi.get(add(z, unit(d, mu)), 0) - cz
            if dz != 0:
                tv += abs(dz)
                j0[(z, mu)] = 1 if dz > 0 else -1
    D = dstar1(j0, d)
    Qbox = sum(chi.get(z, 0) * val for z, val in D.items())
    maxD = max(abs(x) for x in D.values())
    isroot = lambda z: all(c % n == 0 for c in z)
    Dperp = {z: val for z, val in D.items() if not isroot(z)}
    q_perp = sum(chi.get(z, 0) * val for z, val in Dperp.items())
    maxDp = max(abs(x) for x in Dperp.values())
    Rratio = F(abs(q_perp)) / (n * maxDp)
    return tv, Qbox, maxD, D.get(tuple([0] * d), 0), q_perp, maxDp, Rratio


def part_B():
    print("=== Part B: TENTQ QFALSE ===")
    ok1 = ok2 = ok3 = ok4 = ok5 = True
    for d, ks in ((2, (1, 2, 3)), (4, (1, 2))):
        for k in ks:
            n = L ** k
            tv, Qb, mD, D0, qp, mDp, Rr = part_B_case(d, n, n)
            tgt = 2 * d * n ** (d - 1)
            print(f"  d={d} k={k} n={n}: TV={tv} (2d n^(d-1)={tgt}) Qbox={Qb} maxD={mD} D(c)={D0} "
                  f"<chi,D_perp>={qp} ||D_perp||={mDp} R={Rr} = {Rr.numerator}/{Rr.denominator}; "
                  f"n^2-1={n*n-1}, n^(d-2)-1/n={F(n**(d-2)) - F(1, n)}")
            ok1 &= (tv == tgt)
            ok2 &= (Qb == tgt)
            ok3 &= (mD == 2 * d)
            if d == 4:
                ok4 &= (Rr >= n * n - 1)
            # B5: 1-D partition of unity (the d-dim one is its product)
            s = {t: sig5(F(abs(t), n)) for t in range(-3 * n, 3 * n + 1)}
            for t in range(-n, n + 1):
                ok5 &= (sum(s.get(t - m * n, 0) for m in range(-2, 3)) == 1)
    verdict("B1", ok1, "||d chi^5||_1 = 2d n^{d-1}")
    verdict("B2", ok2, "box sum <chi^5, d* j0> = 2d n^{d-1}")
    verdict("B3", ok3, "||D||_inf = 2d exactly")
    verdict("B4", ok4, "NEUT-box ratio >= n^2 - 1 (d=4)")
    verdict("B5", ok5, "partition of unity (1-D factor)")
    # B6 control: tent scale n - 1
    d, k = 4, 1
    n = L ** k
    tv, Qb, *_ = part_B_case(d, n, n - 1)
    fired = (tv != 2 * d * n ** (d - 1))
    print(f"  B6 control (scale n-1, d=4, n=3): TV = {tv} vs 2d n^(d-1) = {2*d*n**(d-1)}")
    verdict("B6", fired, "control fired (B1 fails under corruption)" if fired else "control did NOT fire")


# ---------------- Part C: bootstrap algebra ----------------
def solve(A, b):
    n = len(A)
    Mx = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if Mx[r][c] != 0)
        Mx[c], Mx[p] = Mx[p], Mx[c]
        for r in range(n):
            if r != c and Mx[r][c] != 0:
                f = Mx[r][c] / Mx[c][c]
                Mx[r] = [x - f * y for x, y in zip(Mx[r], Mx[c])]
    return [Mx[i][n] / Mx[i][i] for i in range(n)]


def part_C():
    print("=== Part C: bootstrap algebra ===")
    G = [[F(0), F(-1, 2)], [F(0), F(1, 2)]]
    a = [F(1), F(1)]
    IminusG = [[(1 if i == j else 0) - G[i][j] for j in range(2)] for i in range(2)]
    y = solve(IminusG, a)
    verdict("C1", y == [F(0), F(2)], f"y = {y}")
    rnd = random.Random(1028)
    ok = True
    worst = None
    for trial in range(200):
        eps = [F(1, 2), F(1, 4), F(1, 10)][trial % 3]
        n = 4
        G = []
        for i in range(n):
            g = [rnd.randint(-5, 5) for _ in range(n)]
            ssum = sum(abs(x) for x in g)
            frac = F(rnd.randint(0, 10), 10)
            G.append([F(x) * eps * frac / ssum if ssum else F(0) for x in g])
        a = [F(rnd.randint(-20, 20), rnd.randint(1, 5)) for _ in range(n)]
        z = [F(rnd.randint(-20, 20), rnd.randint(1, 5)) for _ in range(n)]
        IminusG = [[(1 if i == j else 0) - G[i][j] for j in range(n)] for i in range(n)]
        y = solve(IminusG, [a[i] + z[i] for i in range(n)])
        Mv = max(abs(t) for t in y)
        A = max(abs(t) for t in a)
        B = max(abs(t) for t in z)
        lo = (A - B) / (1 + eps)
        hi = (A + B) / (1 - eps)
        if not (Mv >= lo and Mv <= hi):
            ok = False
            worst = (trial, Mv, lo, hi)
    verdict("C2", ok, "M >= (A-B)/(1+eps) and M <= (A+B)/(1-eps) on 200 exact instances" + (f" VIOLATION {worst}" if worst else ""))
    y = solve([[F(3, 2)]], [F(1)])
    verdict("C3", y == [F(2, 3)], f"scalar G=-1/2: y = {y[0]} a")


# ---------------- Part D: arithmetic and rigorous log intervals ----------------
def ln_interval(x, N=120):
    """Rigorous [lo, hi] for ln x, x > 1 rational: 2 atanh(t), t = (x-1)/(x+1), N terms + remainder."""
    x = F(x)
    assert x > 1
    t = (x - 1) / (x + 1)
    s = F(0)
    tp = t
    for j in range(N):
        s += tp / (2 * j + 1)
        tp *= t * t
    lo = 2 * s
    rem = 2 * tp / ((2 * N + 1) * (1 - t * t))  # tp = t^{2N+1}
    return lo, lo + rem


def iadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def part_D():
    print("=== Part D: arithmetic ===")
    diff = F(24768, 10 ** 7) - F(65, 26244)
    verdict("D1", diff > 0, f"0.0024768 - 65/26244 = {diff}")
    ok2 = (F(1, 54) / F(130, 6561) == F(243, 260) and F(1, 54) / F(65, 26244) == F(486, 65)
           and F(1, 432) / F(65, 26244) == F(243, 260))
    verdict("D2", ok2, "243/260, mixed 486/65")
    ok3 = all(F(1, 3) * sum(3 ** (3 * (k - i)) for i in range(k)) == F(9, 26) * (27 ** k - 1) for k in range(1, 7))
    d3 = F(3462, 10000) - F(9, 26)
    verdict("D3", ok3 and d3 > 0, f"(1/3)sum = (9/26)(n^3-1) k<=6: {ok3}; 0.3462 - 9/26 = {d3}")
    verdict("D4", 8 * F(65, 26244) == F(130, 6561), "8*65/26244 = 130/6561")
    ln2 = ln_interval(2)
    ln54 = ln_interval(F(5, 4))
    ln10 = (3 * ln2[0] + ln54[0], 3 * ln2[1] + ln54[1])
    ln32 = ln_interval(F(3, 2))
    ln3 = iadd(ln2, ln32)
    ln307_250 = ln_interval(F(307, 250))
    ln_q = iadd(ln2, ln307_250)  # ln(307/125)
    lg3 = (ln3[0] / ln10[1], ln3[1] / ln10[0])
    lgq = (ln_q[0] / ln10[1], ln_q[1] / ln10[0])
    Dd = (152 - lgq[1], 152 - lgq[0])
    ks = ((3 + Dd[0] / lg3[1]) / 2, (3 + Dd[1] / lg3[0]) / 2)
    kd = ((3 + Dd[0] / (2 * lg3[1])) / 2, (3 + Dd[1] / (2 * lg3[0])) / 2)
    fmt = lambda iv: f"[{float(iv[0]):.9f}, {float(iv[1]):.9f}]"  # display only
    print(f"  log10 3 in {fmt(lg3)}; D in {fmt(Dd)}; k* in {fmt(ks)}; k*_double in {fmt(kd)}")
    ok5 = (ks[0] >= F(16037, 100) and ks[1] <= F(16039, 100) and kd[0] >= F(8093, 100) and kd[1] <= F(8095, 100))
    refute817 = (kd[1] < F(8165, 100))
    verdict("D5", ok5, f"k* and k*_double intervals; FACEB 81.7 refuted: {refute817}")


# ---------------- Part E: top-level root charges, d = 2, k = 1 ----------------
def part_E():
    print("=== Part E: root map and top-level root charges, d = 2, L = 3, k = 1 ===")
    d = 2
    orders = list(itertools.permutations(range(d)))
    K = h_kernel_rel(d, orders, M)

    def Q_row(Y, mu):
        """Kernel of (Q A)(Y, mu) = (Q_str A)(Y, mu) - h(A)(Y + e_mu) + h(A)(Y) on level-0 links."""
        row = {}
        w = F(1, L ** d)
        for r in itertools.product(range(L), repeat=d):
            y0 = add(scal(L, Y), r)
            for j in range(L):
                accum(row, (add(y0, scal(j, unit(d, mu))), mu), w)
        for (o, nu), c in K.items():
            accum(row, (add(scal(L, add(Y, unit(d, mu))), o), nu), -c)
            accum(row, (add(scal(L, Y), o), nu), c)
        return clean(row)

    root = lambda Y: add(scal(L, Y), tuple([M] * d))
    rnd = random.Random(7)
    ok1 = True
    for trial in range(5):
        lam = {z: rnd.randint(-9, 9) for z in itertools.product(range(-5, 11), repeat=d)}
        for Y in itertools.product(range(-1, 2), repeat=d):
            for mu in range(d):
                row = Q_row(Y, mu)
                lhs = F(0)
                for (z, nu), c in row.items():
                    lhs += c * (lam[add(z, unit(d, nu))] - lam[z])
                rhs = lam[root(add(Y, unit(d, mu)))] - lam[root(Y)]
                ok1 &= (lhs == rhs)
    verdict("E1", ok1, "root covariance Q(d lambda) = d(ev lambda)")

    def D_of_QT(Bform):
        S = {}
        for (Y, mu), b in Bform.items():
            for key, c in Q_row(Y, mu).items():
                accum(S, key, b * c)
        return dstar1(clean(S), d)

    # E2: a single level-1 link (not co-closed at level 1)
    Bl = {((0, 0), 0): F(1)}
    DS = D_of_QT(Bl)
    dB = dstar1(Bl, d)  # level-1 function
    evT = {root(Y): v for Y, v in dB.items()}
    off_root = {z: v for z, v in DS.items() if z not in evT}
    print(f"  E2: D(Q^T B) = {DS}; ev^T d*B = {evT}; nonzero off roots: {off_root}")
    gs_base_reading = (len(DS) == 0)
    verdict("E2", gs_base_reading,
            "GS-BASE reading (D == 0 incl. roots) " + ("holds" if gs_base_reading else
            f"FAILS: D(Q^T B) = ev^T d*B exactly: {DS == evT}; vanishes off roots ((cc)): {len(off_root) == 0}"))
    # E3 control: co-closed B (boundary of a level-1 plaquette)
    Bp = dstar_plaquette((0, 0), 0, 1, d)
    DS3 = D_of_QT({k: F(v) for k, v in Bp.items()})
    verdict("E3", len(DS3) == 0, f"co-closed B gives D(Q^T B) = {DS3}")


if __name__ == "__main__":
    part_A()
    part_B()
    part_C()
    part_D()
    part_E()
    print("=== SUMMARY ===")
    for cid, ok in VERDICTS:
        print(f"{cid} {'PASS' if ok else 'FAIL'}")
