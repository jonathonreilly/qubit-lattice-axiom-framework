"""C5 s2: the two-qubit Clifford family U = f + i(h1 tau1 + h2 tau2) + i tau3 g.sigma has W3 = 0.

Lemma C (NOTE.md): Phi: S^5 -> U(4), Phi(x) = x0 + i sum_{j=1..5} x_j Gamma_j with five pairwise
anticommuting Hermitian involutions. (i) Phi^* tr(theta^3) = 0 POINTWISE (checked symbolically here),
(ii) hence W3[Phi o x] = 0 for every smooth x: T^3 -> S^5 (covariant or not, finite range or not).
"""
import itertools
import sys
import numpy as np
import sympy as sp
from w3lib import Checker, PAULI, smooth_grid, wilson_weyl_map, w3_from_fields, lp_eval_grid

ck = Checker()
P = [sp.Matrix(m.tolist()).applyfunc(sp.nsimplify) for m in PAULI]
kr = lambda a, b: sp.kronecker_product(a, b)
G = [kr(P[1], P[0]), kr(P[2], P[0]), kr(P[3], P[1]), kr(P[3], P[2]), kr(P[3], P[3])]  # tau1, tau2, tau3 sigma_a
ok = all((G[a] * G[b] + G[b] * G[a]) == (2 * sp.eye(4) if a == b else sp.zeros(4)) for a in range(5) for b in range(5))
ck.check('Gamma = (tau1, tau2, tau3 sx, tau3 sy, tau3 sz) are Hermitian, square to 1 and pairwise anticommute (exact)',
         ok and all(g.H == g for g in G))

x = sp.symbols('x0:6', real=True)
Phi = x[0] * sp.eye(4) + sp.I * sum((x[j + 1] * G[j] for j in range(5)), sp.zeros(4))
Phid = x[0] * sp.eye(4) - sp.I * sum((x[j + 1] * G[j] for j in range(5)), sp.zeros(4))
r2 = sum(xi ** 2 for xi in x)
ck.check('Phi^dag Phi = |x|^2 * 1 (exact), so Phi(S^5) lies in U(4)', sp.simplify(Phid * Phi - r2 * sp.eye(4)) == sp.zeros(4))
# theta = Phi^{-1} dPhi on S^5 equals Phi^dag dPhi. Components of tr(theta^3) on R^6 (with Phi^dag in place of
# Phi^{-1}; equal on the sphere) as antisymmetrized polynomials T_{ijl}(x).
th = [Phid * Phi.diff(xi) for xi in x]
allzero = True
for i, j, l in itertools.combinations(range(6), 3):
    T = 0
    for (a, b, c), sgn in zip(itertools.permutations((i, j, l)), (1, -1, -1, 1, 1, -1)):
        # sign of permutation: itertools order (i,j,l),(i,l,j),(j,i,l),(j,l,i),(l,i,j),(l,j,i)
        T += sgn * (th[a] * th[b] * th[c]).trace()
    if sp.expand(T) != 0:
        allzero = False
        print('nonzero component', (i, j, l), sp.factor(sp.expand(T)))
ck.check('all 20 components of tr(theta^3) vanish identically as polynomials in x: Phi^* tr(theta^3) = 0 pointwise (exact)', allzero)
# sanity: the same symbolic routine detects the non-vanishing form on SU(2) = S^3 (positive control)
y = sp.symbols('y0:4', real=True)
Ps = y[0] * sp.eye(2) + sp.I * sum((y[j + 1] * P[j + 1] for j in range(3)), sp.zeros(2))
Psd = y[0] * sp.eye(2) - sp.I * sum((y[j + 1] * P[j + 1] for j in range(3)), sp.zeros(2))
ths = [Psd * Ps.diff(yi) for yi in y]
T = 0
for (a, b, c), sgn in zip(itertools.permutations((1, 2, 3)), (1, -1, -1, 1, 1, -1)):
    T += sgn * (ths[a] * ths[b] * ths[c]).trace()
T = sp.expand(T)
print('control: S^3 -> SU(2) component T_123 at y=(1,0,0,0):', T.subs({y[0]: 1, y[1]: 0, y[2]: 0, y[3]: 0}))
ck.check('control: the same routine gives a NONZERO component for SU(2) = S^3 (so the zero above is not an artefact)',
         T.subs({y[0]: 1, y[1]: 0, y[2]: 0, y[3]: 0}) != 0)

# ---------------- numerical checks ----------------
Gn = [np.array(g.tolist(), dtype=complex) for g in G]
rng = np.random.default_rng(5)

def smooth_S5_map(coef):
    # x(k) = v(k)/|v(k)|, v_j = sum over |n|_inf <= 1 of coef * cos/sin; nonvanishing checked
    ns = list(itertools.product((-1, 0, 1), repeat=3))
    def func(K1, K2, K3):
        Ks = [K1, K2, K3]
        v = []
        dv = []
        for j in range(6):
            vj = coef[j, 0] + 0 * K1
            dvj = [0 * K1, 0 * K1, 0 * K1]
            for m, n in enumerate(ns):
                arg = n[0] * K1 + n[1] * K2 + n[2] * K3
                vj = vj + coef[j, m + 1] * np.cos(arg + coef[j, 28 + m])
                for b in range(3):
                    dvj[b] = dvj[b] - coef[j, m + 1] * n[b] * np.sin(arg + coef[j, 28 + m])
            v.append(vj)
            dv.append(dvj)
        nr = np.sqrt(sum(vj ** 2 for vj in v))
        xs = [vj / nr for vj in v]
        dx = [[dv[j][b] / nr - v[j] * sum(v[i] * dv[i][b] for i in range(6)) / nr ** 3 for b in range(3)] for j in range(6)]
        U = xs[0][..., None, None] * np.eye(4) + 1j * sum(xs[j + 1][..., None, None] * Gn[j] for j in range(5))
        dU = [dx[0][b][..., None, None] * np.eye(4) + 1j * sum(dx[j + 1][b][..., None, None] * Gn[j] for j in range(5)) for b in range(3)]
        return U, dU, nr.min()
    return func

worst = 0.0
for t in range(6):
    coef = rng.normal(size=(6, 55))
    coef[:, 0] += 0.0
    f = smooth_S5_map(coef)
    U, dU, mn = smooth_grid(f, 32)
    w = w3_from_fields(U, dU)
    worst = max(worst, abs(w))
    print(f'random smooth T^3 -> S^5 map {t}: min|v| on grid {mn:.2e}, W3 = {w.real:+.2e}{w.imag:+.1e}i')
ck.check(f'[numerical] 6 random smooth maps T^3 -> S^5 -> U(4): |W3| <= {worst:.1e} (pointwise-zero integrand)', worst < 1e-10)

# embed the W3 = -1 control V_2 as x = (f, 0, 0, g): block structure V (+) V^dag
def emb(K1, K2, K3):
    V, dV = wilson_weyl_map(2.0)(K1, K2, K3)
    f = np.real(V[..., 0, 0] + V[..., 1, 1]) / 2
    g = [np.real(np.trace(V @ PAULI[a + 1], axis1=-2, axis2=-1) / 2j) for a in range(3)]
    df = [np.real(d[..., 0, 0] + d[..., 1, 1]) / 2 for d in dV]
    dg = [[np.real(np.trace(dV[b] @ PAULI[a + 1], axis1=-2, axis2=-1) / 2j) for b in range(3)] for a in range(3)]
    U = f[..., None, None] * np.eye(4) + 1j * sum(g[a][..., None, None] * Gn[2 + a] for a in range(3))
    dU = [df[b][..., None, None] * np.eye(4) + 1j * sum(dg[a][b][..., None, None] * Gn[2 + a] for a in range(3)) for b in range(3)]
    return U, dU
w_emb = w3_from_fields(*smooth_grid(emb, 64))
w_blk = w3_from_fields(*smooth_grid(wilson_weyl_map(2.0), 64))
ck.check(f'[numerical] the W3=-1 one-qubit control embedded in the Clifford family gives W3 = {w_emb.real:+.1e} '
         f'(blocks V and V^dag carry {w_blk.real:+.3f} and its negative)', abs(w_emb) < 1e-10 and abs(w_blk + 1) < 1e-8)

# ---------------- the explicit finite-range O-covariant member b* of the two-qubit note ----------------
b0, b2 = 11 / 30, 3 / 20
def Gram(b0, b1, b2):
    return np.array([
        [1 - 3 * b0 ** 2, -2 * b0 * b1, b1 ** 2 - b0 ** 2 - b0 * b2, -3 * b1 * (b0 - b2)],
        [-2 * b0 * b1, b0 ** 2 - 2 * b1 ** 2, b1 * (b0 - b2), b0 * b2 - b1 ** 2 + b2 ** 2],
        [b1 ** 2 - b0 ** 2 - b0 * b2, b1 * (b0 - b2), 2 * b1 ** 2 - b2 ** 2, 2 * b1 * b2],
        [-3 * b1 * (b0 - b2), b0 * b2 - b1 ** 2 + b2 ** 2, 2 * b1 * b2, 3 * b2 ** 2]])
u = sp.Symbol('u')
quart = 259200000000 * u ** 4 - 453744000000 * u ** 3 + 12644840000 * u ** 2 + 1185396800 * u - 39225499
roots = sorted(float(r) for r in sp.Poly(quart, u).nroots(n=30) if abs(sp.im(r)) < 1e-20 and sp.re(r) > 0)
b1 = np.sqrt(roots[0])
Gm = Gram(b0, b1, b2)
ev, EV = np.linalg.eigh(Gm)
print(f'b* = ({b0}, {b1:.10f}, {b2}); Gram eigenvalues {ev}')
ck.check('[numerical] G(b*) is PSD of rank 3 (smallest eigenvalue ~ 0)', abs(ev[0]) < 1e-10 and ev[1] > 1e-3)
F = (EV[:, 1:] * np.sqrt(ev[1:])).T     # 3 x 4: rows = coefficients of (f, h1, h2) on phi = (1, sum c, sum cc, ccc)
# build Laurent dict: phi functions and v0, v1, v2 vectors in exponentials
def cosmono(idx):  # product of cos k_a over a in idx -> dict n -> coeff
    out = {(0, 0, 0): 1.0}
    for a in idx:
        new = {}
        for n, cf in out.items():
            for s in (1, -1):
                m = list(n); m[a] += s
                new[tuple(m)] = new.get(tuple(m), 0) + cf / 2
        out = new
    return out
def sin_times_cos(a, idx):
    out = {}
    for n, cf in cosmono(idx).items():
        for s in (1, -1):
            m = list(n); m[a] += s
            out[tuple(m)] = out.get(tuple(m), 0) + cf * s / 2j
    return out
phi = [cosmono([]), {}, {}, cosmono([0, 1, 2])]
for a in range(3):
    for n, cf in cosmono([a]).items():
        phi[1][n] = phi[1].get(n, 0) + cf
for a, bb in itertools.combinations(range(3), 2):
    for n, cf in cosmono([a, bb]).items():
        phi[2][n] = phi[2].get(n, 0) + cf
F0 = F @ np.array([1, 3, 3, 1])
Q = np.linalg.qr(np.column_stack([F0, np.eye(3)[:, :2]]))[0]
if Q[:, 0] @ F0 < 0:
    Q[:, 0] *= -1
F = Q.T @ F
A = {}
def add(dct, M):
    for n, cf in dct.items():
        A[n] = A.get(n, 0) + cf * M
for r, Mat in enumerate([np.eye(4), 1j * Gn[0], 1j * Gn[1]]):
    for i in range(4):
        add(phi[i], F[r, i] * Mat)
for a in range(3):
    others = [c for c in range(3) if c != a]
    add(sin_times_cos(a, []), b0 * 1j * Gn[2 + a])
    for c in others:
        add(sin_times_cos(a, [c]), b1 * 1j * Gn[2 + a])
    add(sin_times_cos(a, others), b2 * 1j * Gn[2 + a])
A = {n: np.asarray(M, complex) for n, M in A.items() if np.abs(M).max() > 1e-15}
Ug, dUg = lp_eval_grid(A, 8)
uerr = np.abs(Ug @ np.conj(np.swapaxes(Ug, -1, -2)) - np.eye(4)).max()
ck.check(f'[numerical] reconstructed b* walk (range 1, {len(A)} hop matrices) is unitary on the grid (err {uerr:.1e})', uerr < 1e-12)
for N in (8, 13):
    Ug, dUg = lp_eval_grid(A, N)
    w = w3_from_fields(Ug, dUg)
    ck.check(f'b* O-covariant Clifford walk: exact-grid W3 (N={N} >= 6r+1 = 7) = {w.real:+.1e}{w.imag:+.1e}i, rounds to 0', abs(w) < 1e-10)
sys.exit(ck.total())
