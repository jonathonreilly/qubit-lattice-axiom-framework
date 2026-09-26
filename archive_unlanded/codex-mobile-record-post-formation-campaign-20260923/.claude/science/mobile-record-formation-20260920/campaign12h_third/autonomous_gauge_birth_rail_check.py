#!/usr/bin/env python3
"""Exact finite link algebra, packet moments, and a rational Bessel control.

Infinite-rail convergence is an analytic argument in the companion note.
No finite matrix computation is claimed to establish an infinite-time limit.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import itertools
import json
import math
import sympy as s

HERE = Path(__file__).resolve().parent


def local_system():
    basis = list(itertools.product((0, 1, -1), (0, 1, -1), (0, 1)))
    ix = {row: j for j, row in enumerate(basis)}
    V = s.SparseMatrix(18, 18, {
        (ix[(1, -1, 1)], ix[(0, 0, 0)]): 1,
        (ix[(-1, 1, 0)], ix[(0, 0, 1)]): 1,
    })
    N = s.diag(*[int(a != 0) + int(b != 0) for a, b, e in basis])
    E = s.diag(*[s.Rational(2*e-1, 2) for a, b, e in basis])
    gx = E - s.diag(*[a for a, b, e in basis])
    gy = -E - s.diag(*[b for a, b, e in basis])
    fuel = s.diag(1, 0)
    A = s.kronecker_product(V, s.Matrix([[0, 0], [1, 0]]))
    C = s.SparseMatrix(A + A.T)
    resource = s.kronecker_product(N, s.eye(2)) + 2*s.kronecker_product(s.eye(18), fuel)
    assert C**3 == C and C*resource == resource*C
    for g in (gx, gy):
        G = s.kronecker_product(g, s.eye(2))
        assert G*C == C*G
    return C, s.SparseMatrix(resource), V, (gx, gy)


def finite_link_check():
    C, resource, V, gauss = local_system()
    size = 36
    I = s.SparseMatrix(s.eye(size))
    rows = []
    # Two rational specializations, including deterministic formation.
    for cosine, sine in [(s.Rational(3, 5), s.Rational(4, 5)), (s.S.Zero, s.S.One)]:
        U = I + (cosine-1)*C*C - s.I*sine*C
        assert U.adjoint()*U == I
        assert U*resource == resource*U
        clock_positions = list(range(-2, 4))
        d = len(clock_positions)
        h = s.SparseMatrix(d, d, {})
        direct = s.SparseMatrix(d*size, d*size, {})
        W = s.SparseMatrix(d*size, d*size, {})
        for x, position in enumerate(clock_positions):
            W[x*size:(x+1)*size, x*size:(x+1)*size] = I if position <= 0 else U
            if x+1 < d:
                h[x+1, x] = h[x, x+1] = -1
                gate = U if position == 0 else I
                direct[(x+1)*size:(x+2)*size, x*size:(x+1)*size] = -gate
                direct[x*size:(x+1)*size, (x+1)*size:(x+2)*size] = -gate.adjoint()
        free = s.kronecker_product(h, I)
        assert direct == W*free*W.adjoint()
        assert direct == direct.adjoint()
        total_resource = s.kronecker_product(s.eye(d), resource)
        assert total_resource*direct == direct*total_resource
        for g in gauss:
            G = s.kronecker_product(s.eye(d), s.kronecker_product(g, s.eye(2)))
            assert G*direct == direct*G
        # Plane-wave matching at both sides of the defect, for arbitrary
        # nonzero z. U is transmitted without reflection or k-dependent gate.
        z = s.symbols('z', nonzero=True)
        energy = -(z+1/z)
        psi = lambda j: z**j * (I if j <= 0 else U)
        at_zero = -psi(-1)-U.adjoint()*psi(1)-energy*psi(0)
        at_one = -U*psi(0)-psi(2)-energy*psi(1)
        assert at_zero.applyfunc(s.expand) == s.zeros(size)
        assert at_one.applyfunc(s.expand) == s.zeros(size)
        fuel_indices = list(range(0, size, 2))
        M0 = U.extract(fuel_indices, fuel_indices)
        M1 = U.extract(list(range(1, size, 2)), fuel_indices)
        P = V.T*V
        assert M0 == s.eye(18)-P+cosine*P
        assert M1 == -s.I*sine*V
        rows.append({'cosine': str(cosine), 'sine': str(sine),
                     'clock_sites': d, 'total_matrix_dimension': d*size,
                     'direct_defect_equals_unitary_conjugate': True,
                     'exact_Gauss_and_resource_conservation': True,
                     'both_plane_wave_boundary_equations_exact': True})
    return rows


def packet_moments():
    rows = []
    for M in range(1, 17):
        L = 2*M
        coordinates = list(range(-L-3, -L+M+4))
        d = len(coordinates)
        loc = {x: i for i, x in enumerate(coordinates)}
        psi = s.zeros(d, 1)
        for r in range(M+1):
            psi[loc[-L+r]] = s.I**r*s.binomial(M, r)
        norm = (psi.adjoint()*psi)[0]
        assert norm == s.binomial(2*M, M)
        X = s.diag(*coordinates)
        S = s.zeros(d)
        for j in range(d-1):
            S[j+1, j] = 1
        velocity = s.I*(S-S.T)
        ev = lambda A: s.simplify((psi.adjoint()*A*psi)[0]/norm)
        ex = -L+s.Rational(M, 2)
        evv = 2*s.Rational(M, M+1)
        bx = s.Rational(M*M, 4*(2*M-1))
        cv = 4*s.Rational(2*M+1, (M+1)**2*(M+2))
        assert ev(X) == ex and ev(velocity) == evv
        assert ev(X*X)-ex**2 == bx
        assert s.factor(ev(velocity*velocity)-evv**2-cv) == 0
        assert ev(X*velocity+velocity*X)-2*ex*evv == 0
        rows.append({'M': M, 'position_variance': str(bx),
                     'mean_velocity_at_J1': str(evv), 'velocity_variance_at_J1': str(cv),
                     'symmetrized_covariance': '0'})
    a, b, c, v, t = s.symbols('a b c v t', positive=True)
    ratio = (b+c*t*t)/(v*t-a)**2
    assert s.factor(s.diff(ratio, t)+2*(a*c*t+v*b)/(v*t-a)**3) == 0
    bounds = []
    for M, L, T in [(16, 32, 40), (40, 80, 100), (80, 160, 200)]:
        mu = -L+s.Rational(M, 2)+2*s.Rational(M, M+1)*T
        variance = s.Rational(M*M, 4*(2*M-1))+4*s.Rational(2*M+1, (M+1)**2*(M+2))*T*T
        bound = s.factor(variance/(variance+mu*mu))
        assert mu > 0
        bounds.append({'M': M, 'L': L, 'T': T, 'mean_position': str(mu),
                       'position_variance_at_T': str(variance),
                       'uniform_later_nonpassage_bound': str(bound),
                       'decimal_bound': float(bound)})
    return {'exact_finite_sum_controls': rows, 'uniform_time_bound_derivative_checked': True,
            'finite_time_bounds': bounds}


def directional_tail():
    rows = []
    for M in (1, 2, 4, 8, 16, 40, 80):
        central = s.binomial(2*M, M)
        odd_sum = sum((-1)**((d-1)//2)*s.binomial(2*M, M-d)/d
                      for d in range(1, M+1, 2))
        epsilon = s.Rational(1, 2)-2*odd_sum/(s.pi*central)
        # First bound is derived by the integral inequality in the note.
        # The second is also an exact integer comparison for these controls.
        first = s.Rational(2**(M-1), central)
        second = s.Rational(2*M+1, 2**(M+1))
        assert central*(2*M+1) >= 4**M and first <= second
        value = epsilon.evalf(110)
        assert value > 0 and value < first.evalf(110)
        rows.append({'M': M, 'exact_tail': str(epsilon),
                     'tail_decimal_diagnostic': str(value.evalf(16)),
                     'integral_bound_exact': str(first),
                     'elementary_bound_exact': str(second)})
    return rows


def rational_bessel_control():
    # For x=2 sqrt(q), J0(x)=sum_n (-q)^n/(n!)^2. From n>=2 for q<=4,
    # magnitudes decrease to zero. Consecutive even/odd truncations bracket
    # the exact value, including the earlier finite terms exactly.
    intervals = []
    for q in (1, 4):
        upper = sum(s.Rational((-q)**n, math.factorial(n)**2) for n in range(21))
        lower = upper+s.Rational((-q)**21, math.factorial(21)**2)
        assert lower < upper
        assert s.Rational(q, 22**2) < 1
        intervals.append((lower, upper))
    lo2, hi2 = intervals[0]
    lo4, hi4 = intervals[1]
    assert 0 < lo2 < hi2 and lo4 < hi4 < 0
    assert hi4**2 > hi2**2
    # Therefore p(t=1) > p(t=2) at J=1 exactly, not just numerically.
    p1_lower = (1-hi2**2)/2
    p2_upper = (1-hi4**2)/2
    assert p1_lower > p2_upper
    return {'preparation': 'walker localized at rail position 0', 'J': 1,
            't_early': 1, 't_late': 2,
            'p_early_lower_bound_decimal': str(p1_lower.evalf(20)),
            'p_late_upper_bound_decimal': str(p2_upper.evalf(20)),
            'strict_decrease_proved_by_rational_alternating_series_bounds': True,
            'J0_2_interval': [str(lo2), str(hi2)],
            'J0_4_interval': [str(lo4), str(hi4)],
            'scope': 'A specified reversible Hamiltonian and localized preparation; not a universal obstruction.'}


if __name__ == '__main__':
    out = {'created_utc': datetime.now(timezone.utc).isoformat(),
           'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'finite_link_checks': finite_link_check(),
           'packet_moments_and_bounds': packet_moments(),
           'asymptotic_directional_tail_controls': directional_tail(),
           'specified_nonmonotone_control': rational_bessel_control(),
           'limits': 'Infinite-rail velocity-limit and all-M bounds are analytic proofs in the companion note. Finite checks do not prove a native compiler, continuous permanence, or many-carrier dynamics.'}
    encoded = json.dumps(out, indent=2)+'\n'
    (HERE/'AUTONOMOUS_GAUGE_BIRTH_RAIL_RESULTS.json').write_text(encoded)
    print(encoded, end='')
