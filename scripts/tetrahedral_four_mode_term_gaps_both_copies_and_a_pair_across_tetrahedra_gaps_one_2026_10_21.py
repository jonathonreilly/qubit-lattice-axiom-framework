#!/usr/bin/env python3
"""Four-mode terms on the CL-2 cube: the tetrahedral top form versus the pair-across-tetrahedra (one-copy) term.

Supplied model: the CL-1/CL-2 Margolus tick (one fermion mode per site, spin-3/2 edge hop W, step st, mass mu) and supplied
four-mode terms added to it.  Sections:
 A  one cube (rung 0): which four-mode terms the 24 rotations, inversion and the mirror M = (odd rotation)(inversion) allow;
    the two light copies as eigen-pairs of the face-diagonal spin-3/2 hop F;
 B  zero momentum (0+1D): Fidkowski-Kitaev count on a tetrahedron's 8 Majoranas; which copy each term gaps;
 C  two-cube chain (4x2x2 torus, both tilings, 16 modes, 2^16 states, sparse) with the static stand-in h = i log(tick);
 D  rung 1 (2x2x2 cell = C^4 x C^2): the tetrahedral top form against SU(3) x SU(2) x U(1)_Y;
 E  anomaly bookkeeping (exact fractions);  F  estimates against measurement.
Finite diagnostics of supplied models; no physical identification.  Cited, not rederived: Z16 for Spin-Z4 in 3+1D,
symmetric-mass-generation existence, sphaleron washout factor, lattice proton-decay matrix element, measured bounds."""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/TETRAHEDRAL_FOUR_MODE_TERM_GAPS_BOTH_COPIES_AND_A_PAIR_ACROSS_TETRAHEDRA_GAPS_ONE_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from fractions import Fraction as Fr
import numpy as np
import scipy.sparse as sps
from scipy.linalg import expm, logm, null_space, schur
from scipy.sparse.linalg import eigsh

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max())
OM = np.exp(2j * np.pi / 3)

# ------------------------------------------------ the cube: corners, spin-3/2 phases, W, F, rotations, inversion, M
C = np.array(list(itertools.product((0, 1), repeat=3))); cc0 = C - 0.5
EVi = [i for i in range(8) if C[i].sum() % 2 == 0]; ODi = [i for i in range(8) if C[i].sum() % 2 == 1]
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
def hop(dist2, sign):
    H = np.zeros((8, 8), complex)
    for a in range(8):
        for b in range(8):
            if round(float(np.sum((C[a] - C[b]) ** 2))) == dist2: g = XI[a].conj() @ XI[b]; H[a, b] = sign * g / abs(g) / np.sqrt(3)
    return H
W = hop(1, -1.0); F = hop(2, 1.0)                       # edge hop (CL-2) and face-diagonal hop, same spin-3/2 phases
I8 = np.eye(8); S = np.diag([(-1.0) ** int(x.sum()) for x in C]).astype(complex)
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(R), 1): rots.append(R)
def axang(R):
    a = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((R + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(a)), a
def img(R, i): return int(np.argmin(np.sum(abs(cc0 - R @ cc0[i]), 1)))
def Grot(R):
    n_, a = axang(R); Dm = expm(-1j * a * sum(n_[k] * J3[k] for k in range(3))); G = np.zeros((8, 8), complex)
    for i in range(8): k = img(R, i); G[k, i] = XI[k].conj() @ Dm @ XI[i]
    return G
Gs = [Grot(R) for R in rots]; ODD = [nrm(G @ S @ G.conj().T - S) > 1e-9 for G in Gs]
iC3 = [i for i, R in enumerate(rots) if abs(np.trace(R)) < 1e-9 and np.allclose(axang(R)[0], np.ones(3) / np.sqrt(3))][0]
Pi = np.zeros((8, 8))
for i in range(8): Pi[img(-np.eye(3), i), i] = 1
ph = {0: 1.0 + 0j}
while len(ph) < 8:
    for a in list(ph):
        for b in range(8):
            if b not in ph and abs(W[a, b]) > 0:
                ia, ib = int(np.argmax(Pi[:, a])), int(np.argmax(Pi[:, b])); ph[b] = np.conj(W[ia, ib] / (ph[a] * W[a, b]))
Pinv = Pi @ np.diag([ph[i] for i in range(8)]); iodd = ODD.index(True); M = Gs[iodd] @ Pinv
def ex(th): return np.cos(th) * I8 + 1j * np.sin(th) * W   # exp(i th W)
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def Ut(K, st, mu=0.0): return Dg(K).conj().T @ ex(st + mu / 2) @ Dg(K) @ ex(-(st - mu / 2))   # even cubes, then odd cubes
# exterior powers: Lambda^4 of C^8 on the 70 sorted 4-subsets (vectorised 4x4 minors)
subs = list(itertools.combinations(range(8), 4)); SUBS = np.array(subs)
def L4(G):
    Mx = G[SUBS[:, None, :, None], SUBS[None, :, None, :]]; return np.linalg.det(Mx)        # [row-subset, col-subset]
def vec4(U): return np.array([np.linalg.det(U[list(R), :]) for R in subs])                # top form of span(U)
def pairs(T, sgn):
    w, v = np.linalg.eigh(F[np.ix_(T, T)]); B = np.zeros((8, 2), complex); B[T, :] = v[:, np.isclose(w, sgn)]; return B
s3 = -S @ F; PA = (I8 + s3) / 2; PB = (I8 - s3) / 2
UA = np.hstack([pairs(EVi, -1), pairs(ODi, 1)]); UB = np.hstack([pairs(EVi, 1), pairs(ODi, -1)])
Oe, Oo = vec4(I8[:, EVi]), vec4(I8[:, ODi]); OA, OB = vec4(UA), vec4(UB)

# ===================================== A. one cube: allowed four-mode terms =====================================
print('== A. one cube (rung 0): tetrahedral top forms, copies, mirror')
L4s = [L4(G) for G in Gs]; LP, LM = L4(Pinv), L4(M)
inv = null_space(np.vstack([A - np.eye(70) for A in L4s])); Tinv = null_space(np.vstack([A - np.eye(70) for A, o in zip(L4s, ODD) if not o]))
ev_e = [complex(A[:, subs.index(tuple(EVi))] @ Oe) for A, o in zip(L4s, ODD) if not o]
odd_img = [(complex(Oo @ A @ Oe), complex(Oe @ A @ Oo)) for A, o in zip(L4s, ODD) if o]
pm = np.linalg.eigvals(inv.conj().T @ LP @ inv); mE, mO = complex(Oe @ LM @ Oe), complex(Oo @ LM @ Oo)
Kr = np.random.default_rng(5).uniform(-np.pi, np.pi, 3); Mcov = max(nrm(M @ Ut(Kr, st, mu) @ M.conj().T - Ut(-(rots[iodd] @ Kr), st, mu)) for st, mu in ((np.pi / 2, 0), (0.3, .2), (0.04, .1)))
check('A1 [theorem] a tetrahedron has one four-mode term (top form O_e, O_o); the 12 even turns fix each (det 1), the 12 odd turns swap them, so O_e + O_o is the only '
      'rotation-covariant one (O_e - O_o is A2); inversion swaps them; M fixes both with one phase, so M survives every tetrahedral term',
      inv.shape[1] == 7 and Tinv.shape[1] == 10 and np.allclose(ev_e, 1) and np.allclose([complex(Oo @ A @ Oo) for A, o in zip(L4s, ODD) if not o], 1) and np.allclose(odd_img, 1) and abs(Oo @ LP @ Oe - 1) < 1e-9 and abs(mE - 1) < 1e-9 and abs(mO - 1) < 1e-9 and Mcov < 1e-12,
      f'Lambda^4: 70 terms, 7 rotation-invariant ({int(np.sum(np.isclose(pm, 1)))} M-even, {int(np.sum(np.isclose(pm, -1)))} M-odd), 10 tetrahedral-invariant; M phases {mE.real:+.0f}, {mO.real:+.0f}; M U(K) M^+ = U(-R K) to {Mcov:.0e}')
cop = {}
for st in (np.pi / 2, 0.3, 0.04):
    def H(q): return 1j * logm(Ut(q, st))
    al = []
    for a in range(3):
        e = np.zeros(3); e[a] = 1e-5; A_ = (H(e) - H(-e)) / 2e-5; al.append((A_ + A_.conj().T) / 2)
    v = np.sqrt(np.trace(al[0] @ al[0]).real / 8); al = [x / v for x in al]; g5 = -1j * al[0] @ al[1] @ al[2]; g5 = (g5 + g5.conj().T) / 2
    Sig = [-1j * al[1] @ al[2], -1j * al[2] @ al[0], -1j * al[0] @ al[1]]; L = Gs[iC3]
    Mr = np.array([[np.trace(L @ al[a] @ L.conj().T @ al[b]).real / 8 for b in range(3)] for a in range(3)]); nn, ang = axang(np.round(Mr).T)
    errs = [(max(nrm(Sx @ al[q] @ Sx.conj().T - L @ al[q] @ L.conj().T) for q in range(3)), Sx) for Sx in
            [expm(-1j * s_ * ang / 2 * sum(nn[k] * Sig[k] for k in range(3))) for s_ in (1, -1)]]
    Sx = min(errs, key=lambda t: t[0])[1]; rho = Sx.conj().T @ L; w_, V_ = np.linalg.eig(rho)
    Vl = V_[:, np.abs(w_ - OM) < 1e-5]; P1 = Vl @ np.linalg.pinv(Vl); P1 = (P1 + P1.conj().T) / 2
    cop[st] = (nrm(P1 - PA), nrm(S - g5 @ s3), nrm(g5 + F), float(np.trace(np.diag(np.diag(S).real > 0) @ P1).real))
kd = np.array([.3, .5, .81]); slope = {st: np.log2(nrm(s3 @ Ut(.04 * kd, st) - Ut(.04 * kd, st) @ s3) / nrm(s3 @ Ut(.02 * kd, st) - Ut(.02 * kd, st) @ s3)) for st in (np.pi / 2, 0.04)}
check('A2 [theorem] the two light copies (C3 character w, w^2) are the eigenspaces of s3 = -S F, F the face-diagonal spin-3/2 hop (F^2 = 1, [F,S] = 0, {F,W} = 0); s3 commutes '
      'with W and every [C_a, W], so with the light algebra at every step (broken at O(K^2)); each tetrahedron holds one F-pair of each copy; S = g5 s3 (g5 = -F) at step pi/2',
      all(c[0] < 1e-8 and abs(c[3] - 2) < 1e-8 for c in cop.values()) and nrm(F @ F - I8) < 1e-12 and nrm(F @ S - S @ F) < 1e-12 and nrm(F @ W + W @ F) < 1e-12
      and cop[np.pi / 2][1] < 1e-8 and cop[np.pi / 2][2] < 1e-8 and cop[0.04][1] > 0.5
      and max(nrm(s3 @ (np.diag(C[:, a] * 1.0) @ W - W @ np.diag(C[:, a] * 1.0)) - (np.diag(C[:, a] * 1.0) @ W - W @ np.diag(C[:, a] * 1.0)) @ s3) for a in range(3)) < 1e-12 and all(abs(x - 2) < 0.05 for x in slope.values()),
      'copies vs -SF: ' + ', '.join(f'{c[0]:.0e}' for c in cop.values()) + f' (steps pi/2, .3, .04); |[s3,U(K)]| slope {slope[0.04]:.2f}; |S - g5 s3| = {cop[0.3][1]:.2f}, {cop[0.04][1]:.2f} at .3, .04')
def char(vec, A): return complex(vec.conj() @ A @ vec / (vec.conj() @ vec))
c3 = [round(np.angle(char(x, L4s[iC3])) / (2 * np.pi / 3)) % 3 for x in (Oe, Oo, OA, OB)]
pr = lambda X, Y: abs(abs(complex(X.conj() @ Y)) - np.linalg.norm(X) * np.linalg.norm(Y)) < 1e-9
oddmap = all(pr(L4s[i] @ Oe, Oo) and pr(L4s[i] @ OA, OB) for i in range(24) if ODD[i])
def hom(P1_, P2_, Gset):
    U1 = np.linalg.svd(P1_)[0][:, :4]; U2 = np.linalg.svd(P2_)[0][:, :4]
    return null_space(np.vstack([np.kron(U1.conj().T @ G @ U1, (U2.conj().T @ G @ U2).conj()) - np.eye(16) for G in Gset])).shape[1]
Ev = [G for G, o in zip(Gs, ODD) if not o]
chiB = [np.linalg.det(UB.conj().T @ G @ UB) for G in Ev]
nsB = null_space(np.vstack([L4s[i] - cb * np.eye(70) for i, cb in zip([i for i in range(24) if not ODD[i]], chiB)]))
dimB = nsB.shape[1]; dimBi = int(np.sum(np.isclose(np.linalg.eigvals(nsB.conj().T @ LP @ nsB), 1)))
check('A3 [theorem] pair products: O_e = (B-pair)(A-pair) of one tetrahedron; O_A, O_B = one F-pair from each tetrahedron = top form of one copy. C3 charges (1,1,w,w^2); '
      'odd turns swap O_e<->O_o, O_A<->O_B; inversion fixes O_A, O_B; M fixes O_e, O_o, swaps O_A<->O_B; the 12 even turns forbid all copy-mixing bilinears',
      c3 == [0, 0, 1, 2] and oddmap and pr(LP @ OA, OA) and pr(LP @ OB, OB) and pr(LM @ OA, OB) and pr(LM @ Oe, Oe) and pr(LM @ Oo, Oo)
      and hom(PA, PB, Ev) == 0 and hom(PA, PB, [Gs[iC3]]) == 4 and hom(PA, PA, Ev) == 4 and dimB == 6 and dimBi == 4,
      f'C3 alone would allow 4 mixing bilinears; terms with the character of O_B: {dimB} ({dimBi} inversion-even), O_B the only one-copy one')

# ===================================== B. zero momentum (0+1D) =====================================
print('== B. K = 0 (0+1D): Fidkowski-Kitaev and which copy is gapped')
sz = np.diag([1., -1]); aa = np.array([[0, 1], [0, 0]], float)
def ferm(n):
    ops = []
    for i in range(n):
        o = np.array([[1.0]])
        for M_ in [sz] * i + [aa] + [np.eye(2)] * (n - i - 1): o = np.kron(o, M_)
        ops.append(o.astype(complex))
    return ops
k0 = max(nrm(Ut(np.zeros(3), st) - I8) for st in (np.pi / 2, 0.3, 0.04))
e4 = ferm(4); gam = []
for c_ in e4: gam += [c_ + c_.conj().T, -1j * (c_ - c_.conj().T)]
rr = np.random.default_rng(3); z8 = {}
for n in (2, 4, 6, 8):
    Hm = np.zeros((16, 16), complex)
    for k in (4, 8):
        for ids in itertools.combinations(range(n), k):
            X = np.eye(16, dtype=complex)
            for i in ids: X = X @ gam[i]
            Hm += rr.normal() * X
    ev = np.linalg.eigvalsh((Hm + Hm.conj().T) / 2); z8[n] = int(np.sum(ev < ev[0] + 1e-9)) // 2 ** ((8 - n) // 2)
O4 = e4[0].conj().T @ e4[1].conj().T @ e4[2].conj().T @ e4[3].conj().T; Ht = O4 + O4.conj().T; wt = {}
for ids in itertools.chain.from_iterable(itertools.combinations(range(8), k) for k in range(9)):
    X = np.eye(16, dtype=complex)
    for i in ids: X = X @ gam[i]
    cf = np.trace(X.conj().T @ Ht) / 16
    if abs(cf) > 1e-12: wt.setdefault(len(ids), []).append(cf)
check('B1 [theorem] K = 0 tick = 1 at mu = 0 (8 zero modes, every step); on a tetrahedron (8 Majoranas, even under the antiunitary c -> c^dag) generic invariant '
      'interactions leave a unique state only for 8 Majoranas (Z8); top form + h.c. is a real quartic Majorana term: the FK term',
      k0 < 1e-12 and z8 == {2: 2, 4: 2, 6: 2, 8: 1} and list(wt) == [4] and max(abs(np.imag(x)) for x in wt[4]) < 1e-12, f'degeneracies {z8}; Majorana orders in top form {sorted(wt)}')
V = np.hstack([UA, UB]); d = ferm(8); cdag = [sum(np.conj(V[t, k]) * d[k].conj().T for k in range(8)) for t in range(8)]
def prod(ops):
    out = np.eye(256, dtype=complex)
    for o in ops: out = out @ o
    return out
FOe, FOo = prod([cdag[t] for t in EVi]), prod([cdag[t] for t in ODi]); FOB = prod([d[k].conj().T for k in range(4, 8)])
res = {}
for nm, Hm in (('tetra', -(FOe + FOo + (FOe + FOo).conj().T)), ('e only', -(FOe + FOe.conj().T)), ('copy B', -(FOB + FOB.conj().T))):
    w, v = np.linalg.eigh(Hm); g0 = int(np.sum(w < w[0] + 1e-9)); Sx = 0.0
    if g0 == 1:
        rho = v[:, 0].reshape(16, 16) @ v[:, 0].reshape(16, 16).conj().T; e_ = np.linalg.eigvalsh(rho); e_ = e_[e_ > 1e-12]; Sx = float(-(e_ * np.log(e_)).sum())
    res[nm] = (g0, w[g0] - w[0], Sx)
cs = [sum(V[t, k] * d[k] for k in range(8)) for t in range(8)]
GW = expm(1j * 0.37 * sum(W[i, j] * cs[i].conj().T @ cs[j] for i in range(8) for j in range(8)))
comm = (nrm(GW @ FOB - FOB @ GW), nrm(GW @ FOe - FOe @ GW))
check('B2 [theorem] one cube, K = 0: g(O_e + O_o + h.c.) has a unique ground state (both copies gapped; copy A carries 2 ln 2 entanglement); g(O_B + h.c.) leaves '
      'exactly 2^4 states = copy A free x copy B unique, gap g; tr(W P_B) = 0, so O_B commutes with every free half-tick, O_e does not',
      res['tetra'][0] == 1 and abs(res['tetra'][2] - 2 * np.log(2)) < 1e-9 and res['e only'][0] == 16 and res['copy B'][0] == 16 and abs(res['copy B'][1] - 1) < 1e-9
      and abs(np.trace(W @ PB)) < 1e-12 and comm[0] < 1e-10 and comm[1] > 0.1,
      f"(degeneracy, gap): tetra ({res['tetra'][0]}, {res['tetra'][1]:.3f}), one tetrahedron ({res['e only'][0]}, {res['e only'][1]:.3f}), copy B ({res['copy B'][0]}, {res['copy B'][1]:.3f}); |[G(e^iW), O]| {comm[0]:.0e} / {comm[1]:.2f}")

# ===================================== C. two-cube chain =====================================
print('== C. two-cube chain (4x2x2 torus, both tilings, 16 modes, sparse 2^16)')
Lx, Ly, Lz = 4, 2, 2; NS = Lx * Ly * Lz
def sid(x, y, z): return ((x % Lx) * Ly + (y % Ly)) * Lz + (z % Lz)
def corner(i):
    x, r = divmod(i, Ly * Lz); y, z = divmod(r, Lz); return 4 * (x % 2) + 2 * (y % 2) + (z % 2)
cubes = [[sid(o[0] + c[0], o[1] + c[1], o[2] + c[2]) for c in C] for o in ((0, 0, 0), (2, 0, 0), (1, 1, 1), (3, 1, 1))]
def layer(cbs):
    Mx = np.zeros((NS, NS), complex)
    for cb in cbs:
        ix = np.array(cb); cr = [corner(i) for i in cb]; Mx[np.ix_(ix, ix)] = W[np.ix_(cr, cr)]
    return Mx
WA, WB = layer(cubes[:2]), layer(cubes[2:])
popc = np.array([bin(s).count('1') for s in range(1 << NS)], np.int64); sectors = [np.nonzero(popc % 4 == r)[0] for r in range(4)]
def below(s, a): return popc[s & ((1 << a) - 1)]
def build(sec, h, terms, sec_out=None):     # sparse block of sum h_ij c+_i c_j + sum (coef * c+c+c+c+ + h.c.), memory-light
    st = sectors[sec]; pos = -np.ones(1 << NS, np.int64); pos[st] = np.arange(len(st)); Hs = sps.csr_matrix((len(st), len(st)), dtype=complex)
    for i in range(NS):
        R_, C_, V_ = [], [], []
        for j in range(NS):
            if abs(h[i, j]) < 1e-12: continue
            if i == j:
                k = np.nonzero((st >> i) & 1)[0]; R_.append(k); C_.append(k); V_.append(np.full(len(k), h[i, i])); continue
            ok = ((st >> j) & 1) == 1; sg = np.where(below(st, j) % 2 == 0, 1.0, -1.0); s = st & ~(1 << j)
            ok &= ((s >> i) & 1) == 0; sg = sg * np.where(below(s, i) % 2 == 0, 1.0, -1.0); s = s | (1 << i)
            R_.append(pos[s[ok]]); C_.append(np.nonzero(ok)[0]); V_.append(h[i, j] * sg[ok])
        if R_: Hs = Hs + sps.csr_matrix((np.concatenate(V_), (np.concatenate(R_), np.concatenate(C_))), shape=Hs.shape)
    R_, C_, V_ = [], [], []
    for coef, seq in terms:
        s = st.copy(); sg = np.ones(len(s)); ok = np.ones(len(s), bool)
        for a in reversed(seq):
            ok &= ((s >> a) & 1) == 0; sg *= np.where(below(s, a) % 2 == 0, 1.0, -1.0); s = s | (1 << a)
        r = pos[s[ok]]; c = np.nonzero(ok)[0]; v = coef * sg[ok]; R_ += [r, c]; C_ += [c, r]; V_ += [v, np.conj(v)]
    if R_: Hs = Hs + sps.csr_matrix((np.concatenate(V_), (np.concatenate(R_), np.concatenate(C_))), shape=Hs.shape)
    return Hs
def annih(phi, sec_in):                    # a(phi) = sum conj(phi_i) c_i from sector sec_in to sec_in - 1
    st = sectors[sec_in]; so = sectors[(sec_in - 1) % 4]; pos = -np.ones(1 << NS, np.int64); pos[so] = np.arange(len(so)); R_, C_, V_ = [], [], []
    for i in range(NS):
        ok = ((st >> i) & 1) == 1; sg = np.where(below(st, i) % 2 == 0, 1.0, -1.0)
        R_.append(pos[(st & ~(1 << i))[ok]]); C_.append(np.nonzero(ok)[0]); V_.append(np.conj(phi[i]) * sg[ok])
    return sps.csr_matrix((np.concatenate(V_), (np.concatenate(R_), np.concatenate(C_))), shape=(len(so), len(st)))
def terms(kind, g, cbs=None):
    out = []
    for cb in (cubes if cbs is None else cbs):
        cr = {corner(i): i for i in cb}
        if kind == 'tetra': out += [(-g, [cr[c] for c in EVi]), (-g, [cr[c] for c in ODi])]
        else: out += [(-g * dd, [cr[c] for c in R]) for R, dd in zip(subs, OB) if abs(dd) > 1e-12]
    return out
chain = {}; spq = {}
for st in (np.pi / 2, 0.04):
    u = expm(1j * st * WB) @ expm(-1j * st * WA); Tm, Z = schur(u, output='complex'); h = Z @ np.diag(-np.angle(np.diag(Tm))) @ Z.conj().T
    spq[st] = np.round(np.sort(np.abs(np.linalg.eigvalsh(h))), 4)
    for kind in ('tetra', 'copyB'):
        allE = []
        for sec in range(4):
            allE += [(x, sec) for x in eigsh(build(sec, h, terms(kind, 1.0)), k=20, which='SA', tol=1e-10, return_eigenvectors=False)]
        allE.sort(); E0 = allE[0][0]; gs = [s for x, s in allE if x < E0 + 1e-7]
        chain[st, kind] = (len(gs), allE[len(gs)][0] - E0, [gs.count(r) for r in range(4)])
check('C1 free 16-mode tick: 8 zero modes (uniform, K = 0) and the K = (pi,0,0) modes at |w| = arccos(1/3) (step pi/2), ~1.15 st (step .04)',
      all(np.allclose(spq[st][:8], 0) for st in spq) and np.allclose(spq[np.pi / 2][8:], np.arccos(1 / 3), atol=1e-4) and abs(spq[0.04][8] - 0.0462) < 1e-3, f'|w| = {spq[np.pi/2][8]}, {spq[0.04][8]}')
check('C2 [finite] H = h + g sum_cubes(term + h.c.), g = 1, all N mod 4: the tetrahedral term leaves a unique gapped ground state; the one-copy term leaves exactly '
      '16 states (uniform copy-A modes, 2/4/6/4 over N mod 4) and gaps the rest',
      all(chain[st, 'tetra'][0] == 1 and chain[st, 'copyB'][0] == 16 and chain[st, 'copyB'][2] == [2, 4, 6, 4] and min(chain[st, 'tetra'][1], chain[st, 'copyB'][1]) > 0.05 for st in spq),
      'gaps (tetra, copy B): ' + '; '.join(f'step {st:.2f}: {chain[st, "tetra"][1]:.3f}, {chain[st, "copyB"][1]:.3f}' for st in spq) + f'  [{time.monotonic() - T0:.0f} s]')

from scipy.sparse.linalg import expm_multiply
st = 0.04; rngC = np.random.default_rng(11); fl = {}
phis = [np.array([UA[corner(i), k] for i in range(NS)]) / np.sqrt(2) for k in range(4)]
for kind in ('tetra', 'copyB'):
    Hq = {}
    for sec in (0, 1):
        for q, cb in enumerate(cubes):
            hq = np.zeros((NS, NS), complex); ix = np.array(cb); cr = [corner(i) for i in cb]; hq[np.ix_(ix, ix)] = (st if q < 2 else -st) * W[np.ix_(cr, cr)]
            Hq[sec, q] = build(sec, hq, terms(kind, 1.0, [cb]))
    def UF(v, sec):
        for q in range(4): v = expm_multiply(-1j * Hq[sec, q], v)
        return v
    psi = rngC.normal(size=len(sectors[1])) + 1j * rngC.normal(size=len(sectors[1])); psi /= np.linalg.norm(psi)
    fl[kind] = max(np.linalg.norm(UF(annih(ph_, 1) @ psi, 0) - annih(ph_, 1) @ UF(psi, 1)) for ph_ in phis)
check('C3 [finite] Floquet form, term inside each cube unitary exp(-i(st W + g T)), step .04: the uniform copy-A modes commute with the interacting tick '
      'for the one-copy term (light copy exactly free at K = 0), not for the tetrahedral term', fl['copyB'] < 1e-9 and fl['tetra'] > 1e-2,
      f"max |U a - a U| on random states: one-copy {fl['copyB']:.0e}, tetrahedral {fl['tetra']:.2f}  [{time.monotonic() - T0:.0f} s]")

# ===================================== D. rung 1: the tetrahedral top form against the Standard Model group =====================================
print('== D. rung 1: one 2x2x2 cell = C^4 (body diagonals) x C^2 (tetrahedron parity)')
uu = np.ones(4) / 2; Bq = np.vstack([uu, np.array([[1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]]) / 2.0]).T
gm = []
for i in range(3):
    for j in range(i + 1, 3):
        X = np.zeros((3, 3), complex); X[i, j] = X[j, i] = 1; gm.append(X)
        Y = np.zeros((3, 3), complex); Y[i, j] = -1j; Y[j, i] = 1j; gm.append(Y)
gm += [np.diag([1, -1, 0]).astype(complex), np.diag([1, 1, -2]).astype(complex) / np.sqrt(3)]
def emb3(X):
    E = np.zeros((4, 4), complex); E[1:, 1:] = X; return Bq @ E @ Bq.T
BL = (np.eye(4) - 4 * np.outer(uu, uu)) / 3; sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]])
Tg = [np.kron(np.eye(4), t) for t in (np.diag([.5, -.5]).astype(complex), sy / 2, sx / 2)]   # T3 = X/2 (X swaps the tetrahedra)
col = [np.kron(emb3(X), np.eye(2)) for X in gm]; Ye = np.kron(BL / 2, np.eye(2)); Yo = Ye + Tg[2]
def dL4(X, e=1e-5): return (L4(expm(1j * e * X)) - L4(expm(-1j * e * X))) / (2j * e)
nsE = null_space(np.vstack([dL4(X) for X in col + Tg + [Ye]]), rcond=1e-7); nsO = null_space(np.vstack([dL4(X) for X in col + [Yo]]), rcond=1e-7)
NL, BLg = dL4(np.eye(8)), dL4(np.kron(BL, np.eye(2))); qn = [(round((v.conj() @ NL @ v).real, 6), round((v.conj() @ BLg @ v).real, 6)) for v in nsO.T]
tv = np.zeros(70, complex); tv[subs.index((0, 2, 4, 6))] = 1                     # one t on all four diagonals
cas = (tv @ sum(dL4(X) @ dL4(X) for X in Tg) @ tv).real; wY, UY = np.linalg.eigh(dL4(Yo)); yc = {}
for wi, ui in zip(wY, UY.T): yc[round(wi, 6) + 0.0] = yc.get(round(wi, 6) + 0.0, 0) + abs(ui.conj() @ tv) ** 2
yc = {float(k): round(float(v), 4) for k, v in yc.items() if v > 1e-9}
check('D1 [theorem] the intra-cell tetrahedral top form is a colour singlet, B - L = 0, but weak isospin 2 (T3 = X/2) and on odd cells hypercharge -2..2: it breaks SU(2)_L '
      'or U(1)_Y. Invariant four-mode terms of a cell: none on even cells, two on odd cells (uude, uddn), both dN = 4, d(B-L) = 0',
      nsE.shape[1] == 0 and nsO.shape[1] == 2 and all(q == (4.0, 0.0) for q in qn) and abs(cas - 6) < 1e-6 and max(abs(dL4(X) @ tv).max() for X in col) < 1e-9
      and yc == {-2.0: 0.0625, -1.0: 0.25, 0.0: 0.375, 1.0: 0.25, 2.0: 0.0625},
      f'Casimir {cas:.0f}; Y weights {list(yc.values())}; under CL-5 the literal term deletes the W and hypercharge links')

# ===================================== E. anomaly bookkeeping =====================================
print('== E. anomalies of the residual Z4 (left-handed Weyl basis, exact fractions)')
fam = [('Q', 1, Fr(1, 6), Fr(1, 3), 2, 3), ('u^c', -1, Fr(-2, 3), Fr(-1, 3), 1, 3), ('d^c', -1, Fr(1, 3), Fr(-1, 3), 1, 3),
       ('L', 1, Fr(-1, 2), Fr(-1), 2, 1), ('e^c', -1, Fr(1), Fr(1), 1, 1), ('n^c', -1, Fr(0), Fr(1), 1, 1)]   # (name, N, Y, B-L, dim SU2, dim SU3)
def anom(fs):
    m = lambda f: f[4] * f[5]
    X = {f[0]: 5 * f[3] - 4 * f[2] for f in fs}
    return dict(SU2=sum(f[1] * f[5] for f in fs if f[4] == 2), SU3=sum(f[1] * f[4] * (1 if f[5] == 3 else 0) for f in fs if f[5] == 3),
                Y2=sum(m(f) * f[1] * (6 * f[2]) ** 2 for f in fs), grav=sum(m(f) * f[1] for f in fs),
                nuN=sum(m(f) for f in fs if f[1] == 1) - sum(m(f) for f in fs if f[1] == -1), nuX=sum(m(f) for f in fs if X[f[0]] % 4 == 1) - sum(m(f) for f in fs if X[f[0]] % 4 == 3),
                X=X, NY2=sum(m(f) * f[1] * f[2] ** 2 for f in fs), NSU2=sum(Fr(f[1] * f[5], 2) for f in fs if f[4] == 2))
a, a15 = anom(fam), anom(fam[:-1])
ident = all((a['X'][f[0]] - f[1]) % 4 == (0 if f[4] == 2 else 2) for f in fam)
check('E1 [theorem] on every Weyl field X = 5(B-L) - 4Y = 1 mod 4 and exp(i pi X/2) = exp(i pi N/2)(-1)^F z_SU(2): the residual Z4 of mode number is the Spin-Z4 symmetry up to gauge',
      ident and all(x.denominator == 1 and int(x) % 4 == 1 for x in a['X'].values()), f'N - X mod 4 = 0 on doublets, 2 on singlets')
check('E2 [theorem] per family with n^c: U(1)_N anomalies N-Y^2 = -2, N-SU(2)^2 = 2; Z4 anomalies SU(2)^2: 4 = 0 mod 4, SU(3)^2: 0, (6Y)^2: -72 = 0 mod 4, gravity: 0; '
      'Z16 index 0 (N) and 16 = 0 mod 16 (X); without n^c 1 and 15: so a family is symmetric-gappable only with n^c, and Z_k of N survives instantons iff k | 4 (Z4 or Z2)',
      a['NY2'] == -2 and a['NSU2'] == 2 and a['SU2'] % 4 == 0 and a['SU3'] == 0 and a['Y2'] == -72 and a['Y2'] % 4 == 0 and a['grav'] == 0 and a['nuN'] % 16 == 0 and a['nuX'] == 16
      and a15['nuN'] == 1 and a15['nuX'] == 15 and a15['grav'] == 1 and [k for k in range(1, 9) if 4 % k == 0] == [1, 2, 4])
rules = {'p -> e+ pi0 (dB,dL)=(-1,-1)': (-1, -1), 'p -> e- pi+ pi+ (-1,+1)': (-1, 1), 'n-nbar (-2,0)': (-2, 0), '0nubb/Majorana (0,2)': (0, 2), 'nu_R^4 (0,4)': (0, 4)}
allowed = {k: (3 * b + l) % 4 == 0 for k, (b, l) in rules.items()}
check('E3 [theorem] Z4 selection rule dN = 3dB + dL = 0 mod 4: allows B-L-conserving proton decay and dL = 4; forbids Majorana masses, 0nubb, n-nbar and B+L-conserving proton decay to all orders',
      allowed == {'p -> e+ pi0 (dB,dL)=(-1,-1)': True, 'p -> e- pi+ pi+ (-1,+1)': False, 'n-nbar (-2,0)': False, '0nubb/Majorana (0,2)': False, 'nu_R^4 (0,4)': True})

# ===================================== F. against measurement (estimates) =====================================
print('== F. estimates against measurement')
GeV_s, yr, MP = 6.582e-25, 3.156e7, 1.22e19; Lam = MP / 3; mp, mpi, W0 = 0.938, 0.135, 0.15
Gam = mp / (32 * np.pi) * (1 - (mpi / mp) ** 2) ** 2 * W0 ** 2 / Lam ** 4; tau = GeV_s / Gam / yr; Lmin = Lam * (2.4e34 / tau) ** 0.25
Teq = (1.66 * np.sqrt(106.75) * Lam ** 4 / MP) ** (1 / 3)
print(f'   proton: O(1) coefficient at Lambda = M_P/3, W0 = {W0} GeV^2: tau(p -> e+ pi0) ~ {tau:.0e} yr vs > 2.4e34 (Super-K); safe for Lambda > {Lmin:.0e} GeV;')
print('     via the one-copy term the light family reaches it only through copy mixing ~ (ka)^2 per leg')
print('   n-nbar: forbidden by Z4 (measured tau > 8.6e7 s free, > 4.7e8 s bound); Majorana nu and 0nubb forbidden (T1/2(Xe) > 3.8e26 yr): neutrinos Dirac, no seesaw')
print(f'   baryon excess: every dN = 4 piece here conserves B - L, so sphalerons leave B = (28/79)(B-L) = 0, against eta_B = 6.1e-10; the term is in equilibrium only above ~{Teq:.0e} GeV')
print('   links: U(1)_N is broken (no N link); B - L is kept by the tetrahedral and Spin(10) forms, so its massless link survives unless a dL = 4 term is added')
check('F1 estimates: proton safe by > 1e10 in rate; n-nbar, 0nubb forbidden; B - L conserved so no surviving baryon excess from this term', tau / 2.4e34 > 1e10 and Lmin < 1e16 and Teq > 1e18)
print('theorems: A1-A3, B1-B2, D1, E1-E3.  finite: C1-C3 (C2 uses the static stand-in h = i log(tick)).  estimates: F.')
print('cited: Z16 (Spin-Z4), SMG existence for an anomaly-free 16, sphaleron factor 28/79, lattice W0, measured bounds.')
print('supplied: the four-mode terms, g, which copy is the mirror (one handedness bit), the rung-1 gauge generators, h = i log(tick).')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
