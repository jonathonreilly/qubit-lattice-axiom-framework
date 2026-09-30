#!/usr/bin/env python3
"""Exact local translation and original-instrument checks for the cubic note.

The analytic Bloch/volume proofs are in the note. This runner does not enumerate
their complete internal quotient or infer dispersion from a few path entries.
"""
from collections import Counter
import json
import cubic_one_pair_primitives_2026_09_26 as p
import cubic_one_pair_incidence_2026_09_26 as independent

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'docs/CUBIC_ONE_PAIR_BAND_ACTUAL_FIRST_BIRTH_LIMIT_AND_ELECTRIC_EXCITATION_BOUNDED_THEOREM_NOTE_2026-09-26.md',
    'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'scripts/cubic_one_pair_primitives_2026_09_26.py',
    'scripts/cubic_one_pair_incidence_2026_09_26.py',
)

FIXTURE = {'translation_path_states': [[[[[0, 0, 0], -1], [[0, 1, 0], 1], [[1, 0, 0], 1]],
                              [[[[0, 0, 0], [0, 1, 0]], -1], [[[0, 0, 0], [1, 0, 0]], -1]]],
                             [[[[0, 0, 0], -1], [[0, 0, 1], 1], [[1, 1, 1], 1]],
                              [[[[0, 0, 0], [0, 1, 0]], -1],
                               [[[0, 0, 0], [1, 0, 0]], -1],
                               [[[0, 1, 1], [0, 1, 0]], 1],
                               [[[0, 1, 1], [1, 1, 1]], -1],
                               [[[1, 0, 1], [0, 0, 1]], -1],
                               [[[1, 0, 1], [1, 0, 0]], 1]]],
                             [[[[0, 0, 1], 1], [[1, 1, 0], -1], [[1, 1, 1], 1]],
                              [[[[0, 1, 1], [0, 1, 0]], 1],
                               [[[0, 1, 1], [1, 1, 1]], -1],
                               [[[1, 0, 1], [0, 0, 1]], -1],
                               [[[1, 0, 1], [1, 0, 0]], 1],
                               [[[1, 1, 0], [0, 1, 0]], -1],
                               [[[1, 1, 0], [1, 0, 0]], -1]]],
                             [[[[0, 1, 0], 1], [[1, 0, 0], 1], [[1, 1, 0], -1]],
                              [[[[1, 1, 0], [0, 1, 0]], -1], [[[1, 1, 0], [1, 0, 0]], -1]]],
                             [[[[0, 1, 0], 1], [[1, 1, 1], -1]],
                              [[[[1, 1, 0], [0, 1, 0]], -1], [[[1, 1, 0], [1, 1, 1]], 1]]],
                             [[[[0, 1, 0], 1], [[1, 1, 0], -1], [[2, 1, 0], 1]],
                              [[[[1, 1, 0], [0, 1, 0]], -1], [[[1, 1, 0], [2, 1, 0]], -1]]],
                             [[[[1, 1, 1], -1], [[2, 1, 0], 1]],
                              [[[[1, 1, 0], [1, 1, 1]], 1], [[[1, 1, 0], [2, 1, 0]], -1]]],
                             [[[[1, 1, 0], -1], [[1, 2, 0], 1], [[2, 1, 0], 1]],
                              [[[[1, 1, 0], [1, 2, 0]], -1], [[[1, 1, 0], [2, 1, 0]], -1]]]],
 'claimed_translation': [1, 1, 0],
 'additional_matrix_element_states': [[[[[0, 0, 0], -1], [[0, 1, 0], 1], [[1, 0, 0], 1]],
                                       [[[[0, 0, 0], [0, 1, 0]], -1], [[[0, 0, 0], [1, 0, 0]], -1]]],
                                      [[[[0, 0, 0], -1], [[0, 1, 0], 1], [[1, 2, 0], 1]],
                                       [[[[0, 0, 0], [0, 1, 0]], -1],
                                        [[[0, 0, 0], [1, 0, 0]], -1],
                                        [[[1, 1, 0], [1, 0, 0]], 1],
                                        [[[1, 1, 0], [1, 2, 0]], -1]]]],
 'birth_input': [[[[0, 0, 0], -1], [[0, 1, 0], 1], [[1, 2, 0], 1]],
                 [[[[0, 0, 0], [0, 1, 0]], -1],
                  [[[0, 0, 0], [1, 0, 0]], -1],
                  [[[1, 1, 0], [1, 0, 0]], 1],
                  [[[1, 1, 0], [1, 2, 0]], -1]]],
 'birth_mark': [[1, 1, 0], [2, 1, 0], -1],
 'outward_destination': [1, 1, 1],
 'state_format': '[q_deviations, nonzero_E], positions integer triples, A even coordinate sum; default '
                 'q_A=+1,q_B=0; E oriented A to B. No expected coefficients or costs supplied.'}


def word(raw):
    return p.pack({tuple(v): q for v, q in raw[0]},
                  {(tuple(a), tuple(b)): e for (a, b), e in raw[1]})


def histogram(outputs, cost):
    out = Counter()
    for s, amplitude in outputs.items():
        out[cost(s)] += amplitude * amplitude
    return dict(sorted(out.items()))


def calculate():
    path = [word(s) for s in FIXTURE['translation_path_states']]
    extra = [word(s) for s in FIXTURE['additional_matrix_element_states']]
    s = word(FIXTURE['birth_input'])
    a, b, sigma = FIXTURE['birth_mark']
    a, b = tuple(a), tuple(b)
    dest = tuple(FIXTURE['outward_destination'])
    shift = tuple(FIXTURE['claimed_translation'])
    assert all(p.gauss(v) and p.cost(v) == 0 for v in path + extra + [s])
    assert p.translate(path[0], shift) == path[-1]
    links = list(zip(path, path[1:])) + [tuple(extra)]
    primary_entries = []
    for x, y in links:
        h, witnesses = p.projected_offdiag(x, y)
        primary_entries.append(h[y])
        aa, cc, *moves = witnesses[y]
        intermediate = x
        for operation, center, move in zip(
                (p.outgoing, p.outgoing, p.incoming, p.incoming),
                (aa, cc, cc, aa), moves):
            intermediate = next(z for z, step in operation(intermediate, center) if step == move)
            assert p.gauss(intermediate)
        assert intermediate == y
    expected = [-2, -4, -2, -186, -186, -186, -186, -186]
    assert primary_entries == expected

    resolved = p.jump(s, a, b, sigma)
    coherent = Counter()
    for sign in (-1, 1):
        coherent.update(p.jump(s, a, b, sign))
    assert all(p.gauss(v) for v in coherent)
    resolved_hist = histogram(resolved, p.cost)
    coherent_hist = histogram(coherent, p.cost)
    assert resolved_hist == {0: 1, 2: 2}
    assert coherent_hist == {0: 4, 2: 2}
    outgoing = next(z for z, move in p.outgoing(s, a) if move[1] == dest)
    target = p.born(outgoing, a, b, sigma)
    assert target in resolved and p.cost(target) == 2

    # Primary inverse: undo pair creation, then apply the full adjoint hop.
    q, e = p.unpack(target)
    q[a] = q[b] = 0
    e[a, b] -= sigma
    before_creation = p.pack(q, e)
    primary_preimages = Counter(v for v, _ in p.incoming(before_creation, a) if p.cost(v) == 0)
    first = p.jump(p.OMEGA, (0, 0, 0), (1, 0, 0), -1)
    assert len(first) == 5 and sum(v*v for v in first.values()) == 5
    assert all(p.gauss(v) and p.cost(v) == 0 for v in first)
    for sign in (-1, 1):
        output = p.jump(p.OMEGA, (0, 0, 0), (1, 0, 0), sign)
        assert len(output) == 5 and sum(v*v for v in output.values()) == 5
        assert all(p.gauss(v) and p.cost(v) == 0 for v in output)
    assert not (first.keys() & primary_preimages.keys()), 'No diagonal term is allowed in this fixture.'
    primary_matrix = {}
    for x in first:
        h, _ = p.projected_offdiag(x)
        for y in primary_preimages:
            primary_matrix[y, x] = h.get(y, 0)
    primary_amplitude = sum(first[x] * primary_preimages[y] * value
                            for (y, x), value in primary_matrix.items())
    assert primary_amplitude == -372

    # Independent simultaneous-output construction: full finite torus, no local
    # pair prefilter and no calls to primary hopping, birth, Gauss or cost code.
    torus = independent.Torus(8)
    decode = lambda x: independent.decode(x, 8)
    si = decode(FIXTURE['birth_input'])
    independent_resolved, routes = torus.fixed_birth(si, a, b, sigma)
    target_i = next(v for v in independent_resolved if dest in routes[v])
    assert target_i == decode(target)
    independent_coherent = Counter()
    for sign in (-1, 1):
        output, _ = torus.fixed_birth(si, a, b, sign)
        independent_coherent.update(output)
    assert independent_resolved == Counter({decode(v): n for v, n in resolved.items()})
    assert independent_coherent == Counter({decode(v): n for v, n in coherent.items()})
    cost_i = lambda v: torus.check(v)['D']
    assert histogram(independent_resolved, cost_i) == resolved_hist
    assert histogram(independent_coherent, cost_i) == coherent_hist

    # Independent inverse: final occupied destinations determine unique inputs.
    tq, te = map(dict, target_i)
    inverse_i = Counter()
    for d in torus.neighbors[a]:
        if d == b or tq.get(d, 0) == 0:
            continue
        old_charge = tq[d]
        iq, ie = dict(tq), dict(te)
        iq.update({a: old_charge, b: 0, d: 0})
        ie[a, d] = te.get((a, d), 0) + old_charge
        ie[a, b] = te.get((a, b), 0) - sigma
        predecessor = independent.key(iq, ie)
        if cost_i(predecessor) == 0:
            outs, _ = torus.fixed_birth(predecessor, a, b, sigma)
            inverse_i[predecessor] += outs[target_i]
    assert inverse_i == Counter({decode(v): n for v, n in primary_preimages.items()})
    first_i, _ = torus.fixed_birth(independent.key({}, {}), (0, 0, 0), (1, 0, 0), -1)
    assert first_i == Counter({decode(v): n for v, n in first.items()})
    assert len(inverse_i) == 3

    base_links = [(decode(x), decode(y)) for x, y in links]
    extension_links = [(x, y) for y in sorted(inverse_i) for x in sorted(first_i)]
    all_links = base_links + extension_links
    states_i = sorted({v for xy in all_links for v in xy})
    index = {v: i for i, v in enumerate(states_i)}
    state_checks = [torus.check(v) for v in states_i]
    for check in state_checks:
        assert not check['gauss_failures'] and not check['a_vacancies']
        assert check['D'] == 0 and check['records_over_background'] == 2
    for v in independent_coherent:
        check = torus.check(v)
        assert not check['gauss_failures'] and not check['a_vacancies']
        assert check['records_over_background'] == 4
    incidence = [0] * len(all_links)
    pair_counts = [0] * len(all_links)
    for aa, cc in torus.pairs:
        outs = [torus.two_hole(v, aa, cc)[0] for v in states_i]
        for i, (x, y) in enumerate(all_links):
            x_out, y_out = outs[index[x]], outs[index[y]]
            value = sum(x_out[z] * y_out[z] for z in x_out.keys() & y_out.keys())
            incidence[i] += value
            pair_counts[i] += bool(value)
    matrix_i = [-2 * value for value in incidence]
    assert matrix_i[:8] == primary_entries
    # Compare by words, because modulo reduction can reorder coordinates.
    primary_by_torus = {(decode(x), decode(y)): value
                        for (y, x), value in primary_matrix.items()}
    assert matrix_i[8:] == [primary_by_torus[x, y] for x, y in extension_links]
    amplitude_i = sum(first_i[x] * inverse_i[y] * value
                      for (x, y), value in zip(extension_links, matrix_i[8:]))
    assert amplitude_i == primary_amplitude == -372
    assert pair_counts[:8] == [1, 1, 1, 18, 18, 18, 18, 18]
    assert sorted(matrix_i[8:]) == [-186, -186] + [0] * 13

    # Vacuum subtraction and translation-lattice arithmetic used in the proof.
    overlap_counts = Counter(len(set(p.nb((0, 0, 0))) & set(p.nb(c)))
                             for c in p.partners((0, 0, 0)))
    assert overlap_counts == {1: 6, 2: 12}
    vacuum_scalar_per_A = -sum(n * (36 - shared) for shared, n in overlap_counts.items())
    assert vacuum_scalar_per_A == -618
    return {'scope': 'exact local coefficients and instruments, not a numerical band or full-law simulation',
            'translation': shift, 'path_matrix_entries': primary_entries[:7],
            'additional_entry': primary_entries[-1], 'vacuum_scalar_per_A': vacuum_scalar_per_A,
            'independent_torus_side': 8, 'all_pair_count': len(torus.pairs),
            'contributing_pairs_per_entry': pair_counts[:8],
            'resolved_D_raw_weights': resolved_hist, 'coherent_D_raw_weights': coherent_hist,
            'first_mark_norm_squared': sum(v*v for v in first.values()),
            'D0_second_mark_preimage_count': len(inverse_i),
            'extension_matrix_in_sorted_torus_order': [matrix_i[8+i*5:13+i*5] for i in range(3)],
            'complete_first_vector_coefficient': amplitude_i,
            'statewise_primitive_incidence_agreement': True}


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
    print('Verification complete: exact local coefficients and full original instrument outputs; analytic band and joint-limit proofs remain in the note.')
