#!/usr/bin/env python3
"""Independent exact finite-word check; no author or parent builder import.

Every amplitude is an integer. Real and imaginary coefficients are accumulated
separately, and expectation values use Fraction. This is an algebraic control on
selected physical words, not a semigroup simulation or uniform Taylor bound.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import hashlib
import json


def sparse(d):
    return tuple(sorted((k, v) for k, v in d.items() if v))


def add_sparse(x, y, factor=1):
    d = dict(x)
    for k, v in y:
        d[k] = d.get(k, 0) + factor * v
    return sparse(d)


def dot(x, y):
    d = dict(y)
    return sum(v * d.get(k, 0) for k, v in x)


def clean(d):
    return {k: v for k, v in d.items() if v}


def add_vector(out, vec, factor=1):
    for w, v in vec.items():
        out[w] += factor * v


class PrimitiveGraph:
    def __init__(self, name, side=None):
        self.name = name
        self.side = side
        coords = list(product(range(side or 2), repeat=3))
        self.coords = coords
        self.A = tuple(i for i, x in enumerate(coords) if sum(x) % 2 == 0)
        self.Aset = set(self.A)
        self.B = tuple(i for i in range(len(coords)) if i not in self.Aset)
        inv = {x: i for i, x in enumerate(coords)}
        edges = set()
        for a in self.A:
            for axis in range(3):
                if side is None:
                    x = list(coords[a]); x[axis] = 1 - x[axis]
                    edges.add((a, inv[tuple(x)]))
                else:
                    for step in (-1, 1):
                        x = list(coords[a]); x[axis] = (x[axis] + step) % side
                        edges.add((a, inv[tuple(x)]))
        self.edges = sorted(edges)
        self.eid = {e: i for i, e in enumerate(self.edges)}
        self.neigh = defaultdict(list)
        self.atB = defaultdict(list)
        for e, (a, b) in enumerate(self.edges):
            self.neigh[a].append((b, e)); self.atB[b].append((a, e))
        self.pairs = []
        self.plaquettes = []
        for a, c in combinations(self.A, 2):
            common = sorted(set(b for b, _ in self.neigh[a]) &
                            set(b for b, _ in self.neigh[c]))
            if common:
                self.pairs.append((a, c, len(common)))
            for b, d in combinations(common, 2):
                p = sparse({self.eid[a, b]: 1, self.eid[c, b]: -1,
                            self.eid[c, d]: 1, self.eid[a, d]: -1})
                self.plaquettes.append(p)
        self.nu = {b: sum(len(self.neigh[a]) - 1 for a, _ in self.atB[b])
                   for b in self.B}
        self.R = 2 * sum(len(self.neigh[a]) * (len(self.neigh[a]) - 1)
                         for a in self.A)

    def charge(self, qdiff, x):
        return (1 if x in self.Aset else 0) + qdiff.get(x, 0)

    def alter(self, w, changes, e, shift):
        qd, E = dict(w[0]), dict(w[1])
        for x, val in changes.items():
            qd[x] = val - (1 if x in self.Aset else 0)
        E[e] = E.get(e, 0) + shift
        return sparse(qd), sparse(E)

    def inP(self, w):
        qd = dict(w[0])
        return all(self.charge(qd, a) != 0 for a in self.A)

    def physical(self, w):
        qd = dict(w[0]); div = defaultdict(int)
        for e, val in w[1]:
            a, b = self.edges[e]; div[a] += val; div[b] -= val
        assert sparse(div) == w[0], (self.name, w, sparse(div))
        assert all(self.charge(qd, x) in (-1, 0, 1)
                   for x in set(qd) | self.Aset)

    def F(self, w, a, adjoint=False):
        qd = dict(w[0]); qa = self.charge(qd, a)
        out = defaultdict(int)
        if not adjoint and qa:
            for b, e in self.neigh[a]:
                if self.charge(qd, b) == 0:
                    out[self.alter(w, {a: 0, b: qa}, e, -qa)] += 1
        if adjoint and qa == 0:
            for b, e in self.neigh[a]:
                qb = self.charge(qd, b)
                if qb:
                    out[self.alter(w, {a: qb, b: 0}, e, qb)] += 1
        return dict(out)

    def j(self, w, e, sigma, adjoint=False):
        a, b = self.edges[e]; qd = dict(w[0])
        qa, qb = self.charge(qd, a), self.charge(qd, b)
        if not adjoint and qa == qb == 0:
            return {self.alter(w, {a: sigma, b: -sigma}, e, sigma): 1}
        if adjoint and qa == sigma and qb == -sigma:
            return {self.alter(w, {a: 0, b: 0}, e, -sigma): 1}
        return {}

    def Bop(self, w, e, signs, adjoint=False):
        a, _ = self.edges[e]; out = defaultdict(int)
        if not self.inP(w):
            return {}
        if not adjoint:
            for x, u in self.F(w, a).items():
                for sigma in signs:
                    for y, v in self.j(x, e, sigma).items():
                        if self.inP(y): out[y] += u * v
        else:
            for sigma in signs:
                for x, u in self.j(w, e, sigma, True).items():
                    for y, v in self.F(x, a, True).items():
                        if self.inP(y): out[y] += u * v
        return clean(out)

    def D(self, w, freeze_charge=False, field_only=False):
        if field_only:
            return sum(v * v for _, v in w[1])
        qd = dict(w[0]); ans = 0
        for e, val in w[1]:
            a, b = self.edges[e]
            if self.charge(qd, b) == 0:
                qa = 1 if freeze_charge else self.charge(qd, a)
                ans += val * (val - qa)
        return ans

    def W(self, w, loop):
        return w[0], add_sparse(w[1], loop)

    def d(self, w, loop, **kwargs):
        return self.D(self.W(w, loop), **kwargs) - self.D(w, **kwargs)

    def apply_F(self, vec, a, adjoint=False):
        out = defaultdict(int)
        for w, coeff in vec.items():
            add_vector(out, self.F(w, a, adjoint), coeff)
        return clean(out)

    def magnetic_from_primitives(self, w):
        out = defaultdict(int)
        for a, c, _ in self.pairs:
            vec = {w: 1}
            for site, adjoint in ((a, False), (c, False), (c, True), (a, True)):
                vec = self.apply_F(vec, site, adjoint)
            add_vector(out, {x: u for x, u in vec.items() if self.inP(x)}, -2)
        return clean(out)


def graph_check(g):
    zero = ((), ())
    l = g.plaquettes[0]
    other = next(p for p in g.plaquettes[1:] if dot(l, p))
    Etests = [(), l, add_sparse(l, other, 2)]
    for E in Etests: g.physical(((), E))
    mag = g.magnetic_from_primitives(zero)
    expected_mag = defaultdict(int)
    cG = -2 * sum(len(g.neigh[a]) * len(g.neigh[c]) - r for a, c, r in g.pairs)
    expected_mag[zero] += cG
    for p in g.plaquettes:
        expected_mag[((), p)] -= 2
        expected_mag[((), add_sparse((), p, -1))] -= 2
    assert mag == clean(expected_mag)
    for word in mag: g.physical(word)
    assert all(qd == () for qd, _ in mag)
    mag_kernel = {E: v for (_, E), v in mag.items()}

    def H0(w):
        assert w[0] == ()
        out = defaultdict(int)
        out[w] += g.D(w)
        for p, coeff in mag_kernel.items():
            out[g.W(w, p)] += coeff
        return clean(out)

    def hamiltonian_second(w):
        # -[H0, W_l A_l], where X = W_l d_l, computed on words.
        out = defaultdict(int)
        add_vector(out, H0(g.W(w, l)), -g.d(w, l))
        for y, coeff in H0(w).items():
            out[g.W(y, l)] += coeff * g.d(y, l)
        return clean(out)

    def expected_hamiltonian_second(w):
        out = defaultdict(int)
        out[g.W(w, l)] -= g.d(w, l) ** 2
        for p in g.plaquettes:
            overlap = dot(l, p)
            out[g.W(g.W(w, l), p)] -= 4 * overlap
            out[g.W(g.W(w, l), add_sparse((), p, -1))] += 4 * overlap
        return clean(out)

    def jump_second(w, coherent, field_only=False):
        out = defaultdict(int)
        for e in range(len(g.edges)):
            marklists = [(1, -1)] if coherent else [(1,), (-1,)]
            for signs in marklists:
                source = g.Bop(w, e, signs)
                for y, coeff in source.items():
                    shifted = g.W(y, l)
                    dy = g.d(y, l, field_only=field_only)
                    add_vector(out, g.Bop(shifted, e, signs, True), coeff * dy)
        out[g.W(w, l)] -= g.R * g.d(w, l, field_only=field_only)
        return clean(out)

    counts = defaultdict(int); drift = defaultdict(int); second = defaultdict(int)
    false_charge_branches = []
    nonzero_postbirth_commutation_checks = 0
    angle_real = angle_imag = 0
    roots = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    gamma_initial = defaultdict(int)
    for e, (a, b) in enumerate(g.edges):
        for sigma in (1, -1):
            source = g.Bop(zero, e, (sigma,))
            assert len(source) == len(g.neigh[a]) - 1
            assert len({word[0] for word in source}) == len(source)
            for y, coeff in source.items():
                assert coeff == 1
                g.physical(y)
                counts[y[1]] += 1
                add_vector(gamma_initial, g.Bop(y, e, (sigma,), True))
                for k, val in y[1]: drift[k] += val
                for k, val in y[1]:
                    for m, val2 in y[1]: second[k, m] += val * val2
                r, i = roots[dot(y[1], l) % 4]
                angle_real += r - 1; angle_imag += i
                # Check FULL matter-dependent d on each birth, not just its sum.
                qd = dict(y[0])
                occupied_B = [x for x in g.B if g.charge(qd, x)]
                assert len(occupied_B) == 2 and b in occupied_B
                dsite = next(x for x in occupied_B if x != b)
                expected_shift = sparse({e: sigma, g.eid[a, dsite]: -1})
                assert y[1] == expected_shift
                deleted = {edge for x in occupied_B for _, edge in g.atB[x]}
                A0 = dot(l, l)
                target = A0 - sum(val * val for edge, val in l if edge in deleted)
                if sigma == -1:
                    ld = dict(l)
                    target -= 2 * (ld.get(e, 0) + ld.get(g.eid[a, dsite], 0))
                assert g.d(y, l) == target
                wrong = g.d(y, l, freeze_charge=True)
                if wrong != target:
                    false_charge_branches.append([e, sigma, dsite, target, wrong])
                # A Wilson loop commutes with the original primitive B, even
                # on the born state when another formation is possible.
                if e == 0:
                    second_edge = next(f for f in range(len(g.edges))
                                       if g.Bop(y, f, (1, -1)))
                    lhs = g.Bop(g.W(y, l), second_edge, (1, -1))
                    rhs = {g.W(v, l): u for v, u in
                           g.Bop(y, second_edge, (1, -1)).items()}
                    assert lhs == rhs and lhs
                    nonzero_postbirth_commutation_checks += 1
    assert clean(gamma_initial) == {zero: g.R}
    assert sum(counts.values()) == g.R
    expected_counts = defaultdict(int)
    direct_angle_real = direct_angle_imag = 0
    for a in g.A:
        for b, e in g.neigh[a]:
            for dsite, f in g.neigh[a]:
                if b == dsite: continue
                for sigma in (1, -1):
                    kick = sparse({e: sigma, f: -1})
                    expected_counts[kick] += 1
                    r, i = roots[(sigma * dict(l).get(e, 0) - dict(l).get(f, 0)) % 4]
                    direct_angle_real += r - 1; direct_angle_imag += i
    assert counts == expected_counts
    assert (angle_real, angle_imag) == (direct_angle_real, direct_angle_imag)
    assert clean(drift) == {e: -2 * (len(g.neigh[a]) - 1) for e, (a, _) in enumerate(g.edges)}
    assert clean(second) == {(e, e): 4 * (len(g.neigh[a]) - 1) for e, (a, _) in enumerate(g.edges)}
    assert sum(v * drift[e] for e, v in l) == 0
    zset = {len(g.neigh[a]) for a in g.A} | {len(g.atB[b]) for b in g.B}
    assert len(zset) == 1
    z = zset.pop(); gamma = 4 * z * (z - 1)
    assert all(v == z * (z - 1) for v in g.nu.values())
    assert false_charge_branches
    assert nonzero_postbirth_commutation_checks == 2 * (z - 1)

    # Retain original coherent channels: equal field source does not mean
    # equal joint source. Per fixed edge, all sign/destination matter labels
    # differ, so only the diagonal of the source survives the matter trace.
    source_plus = g.Bop(zero, 0, (1,))
    source_minus = g.Bop(zero, 0, (-1,))
    source_coh = g.Bop(zero, 0, (1, -1))
    assert len({word[0] for word in source_coh}) == len(source_coh)
    assert source_coh == dict(list(source_plus.items()) + list(source_minus.items()))
    coh_gram = defaultdict(int)
    for y, coeff in source_coh.items():
        add_vector(coh_gram, g.Bop(y, 0, (1, -1), True), coeff)
    assert clean(coh_gram) == {zero: 2 * (z - 1)}
    joint_difference_hs_squared = 2 * len(source_plus) * len(source_minus)
    field_source_res = defaultdict(int); field_source_coh = defaultdict(int)
    for vec in (source_plus, source_minus):
        for y, coeff in vec.items(): field_source_res[y[1]] += coeff * coeff
    for y, coeff in source_coh.items(): field_source_coh[y[1]] += coeff * coeff
    assert field_source_res == field_source_coh

    derivative_records = []
    second_vectors = {}
    for E in Etests:
        w = ((), E); A = g.d(w, l)
        assert A == 2 * dot(l, E) + dot(l, l)
        ham = hamiltonian_second(w)
        assert ham == expected_hamiltonian_second(w)
        jr = jump_second(w, False); jc = jump_second(w, True)
        general_coefficient = -4 * sum(g.nu[g.edges[e][1]] * (2 * val * dict(E).get(e, 0) + val * val)
                                       for e, val in l)
        target_jump = clean({g.W(w, l): general_coefficient})
        assert jr == jc == target_jump
        assert general_coefficient == -gamma * A
        frozen = jump_second(w, False, field_only=True)
        assert frozen == {}
        second_vectors[E] = (ham, jr)
        derivative_records.append({'field': E, 'A_l': A,
                                   'second_real_support': len(ham),
                                   'second_jump_imaginary_coefficient': general_coefficient,
                                   'field_only_D_wrong_jump_coefficient': 0,
                                   'resolved_coherent_equal': True})

    # Exact expectation in (|0> + i|l>)/sqrt(2), with K=delta=kappa=1.
    # Store unnormalized Gaussian integer coefficients, then divide by 2.
    psi = {(): (1, 0), l: (0, 1)}
    def expect(real_vectors, imag_vectors):
        re = im = 0
        for E, (ar, ai) in psi.items():
            keys = set(real_vectors[E]) | set(imag_vectors[E])
            for qd, F in keys:
                if qd or F not in psi: continue
                br, bi = psi[F]
                cr = real_vectors[E].get((qd, F), 0)
                ci = imag_vectors[E].get((qd, F), 0)
                ur, ui = cr * ar - ci * ai, cr * ai + ci * ar
                re += br * ur + bi * ui
                im += br * ui - bi * ur
        return Fraction(re, 2), Fraction(im, 2)
    real0 = {E: {g.W(((), E), l): 1} for E in psi}
    zero_vec = {E: {} for E in psi}
    imag1 = {E: {g.W(((), E), l): g.d(((), E), l)} for E in psi}
    real2 = {E: second_vectors[E][0] for E in psi}
    imag2 = {E: second_vectors[E][1] for E in psi}
    w0 = expect(real0, zero_vec); w1 = expect(zero_vec, imag1)
    w2 = expect(real2, imag2); wham2 = expect(real2, zero_vec)
    assert w0 == (0, Fraction(-1, 2))
    assert w1 == (2, 0)
    assert wham2 == (16, 8)
    assert w2 == (16 - 2 * gamma, 8)
    return {
        'graph': g.name, 'side': g.side,
        'vertices': len(g.coords), 'A': len(g.A), 'B': len(g.B), 'edges': len(g.edges),
        'degree': z, 'dist2_A_pairs': len(g.pairs),
        'common_neighbor_histogram': {str(r): sum(1 for _, _, rr in g.pairs if rr == r) for _, _, r in g.pairs},
        'simple_unoriented_four_cycles': len(g.plaquettes),
        'primitive_H4_initial_scalar': cG,
        'primitive_H4_initial_support': len(mag),
        'loss_rate_divided_by_kappa': g.R,
        'per_edge_electric_drift_divided_by_kappa': -2 * (z - 1),
        'per_edge_electric_covariance_rate_divided_by_kappa': 4 * (z - 1),
        'loop_norm_squared': dot(l, l),
        'loop_electric_variance_rate_divided_by_kappa': sum(v * v * second[e, e] for e, v in l),
        'loop_transverse_mean_drift': sum(v * drift[e] for e, v in l),
        'initial_Wilson_second_coefficient_gamma_divided_by_kappa': gamma,
        'angle_kernel_at_u_pi_over_2_times_loop_divided_by_kappa': [angle_real, angle_imag],
        'coherent_resolved_fixed_edge_joint_source_difference_hs_squared': joint_difference_hs_squared,
        'coherent_resolved_fixed_edge_reduced_field_source_equal': True,
        'incorrect_frozen_A_charge_detected_branch_count': len(false_charge_branches),
        'nonzero_postbirth_primitive_jump_commutation_checks': nonzero_postbirth_commutation_checks,
        'first_incorrect_frozen_A_charge_example_e_sigma_d_correct_wrong': false_charge_branches[0],
        'word_derivatives': derivative_records,
        'psi_zero_plus_i_loop': {'parameters': {'K': 1, 'delta': 1, 'kappa': 1},
                               'W_0': [str(x) for x in w0],
                               'W_prime_0': [str(x) for x in w1],
                               'W_double_prime_0_hamiltonian_only': [str(x) for x in wham2],
                               'W_double_prime_0_full': [str(x) for x in w2]},
        'checks': 'exact integer sparse-word equalities passed; no state truncation or floating eigensolver used',
    }


def main():
    base = Path(__file__).resolve().parent
    pins = json.loads((base / 'SOURCE_PINS.json').read_text())
    for src in pins['sources']:
        data = (base / src['snapshot']).read_bytes()
        assert hashlib.sha256(data).hexdigest() == src['sha256']
    result = {
        'scope': 'Independent primitive finite-word corroboration of initial rotor identities only; analytic proof supplies graph/state generality. No photon propagation or finite-time damping is tested.',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_pins_sha256': hashlib.sha256((base / 'SOURCE_PINS.json').read_bytes()).hexdigest(),
        'graphs': [graph_check(PrimitiveGraph('cube')), graph_check(PrimitiveGraph('periodic_6x6x6_cubic_torus', side=6))],
        'overall': 'all exact checks passed',
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + '\n'
    (base / 'PRIMITIVE_RESULTS.json').write_text(payload)
    print(payload, end='')


if __name__ == '__main__':
    main()
