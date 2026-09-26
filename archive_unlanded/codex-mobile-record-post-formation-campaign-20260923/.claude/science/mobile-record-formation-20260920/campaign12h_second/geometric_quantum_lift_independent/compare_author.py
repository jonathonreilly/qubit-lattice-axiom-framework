#!/usr/bin/env python3
"""Post-seal exact source/witness comparison. Never calls author main."""
from pathlib import Path
import datetime, hashlib, importlib.util, json, sys
import numpy as np
import sympy as sp
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
RAW = HERE.parent

def identity(p):
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def loadmodule(name, p):
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def main():
    seal = json.loads((HERE / 'PRE_COMPARISON_SEAL.json').read_text())
    for row in seal['artifacts']:
        assert identity(Path(row['path'])) == row
    assert identity(RAW / 'GEOMETRIC_QUANTUM_LIFT_BOUNDARY.md') == seal['sources']['source_read_completely']
    own = loadmodule('independent_quantum_lift', HERE / 'independent_check.py')
    author = loadmodule('author_quantum_lift', RAW / 'geometric_quantum_lift_check.py')
    result_path = RAW / 'geometric_quantum_lift_checks/RESULTS.json'
    author_result = json.loads(result_path.read_text())
    for name, digest in author_result['sources_sha256'].items():
        assert identity(RAW / name)['sha256'] == digest
    assert result_path.read_bytes() == (RAW / 'GEOMETRIC_QUANTUM_LIFT_RUN.log').read_bytes()
    assert (RAW / 'GEOMETRIC_QUANTUM_LIFT_RUN.stderr').read_bytes() == b''
    independent = json.loads((HERE / 'INDEPENDENT_RESULTS.json').read_text())
    for a, b in zip(author_result['lifts'], independent['orthogonal_controls']):
        assert (a['unmarked_states'], a['fiber_size'], a['marked_states'], a['local_channels']) == (
            b['perfect_matchings'], b['fiber_size'], b['marked_states'], b['two_sense_local_channels'])
        assert a['literal_qubit_dimension'] == 2 ** b['vertices']
    assert author_result['physical_square']['marked_Gram_rank'] == independent['square_literal_map']['z_x_gram_rank'] == 11
    assert author_result['physical_square']['different_geometry_overlap'] == '1/2'
    assert author_result['physical_square']['coherent_Gram_orthogonal_key_axes'] == 'Matrix([[1, 1], [1, 1]])'
    assert author_result['physical_square']['coherent_Gram_generic_key_axes'] == 'Matrix([[674/625, 1], [1, 674/625]])'
    assert author_result['square_probability']['definite_or_incoherent_same_geometry'] == independent['single_orbit']['definite_probability']
    assert author_result['square_probability']['coherent_uniform_fiber'] == independent['single_orbit']['coherent_probability']

    edges = {(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)}
    squares = [(0, 1, 4, 3), (1, 2, 5, 4)]
    _, _, _, states, kinetic, count = own.orthogonal_lift(6, edges, squares, matrices=True)
    _, author_states, _, h2, degree, _, _, _ = author.build(6, edges, squares)
    permutation = [states.index(eta) for eta in author_states]
    assert np.array_equal(h2, -kinetic[np.ix_(permutation, permutation)])
    assert np.array_equal(degree, count[permutation])
    root2 = sp.sqrt(2)
    spinors = [sp.Matrix([1, 0]), sp.Matrix([0, 1]),
               sp.Matrix([1, 1]) / root2, sp.Matrix([-1, 1]) / root2,
               sp.Matrix([1, sp.I]) / root2, sp.Matrix([-1, sp.I]) / root2]
    author_minus_y = sp.Matrix([sp.I, 1]) / root2
    assert author_minus_y == -sp.I * spinors[-1]

    def overlap(eta, xi):
        return sp.simplify(sp.prod((spinors[a].conjugate().T * spinors[b])[0] for a, b in zip(eta, xi)))

    def neighbors(eta):
        M = own.geometry(eta)
        return [own.rotate(eta, p, sign) for p in squares if own.flippable(M, p) for sign in [-1, 1]]

    witnesses = []
    for row in author_result['ladder_Gram_compatibility_witnesses']:
        eta, xi = tuple(row['source_state']), tuple(row['target_state'])
        assert author_states[row['row']] == eta and author_states[row['column']] == xi
        v = sp.Rational(row['v'])
        eta_neighbors, xi_neighbors = neighbors(eta), neighbors(xi)
        kinetic_entry = (sum(overlap(z, xi) for z in eta_neighbors) - sum(overlap(eta, z) for z in xi_neighbors)) / 2
        potential_entry = v * (len(xi_neighbors) - len(eta_neighbors)) * overlap(eta, xi) / 2
        exact = sp.simplify(kinetic_entry + potential_entry)
        assert exact == sp.sympify(row['exact_Gram_commutator']) and exact != 0
        assert abs(float(abs(exact)) - row['numeric_max_abs']) < 1e-14
        witnesses.append({'v': str(v), 'author_indices': [row['row'], row['column']],
                          'configurations': [list(eta), list(xi)],
                          'independent_sparse_commutator': str(exact),
                          'kinetic_part': str(sp.simplify(kinetic_entry)),
                          'potential_part': str(sp.simplify(potential_entry))})
    for row in seal['artifacts']:
        assert identity(Path(row['path'])) == row
    output = {'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'author_result': identity(result_path),
              'author_sources': [identity(RAW / name) for name in author_result['sources_sha256']],
              'note_binding_supplied_by_this_review': identity(RAW / 'GEOMETRIC_QUANTUM_LIFT_BOUNDARY.md'),
              'all_declared_lift_counts_and_square_values_agree': True,
              'complete_ladder_kinetic_and_potential_matrices_agree_after_reindexing': True,
              'author_minus_y_phase_relative_to_independent': '-i, giving common phase -i to every full product column',
              'exact_declared_witnesses': witnesses,
              'author_log_is_byte_identical_to_result_and_stderr_empty': True,
              'author_full_suite_reexecuted': False,
              'unresolved_findings': [], 'failed_attempts': []}
    (HERE / 'AUTHOR_COMPARISON_RESULTS.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(witnesses, indent=2))
    print('Exact declared witnesses, complete ladder matrices, source/result/log bindings all agree.')

if __name__ == '__main__':
    main()
