"""Finite author challenges of the commuting exclusion-operator route.

Compares occupancy exclusions with explicit auxiliary operator products and
original weighted cycle sums. Cochains are shared from the forest fixture;
neither these tests nor auxiliary qubits identify the physical field law.
"""
import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from block2_forest_interpolation_check import cochains
from block2_gaussian_cycle_check import compositions


def resource_representation(footprints):
    """Compress resources with identical family membership into one qubit.

    A class of multiplicity r has lowering expectation 2^-r in a unit
    vector. Every family uses the whole class, so all words are preserved.
    """
    groups = {}
    for resource in set().union(*footprints):
        mask = tuple(i for i, s in enumerate(footprints) if resource in s)
        groups[mask] = groups.get(mask, 0)+1
    v = np.ones(1)
    operators = [np.ones((1, 1)) for _ in footprints]
    lower = np.array([[0., 1.], [0., 0.]])
    for members, multiplicity in groups.items():
        mean = 2.**(-multiplicity)
        first = np.sqrt((1+np.sqrt(1-4*mean*mean))/2)
        state = np.array([first, mean/first])
        assert abs(np.linalg.norm(state)-1) < 2e-15
        v = np.kron(v, state)
        for i in range(len(footprints)):
            operators[i] = np.kron(operators[i], lower if i in members else np.eye(2))
    assert abs(np.linalg.norm(v)-1) < 1e-13
    for left, right in itertools.combinations(operators, 2):
        assert np.array_equal(left@right, right@left)
    return v, operators, groups


def hard_core(footprints, labels):
    used = set()
    for label in labels:
        if used & footprints[label]:
            return 0
        used |= footprints[label]
    return 1


def exclusion_words():
    footprints = [{0}, {1}, {0, 1}, {2}, {3}, {2, 3}]
    v, operators, groups = resource_representation(footprints)
    maximum, count = 0., 0
    for length in range(1, 6):
        for labels in itertools.product(range(6), repeat=length):
            out = v.copy()
            for label in reversed(labels):
                out = operators[label]@out
            value = 2**sum(len(footprints[i]) for i in labels)*(v@out)
            error = abs(value-hard_core(footprints, labels))
            maximum = max(maximum, error)
            assert error < 2e-12
            count += 1
    # Projector repeats survive, unlike repeated lowering operators.
    plus = np.ones(2)/np.sqrt(2)
    projector = np.diag([0., 1.])
    wrong_overlap = 4*(plus@projector@projector@plus)
    no_boost_single = plus@np.array([[0., 1.], [0., 0.]])@plus
    assert wrong_overlap > 1.9 and abs(no_boost_single-.5) < 1e-14
    return dict(words=count, maximum_error=float(maximum),
                projector_overlap_wrong_value=float(wrong_overlap),
                missing_boost_single_wrong_value=float(no_boost_single),
                auxiliary_groups=len(groups))


def cycle_fixture(t, footprints, source, seed, all_patterns=True, length=4):
    rng = np.random.default_rng(seed)
    ne, nm = t.shape[1], t.shape[0]
    count = ne+nm
    v, qs, groups = resource_representation(footprints)
    dimension = len(v)
    boost = np.array([2.**len(s) for s in footprints])
    tb = np.sqrt(boost[ne:, None]*boost[None, :ne])*t
    j = np.block([[np.zeros((ne, ne)), tb.T], [tb, np.zeros((nm, nm))]])
    original = np.block([[np.zeros((ne, ne)), t.T], [t, np.zeros((nm, nm))]])
    rho = np.linalg.norm(j, 2)
    big_j = np.kron(j, np.eye(dimension))
    embedding = np.kron(np.eye(count), v[:, None])
    s4 = np.sum(abs(source)**4*np.diag(j@j))
    phase = np.exp(1j*rng.normal(size=(length, count)))
    maximum_error, maximum_ratio = 0., 0.
    patterns = list(compositions(4, length)) if all_patterns else [
        x+(0,)*(length-4) for x in
        [(4, 0, 0, 0), (3, 1, 0, 0), (2, 2, 0, 0), (2, 1, 1, 0), (1, 1, 1, 1)]]
    # Include species projectors and permit all component labels before HC.
    for i in range(length):
        phase[i, ne:] = 0 if i % 2 == 0 else phase[i, ne:]
        phase[i, :ne] = 0 if i % 2 else phase[i, :ne]
    for ks in patterns:
        matrix = np.eye(count*dimension, dtype=complex)
        for i in range(length):
            multiplier = np.zeros_like(matrix)
            for label in range(count):
                sl = slice(label*dimension, (label+1)*dimension)
                multiplier[sl, sl] = phase[i, label]*source[label]**ks[i]*qs[label]
            matrix = matrix@multiplier@big_j
        traced = np.trace(embedding.T@matrix@embedding)
        direct = 0j
        for labels in itertools.product(range(count), repeat=length):
            if not hard_core(footprints, labels):
                continue
            term = 1+0j
            for i, label in enumerate(labels):
                term *= original[label, labels[(i+1) % length]]*phase[i, label]*source[label]**ks[i]
            direct += term
        error = abs(traced-direct)
        # Tolerance is relative to the source bound, with a roundoff floor.
        bound = rho**(length-2)*s4
        assert error <= 3e-12*max(1., bound)
        assert abs(traced) <= bound*(1+3e-12)
        maximum_error = max(maximum_error, error)
        maximum_ratio = max(maximum_ratio, abs(traced)/bound)
    return dict(length=length, source_patterns=len(patterns), groups=len(groups),
                auxiliary_dimension=dimension, rho=float(rho),
                source_bound=float(rho**(length-2)*s4),
                maximum_operator_vs_exclusion_error=float(maximum_error),
                maximum_source_bound_ratio=float(maximum_ratio))


def physical_footprints():
    incidence, p, q = cochains()
    c0, d, b, c3 = incidence
    footprints = [[], []]
    masses = [[], []]
    for face in range(len(p)):
        electric = set(np.flatnonzero(d[face]))
        vertices = set(np.flatnonzero(np.any(c0[list(electric)] != 0, axis=0)))
        footprints[0].append({('e', 'edge', int(e)) for e in electric}
                             | {('e', 'vertex', int(v)) for v in vertices})
        masses[0].append(np.sum(abs(d[face])))
        magnetic = set(np.flatnonzero(b[:, face]))
        cubes4 = set(np.flatnonzero(np.any(c3[:, list(magnetic)] != 0, axis=1)))
        footprints[1].append({('m', 'cell3', int(e)) for e in magnetic}
                             | {('m', 'cell4', int(v)) for v in cubes4})
        masses[1].append(np.sum(abs(b[:, face])))
    tested = 0
    for species in [0, 1]:
        for i, j in itertools.product(range(len(p)), repeat=2):
            # Direct support-graph adjacency, rather than the resource helper.
            if species == 0:
                ci, cj = np.flatnonzero(d[i]), np.flatnonzero(d[j])
                adjacent = bool(set(ci)&set(cj)) or bool(np.any(abs(c0[ci])@abs(c0[cj]).T))
            else:
                ci, cj = np.flatnonzero(b[:, i]), np.flatnonzero(b[:, j])
                adjacent = bool(set(ci)&set(cj)) or bool(np.any(abs(c3[:, ci]).T@abs(c3[:, cj])))
            assert adjacent == bool(footprints[species][i]&footprints[species][j])
            tested += 1
        assert all(len(f) <= 3*m for f, m in zip(footprints[species], masses[species]))
    ne, beta = 3, .5
    h = .013*np.sin(np.arange(len(p))*.79+.3)
    es, ms = [0, 6], [0, 18]
    xe, xm = ne*ne/beta, 4*np.pi*np.pi*beta
    weights_e = np.exp(-xe*np.sum(d[es]**2, axis=1)/64)
    weights_m = np.exp(-xm*np.sum(b[:, ms]**2, axis=0)/64)
    t = np.sqrt(weights_m[:, None]*weights_e[None, :])*np.sin(2*np.pi*ne*p[np.ix_(ms, es)])
    source = np.concatenate([-np.sqrt(xe)*(p@h)[es], -1j*np.sqrt(xm)*(q@h)[ms]])
    selected = [footprints[0][i] for i in es]+[footprints[1][i] for i in ms]
    fixture = cycle_fixture(t, selected, source, 97321)
    return dict(support_pairs=tested, footprint_bound='size <= 3 l1-current mass',
                finite_free_fixture_scope='incidence identity only; no finite-boundary scaling assertion',
                actual_cycle=fixture)


def endpoint():
    mp.mp.dps = 60
    x = mp.mpf(32768)
    def moment(k):
        e = mp.exp(-x/256)
        return 4*1562500*4**k*e/(1-393*2**(2*k+4)*e)
    rho = x*moment(2)+x**3*moment(6)/6
    assert rho < mp.mpf('1e-31')
    assert 4*mp.pi**2*1024 > x and mp.mpf(8192)**2/1024 > x
    return dict(endpoint_x=str(x), operator_norm_upper=str(rho),
                example_beta=1024, example_N=8192,
                scope='sufficient restricted loop bound, not a phase window')


def main():
    rng = np.random.default_rng(26142)
    footprints = [{0}, {1}, {0, 1}, {2}, {3}, {2, 3}]
    result = dict(status='finite_author_checks_passed', independent_review=False,
                  exclusion=exclusion_words(),
                  generic_source_cycle=cycle_fixture(rng.normal(size=(3, 3))*.025,
                        footprints, rng.normal(size=6)+1j*rng.normal(size=6), 32993),
                  six_cycle=cycle_fixture(rng.normal(size=(3, 3))*.025,
                        [{i} for i in range(6)], rng.normal(size=6)+1j*rng.normal(size=6),
                        99872, all_patterns=False, length=6),
                  cochain_footprints=physical_footprints(),
                  fixed_parameter_bound=endpoint())
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
