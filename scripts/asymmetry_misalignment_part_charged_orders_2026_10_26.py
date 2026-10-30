#!/usr/bin/env python3
"""sol_E v2 (POST HOC, disclosed in sol_E_v2_posthoc_note_pre_run.txt, written before this file was first run):
same model and frozen thresholds as sol_E_charged_orders.py (run 1), plus
 1. the full principle-allowed local Yukawa vertex (on-site + X-shifted and Q-shifted transverse bonds),
 2. a degeneracy-safe Jarlskog invariant, and
 3. T-symmetrised numerics (removes rounding-induced T violation only).
Self-contained, numpy only, deterministic."""
import itertools, time, numpy as np
T0 = time.time(); NP = [0, 0]
def check(tag, ok, msg):
    ok = bool(ok); NP[0 if ok else 1] += 1; print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}")
s0 = np.eye(2, dtype=complex); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
PAULI = [sx, sy, sz]
Gm = [np.kron(sx, sx), np.kron(sx, sy), np.kron(sx, sz), np.kron(sy, s0), np.kron(sz, s0)]
G5, G4 = Gm[4], Gm[3]; A_UP = (G5 + 1j * G4) / 2; EPS = 1j * sy; C_T = Gm[0] @ Gm[2]
M_SLAB, XI_PHI = 2.5, 0.5
BITS = [tuple(b) for b in itertools.product((0, 1), repeat=3)]
XN = {'x': (1, 0, 0), 'y': (0, 1, 0), 'z': (0, 0, 1)}; FAM = ['x', 'y', 'z']; SPEC = ['Q', 'U', 'D']
DIRS = {'0': (0, 0, 0), 'ex': (1, 0, 0), 'ey': (0, 1, 0), 'ez': (0, 0, 1)}
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
    def __init__(self, Ls, m=M_SLAB, tsym=True):
        self.Ls = Ls; self.R = {}; CTb = np.kron(C_T, np.eye(Ls))
        Hp = {b: Hk(np.pi * np.array(b, float), m, Ls) for b in BITS}
        for b, Hm in Hp.items():
            e, U = np.linalg.eigh(Hm); keep = np.abs(e) > 1e-8; R = -(U[:, keep] / e[keep]) @ U[:, keep].conj().T
            if tsym: R = (R + R.conj().T) / 2; R = (R + CTb @ R.conj() @ CTb.T) / 2      # exact T and hermiticity
            self.R[b] = R
        Xpos = np.kron(np.eye(4), np.diag(np.arange(Ls))); self.Z = {}
        for a in FAM:
            k = np.pi * np.array(XN[a], float); e, v = np.linalg.eigh(Hp[XN[a]]); Z = v[:, np.abs(e) < 1e-8]
            xw, xv = np.linalg.eigh(Z.conj().T @ Xpos @ Z); near = (Z @ xv)[:, xw < Ls / 2]; assert near.shape[1] == 2
            Vs = [near.conj().T @ dHk(k, i, Ls) @ near for i in range(3)]
            Mv = np.array([[np.real(np.trace(V @ P)) / 2 for P in PAULI] for V in Vs])
            chi = np.sign(np.linalg.det(Mv)); vel = abs(np.linalg.det(Mv)) ** (1 / 3)
            Zf = near @ su2_from_rot(np.linalg.inv(Mv) @ (chi * vel * np.eye(3)))
            Th = Zf.conj().T @ CTb @ Zf.conj(); ph = np.trace(Th @ (1j * sy).conj().T) / 2
            Zf = Zf * np.sqrt(ph); assert np.allclose(Zf.conj().T @ CTb @ Zf.conj(), 1j * sy, atol=1e-8)
            if tsym: Zf = (Zf + CTb @ Zf.conj() @ np.linalg.inv(1j * sy)) / 2               # C_T Z^* = Z E exactly
            self.Z[a] = Zf.reshape(4, Ls, 2)                    # (spin, layer, mode)
JMAX = 1 / (6 * np.sqrt(3))
def jarl(Yu, Yd):                       # -> (J/Jmax, normalised commutator invariant, degenerate?)
    Hu, Hd = Yu @ Yu.conj().T, Yd @ Yd.conj().T; mu, md = np.linalg.eigvalsh(Hu), np.linalg.eigvalsh(Hd)
    dC = np.linalg.det(Hu @ Hd - Hd @ Hu); inv = abs(dC) / (np.linalg.norm(Hu) ** 3 * np.linalg.norm(Hd) ** 3)
    if min(np.min(np.diff(mu)) / mu[-1], np.min(np.diff(md)) / md[-1]) < 1e-9: return 0.0, inv, True
    den = np.prod([mu[j] - mu[i] for i in range(3) for j in range(i + 1, 3)]) * np.prod([md[j] - md[i] for i in range(3) for j in range(i + 1, 3)])
    return (dC / (2j * den)).real / JMAX, inv, False
def jarlskog(Yu, Yd): return jarl(Yu, Yd)[0]
def wrap(x): return (x + np.pi / 2) % np.pi - np.pi / 2
# ------------------------------------------------------------------ E0: the principle as an explicit U(1)_H
CHG = {'phi_u': 1, 'phi_d': -1, 'phi_u*': -1, 'phi_d*': 1, 'Q': 0, 'U': -1, 'D': 1, 'Q+': 0, 'U+': 1, 'D+': -1}
BIL = {'uu': ('phi_u*', 'phi_u'), 'dd': ('phi_d*', 'phi_d'), 'ud': ('phi_u', 'phi_d'), 'du': ('phi_d', 'phi_u')}
LIN = {'lin_u': ('phi_u',), 'lin_d': ('phi_d',)}
def terms(model):
    T = [('vertex_u', ('phi_u', 'Q', 'U')), ('vertex_d', ('phi_d', 'Q', 'D'))]
    T += [(f'vertex_{s}_{side}{dn}', (f'phi_{s}', 'Q', X)) for s, X in (('u', 'U'), ('d', 'D')) for side in 'XQ' for dn in ('ex', 'ey', 'ez')]
    for nm, bl in BIL.items():
        for X in SPEC: T.append((f'{nm}:{X}', bl + (X + '+', X)))
    if model == 'control':
        for nm, bl in LIN.items():
            for X in SPEC: T.append((f'{nm}:{X}', bl + (X + '+', X)))
    return T
q = lambda fs: sum(CHG[f] for f in fs)
neutral_p = all(q(fs) == 0 for _, fs in terms('principle'))
charged_c = [nm for nm, fs in terms('control') if q(fs) != 0]
check("E0", neutral_p and len(charged_c) > 0, f"principle model: all {len(terms('principle'))} terms U(1)_H-neutral; control adds {len(charged_c)} charged terms ({', '.join(charged_c[:2])}, ...)")
# ------------------------------------------------------------------ draws
def herm_c(rng): return rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
def law_M(rng): G = herm_c(rng); return (G + C_T.conj().T @ G.conj() @ C_T) / 2          # T-real density coupling
def law_g(rng): G = herm_c(rng); return (G + C_T.T @ G.conj() @ C_T) / 2                 # T-compatible vertex coupling
def cell_ft(f): return {K: sum(f[c] * (-1) ** dot(K, c) for c in BITS) / 8 for K in BITS}
def draw(rng, aligned=False):
    pu = {}
    if aligned:
        pu = {c: rng.normal() for c in BITS}
    else:
        for c in BITS:
            if c[0] == 0: pu[c] = rng.normal() + 1j * rng.normal()
        for c in BITS:
            if c[0] == 1: pu[c] = np.conj(pu[xor(c, (1, 0, 0))])
    pd = {c: rng.normal() for c in BITS}
    couplings = {(ch, dn, X): law_M(rng) for ch in list(BIL) + list(LIN) for dn in DIRS for X in SPEC}
    return dict(pu=pu, pd=pd, gu=law_g(rng), gd=law_g(rng), M=couplings)
VB = [(side, dn) for side in 'XQ' for dn in ('ex', 'ey', 'ez')]
def add_vertex(dr, rng2):                # on-site coupling = run-1 g_s; bond couplings from the separate generator
    dr['Vu'] = {'0': dr['gu'], **{k: law_g(rng2) for k in VB}}; dr['Vd'] = {'0': dr['gd'], **{k: law_g(rng2) for k in VB}}
    return dr
def Gv(V, pQ, pX):                       # phi(c) Q(c)^T g X(c+d) -> (-1)^{pX.d};  phi(c) Q(c+d)^T g' X(c) -> (-1)^{pQ.d}
    G = V['0'].copy()
    for side, dn in VB: G = G + (-1) ** dot(pX if side == 'X' else pQ, DIRS[dn]) * V[side, dn]
    return G
def bilinear_cell(dr, ch, d):
    pu, pd = dr['pu'], dr['pd']
    f = {}
    for c in BITS:
        cd = xor(c, d)
        f[c] = {'uu': np.conj(pu[c]) * pu[cd], 'dd': np.conj(pd[c]) * pd[cd], 'ud': pu[c] * pd[cd], 'du': pd[c] * pu[cd],
                'lin_u': pu[c], 'lin_d': pd[c]}[ch]
    return cell_ft(f)
def layer_w(l0, Ls): return np.exp(-np.abs(np.arange(Ls) - l0) / XI_PHI)
def pair_scalar(Za, Zb, g):            # per-layer scalar channel of Za(s)^T g Zb(s)
    B = np.einsum('isk,ij,jsl->skl', Za, g, Zb)
    return np.einsum('kl,skl->s', EPS.T, B) / 2
GROUPS = {'uu_onsite': [('uu', '0')], 'uu_bond': [('uu', d) for d in ('ex', 'ey', 'ez')],
          'mixed': [('ud', d) for d in DIRS] + [('du', d) for d in ('ex', 'ey', 'ez')], 'dd': [('dd', d) for d in DIRS],
          'lin': [('lin_u', d) for d in DIRS] + [('lin_d', d) for d in DIRS]}
def evaluate(sl, dr, lu, ld, groups):
    Ls = sl.Ls; wu, wd = layer_w(lu, Ls), layer_w(ld, Ls)
    phu, phd = cell_ft(dr['pu']), cell_ft(dr['pd'])
    PS = {(a, b, s_): pair_scalar(sl.Z[a], sl.Z[b], Gv(dr['V' + s_], XN[a], XN[b])) for a in FAM for b in FAM for s_ in 'ud'}
    Yu = np.array([[np.sum(phu[xor(XN[a], XN[b])] * wu * PS[a, b, 'u']) for b in FAM] for a in FAM])
    Yd = np.array([[np.sum(phd[xor(XN[a], XN[b])] * wd * PS[a, b, 'd']) for b in FAM] for a in FAM])
    jt = jarl(Yu, Yd)
    out = dict(Yu=Yu, Yd=Yd, th_tree=wrap(-np.angle(np.linalg.det(Yu)) - np.angle(np.linalg.det(Yd))), J_tree=jt[0], inv_tree=jt[1], deg_tree=jt[2])
    lay = {'uu': wu * wu, 'dd': wd * wd, 'ud': wu * wd, 'du': wu * wd, 'lin_u': wu, 'lin_d': wd}
    dYtot_u = np.zeros((3, 3), complex); dYtot_d = np.zeros((3, 3), complex)
    for gname in groups:
        terms_g = [(ch, dn, bilinear_cell(dr, ch, DIRS[dn])) for ch, dn in GROUPS[gname]]
        dZ = {}
        for X in SPEC:
            for a in FAM:
                for K in BITS:
                    Mt = np.zeros((Ls, 4, 4), complex)
                    for ch, dn, bh in terms_g:
                        d = DIRS[dn]; M = dr['M'][ch, dn, X]; sgn_a = (-1) ** dot(XN[a], d)
                        Mt += lay[ch][:, None, None] * sgn_a * (bh[K] * M + (-1) ** dot(K, d) * np.conj(bh[K]) * M.conj().T)[None]
                    v = np.einsum('sij,jsk->isk', Mt, sl.Z[a])
                    dZ[X, a, K] = (sl.R[xor(XN[a], K)] @ v.reshape(4 * Ls, 2)).reshape(4, Ls, 2)
        dYu = np.zeros((3, 3), complex); dYd = np.zeros((3, 3), complex)
        for ia, a in enumerate(FAM):
            for ib, b in enumerate(FAM):
                for K in BITS:
                    Kv = xor(xor(XN[a], XN[b]), K)
                    pa, pb = XN[a], XN[b]; pbK, paK = xor(XN[b], K), xor(XN[a], K)
                    dYu[ia, ib] += np.sum(phu[Kv] * wu * (pair_scalar(sl.Z[a], dZ['U', b, K], Gv(dr['Vu'], pa, pbK)) + pair_scalar(dZ['Q', a, K], sl.Z[b], Gv(dr['Vu'], paK, pb))))
                    dYd[ia, ib] += np.sum(phd[Kv] * wd * (pair_scalar(sl.Z[a], dZ['D', b, K], Gv(dr['Vd'], pa, pbK)) + pair_scalar(dZ['Q', a, K], sl.Z[b], Gv(dr['Vd'], paK, pb))))
        out['c_' + gname] = -np.imag(np.trace(np.linalg.solve(Yu, dYu))) - np.imag(np.trace(np.linalg.solve(Yd, dYd)))
        dYtot_u += dYu; dYtot_d += dYd
    out['J_corr'] = jarlskog(Yu + dYtot_u, Yd + dYtot_d)
    out['th_corr'] = wrap(-np.angle(np.linalg.det(Yu + dYtot_u)) - np.angle(np.linalg.det(Yd + dYtot_d)))
    return out
PRINC = ['uu_onsite', 'uu_bond', 'mixed', 'dd']
EPS_EW = 246 / 2.4e18
sl = Slab(48); ND = 10; rng = np.random.default_rng(2026102601); rng2 = np.random.default_rng(2026102602)
DR = [draw(rng) for _ in range(ND)]; DR = [add_vertex(dr, rng2) for dr in DR]
DELTAS = list(range(0, 23))
res = {}
for order in ('a', 'b'):
    for D in DELTAS:
        lu, ld = (1, 1 + D) if order == 'a' else (1 + D, 1)
        res[order, D] = [evaluate(sl, dr, lu, ld, PRINC) for dr in DR]
mx_tree = max(abs(np.sin(o['th_tree'])) for k in res for o in res[k]); medJ = np.median([abs(o['J_tree']) for k in res for o in res[k]])
ndeg = sum(o['deg_tree'] for k in res for o in res[k]); minv = np.median([o['inv_tree'] for k in res for o in res[k]])
check("E1", mx_tree < 1e-8 and medJ > 1e-2, f"tree: max |sin theta_bar_tree| {mx_tree:.1e}; median |J_tree|/Jmax {medJ:.2f} "
      f"(degenerate spectra {ndeg}/{sum(len(v) for v in res.values())}; median commutator invariant {minv:.1e})")
e2 = max(abs(o['c_uu_onsite']) for k in res for o in res[k])
check("E2", e2 < 1e-6, f"on-site |phi_u|^2 channel alone: max |theta_bar_ind|/eps^2 = {e2:.1e}")
print("  c2(Delta) = median |theta_bar_ind|/eps^2 (all allowed channels) and by channel; Ls = 48")
print("  Delta |  a: total  uu_bond  mixed     dd   |  b: total  uu_bond  mixed     dd")
c2 = {}
for D in DELTAS:
    rowa = [np.median([abs(sum(o['c_' + g] for g in PRINC)) for o in res['a', D]])] + [np.median([abs(o['c_' + g]) for o in res['a', D]]) for g in ('uu_bond', 'mixed', 'dd')]
    rowb = [np.median([abs(sum(o['c_' + g] for g in PRINC)) for o in res['b', D]])] + [np.median([abs(o['c_' + g]) for o in res['b', D]]) for g in ('uu_bond', 'mixed', 'dd')]
    c2['a', D], c2['b', D] = rowa[0], rowb[0]
    if D in (0, 1, 2, 3, 4, 6, 8, 10, 12, 15, 18, 20, 22):
        print(f"  {D:5d} | " + " ".join(f"{x:8.1e}" for x in rowa) + " | " + " ".join(f"{x:8.1e}" for x in rowb))
c2min = min(v for (o, D), v in c2.items() if D >= 1); argmin = min(((v, k) for k, v in c2.items() if k[1] >= 1))[1]
c2max = max(v for (o, D), v in c2.items() if D >= 1); argmax = max(((v, k) for k, v in c2.items() if k[1] >= 1))[1]
print(f"  [diagnostic] c2 range over Delta in [1,22], both orderings: min {c2min:.2e} at {argmin}, max {c2max:.2e} at {argmax}; "
      f"eps_max(worst case) = {np.sqrt(1e-10 / c2max):.1e}")
check("E3", c2min * EPS_EW ** 2 < 1e-10, f"electroweak-scale order eps = {EPS_EW:.2e}: min_Delta median theta_bar_ind = {c2min * EPS_EW**2:.1e} (at {argmin})")
check("E3h", c2min * 0.2 ** 2 < 1e-10, f"lattice-scale order eps = 0.2: min_Delta median theta_bar_ind = {c2min * 0.04:.1e}")
emax = np.sqrt(1e-10 / c2min)
check("E7", emax >= 1e-6, f"quality bound: c2_min = {c2min:.2e}, eps_max = sqrt(1e-10/c2_min) = {emax:.1e} (order amplitude / cutoff)")
# E4 control: linear couplings restore an O(eps) leak
c1 = []
for order in ('a', 'b'):
    lu, ld = (1, 5) if order == 'a' else (5, 1)
    c1.append(np.median([abs(evaluate(sl, dr, lu, ld, ['lin'])['c_lin']) for dr in DR]))
check("E4", min(c1) > 1e-3, f"control (principle broken, linear order couplings): median c1 at Delta = 4: a {c1[0]:.2e}, b {c1[1]:.2e} "
      f"-> theta_bar = c1*eps: at eps_EW {max(c1) * EPS_EW:.1e}, eps_max(control) = {1e-10 / max(c1):.1e}; principle model has no linear term")
# E5 aligned control
rngA = np.random.default_rng(5); mxJ = 0; mxth = 0
for _ in range(6):
    dr = add_vertex(draw(rngA, aligned=True), rng2)
    for D in (0, 3, 9):
        o = evaluate(sl, dr, 1, 1 + D, PRINC + ['lin']); mxJ = max(mxJ, abs(o['J_tree']), abs(o['J_corr'])); mxth = max(mxth, abs(np.sin(o['th_tree'])), abs(np.sin(o['th_corr'])))
check("E5", mxJ < 1e-9 and mxth < 1e-9, f"aligned orders (both T-even): max |J|/Jmax {mxJ:.1e}, max |sin theta| {mxth:.1e} (tree and corrected, incl. linear terms)")
# E6 convergence
sl56 = Slab(56); conv = []
for order in ('a', 'b'):
    lu, ld = (1, 5) if order == 'a' else (5, 1)
    v56 = np.median([abs(sum(evaluate(sl56, dr, lu, ld, PRINC)['c_' + g] for g in PRINC)) for dr in DR]); conv.append(abs(v56 - c2[order, 4]) / c2[order, 4])
check("E6", max(conv) < 1e-3, f"Ls 48 -> 56 relative change of c2 at Delta = 4: {max(conv):.1e}")
# ---------------- disclosed diagnostics (no PASS/FAIL)
slr = Slab(48, tsym=False); worst = 0.0
for order in ('a', 'b'):
    for D in (4, 12):
        lu, ld = (1, 1 + D) if order == 'a' else (1 + D, 1)
        for dr, o in zip(DR, res[order, D]):
            orw = evaluate(slr, dr, lu, ld, PRINC)
            for g in ('uu_bond', 'mixed', 'dd'):
                if abs(o['c_' + g]) > 1e-6: worst = max(worst, abs(orw['c_' + g] - o['c_' + g]) / abs(o['c_' + g]))
print(f"  [diagnostic] raw vs T-symmetrised numerics, channels > 1e-6 at Delta = 4, 12: max relative difference {worst:.1e}")
sl64 = Slab(64)
for order in ('a', 'b'):
    for D in (15, 22):
        lu, ld = (1, 1 + D) if order == 'a' else (1 + D, 1)
        v64 = np.median([abs(sum(evaluate(sl64, dr, lu, ld, PRINC)['c_' + g] for g in PRINC)) for dr in DR])
        print(f"  [diagnostic] ordering {order}, Delta = {D}: median c2 Ls=48 {c2[order, D]:.3e}  Ls=64 {v64:.3e}")
print(f"time {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
