#!/usr/bin/env python3
"""B11: the corner Weyl step W = S R_L U_H U_L as a finite-depth fermionic circuit, and its
qubit images in the 48-qubit-per-site corner code (BKSF, flux 1011).

Part A (one-particle / Gaussian level, L = 4 torus):
  - rebuild W exactly as the scale-ladder runner Part 6 does (gauge, S, R_L, U_H, U_L);
  - build an explicit gate list g_j = exp(-i theta_j k_j) with k_j a 2-mode hopping
    (sigma_x or sigma_y on a mode pair, gauge-signed) or a mode number n_q, from geometry
    (plaquette 4-cycles, plaquette diagonals, on-site antipodes, on-site Givens elimination);
  - check prod g_j == W entrywise (no global phase freedom used);
  - flow (GNVW / one-particle) index of every factor across the three cut planes;
  - Majorana-monomial (Clifford) test and Clifford/T/irrational angle census.
Part B (qubit level, imported from qubit_part.py).
Supplied model only; no physical identification.
"""
import itertools, os, sys
import numpy as np

REPO = '/home/user/qubit-lattice-axiom-framework'
sys.path.insert(0, os.path.join(REPO, 'scripts'))
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)

import corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17 as _model
C = _model._run_reviewed_program(definitions_only=True)
L = C['L']; VERTS = C['VERTS']; nV = len(VERTS); CORN = C['CORNERS']; ROTS = C['ROTS']; DIRS = C['DIRS']
F = dict(square=1, triangle=0, plaquette=1, tube=1)
def dmod(x): return ((x + 1) % L) - 1
def neg(d): return tuple(-x for x in d)
def perp(d, e): return sum(a*b for a, b in zip(d, e)) == 0 and d != e
def vadd(a, b): return tuple(x + y for x, y in zip(a, b))
def vmod(a): return tuple(x % L for x in a)

# ---------------- translation-invariant gauge: copied from the scale-ladder runner (read-only reuse)
etypes = []; ekey = {}
def addt(c1, c2, sh):
    if (c1, c2, sh) in ekey or (c2, c1, neg(sh)) in ekey: return
    ekey[(c1, c2, sh)] = ekey[(c2, c1, neg(sh))] = len(etypes); etypes.append((c1, c2, sh))
Z0 = (0, 0, 0)
for c in CORN:
    d, e = tuple(c)
    for a, b in ((d, e), (e, d)):
        for f in DIRS:
            if perp(f, a) and perp(f, b) and f != neg(b) and f != neg(a):
                addt(c, frozenset((a, f)), Z0)
        addt(c, frozenset((neg(a), b)), a)
nT = len(etypes)
def cyc(seq):
    return [ekey[(c1, c2, tuple(y - x for x, y in zip(p1, p2)))] for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1])]
cell = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
for d in DIRS:
    a = [f for f in DIRS if perp(f, d) and f != neg(d)]; a0 = a[0]
    b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]; ring = [a0, b0, neg(a0), neg(b0)]
    cell['square'].append(cyc([(frozenset((d, r)), Z0) for r in ring]))
    for i in range(4):
        p, q = ring[i], ring[(i+1) % 4]
        cell['tube'].append(cyc([(frozenset((d, p)), Z0), (frozenset((neg(d), p)), d), (frozenset((neg(d), q)), d), (frozenset((d, q)), Z0)]))
for s in itertools.product((1, -1), repeat=3):
    x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
    cell['triangle'].append(cyc([(frozenset((x, y)), Z0), (frozenset((y, z)), Z0), (frozenset((z, x)), Z0)]))
for d, e in (((1,0,0),(0,1,0)), ((0,1,0),(0,0,1)), ((0,0,1),(1,0,0))):
    cell['plaquette'].append(cyc([(frozenset((d, e)), Z0), (frozenset((neg(d), e)), d), (frozenset((neg(d), neg(e))), vadd(d, e)), (frozenset((d, neg(e))), e)]))
rows = []; rhs = []
for k, cs in cell.items():
    for c in cs: rows.append(c); rhs.append(F[k])
ucell = C['gf2_solve'](rows, rhs, nT)
u = np.zeros(C['nE'], np.uint8)
for key, i in C['EID'].items():
    a, b = tuple(key); (v, c), (w, c2) = VERTS[a], VERTS[b]
    u[i] = ucell[ekey[(c, c2, tuple(dmod(y - x) for x, y in zip(v, w)))]]
psg = lambda f: C['psg_sign'](f, u)
rots = [psg(lambda q, M=R: C['rot_vert'](M, q)) for R in ROTS]
TV = list(itertools.product(range(L), repeat=3))
trans = [psg(lambda q, t=t: C['trans_vert'](t, q)) for t in TV]
def H0(t1, t2):
    H = np.zeros((nV, nV))
    for key in C['EDGES']:
        i, j = tuple(key); t = t1 if C['edges'][key] == 'onsite' else t2
        H[i, j] = H[j, i] = -t * (-1.0) ** u[C['EID'][key]]
    return H
VID = C['VID']
loc0 = [VID[((0, 0, 0), c)] for c in CORN]; CI = {c: i for i, c in enumerate(CORN)}

# ---------------- W exactly as in runner Part 6 (real-space form of Ws(k) = S(k) L(k) UH UL / sqrt2)
RLr = H0(0.0, 1.0) / np.sqrt(2)
Hon = H0(1.0, 0.0)[np.ix_(loc0, loc0)]        # = Bloch(0)^dag H0(1,0) Bloch(0) for a one-site cell
Lam = np.zeros((12, 12), complex)
for sg in itertools.product((1, -1), repeat=3):
    x, y, z = (sg[0], 0, 0), (0, sg[1], 0), (0, 0, sg[2])
    cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
    if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
    for a_ in range(3):
        q_, r_ = cy[a_], cy[(a_ + 1) % 3]; ii, jj = VID[((0, 0, 0), q_)], VID[((0, 0, 0), r_)]
        amp = 1j * (-1.0) ** u[C['EID'][frozenset((ii, jj))]]; Lam[CI[r_], CI[q_]] += amp; Lam[CI[q_], CI[r_]] += np.conj(amp)
def eproj(M):
    w_, V_ = np.linalg.eigh(M); ls = sorted(set(np.round(w_, 6)))
    return ls, [V_[:, np.abs(w_ - l) < 1e-6] @ V_[:, np.abs(w_ - l) < 1e-6].conj().T for l in ls]
lsH, PH = eproj(Hon); lsL, PLm = eproj(Lam)
UH = PH[0] - PH[1] - 1j * PH[2]; UL = PLm[0] + 1j * PLm[1] + 1j * PLm[2] + PLm[3]
c_xy = [c for c in CORN if set(c) == {(1, 0, 0), (0, 1, 0)}][0]
i0 = VID[((0, 0, 0), c_xy)]; j0 = VID[((1, 1, 0), c_xy)]
Sr = np.zeros((nV, nV))
for Pr, sr in rots:
    for Pt, st in trans:
        P = Pt[Pr]; s_ = sr ^ st[Pr]; Sr[P[j0], P[i0]] += (-1.0) ** (int(s_[i0]) + int(s_[j0]))
Sr /= np.abs(Sr).max()
def onsite_full(V):
    M = np.zeros((nV, nV), complex)
    for v in TV:
        idx = [VID[(v, c)] for c in CORN]; M[np.ix_(idx, idx)] = V
    return M
Vos = UH @ UL
Wref = Sr @ RLr @ onsite_full(Vos)
print(f"on-site hopping eigenvalues {lsH}, Lambda eigenvalues {lsL}")
check("reference W = S R_L (U_H U_L) is unitary on the L = 4 torus (768 modes)", np.allclose(Wref @ Wref.conj().T, np.eye(nV)))

# ---------------- gate list: (modes tuple, generator k (len(modes) x len(modes) Hermitian), theta, tag)
SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]])
gates = []
def g_hop(m, n, k2, th, tag): gates.append(((m, n), k2, th, tag))
def g_num(m, th, tag): gates.append(((m,), np.array([[1.0 + 0j]]), th, tag))
def g_phase(m, z, tag):
    """one-particle phase z on mode m as exp(-i phi n_m)"""
    phi = -np.angle(z)
    if abs(phi) > 1e-13: g_num(m, phi, tag)
def g_signed_swap(m, n, s_mn, s_nm, tag):
    """one-particle block [[0, s_mn],[s_nm, 0]] on (m, n), s = +-1: exp(-i pi/2 sx) = -i sx, then phases"""
    g_hop(m, n, SX, np.pi / 2, tag)
    g_phase(m, 1j * s_mn, tag); g_phase(n, 1j * s_nm, tag)   # row m gets s_mn, row n gets s_nm
def apply_gates(glist, M=None):
    U = np.eye(nV, dtype=complex) if M is None else M.copy()
    for modes, k, th, tag in glist:
        w_, V_ = np.linalg.eigh(k); g = V_ @ np.diag(np.exp(-1j * th * w_)) @ V_.conj().T
        mi = list(modes); U[mi, :] = g @ U[mi, :]
    return U

# ---- (1) on-site layer V = U_H U_L by Givens elimination (Reck order), at every site
def givens_decompose(V):
    """returns list of local gates (modes in 0..n-1) in application order with prod == V"""
    n = V.shape[0]; X = V.copy(); ops = []   # ops: G with G_N...G_1 V = D
    def lphase(m, z):   # left-multiply row m by z
        X[m, :] *= z; ops.append(('ph', m, z))
    for j in range(n - 1):
        for i in range(n - 1, j, -1):
            a, b = X[i - 1, j], X[i, j]
            if abs(b) < 1e-13: continue
            if abs(a) > 1e-13: lphase(i - 1, np.exp(-1j * np.angle(a)))
            lphase(i, np.exp(-1j * np.angle(b)))
            a, b = X[i - 1, j].real, X[i, j].real
            th = np.arctan2(b, a)    # rotation R = exp(-i th sy) acting [[c,-s],[s,c]]^T ... chosen to zero row i
            c_, s_ = np.cos(th), np.sin(th)
            R = np.array([[c_, s_], [-s_, c_]])   # = exp(+i th sy)
            X[[i - 1, i], :] = R @ X[[i - 1, i], :]; ops.append(('rot', i - 1, i, -th))   # exp(-i(-th) sy)
    D = np.diag(X)
    assert np.allclose(X, np.diag(D), atol=1e-10)
    # V = G_1^{-1} ... G_N^{-1} D ; application order: D, then G_N^{-1}, ..., G_1^{-1}
    out = [('ph', m, D[m]) for m in range(n)]
    for op in reversed(ops):
        if op[0] == 'ph': out.append(('ph', op[1], np.conj(op[2])))
        else: out.append(('rot', op[1], op[2], -op[3]))
    return out
loc_ops = givens_decompose(Vos)
# local check
Ut = np.eye(12, dtype=complex)
for op in loc_ops:
    if op[0] == 'ph': Ut[op[1], :] *= op[2]
    else:
        th = op[3]; R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]]); Ut[[op[1], op[2]], :] = R @ Ut[[op[1], op[2]], :]
check("on-site Givens decomposition reproduces the 12 x 12 on-site factor U_H U_L", np.allclose(Ut, Vos, atol=1e-10),
      f"{sum(o[0]=='rot' for o in loc_ops)} rotations, {sum(o[0]=='ph' for o in loc_ops)} phase gates")
for v in TV:
    idx = [VID[(v, c)] for c in CORN]
    for op in loc_ops:
        if op[0] == 'ph': g_phase(idx[op[1]], op[2], 'onsite')
        else: g_hop(idx[op[1]], idx[op[2]], SY, op[3], 'onsite')   # exp(-i th sy) = [[c,-s],[s,c]]
n_onsite = len(gates)

# ---- (2) link reflection R_L: plaquette 4-cycles, R = A exp(pi/4 AB)
HL = H0(0.0, 1.0)
plaqs = []
seen = set()
for a_ in range(nV):
    if a_ in seen: continue
    (v, c) = VERTS[a_]; d, e = sorted(c)
    ring = [(v, frozenset((d, e))), (vmod(vadd(v, d)), frozenset((neg(d), e))),
            (vmod(vadd(vadd(v, d), e)), frozenset((neg(d), neg(e)))), (vmod(vadd(v, e)), frozenset((d, neg(e))))]
    ids = [VID[q] for q in ring]
    plaqs.append(ids); seen.update(ids)
check("the link graph is a disjoint union of 4-cycles (one per corner orbit {d,e},{-d,e},{-d,-e},{d,-e} around a plaquette): "
      "3 L^3 plaquettes cover all 12 L^3 corners once, and H_link is block diagonal on them",
      len(plaqs) == 3 * L**3 and len(seen) == nV and
      np.allclose(sum(np.abs(HL[np.ix_(p, p)]).sum() for p in plaqs), np.abs(HL).sum()))
ok_pi = True; ok_anti = True
for p in plaqs:
    h = HL[np.ix_(p, p)]
    A_ = np.zeros((4, 4)); B_ = np.zeros((4, 4))
    for (i, j) in ((0, 1), (2, 3)): A_[i, j] = A_[j, i] = h[i, j]
    for (i, j) in ((1, 2), (3, 0)): B_[i, j] = B_[j, i] = h[i, j]
    ok_pi &= np.isclose(h[0, 1] * h[1, 2] * h[2, 3] * h[3, 0], -1)
    ok_anti &= np.allclose(A_ @ B_ + B_ @ A_, 0) and np.allclose(A_ @ A_, np.eye(4)) and np.allclose(B_ @ B_, np.eye(4))
    AB = A_ @ B_
    assert np.allclose(AB, -AB.T) and np.allclose((A_ + B_) / np.sqrt(2), A_ @ (np.eye(4) + AB) / np.sqrt(2))
    # exp(pi/4 AB): AB = -i K, K = i AB Hermitian, nonzero only on diagonals (0,2), (1,3)
    K = 1j * AB
    for (i, j) in ((0, 2), (1, 3)):
        assert np.allclose(np.abs(K[i, j]), 1)
        g_hop(p[i], p[j], K[np.ix_([i, j], [i, j])], np.pi / 4, 'RL-diag')
    for (i, j) in ((0, 1), (2, 3)):
        g_signed_swap(p[i], p[j], A_[i, j], A_[j, i], 'RL-link')
check("each plaquette block of H_link has flux pi, splits into two anticommuting matchings A, B with A^2 = B^2 = 1, "
      "so R_L = (A+B)/sqrt2 = A exp((pi/4) AB) with AB supported on the two plaquette diagonals", ok_pi and ok_anti)
n_RL = len(gates) - n_onsite

# ---- (3) diagonal shift S = D_sign . S_B (on-site antipodes) . S_A (plaquette diagonals)
PA = np.zeros((nV, nV)); PB = np.zeros((nV, nV))
for p in plaqs:
    for (i, j) in ((0, 2), (1, 3)): PA[p[i], p[j]] = PA[p[j], p[i]] = 1
for v in TV:
    for c in CORN:
        d, e = tuple(c); a_ = VID[(v, c)]; b_ = VID[(v, frozenset((neg(d), neg(e))))]; PB[a_, b_] = 1
Dg = Sr @ np.linalg.inv(PB @ PA)
check("S = D . S_B . S_A with S_A = swaps of the two diagonals of every link plaquette ({d,e}@v <-> {-d,-e}@v+d+e) and S_B = on-site "
      "antipodal swaps ({d,e} <-> {-d,-e}); the residual D is a diagonal +-1 sign layer",
      np.allclose(Dg, np.diag(np.diag(Dg))) and np.allclose(np.abs(np.diag(Dg)), 1))
# sign-dressed swaps: fold D into S_B (row signs)
for p in plaqs:
    for (i, j) in ((0, 2), (1, 3)): g_signed_swap(p[i], p[j], 1.0, 1.0, 'S-diag')
done = set()
for v in TV:
    for c in CORN:
        d, e = tuple(c); a_ = VID[(v, c)]; b_ = VID[(v, frozenset((neg(d), neg(e))))]
        if a_ in done: continue
        done.update((a_, b_)); g_signed_swap(a_, b_, Dg[a_, a_], Dg[b_, b_], 'S-onsite')
n_S = len(gates) - n_onsite - n_RL

Ucirc = apply_gates(gates)
err = np.abs(Ucirc - Wref).max()
check("the explicit gate list (on-site Givens layer, plaquette layer for R_L, plaquette-diagonal + on-site antipode swaps for S) "
      "reproduces the one-particle step W entrywise on the L = 4 torus (no global phase used)", err < 1e-10, f"max |circuit - W| = {err:.2e}")
# factor-wise
U_RL = apply_gates(gates[n_onsite:n_onsite + n_RL]); U_S = apply_gates(gates[n_onsite + n_RL:])
check("factor-wise: plaquette sub-circuit == R_L and swap sub-circuit == S exactly",
      np.abs(U_RL - RLr).max() < 1e-12 and np.abs(U_S - Sr).max() < 1e-12)
# control: dropping one non-Clifford diagonal rotation changes W
bad = [g for g in gates if g[3] == 'RL-diag'][0]
Ubad = apply_gates([g for g in gates if g is not bad])
check("control: deleting a single pi/4 plaquette-diagonal rotation breaks the agreement", np.abs(Ubad - Wref).max() > 0.1,
      f"max diff {np.abs(Ubad - Wref).max():.3f}")

# ---------------- flow (one-particle GNVW) index across cuts, per axis
pos = np.array([VERTS[i][0] for i in range(nV)])
def flow(U, axis, x0=0):
    """net number of modes moving across the plane x_axis = x0 + 1/2 (range-1 unitaries, L = 4)"""
    xs = (pos[:, axis] - x0 - 1) % L          # 0,1 = slab {x0+1, x0+2}; window near first cut: xs in {L-1, 0}
    P = np.diag(((xs == 0) | (xs == 1)).astype(float))
    D = U @ P @ U.conj().T - P
    win = (xs == L - 1) | (xs == 0)
    return np.real(np.trace(D[np.ix_(win, win)]))
def rng_(U):
    r = 0
    for i, j in zip(*np.nonzero(np.abs(U) > 1e-12)):
        r = max(r, max(abs(dmod(a - b)) for a, b in zip(pos[i], pos[j])))
    return r
Von = onsite_full(Vos)
fl = {nm: [round(flow(M, ax), 9) for ax in range(3)] for nm, M in (('S', Sr), ('R_L', RLr), ('U_H U_L', Von))}
# per corner-type sublattice flow of S
sub = {}
for c in CORN:
    fv = [0, 0, 0]
    for i in range(nV):
        if VERTS[i][1] != c: continue
        j = int(np.argmax(np.abs(Sr[:, i])))
        for ax in range(3):
            dl = dmod(pos[j][ax] - pos[i][ax])
            if pos[i][ax] == 0 and dl == 1: fv[ax] += 1
            if pos[i][ax] == 1 and dl == -1: fv[ax] -= 1
    sub[tuple(sorted(c))] = fv
check("flow index: every factor has range 1 (sup norm) and zero net flow through each cut plane; within S each corner type "
      "{d,e} alone carries flow (d+e) per site and its opposite {-d,-e} carries -(d+e), cancelling pairwise",
      all(rng_(M) <= 1 for M in (Sr, RLr, Von)) and all(f == [0, 0, 0] for f in fl.values())
      and all(np.allclose(np.array(sub[k]), L**2 * (np.array(k[0]) + np.array(k[1]))) for k in sub),
      f"flows {fl}; S per-corner-type flows (units of L^2 modes) { {str(k): [x // L**2 for x in v_] for k, v_ in list(sub.items())[:4]} }")

# ---------------- Clifford tests
def monomial(U):
    re, im = np.abs(U.real), np.abs(U.imag)
    return bool(np.all((np.isclose(re, 0) | np.isclose(re, 1)) & (np.isclose(im, 0) | np.isclose(im, 1))))
mono = {nm: monomial(M) for nm, M in (('S', Sr), ('R_L', RLr), ('U_H', UH), ('U_L', UL), ('U_H U_L', Vos), ('W', Wref))}
print("Majorana-monomial (Clifford-implementable) test:", mono)
check("Majorana monomial test: S is a signed permutation (Clifford); R_L, U_H, U_L and W are not, so no Clifford circuit "
      "on the corner code implements them", mono['S'] and not any(mono[k] for k in ('R_L', 'U_H', 'U_L', 'W')))

def classify(th):
    """Pauli rotation angle alpha = th/2 (image of exp(-i th k) is exp(-i th/2 P1) exp(-+ i th/2 P2))"""
    a = (th / 2) / (np.pi / 8); r = round(a)
    if abs(a - r) > 1e-9: return 'irrational/other'
    return 'Clifford' if r % 2 == 0 else 'pi/8 (T-type)'
census = {}
for modes, k, th, tag in gates:
    key = (tag, 'hop' if len(modes) == 2 else 'num', classify(th)); census[key] = census.get(key, 0) + 1
print("gate census over the torus (tag, kind, Pauli-angle class): count")
for k_, v_ in sorted(census.items()): print(f"   {k_}: {v_}   ({v_ / L**3:g} per site)")
loc_rot = [o[3] for o in loc_ops if o[0] == 'rot']
loc_ph = [-np.angle(o[2]) for o in loc_ops if o[0] == 'ph']
print("on-site rotation angles theta/pi:", np.round(np.array(loc_rot) / np.pi, 6))
print("on-site phase angles phi/pi:", np.round(np.array(loc_ph) / np.pi, 6))
check("angle census: S gates are all Clifford (Pauli angles in (pi/4)Z); R_L uses exactly 4 pi/8 Pauli rotations per plaquette "
      "(12 per site) plus Clifford swaps; the on-site factor needs Pauli angles outside (pi/8)Z",
      all(c_ == 'Clifford' for (t_, kd, c_) in census if t_.startswith('S'))
      and census.get(('RL-diag', 'hop', 'pi/8 (T-type)'), 0) == 2 * 3 * L**3
      and all(c_ == 'Clifford' for (t_, kd, c_) in census if t_ == 'RL-link')
      and any(c_ == 'irrational/other' for (t_, kd, c_) in census if t_ == 'onsite'))

# depth (greedy ASAP layering of 2-mode / 1-mode gates; gates on disjoint modes commute)
def depth(glist, only2=False):
    t = {}
    D_ = 0
    for modes, k, th, tag in glist:
        if only2 and len(modes) == 1: continue
        l = max(t.get(m, 0) for m in modes) + 1
        for m in modes: t[m] = l
        D_ = max(D_, l)
    return D_
print(f"ASAP depth (2-mode gates only / all gates): on-site {depth(gates[:n_onsite], True)}/{depth(gates[:n_onsite])}, "
      f"R_L {depth(gates[n_onsite:n_onsite+n_RL], True)}/{depth(gates[n_onsite:n_onsite+n_RL])}, "
      f"S {depth(gates[n_onsite+n_RL:], True)}/{depth(gates[n_onsite+n_RL:])}, total {depth(gates, True)}/{depth(gates)}")
np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Wref_check.npy'), np.array([err]))
print(f"\nPart A TOTAL: PASS={PASS} FAIL={FAIL}")
