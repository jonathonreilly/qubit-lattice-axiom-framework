#!/usr/bin/env python3
"""Independent finite pointer-code and full-generator inversion checks."""
from __future__ import annotations
from pathlib import Path
from itertools import product, permutations
from fractions import Fraction
import datetime
import hashlib
import json
import sys
import time

import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
D = 14
LABELS = [tuple(int(j == i)*sign for j in range(3)) for i in range(3) for sign in (1, -1)]
LABELS += list(product((-1, 1), repeat=3))
E = np.array(LABELS[:6]+[(0, 0, 0)]*8, dtype=np.int64)
B = np.array([(0, 0, 0)]*6+LABELS[6:], dtype=np.int64)
LOOKUP = {z: i for i, z in enumerate(LABELS)}


def encode_and_vacuum():
    cols = []
    for label in LABELS:
        u = s.Matrix((1,)+label)
        cols.append(s.kronecker_product(u, u, u))
    F = s.Matrix.hstack(*cols)
    G = F.T*F
    for a in range(D):
        for b in range(D):
            assert G[a, b] == (1+sum(x*y for x, y in zip(LABELS[a], LABELS[b])))**3
    lam = s.symbols('lam')
    cp = G.charpoly(lam).as_expr()
    expected = (lam*lam-92*lam+192)*(lam*lam-88*lam+384)**3*(lam-6)**2*(lam-48)**4
    assert s.expand(cp-expected) == 0
    determinant = int(G.det(method='domain-ge'))
    assert determinant == 192*384**3*6**2*48**4 > 0
    assert F.to_DM().rank() == 14
    vnum = s.zeros(64, 1)
    idx = lambda a, b, c: 16*a+4*b+c
    for i in range(1, 4):
        vnum[idx(0, i, i)] += 1
        vnum[idx(i, 0, i)] -= 1
    assert (vnum.T*vnum)[0] == 6
    assert F.T*vnum == s.zeros(14, 1)
    rotations = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            R = s.zeros(3)
            for j in range(3):
                R[perm[j], j] = signs[j]
            if R.det() == 1:
                rotations.append(R)
    for R in rotations:
        U = s.diag(1, R)
        V = s.kronecker_product(U, U, U)
        P = s.zeros(D)
        for a, label in enumerate(LABELS):
            new = tuple(map(int, R*s.Matrix(label)))
            P[LOOKUP[new], a] = 1
        assert V*F == F*P
        assert G*P == P*G
        assert V*vnum == vnum
    return {'dimension': 64, 'occupied_columns': D, 'rank': 14,
            'Gram_characteristic_polynomial': str(s.factor(cp)),
            'Gram_determinant': str(determinant),
            'Gram_eigenvalues': {'46-2*sqrt(481)': 1, '46+2*sqrt(481)': 1,
                                '44-4*sqrt(97)': 3, '44+4*sqrt(97)': 3,
                                '6': 2, '48': 4},
            'proper_cubic_transformations_checked': len(rotations),
            'vacuum_numerator_norm_squared': 6,
            'vacuum_all_occupied_inner_products': [0]*D,
            'vacuum_rotation_residuals_zero': True,
            'orthonormalization_scope': 'G>0 and W=F G^(-1/2) imply W^dagger W=I exactly; covariance follows from the checked commutation GP=PG by spectral functional calculus.'}


def support_reduction():
    N = 12
    diff = {(0, 0, 0), (10, 0, 0), (8, 0, 0)}
    black = [u for u in product(range(N), repeat=3) if sum(u) % 2 == 0]
    directions = [tuple(int(j == i)*sign for j in range(3)) for i in range(3) for sign in (1, -1)]
    hits = []
    all_count = 0
    for u in black:
        for delta in directions:
            if delta == (1, 0, 0):
                continue
            a = tuple(delta[j]-int(j == 0) for j in range(3))
            sites = [tuple((u[j]+shift*a[j]) % N for j in range(3)) for shift in (-1, 0, 1, 2)]
            assert len(set(sites)) == 4
            all_count += 1
            if diff <= set(sites):
                hits.append({'origin': u, 'delta': delta, 'sites': sites})
    assert all_count == 864*5
    assert [r['origin'] for r in hits] == [(0, 0, 0), (10, 0, 0)]
    assert all(r['delta'] == (-1, 0, 0) for r in hits)
    return {'black_sites': len(black), 'nonidentity_channels': all_count,
            'different_sites': sorted(diff), 'contributing_four_context_channels': hits}


def convolve(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def poly_product(factors):
    out = [1]
    for factor in factors:
        out = convolve(out, factor)
    return out


def invert_generator():
    # In full configurations I and O differ at exactly these three anchors.
    alpha = LOOKUP[(-1, -1, -1)]
    beta = LOOKUP[(1, -1, -1)]
    chi = LOOKUP[(0, 1, 0)]
    neutral = LOOKUP[(1, 0, 0)]
    I = (alpha, beta, chi)
    O = (chi, alpha, beta)
    delta = np.array([-1, 0, 0], dtype=np.int64)
    sn = (np.cross(E[:, None, :], B[None, :, :])+np.cross(E[None, :, :], B[:, None, :]))@delta
    assert np.array_equal(sn, sn.T)
    # S=sn/2. The two surviving three-site parts have rate hn/8.
    polys = [[0]*7, [0]*7]
    numeric_three = [0, 0]
    for st in product(range(D), repeat=3):
        invpoly = poly_product([[D*int(st[j] == I[j]), -1] for j in range(3)])
        oldpoly = poly_product([[D*int(O[j] == st[j]), 1-D*int(O[j] == st[j])] for j in range(3)])
        # eta=1/2: T entries (1+14 delta)/28; inverse entries (28 delta-1)/14.
        invhalf = int(np.prod([28*int(st[j] == I[j])-1 for j in range(3)]))
        oldhalf = int(np.prod([1+14*int(O[j] == st[j]) for j in range(3)]))
        for edge in (0, 1):
            nxt = list(st)
            nxt[edge], nxt[edge+1] = nxt[edge+1], nxt[edge]
            hn = int(sn[st[0], st[2]]-sn[st[1], st[2]]) if edge == 0 else int(sn[st[0], st[1]]-sn[st[0], st[2]])
            newpoly = poly_product([[D*int(O[j] == nxt[j]), 1-D*int(O[j] == nxt[j])] for j in range(3)])
            contrib = convolve(invpoly, [a-b for a, b in zip(newpoly, oldpoly)])
            for degree, value in enumerate(contrib):
                polys[edge][degree] += hn*value
            newhalf = int(np.prod([1+14*int(O[j] == nxt[j]) for j in range(3)]))
            numeric_three[edge] += hn*invhalf*(newhalf-oldhalf)
    eta = s.symbols('eta')
    values = [s.factor(sum(c*eta**j for j, c in enumerate(poly))/(8*D**6*(1-eta)**3)) for poly in polys]
    # Independently sum the complete four-context channel, including the positive
    # constant rate and both context contributions. This does not drop jumps by hand.
    input4 = [(neutral,)+I, I+(neutral,)]
    output4 = [(neutral,)+O, O+(neutral,)]
    fullhalf = []
    constant_half = []
    ranges = []
    for ix, ox in zip(input4, output4):
        total, stir, minrate, maxrate = 0, 0, 10**9, -10**9
        for st in product(range(D), repeat=4):
            l, a, b, r = st
            hn = int(sn[l, a]+sn[a, r]-sn[l, b]-sn[b, r])
            rn = 22+5*hn  # c=rn/40.
            minrate, maxrate = min(minrate, rn), max(maxrate, rn)
            inv = 1
            before = 1
            after = 1
            swapped = (l, b, a, r)
            for j in range(4):
                inv *= 28*int(st[j] == ix[j])-1
                before *= 1+14*int(ox[j] == st[j])
                after *= 1+14*int(ox[j] == swapped[j])
            weight = inv*(after-before)
            total += rn*weight
            stir += 22*weight
        fullhalf.append(s.Rational(total, 40*14**4*28**4))
        constant_half.append(s.Rational(stir, 40*14**4*28**4))
        ranges.append((str(s.Rational(minrate, 40)), str(s.Rational(maxrate, 40))))
    for edge in range(2):
        assert values[edge].subs(eta, s.Rational(1, 2)) == fullhalf[edge]
        assert s.Rational(numeric_three[edge], 8*14**3*28**3) == fullhalf[edge]
        assert constant_half[edge] == 0
    total = s.factor(sum(values))
    # Verify the local preparation inverse exactly as an independent support control.
    T = (1-eta)*s.eye(D)+eta*s.ones(D)/D
    Tinverse = (s.eye(D)-eta*s.ones(D)/D)/(1-eta)
    assert (T*Tinverse-s.eye(D)).applyfunc(s.factor) == s.zeros(D)
    # Also check the transverse local metric in the noisy pointer encoding.
    RX = s.diag(*list((1-eta)*s.Matrix(E[:, 1].tolist())/2))
    RY = s.diag(*list((1-eta)*s.Matrix(B[:, 2].tolist())/8))
    u, v, cross = s.factor((D*RX*RX).trace()), s.factor((D*RY*RY).trace()), s.factor((D*RX*RY).trace())
    assert u == 7*(eta-1)**2 and v == s.Rational(7, 4)*(eta-1)**2 and cross == 0
    return {'input_color_indices': I, 'output_color_indices': O, 'all_other_color_index': neutral,
            'label_order': LABELS, 'two_local_symbolic_entries': list(map(str, values)),
            'full_generator_symbolic_entry': str(total),
            'two_full_four_context_entries_at_eta_half': list(map(str, fullhalf)),
            'full_generator_entry_at_eta_half': str(sum(fullhalf)),
            'symbolic_numerator_polynomials_before_cancellation': polys,
            'actual_rate_ranges_for_full_sums': ranges,
            'constant_stirring_contributions': list(map(str, constant_half)),
            'symbolic_inverse_verified': True,
            'local_metric': {'u': str(u), 'v': str(v), 'cross': str(cross)},
            'eta_zero_limit': str(s.limit(total, eta, 0)),
            'eta_one_limit_from_below': str(s.limit(total, eta, 1, dir='-'))}


def main():
    started = time.monotonic()
    sources = json.loads((HERE/'SOURCES.json').read_text())
    for r in sources['sources']:
        data = Path(r['path']).read_bytes()
        assert len(data) == r['bytes'] and hashlib.sha256(data).hexdigest() == r['sha256']
    code = encode_and_vacuum()
    print('Exact code rank, Gram spectrum, all proper cubic transformations and vacuum checked.', flush=True)
    support = support_reduction()
    print('Full route support reduction:', json.dumps(support), flush=True)
    inverse = invert_generator()
    result = {'boundary': 'Independent pre-author-source calculation.', 'pointer_code': code,
              'support': support, 'noisy_intertwiner': inverse, 'runtime_seconds': time.monotonic()-started,
              'versions': {'python': sys.version, 'numpy': np.__version__, 'sympy': s.__version__}}
    (HERE/'RESULTS.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
