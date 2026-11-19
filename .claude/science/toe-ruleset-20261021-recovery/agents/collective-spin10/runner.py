#!/usr/bin/env python3
"""collective-spin10: which Spin(10)-invariant gapping terms of one Weyl 16 are atomic and which collective, and does a
point-split (cube-filtered) far-rung term avoid the smg-qmc corner releases? (supplied models; exact theorems, finite
diagnostics, mean-field diagnostics; mean field cannot establish symmetric mass generation)
 A  representation theory: Spin(10) invariants in Lambda^n of (16 x orbitals), by site support (exact)
 B  form factors of the 10-channel pair on the far rung (exact)
 C  the hybrid wall (R = 1, zoom rate, slot = P+ copy 2) with a 10-channel pair field: mean-field / Born diagnostics
 D  anomalous content (15 components) and register checks"""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from functools import reduce
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
print('== A. Spin(10) invariants (16 = +1 eigenspace of Z^5 in the five-qubit Clifford basis; M_a = (C gamma_a)|_+, C = YXYXY, as on main)')
Xp = np.array([[0, 1], [1, 0]], complex); Yp = np.array([[0, -1j], [1j, 0]]); Zp = np.diag([1., -1.]).astype(complex); I2 = np.eye(2)
kr = lambda *m: reduce(np.kron, m); gam = []
for k in range(5):
    gam.append(kr(*([I2] * k + [Xp] + [Zp] * (4 - k)))); gam.append(kr(*([I2] * k + [Yp] + [Zp] * (4 - k))))
ev = np.where(np.isclose(np.diag(kr(*[Zp] * 5)).real, 1))[0]
pairs = [(a, b) for a in range(10) for b in range(a + 1, 10)]
t = [(0.5j * gam[a] @ gam[b])[np.ix_(ev, ev)] for a, b in pairs]
Mv = [(kr(Yp, Xp, Yp, Xp, Yp) @ g)[np.ix_(ev, ev)] for g in gam]
cart = [i for i, x in enumerate(t) if np.abs(x - np.diag(np.diag(x))).max() < 1e-12]
wts = np.array([[t[i][a, a].real for i in cart] for a in range(16)])
vec_err = max(np.abs(t[i].T @ Mv[c] + Mv[c] @ t[i] - 1j * ((a == c) * Mv[b] - (b == c) * Mv[a])).max() for i, (a, b) in enumerate(pairs) for c in range(10))
rng = np.random.default_rng(7); phi = rng.normal(size=10); Pm = sum(p * m for p, m in zip(phi, Mv))
cliff = np.abs(Pm @ Pm.conj().T - phi @ phi * np.eye(16)).max()
check('A1 the 16: Casimir 45/4, M_a symmetric with zero diagonal, t^T M_c + M_c t = i(d_ac M_b - d_bc M_a) (10-vector), and the Clifford '
      'identity (phi.M)(phi.M)^+ = |phi|^2 for every real phi',
      np.abs(sum(x @ x for x in t) - 45 / 4 * np.eye(16)).max() < 1e-12 and max(np.abs(m - m.T).max() for m in Mv) < 1e-14
      and max(np.abs(np.diag(m)).max() for m in Mv) == 0 and vec_err < 1e-12 and cliff < 1e-12, f'vec {vec_err:.0e}, Clifford {cliff:.0e}')
# 16^{x4}: zero-weight Casimir kernel and its S4 character
Zs = [s for s in itertools.product(range(16), repeat=4) if np.allclose(wts[list(s)].sum(0), 0)]
zi = np.array([((s[0] * 16 + s[1]) * 16 + s[2]) * 16 + s[3] for s in Zs]); I16 = sp.identity(16, format='csr'); C4 = np.zeros((len(Zs),) * 2, complex)
for x in t:
    xs = sp.csr_matrix(x); T = sum(reduce(sp.kron, [xs if j == i else I16 for j in range(4)]) for i in range(4)).tocsc(); A = T[:, zi]
    C4 += (A.conj().T @ A).toarray()
w4, V4 = np.linalg.eigh(C4); K4 = V4[:, w4 < 1e-8]; posZ = {s: i for i, s in enumerate(Zs)}
def chi(p):
    Pq = np.zeros((len(Zs),) * 2)
    for i, s in enumerate(Zs): Pq[posZ[tuple(s[p[j]] for j in range(4))], i] = 1
    return round(float(np.trace(K4.conj().T @ Pq @ K4).real), 6)
ch = [K4.shape[1], chi((1, 0, 2, 3)), chi((1, 0, 3, 2)), chi((1, 2, 0, 3)), chi((1, 2, 3, 0))]
check('A2 THEOREM 16^{x4} has exactly 2 Spin(10) singlets, carrying the S4 irrep (2,2); so Lambda^4(16 x W)^Spin(10) = S_(2,2)(W): '
      'every charge-4 invariant is the unique Spin(10) tensor times an algebraic-curvature tensor on the orbitals, dim m^2(m^2-1)/12',
      ch == [2, 0, 2, -1, 0],
      f'zero-weight dim {len(Zs)}; character {ch}')
def lam_singlets(m, n):   # Casimir kernel on the zero-weight part of the N = n sector of 16*m CAR modes
    q = 16 * m; wq = np.tile(wts, (m, 1)); states = [s for s in itertools.combinations(range(q), n) if np.allclose(wq[list(s)].sum(0), 0)]
    if not states: return 0, 0
    allst = {s: i for i, s in enumerate(itertools.combinations(range(q), n))}; C2 = np.zeros((len(states),) * 2, complex)
    for x in t:
        nz = np.argwhere(np.abs(x) > 1e-12); r, c, v = [], [], []
        for j, s in enumerate(states):
            ss = set(s)
            for o in range(m):
                for a, b in nz:
                    A_, B_ = o * 16 + a, o * 16 + b
                    if B_ not in ss or (A_ != B_ and A_ in ss): continue
                    lst = list(s); sg = (-1) ** lst.index(B_); lst.remove(B_); ins = sum(1 for y in lst if y < A_); sg *= (-1) ** ins; lst.insert(ins, A_)
                    r.append(allst[tuple(lst)]); c.append(j); v.append(sg * x[a, b])
        A_ = sp.csr_matrix((v, (r, c)), shape=(len(allst), len(states))); C2 += (A_.conj().T @ A_).toarray()
    return len(states), int(np.sum(np.linalg.eigvalsh(C2) < 1e-8))
lam1 = {n: lam_singlets(1, n)[1] for n in range(17)}; lam2 = lam_singlets(2, 4)
check('A3 THEOREM (3+1D Pauli, the A4 analogue) one mode per flavour on a site: Lambda^n(16) has a Spin(10) singlet only for n = 0, 16; '
      'no charge-4, 8 or 12 invariant fits a site; single-site gapping only via the charge-16 atom on |0>, |F> (a local zero)',
      [n for n in lam1 if lam1[n]] == [0, 16] and all(lam1[n] in (0, 1) for n in lam1), f'singlet n: {[n for n in lam1 if lam1[n]]}')
s22 = lambda m: m * m * (m * m - 1) // 12; sup = [sum((-1) ** (s - u) * int(np.round(np.prod(range(s - u + 1, s + 1)) / max(1, np.prod(range(1, u + 1))))) * s22(u) for u in range(s + 1)) for s in range(1, 6)]
check('A4 THEOREM the Weyl slot (W = C^2, one cell) carries exactly one charge-4 invariant, the pair square (Fock count = S_(2,2)(C^2), '
      'a spinor singlet): the spinor lifts the 1+1D obstruction, atomicity is allowed. One orbital per site: invariants on exactly s '
      'sites number 0, 1, 3, 2, 0 (s = 1..5)', lam2[1] == 1 and s22(2) == 1 and sup == [0, 1, 3, 2, 0],
      f'Lambda^4(32): zero-weight dim {lam2[0]}, singlets {lam2[1]}; exact-support counts {sup}')

# ============================================================ B
print('== B. form factors of the 10-channel pair b^T (M_a x E) b on the far rung (b = slot, E the orbital pair kernel)')
Bq = np.array(list(itertools.product((0, 1), repeat=3))); TRIM = [np.pi * q.astype(float) for q in Bq]
print('   B1 THEOREM E(k)^T = -E(-k) (M_a symmetric): at a TRIM E is antisymmetric on the orbitals, so with one orbital per flavour it '
      'vanishes at all 8 TRIMs, Gamma included (p-wave only); on the Weyl slot E(Q) = f(Q) eps with f even')
Hd = np.array([[(-1) ** int(a @ b) for b in Bq] for a in Bq])     # TRIM values of prod_{i in S} cos k_i
star = np.array([[1, sum(np.cos(Q))] for Q in TRIM]); cube = np.linalg.solve(Hd.T, np.r_[1.0, np.zeros(7)])
star_ok = np.linalg.matrix_rank(star[1:]) == 2
fz = lambda k: np.prod(np.cos(np.asarray(k) / 2) ** 2)
grid = [np.array(k) * np.pi / 4 for k in itertools.product(range(-4, 5), repeat=3)]
zset = all((fz(k) < 1e-14) == (np.max(np.abs(k)) > np.pi - 1e-9) for k in grid)
check('B2 THEOREM even form factors with offsets in one cube: TRIM values are a Hadamard transform, so f = 0 at X, M, R with f(Gamma) = 1 '
      'forces f = prod cos^2(k_i/2) (mod terms vanishing at all TRIMs), the cube-averaged slot b~_x; a nearest-neighbour star cannot. '
      'Zero set of f: the zone faces (double zero)',
      star_ok and np.allclose(cube, 1 / 8) and zset, f'cube coefficients {np.round(cube, 4).tolist()[:2]}..., star rank on X..R {np.linalg.matrix_rank(star[1:])}')
L4 = 4; xs_ = np.array(list(itertools.product(range(L4), repeat=3))); worst = 0.0
for Q in TRIM[1:] + [np.array([np.pi, 0.7, 2.1])]:
    bQ = np.exp(-1j * xs_ @ Q) / np.sqrt(L4 ** 3)
    for x in xs_[:5]:
        bt = np.zeros(L4 ** 3); 
        for c in Bq: bt[np.ravel_multi_index(tuple((x + c) % L4), (L4,) * 3)] += 1 / 8
        worst = max(worst, abs(bQ @ bt))
ov = {d: float(np.prod([(2 - abs(di)) / 8 for di in d])) * 8 for d in ((1, 0, 0), (1, 1, 0), (1, 1, 1))}
check('B3 THEOREM (every coupling) {b(Q), b~_x^+} = 0 for Q with a component pi: all modes on the zone faces commute with H_int[b~], '
      'G = G_free there, X, M, R keep their free gaps, no corner zero (smg-qmc C2) and no local zero (C4). Neighbouring b~ overlap '
      '(1/16, 1/32, 1/64), so the terms do not commute: no atomic limit, a collective problem',
      worst < 1e-15 and np.allclose(list(ov.values()), [1 / 16, 1 / 32, 1 / 64]),
      f'max |{{b(Q), b~^+}}| {worst:.0e} on 4^3; overlaps {[round(v, 4) for v in ov.values()]}')

# ============================================================ C
print('== C. hybrid wall + 10-channel pair field Delta f(k) on the slot (BdG per Clifford pair; exact for a uniform field of any direction)')
tk = Tick(0.04); MC = tk.st; KAP = 0.5; g5 = tk.g5; Pp = (I8 + g5) / 2; RR = 1; Vs, Vk = span(Pp @ tk.P2); EPS = np.array([[0, 1], [-1, 0]], complex)
def lad(Q):
    H, rung, nodes, idx = Hlad(tk, RR, np.asarray(Q, float), KAP, MC, zoom, tk.X); n = H.shape[0]; top = idx[(RR, (0, 0, 0))]
    Ps = np.zeros((n, 2), complex); Ps[8 * top:8 * top + 8] = Vs; return H, Ps, nodes, idx
def bdg(Q, Dl, f):
    H, Ps, nodes, idx = lad(Q); Hm = lad(-np.asarray(Q, float))[0]; Dt = Dl * f(Q) * Ps @ EPS @ Ps.T
    return np.block([[H, Dt], [Dt.conj().T, -Hm.conj()]]), H.shape[0], Ps, nodes, idx
one = lambda Q: 1.0; DLS = (0.3, 1.0, 3.0, 10.0, 30.0); TQ = {'X': (1, 0, 0), 'M': (1, 1, 0), 'R': (1, 1, 1)}
gaps = {}
for nm, q in TQ.items():
    for fn, f in (('cell', one), ('cube', fz)):
        gaps[nm, fn] = [float(np.min(np.abs(np.linalg.eigvalsh(bdg(np.pi * np.array(q, float), Dl, f)[0])))) for Dl in (0.0,) + DLS]
Vc = {'X': 0.3157, 'M': 0.6138, 'R': 0.9701}
ok = all(abs(gaps[nm, 'cell'][-1] * 30 / Vc[nm] ** 2 - 1) < 0.02 and np.allclose(gaps[nm, 'cube'], gaps[nm, 'cube'][0], atol=1e-9) for nm in TQ)
check('C1 DIAGNOSTIC corners: a cell-local (atomic) pair field softens the gap to |V(Q)|^2/Delta; the cube filter keeps the free gap '
      'at every Delta (B3)', ok,
      'cell X/M/R at Delta = 0, 1, 30: ' + '; '.join(f"{gaps[nm, 'cell'][0]:.3f}, {gaps[nm, 'cell'][2]:.3f}, {gaps[nm, 'cell'][5]:.4f}" for nm in TQ)
      + ' | cube: ' + ', '.join(f"{gaps[nm, 'cube'][5]:.4f}" for nm in TQ))
B, n, Ps, nodes, idx = bdg(np.zeros(3), 1.0, fz); E, U = np.linalg.eigh(B); z = np.abs(E) < 1e-7
pw = float(np.sum(np.abs(U[:n, z]) ** 2)); sw = float(np.sum(np.abs(Ps.conj().T @ U[:n, z]) ** 2))
mE = float(np.mean(np.abs(E[np.sum(np.abs(Ps.conj().T @ U[:n]) ** 2, 0) > 0.4])))
Gl = Gp(RR, np.zeros(3), nodes, idx, I8); Gc = np.block([[Gl, 0 * Gl], [0 * Gl, -Gl.conj()]])
gerr = np.abs(Gc @ B @ Gc + B).max(); nu_c = float(np.trace(U[:, z].conj().T @ Gc @ U[:, z]).real)
Uz = U[:n, z]; Pz = np.linalg.svd(Uz)[0][:, :int(round(pw))]; nu_p = float(np.trace(Pz.conj().T @ Gl @ Pz).real)
check("C2 DIAGNOSTIC Gamma, Delta = 1, cube filter: 4 Nambu zero modes of physical weight 2 (the light), slot weight 0; the mirror sits "
      "at |E| = Delta. G'_c = G' + (-G'*) is kept; G'-index of the light -2, of the Nambu completion 0: C5 is met only via the light's "
      "hole, a gapless hidden mode", int(z.sum()) == 4 and abs(pw - 2) < 1e-6 and sw < 1e-12 and abs(mE - 1) < 1e-6 and gerr < 1e-8
      and abs(nu_c) < 1e-8 and abs(nu_p + 2) < 1e-6, f"weight {pw:.3f}, slot {sw:.0e}, mirror |E| {mE:.4f}, G'err {gerr:.0e}, nu {nu_p:+.2f}, nu_c {nu_c:+.2f}")
Lg = 6; zer, nod, offE, free_off = [], [], [], []
for k in itertools.product(range(Lg), repeat=3):
    Q = 2 * np.pi * np.array(k) / Lg; B, n, Ps, _, _ = bdg(Q, 1.0, fz); E, U = np.linalg.eigh(B)
    Gpp = ((U * (1 / (1e-4j - E))) @ U.conj().T)[:n, :n]; svs = np.linalg.svd(Gpp, compute_uv=False); smin = svs[-1]
    if k == (0, 0, 0): zrank = int(np.sum(svs < 1e-2))
    if smin < 1e-2: zer.append(k)
    if np.min(np.abs(E)) < 1e-3: nod.append(k)
    if k != (0, 0, 0): offE.append(np.min(np.abs(E)))
check('C3 DIAGNOSTIC 6^3 top-rung grid (Delta = 1, cube filter): the w = 0 zero of G sits only at Gamma (rank 2, on the slot), BdG '
      'nodes only at Gamma, no new gapless point: the zero set the register asks for, at mean-field level',
      zer == [(0, 0, 0)] and zrank == 2 and nod == [(0, 0, 0)] and min(offE) > 0.2, f'zeros {zer} (rank {zrank}), nodes {nod}, min |E| off Gamma {min(offE):.3f}')
Xq = np.array([np.pi, 0, 0]); soft = []
for d in (0.2, 0.1, 0.05):
    Q = Xq + d * np.array([-1, 0.37, 0.21]); H, Ps, _, _ = lad(Q); n = H.shape[0]; s = np.sqrt(30.0) * fz(Q)
    Hc = np.zeros((n + 2, n + 2), complex); Hc[:n, :n] = H; Hc[:n, n:] = s * Ps; Hc[n:, :n] = s * Ps.conj().T
    E, U = np.linalg.eigh(Hc); i = np.argmin(np.abs(E)); soft.append((d, abs(E[i]), float(np.sum(np.abs(U[:n, i]) ** 2))))
se = np.polyfit(np.log([x[0] for x in soft]), np.log([x[1] for x in soft]), 1)[0]; sw_ = np.polyfit(np.log([x[0] for x in soft]), np.log([x[2] for x in soft]), 1)[0]
check('C4 THEOREM-CHECK (3D smg-3450 C3) if the filtered slot zero is local in time (Sigma = |f|^2 S/iw, flat hidden level, the '
      'atomic shape), a branch E ~ |k-X|^5 of weight ~ |k-X|^4 reaches w = 0 at each corner: the filter protects the corners only '
      'if the hidden (composite) band disperses and is gapped there', abs(se - 5) < 0.3 and abs(sw_ - 4) < 0.3,
      f'S = 30: E slope {se:.2f}, weight slope {sw_:.2f}; E(0.05) = {soft[-1][1]:.1e}')
xi = 2.0; bres = []
for Lb in (6, 10):
    acc = []; ws = 0.0
    for k in itertools.product(range(Lb), repeat=3):
        q = 2 * np.pi * np.array(k) / Lb; w = np.exp(-xi ** 2 * np.sum(4 * np.sin(q / 2) ** 2) / 2); ws += w
        H, Ps, _, _ = lad(q); E, U = np.linalg.eigh(H); acc.append((k, w * fz(q) ** 2, E, Ps.T @ U.conj()))
    row = []
    for om in (1e-3, 1e-4):
        Sf = np.zeros((2, 2), complex); S0 = np.zeros((2, 2), complex)
        for k, w, E, A in acc:
            T = EPS @ ((A * (1 / (1j * om + E))) @ A.conj().T) @ EPS.conj().T * w / ws; Sf += T
            if k != (0, 0, 0): S0 += T
        row.append((np.abs(om * Sf).max(), np.abs(om * S0).max(), np.abs(S0 / om).max()))
    bres.append((Lb, 1 / ws, row))
ok = all(abs(r[2][1][0] - r[1]) / r[1] < 1e-3 and r[2][1][1] < 1e-5 for r in bres) and bres[1][1] < 0.3 * bres[0][1]
check('C5 DIAGNOSTIC (Born, pair field of correlation length 2 cells) the Gamma zero strength w*Sigma = Delta^2 w(q=0) comes only from '
      'the ordered q = 0 part (falls as L^-3); q != 0 gives Sigma ~ iw c, a Z-factor (mirror stays gapless): mean field gaps the mirror '
      'only through order; a symmetric-phase zero must be non-perturbative',
      ok, '; '.join(f'L={r[0]}: w0 {r[1]:.3f}, wS {r[2][1][0]:.3f}, wS(q!=0) {r[2][1][1]:.0e}, c {r[2][1][2]:.1f}' for r in bres))

# ============================================================ D
print('== D. anomalous content and register checks')
ker = []
for trial in range(20):
    ph = rng.normal(size=10); Pq = sum(p * m for p, m in zip(ph, Mv)); drop = trial % 16
    keep = [a for a in range(16) if a != drop]; sv = np.linalg.svd(Pq[np.ix_(keep, keep)] / np.linalg.norm(ph), compute_uv=False)
    ker.append((int(np.sum(sv < 1e-10)), round(float(sv[-2]), 6)))
check('D1 THEOREM 16 minus one component: for every pair direction the 15 x 15 pair matrix has exactly one zero singular value, so one '
      'Weyl component stays gapless at Gamma (the Z16 class of 15 Weyl fermions); the full 16 gaps for every direction (A1)',
      all(k == (1, 1.0) for k in ker), f'{ker[:3]}')
print('   D2 register: each b~ pair-square term spans one 2^3 block of top-rung cells (one CL-1 cube at rung R: finite range, inside the edge '
      "cone), is Spin(10) x Z4 invariant, G'-even on the slot (f even), keeps charge 4 only; not checked: electric backgrounds, the tick form")
print('supplied: the hybrid-wall ladder (R = 1, zoom, kap = 0.5, X = W(1-g5)/2, st = M = 0.04), slot = P+ copy 2, the 10-channel pair field '
      'and its amplitude/correlation ansatz, the cube filter, the flat-level strong-coupling ansatz, grids; assumed: translation invariance')
print('cited: smg-3450 A4/C3/D1, smg-qmc C2-C5, inversion-break C1-C3, SPIN10_SYMMETRIC_ATOMIC_GAPS (main, 2026-09-14), Golterman-Shamir')
print(f'elapsed {time.monotonic() - T0:.1f} s')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
