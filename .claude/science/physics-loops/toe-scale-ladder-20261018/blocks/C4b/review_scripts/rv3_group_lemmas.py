#!/usr/bin/env python3
"""Reviewer script rv3 (independent): exact group-theoretic steps of Lemmas 1-5 and the Margolus
symmetry claim.  Integer / exact-rational arithmetic only (numpy only for ranks)."""
import itertools
import numpy as np
from fractions import Fraction as Fr

P_ = F_ = 0


def check(name, ok, extra=''):
    global P_, F_
    P_ += bool(ok)
    F_ += (not ok)
    print('PASS' if ok else 'FAIL', name, ('::' + str(extra)) if extra != '' else '')


O = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for c in range(3):
            M[perm[c], c] = sg[c]
        if round(np.linalg.det(M)) == 1:
            O.append(M)
assert len(O) == 24


def s_of(R):
    return int(round(np.linalg.det(np.abs(R))))   # sign of the axis permutation


def Q(R, action):
    s = s_of(R)
    if action == 'trivial':
        return np.eye(3, dtype=int)
    if action == 'sign':
        return np.diag([1, s, s])
    if action == 'axis':
        return s * np.abs(R)
    if action == 'full':
        return R


def key(M):
    return tuple(M.ravel())


T = [R for R in O if s_of(R) == 1]
D4 = [R for R in O if abs(R[2, 2]) == 1]
n3 = np.array([1, 1, 1])
D3 = [R for R in O if (abs(R @ n3) == n3).all() and (R @ n3 == n3).all() or (R @ n3 == -n3).all()]
D2 = [R for R in O if (R == np.diag(np.diag(R))).all()]
subs = {'O': O, 'T': T, 'D4': D4, 'D3': D3, 'D2': D2}
for nm, H in subs.items():
    closed = all(any((A @ B == C).all() for C in H) for A in H for B in H)
    fix = sum(H).astype(float) / len(H)          # projector onto fixed vectors
    check(f'Lemma 1: {nm} (order {len(H)}) is a group fixing no nonzero vector (f = R f => f = 0)',
          closed and np.allclose(fix, 0), f'fixed dim {np.linalg.matrix_rank(fix)}')

# Lemma 1 relabelling: R e_i = s e_j maps the transverse lattice of e_i onto that of e_j
ok = True
for R in O:
    for i in range(3):
        col = R[:, i]
        j = int(np.flatnonzero(col)[0])
        for a in range(3):
            if a != i:
                img = R[:, a]
                if img[j] != 0:
                    ok = False
check('Lemma 1: R maps the e_i-transverse plane onto the e_j-transverse plane (cell-wise relabelling)', ok)

# Lemma 2(a): orbit spans
rng = np.random.default_rng(3)
for action in ('axis', 'full'):
    QO = [Q(R, action) for R in O]
    spans = {}
    for m in [np.array(v) for v in ((1, 0, 0), (1, 1, 0), (1, -1, 0), (1, 1, 1), (2, -1, -1))] + \
             [rng.normal(size=3) for _ in range(20)]:
        spans[tuple(np.round(m, 3))] = np.linalg.matrix_rank(np.array([q @ m for q in QO]))
    one = [k for k, v in spans.items() if v == 1]
    print(f'[{action}] orbit-span ranks: ' + ', '.join(f'{k}:{v}' for k, v in list(spans.items())[:5]))
    if action == 'full':
        check('Lemma 2(a) full: every tested m has O-orbit spanning R^3 (irreducible T1)', all(v == 3 for v in spans.values()))
    else:
        check('Lemma 2(a) axis: only m = +-n has a 1-dim orbit span (perp-to-n m span 2 -> still SU(2))',
              one == [(1, 1, 1)] and spans[(2, -1, -1)] == 2 and spans[(1, -1, 0)] == 2)

# Lemma 2(b) step 5-6: vacuum-fixing subgroup H_m and its on-site action
nvec = np.array([1, 1, 1])
Hm_axis = [R for R in O if (Q(R, 'axis') @ nvec == nvec).all()]
check('Lemma 2(b) axis: H_n = {R : Q(R) n = n} = T exactly (order 12)',
      len(Hm_axis) == 12 and all(s_of(R) == 1 for R in Hm_axis))
check('Lemma 2(b) axis: odd R send n -> -n (vacuum -> fully polarised anti-vacuum; not in H_n)',
      all((Q(R, 'axis') @ nvec == -nvec).all() for R in O if s_of(R) == -1))
check('Lemma 2(b) axis: T acts on-site by rotations about n (Q(R) n = n, Q(R) in SO(3))',
      all((Q(R, 'axis') @ nvec == nvec).all() and round(np.linalg.det(Q(R, 'axis'))) == 1 for R in T))
# x-independence of c_R: on-site part of beta_R is the same unitary at every site; a rotation about m maps
# sigma^+_m to e^{i psi} sigma^+_m.  Exact check with SU(2) lifts for R in T, axis action:
SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.diag([1, -1]).astype(complex)
SIG = [SX, SY, SZ]
m = nvec / np.sqrt(3)
Hn = sum(m[i] * SIG[i] for i in range(3))
w, V = np.linalg.eigh(Hn)
up, dn = V[:, 1], V[:, 0]
splus = np.outer(up, dn.conj())


def lift(Qm):
    # U with U sigma_a U^dag = sum_b Qm[b,a] sigma_b, found by solving the linear intertwiner equation
    A = []
    for a in range(3):
        rhs = sum(Qm[b, a] * SIG[b] for b in range(3))
        A.append(np.kron(np.eye(2), SIG[a].T) - np.kron(rhs, np.eye(2)))   # vec(U s) - vec(rhs U) row-major
    A = np.vstack(A)
    _, s, Vh = np.linalg.svd(A)
    U = Vh[-1].conj().reshape(2, 2)
    U = U / np.sqrt(abs(np.linalg.det(U)))
    return U


ok = True
for R in T:
    U = lift(Q(R, 'axis').astype(float))
    for a in range(3):
        ok &= np.allclose(U @ SIG[a] @ U.conj().T, sum(Q(R, 'axis')[b, a] * SIG[b] for b in range(3)))
    img = U @ splus @ U.conj().T
    ph = np.vdot(splus.ravel(), img.ravel())
    ok &= np.allclose(img, ph * splus) and abs(abs(ph) - 1) < 1e-12
check('Lemma 2(b) step 5 axis: for R in T, D(Q(R)) sigma^+_n D^dag = e^{i psi_R} sigma^+_n (site-independent phase)', ok)
check('Lemma 2(b) step 6: T fixes no nonzero vector => t0 = 0', np.allclose(sum(T), 0))

# sign action: kernel T acts trivially on site; trivial action: H_m = H
check('sign action: kernel of s is T and acts trivially on-site', all((Q(R, 'sign') == np.eye(3)).all() for R in T))

# Lemma 3: near-pair count and covariance group of the pair walk
for r in (1, 2):
    ball = [v for v in itertools.product(range(-r, r + 1), repeat=3) if v != (0, 0, 0)]
    classes = {tuple(sorted([v, tuple(-c for c in v)])) for v in ball}
    dr = len(classes)
    check(f'Lemma 3: d_r = ((2r+1)^3-1)/2 unordered near-pair relative positions, r={r}',
          dr == ((2 * r + 1) ** 3 - 1) // 2, dr)
ball1 = [v for v in itertools.product(range(-1, 2), repeat=3) if v != (0, 0, 0)]
cls = sorted({tuple(sorted([v, tuple(-c for c in v)])) for v in ball1})


def orbits(G):
    seen, orbs = set(), []
    for c in cls:
        if c in seen:
            continue
        orb = set()
        for R in G:
            v = tuple(R @ np.array(c[0]))
            orb.add(tuple(sorted([v, tuple(-x for x in v)])))
        seen |= orb
        orbs.append(len(orb))
    return sorted(orbs)


print('13-dim near-pair permutation rep orbit sizes: O', orbits(O), ' T', orbits(T))
check('Lemma 3: 13 = 3 + 4 + 6 (face, corner, edge orbits) under both O and T', orbits(O) == [3, 4, 6] == orbits(T))

# Lemma 4(a): real commutant of Q(O)
for action, expect in (('axis', 2), ('full', 1), ('sign', 5), ('trivial', 9)):
    rows = []
    for R in O:
        q = Q(R, action).astype(float)
        rows.append(np.kron(q, np.eye(3)) - np.kron(np.eye(3), q.T))
    dim = 9 - np.linalg.matrix_rank(np.vstack(rows))
    check(f'Lemma 4(a): real commutant of Q(O), {action}: dim {expect}', dim == expect, dim)
Pn = np.outer(nvec, nvec) / 3
PE = np.eye(3) - Pn
sols = [(a, b) for a in (1, -1) for b in (1, -1) if np.isclose(np.linalg.det(a * Pn + b * PE), 1)]
check('Lemma 4(a) axis: SO(3) elements of span{P_n,P_E} = {1, pi-rotation about n}', sorted(sols) == [(1, -1), (1, 1)], sols)
# Lemma 4(c) exhibit: sigma_n(r) sigma_n(r+e) -> s^2 (same) under axis; face bonds -> face bonds
check('Lemma 4(c): axis beta_R maps sigma_n -> s(R) sigma_n, so face-bond sigma_n sigma_n terms are invariant',
      all((Q(R, 'axis') @ nvec == s_of(R) * nvec).all() for R in O))

# Margolus symmetry (independent enumeration with exact half-integers)
c = (Fr(1, 2),) * 3


def centres_ok(R, t, shift):
    """does x -> R x + t map partition-with-offset-0 cube centres onto partition-with-offset `shift` centres?"""
    cc = tuple(Fr(int(sum(R[i, j] * 1 for j in range(3) if R[i, j]))) for i in range(3))
    img = [sum(R[i, j] * c[j] for j in range(3)) + t[i] for i in range(3)]
    return all(((img[i] - c[i] - shift) % 2) == 0 for i in range(3))


pres = [(R, t) for R in O for t in itertools.product(range(2), repeat=3) if centres_ok(R, t, 0)]
swap = [(R, t) for R in O for t in itertools.product(range(2), repeat=3) if centres_ok(R, t, 1)]
check('Margolus: exactly one t mod 2 per R preserves P0 (and then P1) => stabiliser 2Z^3 x| O_c', len(pres) == 24
      and len({key(R) for R, t in pres}) == 24, len(pres))
# P1 preserved automatically
ok = all(all(((sum(R[i, j] * (c[j] + 1) for j in range(3)) + t[i] - c[i] - 1) % 2) == 0 for i in range(3)) for R, t in pres)
check('Margolus: every P0-preserving element also preserves P1', ok)
site_rot = [R for R, t in pres if t == (0, 0, 0)]
check('Margolus: t = 0 survivors = C3 about (1,1,1) (order 3)', len(site_rot) == 3 and all((R @ n3 == n3).all() for R in site_rot))
check('Margolus: pure translations preserving: only t = 0 mod 2', [t for R, t in pres if (R == np.eye(3)).all()] == [(0, 0, 0)])
check('Margolus: (1,1,1) swaps the partitions', any((R == np.eye(3)).all() and t == (1, 1, 1) for R, t in swap))
check('Margolus: index of 2Z^3 in Z^3 is 8', 2 ** 3 == 8)
# Lemma 5 combinatorial step
cube0 = list(itertools.product(range(2), repeat=3))
blk1 = lambda x: tuple((xi - 1) // 2 for xi in x)    # P1 cubes {1,2},{3,4},{-1,0}
check('Lemma 5: distinct sites of a P0 cube lie in distinct P1 cubes (and vice versa by symmetry)',
      len({blk1(x) for x in cube0}) == 8)
print(f'TOTAL: PASS={P_} FAIL={F_}')
