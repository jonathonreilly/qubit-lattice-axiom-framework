#!/usr/bin/env python3
"""Site-local realization of the translation-invariant BKSF cubic fermion codes.

Six qubits per site of Z^3, one per direction d in {+x,+y,+z,-x,-y,-z} (half-edges). For an ordering of the six
directions (the same at every site):
  B_v       = Z on the six qubits of site v                           (one site)
  R_(v,a)   = Z_(v,+a) Z_(v+e_a,-a)                                   (nearest-neighbour pair; repetition)
  A_(v,a)   = X_(v,+a) X_(v+e_a,-a) * Z on v's qubits ordered before +a * Z on (v+e_a)'s qubits ordered before -a
                                                                      (nearest-neighbour pair; charge hop)
  S_p       = product of the four A around a plaquette                 (four sites of a plaquette)
Code = <B, R, S>. On the repetition code space each edge carries one logical qubit (X = X X, Z = Z on either
half) and the code is the edge BKSF code of the companion notes.

The framework site rotation about a site (permute sites, and permute each site's six qubits as directions)
induces exactly the edge rotation on the logical qubits. The runner checks, on the L = 4 torus:
- all 60 codes (classes of the 720 orderings) are commuting with log2 code dimension 3 (also L = 6, one code
  per orbit type);
- the site action maps A_(v,a) of ordering o exactly to A of the rotated edge with the rotated ordering;
- the stabilizer of each code in O under the site action equals its stabilizer under the edge action, so the
  orbits have sizes 4, 6 and 12 (12, 12 and 36 codes), as for the edge codes;
- on-site Cliffords (signed permutations of the twelve in-site Jordan-Wigner Majoranas mu_d = X_d Z_<d,
  nu_d = Y_d Z_<d, with the code's own ordering as the in-site order): for one code of each orbit type and both
  uniform sign sectors, every one of the 24 rotations maps the signed group to itself for some sign choice.
  So with on-site Clifford actions each code is O-invariant; the minimal orbit four is a statement about the
  bare site action.
"""

from __future__ import annotations

import itertools
import os
import sys
from collections import Counter, defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk  # noqa: E402
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1  # noqa: E402

AUDIT_TIMEOUT_SEC = 1200
AUDIT_INPUT_PATHS = (
    'docs/BKSF_CUBIC_FERMION_CODES_SITE_LOCAL_REALIZATION_WITH_SIX_DIRECTION_QUBITS_PER_SITE_BOUNDED_THEOREM_NOTE_2026-10-17.md',
)

E, DIRS = bk.E, bk.DIRS


class Half:
    def __init__(self, L):
        self.L = L
        self.n = 6 * L ** 3
        self.V = list(itertools.product(range(L), repeat=3))

    def q(self, v, d):
        L = self.L
        return 6 * (((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)) + d

    def A(self, v, a, order):
        x = np.zeros(self.n, np.uint8)
        z = np.zeros(self.n, np.uint8)
        w = tuple(v[i] + E[a][i] for i in range(3))
        dp, dm = DIRS.index((a, 1)), DIRS.index((a, -1))
        x[self.q(v, dp)] ^= 1
        x[self.q(w, dm)] ^= 1
        pos = {d: i for i, d in enumerate(order)}
        for d in range(6):
            if pos[d] < pos[dp]:
                z[self.q(v, d)] ^= 1
            if pos[d] < pos[dm]:
                z[self.q(w, d)] ^= 1
        return np.concatenate([x, z])

    def B(self, v):
        z = np.zeros(self.n, np.uint8)
        for d in range(6):
            z[self.q(v, d)] = 1
        return np.concatenate([np.zeros(self.n, np.uint8), z])

    def R(self, v, a):
        z = np.zeros(self.n, np.uint8)
        w = tuple(v[i] + E[a][i] for i in range(3))
        z[self.q(v, DIRS.index((a, 1)))] = 1
        z[self.q(w, DIRS.index((a, -1)))] = 1
        return np.concatenate([np.zeros(self.n, np.uint8), z])

    def S(self, v, c, order):
        a, b = [t for t in range(3) if t != c]
        va = tuple(v[i] + E[a][i] for i in range(3))
        vb = tuple(v[i] + E[b][i] for i in range(3))
        return self.A(v, a, order) ^ self.A(va, b, order) ^ self.A(vb, a, order) ^ self.A(v, b, order)

    def code(self, order):
        return np.array([self.B(v) for v in self.V] + [self.R(v, a) for v in self.V for a in range(3)]
                        + [self.S(v, c, order) for v in self.V for c in range(3)])

    def site_perm(self, M):
        perm = np.zeros(self.n, int)
        for v in self.V:
            w = tuple(int(x) for x in M @ np.array(v))
            for d in range(6):
                a, s = DIRS[d]
                dv = M @ (s * np.array(E[a]))
                b = int(np.nonzero(dv)[0][0])
                perm[self.q(v, d)] = self.q(w, DIRS.index((b, int(dv[b]))))
        return perm

    def act(self, R, perm):
        out = np.zeros_like(R)
        out[:, perm] = R[:, :self.n]
        out[:, self.n + perm] = R[:, self.n:]
        return out

    def commuting(self, C):
        n = self.n
        return not ((C[:, :n].astype(np.int32) @ C[:, n:].T.astype(np.int32)
                     + C[:, n:].astype(np.int32) @ C[:, :n].T.astype(np.int32)) % 2).any()


def rank(M):
    A = (np.array(M, np.uint8) % 2).copy()
    m, n = A.shape
    r = 0
    for c in range(n):
        nz = np.flatnonzero(A[r:, c])
        if nz.size == 0:
            continue
        p = r + nz[0]
        if p != r:
            A[[r, p]] = A[[p, r]]
        rows = np.flatnonzero(A[:, c])
        rows = rows[rows != r]
        if rows.size:
            A[rows] ^= A[r]
        r += 1
        if r == m:
            break
    return r


def _signed_onsite_check(order, sec, L=4):
    """True if every rotation, with some on-site signed Majorana permutation, preserves the signed group."""
    import bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17 as rb
    n = 6 * L ** 3
    rb.L, rb.N = L, n
    V = list(itertools.product(range(L), repeat=3))
    s_ = lambda v: ((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)
    one = lambda: [np.zeros(n, np.uint8), np.zeros(n, np.uint8), 0]

    def single(qq, lab):
        P = one()
        if lab in 'XY':
            P[0][qq] = 1
        if lab in 'YZ':
            P[1][qq] = 1
        if lab == 'Y':
            P[2] = 1
        return P

    def mul(*Ps):
        R = one()
        for P in Ps:
            R = rb.mulp(R, P)
        return R
    pos = {dd: i for i, dd in enumerate(order)}

    def maj(v, d, kind):
        P = single(6 * s_(v) + d, 'X' if kind == 0 else 'Y')
        for dd in range(6):
            if pos[dd] < pos[d]:
                P = mul(single(6 * s_(v) + dd, 'Z'), P)
        return P

    def A(v, a):
        w = tuple(v[i] + E[a][i] for i in range(3))
        return mul(maj(v, DIRS.index((a, 1)), 0), maj(w, DIRS.index((a, -1)), 0))
    G = []
    for v in V:
        G.append(mul(*[single(6 * s_(v) + d, 'Z') for d in range(6)]))
        for a in range(3):
            w = tuple(v[i] + E[a][i] for i in range(3))
            G.append(mul(single(6 * s_(v) + DIRS.index((a, 1)), 'Z'), single(6 * s_(w) + DIRS.index((a, -1)), 'Z')))
        for c in range(3):
            a, b = [t for t in range(3) if t != c]
            va = tuple(v[i] + E[a][i] for i in range(3))
            vb = tuple(v[i] + E[b][i] for i in range(3))
            P = mul(A(v, a), A(va, b), A(vb, a), A(v, b))
            if (P[2] - int(P[0].astype(int) @ P[1].astype(int))) % 2:
                P[2] = (P[2] + 1) % 4
            P[2] = (P[2] + 2 * sec[c]) % 4
            G.append(P)
    mlist = [(d, k) for d in range(6) for k in (0, 1)]
    base = [maj((0, 0, 0), d, k) for d, k in mlist]
    tab = {}
    for mask in range(1 << 12):
        P = one()
        for i in range(12):
            if mask >> i & 1:
                P = rb.mulp(P, base[i])
        tab.setdefault((tuple(P[0][:6]), tuple(P[1][:6])), (mask, P[2]))

    def image(P, M, eps):
        out = [np.zeros(n, np.uint8), np.zeros(n, np.uint8), P[2]]
        for s in sorted(set((np.flatnonzero(P[0] | P[1]) // 6).tolist())):
            v = (s // (L * L), (s // L) % L, s % L)
            mask, k = tab[(tuple(P[0][6 * s:6 * s + 6]), tuple(P[1][6 * s:6 * s + 6]))]
            w = tuple(int(x) for x in M @ np.array(v))
            W, sgn = one(), 1
            for i in range(12):
                if mask >> i & 1:
                    d, kk = mlist[i]
                    sgn *= eps[i]
                    W = rb.mulp(W, maj(w, bk.rotdir(M, d), kk))
            add = [W[0], W[1], (W[2] - k + (0 if sgn == 1 else 2)) % 4]
            sg = int(out[1].astype(int) @ add[0].astype(int)) % 2
            out = [out[0] ^ add[0], out[1] ^ add[1], (out[2] + add[2] + 2 * sg) % 4]
        return out
    Mg = np.array([np.concatenate([g[0], g[1]]) for g in G]).T
    near = [g for g in G if (g[0][:6] | g[1][:6]).any()]
    for M in c1.O:
        found = False
        for eps in itertools.product((1, -1), repeat=12):
            good = True
            for g in near:
                im = image(g, M, eps)
                W, okk = rb.solve_multi(Mg, np.concatenate([im[0], im[1]])[:, None])
                if not okk[0]:
                    good = False
                    break
                R = rb.one()
                for i in np.nonzero(W[:, 0])[0]:
                    R = rb.mulp(R, G[i])
                if R[2] != im[2]:
                    good = False
                    break
            if good:
                found = True
                break
        if not found:
            return False
    return True


def main() -> int:
    ck = c1.Checks()
    orders = list(itertools.permutations(range(6)))
    Hedge = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
    classes = defaultdict(list)
    for o in orders:
        classes[Hedge[o]].append(o)
    h4 = Half(4)
    perms = [h4.site_perm(M) for M in c1.O]
    comm, dims, orb, exact, same_stab = True, Counter(), Counter(), True, True
    reps = {}
    for h, ords in classes.items():
        o = ords[0]
        C = h4.code(o)
        comm &= h4.commuting(C)
        dims[h4.n - rank(C)] += 1
        hh = bk.span_hash(C)
        st = [k for k, M in enumerate(c1.O) if bk.span_hash(h4.act(C, perms[k])) == hh]
        st_edge = [k for k, M in enumerate(c1.O) if Hedge[bk.rot_order(M, o)] == h]
        same_stab &= st == st_edge
        orb[24 // len(st)] += 1
        reps.setdefault(24 // len(st), o)
        for k, M in enumerate(c1.O):
            for a in range(3):
                img = h4.act(h4.A((0, 0, 0), a, o)[None, :], perms[k])[0]
                d = M @ np.array(E[a])
                b = int(np.nonzero(d)[0][0])
                base = (0, 0, 0) if d[b] == 1 else tuple(-E[b][t] for t in range(3))
                exact &= bool((img == h4.A(base, b, bk.rot_order(M, o))).all())
    ck.check('all 60 half-edge codes are commuting stabilizer groups (L = 4)', comm)
    ck.check('all 60 have log2 code dimension 3 on the L = 4 torus', dims == Counter({3: 60}))
    ck.check('the site action (permute sites and the six direction labels) maps A_(v,a) of ordering o exactly to A of the rotated edge with the rotated ordering (all 24 rotations, all 60 codes)', exact)
    ck.check('for every code, its stabilizer in O under the site action equals its stabilizer under the edge action', same_stab)
    print('orbit sizes under the site action (size: number of codes):', dict(orb))
    ck.check('orbits under the site action have sizes 4, 6 and 12 (12, 12 and 36 codes); no code is O-invariant', orb == Counter({4: 12, 6: 12, 12: 36}))
    h6 = Half(6)
    d6 = {k: h6.n - rank(h6.code(o)) for k, o in reps.items()}
    print('L = 6 log2 code dimension, one code per orbit type:', d6)
    ck.check('L = 6: log2 code dimension 3 for one code of each orbit type', all(v == 3 for v in d6.values()))
    onsite = {k: all(_signed_onsite_check(o, sec) for sec in ((0, 0, 0), (1, 1, 1))) for k, o in reps.items()}
    print('on-site Clifford O-invariance (orbit type: all 24 rotations preserved in both uniform sectors):', onsite)
    ck.check('with on-site signed Majorana-permutation Cliffords, one code of each orbit type is invariant under all 24 rotations (both uniform sectors, L = 4)',
             all(onsite.values()))
    print('per_element: all 60 codes; all 24 rotations')
    print('per_site: six qubits per site (one per direction); generators on one site, nearest-neighbour pairs and plaquettes')
    print('per_mode: checked and not executed — no momentum-mode or spectral-dispersion claim is tested')
    print('per_block: checked and not executed — no coarse-grained block dynamics is tested')
    print('lattice_wide: L = 4 torus (all codes), L = 6 (one per orbit type)')
    print(f"TOTAL: PASS={ck.passed} FAIL={ck.failed}")
    return 0 if ck.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
