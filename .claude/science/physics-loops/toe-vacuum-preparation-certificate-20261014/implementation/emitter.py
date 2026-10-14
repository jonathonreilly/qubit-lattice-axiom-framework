#!/usr/bin/env python3
"""Literal chain-vacuum circuit and ordinary-edge routing, with scoped checks.

No quantum matrix identity is inferred from the routing label checker. The
independent circuit check and the complete analytic proofs have that scope.
"""
import argparse
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def geometry(m):
    assert isinstance(m, int) and m >= 1
    yz = [(0, 1), (1, 2), (2, 1), (1, 0)]
    signs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    connectors = [(i, *yz[i % 4]) for i in range(m + 1)]
    originals, auxiliaries, cells, parent_edges = [], [], [], []
    beta = (1, 0, 0)
    for i in range(m):
        sy, sz = signs[i % 4]
        eta, gamma = ((0, 0, sz), (0, sy, 0))
        if i % 2:
            eta, gamma = gamma, eta
        d = connectors[i]
        p = add(d, eta)
        a, b = add(d, beta), add(add(d, eta), beta)
        ap, bp = add(d, gamma), add(add(d, eta), gamma)
        z = connectors[i + 1]
        assert z == add(add(add(d, beta), eta), gamma)
        originals.append(p)
        auxiliaries.extend([a, b, ap, bp])
        cells.append({'i': i, 'd': d, 'p': p, 'z': z,
                      'a': a, 'b': b, 'ap': ap, 'bp': bp})
        parent_edges.extend([(d, a), (d, ap), (z, b), (z, bp),
                             (p, b), (p, bp), (a, b), (ap, bp)])
    originals += connectors
    sites = list(itertools.product(range(-1, m + 1), range(3), range(3)))
    pointer, borrowed = (-1, 0, 0), (-1, 0, 1)
    assert len(set(originals)) == 2*m + 1
    assert len(set(auxiliaries)) == 4*m
    assert not set(originals) & set(auxiliaries)
    assert len(sites) == 9*(m+2)
    assert set(originals + auxiliaries + [pointer, borrowed]) <= set(sites)
    assert not {pointer, borrowed} & set(originals + auxiliaries)
    assert len({tuple(sorted(e)) for e in parent_edges}) == 8*m
    assert all(distance(*e) == 1 for e in parent_edges)
    return sites, auxiliaries, pointer, borrowed, cells


def distance(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))


def ladder(controls, target, workspace):
    m = len(controls)
    if m == 1:
        return [('CX', controls[0], target)]
    if m == 2:
        return [('T', controls[0], controls[1], target)]
    workspace = workspace[:m-2]
    assert len(workspace) == m-2
    assert len(set(controls + [target] + workspace)) == 2*m-1
    gs = [('T', controls[0], controls[1], workspace[0])]
    for j in range(1, m-2):
        gs.append(('T', controls[j+1], workspace[j-1], workspace[j]))
    gs.append(('T', controls[-1], workspace[-1], target))
    first = gs[:-1] + gs[-1:] + gs[-2::-1]
    second = gs[1:-1] + gs[-1:] + gs[-2:0:-1]
    word = first + second
    assert len(word) == 4*(m-2)
    return word


def vacuum_word(auxiliaries, pointer, borrowed):
    n = len(auxiliaries)
    assert n >= 4 and n % 4 == 0
    size_s = 2 if n == 4 else (n+2)//2
    s, t = auxiliaries[:size_s], auxiliaries[size_s:]
    a = ladder(s, borrowed, t + [pointer])
    b = ladder(t + [borrowed], pointer, s)
    middle = a + b + a + b
    count = 10 if n == 4 else 8*(n-3)
    assert len(middle) == count and all(g[0] == 'T' for g in middle)
    xs = [('X', c) for c in auxiliaries]
    return xs + middle + xs, count


def decompose(word):
    result = []
    for gate in word:
        if gate[0] != 'T':
            result.append(gate)
            continue
        _, a, b, t = gate
        result.extend([('CV', b, t), ('CX', a, b), ('CVdg', b, t),
                       ('CX', a, b), ('CV', a, t)])
    return result


def manhattan(a, b):
    pos = list(a)
    path = [tuple(pos)]
    for axis in range(3):
        step = 1 if b[axis] > pos[axis] else -1
        while pos[axis] != b[axis]:
            pos[axis] += step
            path.append(tuple(pos))
    assert path[-1] == b and len(set(path)) == len(path)
    return path


def route(gate):
    if gate[0] == 'X':
        return [gate]
    kind, a, b = gate
    path = manhattan(a, b)
    swaps = [('SWAP', path[i], path[i+1]) for i in range(len(path)-2)]
    return swaps + [(kind, path[-2], path[-1])] + swaps[::-1]


def check_route(logical, emitted, sites):
    labels = {site: site for site in sites}
    non_swaps = []
    for gate in emitted:
        kind, *support = gate
        if not set(support) <= set(sites):
            raise AssertionError('outside physical box')
        if len(support) == 2 and distance(*support) != 1:
            raise AssertionError('non-neighbor primitive')
        if kind == 'SWAP':
            a, b = support
            labels[a], labels[b] = labels[b], labels[a]
        else:
            non_swaps.append((kind, *(labels[x] for x in support)))
    if non_swaps != [logical]:
        raise AssertionError('wrong operation or operand order at logical factors')
    if any(labels[x] != x for x in sites):
        raise AssertionError('unreturned transit permutation')


def Boolean_apply(word, bits):
    out = dict(bits)
    for gate in word:
        kind, *args = gate
        if kind == 'X':
            out[args[0]] ^= 1
        elif kind == 'CX':
            out[args[1]] ^= out[args[0]]
        elif kind == 'T':
            out[args[2]] ^= out[args[0]] & out[args[1]]
        else:
            raise ValueError(kind)
    return out


def check_all_basis(word, auxiliaries, pointer, borrowed):
    # Oracle directly evaluates vacuum and identity on every other factor.
    factors = auxiliaries + [pointer, borrowed]
    for values in itertools.product((0, 1), repeat=len(factors)):
        initial = dict(zip(factors, values))
        expected = dict(initial)
        expected[pointer] ^= int(not any(initial[x] for x in auxiliaries))
        assert Boolean_apply(word, initial) == expected
    return 2**len(factors)


def dump(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    results = []
    for m in (1, 2, 3, 8):
        sites, aux, pointer, borrowed, cells = geometry(m)
        logical, toffolis = vacuum_word(aux, pointer, borrowed)
        two_local = decompose(logical)
        assert len(two_local) == 8*m + 5*toffolis
        emitted = []
        offsets = []
        for gate in two_local:
            routed = route(gate)
            check_route(gate, routed, sites)
            offsets.append([len(emitted), len(emitted)+len(routed)])
            emitted.extend(routed)
        limit = 8*m + 5*toffolis*(2*m+9)
        assert len(emitted) <= limit
        checked_basis = check_all_basis(logical, aux, pointer, borrowed) if m <= 3 else 0
        word = {'M': m, 'sites': sites, 'cells': cells, 'auxiliaries': aux,
                'pointer': pointer, 'borrowed': borrowed, 'logical': logical,
                'two_local': two_local, 'physical': emitted, 'route_offsets': offsets}
        pin = dump(args.out/f'word_M{m}.json', word)
        results.append({'M': m, 'sites': len(sites), 'toffolis': toffolis,
                        'one_and_two_qubit_logical_primitives': len(two_local),
                        'ordinary_neighbor_and_one_qubit_primitives': len(emitted),
                        'analytic_upper_bound': limit,
                        'physical_gate_kinds': dict(Counter(g[0] for g in emitted)),
                        'basis_columns_checked_on_phase_free_logical_word': checked_basis,
                        'route_blocks_checked': len(offsets), 'word': pin})
    sites, aux, pointer, borrowed, _ = geometry(1)
    witness = ('CV', aux[0], pointer)
    good = route(witness)
    check_route(witness, good, sites)
    assert good[0][0] == good[-1][0] == 'SWAP'
    controls = []
    for name, broken in [('omit_first_swap', good[1:]),
                         ('omit_last_return_swap', good[:-1]),
                         ('reverse_control_target',
                          [(g[0],g[2],g[1]) if g[0]=='CV' else g for g in good])]:
        try:
            check_route(witness, broken, sites)
        except AssertionError as exc:
            controls.append({'name': name, 'rejected': True, 'reason': str(exc),
                             'logical': witness, 'actual_mutated_word': broken})
        else:
            raise AssertionError('mutation was not rejected: '+name)
    # Dropping the final B block reintroduces dirty-bit dependence or a wrong flag.
    logical, _ = vacuum_word(aux, pointer, borrowed)
    bad_word = logical[:-(4+4)] + logical[-4:]
    mismatch = None
    for vals in itertools.product((0,1), repeat=6):
        bits = dict(zip(aux+[pointer,borrowed], vals))
        if Boolean_apply(bad_word, bits) != Boolean_apply(logical, bits):
            mismatch = {'input': vals, 'correct': list(Boolean_apply(logical,bits).values()),
                        'broken': list(Boolean_apply(bad_word,bits).values())}
            break
    assert mismatch is not None
    controls.append({'name': 'omit_final_four_toffoli_B_block', 'rejected': True,
                     'witness': mismatch, 'actual_mutated_word': bad_word})
    report = {'status': 'scoped exact finite emitter/routing checks completed',
              'scope': 'Basis permutations and routing labels; not a fresh full quantum matrix check, native record, arbitrary noise model, all-M proof by testing, or retained audit.',
              'results': results, 'mutation_controls': controls}
    pin = dump(args.out/'RESULT.json', report)
    print(json.dumps({'result': pin, 'counts': results,
                      'mutations_rejected': len(controls)}, indent=2))


if __name__ == '__main__':
    main()
