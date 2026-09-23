"""Bounded post-PRE reconstruction; author code is neither imported nor run.

The complete-spin basis uses the independently frozen charge, Gauss and hop
rules. The post-exposure choice of matrix diagnostics matches the author's
controls; this runner is not represented as a second blind reconstruction.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
from functools import lru_cache
from itertools import combinations, product
import hashlib
import json
import numpy as np
import scipy.sparse as sparse
import cube_controls as independent

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'cube_unprepared_author'
SPECTRAL = HERE.parent / 'cube_point_spectrum_independent'
PRE_HASH = '5d7d37fcc06fb75a647a1b5e2fe40b49ed6467c2185f5218da78b2fa2f8ca715'
AUTHOR_HASH = 'ed066b95b18992f86718fe960ed6624c163854d142d0f90a742a4c85377159f4'
SPECTRAL_HASH = 'f2df1efd5a7c7a63fb5200c0becb48278f79e448000afddcc8dc2bc48785111f'
SPECTRAL_COMPARISON_HASH = '8872145e6701ca9ee33e33572a9bc01fc816af429ad36867582aa8b9b31cbe08'
READS = {}


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    row = {'path': str(path), 'bytes': len(data),
           'sha256': hashlib.sha256(data).hexdigest()}
    READS[str(path)] = row
    return row


def authenticate(row):
    got = identity(row['path'])
    assert got['bytes'] == row['bytes'] and got['sha256'] == row['sha256'], row
    return got


def auth_json(path, expected):
    row = identity(path)
    assert row['sha256'] == expected, row
    return json.loads(Path(path).read_text())


def authenticate_sources():
    pre = auth_json(HERE / 'PRE_COMPARISON_SEAL.json', PRE_HASH)
    for row in pre['science_sources'] + pre['independent_artifacts']:
        authenticate(row)
    assert len(pre['science_sources']) == 5 and len(pre['independent_artifacts']) == 20
    author = auth_json(AUTHOR / 'AUTHOR_SEAL.json', AUTHOR_HASH)
    for row in author['artifacts']:
        assert Path(row['path']).parent == AUTHOR
        authenticate(row)
    # Do not recursively open source paths merely because a manifest names them.
    already_authorized = {row['path'] for row in pre['science_sources']}
    already_authorized.add(str(HERE.parent / 'actual_first_output_independent' /
                               'PRE_COMPARISON_SEAL.json'))
    source_checks = []
    source_unopened = []
    for row in author['sources']:
        if row['path'] in already_authorized:
            source_checks.append(authenticate(row))
        else:
            source_unopened.append(row)
    spectral = auth_json(SPECTRAL / 'FINAL_SEAL.json', SPECTRAL_HASH)
    comparison = identity(SPECTRAL / 'COMPARISON.md')
    assert comparison['sha256'] == SPECTRAL_COMPARISON_HASH
    relevant = {str(SPECTRAL / name) for name in
                ['COMPARISON.md', 'REPORT.md', 'PRE_COMPARISON_SEAL.json']}
    spectral_rows = [row for row in spectral['artifacts'] if row['path'] in relevant]
    assert len(spectral_rows) == 3
    for row in spectral_rows:
        authenticate(row)
    assert spectral['required_corrections'] == []
    saved = json.loads((AUTHOR / 'CUBE_LOCAL_LIMIT_CONTROLS.json').read_text())
    receipt = json.loads((AUTHOR / 'CONTROLS_RUN_RECEIPT.json').read_text())
    assert receipt['exit_code'] == 0
    assert receipt['source_sha256'] == saved['source_sha256']
    assert saved['source_sha256'] == identity(AUTHOR / 'cube_physical_controls.py')['sha256']
    assert (AUTHOR / 'CONTROLS.stderr.log').read_bytes() == b''
    stream = (AUTHOR / 'CONTROLS.stdout.log').read_text()
    decoder = json.JSONDecoder()
    objects = []
    while stream.strip():
        obj, end = decoder.raw_decode(stream.lstrip())
        objects.append(obj)
        stream = stream.lstrip()[end:]
    assert len(objects) == 3
    assert objects[:2] == saved['complete_spin_operator_controls']
    assert objects[-1] == saved
    return saved, {
        'pre_original_source_and_artifact_bindings': 25,
        'author_artifact_bindings': len(author['artifacts']),
        'author_source_rows_authenticated': source_checks,
        'author_source_rows_deliberately_not_opened': source_unopened,
        'spectral_final_binding': identity(SPECTRAL / 'FINAL_SEAL.json'),
        'spectral_comparison_binding': comparison,
        'spectral_relevant_artifact_bindings': spectral_rows,
        'spectral_comparison_required_corrections': spectral['required_corrections'],
        'spectral_scope': 'Dependency comparison closed; no new spectral proof executed here.',
        'author_stdout_json_objects_parsed_and_matched': len(objects),
        'author_stderr_empty': True,
        'author_receipt_exit_code': receipt['exit_code'],
        'author_runner_executed': False,
    }


@lru_cache(None)
def charge_words(number):
    """Enumerate all charge-four matter words before imposing grade."""
    result = []
    nminus = (number - 4) // 2
    for occupied in combinations(range(8), number):
        for negative in combinations(occupied, nminus):
            q = [0] * 8
            for v in occupied:
                q[v] = -1 if v in negative else 1
            assert sum(q) == 4
            result.append(tuple(q))
    return tuple(result)


@lru_cache(None)
def origin_field(q):
    return np.array(independent.fields(q), dtype=np.int64)


def physical_basis(number, grade, spin):
    coords = np.array(list(product(range(-spin, spin + 1), repeat=5)), dtype=np.int64)
    circulations = coords @ np.array(independent.CYCLE, dtype=np.int64).T
    states = []
    fieldrows = []
    for q in charge_words(number):
        if independent.grade(q) != grade:
            continue
        fields = circulations + origin_field(q)
        allowed = np.all(np.abs(fields) <= spin, axis=1)
        for m, E in zip(coords[allowed], fields[allowed]):
            states.append((q, tuple(map(int, m))))
            fieldrows.append(E)
    fields = np.array(fieldrows, dtype=np.int64)
    assert len(states) == len(set(states))
    return states, fields


@lru_cache(None)
def transitions(q, kind):
    out = []
    E = tuple(map(int, origin_field(q)))
    if kind == 'hop':
        for (qq, EE), amplitude, edge, k in independent.hops((q, E)):
            assert amplitude == -1
            dm = tuple(EE[e] - E[e] for e in independent.CHORDS)
            assert tuple(EE) == independent.fields(qq, dm)
            out.append((qq, dm, edge, k))
    else:
        assert kind == 'birth'
        for edge, (u, v) in enumerate(independent.EDGES):
            if q[u] or q[v]:
                continue
            for sigma in (-1, 1):
                qq = list(q)
                qq[u], qq[v] = sigma, -sigma
                EE = list(E)
                EE[edge] += sigma
                assert independent.physical(tuple(qq), tuple(EE))
                dm = tuple(EE[e] - E[e] for e in independent.CHORDS)
                assert tuple(EE) == independent.fields(tuple(qq), dm)
                out.append((tuple(qq), dm, edge, sigma))
    return tuple(out)


def matrices(source, target, spin, kind):
    states, fields = source
    index = {state: j for j, state in enumerate(target[0])}
    channels = [None] if kind == 'hop' else [(e, s) for e in range(12) for s in (-1, 1)]
    data = {c: ([], [], []) for c in channels}
    for j, ((q, m), E) in enumerate(zip(states, fields)):
        for qq, dm, edge, k in transitions(q, kind):
            targetstate = (qq, tuple(a + b for a, b in zip(m, dm)))
            i = index.get(targetstate)
            if i is None:
                continue
            w = independent.weight(int(E[edge]), k, spin)
            if not w:
                continue
            c = None if kind == 'hop' else (edge, k)
            rr, cc, vv = data[c]
            rr.append(i)
            cc.append(j)
            vv.append(-w if kind == 'hop' else w)
    return {c: sparse.csc_matrix((vv, (rr, cc)), shape=(len(target[0]), len(states)))
            for c, (rr, cc, vv) in data.items()}


def maxabs(matrix):
    return float(max(np.abs(matrix.data), default=0.))


def diag_range(matrix):
    values = matrix.diagonal()
    return [float(np.min(values)), float(np.max(values))]


def gram_sum(maps):
    return sum(j.T @ j for j in maps.values()).tocsc()


def spin_controls(spin, expected):
    bases = {name: physical_basis(n, g, spin) for name, n, g in
             [('P4', 4, 0), ('Q4', 4, 1), ('P6', 6, 0),
              ('Q6', 6, 1), ('R6', 6, 2), ('P8', 8, 0)]}
    a4 = matrices(bases['P4'], bases['Q4'], spin, 'hop')[None]
    j4 = matrices(bases['Q4'], bases['P6'], spin, 'birth')
    b4 = {c: -j @ a4 for c, j in j4.items()}
    g4 = gram_sum(b4)
    assert maxabs(g4 - sparse.diags(g4.diagonal())) == 0
    E2 = np.sum(bases['P4'][1] ** 2, axis=1)
    electric_error = maxabs(a4.T @ a4 - sparse.diags(12 - E2 / (spin * (spin + 1))))
    assert electric_error < 2e-13
    i0 = bases['P4'][0].index((independent.q0, (0,) * 5))
    a6 = matrices(bases['P6'], bases['Q6'], spin, 'hop')[None]
    r6 = matrices(bases['Q6'], bases['R6'], spin, 'hop')[None]
    j6 = matrices(bases['Q6'], bases['P8'], spin, 'birth')
    jgram = gram_sum(j6)
    assert maxabs(jgram - sparse.diags(jgram.diagonal())) == 0
    cross = max(maxabs(j6[e, 1].T @ j6[e, -1]) for e in range(12))
    assert cross == 0
    # An extra complete-basis corroboration of the independently proved bound16.
    b6 = {c: -j @ a6 for c, j in j6.items()}
    g6 = gram_sum(b6)
    g6_rowsum = float(np.max(np.asarray(abs(g6).sum(axis=1))))
    assert g6_rowsum <= 16 + 1e-12
    coherent = {e: b6[e, 1] + b6[e, -1] for e in range(12)}
    coherent_difference = maxabs(gram_sum(coherent) - g6)
    assert coherent_difference < 1e-12
    row = {
        'S': spin,
        'dimensions': {name: len(basis[0]) for name, basis in bases.items()},
        'first_electric_identity_max_error': electric_error,
        'first_loss_diagonal_range': diag_range(g4),
        'first_zero_field_loss': float(g4[i0, i0]),
        'P6_to_Q6_max_column_entries': int(max(np.diff(a6.indptr))),
        'P6_to_Q6_max_row_entries': int(max(np.diff(a6.tocsr().indptr))),
        'Q6_to_R6_max_column_entries': int(max(np.diff(r6.indptr))),
        'Q6_to_R6_max_row_entries': int(max(np.diff(r6.tocsr().indptr))),
        'next_bare_creation_gram_range': diag_range(jgram),
        'coherent_resolved_cross_gram_max': cross,
    }
    differences = {}
    for key, value in row.items():
        if key in ('first_electric_identity_max_error', 'first_loss_diagonal_range'):
            differences[key] = float(np.max(np.abs(np.array(value) - np.array(expected[key]))))
            assert differences[key] < 2e-13, (key, value, expected[key])
        else:
            assert value == expected[key], (key, value, expected[key])
    answer = {'reconstructed_author_fields': row, 'floating_discrepancies': differences,
              'independent_refinement_next_gram_max_absolute_row_sum': g6_rowsum,
              'independent_refinement_next_coherent_resolved_gram_error': coherent_difference}
    print(json.dumps(answer), flush=True)
    return answer


def exact_controls(saved):
    seed = {independent.SEED: 1}
    h2 = independent.h2(seed)
    h4 = independent.h4(seed)
    z = independent.hop(independent.hop(seed, 1), 2)
    assert h2 == {independent.SEED: -12}
    assert h4[independent.SEED] == 60
    assert independent.inner(z, z) == 168
    expected = {independent.SEED: 60}
    for face in independent.FACES:
        for sign in (-1, 1):
            expected[independent.q0, tuple(sign * e for e in face)] = -2
    assert h4 == expected
    got = {'H2_diagonal': -12, 'H4_diagonal': 60, 'ZdaggerZ_diagonal': 168,
           'face_shifts': [list(f) for f in independent.FACES],
           'H4_face_coefficient': -2, 'total_H4_Laurent_terms': len(h4)}
    assert got == saved['exact_rotor_first_sector']
    return got


def main():
    assert not (HERE / 'COMPARISON_RESULTS.json').exists()
    saved, sources = authenticate_sources()
    exact = exact_controls(saved)
    rows = [spin_controls(row['S'], row) for row in saved['complete_spin_operator_controls']]
    result = {
        'source_sha256': identity(Path(__file__))['sha256'],
        'source_authentication': sources,
        'exact_first_sector': exact,
        'complete_spin_comparisons': rows,
        'tree_convention': {'independent_deleted_vertex': 7,
                            'author_deleted_vertex': 0,
                            'independent_tree_minor_determinant': int(independent.TREE_MINOR.det()),
                            'chords': independent.CHORDS,
                            'meaning': 'Same unique Gauss solution at each charge/chord field; no phase/sign change.'},
        'read_identities': sorted(READS.values(), key=lambda r: r['path']),
        'scope': 'Exact combinatorics plus full physical S1/S2 matrix corroboration; no spin evolution or new spectral proof.',
    }
    (HERE / 'COMPARISON_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
