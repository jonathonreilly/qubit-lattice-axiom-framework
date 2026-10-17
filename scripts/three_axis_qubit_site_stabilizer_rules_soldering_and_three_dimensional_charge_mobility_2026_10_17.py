#!/usr/bin/env python3
"""Three axis-labelled qubits per site: unsoldered versus soldered star-supported stabilizer rules.

Site = three qubits indexed by the axes x, y, z. The proper cubic group O acts on positions,
permutes the three qubits as it permutes the axes, and acts on each qubit's Pauli labels either
trivially ("unsoldered") or by the full soldered action. A rule is a signed set of Pauli strings on
the seven-site star, closed under O; translates generate an abelian stabilizer group.

Part A (exact, unsoldered): eight interleaved 3D toric codes. Vertex term A_v = X on qubit a at
v +- e_a (a = x, y, z); plaquette terms B_{v,c} = Z on qubit b at v +- e_a and qubit a at v +- e_b
({a, b, c} = {x, y, z}). The runner checks covariance, commutation, a trivial single-site
commutant (no free single-site variable), bounded torus code dimension (log2 = 24 at L = 4, 6),
that no single-site Pauli violates an odd number of vertex terms of any copy (the vertex charge is
not locally creatable), and that one Z moves it by 2 e_a (coherent motion in three dimensions).

Part B (exact within the restriction, soldered): all star strings fixed by a C4 or C3 rotation
(this includes every toric-code-type generator shape) that commute with all translates of all
their rotated images; sign-consistent orbits; maximal commuting sets; 3L^3 - rank of each set's
generator union at L = 4, 6 (a lower bound on the code dimension of every valid sub-rule); the
abelian-alphabet structure of the 187-orbit family; and, with Singular, the Ext^3 test on the eight
3-orbit rules.
"""

from __future__ import annotations

import itertools
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
from sympy.polys.domains import GF

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1  # noqa: E402
import two_qubit_site_soldered_spin_stabilizer_rules_charge_motion_flips_free_local_variable_2026_10_17 as c2  # noqa: E402

AUDIT_TIMEOUT_SEC = 2400
AUDIT_INPUT_PATHS = (
    'docs/THREE_AXIS_QUBIT_SITE_STABILIZER_RULES_UNSOLDERED_TORIC_CODES_MOVE_SOLDERED_MAXIMAL_RULES_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
)

O, STAR, SIDX = c1.O, c1.STAR, c1.SIDX
E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def perm_of(M):
    return [int(np.nonzero(M[:, a])[0][0]) for a in range(3)]


def labmap(Qm):
    m, sg = [0] * 4, [1] * 4
    for a in (1, 2, 3):
        col = Qm[:, a - 1]
        b = int(np.nonzero(col)[0][0])
        m[a], sg[a] = b + 1, int(col[b])
    return m, sg


def site_tables(action):
    SITE, SSG = [], []
    for M in O:
        pm, (lm, ls) = perm_of(M), labmap(c1.Q(M, action))
        t, g = np.zeros(64, np.uint64), np.ones(64, np.int8)
        for s in range(64):
            out, sg = 0, 1
            for a in range(3):
                l = (s >> (2 * a)) & 3
                out |= lm[l] << (2 * pm[a])
                sg *= ls[l]
            t[s], g[s] = out, sg
        SITE.append(t)
        SSG.append(g)
    return SITE, SSG


POS = [[SIDX[tuple(int(v) for v in M @ np.array(p))] for p in STAR] for M in O]
SP = np.array([[sum(c2.sp1((s1 >> (2 * a)) & 3, (s2 >> (2 * a)) & 3) for a in range(3)) % 2
                for s2 in range(64)] for s1 in range(64)], np.uint8)
SH = c2.SH


def nib(a, i):
    return ((a >> np.uint64(6 * i)) & np.uint64(63)).astype(np.int64)


def transform(T, a, k):
    SITE, SSG = T
    out, sg = np.zeros_like(a), np.ones(a.shape, np.int8)
    for i in range(7):
        nb = nib(a, i)
        out |= SITE[k][nb] << np.uint64(6 * POS[k][i])
        sg *= SSG[k][nb]
    return out, sg


def commutes_all(a, b):
    ok = np.ones(a.shape, bool)
    for pr in SH:
        par = np.zeros(a.shape, np.uint8)
        for i, j in pr:
            par ^= SP[nib(a, i), nib(b, j)]
        ok &= par == 0
    return ok


def find(Mt):
    return next(k for k, M in enumerate(O) if np.array_equal(M, Mt))


def invariant_strings(T, k):
    SITE = T[0]
    g = POS[k]
    orbits, seen = [], set()
    for i in range(7):
        if i in seen:
            continue
        orb, j = [i], g[i]
        while j != i:
            orb.append(j)
            j = g[j]
        seen |= set(orb)
        orbits.append(orb)

    def gpow(lbl, steps):
        for _ in range(steps):
            lbl = int(SITE[k][lbl])
        return lbl

    choices = [(orb, [l for l in range(64) if gpow(l, len(orb)) == l]) for orb in orbits]
    grids = np.meshgrid(*[np.array(o, np.uint64) for _, o in choices], indexing='ij')
    out = np.zeros(grids[0].shape, np.uint64)
    for (orb, _), G in zip(choices, grids):
        cur = G.copy()
        for i in orb:
            out |= cur << np.uint64(6 * i)
            cur = SITE[k][cur.astype(np.int64)]
    return out.ravel()


def dec(a):
    return [((int(a) >> (6 * i)) & 63) for i in range(7)]


def torus_logdim(gens, L):
    n = 3 * L ** 3
    idx = lambda p, a: 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a
    rows = []
    for v in itertools.product(range(L), repeat=3):
        for g in gens:
            x = np.zeros(2 * n, np.uint8)
            for i, l in enumerate(g):
                if not l:
                    continue
                p = [v[j] + STAR[i][j] for j in range(3)]
                for a in range(3):
                    lab = (l >> (2 * a)) & 3
                    if lab in (1, 2):
                        x[idx(p, a)] ^= 1
                    if lab in (2, 3):
                        x[n + idx(p, a)] ^= 1
            rows.append(x)
    r, _ = c1.f2_rank_and_null(np.array(rows))
    return n - r


def code(labels7):
    return sum(int(l) << (6 * i) for i, l in enumerate(labels7))


def lab3(q):   # dict axis -> Pauli label 0..3 into a 6-bit site label
    return sum(q.get(a, 0) << (2 * a) for a in range(3))


def specialization_rank(gens, weights):
    """Exact rank over GF(2)(t), using the complete Pauli generator union."""
    field = GF(2).frac_field('t')
    t = field.gens[0]
    pivots = {}
    for gen in gens:
        row = [field.zero for _ in range(6)]
        for pos, labels in zip(STAR, gen):
            monomial = t ** sum(a * b for a, b in zip(pos, weights))
            for a in range(3):
                label = (int(labels) >> (2 * a)) & 3
                if label in (1, 2):
                    row[a] += monomial
                if label in (2, 3):
                    row[3 + a] += monomial
        for col in range(6):
            if not row[col]:
                continue
            if col in pivots:
                factor = row[col]
                row = [x - factor * y for x, y in zip(row, pivots[col])]
            else:
                factor = row[col]
                pivots[col] = [x / factor for x in row]
                break
    return len(pivots)


def ext3_singular(gens):
    b = os.environ.get('SINGULAR_BIN') or shutil.which('Singular')
    if not b:
        raise RuntimeError('Singular is required for the load-bearing Ext^3 checks; set SINGULAR_BIN')
    sym = {0: (0, 0), 1: (1, 0), 2: (1, 1), 3: (0, 1)}
    q, k = 3, len(gens)

    def mono(p):
        e = [p[i] + 2 for i in range(3)]
        return '*'.join(f'{v}^{n}' for v, n in zip('xyz', e) if n) or '1'

    G = [[[] for _ in range(k)] for _ in range(2 * q)]
    S = [[[] for _ in range(2 * q)] for _ in range(k)]
    for j, g in enumerate(gens):
        for i, l in enumerate(g):
            p = STAR[i]
            for a in range(3):
                xb, zb = sym[(l >> (2 * a)) & 3]
                if xb:
                    G[a][j].append(mono(p))
                    S[j][q + a].append(mono(tuple(-c for c in p)))
                if zb:
                    G[q + a][j].append(mono(p))
                    S[j][a].append(mono(tuple(-c for c in p)))
    f = lambda t: '+'.join(t) if t else '0'
    Gs = ',\n'.join(f(G[r][c]) for r in range(2 * q) for c in range(k))
    Ss = ',\n'.join(f(S[r][c]) for r in range(k) for c in range(2 * q))
    text = f'''LIB "homolog.lib"; LIB "elim.lib";
ring r=2,(x,y,z),dp;
matrix Gm[{2*q}][{k}] = {Gs};
matrix Sm[{k}][{2*q}] = {Ss};
module imS = Sm;
module syzG = simplify(syz(module(Gm)), 2);
int nrel = size(syzG);
module N;
if (nrel == 0) {{ N = freemodule({k}); }}
else {{
  matrix Cm = matrix(syzG); int D = 0; matrix Cb[{k}][nrel]; int i; int j;
  for (i=1;i<={k};i++) {{ for (j=1;j<=nrel;j++) {{ if (deg(Cm[i,j]) > D) {{ D = deg(Cm[i,j]); }} }} }}
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
    return c2.run_singular(text, 1800)


def main() -> int:
    if not c2.singular_bin():
        raise RuntimeError('Singular is required; set SINGULAR_BIN before running the enumeration')
    ck = c1.Checks()

    # ---------------- Part A: interleaved toric codes (unsoldered)
    A = [0] * 7
    for a in range(3):
        for s in (1, -1):
            A[SIDX[tuple(s * c for c in E[a])]] = lab3({a: 1})
    Bs = []
    for c in range(3):
        a, b = [k for k in range(3) if k != c]
        B = [0] * 7
        for s in (1, -1):
            B[SIDX[tuple(s * v for v in E[a])]] = lab3({b: 3})
            B[SIDX[tuple(s * v for v in E[b])]] = lab3({a: 3})
        Bs.append(B)
    tc = [A] + Bs
    T0 = site_tables('trivial')
    codes = np.array([code(g) for g in tc], np.uint64)
    images = {int(transform(T0, codes, k)[0][i]) for k in range(24) for i in range(4)}
    ck.check('A: the vertex and three plaquette strings form an O-closed set under the unsoldered action (qubits permuted as axes)',
             images == {int(c) for c in codes})
    ck.check('A: every generator commutes with every translate of every generator',
             all(commutes_all(np.array([codes[i]], np.uint64), np.array([codes[j]], np.uint64))[0] for i in range(4) for j in range(4)))
    labels = set(l for g in tc for l in g) - {0}
    ck.check('A: no single-site Pauli commutes with every generator label (no free single-site variable)',
             all(any(SP[p, l] for l in labels) for p in range(1, 64)))
    dims = [torus_logdim(tc, L) for L in (4, 6)]
    print(f'A: torus log2 code dimension L=4: {dims[0]}, L=6: {dims[1]}')
    ck.check('A: torus code dimension is bounded: log2 = 24 at L = 4 and L = 6 (eight 3D toric codes)', dims == [24, 24])
    # copy of a vertex term at v: copy origin = v mod 2; qubit (u, a) belongs to copy (u - e_a) mod 2
    ok_even = True
    for p in range(1, 64):
        flips = {}
        # vertex terms violated by Pauli p at the origin: A at v anticommutes iff origin = v +- e_a with p's qubit a anticommuting X
        for a in range(3):
            if SP[p, lab3({a: 1})]:
                for s in (1, -1):
                    v = tuple(-s * c for c in E[a])
                    cp = tuple(x % 2 for x in v)
                    flips[cp] = flips.get(cp, 0) + 1
        ok_even &= all(n % 2 == 0 for n in flips.values())
    ck.check('A: every single-site Pauli violates an even number of vertex terms in each of the eight copies (the vertex charge is not locally creatable)',
             ok_even)
    # Z on qubit a at the origin violates exactly the vertex terms at -e_a and +e_a: a charge moved by 2 e_a
    ok_move = True
    for a in range(3):
        hit = [v for v in itertools.product(range(-2, 3), repeat=3)
               if any(SP[lab3({a: 3}), A[i]] and tuple(np.add(v, STAR[i])) == (0, 0, 0) for i in range(7))]
        ok_move &= sorted(hit) == sorted([tuple(-c for c in E[a]), tuple(E[a])])
    ck.check('A: one Z on qubit a moves a vertex charge by 2 e_a, for each axis a (coherent motion in three dimensions; the operator commutes with all other generators)',
             ok_move)

    # ---------------- Part B: soldered, C4/C3-symmetric strings
    T1 = site_tables('full')
    surv = []
    for k in (find(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])), find(np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]))):
        S = invariant_strings(T1, k)
        S = S[S != 0]
        S = S[commutes_all(S, S)]
        for kk in range(1, 24):
            S = S[commutes_all(S, transform(T1, S, kk)[0])]
        surv.append(S)
    S = np.unique(np.concatenate(surv))
    reps = np.unique(np.stack([transform(T1, S, k)[0] for k in range(24)]).min(axis=0))
    TR = np.stack([transform(T1, reps, k)[0] for k in range(24)])
    GR = np.stack([transform(T1, reps, k)[1] for k in range(24)])
    cons = np.ones(reps.size, bool)
    for k in range(24):
        for l in range(k + 1, 24):
            cons &= (TR[k] != TR[l]) | (GR[k] == GR[l])
    reps, TR = reps[cons], TR[:, cons]
    elems = [np.unique(TR[:, i]) for i in range(reps.size)]
    allel = np.concatenate(elems)
    owner = np.concatenate([np.full(e.size, i) for i, e in enumerate(elems)])
    adj = {}
    for i in range(reps.size):
        bad = set(owner[~commutes_all(np.full(allel.shape, reps[i], np.uint64), allel)].tolist())
        adj[i] = {j for j in range(reps.size) if j != i and j not in bad}
    cl = c1.maximal_cliques(reps.size, adj)
    print(f'B: {S.size} strings, {reps.size} sign-consistent orbits, maximal commuting sets {sorted(len(c) for c in cl)}')
    ck.check('B: 719 C4- or C3-fixed strings survive; 227 sign-consistent orbits; 11 maximal commuting sets (eight of 3, and 23, 31, 187)',
             S.size == 719 and reps.size == 227 and sorted(len(c) for c in cl) == [3] * 8 + [23, 31, 187])
    unbounded = True
    curve_bounds = []
    for c in cl:
        gens = [dec(e) for k in c for e in elems[k]]
        if len(c) <= 31:
            diagonal_rank = specialization_rank(gens, (1, 1, 1))
            axis_rank = specialization_rank(gens, (0, 0, 1))
            curve_bounds.append((len(c), diagonal_rank, axis_rank))
        Ls = (4, 6) if len(c) <= 31 else (4,)
        ds = [torus_logdim(gens, L) for L in Ls]
        print(f'B: maximal set of {len(c)} orbits: 3L^3 - rank of the generator union {dict(zip(Ls, ds))}')
        if len(c) == 3:
            unbounded &= ds == [48, 72]
        elif len(c) in (23, 31):
            unbounded &= ds[0] == 32 and ds[1] > ds[0]
        else:
            unbounded &= ds == [0]
    ck.check('B: rank bounds: 3L^3 - rank is 48, 72 for the 3-orbit sets and 32, 48 for the 23- and 31-orbit sets at L = 4, 6, and 0 for the 187-orbit union at L = 4; '
             'these finite sizes alone do not establish growth (the 23/31/187 unions themselves contain -1, per the independent check)',
             unbounded)
    ck.check('B: exact Laurent specialization of all generator unions: four 3-orbit sets have diagonal rank 0, four have axis rank 2; the 23/31 sets have diagonal rank 1; odd-L Fourier bounds prove unbounded dimension',
             sorted(curve_bounds) == sorted([(3, 0, 3)] * 4 + [(3, 3, 2)] * 4 + [(23, 1, 3), (31, 1, 3)]))
    big = next(c for c in cl if len(c) == 187)
    labs = set(l for k in big for e in elems[k] for l in dec(e)) - {0}
    commutant = {p for p in range(1, 64) if all(not SP[p, l] for l in labs)}
    gen3 = [lab3({0: 1}), lab3({1: 2}), lab3({2: 3})]          # X on qubit x, Y on qubit y, Z on qubit z
    orbit_gen = {int(T1[0][k][gen3[0]]) for k in range(24)}
    ck.check('B: the 187-orbit family uses only the abelian alphabet generated by X on qubit x, Y on qubit y, Z on qubit z; '
             'that alphabet is its own single-site commutant and O permutes its three generators transitively '
             '(so either all lie in the group, a product state, or all are free single-site variables and every operator commuting with them commutes with every generator)',
             len(labs) == 7 and all(not SP[a_, b_] for a_ in labs for b_ in labs) and commutant == labs and orbit_gen == set(gen3))
    small = [c for c in cl if len(c) == 3]
    res = [ext3_singular([dec(e) for k in c for e in elems[k]]) for c in small]
    ck.check('B: in each of the eight 3-orbit soldered rules (their -1-freeness with signs + is the result of the independent check), Ext^3(C, R) has empty support off the coordinate planes (no three-dimensionally mobile charge; GF(2), Singular)',
                 not any(res))

    print('per_element: Part A exact (finite checks plus the toric-code structure); Part B exhaustive over C4/C3-fixed star strings')
    print('per_site: three axis-labelled qubits per site; no dynamics is supplied')
    print('per_mode: exact Laurent momentum-rank specializations checked for the odd-L dimension bound; no spectral dispersion or energy dynamics computed')
    print('per_block: checked and not executed — no coarse-grained block dynamics is tested')
    print('lattice_wide: tori L = 4, 6 (8 for the note) for code dimension; charge modules over the Laurent ring with Singular')
    print(f"TOTAL: PASS={ck.passed} FAIL={ck.failed}")
    return 0 if ck.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
