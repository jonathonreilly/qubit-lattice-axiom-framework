#!/usr/bin/env python3
"""euclidean-b4: can the update be the transfer matrix of a 4D hypercubic (B4) Euclidean lattice action?

Supplied models (finite diagnostics unless marked THEOREM; no physical identification is established):
 A  exact group theory: dimension-4 invariant counts under the spatial cubic group, B4+ and B4; all two-generated
    subgroups of B4+; the spinor (taste) content of one-mode-per-site fields with spin-taste locking.
 B  the free Wilson r = 1 fermion on Z^3 x Z_tau with a_tau = a: its transfer recursion R(p), positivity, the real-time
    Hamiltonian H = -ln T / a, its locality (branch point), the Lieb-Robinson front, T as an odds step (Fock toy).
 C  one loop with Euclidean dressing: Wilson fermion + plaquette photon (Feynman gauge) on an anisotropic lattice
    xi = a_s/a_t (xi = 1 is B4); fermion speed from Z_s/Z_t, photon speed from the fermion loop; engine validation.
 D  chirality: 4D Neuberger overlap (GW, species, locality in time, index with electric flux), free two-point
    transfer-positivity tests (Wilson, naive, overlap, Shamir domain-wall), the DWF slice form and residual mass,
    a 2D anomaly-free 3-4-5 check.
 E  estimates against measured bounds (supplied numbers).
Cited, not rederived: Nielsen-Ninomiya, Luscher's anomaly-free U(1) construction, Osterwalder-Seiler / Luscher RP."""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 120
import itertools, os, sys, time, signal
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
np.seterr(all='ignore')
T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0, -1.0]).astype(complex)]
Z2 = np.zeros((2, 2)); I4 = np.eye(4)
GAM = [np.block([[Z2, -1j * S], [1j * S, Z2]]) for S in SIG] + [np.diag([1, 1, -1, -1]).astype(complex)]  # x,y,z,t
G4 = GAM[3]; G5 = GAM[0] @ GAM[1] @ GAM[2] @ GAM[3]

# ================================================================== A. symmetry
print('== A. symmetry (exact)')
allR = []
for perm in itertools.permutations(range(4)):
    for sg in itertools.product((1, -1), repeat=4):
        R = np.zeros((4, 4))
        for i in range(4): R[i, perm[i]] = sg[i]
        allR.append(R)
def inv_counts(G):
    ch = np.array([np.trace(R) for R in G]); ch2 = np.array([np.trace(R @ R) for R in G]); ch4 = np.array([np.trace(np.linalg.matrix_power(R, 4)) for R in G])
    cL = (ch ** 2 - ch2) / 2; cL2 = (ch2 ** 2 - ch4) / 2
    return [int(round(np.mean(x))) for x in ((ch ** 2 + ch2) / 2, (ch ** 2 - ch2) / 2, (cL ** 2 + cL2) / 2)]
Bp = [R for R in allR if np.linalg.det(R) > 0]; Osp = [R for R in Bp if R[3, 3] == 1]
cO, cBp, cB = inv_counts(Osp), inv_counts(Bp), inv_counts(allR)
def lift(R):
    A = np.vstack([np.kron(np.eye(4), GAM[r].T) - np.kron(sum(R[s, r] * GAM[s] for s in range(4)), np.eye(4)) for r in range(4)])
    _, sv, Vh = np.linalg.svd(A); S = Vh[-1].conj().reshape(4, 4)
    return S / np.sqrt(np.trace(S.conj().T @ S).real / 4), sv[-2] > 1e-6 and sv[-1] < 1e-10
lifts = [lift(R) for R in Bp]; SP = [x[0] for x in lifts]
lift_ok = all(x[1] for x in lifts) and all(np.allclose(S @ GAM[r] @ np.linalg.inv(S), sum(R[s, r] * GAM[s] for s in range(4))) for R, S in zip(Bp, SP) for r in range(4))
qt = [i for i, R in enumerate(Bp) if R[3, 0] == 1 and R[0, 3] == -1 and R[1, 1] == 1 and R[2, 2] == 1][0]   # t-x quarter turn
cks = [np.array([1.0, 1, 1, c]) for c in (1.0, 1.2)]
def kin(c, p): return sum(c[m] * p[m] * GAM[m] for m in range(4))
pp = np.array([0.3, -0.2, 0.5, 0.7])
kin_inv = [np.abs(SP[qt] @ kin(c, pp) @ np.linalg.inv(SP[qt]) - kin(c, Bp[qt] @ pp)).max() for c in cks]
check(f'A1 THEOREM dim-4 invariants [n_S, n_A, n_F photon]: spatial O {cO}, B4+ {cBp}, B4 {cB}; the spin lift exists and '
      'the Dirac form is quarter-turn invariant only at c_t = c_s', cO == [2, 0, 3] and cBp == [1, 0, 2]
      and cB == [1, 0, 1] and lift_ok and kin_inv[0] < 1e-12 and kin_inv[1] > 0.1, f'{kin_inv[0]:.0e} vs {kin_inv[1]:.2f} at c_t/c_s = 1.2')
n = len(Bp); key = {tuple(R.astype(int).ravel()): i for i, R in enumerate(Bp)}
mul = np.array([[key[tuple((Bp[i] @ Bp[j]).astype(int).ravel())] for j in range(n)] for i in range(n)])
e0 = key[tuple(np.eye(4, dtype=int).ravel())]; inv = [int(np.where(mul[i] == e0)[0][0]) for i in range(n)]
def closure(gens):
    S = {e0}; fr = [e0]
    while fr:
        new = []
        for a in fr:
            for g in gens:
                b = int(mul[a, g])
                if b not in S: S.add(b); new.append(b)
        fr = new
    return frozenset(S)
seen = set(); reps = []
for i in range(n):
    if i not in seen: seen |= {int(mul[mul[g, i], inv[g]]) for g in range(n)}; reps.append(i)
subs = {closure([r, g]) for r in reps for g in range(n)}
def k4(M): return tuple(np.round(np.concatenate([M.real.ravel(), M.imag.ravel()]), 6))
def taste1(H):
    """1 if the binary lift of H has a 1-dim spinorial rep, i.e. -1 is not in its commutator subgroup"""
    H = list(H); rg = np.random.default_rng(len(H))
    pr = list(itertools.product(range(len(H)), repeat=2)) if len(H) <= 24 else rg.integers(0, len(H), (40, 2))
    gens = [SP[H[a]] @ SP[H[b]] @ np.linalg.inv(SP[H[a]]) @ np.linalg.inv(SP[H[b]]) for a, b in pr]
    seen = {k4(I4)}; fr = [I4.astype(complex)]
    while fr:
        new = []
        for X in fr:
            for g_ in gens:
                Y = X @ g_; kk = k4(Y)
                if kk not in seen: seen.add(kk); new.append(Y)
        fr = new
    return int(k4(-I4.astype(complex)) not in seen)
res = {H: (inv_counts([Bp[i] for i in H]), taste1(H)) for H in subs}
good = [H for H in subs if res[H][0][0] == 1 and res[H][0][2] == 2]; t1 = [H for H in subs if res[H][1] > 0]
check(f'A2 THEOREM of {len(subs)} two-generated subgroups of B4+ only B4+ fixes one dim-4 form for matter and light, and its '
      'binary lift has -1 in its commutator subgroup (no 1-dim spinorial rep); every subgroup with one allows photon '
      'anisotropy: one mode per 4D site plus a protected cone leaves >= 2 light tastes', len(good) == 1 and len(good[0]) == 192 and res[good[0]][1] == 0 and all(res[H][0][2] >= 3 for H in t1),
      f'{len(t1)} subgroups with one, min n_F {min(res[H][0][2] for H in t1)}')

# ================================================================== B. transfer matrix
print('== B. transfer matrix of the free B4 Wilson r=1 fermion (a_t = a_s = 1)')
def Rmat(P, m):
    s = np.sin(P); B = 4 + m - np.cos(P).sum(-1); s2 = (s ** 2).sum(-1); ss = sum(s[..., j, None, None] * SIG[j] for j in range(3))
    R = np.zeros(P.shape[:-1] + (4, 4), complex)
    R[..., :2, :2] = ((1 + s2) / B)[..., None, None] * np.eye(2); R[..., :2, 2:] = -ss; R[..., 2:, :2] = -ss; R[..., 2:, 2:] = B[..., None, None] * np.eye(2)
    return R, B, ss
def Ewil(P, m):
    s2 = (np.sin(P) ** 2).sum(-1); Ms = m + (1 - np.cos(P)).sum(-1); return np.arccosh(1 + (Ms ** 2 + s2) / (2 * (1 + Ms)))
def Dw(K, mass, r=1.0):          # K[..., 3] = time
    out = (mass + r * (1 - np.cos(K)).sum(-1))[..., None, None] * I4
    for mu in range(4): out = out + 1j * np.sin(K[..., mu])[..., None, None] * GAM[mu]
    return out
rng = np.random.default_rng(20261022); P = rng.uniform(-np.pi, np.pi, (400, 3)); b1 = []
for m in (0.0, 0.3):
    R, B, ss = Rmat(P, m); ev = np.linalg.eigvalsh(R); E = Ewil(P, m)
    L = np.zeros_like(R); L[:, :2, :2] = (B ** -0.5)[:, None, None] * np.eye(2); L[:, :2, 2:] = -(B ** -0.5)[:, None, None] * ss; L[:, 2:, 2:] = (B ** 0.5)[:, None, None] * np.eye(2)
    K = np.c_[P[:60], 1j * E[:60]]
    b1.append(max(np.abs(R - np.conj(np.swapaxes(R, 1, 2))).max(), np.abs(np.linalg.det(R) - 1).max(), np.abs(np.sort(ev, 1)[:, :2] - np.exp(-E)[:, None]).max(),
                  np.abs(R - L @ np.conj(np.swapaxes(L, 1, 2))).max(), np.abs(np.linalg.det(Dw(K, m))).max()))
    b1.append(-ev.min())
check('B1 THEOREM r=1 recursion R = [[(1+s^2)/B, -s.sig],[-s.sig, B]] = L L^dag (adjoint half-steps): Hermitian, det 1, '
      'eigenvalues e^{-+E}, E = 4D pole, positive for m > -1: T >= 0, H = -ln T Hermitian, U = T^{it} unitary with the '
      'Euclidean dispersion', max(b1[0], b1[2]) < 1e-12 and max(b1[1], b1[3]) < 0,
      f'residual {max(b1[0], b1[2]):.0e}; min eig {-b1[1]:.3f}, {-b1[3]:.3f} (m = 0, .3)')
fits = []; g1 = 2 * np.pi * np.arange(256) / 256; Pl = np.stack([g1, 0 * g1, 0 * g1], -1)
for m in (0.0, 0.3):
    w, V = np.linalg.eigh(Rmat(Pl, m)[0]); hl = np.fft.ifft(np.einsum('...ij,...j,...kj->...ik', V, -np.log(w), V.conj()), axis=0)
    nl = np.linalg.norm(hl, ord=2, axis=(-2, -1)); xs = np.arange(6, 26)
    co = np.linalg.lstsq(np.c_[np.ones(len(xs)), -xs, -np.log(xs)], np.log(nl[xs]), rcond=None)[0]
    K3 = 3 + m; fits.append((co[1], np.arccosh((K3 ** 2 + 1) / (2 * K3)), nl[25]))
check('B2 THEOREM H has an inverse-square-root branch point (eigenvalue collision at -1) at cosh eta = ((3+m)^2+1)/(2(3+m)), '
      'eta = ln 3 at m = 0: quasi-local at the massless point, not finite range (the arcsinh(m) rate on main is the staggered '
      'number-operator form)', all(abs(f[0] - f[1]) / f[1] < 0.02 for f in fits) and abs(fits[0][1] - np.log(3)) < 1e-12 and fits[0][2] > 1e-14,
      f'fit {fits[0][0]:.3f} vs {fits[0][1]:.4f}, {fits[1][0]:.3f} vs {fits[1][1]:.4f}; |h(25)| {fits[0][2]:.0e}')
NB = 40; g = 2 * np.pi * np.arange(NB) / NB; PP = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1)
w0, V0 = np.linalg.eigh(Rmat(PP, 0.0)[0]); lw0 = -np.log(w0)
amp = np.fft.ifftn(np.einsum('...ij,...j,...j->...i', V0, np.exp(-1j * lw0 * 10.0), V0[..., 0, :].conj()), axes=(0, 1, 2)); prob = (np.abs(amp) ** 2).sum(-1)
X = np.minimum(np.arange(NB), NB - np.arange(NB)); R2 = np.sqrt(X[:, None, None] ** 2 + X[None, :, None] ** 2 + X[None, None, :] ** 2)
leak = [prob[R2 > 10 + d].sum() / prob.sum() for d in (0, 2, 4, 8)]; del amp, prob
go = 2 * np.pi * (np.arange(40) + 0.5) / 40; P3 = np.stack(np.meshgrid(go, go, go, indexing='ij'), -1)
vmax = [np.sqrt(sum(((Ewil(P3 + 1e-5 * e, m) - Ewil(P3 - 1e-5 * e, m)) / 2e-5) ** 2 for e in np.eye(3))).max() for m in (0.0, 0.3)]
check('B3 FINITE Lieb-Robinson: max group velocity < 1 edge/tick; a point source at t = 10 leaks past |x| = t + d with weight '
      'falling exponentially in d',
      vmax[0] < 1 and all(leak[i + 1] < leak[i] / 5 for i in range(3)) and leak[3] > 0,
      f'v_max {vmax[0]:.3f}, {vmax[1]:.3f}; leak d=0,2,4,8: ' + ' '.join(f'{x:.0e}' for x in leak))
# 1+1D Fock toy: T as an odds step
L1 = 4; ps = 2 * np.pi * np.arange(L1) / L1; m1 = 0.3; hp = []
for p in ps:
    s, Bq = np.sin(p), 2 + m1 - np.cos(p); Rq = np.array([[(1 + s * s) / Bq, -s], [-s, Bq]]); w_, V_ = np.linalg.eigh(Rq); hp.append(-(V_ * np.log(w_)) @ V_.T)
h1 = np.zeros((2 * L1, 2 * L1), complex)
for x in range(L1):
    for y in range(L1): h1[2 * x:2 * x + 2, 2 * y:2 * y + 2] = sum(np.exp(1j * p * (x - y)) * hq for p, hq in zip(ps, hp)) / L1
NM = 2 * L1; DIM = 2 ** NM
def cop(j):
    M_ = np.zeros((DIM, DIM))
    for st in range(DIM):
        if (st >> j) & 1: M_[st ^ (1 << j), st] = (-1) ** bin(st & ((1 << j) - 1)).count('1')
    return M_
cs = [cop(j) for j in range(NM)]; HF = sum(h1[i, j] * cs[i].T @ cs[j] for i in range(NM) for j in range(NM))
EF, VF = np.linalg.eigh((HF + HF.conj().T) / 2); TF = (VF * np.exp(-EF)) @ VF.conj().T; UF = (VF * np.exp(-1j * EF)) @ VF.conj().T
psi = rng.normal(size=DIM) + 1j * rng.normal(size=DIM); psi /= np.linalg.norm(psi); nr = []; fid = []
for k_ in range(30):
    psi = TF @ psi; nr.append(np.linalg.norm(psi)); psi /= nr[-1]; fid.append(1 - abs(VF[:, 0].conj() @ psi) ** 2)
gap = EF[1] - EF[0]
check('B4 THEOREM T as the odds step projects onto the vacuum and rescales the norm, so it cannot carry CL-2; U = T^i is '
      'unitary and commutes with T (1+1D Fock, 8 modes)', fid[9] < 0.1 and fid[29] < 1e-5 and fid[29] < fid[9] and
      np.abs(UF @ UF.conj().T - np.eye(DIM)).max() < 1e-12 and np.abs(UF @ TF - TF @ UF).max() < 1e-12 and abs(nr[-1] - 1) > 0.05,
      f'1-F after 10, 30 steps {fid[9]:.0e}, {fid[29]:.0e}; norm x{nr[-1]:.1f} per step')
print(f'   [{time.time() - T0:.0f} s]')

# ================================================================== C. one loop
print('== C. one loop, Euclidean dressing: Wilson fermion + plaquette photon, Feynman gauge, xi = a_s/a_t, units e^2/16pi^2')
def grids(N, xi, full=None):
    a = np.array([1.0 / xi, 1.0, 1.0, 1.0]); Ns = [int(round(N * xi)), N, N, N]; gs, hs = [], []
    for i, n_ in enumerate(Ns):
        if i == full: h = np.pi / n_; gs.append(-np.pi + h * (np.arange(2 * n_) + 0.5))
        else: h = np.pi / n_; gs.append(h * (np.arange(n_) + 0.5))
        hs.append(h)
    return a, gs, hs
def slices(gs):
    for u4 in gs[0]: yield [np.array([[[u4]]]), gs[1][:, None, None], gs[2][None, :, None], gs[3][None, None, :]]
def zfer(N, xi, m, nu, d=1e-4, r=1.0, scalar=False):
    """dZ_nu (sunset + tadpole) per e^2 at p = 0; scalar=True returns Sigma(0)/e^2 (m = given)"""
    a, gs, hs = grids(N, xi); w = 8 * np.prod([h / (2 * np.pi) for h in hs]) * np.prod(1 / a); tot = IG = sc = 0.0
    for U in slices(gs):
        kh2 = sum(4 / a[i] ** 2 * np.sin(U[i] / 2) ** 2 for i in range(4)); IG += 2 * w * np.sum(1 / kh2)
        if scalar:
            M = m + sum(r * (1 - np.cos(U[i])) / a[i] for i in range(4)); den = M ** 2 + sum(np.sin(U[i]) ** 2 / a[i] ** 2 for i in range(4))
            sc += 2 * w * sum(np.sum((M * (r * r * np.sin(U[i] / 2) ** 2 - np.cos(U[i] / 2) ** 2) + r * np.sin(U[i]) ** 2 / a[i]) / den / kh2) for i in range(4))
            continue
        for sg in (1, -1):
            pu = [0.0] * 4; pu[nu] = sg * d * a[nu]; V = [pu[i] - U[i] for i in range(4)]; Mid = [pu[i] - U[i] / 2 for i in range(4)]
            q = [np.sin(V[i]) / a[i] for i in range(4)]; M = m + sum(r * (1 - np.cos(V[i])) / a[i] for i in range(4)); den = M ** 2 + sum(x ** 2 for x in q)
            f = 0.0
            for mu in range(4):
                C, S = np.cos(Mid[mu]), np.sin(Mid[mu]); f = f - (C * C + r * r * S * S) * q[nu]
                if mu == nu: f = f + 2 * r * M * S * C + 2 * C * C * q[mu]
            tot += sg * (-w) * np.sum(f / den / kh2)
    if scalar: return sum(a[i] * r / 2 for i in range(4)) * IG - sc, IG
    return tot / d - (a[nu] ** 2 / 2) * IG, IG
def pbub(N, xi, m, qv, nu, r=1.0):
    a, gs, hs = grids(N, xi, full=nu); w = 8 * np.prod([h / (2 * np.pi) for h in hs]) * np.prod(1 / a); tot = 0.0
    for U in slices(gs):
        qa = [0.0] * 4; qa[nu] = qv * a[nu]; k1 = [U[i] - qa[i] / 2 for i in range(4)]; k2 = [U[i] + qa[i] / 2 for i in range(4)]
        s1 = [np.sin(k1[i]) / a[i] for i in range(4)]; s2 = [np.sin(k2[i]) / a[i] for i in range(4)]
        M1 = m + sum(r * (1 - np.cos(k1[i])) / a[i] for i in range(4)); M2 = m + sum(r * (1 - np.cos(k2[i])) / a[i] for i in range(4))
        ss = sum(s1[i] * s2[i] for i in range(4)); C, S = np.cos(U[2]), np.sin(U[2])
        tr4 = r * r * S * S * (M1 * M2 - ss) - C * C * (M1 * M2 + ss - 2 * s1[2] * s2[2]) + 2 * r * S * C * (M1 * s2[2] + M2 * s1[2])
        tot += w * np.sum(4 * tr4 / ((M1 ** 2 + sum(x ** 2 for x in s1)) * (M2 ** 2 + sum(x ** 2 for x in s2))))
    return tot
def ptad(N, xi, m, r=1.0):
    a, gs, hs = grids(N, xi); w = 16 * np.prod([h / (2 * np.pi) for h in hs]) * np.prod(1 / a); tot = 0.0
    for U in slices(gs):
        s = [np.sin(U[i]) / a[i] for i in range(4)]; M = m + sum(r * (1 - np.cos(U[i])) / a[i] for i in range(4))
        tot += w * np.sum((r * M * np.cos(U[2]) - np.sin(U[2]) * s[2]) / (M ** 2 + sum(x ** 2 for x in s)))
    return -4 * a[2] * tot
def Acoef(N, xi, m, nu, p0, dq=0.05):
    P1 = pbub(N, xi, m, dq, nu) - p0; P2 = pbub(N, xi, m, 2 * dq, nu) - p0; return (16 * P1 - P2) / (12 * dq * dq)
KF = 16 * np.pi ** 2
def kappa(N, xi, m):
    dce = (zfer(N, xi, m, 1)[0] - zfer(N, xi, m, 0)[0]) * KF; p0 = pbub(N, xi, m, 0.0, 1)
    dcg = (Acoef(N, xi, m, 1, p0) - Acoef(N, xi, m, 0, p0)) / 2 * KF
    return dce, dcg, (dce - dcg) / (4 * np.pi)
s0, IG0 = zfer(48, 1.0, 0.0, 0, scalar=True)
p0 = pbub(32, 1.0, 0.4, 0.0, 1); ward = abs(p0 + ptad(32, 1.0, 0.4))
lf = (zfer(32, 1.0, 0.1, 0)[0] - zfer(32, 1.0, 0.2, 0)[0]) * KF / np.log(2)
def pmap(N, beta, m, qv, nu, cont):
    t = (np.arange(N) + 0.5) / N; u = np.pi * np.sinh(beta * t) / np.sinh(beta); wq = np.pi * beta * np.cosh(beta * t) / np.sinh(beta) / N
    gs = [u] * 4; ws = [wq] * 4; gs[nu] = np.concatenate([-u[::-1], u]); ws[nu] = np.concatenate([wq[::-1], wq]); tot = 0.0
    for i4, u4 in enumerate(gs[0]):
        U = [np.array([[[u4]]]), gs[1][:, None, None], gs[2][None, :, None], gs[3][None, None, :]]
        Wt = ws[0][i4] * ws[1][:, None, None] * ws[2][None, :, None] * ws[3][None, None, :]; qa = [0.0] * 4; qa[nu] = qv
        k1 = [U[i] - qa[i] / 2 for i in range(4)]; k2 = [U[i] + qa[i] / 2 for i in range(4)]
        if cont: s1, s2, M1, M2, C, S = k1, k2, m, m, 1.0, 0.0
        else:
            s1 = [np.sin(x) for x in k1]; s2 = [np.sin(x) for x in k2]; C, S = np.cos(U[2]), np.sin(U[2])
            M1 = m + sum(1 - np.cos(x) for x in k1); M2 = m + sum(1 - np.cos(x) for x in k2)
        ss = sum(s1[i] * s2[i] for i in range(4))
        tr4 = S * S * (M1 * M2 - ss) - C * C * (M1 * M2 + ss - 2 * s1[2] * s2[2]) + 2 * S * C * (M1 * s2[2] + M2 * s1[2])
        tot += 8 / (2 * np.pi) ** 4 * np.sum(Wt * 4 * tr4 / ((M1 ** 2 + sum(x ** 2 for x in s1)) * (M2 ** 2 + sum(x ** 2 for x in s2))))
    return tot
def Amap(m, cont, N=40, beta=8.0):
    q0 = pmap(N, beta, m, 0.0, 1, cont); dq = 0.25 * m
    return (16 * (pmap(N, beta, m, dq, 0, cont) - q0) - (pmap(N, beta, m, 2 * dq, 0, cont) - q0)) / (12 * dq * dq)
lp = (Amap(0.05, True) - Amap(0.1, True)) * KF / (2 * np.log(2))
off = [Amap(m, False) * KF - 4 / 3 * np.log(1 / m ** 2) for m in (0.1, 0.05, 0.025, 0.0125, 0.00625)]; stp = np.diff(off)
check('C1 engine: Sigma(0) 16pi^2/e^2 = 51.43 (lit. 51.4347), I_G = Z0 .154933, Ward Pi(0) = 0, fermion IR log 2 (alpha/2pi '
      'per ln 1/m); vacuum polarisation: continuum integrand 4/3 per ln 1/m^2, Wilson offset converging',
      abs(s0 * KF - 51.4347) < 0.01 and abs(IG0 - 0.154933) < 2e-5 and ward < 1e-10 and abs(lf - 2) < 0.12 and abs(lp - 4 / 3) < 2e-3
      and np.all(np.diff(stp) < 0) and stp[-1] < 0.5 * stp[0],
      f'{s0 * KF:.3f}, {IG0:.6f}, {ward:.0e}, {lf:.3f}; {lp:.4f}; steps ' + ' '.join(f'{x:.2f}' for x in stp))
b4z = [kappa(24, 1.0, m)[:2] for m in (0.4, 0.1)]
check('C2 THEOREM at the B4 point xi = 1 the electron and photon one-loop speed shifts vanish identically',
      max(abs(v) for b in b4z for v in b) < 1e-9, f'max {max(abs(v) for b in b4z for v in b):.0e} at m = .4, .1')
kx = {xi: kappa(24, xi, 0.2) for xi in (1.25, 1.5, 2.0, 4.0, 8.0, 16.0, 32.0)}
km = [kappa(N_, 2.0, m)[2] for N_, m in ((24, 0.4), (32, 0.1), (48, 0.05))]
kinf = kx[32.0][2] + (kx[32.0][2] - kx[16.0][2]) * (kx[32.0][2] - kx[16.0][2]) / ((kx[16.0][2] - kx[8.0][2]) - (kx[32.0][2] - kx[16.0][2]))
aa = np.linalg.solve([[0.25, 0.0625], [0.5, 0.25]], [kx[1.25][2], kx[1.5][2]])
check('C3 FINITE off B4, kappa = d(c_e - c_gamma)/alpha is O(1) and negative, m-independent as m -> 0, and tends to -1.8 '
      'at continuous time (fermion-cones C3: -0.17..-1.0); the photon part is small', all(kx[x][2] < -0.3 for x in kx) and
      np.all(np.diff([kx[x][2] for x in sorted(kx)]) < 0) and max(km) - min(km) < 0.03 and all(0 < kx[x][1] < 1 for x in kx),
      'xi ' + ' '.join(f'{x:g}:{kx[x][2]:+.2f}' for x in sorted(kx)) + f' -> {kinf:+.2f}; m .4/.1/.05: '
      + '/'.join(f'{x:+.3f}' for x in km) + f'; slope at 1: {aa[0]:+.2f}')
print(f'   [{time.time() - T0:.0f} s]')

# ================================================================== D. chirality
print('== D. chirality on the B4 lattice')
def Dov(K, M, m=0.0):
    X = Dw(K, -M); nrm = np.sqrt((np.sin(K) ** 2).sum(-1) + ((1 - np.cos(K)).sum(-1) - M) ** 2)
    return (1 - m / 2) * (I4 + X / nrm[..., None, None]) + m * I4
Kr = rng.uniform(-np.pi, np.pi, (300, 4)); Do = Dov(Kr, 1.0)
gw = np.abs(G5 @ Do + Do @ G5 - Do @ G5 @ Do).max()
corn = np.array(list(itertools.product((0, np.pi), repeat=4)))[1:]; dc_ = np.abs(Dov(corn, 1.0) - 2 * I4).max()
N4 = 16; g4 = 2 * np.pi * np.arange(N4) / N4; K4 = np.stack(np.meshgrid(g4, g4, g4, g4, indexing='ij'), -1)
Dx = np.fft.ifftn(Dov(K4, 1.0), axes=(0, 1, 2, 3)); nt = np.array([np.linalg.norm(Dx[0, 0, 0, t], 2) for t in range(1, 8)])
nxs = np.array([np.linalg.norm(Dx[t, 0, 0, 0], 2) for t in range(1, 8)]); rt = np.log(nt[2] / nt[5]) / 3; del Dx, K4
check('D1 THEOREM 4D overlap (M = 1): GW exact, one light species (15 corners at D = 2), |D| along t = along x (B4), '
      'nonzero at every time separation: no nearest-slice transfer matrix of its own',
      gw < 1e-12 and dc_ < 1e-12 and np.abs(nt - nxs).max() < 1e-12 and nt[-1] > 1e-8, f'GW {gw:.0e}; |D(t=1,4,7)| '
      + ' '.join(f'{nt[i]:.0e}' for i in (0, 3, 6)) + f'; rate {rt:.2f}')
def DW4(L, U, M):
    X_ = np.array(list(itertools.product(range(L), repeat=4))); idx = {tuple(x): i for i, x in enumerate(X_)}; Nn = len(X_)
    D = np.kron(np.eye(Nn), (4 - M) * I4).astype(complex)
    for mu in range(4):
        for i, x in enumerate(X_):
            y = x.copy(); y[mu] = (y[mu] + 1) % L; j = idx[tuple(y)]
            D[4 * i:4 * i + 4, 4 * j:4 * j + 4] += -0.5 * (I4 - GAM[mu]) * U[mu][i]; D[4 * j:4 * j + 4, 4 * i:4 * i + 4] += -0.5 * (I4 + GAM[mu]) * np.conj(U[mu][i])
    return D
def thooft(L, n01, n23):
    X_ = np.array(list(itertools.product(range(L), repeat=4))); U = np.ones((4, len(X_)), complex)
    for (a_, b_, nn) in ((0, 1, n01), (2, 3, n23)):
        U[b_] *= np.exp(2j * np.pi * nn * X_[:, a_] / L ** 2); ed = X_[:, a_] == L - 1; U[a_][ed] *= np.exp(-2j * np.pi * nn * X_[ed, b_] / L)
    return U
G5b = np.kron(np.eye(256), G5); idxs = {}
for fl in ((1, 1), (1, -1), (0, 1), (2, 1)):
    wv = np.linalg.eigvalsh(G5b @ DW4(4, thooft(4, *fl), 1.0)); idxs[fl] = (int(np.sum(wv < 0)) - int(np.sum(wv > 0))) // 2
U3 = np.exp(1j * rng.normal(0, 0.4, (4, 81))); G5c = np.kron(np.eye(81), G5); Hc = G5c @ DW4(3, U3, 1.0)
wv, Vv = np.linalg.eigh((Hc + Hc.conj().T) / 2); Dc = np.eye(324) + G5c @ ((Vv * np.sign(wv)) @ Vv.conj().T); gwc = np.abs(G5c @ Dc + Dc @ G5c - Dc @ G5c @ Dc).max()
check('D2 THEOREM 4^4 with electric (z,t) and magnetic flux: overlap index = -Q; GW holds with random temporal links: exact '
      'chirality in electric backgrounds, unlike the 3D overlap (s-tick-dressing T5)', all(idxs[f] == -f[0] * f[1] for f in idxs) and gwc < 1e-12,
      'Q:index ' + ' '.join(f'{f[0] * f[1]}:{idxs[f]:+d}' for f in idxs) + f'; GW {gwc:.0e}')
def corr_t(Dfun, p, Tt=128):
    k4 = 2 * np.pi * (np.arange(Tt) + 0.5) / Tt; K = np.c_[np.broadcast_to(p, (Tt, 3)), k4]
    S = np.linalg.inv(Dfun(K)); ts = np.arange(1, 16)
    return dict(zip(ts, np.einsum('kt,kab->tab', np.exp(1j * np.outer(k4, ts)), S) / Tt))
def hank(G, t0, nh=6):
    H = np.block([[G4 @ G[t0 + i + j] for j in range(nh)] for i in range(nh)]); ev = np.linalg.eigvalsh((H + H.conj().T) / 2); return ev.min() / ev.max()
PP5, PM5, Pp4, Pm4 = (I4 + G5) / 2, (I4 - G5) / 2, (I4 + G4) / 2, (I4 - G4) / 2
def dwf_slice(p, M5, Ls, mf):
    Ms = (1 - np.cos(p)).sum(); W = np.zeros((4 * Ls, 4 * Ls), complex)
    for s in range(Ls):
        W[4 * s:4 * s + 4, 4 * s:4 * s + 4] = (2 + Ms - M5) * I4 + sum(1j * np.sin(p[j]) * GAM[j] for j in range(3))
        if s + 1 < Ls: W[4 * s:4 * s + 4, 4 * s + 4:4 * s + 8] = -PM5
        if s >= 1: W[4 * s:4 * s + 4, 4 * s - 4:4 * s] = -PP5
    W[-4:, :4] += mf * PM5; W[:4, -4:] += mf * PP5
    return W
def dwfq(M5, Ls, mf=0.05):
    def f(K):
        out = []
        for kk in K:
            D = dwf_slice(kk[:3], M5, Ls, mf) - np.kron(np.eye(Ls), Pm4) * np.exp(1j * kk[3]) - np.kron(np.eye(Ls), Pp4) * np.exp(-1j * kk[3]); Gi = np.linalg.inv(D)
            out.append(np.linalg.inv(PM5 @ Gi[:4, :4] @ PP5 + PM5 @ Gi[:4, -4:] @ PM5 + PP5 @ Gi[-4:, :4] @ PP5 + PP5 @ Gi[-4:, -4:] @ PM5))
        return np.array(out)
    return f
cand = {'Wilson r=1': lambda K: Dw(K, 0.2), 'r=.5': lambda K: Dw(K, 0.2, 0.5), 'naive': lambda K: Dw(K, 0.2, 0.0),
        'ov M=.5': lambda K: Dov(K, 0.5, 0.2), 'ov M=1': lambda K: Dov(K, 1.0, 0.2), 'ov M=1.5': lambda K: Dov(K, 1.5, 0.2),
        'DWF M5=.5': dwfq(0.5, 8), 'DWF M5=.9': dwfq(0.9, 8), 'DWF M5=1.5': dwfq(1.5, 8)}
pset = [np.zeros(3), np.array([0.5, 0, 0]), np.array([0.9, 0.4, 0.2]), np.array([np.pi, 0, 0]), np.array([2.0, 2.0, 2.0])]
hk = {}
for nm, f in cand.items():
    Gs = [corr_t(f, p) for p in pset]; hk[nm] = (min(hank(G_, 1) for G_ in Gs), min(hank(G_, 2) for G_ in Gs))
passT = ['Wilson r=1', 'ov M=.5', 'ov M=1', 'DWF M5=.5', 'DWF M5=.9']; failT = ['r=.5', 'naive', 'ov M=1.5', 'DWF M5=1.5']
check('D3 FINITE free 2-point transfer positivity (Hankel of g4 G(tau >= 2), necessary): pass Wilson r=1, overlap M = .5, 1, '
      'DWF M5 = .5, .9; fail below; link RP (tau >= 1) passes all', all(hk[x][1] > -1e-10 for x in passT) and all(hk[x][1] < -1e-3 for x in failT)
      and all(hk[x][0] > -1e-10 for x in hk), 'fails: ' + ', '.join(f'{x} {hk[x][1]:+.0e}' for x in failT))
dres = []; sim = 0.0
for M5 in (0.5, 0.9, 1.4):
    bm, rm = [], []
    for p in (np.zeros(3), np.array([0.3, 0, 0]), np.array([1.0, 0.5, 0.2]), np.array([np.pi, 0, 0])):
        W = dwf_slice(p, M5, 8, 0.0); G4b = np.kron(np.eye(8), G4); B = (W + G4b @ W @ G4b) / 2; C = (W - G4b @ W @ G4b) / 2
        iu = [i for i in range(32) if i % 4 < 2]; iv = [i for i in range(32) if i % 4 >= 2]
        Bu, Bv, c, cp = B[np.ix_(iu, iu)], B[np.ix_(iv, iv)], C[np.ix_(iu, iv)], C[np.ix_(iv, iu)]; Bi = np.linalg.inv(Bu)
        ev = np.linalg.eigvals(np.block([[Bi @ (np.eye(16) - c @ cp), -Bi @ c @ Bv], [cp, Bv]]))
        bm.append(np.linalg.eigvalsh(Bu).min()); rm.append(ev.real.min() if np.abs(ev.imag).max() < 1e-9 else -99)
        if M5 < 1:
            wb, Vb = np.linalg.eigh(Bu); Bh = (Vb * np.sqrt(wb)) @ Vb.conj().T; Bmh = (Vb / np.sqrt(wb)) @ Vb.conj().T
            Rm = np.block([[Bi @ (np.eye(16) - c @ cp), -Bi @ c @ Bv], [cp, Bv]]); Sd = np.kron(np.eye(2), Bh)
            Lt = np.block([[Bmh, -Bmh @ c], [np.zeros((16, 16)), Bh]]); sim = max(sim, np.abs(Sd @ Rm @ np.linalg.inv(Sd) - Lt @ Lt.conj().T).max())
        herm = max(np.abs(B - B.conj().T).max(), np.abs(C + C.conj().T).max())
    dres.append((min(bm), min(rm), herm))
Ls3 = 4; X3 = np.array(list(itertools.product(range(3), repeat=3))); i3 = {tuple(x): i for i, x in enumerate(X3)}
Bg = np.zeros((27 * Ls3, 27 * Ls3), complex); Uj = np.exp(1j * rng.uniform(-np.pi, np.pi, (3, 27)))
for i, x in enumerate(X3):
    for j_ in range(3):
        y = x.copy(); y[j_] = (y[j_] + 1) % 3; k_ = i3[tuple(y)]
        for s_ in range(Ls3): Bg[27 * s_ + i, 27 * s_ + k_] -= 0.5 * Uj[j_, i]; Bg[27 * s_ + k_, 27 * s_ + i] -= 0.5 * np.conj(Uj[j_, i])
for s_ in range(Ls3):
    Bg[27 * s_:27 * s_ + 27, 27 * s_:27 * s_ + 27] += (2 + 3 - 0.9) * np.eye(27)
    if s_ + 1 < Ls3: Bg[27 * s_:27 * s_ + 27, 27 * s_ + 27:27 * s_ + 54] -= 0.5 * np.eye(27); Bg[27 * s_ + 27:27 * s_ + 54, 27 * s_:27 * s_ + 27] -= 0.5 * np.eye(27)
bgmin = np.linalg.eigvalsh(Bg).min()
mres = {}
for M5 in (0.5, 0.9):
    v = []
    for Ls in (4, 6, 8, 10):
        D = dwf_slice(np.zeros(3), M5, Ls, 0.0) - np.kron(np.eye(Ls), Pm4 + Pp4); Gi = np.linalg.inv(D)
        v.append(np.linalg.svd(np.linalg.inv(PM5 @ Gi[:4, :4] @ PP5 + PM5 @ Gi[:4, -4:] @ PM5 + PP5 @ Gi[-4:, :4] @ PP5 + PP5 @ Gi[-4:, -4:] @ PM5), compute_uv=False).min())
    mres[M5] = v
check('D4 THEOREM Shamir DWF have the r=1 slice form (B Herm., C anti-Herm.); for any B > 0 the recursion is similar to '
      'L L^dag, so M5 < 1 gives positive physical-time transfer at every L_s; M5 > 1 gives negative modes; free m_res = '
      '(1 - M5)^L_s exactly; B >= 1 - M5 holds with any spatial links', sim < 1e-10 and bgmin >= 0.1 - 1e-12 and dres[0][0] > 0 and dres[1][0] > 0 and dres[0][1] > 0 and dres[1][1] > 0 and dres[2][0] < 0 and dres[2][1] < 0 and max(d[2] for d in dres) < 1e-12
      and all(abs(mres[M5][i] - (1 - M5) ** L_) < 1e-6 * (1 - M5) ** L_ for M5 in mres for i, L_ in enumerate((4, 6, 8, 10))),
      f'M5 .5/.9/1.4: min B {dres[0][0]:.2f}/{dres[1][0]:.2f}/{dres[2][0]:+.2f}, min R {dres[0][1]:.2f}/{dres[1][1]:.2f}/'
      f'{dres[2][1]:+.1f}; random U(1) links, M5 .9: min B {bgmin:.2f}; m_res(10) {mres[0.5][3]:.2e}, {mres[0.9][3]:.0e}')
L2 = 16; xs2 = np.arange(L2)
def DW2(A0, A1, M):
    D = np.kron(np.eye(L2 * L2), (2 - M) * np.eye(2)).astype(complex)
    for x0 in range(L2):
        for x1 in range(L2):
            i = x0 * L2 + x1
            for mu, ph in ((0, A0), (1, A1)):
                y = [x0, x1]; y[mu] = (y[mu] + 1) % L2; j = y[0] * L2 + y[1]; u = np.exp(1j * ph[x0, x1])
                D[2 * i:2 * i + 2, 2 * j:2 * j + 2] += -0.5 * (np.eye(2) - SIG[mu]) * u; D[2 * j:2 * j + 2, 2 * i:2 * i + 2] += -0.5 * (np.eye(2) + SIG[mu]) * np.conj(u)
    return D
A1f = np.outer(2 * np.pi * xs2 / L2 ** 2, np.ones(L2)) + 0.25 * np.outer(np.cos(2 * np.pi * xs2 / L2), np.sin(2 * np.pi * xs2 / L2))
A0f = np.zeros((L2, L2)); A0f[L2 - 1, :] = -2 * np.pi * xs2 / L2; g52 = np.kron(np.eye(L2 * L2), SIG[2]); dens = {}
for e in (1, 3, 4, 5):
    H2 = g52 @ DW2(e * A0f, e * A1f, 1.0); w2, V2 = np.linalg.eigh((H2 + H2.conj().T) / 2); Do2 = np.eye(2 * L2 * L2) + g52 @ ((V2 * np.sign(w2)) @ V2.conj().T)
    dens[e] = np.array([-0.5 * np.trace(SIG[2] @ Do2[2 * i:2 * i + 2, 2 * i:2 * i + 2]).real for i in range(L2 * L2)])
Aan = 3 * dens[3] + 4 * dens[4] - 5 * dens[5]; rel = np.abs(Aan).max() / np.abs(5 * dens[5]).max()
check('D5 FINITE 2D 3-4-5 (non-uniform flux, 16^2): indices -e exactly; anomaly densities cancel pointwise to a lattice artifact',
      all(abs(dens[e].sum() + e) < 1e-9 for e in dens) and rel < 1e-3 and abs(Aan.sum()) < 1e-9,
      f'residual/|5 q5| {rel:.0e}')
print(f'   [{time.time() - T0:.0f} s]')

# ================================================================== E. estimates
print('== E. ESTIMATES (measured numbers supplied; not theorems)')
al = 1 / 137.036; me = 0.51099895e6; EP = 1.22089e28; aP = 5.0
dI = abs(kinf) * al; print(f'   no B4 (continuous time): |dc| {dI:.1e}, photon decay above {2 * me / np.sqrt(2 * dI) / 1e6:.0f} MeV; x{dI / 3e-19:.0e} LHAASO 3e-19')
print(f'   B4: dim-4 shift 0 at all orders; dim-6 (E a)^2 at 1.4 PeV (a = 5 l_P) {(1.4e15 * aP / EP) ** 2:.0e}')
kpr = aa[0]
for nm, ph in (('Earth surface', 7e-10), ('Sun at 1 AU', 1e-8), ('Galaxy', 1e-6)):
    dd = abs(kpr) * al * 2 * ph; print(f'   cells 2|Phi| anisotropic ({nm} {ph:.0e}): |dc| {dd:.0e}, decay above {2 * me / np.sqrt(2 * dd) / 1e9:.0f} GeV, x{dd / 3e-19:.0e}')
mea = me * aP / EP; L9 = int(np.ceil(np.log(mea) / np.log(0.1))); L5 = int(np.ceil(np.log(mea) / np.log(0.5)))
print(f'   DWF: m_res < m_e a = {mea:.1e} needs L_s >= {L9} (M5 .9) or {L5} (M5 .5): {4 * L9}-{4 * L5} modes per site')
check('E1 arithmetic: non-B4 shift excluded by > 1e15; Earth-surface cell anisotropy by > 1e6',
      dI / 3e-19 > 1e15 and abs(kpr) * al * 2 * 7e-10 / 3e-19 > 1e6)
print('supplied: 4D action (B4, r, M, M5, L_s), plaquette photon, Feynman gauge, one loop, e^2 = 4 pi alpha, cell anisotropy 2|Phi|,')
print('  a = 5 l_P, bounds. forced: T >= 0, quasi-local H (ln 3), B4 zero shifts, kappa != 0 off B4, >= 2 tastes, GW index, m_res.')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
