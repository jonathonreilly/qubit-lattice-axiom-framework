#!/usr/bin/env python3
"""One M=5 integer/Fraction geometry and complete monomial-word fixture.
No parent code or amplitudes are loaded; no active-background simulation.
"""
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys

M = 5
K = (4 * M).bit_length()  # ceil(log2(4M+1)), since 4M>=1
Y = (0, 1, 2, 1)
Z = (1, 2, 1, 0)
SIGNS = ((1, 1), (1, -1), (-1, -1), (-1, 1))


def add(*vectors):
    return tuple(sum(v[c] for v in vectors) for c in range(3))


def connector(i):
    return (i, Y[i % 4], Z[i % 4])


def cell(i):
    sy, sz = SIGNS[i % 4]
    eta, gamma = ((0, 0, sz), (0, sy, 0)) if i % 2 == 0 else ((0, sy, 0), (0, 0, sz))
    d, beta = connector(i), (1, 0, 0)
    assert connector(i + 1) == add(d, beta, eta, gamma)
    return {'i': i, 'd': d, 'p': add(d, eta), 'z': connector(i + 1),
            'a': add(d, beta), 'b': add(d, eta, beta),
            'ap': add(d, gamma), 'bp': add(d, eta, gamma)}


def pointer(j):
    return (M + 1 + j, 3, 3)


def route(j, u):
    """Every vertex of the stated four-segment path, with junctions once."""
    x, y, z = u
    p = [pointer(j), (M + 1 + j, 4, 3)]
    p.extend((xx, 4, 3) for xx in range(M + j, x - 1, -1))
    p.extend((x, yy, 3) for yy in range(3, y - 1, -1))
    p.extend((x, y, zz) for zz in range(2, z - 1, -1))
    return p


def edge(a, b):
    return sum(abs(x-y) for x, y in zip(a, b)) == 1


def dump(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')


def emit_jsonl(path, word):
    path.write_text(''.join(json.dumps(x, sort_keys=True) + '\n' for x in word))


def token_check(word, box, require_expected):
    """Permutation/phase-label structure, valid for all basis bit assignments."""
    labels = {v: v for v in box}
    phase_mismatches = []
    return_mismatches = []
    for index, op in enumerate(word):
        if op['op'] == 'SWAP':
            a, b = map(tuple, op['sites'])
            assert edge(a, b)
            labels[a], labels[b] = labels[b], labels[a]
        elif op['op'] == 'PHASE':
            a, b = map(tuple, op['sites'])
            expected = (tuple(op['logical_pointer']), tuple(op['logical_auxiliary']))
            actual = (labels[a], labels[b])
            if actual != expected:
                phase_mismatches.append({'index': index, 'block': op['block'],
                                         'expected': expected, 'actual': actual})
        if op.get('block_end'):
            wrong = [(v, labels[v]) for v in box if labels[v] != v]
            if wrong:
                return_mismatches.append({'index': index, 'block': op['block'], 'mismatches': wrong})
    final = [(v, labels[v]) for v in box if labels[v] != v]
    if require_expected:
        assert not phase_mismatches
        assert not return_mismatches
        assert not final
    return {'phase_label_mismatches': phase_mismatches,
            'block_return_mismatches': return_mismatches,
            'final_token_mismatches': final}


def main():
    out = Path(sys.argv[1]).resolve()
    out.mkdir(parents=True, exist_ok=False)
    assert M == 5 and K == 5
    box = [(x, y, z) for x in range(M + K + 1) for y in range(5) for z in range(4)]
    old_box = {(x, y, z) for x in range(M + 1) for y in range(3) for z in range(3)}
    box_set = set(box)
    cells = [cell(i) for i in range(M)]
    auxiliaries = [(i, name, tuple(c[name])) for i, c in enumerate(cells) for name in ('a', 'b', 'ap', 'bp')]
    aux_set = {u for _, _, u in auxiliaries}
    original = {connector(i) for i in range(M + 1)} | {tuple(c['p']) for c in cells}
    pointers = {pointer(j) for j in range(K)}
    assert len(aux_set) == 4 * M and len(original) == 2 * M + 1
    assert not aux_set & original
    assert aux_set | original <= old_box
    assert pointers <= box_set - old_box and len(pointers) == K
    # Direct old-edge inventory is independent of the new routing inventory.
    old_edges = []
    for c in cells:
        for a, b in (('d','a'),('d','ap'),('z','b'),('z','bp'),('p','b'),('p','bp'),('a','b'),('ap','bp')):
            aa, bb = tuple(c[a]), tuple(c[b])
            assert edge(aa, bb)
            old_edges.append(tuple(sorted((aa, bb))))
    assert len(set(old_edges)) == 8 * M
    word = [{'op': 'PREP_PLUS', 'site': pointer(j), 'rotation_y_radians_over_pi': [1,4]} for j in range(K)]
    paths = []
    for j in range(K):
        for i, name, u in auxiliaries:
            p = route(j, u)
            length = len(p) - 1
            block = len(paths)
            assert p[0] == pointer(j) and p[-1] == u
            assert len(set(p)) == len(p) and set(p) <= box_set
            assert all(edge(a,b) for a,b in zip(p,p[1:]))
            assert not (set(p) & (pointers - {pointer(j)}))
            assert length == M + j + 9 - sum(u)
            paths.append({'block': block, 'j': j, 'cell': i, 'role': name,
                          'length': length, 'vertices': p})
            for e in range(length - 1):
                word.append({'op': 'SWAP', 'sites': [p[e],p[e+1]], 'block': block,
                             'stage': 'forward', 'edge_index': e})
            frac = Fraction(1, 2**j)
            word.append({'op': 'PHASE', 'sites': [p[-2],p[-1]], 'block': block,
                         'logical_pointer': pointer(j), 'logical_auxiliary': u,
                         'theta_over_pi': [frac.numerator,frac.denominator],
                         'error_symbol': 'e_%d_%d_%s' % (j,i,name)})
            for e in reversed(range(length - 1)):
                word.append({'op': 'SWAP', 'sites': [p[e],p[e+1]], 'block': block,
                             'stage': 'reverse', 'edge_index': e, 'block_end': e == 0})
    word.extend({'op': 'READ_X', 'site': pointer(j), 'outcome_bit': j} for j in range(K))
    counts = Counter(op['op'] for op in word)
    chi = int(M % 4 in (2,3))
    coordinate_sum = sum(sum(u) for u in aux_set)
    sum_lengths = sum(p['length'] for p in paths)
    expected_lengths = K * (2*M*M + 28*M - 4*chi) + 2*M*K*(K-1)
    expected_swaps = 4*K*(M*M + M*K + 11*M - 2*chi)
    assert coordinate_sum == 2*M*M + 8*M + 4*chi
    assert sum_lengths == expected_lengths
    assert max(p['length'] for p in paths) == M + K + 6
    assert counts == {'PREP_PLUS': K, 'SWAP': expected_swaps, 'PHASE': 4*M*K, 'READ_X': K}
    correct = token_check(word, box, True)
    removed = [i for i, op in enumerate(word) if op['op'] == 'SWAP' and op['block'] == 0 and op['stage'] == 'reverse' and op['edge_index'] == 0]
    assert len(removed) == 1
    bad_word = [op for i, op in enumerate(word) if i != removed[0]]
    bad = token_check(bad_word, box, False)
    first_transit = tuple(paths[0]['vertices'][1])
    assert sorted(bad['final_token_mismatches']) == sorted([(pointer(0),first_transit),(first_transit,pointer(0))])
    assert len(bad['phase_label_mismatches']) == 4*M - 1
    use = Counter()
    for op in word:
        if op['op'] in ('SWAP','PHASE'):
            use.update(map(tuple,op['sites']))
        elif op['op'] == 'PREP_PLUS':
            use[tuple(op['site'])] += 1
    assert max(use.values()) <= 4*4*M*K + 1
    phase_action = sum((Fraction(*op['theta_over_pi']) for op in word if op['op']=='PHASE'),Fraction(0))
    nominal_action = counts['SWAP'] + phase_action + Fraction(K,4)
    assert phase_action == 8*M*(1-Fraction(1,2**K))
    assert nominal_action == 2140
    inventory = {'M':M,'k':K,'box_dimensions':[M+K+1,5,4],'box_sites':len(box),
                 'old_box_sites':len(old_box),'new_sites':len(box_set-old_box),
                 'new_clean_pointers':K,'new_dirty_transit_or_spectators':len(box_set-old_box)-K,
                 'old_required_originals':len(original),'old_auxiliary_sites':len(aux_set),
                 'old_selected_edges':len(set(old_edges)),'cells':cells,'pointers':sorted(pointers)}
    dump(out/'INVENTORY.json',inventory)
    dump(out/'PATHS.json',paths)
    emit_jsonl(out/'WORD.jsonl',word)
    emit_jsonl(out/'DELETED_RETURN_WORD.jsonl',bad_word)
    dump(out/'CORRECT_LABEL_RESULT.json',correct)
    dump(out/'DELETED_RETURN_RESULT.json',{'removed_index':removed[0],'removed_gate':word[removed[0]],
         'actual_result':bad,'analytic_Bell_transit_false_negative_probability':[1,2],
         'witness_scope':'All B vacuum, pointer plus, first transit Bell-entangled to R; phases are identity, so final exchanged Bell half has random X. No amplitude simulation.'})
    dump(out/'SITE_USES.json',[{'site':v,'gate_incidence_count':use[v]} for v in sorted(use)])
    summary={'M':M,'k':K,'coordinate_sum':coordinate_sum,'sum_path_lengths':sum_lengths,
             'max_path_length':max(p['length'] for p in paths),'counts':dict(counts),
             'coherent_gate_count':counts['SWAP']+counts['PHASE']+counts['PREP_PLUS'],
             'total_emitted_records':len(word),'phase_action_over_pi':[phase_action.numerator,phase_action.denominator],
             'nominal_coherent_action_over_pi':[nominal_action.numerator,nominal_action.denominator],
             'maximum_site_gate_incidence':max(use.values()),'correct_phase_label_mismatches':len(correct['phase_label_mismatches']),
             'correct_return_mismatches':len(correct['final_token_mismatches']),
             'deleted_reverse_final_mismatches':bad['final_token_mismatches'],
             'deleted_reverse_phase_label_mismatch_count':len(bad['phase_label_mismatches']),
             'scope':'One exact integer/Fraction monomial-word control; not an all-M proof, amplitude simulation or active-K dynamics test.'}
    dump(out/'SUMMARY.json',summary)
    print(json.dumps(summary,indent=2,sort_keys=True))
    print('ARTIFACT_IDENTITIES')
    for p in sorted(out.iterdir()):
        raw=p.read_bytes()
        print(json.dumps({'name':p.name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()},sort_keys=True))


if __name__ == '__main__':
    main()
