#!/usr/bin/env python3
"""Exact sparse geometry/word control; no time evolution or Hilbert enumeration."""
import json
from fractions import Fraction


def one_size(L):
    assert L >= 16 and L % 8 == 0
    m, n = L // 2, L**3 // 2
    def add(v, d):
        return tuple((v[i] + d[i]) % L for i in range(3))
    dirs = [tuple(s if i == j else 0 for i in range(3)) for j in range(3) for s in (-1, 1)]
    def nei(v):
        return [add(v, d) for d in dirs]
    def is_A(v):
        return sum(v) % 2 == 0
    A = {(x, y, z) for x in range(L) for y in range(L) for z in range(L) if (x+y+z) % 2 == 0}
    allowed = {d % L for d in range(-3, 4)}
    strip = {(x, y, z) for x in range(L) for y in range(L) for z in range(L)
             if (x+y+z) % 2 and (y+z-m) % L in allowed}
    extra = (1, m-4, 0)
    occ = strip | {extra}
    plane = {h for h in A if (h[1]+h[2]-m) % L == 0}
    p, k = L*L//2, 7*L*L//2+1
    assert len(A) == n and len(plane) == p and len(strip) == k-1 and len(occ) == k
    assert extra not in strip
    halo_checks = 0
    for h in plane:
        for dx in range(-3, 4):
            for dy in range(-3, 4):
                for dz in range(-3, 4):
                    if abs(dx)+abs(dy)+abs(dz) <= 3:
                        v = add(h, (dx, dy, dz))
                        if not is_A(v):
                            assert v in strip
                            halo_checks += 1
    def phase(h, sign):
        return (1, 1j, -1, -1j)[(sign*(h[0]//2)) % 4] * (-1 if h[2] % 2 else 1)
    currents = []
    for sign in (1, -1):
        f = {h: phase(h, sign) for h in plane}
        Kf = {}
        for h, val in f.items():
            for b in nei(h):
                assert b in occ
                Kf[b] = Kf.get(b, 0) + val
        Hf = {}
        for b, val in Kf.items():
            for a in nei(b):
                Hf[a] = Hf.get(a, 0) + val
        assert all(val == 2*f.get(a, 0) for a, val in Hf.items())
        assert all(Hf.get(a, 0) == 2*val for a, val in f.items())
        def dx(a, b):
            d = (b[0]-a[0]) % L
            return 1 if d == 1 else (-1 if d == L-1 else 0)
        raw_current = 0j
        for h, val in f.items():
            for b in nei(h):
                for a in nei(b):
                    displacement = dx(h, b)-dx(a, b)
                    raw_current += f.get(a, 0).conjugate() * (-1j*displacement) * val
        assert raw_current == -sign*4*p
        currents.append(str(Fraction(-sign*4*n, n-1+k)))
    pairs = []
    for y in range(L):
        for z in range(L):
            if (y+z-m) % L not in allowed:
                continue
            parity = (1-y-z) % 2
            if (y, z) == (m, 0):
                pairs.append(((L-1, y, z), (1, y, z), (0, y, z)))
                for x in range(3, L-3, 4):
                    pairs.append(((x, y, z), (x+2, y, z), (x+1, y, z)))
            else:
                for j in range(L//4):
                    x = parity+4*j
                    pairs.append(((x, y, z), ((x+2) % L, y, z), ((x+1) % L, y, z)))
    def remove(b, c):
        inds = [i for i, (u, v, a) in enumerate(pairs) if {u, v} == {b, c}]
        assert len(inds) == 1
        pairs.pop(inds[0])
    a = (0, m, 0)
    b1, b2, b3 = (1, m, 0), (L-1, m, 0), (0, m-1, 0)
    remove(b1, b2)
    remove((0, m-1, 0), (2, m-1, 0))
    remove((1, m-2, 0), (3, m-2, 0))
    remove((0, m-3, 0), (2, m-3, 0))
    pairs += [((2, m-1, 0), (3, m-2, 0), (2, m-2, 0)),
              ((1, m-2, 0), (0, m-3, 0), (1, m-3, 0)),
              ((2, m-3, 0), extra, (2, m-4, 0))]
    endpoints = [v for u, v, c in pairs] + [u for u, v, c in pairs]
    centers = [c for u, v, c in pairs]
    assert len(pairs) == 7*L*L//4-1
    assert len(endpoints) == len(set(endpoints)) and set(endpoints) == occ-{b1, b2, b3}
    assert len(centers) == len(set(centers)) and a not in centers
    q = {h: 1 for h in A}
    E, div, used_edges = {}, {}, set()
    endpoint_gauss_checks = 0
    marks = []
    def edge_change(c, b, change):
        nonlocal endpoint_gauss_checks
        assert c in A and b in nei(c) and b not in A
        edge = (c, b)
        assert edge not in used_edges
        used_edges.add(edge)
        E[edge] = E.get(edge, 0) + change
        assert abs(E[edge]) <= 1  # every INPUT was legal too, inductively from E=0
        div[c] = div.get(c, 0) + change
        div[b] = div.get(b, 0) - change
        assert div[c] == q.get(c, 0)-1 and div[b] == q.get(b, 0)
        endpoint_gauss_checks += 2
    def hop(c, b):
        assert q.get(c, 0) == 1 and q.get(b, 0) == 0
        q[c], q[b] = 0, 1
        edge_change(c, b, -1)
    def birth(c, b):
        assert q.get(c, 0) == 0 and q.get(b, 0) == 0
        q[c], q[b] = 1, -1
        edge_change(c, b, 1)
        marks.append((c, b, 1))
    for u, v, c in pairs:
        hop(c, u)
        birth(c, v)
    hop(a, b1)
    birth(a, b2)
    hop(a, b3)
    assert {b for b, charge in q.items() if b not in A and charge} == occ
    assert {h for h in A if not q.get(h, 0)} == {a}
    assert sum(q.values()) == n
    assert sum(charge == -1 for charge in q.values()) == (k-1)//2
    assert len(marks) == (k-1)//2 and marks[-1] == (a, b2, 1)
    assert sum(e*e for e in E.values()) == k and len(E) == k
    for v in A | occ:
        assert div.get(v, 0) == q.get(v, 0)-(1 if v in A else 0)
    return dict(L=L, n=n, occupied_B=k, density=str(Fraction(k, n)), plane=p,
                ordinary_births=len(pairs), original_marks=len(marks), Q2=k,
                currents=currents, halo_checks=halo_checks,
                endpoint_gauss_checks=endpoint_gauss_checks,
                scope='selected exact original word and complete scalar plane incidence; no probability or evolution')


if __name__ == '__main__':
    rows = [one_size(L) for L in (16, 24, 32)]
    print(json.dumps({'cases': rows, 'all_gaussian_integer_identities_exact': True}, indent=2))
    print('TOTAL PASS=3 FAIL=0')
