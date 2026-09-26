#!/usr/bin/env python3
"""Finite-coupling corrections for block 142's excluded nearest-neighbour pair -- worker w-macbookpro9927a-jce96.

Recovery of block 142 (PR #9227 frozen head 5c7c52847e; landed on main). Coin-blind bond term V = g sum_bonds 1.
Families (see ATTEMPT.md):
  R  reproduction: block 142's same-bond law, no link between a bond's two ends, the coin-blind rest levels and
     axis sums (fermions 7/10, 3/2, -1/2, -17/10; bosons 3/2, 1/2, -5/2).
  F  the Feshbach reduction: odd orders vanish, ||H2(K)|| <= 2 sqrt 3, and the window/contraction/tail constants
     that control the levels for |g| >= 20.
  X  the expansion algebra: E^2/2 - g^2/2 is the spectrum of Omega = L2 + (L4 - L2^2/2)/g^2 to O(g^-4).
  N  the next order: [L2(0), Delta(0)] = 0, level shifts delta, and the O(g^-2) axis-sum corrections.
  I  at a rest point the inertial K^2-form of E is the energy-squared form divided by E0.
  C  [float, labelled] exact diagonalisation of the pair in a box at g = 20 against the expansion.
Families R, F, X, N, I are exact (integers, fractions, sympy). Laurent matrices hold Gaussian integers.
"""
import sys
from itertools import product

import numpy as np
import sympy as sp

FAILS = []


def ok(tag, cond, msg=""):
    if not cond:
        FAILS.append(tag)
    print(f"{tag} {'ok' if cond else 'FAIL'} {msg}".rstrip())


# ------------------------------------------------------------------ the exact engine
S0 = np.eye(2, dtype=complex)
PAULI = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]], dtype=complex),
         np.array([[1, 0], [0, -1]], dtype=complex)]
SWAP = np.zeros((4, 4), dtype=complex)
for i in range(4):
    for j in range(4):
        if i // 2 == j % 2 and i % 2 == j // 2:
            SWAP[i, j] = 1
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
BONDS = [e for a in range(3) for e in (E3[a], tuple(-x for x in E3[a]))]
ZERO = (0, 0, 0)


def unit(a, p):
    t = [0, 0, 0]
    t[a] = p
    return tuple(t)


def hop_terms(a, sgn):
    """<r|H2|r + sgn e_a> times 2i (block 142's matrices, record 1's coin first), u_a = exp(i K_a / 2)."""
    A = np.kron(PAULI[a], S0)
    B = np.kron(S0, PAULI[a])
    if sgn > 0:
        return [(unit(a, 1), A), (unit(a, -1), -B)]
    return [(unit(a, -1), -A), (unit(a, 1), B)]


def paths(source, nsteps):
    """sum over paths of <r_n|H2|r_{n-1}>...<r_1|H2|source> times (2i)^n; intermediates avoid bonds and 0."""
    cur = {source: {ZERO: np.eye(4, dtype=complex)}}
    bset = set(BONDS)
    for step in range(nsteps):
        nxt = {}
        for r, L in cur.items():
            for a in range(3):
                for sgn in (1, -1):
                    rp = tuple(r[i] - (sgn if i == a else 0) for i in range(3))
                    if rp == ZERO or (step < nsteps - 1 and rp in bset):
                        continue
                    tgt = nxt.setdefault(rp, {})
                    for ex, M in L.items():
                        for eh, H in hop_terms(a, sgn):
                            k = tuple(x + y for x, y in zip(ex, eh))
                            tgt[k] = tgt[k] + H @ M if k in tgt else H @ M
        cur = nxt
    return cur


def lam_blocks(n):
    out = {}
    for s in BONDS:
        P = paths(s, n)
        for t in BONDS:
            if t in P:
                out[(t, s)] = P[t]
    return out


def sector(blocks, sign):
    out = {}
    for a in range(3):
        for b in range(3):
            ea, eb = E3[a], E3[b]
            meb = tuple(-x for x in eb)
            for key, fac in (((ea, eb), None), ((ea, meb), sign)):
                if key not in blocks:
                    continue
                for ex, M in blocks[key].items():
                    MM = M if fac is None else fac * (M @ SWAP)
                    big = out.setdefault(ex, np.zeros((12, 12), dtype=complex))
                    big[4 * a:4 * a + 4, 4 * b:4 * b + 4] += MM
    return out


def gauss_int(M):
    Mr, Mi = np.round(M.real), np.round(M.imag)
    assert np.array_equal(M, Mr + 1j * Mi) and np.abs(M).max() < 2**40
    return Mr, Mi


def derivs(L, p, d):
    """exact sympy M(0), dM/dK_d(0), d2M/dK_d2(0) from a Laurent matrix scaled by (2i)^p."""
    n = next(iter(L.values())).shape[0]
    out = [sp.zeros(n, n) for _ in range(3)]
    for ex, M in L.items():
        Mr, Mi = gauss_int(M)
        Ms = sp.Matrix(n, n, lambda i, j: sp.Integer(int(Mr[i, j])) + sp.I * sp.Integer(int(Mi[i, j])))
        w = sp.I * sp.Rational(ex[d], 2)
        out[0] += Ms
        out[1] += Ms * w
        out[2] += Ms * w**2
    sc = (2 * sp.I)**p
    return [m / sc for m in out]


L2, L4 = lam_blocks(2), lam_blocks(4)
L3, L5 = lam_blocks(3), lam_blocks(5)

# ------------------------------------------------------------------ family R
kr = np.kron
form = {ZERO: 2.5 * np.eye(4)}
for a, c in ((0, -0.25), (1, -0.5), (2, -0.5)):      # cos K = (u^2 + u^-2)/2
    for s in (2, -2):
        form[unit(a, s)] = c * kr(PAULI[a], PAULI[a])
got = {k: v / (2j)**2 for k, v in L2[(E3[0], E3[0])].items()}
law_ok = set(got) == set(form) and all(np.array_equal(got[k], form[k]) for k in form)
ends_ok = all((tuple(-x for x in e), e) not in L2 and (tuple(-x for x in e), e) not in L4 for e in E3)
ok("R1", law_ok and ends_ok and len(L3) == 0 and len(L5) == 0,
   "Lambda2(e1,e1) = 5/2 - 1/2 cos K1 s1s1 - cos K2 s2s2 - cos K3 s3s3 exactly (block 142 T2); no path joins "
   "e_a to -e_a at orders 2 and 4; odd orders 3 and 5 are empty")

SECT = {}
for sign, nm in ((-1, "fermions"), (1, "bosons")):
    S2, S4 = sector(L2, sign), sector(L4, sign)
    per = {}
    for d in range(3):
        A0, A1, A2 = derivs(S2, 2, d)
        B0, B1, B2 = derivs(S4, 4, d)
        per[d] = (A0, A1, A2, B0 - A0 * A0 / 2, B1 - (A1 * A0 + A0 * A1) / 2,
                  B2 - (A2 * A0 + 2 * A1 * A1 + A0 * A2) / 2)
    A0, D0 = per[0][0], per[0][3]
    levels = []
    for val, mult, vecs in A0.eigenvects():
        levels.append((sp.nsimplify(val), sp.Matrix.hstack(*sp.GramSchmidt(vecs, True))))
    levels.sort(key=lambda x: float(x[0]))
    SECT[nm] = (per, levels, A0, D0)

res = {}
for nm, (per, levels, A0, D0) in SECT.items():
    rows = []
    for (w, q) in levels:
        dl = (q.H * D0 * q).applyfunc(sp.nsimplify)
        dsc = dl[0, 0]
        scal = (dl - dsc * sp.eye(dl.shape[0])).applyfunc(sp.simplify) == sp.zeros(*dl.shape)
        R = sp.zeros(12, 12)
        Rp = sp.zeros(12, 12)
        for (w2, q2) in levels:
            if w2 == w:
                continue
            d2 = sp.nsimplify((q2.H * D0 * q2)[0, 0])
            R += q2 * q2.H / (w - w2)
            Rp += q2 * q2.H * (dsc - d2) / (w - w2)**2
        t2 = sp.zeros(q.shape[1], q.shape[1])
        t4 = sp.zeros(q.shape[1], q.shape[1])
        first = True
        for d in range(3):
            a0, a1, a2, d0, d1, dd = per[d]
            first &= (q.H * a1 * q).applyfunc(sp.simplify) == sp.zeros(q.shape[1], q.shape[1])
            first &= (q.H * d1 * q).applyfunc(sp.simplify) == sp.zeros(q.shape[1], q.shape[1])
            t2 += q.H * (a2 + 2 * a1 * R * a1) * q
            t4 += q.H * (dd + 2 * (a1 * R * d1 + d1 * R * a1) - 2 * a1 * Rp * a1) * q
        e2 = sorted(sp.nsimplify(k) for k, v in t2.applyfunc(sp.nsimplify).eigenvals().items() for _ in range(v))
        e4 = sorted(sp.nsimplify(k) for k, v in t4.applyfunc(sp.nsimplify).eigenvals().items() for _ in range(v))
        rows.append((w, q.shape[1], dsc, scal, first, e2, e4))
    res[nm] = rows

f_rows, b_rows = res["fermions"], res["bosons"]
f_lead = [r[5] for r in f_rows]
b_lead = [r[5] for r in b_rows]
ok("R2", [(r[0], r[1]) for r in f_rows] == [(0, 3), (1, 3), (4, 3), (5, 3)]
   and [(r[0], r[1]) for r in b_rows] == [(1, 3), (2, 6), (5, 3)]
   and f_lead == [[sp.Rational(7, 10)] * 3, [sp.Rational(3, 2)] * 3, [sp.Rational(-1, 2)] * 3, [sp.Rational(-17, 10)] * 3]
   and b_lead == [[sp.Rational(3, 2)] * 3, [sp.Rational(1, 2)] * 6, [sp.Rational(-5, 2)] * 3],
   "coin-blind rest levels of Lambda2(0): fermions 0,1,4,5 (x3); bosons 1 (x3), 2 (x6), 5 (x3); leading axis sums "
   "7/10, 3/2, -1/2, -17/10 and 3/2, 1/2, -5/2: block 142 T3(c)'s coin-blind rows")

# ------------------------------------------------------------------ family F
h2 = 12                                   # (2 sqrt 3)^2: |s(k)|^2 <= 3 for each record, ||h(q)|| <= 2 sqrt 3
g0, win = 20, 1
q_ = sp.Rational(h2, (g0 - win)**2)       # 12/E^2 with |E| >= 19
Gnorm = sp.Rational(h2, g0 - win) / (1 - q_)
Lip = q_ * (1 + q_) / (1 - q_)**2
tail_const = sp.Integer(h2)**3 / (1 - q_) / (1 - Lip)
ok("F1", Gnorm < 1 and Lip < 1 and tail_const < 1860 and sp.sqrt(12) < sp.Rational(7, 2),
   f"|g| >= 20, |E - g| <= 1: ||G(E)|| <= {Gnorm} < 1 (window kept), ||G'(E)|| <= {Lip} < 1 "
   f"(contraction); the 12 levels of each sector are the fixed points E = g + gamma_j(E), within "
   f"{float(tail_const):.0f}/(|g|-1)^5 of the Lambda4-truncated ones, uniformly in K")

# ------------------------------------------------------------------ family X
g, lam, lam1, om, dl = sp.symbols('g lambda lambda1 omega delta', real=True)
x = sp.symbols('x', positive=True)          # x = 1/g
Ex = (1 + sp.sqrt(1 + 4 * lam * x**2)) / (2 * x)          # root of E(E - g) = lambda near g
half = sp.series((Ex**2 - 1 / x**2) / 2, x, 0, 4).removeO()
Eser = sp.series(Ex.subs(lam, om + (dl + om**2 / 2) * x**2), x, 0, 4).removeO()
ok("X1", sp.simplify(half - (lam - lam**2 * x**2 / 2)) == 0
   and sp.simplify(Eser - (1 / x + om * x + (dl - om**2 / 2) * x**3)) == 0,
   "E(E - g) = lambda gives E^2/2 - g^2/2 = lambda - lambda^2/(2g^2) + O(g^-4); with lambda = eig(L2 + L4/g^2) "
   "this is the spectrum of Omega = L2 + (L4 - L2^2/2)/g^2, and E0 = g + omega/g + (delta - omega^2/2)/g^3")

# ------------------------------------------------------------------ family N
comm_ok = all(((A0 * D0 - D0 * A0).applyfunc(sp.simplify) == sp.zeros(12, 12)) for (_, _, A0, D0) in SECT.values())
shifts_f = [r[2] for r in f_rows]
shifts_b = [r[2] for r in b_rows]
scal_ok = all(r[3] and r[4] for r in f_rows + b_rows)
ok("N1", comm_ok and scal_ok and shifts_f == [0, sp.Rational(9, 2), 8, sp.Rational(-15, 2)]
   and shifts_b == [sp.Rational(9, 2), 6, sp.Rational(-15, 2)],
   "[Lambda2(0), Delta(0)] = 0; Delta(0) is scalar on each rest level: delta = 0, 9/2, 8, -15/2 (fermions), "
   "9/2, 6, -15/2 (bosons); first-order K terms vanish at both orders")
f4 = [r[6] for r in f_rows]
b4 = [r[6] for r in b_rows]
want_f4 = [[sp.Rational(6, 5)] * 3, [sp.Rational(-21, 2), sp.Rational(3, 2), sp.Rational(3, 2)],
           [sp.Integer(-12)] * 3, [sp.Rational(123, 10)] * 3]
want_b4 = [[sp.Rational(-5, 2)] * 3, [sp.Integer(-7)] * 6, [sp.Rational(31, 2)] * 3]
ok("N2", f4 == want_f4 and b4 == want_b4,
   "O(g^-2) axis-sum corrections: fermions 6/5; {3/2, 3/2, -21/2}; -12; 123/10 -- bosons -5/2; -7; 31/2. The "
   "fermion 3/2 level reaches 3/2 + 3/(2g^2) on two states")

# ------------------------------------------------------------------ family I
t = sp.symbols('t', real=True)
Xf = sp.Function('X')
Et = sp.sqrt(g**2 + 2 * Xf(t))
inertia = sp.simplify(sp.diff(Et, t, 2).subs(t, 0) - sp.diff(Xf(t), t, 2).subs(t, 0) / Et.subs(t, 0)
                      + (sp.diff(Xf(t), t).subs(t, 0))**2 / Et.subs(t, 0)**3)
ok("I1", inertia == 0,
   "E = sqrt(g^2 + 2X): E'' = X''/E0 - X'^2/E0^3, so at a rest point (X' = 0) the inertial K^2-form of E is the "
   "energy-squared form W divided by E0, at every order in 1/g")

# ------------------------------------------------------------------ family C [float]
Rb = 3
sites = [r for r in product(range(-Rb, Rb + 1), repeat=3) if r != ZERO]
idx = {r: i for i, r in enumerate(sites)}
nb = 4 * len(sites)
X = np.zeros((nb, nb))
for r in sites:
    i, j = idx[r], idx[tuple(-y for y in r)]
    X[4 * j:4 * j + 4, 4 * i:4 * i + 4] = SWAP.real


def box(K, gg):
    H = np.zeros((nb, nb), dtype=complex)
    for r in sites:
        i = idx[r]
        for a in range(3):
            for sgn in (1, -1):
                rp = tuple(r[k] + (sgn if k == a else 0) for k in range(3))
                if rp in idx:
                    j = idx[rp]
                    H[4 * i:4 * i + 4, 4 * j:4 * j + 4] += sum(M * np.exp(1j * np.dot(ex, K) / 2)
                                                               for ex, M in hop_terms(a, sgn)) / (2j)
        if r in BONDS:
            H[4 * i:4 * i + 4, 4 * i:4 * i + 4] += gg * np.eye(4)
    return H


gg = 20.0
worst_o, worst_l = 0.0, 1.0
for K in (np.zeros(3), np.array([0.3, 0.2, -0.1])):
    Hb = box(K, gg)
    for sign in (-1, 1):
        Ps = (np.eye(nb) + sign * X) / 2
        w = np.linalg.eigvalsh(Ps @ Hb @ Ps)
        near = np.sort(w[np.abs(w - gg) < 2])
        A = sum(M * np.exp(1j * np.dot(ex, K) / 2) for ex, M in sector(L2, sign).items()) / (2j)**2
        B = sum(M * np.exp(1j * np.dot(ex, K) / 2) for ex, M in sector(L4, sign).items()) / (2j)**4
        Om = A + (B - A @ A / 2) / gg**2
        pred = np.sort(np.sqrt(gg**2 + 2 * np.linalg.eigvalsh((Om + Om.conj().T) / 2)))
        lead = np.sort(np.sqrt(gg**2 + 2 * np.linalg.eigvalsh((A + A.conj().T) / 2)))
        worst_o = max(worst_o, np.abs(near - pred).max())
        worst_l = min(worst_l, np.abs(near - lead).max())
ok("C1", worst_o < 1e-4 < 3e-4 < worst_l,
   f"[float] 3^3-box exact diagonalisation at g = 20, K = 0 and (0.3, 0.2, -0.1), both sectors: 12 levels each; "
   f"|E - Omega prediction| <= {worst_o:.1e}, while the leading order misses by >= {worst_l:.1e}")

print(f"checks: {'all passed' if not FAILS else 'FAILED ' + ' '.join(FAILS)}")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
    sys.exit(1)
print("SUMMARY: PARTIAL coin-blind excluded pair on Z^3: exact Feshbach control of the levels for |g| >= 20, "
      "the exact g^-3 term and the first finite-coupling curvature corrections; block 142's axis-sum bound 3/2 "
      "is exceeded at next order on two fermion states")
print("HIT: Block 142's excluded pair, coin-blind bond term g: the exact Feshbach series F(E) = g + L2/E + L4/E^3 "
      "+ ... (odd orders vanish, ||H2(K)|| <= 2 sqrt 3) puts the 12 levels of each exchange sector in |E - g| <= 1 "
      "for |g| >= 20, within 1856/(|g|-1)^5 of the L4-truncated levels, for every K. To relative order g^-2, "
      "E^2/2 - g^2/2 is the spectrum of L2 + (L4 - L2^2/2)/g^2 (L4 by exact path enumeration): rest values omega "
      "+ delta/g^2, (omega, delta) = (0,0), (1,9/2), (4,8), (5,-15/2) for fermions, (1,9/2), (2,6), (5,-15/2) for "
      "bosons; curvature axis sums 7/10 + 6/(5g^2), 3/2 + {3/2, 3/2, -21/2}/g^2, -1/2 - 12/g^2, -17/10 + "
      "123/(10g^2) (fermions), 3/2 - 5/(2g^2), 1/2 - 7/g^2, -5/2 + 31/(2g^2) (bosons). So the bound 3/2 holds "
      "at leading order only: two fermion states reach 3/2 + 3/(2g^2).")
