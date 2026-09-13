"""Exact finite marginal and physical-geometry checks of Block16.

The continuous matrix-law argument is in the proof, not simulated here.
One path uses powers of the derived binary channel. The other sums every
copy / fresh-plus / fresh-minus history, including failed copies.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import time

HERE = Path(__file__).resolve().parent
AUDIT_TIMEOUT_SEC = 180
SIGNS = (1, -1)


@dataclass(frozen=True)
class Radical:
    """The exact real field Q(sqrt(2)), with a checked sign operation."""
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def of(value):
        return value if isinstance(value, Radical) else Radical(F(value))

    def __add__(self, other):
        other = self.of(other)
        return Radical(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Radical(-self.a, -self.b)

    def __sub__(self, other):
        return self + -self.of(other)

    def __mul__(self, other):
        other = self.of(other)
        return Radical(self.a * other.a + 2 * self.b * other.b,
                       self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def sign(self):
        if not self.b:
            return (self.a > 0) - (self.a < 0)
        if not self.a:
            return (self.b > 0) - (self.b < 0)
        if self.a * self.b > 0:
            return (self.a > 0) - (self.a < 0)
        delta = self.a * self.a - 2 * self.b * self.b
        return ((self.a > 0) - (self.a < 0)) * ((delta > 0) - (delta < 0))

    def absolute(self):
        return self if self.sign() >= 0 else -self

    def record(self):
        return {'rational': str(self.a), 'sqrt2_coefficient': str(self.b)}


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def scale(c, x):
    return tuple(c * a for a in x)


AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
OFFSETS = tuple(scale(s, e) for e in AXES for s in SIGNS)


def neighbors(site, records):
    return {add(site, d) for d in OFFSETS} & set(records)


def proper_rotations():
    answer = []
    for p in permutations(range(3)):
        parity = (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
        for signs in product(SIGNS, repeat=3):
            if parity * signs[0] * signs[1] * signs[2] == 1:
                answer.append(tuple(scale(signs[j], AXES[p[j]]) for j in range(3)))
    return answer


def rotate(matrix, vector):
    return tuple(sum(matrix[j][i] * vector[j] for j in range(3)) for i in range(3))


def matrix_product(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def run():
    start = time.monotonic()
    checks = []

    def checked(name, condition, **data):
        assert condition, name
        checks.append({'name': name, **data})

    lam = F(19, 20)
    kappa = lam ** 6
    checked('exact_six_draw_attenuation', kappa == F(47045881, 64000000))
    checked('strict_positive_quantum_arm_table', 2 * kappa ** 2 > 1)
    checked('radical_arithmetic_sign_sanity',
            Radical(F(1), F(-1)).sign() == -1 and
            Radical(F(3), F(-2)).sign() == 1 and
            Radical(F(-3), F(2)).sign() == -1 and
            Radical(F(0), F(1)) * Radical(F(0), F(1)) == Radical(F(2)))
    channel = [[(1 + lam * x * s) / 2 for s in SIGNS] for x in SIGNS]
    checked('one_step_channel', channel == [[F(39, 40), F(1, 40)], [F(1, 40), F(39, 40)]])
    channel2 = matrix_product(channel, channel)
    channel3 = matrix_product(channel2, channel)
    checked('three_step_channel', channel3 == [[(1 + lam ** 3 * x * s) / 2 for s in SIGNS] for x in SIGNS])

    # A second path: retain all three alternatives at EACH actual local draw.
    # 'copy' has weight lambda, fresh +/- each have weight (1-lambda)/2.
    # These paths retain redundant histories that produce the same readout.
    paths = {}
    for arm in SIGNS:
        local_paths = []
        for history in product(('copy', 'plus', 'minus'), repeat=3):
            current = arm
            weight = F(1)
            for choice in history:
                if choice == 'copy':
                    weight *= lam
                else:
                    weight *= (1 - lam) / 2
                    current = 1 if choice == 'plus' else -1
            local_paths.append((current, weight, history))
        paths[arm] = local_paths
        checked('complete_three_draw_paths_' + str(arm), len(local_paths) == 27 and sum(w for _, w, _ in local_paths) == 1)
        checked('path_marginal_matches_matrix_' + str(arm),
                all(sum(w for x, w, _ in local_paths if x == out) == channel3[i][SIGNS.index(arm)]
                    for i, out in enumerate(SIGNS)))

    def arm_table(model, a, b):
        parity = (-1) ** (a * b)
        if model == 'independent':
            return {(s, t): Radical(F(1, 4)) for s, t in product(SIGNS, repeat=2)}
        if model == 'quantum_comparison':
            return {(s, t): Radical(F(1, 4), -F(s * t * parity, 8) / kappa)
                    for s, t in product(SIGNS, repeat=2)}
        return {(s, t): Radical(F(1, 2) if s * t == parity else F(0))
                for s, t in product(SIGNS, repeat=2)}

    results = {}
    for model in ('independent', 'quantum_comparison', 'larger_comparison'):
        correlations = {}
        model_tables = {}
        for a, b in product((0, 1), repeat=2):
            q = arm_table(model, a, b)
            checked(f'{model}_{a}{b}_arm_probability',
                    sum(q.values(), Radical()) == Radical(F(1)) and all(v.sign() >= 0 for v in q.values())
                    and all(sum(q[s, t] for t in SIGNS) == Radical(F(1, 2)) for s in SIGNS)
                    and all(sum(q[s, t] for s in SIGNS) == Radical(F(1, 2)) for t in SIGNS))
            by_matrix = {(x, y): sum((q[s, t] * channel3[i][SIGNS.index(s)] * channel3[j][SIGNS.index(t)]
                                      for s, t in product(SIGNS, repeat=2)), Radical())
                         for i, x in enumerate(SIGNS) for j, y in enumerate(SIGNS)}
            by_paths = {(x, y): Radical() for x, y in product(SIGNS, repeat=2)}
            number = 0
            for s, t in product(SIGNS, repeat=2):
                for (x, wx, _), (y, wy, _) in product(paths[s], paths[t]):
                    by_paths[x, y] += q[s, t] * wx * wy
                    number += 1
            checked(f'{model}_{a}{b}_complete_branch_sum',
                    number == 2916 and by_paths == by_matrix and sum(by_paths.values(), Radical()) == Radical(F(1)),
                    enumerated_paths=number)
            e = sum((x * y * weight for (x, y), weight in by_paths.items()), Radical())
            parity = (-1) ** (a * b)
            expected = {'independent': Radical(),
                        'quantum_comparison': Radical(F(0), F(-parity, 2)),
                        'larger_comparison': Radical(kappa * parity)}[model]
            checked(f'{model}_{a}{b}_fixed_output_table', e == expected
                    and all(v == (Radical(F(1)) + x * y * e) * F(1, 4) for (x, y), v in by_paths.items())
                    and all(sum(by_paths[x, y] for y in SIGNS) == Radical(F(1, 2)) for x in SIGNS)
                    and all(sum(by_paths[x, y] for x in SIGNS) == Radical(F(1, 2)) for y in SIGNS))
            correlations[a, b] = e
            model_tables[str((a, b))] = {str(key): val.record() for key, val in by_paths.items()}
        chsh = (correlations[0, 0] + correlations[0, 1] + correlations[1, 0] - correlations[1, 1]).absolute()
        expected_chsh = {'independent': Radical(), 'quantum_comparison': Radical(0, F(2)),
                         'larger_comparison': Radical(4 * kappa)}[model]
        checked(model + '_CHSH', chsh == expected_chsh, exact=chsh.record())
        results[model] = {'CHSH': chsh.record(), 'tables': model_tables}

    checked('larger_comparison_strictly_exceeds_quantum', (Radical(4 * kappa) - Radical(0, F(2))).sign() == 1)
    checked('settings_independent_fair_and_complete', sum(F(1, 4) for _ in product((0, 1), repeat=2)) == 1)
    checked('omitted_noise_step_changes_quantum_target', lam ** 4 != kappa and
            (Radical(0, -F(1, 2) * lam ** 4 / kappa) != Radical(0, -F(1, 2))))
    checked('arm_location_is_not_final_readout', channel3[0][1] > 0 and channel3[0][1] < F(1, 2))
    copy_only_mass = lam ** 6
    checked('copy_only_postselection_discards_mass_and_changes_output', copy_only_mass < 1 and
            Radical(0, -F(1, 2) / kappa) != Radical(0, -F(1, 2)), retained_mass_if_wrong=str(copy_only_mass))

    # Actual physical lattice geometry. Symbolic contents are immutable labels;
    # the neighbor test concerns occurrences and thus covers ALL matrix draws.
    centers = ((0, 0, 0), (20, 0, 0))
    settings = tuple(add(c, (0, 10, 0)) for c in centers)
    f = (-10, -10, -10)
    marker_offsets = ((0, 0, 0), (1, 0, 0), (0, 2, 0), (0, 0, 3))
    markers = {add(f, d): 'marker' + str(j) for j, d in enumerate(marker_offsets)}
    initial = dict(markers)
    for center, setting in zip(centers, settings):
        for s in SIGNS:
            initial[add(center, (3 * s, 0, 0))] = 'seed' + str(s)
            initial[add(setting, (0, 0, s))] = 'setting_seed' + str(s)
    checked('twelve_distinct_prepared_records', len(initial) == 12 and len(markers) == 4)
    all_domains = []
    for arms in product(SIGNS, repeat=2):
        records = dict(initial)
        transitions = []
        stages = [settings,
                  tuple(add(c, (2 * s, 0, 0)) for c, s in zip(centers, arms)),
                  tuple(add(c, (s, 0, 0)) for c, s in zip(centers, arms)), centers]
        for stage, sites in enumerate(stages):
            before = dict(records)
            for wing, (site, center, setting, arm) in enumerate(zip(sites, centers, settings, arms)):
                if stage == 0:
                    expected = {add(setting, (0, 0, s)) for s in SIGNS}
                else:
                    expected = {add(center, ((4 - stage) * arm, 0, 0))}
                assert neighbors(site, records) == expected, (arms, stage, wing, neighbors(site, records), expected)
                assert site not in records and not (neighbors(site, records) & set(markers))
            assert sites[1] not in {add(sites[0], d) for d in OFFSETS}
            for wing, site in enumerate(sites):
                records[site] = ('new_content', stage, wing)
            assert all(records[x] == content for x, content in before.items())
            assert len(records) == 14 + 2 * stage
            transitions.append((before, sites))
        checked('all_six_neighbor_lists_and_permanence_' + str(arms), len(records) == 20
                and all(c in records for c in centers)
                and all(add(c, (-d * s, 0, 0)) not in records for c, s in zip(centers, arms) for d in (1, 2)))
        all_domains.append((arms, records, transitions))

    rotations = proper_rotations()
    checked('twenty_four_proper_rotations', len(rotations) == 24 and len(set(rotations)) == 24)
    translation = (31, -17, 9)
    covariance_cases = 0
    for rotation in rotations:
        def transform(site):
            return add(rotate(rotation, site), translation)
        assert {rotate(rotation, d) for d in OFFSETS} == set(OFFSETS)
        for _, _, transitions in all_domains:
            for before, sites in transitions:
                transported = {transform(x): value for x, value in before.items()}
                for site in sites:
                    assert neighbors(transform(site), transported) == {transform(x) for x in neighbors(site, before)}
                    covariance_cases += 1
    checked('literal_translated_rotated_neighbor_covariance', covariance_cases == 768, cases=covariance_cases)

    # Stronger than relying on marker contents being unique: even if a fresh
    # Gaussian has one of those exact values, no second marker GEOMETRY can
    # occur anywhere in the union of all possible event sites.
    total_domain = set().union(*(set(records) for _, records, _ in all_domains))
    frame_candidates = []
    for origin in total_domain:
        for rotation in rotations:
            if {add(origin, rotate(rotation, d)) for d in marker_offsets} <= total_domain:
                frame_candidates.append((origin, rotation))
    checked('unique_marker_geometry_even_for_exceptional_contents', len(frame_candidates) == 1
            and frame_candidates[0][0] == f and frame_candidates[0][1] == AXES,
            total_possible_sites=len(total_domain), frames=len(frame_candidates))
    dirty = dict(initial)
    dirty[(-1, 0, 0)] = 'unintended_opposite_source'
    dirty[(1, 0, 0)] = 'selected_second_relay'
    checked('opposite_nearest_neighbor_contamination_detected', neighbors(centers[0], dirty) != {(1, 0, 0)})

    # Independent elementary finite Bell vertices, with its extra hypotheses.
    vertices = [a0 * (b0 + b1) + a1 * (b0 - b1) for a0, a1, b0, b1 in product(SIGNS, repeat=4)]
    checked('factorized_deterministic_CHSH_vertices', len(vertices) == 16 and set(vertices) == {-2, 2},
            scope='separately assumed setting-independent local response factorization')
    return {'status': 'passed', 'count': len(checks), 'checks': checks, 'results': results,
            'seconds': time.monotonic() - start,
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'derivation_sha256': hashlib.sha256((HERE / 'BLOCK16_DERIVATION.md').read_bytes()).hexdigest(),
            'scope': 'Exact marginal probabilities and physical finite geometry; full-support continuous-kernel and axiom interpretation require the written proof. Supplied occurrence tables, not a Born derivation, causal apparatus, independent review or axiom no-go.'}


if __name__ == '__main__':
    import signal
    signal.alarm(AUDIT_TIMEOUT_SEC)
    result = run()
    (HERE / 'BLOCK16_OCCURRENCE_CHECKS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('checks', 'results')}, indent=2))
