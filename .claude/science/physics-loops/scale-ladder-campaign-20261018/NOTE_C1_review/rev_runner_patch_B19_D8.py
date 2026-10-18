#!/usr/bin/env python3
"""Corner-fermion eight-node step: the doublers cannot be selectively gapped under full O; pairing is all-or-nothing,
and the doublers (like +-k*) carry a Z2 Weyl dipole pi(1,1,1).

Supplied model only (corner fermion, flux square = plaquette = tube = pi, triangle = 0; the eight-node step
W = S . R_L . U_H . U_Lambda of the cross-rung note, item 6); no physical identification.

Two code paths build the same step independently:
  Section A  repo-model path (campaign C1): gauge, PSG lifts and step factors from the repo model
             (scripts/corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17.py), as in the
             cross-rung runner; Bloch convention H(k) = sum_d h_d e^{+ik.d}.
  Section B  independent-core path (campaign C1_check): own GF(2) gauge solve, own brute-force PSG over all
             2^15 (lam, tau) per O_h element, own step factors; Bloch convention H(k) = sum_d h_d e^{-ik.d};
             chiralities by Berry flux.
  Section C  cross-path agreement of the convention-independent data.
  Section E  exact bookkeeping in integer arithmetic (units of pi/2) and the 2O character products behind decoupling.
  Section D  (only with --bdg) Floquet-BdG spot checks: numerical illustrations, not certificates.

Checks (exact unless marked numerical):
  determinant lemma: det(U_g|V) is a genuine character, the same for every 2-fold level at +-k* (A2 for the real
    signed-permutation lift) and its D4 restriction (B1) at every doubler level; rephasing the lifts relabels it A1;
  selection rule: on-site and range-1 pairing channels at Q = R: chi = det gives the singlet at all eight nodes,
    chi != det at none (null-space certificates; exact zeros to ~1e-14); Q in {0, R}; O_h version;
  subgroup scope: selective channels exist only for |H| <= 12 (T with chi(C3) = omega), none for H = O;
  decoupling at +-k*: an A2-channel pairing has zero blocks between the node doublet and every other level;
  anomaly: chiralities (two methods), Weyl-dipole table, Q = 0 BdG charge +-2, slice obstruction with C2x only.
Usage:  python3 <this file> [--bdg]     default ~2-3 min; --bdg adds ~3-5 min.
Companion: docs/CORNER_FERMION_EIGHT_CUBE_NODES_CANNOT_BE_SELECTIVELY_GAPPED_UNDER_FULL_OCTAHEDRAL_SYMMETRY_PAIRING_IS_ALL_OR_NOTHING_AND_THE_DOUBLERS_CARRY_A_Z2_WEYL_DIPOLE_BOUNDED_THEOREM_NOTE_2026-10-18.md
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "2")
import cmath, itertools, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
BDG = '--bdg' in sys.argv
T0 = time.time()
PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


A2_CLASS = {'E': 1, 'C3': 1, 'C2': 1, 'C4': -1, "C2'": -1}


def cls(M):
    t = int(round(np.trace(M)))
    if t == 3: return 'E'
    if t == 0: return 'C3'
    if t == 1: return 'C4'
    return 'C2' if all(abs(M[i, i]) == 1 for i in range(3)) else "C2'"


PAU = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
SG = np.array([1, -1, 1])


# =====================================================================================================================
# Section A: repo-model path (C1 code path)
# =====================================================================================================================
def section_A():
    print("\n=== Section A: repo-model construction path (campaign C1) ===", flush=True)
    t0 = time.time()
    import corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17 as _model
    C = _model._run_reviewed_program(definitions_only=True)
    L = C['L']; VERTS = C['VERTS']; nV = len(VERTS); CORN = C['CORNERS']; ROTS = C['ROTS']; DIRS = C['DIRS']
    F = dict(square=1, triangle=0, plaquette=1, tube=1)
    def dmod(x): return ((x + 1) % L) - 1
    def neg(d): return tuple(-x for x in d)
    def perp(d, e): return sum(a * b for a, b in zip(d, e)) == 0 and d != e
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
    def vadd(a, b): return tuple(x + y for x, y in zip(a, b))
    cell = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
    for d in DIRS:
        a = [f for f in DIRS if perp(f, d) and f != neg(d)]; a0 = a[0]
        b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]; ring = [a0, b0, neg(a0), neg(b0)]
        cell['square'].append(cyc([(frozenset((d, r)), Z0) for r in ring]))
        for i in range(4):
            p, q = ring[i], ring[(i + 1) % 4]
            cell['tube'].append(cyc([(frozenset((d, p)), Z0), (frozenset((neg(d), p)), d), (frozenset((neg(d), q)), d), (frozenset((d, q)), Z0)]))
    for s in itertools.product((1, -1), repeat=3):
        x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
        cell['triangle'].append(cyc([(frozenset((x, y)), Z0), (frozenset((y, z)), Z0), (frozenset((z, x)), Z0)]))
    for d, e in (((1, 0, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 1)), ((0, 0, 1), (1, 0, 0))):
        cell['plaquette'].append(cyc([(frozenset((d, e)), Z0), (frozenset((neg(d), e)), d), (frozenset((neg(d), neg(e))), vadd(d, e)), (frozenset((d, neg(e))), e)]))
    rows = []; rhs = []
    for k_, cs in cell.items():
        for c in cs: rows.append(c); rhs.append(F[k_])
    ucell = C['gf2_solve'](rows, rhs, nT)
    u = np.zeros(C['nE'], np.uint8)
    for key, i in C['EID'].items():
        a, b = tuple(key); (v, c), (w, c2) = VERTS[a], VERTS[b]
        u[i] = ucell[ekey[(c, c2, tuple(dmod(y - x) for x, y in zip(v, w)))]]
    assert all({int(sum(u[j] for j in c) % 2) for c in cs} == {F[k_]} for k_, cs in C['cycles'].items())
    INVM = -np.eye(3, dtype=int)
    psg = lambda f: C['psg_sign'](f, u)
    rots = [psg(lambda q, M=R: C['rot_vert'](M, q)) for R in ROTS]
    invs = [psg(lambda q, M=R @ INVM: C['rot_vert'](M, q)) for R in ROTS]
    TV = list(itertools.product(range(L), repeat=3))
    trans = [psg(lambda q, t=t: C['trans_vert'](t, q)) for t in TV]
    def conj(Xm, P, s):
        sg = (-1.0) ** s; Y = np.zeros_like(Xm); Y[np.ix_(P, P)] = Xm * np.outer(sg, sg); return Y
    def opmat_from(P, s):
        M = np.zeros((nV, nV)); M[P, np.arange(nV)] = (-1.0) ** s; return M
    loc0 = [C['VID'][((0, 0, 0), c)] for c in CORN]; CI = {c: i for i, c in enumerate(CORN)}
    def H0(t1, t2):
        H = np.zeros((nV, nV))
        for key in C['EDGES']:
            i, j = tuple(key); t = t1 if C['edges'][key] == 'onsite' else t2
            H[i, j] = H[j, i] = -t * (-1.0) ** u[C['EID'][key]]
        return H
    def blocks_from(Hr):
        bl = {}
        for a, v in enumerate(VERTS):
            sh = tuple(dmod(x) for x in v[0])
            for bi, j in enumerate(loc0):
                if abs(Hr[a, j]) > 1e-12: bl.setdefault(sh, np.zeros((12, 12), complex))[CI[v[1]], bi] += Hr[a, j]
        return bl
    def Hk(bl, k):
        H = np.zeros((12, 12), complex)
        for sh, M in bl.items(): H += M * np.exp(1j * np.dot(k, sh))
        return H
    kst = np.array([1, -1, 1]) * np.pi / 2
    def Bloch(k):
        B = np.zeros((nV, 12), complex)
        for a, (v, c) in enumerate(VERTS): B[a, CI[c]] = np.exp(1j * np.dot(k, v)) / np.sqrt(L ** 3)
        return B
    def wrap(x): return np.angle(np.exp(1j * x))
    RLr = H0(0.0, 1.0) / np.sqrt(2); blL = blocks_from(RLr); HonR = H0(1.0, 0.0)
    c_xy = [c for c in CORN if set(c) == {(1, 0, 0), (0, 1, 0)}][0]
    i0 = C['VID'][((0, 0, 0), c_xy)]; j0 = C['VID'][((1, 1, 0), c_xy)]
    Sr = np.zeros((nV, nV))
    for Pr, sr in rots:
        for Pt, st in trans:
            P = Pt[Pr]; s_ = sr ^ st[Pr]; Sr[P[j0], P[i0]] += (-1.0) ** (int(s_[i0]) + int(s_[j0]))
    Sr /= np.abs(Sr).max()
    assert np.allclose(Sr @ Sr.T, np.eye(nV)) and all(np.allclose(conj(Sr, P, s_), Sr) for P, s_ in rots + trans[:5])
    Lam = np.zeros((12, 12), complex)
    for sg in itertools.product((1, -1), repeat=3):
        x, y, z = (sg[0], 0, 0), (0, sg[1], 0), (0, 0, sg[2])
        cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
        if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
        for a_ in range(3):
            q_, r_ = cy[a_], cy[(a_ + 1) % 3]; ii, jj = C['VID'][((0, 0, 0), q_)], C['VID'][((0, 0, 0), r_)]
            amp = 1j * (-1.0) ** u[C['EID'][frozenset((ii, jj))]]; Lam[CI[r_], CI[q_]] += amp; Lam[CI[q_], CI[r_]] += np.conj(amp)
    def eproj(M):
        w_, V_ = np.linalg.eigh(M); ls = sorted(set(np.round(w_, 6)))
        return [V_[:, np.abs(w_ - l) < 1e-6] @ V_[:, np.abs(w_ - l) < 1e-6].conj().T for l in ls]
    Hon0 = (Bloch(np.zeros(3)).conj().T @ HonR @ Bloch(np.zeros(3)))
    PH, PLm = eproj(Hon0), eproj(Lam)
    UH = PH[0] - PH[1] - 1j * PH[2]; UL = PLm[0] + 1j * PLm[1] + 1j * PLm[2] + PLm[3]
    blS = blocks_from(Sr)
    UU = UH @ UL
    def W(k): return Hk(blS, k) @ Hk(blL, k) @ UU
    def dHk(bl, k, j):
        H = np.zeros((12, 12), complex)
        for sh, Mx in bl.items(): H += 1j * sh[j] * Mx * np.exp(1j * np.dot(k, sh))
        return H
    def dW(k, j): return (dHk(blS, k, j) @ Hk(blL, k) + Hk(blS, k) @ dHk(blL, k, j)) @ UU
    def fibre_matrix(P, s):
        U = np.zeros((12, 12))
        for ci, a in enumerate(loc0):
            v2, c2 = VERTS[P[a]]
            assert tuple(v2) == (0, 0, 0)
            U[CI[c2], ci] = (-1.0) ** int(s[a])
        return U
    def find_kmap(U, M, fun, ks):
        for th in itertools.product((0, 1), repeat=3):
            th = np.pi * np.array(th)
            if all(np.allclose(U @ fun(k) @ U.T, fun(M @ k + th), atol=1e-10) for k in ks): return th
        return None
    _KT = np.random.default_rng(2026).uniform(-np.pi, np.pi, (4, 3))
    ROT = []
    for R, (P, s) in zip(ROTS, rots):
        U = fibre_matrix(P, s); ROT.append(dict(M=R.astype(int), U=U, th=find_kmap(U, R.astype(float), W, _KT)))
    def gk(g, k): return g['M'] @ k + g['th']
    def same_k(a, b): return np.allclose(np.exp(1j * (np.asarray(a) - np.asarray(b))), 1, atol=1e-9)
    def stab(k): return [i for i, g in enumerate(ROT) if same_k(gk(g, k), k)]
    def find(Mx):
        for j, h in enumerate(ROT):
            if (h['M'] == Mx).all(): return j
    Q_R = np.pi * np.ones(3)
    NODES = {'k*': kst, '-k*': -kst}
    for i, ax in enumerate('xyz'):
        NODES[f'k*+pi e{ax}'] = kst + np.pi * np.eye(3)[i]
        NODES[f'-k*+pi e{ax}'] = -kst + np.pi * np.eye(3)[i]
    NVEC = {nm: tuple(int(x) for x in np.round(np.mod((k - kst) / np.pi, 2)).astype(int) % 2) for nm, k in NODES.items()}
    def level(k, E, tol=1e-7):
        e, V = np.linalg.eig(W(k)); ph = np.angle(e); sel = np.abs(wrap(ph - E)) < tol
        Qm, _ = np.linalg.qr(V[:, sel]); return Qm
    def all_levels(k, tol=1e-7):
        e, V = np.linalg.eig(W(k)); ph = np.angle(e); used = np.zeros(12, bool); out = []
        for i in np.argsort(ph):
            if used[i]: continue
            grp = np.where((~used) & (np.abs(wrap(ph - ph[i])) < tol))[0]; used[grp] = True
            Qm, _ = np.linalg.qr(V[:, grp]); out.append((ph[i], len(grp), Qm))
        return out
    def weyl_data(k, Qm):
        Wk = W(k); A = [-1j * Qm.conj().T @ Wk.conj().T @ dW(k, j) @ Qm for j in range(3)]
        a = np.array([np.trace(x).real / 2 for x in A])
        B = np.array([[np.trace(A[j] @ PAU[b]).real / 2 for b in range(3)] for j in range(3)])
        return a, B
    print(f"   model built in {time.time() - t0:.1f}s", flush=True)
    rng = np.random.default_rng(7)
    out = {}

    # ---- A1-A3 fibre maps ----
    KR = rng.uniform(-np.pi, np.pi, (6, 3))
    ok = all(np.allclose(g['U'] @ W(k) @ g['U'].T, W(gk(g, k)), atol=1e-10) for g in ROT for k in KR)
    check("A1 fibre maps U_g W(k) U_g^T = W(M_g k + pi s_g) for all 24 dressed rotations (6 random k); exactly 21 have s_g != 0",
          ok and sum(np.any(g['th'] != 0) for g in ROT) == 21)
    mult_ok = th_ok = True
    for g in ROT:
        for h in ROT:
            j = find(g['M'] @ h['M']); P_ = g['U'] @ h['U']
            mult_ok &= np.allclose(P_, ROT[j]['U']) or np.allclose(P_, -ROT[j]['U'])
            th_ok &= same_k(g['M'] @ h['th'] + g['th'], ROT[j]['th'])
    check("A2 projective closure U_g U_h = +-U_gh (cocycle +-1) and the affine shifts compose", mult_ok and th_ok)
    ax = [find(np.diag(d)) for d in ([1, -1, -1], [-1, 1, -1], [-1, -1, 1])]
    check("A3 the three axis-C2 lifts pairwise anticommute on C^12",
          all(np.allclose(ROT[a]['U'] @ ROT[b]['U'], -ROT[b]['U'] @ ROT[a]['U']) for a in ax for b in ax if a != b))

    # ---- A4 node table ----
    vs = np.sqrt(2) / 3; TAB = {}
    for E in (np.pi / 2, -np.pi / 2):
        for nm, k in NODES.items():
            Qm = level(k, E); a, B = weyl_data(k, Qm); sv = np.linalg.svd(B, compute_uv=False)
            TAB[(nm, E)] = dict(Q=Qm, dim=Qm.shape[1], sv=np.sort(sv), chi=int(np.sign(np.linalg.det(B))), tilt=np.linalg.norm(a))
    ok = all(r['dim'] == 2 for r in TAB.values())
    ok &= all(np.allclose(TAB[(nm, np.pi / 2)]['sv'], vs, atol=1e-8) for nm in ('k*', '-k*'))
    ok &= all(np.allclose(TAB[(nm, np.pi / 2)]['sv'], [0.2467203, 0.5837466, 0.5837466], atol=2e-7) for nm in NODES if '+pi' in nm)
    chi_n = {nm: TAB[(nm, np.pi / 2)]['chi'] for nm in NODES}
    ok &= all(chi_n[nm] == (-1) ** sum(NVEC[nm]) * chi_n['k*'] for nm in NODES)
    ok &= all(TAB[(nm, -np.pi / 2)]['chi'] == -chi_n[nm] for nm in NODES)
    check("A4 (numerical, degenerate PT) at E = +pi/2 all eight cube points carry 2-fold Weyl doublets: +-k* isotropic sqrt2/3, doublers "
          "uniaxial (0.2467, 0.5837); chirality(k* + pi n) = (-1)^|n| chirality(k*); the -pi/2 set has the opposite chiralities", ok,
          f"chiralities {chi_n}")
    out['speeds'] = (TAB[('k*', np.pi / 2)]['sv'], TAB[('k*+pi ex', np.pi / 2)]['sv'])
    out['chi_rel'] = {NVEC[nm]: chi_n[nm] * chi_n['k*'] for nm in NODES}

    # ---- A5-A6 determinant characters ----
    def det_char(Qm, idx): return {i: np.linalg.det(Qm.conj().T @ ROT[i]['U'] @ Qm) for i in idx}
    def is_char(dc):
        okc = all(abs(abs(v) - 1) < 1e-9 for v in dc.values())
        for i in dc:
            for j in dc:
                l = find(ROT[i]['M'] @ ROT[j]['M'])
                if l in dc: okc &= abs(dc[i] * dc[j] - dc[l]) < 1e-9
        return okc
    O_idx = list(range(24))
    dets_star = [(nm, E, det_char(Qm, O_idx)) for nm in ('k*', '-k*') for E, m, Qm in all_levels(NODES[nm]) if m == 2]
    ref = dets_star[0][2]
    uniform = all(all(abs(dc[i] - ref[i]) < 1e-9 for i in O_idx) for _, _, dc in dets_star)
    isA1 = all(abs(ref[i] - 1) < 1e-9 for i in O_idx); isA2 = all(abs(ref[i] - A2_CLASS[cls(ROT[i]['M'])]) < 1e-9 for i in O_idx)
    DETNAME = 'A1' if isA1 else ('A2' if isA2 else '?')
    check("A5 det(U_g|V) is a genuine 1-dim character of O, the same for every 2-fold level at k* and -k* (all quasi-energies); "
          "for the real signed-permutation lift it is A2", all(is_char(dc) for _, _, dc in dets_star) and uniform and DETNAME == 'A2',
          f"{len(dets_star)} doublets; det character = {DETNAME}")
    chi_det = {i: A2_CLASS[cls(ROT[i]['M'])] for i in O_idx}; chi_oth = {i: 1 for i in O_idx}
    ok = True; nd = 0
    for nm, k in NODES.items():
        if '+pi' not in nm: continue
        st = stab(k)
        for E, m, Qm in all_levels(k):
            if m != 2: continue
            dc = det_char(Qm, st); ok &= is_char(dc) and all(abs(dc[i] - chi_det[i]) < 1e-9 for i in st); nd += 1
    a2r = all(any(abs(chi_oth[i] - chi_det[i]) > 1 for i in stab(NODES[nm])) for nm in NODES if '+pi' in nm)
    check("A6 at each doubler (little group D4) every 2-fold level has det = A2|D4 (= B1); A1|D4 differs", ok and a2r and nd == 36,
          f"{nd} doubler doublets")
    out['det'] = DETNAME

    # ---- A7 real-space convention ----
    AB = []
    for i in range(12):
        for j in range(i + 1, 12):
            X = np.zeros((12, 12)); X[i, j] = 1; X[j, i] = -1; AB.append(X)
    def channel_space(chi, Ulist):
        rowsM = [np.array([(U @ X @ U.T - c * X)[np.triu_indices(12, 1)] for X in AB]).T for U, c in zip(Ulist, chi)]
        _, s, Vh = np.linalg.svd(np.vstack(rowsM)); s = np.concatenate([s, np.zeros(Vh.shape[0] - len(s))])
        return [sum(cf * X for cf, X in zip(v, AB)) for v in Vh[s < 1e-10]]
    UO = [g['U'] for g in ROT]
    Vdet = channel_space([chi_det[i] for i in O_idx], UO); Voth = channel_space([chi_oth[i] for i in O_idx], UO)
    out['dims'] = (len(Vdet), len(Voth))
    def rnd(V): return sum(rng.normal() * X for X in V)
    A_det = rnd(Vdet); A_det /= np.linalg.norm(A_det); A_oth = rnd(Voth); A_oth /= np.linalg.norm(A_oth)
    Dd = np.zeros((nV, nV), complex)
    for a, (v, c) in enumerate(VERTS):
        for c2 in CORN: Dd[a, C['VID'][(v, c2)]] = np.exp(1j * np.dot(Q_R, v)) * A_det[CI[c], CI[c2]]
    ok = all(np.allclose(conj(Dd, P, s_), chi_det[i] * Dd) for i, (P, s_) in enumerate(rots))
    odd_t = [t for t in TV if sum(t) % 2 == 1][:3]; ev_t = [t for t in TV if sum(t) % 2 == 0 and any(t)][:3]
    ok_t = all(np.allclose(conj(Dd, *trans[TV.index(t)]), -Dd) for t in odd_t) and all(np.allclose(conj(Dd, *trans[TV.index(t)]), Dd) for t in ev_t)
    ok_neg = not all(np.allclose(conj(Dd, P, s_), chi_oth[i] * Dd) for i, (P, s_) in enumerate(rots))
    check("A7 real-space L = 4 cross-check of the pairing convention: D = sum_v e^{iR.v} A_v obeys R_g D R_g^T = chi(g) D for all 24 lifts; "
          "odd translations give -D (absorbed by the U(1) dressing e^{i pi |e| N/2}); negative control fails", ok and ok_t and ok_neg,
          f"dim V_det = {len(Vdet)}, dim V_A1 = {len(Voth)} (of 66)")

    # ---- A8-A9 on-site singlets ----
    def singlet(Qm, Dm): return (Qm.conj().T @ Dm @ Qm.conj())[0, 1]
    ok = True; info = []
    for E in (np.pi / 2, -np.pi / 2):
        md = {nm: abs(singlet(TAB[(nm, E)]['Q'], A_det)) for nm in NODES}
        mo = {nm: abs(singlet(TAB[(nm, E)]['Q'], A_oth)) for nm in NODES}
        ok &= min(md.values()) > 1e-3 and max(mo.values()) < 1e-12; info.append(f"E={E:+.2f}: det min {min(md.values()):.3f}, A1 max {max(mo.values()):.1e}")
    check("A8 on-site pairing at Q = R (both node sets): channel chi = det gives a nonzero singlet at all eight nodes, chi = A1 exactly zero "
          "at all eight", ok, "; ".join(info))
    Fm = np.array([[singlet(TAB[(nm, np.pi / 2)]['Q'], X) for X in Vdet] for nm in NODES]); rk = np.linalg.matrix_rank(Fm, tol=1e-9)
    _, s, Vh = np.linalg.svd(Fm[:2]); nullv = Vh[np.sum(s > 1e-9):]
    cvec = nullv.T @ rng.normal(size=len(nullv)); A_t = sum(ci * X for ci, X in zip(cvec, Vdet))
    mt = {nm: abs(singlet(TAB[(nm, np.pi / 2)]['Q'], A_t)) for nm in NODES}
    check("A9 the node-singlet functionals on V_det have rank 3 (k*, -k*, doublers): m_{+-k*} = 0 is a tuning; an on-site example with "
          "m_{+-k*} = 0 and all six doubler singlets nonzero exists", rk == 3 and max(mt['k*'], mt['-k*']) < 1e-12
          and min(v for nm, v in mt.items() if '+pi' in nm) > 1e-3, f"rank {rk}; tuned doubler |m| = {min(v for nm, v in mt.items() if '+pi' in nm):.3f}")

    # ---- A10 k-dependent pairings ----
    shifts = list(itertools.product((-1, 0, 1), repeat=3))
    def seed_delta():
        C0 = {s_: rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12)) for s_ in shifts}
        return lambda k: sum(Cm * np.exp(1j * np.dot(k, s_)) for s_, Cm in C0.items())
    def symmetrize(D0, chi, Q):
        def Dk(k):
            Dfa = lambda kk: 0.5 * (D0(kk) - D0(Q - kk).T)
            return sum(np.conj(chi[i]) * ROT[i]['U'].T @ Dfa(gk(ROT[i], k)) @ ROT[i]['U'] for i in O_idx) / 24
        return Dk
    res = {}
    for Qn, Q in (('R', Q_R), ('0', np.zeros(3))):
        for cn, chi in (('A2', chi_det), ('A1', chi_oth)):
            Dk = symmetrize(seed_delta(), chi, Q); kt = rng.uniform(-np.pi, np.pi, (2, 3))
            symok = all(np.allclose(Dk(gk(ROT[i], k)), chi[i] * ROT[i]['U'] @ Dk(k) @ ROT[i]['U'].T, atol=1e-10) for i in O_idx[::5] for k in kt)
            fermi = all(np.allclose(Dk(k), -Dk(Q - k).T, atol=1e-10) for k in kt)
            if Qn == 'R': m = {nm: abs(singlet(TAB[(nm, np.pi / 2)]['Q'], Dk(NODES[nm]))) for nm in NODES}
            else: m = {nm: np.abs(TAB[(nm, np.pi / 2)]['Q'].conj().T @ Dk(NODES[nm]) @ level(-NODES[nm], np.pi / 2).conj()).max() for nm in NODES}
            res[(Qn, cn)] = (symok and fermi, m)
    ok = all(v[0] for v in res.values()) and min(res[('R', 'A2')][1].values()) > 1e-4 and max(res[('R', 'A1')][1].values()) < 1e-11
    check("A10 random range-1 k-dependent symmetric Delta(k) (group-averaged, Fermi-antisymmetrised): at Q = R the singlet is nonzero at all "
          "eight (chi = det) or zero at all eight (chi = A1); at Q = 0 the K <-> -K blocks are generic for A1, zero for A2", ok
          and min(res[('0', 'A1')][1].values()) > 1e-3 and max(res[('0', 'A2')][1].values()) < 1e-11)

    # ---- A11-A12 O_h ----
    IMP = []
    for R, (P, s_) in zip(ROTS, invs):
        U = fibre_matrix(P, s_); M = (R @ INVM).astype(int); IMP.append(dict(M=M, U=U, th=find_kmap(U, M.astype(float), W, KR[:4]), R=R))
    inv_el = [g for g in IMP if (g['R'] == np.eye(3)).all()][0]
    check("A11 all 24 improper dressed lifts are unitary symmetries of the step; the pure inversion has zero shift, maps K -> -K and fixes no node",
          all(g['th'] is not None for g in IMP) and same_k(inv_el['th'], np.zeros(3)))
    OH_ALL = ROT + IMP; okc = True; dims_oh = {}
    for base in ('A1', 'A2'):
        for par in ('g', 'u'):
            chi = [(1 if base == 'A1' else A2_CLASS[cls(g['M'] if j < 24 else g['R'])]) * (1 if (j < 24 or par == 'g') else -1) for j, g in enumerate(OH_ALL)]
            Vc = channel_space(chi, [g['U'] for g in OH_ALL]); dims_oh[base + par] = len(Vc)
            if not Vc: continue
            Ac = sum((rng.normal() + 1j * rng.normal()) * X for X in Vc)
            m = {nm: abs(singlet(TAB[(nm, np.pi / 2)]['Q'], Ac)) for nm in NODES}
            pair_eq = all(abs(m[nm] - m[[n2 for n2, kk in NODES.items() if same_k(kk, -NODES[nm])][0]]) < 1e-9 for nm in NODES)
            okc &= (min(m.values()) > 1e-4 and pair_eq) if base == 'A2' else max(m.values()) < 1e-11
    check("A12 O_h channels: A2g, A2u allow the singlet at all eight with |m_K| = |m_-K|; A1g, A1u forbid it at all eight (or are empty)", okc,
          str(dims_oh))
    out['dims_oh'] = dims_oh

    # ---- A13 decoupling at +-k* ----
    cross = 0.0
    for nm in ('k*', '-k*'):
        Dn = TAB[(nm, np.pi / 2)]['Q']
        for E, m, Qm in all_levels(NODES[nm]):
            if abs(wrap(E - np.pi / 2)) < 1e-6: continue
            cross = max(cross, max(np.abs(Dn.conj().T @ X @ Qm.conj()).max() for X in Vdet))
    check("A13 decoupling at +-k*: every on-site chi = det (A2) pairing matrix has zero blocks between the node doublet and all other levels",
          cross < 1e-12, f"max cross block {cross:.1e}")

    # ---- A14-A20 anomaly bookkeeping ----
    def orbit(nm):
        o = set()
        for g in ROT: o |= {m for m, kk in NODES.items() if same_k(gk(g, NODES[nm]), kk)}
        return frozenset(o)
    orbits = sorted({orbit(nm) for nm in NODES}, key=lambda o: (len(o), sorted(o)))
    check("A14 four rotation orbits {k*}, {-k*}, A = {k*+pi e_i}, B = {-k*+pi e_i}, chirality constant on each, net chirality 0",
          len(orbits) == 4 and all(len({chi_n[m] for m in o}) == 1 for o in orbits) and sum(chi_n.values()) == 0)
    ok = True
    for nm, k in NODES.items():
        psi = Bloch(-k) @ level(k, np.pi / 2)[:, 0]
        for t in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            ph = np.vdot(psi, opmat_from(*trans[TV.index(t)]) @ psi)
            ok &= np.isclose(ph, np.exp(1j * np.dot(k, t))) and np.isclose(ph / np.exp(1j * np.dot(kst, t)), (-1) ** int(np.array(NVEC[nm]) @ np.array(t)))
    check("A15 (L = 4 real space) unit translations act on each node doublet by a phase; after the common U(1) phase e^{ik*.e} the IR action "
          "is the taste sign (-1)^{n.e}, an IR Z2^3", ok)
    lab_of = lambda o: '{k*}' if o == {'k*'} else '{-k*}' if o == {'-k*'} else ('A' if 'k*+pi ex' in o else 'B')
    free = []; rowsb = {}
    for r in range(5):
        for combo in itertools.combinations(range(4), r):
            S = set().union(*[orbits[i] for i in combo]) if combo else set()
            nchi = sum(chi_n[m] for m in S); b = sum((chi_n[m] * NODES[m] for m in S), np.zeros(3))
            bmod = np.round(np.mod(b, 2 * np.pi) / np.pi, 6) % 2
            z2 = tuple(int(sum(chi_n[m] for m in S if NVEC[m][i] == 1)) % 2 for i in range(3))
            lab = '+'.join(sorted(lab_of(orbits[i]) for i in combo)) or 'empty'; rowsb[lab] = (nchi, bmod, z2)
            if nchi == 0 and np.allclose(bmod, 0) and z2 == (0, 0, 0): free.append(lab)
    check("A16 Weyl-dipole table: doublers A+B and {+-k*} each have net chirality 0 and b = pi(1,1,1) mod 2pi (U(1)^2-Z2 counts (1,1,1)); "
          "only 'empty' and 'all eight' are anomaly-free among rotation-invariant subsets",
          sorted(free) == sorted(['empty', 'A+B+{-k*}+{k*}']) and rowsb['A+B'][0] == 0 and np.allclose(rowsb['A+B'][1], 1)
          and rowsb['{-k*}+{k*}'][0] == 0 and np.allclose(rowsb['{-k*}+{k*}'][1], 1), f"anomaly-free: {free}")
    out['free'] = len(free)
    Sd = [m for m in NODES if '+pi' in m]
    b1 = sum(chi_n[m] * NODES[m] for m in Sd)
    b2 = sum(chi_n[m] * (NODES[m] + 2 * np.pi * np.array(sh)) for m, sh in zip(Sd, itertools.cycle([(1, 0, 0), (0, -1, 1), (2, 0, 0)])))
    check("A17 for a zero-net-chirality set, b mod 2pi Z^3 does not depend on the momentum representatives", np.allclose(np.exp(1j * (b1 - b2)), 1))
    bq0 = {nm: chi_n[nm] - chi_n[[m for m, kk in NODES.items() if same_k(kk, -NODES[nm])][0]] for nm in NODES}
    check("A18 Q = 0 pairing: every BdG point K carries Weyl charge chi_K - chi_{-K} = +-2, so no small Q = 0 pairing gaps any node",
          all(abs(v) == 2 for v in bq0.values()))
    ok = True; rinv = []
    for p in itertools.product((0, 1), repeat=3):
        p = np.array(p); Q = np.pi * p
        if all(same_k(g['M'] @ Q, Q) for g in ROT): rinv.append(tuple(p))
        pairs = []
        for nm in NODES:
            partner = [m for m, kk in NODES.items() if same_k(kk, Q - NODES[nm])]; ok &= len(partner) == 1
            pairs.append(chi_n[nm] == chi_n[partner[0]])
        ok &= all(pairs) if p.sum() % 2 == 1 else not any(pairs)
    check("A19 Q = pi p maps the eight nodes to themselves; partners have equal chirality (gappable) iff |p| odd; rotation-invariant: only "
          "Q = 0 (protected) and Q = R (intra-node, gappable)", ok and rinv == [(0, 0, 0), (1, 1, 1)])
    seen = []
    for Lt in (1, 3, 5, 7, 9, 11):
        for th in (kst, -kst):
            for sgn in (1, -1): seen.append(sorted(nm for nm, k in NODES.items() if same_k(sgn * Lt * k, th)))
    check("A20 on every odd-L twisted torus of the odd-filling note (theta = +-k*, L = 1..11) the allowed momenta contain exactly one of "
          "+-k* and none of the six doublers", all(len(v) == 1 and v[0] in ('k*', '-k*') for v in seen))
    print(f"   Section A done in {time.time() - t0:.0f}s", flush=True)
    return out


# =====================================================================================================================
# Section B: independent-core path (C1_check code path)
# =====================================================================================================================
def section_B():
    print("\n=== Section B: independent-core path (campaign C1_check: own gauge, own brute-force PSG) ===", flush=True)
    t0 = time.time()
    from scipy.linalg import expm
    DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    def dot(a, b): return sum(x * y for x, y in zip(a, b))
    def neg(a): return tuple(-x for x in a)
    def vadd(a, b): return tuple(x + y for x, y in zip(a, b))
    CORN = [frozenset((d, e)) for d, e in itertools.combinations(DIRS, 2) if dot(d, e) == 0]
    CI = {c: i for i, c in enumerate(CORN)}; Z = (0, 0, 0)
    def third(a, b): return [f for f in DIRS if dot(f, a) == 0 and dot(f, b) == 0]
    def edge_key(c1, c2, s):
        k1 = (CI[c1], CI[c2], tuple(s)); k2 = (CI[c2], CI[c1], neg(s)); return min(k1, k2)
    ETYPES = {}
    for c in CORN:
        a, b = tuple(c)
        for x, y in ((a, b), (b, a)):
            for f in third(x, y): ETYPES.setdefault(edge_key(c, frozenset((x, f)), Z), len(ETYPES))
            ETYPES.setdefault(edge_key(c, frozenset((neg(x), y)), x), len(ETYPES))
    NT = len(ETYPES); ELIST = sorted(ETYPES, key=ETYPES.get)
    def gf2_solve(A, b):
        A = (np.array(A, np.uint8) % 2).copy(); b = (np.array(b, np.uint8) % 2).copy()
        m, n = A.shape; M = np.concatenate([A, b[:, None]], 1); r = 0; piv = []
        for col in range(n):
            rws = np.nonzero(M[r:, col])[0]
            if len(rws) == 0: continue
            p = r + rws[0]; M[[r, p]] = M[[p, r]]
            for i in range(m):
                if i != r and M[i, col]: M[i] ^= M[r]
            piv.append(col); r += 1
            if r == m: break
        if M[r:, n].any(): return None
        x = np.zeros(n, np.uint8)
        for i, col in enumerate(piv): x[col] = M[i, n]
        return x
    def cyc_row(seq):
        row = np.zeros(NT, np.uint8)
        for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1]): row[ETYPES[edge_key(c1, c2, tuple(y - x for x, y in zip(p1, p2)))]] ^= 1
        return row
    def ring(d):
        a = [f for f in DIRS if dot(f, d) == 0]; a0 = a[0]; b0 = [f for f in a if dot(f, a0) == 0][0]
        return [a0, b0, neg(a0), neg(b0)]
    CYC = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
    for d in DIRS:
        rg = ring(d)
        CYC['square'].append(cyc_row([(frozenset((d, r)), Z) for r in rg]))
        for i in range(4):
            p, q = rg[i], rg[(i + 1) % 4]
            CYC['tube'].append(cyc_row([(frozenset((d, p)), Z), (frozenset((neg(d), p)), d), (frozenset((neg(d), q)), d), (frozenset((d, q)), Z)]))
    for s in itertools.product((1, -1), repeat=3):
        x, y, zz = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
        CYC['triangle'].append(cyc_row([(frozenset((x, y)), Z), (frozenset((y, zz)), Z), (frozenset((zz, x)), Z)]))
    for d, e in itertools.permutations(DIRS, 2):
        if dot(d, e) != 0: continue
        CYC['plaquette'].append(cyc_row([(frozenset((d, e)), Z), (frozenset((neg(d), e)), d), (frozenset((neg(d), neg(e))), vadd(d, e)), (frozenset((d, neg(e))), e)]))
    FLUX = dict(square=1, triangle=0, plaquette=1, tube=1)
    rows = []; rhs = []
    for k_, rs in CYC.items():
        for r in rs: rows.append(r); rhs.append(FLUX[k_])
    u = gf2_solve(rows, rhs)
    FLUX_OK = u is not None and all(int(r @ u % 2) == FLUX[k_] for k_, rs in CYC.items() for r in rs)
    OH = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3): M[i, perm[i]] = sg[i]
            OH.append(M)
    OH.sort(key=lambda M: (round(np.linalg.det(M)) != 1))
    PROPER = list(range(24))
    def rdir(M, d): return tuple(int(x) for x in M @ np.array(d))
    def rcorn(M, c): return frozenset(rdir(M, d) for d in c)
    allbits = np.array(list(itertools.product((0, 1), repeat=15)), np.uint8); lamb, taub = allbits[:, :3], allbits[:, 3:]
    LAM, UF = [], []; uniq = True
    for M in OH:
        okm = np.ones(len(allbits), bool)
        for (i1, i2, s) in ELIST:
            ue = u[ETYPES[(i1, i2, s)]]; ume = u[ETYPES[edge_key(rcorn(M, CORN[i1]), rcorn(M, CORN[i2]), rdir(M, s))]]
            okm &= ((taub[:, i1] + lamb @ np.array(s) % 2 + taub[:, i2]) % 2) == (ue ^ ume)
        good = allbits[okm]; uniq &= len(good) == 2
        lam, tau = good[0][:3].astype(int), good[0][3:].astype(int)
        U = np.zeros((12, 12))
        for c in CORN: U[CI[rcorn(M, c)], CI[c]] = (-1.0) ** tau[CI[c]]
        LAM.append(lam); UF.append(U)
    check("B0 own GF(2) gauge satisfies every flux constraint (all plaquette orientations); brute-force PSG over 2^15 (lam, tau) has a "
          "solution, unique up to the global sign, for each of the 48 O_h elements", FLUX_OK and uniq)
    def wrap(x): return (np.asarray(x) + np.pi) % (2 * np.pi) - np.pi
    def same_k(a, b, tol=1e-8): return np.allclose(wrap(np.asarray(a, float) - np.asarray(b, float)), 0, atol=tol)
    def add(bl, d, M):
        d = tuple(int(x) for x in d); bl.setdefault(d, np.zeros((12, 12), complex)); bl[d] += M
    Hon = np.zeros((12, 12)); blL = {}
    for (i1, i2, s) in ELIST:
        a = -(-1.0) ** int(u[ETYPES[(i1, i2, s)]])
        if tuple(s) == Z: Hon[i2, i1] += a; Hon[i1, i2] += a
        else:
            M1 = np.zeros((12, 12)); M1[i2, i1] = a / np.sqrt(2); add(blL, s, M1)
            M2 = np.zeros((12, 12)); M2[i1, i2] = a / np.sqrt(2); add(blL, neg(s), M2)
    Lam = np.zeros((12, 12), complex)
    for sg in itertools.product((1, -1), repeat=3):
        x, y, zz = (sg[0], 0, 0), (0, sg[1], 0), (0, 0, sg[2])
        cy = [frozenset((x, y)), frozenset((y, zz)), frozenset((zz, x))]
        if round(np.linalg.det(np.array([x, y, zz]))) < 0: cy = cy[::-1]
        for a_ in range(3):
            q, r = cy[a_], cy[(a_ + 1) % 3]; amp = 1j * (-1.0) ** int(u[ETYPES[edge_key(q, r, Z)]])
            Lam[CI[r], CI[q]] += amp; Lam[CI[q], CI[r]] += np.conj(amp)
    def eproj(M):
        w, V = np.linalg.eigh(M); ls = sorted(set(np.round(w, 6)))
        return [V[:, np.abs(w - l) < 1e-6] @ V[:, np.abs(w - l) < 1e-6].conj().T for l in ls]
    PH = eproj(Hon); PL = eproj(Lam)
    UH = PH[0] - PH[1] - 1j * PH[2]; UL = PL[0] + 1j * PL[1] + 1j * PL[2] + PL[3]
    def rot_blocks(bl, g):
        o = {}
        for d, h in bl.items(): add(o, OH[g] @ np.array(d), (-1.0) ** int(LAM[g] @ np.array(d)) * UF[g] @ h @ UF[g].T)
        return o
    def sym_blocks(bl, idx=PROPER, chi=None):
        o = {}
        for g in idx:
            c = 1.0 if chi is None else np.conj(chi[g])
            for d, h in rot_blocks(bl, g).items(): add(o, d, c * h / len(idx))
        return {d: h for d, h in o.items() if np.abs(h).max() > 1e-13}
    cxy = frozenset(((1, 0, 0), (0, 1, 0))); seed = {}; M0 = np.zeros((12, 12)); M0[CI[cxy], CI[cxy]] = 1.0; add(seed, (1, 1, 0), M0)
    blS = sym_blocks(seed); mx = max(np.abs(h).max() for h in blS.values()); blS = {d: h / mx for d, h in blS.items()}
    def bloch(bl, ks):
        ks = np.atleast_2d(np.asarray(ks, float)); o = np.zeros((len(ks), 12, 12), complex)
        for d, h in bl.items(): o += np.exp(-1j * ks @ np.array(d, float))[:, None, None] * h[None]
        return o
    def dbloch(bl, ks, j):
        ks = np.atleast_2d(np.asarray(ks, float)); o = np.zeros((len(ks), 12, 12), complex)
        for d, h in bl.items(): o += (-1j * d[j]) * np.exp(-1j * ks @ np.array(d, float))[:, None, None] * h[None]
        return o
    UU = UH @ UL
    def Wb(ks): return bloch(blS, ks) @ bloch(blL, ks) @ UU
    def W(k): return Wb(k)[0]
    def dW(k, j): return (dbloch(blS, k, j)[0] @ bloch(blL, k)[0] + bloch(blS, k)[0] @ dbloch(blL, k, j)[0]) @ UU
    def gk(g, k): return OH[g] @ np.asarray(k, float) + np.pi * (OH[g] @ LAM[g])
    def stab(k, idx=PROPER): return [g for g in idx if same_k(gk(g, k), k)]
    def find_el(M): return [g for g in range(48) if (OH[g] == np.array(M)).all()][0]
    A2 = {g: A2_CLASS[cls(OH[g])] for g in PROPER}; A1 = {g: 1 for g in PROPER}
    def levels(k, Wfun=W, tol=1e-7):
        e, V = np.linalg.eig(Wfun(k)); ph = np.angle(e); used = np.zeros(len(e), bool); o = []
        for i in np.argsort(ph):
            if used[i]: continue
            grp = np.where((~used) & (np.abs(wrap(ph - ph[i])) < tol))[0]; used[grp] = True
            Qm, _ = np.linalg.qr(V[:, grp]); o.append((ph[i], Qm))
        return o
    def level_at(k, E, Wfun=W):
        for e, Qm in levels(k, Wfun):
            if abs(wrap(e - E)) < 1e-6: return Qm
    def weyl_B(k, Qm):
        Wk = W(k); A = [-1j * Qm.conj().T @ Wk.conj().T @ dW(k, j) @ Qm for j in range(3)]
        return np.array([[np.trace(A[j] @ PAU[b]).real / 2 for b in range(3)] for j in range(3)])
    KST = np.array([1, -1, 1]) * np.pi / 2; QR = np.pi * np.ones(3); Q0 = np.zeros(3)
    CUBE = [np.array(s) * np.pi / 2 for s in itertools.product((1, -1), repeat=3)]
    NODES = {tuple(int(x) for x in np.round(np.mod((k - KST) / np.pi, 2)).astype(int) % 2): k for k in CUBE}
    DOUB = [n for n in NODES if n not in ((0, 0, 0), (1, 1, 1))]
    NAME = {n: ('k*' if n == (0, 0, 0) else '-k*' if n == (1, 1, 1) else f'k*+pi{n}') for n in NODES}
    def fermi(bl, Q):
        o = {}
        for d, h in bl.items(): add(o, d, 0.5 * h); add(o, neg(d), -0.5 * np.exp(-1j * np.dot(Q, d)) * h.T)
        return o
    def rand_blocks(rng_, r=1):
        return {d: rng_.normal(size=(12, 12)) + 1j * rng_.normal(size=(12, 12)) for d in itertools.product(range(-r, r + 1), repeat=3)}
    def sym_pair(bl, chi, Q, idx=PROPER): return sym_blocks(fermi(bl, Q), idx, chi)
    def Delta(bl, Q, ks):
        ks = np.atleast_2d(np.asarray(ks, float)); o = np.zeros((len(ks), 12, 12), complex)
        for d, h in bl.items(): o += np.exp(-1j * (ks + Q) @ np.array(d, float))[:, None, None] * h[None]
        return o
    def check_sym(bl, chi, Q, idx=PROPER, ntest=2, rng_=None):
        rng_ = rng_ or np.random.default_rng(0); okk = True
        for k in rng_.uniform(-np.pi, np.pi, (ntest, 3)):
            Dk = Delta(bl, Q, k)[0]; okk &= np.allclose(Dk, -Delta(bl, Q, -Q - k)[0].T, atol=1e-10)
            for g in idx: okk &= np.allclose(UF[g] @ Dk @ UF[g].T, chi[g] * Delta(bl, Q, gk(g, k))[0], atol=1e-10)
        return okk
    ASB = []
    for i in range(12):
        for j in range(i + 1, 12):
            X = np.zeros((12, 12)); X[i, j] = 1; X[j, i] = -1; ASB.append(X)
    def onsite_channel(chi, idx=PROPER, tol=1e-9):
        rws = [np.array([(UF[g] @ X @ UF[g].T - chi[g] * X)[np.triu_indices(12, 1)] for X in ASB]).T for g in idx]
        _, s, Vh = np.linalg.svd(np.vstack(rws)); s = np.concatenate([s, np.zeros(Vh.shape[0] - len(s))])
        return [sum(c * X for c, X in zip(v.conj(), ASB)) for v in Vh[s < tol]]
    def node_doublet(n, E=np.pi / 2): return level_at(NODES[n], E)
    def singlet(Qm, Dm):
        M = Qm.conj().T @ Dm @ Qm.conj(); return 0.5 * (M[0, 1] - M[1, 0])
    def bdg_U(ks, Dfun, tau, Q, mu=np.pi / 2):
        ks = np.atleast_2d(np.asarray(ks, float)); n = len(ks)
        D = Dfun(ks); Da = D - np.transpose(Dfun(-Q - ks), (0, 2, 1))
        h = np.zeros((n, 24, 24), complex); h[:, :12, 12:] = Da; h[:, 12:, :12] = np.conj(np.transpose(Da, (0, 2, 1)))
        w, V = np.linalg.eigh(h); P = (V * np.exp(-1j * tau * w)[:, None, :]) @ np.conj(np.transpose(V, (0, 2, 1)))
        N = np.zeros((n, 24, 24), complex); N[:, :12, :12] = np.exp(-1j * mu) * Wb(ks); N[:, 12:, 12:] = np.exp(1j * mu) * np.conj(Wb(-Q - ks))
        return P @ N
    def bdg_eps(ks, Dfun, tau, Q): return np.angle(np.linalg.eigvals(bdg_U(ks, Dfun, tau, Q)))
    def gap0(ks, Dfun, tau, Q): return np.min(np.abs(bdg_eps(ks, Dfun, tau, Q)), axis=-1)
    def gappi(ks, Dfun, tau, Q): return np.min(np.abs(wrap(bdg_eps(ks, Dfun, tau, Q) - np.pi)), axis=-1)
    def grid_min(Dfun, tau, Q, N=20, exclude=(), r_ex=0.0, chunk=1500):
        g = 2 * np.pi * np.arange(N) / N - np.pi + 1e-3; K = np.array(list(itertools.product(g, g, g)))
        if exclude:
            keep = np.ones(len(K), bool)
            for e in exclude: keep &= np.linalg.norm(wrap(K - e), axis=1) >= r_ex
            K = K[keep]
        b0 = bp = np.inf; k0 = kp = None
        for i in range(0, len(K), chunk):
            ev = bdg_eps(K[i:i + chunk], Dfun, tau, Q); a0 = np.min(np.abs(ev), axis=1); ap = np.min(np.abs(wrap(ev - np.pi)), axis=1)
            j = np.argmin(a0); j2 = np.argmin(ap)
            if a0[j] < b0: b0, k0 = a0[j], K[i + j]
            if ap[j2] < bp: bp, kp = ap[j2], K[i + j2]
        return (b0, k0), (bp, kp)
    print(f"   model built in {time.time() - t0:.1f}s", flush=True)
    rng = np.random.default_rng(20261018)
    out = {}

    # ---- D1-D3 lifts and det characters ----
    ax = [find_el(np.diag(d)) for d in ([1, -1, -1], [-1, 1, -1], [-1, -1, 1])]
    ords = {}
    for g in PROPER:
        c = cls(OH[g]); o = {'E': 1, 'C2': 2, "C2'": 2, 'C3': 3, 'C4': 4}[c]; P = np.linalg.matrix_power(UF[g], o)
        ords.setdefault(c, set()).add(int(round(P[0, 0])) if np.allclose(P, P[0, 0] * np.eye(12)) else None)
    check("B1 the three axis-C2 lifts anticommute; U_g^{order(g)} = +-1 per element (the real signed-permutation lift is not the SU(2) lift: "
          "it has U^2 = -1 on axis C2 but +1 on face-diagonal C2')", all(np.allclose(UF[a] @ UF[b], -UF[b] @ UF[a]) for a in ax for b in ax if a != b)
          and ords['C2'] == {-1} and ords["C2'"] == {1}, str({k: sorted(v) for k, v in ords.items()}))
    def det_char(Qm, idx): return {g: np.linalg.det(Qm.conj().T @ UF[g] @ Qm) for g in idx}
    def rand_sym_herm(r=1):
        bl = sym_blocks({d: rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12)) for d in itertools.product(range(-r, r + 1), repeat=3)})
        o = {}
        for d, h in bl.items(): add(o, d, 0.5 * h); add(o, neg(d), 0.5 * h.conj().T)
        return o
    H1, H2, H3 = rand_sym_herm(), rand_sym_herm(), rand_sym_herm()
    UHv = PH[0] + 1j * PH[1] - PH[2]; ULv = PL[0] - PL[1] + 1j * PL[2] - 1j * PL[3]
    STEPS = dict(eight_node=W,
                 rand_step=lambda k: expm(-1j * bloch(H1, k)[0]) @ W(k) @ expm(-1j * 0.7 * bloch(H2, k)[0]),
                 rand_ham=lambda k: expm(-1j * 0.3 * bloch(H3, k)[0]),
                 rand_prod=lambda k: expm(-1j * bloch(H1, k)[0]) @ expm(-1j * bloch(H2, k)[0]),
                 phase_variant=lambda k: bloch(blS, k)[0] @ bloch(blL, k)[0] @ UHv @ ULv)
    ok = True; cnts = []
    for nmS, Wf in STEPS.items():
        ok &= all(np.allclose(UF[g] @ Wf(k) @ UF[g].T, Wf(gk(g, k)), atol=1e-9) for g in PROPER[::5] for k in rng.uniform(-np.pi, np.pi, (2, 3)))
        ns = nd = 0
        for n, K in NODES.items():
            st = stab(K)
            for E, Qm in levels(K, Wf):
                if Qm.shape[1] != 2: continue
                dc = det_char(Qm, st); ok &= all(abs(dc[g] - A2[g]) < 1e-7 for g in st)
                if n in ((0, 0, 0), (1, 1, 1)): ns += 1
                else: nd += 1
        ok &= nd > 0; cnts.append(f"{nmS}: {ns}+{nd}")
    check("B2 det(U_g|V) = A2 at every 2-fold level at +-k* and = A2|D4 at every doubler level, for the eight-node step and four other "
          "PSG-symmetric steps/Hamiltonians", ok, "; ".join(cnts))
    st = stab(NODES[(1, 0, 0)]); ncl = {c: sum(cls(OH[g]) == c for g in st) for c in ('C4', 'C2', "C2'")}
    check("B3 the doubler little group (affine) is D4: 2 C4, 3 axis C2, 2 diagonal C2'; A2|D4 = (C4 -1, C2 +1, C2' -1) = B1, which differs from A1|D4",
          len(st) == 8 and ncl == {'C4': 2, 'C2': 3, "C2'": 2})
    tr = [(E, {g: np.trace(Qm.conj().T @ UF[g] @ Qm) for g in PROPER}) for E, Qm in levels(KST) if Qm.shape[1] == 2]
    check("B4 at k* the two 2-fold levels are different 2-dim irreps whose characters differ exactly by A2 (E1/2 vs E5/2 = E1/2 x A2), hence "
          "have equal det (A2^2 = 1)", len(tr) == 2 and all(abs(tr[1][1][g] - A2[g] * tr[0][1][g]) < 1e-7 for g in PROPER)
          and any(abs(tr[1][1][g] - tr[0][1][g]) > 1e-3 for g in PROPER))

    # ---- S1-S3 selection rule and decoupling ----
    DQ = {n: node_doublet(n) for n in NODES}
    VA2, VA1 = onsite_channel(A2), onsite_channel(A1)
    out['dims'] = (len(VA2), len(VA1))
    def node_m(bl, Q):
        o = {}
        for n, K in NODES.items():
            Dk = Delta(bl, Q, K)[0]; Da = Dk - Delta(bl, Q, -Q - K)[0].T
            if np.allclose(Q, 0): o[n] = np.abs(DQ[n].conj().T @ Da @ DQ[tuple((1 - x) % 2 for x in n)].conj()).max()
            else: o[n] = abs(singlet(DQ[n], Da))
        return o
    summ = {}
    for Qn, Q in (('R', QR), ('0', Q0)):
        for cn, chi in (('A2', A2), ('A1', A1)):
            vals = []; symok = True
            for _ in range(2):
                bl = sym_pair(rand_blocks(rng, 1), chi, Q); symok &= check_sym(bl, chi, Q, rng_=rng); vals.append(node_m(bl, Q))
            for X in (VA2 if cn == 'A2' else VA1): vals.append(node_m({(0, 0, 0): X + 0j}, Q))
            summ[(Qn, cn)] = (symok, {n: min(v[n] for v in vals[:2]) for n in NODES}, {n: max(v[n] for v in vals) for n in NODES})
    check("B5 Q = R: chi = A2 gives a nonzero intra-node singlet at all eight nodes (range-1 random), chi = A1 exactly zero at all eight "
          "(range-1 random and the whole on-site basis): all-or-nothing", summ[('R', 'A2')][0] and summ[('R', 'A1')][0]
          and min(summ[('R', 'A2')][1].values()) > 1e-3 and max(summ[('R', 'A1')][2].values()) < 1e-10,
          f"A1 max {max(summ[('R', 'A1')][2].values()):.1e}")
    rule_ok = True
    for n, K in NODES.items():
        stK = stab(K); dc = det_char(DQ[n], stK)
        for cn, chi in (('A2', A2), ('A1', A1)):
            rule_ok &= all(abs(chi[g] - dc[g]) < 1e-7 for g in stK) == (summ[('R', cn)][1][n] > 1e-3)
    check("B6 node by node: singlet observed nonzero <=> chi|G_K = det_K (all eight nodes, both characters)", rule_ok)
    check("B7 Q = 0: symmetric pairings exist for both characters; K <-> -K blocks are generic for A1 and vanish for A2",
          summ[('0', 'A1')][0] and summ[('0', 'A2')][0] and min(summ[('0', 'A1')][1].values()) > 1e-3 and max(summ[('0', 'A2')][2].values()) < 1e-10)
    cand = [np.pi / 2 * np.array(p) for p in itertools.product((-1, 0, 1, 2), repeat=3)]
    inv = sorted({tuple(int(x) for x in np.round(np.mod(Q, 2 * np.pi) / np.pi) % 2) for Q in cand if all(same_k(OH[g] @ Q, Q) for g in PROPER)})
    check("B8 among Q in (pi/2)Z^3 only Q = 0 and Q = R are fixed mod 2pi by the 24 linear parts (the affine shifts cancel in the pair momentum)",
          inv == [(0, 0, 0), (1, 1, 1)], str(inv))
    cross = {}
    for cn, chi in (('A2', A2), ('A1', A1)):
        worst = {}
        bls = [sym_pair(rand_blocks(rng, 1), chi, QR) for _ in range(2)] + [{(0, 0, 0): X + 0j} for X in (VA2 if cn == 'A2' else VA1)]
        for n in ((0, 0, 0), (1, 1, 1)):
            K = NODES[n]
            for bl in bls:
                Da = Delta(bl, QR, K)[0] - Delta(bl, QR, -QR - K)[0].T
                for E, Qm in levels(K):
                    if abs(wrap(E - np.pi / 2)) < 1e-6: continue
                    kk = f"dim{Qm.shape[1]}"; worst[kk] = max(worst.get(kk, 0), np.abs(DQ[n].conj().T @ Da @ Qm.conj()).max())
        cross[cn] = worst
    check("B9 decoupling at +-k*: an A2 pairing (on-site or range-1) couples the node doublet to no other level; an A1 pairing couples it to "
          "the other 2-dim irrep only, never to G3/2", max(cross['A2'].values()) < 1e-10 and cross['A1']['dim2'] > 1e-3 and cross['A1']['dim4'] < 1e-10,
          f"A2 max {max(cross['A2'].values()):.1e}")
    bl = sym_pair(rand_blocks(rng, 1), A2, QR); Df = lambda ks, bl=bl: Delta(bl, QR, ks); inv_ok = True
    for n in ((0, 0, 0), (1, 1, 1)):
        Ub = bdg_U(NODES[n], Df, 1.3, QR)[0]; P = np.zeros((24, 4), complex); P[:12, :2] = DQ[n]; P[12:, 2:] = DQ[n].conj(); Pr = P @ P.conj().T
        inv_ok &= np.allclose(Pr @ Ub @ Pr, Ub @ Pr, atol=1e-10)
    check("B10 the particle+hole node 4-space at +-k* is invariant under the full Floquet-BdG step (tau = 1.3, range-1 A2 pairing): exact "
          "decoupling at all orders, so +-k* is gapless iff its single complex singlet m_K vanishes", inv_ok)

    # ---- Berry-flux chiralities, dipole, BdG charges ----
    def upper_vec(Uk, E0):
        e, V = np.linalg.eig(Uk); d = wrap(np.angle(e) - E0); cnd = np.where(np.abs(d) < 0.3)[0]; j = cnd[np.argmax(d[cnd])]
        return V[:, j] / np.linalg.norm(V[:, j])
    def berry_flux(Ufun, K, E0, r=2e-3, nt=16, nph=32):
        th = np.linspace(1e-4, np.pi - 1e-4, nt + 1); ph = np.linspace(0, 2 * np.pi, nph + 1)[:-1]
        vec = np.empty((nt + 1, nph, Ufun(K).shape[0]), complex)
        for i, t in enumerate(th):
            for j, p in enumerate(ph): vec[i, j] = upper_vec(Ufun(K + r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])), E0)
        Fx = 0.0
        for i in range(nt):
            for j in range(nph):
                a, b, c, d = vec[i, j], vec[i + 1, j], vec[i + 1, (j + 1) % nph], vec[i, (j + 1) % nph]
                Fx += np.angle(np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, d) * np.vdot(d, a))
        return Fx / (2 * np.pi)
    chi = {}; agree = True; fl = []
    for n, K in NODES.items():
        f = berry_flux(W, K, np.pi / 2); chi[n] = int(round(f)); fl.append(abs(f - chi[n]))
        agree &= chi[n] == int(np.sign(np.linalg.det(weyl_B(K, DQ[n]))))
    check("B11 (numerical, rounded to integers) Berry-flux chiralities: |flux| = 1 at all eight, chi(k* + pi n) = (-1)^|n| chi(k*), net zero; "
          "they agree with the degenerate-PT sign det B", all(abs(c) == 1 for c in chi.values()) and sum(chi.values()) == 0 and agree
          and all(chi[n] == (-1) ** sum(n) * chi[(0, 0, 0)] for n in NODES), f"max |flux - integer| = {max(fl):.1e}")
    out['chi_rel'] = {n: chi[n] * chi[(0, 0, 0)] for n in NODES}
    orbs = {'k*': [(0, 0, 0)], '-k*': [(1, 1, 1)], 'A': [n for n in DOUB if sum(n) == 1], 'B': [n for n in DOUB if sum(n) == 2]}
    rws = {}
    for r in range(5):
        for combo in itertools.combinations(orbs, r):
            S = [n for o in combo for n in orbs[o]]
            net = sum(chi[n] for n in S); b = sum((chi[n] * NODES[n] for n in S), np.zeros(3))
            rws['+'.join(combo) or 'empty'] = (net, np.round(np.mod(b, 2 * np.pi) / np.pi, 6) % 2, tuple(int(sum(chi[n] for n in S if n[i] == 1)) % 2 for i in range(3)))
    free = sorted(l for l, (net, bm, z2) in rws.items() if net == 0 and np.allclose(bm, 0) and z2 == (0, 0, 0))
    check("B12 dipole table: A+B and {+-k*} each have net chirality 0 and b = pi(1,1,1) mod 2pi; all eight: b = 0; only 'empty' and 'all "
          "eight' anomaly-free", rws['A+B'][0] == 0 and np.allclose(rws['A+B'][1], 1) and rws['k*+-k*'][0] == 0 and np.allclose(rws['k*+-k*'][1], 1)
          and free == sorted(['empty', 'k*+-k*+A+B']), f"anomaly-free: {free}")
    out['free'] = len(free)
    check("B13 for net-zero subsets the U(1)^2-Z2^3 counts equal b/pi mod 2 (one invariant, not independent anomalies)",
          all(np.allclose(bm, z2) for net, bm, z2 in rws.values() if net == 0))
    mu = np.pi / 2; chg = {}
    for Qn, Q in (('R', QR), ('0', Q0)):
        for n, K in NODES.items():
            chg[(Qn, n)] = (int(round(berry_flux(lambda k: np.exp(-1j * mu) * W(k), K, 0.0))),
                            int(round(berry_flux(lambda k, Q=Q: np.exp(1j * mu) * np.conj(W(-Q - k)), K, 0.0))))
    check("B14 BdG charges by Berry flux (particle + hole sector at each node): Q = R gives 0 (intra-node, gappable); Q = 0 gives +-2 (not "
          "gappable by small pairing)", all(sum(chg[('R', n)]) == 0 for n in NODES) and all(abs(sum(chg[('0', n)])) == 2 for n in NODES))

    # ---- L1 slice obstruction, L2 lift independence, I1 O_h ----
    c2x = find_el(np.diag([1, -1, -1]))
    th_z = round(float(wrap(gk(c2x, np.zeros(3))[2])) / np.pi) % 2
    def slice_ok(S):
        planes = {}
        for n in S:
            zq = round(float(wrap(NODES[n][2])) / (np.pi / 2)); planes[zq] = planes.get(zq, 0) + chi[n]
        J = planes.get(1, 0); Jm = planes.get(-1, 0)
        if J + Jm != 0: return False
        for a in range(-5, 6):
            nu0, nu1 = a, a - J
            if th_z == 0 and nu0 == 0 and nu1 == 0: return True
            if th_z == 1 and nu1 == -nu0: return True
        return False
    sres = {}
    for r in range(5):
        for combo in itertools.combinations(orbs, r): sres['+'.join(combo) or 'empty'] = slice_ok([n for o in combo for n in orbs[o]])
    check("B15 slice bookkeeping with C2x only (odd affine shift theta_z = pi; orientation-reversing on k_z-slices, so nu(k_z) = -nu(pi - k_z)): "
          "'{+-k*} only' and 'doublers only' admit no integer slice invariant; 'all eight' and 'empty' do; no other rotation-invariant subset does",
          th_z == 1 and sorted(l for l, v in sres.items() if v) == sorted(['empty', 'k*+-k*+A+B']))
    cph = {g: (1j if A2[g] == -1 else 1.0) for g in PROPER}; Up = {g: cph[g] * UF[g] for g in PROPER}
    okc = all(np.allclose(Up[g] @ W(k) @ Up[g].conj().T, W(gk(g, k))) for g in PROPER for k in rng.uniform(-np.pi, np.pi, (2, 3)))
    Dd = node_doublet((1, 0, 0)); stD = stab(NODES[(1, 0, 0)])
    det_new = all(abs(np.linalg.det(DQ[(0, 0, 0)].conj().T @ Up[g] @ DQ[(0, 0, 0)]) - 1) < 1e-9 for g in PROPER) and \
        all(abs(np.linalg.det(Dd.conj().T @ Up[g] @ Dd) - 1) < 1e-9 for g in stD)
    ch_new = all(np.allclose(Up[g] @ X @ Up[g].T, X) for g in PROPER for X in VA2)
    check("B16 lift-label caveat: the rephased lifts U'_g = c(g) U_g with c(g)^2 = A2(g) are equally symmetries; with them det = A1 at +-k* "
          "and at the doublers, and the old A2 channel is the new A1 channel: the rule 'allowed iff chi|G_K = det_K' is lift-independent, the "
          "label A2 is a convention", okc and det_new and ch_new)
    def proper_part(g): return find_el(-OH[g]) if g >= 24 else g
    okall = True; dims_oh = {}
    for base in ('A1', 'A2'):
        for par in ('g', 'u'):
            chiO = {g: (A2[proper_part(g)] if base == 'A2' else 1) * (1 if (g < 24 or par == 'g') else -1) for g in range(48)}
            V = onsite_channel(chiO, idx=list(range(48))); dims_oh[base + par] = len(V)
            if not V: continue
            A = sum((rng.normal() + 1j * rng.normal()) * X for X in V); m = {n: abs(singlet(DQ[n], 2 * A)) for n in NODES}
            eq = all(abs(m[n] - m[tuple((1 - x) % 2 for x in n)]) < 1e-9 for n in NODES)
            okall &= (min(m.values()) > 1e-4 and eq) if base == 'A2' else max(m.values()) < 1e-11
    check("B17 O_h channels: A2g, A2u allow the singlet at all eight with |m_K| = |m_-K|; A1g, A1u forbid it at all eight (or are empty)", okall,
          str(dims_oh))
    out['dims_oh'] = dims_oh

    # ---- X1 subgroup channels ----
    MUL = {(a, b): find_el(OH[a] @ OH[b]) for a in PROPER for b in PROPER}; E0 = find_el(np.eye(3, dtype=int))
    def closure(gens):
        S = {E0} | set(gens); ch = True
        while ch:
            ch = False
            for a in list(S):
                for b in list(S):
                    if MUL[(a, b)] not in S: S.add(MUL[(a, b)]); ch = True
        return frozenset(S)
    subs = sorted({closure([a, b]) for a in PROPER for b in PROPER}, key=len)
    def characters(H):
        gens = []; cur = frozenset([E0])
        for h in sorted(H):
            if h not in cur: gens.append(h); cur = closure(gens)
        roots = [cmath.exp(2j * np.pi * m / 12) for m in range(12)]; o = []
        for vals in itertools.product(roots, repeat=len(gens)):
            ch_ = {E0: 1.0}; frontier = [E0]; okk = True
            while frontier and okk:
                new = []
                for x in frontier:
                    for gi, gv in zip(gens, vals):
                        y = MUL[(x, gi)]; v = ch_[x] * gv
                        if y in ch_:
                            if abs(ch_[y] - v) > 1e-9: okk = False; break
                        else: ch_[y] = v; new.append(y)
                    if not okk: break
                frontier = new
            if okk and all(abs(ch_[MUL[(a, b)]] - ch_[a] * ch_[b]) < 1e-9 for a in H for b in H):
                if not any(all(abs(c[g] - ch_[g]) < 1e-9 for g in H) for c in o): o.append(ch_)
        return o
    selective = []
    for H in subs:
        for ch_ in characters(H):
            V = onsite_channel(ch_, idx=sorted(H))
            if not V: continue
            al = {n: max(abs(singlet(DQ[n], 2 * X)) for X in V) > 1e-9 for n in NODES}
            if not (al[(0, 0, 0)] or al[(1, 1, 1)]) and sum(al[n] for n in DOUB) > 0:
                selective.append((len(H), sum(al[n] for n in DOUB), sorted(H), ch_))
    fullT = [s for s in selective if s[0] == 12 and s[1] == 6]
    check("B18 subgroup scope (adversarial): over all 30 subgroups H of O and their 1-dim characters, selective on-site Q = R channels (singlet "
          "forbidden at +-k*, allowed at some doubler) exist only for |H| <= 12; none for H = O; T with chi(C3) = omega or omega-bar forbids it at "
          "+-k* and allows it at all six doublers", len(subs) == 30 and all(s[0] <= 12 for s in selective) and len(fullT) == 2,
          f"{len(selective)} selective (H, chi); orders {sorted(set(s[0] for s in selective))}")

    sel8 = [s for s in selective if s[0] == 8]
    def restricts_from(s_):
        return any(set(s_[2]) <= set(b[2]) and all(abs(b[3][g] - s_[3][g]) < 1e-9 for g in s_[2]) for b in fullT + sel8)
    check("B19 subgroup coverage (exact enumeration): every selective (H, chi) is the restriction of a selective T-omega/omega-bar or "
          "D4 channel (three D4s, each chi = A1, conjugate under O), so its channel space contains one of those",
          len(sel8) == 3 and all(all(abs(v - 1) < 1e-9 for v in s[3].values()) for s in sel8) and all(restricts_from(s_) for s_ in selective))

    # ---- Section D: BdG spot checks (optional) ----
    if BDG:
        print("\n=== Section D (--bdg): Floquet-BdG spot checks, numerical illustrations (independent-core path) ===", flush=True)
        td = time.time()
        def const(Am): return lambda ks: np.broadcast_to(Am, (len(np.atleast_2d(ks)), 12, 12)).copy()
        rngd = np.random.default_rng(4242)
        A2m = sum((rngd.normal() + 1j * rngd.normal()) * X for X in VA2); A2m /= np.linalg.norm(A2m)
        A1m = sum((rngd.normal() + 1j * rngd.normal()) * X for X in VA1); A1m /= np.linalg.norm(A1m)
        tau = 0.5
        # threshold 1e-3 (numerical zeros here are ~1e-12); a first version used 1e-2 and failed on this draw (node gap 0.0073):
        # the gap size depends on the random channel vector, so three draws are tested and the minima reported.
        okD1 = True; infoD1 = []
        for A_ in [A2m] + [sum((rngd.normal() + 1j * rngd.normal()) * X for X in VA2) for _ in range(2)]:
            A_ = A_ / np.linalg.norm(A_)
            gB1 = [gap0(K, const(A_), tau, QR)[0] for K in NODES.values()]
            (b0, _), (bp, _) = grid_min(const(A_), tau, QR, N=20)
            okD1 &= min(gB1) > 1e-3 and b0 > 1e-3 and bp > 1e-3; infoD1.append(f"{min(gB1):.4f}/{b0:.4f}/{bp:.4f}")
        check("D1 (numerical) Q = R, chi = A2 on-site (tau = 0.5, three random channel vectors): all eight nodes gapped; grid N = 20 minima of "
              "|eps| and |eps - pi| stay open", okD1, "node-gap min / grid 0-gap / grid pi-gap per draw: " + ", ".join(infoD1))
        zA1 = [int(np.sum(np.abs(bdg_eps(NODES[n], const(A1m), tt, QR)[0]) < 1e-10)) for n in ((0, 0, 0), (1, 1, 1)) for tt in (0.3, 1.1)]
        check("D2 Q = R, chi = A1 on-site: +-k* keep an exact 4-fold BdG zero (tau = 0.3, 1.1)", all(v == 4 for v in zA1))
        from scipy.optimize import minimize
        def ball_min(K, Dfun, tt, Q, r=0.3, ng=13):
            gg = np.linspace(-r, r, ng); P = K + np.array(list(itertools.product(gg, gg, gg))); v = gap0(P, Dfun, tt, Q); j = np.argmin(v)
            return minimize(lambda k: gap0(k, Dfun, tt, Q)[0], P[j], method='Nelder-Mead', options=dict(xatol=1e-11, fatol=1e-15, maxiter=4000)).fun
        m0 = [ball_min(K, const(A1m), 0.1, Q0) for K in NODES.values()]
        check("D3 (numerical) Q = 0 symmetric on-site pairing (A1, tau = 0.1): a BdG zero survives within 0.3 of every node", max(m0) < 1e-8,
              f"max local min {max(m0):.1e}")
        def wfun(ks):
            s = np.sin(np.atleast_2d(ks)) * SG; return 3.0 - (s[:, 0] * s[:, 1] + s[:, 1] * s[:, 2] + s[:, 2] * s[:, 0])
        kt = rngd.uniform(-np.pi, np.pi, (5, 3))
        w_ok = all(abs(wfun(gk(g, k))[0] - wfun(k)[0]) < 1e-12 for g in PROPER for k in kt) and all(abs(wfun(-QR - k)[0] - wfun(k)[0]) < 1e-12 for k in kt)
        w_ok &= abs(wfun(KST)[0]) < 1e-14 and abs(wfun(-KST)[0]) < 1e-14 and all(abs(wfun(NODES[n])[0] - 4) < 1e-12 for n in DOUB)
        DW = lambda ks: wfun(ks)[:, None, None] * A2m[None]
        zW = [int(np.sum(np.abs(bdg_eps(NODES[n], DW, tau, QR)[0]) < 1e-10)) for n in ((0, 0, 0), (1, 1, 1))]
        gW = [gap0(NODES[n], DW, tau, QR)[0] for n in DOUB]
        cone = []
        for n in ((0, 0, 0), (1, 1, 1)):
            d = rngd.normal(size=(20, 3)); d /= np.linalg.norm(d, axis=1)[:, None]
            cone.append(np.sort(np.abs(bdg_eps(NODES[n] + 1e-4 * d, DW, tau, QR)), axis=1)[:, :4] / 1e-4)
        cone = np.array(cone)
        (b0, _), (bp, _) = grid_min(DW, tau, QR, N=20, exclude=(KST, -KST), r_ex=0.35)
        check("D4 (numerical) Wilson-type pairing w(k) A2 (w invariant under the 24 affine maps and k -> -Q-k; w(+-k*) = 0, w = 4 at the "
              "doublers): +-k* exact 4-fold zeros with isotropic BdG cone sqrt2/3, doublers gapped, nothing else outside 0.35-balls (grid N = 20)",
              w_ok and zW == [4, 4] and min(gW) > 1e-2 and np.allclose(cone, np.sqrt(2) / 3, atol=2e-4) and b0 > 1e-3 and bp > 1e-3,
              f"cone [{cone.min():.6f}, {cone.max():.6f}]; doubler gaps min {min(gW):.4f}; outside-ball 0/pi {b0:.4f}/{bp:.4f}")
        Fm = np.array([[singlet(DQ[n], 2 * X) for X in VA2] for n in ((0, 0, 0), (1, 1, 1))])
        _, s, Vh = np.linalg.svd(Fm); nullv = Vh[np.sum(s > 1e-9):].conj()
        cvec = nullv.T @ (rngd.normal(size=len(nullv)) + 1j * rngd.normal(size=len(nullv)))
        At = sum(ci * X for ci, X in zip(cvec, VA2)); At /= np.linalg.norm(At)
        gt = max(gap0(NODES[n], const(At), tt, QR)[0] for n in ((0, 0, 0), (1, 1, 1)) for tt in (0.05, 0.2, 0.6, 1.2))
        dbl = [gap0(NODES[n], const(At), tau, QR)[0] for n in DOUB]
        (b0, _), (bp, _) = grid_min(const(At), tau, QR, N=20, exclude=(KST, -KST), r_ex=0.35)
        check("D5 (numerical) on-site A2 pairing tuned to m_{+-k*} = 0 (two complex conditions): +-k* exact zeros for all tau, doublers gapped, "
              "nothing else outside 0.35-balls (grid N = 20)", gt < 1e-10 and min(dbl) > 1e-3 and b0 > 1e-3 and bp > 1e-3,
              f"doubler gap {min(dbl):.4f}; outside-ball 0/pi {b0:.4f}/{bp:.4f}")
        Ar = sum((rngd.normal() + 1j * rngd.normal()) * X for X in VA2); Ar /= np.linalg.norm(Ar)
        etas = (1e-3, 1e-2, 1e-1); gp = [gap0(KST, const((At + e * Ar) / np.linalg.norm(At + e * Ar)), tau, QR)[0] for e in etas]
        sl = np.polyfit(np.log(etas), np.log(gp), 1)[0]
        check("D6 (numerical) a generic A2 admixture eta re-gaps +-k* linearly: tuning, not protection", 0.9 < sl < 1.1, f"slope {sl:.3f}")
        Hs, chiT = fullT[0][2], fullT[0][3]; VT = onsite_channel(chiT, idx=Hs)
        rngt = np.random.default_rng(77)
        AT = sum((rngt.normal() + 1j * rngt.normal()) * X for X in VT); AT /= np.linalg.norm(AT)
        mK = {n: abs(singlet(DQ[n], 2 * AT)) for n in NODES}; gK = {n: gap0(NODES[n], const(AT), tau, QR)[0] for n in NODES}
        taus = (0.05, 0.1, 0.2, 0.4)
        sh = {n: [np.sort(np.abs(bdg_eps(NODES[n], const(AT), tt, QR)[0]))[0] for tt in taus] for n in ((0, 0, 0), (1, 1, 1))}
        slT = [np.polyfit(np.log(taus), np.log(v), 1)[0] for v in sh.values()]
        g4 = all(np.allclose(np.sort(np.abs(bdg_eps(NODES[n], const(AT), 0.2, QR)[0]))[:4], sh[n][2], atol=1e-9) for n in sh)
        check("D7 (numerical) T-omega on-site pairing: first-order singlet exactly zero at +-k*, nonzero at the six doublers, doublers gapped; "
              "but the 4-fold BdG level at +-k* is shifted off zero by delta ~ tau^2 (still 4-fold): the residual T does not protect a point node",
              max(mK[(0, 0, 0)], mK[(1, 1, 1)]) < 1e-12 and min(mK[n] for n in DOUB) > 1e-3 and min(gK[n] for n in DOUB) > 1e-2
              and all(1.9 < v < 2.1 for v in slT) and g4, f"log-log slopes {[round(float(v), 3) for v in slT]}")
        H8, ch8 = sel8[0][2], sel8[0][3]; V8 = onsite_channel(ch8, idx=H8)
        A8 = sum((rngt.normal() + 1j * rngt.normal()) * X for X in V8); A8 /= np.linalg.norm(A8)
        m8 = {n: abs(singlet(DQ[n], 2 * A8)) for n in NODES}
        sh8 = {n: [np.sort(np.abs(bdg_eps(NODES[n], const(A8), tt, QR)[0]))[0] for tt in taus] for n in ((0, 0, 0), (1, 1, 1))}
        sl8 = [np.polyfit(np.log(taus), np.log(v), 1)[0] for v in sh8.values()]
        check("D8 (numerical) D4-A1 on-site pairing (with B19 and D7 this covers every selective subgroup channel): singlet exactly zero at "
              "+-k*, nonzero at the four doublers off the D4 axis; the +-k* BdG level is shifted off zero by delta ~ tau^2: not protected",
              max(m8[(0, 0, 0)], m8[(1, 1, 1)]) < 1e-12 and sum(m8[n] > 1e-3 for n in DOUB) == 4 and all(1.9 < v < 2.1 for v in sl8),
              f"log-log slopes {[round(float(v), 3) for v in sl8]}")
        print(f"   Section D done in {time.time() - td:.0f}s", flush=True)
    print(f"   Section B done in {time.time() - t0:.0f}s", flush=True)
    return out


# =====================================================================================================================
# Section E: exact integer bookkeeping and 2O character products
# =====================================================================================================================
def section_E():
    print("\n=== Section E: exact bookkeeping (integers, units of pi/2) and 2O character products ===", flush=True)
    ROT24 = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3): M[i, perm[i]] = sg[i]
            if round(np.linalg.det(M)) == 1: ROT24.append(M)
    # pair momenta / Weyl dipoles in (pi/2)Z^3 mod 2pi fixed by all 24 linear parts
    fixed = [q for q in itertools.product(range(4), repeat=3) if all(tuple((M @ np.array(q)) % 4) == q for M in ROT24)]
    check("E1 (exact) the vectors in (pi/2)Z^3 mod 2pi fixed by all 24 rotations are exactly 0 and R = pi(1,1,1); every cube point K = (pi/2)(+-1)^3 "
          "has 2K = R mod 2pi, so a Q = R pair term pairs every node with itself", fixed == [(0, 0, 0), (2, 2, 2)]
          and all(tuple((2 * np.array(m)) % 4) == (2, 2, 2) for m in itertools.product((1, 3), repeat=3)), str(fixed))
    # general real Q: C4z and C4x force Q in {0, R} (analytic statement; spot-check on a fine rational grid)
    grid = [tuple(x) for x in itertools.product(range(8), repeat=3)]
    fixed8 = [q for q in grid if all(tuple((M @ np.array(q)) % 8) == q for M in ROT24)]
    check("E2 (exact) on the finer grid (pi/4)Z^3 the rotation-fixed vectors are again only 0 and R (C4z: Q_x = Q_y in {0, pi}; C4x: Q_y = Q_z)",
          fixed8 == [(0, 0, 0), (4, 4, 4)])
    # dipole table from the chirality pattern chi(k* + pi n) = s (-1)^|n|, k* = (pi/2)(1,-1,1); both signs s
    kst = np.array([1, -1, 1])
    ok = True
    for s in (1, -1):
        nodes = {n: (kst + 2 * np.array(n)) % 4 for n in itertools.product((0, 1), repeat=3)}
        ch = {n: s * (-1) ** sum(n) for n in nodes}
        orbs = {'k*': [(0, 0, 0)], '-k*': [(1, 1, 1)], 'A': [n for n in nodes if sum(n) == 1], 'B': [n for n in nodes if sum(n) == 2]}
        free = []; tab = {}
        for r in range(5):
            for combo in itertools.combinations(orbs, r):
                S = [n for o in combo for n in orbs[o]]; net = sum(ch[n] for n in S)
                b = tuple(int(x) for x in sum((ch[n] * nodes[n] for n in S), np.zeros(3, int)) % 4)
                tab['+'.join(combo) or 'empty'] = (net, b)
                if net == 0 and b == (0, 0, 0): free.append('+'.join(combo) or 'empty')
                if net == 0: ok &= all(bi % 2 == 0 for bi in b) and tuple(bi // 2 for bi in b) == tuple(sum(ch[n] for n in S if n[i]) % 2 for i in range(3))
        ok &= tab['A+B'] == (0, (2, 2, 2)) and tab['k*+-k*'] == (0, (2, 2, 2)) and tab['k*+-k*+A+B'] == (0, (0, 0, 0))
        ok &= sorted(free) == sorted(['empty', 'k*+-k*+A+B'])
    check("E3 (exact, given the integer chirality pattern) dipole table in units of pi/2 mod 4: A+B -> (2,2,2) = R, {+-k*} -> R, all eight -> 0; "
          "only 'empty' and 'all eight' anomaly-free; for net-zero sets b/pi mod 2 equals the U(1)^2-Z2 counts; for either overall sign", ok)
    # slice obstruction: nu0 - nu1 = J (jump at k_z = pi/2), C2x: nu1 = -nu0  =>  J = 2 nu0 even
    def jump(S, ch, nodes): return sum(ch[n] for n in S if (nodes[n][2] % 4) == 1)
    s = 1; nodes = {n: (kst + 2 * np.array(n)) % 4 for n in itertools.product((0, 1), repeat=3)}; ch = {n: s * (-1) ** sum(n) for n in nodes}
    Jk = jump([(0, 0, 0), (1, 1, 1)], ch, nodes); Jd = jump([n for n in nodes if 0 < sum(n) < 3], ch, nodes); Ja = jump(list(nodes), ch, nodes)
    check("E4 (exact integer arithmetic) jumps of a slice invariant at the plane k_z = pi/2: {+-k*} only -> odd, doublers only -> odd, all eight -> 0; "
          "with C2x (nu(k_z) = -nu(pi - k_z)) an odd jump is impossible", Jk % 2 == 1 and Jd % 2 == 1 and Ja == 0, f"J = {Jk}, {Jd}, {Ja}")
    # 2O character table (classes: E, -E, 8 C3(order 6), 8 C3(order 3), 6 C4(order 8), 6 C4(order 8'), 12 C2', 6 C2)
    r2 = np.sqrt(2); size = np.array([1, 1, 8, 8, 6, 6, 12, 6])
    X = dict(A1=[1, 1, 1, 1, 1, 1, 1, 1], A2=[1, 1, 1, 1, -1, -1, -1, 1], E=[2, 2, -1, -1, 0, 0, 0, 2],
             T1=[3, 3, 0, 0, 1, 1, -1, -1], T2=[3, 3, 0, 0, -1, -1, 1, -1],
             E12=[2, -2, 1, -1, r2, -r2, 0, 0], E52=[2, -2, 1, -1, -r2, r2, 0, 0], G32=[4, -4, -1, 1, 0, 0, 0, 0])
    X = {k: np.array(v, float) for k, v in X.items()}
    def mult(a, b): return {c: round(float(np.sum(size * X[a] * X[b] * X[c])) / 48, 9) for c in ('A1', 'A2', 'E', 'T1', 'T2')}
    orth = all(abs(np.sum(size * X[a] * X[b]) / 48 - (a == b)) < 1e-12 for a in X for b in X)
    p11, p15, p13, p55 = mult('E12', 'E12'), mult('E12', 'E52'), mult('E12', 'G32'), mult('E52', 'E52')
    ok = orth and p11 == dict(A1=1, A2=0, E=0, T1=1, T2=0) and p15 == dict(A1=0, A2=1, E=0, T1=0, T2=1) \
        and p13 == dict(A1=0, A2=0, E=1, T1=1, T2=1) and p55 == dict(A1=1, A2=0, E=0, T1=1, T2=0) and np.allclose(X['E52'], X['E12'] * X['A2'])
    check("E5 (exact character arithmetic, 2O) E1/2 x E1/2 = A1 + T1, E1/2 x E5/2 = A2 + T2, E1/2 x G3/2 = E + T1 + T2, E5/2 = E1/2 x A2: "
          "a 1-dim pair channel couples a 2-dim node irrep to exactly one 2-dim irrep type (itself or the other) and never to G3/2; with "
          "E1/2 and E5/2 each occurring once at k* this is the decoupling", ok)


# =====================================================================================================================
def main():
    print(__doc__.split('\n')[0])
    print(f"options: bdg={BDG}")
    oa = section_A()
    ob = section_B()
    section_E()
    print("\n=== Section C: cross-path agreement (convention-independent data) ===", flush=True)
    check("C1 both paths: det character label A2 / channel dimensions (dim V_A2, dim V_A1) = (5, 2) of 66 / O_h channel dimensions agree",
          oa['det'] == 'A2' and oa['dims'] == ob['dims'] == (5, 2) and oa['dims_oh'] == ob['dims_oh'] == {'A1g': 0, 'A1u': 2, 'A2g': 3, 'A2u': 2},
          f"{oa['dims_oh']}")
    check("C2 both paths: relative chirality pattern chi(k* + pi n)/chi(k*) = (-1)^|n| (degenerate PT in A, Berry flux in B; the overall sign "
          "is a convention) and two anomaly-free rotation-invariant subsets", oa['chi_rel'] == ob['chi_rel'] and oa['free'] == ob['free'] == 2)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - T0:.0f}s]")
    sys.exit(0 if FAIL == 0 else 1)


if __name__ == '__main__':
    main()
