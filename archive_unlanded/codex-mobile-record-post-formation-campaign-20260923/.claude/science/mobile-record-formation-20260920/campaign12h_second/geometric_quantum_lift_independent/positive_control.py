#!/usr/bin/env python3
"""Positive square witness: literal tensor permutation and consistent rephasing."""
from pathlib import Path
import datetime, hashlib, importlib.util, itertools, json, sys
import sympy as sp
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('own_quantum_check', HERE / 'independent_check.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

def main():
    square = (0, 1, 2, 3)
    edges = {c.edge(i, (i + 1) % 4) for i in range(4)}
    _, _, _, states, kinetic, _ = c.orthogonal_lift(4, edges, [square], matrices=True)
    spinors = [sp.Matrix([1, 0]), sp.Matrix([0, 1]),
               sp.Matrix([1, 1]) / sp.sqrt(2), sp.Matrix([-1, 1]) / sp.sqrt(2)]
    V = sp.Matrix.hstack(*(c.tensor_column(eta, spinors) for eta in states))
    R = sp.zeros(len(states))
    for i, eta in enumerate(states):
        R[states.index(c.rotate(eta, square)), i] = 1
    basis = list(itertools.product(range(2), repeat=4))
    P = sp.zeros(16)
    for i, bits in enumerate(basis):
        P[basis.index(c.rotate(bits, square)), i] = 1
    assert P * V == V * R
    assert sp.Matrix(kinetic.tolist()) == R + R.T
    H = sp.Rational(2, 3) * sp.eye(16) - (R + R.T) / 2
    physical = sp.Rational(2, 3) * sp.eye(16) - (P + P.T) / 2
    G = V.T * V
    assert physical * V == V * H and G * H == H * G
    D = sp.diag(*(sp.I ** (i % 4) for i in range(16)))
    vp, hp, gp = V * D, D.conjugate().T * H * D, D.conjugate().T * G * D
    assert physical * vp == vp * hp and gp * hp == hp * gp
    assert vp.conjugate().T * vp == gp
    result = {'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'positive_literal_square_intertwiner_exact': True,
              'square_Gram_commutes_even_though_not_isometric': True,
              'consistent_configuration_basis_rephasing_preserves_compatibility': True,
              'scope': 'All configurations of one square are flippable. This does not construct the sharply conditioned ladder operation.',
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'independent_helper_sha256': hashlib.sha256((HERE / 'independent_check.py').read_bytes()).hexdigest()}
    (HERE / 'POSITIVE_CONTROL_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print('Exact literal square permutation witness and consistent rephasing passed.')

if __name__ == '__main__':
    main()
