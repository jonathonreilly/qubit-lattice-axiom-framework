#!/usr/bin/env python3
"""One n=4 literal-cell control; no parent-code import, no sweep."""
import cmath
import json
import math

N_AUX, N_PTR, DIM = 4, 3, 256
THETA = [2 * math.pi / (2 ** (j + 1)) for j in range(N_PTR)]
ANGLE_ERROR = 1 / 64
ERRORS = [[ANGLE_ERROR for _ in range(N_AUX)] for _ in range(N_PTR)]
DELTA = 16
SCALAR = 928 / 209 + 17
TOL = 3e-10


def aux_word(i):
    return (i >> 3) & 15


def zero():
    return [0j] * DIM


def norm2(v):
    return sum(abs(a) ** 2 for a in v)


def add(*terms):
    return [sum(c * v[i] for c, v in terms) for i in range(DIM)]


def inner(v, w):
    return sum(a.conjugate() * b for a, b in zip(v, w))


def physical_kraus(errors):
    # Explicit coherent pointer preparation, every controlled phase, then X read.
    ans = [[0j] * 16 for _ in range(8)]
    for z in range(16):
        ptr = [1 / math.sqrt(8) + 0j for _ in range(8)]
        for j in range(3):
            for u in range(4):
                if (z >> u) & 1:
                    for f in range(8):
                        if (f >> j) & 1:
                            ptr[f] *= cmath.exp(1j * (THETA[j] + errors[j][u]))
        for b in range(8):
            ans[b][z] = sum(((-1) ** ((b & f).bit_count())) * ptr[f]
                             for f in range(8)) / math.sqrt(8)
    return ans


def product_kraus(errors):
    ans = [[1 + 0j] * 16 for _ in range(8)]
    for b in range(8):
        for z in range(16):
            for j in range(3):
                phase = sum(THETA[j] + errors[j][u]
                            for u in range(4) if (z >> u) & 1)
                ans[b][z] *= (1 + (-1) ** ((b >> j) & 1)
                                 * cmath.exp(1j * phase)) / 2
    return ans


def apply_H(v):
    out = zero()
    for i, a in enumerate(v):
        out[i] += .3 * (1 - 2 * (i & 1)) * a
        out[i ^ 2] += .2 * a
        out[i ^ 1 ^ 4] += .1 * a
    return out


def apply_L(v):
    out = zero()
    for i, a in enumerate(v):
        z = aux_word(i)
        nb, nbp = (z >> 1) & 1, (z >> 3) & 1
        old_B = 1 - 2 * ((i >> 1) & 1)
        out[i] += (z.bit_count() + .25 * old_B * (nb - nbp)) * a
        for u, u2 in ((0, 1), (2, 3)):
            if ((z >> u) & 1) != ((z >> u2) & 1):
                out[i ^ (1 << (3 + u)) ^ (1 << (3 + u2))] -= .25 * a
    return out


def apply_V(v):
    out = zero()
    for i, a in enumerate(v):
        for u, old_mask, coeff in ((0, 1, 1), (1, 4, 1),
                                    (2, 1, 1), (3, 4, -1)):
            out[i ^ old_mask ^ (1 << (3 + u))] += coeff * a
    return out


def apply_K(v):
    return add((1, apply_H(v)), (DELTA, apply_L(v)),
               (math.sqrt(DELTA), apply_V(v)), (SCALAR, v))


def moment_sums(vectors, op=apply_K):
    weight = sum(norm2(v) for v in vectors)
    mu = 0j
    second = 0.0
    for v in vectors:
        kv = op(v)
        mu += inner(v, kv)
        second += norm2(kv)
    assert abs(mu.imag) < TOL
    return {'weight': weight, 'mean_unnormalized': mu.real,
            'second_unnormalized': second,
            'mean': mu.real / weight if weight else None,
            'variance': second / weight - (mu.real / weight) ** 2
                        if weight else None}


def populations(vectors):
    probs = [sum(abs(v[i]) ** 2 for v in vectors for i in range(DIM)
                 if aux_word(i) == z) for z in range(16)]
    return probs


def old_marginal(vectors):
    out = [[0j] * 16 for _ in range(16)]
    for v in vectors:
        for z in range(16):
            old = [v[(o & 7) | (z << 3) | ((o >> 3) << 7)]
                   for o in range(16)]
            for o in range(16):
                for p in range(16):
                    out[o][p] += old[o] * old[p].conjugate()
    return out


def filter_vectors(kraus, v):
    return [[kraus[b][aux_word(i)] * a for i, a in enumerate(v)]
            for b in range(8)]


def kernel(kraus, z, zp, start=0):
    return sum(kraus[b][z] * kraus[b][zp].conjugate()
               for b in range(start, 8))


def maximum_residual(a, b):
    return max(abs(x - y) for rowa, rowb in zip(a, b)
               for x, y in zip(rowa, rowb))


def main():
    exact = physical_kraus([[0.0] * 4 for _ in range(3)])
    actual = physical_kraus(ERRORS)
    product = product_kraus(ERRORS)
    res_product = maximum_residual(actual, product)
    res_complete = max(abs(kernel(actual, z, z) - 1) for z in range(16))
    res_pinching = max(abs(kernel(exact, z, zp)
                           - (1 if z.bit_count() == zp.bit_count() else 0))
                       for z in range(16) for zp in range(16))
    res_projector = max(abs(exact[0][z] - (1 if z == 0 else 0))
                        for z in range(16))
    res_vacuum = max(abs(actual[b][0] - (1 if b == 0 else 0))
                     for b in range(8))
    assert max(res_product, res_complete, res_pinching,
               res_projector, res_vacuum) < TOL
    alpha = max(abs(actual[0][z]) for z in range(1, 16))
    a1 = max(abs(actual[0][1 << u]) for u in range(4))
    a2 = max(abs(actual[0][(1 << u) | (1 << v)])
             for u in range(4) for v in range(u + 1, 4))
    assert alpha <= 4 * ANGLE_ERROR / 2 + TOL
    assert a1 <= ANGLE_ERROR / 2 + TOL
    assert a2 <= ANGLE_ERROR + TOL

    phi = zero()
    phi[0] = phi[7 | 128] = 1 / math.sqrt(2)
    psi = zero()
    align = actual[0][1].conjugate() / abs(actual[0][1])
    # One fixed coherent, old/reference-entangled input. The one-flip phase
    # is chosen before execution to expose the surviving success P-Q term.
    for i, amp in enumerate(phi):
        psi[i] += math.sqrt(.6) * amp
        psi[(i ^ 1) | (1 << 3)] += math.sqrt(.2) * align * amp
        psi[(i ^ 4) | (3 << 3)] += math.sqrt(.15) * 1j * amp
        psi[i | (15 << 3)] += math.sqrt(.05) * cmath.exp(.3j) * amp
    assert abs(norm2(psi) - 1) < TOL
    out = filter_vectors(actual, psi)
    pop_in, pop_out = populations([psi]), populations(out)
    res_pop = max(abs(a - b) for a, b in zip(pop_in, pop_out))
    res_old = maximum_residual(old_marginal([psi]), old_marginal(out))
    assert max(res_pop, res_old) < TOL
    q = 1 - pop_in[0]
    eta = sum(z.bit_count() * p for z, p in enumerate(pop_in))
    success = out[0]
    s = norm2(success)
    t = sum(abs(a) ** 2 for i, a in enumerate(success) if aux_word(i))
    qs = t / s
    etas = sum(aux_word(i).bit_count() * abs(a) ** 2
               for i, a in enumerate(success)) / s
    assert .6 - TOL <= s <= .6 + alpha ** 2 * q + TOL
    assert qs <= alpha ** 2 * q / (.6 + alpha ** 2 * q) + TOL
    assert etas <= alpha ** 2 * eta / s + TOL

    # Vacuum extensions of the exact old/reference marginal, as a mixture.
    ideal_vectors = []
    for z in range(16):
        v = zero()
        for i in range(DIM):
            if aux_word(i) == z:
                v[i & ~(15 << 3)] = psi[i]
        ideal_vectors.append(v)
    baseline = moment_sums(ideal_vectors)
    h_baseline = moment_sums(ideal_vectors, apply_H)
    assert abs(baseline['mean'] - SCALAR - h_baseline['mean']) < TOL
    assert abs(baseline['variance'] - h_baseline['variance'] - 64) < TOL
    retained = moment_sums(out)
    accepted = moment_sums([success])
    p_success = [a if aux_word(i) == 0 else 0j
                 for i, a in enumerate(success)]
    q_success = [a if aux_word(i) != 0 else 0j
                 for i, a in enumerate(success)]
    dephased_success = moment_sums([p_success, q_success])
    missing_pq_mean = accepted['mean'] - dephased_success['mean']
    missing_pq_variance = accepted['variance'] - dephased_success['variance']
    assert abs(missing_pq_mean) > 1e-4

    h0, d, kap, vnorm, kap2 = .6, 1.2, 4, 4, 24
    l1 = (9 + math.sqrt(5)) / 8
    gamma1 = math.sqrt(DELTA * kap) * (2 * d + DELTA * l1)
    gamma2 = DELTA * math.sqrt(kap2)
    gamma_e = math.sqrt(a1*a1*gamma1*gamma1 + a2*a2*gamma2*gamma2)
    eta_a = sum(((z & 1) + ((z >> 2) & 1)) * p
                for z, p in enumerate(pop_in))
    eta_b = eta - eta_a
    u = min(1.25 * eta_a + 1.5 * eta_b, 4 * q)
    cv = max(kap, vnorm*vnorm - kap)
    rq = (4 * DELTA**2 * u + DELTA * cv * q
          + 2 * DELTA * (d + math.sqrt(DELTA) * vnorm) * math.sqrt(4*q*u)
          + 2 * math.sqrt(DELTA) * d * vnorm * q)
    e1 = DELTA * u + 2 * a1 * math.sqrt(DELTA*kap*eta)
    e2 = 2 * gamma_e * math.sqrt(q*(1-q)) + rq
    mu0 = baseline['mean']
    centered_second = (retained['second_unnormalized']
                       - 2*mu0*retained['mean_unnormalized'] + mu0*mu0)
    observed_mean_error = abs(retained['mean'] - mu0)
    observed_e2_error = abs(centered_second - baseline['variance'])
    observed_var_error = abs(retained['variance'] - baseline['variance'])
    assert observed_mean_error <= e1 + TOL
    assert observed_e2_error <= e2 + TOL
    assert observed_var_error <= e2 + e1*e1 + TOL

    comm = add((1, apply_H(apply_L(psi))), (-1, apply_L(apply_H(psi))))
    noncommuting_H_L = math.sqrt(norm2(comm))
    assert noncommuting_H_L > 1e-4
    wrong_failure_kernel = kernel(exact, 1, 3, start=1)
    wrong_failure_trace_witness = abs(1 - wrong_failure_kernel)
    assert wrong_failure_trace_witness > .999
    omitted_row_amplitude = 1 + 0j
    for j in (1, 2):
        omitted_row_amplitude *= (1 + cmath.exp(1j*THETA[j])) / 2
    assert abs(omitted_row_amplitude)**2 > .4
    outcomes = []
    for b, vec in enumerate(out):
        mom = moment_sums([vec])
        mom.update({'b_little_endian': ''.join('+' if not ((b>>j)&1) else '-'
                                              for j in range(3)),
                    'vacuum_weight': sum(abs(a)**2 for i,a in enumerate(vec)
                                         if aux_word(i)==0)})
        outcomes.append(mom)
    result = {'fixture': {'n':4,'k':3,'Delta':DELTA,'scalar':SCALAR,
                          'angle_error':ANGLE_ERROR,'H_norm_certificate':h0,
                          'H_L_commutator_on_input_norm':noncommuting_H_L},
              'residuals': {'physical_vs_product_kraus':res_product,
                            'completeness':res_complete,'ideal_number_pinching':res_pinching,
                            'ideal_success_projector':res_projector,'actual_vacuum_immunity':res_vacuum,
                            'population_preservation':res_pop,'old_reference_marginal':res_old},
              'amplitudes': {'alpha':alpha,'a1':a1,'a2':a2},
              'input': {'q':q,'eta':eta},
              'success': {'probability':s,'false_acceptance_mass':t,
                          'conditional_q':qs,'conditional_eta':etas},
              'all_actual_outcomes':outcomes,
              'moments': {'baseline':baseline,'retained':retained,'accepted':accepted,
                          'success_PQ_dephased_wrong_comparator':dephased_success,
                          'missing_PQ_mean':missing_pq_mean,
                          'missing_PQ_variance':missing_pq_variance,
                          'observed_mean_error':observed_mean_error,'E1_bound':e1,
                          'observed_centered_second_error':observed_e2_error,'E2_bound':e2,
                          'observed_variance_error':observed_var_error,
                          'variance_bound':e2+e1*e1},
              'countermodels': {'binary_Q_failure_full_reference_trace_witness':wrong_failure_trace_witness,
                                'omitted_j0_false_success_on_number_one':abs(omitted_row_amplitude)**2},
              'scope': 'One selected floating n=4 full auxiliary/old/reference fixture; not all-M proof, apparatus simulation, audit or error-model enlargement.'}
    print(json.dumps(result,indent=2,sort_keys=True))
    print('CONTROL_SCOPE: one fixed n=4 fixture, no sweep or parent code')
    print('CHANNEL_SCOPE: every X outcome retained; arbitrary-reference theorem remains analytic')
    print('ERROR_SCOPE: diagonal angles only; exact clean pointers/readout and no drift')
    print('MOMENT_SCOPE: actual literal one-cell K including scalar and noncommuting H')
    print('STATUS: selected controls completed; no theorem or audit verdict inferred')


if __name__ == '__main__':
    main()
