#!/usr/bin/env python3
"""Independent exact finite calculation; no author code or result imports."""
from __future__ import annotations
import hashlib
import itertools as it
import json
from pathlib import Path
import sys
import time

import numpy as np
import sympy as sp

OUT = Path(__file__).resolve().parent
N = 2048
k0 = sp.Rational(11, 10)
gamma = sp.Integer(1)


def exact(x):
    return str(sp.cancel(x))


def determinant3(a):
    return (a[0, 0]*(a[1, 1]*a[2, 2]-a[1, 2]*a[2, 1])
            -a[0, 1]*(a[1, 0]*a[2, 2]-a[1, 2]*a[2, 0])
            +a[0, 2]*(a[1, 0]*a[2, 1]-a[1, 1]*a[2, 0]))


def encoding():
    rotations = []
    for perm in it.permutations(range(3)):
        for signs in it.product((-1, 1), repeat=3):
            r = np.zeros((3, 3), dtype=np.int64)
            for j in range(3):
                r[perm[j], j] = signs[j]
            if determinant3(r) == 1:
                rotations.append(r)
    assert len(rotations) == 24
    def V(r):
        u = np.zeros((4, 4), dtype=np.int64)
        u[0, 0] = 1
        u[1:, 1:] = r
        return np.kron(u, u)
    vs = [V(r) for r in rotations]
    aa = [np.eye(3, dtype=np.int64)[i]*s for i in range(3) for s in (1, -1)]
    bb = [np.array(s, dtype=np.int64) for s in it.product((-1, 1), repeat=3)]
    e = np.array(aa + [np.zeros(3, dtype=np.int64)]*8)
    b = np.array([np.zeros(3, dtype=np.int64)]*6 + bb)
    seeds = [np.array([(7*i*i+3*i+5) % 17-8 for i in range(16)], dtype=np.int64),
             np.array([(11*i*i*i+4*i+1) % 19-9 for i in range(16)], dtype=np.int64)]
    origins = [np.array([1, 0, 0]), np.array([1, 1, 1])]
    tensors = []
    traces = []
    stabilizer_sizes = []
    for origin, seed, labels in zip(origins, seeds, (aa, bb)):
        stab = [v for r, v in zip(rotations, vs) if np.array_equal(r@origin, origin)]
        stabilizer_sizes.append(len(stab))
        s0 = np.eye(16, dtype=np.int64)
        for v in stab:
            z = v@seed
            s0 += np.outer(z, z)
        tr = int(np.trace(s0))
        traces.append(tr)
        for a in labels:
            candidates = [v@s0@v.T for r, v in zip(rotations, vs) if np.array_equal(r@origin, a)]
            assert all(np.array_equal(candidates[0], c) for c in candidates)
            tensors.append(candidates[0])
    assert stabilizer_sizes == [4, 3]
    assert traces == [1168, 2125]
    den = [traces[0]]*6+[traces[1]]*8
    rho = [sp.Matrix(t.tolist())/d for t, d in zip(tensors, den)]
    tau = sum(rho, sp.zeros(16))/14
    rx = (rho[2]-rho[3])/2
    ry = sum((int(b[a, 2])*rho[a] for a in range(14)), sp.zeros(16))/8
    assert tau.trace() == 1 and rx.trace() == 0 and ry.trace() == 0
    print('Encoding rebuilt from integer stabilizer twirls; inverting tau.', flush=True)
    tinv = tau.inv(method='DM')
    assert tau*tinv == sp.eye(16)
    metric = sp.Matrix([[(r*tinv*s).trace() for s in (rx, ry)] for r in (rx, ry)])
    assert metric == metric.T and metric[0, 0] > 0 and metric.det() > 0
    quantum = {
        'stabilizer_sizes': stabilizer_sizes,
        'traces': traces,
        'tau_numerator_denominator': 14*1168*2125,
        'tau_integer_numerator': [[int(x) for x in row] for row in (tau*(14*1168*2125)).tolist()],
        'RX_integer_numerator_denominator': 2*1168,
        'RX_integer_numerator': [[int(x) for x in row] for row in (rx*(2*1168)).tolist()],
        'RY_integer_numerator_denominator': 8*2125,
        'RY_integer_numerator': [[int(x) for x in row] for row in (ry*(8*2125)).tolist()],
        'metric': [[exact(x) for x in row] for row in metric.tolist()],
        'metric_decimal': [[str(sp.N(x, 24)) for x in row] for row in metric.tolist()],
        'inverse_verified_exactly': True,
        'metric_ratio_Gyy_Gxx': exact(metric[1, 1]/metric[0, 0]),
    }
    return e, b, metric, quantum


def microscopic_checks(e, b):
    # The Cartesian table is our finite control; it uses actual four-context rates.
    states = np.array(list(it.product(range(14), repeat=4)), dtype=np.int64)
    l, a, c, r = states.T
    cross = np.cross(e[:, None, :], b[None, :, :])+np.cross(e[None, :, :], b[:, None, :])
    directions = [np.eye(3, dtype=np.int64)[i]*s for i in range(3) for s in (1, -1)]
    basisnums = (e[:, 1], b[:, 2])
    basisdens = (2, 8)
    rows = []
    minrate, maxrate = sp.Integer(100), sp.Integer(-100)
    for delta in directions:
        sn = cross@delta  # S = sn/2, gamma=1.
        hn = sn[l, a]+sn[a, r]-sn[l, c]-sn[c, r]
        rate_num = 22+5*hn  # actual c = rate_num/40.
        minrate = min(minrate, sp.Rational(int(rate_num.min()), 40))
        maxrate = max(maxrate, sp.Rational(int(rate_num.max()), 40))
        assert rate_num.min() > 0
        # Sum h on a four-site route cycle. For this control all 14^4 words occur.
        hsum = np.zeros(len(states), dtype=np.int64)
        for j in range(4):
            ll, aa, cc, rr = (states[:, (j+s) % 4] for s in (-1, 0, 1, 2))
            hsum += sn[ll, aa]+sn[aa, rr]-sn[ll, cc]-sn[cc, rr]
        assert not np.any(hsum)
        # Actual reverse rate: external l,r fixed and the two endpoint colors swap.
        reverse_hn = sn[l, c]+sn[c, r]-sn[l, a]-sn[a, r]
        assert np.array_equal(reverse_hn, -hn)
        # Constant product current exactly zero.
        for out in range(14):
            assert int(np.sum(rate_num*((a == out).astype(np.int64)-(c == out).astype(np.int64)))) == 0
        if np.array_equal(delta, np.array([1, 0, 0])):
            # Physically this winding route is fixed; its local algebra was still checked.
            continue
        for slot in range(4):
            for bn, bd in zip(basisnums, basisdens):
                weighted = rate_num*bn[states[:, slot]]
                got = sp.Matrix([sp.Rational(int(np.sum(weighted*((a == out).astype(np.int64)-(c == out).astype(np.int64)))), 40*bd*14**3) for out in range(14)])
                f = sp.Matrix(bn.tolist())/bd
                expected = (k0*f/2 if slot == 1 else -k0*f/2 if slot == 2 else sp.Matrix(sn.tolist())*f/56)
                assert got == expected, (delta, slot, bd, got, expected)
                rows.append({'direction': list(map(int, delta)), 'varied_slot': slot,
                             'basis_denominator': bd, 'full_vector': list(map(exact, got))})
    assert minrate == sp.Rational(1, 20) and maxrate == sp.Rational(21, 20)
    return {'number_of_words_per_direction': len(states), 'directions_for_stationarity': 6,
            'linearized_full_vector_cases': rows, 'number_linearized_cases': len(rows),
            'rate_min': exact(minrate), 'rate_max': exact(maxrate),
            'all_periodic_stationarity_coboundaries_zero': True}, cross


def spatial_and_metric_checks(e, b, cross, G):
    h = N//2
    xx = np.arange(N, dtype=np.int64)
    tx = h-2*np.abs(xx-h)
    ty = np.roll(tx, N//4)
    def lap(x, step):
        return np.roll(x, -step)+np.roll(x, step)-2*x
    def drive(x):
        return np.roll(x, -4)+np.roll(x, 2)-np.roll(x, -2)-np.roll(x, 4)
    sx = lap(tx, 2)+4*lap(tx, 1)
    sy = lap(ty, 2)+4*lap(ty, 1)
    dx, dy = drive(tx), drive(ty)
    mean = lambda a, c: sp.Rational(int(np.dot(a, c)), N*h*h)
    A = k0*mean(tx, sx)/2
    C = mean(tx, dy)
    assert A == k0*mean(ty, sy)/2
    assert mean(tx, sy) == mean(ty, sx) == mean(tx, dx) == mean(ty, dy) == 0
    assert mean(ty, dx) == -C
    assert A == -64*k0*(N-1)/N**3
    assert C == sp.Rational(8*(N*N-144), N**3)
    # Independently construct full fourteen-component generator derivative from
    # all incoming/outgoing actual channel linearizations on the complete profile.
    # f_x(a) = [4 e_a2 tx_x + b_a3 ty_x]/(8h).
    pnum = 4*tx[:, None]*e[None, :, 1]+ty[:, None]*b[None, :, 2]
    # A common denominator for the derivative is 8h*280:
    # (k0/2) = 154/280; (S/28) = sn/56 = 5 sn/280.
    fullnum = np.zeros((N, 14), dtype=np.int64)
    for i in range(3):
        for sign in (1, -1):
            delta = np.eye(3, dtype=np.int64)[i]*sign
            shift = int(delta[0]-1)
            if i == 0 and sign == 1:
                continue
            sn = cross@delta
            symmetric = np.roll(pnum, shift, axis=0)+np.roll(pnum, -shift, axis=0)-2*pnum
            stencil = (np.roll(pnum, 2*shift, axis=0)+np.roll(pnum, -shift, axis=0)
                       -np.roll(pnum, shift, axis=0)-np.roll(pnum, -2*shift, axis=0))
            fullnum += 154*symmetric+5*(stencil@sn.T)
    # Scalar component formula uses common denominator 280h.
    xdotnum = 154*sx-10*dy
    ydotnum = 154*sy-40*dx
    expected = 4*xdotnum[:, None]*e[None, :, 1]+ydotnum[:, None]*b[None, :, 2]
    assert np.array_equal(fullnum, expected)
    # No numerical approximation enters either evaluation of the Q derivative.
    scalar_coefficients = [sp.Rational(int(np.dot(tx, xdotnum)), 280*N*h*h),
                           sp.Rational(int(np.dot(ty, ydotnum)), 280*N*h*h),
                           sp.Rational(int(np.dot(tx, ydotnum)+np.dot(ty, xdotnum)), 280*N*h*h)]
    Q = sp.cancel(2*(G[0, 0]*scalar_coefficients[0]+G[1, 1]*scalar_coefficients[1]+G[0, 1]*scalar_coefficients[2]))
    Qclosed = sp.cancel(2*(G[0, 0]+G[1, 1])*A-(G[0, 0]-4*G[1, 1])*C/14)
    assert Q == Qclosed
    Qspec = (-sp.Integer(1468294)*G[0, 0]+sp.Integer(5085081)*G[1, 1])/sp.Integer(4697620480)
    assert Q == Qspec
    stirring = sp.cancel(2*(G[0, 0]+G[1, 1])*A)
    drive_contribution = sp.cancel(-(G[0, 0]-4*G[1, 1])*C/14)
    classical = sp.cancel(2*(sp.Integer(7)+sp.Rational(7, 4))*A)
    assert classical < 0 and stirring < 0
    assert np.all(lap(np.ones(N, dtype=np.int64), 1) == 0)
    assert np.all(drive(np.ones(N, dtype=np.int64)) == 0)
    # Alternative signed quadrature profile has the opposite antisymmetric term.
    opposite = sp.cancel(stirring-drive_contribution)
    result = {'N': N, 'number_of_pairs': N**3//2, 'microscopic_time_rate_k0': exact(k0),
              'gamma': exact(gamma), 'A': exact(A), 'C': exact(C),
              'direct_sum_scalar_coefficients': list(map(exact, scalar_coefficients)),
              'Gxy_coefficient_zero': scalar_coefficients[2] == 0,
              'full_fourteen_component_spatial_identity_exact': True,
              'Q_derivative_per_pair': exact(Q), 'Q_derivative_decimal': str(sp.N(Q, 40)),
              'Q_derivative_sign': int(sp.sign(Q)),
              'Euler_accelerated_derivative_per_pair': exact(N*Q),
              'stirring_contribution': exact(stirring), 'drive_contribution': exact(drive_contribution),
              'stirring_decimal': str(sp.N(stirring, 25)), 'drive_decimal': str(sp.N(drive_contribution, 25)),
              'classical_Fisher_control': exact(classical),
              'opposite_quadrature_derivative': exact(opposite),
              'opposite_quadrature_decimal': str(sp.N(opposite, 25)),
              'stationary_constant_profile_derivative': '0',
              'minimum_unperturbed_probability': '1/14',
              'sufficient_open_tangent_parameter_range': '|theta| < 1/7'}
    return result


def marginal_reduction_control():
    t = sp.diag(sp.Rational(1, 3), sp.Rational(2, 3))
    r1 = sp.Matrix([[sp.Rational(1, 5), sp.Rational(1, 7)], [sp.Rational(1, 7), -sp.Rational(1, 5)]])
    r2 = sp.Matrix([[0, 1], [1, 0]])/11
    s = sp.kronecker_product(t, t)
    d = sp.kronecker_product(r1, t)+sp.kronecker_product(t, r2)
    z = sp.diag(1, -1)
    # The final term has both marginals zero and is allowed in the full derivative.
    derivative = sp.kronecker_product(r2, t)+2*sp.kronecker_product(t, r1)+sp.kronecker_product(z, z)/13
    direct = (derivative*s.inv()*d+d*s.inv()*derivative).trace()
    reduced = (r2*(t.inv()*r1+r1*t.inv())).trace()+(2*r1*(t.inv()*r2+r2*t.inv())).trace()
    assert direct == reduced
    # Two-positive contraction check: dephasing fixes diagonal t, with a genuine loss.
    pinched = sp.diag(r1[0, 0], r1[1, 1])
    before = (r1*t.inv()*r1).trace()
    after = (pinched*t.inv()*pinched).trace()
    assert before > after
    return {'two_site_with_zero_marginal_correlation_derivative': exact(direct),
            'reduced_value': exact(reduced), 'dephasing_Q_before': exact(before),
            'dephasing_Q_after': exact(after)}


def main():
    start = time.monotonic()
    sources = json.loads((OUT/'SOURCES.json').read_text())
    for row in sources['sources']:
        data = Path(row['path']).read_bytes()
        assert len(data) == row['bytes'] and hashlib.sha256(data).hexdigest() == row['sha256']
    e, b, G, quantum = encoding()
    print('Exact local metric:', quantum['metric'], flush=True)
    microscopic, cross = microscopic_checks(e, b)
    print('Microscopic current cases:', microscopic['number_linearized_cases'], flush=True)
    spatial = spatial_and_metric_checks(e, b, cross, G)
    toy = marginal_reduction_control()
    result = {'boundary': 'Independent implementation before third-campaign author source/result access.',
              'quantum': quantum, 'microscopic': microscopic, 'spatial': spatial, 'toy_controls': toy,
              'runtime_seconds': time.monotonic()-start,
              'versions': {'python': sys.version, 'numpy': np.__version__, 'sympy': sp.__version__}}
    (OUT/'RESULTS.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(spatial, indent=2), flush=True)
    print('All exact assertions passed.', flush=True)


if __name__ == '__main__':
    main()
