#!/usr/bin/env python3
"""Exact finite contraction witness for a specified record preparation.

Reconstructs the existing 14-state, four-qubit covariant code using integer
matrices. The exact certificate is a rational triangular spatial profile.
No quantum CP extension is assumed by this calculation. This is the author
calculation, not an independent review. It never edits earlier evidence.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import itertools
import json
import math
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / 'campaign12h_second'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def construct():
    group = []
    for perm in itertools.permutations(range(3)):
        parity = (-1) ** sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
        for signs in itertools.product((-1, 1), repeat=3):
            if parity * math.prod(signs) != 1:
                continue
            R = sp.zeros(3)
            for i in range(3):
                R[i, perm[i]] = signs[i]
            U = sp.diag(1, R)
            group.append((R, sp.kronecker_product(U, U)))
    origins = [sp.Matrix([1, 0, 0]), sp.ones(3, 1)]
    seeds = [sp.Matrix([(7*i*i+3*i+5) % 17-8 for i in range(16)]),
             sp.Matrix([(11*i**3+4*i+1) % 19-9 for i in range(16)])]
    labels = [(0, sp.eye(3)[:, i]*s) for i in range(3) for s in (1, -1)]
    labels += [(1, sp.Matrix(b)) for b in itertools.product((-1, 1), repeat=3)]
    starts = []
    for origin, seed in zip(origins, seeds):
        S = sp.eye(16)
        for R, V in group:
            if R*origin == origin:
                w = V*seed
                S += w*w.T
        starts.append(S)
    assert [sp.trace(s) for s in starts] == [1168, 2125]
    rho = []
    for orbit, label in labels:
        V = next(V for R, V in group if R*origins[orbit] == label)
        rho.append(V*starts[orbit]*V.T/sp.trace(starts[orbit]))
    lookup = {(orbit, tuple(label)): i for i, (orbit, label) in enumerate(labels)}
    for R, V in group:
        for i, (orbit, label) in enumerate(labels):
            j = lookup[(orbit, tuple(R*label))]
            assert V*rho[i]*V.T == rho[j]
    tau = sum(rho, sp.zeros(16))/14
    assert sp.trace(tau) == 1 and tau == tau.T
    assert all(sp.trace(s) == 1 and s == s.T for s in rho)
    # Strict positivity follows directly from I + sum ww^T, including tau.
    e = np.array([list(z) if orbit == 0 else [0, 0, 0] for orbit, z in labels], dtype=np.int64)
    b = np.array([list(z) if orbit == 1 else [0, 0, 0] for orbit, z in labels], dtype=np.int64)
    return rho, tau, e, b


def shift(f, s):
    """At array index x return f(x+s)."""
    return np.roll(f, -s, axis=0)


def full_linearized_numerator(f, e, b):
    """Denominator 280 times that of f; k0=11/10, gamma=1.

    This implements the full 14-color current linearization independently
    of the transverse two-component spatial formula below.
    """
    out = np.zeros_like(f)
    for axis in range(3):
        for sign in (1, -1):
            if axis == 0 and sign == 1:
                continue  # the matching's identity route
            delta = np.eye(3, dtype=np.int64)[axis]*sign
            s = int(delta[0])-1
            C = np.zeros((14, 14), dtype=np.int64)
            for a in range(14):
                for c in range(14):
                    C[a, c] = delta @ (np.cross(e[a], b[c]) + np.cross(e[c], b[a]))
            assert np.array_equal(C, C.T)
            assert np.array_equal(C @ np.ones(14, dtype=np.int64), np.zeros(14, dtype=np.int64))
            out += 154*(shift(f, -s)+shift(f, s)-2*f)
            out += 5*(shift(f, -2*s)+shift(f, s)-shift(f, -s)-shift(f, 2*s)) @ C.T
    return out


def triangle_certificate(N, orientation, e, b, u, v, cross):
    assert N % 4 == 0 and N >= 8
    scale = N//2
    X = scale-2*np.abs(np.arange(N, dtype=np.int64)-scale)
    Y = orientation*shift(X, -N//4)
    assert int(X.sum()) == int(Y.sum()) == 0
    def diff(f):
        return shift(f, -2)+shift(f, 2)-2*f+4*(shift(f, -1)+shift(f, 1)-2*f)
    def skew(f):
        return shift(f, 4)+shift(f, -2)-shift(f, 2)-shift(f, -4)
    dX = 154*diff(X)-10*skew(Y)
    dY = 154*diff(Y)-40*skew(X)
    f = 4*X[:, None]*e[None, :, 1]+Y[:, None]*b[None, :, 2]
    actual = full_linearized_numerator(f, e, b)
    expected = 4*dX[:, None]*e[None, :, 1]+dY[:, None]*b[None, :, 2]
    assert np.array_equal(actual, expected)
    # Delta rho_x=(X_x Rx+Y_x Ry)/scale; dots divide by 280*scale.
    denom = 280*N*scale*scale
    coeff_u = sp.Rational(2*int(X @ dX), denom)
    coeff_v = sp.Rational(2*int(Y @ dY), denom)
    coeff_cross = sp.Rational(2*int(X @ dY+Y @ dX), denom)
    derivative = sp.factor(coeff_u*u+coeff_v*v+coeff_cross*cross)
    return dict(N=N, orientation=orientation, coefficient_u=str(coeff_u),
                coefficient_v=str(coeff_v), coefficient_cross=str(coeff_cross),
                chi_squared_derivative_per_pair=str(derivative),
                decimal_derivative=str(sp.N(derivative, 18)),
                strictly_positive=bool(derivative > 0),
                full_14_color_residual_exactly_zero=True,
                physical_pairs=N**3//2,
                profile='X=T_x/(N/2); Y=orientation*T_(x-N/4)/(N/2); T_x=N/2-2*abs(x-N/2)')


def main():
    rho, tau, e, b = construct()
    inverse = tau.inv()
    assert tau*inverse == sp.eye(16)
    Rx = sum((sp.Rational(int(e[a, 1]), 2)*rho[a] for a in range(14)), sp.zeros(16))
    Ry = sum((sp.Rational(int(b[a, 2]), 8)*rho[a] for a in range(14)), sp.zeros(16))
    assert sp.trace(Rx) == sp.trace(Ry) == 0
    u = sp.factor(sp.trace(Rx*inverse*Rx))
    v = sp.factor(sp.trace(Ry*inverse*Ry))
    cross = sp.factor(sp.trace(Rx*inverse*Ry))
    assert u > 0 and v > 0 and cross == 0
    # These sizes were chosen after the floating Fourier screen, not preregistered.
    witnesses = [triangle_certificate(N, s, e, b, u, v, cross)
                 for N in (512, 1024, 2048) for s in (-1, 1)]
    assert any(w['strictly_positive'] for w in witnesses)
    inputs = [OLD/'DIMER_TWO_PAIR_FAITHFUL_COVARIANT_ENCODING.md',
              OLD/'dimer_two_pair_faithful_encoding_check.py',
              OLD/'DIMER_ROUTED_RECORD_TRANSPORT.md',
              OLD/'DIMER_NONLINEAR_INITIAL_DRIFT.md']
    result = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  status='author_exact_finite_certificate_independent_check_pending',
                  source_sha256={str(p.relative_to(HERE.parent)): digest(p) for p in inputs},
                  script_sha256=digest(Path(__file__)),
                  code=dict(hilbert_dimension=16, colors=14, group_size=24,
                            seed_traces=[1168, 2125], covariance_checks=24*14,
                            positivity='I + sum vv^T before positive normalization',
                            tau_inverse_exactly_checked=True),
                  metric=dict(u=str(u), v=str(v), cross=str(cross),
                              u_minus_4v=str(sp.factor(u-4*v)),
                              decimal_u=str(sp.N(u, 18)), decimal_v=str(sp.N(v, 18))),
                  rates=dict(k0='11/10', gamma='1', lower_bound='(k0-|gamma|)/2=1/20'),
                  witnesses=witnesses,
                  mathematical_scope='Necessary stationary quantum chi-squared contraction, fixed product preparation, exact specified routed classical generator on a finite winding matching. Proof linking the local certificate to a full CPTP obstruction is in the companion note. No claim about other codes or physical generators.')
    encoded=json.dumps(result, indent=2)+'\n'
    (HERE/'QUANTUM_METRIC_EXACT_RESULTS.json').write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
