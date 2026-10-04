#!/usr/bin/env python3
"""Composite-site network, flux-free comparator: exact straight surface zero lines of the cell-cut a3 slab (u = f1 = 1/2 top, v = f2 = 1/2 bottom).

Supplied u = +1 quadratic Majorana comparator of the landed notes (one copy, landed hopping-sign convention), four-site Bloch matrix H(f) = i M(f),
M(f)[a, b] += t e^{2 pi i f.n}, M[b, a] -= t e^{-2 pi i f.n} for each real hopping term (a, b, n, t), n in units of the primitive translations
a1 = (2,0,0), a2 = (0,2,0), a3 = (1,1,2); couplings J = (J_x, J_y, J_z) and odd term kappa (amplitudes 2 J_flavour and 2 kappa).  Slab: open along a3,
"cell cut" (every site of cell R sits in layer R_3), basis index 4 L + a, good momenta (f1, f2) = (u, v), hoppings leaving the layers are dropped,
H_slab = i M_slab.  Top surface = layer 0 of the half-infinite slab 0, 1, 2, ...; bottom surface = the last layer.  Sites {0,1} = p, {2,3} = q.

EXACT (sympy rational-function identities for symbolic J_x, J_y, J_z, kappa, z1 = e^{2 pi i u}, z2 = e^{2 pi i v}; elementary inequalities):
 the layer blocks A = H_{L,L}, B = H_{L,L+1} (H_{L,L-1} = B^dagger, nothing beyond nearest layers); B is nonzero only at [2,0], [3,0], [3,1]; at f1 = 1/2
 the p-block of A is -2 (J_x - J_y) sigma_y, so it vanishes iff J_x = J_y (REQUIRED below); for J_x = J_y and kappa, J_z != 0 the half-infinite top slab has,
 at every (1/2, v), v in [0,1), an l^2 kernel of dimension exactly one, psi_L = lambda^L (1, r, 0, 0) with lambda = rho e^{i pi (v - 1/2)},
 |tau| = sigma + (4 kappa^2 + J_z^2)/(4 kappa^2 sigma), sigma = sin pi v, rho = (|tau| - sqrt(tau^2 - 4))/2, r = -J_z rho/(2 kappa (sigma - rho));
 the bottom surface (line v = 1/2) is the mirror statement with u; the bulk has no zero-energy state on the plane f1 = 1/2.
FLOAT diagnostics (finite float slabs N = 4..40, 50-digit mpmath slabs N <= 12, random couplings, a 48 x 48 bulk grid): cross-checks of the exact statements
 and a negative control J_x != J_y (reported, not asserted).  No interval arithmetic, nothing is certified; no statement about other terminations.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"

import time

import mpmath as mp
import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 300

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label} :: {detail}", flush=True)


# ------------------------------------------------------------------------------------------------ network and Bloch terms (as landed; copied)
AX = {"x": 0, "y": 1, "z": 2}


def is_site(p):
    i, j, z = p
    m = z % 4
    if m == 0:
        return j % 2 == 0
    if m == 1:
        return i % 2 == 1
    if m == 2:
        return j % 2 == 1
    return i % 2 == 0


def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0:
        return "z"
    lo = p if sum(d) > 0 else q
    m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"


def neighbours(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
            if is_site(q):
                out.append(q)
    return out


REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]


def reduce(p):
    """p = rep + n1 a1 + n2 a2 + n3 a3 with rep in the 2x2x2 box; returns (rep index, n)."""
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)


def terms(J, kappa):
    """Real hopping terms (a, b, n, t): M(f)[a, b] += t e^{2 pi i f.n}, M(f)[b, a] -= t e^{-2 pi i f.n}, gauge u = +1."""
    out = []
    for p in REPS:
        a, n0 = reduce(p)
        assert n0 == (0, 0, 0) and is_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce(q)
                out.append((a, b, n, 2.0 * J[AX[flavour(p, q)]]))
        if kappa:
            nb = {flavour(p, q): q for q in neighbours(p)}
            assert len(nb) == 3
            for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
                r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
                out.append((r1, r2, tuple(np.subtract(n2, n1)), 2.0 * kappa))
    return out


def slab_hamiltonian(T, d, fperp, N, shift=(0, 0, 0, 0), periodic=None):
    """Slab of N layers along the primitive translation a_{d+1} (d = 0, 1, 2), good momenta fperp along the other two.
    Basis index 4 L + a.  Site a of cell R sits in layer R_d + shift[a]; the term (a, b, n, t) joins (a, L) to (b, L + n_d + shift[b] - shift[a]).
    Hoppings leaving layers 0..N-1 are dropped, or wrapped modulo N with phase e^{2 pi i periodic wrap} if `periodic` is given (tests)."""
    perp = [i for i in range(3) if i != d]
    M = np.zeros((4 * N, 4 * N), dtype=complex)
    for (a, b, n, t) in T:
        ph = np.exp(2j * np.pi * (fperp[0] * n[perp[0]] + fperp[1] * n[perp[1]]))
        dl = n[d] + shift[b] - shift[a]
        L = np.arange(N); L2 = L + dl
        if periodic is None:
            keep = (L2 >= 0) & (L2 < N)
            L, L2 = L[keep], L2[keep]
            w = 1.0
        else:
            wrap, L2 = np.divmod(L2, N)
            w = np.exp(2j * np.pi * periodic * wrap)
        r, c = 4 * L + a, 4 * L2 + b
        M[r, c] += t * ph * w
        M[c, r] -= t * np.conj(ph * w)
    return 1j * M


def bulk_H(Tl, f):
    """Plain double-loop H(f) = i M(f) from a float term list (independent of the slab code)."""
    M = np.zeros((4, 4), dtype=complex)
    for (a, b, n, t) in Tl:
        ph = np.exp(2j * np.pi * (f[0] * n[0] + f[1] * n[1] + f[2] * n[2]))
        M[a, b] += t * ph
        M[b, a] -= t * np.conj(ph)
    return 1j * M


# ------------------------------------------------------------------------------------------------ symbolic layer blocks (same term list, symbolic amplitudes)
Jx, Jy, Jz, kap = sp.symbols("J_x J_y J_z kappa", real=True)
z1, z2, q, lam, mu = sp.symbols("z1 z2 q lambda mu")
sg = sp.symbols("sigma", positive=True)
I = sp.I


def terms_sym():
    """Same list as `terms` with symbolic amplitudes 2 J_flavour, 2 kappa and python-int translations."""
    JS = (Jx, Jy, Jz); out = []
    for p in REPS:
        a, n0 = reduce(p)
        if sum(p) % 2 == 0:
            for qq in neighbours(p):
                b, n = reduce(qq)
                out.append((a, b, tuple(int(x) for x in n), 2 * JS[AX[flavour(p, qq)]]))
        nb = {flavour(p, qq): qq for qq in neighbours(p)}
        for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
            r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
            out.append((r1, r2, tuple(int(x) for x in (n2[0] - n1[0], n2[1] - n1[1], n2[2] - n1[2])), 2 * kap))
    return out


def layer_blocks(Ts):
    """m -> 4x4 sympy Matrix H_{L, L+m} (a3 open: layer shift = n_3; H = i M); entries are Laurent polynomials in z1, z2."""
    M = {}
    for (a, b, n, t) in Ts:
        ph = z1 ** n[0] * z2 ** n[1]
        phc = z1 ** (-n[0]) * z2 ** (-n[1])
        M.setdefault(n[2], sp.zeros(4, 4))[a, b] += t * ph
        M.setdefault(-n[2], sp.zeros(4, 4))[b, a] -= t * phc
    return {m: (I * X).applyfunc(sp.expand) for m, X in M.items()}


def dag(X):
    """Hermitian conjugate for unimodular z1, z2 and real couplings: z -> 1/z, I -> -I, transpose."""
    return X.subs({z1: 1 / z1, z2: 1 / z2}, simultaneous=True).xreplace({I: -I}).T.applyfunc(sp.expand)


def zero(e):
    return sp.simplify(sp.together(e)) == 0


def mzero(Mx):
    return all(zero(e) for e in Mx)


TS = terms_sym()
BK = layer_blocks(TS)
A, B = BK[0], BK[1]
TOP = {z1: -1, Jy: Jx}                         # f1 = 1/2 and J_x = J_y
A0 = A.subs(TOP).applyfunc(sp.expand); B0 = B.subs(TOP).applyfunc(sp.expand)
fA = sp.lambdify((z1, z2, Jx, Jy, Jz, kap), A, "numpy"); fB = sp.lambdify((z1, z2, Jx, Jy, Jz, kap), B, "numpy")
rng = np.random.default_rng(20261001)

# ------------------------------------------------------------------------------------------------ (1) symbolic blocks vs the float slab
worst = 0.0; badterms = 0; worst_t = 0.0
for it in range(200):
    J = tuple(rng.uniform(0.2, 2.5, 3)); kp = rng.uniform(0.05, 1.5); u, v = rng.uniform(0, 1, 2)
    Tf = terms(J, kp)
    if it < 40:
        sub = {Jx: J[0], Jy: J[1], Jz: J[2], kap: kp}
        badterms += len(Tf) != len(TS)
        for (a, b, n, t), (a2, b2, n2, t2) in zip(Tf, TS):
            badterms += (a, b, tuple(int(x) for x in n)) != (a2, b2, n2)
            worst_t = max(worst_t, abs(float(t2.subs(sub)) - t))
    H = slab_hamiltonian(Tf, 2, (u, v), 5)
    Af = np.array(fA(np.exp(2j * np.pi * u), np.exp(2j * np.pi * v), *J, kp), dtype=complex)
    Bf = np.array(fB(np.exp(2j * np.pi * u), np.exp(2j * np.pi * v), *J, kp), dtype=complex)
    for L in range(5):
        worst = max(worst, np.abs(H[4*L:4*L+4, 4*L:4*L+4] - Af).max())
        for L2 in range(5):
            if abs(L - L2) >= 2:
                worst = max(worst, np.abs(H[4*L:4*L+4, 4*L2:4*L2+4]).max())
    for L in range(4):
        worst = max(worst, np.abs(H[4*L:4*L+4, 4*L+4:4*L+8] - Bf).max(), np.abs(H[4*L+4:4*L+8, 4*L:4*L+4] - Bf.conj().T).max())
wb = 0.0
for it in range(100):
    J = tuple(rng.uniform(0.2, 2.5, 3)); kp = rng.uniform(0.05, 1.5); f = rng.uniform(0, 1, 3)
    Af = np.array(fA(np.exp(2j * np.pi * f[0]), np.exp(2j * np.pi * f[1]), *J, kp), dtype=complex); Bf = np.array(fB(np.exp(2j * np.pi * f[0]), np.exp(2j * np.pi * f[1]), *J, kp), dtype=complex)
    lm = np.exp(2j * np.pi * f[2]); wb = max(wb, np.abs(Af + lm * Bf + Bf.conj().T / lm - bulk_H(terms(J, kp), f)).max())
ok1 = (sorted(BK) == [-1, 0, 1] and mzero(BK[-1] - dag(B)) and mzero(A - dag(A)) and worst < 1e-14 and badterms == 0 and worst_t == 0.0 and wb < 1e-14)
check("(1) symbolic layer blocks A, B (J_x, J_y, J_z, kappa free) = float cell-cut a3 slab blocks; H_{L,L-1} = B^dag and A Hermitian exact", ok1,
      f"offsets {sorted(BK)}; 200 random (J, kappa, u, v), N = 5: max |float - symbolic| over all blocks = {worst:.2e} (< 1e-14); 40 term lists identical (mismatches {badterms}); A + lam B + B^dag/lam vs bulk H(f) (100 f): {wb:.1e}")

# ------------------------------------------------------------------------------------------------ (2) block structure (exact)
Bhand = sp.zeros(4, 4)
Bhand[2, 0] = -2 * I * kap * (z2 - 1) / z2; Bhand[3, 0] = -2 * I * Jz; Bhand[3, 1] = 2 * I * kap * (z1 - 1) / z1
Bsupp = [(i, j) for i in range(4) for j in range(4) if B[i, j] != 0]
pblock = A0[0:2, 0:2]
sy = sp.Matrix([[0, -I], [I, 0]])
solpp = sp.solve([A.subs(z1, -1)[0, 1], A.subs(z1, -1)[1, 0]], [Jx, Jy], dict=True)
ok2 = (mzero(B - Bhand) and Bsupp == [(2, 0), (3, 0), (3, 1)] and B.free_symbols.isdisjoint({Jx, Jy})
       and A[3, 0] == 0 and zero(A.subs(z1, -1)[0, 0]) and zero(A.subs(z1, -1)[1, 1])
       and mzero(A.subs(z1, -1)[0:2, 0:2] + 2 * (Jx - Jy) * sy) and pblock == sp.zeros(2, 2) and solpp == [{Jx: Jy}])
check("(2) block structure: B nonzero only at [2,0],[3,0],[3,1] (no J_x, J_y); A[3,0] = 0; at f1 = 1/2 the p-block of A is -2(J_x - J_y) sigma_y", ok2,
      f"exact; B[2,0] = -2i k (z2-1)/z2, B[3,0] = -2i J_z, B[3,1] = 2i k (z1-1)/z1; A[0,0] = A[1,1] = 0 for all J, kappa; p-block = 0 iff J_x = J_y: {solpp}")

# ------------------------------------------------------------------------------------------------ (3) restricted blocks, det T, tr T, empty boundary condition (exact)
As = A0[2:4, 0:2]; Bs = B0[2:4, 0:2]
As_h = sp.Matrix([[4 * I * kap, 2 * I * Jz], [0, 2 * I * kap * (z2 - 1)]]); Bs_h = sp.Matrix([[-2 * I * kap * (z2 - 1) / z2, 0], [-2 * I * Jz, 4 * I * kap]])
T = (-(Bs.inv()) * As).applyfunc(sp.cancel); dT = sp.cancel(T.det()); tT = sp.cancel(T.trace())
t_h = ((4 * kap ** 2 + Jz ** 2) * z2 - kap ** 2 * (z2 - 1) ** 2) / (2 * kap ** 2 * (z2 - 1))
xm = sp.Matrix(sp.symbols("xm0 xm1")); x0 = sp.Matrix(sp.symbols("x0 x1")); xp = sp.Matrix(sp.symbols("xp0 xp1"))
pad = lambda w: sp.Matrix([w[0], w[1], 0, 0])
Bd0 = dag(B).subs(TOP).applyfunc(sp.expand)
res = (Bd0 * pad(xm) + A0 * pad(x0) + B0 * pad(xp)).applyfunc(sp.expand)
want = sp.Matrix([0, 0, *(As * x0 + Bs * xp)]).applyfunc(sp.expand)
ok3 = (mzero(As - As_h) and mzero(Bs - Bs_h) and zero(As.det() + 8 * kap ** 2 * (z2 - 1)) and zero(Bs.det() - 8 * kap ** 2 * (z2 - 1) / z2)
       and zero(dT + z2) and zero(tT - t_h) and T.free_symbols.isdisjoint({Jx, Jy}) and (res - want) == sp.zeros(4, 1) and Bd0[:, 0:2] == sp.zeros(4, 2))
check("(3) restricted blocks A_s, B_s, det T = -z2, tr T formula; empty boundary condition: A_s x_L + B_s x_{L+1} = 0 for all L >= 0 (no x_{L-1}, same at L = 0)", ok3,
      "exact; A_s = [[4ik, 2iJ_z],[0, 2ik(z2-1)]], B_s = [[-2ik(z2-1)/z2, 0],[-2iJ_z, 4ik]]; det A_s = -8k^2(z2-1), det B_s = 8k^2(z2-1)/z2; "
      "tr T = [(4k^2+J_z^2) z2 - k^2 (z2-1)^2]/(2k^2 (z2-1)); T has no J_x, J_y; B^dag[:,0:2] = 0 so psi_{L-1} drops out of the p-supported equations")

# ------------------------------------------------------------------------------------------------ (4) top theorem: characteristic polynomial and the strict inequality (exact)
a_ = 4 * kap ** 2 + Jz ** 2
sig = (q - 1 / q) / (2 * I)                    # sin(pi v) for q = e^{i pi v}
tq = sp.cancel(tT.subs(z2, q ** 2)); dq = sp.cancel(dT.subs(z2, q ** 2))
tau_h = -(a_ + 4 * kap ** 2 * sig ** 2) / (4 * kap ** 2 * sig)
tau = sp.cancel(tq / (I * q))
cp = sp.cancel((lam ** 2 - tq * lam + dq).subs(lam, I * q * mu))
delta = Jz ** 2 / (4 * kap ** 2); b_ = 1 + delta
tau_abs = sg + a_ / (4 * kap ** 2 * sg)
cexp = (z2 + 1 / z2) / 2
conj_ = lambda e: e.subs({z2: 1 / z2}, simultaneous=True).xreplace({I: -I})
abs2 = sp.cancel(tT * conj_(tT))
ok4 = (zero(tau - tau_h) and zero(cp + q ** 2 * (mu ** 2 - tau_h * mu + 1)) and zero(dq + q ** 2)
       and zero(tau_abs ** 2 - 4 - ((sg - b_ / sg) ** 2 + 4 * delta))
       and zero(abs2 - 4 - ((2 * kap ** 2 * (1 - cexp) + Jz ** 2 - 4 * kap ** 2) ** 2 + 16 * kap ** 2 * Jz ** 2) / (8 * kap ** 4 * (1 - cexp))))
check("(4) top line: p(lambda) at lambda = i q mu equals -q^2 (mu^2 - tau mu + 1), tau = -(sigma + (4k^2+J_z^2)/(4k^2 sigma)) real < 0; tau^2 - 4 = (sigma - b/sigma)^2 + 4 delta > 0", ok4,
      "exact (|det T| = 1, det T = -q^2; delta = J_z^2/(4k^2), b = 1 + delta); so for kappa J_z != 0 and every v in (0,1): tau^2 - 4 >= J_z^2/k^2 > 0, "
      "exactly one eigenvalue of T inside the unit disc (mu = -rho, |lambda| = rho < 1) and one outside (|lambda| = 1/rho); also |tr T|^2 - 4 = [(2k^2(1-c)+J_z^2-4k^2)^2 + 16k^2 J_z^2]/(8k^4 (1-c)) exact")

# ------------------------------------------------------------------------------------------------ (5) top theorem: kernel dimension (incl. v = 0), explicit mode and rho (exact)
Apq = A0[0:2, 2:4]
dApq = sp.factor(Apq.det())
M2 = As + lam * Bs
rr = sp.cancel(-M2[1, 0] / M2[1, 1])                           # row 3 of (A_s + lam B_s) x = 0, x = (1, r)
r_mu = sp.cancel(rr.subs({lam: I * q * mu, z2: q ** 2}))
row2 = sp.numer(sp.together(sp.simplify(M2[0, 0] + M2[0, 1] * rr)))
rem2 = sp.simplify(sp.rem(row2, sp.numer(sp.together(lam ** 2 - tT * lam + dT)), lam))
Bd_pq1 = Bd0[0:2, 2:4].subs(z2, 1); Apq1 = Apq.subs(z2, 1)
Mv0 = sp.Matrix([[Apq1[0, 0], Bd_pq1[0, 1]], [Apq1[1, 0], Bd_pq1[1, 1]]])
As1 = As.subs(z2, 1); Bs1 = Bs.subs(z2, 1)
cons = sp.Matrix([[As1[0, 0], As1[0, 1]], [Bs1[1, 0], Bs1[1, 1]]])
rho_s = (tau_abs - sp.sqrt(tau_abs ** 2 - 4)) / 2
kP, jP = sp.symbols("k_P j_P", positive=True)
dP = jP ** 2 / (4 * kP ** 2)
rho_max_h = ((sp.sqrt(jP ** 2 + 16 * kP ** 2) - jP) / (4 * kP)) ** 2          # claimed rho at v = 1/2
rho_max_s = ((2 + dP) - sp.sqrt((2 + dP) ** 2 - 4)) / 2                       # (|tau| - sqrt(tau^2 - 4))/2 at sigma = 1, |tau| = 2 + delta
ok5 = (zero(dApq - 8 * kap ** 2 * (z2 - 1) / z2) and zero(Mv0.det() + 4 * (Jz ** 2 + 4 * kap ** 2)) and zero(cons.det() + 4 * (Jz ** 2 + 4 * kap ** 2))
       and mzero(As1 * sp.Matrix([Jz, -2 * kap])) and zero(r_mu - Jz * mu / (2 * kap * (mu + sig))) and rem2 == 0
       and zero(tau_abs.subs(sg, 1) - 2 - delta) and zero(rho_max_s - rho_max_h))
check("(5) top line kernel: q-part = 0 (det A_pq = 8k^2 (z2-1)/z2 != 0 for v != 0; v = 0 by a 2x2 system, det = -4(J_z^2+4k^2)); p-part: one decaying mode lambda = rho e^{i pi(v-1/2)}, x = (1, r)", ok5,
      "exact; r = J_z mu/(2k (mu + sigma)) = -J_z rho/(2k (sigma - rho)) real, rho < sigma (f(x) = x + 1/x decreasing on (0,1)); rho_max (v = 1/2) = ((sqrt(J_z^2+16k^2) - abs(J_z))/(4abs(k)))^2; "
      "v = 0: x_0 = (J_z, -2k) on layer 0 only, x_L = 0 for L >= 1; kernel dimension exactly 1 for all v in [0,1)")

# ------------------------------------------------------------------------------------------------ (6) bottom theorem (exact)
BOT = {z2: -1, Jy: Jx}
Ab = A.subs(BOT).applyfunc(sp.expand); Bb = B.subs(BOT).applyfunc(sp.expand); Bdb = dag(B).subs(BOT).applyfunc(sp.expand)
Apq_b = Ab[0:2, 2:4]; Bdpq_b = Bdb[0:2, 2:4]; Aqp_b = Ab[2:4, 0:2]; Bqp_b = Bb[2:4, 0:2]
Tp = (-(Bdpq_b.inv()) * Apq_b).applyfunc(sp.cancel); dTp = sp.cancel(Tp.det()); tTp = sp.cancel(Tp.trace())
t_top_z1 = ((4 * kap ** 2 + Jz ** 2) * z1 - kap ** 2 * (z1 - 1) ** 2) / (2 * kap ** 2 * (z1 - 1))
tqp = sp.cancel(tTp.subs(z1, q ** 2)); dqp = sp.cancel(dTp.subs(z1, q ** 2))
taup_h = +(a_ + 4 * kap ** 2 * sig ** 2) / (4 * kap ** 2 * sig)
cpp = sp.cancel((lam ** 2 - tqp * lam + dqp).subs(lam, I * mu / q))
M2b = Apq_b + lam * Bdpq_b
rb = sp.cancel(-M2b[1, 0] / M2b[1, 1]).subs({lam: I * mu / q, z1: q ** 2})
Apq_u0 = Apq_b.subs(z1, 1); Bdpq_u0 = Bdpq_b.subs(z1, 1); Aqp_u0 = Aqp_b.subs(z1, 1); Bqp_u0 = Bqp_b.subs(z1, 1)
consb = sp.Matrix([[Bdpq_u0[0, 0], Bdpq_u0[0, 1]], [Apq_u0[1, 0], Apq_u0[1, 1]]])
P2 = sp.Matrix([[Aqp_u0[0, 1], Bqp_u0[0, 0]], [Aqp_u0[1, 1], Bqp_u0[1, 0]]])
ok6 = (Ab[2:4, 2:4] == sp.zeros(2, 2) and zero(dTp + 1 / z1) and zero(tTp + t_top_z1 / z1) and zero(sp.cancel(tTp.subs(z1, q ** 2) / (I / q)) - taup_h)
       and zero(cpp + (mu ** 2 - taup_h * mu + 1) / q ** 2) and zero(sp.cancel(rb) - Jz / (2 * kap * (1 - mu * sig)))
       and zero(Aqp_b.det() + 8 * kap ** 2 * (z1 - 1)) and zero(consb.det() + 4 * (Jz ** 2 + 4 * kap ** 2)) and zero(P2.det() - 4 * (Jz ** 2 + 4 * kap ** 2))
       and zero(Aqp_u0[0, 1] - 2 * I * Jz) and zero(Aqp_u0[1, 1] + 4 * I * kap) and mzero(Apq_u0[1, :] * sp.Matrix([2 * kap, Jz])))
check("(6) bottom line v = 1/2 (sites {2,3}, last layer): A_qq = 0; T' = -(B^dag_pq)^{-1} A_pq has det -1/z1, tr T' = -tr T_top(z1)/z1, tau' = +|tau(sigma_u)|; kernel dimension exactly 1", ok6,
      "exact (J_x = J_y); eigenvalues of T' are the reciprocals of the top ones with v -> u, so one inside, modulus rho(sigma_u), lambda' = rho e^{i pi (1/2 - u)}, y = (1, J_z/(2k (1 - rho sigma_u))); "
      "p-part = 0 since det A_qp = -8k^2 (z1 - 1) != 0 (u != 0), u = 0 by a 2x2 system; at u = 0 the mode sits on the last layer, y = (2k, J_z)")

# ------------------------------------------------------------------------------------------------ (7) bulk: no zero energy on the plane f1 = 1/2
Hb = (A0 + lam * B0 + Bd0 / lam).applyfunc(sp.expand)
dH = sp.cancel(Hb.det())
Pm = A0[0:2, 2:4] + Bd0[0:2, 2:4] / lam; Rm = A0[2:4, 0:2] + lam * B0[2:4, 0:2]
detR = sp.cancel(Rm.det())
conjR = detR.subs({lam: 1 / lam, z2: 1 / z2}, simultaneous=True).xreplace({I: -I})
ok7_exact = (zero(dH - Pm.det() * Rm.det()) and zero(sp.cancel(Pm.det()) - sp.cancel(conjR)) and zero(detR - Bs.det() * (lam ** 2 - tT * lam + dT))
             and zero(detR.subs(z2, 1) + 4 * lam * (4 * kap ** 2 + Jz ** 2)))
gap = {}
for kp in (0.3, 0.6):
    Tf = terms((1, 1, 1), kp); mn = 9e9
    for v in (np.arange(48) + 0.5) / 48:
        for f3 in (np.arange(48) + 0.5) / 48:
            mn = min(mn, np.abs(np.linalg.eigvalsh(bulk_H(Tf, (0.5, v, f3)))).min())
    gap[kp] = mn
ok7 = ok7_exact and min(gap.values()) > 0.9
check("(7) bulk on the plane f1 = 1/2 (J_x = J_y): det H = det(A_pq + B^dag_pq/lam) det(A_qp + lam B_qp) = |det R|^2 on the torus, det R = det B_s (lam^2 - tr T lam + det T); no zero energy", ok7,
      f"exact: det H_bulk factorisation, det P = conj(det R) for unimodular z2, lam; roots of det R have |lam| != 1 by (4), and det R(v = 0) = -4 lam (4k^2 + J_z^2) != 0; FLOAT diagnostic: min |E| over a 48 x 48 (v, f3) grid, "
      f"J = (1,1,1): kappa 0.3 -> {gap[0.3]:.4f}, kappa 0.6 -> {gap[0.6]:.4f} (not a bound)")


# ------------------------------------------------------------------------------------------------ closed forms (float) used by the cross-checks
def rho_f(kp, jz, s):
    ta = s + (4 * kp ** 2 + jz ** 2) / (4 * kp ** 2 * s)
    return (ta - np.sqrt(ta ** 2 - 4)) / 2


def rho_mp(kp, jz, v):
    kp, jz, v = mp.mpf(kp), mp.mpf(jz), mp.mpf(v)
    s = mp.sin(mp.pi * v); ta = s + (4 * kp ** 2 + jz ** 2) / (4 * kp ** 2 * s)
    return (ta - mp.sqrt(ta ** 2 - 4)) / 2


def blocks_float(J, kp, u, v):
    H = slab_hamiltonian(terms(J, kp), 2, (u, v), 4)
    return H[0:4, 0:4], H[0:4, 4:8]


def top_mode(J, kp, v, N):
    s = np.sin(np.pi * v); rho = rho_f(kp, J[2], s); lm = rho * np.exp(1j * np.pi * (v - 0.5)); r = -J[2] * rho / (2 * kp * (s - rho))
    psi = np.zeros(4 * N, complex)
    for L in range(N):
        psi[4 * L] = lm ** L; psi[4 * L + 1] = r * lm ** L
    return psi


def bottom_mode(J, kp, u, N):
    s = np.sin(np.pi * u); rho = rho_f(kp, J[2], s); lm = rho * np.exp(1j * np.pi * (0.5 - u)); r = J[2] / (2 * kp * (1 - rho * s))
    psi = np.zeros(4 * N, complex)
    for n in range(N):
        L = N - 1 - n; psi[4 * L + 2] = lm ** n; psi[4 * L + 3] = r * lm ** n
    return psi


# ------------------------------------------------------------------------------------------------ (8) float cross-checks against the float slab
mp.mp.dps = 30
parts = []; ok8 = True
for kp in (0.3, 0.6):
    A_, B_ = blocks_float((1, 1, 1), kp, 0.5, 0.2)
    ev = np.linalg.eigvals(-np.linalg.solve(B_[2:4, 0:2], A_[2:4, 0:2])); ev = ev[np.argsort(np.abs(ev))]
    rx = rho_mp(mp.mpf(str(kp)), 1, mp.mpf(1) / 5)
    w, V = np.linalg.eigh(slab_hamiltonian(terms((1, 1, 1), kp), 2, (0.5, 0.2), 40)); k_ = np.argmin(np.abs(w))
    Wl = (np.abs(V[:, k_]) ** 2).reshape(40, 4).sum(1); ratio = np.sqrt(Wl[1] / Wl[0])
    lm_ex = complex(rx * mp.expjpi(mp.mpf(1) / 5 - mp.mpf(1) / 2))
    psi = top_mode((1, 1, 1), kp, 0.2, 40); resid_t = np.abs((slab_hamiltonian(terms((1, 1, 1), kp), 2, (0.5, 0.2), 40) @ psi).reshape(40, 4)[:39]).max()
    psi = bottom_mode((1, 1, 1), kp, 0.2, 40); resid_b = np.abs((slab_hamiltonian(terms((1, 1, 1), kp), 2, (0.2, 0.5), 40) @ psi).reshape(40, 4)[1:]).max()
    nin = 0
    for v in np.linspace(0.0013, 0.9987, 400):
        A_, B_ = blocks_float((1, 1, 1), kp, 0.5, v); e = np.abs(np.linalg.eigvals(-np.linalg.solve(B_[2:4, 0:2], A_[2:4, 0:2])))
        nin += int((e < 1).sum() != 1)
    ok8 &= (abs(abs(ev[0]) - float(rx)) < 1e-12 and abs(abs(ev[1]) - 1 / float(rx)) < 1e-9 and abs(ev[0] - lm_ex) < 1e-12 and abs(ratio - float(rx)) < 1e-7
            and resid_t <= 1e-14 and resid_b <= 1e-14 and nin == 0)
    parts.append(f"kappa {kp}: rho(v=0.2) exact {mp.nstr(rx, 9)} vs float |eig T| {abs(ev[0]):.9f}, layer ratio {ratio:.9f}; |H psi| top {resid_t:.1e} bottom {resid_b:.1e} (N=40); v-grid #bad {nin}")
rr_ = np.random.default_rng(7); wr = 0.0; wm = 0.0; ninset = set()
for it in range(100):
    Jp = rr_.choice([-1, 1]) * rr_.uniform(0.3, 2.0); jz = rr_.choice([-1, 1]) * rr_.uniform(0.2, 2.5); kp = rr_.choice([-1, 1]) * rr_.uniform(0.1, 1.5); x = rr_.uniform(0.02, 0.98)
    Jr = (Jp, Jp, jz); rx = rho_f(abs(kp), abs(jz), np.sin(np.pi * x))
    A_, B_ = blocks_float(Jr, kp, 0.5, x); ev = np.abs(np.linalg.eigvals(-np.linalg.solve(B_[2:4, 0:2], A_[2:4, 0:2]))); ninset.add(int((ev < 1).sum()))
    wr = max(wr, abs(np.sort(ev)[0] - rx) / rx)
    A_, B_ = blocks_float(Jr, kp, x, 0.5); Bd_ = B_.conj().T; ev = np.abs(np.linalg.eigvals(-np.linalg.solve(Bd_[0:2, 2:4], A_[0:2, 2:4]))); ninset.add(100 + int((ev < 1).sum()))
    wr = max(wr, abs(np.sort(ev)[0] - rx) / rx)
    N = 24; psi = top_mode(Jr, kp, x, N); res = (slab_hamiltonian(terms(Jr, kp), 2, (0.5, x), N) @ psi).reshape(N, 4)
    wm = max(wm, np.abs(res[:N - 1]).max() / np.linalg.norm(psi))
    psi = bottom_mode(Jr, kp, x, N); res = (slab_hamiltonian(terms(Jr, kp), 2, (x, 0.5), N) @ psi).reshape(N, 4)
    wm = max(wm, np.abs(res[1:]).max() / np.linalg.norm(psi))
ok8 &= (ninset == {1, 101} and wr < 1e-11 and wm < 1e-11)
check("(8) float: exact rho, lambda, mode vs the float slab (top u = 1/2 and bottom v = 1/2)", ok8,
      " | ".join(parts) + f" | 100 random couplings of random sign (J_x = J_y), top and bottom: #inside in {sorted(ninset)} (1 = top, 101 = bottom), max rel |float rho - exact| {wr:.1e}, max rel |H psi| {wm:.1e}")

# ------------------------------------------------------------------------------------------------ (9) finite-N splitting (50-digit slab) and |det H_N|
mp.mp.dps = 50
fAm = sp.lambdify((z1, z2, Jx, Jy, Jz, kap), A, "mpmath"); fBm = sp.lambdify((z1, z2, Jx, Jy, Jz, kap), B, "mpmath")


def HN(J, kp, u, v, N):
    zz1 = mp.expjpi(2 * mp.mpf(u)); zz2 = mp.expjpi(2 * mp.mpf(v)); ar = (zz1, zz2, mp.mpf(J[0]), mp.mpf(J[1]), mp.mpf(J[2]), mp.mpf(kp))
    Am = mp.matrix(fAm(*ar)); Bm = mp.matrix(fBm(*ar)); H = mp.zeros(4 * N, 4 * N)
    for L in range(N):
        for a in range(4):
            for b in range(4):
                H[4 * L + a, 4 * L + b] = Am[a, b]
                if L + 1 < N:
                    H[4 * L + a, 4 * (L + 1) + b] = Bm[a, b]; H[4 * (L + 1) + b, 4 * L + a] = mp.conj(Bm[a, b])
    return H


parts = []; ok9 = True
for kp in ('0.3', '0.6'):
    kpm = mp.mpf(kp); v = mp.mpf(1) / 5; rx = rho_mp(kpm, 1, v); E = {}
    for N in (10, 12):
        E[N] = min(abs(x) for x in mp.eigh(HN((1, 1, 1), kpm, mp.mpf(1) / 2, v, N), eigvals_only=True))
    rat = (E[12] / E[10]) ** (mp.mpf(1) / 2)
    H6 = HN((1, 1, 1), kpm, mp.mpf(1) / 2, v, 6); dr = abs(mp.det(H6)) / (16 * kpm ** 2 * mp.sin(mp.pi * v)) ** 12
    ok9 &= (abs(rat / rx ** 2 - 1) < 1e-6 and abs(dr - 1) < 1e-30 and E[12] < E[10])
    parts.append(f"kappa {kp}, v = 0.2: (E_12/E_10)^(1/2) = {mp.nstr(rat, 9)} vs rho^2 = {mp.nstr(rx ** 2, 9)}, E_12 = {mp.nstr(E[12], 5)}; |det H_6|/(16 k^2 sin pi v)^12 - 1 = {mp.nstr(dr - 1, 3)}")
check("(9) finite-N slab at (1/2, 0.2), 50-digit: lowest level decays as rho^{2N} (per-layer ratio rho^2); |det H_N| = (16 kappa^2 sin pi v)^{2N}", ok9,
      " | ".join(parts) + " (the determinant identity is exact: det H_N = |det A_pq|^{2N}, A_pp = 0; the ratio test is float/mp)")

# ------------------------------------------------------------------------------------------------ (10) negative control J_x != J_y (float; reported, not asserted)
def Etop(J, kp, u, v, N=40, tw=0.9):
    w, V = np.linalg.eigh(slab_hamiltonian(terms(J, kp), 2, (u, v), N))
    W = (np.abs(V) ** 2).reshape(N, 4, -1).sum(1); cand = np.where(W[:2].sum(0) > tw)[0]
    return w[cand[np.argmin(np.abs(w[cand]))]] if len(cand) else np.nan


def crossing(J, kp, v, lo=0.47, hi=0.53, n=13):
    us = np.linspace(lo, hi, n); Es = np.array([Etop(J, kp, u, v) for u in us])
    for i in range(n - 1):
        if np.isfinite(Es[i]) and np.isfinite(Es[i + 1]) and Es[i] * Es[i + 1] < 0:
            a, b, fa = us[i], us[i + 1], Es[i]
            for _ in range(45):
                m = 0.5 * (a + b); fm = Etop(J, kp, m, v)
                if fa * fm <= 0:
                    b = m
                else:
                    a, fa = m, fm
            return 0.5 * (a + b)
    return None


dd = sp.symbols("d_", positive=True)
ppd = (A.subs({z1: -1, Jx: Jy + dd}))[0:2, 0:2].applyfunc(sp.expand)
evp = sorted(ppd.eigenvals().keys(), key=lambda e: str(e))
E_ctrl = Etop((1, 1, 1), 0.3, 0.5, 0.2); E_neg = Etop((1, 0.8, 1), 0.3, 0.5, 0.2)
ustar = {v: crossing((1, 0.8, 1), 0.3, v) for v in (0.1, 0.25, 0.75)}
ok10 = (mzero(ppd + 2 * dd * sy) and set(evp) == {2 * dd, -2 * dd} and abs(E_ctrl) < 1e-12 and abs(E_neg) > 1e-3 and all(x is not None for x in ustar.values()))
check("(10) negative control J_x != J_y: p-block = -2 d sigma_y (eigenvalues +-2d) so the p-supported mode is not exact; float N = 40 shift of the zero line reported, no form asserted", ok10,
      f"float, kappa = 0.3, J = (1,0.8,1): E_top(1/2, 0.2) = {E_neg:+.4f} (control J = (1,1,1): {E_ctrl:+.1e}); zero crossing u*(v) of E_top: " + ", ".join(f"v={v}: {x:.5f}" for v, x in ustar.items()))

print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")

# A failed decisive check must fail the bounded execution.
if __name__ == "__main__":
    raise SystemExit(int(not all(RESULTS)))
