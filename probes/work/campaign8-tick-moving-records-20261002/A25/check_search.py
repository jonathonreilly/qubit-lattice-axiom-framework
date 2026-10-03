"""A25 check 4: small search over a 9-parameter family of O-covariant, local, collocated, lattice-modified
gauge generators (correct linearized-diffeomorphism infrared limit) for one that passes the NECESSARY
no-doubler condition dim S_K <= 4 at all three zone-corner classes.  Plus an r-scan of the Wilson lift.
Building blocks (c2(x) = (1+cos x)/2; {i,j,m} distinct):
  diag  (D xi)_jj  = 2i sin k_j [1 + a1 (c2_l c2_m - 1) + a2 ((c2_l + c2_m)/2 - 1)] xi_j
  sym   (D xi)_ij += i sin k_i [1 + b1 (c2_j - 1) + b2 (c2_m - 1) + b3 (c2_j c2_m - 1) + b4 (c2_i - 1)] xi_j  (+ i<->j)
  chiral(D xi)_ij += (cos k_i - cos k_j) [l1 + l2 c2_m + l3 (c2_i + c2_j)/2] xi_m   (cyclic orientation)
Finite family; a negative result here is CHECKED for this family only.  Supplied toy."""
import time, itertools
import numpy as np
import scipy.optimize as so
import scipy.sparse as sp
from stag2 import *

t0 = time.time()
rng = np.random.default_rng(5)
O = signed_perms(proper=True)
c2 = lambda x: (1 + np.cos(x)) / 2
CYC = {(0, 1): 2, (1, 2): 0, (0, 2): 1}
ORI = {(0, 1): (0, 1), (1, 2): (1, 2), (0, 2): (2, 0)}    # (i,j) order in (cos k_i - cos k_j) following 01->12->20


def rho_sym(Rm):
    P, sg = perm_sign(Rm)
    M = np.zeros((6, 6))
    for a, (i, j) in enumerate(H_PAIR):
        M[hidx(P[i], P[j]), a] = sg[i] * sg[j]
    return M


def gen(th):
    a1, a2, b1, b2, b3, b4, l1, l2, l3 = th

    def D(k):
        M = np.zeros((6, 3), complex)
        for j in range(3):
            l, m = [x for x in range(3) if x != j]
            M[hidx(j, j), j] = 2j * np.sin(k[j]) * ((1 - a1 - a2) + a1 * c2(k[l]) * c2(k[m]) + a2 * (c2(k[l]) + c2(k[m])) / 2)
        for (i, j) in ((0, 1), (0, 2), (1, 2)):
            m = 3 - i - j
            f = lambda i_, j_: (1 - b1 - b2 - b3 - b4) + b1 * c2(k[j_]) + b2 * c2(k[m]) + b3 * c2(k[j_]) * c2(k[m]) + b4 * c2(k[i_])
            M[hidx(i, j), j] += 1j * np.sin(k[i]) * f(i, j)
            M[hidx(i, j), i] += 1j * np.sin(k[j]) * f(j, i)
            p, q = ORI[(i, j)]
            M[hidx(i, j), m] += (np.cos(k[p]) - np.cos(k[q])) * (l1 + l2 * c2(k[m]) + l3 * (c2(k[i]) + c2(k[j])) / 2)
        return M
    return D


def cov_err(D):
    e = 0.0
    for _ in range(3):
        k = rng.uniform(-np.pi, np.pi, 3)
        for g in O:
            e = max(e, np.abs(D(g @ k) - rho_sym(g) @ D(k) @ g.T).max())
    return e


DIRS = [d / np.linalg.norm(d) for d in list(np.random.default_rng(1).normal(size=(60, 3))) +
        [np.array(v, float) for v in itertools.product((-1, 0, 1), repeat=3) if any(v)]]
CORN = [np.pi * np.array(v, float) for v in ((1, 0, 0), (1, 1, 0), (1, 1, 1))]


def span_sv(D, K, eps=1e-3):
    bases = []
    for q in DIRS:
        u, s, vh = np.linalg.svd(D(K + eps * q))
        r = int(np.sum(s > 1e-9 * max(s[0], 1e-300)))
        bases.append(u[:, :r])
    sv = np.linalg.svd(np.hstack(bases), compute_uv=False)
    return sv / sv[0]


def objective(th):
    D = gen(th)
    return max(span_sv(D, K)[4] for K in CORN)


if __name__ == "__main__":
    # sanity: central = all zeros
    print(f'central member (all parameters 0): covariance err {cov_err(gen(np.zeros(9))):.0e}; s5 per corner {[round(span_sv(gen(np.zeros(9)), K)[4], 3) for K in CORN]}')
    th_r = rng.uniform(-2, 2, 9)
    print(f'random member: covariance err under O {cov_err(gen(th_r)):.0e}')
    # random sampling
    samples = rng.uniform(-2, 2, size=(500, 9))
    vals = np.array([objective(t) for t in samples])
    order = np.argsort(vals)
    print(f'500 random members: best max_K s5 = {vals[order[0]]:.3f}, median {np.median(vals):.3f}')
    best = []
    for idx in order[:4]:
        r = so.minimize(objective, samples[idx], method='Nelder-Mead', options={'maxfev': 600, 'xatol': 1e-4, 'fatol': 1e-6})
        best.append((r.fun, r.x))
    best.sort(key=lambda t: t[0])
    fb, xb = best[0]
    dims = []
    for K in CORN:
        sv = span_sv(gen(xb), K)
        dims.append(int(np.sum(sv > 0.1)))
    print(f'after Nelder-Mead from the 4 best: best max_K s5 = {fb:.3f} at theta = {np.round(xb, 3)}; dim S_K at (pi,0,0),(pi,pi,0),(pi,pi,pi) = {dims}')
    per_corner = [round(span_sv(gen(xb), K)[4], 3) for K in CORN]
    print(f'   per-corner s5 at the optimum: {per_corner}  (all must be ~0 to pass)')
    # which corner is the bottleneck across the 4 optima
    for fval, x in best:
        print(f'   optimum {fval:.3f}: per-corner s5 {[round(span_sv(gen(x), K)[4], 3) for K in CORN]}')

    # ---------------------------------------------------------------- Wilson r-scan (collocated central)
    N = 4
    opc = build(N, 'central'); latc = opc['lat']
    Lap = [latc.Sp[a] - 2 * latc.I + latc.Sm[a] for a in range(3)]
    W1 = sum(Lp.T @ Lp for Lp in Lap)
    ks = kgrid(N)
    Z12 = H_OFF + H_OFF
    for r in (0.01, 0.05, 0.25):
        for nm, Wm in (('full', sp.kron(sp.diags([1, 1, 1, 2, 2, 2]), W1, format='csr')),):
            op = dict(opc); op['Vp'] = (opc['Vp'] + r * Wm).tocsr()
            A, B, C = layers_hp(op, 0.5)
            Uk = bloch(latc, (C @ B @ A).tocsr(), Z12, Z12, ks, mode='central')
            mm = max(np.abs(np.linalg.eigvals(Uk[i])).max() for i in range(len(ks)))
            print(f'Wilson lift r={r}: max |eig| over the N={N} zone = {mm:.4f}')
    print(f'done in {time.time() - t0:.1f}s')
