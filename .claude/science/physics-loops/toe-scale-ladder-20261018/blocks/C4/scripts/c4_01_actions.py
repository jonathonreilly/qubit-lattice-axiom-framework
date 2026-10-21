#!/usr/bin/env python3
"""C4 step 1: the Clifford-valued soldering actions of O on one qubit.

Checks
  * O has 24 elements, closed, with the generators used.
  * Every menu action (trivial, sign, axis, full; matrices exactly as in the 2026-10-17 runner)
    is a homomorphism O -> O(signed perms, det 1) and its label action is an automorphism of the
    one-qubit Pauli algebra (preserves sigma_a sigma_b = i eps_abc sigma_c with signs), i.e. it is
    conjugation by an on-site Clifford unitary.  Explicit SU(2) lifts are constructed and checked.
  * All homomorphisms O -> O are enumerated exhaustively (58) and fall into exactly 5 conjugacy
    classes under the target O (= on-site Clifford group mod phases).  Four are the menu; the fifth
    ('sign-f') is a C2-valued action through the sign character, realised by a face-diagonal half
    turn instead of the axis half turn diag(1,-1,-1).  As SO(3) representations sign and sign-f are
    conjugate (both A1+2A2), so the menu, which is up to SO(3) conjugacy, lists them once; as
    Clifford actions they are not conjugate, so both are covered here.
  * The unsigned symplectic matrices B_R are a representation and preserve the commutation form.
"""
import sys
import os
import itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c4lib as L

P = F = 0


def check(name, ok):
    global P, F
    if ok:
        P += 1
        print('PASS', name)
    else:
        F += 1
        print('FAIL', name)


check('O has 24 elements', len(L.O) == 24)
check('O closed under multiplication', all(L.MUL[i, j] >= 0 for i in range(24) for j in range(24)))
for n, H in L.SUBGROUPS.items():
    exp = {'O': 24, 'T': 12, 'D4': 8, 'D3': 6, 'D2': 4}[n]
    check(f'subgroup {n} has order {exp}', len(H) == exp)

# Pauli matrices
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
SIG = [SX, SY, SZ]


def su2_lift(Qm):
    """Find U in SU(2) with U sigma_a U^dag = sum_b Q[b,a] sigma_b (axis-angle formula)."""
    Qm = np.array(Qm, float)
    tr = np.trace(Qm)
    ang = np.arccos(np.clip((tr - 1) / 2, -1, 1))
    if abs(ang) < 1e-9:
        return I2
    if abs(ang - np.pi) < 1e-9:
        # axis from Q + I
        Mx = (Qm + np.eye(3)) / 2
        k = int(np.argmax(np.diag(Mx)))
        n = Mx[:, k] / np.sqrt(Mx[k, k])
    else:
        n = np.array([Qm[2, 1] - Qm[1, 2], Qm[0, 2] - Qm[2, 0], Qm[1, 0] - Qm[0, 1]]) / (2 * np.sin(ang))
    return np.cos(ang / 2) * I2 - 1j * np.sin(ang / 2) * sum(n[i] * SIG[i] for i in range(3))


for action in ('trivial', 'sign', 'axis', 'full'):
    h = L.menu_hom(action)
    check(f'{action}: is a homomorphism O -> O', L.is_hom(h))
    ok = True
    for R in range(24):
        Qm = L.menu_Q(L.O[R], action)
        U = su2_lift(Qm)
        for a in range(3):
            lhs = U @ SIG[a] @ U.conj().T
            rhs = sum(Qm[b, a] * SIG[b] for b in range(3))
            ok &= np.allclose(lhs, rhs)
    check(f'{action}: every Q(R) is conjugation by an explicit SU(2) (Clifford) unitary', ok)
    # unsigned symplectic rep on the cell is a homomorphism and preserves the form
    Bs = [L.B_matrix(R, L.O[h[R]]) for R in range(24)]
    okh = all(np.array_equal((Bs[i] @ Bs[j]) % 2, Bs[L.MUL[i, j]]) for i in range(24) for j in range(24))
    check(f'{action}: R -> B_R is a representation on F2^{L.D}', okh)
    rng = np.random.default_rng(1)
    U = rng.integers(0, 2, (40, L.D)).astype(np.uint8)
    W = rng.integers(0, 2, (40, L.D)).astype(np.uint8)
    okf = True
    for R in range(24):
        BU = (U @ Bs[R].T) % 2
        BW = (W @ Bs[R].T) % 2
        # rotation by R maps T_t to T_{Rt}; compare multisets of form values over all shifts
        f1 = L.forms_batch(U, W)
        f2 = L.forms_batch(BU.astype(np.uint8), BW.astype(np.uint8))
        perm = [L.SHIFTS.index(tuple(int(v) for v in L.O[R] @ np.array(t))) for t in L.SHIFTS]
        okf &= np.array_equal(f1, f2[:, perm])
    check(f'{action}: B_R preserves <u, T_t w> (with t -> R t), 40 random pairs', okf)

homs = L.all_homs()
check('exhaustive: 58 homomorphisms O -> O', len(homs) == 58)
classes = {}
for h in homs:
    classes.setdefault(L.conj_class_of_hom(h), []).append(h)
check('exactly 5 conjugacy classes of homomorphisms', len(classes) == 5)
sizes = sorted(len(c) for c in classes.values())
check('class sizes 1,3,6,24,24', sizes == [1, 3, 6, 24, 24])
menu_cls = {}
for a in ('trivial', 'sign', 'axis', 'full'):
    h = tuple(L.menu_hom(a))
    menu_cls[a] = [i for i, c in enumerate(classes) if h in c][0]
check('menu actions lie in 4 distinct classes', len(set(menu_cls.values())) == 4)
extra = [i for i in range(5) if i not in menu_cls.values()]
c_extra = list(classes)[extra[0]]
h_extra = min(c_extra)
img = sorted(set(h_extra))
ker = sum(1 for g in range(24) if h_extra[g] == L.ID)
check('fifth class: kernel A4 (order 12), image C2', ker == 12 and len(img) == 2)
nonid = [g for g in img if g != L.ID][0]
Mi = L.O[nonid]
# a face-diagonal half turn has trace -1 and its axis is a face diagonal (two nonzero entries)
check('fifth class image is a face-diagonal half turn (trace -1, not diagonal)',
      int(np.trace(Mi)) == -1 and np.count_nonzero(Mi - np.diag(np.diag(Mi))) > 0)
# canonical representative of sign-f used downstream: R -> I if s(R)=1 else Hf, Hf = half turn about (0,1,1)
Hf = L.G([[-1, 0, 0], [0, 0, 1], [0, 1, 0]])
hsf = tuple(L.ID if L.perm_sign(L.O[R]) == 1 else Hf for R in range(24))
check('sign-f canonical rep (R -> half turn about (0,1,1) on odd R) is a hom in the fifth class',
      L.is_hom(hsf) and hsf in c_extra)
for a in ('trivial', 'sign', 'axis', 'full'):
    h = L.menu_hom(a)
    ker = sum(1 for g in range(24) if h[g] == L.ID)
    exp = {'trivial': 24, 'sign': 12, 'axis': 4, 'full': 1}[a]
    check(f'{a}: kernel order {exp} (as in the 2026-09-22 menu note)', ker == exp)
print(f'TOTAL: PASS={P} FAIL={F}')
