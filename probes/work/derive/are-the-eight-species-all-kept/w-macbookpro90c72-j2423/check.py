#!/usr/bin/env python3
"""J:derive:are-the-eight-species-all-kept:a2 -- worker w-macbookpro90c72-j2423 (claude-opus-5-5).

Sixteen branches of block 54's walk: can a supplied clause remove them, read them as one object, or let records tell
them apart; and a closed static system with both signs. All checks exact (sympy, Fractions, integer matrices).
"""
import itertools, sys, time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

T0 = time.time(); FAILS = []
def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)

I = sp.I
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]

# ------------------------------------------------------------------ E.gap: nothing in M2(C) gaps a species; senses cancel
Mx = sp.Matrix(2, 2, sp.symbols("a b c d"))
eqs = []
for s_ in sig:
    eqs += list(Mx * s_ + s_ * Mx)
good = sp.solve(eqs, list(Mx), dict=True) == [{v: 0 for v in Mx}]
species = list(itertools.product((0, 1), repeat=3))
senses = {n: (-1) ** sum(n) for n in species}                                   # det D_n, D = diag((-1)^{n_a})
good &= sum(senses.values()) == 0 and all(senses[tuple(1 - x for x in n)] == -senses[n] for n in species)
a0, a1, beta = sp.symbols("a0 a beta", real=True)
for n in species:
    ks = [sp.pi * x for x in n]
    Hk = (a0 + 2 * a1 * sum(sp.cos(k) for k in ks)) * sp.eye(2) + beta * sum((sp.sin(k) * s_ for k, s_ in zip(ks, sig)), sp.zeros(2, 2))
    ev = list(Hk.eigenvals().keys())
    good &= len(ev) == 1                                                        # the two coin states coincide: no gap at any species
# the staggered mass on the (n, nbar) pair at k = pi n: 4x4 block [[H_n, m],[m, H_nbar]] with H_n = H_nbar = 0 (the walk alone)
m = sp.symbols("m", positive=True)
blk = sp.zeros(4, 4); blk[0:2, 2:4] = m * sp.eye(2); blk[2:4, 0:2] = m * sp.eye(2)
good &= sorted(blk.eigenvals().items(), key=lambda t: sp.re(t[0])) == [(-m, 2), (m, 2)]
ok("E.gap", good, "no nonzero 2x2 matrix anticommutes with the coin's three matrices, and every term of the covariant nearest-neighbour "
   "family a0 + 2a sum cos k + beta sigma.sin k is scalar at the eight species points, so none of them gaps a species; the "
   "staggered mass pairs each species n with its opposite nbar = n + (1,1,1), of opposite sense (det D_nbar = -det D_n), and gaps "
   "the pair to +-m; the senses sum to zero (four of each)")

# ------------------------------------------------------------------ E.ops: what the staggered mass does (exact integer matrices, 4^3 torus)
L = 4; N3 = L ** 3
sites = list(itertools.product(range(L), repeat=3)); idx = {s_: i for i, s_ in enumerate(sites)}
def shift(a):
    T = np.zeros((N3, N3), dtype=np.int64)
    for s_ in sites:
        t = list(s_); t[a] = (t[a] + 1) % L
        T[idx[s_], idx[tuple(t)]] = 1                                           # (T psi)(x) = psi(x + e_a)
    return T
Ts = [shift(a) for a in range(3)]
twoS = [T - T.T for T in Ts]                                                    # 2i S_a (integer)
twoC = [T + T.T for T in Ts]                                                    # 2 C_a
sg = [np.array([[0, 1], [1, 0]], dtype=np.complex128), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], dtype=np.complex128)]
def kron(A, B):
    return np.kron(A.astype(np.complex128), B)
H2i = sum(kron(twoS[a], sg[a]) for a in range(3))                              # 2i H, entries in {0, +-1, +-i}
eps = np.diag([(-1) ** sum(s_) for s_ in sites]).astype(np.int64)
E2 = kron(eps, np.eye(2))
Sone = [kron(twoS[a], np.eye(2)) for a in range(3)]
Ptwo = [kron(twoS[a] @ twoC[a], np.eye(2)) for a in range(3)]                   # 4i S_a C_a
good = True
for a in range(3):
    good &= np.array_equal(E2 @ Sone[a] + Sone[a] @ E2, np.zeros_like(E2))     # eps anticommutes with the one-step momentum
    good &= np.array_equal(E2 @ Ptwo[a] - Ptwo[a] @ E2, np.zeros_like(E2))      # and commutes with the two-step one
good &= np.array_equal(E2 @ H2i + H2i @ E2, np.zeros_like(E2))                  # eps H eps = -H
# block 70's maps: V_n = R_n U_n with U_n = (-1)^{n.x}; V_n H V_n = s_n H but V_n (m eps) V_n = m eps
for n in [(1, 0, 0), (1, 1, 1), (1, 1, 0)]:
    Un = np.diag([(-1) ** sum(p * q for p, q in zip(n, s_)) for s_ in sites]).astype(np.int64)
    sn = (-1) ** sum(n)
    rho = [sn * (-1) ** n[a] for a in range(3)]                                 # rho_n = s_n D_n
    # the coin's half turn R_n with R sigma_a R^-1 = rho_a sigma_a: axis = the a with rho_a = +1 when exactly one, else identity
    plus = [a for a in range(3) if rho[a] == 1]
    Rn = sg[plus[0]] if len(plus) == 1 else np.eye(2, dtype=np.complex128)
    Vn = np.kron(Un.astype(np.complex128), Rn)
    good &= np.allclose(Vn @ H2i @ Vn.conj().T, sn * H2i, atol=0) and np.allclose(Vn @ E2 @ Vn.conj().T, E2, atol=0)
ok("E.ops", good, "on the 4^3 torus in exact integer arithmetic: the staggered term anticommutes with the walk and with each one-step "
   "momentum S_a (block 63's conserved current is lost) and commutes with each two-step momentum S_a C_a (block 69's survives); "
   "block 70's maps give V_n H V_n = s_n H but V_n eps V_n = eps, so for the four odd species H + m eps goes to -H + m eps: the "
   "odd maps and the energy reversal no longer map solutions to solutions")

# ------------------------------------------------------------------ E.map: sixteen components on the doubled lattice (exact)
Lc = L // 2
Had = np.array([[(-1) ** sum(p * q for p, q in zip(n, e)) for e in species] for n in species], dtype=np.int64)
good = np.array_equal(Had @ Had.T, 8 * np.eye(8, dtype=np.int64))
for n in species:
    psi = np.array([(-1) ** sum(p * q for p, q in zip(n, s_)) for s_ in sites], dtype=np.int64)     # the species' plane wave at k = pi n
    for y in itertools.product(range(Lc), repeat=3):
        block = np.array([psi[idx[tuple(2 * yy + ee for yy, ee in zip(y, e))]] for e in species])
        taste = Had @ block
        good &= all(taste[j] == (8 if species[j] == n else 0) for j in range(8))
ok("E.map", good, "the regrouping x = 2y + eta (eta in {0,1}^3) followed by the Hadamard transform over eta is unitary (H H^T = 8), and "
   "carries species n exactly to taste n at every coarse site: the sixteen branches become one C^2 (x) C^8 object per coarse site, "
   "which, read as a site, is a larger one-site algebra than M2(C) -- the parked decision; stopped there")

# ------------------------------------------------------------------ E.form: a formed record weighs both signs of energy equally
Hr = H2i                                                                        # 2i H; odd powers stay off the diagonal
good = True
v = np.zeros(2 * N3, dtype=np.complex128); v[2 * idx[(0, 0, 0)]] = 1; v[2 * idx[(0, 0, 0)] + 1] = 1
w_ = v.copy()
for k in range(1, 8):
    w_ = Hr @ w_
    if k % 2 == 1:
        good &= np.vdot(v, w_) == 0                                             # <H^k> = 0 for odd k: symmetric spectral measure
for n in species:
    psi = np.array([(-1) ** sum(p * q for p, q in zip(n, s_)) for s_ in sites])
    good &= abs(psi[idx[(0, 0, 0)]]) == 1                                       # every species overlaps a site equally
ok("E.form", good, "an amplitude localised at a site (a formed record's) has <H^k> = 0 for every odd k (the walk is bipartite with no "
   "on-site term), so its spectral measure is symmetric: it weighs both signs of energy equally and all eight species equally "
   "(each plane wave has modulus 1 at every site); a record, which reads only its site, cannot tell species or signs apart")

# ------------------------------------------------------------------ E.zero: a closed static system with both signs (curvature member)
nx, ny, nz = 5, 3, 3
bsites = list(itertools.product(range(nx), range(ny), range(nz))); bidx = {s_: i for i, s_ in enumerate(bsites)}; Nb = len(bsites)
def nbrs(s_):
    out = []
    for a in range(3):
        for d in (1, -1):
            t = list(s_); t[a] += d; t = tuple(t)
            out.append(bidx.get(t))
    return out
def lap_minus():                                                                # -Delta with zero walls
    A = [[Fr(0)] * Nb for _ in range(Nb)]
    for i, s_ in enumerate(bsites):
        A[i][i] = Fr(6)
        for j in nbrs(s_):
            if j is not None:
                A[i][j] -= 1
    return A
def solve(A, b):
    n = len(A); M_ = [row[:] + [bi] for row, bi in zip(A, b)]
    for c in range(n):
        p = next(r for r in range(c, n) if M_[r][c] != 0); M_[c], M_[p] = M_[p], M_[c]
        pv = M_[c][c]; M_[c] = [x / pv for x in M_[c]]
        for r in range(n):
            if r != c and M_[r][c] != 0:
                f = M_[r][c]; M_[r] = [x - f * y for x, y in zip(M_[r], M_[c])]
    return [M_[r][n] for r in range(n)]
def ldl_pivots(A):
    n = len(A); M_ = [row[:] for row in A]; piv = []
    for c in range(n):
        pv = M_[c][c]; piv.append(pv)
        if pv == 0:
            return piv
        for r in range(c + 1, n):
            if M_[r][c] != 0:
                f = M_[r][c] / pv; M_[r] = [x - f * y for x, y in zip(M_[r], M_[c])]
    return piv
Am = lap_minus()
x1, x2 = bidx[(1, 1, 1)], bidx[(3, 1, 1)]
g1 = solve(Am, [Fr(1) if i == x1 else Fr(0) for i in range(Nb)]); g2 = solve(Am, [Fr(1) if i == x2 else Fr(0) for i in range(Nb)])
Kc = Fr(1, 2); Q = Fr(1, 10)
chi = [1 + Q * (a - b) for a, b in zip(g1, g2)]                                 # Q1 = Q, Q2 = -Q: the walls' ledger 8K(Q1 + Q2) = 0
mu1, mu2 = Q * chi[x1], -Q * chi[x2]
Lm = [row[:] for row in Am]; Lm[x1][x1] += Q / chi[x1]; Lm[x2][x2] += -Q / chi[x2]
piv = ldl_pivots(Lm)
bw = [Fr(sum(1 for j in nbrs(s_) if j is None)) for s_ in bsites]              # walls held at N = 1
Nv = solve(Lm, bw)
good = min(chi) > 0 and all(p > 0 for p in piv) and min(Nv) > 0 and mu1 > 0 and mu2 < 0
# stationarity of block 60's bond-form ledger at every site (bodies at rest: e = m w at the bodies, tau = 0)
def lapv(f, wall):
    return [sum((f[j] if j is not None else wall) for j in nbrs(s_)) - 6 * f[i] for i, s_ in enumerate(bsites)]
lc, lN = lapv(chi, Fr(1)), lapv(Nv, Fr(1))
mz = {x1: 8 * Kc * mu1, x2: 8 * Kc * mu2}
for i in range(Nb):
    wv = Nv[i] / chi[i]; e = mz.get(i, Fr(0)) * wv
    good &= e + 8 * Kc * Nv[i] * lc[i] == 0                                    # dE/du_z = 0
    good &= 4 * Kc * (Nv[i] * lc[i] + chi[i] * lN[i]) == 0                      # dE/dlam_z = 0 (no hop energy)
good &= Q + (-Q) == 0 and mu1 + mu2 > 0
ok("E.zero", good, f"on a 5x3x3 box with held walls, a positive body at (1,1,1) and a negative one at (3,1,1) with charges Q1 = -Q2 = {Q}: "
   f"lengths chi = 1 + Q(g1 - g2) > 0 everywhere, bare energies m1 = 8K mu1 = {8 * Kc * mu1}, m2 = {8 * Kc * mu2} (K = 1/2), the "
   f"rates' operator -Lap + Q/chi positive definite (all {len(piv)} exact pivots > 0, block 71 T3(d)), rates N > 0 everywhere, "
   "block 60's bond-form ledger stationary at every site exactly, and the walls' ledger 8K(Q1 + Q2) = 0: a static closed system "
   "with both signs and total ledger zero, the positive body heavier in bare energy")
print(f"runtime {time.time() - T0:.0f} s")

if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PARTIAL no supplied clause removes branches (nothing in M2(C) gaps a species, a staggered mass gaps opposite-sense "
      "pairs and breaks the odd maps, records cannot tell species or signs apart, reading the sixteen as one object is the parked "
      "site-algebra decision); and a static closed system with a positive and a negative body has total ledger zero exactly")
print("HIT: in block 60's curvature member a positive and a negative body at rest with charges Q1 = -Q2 have walls' ledger "
      "8K(Q1 + Q2) = 0 and an exact static solution with positive lengths and rates (5x3x3 box, Q = 1/10: bare energies "
      f"{8 * Kc * mu1} and {8 * Kc * mu2}, rates' operator positive definite): with amplitudes of both signs the unit of rate can be "
      "a variable, as block 60 T1 allows only at total zero.")
print("HIT: no supplied clause removes any of the sixteen branches: in M2(C) no term anticommutes with the coin, so covariant "
      "nearest-neighbour terms are scalar at every species point; the staggered mass gaps species only in opposite-sense pairs "
      "(senses sum to zero) and breaks the odd species maps; a formed record weighs both signs and all species equally.")
