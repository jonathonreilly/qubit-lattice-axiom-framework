#!/usr/bin/env python3
"""smg-qmc: can a finite-coupling far end gap the mirror AND the zone-corner doublers of the hybrid wall?
(supplied models; exact theorems, finite diagnostics, estimates; no physical identification established)
 A  feasibility: sign-free auxiliary-field run of the 3D wall vs the 90 s / 300 MB limits (estimate)
 B  the wall at the 8 TRIM corners (R = 1 zoom-rate ladder, slot = P+ copy 2 of the top cell): index facts
 C  exact Green-function theorems for slot-only interactions, at every coupling
 D  exact ED, 2-cell twisted clusters {Gamma, Q0}: Z4 atom on 2 flavours x Weyl slot, doublers from the ladder
 E  estimates and reading against Golterman-Shamir"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm

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
print('== A. sign-free auxiliary-field route against the limits')
a_qmc = 29.7 / (1152 ** 3 * 40)            # QMC-1 (repo archive): 2+1D L = 6 Spin(10), N_d = 2 x 16 x 36, L_tau = 40: 29.7 s/sweep
Nd_wall = 16 * (8 * 8 + 64 * 8)            # 2^3 top cells (all 8 corners), R = 1 ladder, 16 flavours
print(f'   A1 ESTIMATE the main-branch pairing identity (kappa = 3/2, -1/2, Kramers-graded) is a local sign-free vertex only; the '
      f'smallest wall with all 8 corners has N_d = {Nd_wall}: ~{a_qmc * Nd_wall ** 3 * 40 / 3600:.1f} h/sweep, {Nd_wall ** 2 * 16 / 2 ** 30:.1f} GB '
      'per Green matrix (cost a N^3 L_tau); Kramers-reality of the tick hop unchecked. Not within 90 s / 300 MB: exact theorems + exact ED')

# ============================================================ B
print('== B. the wall at the 8 TRIMs (3D tick st = M = 0.04, kap = 0.5, X = W(1-g5)/2, R = 1, zoom rate; slot = P+ copy 2 of the top cell)')
tk = Tick(0.04); MC = tk.st; KAP = 0.5; g5 = tk.g5; Pp = (I8 + g5) / 2; RR = 1
Vs, Vk = span(Pp @ tk.P2)
Bq = np.array(list(itertools.product((0, 1), repeat=3))); TRIM = [np.pi * q.astype(float) for q in Bq]
def lad(Q):
    H, rung, nodes, idx = Hlad(tk, RR, np.asarray(Q, float), KAP, MC, zoom, tk.X); n = H.shape[0]; top = idx[(RR, (0, 0, 0))]
    Ps = np.zeros((n, 2), complex); Ps[8 * top:8 * top + 8] = Vs
    w, U = np.linalg.eigh(np.eye(n) - Ps @ Ps.conj().T); Ur = U[:, w > 0.5]
    er, Ue = np.linalg.eigh(Ur.conj().T @ H @ Ur); K = Ur @ Ue[:, np.abs(er) < 1e-8]
    return H, Ps, Ur, K, Gp(RR, Q, nodes, idx, I8), top
LD = {tuple(q): lad(Q) for q, Q in zip(Bq, TRIM)}
errB, trs, sl, nz, gap0, Vsv = 0.0, set(), set(), set(), {}, {}
for q in map(tuple, Bq):
    H, Ps, Ur, K, G, top = LD[q]; PsP = Ps @ Ps.conj().T
    errB = max(errB, np.abs(G @ H @ G + H).max(), np.abs(G @ PsP - PsP @ G).max())
    trs.add(round(np.trace(G).real, 6)); sl.add(round(np.trace(Ps.conj().T @ G @ Ps).real, 6)); nz.add(K.shape[1])
    gap0[q] = float(np.sort(np.abs(np.linalg.eigvalsh(H)))[0]); Vsv[q] = np.linalg.svd(Ps.conj().T @ H @ K, compute_uv=False)
XQ, MQ, RQ = (1, 0, 0), (1, 1, 0), (1, 1, 1)
check("B1 THEOREM (hybrid-wall B4) G'HG' = -H, [G', P_slot] = 0, G' = +1 on the slot, Tr G' = 0 on the ladder; deleted slot: 2 zero "
      'modes per TRIM; at g = 0 X, M, R gapped', errB < 1e-8 and trs == {0.0} and sl == {2.0} and nz == {2} and min(gap0[q] for q in (XQ, MQ, RQ)) > 0.2,
      f"err {errB:.0e}; gaps {gap0[XQ]:.4f}, {gap0[MQ]:.4f}, {gap0[RQ]:.4f}; slot-doubler |V| {Vsv[XQ][0]:.4f}, {Vsv[MQ][0]:.4f}, {Vsv[RQ][0]:.4f}")

# ============================================================ C
print("== C. exact, every coupling: interactions built from slot operators (the pair square is chiral-inversion symmetric: G' = +1 on the slot)")
print('   C1 THEOREM [c_r, H_int] = 0 off the slot, so Sigma lives on the slot block and every zero of G lies in the slot space (checked in D1)')
def Gw(H, Ps, S, w): return np.linalg.inv(1j * w * np.eye(H.shape[0]) - H - Ps @ (S / (1j * w)) @ Ps.conj().T)
def poles(H, Ps, S, w1=1e-6):
    Z = 2 * (1j * w1 * Gw(H, Ps, S, w1)) - 1j * 2 * w1 * Gw(H, Ps, S, 2 * w1); ev = np.linalg.eigvalsh((Z + Z.conj().T) / 2); return ev[ev > 1e-6]
rng = np.random.default_rng(1); Mr_ = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); Srand = Mr_ @ Mr_.conj().T + 0.3 * np.eye(2)
c2, zerr = {}, 0.0
for q in (XQ, MQ, RQ):
    H, Ps, Ur, K, G, top = LD[q]
    c2[q] = [len(poles(H, Ps, S)) for S in (np.zeros((2, 2)), Srand, np.diag([3.0, 0.0]))]
    Zf = np.linalg.inv(np.eye(2) + K.conj().T @ H @ Ps @ np.linalg.inv(Srand) @ Ps.conj().T @ H @ K)
    zerr = max(zerr, np.abs(np.sort(poles(H, Ps, Srand)) - np.sort(np.linalg.eigvalsh((Zf + Zf.conj().T) / 2))).max())
check('C2 THEOREM at X, M, R a rank-r slot zero (Sigma_ss ~ S/iw) forces >= r poles at w = 0 (full rank: on the deleted-slot kernel K, '
      'Z = [1 + K+H P S^-1 P+H K]^-1); a regular (odd) Sigma_ss keeps the corner gapped', all(c2[q] == [0, 2, 1] for q in c2) and zerr < 1e-3,
      f'poles (S = 0, full, rank 1) X {c2[XQ]}, M {c2[MQ]}, R {c2[RQ]}; Z vs formula {zerr:.0e}')
H, Ps, Ur, K, G, top = LD[(0, 0, 0)]
pG = [len(poles(H, Ps, S)) for S in (np.zeros((2, 2)), Srand)]; dec = np.abs(H @ Ps).max()
check('C3 THEOREM H(Gamma) P_slot = 0: the mirror pole leaves only through a slot zero at Gamma (or symmetry breaking); then only the light '
      'pole remains', dec < 1e-9 and pG == [4, 2], f'|H P_s| {dec:.0e}; poles at Gamma {pG[0]} -> {pG[1]}')
print('   C4 THEOREM a local (k-independent) zero sits at all 8 TRIMs: 7 doublers by C2 (atomic limit, DMFT-type, strong coupling). With '
      'G(k,0) analytic off Gamma (gapped phase) zeros cannot fill an open set, so a far end gapping both needs a lower-dimensional, '
      'dispersing zero set through Gamma avoiding X, M, R: an intermediate phase, adiabatic to neither limit')
Hd = np.array([[(-1) ** int(qq @ w) for w in Bq] for qq in Bq]); Hinv = np.linalg.inv(Hd); tsol = Hinv @ np.r_[-2.0, np.zeros(7)]
okp = [p for p in (np.r_[-2.0, p_] for p_ in itertools.product((-2.0, 0.0, 2.0), repeat=7)) if np.allclose(Hinv @ p, np.round(Hinv @ p))]
mext = min(int(np.sum(p[1:] != 0)) for p in okp); mmin = min(m for m in range(1, 17) if np.allclose(Hinv @ np.r_[float(m), np.zeros(7)] % 1, 0))
sym_min = min((p for p in okp if len(set(p[[1, 2, 4]])) == 1 and len(set(p[[3, 5, 6]])) == 1), key=lambda p: np.sum(p[1:] != 0))
fQ = lambda Q: np.prod((1 + np.cos(Q)) / 2); ext = {}
for nmD, Dl in (('local', lambda Q: 0.7), ('filtered', lambda Q: 0.7 * fQ(Q))):
    row = []
    for q, Q in zip(map(tuple, Bq), TRIM):
        H, Ps, Ur, K, G, top = LD[q]; n = H.shape[0]
        He = np.zeros((n + 2, n + 2), complex); He[:n, :n] = H; He[:n, n:] = Dl(Q) * Ps; He[n:, :n] = Dl(Q) * Ps.conj().T
        E, U = np.linalg.eigh(He); z = np.abs(E) < 1e-8; row.append((int(z.sum()), round(float(np.sum(np.abs(U[n:, z]) ** 2)), 3)))
    ext[nmD] = row
check("C5 THEOREM TRIM integrality: any translation-invariant quadratic model with G' (any range, any added local orbitals) has "
      "nu(Q) = Tr G'(Q) = sum_w t_w e^{iQ.w}, t_w integer; light only (nu = -2 delta_Gamma) needs t_w = -1/4, so no complete local "
      'interpolator set exists in a light-only phase; >= 3 extra corners (cubic: the 3 M); multiplicity 8 per irrep evades the index only. '
      "A chi (G' = -1) gapping the mirror leaves 2 zero modes at every TRIM",
      np.allclose(tsol, -0.25) and mext == 3 and mmin == 8 and all(r[0] == 2 for r in ext['local'] + ext['filtered'])
      and ext['filtered'][7][1] == 2.0 and ext['local'][0][1] == 0.0,
      f"t_w {tsol[0]:+.2f}; {len(okp)} patterns, min extra {mext}, symmetric (nu_X, nu_M, nu_R) = ({sym_min[1]:+.0f}, {sym_min[3]:+.0f}, "
      f"{sym_min[7]:+.0f}); free multiplicity {mmin}; chi weight at R: local {ext['local'][7][1]}, filtered {ext['filtered'][7][1]}")

# ============================================================ D
print('== D. exact ED, 2-cell twisted cluster {Gamma, Q0}: per cell 2 flavours x Weyl slot with the Z4 atom g(1 - |s><s|), '
      '|s> = (|0> + |F>)/sqrt2 (local zero, <c> = <cc> = 0); d(Q0) = deleted-slot kernel, hybridised by |V| (exact at w = 0); 4096 states')
NMd = 12; DIM = 1 << NMd; sts = np.arange(DIM)
def cop(i):
    m = ((sts >> i) & 1) == 1; s0 = sts[m]; sg = (-1.0) ** np.array([bin(int(x) & ((1 << i) - 1)).count('1') for x in s0])
    return sp.csr_matrix((sg, (s0 ^ (1 << i), s0)), shape=(DIM, DIM))
Cs = [cop(i) for i in range(NMd)]; cA, cB, cD = [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]
Nop = np.array([bin(int(x)).count('1') for x in sts]); Id = sp.identity(DIM, format='csr')
def atom(cell):
    P0, PF = Id, Id
    for i in cell: n_ = Cs[i].T @ Cs[i]; P0 = P0 @ (Id - n_); PF = PF @ n_
    Od = Cs[cell[0]].T @ Cs[cell[1]].T @ Cs[cell[2]].T @ Cs[cell[3]].T
    return Id - 0.5 * (P0 + PF + Od + Od.T)
ATOM = atom(cA) + atom(cB)
def psq(cell):   # 4-mode pair square -(Omega + Omega^+), Omega = c0 c1 c2 c3: the SU(4) x Z4 analogue of the Spin(10) pair square
    Od = Cs[cell[0]].T @ Cs[cell[1]].T @ Cs[cell[2]].T @ Cs[cell[3]].T; return -(Od + Od.T)
PSQ = psq(cA) + psq(cB)
hc = np.zeros((NMd, NMd))
for k in range(4): hc[cA[k], cD[k]] = 1 / np.sqrt(2); hc[cB[k], cD[k]] = -1 / np.sqrt(2)
hc = hc + hc.T                                              # |V| = 1: the cluster depends on g/|V| only (V = |V| x unitary, absorbed in d)
HFREE = sum(hc[i, j] * (Cs[i].T @ Cs[j]) for i in range(NMd) for j in range(NMd) if hc[i, j] != 0)
Um = np.zeros((NMd, NMd))
for k in range(4): Um[cA[k], k] = Um[cB[k], k] = Um[cA[k], 4 + k] = 1 / np.sqrt(2); Um[cB[k], 4 + k] = -1 / np.sqrt(2); Um[cD[k], 8 + k] = 1
hm = Um.T @ hc @ Um; Gc = np.diag([1.0] * 8 + [-1.0] * 4)   # basis s(Gamma), s(Q0), d; G' = +1 on slots, -1 on d
def cluster(g, wp=0.05, win=0.05, at=None):
    H = (HFREE + g * (ATOM if at is None else at)).tocsr(); sol = {}
    for qn in range(4):
        idx = np.where(Nop % 4 == qn)[0]; E, U = np.linalg.eigh(H[idx][:, idx].toarray().real); sol[qn] = (idx, E, U)
    E0 = min(sol[q][1][0] for q in sol); gs = [(q, k) for q in sol for k in range(len(sol[q][1])) if sol[q][1][k] < E0 + 1e-9]
    G = np.zeros((2, NMd, NMd), complex); wd, lowd = 0.0, 9e9
    for (q, k) in gs:
        idx, E, U = sol[q]; psi = np.zeros(DIM); psi[idx] = U[:, k]
        for sg in (1, -1):
            idq, Eq, Uq = sol[(q + sg) % 4]; dE = Eq - E0
            Amp = Uq.T @ np.array([((Cs[i].T if sg > 0 else Cs[i]) @ psi)[idq] for i in range(NMd)]).T
            for iw, w in enumerate((wp, -wp)):
                G[iw] += ((Amp.T / (1j * w - dE)) @ Amp) if sg > 0 else ((Amp.T / (1j * w + dE)) @ Amp)
            wdn = (np.abs(Amp[:, cD]) ** 2).sum(1); wd += wdn[dE < win].sum() / 4; lowd = min(lowd, dE[wdn > 1e-3].min())
    G /= len(gs); wd /= len(gs); Gm = [Um.T @ x @ Um for x in G]
    Sig = (1j * wp * np.eye(NMd) - hm) - np.linalg.inv(Gm[0]); Sp = np.real(np.diag(1j * wp * Sig))
    gaps = sorted(sol[q][1][0] - E0 for q in sol)
    return dict(off=np.abs(Sig[8:, :]).max(), chi=np.abs(Gc @ Gm[0] @ Gc + Gm[1]).max(), SG=Sp[:4].mean(), SQ=Sp[4:8].mean(),
                wd=wd, lowd=lowd, ngs=len(gs), g1=min(sol[(gs[0][0] + 1) % 4][1][0], sol[(gs[0][0] + 3) % 4][1][0]) - E0,
                g2=sol[(gs[0][0] + 2) % 4][1][0] - E0, gs_sector=gs[0][0])
GR = (0.3, 1.0, 2.0, 3.0, 5.0, 10.0, 30.0); CL = {g: cluster(g) for g in GR}
blk = np.where((sts >> 4) == 0)[0]; s_cell = np.zeros(16); s_cell[[0, 15]] = 1 / np.sqrt(2); d0 = []
for OP in (atom(cA), psq(cA)):
    E_, U_ = np.linalg.eigh(OP[blk][:, blk].toarray()); d0.append((E_[1] - E_[0], abs(U_[:, 0] @ s_cell)))
check('D0 THEOREM-CHECK one cell: |s> is the unique ground state of the flat atom and of the 4-mode pair square -(c0c1c2c3 + h.c.) '
      '(the SU(4) x Z4 analogue of the Spin(10) pair square), fermion gap g, G_cell = z/(z^2 - g^2): a local zero',
      all(abs(gp - 1) < 1e-12 and abs(ov - 1) < 1e-12 for gp, ov in d0), f'gaps {d0[0][0]:.3f}, {d0[1][0]:.3f}; overlaps {d0[0][1]:.6f}, {d0[1][1]:.6f}')
GP = (5.0, 7.0); CP = {g: cluster(g, at=PSQ) for g in GP}
gxp = float(np.exp(np.interp(0.0, np.log([CP[g]['SQ'] for g in GP]), np.log(GP))))
r_ = [CL[g] for g in GR]
check('D1 THEOREM-CHECK (C1) Sigma vanishes off the slot block; chiral inversion G(-iw) = -G\'G(iw)G\'; unique ground state (N = 0 mod 4) at every g',
      max(r['off'] for r in r_) < 1e-9 and max(r['chi'] for r in r_) < 1e-9 and all(r['ngs'] == 1 and r['gs_sector'] == 0 for r in r_),
      f"max {max(r['off'] for r in r_):.0e}, {max(r['chi'] for r in r_):.0e}")
lS = np.log([r['SQ'] for r in r_]); i_ = int(np.argmax(lS > 0)); gx = float(np.exp(np.interp(0.0, lS[i_ - 1:i_ + 1], np.log(GR[i_ - 1:i_ + 1]))))
fmt = lambda k, f: ', '.join(f.format(r[k]) for r in r_)
check('D2 DIAGNOSTIC g/|V| = ' + ', '.join(f'{g:g}' for g in GR) + ': the corner zero and the doubler release switch on together; '
      'the pair sector never softens below the single-particle gap (no Z4 -> Z2 breaking signal)',
      all(r['wd'] < 1e-3 for r in r_[:5]) and all(r['wd'] > 0.98 for r in r_[5:]) and 3 < gx < 10 and 3 < gxp < 10 and all(r['g2'] >= r['g1'] for r in r_),
      f"S(Q0)/V^2 {fmt('SQ', '{:.2g}')}; d weight below 0.05|V| {fmt('wd', '{:.3f}')}; gap/|V| {fmt('g1', '{:.3g}')}; pair gap/gap >= "
      f"{min(r['g2'] / r['g1'] for r in r_):.2f}; S(Q0) = V^2 at g = {gx:.1f}|V|; T2 1/(1+V^2/S) at g = 10, 30: "
      f"{1 / (1 + 1 / CL[10.0]['SQ']):.3f}, {1 / (1 + 1 / CL[30.0]['SQ']):.4f} vs {CL[10.0]['wd']:.3f}, {CL[30.0]['wd']:.4f}; pair-square atom: S = V^2 at {gxp:.1f}|V|")
print(f"   D3 ARTEFACT the cluster mirror level is dispersionless, so S(Gamma)/V^2 = {fmt('SG', '{:.2g}')} > 0 at every g: the 'both gapped' "
      f"window 0 < g < 5|V| (largest gap {max(r['g1'] for r in r_):.2f}|V|) is a finite-size effect, not evidence for or against SMG")

# ============================================================ E
print('== E. estimates and reading')
gxs = [gx * Vsv[q][0] for q in (XQ, MQ, RQ)]
def slot_ke(Q):
    H, rung, nodes, idx = Hlad(tk, RR, np.asarray(Q, float), KAP, MC, zoom, tk.X); top = idx[(RR, (0, 0, 0))]
    E, U = np.linalg.eigh(H); w = np.sum(np.abs(Vs.conj().T @ U[8 * top:8 * top + 8]) ** 2, 0); return float(np.sum(w * np.abs(E)) / 2)
KE = np.mean([slot_ke(2 * np.pi * np.array(m) / 6) for m in itertools.product(range(6), repeat=3)])
print(f'   E1 ESTIMATE corner zero onset Delta_f ~ {gx:.1f}|V(Q)| = {gxs[0]:.2f}, {gxs[1]:.2f}, {gxs[2]:.2f} (X, M, R; ladder units), i.e. pair '
      f'square g ~ {gxs[0] / 33.58:.3f}, {gxs[1] / 33.58:.3f}, {gxs[2] / 33.58:.3f} (Delta_f = 33.58 g, same local zero: smg-verify E1); the slot '
      f'kinetic energy, which sets any lattice-level mirror threshold, averages {KE:.2f} over the zone: no parametric window. An SMG far end '
      'needs the mirror cone to get its zero below the X onset with no local zero (C4) and no complete interpolator set (C5); the cone '
      'threshold needs lattices beyond ED and the limits: INCONCLUSIVE on existence')
print('   E2 READING Golterman-Shamir: C2 extends their strong-coupling doubling warning to every g at which the slot zero reaches a corner; '
      'by C5 their complete-interpolator premise cannot hold in a light-only phase here, so an SMG far end must carry irreducible zeros. '
      'Bilayer/staggered SMG (Slagle-You-Xu, He et al., Catterall SO(4)/Spin(7), Ayyar-Chandrasekharan) gaps every component of '
      'vector-like content with complete on-site composites and does not transfer; QMC-1 (2+1D filtered Spin(10)) saw GPR-like correlations')
print('supplied: the hybrid-wall ladder (zoom rate, X, kap, M = st, R = 1, the 16 in parallel), slot = P+ copy 2, the Z4 atom for the pair square, '
      '2 flavours, the w = 0 Schur truncation, probe w = window = 0.05|V|, g grid; assumed: analyticity of G(k, 0) off Gamma, unbroken translations')
print('cited: smg-verify (Delta_f, local zero), hybrid-wall B4/B7, CHIRALITY_LOCAL_ENDPOINT_ALGEBRA (pairing identity), QMC-1 archive, '
      'Golterman-Shamir 2505.20436, Slagle-You-Xu 1409.7401, He-Wu-You-Xu-Meng 2016, Catterall 1510.04153, Nielsen-Ninomiya')
print(f'elapsed {time.monotonic() - T0:.1f} s')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
