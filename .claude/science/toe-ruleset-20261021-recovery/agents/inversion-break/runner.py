#!/usr/bin/env python3
"""inversion-break: the two escapes the smg-qmc far-end theorems leave open, on the hybrid-wall ladder
(supplied models; exact theorems, finite diagnostics, estimates; no physical identification established)
 A  which register terms break the chiral inversion G' (the symmetry behind TRIM integrality, smg-qmc C5)
 B  free deleted-slot ladder with G'-breaking far-end terms: index lost, Nielsen-Ninomiya kept
 C  interactions beyond slot operators: a zero on any mode subspace S (slot, partners, copies, whole cells, rishons)
 D  exact ED, the smg-qmc 2-cell cluster with a G'-breaking term delta, and the moved-node pole theorem
 E  register constraints and reading"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm
from scipy.optimize import minimize

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))

# ---------------------------------------------------------------- 3D cube tick (octree-unify conventions)
OM = np.exp(2j * np.pi / 3); I8 = np.eye(8)
C = np.array(list(itertools.product((0, 1), repeat=3))); cc0 = C - 0.5
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        Rm = np.zeros((3, 3))
        for i in range(3): Rm[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(Rm), 1): rots.append(Rm)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def axang(Rm):
    a = np.arccos(np.clip((np.trace(Rm) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((Rm + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([Rm[2, 1] - Rm[1, 2], Rm[0, 2] - Rm[2, 0], Rm[1, 0] - Rm[0, 1]]) / (2 * np.sin(a)), a
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1: g = XI[a].conj() @ XI[b]; W[a, b] = -g / abs(g) / np.sqrt(3)
def Lrot(Rm):
    n_, a = axang(Rm); Dm = expm(-1j * a * sum(n_[k] * J3[k] for k in range(3))); L = np.zeros((8, 8), complex)
    for i in range(8): k = int(np.argmin(np.sum(abs(cc0 - Rm @ cc0[i]), 1))); L[k, i] = XI[k].conj() @ Dm @ XI[i]
    return L
def ex(th): return np.cos(th) * I8 + 1j * np.sin(th) * W
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def logH(U):
    w, V = np.linalg.eig(U); H = (V * (-np.angle(w))) @ np.linalg.inv(V); return (H + H.conj().T) / 2
class Tick:   # even cube exp(-i st W), odd cube exp(+i st W); copy mass F = exp(i M P1 W/2) on both sides
    def __init__(s, st):
        s.st, s.Ve, s.Vo = st, ex(-st), ex(st); h = 1e-5; al = []
        U0 = lambda K: Dg(K) @ ex(st) @ Dg(K).conj().T @ ex(-st)
        for a in range(3):
            e = np.zeros(3); e[a] = h; A = (logH(U0(e)) - logH(U0(-e))) / (2 * h); al.append((A + A.conj().T) / 2)
        s.v = np.sqrt(np.trace(al[0] @ al[0]).real / 8); s.al = [A / s.v for A in al]
        g5 = 1j * s.al[0] @ s.al[1] @ s.al[2]; s.g5 = (g5 + g5.conj().T) / 2; s.X = W @ (I8 - s.g5) / 2; s.Xp = W @ (I8 + s.g5) / 2
        iC3 = [i for i, Rm in enumerate(rots) if np.isclose(np.trace(Rm), 0) and np.allclose(axang(Rm)[0], np.ones(3) / np.sqrt(3))][0]
        Sig = [-1j * s.al[1] @ s.al[2], -1j * s.al[2] @ s.al[0], -1j * s.al[0] @ s.al[1]]; L3 = Lrot(rots[iC3])
        Mr = np.array([[np.trace(L3 @ s.al[a] @ L3.conj().T @ s.al[b]).real / 8 for b in range(3)] for a in range(3)]); nax, ang = axang(np.round(Mr).T)
        best = min((max(np.abs(Sx @ s.al[q] @ Sx.conj().T - L3 @ s.al[q] @ L3.conj().T).max() for q in range(3)), k, Sx) for k, Sx in
                   enumerate(expm(-1j * sgn * ang / 2 * sum(nax[k_] * Sig[k_] for k_ in range(3))) for sgn in (1, -1)))
        wr, Vr = np.linalg.eig(best[2].conj().T @ L3); Vl = Vr[:, np.abs(wr - OM) < 1e-5]; P1 = Vl @ np.linalg.pinv(Vl)
        s.P1 = (P1 + P1.conj().T) / 2; s.P2 = I8 - s.P1; s.Fc = {}; s.Hc = {}
    def U(s, K, M=0.0):
        X = Dg(K) @ s.Vo @ Dg(K).conj().T @ s.Ve
        if M:
            F = s.Fc.setdefault(M, expm(1j * M * s.P1 @ W / 2)); X = F @ X @ F
        return X
    def H(s, K, M=0.0):
        key = (tuple(np.round(np.mod(np.asarray(K, float) + np.pi, 2 * np.pi) - np.pi, 11)), M)
        if key not in s.Hc:
            if len(s.Hc) > 4000: s.Hc.clear()   # bounded cache (memory budget)
            s.Hc[key] = logH(s.U(K, M)) / s.st
        return s.Hc[key]
def s_amp(q): return np.prod((1 + np.exp(-1j * np.asarray(q))) / 2)
def tree(R, Q):   # Bloch momentum Q of the top rung; rung-j nodes (Q + 2 pi m)/2^(R-j); parent = 2q
    nodes = [(j, np.array(m), (np.asarray(Q, float) + 2 * np.pi * np.array(m)) / 2 ** (R - j)) for j in range(R + 1) for m in itertools.product(range(2 ** (R - j)), repeat=3)]
    idx = {(j, tuple(m)): i for i, (j, m, q) in enumerate(nodes)}
    return nodes, [None if j == R else idx[(j + 1, tuple(m % 2 ** (R - j - 1)))] for (j, m, q) in nodes], idx
zoom = lambda j: 2.0 ** -j; fine = lambda j: 1.0
def Hlad(tk, R, Q, kap, M, rate, Xm, keep_top=None, sparse=False):
    nodes, par, idx = tree(R, Q); n = len(nodes); r_, c_, v_ = [], [], []
    def add(i, j, B):
        rr, cc = np.nonzero(np.abs(B) > 1e-15); r_.extend(8 * i + rr); c_.extend(8 * j + cc); v_.extend(B[rr, cc])
    for i, (j, m, q) in enumerate(nodes):
        add(i, i, rate(j) * tk.H(q, M))
        if par[i] is not None:
            g = kap * np.sqrt(rate(j) * rate(j + 1)) * s_amp(q); add(i, par[i], g * Xm); add(par[i], i, np.conj(g) * Xm.conj().T)
    Hm = sp.csr_matrix((v_, (r_, c_)), shape=(8 * n,) * 2); rung = np.repeat([nd[0] for nd in nodes], 8)
    if keep_top is not None:   # delete frozen top-rung slots: H_eff = V^dag H V on the retained modes
        top = [i for i, nd in enumerate(nodes) if nd[0] == R][0]; cols = []; rr = []
        for i in range(n):
            B = keep_top if i == top else I8; rr += [nodes[i][0]] * B.shape[1]
            for k in range(B.shape[1]): v = np.zeros(8 * n, complex); v[8 * i:8 * i + 8] = B[:, k]; cols.append(v)
        Vm = sp.csr_matrix(np.array(cols).T); Hm = (Vm.conj().T @ Hm @ Vm).tocsr(); rung = np.array(rr)
    return (Hm if sparse else Hm.toarray()), rung, nodes, idx
def span(P, tol=0.5):
    w, V = np.linalg.eigh((P + P.conj().T) / 2); return V[:, w > tol], V[:, w < tol]

def Gp(R, Q, nodes, idx, keep):   # gauge-dressed chiral inversion D_phi (g5 x node inversion), restricted to retained modes
    n = len(nodes); G = np.zeros((8 * n, 8 * n), complex)
    for i, (j, m, q) in enumerate(nodes):
        k = idx[(j, tuple(np.mod(-np.array(m) - np.round(np.asarray(Q) / np.pi).astype(int), 2 ** (R - j))))]
        G[8 * k:8 * k + 8, 8 * i:8 * i + 8] = np.exp(-1j * sum(2 ** t * np.sum(nodes[k][2]) for t in range(R - j))) * g5
    top = [i for i, nd in enumerate(nodes) if nd[0] == R][0]
    blocks = [keep if i == top else I8 for i in range(n)]; Vm = np.zeros((8 * n, sum(b.shape[1] for b in blocks)), complex); c = 0
    for i, b in enumerate(blocks): Vm[8 * i:8 * i + 8, c:c + b.shape[1]] = b; c += b.shape[1]
    return Vm.conj().T @ G @ Vm

# ============================================================ A
print('== A. register terms against the chiral inversion (3D cube tick, st = 0.04; spectral test sigma(H(K)) = -sigma(H(-K)), frame-free)')
tk = Tick(0.04); g5 = tk.g5; MC = tk.st; KAP = 0.5; RR = 1; Pp = (I8 + g5) / 2; Pm = (I8 - g5) / 2
Wi = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(8):
        dd = C[a] - C[b]
        if np.sum(abs(dd)) == 1: Wi[int(np.argmax(abs(dd)))][a, b] = W[a, b]
def Rw(w):
    w = np.asarray(w, float); return sum(w[i] * np.sqrt(3) * Wi[i] for i in range(3)) / np.sqrt(np.sum(w ** 2))
def s_of(R): return 1j * np.sqrt(3) ** 3 * Wi[0] @ Wi[1] @ Wi[2] @ R
def Ugen(K, st=0.04, mu=0.0, M=0.0, w=(1, 1, 1), dP=0.0, rest=0.0, drift=0.0):   # CL-1 species tick, read literally
    R = Rw(w); P1 = (I8 - s_of(R)) / 2
    X = Dg(K) @ expm(1j * (st + mu / 2) * R) @ Dg(K).conj().T @ expm(-1j * (st - mu / 2) * R)
    F = expm(1j * M * P1 @ R / 2) @ expm(1j * dP * P1)
    return np.exp(-1j * rest - 1j * drift * np.sin(K[0])) * F @ X @ F
def asym(**kw):
    e = 0.0
    for K in np.random.default_rng(5).uniform(-np.pi, np.pi, (5, 3)):
        a = np.sort(np.angle(np.linalg.eigvals(Ugen(K, **kw)))); b = np.sort(-np.angle(np.linalg.eigvals(Ugen(-K, **kw)))); e = max(e, np.abs(a - b).max())
    return e
inv = np.zeros((8, 8))
for i in range(8): inv[int(np.argmin(np.abs(C - (1 - C[i])).sum(1))), i] = 1
G0 = np.diag([-1j * (-1) ** int(c[2]) for c in C]) @ inv; s_eq = s_of(W)
alg = max(max(np.abs(G0 @ Wi[i] @ G0.conj().T + Wi[i]).max() for i in range(3)), np.abs(G0 @ s_eq @ G0.conj().T - s_eq).max(), np.abs((I8 - s_eq) / 2 - tk.P1).max())
keep = dict(mass_angle=dict(mu=0.03), copy_mass=dict(M=0.04), metric=dict(w=(1, 1.3, 0.8)), shift=dict(drift=0.02), all=dict(mu=0.03, M=0.04, w=(1, 1.3, 0.8), drift=0.02))
brk = dict(rest_phase=dict(rest=0.02), copy_rest=dict(dP=0.02))
ak = {k: asym(**v) for k, v in keep.items()}; ab = {k: asym(**v) for k, v in brk.items()}
check("A1 THEOREM G0 W_i G0^+ = -W_i (each axis), G0 s G0^+ = s, (1 - s)/2 = P1: every CL-1 term is odd under G' (the mass angle mu, the copy "
      "mass (M/4)(1 - s)R, unequal edges, the shift); only a constant phase (rest phase = electric potential A0, or a copy-selective one "
      "d P1, i.e. s alone) breaks it, by 2 delta (spectrum shifts, not mirrored)",
      alg < 1e-9 and max(ak.values()) < 1e-12 and min(ab.values()) > 0.03,
      f"alg {alg:.0e}; kept {max(ak.values()):.0e}; broken: rest {ab['rest_phase']:.3f}, copy {ab['copy_rest']:.3f}")
errw = 0.0
for rate in (zoom, fine):
    for q in itertools.product((0, 1), repeat=3):
        Q = np.pi * np.array(q, float); H, rung, nodes, idx = Hlad(tk, 2, Q, KAP, MC, rate, tk.X); G = Gp(2, Q, nodes, idx, I8)
        errw = max(errw, np.abs(G @ H @ G + H).max())
check("A2 THEOREM the warp (zoom rate, S H_fine S with S = 2^(-j/2) rung-diagonal) and the rung tilings' offset (the dressing phase "
      "phi = -sum_t 2^t q.1) keep G' at every TRIM, R = 2, both rates: the register holds no inversion-breaking term except A0-type phases", errw < 1e-8, f'{errw:.0e}')

# ============================================================ B
print("== B. free deleted-slot ladder (R = 1, zoom, slot = P+ copy 2 deleted) + delta T on the top cell, T breaking G'")
Vs, Vk = span(Pp @ tk.P2); SZ = -1j * tk.al[0] @ tk.al[1]; SZ = (SZ + SZ.conj().T) / 2
TERMS = dict(rest=I8, copy_rest=tk.P1, axial_b0=g5, bz=SZ)
def Hds(Q, T=None, d=0.0, keep=None):
    keep = Vk if keep is None else keep; H = Hlad(tk, RR, np.asarray(Q, float), KAP, MC, zoom, tk.X, keep_top=keep)[0]
    if T is not None and d: n0 = H.shape[0] - keep.shape[1]; H = H.copy(); H[n0:, n0:] += d * (keep.conj().T @ T @ keep)
    return H
TRIM = [np.pi * np.array(q, float) for q in itertools.product((0, 1), repeat=3)]
idxl = {k: [int(np.sum(np.abs(np.linalg.eigvalsh(Hds(Q, T, 0.05))) < 1e-6)) for Q in TRIM] for k, T in TERMS.items()}
check("B1 DIAGNOSTIC delta = 0.05 (any of A0-type rest, copy rest, axial b0 g5, axial vector b_z Sigma_z): the TRIM zero modes are no "
      "longer forced; only the light (Gamma, rung 0) stays pinned", all(v[0] == 2 and sum(v[1:]) <= 2 for v in idxl.values()),
      '; '.join(f'{k} {v}' for k, v in idxl.items()))
def chern_sphere(k0, T, d, keep=None, r=0.05, nt=8, nph=16):
    Ps = {}
    for a, th in enumerate(np.linspace(0, np.pi, nt + 1)):
        for b, ph in enumerate(np.linspace(0, 2 * np.pi, nph + 1)[:-1]):
            E, V = np.linalg.eigh(Hds(k0 + r * np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)]), T, d, keep)); Ps[a, b] = V[:, E < 0]
    F = 0.0
    for a in range(nt):
        for b in range(nph):
            U = [Ps[a, b], Ps[a + 1, b], Ps[a + 1, (b + 1) % nph], Ps[a, (b + 1) % nph]]
            if any(u.shape[1] != U[0].shape[1] for u in U): return np.nan
            M_ = np.eye(U[0].shape[1], dtype=complex)
            for i in range(4): M_ = M_ @ (U[i].conj().T @ U[(i + 1) % 4])
            F += np.angle(np.linalg.det(M_))
    return F / (2 * np.pi)
def grid(T, d, keep=None, n=12):
    ks = 2 * np.pi * np.arange(n) / n; f = np.zeros((n, n, n)); nm = np.zeros((n, n, n), int)
    for a, b, c in itertools.product(range(n), repeat=3):
        E = np.linalg.eigvalsh(Hds(np.array([ks[a], ks[b], ks[c]]), T, d, keep)); f[a, b, c] = np.abs(E).min(); nm[a, b, c] = np.sum(E < 0)
    return ks, f, nm
def nodes_of(T, d, keep=None, n=12):
    ks, f, nm = grid(T, d, keep, n); out = []; rr = Hlad(tk, RR, np.zeros(3), KAP, MC, zoom, tk.X, keep_top=Vk if keep is None else keep)[1]
    for a, b, c in itertools.product(range(n), repeat=3):
        nb = [f[(a + i) % n, (b + j) % n, (c + l) % n] for i, j, l in itertools.product((-1, 0, 1), repeat=3) if (i, j, l) != (0, 0, 0)]
        if not (f[a, b, c] <= min(nb) and f[a, b, c] < 0.3): continue
        res = minimize(lambda x: np.abs(np.linalg.eigvalsh(Hds(x, T, d, keep))).min(), np.array([ks[a], ks[b], ks[c]]), method='Nelder-Mead',
                       options=dict(xatol=1e-7, fatol=1e-10, maxiter=3000))
        x = np.mod(res.x + np.pi, 2 * np.pi) - np.pi
        if res.fun < 1e-4 and not any(np.linalg.norm(np.mod(x - y[0] + np.pi, 2 * np.pi) - np.pi) < 1e-3 for y in out):
            E, V = np.linalg.eigh(Hds(x, T, d, keep)); nz = max(1, int(np.sum(np.abs(E) < 1e-5))); P = V[:, np.argsort(np.abs(E))[:nz]]
            out.append((x, chern_sphere(x, T, d, keep), float(np.sum(np.abs(P[rr == RR]) ** 2) / nz)))
    return out
NB = {d: nodes_of(SZ, d) for d in (0.0, 0.4)}
far = {d: [o for o in NB[d] if o[2] > 0.5] for d in NB}; tot = {d: sum(o[1] for o in NB[d]) for d in NB}
def line_node(d):
    kz = np.linspace(-np.pi, np.pi, 361)[1:-1]; kz = kz[np.abs(kz) > 0.02]; f = [np.abs(np.linalg.eigvalsh(Hds(np.array([0, 0, z]), SZ, d))).min() for z in kz]
    res = minimize(lambda x: np.abs(np.linalg.eigvalsh(Hds(np.array([0, 0, x[0]]), SZ, d))).min(), [kz[int(np.argmin(f))]], method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-12))
    return float(res.x[0]), float(res.fun)
LN = {d: line_node(d) for d in (0.6, 0.8, 1.5)}
chis = [round(o[1]) for o in far[0.0]] + [round(o[1]) for o in far[0.4]]
check('B2 DIAGNOSTIC b_z on the top cell moves the far-end nodes along z; X-M pairs annihilate: 7 far nodes at delta = 0 -> 1 at 0.4, '
      'net far chirality = -(light) throughout (Nielsen-Ninomiya); the last one is the mirror reborn, still at w = 0 for delta = 0.6-1.5',
      len(far[0.0]) == 7 and len(far[0.4]) == 1 and abs(tot[0.0]) < 1e-6 and abs(tot[0.4]) < 1e-6 and sum(round(o[1]) for o in far[0.4]) == sum(round(o[1]) for o in far[0.0])
      and all(v[1] < 1e-6 for v in LN.values()),
      f"far nodes {len(far[0.0])} -> {len(far[0.4])} at kz/pi = {far[0.4][0][0][2] / np.pi:+.3f} (top weight {far[0.4][0][2]:.2f}); totals {tot[0.0]:+.0e}, {tot[0.4]:+.0e}; "
      f"kz*/pi at 0.6, 0.8, 1.5: " + ', '.join(f'{v[0] / np.pi:+.3f}' for v in LN.values()))
mf = {k: float(np.mean(grid(TERMS[k], 0.3, n=8)[2] != 35)) for k in ('rest', 'copy_rest', 'axial_b0')}
mf0 = float(np.mean(grid(SZ, 0.4, n=8)[2] != 35))
check('B3 DIAGNOSTIC the rotation-scalar breakers (A0-type rest phase, copy rest phase, axial b0) at delta = 0.3 turn the far nodes into '
      'Fermi pockets (filling varies on open sets): a metallic far end, not a gapped one; b_z keeps a semimetal',
      min(mf.values()) > 0.03 and mf0 < 0.01, ', '.join(f'{k} {v:.3f}' for k, v in mf.items()) + f'; b_z {mf0:.3f} (fraction of 8^3 grid off half filling)')
print('   B4 THEOREM (inversion-free C5) any translation-invariant quadratic completion, with or without G\', has Weyl charges summing to 0 '
      '(Nielsen-Ninomiya: Berry flux of the filled bands through the torus); a light-only phase (+1 alone) has none, so the GS no-complete-'
      'interpolator statement survives every G\'-breaking term; breaking G\' only frees the compensating zeros from the 8 TRIMs')

# ============================================================ C
print('== C. beyond slot operators: interactions built from the fermion operators of ANY mode subspace S of the top cell')
print("   C1' THEOREM [c_r, H_int] = 0 for r orthogonal to S (S = slot, partners, copies, cells, rishons), so Sigma lives on S "
      'and zeros lie in S; for a zero of full rank on S at every k, Sigma_SS ~ S(k)/iw, the w = 0 poles are exactly the kernel of the S-deleted Bloch H')
def Gw(H, Ps, S, w): return np.linalg.inv(1j * w * np.eye(H.shape[0]) - H - Ps @ (S / (1j * w)) @ Ps.conj().T)
def poles(H, Ps, S, w1=1e-6):
    Z = 2 * (1j * w1 * Gw(H, Ps, S, w1)) - 1j * 2 * w1 * Gw(H, Ps, S, 2 * w1); ev = np.linalg.eigvalsh((Z + Z.conj().T) / 2); return ev[ev > 1e-6]
def full_top(Q, Sk, T=None, d=0.0):
    H = Hlad(tk, RR, np.asarray(Q, float), KAP, MC, zoom, tk.X)[0].copy(); n = H.shape[0]
    if T is not None and d: H[n - 8:, n - 8:] += d * T
    Ps = np.zeros((n, Sk.shape[1]), complex); Ps[n - 8:] = Sk; return H, Ps
SS = dict(slot=Pp @ tk.P2, P_plus=Pp, copy2=tk.P2, cell=I8)
rng = np.random.default_rng(1); rowsC = {}
for nm, P in SS.items():
    Sk, Kp = span(P); r = Sk.shape[1]; Mr_ = rng.normal(size=(r, r)) + 1j * rng.normal(size=(r, r)); Sr = Mr_ @ Mr_.conj().T + 0.3 * np.eye(r)
    pl = [len(poles(*full_top(Q, Sk), Sr)) for Q in TRIM]; kz = [int(np.sum(np.abs(np.linalg.eigvalsh(Hds(Q, keep=Kp))) < 1e-7)) for Q in TRIM]
    E, V = np.linalg.eigh(Hds(np.zeros(3), keep=Kp)); rr = Hlad(tk, RR, np.zeros(3), KAP, MC, zoom, tk.X, keep_top=Kp)[1]; z = np.abs(E) < 1e-7
    rowsC[nm] = (round(float(np.trace(Sk.conj().T @ g5 @ Sk).real)), pl, kz, round(float(np.sum(np.abs(V[rr == 0][:, z]) ** 2)), 3),
                 round(chern_sphere(np.zeros(3), None, 0.0, Kp, r=0.03)))
ok = all(v[1] == v[2] for v in rowsC.values()) and rowsC['slot'][1] == [2] * 8 and rowsC['P_plus'][1] == [4] * 8 \
     and all(rowsC[k][1][1:] == [0] * 7 and rowsC[k][1][0] == 4 and rowsC[k][3] == 4.0 and rowsC[k][4] == 0 for k in ('copy2', 'cell'))
check("C2' THEOREM-CHECK w = 0 poles of a full-rank S-zero = S-deleted kernel at all 8 TRIMs. Tr_S G' = 0 (copy 2, whole cell): the "
      'corners DO gap (C2 fails there), but Gamma gets 4 poles on the light rung with net chirality 0: the light becomes vector-like '
      '(a light-end doubler); Tr_S G\' = 4 (P+): 4 at every TRIM', ok,
      '; '.join(f'{k}: Tr {v[0]}, poles {v[1][0]}|{v[1][1]},{v[1][3]},{v[1][7]} (G,X,M,R), rung-0 weight at G {v[3]}, chi(G) {v[4]}' for k, v in rowsC.items()))
print("   C3' THEOREM (inversion-free C4) the S-deleted H is a free local Bloch H, so its Weyl charges sum to 0; if S misses the light, a local or "
      'everywhere-full-rank zero on S releases net chirality -(light), whatever S, G\' or link dressing; if S holds '
      'the light, the light gaps. Light-only needs a zero whose rank drops on a dispersing set carrying that chirality (smg-qmc C4)')

# ============================================================ D
print("== D. exact ED, the smg-qmc 2-cell cluster {Gamma, Q0} (2 flavours x Weyl slot, Z4 atom g(1 - |s><s|), d(Q0) = deleted-slot kernel, "
      "|V| = 1) plus a G'-breaking delta(n_d1 - n_d2) on each flavour's d pair; 4096 states, N mod 4 blocks")
NMd = 12; DIM = 1 << NMd; sts = np.arange(DIM)
def cop(i):
    m = ((sts >> i) & 1) == 1; s0 = sts[m]; sg = (-1.0) ** np.array([bin(int(x) & ((1 << i) - 1)).count('1') for x in s0])
    return sp.csr_matrix((sg, (s0 ^ (1 << i), s0)), shape=(DIM, DIM))
Cs = [cop(i) for i in range(NMd)]; cA, cB, cD = [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]
Nop = np.array([bin(int(x)).count('1') for x in sts]); Id = sp.identity(DIM, format='csr'); Nn = [Cs[i].T @ Cs[i] for i in range(NMd)]
def atom(cell):
    P0, PF = Id, Id
    for i in cell: P0 = P0 @ (Id - Nn[i]); PF = PF @ Nn[i]
    Od = Cs[cell[0]].T @ Cs[cell[1]].T @ Cs[cell[2]].T @ Cs[cell[3]].T
    return Id - 0.5 * (P0 + PF + Od + Od.T)
ATOM = atom(cA) + atom(cB); hc = np.zeros((NMd, NMd))
for k in range(4): hc[cA[k], cD[k]] = 1 / np.sqrt(2); hc[cB[k], cD[k]] = -1 / np.sqrt(2)
hc = hc + hc.T; HFREE = sum(hc[i, j] * (Cs[i].T @ Cs[j]) for i in range(NMd) for j in range(NMd) if hc[i, j] != 0)
DEL = Nn[8] - Nn[9] + Nn[10] - Nn[11]
def cluster(g, dl, win=0.05):
    H = (HFREE + g * ATOM + dl * DEL).tocsr(); sol = {}
    for qn in range(4):
        idx = np.where(Nop % 4 == qn)[0]; E, U = np.linalg.eigh(H[idx][:, idx].toarray().real); sol[qn] = (idx, E, U)
    E0 = min(sol[q][1][0] for q in sol); gs = [(q, k) for q in sol for k in range(len(sol[q][1])) if sol[q][1][k] < E0 + 1e-9]; wd = 0.0; lowd = 9e9
    for (q, k) in gs:
        idx, E, U = sol[q]; psi = np.zeros(DIM); psi[idx] = U[:, k]
        for sg in (1, -1):
            idq, Eq, Uq = sol[(q + sg) % 4]; dE = Eq - E0
            Amp = Uq.T @ np.array([((Cs[i].T if sg > 0 else Cs[i]) @ psi)[idq] for i in cD]).T
            wdn = (np.abs(Amp) ** 2).sum(1); wd += wdn[dE < win].sum() / 4; lowd = min(lowd, dE[wdn > 1e-3].min())
    return wd / len(gs), lowd, len(gs)
CLD = {(g, dl): cluster(g, dl) for g in (2.0, 10.0, 30.0) for dl in (0.0, 0.1, 0.3)}
check("D1 DIAGNOSTIC at fixed Q0 the delta term moves the released d pole off w = 0 (to about delta) at g = 10, 30, and at g = 2 nothing "
      'is released: in the cluster the corner looks gapped without release',
      CLD[(10.0, 0.0)][0] > 0.98 and CLD[(30.0, 0.0)][0] > 0.98 and all(CLD[(g, dl)][0] < 1e-3 for g in (10.0, 30.0) for dl in (0.1, 0.3))
      and all(abs(CLD[(30.0, dl)][1] - dl) < 0.02 for dl in (0.1, 0.3)) and all(v[2] == 1 for v in CLD.values()),
      'd weight below 0.05|V| / lowest d level: ' + '; '.join(f'g={g:g},d={dl:g}: {CLD[(g, dl)][0]:.3f}/{CLD[(g, dl)][1]:.3f}' for g in (2.0, 10.0, 30.0) for dl in (0.0, 0.1, 0.3)))
kst = np.array([0.0, 0.0, far[0.4][0][0][2]]); Sk1, _ = span(Pp @ tk.P2)
Hk, Psk = full_top(kst, Sk1, SZ, 0.4); w_, U_ = np.linalg.eigh(np.eye(Hk.shape[0]) - Psk @ Psk.conj().T); Ur = U_[:, w_ > 0.5]
er, Ue = np.linalg.eigh(Ur.conj().T @ Hk @ Ur); Kk = Ur @ Ue[:, np.abs(er) < 1e-6]; Vst = np.linalg.svd(Psk.conj().T @ Hk @ Kk, compute_uv=False)
Mr_ = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); Sr2 = Mr_ @ Mr_.conj().T + 0.3 * np.eye(2)
pk = [len(poles(Hk, Psk, S)) for S in (np.zeros((2, 2)), Sr2)]
check("D2 THEOREM-CHECK on the lattice the node has only moved: at the b_z = 0.4 far node k* the S-deleted kernel is 2-dimensional, the "
      'free ladder is gapped there (0 poles) and a full-rank slot zero gives 2 poles; the cluster is the same cluster at k* with |V(k*)|, '
      'so the release returns at g ~ 6.2|V(k*)| (smg-qmc D2): D1 is a single-k artefact',
      Kk.shape[1] == 2 and pk == [0, 2] and Vst.min() > 0.05, f'kz*/pi {kst[2] / np.pi:+.3f}; kernel {Kk.shape[1]}; poles {pk}; |V(k*)| {Vst[0]:.3f}, {Vst[1]:.3f}; onset ~ {6.2 * Vst.min():.2f}')

# ============================================================ E
print('== E. register constraints and reading')
print("   E1 (A): in-register, G' breaks only by A0-type phases, which make the far end metallic (B3); an imported b_z leaves one far Weyl "
      'node of mirror chirality per member of the 16 (B2): N_nu = 2 per family (6 vs 2.984 +- 0.008), excluded; driven onto Gamma it gaps the light')
print("   E2 (B): enlarging S evades C2 at the corners only by moving the chirality (C2', C3'); link- or rishon-dressed Spin(10) terms are "
      'S-zero interactions: same theorem. Open: a far end whose zeros disperse and carry the mirror chirality (GS); anomaly freedom is not sufficient')
print('supplied: hybrid-wall ladder (zoom, X, kap, M = st, R = 1), slot = P+ copy 2, test terms and strengths, subspaces S, the cluster '
      '(2 flavours, Z4 atom, |V| = 1, delta on d), grids 12^3/8^3, sphere r = 0.05')
print('cited: smg-qmc C1-C5/D2, hybrid-wall A1/B4-B6, smg-verify, SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY (main; 8 Weyl nodes on '
      'slot removal), Golterman-Shamir 2505.20436, Nielsen-Ninomiya')
print(f'elapsed {time.monotonic() - T0:.1f} s')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
