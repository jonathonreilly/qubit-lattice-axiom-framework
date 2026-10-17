"""Exact local/full-Pauli and scalar corroboration; not a dynamics or Gibbs simulation."""
from fractions import Fraction as F
from math import comb
import json
import time


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def conj(a):
    return (a[0], -a[1])


ZERO = (F(0), F(0))
ONE = (F(1), F(0))
IPHASE = (ONE, (F(0), F(1)), (F(-1), F(0)), (F(0), F(-1)))


def add(*operators):
    out = {}
    for op in operators:
        for key, value in op.items():
            out[key] = out.get(key, F(0)) + value
    return {k: v for k, v in out.items() if v}


def scale(value, op):
    return {key: value * coefficient for key, coefficient in op.items() if value * coefficient}


def term(value, *support):
    key = tuple(sorted(support))
    assert len(dict(key)) == len(key)
    return {key: F(value)} if value else {}


Iop = term(1)


def number(j):
    return add(scale(F(1, 2), Iop), term(F(-1, 2), (j, 'Z')))


def vacancy(j):
    return add(Iop, scale(-1, number(j)))


def control_x(g, control, target):
    return add(term(g / 2), term(g / 2, (target, 'X')),
               term(-g / 2, (control, 'Z')),
               term(-g / 2, (control, 'Z'), (target, 'X')))


def hop(t_re, t_im, j, e):
    return add(term(t_re / 2, (j, 'X'), (e, 'X')),
               term(t_re / 2, (j, 'Y'), (e, 'Y')),
               term(t_im / 2, (j, 'Y'), (e, 'X')),
               term(-t_im / 2, (j, 'X'), (e, 'Y')))


def lap(jvalue, j, k):
    return add(scale(jvalue, number(j)), scale(jvalue, number(k)),
               hop(-jvalue, F(0), j, k))


def apply(op, bits):
    out = {}
    for key, coefficient in op.items():
        target, phase = bits, 0
        for site, pauli in key:
            bit = (bits >> site) & 1
            if pauli == 'X':
                target ^= 1 << site
            elif pauli == 'Y':
                target ^= 1 << site
                phase += 3 if bit else 1
            elif pauli == 'Z':
                phase += 2 * bit
            else:
                raise AssertionError(pauli)
        value = cmul((coefficient, F(0)), IPHASE[phase % 4])
        out[target] = cadd(out.get(target, ZERO), value)
    return {k: v for k, v in out.items() if v != ZERO}


def apply_vector(op, vector):
    out = {}
    for bits, value in vector.items():
        for target, coefficient in apply(op, bits).items():
            out[target] = cadd(out.get(target, ZERO), cmul(coefficient, value))
    return {k: v for k, v in out.items() if v != ZERO}


def inner(x, y):
    ans = ZERO
    for k in x.keys() & y.keys():
        ans = cadd(ans, cmul(conj(x[k]), y[k]))
    return ans


def spectral_projector_check(op, top, expected_trace):
    # Exact complete four-dimensional pair matrix, including 00 and 11 sectors.
    columns = [apply(op, j) for j in range(4)]
    for j in range(4):
        for k in range(4):
            assert columns[j].get(k, ZERO) == conj(columns[k].get(j, ZERO))
        assert apply_vector(op, columns[j]) == {
            k: cmul((top, F(0)), v) for k, v in columns[j].items()
        }
    trace = sum((columns[j].get(j, ZERO)[0] for j in range(4)), F(0))
    assert trace == expected_trace
    # Hermiticity and Q^2=top*Q with top>0 prove spectrum subset {0,top}.
    assert top > 0
    return {'top': str(top), 'trace': str(trace), 'rank': int(trace / top)}


def fixture(kappa):
    M, Delta = 17, F(1)
    old1, old2, A, B = 0, 1, 2, 3
    clocks, e = list(range(4, M + 4)), M + 4
    J = F('0.030021107107032')
    nu = F('1.459892813020969')
    ga, gb = F('0.996878563816670'), F('0.599319315560298')
    da, db = F('2.192035527016003'), F('2.186826508897014')
    h, u = F('3.999349697888060'), F('0.544607276405587')
    la, lb = F('3.801781381581202'), F('2.575033765788497')
    mu0, q0 = F('0.321494607058201'), F('4.510351185997098')
    cosk, sink = (q0 * q0 - 1) / (q0 * q0 + 1), 2 * q0 / (q0 * q0 + 1)
    cosphi, sinphi = cosk * cosk - sink * sink, 2 * cosk * sink
    E0 = 4 * J / (q0 * q0 + 1)
    assert cosphi * cosphi + sinphi * sinphi == 1
    assert E0 > 2 * kappa
    ba, bb = 2 * ga, 2 * gb
    K = add(term(2), term(1, (old1, 'Z'), (old2, 'Z')))
    Ga, Gb = control_x(ga, A, old1), control_x(gb, B, old2)
    pair_occupancy = add(term(u / 4), term(-u / 4, (A, 'Z')),
                         term(-u / 4, (B, 'Z')), term(u / 4, (A, 'Z'), (B, 'Z')))
    C = add(scale(da, number(A)), scale(db, number(B)), lap(h, A, B), pair_occupancy)
    Hc = add(scale(J, number(clocks[0])), scale(J, number(clocks[-1])),
             *(lap(J, j, k) for j, k in zip(clocks, clocks[1:])))
    Vc = add(control_x(la, clocks[0], A), control_x(lb, clocks[1], B),
             scale(mu0, number(clocks[0])))
    j1, j2 = clocks[12], clocks[14]
    Q1 = add(scale(kappa, number(e)), scale(kappa, number(j1)), hop(kappa, F(0), j1, e))
    Q2 = add(scale(kappa, number(e)), scale(kappa, number(j2)),
             hop(-kappa * cosphi, -kappa * sinphi, j2, e))
    run = add(K, C, Ga, Gb, Hc, Vc, scale(nu, vacancy(clocks[1])), Q1, Q2,
              scale(E0 - 2 * kappa, number(e)), scale(kappa, vacancy(j1)),
              scale(kappa, vacancy(j2)))
    blanks = [A, B] + clocks
    controls = [add(scale(ba, Iop), scale(-1, Ga)), add(scale(bb, Iop), scale(-1, Gb)),
                add(scale(2 * kappa, Iop), scale(-1, Q1)),
                add(scale(2 * kappa, Iop), scale(-1, Q2)),
                scale(nu, number(clocks[1])), scale(kappa, number(j1)),
                scale(kappa, number(j2)),
                *(scale(Delta, number(j)) for j in blanks),
                scale(E0 - 2 * kappa + Delta, vacancy(e))]
    extra = add(*controls)
    D = add(vacancy(e), *(number(j) for j in blanks))
    aux = add(C, Hc, Vc, scale(Delta, D))
    cprep, crun = ba + bb + nu + E0 + 4 * kappa, nu + E0 + 2 * kappa
    assert not add(run, extra, scale(-1, K), scale(-cprep, Iop), scale(-1, aux))
    alpha = (Delta * (M + 3) + 3 * (ga + gb) + nu + E0 + 4 * kappa) / 2
    assert extra.get((), F(0)) == alpha
    assert max(len(key) for op in controls for key in op) <= 2
    residual_columns = []
    for old_bits in range(4):
        seed = old_bits | (1 << e)
        old_energy = F(3 if old_bits in (0, 3) else 1)
        assert not apply(aux, seed)
        assert apply(add(run, extra), seed) == {seed: (old_energy + cprep, F(0))}
        residual = apply(add(run, scale(-1, K), scale(-crun, Iop)), seed)
        expected = {old_bits | (1 << j1): (kappa, F(0)),
                    old_bits | (1 << j2): (-kappa * cosphi, -kappa * sinphi)}
        assert residual == expected
        residual_columns.append(residual)
        assert apply(extra, seed) == {
            seed: (ba + bb + 2 * kappa, F(0)),
            old_bits | (1 << j1): (-kappa, F(0)),
            old_bits | (1 << j2): (kappa * cosphi, kappa * sinphi)}
    for j in range(4):
        for k in range(4):
            assert inner(residual_columns[j], residual_columns[k]) == (
                2 * kappa * kappa if j == k else F(0), F(0))
    pair_Q = add(scale(kappa, number(0)), scale(kappa, number(1)),
                 hop(-kappa * cosphi, -kappa * sinphi, 0, 1))
    spectra = {
        'emitter_pair': spectral_projector_check(pair_Q, 2 * kappa, 4 * kappa),
        'old_source_A': spectral_projector_check(control_x(ga, 0, 1), ba, ba),
        'clock_bond': spectral_projector_check(lap(J, 0, 1), 2 * J, 4 * J),
        'clock_source_A': spectral_projector_check(control_x(la, 0, 1), 2 * la, 2 * la),
    }
    # Discriminators keep the main construction fixed; they are not alternative proofs.
    missing_vacancy = add(run, extra, scale(-nu, number(clocks[1])),
                          scale(-1, K), scale(-cprep, Iop), scale(-1, aux))
    assert missing_vacancy  # Exposes loss of exact decoupled preparation identity.
    wrong_complement = add(scale(ga, Iop), scale(-1, control_x(ga, 0, 1)))
    plus_on_old_with_source_one = {1: (F(1), F(0)), 3: (F(1), F(0))}
    # This unnormalized vector is a -ga eigenvector, so the half-sized complement is not positive.
    assert apply_vector(wrong_complement, plus_on_old_with_source_one) == {
        j: (-ga, F(0)) for j in (1, 3)}
    return {'M': M, 'physical_qubits': M + 5, 'auxiliary_qubits': M + 3,
            'kappa': str(kappa), 'global_pauli_terms': len(run),
            'extra_pauli_terms': len(extra), 'exact_decomposition': True,
            'seed_columns': 4, 'residual_gram': str(2 * kappa * kappa),
            'extra_identity_coefficient': str(alpha), 'spectra': spectra,
            'preserved_discriminators': ['missing vacancy compensation breaks decomposition',
                                         'g I-G is negative on an actual pair vector']}


def scalar_checks():
    max_n = 5 * 10**31 + 3
    q_bound = F(3, 8)**100
    r = max_n * q_bound
    thermal_target = F(1, 22500000000)
    assert r < thermal_target
    # g(d)<=3 sqrt(d); the squared rational inequality gives g(d)<2e-5.
    assert 9 * r < F(2, 100000)**2
    ga = F('0.996878563816670')
    tau, kmax, allowance = F(10000), F(1, 10**8), F(1, 1000)
    max_slew = F(3, 2) * (1 + 2 * ga) / tau
    assert max_slew < allowance
    # Actual cubic a(x)=1-3x^2+2x^3, release area exactly one half.
    a = [F(1), F(0), F(-3), F(2)]
    integral = sum((coefficient / (power + 1) for power, coefficient in enumerate(a)), F(0))
    assert integral == F(1, 2)
    assert sum(a) == 0 and a[0] == 1
    derivative_at_half = -6 * F(1, 2) + 6 * F(1, 2)**2
    assert derivative_at_half == F(-3, 2)
    release_trace_squared = 2 * (kmax * tau)**2
    assert release_trace_squared < F(15, 100000)**2
    total_bound = F(1, 100) + F(2, 100000) + F(15, 100000)
    assert total_bound == F(1017, 100000) and total_bound < F(102, 10000)
    # Generic nontrivial many-sector thermal example: counting only one qubit fails.
    q, n = F(1, 10), 20
    partition = sum((F(comb(n, k)) * q**k for k in range(n + 1)), F(0))
    assert partition == (1 + q)**n
    defect = 1 - 1 / partition
    assert defect > q
    # In the pure correlated example, good marginal error 2d is below the complete bound g(d).
    d = F(1, 100)
    assert 4 * d - 3 * d * d > d * d  # g(d)>2d.
    return {'N_max': max_n, 'thermal_q_upper': str(q_bound), 'Nq_upper': str(r),
            'thermal_target': str(thermal_target), 'correlated_trace_upper': '1/50000',
            'max_release_slew': str(max_slew), 'slew_allowance': str(allowance),
            'cubic_integral': str(integral), 'release_trace_upper': '3/20000',
            'complete_trace_upper': str(total_bound),
            'mean_aux_upper': str(r / (1 - r)),
            'many_sector_discriminator_N': n, 'many_sector_defect': str(defect),
            'many_sector_false_one_qubit_bound': str(q)}


def main():
    started = time.monotonic()
    fixtures = [fixture(F(1, 10**p)) for p in (12, 10, 8)]
    report = {'scope': 'Exact fraction arithmetic in full Pauli representations and complete 4x4 local matrices; scalar rational bounds only.',
              'limits': 'No full many-body matrix, Gibbs density, dynamics simulation, continuum scattering replay, bath, physical calibration or uniform-family numerical sweep.',
              'fixtures': fixtures, 'scalar': scalar_checks(),
              'largest_dense_dimension': 4, 'conceptual_qubits_in_pauli_fixture': 22,
              'elapsed_seconds': time.monotonic() - started}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
