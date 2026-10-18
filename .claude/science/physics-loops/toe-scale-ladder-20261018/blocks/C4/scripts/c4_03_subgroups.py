#!/usr/bin/env python3
"""C4 step 3: the same exhaustive classification for the subgroups T, D4, D3, D2 of O (actions
restricted from the five Clifford-valued actions on O), radius-1 cell.

For each (action, H): unsigned and signed counts, on-site count, and the dynamical class of every
solution by its trace tau = tr M (proved trichotomy, see c4_04 / NOTE):
   periodic   tau in {0, 1}
   glider     tau = x^r + x^-r, r != 0      (a finite Pauli translates by r every step)
   spreading  otherwise                     (no finite Pauli ever returns to a translate of itself)
Brute-force and split enumerators are cross-checked where dim W <= 24.
"""
import sys
import os
import time
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
REP = {a: tuple(L.menu_hom(a)) for a in ('trivial', 'sign', 'axis', 'full')}
Hf = L.G([[-1, 0, 0], [0, 0, 1], [0, 1, 0]])
REP['sign-f'] = tuple(L.ID if L.perm_sign(L.O[R]) == 1 else Hf for R in range(24))
NAMES = ['trivial', 'sign', 'sign-f', 'axis', 'full']
BRUTE_MAX = int(os.environ.get('C4_BRUTE_MAX', '24'))
GROUPS = os.environ.get('C4_GROUPS', 'T,D4,D3,D2').split(',')


def dyn_class(tau):
    if tau in (L.ZERO, L.ONE):
        return 'periodic'
    if len(tau) == 2:
        a, b = sorted(tau)
        if a == tuple(-v for v in b) and a != (0, 0, 0):
            return 'glider'
    return 'spreading'


def is_onsite(M):
    return all(e == (0, 0, 0) for i in range(2) for j in range(2) for e in M[i][j])


summary = []
for gname in GROUPS:
    H = L.SUBGROUPS[gname]
    for nm in NAMES:
        h = REP[nm]
        check(f'{gname}/{nm}: restriction is a homomorphism on {gname}', L.is_hom(h, H))
        B = L.covariance_space(h, h, H)
        t0 = time.time()
        s2 = L.enumerate_solutions_split(B)
        t2 = time.time() - t0
        if B.shape[0] <= BRUTE_MAX:
            s1 = L.enumerate_solutions(B)
            check(f'{gname}/{nm}: brute-force and split enumerators agree ({len(s2)})',
                  set(map(L.sol_key, s1)) == set(map(L.sol_key, s2)) and len(s1) == len(s2))
        Ms = [L.matrix_of(s) for s in s2]
        check(f'{gname}/{nm}: all {len(Ms)} solutions symplectic (Laurent check) with det 1',
              all(L.is_symplectic(M) and L.det(M) == L.ONE for M in Ms))
        cls = {'periodic': 0, 'glider': 0, 'spreading': 0}
        cls_signed = {'periodic': 0, 'glider': 0, 'spreading': 0}
        glider_dirs = set()
        nsigned = 0
        onsite = 0
        for s, M in zip(s2, Ms):
            c = dyn_class(L.trace(M))
            cls[c] += 1
            onsite += is_onsite(M)
            if c == 'glider':
                glider_dirs.add(tuple(sorted(L.trace(M)))[1])
            ns = sum(1 for sx in (1, -1) for sz in (1, -1)
                     if L.signed_covariant(L.pstr_from_vec(s[:D], sx), L.pstr_from_vec(s[D:], sz), h, h, H))
            nsigned += ns
            if ns:
                cls_signed[c] += 1
        # trace is H-invariant (it must be, by covariance)
        inv = all(frozenset(tuple(int(v) for v in L.O[R] @ np.array(e)) for e in L.trace(M)) == L.trace(M)
                  for M in Ms for R in H)
        check(f'{gname}/{nm}: every trace is {gname}-invariant', inv)
        line = (f'{gname:3s} {nm:8s} dimW={B.shape[0]:3d} unsigned={len(s2):6d} signed={nsigned:6d} '
                f'on-site={onsite:3d} periodic={cls["periodic"]:5d} glider={cls["glider"]:5d} '
                f'spreading={cls["spreading"]:6d} | with valid phases: {cls_signed} '
                f'glider dirs={sorted(glider_dirs)} ({t2:.1f}s)')
        print('  ' + line, flush=True)
        summary.append(line)
        if gname == 'T':
            check(f'T/{nm}: no glider (T-orbits of nonzero vectors have >2 elements)', cls['glider'] == 0)

print('\nSUMMARY')
for s in summary:
    print(s)
print(f'TOTAL: PASS={P} FAIL={F}')
