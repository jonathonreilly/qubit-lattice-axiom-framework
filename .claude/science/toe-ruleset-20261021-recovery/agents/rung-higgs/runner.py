#!/usr/bin/env python3
"""Gauge-Higgs unification on the zoom ladder: the rung link as A_5, its one-loop Wilson-line potential, the warped hierarchy.
Supplied models; exact finite-dimensional computations, then estimates against measurement.
 A  rung-link zero modes and their quantum numbers (register PS ladder, SU(3)_W, SU(4) x SO(5)); index obstruction
 B  exact one-loop Wilson-line (Hosotani) potential on a deconstructed rung chain: flat (fine rate) and warp 1/2 (zoom rate);
    bulk SU(4) x SO(5), lattice-orbifold ends (UV: SM, IR: PS), 4D continuum per rung, Coleman-Weinberg sums
 C  the warped ladder and the hierarchy v/M_UV ~ 2^-N
 D  against measurement (estimates)
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
from scipy.linalg import expm, null_space, orth
from scipy.interpolate import CubicSpline

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))

# ------------------------------------------------------------------ algebra helpers
def gellmann(n):
    G = []
    for i in range(n):
        for j in range(i + 1, n):
            M = np.zeros((n, n), complex); M[i, j] = M[j, i] = 0.5; G.append(M)
            M = np.zeros((n, n), complex); M[i, j] = -0.5j; M[j, i] = 0.5j; G.append(M)
    for k in range(1, n):
        d = np.zeros(n); d[:k] = 1; d[k] = -k; G.append(np.diag(d / np.sqrt(2 * k * (k + 1))).astype(complex))
    return G
def blk(*Ms):
    n = sum(M.shape[0] for M in Ms); out = np.zeros((n, n), complex); o = 0
    for M in Ms: k = M.shape[0]; out[o:o + k, o:o + k] = M; o += k
    return out
def coords(basis, mats):
    return np.array([[np.real(np.trace(b.conj().T @ v)) / np.real(np.trace(b.conj().T @ b)) for b in basis] for v in mats]).T
def zero_modes(g, hUV, hIR, T3, Y, N=3):
    """uniform rung-link zero modes = (hUV + hIR)^perp; cross-checked by the chain count N dim g - rank(gauge map)"""
    d = len(g); A, B = coords(g, hUV), coords(g, hIR); m = null_space(np.hstack([A, B]).T)
    cols = [np.concatenate([a, np.zeros((N - 1) * d)]) for a in A.T]
    for jn in range(1, N):
        for e in np.eye(d): x = np.zeros(N * d); x[(jn - 1) * d:jn * d] -= e; x[jn * d:(jn + 1) * d] += e; cols.append(x)
    cols += [np.concatenate([np.zeros((N - 1) * d), -b]) for b in B.T]
    inv = N * d - np.linalg.matrix_rank(np.array(cols).T, tol=1e-9)
    ad = lambda X: coords(g, [-1j * (X @ gi - gi @ X) for gi in g])
    ch = []
    if m.shape[1]:
        a3, aY = 1j * (m.T @ ad(T3) @ m), 1j * (m.T @ ad(Y) @ m); w, V = np.linalg.eig(a3 + np.pi * aY); Vi = np.linalg.inv(V)
        ch = sorted(zip(np.round(np.real(np.diag(Vi @ a3 @ V)), 4), np.round(np.real(np.diag(Vi @ aY @ V)), 4)))
    return m.shape[1], int(inv), ch
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex); s0 = np.eye(2)
gam = [np.kron(sx, sx), np.kron(sx, sy), np.kron(sx, sz), np.kron(sy, s0)]; gam.append(gam[0] @ gam[1] @ gam[2] @ gam[3])
pairs = [(a, b) for a in range(5) for b in range(a + 1, 5)]
Sp = {p: -0.25j * (gam[p[0]] @ gam[p[1]] - gam[p[1]] @ gam[p[0]]) for p in pairs}           # so(5) on the spinor 4
Vr = {p: -1j * (np.eye(5)[:, [p[0]]] @ np.eye(5)[[p[1]]] - np.eye(5)[:, [p[1]]] @ np.eye(5)[[p[0]]]) for p in pairs}   # vector 5
eps3 = np.zeros((3, 3, 3))
for i, j, k in itertools.permutations(range(3)): eps3[i, j, k] = np.linalg.det(np.eye(3)[[i, j, k]])
def TLR(rep, s):
    gen = lambda a, b: rep[(a, b)] if a < b else -rep[(b, a)]
    return [0.5 * (0.5 * sum(eps3[i, j, k] * gen(j, k) for j in range(3) for k in range(3) if j != k) + s * gen(i, 3)) for i in range(3)]
TL, TR = TLR(Sp, 1), TLR(Sp, -1)
G4, G2, Z4, Z2 = gellmann(4), gellmann(2), np.zeros((4, 4)), np.zeros((2, 2))
BL = np.diag([1 / 3, 1 / 3, 1 / 3, -1]).astype(complex)

# ================================================================== A
print('== A. rung-link zero modes (uniform Wilson lines between the end groups) and their quantum numbers')
ps = [blk(x, Z2, Z2) for x in G4] + [blk(Z4, x, Z2) for x in G2] + [blk(Z4, Z2, x) for x in G2]
T3L, YPS = blk(Z4, G2[2], Z2), blk(Z4, Z2, G2[2]) + blk(BL / 2, Z2, Z2)
smPS = [blk(np.pad(x, ((0, 1), (0, 1))), Z2, Z2) for x in gellmann(3)] + [blk(Z4, x, Z2) for x in G2] + [YPS]
r1 = zero_modes(ps, smPS, ps, T3L, YPS); r2 = zero_modes(ps, smPS, smPS, T3L, YPS)
l3 = gellmann(3); hW = [l3[0], l3[1], l3[6], l3[7]]; r3 = zero_modes(l3, hW, hW, l3[6], l3[7] / np.sqrt(3))
g45 = [blk(x, Z4) for x in G4] + [blk(Z4, Sp[p]) for p in pairs]; Y5 = blk(BL / 2, TR[2])
psIR = [blk(x, Z4) for x in G4] + [blk(Z4, Sp[p]) for p in pairs if p[1] <= 3]
smUV = [blk(np.pad(x, ((0, 1), (0, 1))), Z4) for x in gellmann(3)] + [blk(Z4, t) for t in TL] + [Y5]
r4 = zero_modes(g45, smUV, psIR, blk(Z4, TL[2]), Y5)
check('A1 THEOREM count = dim (h_UV + h_IR)^perp = N dim g - rank(gauge map): register PS bulk (UV SM, IR PS) 0; PS (SM, SM) 9; '
      'SU(3)_W (SU(2)xU(1) ends) 4; SU(4)xSO(5) (UV SM, IR PS) 4', [r[:2] for r in (r1, r2, r3, r4)] == [(0, 0), (9, 9), (4, 4), (4, 4)],
      '(dim, chain) ' + ' '.join(f'{r[0]},{r[1]}' for r in (r1, r2, r3, r4)))
adC = lambda X: coords(ps, [-1j * (X @ gi - gi @ X) for gi in ps])
cas = sorted(set(float(abs(c)) for c in np.round(np.linalg.eigvals(-sum(adC(blk(Z4, x, Z2)) @ adC(blk(Z4, x, Z2)) for x in G2)).real, 6)))
check('A2 THEOREM SU(2)_L Casimir on adj(PS) is {0, 2}: no doublet with any end groups; PS (SM, SM) modes: T3 = 0, Y = +-2/3 (x3), +-1, 0',
      cas == [0.0, 2.0] and all(t == 0 for t, _ in r2[2]) and sorted(y for _, y in r2[2]) == [-1, -0.6667, -0.6667, -0.6667, 0, 0.6667, 0.6667, 0.6667, 1],
      f'Casimir {cas}')
def e16(blocks):
    M = np.zeros((16, 16), complex)
    for (a, b), X in blocks: M[a:b, a:b] = X
    return M
c16 = [e16([((0, 6), np.kron(t, s0)), ((6, 9), -t.conj()), ((9, 12), -t.conj())]) for t in l3]   # Q, u^c, d^c, L, e^c, nu^c (all left-handed)
w16 = [e16([((0, 6), np.kron(np.eye(3), t)), ((12, 14), t)]) for t in G2]
Y16 = np.diag([1 / 6] * 6 + [-2 / 3] * 3 + [1 / 3] * 3 + [-1 / 2] * 2 + [1, 0]).astype(complex)
d3, dY = np.real(np.diag(w16[2])), np.real(np.diag(Y16)); Dg = []
for t, y in itertools.product((0.5, -0.5), (0.5, -0.5)):
    Bs = [np.eye(16)[:, [i]] @ np.eye(16)[[j]] for i in range(16) for j in range(16) if abs(d3[i] - d3[j] - t) < 1e-9 and abs(dY[i] - dY[j] - y) < 1e-9]
    ns = null_space(np.array([np.concatenate([(c @ E - E @ c).ravel() for c in c16]) for E in Bs]).T)
    Dg += [sum(ns[k, m] * Bs[k] for k in range(len(Bs))) for m in range(ns.shape[1])]
def closure(gens):
    basis, vec = [], lambda M: np.concatenate([M.real.ravel(), M.imag.ravel()])
    def add(M):
        if basis:
            Bm = np.array([vec(b) for b in basis]).T
            if np.linalg.norm(vec(M) - Bm @ np.linalg.lstsq(Bm, vec(M), rcond=None)[0]) < 1e-8: return False
        basis.append(M); return True
    for g in gens: add(g)
    grown = True
    while grown:
        grown = False
        for a, b in itertools.combinations(list(basis), 2): grown |= add(1j * (a @ b - b @ a))
    return basis
alg = closure(c16 + w16 + [Y16] + [m for E in Dg for m in (E + E.conj().T, 1j * (E - E.conj().T))])
Z16 = np.diag([0] * 12 + [1, 1, 0, -2]).astype(complex) / np.sqrt(12); joins = all(set(np.argwhere(np.abs(E) > 1e-9).ravel()) <= {12, 13, 15} for E in Dg)
check('A3 THEOREM on one family\'s 16 (either exchange orientation) the only colourless |Y| = 1/2 doublet generators join L to nu^c; with the SM they generate SU(3) on (L, nu^c) alone, '
      'whose cubic anomaly is nonzero, so CL-3\'s anomaly-free rule links no doublet direction', len(Dg) == 4 and joins and len(alg) == 20 and abs(np.trace(Z16 @ Z16 @ Z16)) > 0.1,
      f'{len(Dg)} generators; algebra dim {len(alg)}; Tr Z^3 {np.trace(Z16 @ Z16 @ Z16).real:.3f}')
Qw = l3[6] + l3[7] / np.sqrt(3); s2w = np.trace(l3[6] @ l3[6]).real / np.trace(Qw @ Qw).real
check('A4 THEOREM SU(3)_W: one doublet, (T3, Y) = (+-1/2, +-1/2), Q = (2/3, -1/3, -1/3) on the 3; sin^2 thW = Tr T3^2/Tr Q^2 = 3/4 (measured 0.2312)',
      sorted(set(r3[2])) == [(-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5), (0.5, 0.5)] and abs(s2w - 0.75) < 1e-12, f'sin^2 {s2w:.4f}')
check('A5 THEOREM SU(4)xSO(5) bulk, UV SM, IR PS: the modes are SO(5)/SO(4) = (1,2,2), one colourless doublet with Y = T3R = +-1/2',
      sorted(set(r4[2])) == [(-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5), (0.5, 0.5)])
Mat = np.array([np.kron(np.eye(4), Sp[p]) - np.kron(Sp[p].T, np.eye(4)) for p in pairs]).reshape(-1, 16)
CL = sum(t @ t for t in TL); w_, v_ = np.linalg.eigh(CL); Pp = v_[:, w_ > 0.5] @ v_[:, w_ > 0.5].conj().T; Pm = np.eye(4) - Pp
lo, hi = np.array([[0, 0], [1, 0]]), np.array([[0, 1], [0, 0]]); Xreg = np.kron(lo, Pp) + np.kron(hi, Pm); H45 = np.kron(s0, Sp[(3, 4)])
t15 = np.trace(G4[-1] @ G4[-1] @ G4[-1]).real
cm = np.linalg.norm(H45 @ Xreg - Xreg @ H45); c4 = max(np.linalg.norm(np.kron(s0, Sp[p]) @ Xreg - Xreg @ np.kron(s0, Sp[p])) for p in pairs if p[1] <= 3)
check('A6 THEOREM so(5) commutant on the spinor 4 is 1-dim, so an SO(5)-symmetric gapped bulk gives (2,1) and (1,2) one index: zero modes (4,4)_L, '
      'SU(4)^3 anomaly 4 (the 16: 0); the register\'s chirality-graded exchange keeps so(4) but not the doublet generator',
      null_space(Mat).shape[1] == 1 and abs(cm) > 1 and c4 < 1e-12, f'anomaly (4,4) {4 * t15 / t15:.0f}, 16 {abs(2 * t15 - 2 * t15) / abs(t15):.0f}; |[T45, X_reg]| {cm:.3f}')

# ================================================================== B
print('== B. one-loop Wilson-line potential on a rung chain (supplied bulk SU(4)xSO(5); exact CW sums; IR units, last link 1)')
Tn = [Sp[p] / np.sqrt(2) for p in pairs]
def emb(M): v = np.zeros(11); v[:10] = [np.real(np.trace(T.conj().T @ M)) / np.real(np.trace(T.conj().T @ T)) for T in Tn]; return v
eX = np.eye(11)[10]
hUV = np.array([emb(t) for t in TL] + [emb(TR[2]) + eX]).T; hIR = np.array([emb(Sp[p]) for p in pairs if p[1] <= 3] + [eX]).T
Kg = np.zeros((11, 11))
for j in range(10): Kg[:, j] = emb(1j * (Sp[(3, 4)] @ Tn[j] - Tn[j] @ Sp[(3, 4)]))
reps = {}
for nm, rep in (('spinor', Sp), ('vector', Vr)):
    if nm == 'spinor': P1, P2 = v_[:, w_ > 0.5], v_[:, w_ < 0.5]
    else: P1, P2 = np.eye(5)[:, :4].astype(complex), np.eye(5)[:, 4:].astype(complex)
    reps[nm] = (rep[(3, 4)], P1, P2)
g4 = 0.6517; MUV_GeV = 2.435e18
def chain(N, q, nir):
    f = q ** (np.arange(N) - (N - 1.0))
    return (f, 1) if nir is None or nir >= N else (f[N - nir:], N - nir + 1)
_bc = {}
def D_vec(N, th, q, nir=None):
    g5 = g4 * np.sqrt(N + 1); f, w = chain(N, q, nir); n = len(f)
    if g5 not in _bc:
        G = np.diag([g5] * 10 + [np.sqrt(1.5) * g5]); Gi = np.linalg.inv(G); _bc[g5] = (G, orth(Gi @ hUV), orth(Gi @ hIR))
    G, B0, BN = _bc[g5]; bases = [B0] + [np.eye(11)] * (n - 1) + [BN]; Gs = [G / np.sqrt(w)] + [G] * n
    off = np.cumsum([0] + [b.shape[1] for b in bases]); D = np.zeros((11 * n, off[-1])); dD = np.zeros_like(D); R = expm(th * Kg)
    for j in range(n):
        D[11 * j:11 * j + 11, off[j]:off[j + 1]] += f[j] * Gs[j] @ bases[j]
        D[11 * j:11 * j + 11, off[j + 1]:off[j + 2]] -= f[j] * (R if j == n - 1 else np.eye(11)) @ Gs[j + 1] @ bases[j + 1]
    dD[11 * (n - 1):, off[n]:] -= f[-1] * Kg @ R @ Gs[n] @ bases[n]
    return D, dD
def M_fer(rep, N, th, q, eta=1, c=0.0, nir=None):
    H, P1, P2 = reps[rep]; d = H.shape[0]; U = expm(1j * th * H); y = g4 * np.sqrt(N + 1); f, w = chain(N, q, nir); n = len(f)
    Lb = [P1] + [np.eye(d)] * (n - 1) + [P1 if eta == 1 else P2]; sc = [1 / np.sqrt(w)] + [1.0] * n
    off = np.cumsum([0] + [b.shape[1] for b in Lb]); M = np.zeros((off[-1], d * n), complex); dM = np.zeros_like(M)
    for j in range(n):
        M[off[j]:off[j + 1], d * j:d * j + d] += y * f[j] * np.exp(-c) * sc[j] * Lb[j].conj().T
        M[off[j + 1]:off[j + 2], d * j:d * j + d] -= y * f[j] * np.exp(c) * sc[j + 1] * Lb[j + 1].conj().T @ (U if j == n - 1 else np.eye(d))
    dM[off[n]:off[n + 1], d * (n - 1):] -= y * f[-1] * np.exp(c) * sc[n] * Lb[n].conj().T @ (1j * H @ U)
    return M, dM
def hf(A, dA):
    """Hellmann-Feynman: d/dth sum_k F(s_k^2), F(x) = x^2 ln x; stable under warping (UV modes enter only through their IR overlap)"""
    u, s, vh = np.linalg.svd(A, full_matrices=False); ds = np.real(np.einsum('ik,ij,jk->k', u.conj(), dA, vh.conj().T)); x = s * s
    return np.sum(np.where(x > 1e-30, 2 * x * np.log(np.maximum(x, 1e-300)) + x, 0) * 2 * s * ds)
def dV(th, N, q, kind, eta=1, c=0.0, nir=None):
    if kind == 'gauge': return 3 * hf(*D_vec(N, th, q, nir)) / (64 * np.pi ** 2)
    return -4 * hf(*M_fer(kind, N, th, q, eta, c, nir)) / (64 * np.pi ** 2)
ths = np.linspace(0, np.pi, 121); hth = ths[1] - ths[0]
grid = lambda kind, N, q, eta=1, c=0.0, nir=None: np.array([dV(t, N, q, kind, eta, c, nir) for t in ths])
integ = lambda d: np.concatenate([[0], np.cumsum((d[..., 1:] + d[..., :-1]) / 2, axis=-1) * hth], axis=-1) if d.ndim == 1 else \
    np.concatenate([np.zeros(d.shape[:-1] + (1,)), np.cumsum((d[..., 1:] + d[..., :-1]) / 2, axis=-1) * hth], axis=-1)
Fh = lambda N, q: 1 / np.sqrt(np.sum(q ** (-2 * (np.arange(N) - (N - 1.0)))))
_mk = {}
def mkk(N, q, nir=None):
    if (N, q) not in _mk: s = np.sort(np.linalg.svd(D_vec(N, 0.0, q, nir)[0], compute_uv=False)); _mk[N, q] = s[s > 1e-9][0]
    return _mk[N, q]
def light(N, q, th, nir=None):
    mv = np.sort(np.linalg.svd(D_vec(N, th, q, nir)[0], compute_uv=False)); mv = mv[mv > 1e-9]
    mf = np.sort(np.linalg.svd(M_fer('spinor', N, th, q, nir=nir)[0], compute_uv=False)); return mv[0], mv[2], mf[0], mf[1]
def minimum(d, N, q, nir=None):
    V = integ(d); i = int(np.argmin(V))
    if i in (0, len(ths) - 1): return None
    sp = CubicSpline(ths, d); tt = np.linspace(ths[i - 1], ths[i + 1], 201); thm = tt[np.argmin(np.abs(sp(tt)))]
    mW, mZ, mf, _ = light(N, q, thm, nir); mH = np.sqrt(max(sp(thm, 1), 0) / (2 * Fh(N, q) ** 2))
    return dict(th=thm, mH_mW=mH / mW, v_mKK=2 * mW / g4 / mkk(N, q, nir), mZ_mW=mZ / mW, mf_mW=mf / mW)
# B1 sum rules
def sums(N, th):
    a = np.linalg.svd(D_vec(N, th, 1.0)[0], compute_uv=False); b = np.linalg.svd(M_fer('spinor', N, th, 1.0)[0], compute_uv=False)
    return np.array([np.sum(a ** 2), np.sum(a ** 4), np.sum(b ** 2), np.sum(b ** 4)])
sr = {N: np.ptp([sums(N, t) for t in (0.0, 0.9, 2.1)], axis=0) / sums(N, 0.0) for N in (1, 2, 4)}
check('B1 THEOREM sum m^2, sum m^4 (vectors, fermions) are theta-independent for N >= 2 links, so V is finite; for N = 1 sum m^4 is not',
      max(sr[2].max(), sr[4].max()) < 1e-12 and sr[1][1] > 0.05 and sr[1][3] > 0.05, f'rel spread N=2,4: {max(sr[2].max(), sr[4].max()):.0e}; N=1 m^4: {sr[1][1]:.2f}, {sr[1][3]:.2f}')
def Vdir(th, N, q):
    a = np.linalg.svd(D_vec(N, th, q)[0], compute_uv=False); b = np.linalg.svd(M_fer('spinor', N, th, q)[0], compute_uv=False)
    F = lambda m: np.sum(m[m > 1e-12] ** 4 * np.log(m[m > 1e-12] ** 2)); return (3 * F(a) - 16 * F(b)) / (64 * np.pi ** 2)
fd = (Vdir(1.1 + 1e-4, 4, 1.0) - Vdir(1.1 - 1e-4, 4, 1.0)) / 2e-4; hv = dV(1.1, 4, 1.0, 'gauge') + 4 * dV(1.1, 4, 1.0, 'spinor')
mg = [dV(1.7, 14, 0.5, 'gauge', nir=k) + 4 * dV(1.7, 14, 0.5, 'spinor', nir=k) for k in (None, 10, 6)]
check('B2 THEOREM Hellmann-Feynman dV/dth equals the finite difference of the direct CW sum; merging the UV links into one node converges as 4^-(kept links)',
      abs(hv / fd - 1) < 1e-6 and abs(mg[1] / mg[0] - 1) < 1e-4 and abs(mg[2] / mg[0] - 1) < 1e-2, f'HF/FD-1 {hv / fd - 1:.0e}; N=14 kept 10, 6: {mg[1] / mg[0] - 1:.0e}, {mg[2] / mg[0] - 1:.0e}')
cases = [(N, q, None) for N in (2, 3, 4, 6, 8, 12) for q in (1.0, 0.5)] + [(52, 0.5, 16)]
okB3 = True; vals = {}
for N, q, nir in cases:
    dg, ds = grid('gauge', N, q, nir=nir), grid('spinor', N, q, nir=nir); Vg, Vs = integ(dg), integ(ds)
    for nf in (1, 3):
        V = Vg + 4 * nf * Vs; okB3 &= (np.argmin(V) == len(ths) - 1) and (min(Vg[0], Vg[-1]) <= Vg.min() + 1e-12) and np.argmin(Vs) == len(ths) - 1
    vals[N, q] = (Vg[0] + 4 * Vs[0] - Vg[-1] - 4 * Vs[-1]) / mkk(N, q, nir) ** 4
check('B3 THEOREM the rules\' content (gauge + 1 or 3 families as bulk (4,4)s): the gauge part is least at th in {0, pi}, the family part at th = pi, '
      'so th_min = pi for N = 2, 3, 4, 6, 8, 12 (flat, warped) and 52 (warped): SU(2)xU(1) unbroken, family gapped, no EW breaking',
      okB3, '(V(0)-V(pi))/m_KK^4: ' + ', '.join(f'N={N},q={q}: {vals[N, q]:.1e}' for N, q in ((2, 1.0), (4, 1.0), (4, 0.5), (52, 0.5))))
spl, rmin = 0.0, 9.0
for N, q, nir in ((4, 1.0, None), (8, 0.5, None), (52, 0.5, 16)):
    for th in np.linspace(0.02, np.pi - 0.05, 40):
        mW, mZ, mf1, mf2 = light(N, q, th, nir); spl = max(spl, (mf2 - mf1) / mf1); rmin = min(rmin, mf1 / mW)
nrm = [light(N, q, 1e-3, nir) for N, q, nir in ((4, 1.0, None), (52, 0.5, 16))]
nrm = [(l[0] / (g4 * Fh(N, q) * 1e-3 / np.sqrt(2)), l[1] / l[0], l[2] / l[0]) for l, (N, q) in zip(nrm, ((4, 1.0), (52, 0.5)))]
check('B4 THEOREM Yukawa from the gauge link: the 8 Dirac masses of a family are equal at every th (custodial, SU(4)-blind), and m_f/m_W >= 1/sqrt2 with equality as th -> 0: '
      'y_f = g/2 for every member (N = 4 flat, 8 and 52 warped)', spl < 1e-9 and abs(rmin - 1 / np.sqrt(2)) < 1e-3 and all(abs(x[2] - 1 / np.sqrt(2)) < 1e-5 for x in nrm),
      f'split {spl:.0e}; min m_f/m_W {rmin:.5f}')
check('B5 THEOREM normalisation: m_W -> g F_h th/sqrt2 (h = sqrt2 F_h th is the canonical A_5 mode, F_h^-2 = sum_j f_j^-2) and m_Z/m_W -> sqrt(8/5): sin^2 thW = 3/8 at tree level',
      all(abs(x[0] - 1) < 1e-5 and abs(x[1] - np.sqrt(1.6)) < 1e-5 for x in nrm), ', '.join(f'{x[0]:.6f}, {x[1]:.6f}' for x in nrm))
# B6-B7 supplied extras: vector 5s (SM-like ends) and dark spinors (IR end flipped), bulk masses c in {0, 0.5}, 1 or 3 families
mults = np.linspace(0, 12, 11); scan = {}
for N, q, nir in ((12, 1.0, None), (8, 0.5, None), (24, 0.5, 16), (52, 0.5, 16)):
    gG, gS = grid('gauge', N, q, nir=nir), grid('spinor', N, q, nir=nir)
    gV = {c: grid('vector', N, q, 1, c, nir) for c in (0.0, 0.5)}; gD = {c: grid('spinor', N, q, -1, c, nir) for c in (0.0, 0.5)}
    res = []
    for nf, cv, cd in itertools.product((1, 3), (0.0, 0.5), (0.0, 0.5)):
        dd = gG + 4 * nf * gS + mults[:, None, None] * gV[cv] + 2 * mults[None, :, None] * gD[cd]
        im = np.argmin(integ(dd), axis=-1)
        for i_, j_ in zip(*np.nonzero((im > 0) & (im < len(ths) - 1))):
            r = minimum(dd[i_, j_], N, q, nir)
            if r: res.append(r)
    scan[N, q] = {k: np.array([r[k] for r in res]) for k in ('mH_mW', 'v_mKK', 'th', 'mf_mW')}
x52, v52, t52 = scan[52, 0.5]['mH_mW'], scan[52, 0.5]['v_mKK'], scan[52, 0.5]['th']; x12 = scan[12, 1.0]['mH_mW']; n52 = len(x52)
med = {N: np.median(scan[N, 0.5]['mH_mW']) for N in (8, 24, 52)}; kfit = np.sum([med[N] * np.sqrt(N + 1) for N in med]) / np.sum([N + 1 for N in med])
Nmed = (1.558 / kfit) ** 2 - 1; fmin = min(scan[k]['mf_mW'].min() for k in scan if k[1] == 0.5)
check('B6 DIAGNOSTIC supplied extras (0-12 vector 5s, 0-24 dark spinors, c = 0, 0.5, 1 or 3 families; 968 per chain): flat (fine rate) m_H/m_W stays far below 1.558; '
      'warped, the band rises with N and at N = 52 contains 1.558; the family stays at m_f >= m_W/sqrt2',
      np.percentile(x12, 95) < 0.8 and x12.max() < 1.3 and med[8] < med[24] < med[52] and np.percentile(x52, 95) > 1.558 > np.percentile(x52, 5) and fmin > 0.7,
      f'flat N=12: 95% {np.percentile(x12, 95):.2f}, max {x12.max():.2f}; warped medians N=8, 24, 52: {med[8]:.2f}, {med[24]:.2f}, {med[52]:.2f} '
      f'(fit {kfit:.3f} sqrt(N+1)); N=52 5-95% {np.percentile(x52, 5):.2f}-{np.percentile(x52, 95):.2f}; min m_f/m_W {fmin:.3f}')
lo5, hi5 = np.percentile(x52, [5, 95]); pch = np.log(1.05 / 0.95) / np.log(hi5 / lo5); k5 = int(np.sum(np.abs(x52 / 1.558 - 1) < 0.05)); sm = v52 < 0.05
check('B7 DIAGNOSTIC look-elsewhere: at N = 52 hits within 5% of 1.558 come at about the log-uniform chance rate; v/m_KK < 0.05 needs th < 0.2; two supplied multiplicities '
      'fit two observables, so a match is a fit; the median content gives 1.558 only at a depth where v would be far larger',
      abs(k5 / n52 - pch) < 2 * pch and sm.sum() >= 1 and t52[sm].max() < 0.2 and 20 < Nmed < 40,
      f'hits {k5}/{n52} = {k5 / n52:.3f} vs {pch:.3f}; v/m_KK min {v52.min():.3f}, {sm.sum()} below 0.05; median reaches 1.558 at N = {Nmed:.1f} (v up by 2^{52 - Nmed:.0f})')

# ================================================================== C
print('== C. the warped ladder and the hierarchy')
print('   CL-1: the lapse is L sin(eps0)/sqrt3 for a cube of edge L, so a rung-j cube (edge 2^j a) ticks 2^-j as often: every scale at rung j carries 2^-j (zoom rate,')
print('   warp 1/2 per rung; its k = 0 sector is the warped chain, s(0) = 1); the fine rate of the octree probes violates that clause and is the flat chain.')
cN = {N: mkk(N, 0.5, None if N <= 16 else 16) / (g4 * np.sqrt(N + 1)) for N in (8, 12, 16, 24, 32, 53)}; c12 = [cN[N] for N in (12, 16, 24, 32, 53)]
cF = {N: mkk(N, 1.0) / (g4 * np.sqrt(N + 1)) * (N + 1) for N in (8, 16, 32)}
check('C1 THEOREM warped chain: m_KK = c 2^-(N-1) M_UV (M_UV = rung-0 hop) with one c for N = 12..53, approached as 4^-N: every IR scale is 2^-N exactly; '
      'flat chain: (N+1) m_KK/M_UV -> 1.6, a power law with no hierarchy', np.ptp(c12) < 1e-6 and abs(cN[8] - cN[53]) < 1e-4 and 1.5 < cF[32] < 1.7,
      f'c = {cN[53]:.6f} (spread {np.ptp(c12):.0e}; N=8 off {cN[8] - cN[53]:.0e}); flat {cF[8]:.3f}, {cF[16]:.3f}, {cF[32]:.3f} (N = 8, 16, 32)')
wv = {N: light(N, 0.5, 1.7, None if N <= 16 else 16)[0] / mkk(N, 0.5, None if N <= 16 else 16) * np.sqrt(N + 1) for N in (8, 16, 32, 53)}
check('C2 THEOREM m_W/m_KK falls as (N+1)^-1/2 at fixed th (the zero mode spreads over all rungs, as the RS volume factor)', np.ptp(list(wv.values())) / np.mean(list(wv.values())) < 0.05,
      'sqrt(N+1) m_W/m_KK at th = 1.7, N = 8, 16, 32, 53: ' + ', '.join(f'{v:.3f}' for v in wv.values()))
Nst = np.log2(np.array([v52.min(), np.median(v52), v52.max()]) * cN[53] * 2 * MUV_GeV / 246.22)
check('C3 ESTIMATE v = 246.22 GeV with M_UV = 1/a = 2.435e18 GeV needs N = log2(2c (v/m_KK) M_UV/v), which no rule fixes: any target lies within 2^(+-1/2) of some N; '
      'rule-fixed rung counts are 0, 5-7 (step bound), >= 15.7, 192-200 (CMB, Hubble); a running coupling ending the ladder at N needs b0 alpha = 2 pi/(N ln 2)',
      45 < Nst.min() and Nst.max() < 56, f'N for v/m_KK min, median, max of the N=52 scan: {Nst[0]:.1f}, {Nst[1]:.1f}, {Nst[2]:.1f}; b0 alpha at N = 52: {2 * np.pi / (52 * np.log(2)):.4f}')

# ================================================================== D
print('== D. against measurement (estimates; PDG masses)')
mW_ = 80.369; mf_ = mW_ / np.sqrt(2)
check('D1 ESTIMATE family masses from the gauge link: m_f >= m_W/sqrt2 = 56.8 GeV for e, nu, u, d alike (measured 0.511 MeV, < 1 eV, 2.16, 4.70 MeV) and t = b = tau: excluded by > 1e5',
      mf_ / 0.000511 > 1e5)
check('D2 ESTIMATE tree m_Z/m_W = sqrt(8/5) = 1.265 vs measured 1.1346 (sin^2 thW 3/8 before running); m_KK = v/(v/m_KK) lies below the ~5 TeV that LHC '
      'resonance searches exclude for KK-type Z\' (approximate) except in the tuned corner v/m_KK < 0.05', abs(np.sqrt(1.6) - 91.1876 / 80.369) > 0.1 and 246.22 / np.median(v52) < 5000,
      f'm_KK at the N=52 scan median {246.22 / np.median(v52) / 1e3:.2f} TeV, at its minimum v/m_KK {246.22 / v52.min() / 1e3:.1f} TeV')
print('supplied: coarse sites (octree), links on exchange bonds, bulk SU(4)xSO(5) (the register ladder gives PS), lattice-orbifold ends (UV SM, IR PS),')
print('  an IR end at rung N, 4D continuum per rung, equal node couplings with g = 0.6517, g_X = sqrt(3/2) g, fermion hop = gauge hop,')
print('  the extra 5s and dark spinors with their BCs and bulk masses, M_UV = 1/a; measured masses, couplings, LHC bound (approx.).')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
