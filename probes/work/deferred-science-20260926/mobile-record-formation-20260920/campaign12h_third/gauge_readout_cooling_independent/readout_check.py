#!/usr/bin/env python3
"""Exact plaquette readout, Gauss, and fresh-probe controls; no author imports."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time
import sympy as s

HERE = Path(__file__).resolve().parent


def zero(M):
    return all(s.expand(x) == 0 for x in M)


def controls():
    # Edges: 0->1, 1->2, 3->2, 0->3. Plaquette displacement (+,+,-,-).
    D = s.Matrix([[1, 0, 0, 1], [-1, 1, 0, 0], [0, -1, -1, 0], [0, 0, 1, -1]])
    z = s.Matrix([1, 1, -1, -1]); assert D*z == s.zeros(4, 1)
    W = s.zeros(16); W[3, 12] = 1
    X = W+W.H; Y = -s.I*(W-W.H)
    Z = s.diag(*[2*(b & 1)-1 for b in range(16)])
    P = W.H*W+W*W.H; Znf = (s.eye(16)-P)*Z
    assert P*P == P and zero(X*X-P) and zero(Y*Y-P)
    assert zero(X*Y-Y*X-2*s.I*P*Z)
    assert zero(Z*X-X*Z-2*s.I*Y)
    assert zero(Z*Y-Y*Z+2*s.I*X)
    pulse_rows = []
    for label, observable in [('X', X), ('Y', Y)]:
        rotations = {}
        for sign in (-1, 1):
            R = (s.eye(16)-P)+(P+(s.I*sign*Y if label == 'X' else -s.I*sign*X))/s.sqrt(2)
            assert zero(R.H*R-s.eye(16))
            assert zero(R.H*Z*R-Znf-sign*observable)
            rotations[sign] = R
        for outcome in (-1, 1):
            E = s.zeros(16)
            for sign, R in rotations.items():
                charge = -sign*outcome
                E += R.H*(s.eye(16)-charge*Z)*R/4
            assert zero(E-(s.eye(16)+outcome*observable)/2)
        pulse_rows.append({'observable': label, 'opposite_pulse_offset_cancellation_exact': True,
                           'binary_POVM': '(I+outcome*'+label+')/2',
                           'estimator': '-setting_sign * newly_formed_charge_at_x'})
    # Nonflippable all-low field: the unrandomized readout has a nonzero offset.
    assert X[0, 0] == Y[0, 0] == 0 and Znf[0, 0] == -1

    charges = [(x, y) for x in (0, 1, -1) for y in (0, 1, -1)]
    mix = {c: j for j, c in enumerate(charges)}; dim = 9*16
    V = {q: s.MutableSparseMatrix(dim, dim, {}) for q in (-1, 1)}
    N = s.SparseMatrix(s.diag(*[int(x != 0)+int(y != 0) for x, y in charges for b in range(16)]))
    Qvac = s.SparseMatrix(s.diag(*[int((x, y) == (0, 0)) for x, y in charges for b in range(16)]))
    for q in (-1, 1):
        for b in range(16):
            if (2*(b & 1)-1) == -q:
                V[q][16*mix[(q, -q)]+(b ^ 1), 16*mix[(0, 0)]+b] = 1
        assert N*V[q]-V[q]*N == 2*V[q]
    assert V[1].H*V[-1] == s.zeros(dim)
    assert V[1].H*V[1]+V[-1].H*V[-1] == Qvac
    G = []
    for vertex in range(4):
        diagonal = []
        for x, y in charges:
            for b in range(16):
                E = s.Matrix([s.Rational(2*((b >> e) & 1)-1, 2) for e in range(4)])
                charge = x if vertex == 0 else y if vertex == 1 else 0
                diagonal.append((D*E)[vertex]-charge)
        G.append(s.SparseMatrix(s.diag(*diagonal)))
    for A in G:
        for q in (-1, 1):
            assert A*V[q] == V[q]*A
        for O in (X, Y):
            Oext = s.SparseMatrix(s.kronecker_product(s.eye(9), O))
            assert A*Oext == Oext*A
    # Fresh neutral probe: fuel=0, spent+=1, spent-=2.
    C = s.MutableSparseMatrix(3*dim, 3*dim, {})
    for q, probe_out in ((1, 1), (-1, 2)):
        for (row, col), value in V[q].todok().items():
            C[3*row+probe_out, 3*col] += value
            C[3*col, 3*row+probe_out] += s.conjugate(value)
    assert C.H == C and C*C*C == C
    count = s.SparseMatrix(s.kronecker_product(N, s.eye(3))+2*s.kronecker_product(s.eye(dim), s.diag(1, 0, 0)))
    assert C*count == count*C
    for A in G:
        ext = s.SparseMatrix(s.kronecker_product(A, s.eye(3))); assert C*ext == ext*C
    c, sine = s.Rational(3, 5), s.Rational(4, 5)
    U = s.SparseMatrix.eye(3*dim)+(c-1)*(C*C)-s.I*sine*C
    assert U.H*U == s.eye(3*dim)
    fuel_cols = [3*i for i in range(dim)]
    M = [U.extract([3*i+j for i in range(dim)], fuel_cols) for j in range(3)]
    assert M[0] == s.eye(dim)+(c-1)*Qvac
    assert M[1] == -s.I*sine*V[1] and M[2] == -s.I*sine*V[-1]
    assert sum((A.H*A for A in M), s.SparseMatrix.zeros(dim)) == s.eye(dim)
    gram = s.Matrix([[s.trace(A.H*B) for B in M] for A in M])
    assert gram.det() != 0
    # Boundary permanence and field-independent success on a vacant input.
    deltaN = sum((A.H*N*A for A in M), s.SparseMatrix.zeros(dim))-N
    assert deltaN == 2*sine*sine*Qvac
    for q in (-1, 1):
        block = (V[q].H*V[q]).extract(range(16), range(16))
        assert block == (s.eye(16)-q*Z)/2
    # A fully formed edge readout can destroy plaquette coherence.
    rho = s.zeros(16)
    for a in (3, 12):
        for b in (3, 12): rho[a, b] = s.Rational(1, 2)
    rho_ext = s.SparseMatrix.zeros(dim); rho_ext[:16, :16] = rho
    formed = sum((V[q]*rho_ext*V[q].H for q in (-1, 1)), s.SparseMatrix.zeros(dim))
    field = sum((formed.extract(range(16*m, 16*(m+1)), range(16*m, 16*(m+1))) for m in range(9)), s.zeros(16))
    assert s.trace(X*rho) == 1 and s.trace(X*field) == 0
    return {'field_dimension': 16, 'matter_field_dimension': dim, 'probe_dilation_dimension': 3*dim,
            'plaquette_incidence_times_displacement': list(D*z),
            'exact_pulse_controls': pulse_rows,
            'nonflippable_countercontrol': {'field_bit_word': '0000', 'X_mean': 0, 'Y_mean': 0,
                                           'single_pulse_minus_charge_mean': -1},
            'gauge_commutators_zero': ['X pulse', 'Y pulse', 'V_plus', 'V_minus', 'fresh_probe_C'],
            'C_cubic_identity_and_unitarity_exact': True,
            'conserved_count': 'N_matter+2 P_fuel',
            'finite_step': {'cos_theta': str(c), 'sin_theta': str(sine), 'birth_probability': str(sine**2),
                            'Kraus_Hilbert_Schmidt_Gram': [[str(x) for x in gram.row(i)] for i in range(3)],
                            'global_coarse_channel_Choi_rank': 3,
                            'mean_record_increment_operator': '2*(16/25)*P_vac'},
            'disturbance_control': {'input_X_mean': 1, 'postbirth_field_X_mean': 0},
            'scope': 'Exact finite algebra for the stipulated enlarged matter/link/probe model. No unknown-state nondisturbance or native implementation claim.'}


if __name__ == '__main__':
    started = time.monotonic()
    result = {'created_utc': datetime.now(timezone.utc).isoformat(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'controls': controls(), 'runtime_seconds': time.monotonic()-started}
    text = json.dumps(result, indent=2, default=str)+'\n'
    (HERE/'READOUT_RESULTS.json').write_text(text); print(text, end='')
