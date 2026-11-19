#!/usr/bin/env python3
"""mod-d-lemma: does the families-mod-3 obstruction become N = 0 mod d when the hand-set Z3 is replaced by the actual
body-diagonal turn of the d-cube (d = 2, 3, 4; d = 5 as an extrapolation)?

Lemma structure carried over unchanged from families-mod-3 (its C1/C2): twisted turn group Z_n (n = order of the turn on the
fermions); light copy charge q_l, mirror copy charge q_m; the mirror's single-copy top form (M modes) keeps the twist k iff
M (q_m + k) = 0 mod n; the gapped set S = {Gamma-b, R-a, R-b} carries per-family mixed index m (q_l + k) mod n (m = doublets per
family per sublattice SU(2)); N is obstructed iff no kept k has N m (q_l + k) = 0 mod n.
Inputs: one mode per corner of the d-cube; cell-supplied content m = M = 2^(d-1); d = 3 literal content m = M = 4 and
(q_l, q_m) = (2, 1) (cited from families-mod-3 A2/B1); toy (3-4-5-0) multiplicity 2.  Charges of the turn are computed from its
permutation of the 2^d corners and its spin lift.  Cited, not rederived: 't Hooft matching, crystalline equivalence,
Dobrescu-Poppitz 2001 (6D SU(2) global anomaly, pi_6(SU(2)) = Z12, supplied).
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
from math import gcd

T0 = time.monotonic(); PASS = FAIL = 0
rng = np.random.default_rng(20261023)
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
NS = tuple(range(1, 9))

# ------------------------------------------------ group theory of the d-cube ------------------------------------------------
def signed_perms(d):
    for p in itertools.permutations(range(d)):
        for s in itertools.product((1, -1), repeat=d):
            g = np.zeros((d, d), int)
            for i in range(d): g[p[i], i] = s[i]
            yield g
def order(g):
    d = len(g); h = g.copy()
    for k in range(1, 50):
        if np.array_equal(h, np.eye(d, dtype=int)): return k
        h = h @ g
def cycle(d, axes=None):                       # x_i -> x_{i+1} on the listed axes (body-diagonal turn)
    axes = list(range(d)) if axes is None else axes; g = np.eye(d, dtype=int)
    for i, a in enumerate(axes): g[:, a] = 0
    for i, a in enumerate(axes): g[axes[(i + 1) % len(axes)], a] = 1
    return g
def stab(d):
    u = np.ones(d, int); fix, axis = [], []
    for g in signed_perms(d):
        if round(np.linalg.det(g)) != 1: continue
        if np.array_equal(g @ u, u): fix.append(order(g))
        if np.array_equal(g @ u, -u): axis.append(order(g))
    return sorted(set(fix)), sorted(set(axis))
def spin_sign(g):                              # T^n of the spin lift: (-1)^(sum n theta / 2 pi) over rotation planes
    n = order(g); ev = np.linalg.eigvals(g.astype(float)); th = np.angle(ev); s = 0.0
    pos = th[th > 1e-9]; nneg = int(np.sum(np.abs(th - np.pi) < 1e-9) + np.sum(np.abs(th + np.pi) < 1e-9))
    s = sum(n * t / (2 * np.pi) for t in pos if abs(t - np.pi) > 1e-9) + (nneg // 2) * n / 2
    return n, int(round(s)) % 2
def corner_perm(g):
    d = len(g); C = np.array(list(itertools.product((0, 1), repeat=d))); cc = 2 * C - 1; P = np.zeros((2 ** d, 2 ** d))
    for i in range(2 ** d):
        j = int(np.argmin(np.abs(cc - g @ cc[i]).sum(1))); P[j, i] = 1
    return P
def charges(g):
    n = order(g); P = corner_perm(g); ev = np.linalg.eigvals(P)
    q = sorted(int(round(np.angle(x) / (2 * np.pi / n))) % n for x in ev)
    return n, {c: q.count(c) for c in sorted(set(q))}
def fixed_windows(g):                          # Brillouin-zone corners {0, pi}^d fixed by the turn (same action mod 2 pi)
    d = len(g); return sum(np.array_equal((g @ np.array(w)) % 2, np.array(w)) for w in itertools.product((0, 1), repeat=d))

# ------------------------------------------------ lemma algebra (families-mod-3 C1/C2 with Z3 -> Z_n) ------------------------------------------------
TASTE = lambda ql, qm: {'Gb': (0, qm, -1), 'Ra': (1, ql, -1), 'Rb': (1, qm, +1)}
def S_index(n, m, ql, qm, k, N):               # Z_n(k) x SU(2)_e^2 index of S, as in families-mod-3 anom()['e']
    return (N * sum(m * h * (q + k) for _, q, h in TASTE(ql, qm).values())) % n
def kept(n, M, qm): return [k for k in range(n) if (M * (qm + k)) % n == 0]
def allowed(n, m, M, ql, qm, ks=None):
    ks = kept(n, M, qm) if ks is None else ks
    return [N for N in NS if any(S_index(n, m, ql, qm, k, N) == 0 for k in ks)]
def best(n, m, M, ferm_odd=False):             # strongest obstruction over every charge pair q_l != q_m (best case for PASS)
    qs = [q for q in range(n) if (q % 2 == 1) or not ferm_odd]; out = {}
    for ql, qm in itertools.permutations(qs, 2): out[(ql, qm)] = tuple(allowed(n, m, M, ql, qm))
    return min(out.values(), key=len), out

# ===================================== A. the body-diagonal turn in d = 2, 3, 4, 5 =====================================
print('== A. body-diagonal turns of the d-cube (proper elements of the stabilizer of the diagonal / of its axis)')
info = {}
for d in (2, 3, 4, 5):
    g = cycle(d); fx, ax = stab(d); info[d] = (round(np.linalg.det(g)), order(g), fx, ax)
    print(f'   d={d}: axis d-cycle order {order(g)} det {info[d][0]:+d}; proper orders fixing the diagonal {fx}, reversing it {ax}')
check('A1 theorem: the axis d-cycle maps the body diagonal to itself with order d and det (-1)^(d-1), so it is a proper turn '
      'only for odd d', all(info[d][0] == (-1) ** (d - 1) and info[d][1] == d for d in info))
check('A2 d = 2: no proper turn other than 1 fixes the diagonal; the natural analogue is the pi turn -1 (proper, order 2 = d, '
      'reverses the diagonal) or the diagonal reflection (the 2-cycle, improper)', info[2][2] == [1] and info[2][3] == [2])
check('A3 d = 4: the proper turns that keep the diagonal axis have orders {1,2,3} (fixing) and {2,6} (reversing): no proper '
      'order-4 turn exists; the order-4 body-diagonal turn is a rotoreflection', info[4][2] == [1, 2, 3] and info[4][3] == [2, 6])
cands = {'d2 pi-turn -1': -np.eye(2, dtype=int), 'd2 swap (improper)': cycle(2), 'd3 C3': cycle(3),
         'd4 4-cycle (improper)': cycle(4), 'd4 C3 (3 axes)': cycle(4, [0, 1, 2]), 'd4 -C3': -cycle(4, [0, 1, 2]),
         'd5 C5': cycle(5), 'd5 C3': cycle(5, [0, 1, 2])}
print('== B. charges of each turn on the 2^d corner modes, fixed windows, spin lift')
lift = {}
for nm, g in cands.items():
    n, ch = charges(g); proper = round(np.linalg.det(g)) == 1
    nn, sg = spin_sign(g) if proper else (n, None)
    grp = (f'Z{n}' if (sg == 0 or n % 2) else f'Z{2 * n}^F') if proper else f'Z{n} (antiunitary class)'
    lift[nm] = (n, sg, grp)
    print(f'   {nm:22s} n={n} corner charges {ch} fixed windows {fixed_windows(g)} lift T^n={"-1" if sg else "+1" if sg == 0 else "n/a"} -> {grp}')
P3 = corner_perm(cycle(3)); v = rng.normal(size=8)
check('B1 d = 3 reproduction: the C3 corner charges are {0^4, 1^2, 2^2} (families-mod-3 A4) and the turn fixes exactly the two '
      'windows Gamma and R', charges(cycle(3))[1] == {0: 4, 1: 2, 2: 2} and fixed_windows(cycle(3)) == 2
      and np.allclose(np.linalg.matrix_power(P3, 3) @ v, v))
check('B2 theorem: every axis-permuting turn fixes Gamma and R (all-0 and all-1 corners) in every d, so the two-window S of the '
      'lemma exists in each d; the pi turn fixes all 2^d windows', all(fixed_windows(cands[c]) >= 2 for c in cands)
      and fixed_windows(-np.eye(2, dtype=int)) == 4)
check('B3 spin lift: odd-order turns can be made order n on fermions (T^n = (-1)^F is removed by (-1)^F T); the d = 2 pi turn has '
      'T^2 = (-1)^F and cannot (group Z4^F, fermion charges odd); the d = 4 -C3 lifts with T^6 = +1',
      lift['d3 C3'][1] == 1 and lift['d2 pi-turn -1'][2] == 'Z4^F' and lift['d4 -C3'][1] == 0)

# ===================================== C. the lemma with the actual turn =====================================
print('== C. allowed family numbers N = 1..8 (obstruction = no kept twist k makes the S index vanish)')
rep = {k: allowed(3, 4, 4, 2, 1, ks=[k]) for k in range(3)}
check('C1 d = 3 reproduction of families-mod-3 C2 (n = 3, m = M = 4, q_l = 2, q_m = 1): k = 0, 2 -> {3,6}, k = 1 -> all; the '
      'mirror top form keeps only k = 2, so N = 0 mod 3', rep == {0: [3, 6], 1: list(NS), 2: [3, 6]} and kept(3, 4, 1) == [2]
      and allowed(3, 4, 4, 2, 1) == [3, 6], f'{rep}')
cases = [('d2 pi-turn Z4^F, cell m=M=2', 4, 2, 2, True), ('d2 swap Z2, cell m=M=2', 2, 2, 2, False),
         ('d3 C3 Z3, cell m=M=4', 3, 4, 4, False), ('d4 4-cycle as Z4, cell m=M=8', 4, 8, 8, False),
         ('d4 4-cycle as Z8^F, cell m=M=8', 8, 8, 8, True), ('d4 C3 Z3, cell m=M=8', 3, 8, 8, False),
         ('d4 -C3 Z6, cell m=M=8', 6, 8, 8, False), ('d5 C5 Z5, cell m=M=16', 5, 16, 16, False), ('d5 C3 Z3, cell m=M=16', 3, 16, 16, False)]
res = {}
for nm, n, m, M, fo in cases:
    b, _ = best(n, m, M, fo); res[nm] = b; print(f'   {nm:30s} strongest over all charge pairs: allowed N = {list(b)}')
mult = lambda p: [N for N in NS if N % p == 0]
check('C2 theorem (cell content): d = 2 and the order-4 turn of d = 4 obstruct NO N for any charge pair (unitary or spin-lifted '
      'group), because M = m = 2^(d-1) absorbs the 2-part of n: the twist is not selected and the index vanishes',
      all(list(res[c[0]]) == list(NS) for c in cases if c[0].startswith(('d2', 'd4 4'))))
check('C3 theorem: the proper turns of the 4-cube that keep the diagonal (C3, order 3; -C3, order 6) give N = 0 mod 3; d = 3 gives '
      'N = 0 mod 3; so with the turn read off the cube the obstruction is mod (odd part of the turn order), never mod 4 or mod 2',
      list(res['d3 C3 Z3, cell m=M=4']) == mult(3) and list(res['d4 C3 Z3, cell m=M=8']) == mult(3)
      and list(res['d4 -C3 Z6, cell m=M=8']) == mult(3))
sens = {(m, M): tuple(best(4, m, M)[0]) for m in (1, 2, 4, 8) for M in (1, 2, 4, 8)}
mod4 = sorted(k for k, v_ in sens.items() if list(v_) == mult(4)); mod2 = sorted(k for k, v_ in sens.items() if list(v_) == mult(2))
check('C4 sensitivity (d = 4 order-4 turn as a unitary Z4, best case): N = 0 mod 4 needs an ODD per-family multiplicity m and '
      'M != 0 mod 4; the toy multiplicity 2 gives at most mod 2; the cell (2^d modes) never supplies odd m',
      mod4 == [(1, 1), (1, 2)] and (2, 1) in mod2 and all(list(sens[(m, M)]) == list(NS) for m in (1, 2, 4, 8) for M in (4, 8)),
      f'mod 4 at (m,M) {mod4}; mod 2 at {mod2}')
check('C5 extrapolation (toy algebra only; the 5+1D anomaly is a different invariant): d = 5 gives N = 0 mod 5 from the 5-cycle and '
      'N = 0 mod 3 from its 3-cycles: "mod d" appears only for odd prime d, where the d-cycle is proper and m = 2^(d-1) is a unit',
      list(res['d5 C5 Z5, cell m=M=16']) == mult(5) and list(res['d5 C3 Z3, cell m=M=16']) == mult(3))
passd = {2: list(res['d2 pi-turn Z4^F, cell m=M=2']) == mult(2), 3: list(res['d3 C3 Z3, cell m=M=4']) == mult(3),
         4: list(res['d4 4-cycle as Z4, cell m=M=8']) == mult(4)}
check("C6 RESULT: the PASS criterion ('allowed N = multiples of d in each d') FAILS (d = 2: none, d = 4: none or mod 3); the 3 of "
      'the lemma is the order of the proper body-diagonal turn, which coincides with d only at d = 3 (and odd prime d)',
      passd == {2: False, 3: True, 4: False}, f'mod-d per d: {passd}')

# ===================================== D. Dobrescu-Poppitz comparison (supplied) =====================================
print('== D. Dobrescu-Poppitz 2001 (6D: space x 2 extra; SU(2) global anomaly needs n(2_+) - n(2_-) = 0 mod 6)')
dp_per_gen = 3 * (+1) + 1 * (-1)                    # Q_+ in 3 colours, L_- (their anomaly-free chirality assignment, supplied)
dp_allowed = [N for N in NS if (N * dp_per_gen) % 6 == 0]; ours = allowed(3, 4, 4, 2, 1)
check('D1 agree on the conclusion: DP per-generation doublet excess 2 (a unit times 2 in Z6) gives N = 0 mod 3, the same allowed '
      'set {3,6} as our d = 3 per-family index 4(q_l - q_m) = 1 mod 3; origin differs (pi_6(SU(2)) = Z12 and the colour count vs '
      'the turn order and the cell content)', dp_allowed == ours == [3, 6], f'DP {dp_allowed}, ours {ours}')
d_zoom = 3 + 1
check('D2 zoom as DP\'s extra dimensions: space + zoom is d = 4 (4+1D, odd: no Weyl fermions; pi_5(SU(2)) = Z2 has no 3-part); our '
      'd = 4 class gives mod 3 only via the 3-axis turn, not the zoom; DP needs TWO extra directions with 6D chirality',
      (d_zoom + 1) % 2 == 1 and list(res['d4 C3 Z3, cell m=M=8']) == mult(3))
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('theorems: A1-A3, B2, B3, C1-C3; finite/sensitivity: B1, C4; extrapolation: C5; comparison (supplied DP): D1, D2.')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
