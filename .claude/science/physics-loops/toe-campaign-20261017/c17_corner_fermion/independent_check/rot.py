"""Item 1: own construction of the rotation operators and an exact operator-level group-law check.

Every operator here has the canonical form U = D P with
  P|y> = |pi y>   ((pi y)_{pi(i)} = y_i, so P X_i P^dag = X_{pi(i)}),
  D|y> = (-1)^{q(y)} |y>,  q(y) = sum_{(i,j) in CZ} y_i y_j + sum_{i in Zs} y_i.
No global phase ever appears (all factors are permutations, CZ, Z).  Two such operators are
equal as operators iff (pi, CZ set, Zs) coincide, because a degree-<=2 multilinear polynomial
over GF(2) is determined by its values on {0,1}^n.  So the comparison below is an exact
operator identity on the whole 2^3072-dimensional Hilbert space, not a check on a subset.
"""
import sys, time, itertools, pickle
import numpy as np
from ccode import CornerCode, StabGroup, pmul, pdag, permute_mask, bits
from geom import rotations, classify, w1


class Op:
    def __init__(self, pi, cz, zs):
        self.pi = tuple(pi)
        self.cz = frozenset(cz)  # set of (i,j) i<j
        self.zs = zs  # int mask
        self._nbr = None

    def key(self):
        return (self.pi, self.cz, self.zs)

    def nbr(self):
        if self._nbr is None:
            d = {}
            for (i, j) in self.cz:
                d[i] = d.get(i, 0) | (1 << j)
                d[j] = d.get(j, 0) | (1 << i)
            self._nbr = d
        return self._nbr

    def conj(self, P):
        """U P U^dag."""
        x, z, p = P
        x = permute_mask(x, self.pi)
        z = permute_mask(z, self.pi)
        nb = self.nbr()
        ax = 0
        npairs2 = 0
        for i in bits(x):
            m = nb.get(i, 0)
            ax ^= m
            npairs2 += bin(m & x).count('1')
        qx = npairs2 // 2 + bin(self.zs & x).count('1')
        return (x, z ^ ax, (p + 2 * qx) % 4)


def relabel_cz(cz, pi):
    out = set()
    for (i, j) in cz:
        a, b = pi[i], pi[j]
        out.add((min(a, b), max(a, b)))
    return out


def compose(U1, U2):
    """U1 U2 = D1 P1 D2 P2 = D1 (P1 D2 P1^dag) P1 P2."""
    pi = tuple(U1.pi[U2.pi[i]] for i in range(len(U2.pi)))
    cz = set(U1.cz) ^ relabel_cz(U2.cz, U1.pi)
    zs = U1.zs ^ permute_mask(U2.zs, U1.pi)
    return Op(pi, cz, zs)


def build_U(C, M):
    pi = C.perm(M)
    cz = set()
    nc = C.lat.ncorner
    for c in range(nc):
        c2 = C.rot_corner(M, c)
        pushed = [C.rot_edge(M, e) for e in C.order[c]]  # order at c2 induced by R
        canon = C.rank[c2]
        for a in range(6):
            for b in range(a + 1, 6):
                l, k = pushed[a], pushed[b]  # l <_pushed k
                if canon[l] > canon[k]:
                    i, j = C.zq(l, c2), C.zq(k, c2)
                    assert C.site_of[i] == C.site_of[j]
                    cz.add((min(i, j), max(i, j)))
    U = Op(pi, cz, 0)
    zs = 0
    for e in C.edges:
        j, k = tuple(e)
        img = U.conj(C.hop(j, k))
        tgt = C.hop(C.rot_corner(M, j), C.rot_corner(M, k))
        assert img[:2] == tgt[:2], 'Z-string mismatch'
        if img[2] != tgt[2]:
            assert (img[2] - tgt[2]) % 4 == 2
            q = bits(C.xmask(C.rot_edge(M, e)))[0]
            zs ^= 1 << q
    return Op(pi, cz, zs)


def main():
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    t0 = time.time()
    import os; SEED = os.environ.get("SEED"); C = CornerCode(L, ordering_seed=None if SEED is None else int(SEED))
    Ms = rotations()
    idx = {tuple(M.flatten()): i for i, M in enumerate(Ms)}
    mul = [[idx[tuple((Ms[a] @ Ms[b]).flatten())] for b in range(24)] for a in range(24)]
    Us = [build_U(C, M) for M in Ms]
    print(f'built 24 U ({time.time()-t0:.1f}s); CZ counts', sorted({len(U.cz) for U in Us}),
          'Z-fix counts', sorted({bin(U.zs).count("1") for U in Us}))
    # exact hop map
    bad = 0
    for g, M in enumerate(Ms):
        for e in C.edges:
            j, k = tuple(e)
            if Us[g].conj(C.hop(j, k)) != C.hop(C.rot_corner(M, j), C.rot_corner(M, k)):
                bad += 1
    print('hop images != rotated hop (all 24 x 2304):', bad)
    # stabilizers -> + stabilizers (exact generator images)
    gens = C.generators()
    gdict = {}
    for g in gens:
        gdict[(g[2][0], g[2][1])] = g[2][2]
    G = StabGroup(C.nq)
    for g in gens:
        G.add(g[2])
    bad_img = 0
    not_gen = 0
    for gi, U in enumerate(Us):
        for g in gens:
            img = U.conj(g[2])
            ph = gdict.get((img[0], img[1]))
            if ph is None:
                not_gen += 1
                s = G.member_sign(img)
                if s != 1:
                    bad_img += 1
            elif ph != img[2]:
                bad_img += 1
    print('stabilizer generator images: not a generator:', not_gen, ' not +stabilizer:', bad_img,
          f'({time.time()-t0:.1f}s)')
    # group law before correction
    links = C.links()
    halfpairs = {}
    for e in links:
        a, b = tuple(e)
        qa, qb = C.Q[(e, a)], C.Q[(e, b)]
        halfpairs[e] = (qa, qb)
    rmask = {e: (1 << qa) | (1 << qb) for e, (qa, qb) in halfpairs.items()}
    q2link = {}
    for e, (qa, qb) in halfpairs.items():
        q2link[qa] = e
        q2link[qb] = e
    cocycle = {}
    exact0 = 0
    for a in range(24):
        for b in range(24):
            P = compose(Us[a], Us[b])
            T = Us[mul[a][b]]
            assert P.pi == T.pi
            dcz = P.cz ^ T.cz
            dz = P.zs ^ T.zs
            assert not dcz, 'CZ leftover'
            # dz must be a union of R masks
            ls = set(q2link[q] for q in bits(dz))
            m = 0
            for e in ls:
                m |= rmask[e]
            assert m == dz, 'leftover not a product of R'
            cocycle[(a, b)] = ls
            if not ls:
                exact0 += 1
    print('pairs exact before R-correction:', exact0, '/ 576; max leftover R count',
          max(len(v) for v in cocycle.values()))
    # orbits of links and freeness
    lid = {e: i for i, e in enumerate(links)}
    rotl = [[lid[C.rot_edge(M, e)] for e in links] for M in Ms]
    seen = set()
    orbits = []
    for i in range(len(links)):
        if i in seen:
            continue
        orb = sorted({rotl[g][i] for g in range(24)})
        seen |= set(orb)
        orbits.append(orb)
    print('link orbits:', len(orbits), 'sizes', sorted({len(o) for o in orbits}))
    # solve f_a + a.f_b + f_ab = c(a,b) for f_g subset of links  (U'_g = R(f_g) U_g)
    # check: R(f_a) U_a R(f_b) U_b = R(f_a) R(a f_b) U_a U_b = R(f_a + a f_b + c(a,b)) U_ab
    f = [set() for _ in range(24)]
    for orb in orbits:
        pos = {l: t for t, l in enumerate(orb)}
        nunk = 24 * len(orb)
        rows = {}
        def var(g, l):
            return g * len(orb) + pos[l]
        eqs = []
        for a in range(24):
            for b in range(24):
                cab = {lid[e] for e in cocycle[(a, b)]} & set(orb)
                for l in orb:
                    # coefficient: f_a(l) + f_b(a^{-1} l) + f_ab(l) = c(a,b)(l)
                    ainv_l = next(m for m in orb if rotl[a][m] == l)
                    v = (1 << var(a, l)) ^ (1 << var(b, ainv_l)) ^ (1 << var(mul[a][b], l))
                    rhs = 1 if l in cab else 0
                    eqs.append((v, rhs))
        piv = {}
        for v, r in eqs:
            while v:
                hb = v.bit_length() - 1
                if hb in piv:
                    pv, pr = piv[hb]
                    v ^= pv
                    r ^= pr
                else:
                    piv[hb] = (v, r)
                    break
            if v == 0 and r:
                raise SystemExit('cocycle not a coboundary on orbit')
        # back substitution, free vars = 0
        sol = 0
        for hb in sorted(piv):
            v, r = piv[hb]
            rest = v ^ (1 << hb)
            val = r ^ (bin(rest & sol).count('1') & 1)
            if val:
                sol |= 1 << hb
        for g in range(24):
            for l in orb:
                if (sol >> var(g, l)) & 1:
                    f[g].add(l)
    Uc = []
    for g in range(24):
        m = 0
        for l in f[g]:
            m |= rmask[links[l]]
        U = Us[g]
        # R(f) U = D' P with D' = R(f) D
        Uc.append(Op(U.pi, U.cz, U.zs ^ m))
    exact = 0
    for a in range(24):
        for b in range(24):
            if compose(Uc[a], Uc[b]).key() == Uc[mul[a][b]].key():
                exact += 1
    print('EXACT operator identities U_a U_b = U_ab after correction:', exact, '/ 576')
    print('U_E is the identity operator:', Uc[0].key() == Op(range(C.nq), [], 0).key())
    # corrected ops still map hops exactly and are on-site
    bad = 0
    for g, M in enumerate(Ms):
        for e in C.edges[::7]:
            j, k = tuple(e)
            if Uc[g].conj(C.hop(j, k)) != C.hop(C.rot_corner(M, j), C.rot_corner(M, k)):
                bad += 1
    print('corrected: hop image failures (sample 1/7 of edges):', bad)
    print('all CZ on-site:', all(C.site_of[i] == C.site_of[j] for U in Uc for (i, j) in U.cz))
    print('R-correction sizes per element:', sorted(len(x) for x in f))
    with open(f'U_L{L}' + ('' if SEED is None else '_s' + SEED) + '.pkl', 'wb') as fh:
        pickle.dump({'Uc': [(U.pi, U.cz, U.zs) for U in Uc]}, fh)
    print(f'time {time.time()-t0:.1f}s')


if __name__ == '__main__':
    main()
