"""Author challenges for Gaussian-dressed signed cycles and source insertions.

Finite matrix identities and quadrature are checked here. Infinite shape sums,
the imported ALT inequality and the physical activity-one law are not certified
by this runner. The cochain fixture is explicitly shared with the forest check.
"""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'scripts/forest_interpolation_check_2026_09_15.py']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'signed_forest_fixed_order_remainders_and_restricted_loop_sums_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/gaussian_cycle_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np
from numpy.polynomial.hermite import hermgauss

from forest_interpolation_check_2026_09_15 import cochains


def psqrt(a):
    e, u = np.linalg.eigh(a)
    assert e.min() > -2e-12
    return (u*np.sqrt(np.maximum(e, 0)))@u.T


def absolute(a):
    e, u = np.linalg.eigh(a)
    return (u*np.abs(e))@u.T


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for i in range(total+1):
        for rest in compositions(total-i, length-1):
            yield (i,)+rest


def trace_product(j, multipliers):
    out = np.eye(len(j), dtype=complex)
    for m in multipliers:
        out = out@(m[:, None]*j)
    return np.trace(out)


def source_bounds():
    rng = np.random.default_rng(917362)
    records = []
    for trial in range(4):
        t = rng.normal(size=(5, 4))
        if trial == 1:
            t[2:] = 0
        t *= .45/np.linalg.norm(t, 2)
        j = np.block([[np.zeros((4, 4)), t.T], [t, np.zeros((5, 5))]])
        a, rho = absolute(j), np.linalg.norm(j, 2)
        source = rng.normal(size=9)+1j*rng.normal(size=9)
        if trial == 2:
            source[1:] = 0
        s4 = np.sum(np.abs(source)**4*np.diag(a))
        maximum = 0.
        count = 0
        for length in [4, 6, 8]:
            phases = np.exp(1j*rng.normal(size=(length, 9)))
            phases *= rng.uniform(.3, 1, size=(length, 9))
            for ks in compositions(4, length):
                value = trace_product(j, [phases[i]*source**k for i, k in enumerate(ks)])
                bound = rho**(length-1)*s4
                ratio = abs(value)/bound
                maximum = max(maximum, float(ratio))
                assert ratio <= 1+2e-12
                count += 1
        records.append(dict(trial=trial, insertions=count, maximum_ratio=maximum))
    # Sharp rank-one alternating case rejects an extra rho in the bound.
    rho = .2
    j = np.array([[0., rho], [rho, 0.]])
    s4 = np.trace(absolute(j))
    value = trace_product(j, [np.ones(2)]*4).real
    sharp = rho**3*s4
    assert abs(value-sharp) < 1e-15
    assert value > rho**4*s4*4.9
    return dict(random=records, sharp_value=value, sharp_bound=sharp,
                wrong_rho_power_rejected=True)


def dressed_cochain_cycles():
    incidence, p, q = cochains()
    d, b = incidence[1:3]
    beta, n = .5, 3
    xe, xm = n*n/beta, 4*np.pi*np.pi*beta
    kernels = [p-d@d.T/32, q-b.T@b/32]
    families = [[0, 6], [0, 18]]
    weight = [np.exp(-xe*np.sum(d[families[0]]**2, axis=1)/64),
              np.exp(-xm*np.sum(b[:, families[1]]**2, axis=0)/64)]
    # Finite fixture uses no 384-mark replication and states this explicitly.
    theta = 2*np.pi*n*p[np.ix_(families[1], families[0])]
    t = np.sqrt(weight[1][:, None]*weight[0][None, :])*np.sin(theta)
    rho, trace2 = np.linalg.norm(t, 2), np.sum(t*t)
    j = np.block([[np.zeros((2, 2)), t.T], [t, np.zeros((2, 2))]])
    rng = np.random.default_rng(77192)
    sign_vectors = list(itertools.product([-1., 1.], repeat=4))
    assignments = list(itertools.product(range(2), repeat=4))
    correlations = [np.array([[1., -.43], [-.43, 1.]]),
                    np.array([[1., .62], [.62, 1.]])]
    gram = [x*k[np.ix_(fam, fam)]
            for x, k, fam in zip([xe, xm], kernels, families)]
    square = [psqrt(np.kron(s, k)) for s, k in zip(correlations, gram)]
    trace_error, largest_ratio = 0., 0.
    for _ in range(12):
        fields = [(v@rng.normal(size=4)).reshape(2, 2) for v in square]
        sigma = np.array(sign_vectors[int(rng.integers(16))])
        multipliers = []
        for i in range(4):
            species, replica = i % 2, i//2
            diagonal = np.zeros(4, dtype=complex)
            diagonal[species*2:species*2+2] = np.exp(1j*sigma[i]*fields[species][replica])
            multipliers.append(diagonal)
        traced = trace_product(j, multipliers)
        direct = 0j
        for a0, a1, a2, a3 in assignments:
            values = [a0, a1, a2, a3]
            phase = sum(sigma[i]*fields[i % 2][i//2, values[i]] for i in range(4))
            direct += t[a1, a0]*t[a1, a2]*t[a3, a2]*t[a3, a0]*np.exp(1j*phase)
        trace_error = max(trace_error, abs(traced-direct))
        largest_ratio = max(largest_ratio, abs(traced)/(rho*rho*trace2))
    assert trace_error < 2e-14
    assert largest_ratio <= 1+2e-12

    # Gaussian integration is challenged separately on chosen component lists.
    # This is deterministic four-dimensional Gaussian quadrature, not sampling.
    nodes, quadrature = hermgauss(22)
    grid = np.array(list(itertools.product(nodes*np.sqrt(2), repeat=4)))
    weights = np.prod(np.array(list(itertools.product(quadrature/np.sqrt(np.pi), repeat=4))), axis=1)
    gaussian_error = 0.
    wrong_diagonal_residual = 0.
    for labels in [(0, 0, 1, 1), (0, 1, 0, 1), (1, 0, 1, 0)]:
        cov = np.zeros((4, 4))
        for i in range(4):
            for k in range(4):
                if i % 2 == k % 2:
                    species = i % 2
                    cov[i, k] = correlations[species][i//2, k//2]*gram[species][labels[i], labels[k]]
        root = psqrt(cov)
        # Scale only the diagnostic covariance to make quadrature resolve it.
        cov = cov*.04
        field_grid = grid@(root*.2).T
        for signs in sign_vectors:
            signs = np.asarray(signs)
            expected = np.exp(-.5*signs@cov@signs)
            integrated = weights@np.exp(1j*field_grid@signs)
            gaussian_error = max(gaussian_error, abs(integrated-expected))
            missing_diagonal = np.exp(-.5*signs@(cov-np.diag(np.diag(cov)))@signs)
            wrong_diagonal_residual = max(wrong_diagonal_residual, abs(expected-missing_diagonal))
    assert gaussian_error < 3e-13
    assert wrong_diagonal_residual > .1
    # Original finite cochain source, evaluated before the Taylor subtraction.
    mp.mp.dps = 55
    h = .013*np.sin(np.arange(len(p))*.79+.3)
    source_e = -np.sqrt(xe)*(p@h)[families[0]]
    source_m = -1j*np.sqrt(xm)*(q@h)[families[1]]
    source = np.concatenate([source_e, source_m])
    radius, z = .7, mp.mpc('.4', '.3')
    qt = [weight[0]*np.exp(radius*np.abs(source_e)),
          weight[1]*np.exp(radius*np.abs(source_m))]
    tilted_t = np.sqrt(qt[1][:, None]*qt[0][None, :])*np.sin(theta)
    tilted_j = np.block([[np.zeros((2, 2)), tilted_t.T],
                         [tilted_t, np.zeros((2, 2))]])
    tilted_rho = np.linalg.norm(tilted_t, 2)
    source_trace = np.sum(np.abs(source)**4*np.diag(absolute(tilted_j)))
    remainder = mp.mpc(0)
    for labels in assignments:
        cov = np.zeros((4, 4))
        for i in range(4):
            for k in range(4):
                if i % 2 == k % 2:
                    species = i % 2
                    cov[i, k] = correlations[species][i//2, k//2]*gram[species][labels[i], labels[k]]
        a0, a1, a2, a3 = labels
        prefactor = mp.mpf(float(t[a1, a0]*t[a1, a2]*t[a3, a2]*t[a3, a0]))
        local_source = [source_e[a0], source_m[a1], source_e[a2], source_m[a3]]
        for signs in sign_vectors:
            signs = np.asarray(signs)
            energy = mp.mpf(float(signs@cov@signs))/2
            y = sum(mp.mpc(complex(v))*int(s) for v, s in zip(local_source, signs))
            remainder += prefactor*mp.exp(-energy)*(mp.cosh(z*y)-1-(z*y)**2/2)/16
    source_bound = radius**4*4**4*tilted_rho**3*source_trace/24
    assert abs(remainder) <= source_bound
    return dict(fixture_beta=beta, fixture_N=n, normalized_marks_replicated=False,
                fixed_field_trace_error=float(trace_error),
                fixed_field_bound_maximum_ratio=float(largest_ratio),
                gaussian_quadrature_order=22, diagnostic_covariance_scale=.04,
                gaussian_characteristic_error=float(gaussian_error),
                missing_gaussian_diagonal_difference=float(wrong_diagonal_residual),
                full_unscaled_covariance_source_remainder=str(abs(remainder)),
                full_source_trace_bound=float(source_bound),
                source_scope='fixed finite cochain h, not a macroscopic sequence')


def arbitrary_residual_control():
    h = np.array([[1, 1, 1, 1], [1, -1, 1, -1],
                  [1, 1, -1, -1], [1, -1, -1, 1]], dtype=float)/2
    values = [h[j, i]*h[j, k]*h[l, k]*h[l, i]
              for i, j, k, l in itertools.product(range(4), repeat=4)]
    signed, absolute_sum = sum(values), sum(abs(v) for v in values)
    positive_restricted = sum(v for v in values if v > 0)
    assert signed == 4 and absolute_sum == 16 and positive_restricted == 10
    return dict(signed=signed, absolute_sum=absolute_sum,
                positive_indicator_residual=positive_restricted,
                arbitrary_bounded_residual_extension_rejected=True)


def parameter_bound():
    mp.mp.dps = 60
    x = mp.mpf(16384)
    def moment(k):
        e = mp.exp(-x/128)
        return 4*1562500*4**k*e/(1-393*2**(2*k+4)*e)
    rho = x*moment(2)+x**3*moment(6)/6
    assert rho < mp.mpf('1e-30')
    # At beta=512,N=4096 both species exceed this endpoint.
    assert 4*mp.pi**2*512 > x and mp.mpf(4096)**2/512 > x
    return dict(symmetric_endpoint_x=str(x), rho_upper=str(rho),
                example_beta=512, example_N=4096,
                claim_scope='operator and restricted loop bound only')


def main():
    result = dict(status='finite_author_checks_passed',
                  independent_review=False,
                  source_trace=source_bounds(),
                  actual_cochain_fixture=dressed_cochain_cycles(),
                  residual_negative_control=arbitrary_residual_control(),
                  fixed_parameter_operator_bound=parameter_bound())
    _OUTPUT_JSON.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: finite cochain, signed phase, partition and derivative fixtures')
    print('per_site: finite source-support configurations only')
    print('per_mode: finite matrix/operator directions; no all-order or infinite-kernel execution')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
