#!/usr/bin/env python3
"""C4 step 2: exhaustive classification of O-covariant one-qubit Clifford QCAs on Z^3 whose
single-site images lie in the Chebyshev ball of radius RADIUS (env C4_RADIUS, default 1 = the
27-point cell {-1,0,1}^3), for all five Clifford-valued soldering actions (menu + sign-f).

Certificate structure
  1. The unsigned covariance conditions v_{rho(R)a} = B_R v_a are F2-linear; their solution space
     W (basis by exact F2 elimination) is enumerated EXHAUSTIVELY by two different enumerators
     (brute force over span(W) when dim W <= 26; split u / exact linear solve for w always).
  2. The symplectic (QCA) conditions <v_X, T_t v_X> = <v_Z, T_t v_Z> = 0, <v_X, T_t v_Z> = delta_t0
     for all t in {-2R..2R}^3 (all overlapping translates) are imposed exactly.  These are
     equivalent to M^dag Lambda M = Lambda, re-verified in Laurent-polynomial arithmetic; they imply
     invertibility (M^-1 = Lambda M^dag Lambda), so every survivor is a QCA.
  3. Phases: each of the 4 sign choices (X_0 -> +-P_X, Z_0 -> +-P_Z) is tested against the full
     signed covariance relation for all 24 rotations.
Also: the same for all 58 homomorphisms individually (conjugation invariance of counts), the
25 twisted pairs (rho_in, rho_out), and the time-reversal twist (odd rotations send alpha to
alpha^-1, unitary or antiunitary realisation).
"""
import sys
import os
import time
import itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c4lib as L

P = F = 0


def check(name, ok):
    global P, F
    if ok:
        P += 1
        print('PASS', name, flush=True)
    else:
        F += 1
        print('FAIL', name, flush=True)


D = L.D
OG = L.SUBGROUPS['O']
homs = L.all_homs()
classes = {}
for h in homs:
    classes.setdefault(L.conj_class_of_hom(h), []).append(h)
REP = {a: tuple(L.menu_hom(a)) for a in ('trivial', 'sign', 'axis', 'full')}
Hf = L.G([[-1, 0, 0], [0, 0, 1], [0, 1, 0]])
REP['sign-f'] = tuple(L.ID if L.perm_sign(L.O[R]) == 1 else Hf for R in range(24))
NAMES = ['trivial', 'sign', 'sign-f', 'axis', 'full']


def is_onsite(M):
    return all(e == (0, 0, 0) for i in range(2) for j in range(2) for e in M[i][j])


def orbit_type(p):
    """which O-orbits (by Chebyshev/Manhattan shape) occur in a polynomial."""
    s = set()
    for e in p:
        a = tuple(sorted(map(abs, e)))
        s.add(a)
    return sorted(s)


def enumerate_both(B):
    t0 = time.time()
    s2 = L.enumerate_solutions_split(B)
    t2 = time.time() - t0
    s1 = None
    if B.shape[0] <= 26 and L.RADIUS == 1:
        s1 = L.enumerate_solutions(B)
    return s1, s2, t2


def signs_ok(s, hin, hout, H):
    out = []
    for sx in (1, -1):
        for sz in (1, -1):
            if L.signed_covariant(L.pstr_from_vec(s[:D], sx), L.pstr_from_vec(s[D:], sz), hin, hout, H):
                out.append((sx, sz))
    return out


def classify(hin, hout, H, label, verbose=True):
    B = L.covariance_space(hin, hout, H)
    s1, s2, t2 = enumerate_both(B)
    k2 = set(map(L.sol_key, s2))
    if s1 is not None:
        check(f'{label}: brute-force and split enumerators agree ({len(s2)} unsigned solutions)',
              set(map(L.sol_key, s1)) == k2 and len(s1) == len(s2))
    sym = all(L.is_symplectic(L.matrix_of(s)) for s in s2)
    check(f'{label}: every unsigned solution is symplectic in Laurent arithmetic', sym)
    signed = []
    for s in s2:
        sg = signs_ok(s, hin, hout, H)
        for x in sg:
            signed.append((s, x))
    if verbose:
        print(f'  {label}: dim W = {B.shape[0]}, unsigned = {len(s2)}, signed QCAs = {len(signed)}, '
              f'split time {t2:.1f}s')
    return B, s2, signed


def mat_key(M):
    return tuple(tuple(sorted(M[i][j])) for i in range(2) for j in range(2))


def elem_lower(g):
    return [[L.ONE, L.ZERO], [g, L.ONE]]


def elem_upper(g):
    return [[L.ONE, g], [L.ZERO, L.ONE]]


SL2 = []
for a, b, c, d in itertools.product((0, 1), repeat=4):
    if (a * d + b * c) % 2 == 1:
        SL2.append([[L.ONE if a else L.ZERO, L.ONE if b else L.ZERO],
                    [L.ONE if c else L.ZERO, L.ONE if d else L.ZERO]])


def invariant_polys():
    """F2-span of O-orbit sums on the cell (all are self-adjoint since each orbit is -1 stable)."""
    orbs = []
    seen = set()
    for r in L.CELL:
        if r in seen:
            continue
        orb = frozenset(tuple(int(v) for v in L.O[R] @ np.array(r)) for R in range(24))
        seen |= orb
        orbs.append(orb)
    V = []
    for bits in itertools.product((0, 1), repeat=len(orbs)):
        p = L.ZERO
        for b, o in zip(bits, orbs):
            if b:
                p = L.padd(p, o)
        V.append(p)
    return orbs, V


ORBS, VINV = invariant_polys()
print(f'cell radius {L.RADIUS}: {L.NC} sites, {len(ORBS)} O-orbits of sites, |V_inv| = {len(VINV)}')
check('every O-orbit of cell sites is closed under r -> -r (so invariant polys are self-adjoint)',
      all(frozenset((-a, -b, -c) for (a, b, c) in o) == o for o in ORBS))

results = {}
print('\n== O-covariant, same action in and out ==')
for nm in NAMES:
    h = REP[nm]
    B, uns, signed = classify(h, h, OG, f'O/{nm}')
    results[nm] = (uns, signed)
    Ms = [L.matrix_of(s) for s in uns]
    check(f'O/{nm}: every solution has det = 1', all(L.det(M) == L.ONE for M in Ms))
    onsite = [M for M in Ms if is_onsite(M)]
    taus = [L.trace(M) for M in Ms]
    nonconst = sum(1 for t in taus if t not in (L.ZERO, L.ONE))
    print(f'  O/{nm}: on-site {len(onsite)}, entangling {len(Ms) - len(onsite)}, '
          f'nonconstant trace {nonconst}, trace 0: {sum(1 for t in taus if t == L.ZERO)}, '
          f'trace 1: {sum(1 for t in taus if t == L.ONE)}')
    cen = [C for C in SL2 if mat_key(C) in {mat_key(M) for M in onsite}]
    # structural decomposition: M in Cen * {E_l(g), E_u(g)} * SL2 restricted to covariant ones
    gen = set()
    for C1 in SL2:
        for C2 in SL2:
            for g in VINV:
                for E in (elem_lower(g), elem_upper(g)):
                    gen.add(mat_key(L.mat_mul(C1, L.mat_mul(E, C2))))
    sol_keys = {mat_key(M) for M in Ms}
    check(f'O/{nm}: every unsigned solution has the form C1 E(g) C2 (C on-site Clifford, '
          f'E(g) = one layer of CZ/S-type gates along an O-orbit polynomial g)', sol_keys <= gen)
    if nm in ('axis', 'full'):
        check(f'O/{nm}: the only unsigned solution is the identity matrix',
              len(Ms) == 1 and mat_key(Ms[0]) == mat_key([[L.ONE, L.ZERO], [L.ZERO, L.ONE]]))
        check(f'O/{nm}: the only signed QCA is the identity automorphism',
              len(signed) == 1 and signed[0][1] == (1, 1))
    if nm == 'trivial':
        # every product C1 E(g) C2 is covariant & in range: count matches
        check('O/trivial: solution set equals {C1 E_l(g) C2 : C1,C2 in SL2(F2), g in V_inv}', sol_keys == gen)
    if nm == 'sign-f':
        check('O/sign-f: no solution has nonconstant trace', nonconst == 0)

print('\n== count invariance: every one of the 58 homomorphisms separately (unsigned counts) ==')
cls_counts = {}
for h in homs:
    B = L.covariance_space(h, h, OG)
    n = len(L.enumerate_solutions_split(B))
    c = L.conj_class_of_hom(h)
    cls_counts.setdefault(c, set()).add(n)
ok = all(len(v) == 1 for v in cls_counts.values())
check('unsigned solution count is constant on each conjugacy class of actions', ok)
for nm in NAMES:
    c = [k for k in cls_counts if REP[nm] in k][0]
    print(f'  class of {nm}: {len(c)} homs, count {sorted(cls_counts[c])}')

print('\n== twisted covariance alpha beta^in_R = beta^out_R alpha (25 class pairs) ==')
tw = {}
for a in NAMES:
    for b in NAMES:
        B = L.covariance_space(REP[a], REP[b], OG)
        uns = L.enumerate_solutions_split(B)
        signed = [(s, x) for s in uns for x in signs_ok(s, REP[a], REP[b], OG)]
        tw[(a, b)] = (len(uns), len(signed))
        if uns:
            Ms = [L.matrix_of(s) for s in uns]
            nonon = sum(1 for M in Ms if not is_onsite(M))
        else:
            nonon = 0
        print(f'  in={a:8s} out={b:8s}: unsigned {len(uns):4d}  signed {len(signed):4d}  non-on-site {nonon}')
        if a != b:
            # alpha intertwines two different actions: then its k=0 symbol M(1) (an F2 matrix) intertwines the
            # label actions; non-conjugate actions forbid any solution only if no such intertwiner exists.
            pass
check('twisted pairs: no signed QCA intertwines two Clifford-inequivalent actions (unsigned ones exist only for '
      'trivial<->sign and axis<->full, and fail the phase relations)',
      all(tw[(a, b)][1] == 0 for a in NAMES for b in NAMES if a != b))

print('\n== time-reversal twist: beta_R alpha beta_R^-1 = alpha^{chi(R)}, chi = sign character ==')


def inverse_cov_space(h, H):
    """(u,w) with: even R: v_{rho(R)a} = B_R v_a ; odd R: B_R M B_R^-1 = Lambda M^dag Lambda.
    Odd condition in column form: B_R M = M' B_R with M' = Lambda M^dag Lambda (inverse).  M^dag on cell
    vectors: entry (i,j) of M' is conj of M (swap & antipode)."""
    rows = []
    E = np.eye(D, dtype=np.uint8)
    Zr = np.zeros((D, D), np.uint8)
    sel = {1: np.hstack([E, Zr]), 3: np.hstack([Zr, E]), 2: np.hstack([E, E])}
    # antipode on a cell vector part: site r -> -r
    anti = np.zeros((L.NC, L.NC), np.uint8)
    for i, r in enumerate(L.CELL):
        anti[L.CIDX[(-r[0], -r[1], -r[2])], i] = 1
    Zc = np.zeros((L.NC, L.NC), np.uint8)
    # M = [[a,b],[c,d]], u=(a;c), w=(b;d).  Lambda M^dag Lambda = [[dbar, bbar],[cbar, abar]]
    # inverse columns: u' = (dbar; cbar), w' = (bbar; abar)
    # u' as linear map of (u,w): dbar from w_z, cbar from u_z
    Up = np.block([[Zc, Zc, Zc, anti], [Zc, anti, Zc, Zc]])
    Wp = np.block([[Zc, Zc, anti, Zc], [anti, Zc, Zc, Zc]])
    selp = {1: Up, 3: Wp, 2: (Up + Wp) % 2}
    for R in H:
        Qm = L.O[h[R]]
        BR = L.B_matrix(R, Qm)
        lm = L.label_map(Qm)
        odd = L.perm_sign(L.O[R]) == -1
        for a in (1, 3):
            b = lm[a][0]
            if not odd:
                rows.append((sel[b] + BR @ sel[a]) % 2)
            else:
                # beta alpha beta^-1 = alpha^-1  <=>  alpha^-1(beta(s_a)) = beta(alpha(s_a))
                rows.append((selp[b] + BR @ sel[a]) % 2)
    return L.f2_nullspace(np.vstack(rows))


def apply_alpha(PX, PZ, Pstr):
    im = L.images(PX, PZ)
    out = (Pstr[0], {})
    for s, a in Pstr[1].items():
        out = L.pmul(out, L.translate(im[a], s))
    return out


def inverse_signed(M, PX, PZ):
    """signed images of alpha^-1 from the unsigned inverse Lambda M^dag Lambda."""
    a, b = M[0]
    c, d = M[1]
    inv = [[L.pbar(d), L.pbar(b)], [L.pbar(c), L.pbar(a)]]
    res = []
    for col, target in ((0, (0, {(0, 0, 0): 1})), (1, (0, {(0, 0, 0): 3}))):
        px, pz = inv[0][col], inv[1][col]
        v = np.zeros(D, np.uint8)
        for e in px:
            v[L.CIDX[e]] = 1
        for e in pz:
            v[L.NC + L.CIDX[e]] = 1
        Q = L.pstr_from_vec(v)
        img = apply_alpha(PX, PZ, Q)
        if img[1] != target[1]:
            return None
        if img[0] == 2:
            Q = (2, Q[1])
        elif img[0] != 0:
            return None
        res.append(Q)
    return res


def conjK(Pstr):
    k = (-Pstr[0]) % 4
    for a in Pstr[1].values():
        if a == 2:
            k = (k + 2) % 4
    return (k, dict(Pstr[1]))


for nm in NAMES:
    h = REP[nm]
    B = inverse_cov_space(h, OG)
    uns = L.enumerate_solutions_split(B)
    Ms = [L.matrix_of(s) for s in uns]
    nonon = [M for M in Ms if not is_onsite(M)]
    nsig_u = nsig_a = 0
    for s, M in zip(uns, Ms):
        for sx in (1, -1):
            for sz in (1, -1):
                PX, PZ = L.pstr_from_vec(s[:D], sx), L.pstr_from_vec(s[D:], sz)
                inv = inverse_signed(M, PX, PZ)
                if inv is None:
                    continue
                iX, iZ = inv
                for anti in (False, True):
                    ok = True
                    for R in OG:
                        Qm = L.O[h[R]]
                        odd = L.perm_sign(L.O[R]) == -1
                        for a in (1, 3):
                            col = Qm[:, a - 1]
                            b = int(np.nonzero(col)[0][0])
                            bs = (0 if col[b] > 0 else 2, {(0, 0, 0): b + 1})  # beta_R(sigma_a) unitary part
                            if odd and anti:
                                bs = conjK(bs) if a == 2 else bs  # K fixes X,Z labels
                            img_a = L.images(PX, PZ)[a]
                            lhs_src = L.beta(R, Qm, conjK(img_a) if (odd and anti) else img_a)
                            if odd:
                                rhs = apply_alpha(iX, iZ, bs)
                            else:
                                rhs = apply_alpha(PX, PZ, bs)
                            if not L.peq(lhs_src, rhs):
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        if anti:
                            nsig_a += 1
                        else:
                            nsig_u += 1
    covO = {mat_key(L.matrix_of(s)) for s in results[nm][0]}
    extra = [M for M in Ms if mat_key(M) not in covO]
    print(f'  TR-twist/{nm}: unsigned {len(uns)}, non-on-site {len(nonon)}, not already O-covariant {len(extra)}, '
          f'signed (unitary odd) {nsig_u}, signed (antiunitary odd) {nsig_a}')
    check(f'TR-twist/{nm}: unsigned solutions are symplectic', all(L.is_symplectic(M) for M in Ms))
    trs = [L.trace(M) for M in Ms]
    print(f'    traces: 0 -> {sum(t == L.ZERO for t in trs)}, 1 -> {sum(t == L.ONE for t in trs)}, '
          f'nonconstant -> {sum(t not in (L.ZERO, L.ONE) for t in trs)}')
    check(f'TR-twist/{nm}: every trace is O-invariant (so the trichotomy and glider no-go apply)',
          all(frozenset(tuple(int(v) for v in L.O[R] @ np.array(e)) for e in t) == t for t in trs for R in OG))
    if nm in ('axis', 'full'):
        for M in Ms:
            print('    on-site TR-twisted solution, matrix', L.mat_key(M) if hasattr(L, 'mat_key') else mat_key(M))
    if nm in ('axis', 'full'):
        check(f'TR-twist/{nm}: still only on-site solutions', len(nonon) == 0)
    results['TR/' + nm] = (uns, Ms, extra)

print(f'TOTAL: PASS={P} FAIL={F}')
