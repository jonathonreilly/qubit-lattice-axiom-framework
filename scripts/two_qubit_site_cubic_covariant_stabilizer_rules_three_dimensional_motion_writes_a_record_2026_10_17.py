#!/usr/bin/env python3
"""Two qubits per site, spin soldered: cubic-covariant nearest-neighbour Pauli stabilizer rules.

Site = spin qubit (soldered, full action) (x) flavour qubit (fixed, or also soldered). A rule is a
signed set of two-qubit-per-site Pauli strings on the seven-site star of the origin, closed under
the proper cubic group O; translates generate an abelian stabilizer group without -1.

The runner
1. enumerates all 16^7 - 1 star strings (vectorized) and keeps those commuting with every
   translate of every rotated image, for flavour fixed and for flavour soldered;
2. groups them into sign-consistent O-orbits and finds the maximal mutually commuting sets;
3. checks the structure that the theorem uses:
   - flavour fixed: three sets in which every spin part is Chamon C or identity and every
     flavour factor is one label P; six sets {C, K, C K} with K a flavour cluster string;
   - flavour soldered: one set whose strings use only the Bell labels {II, XX, YY, ZZ}; the set
     {C_s, C_f, C_s C_f}; and the set {E-orbit, B} with B = C_s C_f in Bell labels;
4. checks the lemma ingredients exactly (Chamon curve primes, the Bell commutant, the O action
   on Bell labels);
5. checks the example "spin Chamon (x) flavour X on the six neighbours": its charge ideal is
   ((x+1)^2, (y+1)^2, (z+1)^2) over GF(2), 8 charge types moving by any even translation, and no
   spin-only operator moves a charge;
6. if Singular is available (SINGULAR_BIN or `Singular` on PATH), computes Ext^3(C, R) for the
   two E-family rules (no 3D-mobile charge). Otherwise these two checks are reported as skipped.
"""

from __future__ import annotations

import itertools
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1  # noqa: E402

AUDIT_TIMEOUT_SEC = 2400
AUDIT_INPUT_PATHS = (
    'docs/TWO_QUBIT_SITE_CUBIC_COVARIANT_STABILIZER_RULES_THREE_DIMENSIONAL_DEFECT_MOTION_WRITES_A_LOCAL_RECORD_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/ONE_QUBIT_CUBIC_COVARIANT_NEAREST_NEIGHBOUR_STABILIZER_RULES_HAVE_NO_THREE_DIMENSIONALLY_MOBILE_DEFECT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
)

O, STAR, SIDX = c1.O, c1.STAR, c1.SIDX
L4 = 'IXYZ'
CH = (0, 1, 1, 2, 2, 3, 3)          # Chamon spin labels on the star


def sp1(a, b):
    return int(a != 0 and b != 0 and a != b)


SP = np.array([[sp1(l1 >> 2, l2 >> 2) ^ sp1(l1 & 3, l2 & 3) for l2 in range(16)] for l1 in range(16)], np.uint8)


def labmap(Qm):
    m, sg = np.zeros(4, int), np.ones(4, int)
    for a in (1, 2, 3):
        col = Qm[:, a - 1]
        b = int(np.nonzero(col)[0][0])
        m[a], sg[a] = b + 1, int(col[b])
    return m, sg


def tables(faction):
    RT = []
    for M in O:
        pos = [SIDX[tuple(int(v) for v in M @ np.array(p))] for p in STAR]
        (ms, ss), (mf, sf) = labmap(c1.Q(M, 'full')), labmap(c1.Q(M, faction))
        lm = np.array([4 * ms[l >> 2] + mf[l & 3] for l in range(16)], np.uint32)
        lsg = np.array([ss[l >> 2] * sf[l & 3] for l in range(16)], np.int8)
        RT.append((pos, lm, lsg))
    return RT


SH = []
for _s in itertools.product(range(-2, 3), repeat=3):
    _pr = [(i, j) for i in range(7) for j in range(7) if tuple(np.subtract(STAR[i], STAR[j])) == _s]
    if _pr:
        SH.append(_pr)


def nib(a, i):
    return (a >> (4 * i)) & 15


def transform(RT, a, k):
    pos, lm, lsg = RT[k]
    out, sg = np.zeros_like(a), np.ones(a.shape, np.int8)
    for i in range(7):
        nb = nib(a, i)
        out |= lm[nb] << (4 * pos[i])
        sg *= lsg[nb]
    return out, sg


def commutes_all(a, b):
    ok = np.ones(a.shape, bool)
    for pr in SH:
        par = np.zeros(a.shape, np.uint8)
        for i, j in pr:
            par ^= SP[nib(a, i), nib(b, j)]
        ok &= par == 0
    return ok


def enumerate_rules(faction):
    RT = tables(faction)
    N, CHK, surv = 16 ** 7, 1 << 22, []
    for start in range(0, N, CHK):
        a = np.arange(start, min(N, start + CHK), dtype=np.uint32)
        if start == 0:
            a = a[1:]
        a = a[commutes_all(a, a)]
        for k in range(1, 24):
            if a.size == 0:
                break
            a = a[commutes_all(a, transform(RT, a, k)[0])]
        surv.append(a)
    S = np.unique(np.concatenate(surv))
    T = np.stack([transform(RT, S, k)[0] for k in range(24)])
    reps = np.unique(T.min(axis=0))
    TR = np.stack([transform(RT, reps, k)[0] for k in range(24)])
    GR = np.stack([transform(RT, reps, k)[1] for k in range(24)])
    cons = np.ones(reps.size, bool)
    for k in range(24):
        for l in range(k + 1, 24):
            cons &= (TR[k] != TR[l]) | (GR[k] == GR[l])
    reps, TR = reps[cons], TR[:, cons]
    elems = [np.unique(TR[:, i]) for i in range(reps.size)]
    allel = np.concatenate(elems)
    owner = np.concatenate([np.full(e.size, i) for i, e in enumerate(elems)])
    adj = {i: set() for i in range(reps.size)}
    for i in range(reps.size):
        bad = set(owner[~commutes_all(np.full(allel.shape, reps[i], np.uint32), allel)].tolist())
        adj[i] = {j for j in range(reps.size) if j != i and j not in bad}
    return S.size, reps, elems, adj, c1.maximal_cliques(reps.size, adj)


def dec(a):
    return [((int(a) >> (4 * i)) & 15) for i in range(7)]


def show(a):
    return ' '.join(L4[l >> 2] + L4[l & 3] for l in dec(a))


def code(labels):
    return sum(int(l) << (4 * i) for i, l in enumerate(labels))


def pauli_mul(a, b):
    """Two-qubit Paulis as label pairs (s, f); returns product label pair ignoring phase."""
    xs = lambda l: {0: (0, 0), 1: (1, 0), 2: (1, 1), 3: (0, 1)}[l]
    inv = {(0, 0): 0, (1, 0): 1, (1, 1): 2, (0, 1): 3}
    return tuple(inv[tuple(u ^ v for u, v in zip(xs(p), xs(q)))] for p, q in zip(a, b))


def singular_bin():
    b = os.environ.get('SINGULAR_BIN') or shutil.which('Singular')
    return b


def ext3_script(gens):
    """gens: list of 7-tuples of 16-labels; charge module and Ext^3 support (see the C2 note)."""
    q, k = 2, len(gens)
    sym = {0: (0, 0), 1: (1, 0), 2: (1, 1), 3: (0, 1)}

    def mono(p):
        e = [p[i] + 2 for i in range(3)]
        return '*'.join(f'{v}^{n}' for v, n in zip('xyz', e) if n) or '1'

    G = [[[] for _ in range(k)] for _ in range(2 * q)]
    S = [[[] for _ in range(2 * q)] for _ in range(k)]
    for j, g in enumerate(gens):
        for i, l in enumerate(g):
            p = STAR[i]
            for a, lab in enumerate((l >> 2, l & 3)):
                xb, zb = sym[lab]
                if xb:
                    G[a][j].append(mono(p))
                    S[j][q + a].append(mono(tuple(-c for c in p)))
                if zb:
                    G[q + a][j].append(mono(p))
                    S[j][a].append(mono(tuple(-c for c in p)))
    f = lambda t: '+'.join(t) if t else '0'
    Gs = ',\n'.join(f(G[r][c]) for r in range(2 * q) for c in range(k))
    Ss = ',\n'.join(f(S[r][c]) for r in range(k) for c in range(2 * q))
    return f'''LIB "homolog.lib"; LIB "elim.lib";
ring r=2,(x,y,z),dp;
matrix Gm[{2*q}][{k}] = {Gs};
matrix Sm[{k}][{2*q}] = {Ss};
module imS = Sm;
module syzG = simplify(syz(module(Gm)), 2);
int nrel = size(syzG);
module N;
if (nrel == 0) {{ N = freemodule({k}); }}
else {{
  matrix Cm = matrix(syzG); int D = 12; matrix Cb[{k}][nrel]; int i; int j;
  for (i=1;i<={k};i++) {{ for (j=1;j<=nrel;j++) {{ poly f = Cm[i,j]; poly g = 0;
     while (f != 0) {{ intvec e = leadexp(f); g = g + leadcoef(f)*x^(D-e[1])*y^(D-e[2])*z^(D-e[3]); f = f - lead(f); }}
     Cb[i,j] = g; }} }}
  N = syz(module(transpose(Cb)));
}}
module Cpres = modulo(N, imS);
def E3 = Ext_R(3, Cpres);
ideal annE = sat(std(Ann(std(E3))), x*y*z);
print("RESULT " + string(annE[1] != 1));
quit;
'''


def main() -> int:
    ck = c1.Checks()
    x, y, z = sp.symbols('x y z')

    # ---------------- flavour fixed
    n_ft, reps, elems, adj, cl = enumerate_rules('trivial')
    print(f'flavour fixed: {n_ft} strings, {reps.size} sign-consistent orbits, maximal sets {sorted(len(c) for c in cl)}')
    ck.check('flavour fixed: 775 strings commute with all rotated translates; 127 sign-consistent orbits; 9 maximal commuting sets (3 of 39, 6 of 3)',
             n_ft == 775 and reps.size == 127 and sorted(len(c) for c in cl) == [3] * 6 + [39] * 3)
    spin_ok = all(all((l >> 2) == 0 for l in dec(e)) or all((l >> 2) == CH[i] for i, l in enumerate(dec(e)))
                  for e in np.concatenate(elems))
    ck.check('flavour fixed: every string has spin part Chamon C or identity', spin_ok)
    big = [c for c in cl if len(c) == 39]
    ck.check('flavour fixed, large sets: every flavour factor in a set is one label P (one set for each of X, Y, Z)',
             sorted(tuple(sorted(set(l & 3 for k in c for e in elems[k] for l in dec(e)) - {0})) for c in big) == [(1,), (2,), (3,)])
    small = [c for c in cl if len(c) == 3]
    okK = True
    for c in small:
        strs = [dec(elems[k][0]) for k in c]
        Cs = [s for s in strs if all((l & 3) == 0 for l in s)]
        Ks = [s for s in strs if all((l >> 2) == 0 for l in s)]
        rest = [s for s in strs if s not in Cs and s not in Ks]
        okK &= (len(Cs) == len(Ks) == len(rest) == 1 and all(len(elems[k]) == 1 for k in c)
                and Ks[0][0] != 0 and len(set(Ks[0][1:])) == 1 and Ks[0][1] not in (0, Ks[0][0])
                and tuple(pauli_mul(((Cs[0][i] >> 2), 0), (0, Ks[0][i] & 3)) for i in range(7))
                == tuple(((l >> 2), (l & 3)) for l in rest[0]))
    ck.check('flavour fixed, small sets: each is {C (x) 1, K, C K} with K a flavour cluster string (P at centre, Q != P on all six neighbours)', okK)

    # ---------------- flavour soldered
    n_ff, reps2, elems2, adj2, cl2 = enumerate_rules('full')
    print(f'flavour soldered: {n_ff} strings, {reps2.size} sign-consistent orbits, maximal sets {sorted(len(c) for c in cl2)}')
    ck.check('flavour soldered: 16387 strings; 858 sign-consistent orbits; maximal commuting sets of sizes 2, 3 and 855',
             n_ff == 16387 and reps2.size == 858 and sorted(len(c) for c in cl2) == [2, 3, 855])
    BELL = {0, 5, 10, 15}
    bigset = next(c for c in cl2 if len(c) == 855)
    ck.check('flavour soldered: every string in the 855-orbit set uses only Bell labels {II, XX, YY, ZZ}',
             all(set(dec(e)) <= BELL for k in bigset for e in elems2[k]))
    Cs = code([4 * l for l in CH])
    Cf = code(list(CH))
    Bc = code([5 * l for l in CH])
    s3 = next(c for c in cl2 if len(c) == 3)
    ck.check('flavour soldered: the 3-orbit set is {spin Chamon, flavour Chamon, their product B (XX, YY, ZZ on the axis pairs)}',
             {int(elems2[k][0]) for k in s3} == {Cs, Cf, Bc})
    s2 = next(c for c in cl2 if len(c) == 2)
    Eorb = [k for k in s2 if int(elems2[k][0]) != Bc]
    Estrs = [dec(e) for e in elems2[Eorb[0]]] if Eorb else []
    E_expected = {code([0, 11, 11, 13, 13, 6, 6]), code([0, 14, 14, 7, 7, 9, 9])}   # YZ ZX XY and ZY XZ YX (label 4 s + f)
    ck.check('flavour soldered: the 2-orbit set is {E-orbit, B}, E = YZ(+-x) ZX(+-y) XY(+-z) and its partner ZY XZ YX; E E\' = B up to phase',
             len(Eorb) == 1 and {code(s) for s in Estrs} == E_expected
             and all(4 * pr[0] + pr[1] == bl for pr, bl in zip((pauli_mul(((l >> 2), (l & 3)), ((m >> 2), (m & 3))) for l, m in zip(*Estrs)), dec(Bc))))

    # ---------------- lemma ingredients
    gens = [x, y, z]
    primes = [([y * z + 1, x + y], (1, 1, -1)), ([y * z + 1, x + z], (1, -1, 1)), ([x * z + 1, y + z], (1, -1, -1)), ([y + z, x + z], (1, 1, 1))]
    box = [tv for tv in itertools.product(range(-2, 3), repeat=3) if any(tv)]
    okp = True
    for P, d in primes:
        GP = sp.groebner(P, *gens, modulus=2, order='grevlex')
        for tv in box:
            inP = GP.reduce(sp.expand(x ** (tv[0] + 2) * y ** (tv[1] + 2) * z ** (tv[2] + 2) + x ** 2 * y ** 2 * z ** 2))[1] == 0
            okp &= inP == (sum(a * b for a, b in zip(tv, d)) == 0)
    ck.check('Chamon curve primes: x^t + 1 lies in the prime of diagonal d exactly when t is orthogonal to d '
             '(so no Chamon charge is fixed by three independent translations)', okp)
    two = [(a, b) for a in range(4) for b in range(4)]
    comm = [p for p in two if not (sp1(p[0], 1) ^ sp1(p[1], 1)) and not (sp1(p[0], 3) ^ sp1(p[1], 3))]
    ck.check('the commutant of {XX, ZZ} in the two-qubit Pauli group is the Bell alphabet {II, XX, YY, ZZ}',
             set(comm) == {(0, 0), (1, 1), (2, 2), (3, 3)})
    RT = tables('full')
    orbit_xx = {int(transform(RT, np.array([5], np.uint32), k)[0][0]) for k in range(24)}
    ck.check('with both qubits soldered, O permutes XX, YY, ZZ transitively (all or none of them lie in an O-invariant group)',
             orbit_xx == {5, 10, 15})

    # ---------------- example
    sX = y + 1 / y + z + 1 / z
    sZ = x + 1 / x + y + 1 / y
    d6 = x + 1 / x + y + 1 / y + z + 1 / z
    pol = [sp.expand(x * y * z * f) for f in (sX, sZ, d6)]
    t = sp.Symbol('t')
    GJ = sp.groebner(pol + [t * x * y * z + 1], t, *gens, modulus=2, order='lex')     # saturation by xyz
    J = sp.groebner([g for g in GJ.exprs if not g.has(t)], *gens, modulus=2, order='grevlex')
    ck.check('example "spin Chamon (x) flavour X on six neighbours": charge ideal (Laurent) = ((x+1)^2, (y+1)^2, (z+1)^2) over GF(2)',
             set(J.exprs) == set(sp.groebner([x ** 2 + 1, y ** 2 + 1, z ** 2 + 1], *gens, modulus=2, order='grevlex').exprs))
    std = [m for m in itertools.product(range(2), repeat=3)]
    ck.check('example: the charge module has F2-dimension 8 (standard monomials x^a y^b z^c, a, b, c in {0, 1}), supported only at (1, 1, 1)',
             all(J.reduce(x ** a * y ** b * z ** c)[1] == x ** a * y ** b * z ** c for a, b, c in std) and len(std) == 8)
    ck.check('example: every charge moves by (2,0,0), (0,2,0), (0,0,2) (3D-mobile), but not by (1,0,0)',
             all(J.reduce(v ** 2 + 1)[1] == 0 for v in gens) and J.reduce(x + 1)[1] != 0)
    GI = sp.groebner([sp.expand((y + z) * (1 + y * z)), sp.expand((x + y) * (1 + x * y)), sp.expand((x + z) * (1 + x * z))], *gens, modulus=2, order='grevlex')
    ck.check('example: spin-only operators cannot move a charge by (2,0,0) (x^2 + 1 is not in the Chamon ideal), so the move must flip flavour X',
             GI.reduce(x ** 2 + 1)[1] != 0)

    # ---------------- E family via Singular
    bin_ = singular_bin()
    E1, E2 = sorted(Estrs) if len(Estrs) == 2 else ([0] * 7, [0] * 7)
    if bin_:
        for name, g in (('<E, E\'>', [E1, E2]), ('<E, E\', B>', [E1, E2, dec(Bc)])):
            with tempfile.NamedTemporaryFile('w', suffix='.sing', delete=False) as fh:
                fh.write(ext3_script(g))
            out = subprocess.run([bin_, '-q', fh.name], stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=1200).stdout
            ck.check(f'E family {name}: Ext^3(C, R) has empty support off the coordinate planes (no 3D-mobile charge; GF(2), Singular)',
                     'RESULT 0' in out)
    else:
        print('SKIP E-family Ext^3 checks: Singular not found (set SINGULAR_BIN). Certificates are in the loop pack, c2_two_qubit_site/.')

    print('per_element: exhaustive enumeration of 16^7 strings per flavour action; exact GF(2) algebra')
    print('per_site: two qubits per site; no dynamics or tick is supplied')
    print('per_mode: not applicable')
    print('per_block: not applicable')
    print('lattice_wide: charge modules over the Laurent ring (infinite lattice)')
    print(f"TOTAL: PASS={ck.passed} FAIL={ck.failed}")
    return 0 if ck.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
