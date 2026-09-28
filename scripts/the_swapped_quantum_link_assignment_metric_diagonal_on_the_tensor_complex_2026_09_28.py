#!/usr/bin/env python3
"""The swapped quantum-link assignment on the tensor complex: the metric diagonal.

Question (probe 14's open route 1; the panel's T1, 2026-09-28): make the metric
the diagonal variable instead of the momentum. Does the obstruction go away,
or does it move?

Construction (supplied, not adopted): every tensor slot is a spin S with
h = S^z in the canonical slot coordinates q = (h_xx, h_yy, h_zz, 2h_xy,
2h_yz, 2h_xz). The scalar rule C_y = (S h)_y is diagonal and linear: an exact
Gauss law. The momentum-rule (linearised diffeomorphism) gauge shifts h along
g = G^T delta; its quantum-link strings are V_g = prod (S^{sign g})^{|g|},
whose entries have magnitude 1, so any S >= 1/2 carries them. Kinetic terms
are moves: shift monomials along patterns r with S r = 0 (so they commute with
the Gauss law).

Checks:
  A  construction: the landed lattice Einstein-Hilbert form X (2026-09-24
     symbol, assembled in real space on the torus) is real, symmetric and
     obeys X G^T = 0 exactly; so X(m + g) = X(m) for every integer m and every
     gauge pattern g, and [X(S^z), V_g] = 0 exactly (strong invariance); the
     Gauss law commutes with every V_g (S G^T = 0); the pattern entries have
     magnitude 1.
  B  dual moment lemma (the landed 2026-09-14 E-character bound, re-verified
     on a box): every finitely supported r with S r = 0 has vanishing zeroth
     moments; its first moments span 8 dimensions: 3 pure gauge (invisible to
     the transverse-traceless (TT) channel) and 5 more that are TT-visible.
  C  dual sum rule: for a shift monomial T along r and a diagonal observable
     A = a.S^z, [[T + T^dag, A], A^dag] = |a.r|^2 (T + T^dag) (operator
     identity on spin-1/2 and spin-1 toys). Hence a Hamiltonian of diagonal
     terms and such moves (fixed range, uniform norms, term-by-term
     sector-preserving) has TT metric f-sum m1(q) <= C_K q^2 in a ground state:
     two powers of q below Einstein's O(1), which needs an ultralocal kinetic
     term.
  D  harmonic comparators, reduced to the two TT modes: (i) the swapped
     assignment (moves from the box kernel, E-H potential) and (ii) probe 14's
     assignment (DeWitt kinetic term, moves from the ker G box kernel) both
     give omega ~ q^2; (iii) the non-compact comparator (DeWitt + E-H) gives
     omega ~ q. In both finite-slot assignments the move-built side is q^2
     below Einstein's.
  F  soft scalar law (re-verifies the landed 2026-09-14 penalty block
     B_tt = -g k^2 + 2 V k^4): replacing the exact Gauss law by an energy penalty
     U (S h)^2 lets single-slot moves supply an O(1) kinetic term, but E-H
     plus the penalty has a negative eigenvalue ~ -c q^2 below |q| ~ sqrt(c/U)
     for every finite U (the conformal mode), mirroring probe 13's DeWitt
     penalty statement.
  E  gauge side at finite S: gauge strings overlapping with opposite signs do
     not commute; a move sharing a slot with a gauge string cannot commute
     with both V_g and V_g^dag (toys); only diagonal terms invariant under the
     gauge shifts commute exactly. So exact invariance of the kinetic moves
     under the momentum-rule gauge holds only in the rotor limit.
Reference only: Chandrasekharan and Wiese (hep-lat/9609042); Xu (2006) and
Pretko (2017) rank-2 rotor models. Pre-registered in the probe's scratch file
(PASS iff some Gauss-law-compatible move has a TT-visible zeroth moment).
Prints one line per check, the N5 lines and TOTAL.
"""
import itertools
import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 900
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


rng = np.random.default_rng(20260928)
E3 = np.eye(3, dtype=int); FACE = {(0, 1): 3, (1, 2): 4, (0, 2): 5}; FI = {v: k for k, v in FACE.items()}


def offset(a):
    if a < 3:
        return np.zeros(3)
    i, j = FI[a]
    return (E3[i] + E3[j]) / 2


def S_row(x):
    x = np.array(x); d = {}
    def add(c, a, v): d[(tuple(c), a)] = d.get((tuple(c), a), 0) + v
    for j in range(3):
        for i in range(3):
            if i != j:
                add(x + E3[i], j, 1); add(x - E3[i], j, 1); add(x, j, -2)
    for (i, j), f in FACE.items():
        add(x, f, -1); add(x - E3[i], f, 1); add(x - E3[j], f, 1); add(x - E3[i] - E3[j], f, -1)
    return d


def G_row(x, j):
    x = np.array(x); d = {}
    def add(c, a, v): d[(tuple(c), a)] = d.get((tuple(c), a), 0) + v
    add(x + E3[j], j, 1); add(x, j, -1)
    for i in range(3):
        if i != j:
            f = FACE[tuple(sorted((i, j)))]; add(x, f, 1); add(x - E3[i], f, -1)
    return d


# ---------------------------------------------------------------- the landed lattice E-H symbol and its real-space stencil
def Xr(q):                 # 2026-09-24 oscillator note symbol, midpoint convention, q-coordinates
    K = 2 * np.sin(q / 2); X = np.zeros((6, 6)); fc = {3: (0, 1), 4: (1, 2), 5: (0, 2)}
    for a in range(3):
        for b in range(3):
            if a != b:
                X[a, b] = -K[3 - a - b] ** 2
    for a in range(3):
        for f, (i, jj) in fc.items():
            if a not in (i, jj):
                X[a, f] = X[f, a] = K[i] * K[jj]
    for f, (i, jj) in fc.items():
        X[f, f] = K[3 - i - jj] ** 2 / 2
        for g, (kk, l) in fc.items():
            if g != f:
                sh = set((i, jj)) & set((kk, l)); X[f, g] = -K[(set((i, jj)) - sh).pop()] * K[(set((kk, l)) - sh).pop()] / 2
    return X


# stencil by exact inverse transform on a 6^3 grid of half-integer displacements (K_i K_j has shifts +-1/2 per direction)
Ng = 8; grid = [2 * np.pi * np.array(n) / Ng for n in itertools.product(range(Ng), repeat=3)]
Xq = [Xr(q) for q in grid]
stencil = {}
for a in range(6):
    for b in range(6):
        for dd in itertools.product(np.arange(-1.5, 1.51, 0.5), repeat=3):
            d = np.array(dd)
            if not np.allclose((offset(b) - offset(a) - d) % 1, 0):
                continue
            c = sum(Xq[t][a, b] * np.exp(-1j * grid[t] @ d) for t in range(len(grid))) / len(grid)
            if abs(c) > 1e-12:
                stencil[(a, b, dd)] = c
stencil_real = max(abs(c.imag) for c in stencil.values()) < 1e-12
stencil_halves = all(abs(2 * c.real - round(2 * c.real)) < 1e-12 for c in stencil.values())

# torus matrices
L = 4
cells = list(itertools.product(range(L), repeat=3)); cidx = {c: i for i, c in enumerate(cells)}; nslot = 6 * len(cells)
def sl(c, a):
    return 6 * cidx[tuple(np.array(c).astype(int) % L)] + a
Xt = np.zeros((nslot, nslot))
for c in cells:
    for (a, b, dd), v in stencil.items():
        tgt = np.array(c) + offset(a) + np.array(dd) - offset(b)
        Xt[sl(c, a), sl(np.round(tgt).astype(int), b)] += v.real
Gt = np.zeros((3 * len(cells), nslot), dtype=int); St = np.zeros((len(cells), nslot), dtype=int)
for c in cells:
    for j in range(3):
        for (cc, a), v in G_row(c, j).items():
            Gt[3 * cidx[c] + j, sl(cc, a)] += v
    for (cc, a), v in S_row(c).items():
        St[cidx[c], sl(cc, a)] += v
gpats = [Gt[r].copy() for r in range(Gt.shape[0])]                           # gauge patterns g = G^T delta (rows of G)
XG = np.abs(Xt @ Gt.T).max(); Xsym = np.abs(Xt - Xt.T).max(); SG = np.abs(St @ Gt.T).max()
okX = True
for g in gpats:
    for _ in range(5):
        m = rng.integers(-3, 4, size=nslot).astype(float)
        okX &= abs((m + g) @ Xt @ (m + g) - m @ Xt @ m) < 1e-9
gmag = sorted(set(abs(int(v)) for g in gpats for v in g if v))
# symbol consistency at a torus momentum
qt = 2 * np.pi * np.array([1, 2, 1]) / L
phase = np.array([np.exp(-1j * qt @ (np.array(c) + offset(a))) for c in cells for a in range(6)])
Bq = np.array([[phase[i] if i % 6 == a else 0 for i in range(nslot)] for a in range(6)])
sym_ok = np.allclose(Bq.conj() @ Xt @ Bq.T / len(cells), Xr(qt), atol=1e-12)
check("A: construction: the landed E-H form, assembled in real space, is real, symmetric, in (1/2)Z and obeys X G^T = 0 exactly, so X(m + g) = X(m) for integer m and every gauge pattern g, and [X(S^z), V_g] = 0 strongly; the scalar Gauss law commutes with every V_g (S G^T = 0); gauge patterns have entries of magnitude 1 (any S >= 1/2)",
      stencil_real and stencil_halves and XG < 1e-12 and Xsym < 1e-12 and okX and SG == 0 and gmag == [1] and sym_ok,
      f"stencil entries {len(stencil)}, real {stencil_real}, in (1/2)Z {stencil_halves}; on the {L}^3 torus max|X G^T| = {XG:.1e}, max|X - X^T| = {Xsym:.1e}, symbol reproduced {sym_ok}; X(m + g) = X(m) for {len(gpats)} patterns x 5 integer m: {okX}; S G^T = 0: {SG == 0}; gauge entry magnitudes {gmag}")

# ---------------------------------------------------------------- B: dual moment lemma on a box
def box_kernel(rowfun, nb, rows_iter):
    box = list(itertools.product(range(nb), repeat=3))
    slots = [(c, a) for c in box for a in range(6)]; sidx = {s: i for i, s in enumerate(slots)}
    rows = []
    for key in rows_iter:
        d = rowfun(*key); row = [0] * len(slots); touch = False
        for (c, a), v in d.items():
            if (c, a) in sidx:
                row[sidx[(c, a)]] += v; touch = True
        if touch and any(row):
            rows.append(row)
    basis = []                                                             # exact integer basis (moves shift by integers)
    for v in sp.Matrix(rows).nullspace():
        den = sp.ilcm(*[sp.fraction(x)[1] for x in v]); w = np.array([int(x * den) for x in v]); basis.append(w // np.gcd.reduce(np.abs(w[w != 0])))
    return slots, sidx, np.array(basis).T.astype(float)


nb = 2
sitesS = [(y,) for y in itertools.product(range(-2, nb + 2), repeat=3)]
slotsS, sidxS, KS = box_kernel(lambda y: S_row(y), nb, sitesS)
def moments(r, sidx):
    m0 = np.zeros(6); m1 = np.zeros((6, 3))
    for (c, a), i in sidx.items():
        p = np.array(c, float) + offset(a); m0[a] += r[i]; m1[a] += r[i] * p
    return m0, m1
M0 = np.array([moments(KS[:, t], sidxS)[0] for t in range(KS.shape[1])])
M1 = np.array([moments(KS[:, t], sidxS)[1].ravel() for t in range(KS.shape[1])])
gbox = []
for x in itertools.product(range(-1, nb + 1), repeat=3):
    for j in range(3):
        d = G_row(x, j)
        if all(k in sidxS for k in d):
            v = np.zeros(len(slotsS))
            for k, val in d.items():
                v[sidxS[k]] += val
            gbox.append(v)
M1g = np.array([moments(v, sidxS)[1].ravel() for v in gbox])


def tt_basis(n):
    n = n / np.linalg.norm(n); a = np.array([1., 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1., 0])
    u = np.cross(n, a); u /= np.linalg.norm(u); v = np.cross(n, u)
    return [(np.outer(u, u) - np.outer(v, v)) / np.sqrt(2), (np.outer(u, v) + np.outer(v, u)) / np.sqrt(2)]


def TE(e):   # weights pairing with q-coordinates (the TT observable, and the conjugate's TT direction)
    return np.array([e[0, 0], e[1, 1], e[2, 2], e[0, 1], e[1, 2], e[0, 2]])


def Tq(e):   # q-coordinates of a tensor
    return np.array([e[0, 0], e[1, 1], e[2, 2], 2 * e[0, 1], 2 * e[1, 2], 2 * e[0, 2]])


vis, visg = [], []
for _ in range(30):
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    for e in tt_basis(n):
        w = TE(e)
        vis.append(max(abs(w @ (M1[t].reshape(6, 3) @ n)) for t in range(len(M1))))
        visg.append(max(abs(w @ (M1g[t].reshape(6, 3) @ n)) for t in range(len(M1g))))
rk1 = np.linalg.matrix_rank(M1, tol=1e-9); rkg = np.linalg.matrix_rank(M1g, tol=1e-9)
# a qubit-carriable witness: an 8-slot +-1 move with S r = 0 on the open lattice and a TT first moment (found by an integer program, hard-coded)
W8 = {((0, 1, 0), 5): -1, ((1, 0, 0), 4): 1, ((1, 1, 0), 0): 1, ((1, 1, 0), 1): -1, ((1, 1, 0), 4): -1, ((1, 1, 0), 5): 1, ((1, 1, 1), 0): -1, ((1, 1, 1), 1): 1}
w8_S = max(abs(sum(v * W8.get(k, 0) for k, v in S_row(y).items())) for y in itertools.product(range(-2, 4), repeat=3))
w8_m0 = [sum(v for (c, a_), v in W8.items() if a_ == t) for t in range(6)]
w8_m1 = np.zeros((6, 3))
for (c, a_), v in W8.items():
    w8_m1[a_] += v * (np.array(c, float) + offset(a_))
w8_tt = max(abs(TE(e) @ (w8_m1 @ n_)) for n_ in [np.array([0, 0, 1.]), np.array([1, 1, 1.]) / np.sqrt(3), np.array([1, 0, 0.])] for e in tt_basis(n_))
check("B: dual moment lemma (the landed 2026-09-14 E-character bound, re-verified): every finitely supported r with S r = 0 has vanishing zeroth moments; its first moments span 8 dimensions, 3 pure gauge (TT-invisible) and 5 more that are TT-visible in every sampled direction; an 8-slot +-1 witness shows one qubit per slot can carry such a move",
      np.abs(M0).max() < 1e-12 and rk1 == 8 and rkg == 3 and min(vis) > 1e-2 and max(visg) < 1e-12 and w8_S == 0 and w8_m0 == [0] * 6 and w8_tt > 1,
      f"box {nb}^3 cells: ker S dimension {KS.shape[1]}; max |zeroth moment| {np.abs(M0).max():.1e}; rank of first moments {rk1} (gauge patterns {len(gbox)}, rank {rkg}); TT visibility over 60 (direction, polarisation) pairs: kernel min-of-max {min(vis):.3f}, gauge max {max(visg):.1e}; qubit-carriable 8-slot +-1 witness: S r = 0 {w8_S == 0}, zeroth moments {w8_m0}, largest TT first moment {w8_tt:.3f}")

# ---------------------------------------------------------------- C: dual sum rule, operator identity
def spin(S):
    d = int(round(2 * S + 1)); ms = S - np.arange(d)
    Sp = np.zeros((d, d))
    for a_ in range(1, d):
        Sp[a_ - 1, a_] = np.sqrt(S * (S + 1) - ms[a_] * (ms[a_] + 1))
    return Sp, Sp.T.copy(), np.diag(ms)


def kron_list(ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


okC = True
for S in (0.5, 1.0):
    Sp, Sm, Sz = spin(S); I = np.eye(Sp.shape[0])
    r = np.array([1, -1, 1]); a = rng.normal(size=3) + 1j * rng.normal(size=3)
    T = kron_list([Sp if v > 0 else Sm for v in r]); H = T + T.conj().T
    A = sum(a[k] * kron_list([Sz if kk == k else I for kk in range(3)]) for k in range(3))
    dc = (H @ A - A @ H) @ A.conj().T - A.conj().T @ (H @ A - A @ H)
    ok_ = np.abs(dc - abs(a @ r) ** 2 * H).max() < 1e-10
    okC &= ok_
# the bound's q-dependence on the box kernel: max over moves and polarisations of |w.r_hat(q)|^2 / q^2 at small q
def rhat(r, sidx, q):
    out = np.zeros(6, complex)
    for (c, a_), i in sidx.items():
        out[a_] += r[i] * np.exp(-1j * q @ (np.array(c, float) + offset(a_)))
    return out
ratios = []
for eps in (1e-2, 1e-3):
    n = np.array([0.3, -0.5, 0.81]); n /= np.linalg.norm(n); q = eps * n
    ratios.append(max(abs(TE(e) @ rhat(KS[:, t], sidxS, q)) ** 2 for e in tt_basis(n) for t in range(KS.shape[1])) / eps ** 2)
check("C: dual sum rule: [[T + T^dag, A], A^dag] = |a.r|^2 (T + T^dag) for a shift monomial and a diagonal observable (spin 1/2 and 1); with B, a Hamiltonian of diagonal terms and Gauss-law-compatible moves has TT metric f-sum m1(q) <= C_K q^2 in a ground state, two powers of q below Einstein's O(1), and the q^2 term is attained",
      okC and abs(ratios[0] - ratios[1]) / ratios[1] < 1e-3 and ratios[1] > 1e-3,
      f"operator identity: {okC}; max |w.r_hat(q)|^2 / q^2 over the box kernel at q = 1e-2, 1e-3: {ratios[0]:.4f}, {ratios[1]:.4f} (finite and nonzero)")

# ---------------------------------------------------------------- D: harmonic comparators reduced to the TT modes
sitesG = [(y, j) for y in itertools.product(range(-2, nb + 2), repeat=3) for j in range(3)]
slotsG, sidxG, KG = box_kernel(lambda y, j: G_row(y, j), 3, [(y, j) for y in itertools.product(range(-2, 5), repeat=3) for j in range(3)])
Mdw = np.diag([1, 1, 1, 2, 2, 2.]) - np.outer([1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0]) / 2
def reduced(n, eps):
    q = eps * n; K = 2 * np.sin(q / 2); Kh = K / np.linalg.norm(K)
    es = tt_basis(Kh); TEm = np.array([TE(e) for e in es]).T; Tqm = np.array([Tq(e) for e in es]).T
    Xred = Tqm.T @ Xr(q) @ Tqm
    kap = sum(np.outer(rhat(KS[:, t], sidxS, q), rhat(KS[:, t], sidxS, q).conj()) for t in range(KS.shape[1]))
    kred = TEm.T @ kap @ TEm
    W = sum(np.outer(rhat(KG[:, t], sidxG, q), rhat(KG[:, t], sidxG, q).conj()) for t in range(KG.shape[1]))
    Wred = Tqm.T @ W @ Tqm; Mred = TEm.T @ Mdw @ TEm
    om = lambda P, Q: np.sqrt(np.sort(np.linalg.eigvals(P @ Q).real))
    return om(kred, Xred), om(Mred, Wred), om(Mred, Xred), np.linalg.norm(K)
rows = []; okD = True; expo = []
eps_list = np.array([0.2, 0.1, 0.05, 0.025])
for n in [np.array([0, 0, 1.]), np.array([1, 1, 0.]) / np.sqrt(2), np.array([1, 1, 1.]) / np.sqrt(3), np.array([0.3, -0.5, 0.81]) / np.linalg.norm([0.3, -0.5, 0.81])]:
    rr = [reduced(n, e) for e in eps_list]; Kn = np.array([r_[3] for r_ in rr])
    fits = [np.polyfit(np.log(Kn), np.log([r_[k][m] for r_ in rr]), 1)[0] for k in range(3) for m in range(2)]
    expo.append(fits)
    sw = rr[-1][0] / Kn[-1] ** 2; p14 = rr[-1][1] / Kn[-1] ** 2; gr = rr[-1][2] / Kn[-1]
    okD &= all(abs(f - 2) < 0.05 for f in fits[:4]) and all(abs(f - 1) < 0.05 for f in fits[4:]) and sw.min() > 1e-3 and p14.min() > 1e-3
    rows.append(f"n = {np.round(n, 2)}: exponents swapped {np.round(fits[0:2], 3)}, probe-14 {np.round(fits[2:4], 3)}, non-compact {np.round(fits[4:6], 3)}; at |K| = {Kn[-1]:.3f} swapped omega/K^2 = {np.round(sw, 3)}, probe-14 omega/K^2 = {np.round(p14, 3)}, non-compact omega/K = {np.round(gr, 3)}")
check("D: harmonic comparators on the two TT modes (integer move bases, U = 1): the swapped assignment (Gauss-law-compatible moves, E-H potential) and probe 14's assignment (DeWitt kinetic, ker G moves) both give omega ~ q^2 (fitted exponent 2.00 +- 0.05 on axis, face, body and a generic direction, |k| = 0.2 ... 0.025); the non-compact comparator (DeWitt + E-H) gives omega ~ q",
      okD, f"ker S box kernel {KS.shape[1]} moves, ker G box kernel {KG.shape[1]} moves; " + "; ".join(rows))

# ---------------------------------------------------------------- E: gauge side at finite S
okE = True; det = []
for S in (0.5, 1.0):
    Sp, Sm, Sz = spin(S); I = np.eye(Sp.shape[0])
    V1 = kron_list([Sp, Sm, I]); V2 = kron_list([I, Sp, Sm])                      # overlapping with opposite signs on slot 1
    c12 = np.abs(V1 @ V2 - V2 @ V1).max()
    Tm = kron_list([I, Sp, Sp])                                                     # a move sharing slot 1 with V1
    cv = np.abs(Tm @ V1 - V1 @ Tm).max(); cvd = np.abs(Tm @ V1.conj().T - V1.conj().T @ Tm).max()
    Z = [kron_list([Sz if kk == k else I for kk in range(3)]) for k in range(3)]
    gv = np.array([1, -1, 0]); Q = np.array([[1, 1, 0.], [1, 1, 0], [0, 0, 3]])       # Q g = 0, so the diagonal form is shift-invariant along g
    Xd = sum(Q[i, j] * Z[i] @ Z[j] for i in range(3) for j in range(3))
    cx = np.abs(Xd @ V1 - V1 @ Xd).max()
    okE &= c12 > 1e-6 and max(cv, cvd) > 1e-6 and cx < 1e-12
    det.append(f"S = {S}: |[V1, V2]| = {c12:.3f}, |[T, V1]|, |[T, V1^dag]| = {cv:.3f}, {cvd:.3f}, |[X(S^z), V1]| = {cx:.1e}")
check("E: gauge side at finite S (toys): gauge strings overlapping with opposite signs do not commute (the linearised diffeomorphisms do); a monomial move sharing a slot with a gauge string fails to commute with V_g or with V_g^dag; a diagonal form invariant under the shift commutes exactly; so monomial kinetic moves are exactly invariant under both V_g and V_g^dag only where they avoid the gauge supports or in the rotor limit (sums of monomials commuting with Y_g are not enumerated)",
      okE, "; ".join(det))

# ---------------------------------------------------------------- F: an energetic (soft) scalar law cannot stabilise E-H's scalar block
def S_sym(q):             # the landed scalar stencil's symbol in the midpoint convention: S(q) q = K_i K_j h_ij - K^2 tr h
    K = 2 * np.sin(q / 2); KK = K @ K
    return np.array([K[0] ** 2 - KK, K[1] ** 2 - KK, K[2] ** 2 - KK, K[0] * K[1], K[1] * K[2], K[0] * K[2]])
# consistency with the torus stencil at a torus momentum (up to one overall phase)
st_sym = Bq.conj() @ St[0].astype(float) * np.exp(1j * qt @ np.zeros(3))
sym_S_ok = np.linalg.matrix_rank(np.vstack([st_sym, S_sym(qt)]), tol=1e-9) == 1
nF = np.array([0.3, -0.5, 0.81]) / np.linalg.norm([0.3, -0.5, 0.81]); outF = []; okF = sym_S_ok
for U in (1.0, 1e3, 1e6):
    vals = []
    for eps in (1e-2 / np.sqrt(U), 0.5e-2 / np.sqrt(U)):
        q = eps * nF; K = 2 * np.sin(q / 2); Sv = S_sym(q)
        ev = np.linalg.eigvalsh(Xr(q) + U * np.outer(Sv, Sv)); vals.append(ev.min() / (K @ K))
    okF &= vals[0] < -1e-3 and abs(vals[0] - vals[1]) / abs(vals[1]) < 1e-2
    outF.append(f"U = {U:.0e}: min eigenvalue / K^2 at |q| = 1e-2/sqrt(U), 0.5e-2/sqrt(U): {vals[0]:.4f}, {vals[1]:.4f}")
check("F: (re-verification of the landed 2026-09-14 penalty block) a soft scalar law does not rescue the swapped assignment: with the scalar law only as an energy penalty U (S h)^2, single-slot moves would give an O(1) kinetic term, but E-H plus the penalty has a negative eigenvalue ~ -c q^2 at |q| < sqrt(c/U) for every finite U (the penalty is O(q^4)); the long-wavelength conformal mode is unstable",
      okF, f"S symbol matches the torus stencil: {sym_S_ok}; " + "; ".join(outF))

print("N5 resolution 1: swapping the assignment makes the Einstein-Hilbert potential exactly (strongly) invariant under the quantum-link momentum-rule gauge, and the scalar rule an exact linear Gauss law.")
print("N5 resolution 2: the obstruction moves to the kinetic side: Gauss-law-compatible moves have zero zeroth moments (landed E-character bound), so the TT metric f-sum is O(q^2), two powers below Einstein's; pre-registered outcome FAIL.")
print("N5 resolution 3: in the harmonic comparators both finite-slot assignments give omega ~ q^2; the non-compact comparator gives omega ~ q.")
print("N5 resolution 4: at finite S, monomial kinetic moves overlapping a gauge string are not invariant under both V_g and V_g^dag; the full commutant of the Y_g is not enumerated.")
print("per_element: the stencil's entries; each operator identity on spin-1/2 and spin-1 toys; each gauge pattern's integer invariance.")
print("per_site: all 192 gauge patterns of the 4^3 torus for X(m + g) = X(m); the S G^T = 0 identity at every site.")
print("per_mode: the two TT modes of each harmonic comparator in three directions at two momenta; TT visibility on 60 direction-polarisation pairs.")
print("per_block: the 2^3-cell box kernel of S (moves) and the 3^3-cell box kernel of G (probe 14's potential moves).")
print("lattice_wide: checked and not executed - any ground state, its chi_h(q), quantum closure of the V strings, a phase.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
