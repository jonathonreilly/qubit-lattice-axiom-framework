#!/usr/bin/env python3
"""Majorana-per-direction fermion code on the cubic lattice: one fermion species, covariant under all 24 rotations.

Three qubits per site of Z^3 carry six local Majorana operators gamma_{v,d}, one per direction d (a fixed
Jordan-Wigner choice inside the site: gamma_0..5 = X1, Y1, Z1X2, Z1Y2, Z1Z2X3, Z1Z2Y3, assigned to the
directions +x,+y,+z,-x,-y,-z). Majoranas at different sites commute. Generators:
  B_v   = (-i)^3 gamma_{v,0} ... gamma_{v,5}            (site parity, one site)
  S_p   = product of the four edge operators A_(v,a) = gamma_{v,+a} gamma_{v+e_a,-a} around a plaquette
          (times a sign per plaquette orientation; 8 translation-invariant sectors).
Violations of B are point charges moved by the edge operators. A rotation R acts by permuting sites and by an
on-site Clifford gamma_{v,d} -> eps(d) gamma_{Rv,Rd} with prod eps = sign of the direction permutation.

The runner checks:
- commuting, all 8 sectors valid, log2 code dimension 3 (L = 4; also L = 6 for two sectors);
- Levin-Wen T-junction sign -1 for all 20 triples of straight legs (L = 6): a fermionic charge;
- for each of the 24 rotations and each of the 32 admissible sign choices eps, the signed groups of the sectors
  (0,0,0) and (1,1,1) are mapped to themselves (L = 4): the code is O-covariant with one fermion species;
- group law: choosing eps for a C4 and a C3 generates a signed-permutation group; 128 of the 1024 choices give a
  group of order 48 containing -1 (a central Z2 extension of O by fermion parity); in all of them the lifts of
  the axis C2 square to +1 and the lifts of the edge C2 to -1.
"""

from __future__ import annotations

import itertools
import os
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17 as rb  # noqa: E402

bk, c1 = rb.bk, rb.c1
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = (
    'docs/MAJORANA_PER_DIRECTION_CUBIC_FERMION_CODE_HAS_ONE_SPECIES_COVARIANT_UNDER_ALL_CUBIC_ROTATIONS_BOUNDED_THEOREM_NOTE_2026-10-17.md',
)
E, DIRS, O = bk.E, bk.DIRS, c1.O
JW = [((1, 0, 0), (0, 0, 0), 0), ((1, 0, 0), (1, 0, 0), 1), ((0, 1, 0), (1, 0, 0), 0), ((0, 1, 0), (1, 1, 0), 1),
      ((0, 0, 1), (1, 1, 0), 0), ((0, 0, 1), (1, 1, 1), 1)]   # (x bits, z bits, k): P = i^k X^x Z^z


class Code:
    def __init__(self, L):
        self.L, self.n = L, 3 * L ** 3
        self.V = list(itertools.product(range(L), repeat=3))

    def s(self, v):
        L = self.L
        return ((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)

    def gamma(self, v, d):
        x = np.zeros(self.n, np.uint8)
        z = np.zeros(self.n, np.uint8)
        xb, zb, k = JW[d]
        for t in range(3):
            x[3 * self.s(v) + t] = xb[t]
            z[3 * self.s(v) + t] = zb[t]
        return [x, z, k]

    def word(self, ws):
        P = [np.zeros(self.n, np.uint8), np.zeros(self.n, np.uint8), 0]
        for (v, d) in ws:
            Q = self.gamma(v, d)
            sg = int(P[1].astype(int) @ Q[0].astype(int)) % 2
            P = [P[0] ^ Q[0], P[1] ^ Q[1], (P[2] + Q[2] + 2 * sg) % 4]
        return P

    @staticmethod
    def edge_word(v, a):
        return [(v, DIRS.index((a, 1))), (tuple(v[i] + E[a][i] for i in range(3)), DIRS.index((a, -1)))]

    def plaq_word(self, v, c):
        a, b = [t for t in range(3) if t != c]
        va = tuple(v[i] + E[a][i] for i in range(3))
        vb = tuple(v[i] + E[b][i] for i in range(3))
        return self.edge_word(v, a) + self.edge_word(va, b) + self.edge_word(vb, a) + self.edge_word(v, b)

    def gens(self, signs):
        G, lab, words = [], [], []
        for v in self.V:
            P = self.word([(v, d) for d in range(6)])
            G.append([P[0], P[1], (P[2] + 1) % 4])            # (-i)^3 = i
            lab.append(('B', v, None))
            words.append([(v, d) for d in range(6)])
            for c in range(3):
                P = self.word(self.plaq_word(v, c))
                G.append([P[0], P[1], (P[2] + 2 * signs[c]) % 4])
                lab.append(('S', v, c))
                words.append(self.plaq_word(v, c))
        return G, lab, words


def perm_sign(p):
    p, s = list(p), 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], p[i]
            s = -s
    return s


def mats(G, n):
    return np.array([np.concatenate([g[0], g[1]]) for g in G])


def main() -> int:
    ck = c1.Checks()
    c4 = Code(4)
    rb.L, rb.N = 4, c4.n
    ok_all, dims = True, Counter()
    for s_ in itertools.product((0, 1), repeat=3):
        G, _, _ = c4.gens(s_)
        M = mats(G, c4.n)
        n = c4.n
        comm = not ((M[:, :n].astype(np.int32) @ M[:, n:].T.astype(np.int32) + M[:, n:].astype(np.int32) @ M[:, :n].T.astype(np.int32)) % 2).any()
        ok_all &= comm and rb.valid(G)
        dims[n - c1.f2_rank_and_null(M)[0]] += 1
    ck.check('L = 4: all 8 sign sectors are commuting, valid stabilizer groups', ok_all)
    ck.check('L = 4: log2 code dimension 3 in every sector', dims == Counter({3: 8}))
    c6 = Code(6)
    d6 = []
    for s_ in ((0, 0, 0), (1, 1, 1)):
        G, _, _ = c6.gens(s_)
        d6.append(c6.n - c1.f2_rank_and_null(mats(G, c6.n))[0])
    ck.check('L = 6: log2 code dimension 3 in the sectors (0,0,0) and (1,1,1)', d6 == [3, 3])
    # statistics at L = 6
    om = lambda P, Q: int((P[0].astype(int) @ Q[1].astype(int) + P[1].astype(int) @ Q[0].astype(int)) % 2)

    def leg(d):
        a, s = DIRS[d]
        v, ws = (0, 0, 0), []
        for _ in range(2):
            if s == 1:
                base, v = v, tuple(v[i] + E[a][i] for i in range(3))
            else:
                v = tuple(v[i] - E[a][i] for i in range(3))
                base = v
            ws += Code.edge_word(base, a)
        return c6.word(ws)
    legs = [leg(d) for d in range(6)]
    G6, lab6, _ = c6.gens((0, 0, 0))
    clean = all(om(lg, g) == 0 for lg in legs for g, l in zip(G6, lab6) if l[0] == 'S') and \
        all(sum(om(lg, g) for g, l in zip(G6, lab6) if l[0] == 'B') == 2 for lg in legs)
    tj = Counter((-1) ** (om(legs[a], legs[b]) + om(legs[b], legs[c]) + om(legs[a], legs[c])) for a, b, c in itertools.combinations(range(6), 3))
    print('T-junction signs (L = 6):', dict(tj))
    ck.check('straight legs of edge operators commute with all plaquettes and flip exactly two vertex terms (L = 6)', clean)
    ck.check('fermionic charge: Levin-Wen T-junction sign -1 for all 20 triples of directions (L = 6)', tj == Counter({-1: 20}))
    # O-covariance with on-site signed Majorana permutations (L = 4)
    rb.L, rb.N = 4, c4.n
    cov = Counter()
    for s_ in ((0, 0, 0), (1, 1, 1)):
        G, lab, words = c4.gens(s_)
        Mg = mats(G, c4.n).T
        for M in O:
            pi = [bk.rotdir(M, d) for d in range(6)]
            for eps in itertools.product((1, -1), repeat=6):
                if np.prod(eps) != perm_sign(pi):
                    continue
                imgs = []
                for g, ws in zip(G, words):
                    base = c4.word(ws)
                    sgn = int(np.prod([eps[d] for _, d in ws]))
                    P = c4.word([(tuple(int(x) for x in M @ np.array(v)), pi[d]) for v, d in ws])
                    imgs.append([P[0], P[1], (P[2] + (g[2] - base[2]) + (0 if sgn == 1 else 2)) % 4])
                W, okk = rb.solve_multi(Mg, np.array([np.concatenate([im[0], im[1]]) for im in imgs]).T)
                good = bool(okk.all())
                if good:
                    for j, im in enumerate(imgs):
                        R = rb.one()
                        for i in np.nonzero(W[:, j])[0]:
                            R = rb.mulp(R, G[i])
                        if R[2] != im[2]:
                            good = False
                            break
                cov[(s_, good)] += 1
    print('covariance tests (sector, preserved): count', dict(cov))
    ck.check('every rotation with every admissible sign choice (24 x 32) maps the signed groups of sectors (0,0,0) and (1,1,1) to themselves',
             cov == Counter({((0, 0, 0), True): 768, ((1, 1, 1), True): 768}))
    # group law
    def mat(M, eps):
        P = np.zeros((6, 6), int)
        for d in range(6):
            P[bk.rotdir(M, d), d] = eps[d]
        return P
    C4 = next(M for M in O if bk.kind(M) == 'C4')
    C3 = next(M for M in O if bk.kind(M) == 'C3')
    adm = lambda M: [e for e in itertools.product((1, -1), repeat=6) if np.prod(e) == perm_sign([bk.rotdir(M, d) for d in range(6)])]
    key = lambda P: tuple(P.flatten())
    stats = Counter()
    for e4 in adm(C4):
        for e3 in adm(C3):
            gens_ = [mat(C4, e4), mat(C3, e3)]
            el = {key(np.eye(6, dtype=int)): np.eye(6, dtype=int)}
            fr = [np.eye(6, dtype=int)]
            while fr and len(el) <= 200:
                nf = []
                for A in fr:
                    for g in gens_:
                        B = g @ A
                        if key(B) not in el:
                            el[key(B)] = B
                            nf.append(B)
                fr = nf
            if len(el) != 48 or key(-np.eye(6, dtype=int)) not in el:
                stats['other'] += 1
                continue
            sq = set()
            for B in el.values():
                perm = [int(np.flatnonzero(B[:, d])[0]) for d in range(6)]
                Mr = np.zeros((3, 3), int)
                for a in range(3):
                    b, s = DIRS[perm[a]]
                    Mr[b, a] = s
                kd = bk.kind(Mr)
                if kd in ('C2axis', 'C2edge'):
                    S2 = B @ B
                    sq.add((kd, 1 if (S2 == np.eye(6)).all() else (-1 if (S2 == -np.eye(6)).all() else 0)))
            stats[tuple(sorted(sq))] += 1
    print('group-law choices:', dict(stats))
    ck.check('group law: 128 of 1024 generator sign choices give an order-48 group containing -1 (central extension of O by fermion parity); in all, axis-C2 lifts square to +1 and edge-C2 lifts to -1',
             stats.get((('C2axis', 1), ('C2edge', -1)), 0) == 128)
    print('per_element: 8 sign sectors; 24 rotations x 32 sign choices; 1024 generator choices')
    print('per_site: three qubits per site (six local Majoranas)')
    print('per_mode: not applicable')
    print('per_block: not applicable')
    print('lattice_wide: L = 4 (sectors, covariance), L = 6 (dimension, statistics)')
    print(f"TOTAL: PASS={ck.passed} FAIL={ck.failed}")
    return 0 if ck.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
