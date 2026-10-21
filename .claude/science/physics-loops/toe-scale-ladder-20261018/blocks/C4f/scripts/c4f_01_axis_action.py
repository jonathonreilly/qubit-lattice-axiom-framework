#!/usr/bin/env python3
"""C4f step 1-2: how the axis soldering action acts on magnon sectors, and which pair moves are
symmetry-allowed (monomial, Observation-M style) at range r = 1, 2, 3.

Part A (exact up to float roundoff, 1e-12): for all 24 R in O with Q(R) = sgn(perm R)|R| (C4 c4lib
convention), build the SU(2) lift D_R and write it in the n-basis (|+n> = magnon, |-n> = vacuum spin).
  * R in T (even permutation part): D_R diagonal  => beta_R = phase(N) * P_R  on the N-magnon sector
  * R odd: D_R antidiagonal                        => beta_R = phase(N) * P_R o C (C = global flip)
  * phase(N) is a U(1) rotation e^{i theta N} (times a global constant): checked by writing
    D_R = e^{i a} diag(e^{i th/2}, e^{-i th/2}) X^{odd}.
Part B (exact, integer): monomial pair-move classification.  For G in {T, O-perm}, pair c = {0, rho},
0 < |rho|_inf <= r; images c' a near pair with all four cross distances <= r (C4c Lemma K)
and fixed by Stab(c) in G x| Z^3 (the exact C4c c4c_01 criterion, extended to r = 3).  Report the number of relative-position orbits
admitting a COM-changing image.  Under the AXIS action the 2-magnon sector is only T-covariant
(odd R map it to the 2-hole sector), so the T column is the relevant one; the O-perm column is the
full-action / pure-permutation case of C4c Observation M.
"""
import itertools, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c4f_core import build_O, perm_sign

P = F = 0
def check(name, ok):
    global P, F
    if ok: P += 1; print('PASS', name)
    else: F += 1; print('FAIL', name)

SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex); SIG = [SX, SY, SZ]; I2 = np.eye(2)

def su2_lift(Qm):
    Qm = np.array(Qm, float); tr = np.trace(Qm)
    ang = np.arccos(np.clip((tr - 1) / 2, -1, 1))
    if abs(ang) < 1e-9: return I2.astype(complex)
    if abs(ang - np.pi) < 1e-9:
        Mx = (Qm + np.eye(3)) / 2; k = int(np.argmax(np.diag(Mx))); n = Mx[:, k] / np.sqrt(Mx[k, k])
    else:
        n = np.array([Qm[2, 1] - Qm[1, 2], Qm[0, 2] - Qm[2, 0], Qm[1, 0] - Qm[0, 1]]) / (2 * np.sin(ang))
    return np.cos(ang / 2) * I2 - 1j * np.sin(ang / 2) * sum(n[i] * SIG[i] for i in range(3))

O = build_O()
check('O has 24 elements', len(O) == 24)
odd = [i for i, M in enumerate(O) if perm_sign(M) == -1]
Tset = [i for i, M in enumerate(O) if perm_sign(M) == 1]
check('12 even (T) + 12 odd elements', len(odd) == 12 and len(Tset) == 12)
# T = signed even perms with even number of sign flips: check
check('even-perm elements have an even number of -1 entries (T)', all(int((O[i] < 0).sum()) % 2 == 0 for i in Tset))

nvec = np.ones(3) / np.sqrt(3)
nsig = sum(nvec[i] * SIG[i] for i in range(3))
w, V = np.linalg.eigh(nsig)            # eigenvalues -1, +1
vac, mag = V[:, 0], V[:, 1]            # |-n> vacuum spin, |+n> magnon
Bn = np.column_stack([mag, vac])       # n-basis: index 0 = magnon, 1 = vacuum spin
okA = True; okB = True; okS = True; okhom = True
for i, M in enumerate(O):
    Qm = perm_sign(M) * np.abs(M)
    D = su2_lift(Qm)
    okS &= np.allclose(D @ SIG[0] @ D.conj().T, sum(Qm[b, 0] * SIG[b] for b in range(3)))
    Dn = Bn.conj().T @ D @ Bn
    if i in Tset:
        okA &= abs(Dn[0, 1]) < 1e-12 and abs(Dn[1, 0]) < 1e-12
        # Q(R) n = n
        okhom &= np.allclose(Qm @ nvec, nvec)
    else:
        okB &= abs(Dn[0, 0]) < 1e-12 and abs(Dn[1, 1]) < 1e-12
        okhom &= np.allclose(Qm @ nvec, -nvec)
check('SU(2) lifts implement Q(R) (24 R)', okS)
check('Q(R) n = +n for R in T, = -n for odd R', okhom)
check('R in T: D_R diagonal in n-basis -> beta_R = e^{i th N} P_R on N-magnon sectors', okA)
check('R odd: D_R antidiagonal in n-basis -> beta_R = (U(1) phase) o P_R o C (C = global flip)', okB)

# ------------------------------------------------------------------ Part B
def canon_pair(a, b):
    return tuple(sorted((tuple(int(v) for v in a), tuple(int(v) for v in b))))

def cheb(a, b): return int(np.abs(np.asarray(a) - np.asarray(b)).max())

def stab_c(c, G):
    """space-group elements (R,t), R in G, with R c + t = c setwise (as in C4c c4c_01)."""
    out = []; a, b = [np.array(p) for p in c]
    for M in G:
        for (u, v) in ((a, b), (b, a)):
            t = u - M @ a
            if np.array_equal(M @ b + t, v): out.append((M, t))
    return out

def classify(Gname, r):
    """C4c Observation-M criterion, extended in r: c' a near pair (0 < |rho'| <= r), c' ~ c
    (all four cross Chebyshev distances <= r, Lemma K), c' fixed by Stab(c), COM(c') != COM(c)."""
    G = [O[i] for i in (Tset if Gname == 'T' else range(24))]
    reps = []
    for rho in itertools.product(range(-r, r + 1), repeat=3):
        if rho == (0, 0, 0): continue
        if [v for v in rho if v][0] > 0: reps.append(rho)
    free = []
    for rho in reps:
        c = canon_pair((0, 0, 0), rho); St = stab_c(c, G); a, b = c
        loc = [p for p in itertools.product(range(-r, 2 * r + 1), repeat=3)
               if cheb(p, a) <= r and cheb(p, b) <= r]
        mov = []
        for p, q in itertools.combinations(loc, 2):
            if not (0 < cheb(p, q) <= r): continue
            cc = canon_pair(p, q)
            if all(canon_pair(M @ np.array(cc[0]) + t, M @ np.array(cc[1]) + t) == cc for M, t in St):
                if not np.array_equal(np.add(cc[0], cc[1]), np.add(a, b)): mov.append(cc)
        if mov: free.append((rho, len(St), mov))
    return reps, free

summary = {}
for r in (1, 2, 3):
    for Gname in ('T', 'O'):
        reps, free = classify(Gname, r)
        summary[(Gname, r)] = (len(reps), len(free))
        print(f'r={r} G={Gname}: {len(free)} of {len(reps)} near relative positions admit a '
              f'Stab-fixed, Lemma-K-related, COM-changing monomial image')
        if r <= 2:
            for rho, ns, mov in free:
                dc = sorted(set(tuple(int(v) for v in np.add(m[0], m[1]) - np.array(rho)) for m in mov))
                print(f'    rho={rho} |Stab|={ns} 2*dCOM options={dc}')
# Regression to C4c Observation M (its logs: r=1 T: 6 face positions, O: none; r=2: 56/62 T, 36/62 O)
check('regression Obs. M r=1 O: no exceptions', summary[('O', 1)][1] == 0)
check('regression Obs. M r=1 T: 6 exceptions', summary[('T', 1)][1] == 6)
check('regression Obs. M r=2: 56/62 (T), 36/62 (O)', summary[('T', 2)] == (62, 56) and summary[('O', 2)] == (62, 36))
print(f'TOTAL: PASS={P} FAIL={F}')
