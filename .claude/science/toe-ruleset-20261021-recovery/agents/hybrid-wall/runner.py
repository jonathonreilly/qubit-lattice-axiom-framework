#!/usr/bin/env python3
"""hybrid-wall: the octree ladder at the zoom rate (rung j ticks at 2^-j) with the Spin(10) pair square on the top rung only
(supplied models; exact theorems, finite diagnostics, estimates against measurement; no physical identification established).
 A  zoom-rate ladder (3D cube tick, copy mass, exchange X, the 16 in parallel): chiral inversion, congruence, where light/mirror sit
 B  pair square on the mirror end: one-cell singlet, exact light protection, strong-coupling endpoint, TRIM index, the 7 doublers
 C  1+1D analogue: endpoint compensator, exact interacting ED of a two-cell top ring (zeros vs poles), the 0D end
 D  measured constraints at the zoom rate: power counting, rung-local magnetic recursion, estimates"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from fractions import Fraction as Fr
from functools import reduce
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
from scipy.linalg import expm, eigvalsh

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
        if key not in s.Hc: s.Hc[key] = logH(s.U(K, M)) / s.st
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

# ============================================================ A
print('== A. zoom-rate ladder (3D tick st = 0.04, copy mass M = st, kap = 0.5, X = W(1-g5)/2; the 16 in parallel)')
tk = Tick(0.04); MC = tk.st; KAP = 0.5; v = tk.v / tk.st; g5 = tk.g5; Pp = (I8 + g5) / 2; X = tk.X
inv = np.zeros((8, 8))
for i in range(8): inv[int(np.argmin(np.abs(C - (1 - C[i])).sum(1))), i] = 1
G0 = np.diag([-1j * (-1) ** int(c[2]) for c in C]) @ inv; g5x = expm(1j * tk.st * W) @ G0
rng = np.random.default_rng(2)
e1 = max(np.abs(G0 @ W @ G0.conj().T + W).max(), max(np.abs(G0 @ Dg(K) @ G0.conj().T - np.exp(1j * K.sum()) * Dg(-K)).max() for K in rng.uniform(-3, 3, (3, 3))))
e2 = max(np.abs(g5x @ tk.U(K, M) @ g5x - tk.U(-K, M).conj().T).max() for K in rng.uniform(-np.pi, np.pi, (4, 3)) for M in (0.0, MC))
check('A1 THEOREM chiral inversion: G0 = -i(-1)^cz x (cube inversion) has G0 W G0^+ = -W, G0 Dg(K) G0^+ = e^{iK.1} Dg(-K); '
      'g5 = e^{i st W} G0 then gives g5 U(K) g5 = U(-K)^+ (copy mass included): g5 H(K) g5 = -H(-K)',
      e1 < 1e-8 and e2 < 1e-8 and np.abs(g5x - g5).max() < 1e-7, f'errors {e1:.0e}, {e2:.0e}; vs light-algebra g5 {np.abs(g5x - g5).max():.0e}')
ker, inert = [], []
Vl0, Vm0 = span((I8 - g5) / 2 @ tk.P2)[0], span(Pp @ tk.P2)[0]
for R in (1, 2, 3):
    Hm, rung, nodes, idx = Hlad(tk, R, np.zeros(3), KAP, MC, zoom, X, sparse=True); n8 = Hm.shape[0]
    E = eigsh(Hm, k=8, sigma=1e-7, which='LM', return_eigenvectors=False); nz = int(np.sum(np.abs(E) < 1e-9))
    res_ = 0.0
    for node, Vb in ((idx[(0, (0, 0, 0))], Vl0), (idx[(R, (0, 0, 0))], Vm0)):
        for k in range(2): vv = np.zeros(n8, complex); vv[8 * node:8 * node + 8] = Vb[:, k]; res_ = max(res_, np.abs(Hm @ vv).max())
    ker.append((nz, float(f'{res_:.0e}')))
for Q in rng.uniform(-np.pi, np.pi, (3, 3)):
    Ez = np.linalg.eigvalsh(Hlad(tk, 2, Q, KAP, MC, zoom, X)[0]); Ef = np.linalg.eigvalsh(Hlad(tk, 2, Q, KAP, MC, fine, X)[0])
    inert.append((np.sum(Ez < 0) == np.sum(Ef < 0)) and (np.sum(np.abs(Ez) < 1e-10) == np.sum(np.abs(Ef) < 1e-10)))
check('A2 THEOREM H_zoom = S H_fine S (S = 2^(-j/2), geometric-mean exchange): Sylvester keeps the inertia at every Q, so nodes and '
      'chiralities are the fine-rate ones; Q = 0 kernel = rung-0 P- copy 2 (light) + top P+ copy 2 (mirror), exactly',
      all(k[0] == 4 and k[1] < 1e-9 for k in ker) and all(inert), f'R=1,2,3 (dim, |Hv|): {ker}; inertia equal at 3 random Q')
d = np.array([.3, .5, .81]); d /= np.linalg.norm(d); tab = {}
for rate, nm in ((zoom, 'zoom'), (fine, 'fine')):
    Hm, rung, _, _ = Hlad(tk, 3, 0.02 * d * 8, KAP, MC, rate, X, sparse=True); E, V = eigsh(Hm, k=24, sigma=0.0, which='LM')
    w0 = np.sum(np.abs(V[rung == 0]) ** 2, 0); wT = np.sum(np.abs(V[rung == 3]) ** 2, 0); pos = E > 0
    il = np.argmax(np.where(pos & (w0 > .5), -E, -1e9)); iT = np.argmax(np.where(pos & (wT > .5), -E, -1e9))
    Hm, rung, _, _ = Hlad(tk, 3, 0.01 * d * 8, KAP, MC, rate, X, sparse=True); E2, V2 = eigsh(Hm, k=60, sigma=0.0, which='LM')
    gb = [float(np.min(np.abs(E2[(np.sum(np.abs(V2[rung == j]) ** 2, 0) > .5)]))) for j in (1, 2)]
    tab[nm] = (E[il] / (v * 0.02), E[iT] / (v * 0.02), gb, wT[il])
z_, f_ = tab['zoom'], tab['fine']
check('A3 DIAGNOSTIC R = 3, |q| = 0.02: light speed v; mirror (top) speed v at the zoom rate, 2^R v at the fine rate; rung-j bulk '
      'gap 0.354 x 2^-j (zoom) vs ~0.4 (fine): coarse seas slower and lighter, never faster',
      abs(z_[0] - 1) < 1e-3 and abs(z_[1] - 1) < 0.01 and abs(f_[1] / 8 - 1) < 0.01 and abs(z_[2][0] / 0.1768 - 1) < 0.02 and abs(z_[2][1] / 0.0884 - 1) < 0.02,
      f'zoom: {z_[0]:.4f}, {z_[1]:.3f}, gaps {z_[2][0]:.4f}, {z_[2][1]:.4f}; fine: {f_[1]:.2f}, {f_[2][0]:.3f}, {f_[2][1]:.3f}; light top weight {z_[3]:.0e}')

# ============================================================ B
print('== B. Spin(10) pair square on the top rung\'s mirror slots only (P+ copy 2: 32 modes per cell)')
I2 = np.eye(2); PX = np.array([[0, 1], [1, 0]], complex); PY = np.array([[0, -1j], [1j, 0]]); PZ = np.diag([1., -1.]).astype(complex)
kron = lambda *a: reduce(np.kron, a)
gam = [kron(*([I2] * k + [P] + [PZ] * (4 - k))) for k in range(5) for P in (PX, PY)]
plus = np.where(np.isclose(np.diag(kron(*([PZ] * 5))).real, 1))[0]; Cc = kron(PY, PX, PY, PX, PY)
Ma = [(Cc @ g_)[np.ix_(plus, plus)] for g_ in gam]
cov = max(np.abs((0.5j * gam[a] @ gam[b])[np.ix_(plus, plus)].T @ Ma[c] + Ma[c] @ (0.5j * gam[a] @ gam[b])[np.ix_(plus, plus)]
                 - 1j * ((a == c) * Ma[b] - (b == c) * Ma[a])).max() for a in range(10) for b in range(a + 1, 10) for c in range(10))
def create(state, modes):
    out = {}
    for s, amp in state.items():
        x, sg, ok = s, 1, True
        for m in reversed(modes):
            if (x >> m) & 1: ok = False; break
            sg *= (-1) ** bin(x & ((1 << m) - 1)).count('1'); x |= (1 << m)
        if ok: out[x] = out.get(x, 0) + sg * amp
    return out
terms = []
for a in range(10):
    lst = [(np.conj(Ma[a][al, be]), (16 + be, al)) for al in range(16) for be in range(16) if abs(Ma[a][al, be]) > 1e-12]
    terms += [(c1 * c2, m1 + m2) for (c1, m1), (c2, m2) in itertools.product(lst, lst)]
def Omd(state):
    out = {}
    for c, modes in terms:
        for k, x in create(state, list(modes)).items(): out[k] = out.get(k, 0) + c * x
    return {k: x for k, x in out.items() if abs(x) > 1e-12}
s1 = Omd({0: 1.0}); s2 = Omd(s1); n1 = sum(abs(x) ** 2 for x in s1.values()); n2 = sum(abs(x) ** 2 for x in s2.values())
def chain(f, K): b = np.sqrt([f(k) for k in range(1, K)]); return np.linalg.eigvalsh(np.diag(b, 1) + np.diag(b, -1))[0]
E0 = chain(lambda k: 16 * k * (9 - k) * (k + 4) * (13 - k), 9); D10 = chain(lambda k: 16 * k * (8 - k) * (k + 5) * (13 - k), 8) - E0
Dfm = chain(lambda k: 16 * k * (8 - k) * (k + 4) * (13 - k), 8) - E0
check('B1 THEOREM (smg-verify D0-D4, rechecked) one cell: M_a Spin(10)-covariant; |Om^+|0>|^2 = 7680, |Om^+2|0>|^2 = 113541120 '
      '(so(12) chain); unique singlet E0 = -2g sqrt(11088+48 sqrt21081), gaps 19.0715 g, 33.5804 g',
      cov < 1e-12 and abs(n1 - 7680) < 1e-6 and abs(n2 - 113541120) < 1e-3 and abs(E0 + 2 * np.sqrt(11088 + 48 * np.sqrt(21081))) < 1e-9
      and abs(D10 - 19.0715) < 1e-4 and abs(Dfm - 33.5804) < 1e-4, f'{cov:.0e}; {n1:.0f}, {n2:.0f}; {E0:.6f}; {D10:.4f}, {Dfm:.4f}')
print('   B2 THEOREM the Q = 0 light modes live on rung 0 only (A2): [H, a_l] = 0, G_l(z, 0) = 1/z at any top-rung coupling, R >= 1')
print('   B3 THEOREM the singlet has <c> = <cc> = 0 (Z4), <c+_a c_b> = d_ab/2 (irreducible 32, <N> = 16): P f P = 0, so g -> inf is the '
      'deleted-slot ladder (projection; Feshbach error <= |V|^2/(U-2|V|) at fixed volume)')
slot = Pp @ tk.P2; Vs, Vk = span(slot)
def Gp(R, Q, nodes, idx, keep):   # gauge-dressed chiral inversion D_phi (g5 x node inversion), restricted to retained modes
    n = len(nodes); G = np.zeros((8 * n, 8 * n), complex)
    for i, (j, m, q) in enumerate(nodes):
        k = idx[(j, tuple(np.mod(-np.array(m) - np.round(np.asarray(Q) / np.pi).astype(int), 2 ** (R - j))))]
        G[8 * k:8 * k + 8, 8 * i:8 * i + 8] = np.exp(-1j * sum(2 ** t * np.sum(nodes[k][2]) for t in range(R - j))) * g5
    top = [i for i, nd in enumerate(nodes) if nd[0] == R][0]
    blocks = [keep if i == top else I8 for i in range(n)]; Vm = np.zeros((8 * n, sum(b.shape[1] for b in blocks)), complex); c = 0
    for i, b in enumerate(blocks): Vm[8 * i:8 * i + 8, c:c + b.shape[1]] = b; c += b.shape[1]
    return Vm.conj().T @ G @ Vm
TRIM = [np.array(Q, float) for Q in itertools.product((0, np.pi), repeat=3)]
sym, zc, tr = 0.0, [], []
for R in (1, 2):
    for rate in (zoom, fine):
        for Q in TRIM:
            He, rr, nodes, idx = Hlad(tk, R, Q, KAP, MC, rate, X, keep_top=Vk); G = Gp(R, Q, nodes, idx, Vk)
            sym = max(sym, np.abs(G @ He @ G + He).max(), np.abs(G @ G - np.eye(len(G))).max())
            E = np.sort(np.abs(np.linalg.eigvalsh(He))); zc.append(int(np.sum(E < 1e-8))); tr.append(round(float(np.real(np.trace(G))), 6))
check('B4 THEOREM TRIM index: at the 8 TRIM points of the top zone the deleted-slot Bloch H anticommutes with the involution '
      'G\' = D_phi (g5 x node inversion), phi = -sum_t 2^t q.1; Tr G\' = -2, so >= 2 zero modes at every TRIM',
      sym < 1e-8 and min(zc) == 2 and max(zc) == 2 and set(tr) == {-2.0}, f'error {sym:.0e}; zero modes per TRIM {sorted(set(zc))} (R = 1, 2, both rates); Tr {sorted(set(tr))}')
def node_info(R, Q0, keep, h=1e-4):
    He, rr, _, _ = Hlad(tk, R, Q0, KAP, MC, zoom, X, keep_top=keep); E, Vv = np.linalg.eigh(He); P = Vv[:, np.argsort(np.abs(E))[:2]]
    sig = [PX, PY, PZ]; vm = np.zeros((3, 3))
    for a in range(3):
        e_ = np.zeros(3); e_[a] = h
        dH = P.conj().T @ (Hlad(tk, R, Q0 + e_, KAP, MC, zoom, X, keep_top=keep)[0] - Hlad(tk, R, Q0 - e_, KAP, MC, zoom, X, keep_top=keep)[0]) @ P / (2 * h)
        for b in range(3): vm[a, b] = np.real(np.trace(dH @ sig[b])) / 2
    return int(np.sign(np.linalg.det(vm))), float(np.mean(np.linalg.svd(vm, compute_uv=False))) * 2 ** R / v, [float(np.sum(np.abs(P[rr == j]) ** 2) / 2) for j in range(R + 1)]
info = {R: [node_info(R, Q, Vk) for Q in TRIM] for R in (1, 2)}
chis = {R: [x[0] for x in info[R]] for R in (1, 2)}; r_ = [int(Q.sum() / np.pi + .5) for Q in TRIM]
ok5 = all(chis[R] == [(-1) ** k for k in r_] for R in (1, 2)) and all(info[R][0][2][0] > 1 - 1e-9 for R in (1, 2)) \
      and min(x[2][-1] for R in (1, 2) for x in info[R][1:]) > 0.84 and all(abs(x[1] - 1) < 0.03 for R in (1, 2) for x in info[R])
check('B5 DIAGNOSTIC nodes: Gamma = light Weyl (+1, on rung 0); X (x3) -1, M (x3) +1, R -1 on the TOP rung: no light-end doublers, '
      '7 far-end doublers, net 0 (Nielsen-Ninomiya); speed v',
      ok5, 'R=2 top weights X, M, R ' + ', '.join(f'{info[2][k][2][-1]:.3f}' for k in (1, 3, 7)) + f'; X on rung 0 {info[2][1][2][0]:.3f}; '
      'speeds/v ' + ', '.join(f'{info[2][k][1]:.3f}' for k in (0, 1, 3, 7)))
wr_ = {}
for R in (1, 2):
    Hm, rr, _, _ = Hlad(tk, R, np.zeros(3), KAP, MC, zoom, X, keep_top=np.zeros((8, 0)))
    E, Vv = np.linalg.eigh(Hm); z = np.abs(E) < 1e-9; wr_[R] = (int(z.sum()), [round(float(np.sum(np.abs(Vv[rr == j][:, z]) ** 2)), 4) for j in range(R)])
check('B6 DIAGNOSTIC freezing the whole top rung (index 0) moves the partner to Gamma one rung down; at R = 1 onto the light rung '
      '(a light-end doubler: the thin-strip endpoint)',
      wr_[1] == (4, [4.0]) and wr_[2][0] == 4 and abs(wr_[2][1][1] - 2) < 1e-3, f'Gamma zero modes (count, by rung): R=1 {wr_[1]}, R=2 {wr_[2]}')
print('   B7 ESTIMATE for t << g the 7 cones get t^4/g^3 four-fermion terms (dimension 6: irrelevant): massless wherever the pair '
      'square gaps the cell (t < 3.65 g); g ~ t is uncontrolled')

import gc; tk.Hc.clear(); del info; gc.collect()
# ============================================================ C
print('== C. 1+1D analogue (2-site cells, same tick, binary tree, zoom rate)')
W1 = np.array([[0, -1], [-1, 0]], complex)
def ex1(th): return np.cos(th) * I2 + 1j * np.sin(th) * W1
st1 = 0.04
def D1(K): return np.diag([1, np.exp(1j * K)])
def U1(K): return D1(K) @ ex1(st1) @ D1(K).conj().T @ ex1(-st1)
H1c = {}
def H1(K):
    k_ = round(float(np.mod(K + np.pi, 2 * np.pi) - np.pi), 11)
    if k_ not in H1c: H1c[k_] = logH(U1(K)) / st1
    return H1c[k_]
A_ = (H1(1e-5) - H1(-1e-5)) / 2e-5; v1 = np.sqrt(np.trace(A_ @ A_).real / 2); g51 = (A_ + A_.conj().T) / (2 * v1); X1 = W1 @ (I2 - g51) / 2
def tree1(R, Q):
    nodes = [(j, m, (Q + 2 * np.pi * m) / 2 ** (R - j)) for j in range(R + 1) for m in range(2 ** (R - j))]
    idx = {(j, m): i for i, (j, m, q) in enumerate(nodes)}
    return nodes, [None if j == R else idx[(j + 1, m % 2 ** (R - j - 1))] for (j, m, q) in nodes]
def Hl1(R, Q, rate, keep=None):
    nodes, par = tree1(R, Q); n = len(nodes); Hm = np.zeros((2 * n, 2 * n), complex)
    for i, (j, m, q) in enumerate(nodes):
        Hm[2 * i:2 * i + 2, 2 * i:2 * i + 2] = rate(j) * H1(q)
        if par[i] is not None:
            p = par[i]; g = KAP * np.sqrt(rate(j) * rate(j + 1)) * (1 + np.exp(-1j * q)) / 2
            Hm[2 * i:2 * i + 2, 2 * p:2 * p + 2] += g * X1; Hm[2 * p:2 * p + 2, 2 * i:2 * i + 2] += np.conj(g) * X1.conj().T
    rr = np.repeat([nd[0] for nd in nodes], 2)
    if keep is None: return Hm, rr
    top = [i for i, nd in enumerate(nodes) if nd[0] == R][0]; blocks = [keep if i == top else I2 for i in range(n)]
    Vm = np.zeros((2 * n, sum(b.shape[1] for b in blocks)), complex); c = 0
    for i, b in enumerate(blocks): Vm[2 * i:2 * i + 2, c:c + b.shape[1]] = b; c += b.shape[1]
    return Vm.conj().T @ Hm @ Vm, np.concatenate([np.full(b.shape[1], nodes[i][0]) for i, b in enumerate(blocks)])
def tick_rs(L):
    Ue = np.zeros((L, L), complex); Uo = np.zeros((L, L), complex)
    for n in range(L // 2):
        ids = [2 * n, 2 * n + 1]; Ue[np.ix_(ids, ids)] = ex1(-st1); ids = [(2 * n + 1) % L, (2 * n + 2) % L]; Uo[np.ix_(ids, ids)] = ex1(st1)[np.ix_([1, 0], [1, 0])]
    return logH(Uo @ Ue) / st1
L0 = 8; Hrs = np.zeros((12, 12), complex); Hrs[:8, :8] = tick_rs(8); Hrs[8:, 8:] = 0.5 * tick_rs(4); gx = KAP * np.sqrt(0.5)
for n_ in range(2):
    for b in range(2):
        for c in range(2):
            for a in range(2):
                i, k = 2 * (2 * n_ + c) + a, 8 + 2 * n_ + b; Hrs[i, k] += gx * X1[a, b] / np.sqrt(2); Hrs[k, i] += np.conj(gx * X1[a, b] / np.sqrt(2))
e_rs = np.abs(np.sort(np.linalg.eigvalsh(Hrs)) - np.sort(np.concatenate([np.linalg.eigvalsh(Hl1(1, Q, zoom)[0]) for Q in (0, np.pi)]))).max()
eci1 = max(np.abs(g51 @ U1(K) @ g51 - U1(-K).conj().T).max() for K in rng.uniform(-3, 3, 4))
band = [float(np.abs(np.linalg.eigvalsh(H1(k))).min()) for k in np.linspace(0.3, np.pi, 6)]
check('C1 THEOREM 1D: g5 = a, {g5, W} = 0, g5 U(K) g5 = U(-K)^+; one cone per rung (|E| = 2 at the zone edge); real space = tree', eci1 < 1e-8 and e_rs < 1e-12 and min(band) > 0.2 and abs(band[-1] - 2) < 1e-3,
      f'{eci1:.0e}; {e_rs:.0e}; {band[-1]:.4f}')
_, Vk1 = span((I2 + g51) / 2); c2 = []
for R in (1, 2, 3, 4):
    row = []
    for Q in (0.0, np.pi):
        He, rr = Hl1(R, Q, zoom, Vk1); E, Vv = np.linalg.eigh(He); i0 = np.argmin(np.abs(E))
        dv = np.real(Vv[:, i0].conj() @ (Hl1(R, Q + 1e-4, zoom, Vk1)[0] - Hl1(R, Q - 1e-4, zoom, Vk1)[0]) @ Vv[:, i0]) / 2e-4 * 2 ** R
        row.append((abs(E[i0]), float(np.sum(np.abs(Vv[rr == 0, i0]) ** 2)), float(np.sum(np.abs(Vv[rr == R, i0]) ** 2)), dv))
    c2.append(row)
check('C2 THEOREM 1D endpoint (top slot deleted), R = 1..4: zero modes at Q = 0 (light mover, on rung 0) and Q = pi (compensator, '
      'opposite velocity, on the top rung)',
      all(r[0][0] < 1e-9 and r[1][0] < 1e-9 and r[0][1] > 1 - 1e-9 and r[1][2] > 0.93 and r[0][3] * r[1][3] < 0 for r in c2),
      f'velocities/v {c2[0][0][3] / v1:+.3f}, {c2[3][1][3] / v1:+.3f}; top weight {c2[3][1][2]:.3f}')
# exact interacting ED: 8 + 4 site ring (two top cells), rotate to Bloch x chirality modes; drop the 3 modes that decouple exactly
wv, Vv = np.linalg.eigh((I2 + g51) / 2); vP, vM = Vv[:, np.argmax(wv)], Vv[:, np.argmin(wv)]; Bm = np.zeros((12, 12), complex); lab = []
for m in range(4):
    for nm, vec in (('+', vP), ('-', vM)):
        col = np.zeros(12, complex)
        for n_ in range(4): col[2 * n_:2 * n_ + 2] = np.exp(2j * np.pi * m * n_ / 4) * vec / 2
        Bm[:, len(lab)] = col; lab.append(('r0', m, nm))
for n_ in range(2):
    for nm, vec in (('slot', vP), ('partner', vM)):
        col = np.zeros(12, complex); col[8 + 2 * n_:10 + 2 * n_] = vec; Bm[:, len(lab)] = col; lab.append(('top', n_, nm))
hq = Bm.conj().T @ Hrs @ Bm; excl = [i for i, l in enumerate(lab) if l[0] == 'r0' and (l[1] == 2 or (l[1] == 0 and l[2] == '-'))]
kept = [i for i in range(12) if i not in excl]; dec = np.abs(hq[np.ix_(excl, kept)]).max(); hk = hq[np.ix_(kept, kept)]; lk = [lab[i] for i in kept]; nk = len(kept)
Gr = np.zeros((12, 12), complex)   # chiral inversion in real space: rung-0 cell i -> 1 - i, top cell n -> -n, g5 on each cell
for i in range(4): j_ = (1 - i) % 4; Gr[2 * j_:2 * j_ + 2, 2 * i:2 * i + 2] = g51
for n_ in range(2): m_ = (-n_) % 2; Gr[8 + 2 * m_:10 + 2 * m_, 8 + 2 * n_:10 + 2 * n_] = g51
Gq = Bm.conj().T @ Gr @ Bm; gerr = max(np.abs(Gr @ Hrs @ Gr + Hrs).max(), np.abs(Gq[np.ix_(excl, kept)]).max()); trk = float(np.real(np.trace(Gq[np.ix_(kept, kept)])))
dim = 2 ** nk; sts = np.arange(dim); cs = []
for i in range(nk):
    m_ = ((sts >> i) & 1) == 1; s0 = sts[m_]; sg = (-1.0) ** np.array([bin(x & ((1 << i) - 1)).count('1') for x in s0])
    cs.append(sp.csr_matrix((sg, (s0 ^ (1 << i), s0)), shape=(dim, dim)))
Id = sp.identity(dim, format='csr')
Hfree = sum(hk[i, j] * (cs[i].T @ cs[j]) for i in range(nk) for j in range(nk) if abs(hk[i, j]) > 1e-14)
def atom(a, b):   # 1 - |s><s|, |s> = (1 + a^+ b^+)|0> / sqrt2 on modes a, b (Hubbard + pair terms: interacting)
    na, nb, ab = cs[a].T @ cs[a], cs[b].T @ cs[b], cs[a].T @ cs[b].T
    return Id - 0.5 * ((Id - na) @ (Id - nb) + na @ nb + ab + ab.T)
sl = [i for i, l in enumerate(lk) if l[2] == 'slot']; pa = [i for i, l in enumerate(lk) if l[2] == 'partner']; r0 = [i for i, l in enumerate(lk) if l[0] == 'r0']
res = {}
for key, Ha in (('S1', atom(sl[0], sl[1])), ('S2', atom(sl[0], pa[0]) + atom(sl[1], pa[1]))):
    out = []
    for Dl in (0.0, 1.0, 4.0, 16.0, 256.0):
        Hm = (Hfree + Dl * Ha).toarray(); E, Vg = np.linalg.eigh((Hm + Hm.conj().T) / 2); G = Vg[:, :2]
        wt = lambda ids: sum(np.sum(np.abs(G.conj().T @ (cs[i] @ G)) ** 2) + np.sum(np.abs(G.conj().T @ (cs[i].T @ G)) ** 2) for i in ids) / 2
        out.append((Dl, float(np.abs(E[1::2] - E[0::2]).max()), E[2] - E[0], wt(sl), wt(pa), wt(r0)))
    res[key] = out
S1, S2 = res['S1'], res['S2']
check('C3 EXACT ED (8+4-site ring, interacting atom on the two top slots): all 512 levels stay doubly degenerate at every g (the chiral '
      'inversion anticommutes with h, trace odd on the 9 coupled modes); the zero-energy weight leaves the slot (zero) for elementary top partners',
      dec < 1e-10 and gerr < 1e-9 and abs(abs(trk) - 1) < 1e-9 and max(x[1] for x in S1) < 1e-12 and S1[0][3] > 0.999 and S1[-1][3] < 1e-4 and S1[-1][4] > 0.93,
      f'Tr {trk:+.0f}; slot/partner/rung 0: ' + '; '.join(f'g={x[0]:.0f} {x[3]:.3f}/{x[4]:.3f}/{x[5]:.3f}' for x in S1[::2]))
check('C4 EXACT ED, atoms on whole top cells: the zero-energy fermion moves onto the light rung (light-end doubler)', max(x[1] for x in S2) < 1e-12 and S2[-1][5] > 0.999,
      'rung 0: ' + ', '.join(f'{x[5]:.3f}' for x in S2) + ' (g = 0..256)')
He, rr = Hl1(1, 0.0, zoom, Vk1); n0d = int(np.sum(np.abs(np.linalg.eigvalsh(He)) < 1e-9))
check('C5 THEOREM 0D end (one top cell, Fidkowski-Kitaev setting): only the light zero mode remains, no partner is needed; a wall with '
      'a zone has TRIM partners (B4, C2) that one-cell uniqueness cannot see', n0d == 1, f'zero modes {n0d}')

del cs, Hfree, Id; gc.collect()
# ============================================================ D
print('== D. measured constraints at the zoom rate (a = sqrt(8 pi) l_P; energy unit E_a/(2v) = 2.1e18 GeV)')
pz = [(Fr(1, 2 ** j) * Fr(16) ** j / Fr(8) ** j, Fr(4) ** j * Fr(2) ** j / Fr(8) ** j, Fr(1, 2 ** j) * Fr(256) ** j / Fr(8) ** j) for j in range(6)]
check('D1 THEOREM power counting (energy 2^-j, flux 4^j, cell 8^j): B^2 and E^2 per volume x 1 per rung (fine: 2^j, 2^-j); B^4 x 16^j', all(p == (1, 1, 16 ** j) for j, p in enumerate(pz)), 'exact for j = 0..5')
def lidx(L, x):
    x = np.mod(x, L); return int((x[0] * L[1] + x[1]) * L[2] + x[2])
def coarse_links(A, L):
    Lc = tuple(l // 2 for l in L); Ac = []
    for mu in range(3):
        a = np.zeros(Lc)
        for p in itertools.product(*[range(l) for l in Lc]):
            x = 2 * np.array(p); y = x.copy(); y[mu] += 1; a[p] = A[mu][tuple(np.mod(x, L))] + A[mu][tuple(np.mod(y, L))]
        Ac.append(a)
    return Ac, Lc
def path_phase(A, L, x0, x1):
    ph = 0.0; x = np.array(x0, int).copy()
    for mu in range(3):
        dd = int(x1[mu] - x0[mu])
        for _ in range(abs(dd)):
            if dd > 0: ph += A[mu][tuple(np.mod(x, L))]; x[mu] += 1
            else: x[mu] -= 1; ph -= A[mu][tuple(np.mod(x, L))]
    return ph
P1W = tk.P1 @ W; P1W = (P1W + P1W.conj().T) / 2
def rung_blocks(A, L):   # first-order generator of the tick with species mass mu = st, copy mass M = st: (1/2)W_e - (3/2)W_o - P1W_e
    out = []
    for par, coef in ((0, 0.5), (1, -1.5)):
        for n in itertools.product(*[range(l // 2) for l in L]):
            o = 2 * np.array(n) + par; xs = [o + cp for cp in C]; ids = [lidx(L, x) for x in xs]; lb = [int(np.argmin(np.abs(C - np.mod(x, 2)).sum(1))) for x in xs]
            B = np.zeros((8, 8), complex)
            for i in range(8):
                for k in range(i, 8):
                    val = coef * W[lb[i], lb[k]] if np.abs(C[i] - C[k]).sum() == 1 else 0.0
                    if par == 0: val = val - P1W[lb[i], lb[k]]
                    if abs(val) > 1e-14:
                        B[i, k] = val * (np.exp(1j * path_phase(A, L, xs[k], xs[i])) if i != k else 1.0)
                        if k != i: B[k, i] = np.conj(B[i, k])
            out.append((ids, B))
    return out
def Esea(L, R, F, rate):
    Lx, Ly, Lz = L; A0 = [np.zeros(L), np.zeros(L), np.zeros(L)]
    for x in range(Lx):
        for y in range(Ly):
            A0[0][x, y, :] = -2 * np.pi * F * y / (Lx * Ly)
            if y == Ly - 1: A0[1][x, y, :] = 2 * np.pi * F * x / Lx
    As, Ls = [A0], [tuple(L)]
    for j in range(R): Ac, Lc = coarse_links(As[-1], Ls[-1]); As.append(Ac); Ls.append(Lc)
    Ns = [int(np.prod(l)) for l in Ls]; off = np.concatenate([[0], np.cumsum(Ns)]).astype(int); Hm = np.zeros((off[-1],) * 2, complex)
    for j in range(R + 1):
        for ids, B in rung_blocks(As[j], Ls[j]):
            g_ = off[j] + np.array(ids); Hm[np.ix_(g_, g_)] += rate(j) * B
    for j in range(R):
        Lc = Ls[j + 1]; gg = KAP * np.sqrt(rate(j) * rate(j + 1))
        for n in itertools.product(*[range(l // 2) for l in Lc]):
            n = np.array(n)
            for c in C:
                for ia, a in enumerate(C):
                    x = 2 * (2 * n + c) + a; fi = off[j] + lidx(Ls[j], x)
                    for k, b in enumerate(C):
                        if abs(X[ia, k]) > 1e-15:
                            ci = off[j + 1] + lidx(Lc, 2 * n + b); val = gg * X[ia, k] / np.sqrt(8) * np.exp(1j * path_phase(As[j], Ls[j], 2 * (2 * n + b), x))
                            Hm[fi, ci] += val; Hm[ci, fi] += np.conj(val)
    E = eigvalsh(Hm, overwrite_a=True, check_finite=False); del Hm; return E[E < 0].sum(), np.abs(E).min()
Lf, Lc = (8, 16, 8), (4, 8, 4); rec = {}
for rate, nm, fac in ((zoom, 'zoom', 0.5), (fine, 'fine', 1.0)):
    dd = {}; gp = np.inf
    for key, LL, R in (('0c', Lc, 0), ('1c', Lc, 1), ('1', Lf, 1), ('2', Lf, 2)):
        e1_, g1_ = Esea(LL, R, 1, rate); e0_, g0_ = Esea(LL, R, 0, rate); dd[key] = e1_ - e0_; gp = min(gp, g0_, g1_)
    rec[nm] = (dd['1'] - fac * dd['0c'], dd['2'] - fac * dd['1c'], gp)
check('D2 DIAGNOSTIC flux on 8x16x8 vs 4x8x4 tori: E_R(L) = r E_(R-1)(L/2) + A with rung-local A (r = 1/2 zoom, 1 fine): B^2 coefficient '
      'c_0 + R a (zoom) vs 2^R (c_0 + a) - a (fine)',
      all(abs(rec[k][1] / rec[k][0] - 1) < 0.01 and rec[k][2] > 0.1 for k in rec), f"A(2)/A(1) zoom {rec['zoom'][1] / rec['zoom'][0]:.4f}, fine {rec['fine'][1] / rec['fine'][0]:.4f}; gap >= {min(r[2] for r in rec.values()):.2f}")
Ea, HU, al_ = 2.435e18, 2.435e18 / (2 * v), 1 / 137.036
KB = 0.018; ER = lambda R: 0.354 * 2.0 ** -R * HU
Edec = 1.4e6 ** 2 / (2 * 0.511e-3)   # photon decay to e+e- stays closed up to 1.4 PeV if E_LV > k^2/(2 m_e)
Rmax_sup = max(R for R in range(60) if ER(R) / np.sqrt(al_ * 16 / 3 / (3 * np.pi)) > Edec)
Rmax_sub = max(R for R in range(60) if ER(R) / np.sqrt(al_ * 16 / 3 / (3 * np.pi)) > 7.3e11)
print(f'   stiffness d(1/mu) ~ (R+1) x {KB} (octree-field K per rung, O(1) factor), flat for wavelengths > a_R (fine rate: 1.7e20 at 1/m_e); '
      f'R = {Rmax_sup}: {(Rmax_sup + 1) * KB:.2f}, absorbed in 1/e^2; photon/matter speed: one counterterm')
print(f'   light cone: top-rung terms give photon dv/v ~ (alpha 16/9pi)(E/E_R)^2, E_R = 0.354 x 2^-R x 2.1e18 GeV: R <= {Rmax_sup} '
      f'(1.4 PeV photons, if superluminal), <= {Rmax_sub} (GRB 221009A, if subluminal); B^4 ~ (m_e/E_R)^4 = {(0.511e-3 / ER(Rmax_sup)) ** 4:.0e} of QED')
print(f'   endpoint: 7 massless far-end 16s per family: N_nu = 8 per family (24 for three) vs 2.984 +- 0.008, d(1/alpha)/dln(mu) + {7 * 16 / (9 * np.pi):.1f} per family: excluded')
check(f'D3 ESTIMATES the zoom rate passes what killed the fine rate (flat stiffness, no superluminal sea) for R <= {Rmax_sup}-{Rmax_sub}; '
      'the strong-coupling endpoint is excluded', Rmax_sup >= 8 and Rmax_sub > Rmax_sup, f'{time.monotonic() - T0:.1f} s')
print('supplied: octree sites, zoom rate with geometric-mean exchange, a top rung R, X, kap, M = st = 0.04, the 16, the pair square on top '
      'slots only, g, slot choice; 1D tick and atoms; species mass, tori; K (octree-field)')
print('cited: smg-verify, SPIN10 mirror-boundary note (projection, Feshbach), Golterman-Shamir 2505.20436/2603.15985, Zeng et al. 2202.12355, '
      'Nielsen-Ninomiya, measured values')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
