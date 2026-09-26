#!/usr/bin/env python3
"""Independent periodic matching checks. No author implementation is imported.

Records are a dictionary site -> (permanent identity, signed axis).
Coordinates are explicit tuples, positive labels identify dimers. Run with
--out PATH to write a fresh result without overwriting sealed evidence.
"""
import argparse
from collections import Counter
import itertools as it
import json
import math
from pathlib import Path
import sympy as sp


def vertices(n):
    return list(it.product(range(n), repeat=3))


def shift(x, axis, step, n):
    return tuple((x[j] + (step if j == axis else 0)) % n for j in range(3))


def vector_shift(x, v, n):
    return tuple((x[j] + v[j]) % n for j in range(3))


def content(s):
    return {x: z[1] for x, z in s.items()}


def valid(s, n):
    if len({z[0] for z in s.values()}) != len(s):
        return False
    return all(s.get(shift(x, abs(a)-1, 1 if a > 0 else -1, n), (None, 0))[1] == -a
               for x, (_, a) in s.items())


def pair(s, x, axis, n):
    y = shift(x, axis, 1, n)
    assert x not in s and y not in s
    first = 1 + max((z[0] for z in s.values()), default=0)
    s[x], s[y] = (first, axis+1), (first+1, -axis-1)


def dimers(s, n):
    return [(x, shift(x, a-1, 1, n), a-1) for x, (_, a) in s.items() if a > 0]


def jam(n):
    s = {}
    for c in it.product(range(0, n, 2), repeat=3):
        for p, axis in [((1, 0, 0), 1), ((0, 1, 0), 2), ((0, 0, 1), 0)]:
            pair(s, vector_shift(c, p, n), axis, n)
    assert valid(s, n)
    return s


def columnar(n):
    s = {}
    for x in range(0, n, 2):
        for y, z in it.product(range(n), repeat=2):
            pair(s, (x, y, z), 0, n)
    return s


def odd_sector(n):
    s = columnar(n)
    for x in it.product(range(2), repeat=3):
        del s[x]
    for x, axis in [((1, 0, 0), 1), ((0, 1, 0), 2), ((0, 0, 1), 0)]:
        pair(s, x, axis, n)
    assert valid(s, n)
    return s


def long_two_vacancy(n):
    """Two holes a macroscopic distance apart; demonstrates sharp squared-norm order."""
    s = columnar(n)
    for x in range(n):
        del s[(x, 0, 0)]
    gap = n//2 - 1
    assert gap % 2 == 1
    for x in list(range(1, gap, 2)) + list(range(gap+1, n, 2)):
        pair(s, (x, 0, 0), 0, n)
    assert valid(s, n)
    return s, gap


def swap(s, edges):
    t = dict(s)
    for x, y in edges:
        a, b = s.get(x), s.get(y)
        t.pop(x, None)
        t.pop(y, None)
        if b is not None:
            t[x] = b
        if a is not None:
            t[y] = a
    return t


def cube_edges(base, axis, n):
    other = [j for j in range(3) if j != axis]
    edges = []
    for bits in it.product(range(2), repeat=2):
        v = [0, 0, 0]
        for j, bit in zip(other, bits):
            v[j] = bit
        x = vector_shift(base, v, n)
        edges.append((x, shift(x, axis, 1, n)))
    return edges


def channels(n):
    for base in vertices(n):
        for axis in range(3):
            e = cube_edges(base, axis, n)
            for mask in range(1, 16):
                yield tuple(e[j] for j in range(4) if mask & (1 << j))


def births(s, n):
    return [(x, j) for x in vertices(n) for j in range(3)
            if x not in s and shift(x, j, 1, n) not in s]


def translations(s, n):
    out = []
    for x, y, _ in dimers(s, n):
        for j, sign in it.product(range(3), (-1, 1)):
            a, b = shift(x, j, sign, n), shift(y, j, sign, n)
            if (a in s and a not in (x, y)) or (b in s and b not in (x, y)):
                continue
            t = dict(s)
            t.pop(x)
            t.pop(y)
            t[a], t[b] = s[x], s[y]
            assert valid(t, n)
            out.append((x, y, j, sign))
    return out


def cube_exits(s, n):
    out = []
    for base in vertices(n):
        for normal in range(3):
            directions = [j for j in range(3) if j != normal]
            for order in (directions, directions[::-1]):
                good = True
                for bits in it.product(range(2), repeat=3):
                    x = vector_shift(base, bits, n)
                    axis = order[bits[normal]]
                    want = (axis+1) * (1 if bits[axis] == 0 else -1)
                    good &= s.get(x, (None, 0))[1] == want
                if good:
                    t = swap(s, cube_edges(base, normal, n))
                    assert valid(t, n) and content(t) != content(s)
                    out.append((base, normal))
    assert len(out) == len(set(out))
    return out


def counts(s):
    c = Counter(a for _, a in s.values())
    assert all(c[j] == c[-j] for j in (1, 2, 3))
    return [c[j] for j in (1, 2, 3)]


def parity_gauss(s, n):
    assert valid(s, n)
    holes = set(vertices(n)) - set(s)
    assert all(counts(s)[j] % 2 == sum(x[j] % 2 for x in holes) % 2 for j in range(3))
    # Integer field 6 B_i avoids every floating-point operation.
    field6 = {x: [(-1)**sum(x) * (6 * (s.get(x, (0, 0))[1] == j+1) - 1)
                  for j in range(3)] for x in vertices(n)}
    for x in vertices(n):
        div6 = sum(field6[x][j] - field6[shift(x, j, -1, n)][j] for j in range(3))
        assert div6 == (-6 * (-1)**sum(x) if x in holes else 0)
    assert sum((-1)**sum(x) for x in holes) == 0
    return field6


def finite_fourier(s, n, mode):
    field6 = parity_gauss(s, n)
    phase = lambda x: complex(sp.N(sp.exp(-2*sp.pi*sp.I*sum(a*b for a, b in zip(mode, x))/n), 17))
    b = [sum(phase(x)*field6[x][j]/6 for x in vertices(n))/math.sqrt(n**3) for j in range(3)]
    q = -sum((-1)**sum(x)*phase(x) for x in set(vertices(n))-set(s))/math.sqrt(n**3)
    d = [1-complex(sp.N(sp.exp(-2*sp.pi*sp.I*m/n), 17)) for m in mode]
    norm = sum(abs(z)**2 for z in d)
    assert norm > 0
    assert abs(sum(d[j]*b[j] for j in range(3))-q) < 2e-12
    longitudinal = [z.conjugate()*q/norm for z in d]
    assert abs(sum(d[j]*longitudinal[j] for j in range(3))-q) < 2e-13
    sq = sum(abs(z)**2 for z in longitudinal)
    bound = (n**3-len(s))**2/(n**3*norm)
    assert abs(sq-abs(q)**2/norm) < 2e-13 and sq <= bound+2e-13
    return {'N': n, 'mode': list(mode), 'vacancies': n**3-len(s), 'squared_longitudinal_norm': sq, 'upper_bound': bound}


def exact_complex_control():
    s, n, mode = odd_sector(4), 4, (1, 2, 0)
    f = parity_gauss(s, n)
    phase = lambda x: (-sp.I)**sum(a*b for a, b in zip(mode, x))
    b = sp.Matrix([sp.expand(sum(phase(x)*f[x][j] for x in vertices(n))/48) for j in range(3)])
    q = sp.expand(-sum((-1)**sum(x)*phase(x) for x in set(vertices(n))-set(s))/8)
    d = sp.Matrix([1-(-sp.I)**m for m in mode])
    den = sp.expand((sp.conjugate(d).T*d)[0])
    good = sp.conjugate(d)*q/den
    wrong = d*q/den
    assert sp.expand((d.T*b)[0]-q) == 0
    assert sp.expand((d.T*good)[0]-q) == 0
    wrong_residual = sp.expand((d.T*wrong)[0]-q)
    assert wrong_residual != 0
    squared = sp.simplify((sp.conjugate(good).T*good)[0])
    assert squared == sp.Rational(1, 192)
    return {'d': str(d.T), 'q': str(q), 'B': str(b.T), 'squared_norm': str(squared),
            'bound': str(sp.Rational(1, 96)), 'wrong_unconjugated_projection_residual': str(wrong_residual)}


def cube_census():
    v = list(it.product(range(2), repeat=3))
    edges = [(x, tuple(x[j]+(j == axis) for j in range(3)), axis)
             for x in v for axis in range(3) if x[axis] == 0]
    census, selected = Counter(), []
    for mask in range(1 << len(edges)):
        picked = [e for j, e in enumerate(edges) if mask & (1 << j)]
        ends = [x for e in picked for x in e[:2]]
        if len(set(ends)) != len(ends):
            continue
        census[len(picked)] += 1
        if sorted(e[2] for e in picked) == [0, 1, 2]:
            holes = sorted(set(v)-set(ends))
            assert all(holes[0][j] != holes[1][j] for j in range(3))
            selected.append(holes)
    assert sum(census.values()) == 108 and len(selected) == 8
    return {'matching_census': dict(sorted(census.items())), 'one_dimer_per_axis': len(selected), 'hole_pairs': selected}


def canonical(edges):
    return tuple(sorted(tuple(sorted(e)) for e in edges))


def symmetry_channels():
    n = 4
    original = Counter(canonical(e) for e in channels(n))
    signed_permutations = list(it.product(it.permutations(range(3)), it.product((-1, 1), repeat=3)))
    for perm, signs in signed_permutations:
        tx = lambda x: tuple(signs[j]*x[perm[j]] % n for j in range(3))
        moved = Counter(canonical([(tx(x), tx(y)) for x, y in e]) for e in channels(n))
        assert moved == original
        s = jam(n)
        t = {}
        for x, (identity, a) in s.items():
            old = abs(a)-1
            new = perm.index(old)
            t[tx(x)] = (identity, signs[new]*(new+1)*(1 if a > 0 else -1))
        assert valid(t, n)
    for j in range(3):
        moved = Counter(canonical([(shift(x,j,1,n),shift(y,j,1,n)) for x,y in e]) for e in channels(n))
        assert moved == original
    return {'signed_coordinate_permutations': 48, 'unit_translations': 3,
            'attempted_channels': sum(original.values()), 'distinct_site_permutations': len(original),
            'multiplicity_histogram': dict(sorted(Counter(original.values()).items()))}


def run():
    result = {'method': 'Independent site/identity dictionaries, direct global reciprocity, exact integer Gauss, independent channel lists; no author code imports.'}
    periodic = []
    for n in (4, 6, 8):
        s = jam(n)
        assert len(s) == 3*n**3//4 and counts(s) == [n**3//8]*3
        exits = [len(births(s,n)),len(translations(s,n)),len(cube_exits(s,n))]
        assert exits == [0,0,0]
        parity_gauss(s,n)
        escape = [((0,0,0),(0,1,0)),((0,0,1),(0,1,1)),((1,0,1),(1,1,1))]
        t = swap(s, escape)
        assert valid(t,n) and swap(t,escape) == s
        before = {z[0]:(x,z[1]) for x,z in s.items()}
        after = {z[0]:(x,z[1]) for x,z in t.items()}
        moved = []
        for identity,(x,a) in before.items():
            y,b = after[identity]
            assert a == b
            if x != y:
                assert sum(min((x[j]-y[j])%n,(y[j]-x[j])%n) for j in range(3)) == 1
                moved.append([identity,x,y,a])
        assert len(moved) == 4
        assert (0,1,0) not in t and (0,2,0) not in t
        # Single-vacancy swap alone must be rejected; all three together are essential here.
        assert not valid(swap(s,escape[:1]),n)
        u = dict(t)
        pair(u,(0,1,0),1,n)
        assert len(u) == len(s)+2 and valid(u,n)
        assert all(u[x] == z for x,z in t.items())
        parity_gauss(t,n)
        parity_gauss(u,n)
        o = odd_sector(n)
        assert counts(o) == [n**3//2-3,1,1] and len(o) == n**3-2 and not births(o,n)
        parity_gauss(o,n)
        # Accepted-channel reversibility, including unchanged contents, with all channel multiplicities.
        if n == 4:
            extension = []
            for name, state in [('jam',s),('escaped',t),('after_birth',u),('odd_sector',o),('full_columnar',columnar(n))]:
                accepted = changes = identities = 0
                for edges in channels(n):
                    target = swap(state,edges)
                    if valid(target,n):
                        accepted += 1
                        assert swap(target,edges) == state and counts(target) == counts(state)
                        changes += content(target) != content(state)
                        identities += target != state
                extension.append({'state':name,'accepted_attempts':accepted,'content_changes':changes,'identity_changes':identities})
            result['extension_reversibility_controls'] = extension
        periodic.append({'N':n,'original_exits_birth_translation_cube':exits,'records_before_after':[len(s),len(u)],
                         'moved_old_records':moved,'two_vacancy_counts':counts(o)})
    result['periodic'] = periodic
    result['cube_census'] = cube_census()
    result['channel_covariance'] = symmetry_channels()
    result['exact_complex_Fourier'] = exact_complex_control()
    result['Fourier_controls'] = [finite_fourier(odd_sector(n),n,mode) for n in (4,6) for mode in ((1,0,0),(1,2,0),(1,1,1))]
    sharp = []
    for n in (4,8,16,32):
        s,gap = long_two_vacancy(n)
        parity_gauss(s,n)
        d2 = 4*math.sin(math.pi/n)**2
        squared = 4*math.sin(math.pi*gap/n)**2/(n**3*d2)
        bound = 4/(n**3*d2)
        sharp.append({'N':n,'vacancy_separation':gap,'squared_norm':squared,'upper_bound':bound,'N_times_squared':n*squared})
    result['sharp_squared_norm_scaling'] = {'sequence':sharp,'limit_N_times_squared_norm':'1/pi^2','norm_order':'N^(-1/2), not N^(-1)'}
    odd = {}; pair(odd,(4,0,0),0,5)
    holes = set(vertices(5))-set(odd)
    assert counts(odd)[0] % 2 != sum(x[0]%2 for x in holes)%2
    result['excluded_odd_torus_countercontrol'] = {'N':5,'one_wrapping_x_dimer':True,'Mx_parity':1,'vacancy_x_parity':0}
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('PASS: independent geometry, tracked escape, parity, covariance and Hermitian Fourier controls.')
