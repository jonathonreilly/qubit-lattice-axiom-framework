#!/usr/bin/env python3
"""CL-2 octree ladder: the tick's own fifth matrix as the rung coupling (supplied models; finite diagnostics).
 A  tick light algebra, G4 = i W g5, X = W(1-g5)/2, the tick's own K^2 Wilson term, copy projector and copy mass
 B  ladder: real space = momentum tree; H5 a partial-isometry sum, kernel = 8 per rung-0 cell; exact self-similarity
 C  chirality vs R: Berry flux on rung 0 and on the top rung; bulk gap; no light state on middle rungs
 D  where the mirror goes and how fast it decouples; residual mass; zoom (causal) rate comparison
 E  infinite ladder: unitarity, Eilenberg swindle, truncation restores the mirror, exponential support in real space
 F  against measurement (estimates)   G  large-scale index of natural starts   H  exact charges, anomaly, generations
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/OCTREE_LADDER_OF_CUBE_TICKS_GIVES_ONE_FINE_CHIRALITY_ONLY_BY_A_SWINDLE_WITH_UNBOUNDED_RANGE_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
from scipy.linalg import expm, schur

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
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
def ex(th): return np.cos(th) * I8 + 1j * np.sin(th) * W                     # exp(i th W)
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def logH(U):
    w, V = np.linalg.eig(U); H = (V * (-np.angle(w))) @ np.linalg.inv(V); return (H + H.conj().T) / 2
class Tick:   # CL-2: even cube exp(-i(st-mu/2)W), odd cube exp(+i(st+mu/2)W); copy mass F = exp(i M P1 W/2) on both sides
    def __init__(s, st, mu=0.0):
        s.st, s.Ve, s.Vo = st, ex(-(st - mu / 2)), ex(st + mu / 2); h = 1e-5; al = []
        U0 = lambda K: Dg(K) @ ex(st) @ Dg(K).conj().T @ ex(-st)
        for a in range(3):
            e = np.zeros(3); e[a] = h; A = (logH(U0(e)) - logH(U0(-e))) / (2 * h); al.append((A + A.conj().T) / 2)
        s.v = np.sqrt(np.trace(al[0] @ al[0]).real / 8); s.al = [A / s.v for A in al]
        g5 = 1j * s.al[0] @ s.al[1] @ s.al[2]; s.g5 = (g5 + g5.conj().T) / 2; s.G4 = 1j * W @ s.g5; s.X = (W + 1j * s.G4) / 2
        iC3 = [i for i, Rm in enumerate(rots) if np.isclose(np.trace(Rm), 0) and np.allclose(axang(Rm)[0], np.ones(3) / np.sqrt(3))][0]
        Sig = [-1j * s.al[1] @ s.al[2], -1j * s.al[2] @ s.al[0], -1j * s.al[0] @ s.al[1]]; L3 = Lrot(rots[iC3])
        Mr = np.array([[np.trace(L3 @ s.al[a] @ L3.conj().T @ s.al[b]).real / 8 for b in range(3)] for a in range(3)]); nax, ang = axang(np.round(Mr).T)
        best = min((max(np.abs(Sx @ s.al[q] @ Sx.conj().T - L3 @ s.al[q] @ L3.conj().T).max() for q in range(3)), k, Sx) for k, Sx in
                   enumerate(expm(-1j * sgn * ang / 2 * sum(nax[k_] * Sig[k_] for k_ in range(3))) for sgn in (1, -1)))
        wr, Vr = np.linalg.eig(best[2].conj().T @ L3); Vl = Vr[:, np.abs(wr - OM) < 1e-5]; P1 = Vl @ np.linalg.pinv(Vl)
        s.P1 = (P1 + P1.conj().T) / 2; s.P2 = I8 - s.P1; s.Fc = {}
    def U(s, K, M=0.0):
        X = Dg(K) @ s.Vo @ Dg(K).conj().T @ s.Ve
        if M:
            F = s.Fc.setdefault(M, expm(1j * M * s.P1 @ W / 2)); X = F @ X @ F
        return X
    def H(s, K, M=0.0): return logH(s.U(K, M)) / s.st
def s_amp(q): return np.prod((1 + np.exp(-1j * np.asarray(q))) / 2)          # corner-preserving split, Bloch amplitude
def tree(R, Q):   # supercell = one rung-R cell; rung-j nodes = cell momenta (Q + 2 pi m)/2^(R-j); parent = 2q
    nodes = [(j, np.array(m), (np.asarray(Q, float) + 2 * np.pi * np.array(m)) / 2 ** (R - j)) for j in range(R + 1) for m in itertools.product(range(2 ** (R - j)), repeat=3)]
    idx = {(j, tuple(m)): i for i, (j, m, q) in enumerate(nodes)}
    return nodes, [None if j == R else idx[(j + 1, tuple(m % 2 ** (R - j - 1)))] for (j, m, q) in nodes]
def Hlad(tk, R, Q, kap=0.5, M=0.0, rate=lambda j: 1.0, sparse=False, onlyH5=False):
    nodes, par = tree(R, Q); r_, c_, v_ = [], [], []
    def add(i, j, B):
        rr, cc = np.nonzero(np.abs(B) > 1e-15); r_.extend(8 * i + rr); c_.extend(8 * j + cc); v_.extend(B[rr, cc])
    for i, (j, m, q) in enumerate(nodes):
        if not onlyH5: add(i, i, rate(j) * tk.H(q, M))
        if par[i] is not None:
            g = 1.0 if onlyH5 else kap * np.sqrt(rate(j) * rate(j + 1)); sa = s_amp(q); add(i, par[i], g * sa * tk.X); add(par[i], i, g * np.conj(sa) * tk.X.conj().T)
    Hm = sp.csr_matrix((v_, (r_, c_)), shape=(8 * len(nodes),) * 2); Hm.sum_duplicates()
    return (Hm if sparse else Hm.toarray()), np.repeat([nd[0] for nd in nodes], 8), nodes
def flux(fun, rad, nt=6, nph=12):
    th = np.linspace(0, np.pi, nt + 1); pp = np.linspace(0, 2 * np.pi, nph + 1)[:-1]; V = {}; dims = set()
    for i, t in enumerate(th):
        for k, p in enumerate(pp): V[i, k] = fun(rad * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])); dims.add(V[i, k].shape[1])
    F = sum(np.angle(np.linalg.det(V[i, k].conj().T @ V[i + 1, k]) * np.linalg.det(V[i + 1, k].conj().T @ V[i + 1, (k + 1) % nph])
                     * np.linalg.det(V[i + 1, (k + 1) % nph].conj().T @ V[i, (k + 1) % nph]) * np.linalg.det(V[i, (k + 1) % nph].conj().T @ V[i, k])) for i in range(nt) for k in range(nph))
    return float(round(F / (2 * np.pi), 3)), dims
def select(E, V, rung, target, lo, hi):
    Vs, _ = np.linalg.qr(V[:, (E > lo) & (E < hi)]); e, U = np.linalg.eigh(Vs[rung == target].conj().T @ Vs[rung == target]); return Vs @ U[:, e > 0.5]
def lowest(Hm, k):
    E, V = eigsh(Hm, k=k, sigma=0.0, which='LM') if sp.issparse(Hm) else np.linalg.eigh(Hm); V, _ = np.linalg.qr(V); return E, V
wt = lambda V, mask: np.array([np.sum(np.abs(V[mask, i]) ** 2) for i in range(V.shape[1])])

# ============================================================ A
print('== A. CL-2 tick (st = 0.04): light algebra, fifth matrix, Wilson term, copies')
tk = Tick(0.04); MC = tk.st; KAP = 0.5; v = tk.v / tk.st; al, g5, G4, X = tk.al, tk.g5, tk.G4, tk.X
hh = 1e-5
Bm = (logH(Dg(np.zeros(3)) @ ex(tk.st + hh / 2) @ ex(-(tk.st - hh / 2))) - logH(Dg(np.zeros(3)) @ ex(tk.st - hh / 2) @ ex(-(tk.st + hh / 2)))) / (2 * hh)
e1 = max(np.abs(al[a] @ al[b] + al[b] @ al[a] - 2 * (a == b) * I8).max() for a in range(3) for b in range(3))
e2 = max(np.abs(np.abs(g5 @ g5 - I8)).max(), np.abs(G4 @ G4 - I8).max(), np.abs(Bm + W).max(), max(np.abs(G4 @ A + A @ G4).max() + np.abs(g5 @ A - A @ g5).max() for A in al),
         np.abs(G4 @ W + W @ G4).max(), np.abs(g5 @ W + W @ g5).max())
e3 = max(np.abs(X @ X).max(), np.abs(X @ X.conj().T - (I8 + g5) / 2).max(), np.abs(X.conj().T @ X - (I8 - g5) / 2).max())
check('A1 THEOREM light algebra a_i, mass -W, g5 = i a1a2a3; G4 = i W g5 anticommutes with a_i and W (fifth matrix); '
      'X = (W + iG4)/2 = W(1-g5)/2: X^2 = 0, XX+ = P+, X+X = P-', max(e1, e2, e3) < 1e-7, f'errors {e1:.0e}, {e2:.0e}, {e3:.0e}; v = sin(st)/sqrt3 = {tk.v:.5f}')
cw, rs = [], []
for d in (np.array([1., 0, 0]), np.array([1., 1, 1]) / np.sqrt(3), np.array([.3, .5, .81]) / np.linalg.norm([.3, .5, .81])):
    ev = (tk.H(0.003 * d) + tk.H(-0.003 * d)) / 2 / 0.003 ** 2; ev = (ev + ev.conj().T) / 2
    c0 = np.trace(W @ ev).real / 8; Rr = ev - c0 * W; cw.append(c0)
    rs.append((np.abs(ev + g5 @ ev @ g5).max(), np.abs(Rr @ W + W @ Rr).max(), np.abs(tk.P1 @ Rr @ tk.P1).max() + np.abs(tk.P2 @ Rr @ tk.P2).max(), np.abs(Rr).max()))
check('A2 the tick\'s K^2 term is chirality-odd: (K^2/6) W, an isotropic Wilson mass, plus a copy-mixing quadrupole zero along (1,1,1)', max(r[0] for r in rs) < 1e-4 and max(r[1] + r[2] for r in rs) < 1e-4 and rs[1][3] < 1e-4 and np.ptp(cw) < 1e-4 and abs(cw[0] - 1 / 6) < 2e-3,
      f'W coefficient {cw[0]:.4f}, spread {np.ptp(cw):.0e}')
H0 = tk.H(np.zeros(3), MC)
check('A3 the copy projector commutes with W, a_i, g5; CL-2\'s copy mass is the Dirac mass -M P1 W on copy 1',
      max(np.abs(tk.P1 @ Y - Y @ tk.P1).max() for Y in al + [W, g5]) < 1e-7 and np.abs(H0 + (MC / tk.st) * tk.P1 @ W).max() < 1e-8)

# ============================================================ B
print('== B. the ladder: rung-j cells tick at the fine rate; each cell exchanges with the same corner of its 8 children via X')
def rs_ladder():   # real space, R = 1: rung-1 torus 2^3 cells, rung 0 4^3 cells
    def tickrs(L):
        N = L ** 3; sx = lambda x: int(((x[0] % L) * L + x[1] % L) * L + x[2] % L); Ue = np.zeros((N, N), complex); Uo = np.zeros((N, N), complex)
        for n in itertools.product(range(L // 2), repeat=3):
            ids = [sx(2 * np.array(n) + a) for a in C]; Ue[np.ix_(ids, ids)] = tk.Ve
            ids = [sx(2 * np.array(n) + 1 + cp) for cp in C]; lab = [int(np.argmin(np.abs(C - (1 - cp)).sum(1))) for cp in C]; Uo[np.ix_(ids, ids)] = tk.Vo[np.ix_(lab, lab)]
        return Uo @ Ue
    Lc = 4; Lf = 8; sc = lambda x, L: int(((x[0] % L) * L + x[1] % L) * L + x[2] % L); SX = np.zeros((Lf ** 3, Lc ** 3), complex)
    for n in itertools.product(range(Lc // 2), repeat=3):
        for ib, b in enumerate(C):
            for ia, a in enumerate(C):
                for c in C: SX[sc(2 * (2 * np.array(n) + c) + a, Lf), sc(2 * np.array(n) + b, Lc)] += X[ia, ib] / np.sqrt(8)
    N0, N1 = Lf ** 3, Lc ** 3; H5 = np.zeros((N0 + N1,) * 2, complex); H5[:N0, N0:] = SX; H5[N0:, :N0] = SX.conj().T
    Ut = np.zeros_like(H5); Ut[:N0, :N0] = tickrs(Lf); Ut[N0:, N0:] = tickrs(Lc); return H5, Ut
H5r, Utr = rs_ladder(); tau = KAP * tk.st
ev_rs = np.sort(np.angle(np.linalg.eigvals(expm(-1j * tau * H5r) @ Utr)))
def Ufl(R, Q, M=0.0):
    nodes, _ = tree(R, Q); return expm(-1j * tau * Hlad(tk, R, Q, onlyH5=True)[0]) @ sp.block_diag([tk.U(nd[2], M) for nd in nodes]).toarray()
ev_k = np.sort(np.concatenate([np.angle(np.linalg.eigvals(Ufl(1, np.pi * np.array(mq)))) for mq in itertools.product(range(2), repeat=3)]))
ker = int(np.sum(np.abs(np.linalg.eigvalsh(H5r)) < 1e-9)); H5k = Hlad(tk, 2, np.array([.4, -1.1, 2.3]), onlyH5=True)[0]
kerk = int(np.sum(np.abs(np.linalg.eigvalsh(H5k)) < 1e-9))
check('B1 THEOREM real space (576 modes) = momentum tree; H5 = T + T+, T an isometry (j+1,P-) -> (j,P+): H5^3 = H5, '
      'ker H5 = 8 per rung-0 cell for every R',
      np.abs(ev_rs - ev_k).max() < 1e-12 and np.abs(H5r @ H5r @ H5r - H5r).max() < 1e-8 and ker == 512 and kerk == 512,
      f'spectra {np.abs(ev_rs - ev_k).max():.0e}; ker {ker} (R=1), {kerk} (R=2) = 8 x 64')
Qg = np.array([0.3, -0.7, 1.1]); sss = []
for R in (2, 3):
    Ha, ra, _ = Hlad(tk, R, Qg, KAP, MC, sparse=True); Hb, rb, _ = Hlad(tk, R - 1, Qg, KAP, MC, sparse=True); s_ = np.where(ra >= 1)[0]
    sss.append(abs(Ha[s_][:, s_] - Hb).max())
check('B2 THEOREM self-similarity: the ladder above rung 1 is the ladder on a lattice twice as coarse',
      max(sss) == 0, f'max |H(R)[rungs>=1] - H(R-1)| = {float(max(sss)):.0e} (R = 2, 3)')

# ============================================================ C
print('== C. chirality on the fine lattice vs number of rungs R (kap = 0.5, copy mass M = st)')
RHO = 0.04
def fluxes(R, M=MC, nt=6, nph=12, top=True):
    def f(q, target, lo, hi):
        Hm, rung, _ = Hlad(tk, R, q * 2 ** R, KAP, M, sparse=R > 1); E, V = lowest(Hm, 10); return select(E, V, rung, target, lo, hi)
    e0 = 0.6 * v * RHO * 2 ** R
    return flux(lambda q: f(q, 0, 0, e0), RHO, nt, nph)[0], (flux(lambda q: f(q, R, e0, 0.3), RHO, nt, nph)[0] if top else None)
f10 = fluxes(1, 0.0); f1 = fluxes(1); f2 = fluxes(2); f3 = fluxes(3, nt=4, nph=8, top=False)
def ffl(q, target, lo, hi):
    U = Ufl(1, q * 2, MC); rung = np.repeat([0] * 8 + [1], 8); T_, Z = schur(U, output='complex'); return select(-np.angle(np.diag(T_)), Z, rung, target, lo, hi)
wf = 0.6 * tk.v * RHO * 2; ff = (flux(lambda q: ffl(q, 0, 0, wf), RHO)[0], flux(lambda q: ffl(q, 1, wf, 0.3 * tk.st), RHO)[0])
check('C1 Berry flux (rung 0, top): (+2,-2) without the copy mass; with it (+1,-1) for R = 1, 2, +1 on rung 0 for R = 3, '
      'and (+1,-1) for the discrete-time ladder', f10 == (2, -2) and f1 == (1, -1) and f2 == (1, -1) and f3[0] == 1 and ff == (1, -1),
      f'M=0 {f10}; R=1 {f1}; R=2 {f2}; R=3 {f3[0]:+}; Floquet {ff}')
gaps, tops, bnd = [], [], []
for R in (1, 2, 3):
    Hm, rung, _ = Hlad(tk, R, np.array([.03, .05, .08]) * 2 ** R, KAP, MC, sparse=True); E, V = lowest(Hm, 24)
    w0, wT = wt(V, rung == 0), wt(V, rung == R); bulk = (w0 < .5) & (wT < .5); g_ = np.abs(E[bulk]).min() if bulk.any() else np.inf
    gaps.append(g_); bnd.append(np.sort(np.abs(E[w0 > .5]))[0]); tt = np.abs(E[(wT > .5) & (np.abs(E) < g_)]); tops.append(tt.min() if tt.size else None)
rng = np.random.default_rng(5); mid = 0.0
for Q in rng.uniform(-np.pi, np.pi, (16, 3)):
    Hm, rung, _ = Hlad(tk, 2, Q, KAP, MC); E, V = np.linalg.eigh(Hm); s_ = np.abs(E) < 0.25
    if s_.any(): mid = max(mid, wt(V[:, s_], rung == 1).max())
check('C2 bulk gap ~0.4 st for every R; no state below 0.25 st on a middle rung (16 random Q); at fixed momentum the '
      'mirror\'s energy is 2^R times the boundary\'s, so it leaves the light window',
      min(gaps[1:]) > 0.35 and mid < 0.01 and abs(tops[0] / bnd[0] - 2) < 0.1 and abs(tops[1] / bnd[1] - 4) < 0.2 and tops[2] is None and 8 * bnd[2] > gaps[2],
      f'bulk gap {gaps[1]:.3f}, {gaps[2]:.3f}; middle-rung weight {mid:.1e}; mirror/boundary energy {tops[0]/bnd[0]:.2f} (R=1), {tops[1]/bnd[1]:.2f} (R=2), above the gap (R=3)')

# ============================================================ D
print('== D. where the mirror goes, and how fast it decouples')
d = np.array([.3, .5, .81]); d /= np.linalg.norm(d); tw, mw, ml = [], [], []
for R in (1, 2, 3):
    Hm, rung, nodes = Hlad(tk, R, 0.5 * d, KAP, MC, sparse=True); E, V = lowest(Hm, 8); w0, wT = wt(V, rung == 0), wt(V, rung == R)
    i0 = [k for k, nd in enumerate(nodes) if nd[0] == 0 and not nd[1].any()][0]; mi = np.argmax(wT * (np.abs(E) > 0.25 * v))
    tw.append(wT[np.argmax(w0)]); mw.append(w0[mi]); ml.append(np.sum(np.abs(V[8 * i0:8 * i0 + 8, mi]) ** 2))
pred = [(0.25 / (6 * KAP)) ** (2 * R) * 4.0 ** (-R * (R + 1)) for R in (1, 2, 3)]
check('D1 at |q_R| = 0.5 the rung-0 Weyl state\'s top weight ~ (q_R^2/6kap)^2R 4^-R(R+1); the mirror\'s weight on the '
      'light rung-0 node falls as fast, its off-shell weight more slowly',
      all(0.3 < a / b < 1.2 for a, b in zip(tw, pred)) and ml[2] / ml[1] < 1e-2 and mw[2] < mw[1] < mw[0],
      f'{", ".join(f"{x:.1e}" for x in tw)} (pred {", ".join(f"{x:.1e}" for x in pred)}); mirror: '
      f'{", ".join(f"{x:.0e}" for x in ml)}; all rung 0 {", ".join(f"{x:.0e}" for x in mw)}')
def chain(R, mu_n):     # exact Q = 0 problem: the m = 0 chain decouples (s(pi m) = 0 for m != 0)
    tkm = Tick(0.04, mu_n * 0.04) if mu_n else tk; H0 = tkm.H(np.zeros(3), MC); n = R + 1; Hc = np.zeros((8 * n,) * 2, complex)
    for j in range(n):
        Hc[8 * j:8 * j + 8, 8 * j:8 * j + 8] = H0
        if j + 1 < n: Hc[8 * j:8 * j + 8, 8 * j + 8:8 * j + 16] = KAP * tkm.X; Hc[8 * j + 8:8 * j + 16, 8 * j:8 * j + 8] = KAP * tkm.X.conj().T
    return np.sort(np.abs(np.linalg.eigvalsh(Hc)))[0]
z0 = max(chain(R, 0) for R in (1, 4, 16)); mres = [chain(R, 0.2) for R in range(2, 9)]; ratio = np.exp(np.polyfit(range(2, 9), np.log(mres), 1)[0])
check('D2 THEOREM at zero momentum the light chain decouples; with mu = 0 boundary and mirror are exact zero modes for every R; '
      'a species mass mu leaves a residual mass falling by mu/(kap st) per rung',
      abs(s_amp(np.pi * np.array([1, 0, 1]))) < 1e-15 and z0 < 1e-9 and abs(ratio - 0.4) < 2e-3,
      f'|E| (mu=0, R=1,4,16) < {z0:.0e}; mu = 0.2 st: m_res(R=2..8) {mres[0]:.1e} .. {mres[-1]:.1e}, ratio {ratio:.4f}')
Qz = np.array([.03, .05, .08]) * 8; byz, byf = [], []
for rate, out in ((lambda j: 2.0 ** -j, byz), (lambda j: 1.0, byf)):
    Hm, rung, _ = Hlad(tk, 3, Qz, KAP, MC, rate=rate, sparse=True); E, V = lowest(Hm, 30); s_ = np.abs(E) < 0.1
    out.extend(np.round([np.sum(np.abs(V[rung == j][:, s_]) ** 2) for j in range(4)], 2))
check('D3 DIAGNOSTIC at the causal (zoom) rate 2^-j the mirror stays light on the coarse rungs; only the fine rate removes it', byz[0] > 1.9 and byz[2] + byz[3] > 1.9 and byf[0] > 1.9 and sum(byf[1:]) < 0.05,
      f'|E| < 0.1 weight by rung: zoom {[float(x) for x in byz]}, fine {[float(x) for x in byf]}')

# ============================================================ E
print('== E. infinitely many rungs')
check('E1 THEOREM |H5| = 1 and exp(-i tau H5) = 1 - i sin(tau) H5 + (cos tau - 1) H5^2: with block-unitary rung ticks the ladder is '
      'unitary for any number of rungs, infinitely many included (a quasi-free automorphism)',
      abs(np.linalg.norm(H5k, 2) - 1) < 1e-7 and np.abs(expm(-1j * tau * H5k) - (np.eye(len(H5k)) - 1j * np.sin(tau) * H5k + (np.cos(tau) - 1) * H5k @ H5k)).max() < 1e-7)
L1 = 2 ** 12; sizes = [L1 >> j for j in range(13)]; off = np.cumsum([0] + sizes[:-1]); NN = sum(sizes)
def Qlay(j):
    p = np.arange(sizes[j + 1]); return [np.stack([off[j + 1] + p, off[j] + (2 * p + k) % sizes[j]], 1) for k in (0, 1, 2)]
def swaps(perm, pr): a, b = pr[:, 0], pr[:, 1]; t = perm[a].copy(); perm[a] = perm[b]; perm[b] = t
def circuit(top):
    perm = np.arange(NN)
    for par in (0, 1):
        lays = [[], [], []]
        for j in range(par, top, 2):
            for k, l in enumerate(Qlay(j)): lays[k].append(l)
        for l in lays:
            if l: swaps(perm, np.concatenate(l))
    out = []
    for j in range(len(sizes)):
        vals = {int((perm[off[j] + i] - off[j] - i) % sizes[j]) for i in range(sizes[j])}
        out.append(vals.pop() if len(vals) == 1 else None)
    return out
sh_full, sh_cut = circuit(12), circuit(2)
check('E2 THEOREM (swindle) three cell-child swap layers = Shift_j x Shift_j+1^-1; the depth-6 circuit is Shift_0 (+) 1 (no mirror on '
      'any finite rung); stopped at rung 2 (bounded range) Shift_2^-1 returns on the cut rung', sh_full[0] == sizes[0] - 1 and all(x == 0 for x in sh_full[1:]) and sh_cut[0] == sizes[0] - 1 and sh_cut[1] == 0 and sh_cut[2] == 1,
      f'shifts by rung {sh_full[:4]}..; stopped {sh_cut[:4]}')
ST3 = 0.3; tk3 = Tick(ST3); F3 = expm(1j * ST3 * tk3.P1 @ W / 2); tau3 = KAP * ST3; X3 = tk3.X; Xd3 = X3.conj().T
csh = [tuple(int(1 - x) for x in a) for a in C]
def tick_rs(p):
    p = p @ F3.T @ tk3.Ve.T; G_ = np.empty_like(p)
    for a in range(8): G_[..., a] = np.roll(p[..., a], tuple(-s for s in csh[a]), (0, 1, 2))
    G_ = G_ @ tk3.Vo.T
    for a in range(8): p[..., a] = np.roll(G_[..., a], csh[a], (0, 1, 2))
    return p @ F3.T
def H5_rs(ps):
    out = [np.zeros_like(x) for x in ps]
    for j in range(len(ps) - 1):
        m_ = ps[j + 1].shape[0]; out[j].reshape(m_, 2, m_, 2, m_, 2, 8)[...] += (ps[j + 1] @ X3.T / np.sqrt(8))[:, None, :, None, :, None, :]
        out[j + 1] += ps[j].reshape(m_, 2, m_, 2, m_, 2, 8).sum(axis=(1, 3, 5)) @ Xd3.T / np.sqrt(8)
    return out
def step(ps):
    ps = [tick_rs(p) for p in ps]; h1 = H5_rs(ps); h2 = H5_rs(h1); return [p - 1j * np.sin(tau3) * a + (np.cos(tau3) - 1) * b for p, a, b in zip(ps, h1, h2)]
n0 = 16; shp = [(n0 >> j,) * 3 + (8,) for j in range(4)]
ax = np.arange(n0)[:, None] * 2 + np.array([0, 1])[None, :]; dd_ = np.minimum(np.abs(ax - 16), 32 - np.abs(ax - 16))
Dst = np.zeros(shp[0])
for i in range(8): Dst[..., i] = np.maximum(np.maximum(dd_[:, C[i][0]][:, None, None], dd_[:, C[i][1]][None, :, None]), dd_[:, C[i][2]][None, None, :])
u = np.linalg.svd((I8 - tk3.g5) / 2 @ tk3.P2)[0][:, 0]
def propagate(src, rad, T):
    ps = [np.zeros(s, complex) for s in shp]; ps[0] = src / np.linalg.norm(src); out = []
    for t in range(1, T + 1):
        ps = step(ps); P0 = np.abs(ps[0]) ** 2; out.append((P0[Dst > rad + 2 * t].sum(), Dst[P0 > 1e-28].max(), sum(np.sum(np.abs(p) ** 2) for p in ps)))
    return out
s1 = np.zeros(shp[0], complex); s1[8, 8, 8] = u; pd = propagate(s1, 1, 3)
rr = np.sqrt(np.sum((np.stack(np.meshgrid(*(np.arange(n0),) * 3, indexing='ij'), -1) - 8.0) ** 2, -1))
s2 = np.where(rr < 3, np.cos(np.pi * rr / 6) ** 2, 0)[..., None] * u; pb = propagate(s2, 7, 3)
check('E3 DIAGNOSTIC real space (st = 0.3, R = 3, 32^3 sites): support grows 4 sites per tick against the rung-0 cone\'s 2; '
      'probability lands beyond that cone, much less from a smooth source',
      abs(pd[-1][2] - 1) < 1e-12 and [x[1] for x in pd] == [4, 8, 12] and min(x[0] for x in pd) > 1e-9 and max(x[0] for x in pb) < 1e-2 * min(x[0] for x in pd[:2]),
      f'one cell {", ".join(f"{x[0]:.0e}" for x in pd)}; bump {", ".join(f"{x[0]:.0e}" for x in pb)}')

# ============================================================ F
print('== F. against measurement (estimates; a = sqrt(8 pi) l_P, E_a = 2.435e18 GeV)')
adm, dev = [], []
for q0 in (0.01, 0.02):
    for dd2 in (np.array([1., 0, 0]), d):
        Hm, rung, _ = Hlad(tk, 2, q0 * 4 * dd2, KAP, MC, sparse=True); E, V = lowest(Hm, 6); w0 = wt(V, rung == 0); i = np.argmax(w0 * (E > 0))
        eb = np.linalg.eigvalsh(tk.H(q0 * dd2, MC)); adm.append((1 - w0[i]) / q0 ** 4); dev.append((E[i] - np.sort(eb[eb > 0])[0]) / (v * q0 ** 3))
check('F1 rung-1 admixture of the Weyl state = (q^2/6kap)^2 (q = 2ka), isotropic; its band is slower than the bare band by '
      'q^2/(72 v^2): dv/v = -(ka)^2/2', np.allclose(adm, 1 / (36 * KAP ** 2), rtol=0.02) and np.allclose(dev, -1 / (72 * v ** 2), rtol=0.02),
      f'adm/q^4 {min(adm):.4f}-{max(adm):.4f} (1/9); shift/q^2 {min(dev):.4f}-{max(dev):.4f} ({-1/(72*v**2):.4f})')
Ea, me = 1.22089e19 / np.sqrt(8 * np.pi), 0.51099895e-3; ka = 1.4e6 / Ea
EQG2 = np.sqrt(2) * Ea; Eth = 2 * np.sqrt(me * Ea)
check('F2 ESTIMATE 1.4 PeV: admixture %.0e, dv/v = -%.1e (no vacuum Cherenkov); E_QG,2 = %.1e GeV vs GRB 221009A > 7.3e11, '
      'PeV-photon decay > ~1e16; a bare-band photon decays to e+e- above %.0f PeV (untested)' % ((2 * ka) ** 4 / (36 * KAP ** 2), ka ** 2 / 2, EQG2, Eth / 1e6),
      EQG2 > 1e2 * 1.2e16 and (2 * ka) ** 4 / (36 * KAP ** 2) < 1e-40 and Eth > 1.4e6)
check('F3 ESTIMATE the slab mirror moves at 2^R v with density 8^-R: a thermal mirror adds dN_eff < 0.02 for R >= 2; none if unbounded', 1.04 * 8.0 ** -2 < 0.02)

# ============================================================ G
print('== G. large-scale index of natural starts (T3 premise: strict cone, broken here)')
Ns = 10; L0 = 4 * Ns; grid = 2 * np.pi * np.arange(Ns) / Ns; GQ = {}
for iq in itertools.product(range(Ns), repeat=3):
    Hm, rung, _ = Hlad(tk, 1, grid[list(iq)], KAP, MC); E, V = np.linalg.eigh(Hm); Vo = V[:, E < 0]; GQ[iq] = (Vo @ Vo.conj().T).T.astype(np.complex64)
ml_ = list(itertools.product(range(2), repeat=3)); mid_ = {m: i for i, m in enumerate(ml_)}
def Sp(n, which):
    p = 2 * np.pi * np.array([n, 0, 0]) / L0; Ph = np.concatenate([np.tile(np.exp(-1j * (C @ p)), 8), np.exp(-2j * (C @ p)) * (which == 'all')]); tot = occ = 0.0
    for iq, A in GQ.items():
        A = A.astype(complex); occ += np.real(np.sum(np.abs(Ph) ** 2 * np.diag(A))); s_ = np.array(iq) + np.array([n, 0, 0]); ell = s_ // Ns
        idx = np.concatenate([8 * mid_[tuple((np.array(m) + ell) % 2)] + np.arange(8) for m in ml_] + [64 + np.arange(8)])
        tot += np.real(np.sum((Ph[:, None] * A * Ph.conj()[None, :]) * GQ[tuple(s_ % Ns)].astype(complex)[np.ix_(idx, idx)].T))
    return (occ - tot) / L0 ** 3
S0r = [Sp(n, 'r0') for n in (1, 2, 3)]; Sal = [Sp(n, 'all') for n in (1, 2, 3)]
i0r, ial = np.log(S0r[1] / S0r[0]) / np.log(2), np.log(Sal[1] / Sal[0]) / np.log(2); floor = S0r[0] - (S0r[1] - S0r[0]) / 3
check('G1 ladder sea, 40^3 sites: rung-0 density has a white floor (rung-0 number trades with rung 1): index -> 0; all-rung '
      'density (N exact): index 2; a white start stays white (rho ~ 1 invariant): 0',
      floor > 1e-3 and i0r < 1.3 and abs(ial - 2) < 0.15, f'rung 0: {i0r:.2f}, floor {floor:.1e}; all: {ial:.2f}; 0.965 is 230/246 sigma from 0/2')
print('   counting: a rung-j cell is shared by 8^j sites, so tree-carried correlations give at most |p|^3 (|p|^1 in 1D)')

# ============================================================ H
print('== H. charges and content')
gens = [tk.H(q, MC) for q in np.random.default_rng(3).uniform(-np.pi, np.pi, (6, 3))] + [X, X.conj().T]
cdim = int(np.sum(np.linalg.svd(np.vstack([np.kron(g_, I8) - np.kron(I8, g_.T) for g_ in gens]), compute_uv=False) < 1e-8))
rate = 0.1973 * 59.2 / (4 * np.pi ** 2) * 1.977e35
check('H1 the commutant of the ladder blocks is the identity: N is the one exact charge, and the rung-0 lattice carries one '
      'light Weyl field of one handedness, so N has sum q^3 = 1 (anomalous)',
      cdim == 1 and f1[0] == 1, f'commutant dim {cdim}')
check('H2 ESTIMATE a link on N would drain rung-0 charge at %.0e m^-3 s^-1 in 1 MV/m parallel to 1 T: excluded by vector-like QED; '
      'a link needs a wall orientation tied to an exact charge (none supplied)' % rate, rate > 1e30)
check('H3 generations: the rung-0 count is the bulk invariant, 1 (2 without copy mass), never 3',
      f1[0] == 1 and f10[0] == 2)
print('supplied: octree sites, split, fine rate, X = W(1-g5)/2 (dimerized), kap = 0.5, M = st > kap st, st; measured inputs; cited GNVW.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
