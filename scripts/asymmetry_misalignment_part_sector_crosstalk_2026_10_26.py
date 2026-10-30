#!/usr/bin/env python3
"""sol_D: sector cross-talk runner for the misalignment CP mechanism.
Criteria: sol_D_criteria_pre_run.txt (frozen before the first run). numpy only, deterministic.
Supplied: slab form and m, three species as slab copies, vertex spinor structure Cvert = 1 (x) eps, cell-periodic
profiles, potentials of the same residual symmetry as their vertex (strength kappa = 1), mirror exclusion.
Derived: every Yukawa and every cross-talk vertex from the slab's own near-wall wavefunctions and resolvent."""
import itertools, time, numpy as np
T0 = time.time(); NP = [0, 0]
def check(tag, ok, msg):
    ok = bool(ok); NP[0 if ok else 1] += 1; print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}")
s0 = np.eye(2, dtype=complex); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
PAULI = [sx, sy, sz]
Gm = [np.kron(sx, sx), np.kron(sx, sy), np.kron(sx, sz), np.kron(sy, s0), np.kron(sz, s0)]
G5, G4 = Gm[4], Gm[3]
A_UP = (G5 + 1j * G4) / 2
EPS = 1j * sy                      # Lorentz-invariant pairing of two Weyl spinors
CV = np.kron(s0, EPS)              # vertex spinor structure (rotation-invariant, T-compatible; checked below)
C_T = Gm[0] @ Gm[2]                # time reversal T = C_T K (sol_A nullspace; real, C_T^2 = -1)
M_SLAB = 2.5
BITS = [tuple(b) for b in itertools.product((0, 1), repeat=3)]     # pi-momenta K = pi*b and cell sites c
XN = {'x': (1, 0, 0), 'y': (0, 1, 0), 'z': (0, 0, 1)}; FAM = ['x', 'y', 'z']
def xor(a, b): return tuple(i ^ j for i, j in zip(a, b))
def dot(a, b): return sum(i * j for i, j in zip(a, b)) % 2
def bond(Ls):
    S = np.zeros((Ls, Ls)); S[np.arange(1, Ls), np.arange(Ls - 1)] = 1
    return np.kron(A_UP, S) + np.kron(A_UP.conj().T, S.T)
def h_on(k, m): return sum(np.sin(k[i]) * Gm[i] for i in range(3)) + (m - 1 - sum(1 - np.cos(k[i]) for i in range(3))) * G5
def Hk(k, m, Ls): return np.kron(h_on(k, m), np.eye(Ls)) + bond(Ls)
def dHk(k, i, Ls): return np.kron(np.cos(k[i]) * Gm[i] - np.sin(k[i]) * G5, np.eye(Ls))
def adjoint(W): return np.array([[np.real(np.trace(PAULI[k] @ W.conj().T @ PAULI[j] @ W)) / 2 for k in range(3)] for j in range(3)])
def su2_from_rot(R):
    rows = [np.kron(PAULI[j], np.eye(2)) - np.kron(np.eye(2), sum(R[j, k] * PAULI[k] for k in range(3)).T) for j in range(3)]
    u, sv, vh = np.linalg.svd(np.vstack(rows)); W = vh[-1].conj().reshape(2, 2); W = W / np.sqrt(np.linalg.det(W))
    assert np.allclose(adjoint(W), R, atol=1e-8); return W
class Slab:
    def __init__(self, Ls, m=M_SLAB):
        self.Ls, self.m = Ls, m
        self.Hp = {b: Hk(np.pi * np.array(b, float), m, Ls) for b in BITS}
        self.R = {}
        for b, Hm in self.Hp.items():
            e, U = np.linalg.eigh(Hm); keep = np.abs(e) > 1e-8
            self.R[b] = -(U[:, keep] / e[keep]) @ U[:, keep].conj().T          # reduced resolvent at E = 0
        Xpos = np.kron(np.eye(4), np.diag(np.arange(Ls))); self.Z = {}; self.zsplit = {}
        for a in FAM:
            k = np.pi * np.array(XN[a], float); e, v = np.linalg.eigh(self.Hp[XN[a]]); Z = v[:, np.abs(e) < 1e-8]
            xw, xv = np.linalg.eigh(Z.conj().T @ Xpos @ Z); B = Z @ xv; near = B[:, xw < Ls / 2]
            assert near.shape[1] == 2, (a, near.shape)
            Vs = [near.conj().T @ dHk(k, i, Ls) @ near for i in range(3)]
            Mv = np.array([[np.real(np.trace(V @ P)) / 2 for P in PAULI] for V in Vs])
            chi = np.sign(np.linalg.det(Mv)); vel = abs(np.linalg.det(Mv)) ** (1 / 3)
            Rm = np.linalg.inv(Mv) @ (chi * vel * np.eye(3)); assert np.allclose(Rm @ Rm.T, np.eye(3), atol=1e-8)
            Zf = near @ su2_from_rot(Rm)
            CTb = np.kron(C_T, np.eye(Ls)); Th = Zf.conj().T @ CTb @ Zf.conj(); ph = np.trace(Th @ (1j * sy).conj().T) / 2
            Zf = Zf * np.sqrt(ph); Th = Zf.conj().T @ CTb @ Zf.conj(); assert np.allclose(Th, 1j * sy, atol=1e-8)
            self.Z[a] = Zf; self.zsplit[a] = np.abs(e[np.abs(e) < 1e-8]).max()
    def rows(self, l): return np.arange(4) * self.Ls + l
def fourier(field):                     # f(c) on the 8 cell sites -> f_hat(K) = (1/8) sum_c f(c) (-1)^{K.c}
    return {K: sum(field[c] * (-1) ** dot(K, c) for c in BITS) / 8 for K in BITS}
def herm(rng): A = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)); return (A + A.conj().T) / 2
def T_img(G): return C_T.conj().T @ G.conj() @ C_T
def profiles(rng, kind):
    """vertex profile phi(c) and potential Phi(c) for a sector. kinds: 'up' (residual T*tau_x), 'down' (residual T),
    'generic' (no residual), 'TT' (T and tau_x: T-even, tau_x-even; the D2r restriction)."""
    phi, Phi = {}, {}
    if kind == 'up':
        for c in BITS:
            if c[0] == 0:
                phi[c] = rng.normal() + 1j * rng.normal(); Phi[c] = herm(rng)
        for c in BITS:
            if c[0] == 1:
                cp = xor(c, (1, 0, 0)); phi[c] = np.conj(phi[cp]); Phi[c] = T_img(Phi[cp])
    elif kind == 'down':
        for c in BITS: phi[c] = rng.normal(); G = herm(rng); Phi[c] = (G + T_img(G)) / 2
    elif kind == 'generic':
        for c in BITS: phi[c] = rng.normal() + 1j * rng.normal(); Phi[c] = herm(rng)
    elif kind == 'TT':
        for c in BITS:
            if c[0] == 0:
                phi[c] = rng.normal(); G = herm(rng); Phi[c] = (G + T_img(G)) / 2
        for c in BITS:
            if c[0] == 1: cp = xor(c, (1, 0, 0)); phi[c] = phi[cp]; Phi[c] = Phi[cp]
    return fourier(phi), fourier(Phi)
def scalar(B): return np.trace(EPS.T @ B) / 2
def yukawa(sl, ph, l):
    r = sl.rows(l); Y = np.zeros((3, 3), complex); rem = 0.0; nrm = 0.0
    for ia, a in enumerate(FAM):
        for ib, b in enumerate(FAM):
            B = ph[xor(XN[a], XN[b])] * (sl.Z[a][r].T @ CV @ sl.Z[b][r])
            Y[ia, ib] = scalar(B); rem += np.linalg.norm(B - Y[ia, ib] * EPS) ** 2; nrm += np.linalg.norm(B) ** 2
    return Y, np.sqrt(rem / max(nrm, 1e-300))
def dressed(sl, ph, l, Phh, lp):
    """first-order (in the potential) correction to the vertex (ph at layer l) from the potential Phh at layer lp,
    through the reduced slab resolvent, on either leg; scalar channel."""
    r, rp = sl.rows(l), sl.rows(lp); dY = np.zeros((3, 3), complex)
    dZ = {}
    for a in FAM:
        for K in BITS:
            v = np.zeros_like(sl.Z[a]); v[rp] = Phh[K] @ sl.Z[a][rp]
            dZ[a, K] = sl.R[xor(XN[a], K)] @ v                # lives at momentum X_a + K
    for ia, a in enumerate(FAM):
        for ib, b in enumerate(FAM):
            B = np.zeros((2, 2), complex)
            for K in BITS:
                kv = xor(xor(XN[a], XN[b]), K)
                B += ph[kv] * (sl.Z[a][r].T @ CV @ dZ[b, K][r] + dZ[a, K][r].T @ CV @ sl.Z[b][r])
            dY[ia, ib] = scalar(B)
    return dY
JMAX = 1 / (6 * np.sqrt(3))
def jarlskog(Yu, Yd):
    Hu, Hd = Yu @ Yu.conj().T, Yd @ Yd.conj().T
    mu, md = np.linalg.eigvalsh(Hu), np.linalg.eigvalsh(Hd)
    den = np.prod([mu[j] - mu[i] for i in range(3) for j in range(i + 1, 3)]) * np.prod([md[j] - md[i] for i in range(3) for j in range(i + 1, 3)])
    return (np.linalg.det(Hu @ Hd - Hd @ Hu) / (2j * den)).real / JMAX
def wrap(x): return (x + np.pi / 2) % np.pi - np.pi / 2
def evaluate(sl, pu, pd, lu, ld):
    (phu, Phu), (phd, Phd) = pu, pd
    Yu, remu = yukawa(sl, phu, lu); Yd, remd = yukawa(sl, phd, ld)
    th_tree = wrap(-np.angle(np.linalg.det(Yu)) - np.angle(np.linalg.det(Yd)))
    dYu_self, dYu_x = dressed(sl, phu, lu, Phu, lu), dressed(sl, phu, lu, Phd, ld)
    dYd_self, dYd_x = dressed(sl, phd, ld, Phd, ld), dressed(sl, phd, ld, Phu, lu)
    t = lambda Y, dY: -np.imag(np.trace(np.linalg.solve(Y, dY)))
    out = dict(Yu=Yu, Yd=Yd, th_tree=th_tree, J_tree=jarlskog(Yu, Yd), rem=max(remu, remd),
               th_self=t(Yu, dYu_self) + t(Yd, dYd_self), th_d_from_u=t(Yd, dYd_x), th_u_from_d=t(Yu, dYu_x))
    out['th_ind'] = out['th_self'] + out['th_d_from_u'] + out['th_u_from_d']
    out['J_corr'] = jarlskog(Yu + dYu_self + dYu_x, Yd + dYd_self + dYd_x)
    out['th_corr'] = wrap(-np.angle(np.linalg.det(Yu + dYu_self + dYu_x)) - np.angle(np.linalg.det(Yd + dYd_self + dYd_x)))
    return out
# ------------------------------------------------------------------ setup checks
LS0 = 40; sl = Slab(LS0)
rng0 = np.random.default_rng(1)
resT = max(np.abs(np.kron(C_T, np.eye(LS0)) @ Hk(k, M_SLAB, LS0).conj() @ np.kron(C_T, np.eye(LS0)).T - Hk(-k, M_SLAB, LS0)).max() for k in rng0.uniform(-np.pi, np.pi, (3, 3)))
print(f"setup: Ls {LS0}, m {M_SLAB}, T residual {resT:.0e}, CV T-compatible {np.allclose(C_T.T @ CV.conj() @ C_T, CV)}, "
      f"near/far splitting max {max(sl.zsplit.values()):.1e}")
# ------------------------------------------------------------------ scans
ND = 12; DELTAS = list(range(0, 19))
def draws(seed, ku, kd, n=ND):
    rng = np.random.default_rng(seed); return [(profiles(rng, ku), profiles(rng, kd)) for _ in range(n)]
DR = draws(20261026, 'up', 'down')
res = {}
for order in ('a', 'b'):
    for D in DELTAS:
        lu, ld = (1, 1 + D) if order == 'a' else (1 + D, 1)
        res[order, D] = [evaluate(sl, pu, pd, lu, ld) for pu, pd in DR]
# D6 internal reality (from the Delta = 0 and a deep configuration)
F = np.diag([-1., 1, 1])
d6u = max(np.linalg.norm(o['Yu'] - F.T @ o['Yu'].conj() @ F) / np.linalg.norm(o['Yu']) for k in res for o in res[k])
d6d = max(np.linalg.norm(o['Yd'].imag) / np.linalg.norm(o['Yd']) for k in res for o in res[k])
check("D6", d6u < 1e-12 and d6d < 1e-12, f"derived Yu = F^T conj(Yu) F to {d6u:.0e}; derived Yd real to {d6d:.0e}; "
      f"Lorentz-violating remainder of the projected vertex (max over configs) {max(o['rem'] for k in res for o in res[k]):.2e}")
mx_tree = max(abs(np.sin(o['th_tree'])) for k in res for o in res[k]); medJ = np.median([abs(o['J_tree']) for k in res for o in res[k]])
check("D1", mx_tree < 1e-12 and medJ > 1e-3, f"tree: max |sin theta_bar_tree| {mx_tree:.1e}; median |J_tree|/Jmax {medJ:.2e}")
print("  theta_bar_ind vs Delta (median over draws; Ls = 40): ordering a = up shallow (l_u=1), b = down shallow (l_d=1)")
print("  Delta |  a: total   d<-u     u<-d    |  b: total   d<-u     u<-d")
best = 9.0
for D in DELTAS:
    ra, rb = res['a', D], res['b', D]
    ma = [np.median([abs(o[q]) for o in ra]) for q in ('th_ind', 'th_d_from_u', 'th_u_from_d')]
    mb = [np.median([abs(o[q]) for o in rb]) for q in ('th_ind', 'th_d_from_u', 'th_u_from_d')]
    if D >= 1: best = min(best, ma[0], mb[0])
    print(f"  {D:5d} | " + "  ".join(f"{x:8.1e}" for x in ma) + " | " + "  ".join(f"{x:8.1e}" for x in mb))
check("D2", best < 1e-10, f"decisive cross-talk, generic potentials: min_Delta median |theta_bar_ind| = {best:.2e} (threshold 1e-10, Ls = 40, kappa = 1)")
selfmax = max(abs(o['th_self']) for k in res for o in res[k])
check("D7", selfmax < 1e-12, f"self-dressing theta shift max {selfmax:.1e}")
# D2r: shallow sector's potential restricted to be invariant under the deep sector's residual (T and tau_x)
best_r = 9.0; tab = []
for order in ('a', 'b'):
    rng = np.random.default_rng(777 + (order == 'b'))
    for D in DELTAS[1:]:
        lu, ld = (1, 1 + D) if order == 'a' else (1 + D, 1)
        vals = []
        for _ in range(ND):
            pu, pd = profiles(rng, 'up'), profiles(rng, 'down')
            if order == 'a': pu = (pu[0], profiles(rng, 'TT')[1])     # up shallow: its potential made T- and tau_x-even
            else: pd = (pd[0], profiles(rng, 'TT')[1])                 # down shallow: its potential made tau_x-even
            vals.append(abs(evaluate(sl, pu, pd, lu, ld)['th_ind']))
        m_ = np.median(vals); tab.append((order, D, m_)); best_r = min(best_r, m_)
print("  D2r medians: " + ", ".join(f"{o}{D}:{v:.1e}" for o, D, v in tab if D in (1, 2, 4, 8, 12, 18)))
check("D2r", best_r < 1e-10, f"restricted shallow potential (supplied): min_Delta median |theta_bar_ind| = {best_r:.2e}")
# D3 control (i): aligned sectors (both residual T)
DA = draws(99, 'down', 'down', n=ND); mxJ = 0; mxth = 0
for (pu, pd) in DA:
    for D in (0, 3, 9):
        o = evaluate(sl, pu, pd, 1, 1 + D); mxJ = max(mxJ, abs(o['J_tree']), abs(o['J_corr'])); mxth = max(mxth, abs(np.sin(o['th_tree'])), abs(np.sin(o['th_corr'])), abs(o['th_ind']))
check("D3", mxJ < 1e-12 and mxth < 1e-12, f"aligned control: max |J|/Jmax (tree and corrected) {mxJ:.1e}; max theta {mxth:.1e}")
# D4 control (ii): generic complex up vertex
DG = draws(4242, 'generic', 'down', n=40)
medg = np.median([abs(np.sin(evaluate(sl, pu, pd, 1, 3)['th_tree'])) for pu, pd in DG])
check("D4", medg > 0.1, f"generic complex up vertex: median |sin theta_bar_tree| {medg:.2f}")
# D5 control (iii): convergence in Ls at Delta = 4
conv = {}
for Ls in (40, 48, 56):
    s2 = sl if Ls == LS0 else Slab(Ls)
    conv[Ls] = [np.median([abs(evaluate(s2, pu, pd, *((1, 5) if order == 'a' else (5, 1)))['th_ind']) for pu, pd in DR]) for order in ('a', 'b')]
rel = max(abs(conv[48][i] - conv[40][i]) / max(conv[40][i], 1e-300) for i in range(2)) ; rel2 = max(abs(conv[56][i] - conv[48][i]) / max(conv[48][i], 1e-300) for i in range(2))
check("D5", (rel < 1e-3 and rel2 < 1e-3) or max(max(v) for v in conv.values()) < 1e-14,
      f"Ls convergence at Delta = 4: medians {[[f'{x:.3e}' for x in conv[L]] for L in conv]}; rel changes {rel:.1e}, {rel2:.1e}")
print(f"time {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
