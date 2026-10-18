"""B4b: Ward identity and leading symbol of the 2026-06-08 staggered Kahler-Dirac induced-graviton kernel.

Kernel (reconstructed, see stag_kernel.py): bubble-only, Pi(K)-Pi(0), conserved velocity x momentum
vertex with mom = sin(Pbar) ('D' variant: dispersion + operator-telescope runners), m = 0.7.

Tests
  R   reproduction of runner-cache constants (dispersion runner N=6 C=0.08961606; isotropy runner A=0.975)
  S   symbol extraction: M2(k) = lim Pi(k)-Pi(0) at O(k^2) (Richardson, N=14 quadrature, N=12 cross-check)
  B   B4 covariance of the extracted symbol (projection residual on the B4-invariant tensor basis)
  G   B4 + gauge invariance: dimension of the gauge-invariant B4 symbol space (is linearised EH unique?)
  W   Ward identity of the symbol: k_mu M2_{mu nu, rho sig}(k) = 0 ?
  WK  finite-K lattice Ward residual sum_mu 2 sin(K_mu/2) [Pi(K)-Pi(0)] scaling power
  D   symbol decomposition into B4 invariants (Lorentz / B4-extra; EH / non-EH)
  T   Euclidean 4D TT spectrum, Lorentzian TT speeds along [100],[110],[111], E/T2 split
  L   longitudinal/gauge stiffness and full 10x10 Lorentzian mode spectrum
  M   zero-momentum Pi(0) structure (mass-like term the runners subtract)
"""
import sys
import os
import itertools
import numpy as np
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stag_kernel import (Pi_tensor, grid, b4_basis, symmetrize6, EH_T6, symbol_from_T6, quad, tadpole)

M = 0.7
NQ = int(os.environ.get('B4B_NQ', '14'))
VAR = 'D'
results = []


def check(name, ok, detail=''):
    results.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ('  [' + detail + ']' if detail else ''), flush=True)


def _job(args):
    K, N, var = args
    return Pi_tensor(np.array(K, float), N, M, var).real


def eval_many(Ks, N, var=VAR):
    with Pool(4) as pool:
        return pool.map(_job, [(tuple(K), N, var) for K in Ks])


# ---------------------------------------------------------------------------
# R: reproduction
# ---------------------------------------------------------------------------
print('== R: reproduction of runner-cache constants')
k6 = 2 * np.pi / 6
P0_6, Pt_6, Px_6 = eval_many([[0, 0, 0, 0], [k6, 0, 0, 0], [0, k6, 0, 0]], 6)
C_t = 4 * (Pt_6[2, 3, 2, 3] - P0_6[2, 3, 2, 3]) / k6 ** 2
C_x = 4 * (Px_6[2, 3, 2, 3] - P0_6[2, 3, 2, 3]) / k6 ** 2
check('R1 dispersion-runner C_time(N=6)=0.08961606 reproduced', abs(C_t - 0.08961606) < 1e-7 and abs(C_x - C_t) < 1e-10,
      'C_t=%.8f C_x=%.8f' % (C_t, C_x))
P0s, PKs = eval_many([[0, 0, 0, 0], [0, k6, 0, 0]], 6, 'S')
d = (PKs - P0s) / (2 - 2 * np.cos(k6))
A6 = 2 * d[2, 3, 2, 3] / (d[2, 2, 2, 2] - d[2, 2, 3, 3])
check('R2 isotropy-runner Zener A(N=6, sin(Pbar/2) vertex)=0.975 reproduced', abs(A6 - 0.975) < 6e-4, 'A=%.5f' % A6)

# ---------------------------------------------------------------------------
# S: symbol extraction
# ---------------------------------------------------------------------------
print('== S: leading symbol extraction (N=%d)' % NQ)
dirs = [tuple(np.eye(4)[a]) for a in range(4)] + [tuple(np.eye(4)[a] + np.eye(4)[b]) for a, b in itertools.combinations(range(4), 2)]
eps = (0.05, 0.1)


def symbol_T6(N):
    Ks = [np.zeros(4)]
    for u in dirs:
        for e in eps:
            Ks.append(e * np.array(u))
    Ks.append(-0.1 * np.array(dirs[-1]))  # parity check
    vals = eval_many(Ks, N)
    P0 = vals[0]
    M2 = {}
    i = 1
    for u in dirs:
        D1 = (vals[i] - P0) / eps[0] ** 2
        D2 = (vals[i + 1] - P0) / eps[1] ** 2
        M2[u] = (4 * D1 - D2) / 3.0
        i += 2
    odd = np.abs(vals[-1] - vals[-2]).max()
    T6 = np.zeros((4,) * 6)
    E = np.eye(4)
    for a in range(4):
        T6[..., a, a] = M2[tuple(E[a])]
    for a, b in itertools.combinations(range(4), 2):
        off = 0.5 * (M2[tuple(E[a] + E[b])] - M2[tuple(E[a])] - M2[tuple(E[b])])
        T6[..., a, b] = off
        T6[..., b, a] = off
    return T6, P0, odd


T6, P0, odd = symbol_T6(NQ)
check('S1 kernel even in K (Pi(K)=Pi(-K))', odd < 1e-12, 'max|Pi(K)-Pi(-K)|=%.1e' % odd)
T6b, _, _ = symbol_T6(NQ - 2)
conv = np.abs(T6 - T6b).max() / np.abs(T6).max()
check('S2 symbol quadrature-converged (N=%d vs %d)' % (NQ, NQ - 2), conv < 1e-5, 'rel diff %.1e' % conv)
np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'symbol_T6_D_m0.7.npy'), T6)

# ---------------------------------------------------------------------------
# B: B4 covariance
# ---------------------------------------------------------------------------
print('== B: B4 covariance')
basis, labels, islor = b4_basis()
nL = sum(islor)
Bm = np.array([b.ravel() for b in basis]).T
coef, *_ = np.linalg.lstsq(Bm, T6.ravel(), rcond=None)
resid = np.linalg.norm(Bm @ coef - T6.ravel()) / np.linalg.norm(T6.ravel())
print('   B4 basis size %d (Lorentz %d, B4-extra %d)' % (len(basis), nL, len(basis) - nL))
check('B1 symbol lies in the B4-invariant tensor space', resid < 1e-5, 'projection residual %.1e' % resid)
Tsym = symmetrize6(T6)
check('B2 symbol has the index symmetries (mu nu)(rho sig)(al be) and pair exchange',
      np.abs(Tsym - T6).max() < 1e-9 * np.abs(T6).max() + 1e-12, 'max dev %.1e' % np.abs(Tsym - T6).max())

# ---------------------------------------------------------------------------
# G: gauge-invariant B4 symbols
# ---------------------------------------------------------------------------
print('== G: gauge-invariant B4 symbols')


def ward_tensor(T):
    # sum_mu k_mu T_{mu nu rho sig al be} k_al k_be symmetrised over (mu, al, be)
    W = np.einsum('abcdef->bcdaef', T)  # move mu to position 3: [nu,rho,sig,mu,al,be]
    out = 0
    for p in itertools.permutations([3, 4, 5]):
        out = out + np.transpose(W, [0, 1, 2] + list(p))
    return out / 6.0


Wm = np.array([ward_tensor(b).ravel() for b in basis]).T
sv = np.linalg.svd(Wm, compute_uv=False)
null_dim = int(np.sum(sv < 1e-10 * sv.max()))
_, _, Vh = np.linalg.svd(Wm)
null = Vh[len(basis) - null_dim:].T if null_dim else np.zeros((len(basis), 0))
EH = EH_T6()
cEH, *_ = np.linalg.lstsq(Bm, EH.ravel(), rcond=None)
eh_ward = np.abs(ward_tensor(EH)).max()
check('G1 linearised EH symbol is B4-invariant and exactly gauge invariant',
      np.linalg.norm(Bm @ cEH - EH.ravel()) < 1e-10 and eh_ward < 1e-12, 'ward=%.1e' % eh_ward)
check('G2 gauge-invariant B4 two-derivative symbols form a 1-dim space (EH unique under B4)', null_dim == 1,
      'dim=%d; smallest sv %s' % (null_dim, ', '.join('%.1e' % x for x in sorted(sv)[:3])))

# ---------------------------------------------------------------------------
# W: Ward identity of the symbol
# ---------------------------------------------------------------------------
print('== W: Ward identity of the extracted symbol')
rng = np.random.default_rng(7)
rat = []
for _ in range(20):
    k = rng.normal(size=4)
    k /= np.linalg.norm(k)
    M2k = symbol_from_T6(T6, k)
    L = np.einsum('m,mnrs->nrs', k, M2k)
    rat.append(np.abs(L).max() / np.abs(M2k).max())
ward_rel = max(rat)
ward_t = np.abs(ward_tensor(T6)).max() / np.abs(T6).max()
check('W1 leading-symbol Ward identity k_mu M2_{mu nu,rho sig}(k)=0 HOLDS', ward_rel < 1e-4,
      'max|k.M2|/max|M2| = %.3e (min over k %.3e); coefficient-level %.3e' % (ward_rel, min(rat), ward_t))
check('W2 leading-symbol Ward identity is BROKEN at O(1) relative size (>1e-2)', ward_rel > 1e-2,
      'max|k.M2|/max|M2| = %.3f' % ward_rel)

# ---------------------------------------------------------------------------
# D: decomposition
# ---------------------------------------------------------------------------
print('== D: symbol decomposition into B4 invariants')
for c, lab, lo in zip(coef, labels, islor):
    print('   %-8s %-40s %+.6e' % ('Lorentz' if lo else 'B4xtra', lab, c))
# EH component: least-squares fit of T6 = a EH + rest, with rest orthogonal to EH in coefficient-free Frobenius sense
a_EH = np.vdot(EH.ravel(), T6.ravel()) / np.vdot(EH.ravel(), EH.ravel())
rest = T6 - a_EH * EH
frac_nonEH = np.linalg.norm(rest) / np.linalg.norm(T6)
frac_xtra = np.linalg.norm(Bm[:, nL:] @ coef[nL:]) / np.linalg.norm(T6)
print('   EH-projection coefficient a_EH=%.6f; non-EH Frobenius fraction %.3f; B4-extra fraction %.3f'
      % (a_EH, frac_nonEH, frac_xtra))
check('D1 symbol is NOT linearised EH (non-EH Frobenius fraction > 0.1)', frac_nonEH > 0.1, 'frac=%.3f' % frac_nonEH)
check('D2 symbol carries non-Lorentz B4-extra invariants (fraction > 1e-3)', frac_xtra > 1e-3, 'frac=%.4f' % frac_xtra)

# ---------------------------------------------------------------------------
# T: TT spectrum and speeds
# ---------------------------------------------------------------------------
print('== T: TT spectrum / speeds')


def sym_basis():
    B = []
    for a in range(4):
        for b in range(a, 4):
            h = np.zeros((4, 4))
            if a == b:
                h[a, a] = 1.0
            else:
                h[a, b] = h[b, a] = 1 / np.sqrt(2)
            B.append(h)
    return B


SB = sym_basis()


def mat10(T4):
    return np.array([[quad(T4, x, y).real for y in SB] for x in SB])


def tt4_basis(k):
    """orthonormal 5-dim basis of symmetric traceless h with h.k = 0 (4D TT)."""
    k = k / np.linalg.norm(k)
    Pt = np.eye(4) - np.outer(k, k)
    vecs = []
    for h in SB:
        x = Pt @ h @ Pt
        x = x - np.trace(x) / 3.0 * Pt
        vecs.append(x.ravel())
    U, S, _ = np.linalg.svd(np.array(vecs).T)
    return [U[:, i].reshape(4, 4) for i in range(5)]


def spectrum_TT(k):
    Bt = tt4_basis(k)
    M2k = symbol_from_T6(T6, k)
    Q = np.array([[quad(M2k, x, y).real for y in Bt] for x in Bt])
    return np.sort(np.linalg.eigvalsh(Q))


for name, k in [('[1000] time', [1, 0, 0, 0]), ('[0100] x', [0, 1, 0, 0]), ('[1100] t-x', [1, 1, 0, 0]),
                ('[0110] x-y', [0, 1, 1, 0]), ('[0111]', [0, 1, 1, 1]), ('[1111]', [1, 1, 1, 1])]:
    k = np.array(k, float)
    k /= np.linalg.norm(k)
    print('   4D-TT eigenvalues of M2 at unit k=%-12s: %s' % (name, ', '.join('%.6f' % x for x in spectrum_TT(k))))
ax = spectrum_TT(np.array([0, 1, 0, 0.]))
EoverT = None
# E-type (diag traceless in transverse 3-space) vs T2-type (off-diagonal) along x
k = np.array([0, 1, 0, 0.])
M2x = symbol_from_T6(T6, k)
hT = np.zeros((4, 4)); hT[2, 3] = hT[3, 2] = 1 / np.sqrt(2)
hE = np.diag([0, 0, 1, -1.]) / np.sqrt(2)
cT = quad(M2x, hT).real
cE = quad(M2x, hE).real
print('   along x: C_T2(yz)=%.6f  C_E(yy-zz)=%.6f  E/T2=%.6f' % (cT, cE, cE / cT))
check('T1 4D-TT spectrum is NOT degenerate at fixed k (E/T2 split along an axis)', abs(cE / cT - 1) > 1e-3,
      'E/T2=%.5f' % (cE / cT))


def lorentz_speeds_TT(n):
    """spatial direction n (3-vector in x,y,z); TT pols spatial, transverse to n. c^2 = B/A pencil."""
    n = np.array(n, float)
    n /= np.linalg.norm(n)
    kt = np.array([1, 0, 0, 0.])
    ks = np.concatenate([[0], n])
    Pn = np.eye(3) - np.outer(n, n)
    pols = []
    for h in [np.diag([1, 0, 0.]), np.diag([0, 1, 0.]), np.diag([0, 0, 1.])] + \
             [(np.outer(np.eye(3)[a], np.eye(3)[b]) + np.outer(np.eye(3)[b], np.eye(3)[a])) / np.sqrt(2)
              for a, b in [(0, 1), (0, 2), (1, 2)]]:
        x = Pn @ h @ Pn
        x = x - np.trace(x) / 2.0 * Pn
        pols.append(x.ravel())
    U, S, _ = np.linalg.svd(np.array(pols).T)
    tt = []
    for i in range(2):
        h4 = np.zeros((4, 4))
        h4[1:, 1:] = U[:, i].reshape(3, 3)
        tt.append(h4)
    A = np.array([[quad(symbol_from_T6(T6, kt), x, y).real for y in tt] for x in tt])
    B = np.array([[quad(symbol_from_T6(T6, ks), x, y).real for y in tt] for x in tt])
    Cmix = np.array([[quad(np.einsum('abcdef,e,f->abcd', T6, kt, ks) + np.einsum('abcdef,e,f->abcd', T6, ks, kt), x, y).real
                      for y in tt] for x in tt])
    w = np.linalg.eigvals(np.linalg.solve(A, B))
    return np.sort(w.real), np.abs(Cmix).max(), A, B


spd = {}
for name, n in [('[100]', [1, 0, 0]), ('[110]', [1, 1, 0]), ('[111]', [1, 1, 1])]:
    c2, mix, A, B = lorentz_speeds_TT(n)
    spd[name] = c2
    print('   TT-restricted Lorentzian c^2 along %s: %s  (t-x mixing %.1e; A eig %s)'
          % (name, ', '.join('%.6f' % x for x in c2), mix, ', '.join('%.5f' % x for x in np.linalg.eigvalsh(A))))
check('T2 TT speeds along [100] equal 1 for both pols (forced by t<->x B4 swap)', np.allclose(spd['[100]'], 1, atol=1e-6),
      str(spd['[100]']))
split = max(abs(spd[k][1] - spd[k][0]) for k in spd)
dev = max(abs(spd[k] - 1).max() for k in spd)
check('T3 no leading-order TT birefringence within the TT-restricted pencil (split<1e-4)', split < 1e-4,
      'max split %.2e, max |c^2-1| %.2e' % (split, dev))

# ---------------------------------------------------------------------------
# L: gauge / longitudinal modes
# ---------------------------------------------------------------------------
print('== L: gauge/longitudinal modes')
k = np.array([0, 1, 0, 0.])
M2x = symbol_from_T6(T6, k)
gauge_vals = []
for xi in np.eye(4):
    h = np.outer(k, xi) + np.outer(xi, k)
    h /= np.linalg.norm(h)
    gauge_vals.append(quad(M2x, h).real)
print('   along x, unit-norm gauge modes k(x)xi, xi=e0..e3: %s;  TT(yz)=%.6f' % (', '.join('%.6f' % g for g in gauge_vals), cT))
gr = max(abs(g) for g in gauge_vals) / cT
check('L1 pure-gauge modes carry O(1) k^2 stiffness relative to TT (|gauge|/TT > 0.1)', gr > 0.1, 'ratio %.3f' % gr)
# full 10x10 pencil along spatial [100]: B v = c^2 A v with A=M2(e_t), B=M2(e_x)
A10 = mat10(symbol_from_T6(T6, np.array([1, 0, 0, 0.])))
B10 = mat10(symbol_from_T6(T6, np.array([0, 1, 0, 0.])))
print('   eig A10 (time-direction symbol, 10x10):', ', '.join('%.5f' % x for x in np.linalg.eigvalsh(A10)))
import scipy.linalg as sla
w = sla.eigvals(B10, A10)
print('   full 10x10 Lorentzian c^2 along [100]:', ', '.join('%.5f%+.1ei' % (x.real, x.imag) for x in sorted(w, key=lambda z: z.real)))
negA = int(np.sum(np.linalg.eigvalsh(A10) < -1e-9))
check('L2 time-direction symbol A10 is not positive semidefinite (non-TT ghost-sign directions present)', negA > 0,
      '%d negative eigenvalues' % negA)

# ---------------------------------------------------------------------------
# WK: finite-K lattice Ward residual
# ---------------------------------------------------------------------------
print('== WK: finite-K lattice Ward residual scaling')
u = np.array([0.3, 1.0, -0.5, 0.7])
u /= np.linalg.norm(u)
ks = [0.4, 0.2, 0.1]
vals = eval_many([np.zeros(4)] + [kk * u for kk in ks], NQ)
P0n = vals[0]
Lsub, Lfull = [], []
for kk, Pk in zip(ks, vals[1:]):
    ph = 2 * np.sin(kk * u / 2)
    Lsub.append(np.abs(np.einsum('m,mnrs->nrs', ph, Pk - P0n)).max())
    Lfull.append(np.abs(np.einsum('m,mnrs->nrs', ph, Pk)).max())
psub = np.log(Lsub[1] / Lsub[2]) / np.log(2)
pfull = np.log(Lfull[1] / Lfull[2]) / np.log(2)
print('   |p.(Pi(K)-Pi(0))| = %s ; |p.Pi(K)| = %s' % (', '.join('%.3e' % x for x in Lsub), ', '.join('%.3e' % x for x in Lfull)))
check('WK1 subtracted-kernel lattice Ward residual scales as k^3 (leading symbol violation)', abs(psub - 3) < 0.15,
      'power %.3f' % psub)
check('WK2 unsubtracted kernel Ward residual scales as k^1 (Pi(0) contact/mass term)', abs(pfull - 1) < 0.15, 'power %.3f' % pfull)

# ---------------------------------------------------------------------------
# M: zero-momentum structure
# ---------------------------------------------------------------------------
print('== M: zero-momentum kernel Pi(0)')
d4 = np.eye(4)
I1 = np.einsum('ab,cd->abcd', d4, d4)
I2 = np.einsum('ac,bd->abcd', d4, d4) + np.einsum('ad,bc->abcd', d4, d4)
I3 = np.zeros((4,) * 4)
for a in range(4):
    I3[a, a, a, a] = 1
Bz = np.array([I1.ravel(), I2.ravel(), I3.ravel()]).T
cz, *_ = np.linalg.lstsq(Bz, P0n.ravel(), rcond=None)
rz = np.linalg.norm(Bz @ cz - P0n.ravel()) / np.linalg.norm(P0n)
print('   Pi(0) = %.6f d_mn d_rs + %.6f (d_mr d_ns + d_ms d_nr) + %.6f d_mnrs   (resid %.1e)' % (cz[0], cz[1], cz[2], rz))
tp = tadpole(NQ, M, VAR).real
print('   one-point <V_mn> diag = %s (offdiag max %.1e)' % (', '.join('%.6f' % tp[i, i] for i in range(4)),
                                                          np.abs(tp - np.diag(np.diag(tp))).max()))
mT = quad(P0n, hT).real
mE = quad(P0n, hE).real
print('   Pi(0) on TT pols: T2(yz)=%.6f, E(yy-zz)=%.6f ; ratio to symbol C_T2: m_T2^2=%.4f, m_E^2=%.4f (lattice units, block spacing)'
      % (mT, mE, mT / cT, mE / cE))
check('M1 Pi(0) is B4-invariant with a nonzero non-Lorentz d_mnrs piece', rz < 1e-8 and abs(cz[2]) > 1e-4 * np.abs(cz).max(),
      'c3/c2=%.3f' % (cz[2] / cz[1] if cz[1] else np.inf))

n_pass = sum(ok for _, ok in results)
n_fail = len(results) - n_pass
print('TOTAL: PASS=%d FAIL=%d' % (n_pass, n_fail))
