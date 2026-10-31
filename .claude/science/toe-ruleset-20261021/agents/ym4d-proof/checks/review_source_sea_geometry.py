#!/usr/bin/env python3
"""Independent combinatorial checks, written before author-runner exposure.

All objects are actual four-dimensional periodic cell/link labels. Ribbon
checks are integer-chain geometry, not a commutative replacement for SU(N).
"""
import itertools as it
import json
import time
from collections import Counter

start = time.time()
bits = list(it.product(range(2), repeat=4))
pairs = list(it.combinations(range(4), 2))
checks, controls, results = {}, {}, []


def move(x, d, s, n):
    z = list(x)
    z[d] = (z[d] + s) % n
    return tuple(z)


def vertices(x, n):
    return {tuple((a+b) % n for a, b in zip(x, bts)) for bts in bits}


def links_on(vs, n):
    return {(x, d) for x in vs for d in range(4) if move(x, d, 1, n) in vs}


def faces_on(vs, n):
    return {(x, a, b) for x in vs for a, b in pairs
            if move(x, a, 1, n) in vs and move(x, b, 1, n) in vs
            and move(move(x, a, 1, n), b, 1, n) in vs}


def boundary(face, n):
    x, a, b = face
    return Counter({(x, a): 1, (move(x, a, 1, n), b): 1,
                    (move(x, b, 1, n), a): -1, (x, b): -1})


def add_counter(out, src, sign=1):
    for x, v in src.items():
        out[x] += sign*v
        if not out[x]:
            del out[x]


def path(x, steps, n):
    bd = Counter()
    for d, s in steps:
        y = move(x, d, s, n)
        bd[(x if s == 1 else y, d)] += s
        x = y
    return x, Counter({k: v for k, v in bd.items() if v})


for L, T in [(3, 2), (5, 2), (3, 4)]:
    n = L*T
    # Translation lets one complete cell establish uniform face/link incidence.
    vs = vertices((n-1,)*4, n)
    links = links_on(vs, n)
    faces = faces_on(vs, n)
    assert len(vs) == 16 and len(links) == 32 and len(faces) == 24
    one_p = ((0,)*4, 0, 1)
    pv = {(0,)*4, (1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0)}
    local_bases = list(it.product((0, n-1), repeat=4))
    incidence = [x for x in local_bases if pv <= vertices(x, n)]
    assert len(incidence) == 4
    link_incidence = {p for x in it.product((0, 1, n-1), repeat=4)
                      for p in faces_on(vertices(x, n), n) if ((0,)*4, 0) in boundary(p, n)}
    assert len(link_incidence) == 6

    def coarse(x):
        return tuple(v//L for v in x)

    def dirty(x):
        blockset = {coarse(z) for z in vertices(x, n)}
        return {(b, d) for b in blockset for d in range(4)} | {
            (move(b, d, -1, T), d) for b in blockset for d in range(4)}

    # One full block-residue class plus wrap representatives covers all cells.
    max_dirty = 0
    max_blocks = 0
    for x in it.product(range(L), repeat=4):
        max_dirty = max(max_dirty, len(dirty(x)))
        max_blocks = max(max_blocks, len({coarse(z) for z in vertices(x, n)}))
    assert max_dirty <= 128 and max_blocks <= 16

    # Full support division uses lifted coordinates relative to each plane.
    rp_bad = 0
    checked_cells = 0
    for axis in range(4):
        for plane in range(n):
            for slab in range(n):
                x = [0]*4
                x[axis] = slab
                xv = vertices(tuple(x), n)
                half = []
                for edge, d in links_on(xv, n):
                    endpoints = [edge[axis], move(edge, d, 1, n)[axis]]
                    rel = [(z-plane) % n for z in endpoints]
                    if all(0 <= z <= n//2 for z in rel):
                        half.append(0 if all(z in (0, n//2) for z in rel) else 1)
                    else:
                        half.append(-1)
                rp_bad += int(1 in half and -1 in half)
                # reflection of cells is lower-coordinate 2a-x-1.
                reflect = lambda z: tuple((2*plane-z[k]) % n if k == axis else z[k] for k in range(4))
                reflected = {reflect(z) for z in xv}
                xb = list(x)
                xb[axis] = (2*plane-slab-1) % n
                assert reflected == vertices(tuple(xb), n)
                checked_cells += 1
    assert rp_bad == 0
    # A bond-plane cuts a unit cell: it cannot use the above factorization.
    controls[f'bond_plane_not_claimed_n{n}'] = True if {0, 1} == {z[0] for z in vertices((0,)*4, n)} else False

    # Exact supports for the most highly contaminated local cell.
    A = ((L-1,)*4,)
    Dset = dirty(A[0])
    E = links_on(vertices(A[0], n), n)
    Ecmax = 0
    for b, d in Dset:
        blocks = {b, move(b, d, 1, T)}
        region = {tuple(L*bb[k]+r[k] for k in range(4)) for bb in blocks for r in it.product(range(L), repeat=4)}
        ec = links_on(region, n)
        Ecmax = max(Ecmax, len(ec))
        E |= ec
    assert Ecmax <= 8*L**4
    touched = set()
    for x, a in E:
        for b in range(4):
            if a == b:
                continue
            for base in [x, move(x, b, -1, n)]:
                touched.add((base, min(a, b), max(a, b)))
    nA = 192+6144*L**4
    assert len(touched) <= nA
    controls[f'omitted_dirty_source_budget_n{n}'] = len(touched) > 192
    results.append({'L': L, 'T': T, 'n': n, 'cell_faces': len(faces), 'cell_links': len(links),
                    'plaquette_cell_multiplicity': len(incidence), 'link_plaquette_multiplicity': len(link_incidence),
                    'max_dirty_links': max_dirty, 'max_endpoint_blocks': max_blocks,
                    'site_reflection_cells_checked': checked_cells, 'split_failures': rp_bad,
                    'max_two_block_links': Ecmax, 'one_cell_enlarged_source_count': len(touched),
                    'source_budget': nA})
checks['cell_incidence_reflection_dirty_support'] = True
controls['mutation_plaquette_multiplicity_three_rejected'] = len(incidence) != 3

# Independent paired contour construction, including a wrapped outgoing block.
ribbon_count = 0
max_area = {}
for L, T in [(3, 2), (5, 2), (3, 4)]:
    n = L*T
    block = (T-1,)*4
    anchor = tuple(L*b+(L-1)//2 for b in block)
    for mu in range(4):
        endpoint_blocks = {block, move(block, mu, 1, T)}
        K = {tuple((L*b[k]+s[k]) % n for k in range(4))
             for b in endpoint_blocks for s in it.product(range(-1, L), repeat=4)}
        assert len(K) <= 2*(L+1)**4
        for offset in it.product(range(-(L-1)//2, (L-1)//2+1), repeat=4):
            for order in it.permutations(range(4)):
                axial = [(d, 1 if offset[d] > 0 else -1) for d in order for _ in range(abs(offset[d]))]
                y, gamma = path(anchor, axial, n)
                yend, leg = path(y, [(mu, 1)]*L, n)
                translated_end, trans = path(move(anchor, mu, L, n), axial, n)
                assert yend == translated_end
                _, straight = path(anchor, [(mu, 1)]*L, n)
                loop = Counter()
                for ch, sign in [(gamma, 1), (leg, 1), (trans, -1), (straight, -1)]:
                    add_counter(loop, ch, sign)
                filled = Counter()
                pos = anchor
                area = 0
                for d, sign in axial:
                    if d != mu:
                        low = pos if sign == 1 else move(pos, d, -1, n)
                        for j in range(L):
                            base = move(low, mu, j, n)
                            face = (base, min(d, mu), max(d, mu))
                            # Rectangle gamma followed by +mu has orientation (d,mu).
                            add_counter(filled, boundary(face, n), sign*(1 if d < mu else -1))
                            assert base in K
                            fvs = {base, move(base, d, 1, n), move(base, mu, 1, n), move(move(base, d, 1, n), mu, 1, n)}
                            assert all(tuple(x//L for x in z) in endpoint_blocks for z in fvs)
                            area += 1
                    pos = move(pos, d, sign, n)
                assert filled == loop
                assert area <= 3*L*(L-1)//2
                max_area[L] = max(max_area.get(L, 0), area)
                ribbon_count += 1
checks['paired_ribbon_boundaries_and_K_witnesses'] = True
controls['mutation_ribbon_area_divided_by_two_rejected'] = all(a > 3*L*(L-1)//4 for L, a in max_area.items())
assert all(checks.values()) and all(controls.values())
print(json.dumps({'checks': checks, 'negative_controls': controls, 'geometry': results,
                  'ribbon_words': ribbon_count, 'max_area': max_area,
                  'scope': 'actual four-dimensional geometry; no continuum or probabilistic conclusion from enumeration',
                  'seconds': time.time()-start}, indent=2))
