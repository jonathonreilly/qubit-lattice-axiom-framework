#!/usr/bin/env python3
"""Exact finite-order normal form and dressed birth controls.

This checks the algebra on a complete nine-state square sector. The locality,
volume-uniform estimates and choice of initial state require the separate
analytic argument; a small matrix cannot establish those statements.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import time

import mpmath as mp
import sympy as sp

import hardcore_record_ring_and_formation_check as source

OUT = Path(__file__).resolve().parent
ORDER = 16


def comm(a, b):
    return a * b - b * a


def formal_conjugate(series, generator, power, order):
    ans = [a.copy() for a in series]
    for degree, a in enumerate(series):
        term = a
        for j in range(1, (order-degree)//power+1):
            term = comm(generator, term) / j
            if not any(term):
                break
            ans[degree+j*power] += term
    return ans


def normal_form(nmat, hop, order):
    dim = nmat.rows
    series = [sp.zeros(dim) for _ in range(order+1)]
    series[0] = nmat
    series[1] = hop
    generators = []
    for power in range(1, order+1):
        a = series[power]
        s = sp.zeros(dim)
        for i in range(dim):
            for j in range(dim):
                grade = nmat[i, i]-nmat[j, j]
                if grade:
                    s[i, j] = a[i, j] / grade
        assert s == -s.T
        generators.append(s)
        series = formal_conjugate(series, s, power, order)
        assert comm(nmat, series[power]) == sp.zeros(dim)
    assert series[1] == sp.zeros(dim)
    for power, a in enumerate(series):
        assert a == a.T and comm(nmat, a) == sp.zeros(dim)
        if power % 2:
            assert a == sp.zeros(dim)
    return generators, series


def as_mp(a):
    return mp.matrix([[mp.mpf(int(x.p))/int(x.q) for x in row] for row in a.tolist()])


def frob(a):
    return mp.sqrt(sum(abs(x)**2 for x in a))


def serialize(a):
    return [[str(x) for x in row] for row in a.tolist()]


def main():
    started = time.monotonic()
    dependency = hashlib.sha256((OUT/'hardcore_record_ring_and_formation_check.py').read_bytes()).hexdigest()
    assert dependency == '3c3cb5c32bd66f95668c5b6667aca711d5cfc6ddd95146ee6d0b92f18cbebbf7'
    basis, hop, nb, count, jumps, _ = source.square_model((1, 0, 1, 0), allow_birth=True)
    dim = len(basis)
    assert dim == 9
    star = [sum((b[x]-b[(x-1)%4])**2 for x in range(4))/sp.Integer(2) for m, b in basis]
    onsite_star = [sum(m[x] == -1 for x in (0, 2))+sum(m[x] == 1 for x in (1, 3)) for m, b in basis]
    assert star == onsite_star
    num = sp.diag(*count)
    p = [i for i, k in enumerate(nb) if k == 0]
    projector = sp.diag(*[int(i in p) for i in range(dim)])
    field = sp.diag(*[sp.Rational(2*b[0]-1, 2) for m, b in basis])
    assert all(j*projector == sp.zeros(dim) for j in jumps)
    mp.mp.dps = 90
    rows = []
    for name, penalty in [('B_occupancy', nb), ('homogeneous_star_onsite_extension', onsite_star)]:
        nmat = sp.diag(*penalty)
        assert all(not hop[i,j] or abs(nmat[i,i]-nmat[j,j]) == 1 for i in range(dim) for j in range(dim))
        generators, series = normal_form(nmat, hop, ORDER)
        assert all(comm(num, s) == sp.zeros(dim) for s in generators)
        assert series[2].extract(p, p) == -2*sp.eye(2)
        assert series[4].extract(p, p) == sp.Matrix([[2,-2],[-2,2]])
        coefficients = {'generators': [serialize(s) for s in generators],
                        'normal_coefficients': [serialize(a) for a in series]}
        numeric = []
        for epsilon in ('0.025', '0.04', '0.06', '0.08'):
            eps = mp.mpf(epsilon)
            y = mp.eye(dim)
            for k, s in enumerate(generators, 1):
                y = mp.expm(eps**k*as_mp(s))*y
            actual = y*(as_mp(nmat)+eps*as_mp(hop))*y.T
            target = sum((eps**k*as_mp(a) for k,a in enumerate(series)), mp.zeros(dim))
            residual = frob(actual-target)
            birth_amp = max(frob(y*as_mp(j)*y.T*as_mp(projector)) for j in jumps)
            observable_change = frob(y*as_mp(field)*y.T-as_mp(field))
            unitary_error = frob(y*y.T-mp.eye(dim))
            assert unitary_error < mp.mpf('1e-75')
            assert residual < mp.mpf('1e8')*eps**(ORDER+1)
            assert birth_amp < 10*eps and observable_change < 10*eps
            row = {'epsilon':epsilon, 'residual_Frobenius':mp.nstr(residual,30),
                   'residual_over_epsilon17':mp.nstr(residual/eps**(ORDER+1),30),
                   'dressed_birth_amplitude_over_epsilon':mp.nstr(birth_amp/eps,30),
                   'local_field_change_over_epsilon':mp.nstr(observable_change/eps,30),
                   'unitarity_residual':mp.nstr(unitary_error,8)}
            numeric.append(row)
            print(json.dumps({'model':name, **row}), flush=True)
        rows.append({'model':name,'dimension':dim,'penalty':penalty,'low_indices':p,
                     'order':ORDER,'all_orders_commute_with_penalty':True,
                     'odd_normal_coefficients_zero':True,
                     'second_low_coefficient':serialize(series[2].extract(p,p)),
                     'fourth_low_coefficient':serialize(series[4].extract(p,p)),
                     'exact_formal_matrices':coefficients,'numerical_controls':numeric})
    result = {'status':'PASS','dependency_sha256':dependency,'basis':basis,
              'checks':rows,'mpmath_decimal_digits':mp.mp.dps,
              'elapsed_seconds':time.monotonic()-started,
              'scope':'Complete nine-state square algebra, not a proof of any volume-uniform limit.'}
    (OUT/'LOCAL_NORMAL_FORM_RECORD_RESULTS.json').write_text(json.dumps(result,indent=2,default=str)+'\n')
    print(json.dumps({'status':'PASS','elapsed_seconds':result['elapsed_seconds']}),flush=True)


if __name__ == '__main__':
    main()
