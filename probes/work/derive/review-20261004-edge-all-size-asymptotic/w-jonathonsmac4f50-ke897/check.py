#!/usr/bin/env python3
"""All-N finite-slab level at the top-surface zero line of the cell-cut a3 slab (supplied u=+1 comparator, J_x = J_y).

Disjoint checker for ATTEMPT.md.  It does NOT import the landed runner.  The supplied network (is_site / flavour / neighbours / hopping list)
is a transcription of the landed definition (scripts/composite_site_network_flux_free_exact_surface_zero_line_of_the_cell_cut_slab_2026_10_01.py
lines 43-106 and 149-173); it is the supplied model, so the check is NOT independent of the model, only of the landed proofs and numbers.

Setting: N layers 0..N-1, momenta (f1, f2) = (1/2, v), H_N = block tridiagonal (A on the diagonal, B above, B^dagger below).
Claims checked (labels as in ATTEMPT.md):
  S1  block structure (exact sympy, free J_x = J_y, J_z, kappa): p-block of A = 0, B has only p(L+1) -> q(L) entries, so in the ordering (all p, all q)
      H_N = [[0, U^dagger], [U, Qhat]], U = upper block bidiagonal (A_s on the diagonal, B_s above), Qhat = 1_N (x) A_qq.
  S2  the float slab built from the hopping list equals the block form (random couplings).
  S3  exact algebra on the surface-mode relation: left/right null vectors of A_s + lambda B_s at lambda = -i q rho and at lambda_out = -i q/rho,
      w B_s e, w A_qq w^dagger, in closed form.
  S4  exact rational point (rho = 1/3, sigma = 3/5, kappa = 1, J_z = 8/5, J_x = 1/2) re-verifies S3, U^{-1} = R + Delta, and v = 0 zero mode for every N.
  S5  explicit norm bounds (|1/s_N - Sigma_N| <= delta, |E_N/E_pred - 1| <= eta/(1-eta), lower bound at q0 = 0) against 40-digit slabs.
  S6  limit constants and sign law against 40-digit slabs; refined rate rho^{2N} (checked, not proved).
  S7  counterexample family q0 = 0 (v = 1/2, or Br = 0 at J_x = J_x*(v)): level is Theta(rho^N), not rho^{2N}.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"

import time

import mpmath as mp
import numpy as np
import sympy as sp

T0 = time.time()
RES = []


def check(label, ok, detail=""):
    RES.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {label} :: {detail}", flush=True)


# ---------------------------------------------------------------------------------------------- supplied network (transcribed from the landed definition)
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
            q = list(p)
            q[a] += s
            q = tuple(q)
            if is_site(q):
                out.append(q)
    return out


REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]


def reduce_(p):
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    return REPS.index((x - 2 * n1, y - 2 * n2, z)), (n1, n2, n3)


def hop_terms(J, kappa):
    """real hopping terms (a, b, n, t): M[a,b] += t e^{2 pi i f.n}, M[b,a] -= conj; H = i M."""
    out = []
    for p in REPS:
        a, _ = reduce_(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce_(q)
                out.append((a, b, n, 2 * J[AX[flavour(p, q)]]))
        nb = {flavour(p, q): q for q in neighbours(p)}
        for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
            r1, n1 = reduce_(nb[l])
            r2, n2 = reduce_(nb[m])
            out.append((r1, r2, (n2[0] - n1[0], n2[1] - n1[1], n2[2] - n1[2]), 2 * kappa))
    return out


Jx, Jy, Jz, kap = sp.symbols("J_x J_y J_z kappa", real=True)
z1, z2 = sp.symbols("z1 z2")
I = sp.I


def layer_blocks(terms):
    M = {}
    for (a, b, n, t) in terms:
        ph = z1 ** n[0] * z2 ** n[1]
        phc = z1 ** (-n[0]) * z2 ** (-n[1])
        M.setdefault(n[2], sp.zeros(4, 4))[a, b] += t * ph
        M.setdefault(-n[2], sp.zeros(4, 4))[b, a] -= t * phc
    return {m: (I * X).applyfunc(sp.expand) for m, X in M.items()}


def zero(e):
    return sp.simplify(sp.together(e)) == 0


def mzero(Mx):
    return all(zero(e) for e in Mx)


# ---------------------------------------------------------------------------------------------- S1 block structure (exact, symbolic)
BK = layer_blocks(hop_terms((Jx, Jy, Jz), kap))
A_full, B_full = BK[0], BK[1]
top = {z1: -1, Jy: Jx}
A0 = A_full.subs(top).applyfunc(sp.expand)
B0 = B_full.subs(top).applyfunc(sp.expand)
As_h = sp.Matrix([[4 * I * kap, 2 * I * Jz], [0, 2 * I * kap * (z2 - 1)]])
Bs_h = sp.Matrix([[-2 * I * kap * (z2 - 1) / z2, 0], [-2 * I * Jz, 4 * I * kap]])
Qh = sp.Matrix([[2 * I * kap * (z2 ** 2 - 1) / z2, 2 * I * Jx * (z2 + 1) / z2],
                [-2 * I * Jx * (z2 + 1), 2 * I * kap * (1 - z2 ** 2) / z2]])


def dag(X):
    return X.subs({z2: 1 / z2}, simultaneous=True).xreplace({I: -I}).T.applyfunc(sp.expand)


ok = (sorted(BK) == [-1, 0, 1]
      and A0[0:2, 0:2] == sp.zeros(2, 2)
      and B0[0:2, :] == sp.zeros(2, 4) and B0[2:4, 2:4] == sp.zeros(2, 2)
      and mzero(A0[2:4, 0:2] - As_h) and mzero(B0[2:4, 0:2] - Bs_h) and mzero(A0[2:4, 2:4] - Qh)
      and mzero(A0[0:2, 2:4] - dag(As_h)) and mzero(A0 - dag(A0)) and mzero(BK[-1].subs(top) - dag(B0)))
check("S1 block structure at f1 = 1/2, J_x = J_y: A_pp = 0, B only p(L+1)->q(L); A_s, B_s, A_qq in closed form; H_N = [[0,U^dag],[U,1_N (x) A_qq]]", ok,
      "exact sympy for free (J_x, J_z, kappa, z2); A_qq = [[2ik(z2^2-1)/z2, 2iJ_x(z2+1)/z2],[-2iJ_x(z2+1), 2ik(1-z2^2)/z2]]")

# ---------------------------------------------------------------------------------------------- numerics helpers
mp.mp.dps = 40
rng = np.random.default_rng(20261004)
fAs = sp.lambdify((z2, Jx, Jz, kap), As_h, "mpmath")
fBs = sp.lambdify((z2, Jx, Jz, kap), Bs_h, "mpmath")
fQ = sp.lambdify((z2, Jx, Jz, kap), Qh, "mpmath")


def blocks(jx, jz, k, v):
    zz = mp.expjpi(2 * v)
    return mp.matrix(fAs(zz, jx, jz, k)), mp.matrix(fBs(zz, jx, jz, k)), mp.matrix(fQ(zz, jx, jz, k))


def Umat(As, Bs, N):
    U = mp.zeros(2 * N, 2 * N)
    for L in range(N):
        for a in range(2):
            for b in range(2):
                U[2 * L + a, 2 * L + b] = As[a, b]
                if L + 1 < N:
                    U[2 * L + a, 2 * (L + 1) + b] = Bs[a, b]
    return U


def HN(As, Bs, Q, N):
    """H_N in the ordering (all p, all q)."""
    U = Umat(As, Bs, N)
    H = mp.zeros(4 * N, 4 * N)
    for i in range(2 * N):
        for j in range(2 * N):
            H[2 * N + i, j] = U[i, j]
            H[j, 2 * N + i] = mp.conj(U[i, j])
    for L in range(N):
        for a in range(2):
            for b in range(2):
                H[2 * N + 2 * L + a, 2 * N + 2 * L + b] = Q[a, b]
    return H


def lowest(H):
    ev = mp.eigh(H, eigvals_only=True)
    return min(ev, key=abs)


def rho_of(k, jz, v):
    s = mp.sin(mp.pi * v)
    ta = s + (4 * k ** 2 + jz ** 2) / (4 * k ** 2 * s)
    return (ta - mp.sqrt(ta ** 2 - 4)) / 2


# ---------------------------------------------------------------------------------------------- S2 slab from hopping list == block form
def slab_float(J, k, u, v, N):
    T = hop_terms(J, k)
    M = np.zeros((4 * N, 4 * N), dtype=complex)
    for (a, b, n, t) in T:
        ph = np.exp(2j * np.pi * (u * n[0] + v * n[1]))
        L = np.arange(N)
        L2 = L + n[2]
        keep = (L2 >= 0) & (L2 < N)
        L, L2 = L[keep], L2[keep]
        M[4 * L + a, 4 * L2 + b] += t * ph
        M[4 * L2 + b, 4 * L + a] -= t * np.conj(ph)
    return 1j * M


worst = 0.0
for it in range(12):
    jx = float(rng.uniform(-2, 2))
    jz = float(rng.choice([-1, 1]) * rng.uniform(0.2, 2))
    k = float(rng.choice([-1, 1]) * rng.uniform(0.1, 1.5))
    v = float(rng.uniform(0.05, 0.95))
    N = int(rng.integers(2, 6))
    Hs = slab_float((jx, jx, jz), k, 0.5, v, N)
    As, Bs, Q = blocks(mp.mpf(jx), mp.mpf(jz), mp.mpf(k), mp.mpf(v))
    Hb = np.array(HN(As, Bs, Q, N).tolist(), dtype=complex)
    perm = [4 * L + a for L in range(N) for a in (0, 1)] + [4 * L + a for L in range(N) for a in (2, 3)]
    worst = max(worst, np.abs(Hs[np.ix_(perm, perm)] - Hb).max())
check("S2 float slab from the hopping list = (p,q)-ordered block form H_N, 12 random couplings of random sign, N = 2..5", worst < 1e-12, f"max abs difference {worst:.1e}")

# ---------------------------------------------------------------------------------------------- S3 exact algebra of the surface-mode relation
q, rho, jx_ = sp.symbols("q rho J_x_", nonzero=True)
sig = (q - 1 / q) / (2 * I)                  # sin(pi v)
cs = (q + 1 / q) / 2                         # cos(pi v)
z2q = q ** 2
Jz2 = 4 * kap ** 2 * (sig * (rho + 1 / rho) - sig ** 2 - 1)      # the defining relation rho + 1/rho = sigma + (4k^2+J_z^2)/(4k^2 sigma)


def red(expr):
    """reduce a rational function of (q, rho, kappa, J_z, J_x) modulo J_z^2 = Jz2 and return 0 iff it vanishes."""
    expr = sp.together(expr)
    num, den = sp.fraction(expr)
    num = sp.expand(num)
    r = sp.rem(sp.Poly(num, Jz), sp.Poly(Jz ** 2 - Jz2, Jz))
    return sp.simplify(sp.expand(r.as_expr())) == 0


def conj_(e):
    return e.subs({q: 1 / q}, simultaneous=True).xreplace({I: -I})


Asq = As_h.subs(z2, z2q)
Bsq = Bs_h.subs(z2, z2q)
Qq = Qh.subs(z2, z2q)
ok3 = True
detail = []
for rr, tag in ((rho, "in"), (1 / rho, "out")):
    lam = -I * q * rr
    Mq = (Asq + lam * Bsq).applyfunc(sp.simplify)
    e = sp.Matrix([2 * kap * (sig - rr), -Jz * rr])
    w = sp.Matrix([[2 * I * kap * q * (sig - rr), -Jz]])
    c1 = all(red(x) for x in (Mq * e))
    c2 = all(red(x) for x in (w * Mq))
    ok3 &= c1 and c2
    detail.append(f"{tag}: M e = 0 {c1}, w M = 0 {c2}")
    if tag == "in":
        e1 = sp.Matrix([1, -Jz * rr / (2 * kap * (sig - rr))])          # e = (1, r)
        W = 4 * kap ** 2 * (sig - rr) ** 2 + Jz ** 2
        wBe = (w * Bsq * e1)[0, 0]
        c3 = red(wBe - 2 * I * sig / (sig - rr) * W)
        wd = w.applyfunc(conj_).T
        wQw = (w * Qq * wd)[0, 0]
        Br = sig * (Jz ** 2 - 4 * kap ** 2 * (sig - rr) ** 2) + 2 * Jx * Jz * (sig - rr)
        c4 = red(wQw - 8 * kap * cs * Br)
        c5 = red((w * wd)[0, 0] - W)
        ok3 &= c3 and c4 and c5
        detail.append(f"w B_s e = 2i sigma W/(sigma-rho): {c3}; w A_qq w^dag = 8 kappa cos(pi v) Br: {c4}; |w|^2 = W: {c5}")
# lambda_in * lambda_out = det T = -z2 and the relation is symmetric under rho <-> 1/rho
ok3 &= zero((-I * q * rho) * (-I * q / rho) + z2q)
check("S3 exact: A_s + lambda B_s has right null (2k(sigma-rho), -J_z rho), left null (2ik q(sigma-rho), -J_z) at lambda = -i q rho and (rho -> 1/rho) at -i q/rho; "
      "w B_s e, w A_qq w^dag, |w|^2 in closed form", ok3, "; ".join(detail))

# ---------------------------------------------------------------------------------------------- S4 exact rational point
# sigma = 3/5, cos = 4/5, q = (4+3i)/5, rho = 1/3, kappa = 1  =>  J_z = 8/5 ; J_x = 1/2
R_ = sp.Rational
qv = R_(4, 5) + I * R_(3, 5)
sgv, csv, rv = R_(3, 5), R_(4, 5), R_(1, 3)
kv, jzv, jxv = sp.Integer(1), R_(8, 5), R_(1, 2)
z2v = qv ** 2
tau_ok = sp.simplify(rv + 1 / rv - (sgv + (4 * kv ** 2 + jzv ** 2) / (4 * kv ** 2 * sgv))) == 0
Asv = As_h.subs({z2: z2v, Jz: jzv, kap: kv}).applyfunc(sp.simplify)
Bsv = Bs_h.subs({z2: z2v, Jz: jzv, kap: kv}).applyfunc(sp.simplify)
Qv = Qh.subs({z2: z2v, Jz: jzv, kap: kv, Jx: jxv}).applyfunc(sp.simplify)
lamv = -I * qv * rv
Mv = (Asv + lamv * Bsv).applyfunc(sp.simplify)
ev_ = sp.Matrix([1, -jzv * rv / (2 * kv * (sgv - rv))])
wv = sp.Matrix([[2 * I * kv * qv * (sgv - rv), -jzv]])
okA = tau_ok and (Mv * ev_).applyfunc(sp.simplify) == sp.zeros(2, 1) and (wv * Mv).applyfunc(sp.simplify) == sp.zeros(1, 2)
Tm = (-(Bsv.inv()) * Asv).applyfunc(sp.simplify)
okA &= sp.simplify(Tm.det() + z2v) == 0 and sp.simplify((Tm - lamv * sp.eye(2)).det()) == 0 and sp.simplify((Tm - (-I * qv / rv) * sp.eye(2)).det()) == 0
# exact U^{-1} = R + Delta, N = 4, blocks T^{-k} A_s^{-1}
Ninv = 4
Ue = sp.zeros(2 * Ninv, 2 * Ninv)
for L in range(Ninv):
    Ue[2 * L:2 * L + 2, 2 * L:2 * L + 2] = Asv
    if L + 1 < Ninv:
        Ue[2 * L:2 * L + 2, 2 * L + 2:2 * L + 4] = Bsv
Uinv = Ue.inv().applyfunc(sp.simplify)
Ai = Asv.inv()
Tinv = Tm.inv()
okB = True
for L in range(Ninv):
    for L2 in range(Ninv):
        blk = Uinv[2 * L:2 * L + 2, 2 * L2:2 * L2 + 2]
        want = (Tinv ** (L2 - L) * Ai if L2 >= L else sp.zeros(2, 2))
        okB &= (blk - want).applyfunc(sp.simplify) == sp.zeros(2, 2)
# exact closed forms at the point
Wv = 4 * kv ** 2 * (sgv - rv) ** 2 + jzv ** 2
Brv = sgv * (jzv ** 2 - 4 * kv ** 2 * (sgv - rv) ** 2) + 2 * jxv * jzv * (sgv - rv)
wd_v = wv.applyfunc(sp.conjugate).T
okC = (sp.simplify((wv * Bsv * ev_)[0, 0] - 2 * I * sgv / (sgv - rv) * Wv) == 0
       and sp.simplify((wv * Qv * wd_v)[0, 0] - 8 * kv * csv * Brv) == 0)
# v = 0 compact mode on every N (exact, rational): x_0 = (J_z, -2 kappa) on layer 0, zero energy of H_N for N = 1..8
As0 = As_h.subs({z2: 1, Jz: jzv, kap: kv}); Bs0 = Bs_h.subs({z2: 1, Jz: jzv, kap: kv}); Q0 = Qh.subs({z2: 1, Jz: jzv, kap: kv, Jx: jxv})
okD = True
for N in range(1, 9):
    U = sp.zeros(2 * N, 2 * N)
    for L in range(N):
        U[2 * L:2 * L + 2, 2 * L:2 * L + 2] = As0
        if L + 1 < N:
            U[2 * L:2 * L + 2, 2 * L + 2:2 * L + 4] = Bs0
    Hn = sp.zeros(4 * N, 4 * N)
    Hn[2 * N:, :2 * N] = U
    Hn[:2 * N, 2 * N:] = U.H
    for L in range(N):
        Hn[2 * N + 2 * L:2 * N + 2 * L + 2, 2 * N + 2 * L:2 * N + 2 * L + 2] = Q0
    psi = sp.zeros(4 * N, 1)
    psi[0], psi[1] = jzv, -2 * kv
    okD &= (Hn * psi).applyfunc(sp.simplify) == sp.zeros(4 * N, 1)
check("S4 exact rational point rho=1/3 sigma=3/5 kappa=1 J_z=8/5: null vectors, det T = -z2, eigenvalues -iq rho and -iq/rho, wBe and wQw closed forms; "
      "U_4^{-1} blocks = T^{-(L'-L)} A_s^{-1}", okA and okB and okC, f"relation {tau_ok}, nulls/eigs {okA}, inverse blocks {okB}, closed forms {okC}")
check("S4b v = 0 (z2 = 1) exact: the compact layer-0 vector (J_z, -2 kappa, 0, ...) is an exact zero mode of H_N for every N = 1..8 (J_x = 1/2, J_z = 8/5, kappa = 1)", okD, "E_N = 0 exactly; det A_pq = 0 there")

# ---------------------------------------------------------------------------------------------- explicit constants
def consts(jx, jz, k, v):
    """all quantities of the theorem for (J_x = J_y, J_z, kappa, v); mp numbers."""
    r = rho_of(abs(k), abs(jz), v)
    s = mp.sin(mp.pi * v)
    c = mp.cos(mp.pi * v)
    W = 4 * k ** 2 * (s - r) ** 2 + jz ** 2
    Br = s * (jz ** 2 - 4 * k ** 2 * (s - r) ** 2) + 2 * jx * jz * (s - r)
    X = 16 * k ** 2 * s ** 2 * W / (4 * k ** 2 * (s - r) ** 2 + jz ** 2 * r ** 2)
    rp = 1 / r
    Wp = 4 * k ** 2 * (s - rp) ** 2 + jz ** 2
    Xp = 16 * k ** 2 * s ** 2 * Wp / (4 * k ** 2 * (s - rp) ** 2 + jz ** 2 * rp ** 2)
    q0 = 8 * k * c * Br / W
    qbar = 4 * abs(c) * mp.sqrt(4 * k ** 2 * s ** 2 + jx ** 2)
    delta = (1 / mp.sqrt(X) + r / mp.sqrt(Xp)) / (1 - r)
    return dict(rho=r, sigma=s, cos=c, W=W, Br=Br, X=X, Xp=Xp, q0=q0, qbar=qbar, delta=delta)


def Sigma_N(cst, N):
    r = cst["rho"]
    S1 = sum(r ** (2 * L) for L in range(N))
    S2 = sum(r ** (-2 * L) for L in range(N))
    return mp.sqrt(S1 * S2) / (r * mp.sqrt(cst["X"]))


def E_pred(cst, N):
    q0 = cst["q0"]
    s = 1 / Sigma_N(cst, N)
    return (q0 - mp.sign(q0) * mp.sqrt(q0 ** 2 + 4 * s ** 2)) / 2


def Cclosed(cst):
    return (1 - cst["rho"] ** 2) ** 2 * cst["X"] / abs(cst["q0"])


# ---------------------------------------------------------------------------------------------- S5 explicit bounds against 40-digit slabs
SETS = [("J=(1,1,1) k=0.3 v=0.2", 1, 1, "0.3", "0.2"),
        ("J=(1,1,1) k=0.6 v=0.2", 1, 1, "0.6", "0.2"),
        ("Jx=0.7 Jz=-1.3 k=-0.4 v=0.8", "0.7", "-1.3", "-0.4", "0.8"),
        ("Jx=-1.1 Jz=0.6 k=0.5 v=0.35", "-1.1", "0.6", "0.5", "0.35"),
        ("Jx=2 Jz=0.5 k=-0.2 v=0.65", 2, "0.5", "-0.2", "0.65")]
Nlist = (8, 12, 16)
okS5a = okS5b = okS5c = True
rows = []
bad = []
worst_ratio = 0
for (nm, jx, jz, k, v) in SETS:
    jx, jz, k, v = (mp.mpf(str(x)) for x in (jx, jz, k, v))
    cst = consts(jx, jz, k, v)
    As, Bs, Q = blocks(jx, jz, k, v)
    r = cst["rho"]
    # relation checks: rho < sigma, rho < 1, q0 not zero
    okS5a &= (r < cst["sigma"] < 1) and abs(cst["q0"]) > 0
    # numerical spectral data of the unperturbed matrices: delta and R
    for N in Nlist:
        U = Umat(As, Bs, N)
        Ui = U ** -1
        G = Ui * Ui.H
        smax = mp.sqrt(max(mp.eigh(G, eigvals_only=True)))              # ||U^-1||
        Sg = Sigma_N(cst, N)
        okS5a &= abs(smax - Sg) <= cst["delta"]
        # exact E_N
        H = HN(As, Bs, Q, N)
        E = lowest(H)
        Ep = E_pred(cst, N)
        sN = 1 / smax
        okS5b &= abs(E) <= sN * (1 + mp.mpf(10) ** -30)                 # |E_N| <= s_N (test vector (x0, 0))
        # bound chain
        vN = 2 * Sg * cst["qbar"] * cst["delta"] + cst["qbar"] * cst["delta"] ** 2 + cst["delta"]
        aa = Sg * cst["q0"]
        mud = Sg * (abs(aa) + mp.sqrt(aa ** 2 + 4)) / 2
        mus = 2 * Sg / (abs(aa) + mp.sqrt(aa ** 2 + 4))
        cond = (mud - vN > mus + vN)
        eta = vN / mud
        if cond and eta < 1:
            bound = eta / (1 - eta)
            rel = abs(E / Ep - 1)
            okS5c &= rel <= bound
            rows.append(f"{nm} N={N}: rel err {mp.nstr(rel, 3)} <= bound {mp.nstr(bound, 3)}")
        else:
            rows.append(f"{nm} N={N}: N0 condition not met (no claim)")
check("S5a rho < sigma < 1, q0 != 0, and ||U_N^{-1}|| within delta of Sigma_N (explicit delta) for 5 parameter sets x N = 8,12,16", okS5a, "")
check("S5b |E_N| <= s_N = sigma_min(U_N) (test vector (x0,0)) in all runs", okS5b, "")
check("S5c whenever the N0 condition holds: |E_N/E_pred - 1| <= eta/(1-eta) with eta = ||V||/|mu_d| (Weyl); E_pred = small root of E^2 - q0 E - s_N^2", okS5c,
      " | ".join(rows[:6]) + " | ...")
nbound = sum("not met" not in x for x in rows)
check("S5d the N0 condition (and hence the bound of S5c) is actually exercised in at least 5 runs", nbound >= 5, f"{nbound} of {len(rows)} runs satisfy the condition")

# S5e: the rank-one part R and the remainder Delta, built from the null vectors, against the true U_N^{-1}
def spec_norm(Mx):
    n = Mx.rows
    G = Mx * Mx.H
    return mp.sqrt(max(mp.eigh(G, eigvals_only=True)))


okE = True
detE = []
for (nm, jx, jz, k, v) in SETS:
    jx, jz, k, v = (mp.mpf(str(x)) for x in (jx, jz, k, v))
    cst = consts(jx, jz, k, v)
    As, Bs, Q = blocks(jx, jz, k, v)
    r, sg_ = cst["rho"], cst["sigma"]
    qq = mp.expjpi(v)
    lam = -1j * qq * r
    W = cst["W"]
    e = mp.matrix([1, -jz * r / (2 * k * (sg_ - r))])
    w = mp.matrix([[2j * k * qq * (sg_ - r), -jz]])
    wBe = (w * Bs * e)[0, 0]
    gdag = -w / (lam * wBe)                                 # g^dagger = f A_s^{-1}, f = w B_s / (w B_s e)
    # primes
    lamo = -1j * qq / r
    eo = mp.matrix([1, -jz * (1 / r) / (2 * k * (sg_ - 1 / r))])
    wo = mp.matrix([[2j * k * qq * (sg_ - 1 / r), -jz]])
    wBeo = (wo * Bs * eo)[0, 0]
    gdago = -wo / (lamo * wBeo)
    Pin = e * (w * Bs) / wBe                                # e f
    Pout = eo * (wo * Bs) / wBeo
    Ai = As ** -1
    n_in = spec_norm(e * gdag)
    n_out = spec_norm(eo * gdago)
    okE &= abs(n_in - 1 / (r * mp.sqrt(cst["X"]))) < mp.mpf(10) ** -30 and abs(n_out - r / mp.sqrt(cst["Xp"])) < mp.mpf(10) ** -30
    okE &= spec_norm(Pin + Pout - mp.eye(2)) < mp.mpf(10) ** -30 and spec_norm(Pin * Ai - e * gdag) < mp.mpf(10) ** -30
    N = 8
    Ui = Umat(As, Bs, N) ** -1
    Rm = mp.zeros(2 * N, 2 * N)
    for L in range(N):
        for L2 in range(N):
            blk = (lam ** (L - L2)) * (e * gdag)
            for a in range(2):
                for b in range(2):
                    Rm[2 * L + a, 2 * L2 + b] = blk[a, b]
    nR = spec_norm(Rm)
    nD = spec_norm(Ui - Rm)
    Sg_closed = r ** (-N) * (1 - r ** (2 * N)) / ((1 - r ** 2) * mp.sqrt(cst["X"]))
    okE &= abs(nR - Sigma_N(cst, N)) < mp.mpf(10) ** -25 * nR and nD <= cst["delta"] and abs(Sg_closed / Sigma_N(cst, N) - 1) < mp.mpf(10) ** -30
    detE.append(f"{nm}: ||R|| = Sigma_N ok, ||Delta|| = {mp.nstr(nD, 4)} <= delta = {mp.nstr(cst['delta'], 4)}")
check("S5e R_{L,L'} = lambda^{L-L'} e g^dag has ||R|| = Sigma_N = rho^{-N}(1-rho^{2N})/((1-rho^2) sqrt X) exactly, ||e g^dag|| = 1/(rho sqrt X), ||e' g'^dag|| = rho/sqrt X', and ||U_8^{-1} - R|| <= delta (5 sets)", okE, " | ".join(detE))

# ---------------------------------------------------------------------------------------------- S6 limit constant, sign law, refined rate
okS6 = True
parts = []
for (nm, jx, jz, k, v) in SETS:
    jx, jz, k, v = (mp.mpf(str(x)) for x in (jx, jz, k, v))
    cst = consts(jx, jz, k, v)
    As, Bs, Q = blocks(jx, jz, k, v)
    r = cst["rho"]
    C = Cclosed(cst)
    sgn = -mp.sign(cst["q0"])
    rels = {}
    for N in (6, 9, 12):
        E = lowest(HN(As, Bs, Q, N))
        okS6 &= (mp.sign(E) == sgn)
        rels[N] = abs(E / r ** (2 * N) / (sgn * C) - 1)
    # relative remainder: <= 1000 rho^{2N} at N = 12 and shrinking at least like 30 rho^6 per three layers (CHECKED rate, polynomial prefactors allowed)
    okS6 &= rels[12] <= 1000 * r ** 24 and rels[12] / rels[9] <= 30 * r ** 6 and rels[9] / rels[6] <= 30 * r ** 6
    parts.append(f"{nm}: rel err N=6,9,12 = {mp.nstr(rels[6], 2)}, {mp.nstr(rels[9], 2)}, {mp.nstr(rels[12], 2)}; E/rho^2N(12) = {mp.nstr(E / r ** 24, 10)} vs sign*C = {mp.nstr(sgn * C, 10)}")
check("S6 limit E_N / rho^{2N} -> -(1-rho^2)^2 X / q0, sign = -sgn(kappa cos(pi v) Br), 5 parameter sets; relative remainder decays like rho^{2N} (CHECKED rate, not proved)", okS6, " | ".join(parts))

# ---------------------------------------------------------------------------------------------- S7 counterexample family q0 = 0
# (i) v = 1/2: cos(pi v) = 0.  (ii) v != 1/2 with Br = 0 at J_x = J_x*(v)
okS7 = True
parts = []
for (jz, k, v) in (("1", "0.3", "0.2"), ("-0.8", "0.5", "0.7"), ("1.5", "-0.4", "0.35")):
    jz, k, v = (mp.mpf(x) for x in (jz, k, v))
    r = rho_of(abs(k), abs(jz), v)
    s = mp.sin(mp.pi * v)
    jxs = s * (4 * k ** 2 * (s - r) ** 2 - jz ** 2) / (2 * jz * (s - r))
    cst = consts(jxs, jz, k, v)
    okS7 &= abs(cst["Br"]) < mp.mpf(10) ** -30
    As, Bs, Q = blocks(jxs, jz, k, v)
    out = []
    for N in (6, 10, 14):
        H = HN(As, Bs, Q, N)
        ev = sorted(mp.eigh(H, eigvals_only=True), key=abs)
        E = ev[0]
        Sg = Sigma_N(cst, N)
        vN = 2 * Sg * cst["qbar"] * cst["delta"] + cst["qbar"] * cst["delta"] ** 2 + cst["delta"]
        lower = 1 / (vN + Sg)                                             # |E_N| >= 1/(2 Sigma qbar delta + qbar delta^2 + delta + Sigma) when q0 = 0
        okS7 &= lower <= abs(E) <= 1 / (Sg - cst["delta"]) * (1 + mp.mpf(10) ** -30)
        out.append((N, abs(E) / r ** N, abs(E) / r ** (2 * N)))
    # Theta(rho^N): ratios to rho^N stabilise, ratios to rho^{2N} blow up
    okS7 &= abs(out[2][1] / out[1][1] - 1) < mp.mpf(10) ** -4 and out[2][2] / out[1][2] > r ** -4 / 2
    parts.append(f"Jz={mp.nstr(jz, 3)} k={mp.nstr(k, 3)} v={mp.nstr(v, 3)} Jx*={mp.nstr(jxs, 8)}: |E|/rho^N = " + ", ".join(mp.nstr(o[1], 9) for o in out)
                 + f"; |E|/rho^2N = " + ", ".join(mp.nstr(o[2], 4) for o in out))
# v = 1/2
jz, k = mp.mpf("1"), mp.mpf("0.3")
cst = consts(mp.mpf(1), jz, k, mp.mpf(1) / 2)
As, Bs, Q = blocks(mp.mpf(1), jz, k, mp.mpf(1) / 2)
r = cst["rho"]
o12 = []
for N in (6, 10, 14):
    ev = sorted(mp.eigh(HN(As, Bs, Q, N), eigvals_only=True), key=abs)
    o12.append((abs(ev[0]) / r ** N, abs(ev[1]) / r ** N))
okS7 &= abs(cst["q0"]) < mp.mpf(10) ** -30 and abs(o12[2][0] / o12[1][0] - 1) < mp.mpf(10) ** -4
parts.append("v=1/2 J=(1,1,1) k=0.3: |E|/rho^N = " + ", ".join(mp.nstr(o[0], 9) for o in o12))
check("S7 counterexample family q0 = 0 (v = 1/2, and v != 1/2 at J_x = J_x*(v) = sigma(4k^2(sigma-rho)^2 - J_z^2)/(2 J_z (sigma-rho))): level is Theta(rho^N), "
      "bracketed by the explicit bounds, not O(rho^{2N})", okS7, " | ".join(parts))

# ---------------------------------------------------------------------------------------------- landed diagnostic reproduced as an instance
mp.mp.dps = 50
rows = []
okL = True
for kk in ("0.3", "0.6"):
    kk = mp.mpf(kk)
    cst = consts(mp.mpf(1), mp.mpf(1), kk, mp.mpf(1) / 5)
    As, Bs, Q = blocks(mp.mpf(1), mp.mpf(1), kk, mp.mpf(1) / 5)
    E10, E12 = (abs(lowest(HN(As, Bs, Q, N))) for N in (10, 12))
    ratio = mp.sqrt(E12 / E10)
    r2 = cst["rho"] ** 2
    ep10 = abs(E_pred(cst, 10))
    okL &= abs(ratio / r2 - 1) < mp.mpf(10) ** -6 and abs(E10 / ep10 - 1) < 1000 * cst["rho"] ** 20
    rows.append(f"kappa {kk}: (E12/E10)^(1/2)/rho^2 - 1 = {mp.nstr(ratio / r2 - 1, 3)}; E10/E_pred(10) - 1 = {mp.nstr(E10 / ep10 - 1, 3)}")
check("S8 the landed N = 10, 12 diagnostic (J=(1,1,1), v = 0.2) is an instance: E_N = E_pred(N) (1 + O(rho^{2N})) with the explicit constants", okL, " | ".join(rows))

print(f"runtime {time.time() - T0:.0f} s")
if all(RES):
    print("HIT: for J_x = J_y, kappa J_z != 0, v in (0,1): E_N = -(s_N^2/q0)(1+O(rho^N)) with explicit constants (limit -(1-rho^2)^2 X/q0 rho^{2N}) unless q0 = 0, "
          "where the level is Theta(rho^N); q0 = 0 occurs at v = 1/2 and at J_x = J_x*(v), so the landed rho^2-per-layer ratio is not a law on the whole coupling domain")
print(f"TOTAL: PASS={sum(RES)} FAIL={len(RES) - sum(RES)}")
print("SUMMARY: the finite-N lowest level of the cell-cut slab at (1/2, v) is derived from the block recurrence with explicit constants (rho^{2N} with exact coefficient when q0 != 0, Theta(rho^N) when q0 = 0), "
      "and the claims are checked in exact algebra and 40-digit slabs; the rho^{2N} relative remainder is checked, not proved.")
raise SystemExit(int(not all(RES)))
