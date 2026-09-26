#!/usr/bin/env python3
"""Independent exact controls, written before opening either author checker.

Fractions assemble complete small generators. SymPy derives the de Bruijn
coboundary symbolically. No author implementation is imported or executed.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import hashlib
import json
import math
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []


def clean(x):
    if isinstance(x, (F, s.Basic)):
        return str(x)
    if isinstance(x, dict):
        return {str(k): clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [clean(v) for v in x]
    return x


def check(name, condition, detail=None):
    assert bool(condition), (name, detail)
    checks.append({'name': name, 'passed': True, 'detail': clean(detail)})
    print('PASS:', name, flush=True)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def mv(Q, x):
    return tuple(dot(row, x) for row in Q)


zero = (0, 0, 0)
unit = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
alphabet = [(zero, zero)]
alphabet += [(tuple(sign*x for x in e), zero) for e in unit for sign in (-1, 1)]
alphabet += [(zero, b) for b in product((-1, 1), repeat=3)]
assert len(alphabet) == len(set(alphabet)) == 15

# Full 48 polar/axial actions: rate chirality and pair energy are invariant.
actions = []
for p in permutations(range(3)):
    inversion_sign = (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
    for signs in product((-1, 1), repeat=3):
        Q = tuple(tuple(signs[i] if p[i] == j else 0 for j in range(3)) for i in range(3))
        det = inversion_sign*math.prod(signs)
        transformed = [(mv(Q, e), tuple(det*x for x in mv(Q, b))) for e, b in alphabet]
        assert set(transformed) == set(alphabet)
        for i, j in product(range(15), repeat=2):
            e, b = alphabet[i]; f, c = alphabet[j]
            ep, bp = transformed[i]; fp, cp = transformed[j]
            assert 4*dot(e, f)+dot(b, c) == 4*dot(ep, fp)+dot(bp, cp)
        normal = cross(unit[0], unit[1])
        normalp = cross(mv(Q, unit[0]), mv(Q, unit[1]))
        assert normalp == tuple(det*x for x in mv(Q, normal))
        for (_, b), (_, bp) in zip(alphabet, transformed):
            assert dot(normal, b) == dot(normalp, bp)
        actions.append((Q, det))
check('all_48_cubic_actions_preserve_menu_pair_energy_and_axial_chirality', len(actions) == 48,
      {'pair_checks': 48*15*15, 'proper': sum(det == 1 for _, det in actions)})

# Complete conditional plaquette generator with a nonuniform exterior.
# H_S=(log 2)*h; scores are 4 t(a).t(b). This is a true pair-Hamiltonian
# restriction with one fixed exterior neighbor above each square vertex.
small = [(zero, zero), (unit[0], zero), ((-1, 0, 0), zero), (zero, (1, 1, 1))]
chem = [F(1), F(2), F(3), F(5)]
exterior = (0, 1, 3, 2)
square = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0))
states = list(product(range(4), repeat=4))


def score(a, b):
    return 4*dot(small[a][0], small[b][0])+dot(small[a][1], small[b][1])


def h(eta):
    return -sum(score(eta[i], eta[(i+1) % 4])+score(eta[i], exterior[i]) for i in range(4))


def rotate(eta, forward=True):
    return (eta[-1],)+eta[:-1] if forward else eta[1:]+(eta[0],)


def row(eta, sign_error=False, noninvariant_multiplier=False, swaps=True):
    out = defaultdict(F)
    chi = sum(F(small[a][1][2], 4) for a in eta)
    for forward in (True, False):
        target = rotate(eta, forward)
        amplitude = 1+(1 if forward else -1)*chi/2
        if noninvariant_multiplier:
            amplitude *= 1+F(eta[0], 4)
        rate = amplitude*F(2)**((-1 if sign_error else 1)*h(eta))
        if target != eta:
            out[target] += rate
    if swaps:
        for i in range(4):
            j = (i+1) % 4
            target = list(eta); target[i], target[j] = target[j], target[i]; target = tuple(target)
            if target != eta:
                out[target] += F(1, 3)*min(F(1), F(2)**(h(eta)-h(target)))
    return out


weights = {eta: F(2)**(-h(eta))*math.prod(chem[a] for a in eta) for eta in states}


def stationary_residual(rows, weights):
    residual = defaultdict(F)
    for eta, transitions in rows.items():
        for target, rate in transitions.items():
            residual[target] += weights[eta]*rate
            residual[eta] -= weights[eta]*rate
    return residual


generator = {eta: row(eta) for eta in states}
residual = stationary_residual(generator, weights)
check('complete_256_state_conditional_plaquette_plus_Metropolis_generator_is_Gibbs_stationary',
      all(x == 0 for x in residual.values()), {'states': len(states), 'directed_transitions': sum(map(len, generator.values()))})
witness = (0, 1, 2, 3); rotated = rotate(witness)
flow_ratio = weights[witness]*generator[witness][rotated]/(weights[rotated]*generator[rotated][witness])
check('four_distinct_record_circulation_is_not_reversible', flow_ratio == F(9, 7), {'forward_reverse_flow_ratio': flow_ratio})
for name, kwargs in [('wrong_energy_sign', {'sign_error': True}), ('non_orbit_invariant_amplitude', {'noninvariant_multiplier': True})]:
    wrong = stationary_residual({eta: row(eta, **kwargs) for eta in states}, weights)
    bad = [(eta, value) for eta, value in wrong.items() if value != 0]
    check('negative_control_' + name + '_breaks_stationarity', len(bad) > 0,
          {'nonzero_residuals': len(bad), 'first_witness': bad[0]})


def moment(eta, label):
    return tuple(sum(square[i][j] for i in range(4) if eta[i] == label) for j in range(3))


currents = [[F(0) for j in range(3)] for label in range(4)]
orbit_lengths = set()
for eta in states:
    orbit = [eta]; v = rotate(eta)
    while v != eta:
        orbit.append(v); v = rotate(v)
    orbit_lengths.add(len(orbit))
    for label in range(4):
        orbit_sum = tuple(sum(moment(rotate(v), label)[j]-moment(v, label)[j] for v in orbit) for j in range(3))
        assert orbit_sum == zero
        for target, rate in generator[eta].items():
            for j in range(3):
                currents[label][j] += weights[eta]*rate*(moment(target, label)[j]-moment(eta, label)[j])
check('contractible_orbit_and_complete_stationary_displacement_cancellation',
      all(x == 0 for row_ in currents for x in row_), {'orbit_lengths': sorted(orbit_lengths), 'weighted_currents': currents})

# Constant total birth rate 1 per vacancy attains the harmonic filling bound.
harmonic = [F(0)]
for n in range(1, 5):
    harmonic.append(harmonic[-1]+F(1, n))
for eta in states:
    vacancies = eta.count(0)
    assert sum(rate*(target.count(0)-vacancies) for target, rate in generator[eta].items()) == 0
    assert vacancies*(harmonic[max(0, vacancies-1)]-harmonic[vacancies]) == (-1 if vacancies else 0)
weighted_birth_drift = -sum(w*eta.count(0) for eta, w in weights.items())/sum(weights.values())
check('vacancy_Lyapunov_drift_and_sharp_constant_rate_harmonic_filling_bound',
      weighted_birth_drift < 0, {'grand_Gibbs_expected_vacancy_drift': weighted_birth_drift, 'H4': harmonic[4]})

# Independently solve all 16 de Bruijn edge equations instead of installing h.
z = s.symbols('z', positive=True)
triples = list(product((0, 1), repeat=3))
unknowns = s.symbols('g0:8'); lookup = dict(zip(triples, unknowns))


def rates(a, d, zz):
    return 1 if a == d else (2*zz/(1+zz) if (a, d) == (0, 1) else 2/(1+zz))


equations = []
for a, b, c, d in product((0, 1), repeat=4):
    ff = ((rates(a, d, z)*z**(a-d)) if (b, c) == (0, 1) else 0) - (rates(a, d, z) if (b, c) == (1, 0) else 0)
    equations.append(lookup[a, b, c]-lookup[b, c, d]-ff)
sol = s.solve(equations+[unknowns[0]], unknowns, dict=True)
assert len(sol) == 1 and len(sol[0]) == 8
derived = {''.join(map(str, triple)): s.factor(sol[0][var]) for triple, var in lookup.items()}
expected = {'000': 0, '001': 0, '010': -1, '011': -2/(1+z), '100': 0,
            '101': (z-1)/(z+1), '110': -2/(1+z), '111': -2/(1+z)}
check('symbolically_derived_unique_16_word_coboundary_for_all_positive_z',
      all(s.cancel(derived[k]-expected[k]) == 0 for k in expected), derived)


def binary_weight(eta, zz, ww):
    return zz**sum(eta[i]*eta[(i+1) % len(eta)] for i in range(len(eta)))*ww**sum(eta)


def binary_rows(n, zz):
    ans = {}
    for eta in product((0, 1), repeat=n):
        out = defaultdict(F)
        for i in range(n):
            j = (i+1) % n
            if (eta[i], eta[j]) == (1, 0):
                target = list(eta); target[i], target[j] = 0, 1
                out[tuple(target)] += F(rates(eta[(i-1) % n], eta[(i+2) % n], zz))
        ans[eta] = out
    return ans


finite_details = []
for zz, rr in [(F(2), F(2, 3)), (F(1, 3), F(3, 2)), (F(1), F(1))]:
    ww = rr*rr
    T = s.Matrix([[1, s.Rational(rr.numerator, rr.denominator)],
                  [s.Rational(rr.numerator, rr.denominator), s.Rational((zz*ww).numerator, (zz*ww).denominator)]])
    for n in (4, 5, 6):
        q = binary_rows(n, zz); w = {eta: binary_weight(eta, zz, ww) for eta in q}
        assert all(x == 0 for x in stationary_residual(q, w).values())
        normalization = sum(w.values())
        current = sum(weight*F(rates(eta[-1], eta[2], zz)) for eta, weight in w.items() if eta[:2] == (1, 0))/normalization
        finite_fourword = sum(T[a, 1]*T[1, 0]*T[0, d]*(T**(n-3))[d, a]*s.Rational(F(rates(a, d, zz)).numerator, F(rates(a, d, zz)).denominator)
                              for a, d in product((0, 1), repeat=2))/s.trace(T**n)
        assert s.cancel(finite_fourword-s.Rational(current.numerator, current.denominator)) == 0
        assert current > 0
        finite_details.append({'N': n, 'z': zz, 'exp_mu': ww, 'exact_current': current})
check('nine_complete_binary_ring_generators_stationarity_and_finite_transfer_current', True, finite_details)

# Exact PF/Markov covariance and current at three half-density points.
transfer_details = []
for rootz in [s.Rational(1, 2), s.Integer(1), s.Integer(2)]:
    zz = rootz**2
    T = s.Matrix([[1, 1/rootz], [1/rootz, 1]])
    lam = 1+1/rootz; nu = (1-1/rootz)/lam; P = T/lam
    rho = s.Rational(1, 2)
    current = sum(T[a, 1]*T[1, 0]*T[0, d]*rates(a, d, zz)/(2*lam**3) for a, d in product((0, 1), repeat=2))
    assert s.cancel(current-rootz/((1+rootz)*(1+zz))) == 0
    for distance in range(8):
        assert s.cancel(rho*(P**distance)[1, 1]-rho**2-rho*(1-rho)*nu**distance) == 0
    transfer_details.append({'z': zz, 'rho': rho, 'second_eigenvalue_ratio': nu, 'infinite_current': s.factor(current)})
check('exact_thermodynamic_PF_current_and_correlations_including_repulsion', True, transfer_details)

# Spatial winding exposes the exact excluded hypothesis in the local-cycle proof.
n = 5; eta = (1, 0, 0, 0, 0); cycle = []
for _ in range(n):
    cycle.append(eta)
    i = eta.index(1); target = list(eta); target[i] = 0; target[(i+1) % n] = 1; eta = tuple(target)
check('local_KLS_rates_have_a_winding_configuration_cycle_with_nonzero_displacement',
      eta == cycle[0] and len(set(cycle)) == n, {'cycle_length': n, 'physical_displacement': n,
      'wrapped_coordinate_telescoping_sum': 0, 'canonical_one_particle_current_per_bond': F(1, n)})

# Separate complete fine-label generator with nonuniform chemical potentials.
labels = range(4); chem_fine = [F(1), F(2), F(3), F(5)]
cls = lambda label: int(label < 2)
zz = F(2); qfine = {}; wfine = {}
for eta in product(labels, repeat=4):
    sigma = tuple(map(cls, eta)); wfine[eta] = zz**sum(sigma[i]*sigma[(i+1) % 4] for i in range(4))*math.prod(chem_fine[a] for a in eta)
    out = defaultdict(F)
    for i in range(4):
        j = (i+1) % 4; pair = sigma[i], sigma[j]
        if pair == (1, 0) or pair[0] == pair[1]:
            target = list(eta); target[i], target[j] = target[j], target[i]; target = tuple(target)
            if target != eta:
                out[target] += F(rates(sigma[(i-1) % 4], sigma[(i+2) % 4], zz)) if pair == (1, 0) else F(1, 7)
    qfine[eta] = out
assert all(x == 0 for x in stationary_residual(qfine, wfine).values())
aggregated = defaultdict(F)
for eta, weight in wfine.items():
    aggregated[tuple(map(cls, eta))] += weight
assert all(weight == F(8)**4*binary_weight(sig, zz, F(3, 8)) for sig, weight in aggregated.items())
check('complete_256_state_fine_label_generator_and_coarse_chemical_potential_lift', True,
      {'states': len(qfine), 'coarse_exp_mu': F(3, 8), 'same_class_swap_rate': F(1, 7)})

# Explicitly cover all fifteen labels by assigning vacancy to B.
is_A = [any(e) for e, b in alphabet]
fine_weights = [F(5) if i == 0 else (F(2) if is_A[i] else F(3)) for i in range(15)]
class_weights = {c: sum(w for w, a in zip(fine_weights, is_A) if a == c) for c in (False, True)}
features = [e+b for e, b in alphabet]
conditional_means = {c: tuple(sum(w*f[j] for w, a, f in zip(fine_weights, is_A, features) if a == c)/class_weights[c] for j in range(6)) for c in (False, True)}
assert conditional_means == {False: (0,)*6, True: (0,)*6}
binary = list(product((0, 1), repeat=4)); bw = {sig: binary_weight(sig, F(2), class_weights[True]/class_weights[False]) for sig in binary}; norm = sum(bw.values())
pairs = {(a, b): sum(w for sig, w in bw.items() if sig[0] == a and sig[1] == b)/norm for a, b in product((0, 1), repeat=2)}
cov = [[F(0) for _ in range(6)] for _ in range(6)]
for a, b in product(range(15), repeat=2):
    probability = pairs[int(is_A[a]), int(is_A[b])]*fine_weights[a]/class_weights[is_A[a]]*fine_weights[b]/class_weights[is_A[b]]
    for i, j in product(range(6), repeat=2):
        cov[i][j] += probability*features[a][i]*features[b][j]
rho = pairs[1, 0]+pairs[1, 1]; scalar_cov = pairs[1, 1]-rho*rho
check('explicit_15_label_grand_Gibbs_lift_has_zero_vector_but_nonzero_class_covariance',
      all(x == 0 for row_ in cov for x in row_) and scalar_cov > 0,
      {'vacancy_class': 'B', 'class_weights_A_B': [class_weights[True], class_weights[False]],
       'scalar_covariance_at_distance_one': scalar_cov, 'raw_feature_covariance': cov})
balanced_signs = list(set(permutations((1, 1, -1, -1))))
canonical_cov = F(sum(x[0]*x[1] for x in balanced_signs), len(balanced_signs))
check('negative_control_grand_vector_covariance_statement_cannot_be_imported_into_fixed_fine_counts',
      canonical_cov == F(-1, 3), {'canonical_two_plus_two_minus_covariance': canonical_cov})

result = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'checks': checks, 'check_count': len(checks), 'all_passed': all(c['passed'] for c in checks),
          'arithmetic': 'Exact Fractions and symbolic rational identities only; no Monte Carlo or floating-point comparison.',
          'scope': 'Independent finite controls supplement the written general proofs. No author checker/results read or imported.'}
(HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
print('TOTAL:', len(checks), 'exact control groups passed', flush=True)
