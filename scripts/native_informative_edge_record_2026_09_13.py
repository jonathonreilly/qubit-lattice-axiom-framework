"""Exact native edge Pauli instrument and independent CAR/Slater checks.

The physical Pauli construction does not use a decoded fermion matrix to
build its pulse. A separate occupation-bit CAR construction tests the current
dictionary and the conditional one-particle formula. No random sampling,
numerical SDP or fitted probability enters these checks.
"""
from __future__ import annotations

from itertools import product
from pathlib import Path
import hashlib
import json
import time
import sympy as sp

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    'docs/NATIVE_INFORMATIVE_EDGE_RECORD_AND_DISTURBANCE_BOUNDED_THEOREM_NOTE_2026-09-13.md',
    'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    '.claude/science/physics-loops/native-informative-record-20260913/SOURCE_MANIFEST.json',
    '.claude/science/physics-loops/native-informative-record-20260913/NO_GO_DISCIPLINE_CHECKLIST.md',
    '.claude/science/physics-loops/native-informative-record-20260913/mutations/RESULTS.json',
)
X = sp.Matrix([[0, 1], [1, 0]])
Z2 = sp.diag(1, -1)
I2 = sp.eye(2)


def clean(x):
    return x.applyfunc(sp.expand) if isinstance(x, sp.MatrixBase) else sp.expand(x)


def tensor_factor(op, j, n):
    return sp.kronecker_product(*(op if k == j else I2 for k in range(n)))


def native_graph(edges):
    edges = sorted(tuple(sorted(e)) for e in edges)
    vertices = sorted(set(sum((list(e) for e in edges), [])))
    n = len(edges)
    eye = sp.eye(2**n)
    xs = [tensor_factor(X, j, n) for j in range(n)]
    zs = [tensor_factor(Z2, j, n) for j in range(n)]
    neighbors = {v: sorted(j if i == v else i for i, j in edges if v in (i, j)) for v in vertices}
    b = {v: sp.prod([1]) * eye for v in vertices}
    for v in vertices:
        for eidx, e in enumerate(edges):
            if v in e:
                b[v] = b[v] * zs[eidx]
    a = {}
    for i, j in edges:
        value = xs[edges.index((i, j))]
        for v, other in ((i, j), (j, i)):
            for k in neighbors[v]:
                if k < other:
                    value = value * zs[edges.index(tuple(sorted((v, k))))]
        a[i, j] = value
        a[j, i] = -value
    return edges, eye, zs, b, a


def annihilators(n):
    out = []
    for j in range(n):
        a = sp.zeros(2**n)
        for mask in range(2**n):
            if mask & (1 << j):
                a[mask ^ (1 << j), mask] = (-1) ** ((mask & ((1 << j) - 1)).bit_count())
        out.append(a)
    return out


def covariance(rho, ann):
    return clean(sp.Matrix(len(ann), len(ann), lambda i, j: sp.trace(rho * ann[j].H * ann[i])))


def run():
    start = time.monotonic()
    checks = []

    def checked(name, condition, **data):
        assert bool(condition), name
        checks.append({'name': name, **data})

    def equal(name, actual, expected):
        difference = clean(actual - expected)
        if isinstance(difference, sp.MatrixBase):
            condition = all(sp.simplify(x) == 0 for x in difference)
        else:
            condition = sp.simplify(difference) == 0
        checked(name, condition)

    edges, eye, zs, b, a = native_graph([(0, 1), (1, 2), (2, 3), (0, 3)])
    z = zs[edges.index((0, 1))]
    S = a[0, 1] * a[1, 2] * a[2, 3] * a[3, 0]
    P = (eye + S) / 2
    protected = [(0, 3), (1, 2), (2, 3)]
    B = b[0]
    hops = {f: clean(sp.I * a[f] * (b[f[0]] - b[f[1]]) / 2) for f in protected}
    currents = {f: clean(-a[f] * (eye - b[f[0]] * b[f[1]]) / 2) for f in protected}
    for i, j in protected:
        occupation = (eye - b[i]) / 2
        equal(f'physical_current_continuity_{i}_{j}', currents[i, j],
              -sp.I * (hops[i, j] * occupation - occupation * hops[i, j]))
    H = sum(hops.values(), sp.zeros(16))
    Hinc = hops[0, 3]
    equal('native_incident_energy_split', (H - B * H * B) / 2, Hinc)
    N = sum(((eye - x) / 2 for x in b.values()), sp.zeros(16))
    equal('native_cycle_hermitian_involution', S.H * S, eye)
    equal('native_cycle_is_hermitian', S.H, S)
    equal('native_cycle_anticommutes_record_Z', S * z + z * S, sp.zeros(16))
    checked('native_incoming_even_code_rank', P.rank() == 8 and P * P == P)
    equal('full_native_vertex_product_even', sp.prod([1]) * b[0] * b[1] * b[2] * b[3], eye)
    generators = list(b.values()) + [a[f] for f in protected]
    checked('protected_generators_commute_cycle_and_Record',
            all(g * S == S * g and g * z == z * g for g in generators))

    # A nonscalar, asymmetric positive full-carrier effect. Its two spectral
    # subspaces involve anticommuting parity and protected edge operators.
    M = (3 * B + 4 * a[0, 3]) / 5
    equal('noncommuting_effect_involution', M * M, eye)
    plus, minus = (eye + M) / 2, (eye - M) / 2
    E = (3 * eye + M) / 8
    root = plus / sp.sqrt(2) + minus / 2
    other = plus / sp.sqrt(2) + sp.sqrt(3) * minus / 2
    equal('effect_physical_square_root', root * root, E)
    equal('complement_physical_square_root', other * other, eye - E)
    aa, bb = (root + other) / sp.sqrt(2), (root - other) / sp.sqrt(2)
    U = clean(aa + bb * z * S)
    equal('general_effect_unitary_full_carrier', U.H * U, eye)
    for sign in (1, -1):
        Q = (eye + sign * z) / 2
        J = sp.sqrt(2) * Q * P
        F = root if sign == 1 else other
        K = clean(Q * U * P)
        equal(f'general_native_Lueders_map_{sign}', K, J * F * P)
        equal(f'general_native_effect_{sign}', K.H * K, P * F * F * P)
        equal(f'general_protected_noncommuting_observable_{sign}', K.H * B * K, P * F * B * F * P)
        equal(f'general_next_code_surjectivity_{sign}', J * J.H, Q)
    checked('general_effect_is_matter_informative', E != sp.trace(E) * eye / 16)
    for certain in (1, -1):
        endpoint_U = (eye + certain * z * S) / sp.sqrt(2)
        equal(f'constant_effect_endpoint_unitary_{certain}', endpoint_U.H * endpoint_U, eye)
        impossible = (eye - certain * z) / 2
        equal(f'constant_effect_zero_branch_{certain}', impossible * endpoint_U * P, sp.zeros(16))

    # One fixture carries both nonzero incident current and bond energy.
    rho = clean(P * (eye + currents[0, 3] / 4 + Hinc / 5 + B / 7) / 8)
    checked('native_fixture_positive_normalized',
            sp.trace(rho) == 1 and all(x >= 0 for x in rho.eigenvals()),
            sufficient_perturbation_bound='1/4+1/5+1/7<1')
    mean = lambda op: clean(sp.trace(rho * op))
    checked('native_fixture_has_current_and_energy', mean(currents[0, 3]) != 0 and mean(Hinc) != 0)
    strengths = [(0, 1, 1, 0),
                 (sp.Rational(3, 5), sp.Rational(4, 5), 3 / sp.sqrt(10), 1 / sp.sqrt(10)),
                 (sp.Rational(5, 13), sp.Rational(12, 13), 5 / sp.sqrt(26), 1 / sp.sqrt(26)),
                 (sp.Rational(12, 13), sp.Rational(5, 13), 3 / sp.sqrt(13), 2 / sp.sqrt(13)),
                 (1, 0, 1 / sp.sqrt(2), 1 / sp.sqrt(2))]
    for idx, (kappa, eta, c, s) in enumerate(strengths):
        U = clean(c * eye + s * B * z * S)
        equal(f'parity_physical_unitary_{idx}', U.H * U, eye)
        channel = sp.zeros(16)
        for sign in (1, -1):
            Q = (eye + sign * z) / 2
            J = sp.sqrt(2) * Q * P
            F = clean((c * eye + sign * s * B) / sp.sqrt(2))
            K = clean(Q * U * P)
            equal(f'parity_native_map_{idx}_{sign}', K, J * F * P)
            equal(f'parity_effect_{idx}_{sign}', K.H * K, P * (eye + sign * kappa * B) * P / 2)
            unnorm = clean(F * rho * F)
            prob = clean(sp.trace(unnorm))
            equal(f'parity_probability_{idx}_{sign}', prob, (1 + sign * kappa * mean(B)) / 2)
            equal(f'selective_parity_mean_{idx}_{sign}', sp.trace(unnorm * B), (mean(B) + sign * kappa) / 2)
            equal(f'selective_incident_current_{idx}_{sign}', sp.trace(unnorm * currents[0, 3]), eta * mean(currents[0, 3]) / 2)
            equal(f'normalized_selective_parity_{idx}_{sign}', sp.trace(unnorm * B) / prob,
                  (mean(B) + sign * kappa) / (1 + sign * kappa * mean(B)))
            equal(f'normalized_selective_current_{idx}_{sign}', sp.trace(unnorm * currents[0, 3]) / prob,
                  eta * mean(currents[0, 3]) / (1 + sign * kappa * mean(B)))
            equal(f'selective_number_commutation_{idx}_{sign}', F * N, N * F)
            channel += unnorm
        channel = clean(channel)
        equal(f'nonselective_channel_{idx}', channel, (1 + eta) * rho / 2 + (1 - eta) * B * rho * B / 2)
        equal(f'nonselective_energy_change_{idx}', sp.trace((channel - rho) * H), -(1 - eta) * mean(Hinc))
        for f in protected:
            target = eta * mean(currents[f]) if 0 in f else mean(currents[f])
            equal(f'nonselective_current_{idx}_{f}', sp.trace(channel * currents[f]), target)
        # Disturbance is witnessed on an actual pair of physical code states.
        basis_plus = (P * (eye + B) / 2).columnspace()[0]
        basis_minus = (P * (eye - B) / 2).columnspace()[0]
        ep = basis_plus / sp.sqrt((basis_plus.H * basis_plus)[0])
        em = basis_minus / sp.sqrt((basis_minus.H * basis_minus)[0])
        psi = (ep + em) / sp.sqrt(2)
        delta = clean((1 - eta) * (B * psi * psi.H * B - psi * psi.H) / 2)
        trace_norm = sum(abs(value) * mult for value, mult in delta.eigenvals().items())
        equal(f'diamond_lower_witness_{idx}', trace_norm, 1 - eta)
        equal(f'contrast_disturbance_saturation_{idx}', kappa**2, 2 * (1 - eta) - (1 - eta)**2)

    # Literal physical plaquette stars in the three-dimensional placement.
    vertices = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0))
    factors = set()
    for v in vertices:
        for axis, sign in product(range(3), (1, -1)):
            site = [2*x for x in v]
            site[axis] += sign
            factors.add(tuple(site))
    checked('literal_plaquette_star_support', len(factors) == 20 and
            max(sum(abs(x - y) for x, y in zip(p, (1, 0, 0))) for p in factors) == 4,
            factors=20, radius=4)

    # Two adjacent literal squares, with both bottom edges candidates and
    # all five other edges forming one connected protected tree. The second
    # effect anticommutes with the first; its cycle must survive event one.
    ge, ge_eye, ge_z, ge_b, ge_a = native_graph(
        [(0, 1), (1, 2), (0, 3), (1, 4), (2, 5), (3, 4), (4, 5)])
    se = ge_a[0, 1] * ge_a[1, 4] * ge_a[4, 3] * ge_a[3, 0]
    sf = ge_a[1, 2] * ge_a[2, 5] * ge_a[5, 4] * ge_a[4, 1]
    ze, zf = ge_z[ge.index((0, 1))], ge_z[ge.index((1, 2))]
    pe = clean((ge_eye + se) * (ge_eye + sf) / 4)
    first, second = ge_b[0], ge_a[0, 3]
    equal('two_event_effects_really_noncommute', first * second + second * first, sp.zeros(128))
    checked('two_event_native_code_dimension', pe.rank() == 32)
    ue = clean((3 * ge_eye + first * ze * se) / sp.sqrt(10))
    uf = clean((5 * ge_eye + second * zf * sf) / sp.sqrt(26))
    equal('unused_cycle_survives_first_pulse', sf * ue, ue * sf)
    equal('old_Record_commutes_next_pulse', ze * uf, uf * ze)
    for z1, z2 in product((1, -1), repeat=2):
        q1, q2 = (ge_eye + z1 * ze) / 2, (ge_eye + z2 * zf) / 2
        p1 = clean(q1 * (ge_eye + sf) / 2)
        j1, j2 = sp.sqrt(2) * q1 * pe, sp.sqrt(2) * q2 * p1
        f1 = (3 * ge_eye + z1 * first) / sp.sqrt(20)
        f2 = (5 * ge_eye + z2 * second) / sp.sqrt(52)
        actual = clean(q2 * uf * q1 * ue * pe)
        equal(f'two_native_noncommuting_events_{z1}_{z2}', actual, j2 * j1 * f2 * f1 * pe)
        equal(f'permanent_Record_final_code_{z1}_{z2}', q1 * q2 * actual, actual)
        equal(f'ordered_history_effect_{z1}_{z2}', actual.H * actual,
              pe * f1 * f2 * f2 * f1 * pe)

    # Independent CAR representation verifies the native current sign and the
    # complete rank-one Slater filtering formula, including complex phases.
    ann = annihilators(4)
    feye = sp.eye(16)
    numbers = [a.H * a for a in ann]
    parities = [feye - 2 * n for n in numbers]
    checked('independent_CAR_relations', all(ann[i] * ann[j].H + ann[j].H * ann[i] == (feye if i == j else sp.zeros(16))
                                              and ann[i] * ann[j] + ann[j] * ann[i] == sp.zeros(16)
                                              for i, j in product(range(4), repeat=2)))
    for i, j in [(0, 1), (0, 3), (2, 3)]:
        ai = -sp.I * (ann[i] + ann[i].H) * (ann[j] + ann[j].H)
        current = sp.I * (ann[i].H * ann[j] - ann[j].H * ann[i])
        equal(f'CAR_native_current_dictionary_{i}_{j}', -ai * (feye - parities[i] * parities[j]) / 2, current)
    V = sp.Matrix([[1, 0], [sp.I, 0], [0, 1], [0, 1]]) / sp.sqrt(2)
    vac = feye[:, 0]
    create = lambda column: sum((V[j, column] * ann[j].H for j in range(4)), sp.zeros(16))
    psi = clean(create(0) * create(1) * vac)
    frho = clean(psi * psi.H)
    C = clean(V * V.H)
    equal('initial_even_Slater_covariance', covariance(frho, ann), C)
    equal('initial_even_Slater_two_particles', sum(sp.trace(frho * n) for n in numbers), 2)
    c, s, kappa = 3 / sp.sqrt(10), 1 / sp.sqrt(10), sp.Rational(3, 5)
    for sign in (1, -1):
        v = 0
        FF = (c * feye + sign * s * parities[v]) / sp.sqrt(2)
        rr = sp.simplify((c - sign * s) / (c + sign * s))
        az = (c + sign * s) / sp.sqrt(2)
        R = sp.eye(4)
        R[v, v] = rr
        d = rr**2 - 1
        e = sp.eye(4)[:, v]
        formula = clean(R * (C - d * C * e * e.H * C / (1 + d * C[v, v])) * R)
        unnorm = clean(FF * frho * FF)
        prob = clean(sp.trace(unnorm))
        updated = clean(unnorm / prob)
        equal(f'Slater_filter_probability_{sign}', prob, az**2 * (1 + d * C[v, v]))
        equal(f'Slater_filter_CAR_vs_Gram_{sign}', covariance(updated, ann), formula)
        equal(f'Slater_filtered_projector_{sign}', formula * formula, formula)
        equal(f'Slater_filtered_particle_number_{sign}', sp.trace(formula), 2)
        # A number-conserving free mixing on modes1,2, constructed in Fock
        # space from the actual hopping involution on its active subspace.
        hop = ann[1].H * ann[2] + ann[2].H * ann[1]
        active = hop * hop
        dwell = feye + (1 / sp.sqrt(2) - 1) * active - sp.I * hop / sp.sqrt(2)
        onehop = sp.zeros(4)
        onehop[1, 2] = onehop[2, 1] = 1
        oneU = sp.eye(4) + (1 / sp.sqrt(2) - 1) * onehop**2 - sp.I * onehop / sp.sqrt(2)
        after = clean(dwell * updated * dwell.H)
        Cafter = clean(oneU * formula * oneU.H)
        equal(f'free_dwell_CAR_vs_orbitals_{sign}', covariance(after, ann), Cafter)
        for second in (1, -1):
            FF2 = (c * feye + second * s * parities[2]) / sp.sqrt(2)
            final = clean(FF2 * after * FF2)
            final /= sp.trace(final)
            r2 = sp.simplify((c - second * s) / (c + second * s))
            R2 = sp.diag(1, 1, r2, 1)
            e2 = sp.eye(4)[:, 2]
            d2 = r2**2 - 1
            prediction = clean(R2 * (Cafter - d2 * Cafter * e2 * e2.H * Cafter / (1 + d2 * Cafter[2, 2])) * R2)
            equal(f'interleaved_two_event_Slater_history_{sign}_{second}', covariance(final, ann), prediction)
    # An explicit selective sector-weight change prevents a stronger false
    # particle-number statement from slipping into the theorem.
    pair = feye[:, 3]
    mixture = (vac * vac.H + pair * pair.H) / 2
    FF = (c * feye + s * parities[0]) / sp.sqrt(2)
    chosen = clean(FF * mixture * FF)
    chosen /= sp.trace(chosen)
    beforeN = sum(sp.trace(mixture * n) for n in numbers)
    afterN = sum(sp.trace(chosen * n) for n in numbers)
    checked('selective_number_distribution_is_not_preserved', beforeN == 1 and afterN == sp.Rational(2, 5),
            before=str(beforeN), after=str(afterN))
    # The two-law minimax bound is evaluated independently from the native
    # code probabilities, not by treating a quantum input as framework state.
    distributions = [(sp.Rational(4, 5), sp.Rational(1, 5)), (sp.Rational(1, 5), sp.Rational(4, 5))]
    variation = sum(abs(a - b) for a, b in zip(*distributions)) / 2
    midpoint = [sum(pair) / 2 for pair in zip(*distributions)]
    radius = max(sum(abs(x - y) for x, y in zip(p, midpoint)) / 2 for p in distributions)
    checked('same_condition_pair_minimax', variation == sp.Rational(3, 5) and radius == sp.Rational(3, 10))
    elapsed = time.monotonic() - start
    return {'status': 'pass', 'checks': checks, 'total_pass': len(checks), 'total_fail': 0,
            'elapsed_seconds': elapsed, 'runner_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == '__main__':
    import signal
    signal.alarm(AUDIT_TIMEOUT_SEC)
    result = run()
    print(json.dumps(result, indent=2))
    print('per_element: Full physical effect, square-root and Kraus identities are checked exactly, including zero branches.')
    print('per_site: Native edge Record, twenty-factor plaquette support and physical radius four are checked.')
    print('per_mode: Four independently constructed CAR modes verify current signs and complex Slater updates.')
    print('per_block: Two noncommuting native events and interleaved Slater histories preserve their declared code conditions.')
    print('lattice_wide: checked and not executed — the finite-graph theorem follows from the written algebra; no thermodynamic or complete local-law result is claimed.')
    print(f"TOTAL: PASS={result['total_pass']} FAIL={result['total_fail']}")
    signal.alarm(0)
