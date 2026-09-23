"""New energy-filter controls using only frozen independent ring local rules.

No energy-selected author source or runner is opened. Numerical convergence
is corroboration; the moving-window and instrument-limit proofs are analytic.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
HERE = Path(__file__).resolve().parent
OLD = HERE.parent / 'finite_spin_flat_independent'
sys.path.insert(0, str(OLD))
import json, hashlib
from collections import defaultdict
from fractions import Fraction
import numpy as np
import scipy.linalg as la
import scipy.sparse as sparse
from scipy.sparse.linalg import spsolve
import sympy as sy
import physical_builder as pb
import flat_probe as fp

EXPECTED = {
    'physical_builder.py': '1cbc6dcb8a994c5f7fc4ec178c586b3aefcede49fd6a30906b0446bf332c9dc2',
    'flat_probe.py': 'ba04c00080143a8f0b9bfe3ed6b249139c1201a691f23584d911a78ebf237fd6',
}
for name, digest in EXPECTED.items():
    assert hashlib.sha256((OLD / name).read_bytes()).hexdigest() == digest
q0 = tuple(int(v % 2 == 0) for v in range(8))


def first_outputs(f, spin=None):
    result = defaultdict(lambda: defaultdict(Fraction if spin is None else float))
    for q1, d1, e1, k1, g1 in pb.hop_data(q0):
        a1 = Fraction(1) if spin is None else pb.weight(f, g1, k1, spin)
        for q2, d2, e2, c, g2 in pb.birth_data(q1):
            if pb.grade(q2) != 0:
                continue
            a2 = Fraction(1) if spin is None else pb.weight(f + d1, g2, c, spin)
            if a1 * a2:
                result[e2, c][q2, f + d1 + d2] += a1 * a2
    return {ch: dict(v) for ch, v in result.items()}


def inner(v, w):
    return sum(complex(a).conjugate() * complex(w.get(s, 0)) for s, a in v.items())


def add(v, w):
    answer = defaultdict(complex, v)
    for state, amp in w.items():
        answer[state] += amp
    return {s: a for s, a in answer.items() if a}


def exact_first_projected_grams():
    fields = range(-2, 3)
    outputs = {f: first_outputs(f) for f in fields}
    projected = {f: {ch: fp.project(v) for ch, v in js.items()}
                 for f, js in outputs.items()}
    assert all(len(js) == 16 for js in outputs.values())
    channels = sorted(outputs[0])
    max_residual = 0.
    cross = 0.
    for f in fields:
        for z in fields:
            for ch in channels:
                gram = inner(projected[f][ch], projected[z][ch])
                target = Fraction(1, 2) if f == z else 0
                max_residual = max(max_residual, abs(gram - target))
                assert gram == target
            for edge in range(8):
                gram = inner(projected[f][edge, 1], projected[z][edge, -1])
                cross = max(cross, abs(gram))
                assert gram == 0
    rates = []
    for f in fields:
        res = sum(inner(v, v).real for v in projected[f].values())
        coh = sum(inner(add(projected[f][e, 1], projected[f][e, -1]),
                        add(projected[f][e, 1], projected[f][e, -1])).real for e in range(8))
        assert res == coh == 8
        rates.append({'f': f, 'resolved_selected_rate_without_kappa': res,
                      'coherent_selected_rate_without_kappa': coh})
    # Exact field-translation invariance extends the check to every integer f.
    return {'fields': list(fields), 'resolved_channels': 16, 'coherent_channels': 8,
            'resolved_channel_gram': 'I/2', 'fixed_edge_cross_gram': 0,
            'maximum_exact_residual': max_residual, 'rows': rates,
            'wrong_unchanged_first_rate16_rejected_by': 8,
            'all_field_extension': 'Rotor paths and the compact projector commute with common circulation translation; distinct input f have distinct outputs within each fixed B-occupancy block.'}


def flat_hamiltonian(cut, K, delta):
    modes = [(a, r, f) for a in range(2) for r in range(6)
             for f in range(-cut, cut + 1)]
    index = {s: j for j, s in enumerate(modes)}
    rr, cc, vv = [], [], []
    for a in range(2):
        for r in range(6):
            electric = fp.compress(fp.h2_apply(fp.flat_mode(a, r), correction=True))
            assert set(electric) == {(a, r, 0)}
            h4 = fp.compress(fp.h4_apply(fp.flat_mode(a, r)))
            for f in range(-cut, cut + 1):
                col = index[a, r, f]
                rr.append(col); cc.append(col)
                vv.append(float(K * electric[a, r, 0].subs(fp.f, f)))
                for (b, s, shift), value in h4.items():
                    target = (b, s, f + shift)
                    if target in index:
                        rr.append(index[target]); cc.append(col); vv.append(float(delta * value))
    H = sparse.csc_matrix((vv, (rr, cc)), shape=(len(modes), len(modes)))
    assert sparse.linalg.norm(H - H.T) < 1e-13
    return modes, H


def lift(coeffs, modes):
    result = defaultdict(complex)
    for amp, (a, r, f) in zip(coeffs, modes):
        for state, c in fp.flat_mode(a, r, f).items():
            result[state] += amp * complex(c) / np.sqrt(2)
    return dict(result)


def resolvent_reference(K, delta, mode=(0, 2, 0), cut=8):
    modes, H = flat_hamiltonian(cut, K, delta)
    src = np.zeros(len(modes)); src[modes.index(mode)] = 1
    solutions = {sign: spsolve(H - sign * 1j * sparse.eye(len(modes)), src)
                 for sign in (-1, 1)}
    # Embed the finite-support resolvent solution in a larger flat basis. The
    # residual contains every omitted boundary edge, so ||residual||/|Im z|
    # bounds its error in the exact infinite selfadjoint resolvent.
    larger, HL = flat_hamiltonian(cut + 1, K, delta)
    li = {s: j for j, s in enumerate(larger)}
    residuals = {}
    for sign, v in solutions.items():
        embedded = np.zeros(len(larger), complex)
        for j, state in enumerate(modes): embedded[li[state]] = v[j]
        source = np.zeros(len(larger)); source[li[mode]] = 1
        residual = (HL - sign * 1j * sparse.eye(len(larger))) @ embedded - source
        residuals[sign] = float(np.linalg.norm(residual))
    gvec = (solutions[1] - solutions[-1]) / (2j)
    return lift(gvec, modes), {
        'filter': 'g(x)=1/(1+x^2)', 'flat_mode': list(mode), 'reference_flux_cut': cut,
        'resolvent_residual_norms': residuals,
        'full_reference_norm_error_bound_from_residuals': sum(residuals.values()) / 2,
        'roundoff_limit': 'Floating residual, not an interval-arithmetic certificate.'}


def first_matrices(spin, p6):
    index = {state: j for j, state in enumerate(p6)}
    matrices = {(e, c): np.zeros((len(p6), 2 * spin + 1))
                for e in range(8) for c in (-1, 1)}
    for col, f in enumerate(range(-spin, spin + 1)):
        for ch, output in first_outputs(f, spin).items():
            for state, amp in output.items():
                assert state in index
                matrices[ch][index[state], col] = amp
    return matrices


def gram(matrices):
    return sum(B.conj().T @ B for B in matrices.values())


def compare_vector(v, basis, exact):
    got = {state: amp for state, amp in zip(basis, v)}
    return float(np.sqrt(sum(abs(got.get(s, 0) - exact.get(s, 0)) ** 2
                             for s in set(got) | set(exact))))


def finite_filter_controls():
    K, delta = .4, .25
    reference, reference_info = resolvent_reference(K, delta)
    assert reference_info['full_reference_norm_error_bound_from_residuals'] < 1e-10
    rows = []
    for spin in (2, 4, 8, 16):
        p6, n8, H2, H4, B6, R6 = pb.finite_operators(spin)
        eta = K * spin * (spin + 1)
        shifted = eta * (H2.toarray() + 4 * np.eye(len(p6))) + delta * H4.toarray()
        ev, U = la.eigh(shifted)
        width = eta ** .5
        selected = abs(ev) <= width
        V = U[:, selected]
        B4 = first_matrices(spin, p6)
        selected_B = {ch: V @ (V.conj().T @ B) for ch, B in B4.items()}
        coherent = {e: selected_B[e, 1] + selected_B[e, -1] for e in range(8)}
        original = gram(B4)
        selected_resolved = gram(selected_B)
        selected_coherent = gram(coherent)
        original_coherent = gram({e: B4[e, 1] + B4[e, -1] for e in range(8)})
        assert np.linalg.norm(original - original_coherent) < 1e-12
        assert np.min(la.eigvalsh(original - selected_resolved)) > -1e-10
        assert np.min(la.eigvalsh(original_coherent - selected_coherent)) > -1e-10
        fixed_edge_cross = max(float(la.norm(selected_B[e, 1].conj().T @ selected_B[e, -1], 2)) for e in range(8))
        first_index = spin
        source_error = 0.
        for ch, output in first_outputs(0).items():
            source_error = max(source_error,
                compare_vector(selected_B[ch][:, first_index], p6,
                               {s: complex(a) for s, a in fp.project(output).items()}))
        phi = np.array([complex(fp.flat_mode(0, 2).get(s, 0)) for s in p6]) / np.sqrt(2)
        assert abs(np.linalg.norm(phi) - 1) < 1e-12
        smooth = U @ ((U.conj().T @ phi) / (1 + ev ** 2))
        phi_selected = V @ (V.conj().T @ phi)
        single = first_outputs(0)[0, 1]
        projected = fp.project(single)
        complement = {s: complex(single.get(s, 0) - projected.get(s, 0)) * np.sqrt(2)
                      for s in set(single) | set(projected)}
        qvec = np.array([complement.get(s, 0) for s in p6])
        assert abs(np.linalg.norm(qvec) - 1) < 1e-12
        qselected = V @ (V.conj().T @ qvec)
        # Filter orthogonality need not survive a nonlocal output filter.
        # A fixed smooth C0 filter supplies an additional concrete test.
        GB = {ch: U @ ((U.conj().T @ B) / (1 + ev[:, None] ** 2)) for ch, B in B4.items()}
        smooth_cross = max(float(la.norm(GB[e, 1].conj().T @ GB[e, -1], 2)) for e in range(8))
        row = {'S': spin, 'P6_dimension': len(p6), 'eta': eta, 'sharp_half_width': width,
               'width_over_eta': width / eta, 'selected_rank': int(sum(selected)),
               'flat_sharp_projection_error': float(np.linalg.norm(phi_selected - phi)),
               'continuous_input_selected_norm': float(np.linalg.norm(qselected)),
               'max_zero_field_first_source_vector_error': source_error,
               'smooth_flat_functional_calculus_error': compare_vector(smooth, p6, reference),
               'zero_field_selected_first_rate_resolved_without_kappa': float(selected_resolved[first_index, first_index].real),
               'zero_field_selected_first_rate_coherent_without_kappa': float(selected_coherent[first_index, first_index].real),
               'sharp_total_coherent_resolved_loss_difference_norm': float(la.norm(selected_coherent - selected_resolved, 2)),
               'sharp_fixed_edge_cross_gram_max_norm': fixed_edge_cross,
               'smooth_fixed_edge_cross_gram_max_norm': smooth_cross,
               'finite_spin_original_first_loss_norm': float(la.norm(original, 2))}
        assert row['finite_spin_original_first_loss_norm'] <= 16 + 1e-12
        rows.append(row)
        print(json.dumps(row), flush=True)
    return {'parameters': {'K': K, 'delta': delta}, 'reference': reference_info, 'rows': rows,
            'status': 'Complete physical finite-spin matrices; finite-size values are corroboration, not the analytic convergence proof.'}


def counterexample_and_count_controls():
    # A_N is multiplication by midpoint(floor(Nx)/N) on L2([0,1]);
    # ||A_N-x|| <= 1/(2N). A window around one cell selects its normalized
    # indicator with certainty, but has constant-input probability1/N.
    concentration = [{'N': n, 'window_scaled_half_width': 1 / (3 * n),
                      'constant_input_probability': 1 / n,
                      'cell_normalized_input_probability': 1,
                      'operator_norm_window_projection': 1,
                      'operator_approximation_error_bound': 1 / (2 * n)}
                     for n in (8, 32, 128)]
    t, k = sy.symbols('t k', positive=True)
    p4 = sy.exp(-8 * k * t)
    p6 = 2 * (sy.exp(-4 * k * t) - sy.exp(-8 * k * t))
    p8 = (1 - sy.exp(-4 * k * t)) ** 2
    assert sy.simplify(p4 + p6 + p8) == 1
    assert sy.simplify(sy.diff(p4, t) + 8 * k * p4) == 0
    assert sy.simplify(sy.diff(p6, t) - 8 * k * p4 + 4 * k * p6) == 0
    assert sy.simplify(sy.diff(p8, t) - 4 * k * p6) == 0
    assert [x.subs(t, 0) for x in (p4, p6, p8)] == [1, 0, 0]
    return {'noncompact_input_family_counterexample': concentration,
            'order_eta_width_counterexample': 'H=multiplication by x on [0,1], psi=1, window center eta/2 and half-width eta/4 has probability1/2.',
            'changed_ring_probabilities': [str(p4), str(p6), str(p8)],
            'changed_rates_without_kappa': [8, 4],
            'ODE_and_conservation_residuals': [0, 0, 0, 0],
            'wrong_original_first_clock_rejected': 'Using16 instead of the independently computed selected first rate8 violates the first population derivative at t=0 by8 kappa.'}


def main():
    assert not (HERE / 'FILTER_RESULTS.json').exists()
    result = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'reused_independent_builder_hashes': EXPECTED,
              'projected_first_grams': exact_first_projected_grams(),
              'finite_filters': finite_filter_controls(),
              'counterexamples_and_counts': counterexample_and_count_controls()}
    (HERE / 'FILTER_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
