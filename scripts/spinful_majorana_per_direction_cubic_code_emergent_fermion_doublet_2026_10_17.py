#!/usr/bin/env python3
"""Spinful Majorana-per-direction cubic code: a matter doublet with an exact on-site spin action and conditional w2 identification.

Five qubits per site carry ten Majoranas (Jordan-Wigner inside the site): six link Majoranas b_d, one per
direction, and four matter Majoranas forming two complex modes c_up, c_dn. Commuting Pauli stabilizers:
  D_v = total parity of the ten Majoranas at v; W_p = product of u_e = b_{v,+a} b_{v+e_a,-a} around p;
  P_up,v and P_dn,v = parities of the two matter modes.
H = -K sum D - J sum W - mu sum (P_up + P_dn), with J > 0 and K > mu > 0. The two matter states cost 2mu; compare the bare charge at 2K and four-plaquette representative at8J.
The doublet is cheapest among these displayed representatives only when mu<4J as well.

The runner checks exact Pauli algebra and numerical matter matrices:
- commuting, no -1 in the group, log2 code dimension 3 (L = 6);
- a single matter Majorana flips exactly D_v and P_up,v: this local D+P composite is neutral;
  the dressed P-only endpoint is identified with the parent gauge charge by D=B_link P_up P_dn;
  no operator in a radius-2 ball flips P_up alone (a finite control), and a local operator converts up to down;
- the gauge-dressed matter hops c_up(v) u_e c_up(w) create only the two end charges, and the Levin-Wen T-junction
  sign of the up excitation is -1 for all 20 triples (a fermion);
- the on-site spin action on the matter pair: for the 48 elements of the binary octahedral group 2O the operators
  U(u) = exp(-i theta n.S), S = c^dag sigma c / 2, form a representation, U(-1) is the matter parity (a stabilizer),
  n_up + n_dn and the matter parity are preserved, c_s^dag transforms as the spin-1/2 doublet, and all 18 C2 lifts
  square to -1 on the doublet;
- the link sector is the Majorana-per-direction code of the companion note: its clean pair test (consistent
  on-site Clifford action) gives lambda_f = -1 for an axis C2 and an edge C2.
From these: a pair of doublets in a common eigenvector e of the C2 lift (eigenvalue m = +-i) has pair eigenvalue
lambda_f m^2 = +1. Inferring eta=w2 on O additionally requires consistent symmetry localization
with lambda=theta eta and a compatible vacuum reference; this runner does not prove that input. Local matter spinors change the pair factor, so the
displayed sign is representative-dependent, not an established anyon fractionalization invariant.
"""

from __future__ import annotations

import itertools
import os
import sys
from collections import Counter

import numpy as np
from scipy.linalg import expm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17 as rb  # noqa: E402
import majorana_per_direction_cubic_fermion_code_full_rotation_covariance_2026_10_17 as mpd  # noqa: E402

bk, c1 = rb.bk, rb.c1
E, DIRS = bk.E, bk.DIRS
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = (
    'docs/SPINFUL_MAJORANA_PER_DIRECTION_CUBIC_CODE_EMERGENT_FERMION_DOUBLET_CARRIES_SPIN_HALF_CLASS_ON_ALL_CUBIC_ROTATIONS_BOUNDED_THEOREM_NOTE_2026-10-17.md',
)
Q = 5
UP1, UP2, DN1, DN2 = 6, 7, 8, 9


class Spinful:
    def __init__(self, L):
        self.L, self.n = L, Q * L ** 3
        self.V = list(itertools.product(range(L), repeat=3))

    def s(self, v):
        L = self.L
        return ((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)

    def one(self):
        return [np.zeros(self.n, np.uint8), np.zeros(self.n, np.uint8), 0]

    def maj(self, v, k):
        P = self.one()
        s, j = self.s(v), k // 2
        for t in range(j):
            P[1][Q * s + t] = 1
        P[0][Q * s + j] = 1
        if k % 2:
            P[1][Q * s + j] ^= 1
            P[2] = 1
        return P

    def mul(self, *Ps):
        R = self.one()
        for P in Ps:
            R = rb.mulp(R, P)
        return R

    @staticmethod
    def herm(P):
        if (P[2] - int(P[0].astype(int) @ P[1].astype(int))) % 2:
            P = [P[0], P[1], (P[2] + 1) % 4]
        return P

    def u(self, v, a):
        w = tuple(v[i] + E[a][i] for i in range(3))
        return self.mul(self.maj(v, DIRS.index((a, 1))), self.maj(w, DIRS.index((a, -1))))

    def parity(self, v, indices):
        """Conventional occupation parity: (-i)^m chi_1 ... chi_(2m)."""
        P = self.mul(*[self.maj(v, k) for k in indices])
        P[2] = (P[2] - len(indices) // 2) % 4
        return P

    def gens(self):
        G, lab = [], []
        for v in self.V:
            G.append(self.parity(v, range(10)))
            lab.append(('D', v))
            G.append(self.parity(v, (UP1, UP2)))
            lab.append(('Pup', v))
            G.append(self.parity(v, (DN1, DN2)))
            lab.append(('Pdn', v))
            for c in range(3):
                a, b = [t for t in range(3) if t != c]
                va = tuple(v[i] + E[a][i] for i in range(3))
                vb = tuple(v[i] + E[b][i] for i in range(3))
                G.append(self.herm(self.mul(self.u(v, a), self.u(va, b), self.u(vb, a), self.u(v, b))))
                lab.append(('W', v, c))
        return G, lab


def om(P, R):
    return int((P[0].astype(int) @ R[1].astype(int) + P[1].astype(int) @ R[0].astype(int)) % 2)


def matter_checks():
    I2 = np.eye(2)
    X, Y, Z = np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])
    sp = np.array([[0, 0], [1, 0]])
    cdag = [np.kron(sp, I2), np.kron(Z, sp)]
    c = [m.conj().T for m in cdag]
    num = sum(cd @ cc for cd, cc in zip(cdag, c))
    par = np.kron(Z, Z)
    pauli = [X, Y, Z]
    S = [0.5 * sum(cdag[a] @ c[b] * pauli[k][a, b] for a in range(2) for b in range(2)) for k in range(3)]

    def su2(ax, th):
        nn = np.array(ax, float) / np.linalg.norm(ax)
        return expm(-0.5j * th * sum(nn[k] * pauli[k] for k in range(3)))

    def U(ax, th):
        nn = np.array(ax, float) / np.linalg.norm(ax)
        return expm(-1j * th * sum(nn[k] * S[k] for k in range(3)))
    gens = [((0, 0, 1), np.pi / 2), ((1, 1, 1), 2 * np.pi / 3)]
    key = lambda m: tuple(np.round(m.flatten(), 6))
    els = [(np.eye(2, dtype=complex), np.eye(4, dtype=complex))]
    seen, fr = {key(els[0][0])}, list(els)
    while fr:
        nf = []
        for (u, Uu) in fr:
            for ax, th in gens:
                u2, U2 = su2(ax, th) @ u, U(ax, th) @ Uu
                if key(u2) not in seen:
                    seen.add(key(u2))
                    nf.append((u2, U2))
                    els.append((u2, U2))
        fr = nf
    look = {key(u): Uu for u, Uu in els}
    res = {
        'order48': len(els) == 48,
        'rep': all(np.allclose(U1 @ U2, look[key(u1 @ u2)]) for (u1, U1), (u2, U2) in itertools.product(els, els)),
        'minus_is_parity': np.allclose(look[key(-np.eye(2))], par),
        'preserves': all(np.allclose(Uu @ num @ Uu.conj().T, num) and np.allclose(Uu @ par @ Uu.conj().T, par) for _, Uu in els),
        'doublet': all(np.allclose(Uu @ cdag[s] @ Uu.conj().T, sum(u[t, s] * cdag[t] for t in range(2))) for u, Uu in els for s in range(2)),
    }
    c2 = [(u, Uu) for u, Uu in els if np.allclose(u @ u, -np.eye(2)) and np.isclose(np.trace(u), 0)]
    res['c2'] = len(c2) == 18 and all(np.allclose((Uu @ Uu)[1:3, 1:3], -np.eye(2)) for _, Uu in c2)
    # eigenvalues of each C2 lift on the one-particle doublet block (sites x and Rx carry the same eigenvector)
    res['c2_eigs'] = [np.linalg.eigvals(Uu[1:3, 1:3]) for _, Uu in c2]
    return res


def main() -> int:
    ck = c1.Checks()
    sf = Spinful(6)
    rb.L, rb.N = 6, sf.n
    # Pin the physical vacuum convention; hermiticity alone cannot fix signs.
    origin = (0, 0, 0)
    def zword(indices):
        P = sf.one()
        for k in indices:
            P[1][Q * sf.s(origin) + k] = 1
        return P
    def equal(P, R):
        return np.array_equal(P[0], R[0]) and np.array_equal(P[1], R[1]) and P[2] % 4 == R[2] % 4
    d = sf.parity(origin, range(10))
    pup = sf.parity(origin, (UP1, UP2))
    pdn = sf.parity(origin, (DN1, DN2))
    blink = sf.parity(origin, range(6))
    ck.check('occupation-parity signs and D = B_link P_up P_dn; empty matter has +1 parity',
             equal(pup, zword((3,))) and equal(pdn, zword((4,)))
             and equal(d, zword(range(5))) and equal(d, sf.mul(blink, pup, pdn)))
    G, lab = sf.gens()
    M = np.array([np.concatenate([g[0], g[1]]) for g in G])
    n = sf.n
    comm = not ((M[:, :n].astype(np.int32) @ M[:, n:].T.astype(np.int32) + M[:, n:].astype(np.int32) @ M[:, :n].T.astype(np.int32)) % 2).any()
    ck.check('L = 6: commuting stabilizer group with no -1', comm and rb.valid(G))
    ck.check('L = 6: log2 code dimension 3', n - c1.f2_rank_and_null(M)[0] == 3)
    v0 = (0, 0, 0)
    viol = sorted(l for G_, l in zip(G, lab) if om(sf.maj(v0, UP1), G_))
    ck.check('a single matter Majorana flips exactly D_v and P_up,v (a local neutral D/P pair; dressed P-only endpoints carry the charge)',
             viol == [('D', v0), ('Pup', v0)])
    box = list(itertools.product(range(-2, 3), repeat=3))
    cols = np.array(sorted({Q * sf.s(p) + t for p in box for t in range(Q)}))
    rows, rhs = [], []
    for G_, l in zip(G, lab):
        cg = np.concatenate([G_[1][cols], G_[0][cols]])
        if cg.any():
            rows.append(cg)
            rhs.append(1 if (l[0] == 'Pup' and l[1] == v0) else 0)
    A = np.array(rows, np.uint8)
    Ab = np.concatenate([A, np.array(rhs, np.uint8)[:, None]], 1)
    ck.check('no operator in a radius-2 ball flips P_up,v alone (finite radius-2 control; charge identification uses the stabilizer identity)',
             c1.f2_rank_and_null(Ab)[0] > c1.f2_rank_and_null(A)[0])
    conv = sf.mul(sf.maj(v0, UP1), sf.maj(v0, DN1))
    ck.check('up and down at one site are related by a local operator (one anyon type, two states)',
             sorted(l for G_, l in zip(G, lab) if om(conv, G_)) == [('Pdn', v0), ('Pup', v0)])

    def hop(v, a):
        w = tuple(v[i] + E[a][i] for i in range(3))
        return sf.mul(sf.maj(v, UP1), sf.u(v, a), sf.maj(w, UP1))

    def leg(d):
        a, s = DIRS[d]
        v, P = (0, 0, 0), sf.one()
        for _ in range(2):
            if s == 1:
                base, v = v, tuple(v[i] + E[a][i] for i in range(3))
            else:
                v = tuple(v[i] - E[a][i] for i in range(3))
                base = v
            P = rb.mulp(P, hop(base, a))
        return P
    legs = [leg(d) for d in range(6)]
    clean = all(sum(om(lg, G_) for G_ in G) == 2 and all(l[0] == 'Pup' for G_, l in zip(G, lab) if om(lg, G_)) for lg in legs)
    ck.check('gauge-dressed matter hops create only the two end charges', clean)
    tj = Counter((-1) ** (om(legs[a], legs[b]) + om(legs[b], legs[c]) + om(legs[a], legs[c])) for a, b, c in itertools.combinations(range(6), 3))
    print('T-junction signs of the up excitation:', dict(tj))
    ck.check('the up excitation is a fermion: T-junction sign -1 for all 20 triples', tj == Counter({-1: 20}))
    mc = matter_checks()
    print('matter spin action checks:', {k: v for k, v in mc.items() if k != 'c2_eigs'})
    ck.check('2O acts on the matter pair by a representation with U(-1) = matter parity, preserving number and parity', mc['order48'] and mc['rep'] and mc['minus_is_parity'] and mc['preserves'])
    ck.check('c_s^dag transforms as the spin-1/2 doublet and all 18 C2 lifts square to -1 on it', mc['doublet'] and mc['c2'])
    # link sector: clean pair test of the companion code (gauge charge) for an axis C2 and an edge C2
    adm = lambda Mr: [e for e in itertools.product((1, -1), repeat=6) if np.prod(e) == mpd.perm_sign([bk.rotdir(Mr, d) for d in range(6)])]
    key = lambda P: tuple(P.flatten())

    def mat(Mr, eps):
        P = np.zeros((6, 6), int)
        for d in range(6):
            P[bk.rotdir(Mr, d), d] = eps[d]
        return P
    C4 = next(Mr for Mr in c1.O if bk.kind(Mr) == 'C4')
    C3 = next(Mr for Mr in c1.O if bk.kind(Mr) == 'C3')
    e4, e3 = next((a, b) for a in adm(C4) for b in adm(C3) if mpd._order48(mat(C4, a), mat(C3, b), key))
    el = mpd._generate([mat(C4, e4), mat(C3, e3)], key)
    c8 = mpd.Code(8)
    G8, lab8, _ = c8.gens((0, 0, 0))
    lam, done = {}, set()
    for B in el.values():
        perm = [int(np.flatnonzero(B[:, d])[0]) for d in range(6)]
        Mr = np.zeros((3, 3), int)
        for a in range(3):
            b, s2 = DIRS[perm[a]]
            Mr[b, a] = s2
        kd = bk.kind(Mr)
        if kd in ('C2axis', 'C2edge') and kd not in done:
            done.add(kd)
            eps = tuple(int(B[perm[d], d]) for d in range(6))
            x = next(x for x in itertools.product(range(-2, 3), repeat=3) if 2 <= max(abs(x[i] - int(cc)) for i, cc in enumerate(Mr @ np.array(x))) <= 3)
            lam[kd] = mpd.clean_pair_eigenvalue(c8, G8, lab8, Mr, eps, x)
    print('gauge-charge pair eigenvalues (link sector):', lam)
    ck.check('link sector (companion code, consistent action, clean creators): lambda_f = -1 for an axis C2 and an edge C2', lam == {'C2axis': -1, 'C2edge': -1})
    # composition: doublet pair in a common C2-lift eigenvector: lambda = lambda_f * m^2 with m = +-i
    # composition: |e e> with e an eigenvector of the C2 lift on the doublet (eigenvalue m) has eigenvalue lambda_f m^2
    pair = [complex(lf * m * m) for lf in lam.values() for eig in mc['c2_eigs'] for m in eig]
    ck.check('composition: for all 18 C2 lifts and both eigenvectors, the relative doublet pair factor lambda_f m^2 is +1 (w2 inference requires the declared localization input)',
             all(np.isclose(x, 1) for x in pair))
    print('per_element: L = 6 code; 48 elements of 2O; one axis and one edge C2 for the link pair test')
    print('per_site: five qubits per site (six link and four matter Majoranas)')
    print('per_mode: two matter modes per site')
    print('per_block: not applicable')
    print('lattice_wide: L = 6 (code), L = 8 (link pair test)')
    print(f"TOTAL: PASS={ck.passed} FAIL={ck.failed}")
    return 0 if ck.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
