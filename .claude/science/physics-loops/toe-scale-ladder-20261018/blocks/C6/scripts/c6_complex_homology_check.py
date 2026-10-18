#!/usr/bin/env python3
"""Different-path check of the load-bearing topological input of the C6 lemma (NOTE.md, Lemma 1):
for the 2-complexes underlying the codes (cubic complex for F1-F4; corner complex for F5),
  (H1-loc) every 1-cycle of the graph supported in a cube B is a sum of 2-cells supported in B+1;
  (H^1-loc) every 1-cochain supported on edges of B that vanishes on every 2-cell boundary is the
            coboundary of a 0-cochain supported on vertices of B+1.
This is pure graph/cell homology over GF(2) on an open box of Z^3 (no Pauli operators, no torus),
i.e. an implementation independent of the Pauli-rank counting in c6_tqo_runner.py.
Also checks the torus homology dim H_1 = 3 that fixes k = 3.
"""
import itertools
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c6_lib import Basis, pc, bits   # noqa

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok)
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ''), flush=True)


DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def neg(d): return tuple(-x for x in d)
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def perp(d, e): return dot(d, e) == 0 and d != e
def vadd(v, d, L=None):
    w = tuple(a + b for a, b in zip(v, d))
    return tuple(x % L for x in w) if L else w
def corner(*ds): return tuple(sorted(ds))


CORN = sorted([tuple(sorted((d, e))) for d, e in itertools.combinations(DIRS, 2) if dot(d, e) == 0])


def corner_complex(siteset, L=None):
    """Vertices (v,c); edges: on-site cuboctahedron edges + plaquette links; 2-cells: squares, triangles,
    tubes, plaquettes -- the same cycle families as the repo corner runner. Cells kept only if all their
    vertices lie on sites in siteset (open box) or always on a torus (L given)."""
    V = [(v, c) for v in siteset for c in CORN]
    E = set()
    for v in siteset:
        for c1, c2 in itertools.combinations(CORN, 2):
            s = set(c1) & set(c2)
            if len(s) == 1:
                a = s.pop(); b1 = [d for d in c1 if d != a][0]; b2 = [d for d in c2 if d != a][0]
                if perp(b1, b2) and b1 != neg(b2):
                    E.add(frozenset(((v, c1), (v, c2))))
        for c in CORN:
            for a in c:
                b = [d for d in c if d != a][0]
                w = vadd(v, a, L)
                if w in siteset:
                    E.add(frozenset(((v, c), (w, corner(neg(a), b)))))
    F = []
    for v in siteset:
        for d in DIRS:
            a = [f for f in DIRS if perp(f, d) and f != neg(d)]
            a0 = a[0]; b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]
            ring = [a0, b0, neg(a0), neg(b0)]
            F.append([(v, corner(d, r)) for r in ring])
            w = vadd(v, d, L)
            for i in range(4):
                p, q = ring[i], ring[(i + 1) % 4]
                F.append([(v, corner(d, p)), (w, corner(neg(d), p)), (w, corner(neg(d), q)), (v, corner(d, q))])
        for s in itertools.product((1, -1), repeat=3):
            x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
            F.append([(v, corner(x, y)), (v, corner(y, z)), (v, corner(z, x))])
        for d, e in (((1, 0, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 1)), ((0, 0, 1), (1, 0, 0))):
            F.append([(v, corner(d, e)), (vadd(v, d, L), corner(neg(d), e)),
                      (vadd(vadd(v, d, L), e, L), corner(neg(d), neg(e))), (vadd(v, e, L), corner(d, neg(e)))])
    F = [f for f in F if all(q[0] in siteset for q in f)]
    Fe = []
    for f in F:
        es = [frozenset((f[i], f[(i + 1) % len(f)])) for i in range(len(f))]
        assert all(e in E for e in es), 'cell boundary edge missing'
        Fe.append(es)
    return V, sorted(E, key=str), Fe


def cubic_complex(siteset, L=None):
    V = list(siteset)
    E, F = set(), []
    unit = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    for v in siteset:
        for a in range(3):
            w = vadd(v, unit[a], L)
            if w in siteset:
                E.add(frozenset((v, w)) if L is None or L > 2 else (v, a))
    for v in siteset:
        for a, b in ((0, 1), (1, 2), (0, 2)):
            ea, eb = unit[a], unit[b]
            vs = [v, vadd(v, ea, L), vadd(vadd(v, ea, L), eb, L), vadd(v, eb, L)]
            if all(x in siteset for x in vs):
                F.append([frozenset((vs[i], vs[(i + 1) % 4])) for i in range(4)])
    return V, sorted(E, key=str), F


def analyse(V, E, F, inner_sites, siteof):
    """Return (dim cycles supported in inner, dim of those spanned by cells; dim closed cochains on inner,
    dim of those that are coboundaries of vertex functions)."""
    eid = {e: i for i, e in enumerate(E)}
    vid = {v: i for i, v in enumerate(V)}
    inner_e = [e for e in E if all(siteof(x) in inner_sites for x in e)]
    # cycle space of the inner graph: dim = |E_in| - |V_in| + #components
    Vin = {x for e in inner_e for x in e}
    parent = {x: x for x in Vin}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for e in inner_e:
        a, b = tuple(e)
        parent[find(a)] = find(b)
    ncomp = len({find(x) for x in Vin})
    dim_cyc = len(inner_e) - len(Vin) + ncomp
    # cycles spanned by cells (all cells of the outer complex) intersected with chains on inner edges
    Bc = Basis()
    for f in F:
        m = 0
        for e in f:
            m ^= 1 << eid[e]
        Bc.add(m)
    inner_mask = 0
    for e in inner_e:
        inner_mask |= 1 << eid[e]
    # dim(span(cells) cap C(inner)) = rank(cells) - rank(cells restricted to outside inner)
    Bo = Basis()
    outside = ((1 << len(E)) - 1) ^ inner_mask
    for f in F:
        m = 0
        for e in f:
            m ^= 1 << eid[e]
        Bo.add(m & outside)
    dim_filled = Bc.rank - Bo.rank
    # cochains supported on inner edges, closed on every cell: nullspace size = |E_in| - rank(cell rows restricted)
    Br = Basis()
    for f in F:
        m = 0
        for e in f:
            m ^= 1 << eid[e]
        Br.add(m & inner_mask)
    dim_closed = len(inner_e) - Br.rank
    # coboundaries delta f (f on outer vertices) supported on inner edges
    Bd = Basis()
    Bdo = Basis()
    for v in V:
        m = 0
        for e in E:
            if v in e:
                m ^= 1 << eid[e]
        Bd.add(m)
        Bdo.add(m & outside)
    dim_cobd = Bd.rank - Bdo.rank
    return dim_cyc, dim_filled, dim_closed, dim_cobd


def main():
    print('Local homology of the underlying 2-complexes (open boxes of Z^3)')
    res = []
    for r in (1, 2, 3, 4, 5):
        outer = set(itertools.product(range(-1, r + 1), repeat=3))
        inner = set(itertools.product(range(r), repeat=3))
        V, E, F = cubic_complex(outer)
        a = analyse(V, E, F, inner, lambda x: x)
        res.append(('cubic', r, a))
        print(f'   cubic  r={r}: cycles in B {a[0]}, filled by cells in B+1 {a[1]}; closed cochains on B {a[2]}, coboundaries from B+1 {a[3]}', flush=True)
    for r in (1, 2, 3, 4):
        outer = set(itertools.product(range(-1, r + 1), repeat=3))
        inner = set(itertools.product(range(r), repeat=3))
        V, E, F = corner_complex(outer)
        a = analyse(V, E, F, inner, lambda x: x[0])
        res.append(('corner', r, a))
        print(f'   corner r={r}: cycles in B {a[0]}, filled by cells in B+1 {a[1]}; closed cochains on B {a[2]}, coboundaries from B+1 {a[3]}', flush=True)
    check('(H1-loc) every cycle in a cube B (side 1..5 cubic, 1..4 corner) is a sum of 2-cells in B+1', all(a[0] == a[1] for _, _, a in res))
    check('(H^1-loc) every cell-closed cochain on B is the coboundary of a vertex function on B+1', all(a[2] == a[3] for _, _, a in res))
    print('Torus homology (fixes the expected k = dim H_1 = dim H^1 = 3)')
    for L in (3, 4):
        S = set(itertools.product(range(L), repeat=3))
        for nm, cx in (('cubic', cubic_complex), ('corner', corner_complex)):
            V, E, F = cx(S, L)
            eid = {e: i for i, e in enumerate(E)}
            B = Basis()
            for f in F:
                m = 0
                for e in f:
                    m ^= 1 << eid[e]
                B.add(m)
            # dim H_1 = |E| - rank(d1) - rank(d2); rank(d1) = |V| - 1 (connected)
            h1 = len(E) - (len(V) - 1) - B.rank
            print(f'   {nm} torus L={L}: |V|={len(V)} |E|={len(E)} |F|={len(F)} dim H_1 = {h1}')
            res.append((nm + '_torus', L, h1))
    check('dim H_1(T^3; F2) = 3 for the cubic and the corner complexes on L = 3, 4 tori', all(x[2] == 3 for x in res if x[0].endswith('torus')))
    print(f'TOTAL: PASS={PASS} FAIL={FAIL}')


if __name__ == '__main__':
    main()
