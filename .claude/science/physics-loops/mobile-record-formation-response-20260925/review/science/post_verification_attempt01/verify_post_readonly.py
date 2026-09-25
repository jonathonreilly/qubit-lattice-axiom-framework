#!/usr/bin/env python3
"""Released root39 correspondence: read, hash, parse, and print only.

No evidence program is imported or executed, no subprocess is spawned, and
no file is written. Stored scientific rows are checked by elementary exact
arithmetic and direct finite charge/incidence counting.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
import ast
import datetime
import hashlib
import json

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'formation-response-sum-personal'
SNAPSHOT = HERE / 'post_sources' / 'author39'
PRE_SEAL_HASH = 'd65cdc1e27cd6757c9437f62cec7c45bfa7a3c850da4c5f2f2fe510983c00dad'
AUTHOR_SEAL_HASH = 'ffd9f68e551afb30573d4cf727f8f5c58b4b32d6feb2c128fd660ecd74416486'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def members(root, rows):
    for row in rows:
        path = root / row['path']
        assert path.stat().st_size == row['bytes']
        assert digest(path) == row['sha256'], str(path)
    return len(rows)


def quadratic(flows, key):
    values = {row['winding_multiple']: Fraction(row[key]) for row in flows}
    assert set(values) == {-2, 0, 3}
    c = values[0]
    a = ((values[3]-c)/3 + (values[-2]-c)/2)/5
    b = (values[3]-c)/3-3*a
    assert all(a*t*t+b*t+c == v for t, v in values.items())
    assert all(x.denominator == 1 for x in (a, b, c))
    return tuple(int(x) for x in (a, b, c))


def verify():
    assert digest(HERE / 'PRE_SEAL.json') == PRE_SEAL_HASH
    pre_count = members(HERE, read(HERE / 'PRE_SEAL.json')['members'])
    assert digest(AUTHOR / 'AUTHOR_SEAL.json') == AUTHOR_SEAL_HASH
    assert digest(SNAPSHOT / 'AUTHOR_SEAL.json') == AUTHOR_SEAL_HASH
    sealed = read(SNAPSHOT / 'AUTHOR_SEAL.json')
    author_count = members(AUTHOR, sealed['members'])
    assert members(SNAPSHOT, sealed['members']) == author_count
    pins = read(HERE / 'POST_SOURCE_PINS_INITIAL.json')
    for row in pins['author_sources']:
        assert digest(Path(row['origin'])) == row['sha256']
        assert digest(HERE / row['snapshot']) == row['sha256']
    parent_rows = read(HERE / 'SOURCE_PINS_INITIAL.json')['sources'][:3]
    allowed_parents = {}
    for row in parent_rows:
        assert digest(Path(row['origin'])) == row['sha256']
        assert digest(HERE / row['snapshot']) == row['sha256']
        allowed_parents[row['origin']] = row['sha256']
    compared_pins, not_followed = [], []
    for row in read(SNAPSHOT / 'SOURCE_PINS.json')['sources']:
        if row['path'] in allowed_parents:
            assert row['sha256'] == allowed_parents[row['path']]
            compared_pins.append(row['path'])
        else:
            not_followed.append(row['path'])
    assert len(compared_pins) == 3 and len(not_followed) == 3

    source = SNAPSHOT / 'response_sum_controls.py'
    tree = ast.parse(source.read_text())
    functions = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
    receipt = read(SNAPSHOT / 'EXECUTION_ATTEMPT01.json')
    result = read(SNAPSHOT / 'RESPONSE_SUM_RESULTS.json')
    assert receipt['source_sha256'] == result['source_sha256'] == digest(source)
    assert receipt['exit_code'] == 0 and receipt['stderr_bytes'] == 0
    assert (SNAPSHOT / 'CONTROL_ATTEMPT01.stderr').read_bytes() == b''
    assert (SNAPSHOT / 'CONTROL_ATTEMPT01.stdout').read_bytes() == (
        SNAPSHOT / 'RESPONSE_SUM_RESULTS.json').read_bytes()
    assert receipt['stdout_bytes'] == (SNAPSHOT / 'CONTROL_ATTEMPT01.stdout').stat().st_size
    assert result['all_assertions_passed']
    assert len(result['geometry']) == 3 and len(result['rows']) == 75
    geo = {g['side']: g for g in result['geometry']}
    for length, g in geo.items():
        n = length**3//2
        z, incidence = (3, 2) if length == 2 else (6, 4)
        assert (g['vertices'], g['A_sites'], g['edges']) == (length**3, n, n*z)
        assert (g['degree'], g['edge_squared_incidence']) == (z, incidence)
        assert 4*g['plaquettes'] == incidence*g['edges']
        assert g['response_coefficient_in_K'] == 2*incidence*z
        assert g['per_birth_decrement_in_K'] == 4*incidence*z
        assert g['charge_words'] == (65 if length == 2 else 5)
    tsv_lines = (HERE / 'POST_AUTHOR_ROWS.tsv').read_text().splitlines()
    assert len(tsv_lines) == 76
    summaries = []
    by_side = {}
    for row, tsv in zip(result['rows'], tsv_lines[1:]):
        length = row['side']; g = geo[length]
        coords = tuple(product(range(length), repeat=3))
        index = {x: i for i, x in enumerate(coords)}
        A = tuple(i for i, x in enumerate(coords) if sum(x) % 2 == 0)
        B = tuple(i for i, x in enumerate(coords) if sum(x) % 2)
        q = row['charges']; n = len(A)
        assert len(q) == length**3 and sum(q) == n
        assert all(q[a] in (-1, 1) for a in A)
        assert all(q[b] in (-1, 0, 1) for b in B)
        occupied = sum(q[b] != 0 for b in B)
        assert occupied == row['B_occupied']
        response = 2*g['degree']*g['edge_squared_incidence']*(n-occupied)
        assert response == row['exact_response_in_K']
        paths = 0
        for a in A:
            neighbours = set()
            for axis in range(3):
                for sign in (-1, 1):
                    coordinate = list(coords[a])
                    coordinate[axis] = (coordinate[axis]+sign) % length
                    neighbours.add(index[tuple(coordinate)])
            empty = sum(q[b] == 0 for b in neighbours)
            paths += 2*empty*(empty-1)
        assert paths == row['primitive_paths'] == row['resolved_loss_diagonal'] == row['coherent_loss_diagonal']
        assert row['second_differences'] == 3*g['plaquettes']
        if length == 2:
            loop_B = (index[(1, 0, 0)], index[(0, 1, 0)])
            loop_length = 4
        else:
            loop_B = tuple(index[(x, 0, 0)] for x in range(1, length, 2))
            loop_length = length
        aD, bD, cD = quadratic(row['flows'], 'D')
        aE, bE, cE = quadratic(row['flows'], 'electric_squared_norm')
        assert aD == 2*sum(q[b] == 0 for b in loop_B)
        assert aE == loop_length
        assert bE % 2 == 0
        assert all(f['D'] >= 0 and f['electric_squared_norm'] >= 0 for f in row['flows'])
        fields = tsv.split('\t')
        encoded = ''.join({-1: '-', 0: '0', 1: '+'}[x] for x in q)
        assert fields[2] == encoded
        integer_fields = [row[k] for k in ('side', 'word_index', 'B_occupied',
                                           'exact_response_in_K', 'second_differences',
                                           'primitive_paths', 'resolved_loss_diagonal',
                                           'coherent_loss_diagonal')]
        assert list(map(int, fields[:2]+fields[3:9])) == integer_fields
        assert json.loads(fields[9]) == [[f['winding_multiple'], f['D'], f['electric_squared_norm']]
                                        for f in row['flows']]
        by_side.setdefault(length, []).append(tuple(q))
        summaries.append({'L': length, 'word': row['word_index'], 'response': response,
                          'paths': paths, 'D_polynomial': [aD, bD, cD],
                          'E2_polynomial': [aE, bE, cE]})
    # Complete cube charge enumeration, using only the stored coordinate order.
    cube_coords = tuple(product(range(2), repeat=3))
    cube_A = [i for i, x in enumerate(cube_coords) if sum(x) % 2 == 0]
    expected = {q for q in product((-1, 0, 1), repeat=8)
                if sum(q) == 4 and all(q[a] != 0 for a in cube_A)}
    assert len(expected) == 65 and set(by_side[2]) == expected
    assert len(set(by_side[2])) == len(by_side[2])
    assert sum(row['second_differences'] for row in result['rows']) == result['second_difference_checks'] == 13770
    assert sum(row['primitive_paths'] for row in result['rows']) == result['primitive_paths_checked'] == 27344
    review = read(SNAPSHOT / 'ROOT_REVIEW.json')
    assert review['exact_second_difference_checks'] == result['second_difference_checks']
    assert review['primitive_paths_checked'] == result['primitive_paths_checked']
    own = read(HERE / 'control_attempt02/RESPONSE_PRIMITIVE_RESULTS.json')
    own_geo = {row['L']: row for row in own['geometry_rows']}
    for length in (4, 6):
        assert geo[length]['plaquettes'] == own_geo[length]['plaquettes']
        assert geo[length]['response_coefficient_in_K'] == own_geo[length]['response_per_vacancy_at_K1']
    assert own_geo[4]['response_per_vacancy_if_all_four_cycles_summed'] == 60
    return {
        'verified_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope': 'Released-source correspondence and exact stored-row arithmetic; no author program execution, new simulation or applied audit verdict.',
        'PRE_seal_sha256': PRE_SEAL_HASH, 'PRE_members_unchanged': pre_count,
        'author_seal_sha256': AUTHOR_SEAL_HASH,
        'author_members_live_and_snapshot_verified': author_count,
        'main_parent_origins_verified': len(compared_pins),
        'prior_provenance_references_not_followed': not_followed,
        'author_functions_read_and_AST_parsed': functions,
        'author_source_sha256': digest(source),
        'author_result_and_stdout_sha256': digest(SNAPSHOT / 'RESPONSE_SUM_RESULTS.json'),
        'author_execution_seconds': receipt['seconds'],
        'author_internal_elapsed_seconds': result['elapsed_seconds'],
        'author_exit_code': receipt['exit_code'], 'author_stderr_bytes': 0,
        'geometry_rows': result['geometry'],
        'all_scientific_rows_reviewed': 75,
        'all_three_flow_rows_per_charge_checked': 225,
        'cube_charge_words_completely_enumerated': 65,
        'second_difference_checks_stored': 13770,
        'primitive_paths_stored_and_counted': 27344,
        'stored_row_arithmetic': summaries,
        'lossless_payload_review_tsv_sha256': digest(HERE / 'POST_AUTHOR_ROWS.tsv'),
        'own_PRE_elementary_geometry_agrees': True,
        'PRE_only_L4_all_four_cycle_coefficient_retained': 60,
        'author_code_imported_or_executed': False,
        'file_writes_or_processes_spawned_by_verifier': False,
        'all_checks_passed': True,
    }


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2, allow_nan=False))
