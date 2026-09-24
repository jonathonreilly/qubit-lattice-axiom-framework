"""Author exact first-jump Grams and complete physical ring filter controls.

The physical finite-spin builder and compact flat basis are reused at explicit
source identities. This is not an independent reconstruction. No finite field
cutoff is imposed on the finite-spin model. Only the infinite flat reference
is truncated, with an analytic resolvent-series bound and a Dyson bound.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/energy_filter_check.py', 'scripts/finite_spin_dynamics_check.py', 'scripts/flat_band_spin_correction_probe.py', 'scripts/flat_compressed_operators.py')
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import hashlib, importlib.util, json, math, time
import numpy as np
from scipy.linalg import eigh
from scipy.sparse import coo_matrix, eye
from scipy.sparse.linalg import expm_multiply, spsolve

D = Path(__file__).resolve().parent
P = D
SOURCES = {
    'finite_spin_dynamics_check.py': '90186b1c250d1978003dbb121e43c3b6486830f54b44cab4f8c4fafd2b2be945',
    'flat_band_spin_correction_probe.py': '791330246ebb0f35b696edd17cead1c95fc4db9ccd43792b569c01293e375d4b',
}
# Fresh generated table is checked structurally by finite_spin_dynamics_check.
for name, expected in SOURCES.items():
    assert hashlib.sha256((P / name).read_bytes()).hexdigest() == expected, name
spec = importlib.util.spec_from_file_location('fixed_ring', P / 'finite_spin_dynamics_check.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
m.K, m.delta, m.kappa = .4, .7, 0.


def first_output(edge, sign):
    initial = (tuple(int(a % 2 == 0) for a in range(8)), (0,) * 8)
    out = defaultdict(Fraction)
    u, v = edge, (edge + 1) % 8
    for (q, E), _ in m.fmod.hops(initial):
        if q[u] or q[v]:
            continue
        for sigma in [-1, 1] if sign is None else [sign]:
            qq = list(q)
            qq[u], qq[v] = sigma, -sigma
            EE = list(E)
            EE[edge] += sigma
            state = (tuple(qq), tuple(EE))
            assert m.fmod.valid(state)
            if all(qq[a] for a in [0, 2, 4, 6]):
                out[state] += 1
    return dict(out)


def cross_laurent(v, w):
    out = defaultdict(Fraction)
    for (q, E), a in v.items():
        for (q2, E2), b in w.items():
            if q == q2:
                shift = tuple(x - y for x, y in zip(E, E2))
                assert len(set(shift)) == 1
                out[shift[0]] += a * b
    return {s: a for s, a in out.items() if a}


def exact_grams():
    rows = []
    for e in range(8):
        v = {sign: first_output(e, sign) for sign in [-1, 1, None]}
        fv = {sign: m.fmod.flat(value) for sign, value in v.items()}
        for sign in [-1, 1, None]:
            n = 2 if sign is None else 1
            assert cross_laurent(v[sign], v[sign]) == {0: n}
            assert cross_laurent(fv[sign], fv[sign]) == {0: Fraction(n, 2)}
            assert m.fmod.flat(fv[sign]) == fv[sign]
            rows.append({'edge': e, 'sign': sign, 'unfiltered_Gram': n,
                         'filtered_Gram': str(Fraction(n, 2)),
                         'projected_output_terms': len(fv[sign])})
        assert cross_laurent(v[1], fv[-1]) == {}
    return {'exact_Laurent_Grams_all_24_marks': rows,
            'resolved_first_total': 8, 'coherent_first_total': 8,
            'opposite_sign_projected_cross_Grams_vanish': True,
            'scope': 'Translation-covariant physical field operator identities, not one-flux norms.'}


def reference_matrix(cut):
    basis = [(kind, r, f) for kind in range(2) for r in range(6)
             for f in range(-cut, cut + 1)]
    ix = {s: i for i, s in enumerate(basis)}
    triplets = []
    ar = [-5, -3, 0, 3, 5, 8]
    br = [2, 1, 0, 1, 2, 4]
    boundary = []
    for col, (kind, r, f) in enumerate(basis):
        if kind == 1 and r == 0:
            electric = 4 * (f - 1)**2
        else:
            k = r if kind == 0 else r - 1
            electric = 4 * f*f + ar[k] * f + br[k]
        triplets.append((col, col, m.K * electric))
        row = next(a for a in m.table if a['kind'] == kind and a['r'] == r)
        for term in row['H4_terms']:
            target = (term['kind'], term['r'], f + term['circulation_shift'])
            value = m.delta * int(term['coefficient'])
            if target in ix:
                triplets.append((ix[target], col, value))
            else:
                boundary.append((target, col, value))
    H = m.matrix_from_triplets(triplets, (len(basis), len(basis)))
    assert np.max(abs((H-H.conj().T).data), initial=0.) < 1e-14
    seed = np.zeros(len(basis), complex)
    # F times the actual resolved e=0,+ output is -b_(1,1)/sqrt(2).
    seed[ix[(1, 1, 1)]] = -1 / np.sqrt(2)
    return basis, H, seed, boundary


def rational_filter(H, vectors, width):
    I = eye(H.shape[0], format='csc')
    minus = spsolve((H-1j*width*I).tocsc(), vectors)
    plus = spsolve((H+1j*width*I).tocsc(), vectors)
    value = width / (2j) * (minus-plus)
    return value, minus, plus


def numerical_controls():
    cut, smooth_width = 24, 16.
    basis, h, flat_seed, boundary = reference_matrix(cut)
    reference, rm, rp = rational_filter(h, flat_seed, smooth_width)
    residuals = []
    for x in [rm, rp]:
        residual = defaultdict(complex)
        for target, col, value in boundary:
            residual[target] += value * x[col]
        residuals.append(float(np.sqrt(sum(abs(v)**2 for v in residual.values()))))
    # Split h into its real electric/H4 diagonal and off-diagonal B. The latter
    # has norm <=4 delta=14/5, while either diagonal resolvent has norm <=1/16.
    # The Neumann terms agree before cut-max|f_initial|+1 translation steps.
    # Bounding both tails and combining the two resolvents gives this exact
    # rational truncation bound; it is not a floating-point certification.
    n0 = cut
    ratio = Fraction(7, 40)
    reference_error_bound = math.nextafter(float(2*ratio**n0/(1-ratio)), math.inf)
    interior_residuals = [float(np.linalg.norm((h-1j*smooth_width*eye(h.shape[0]))@rm-flat_seed)),
                          float(np.linalg.norm((h+1j*smooth_width*eye(h.shape[0]))@rp-flat_seed))]
    times = np.array([-.4, 0., .4])
    prepared = flat_seed * np.sqrt(2)
    ref_motion = expm_multiply(-1j*h, prepared, start=-.4, stop=.4, num=3,
                              traceA=-1j*h.diagonal().sum())
    n0 = cut - 1 + 1
    x = Fraction(2)  # upper bound for 4 delta max|time|=1.12
    exact_tail = 2 * x**n0 * (n0+1) / (math.factorial(n0)*(n0+1-x))
    motion_tail = math.nextafter(float(exact_tail), math.inf)
    rows = []
    for S in [4, 8, 16, 32]:
        started = time.monotonic()
        words, H, unused_loss = m.finite_target(S)
        assert m.kappa == 0.
        ix = {s: i for i, s in enumerate(words)}
        psi = np.zeros(len(words), complex)
        for (q, E), amp in first_output(0, 1).items():
            psi[ix[(q, E[-1])]] = float(amp)
        J = m.embedding(words, basis)
        flat = J @ flat_seed
        bright = psi-flat
        assert abs(np.vdot(flat, flat)-.5) < 1e-13
        assert abs(np.vdot(flat, bright)) < 1e-13
        eta = m.K*S*(S+1)
        width = 2*np.sqrt(eta)
        values, vectors = eigh(H.toarray(), subset_by_value=(-width, width),
                               driver='evr', check_finite=True)
        selected = vectors @ (vectors.conj().T @ psi)
        selected_flat = vectors @ (vectors.conj().T @ flat)
        selected_bright = vectors @ (vectors.conj().T @ bright)
        eigen_residual = float(np.linalg.norm(H @ vectors-vectors*values, ord='fro'))
        assert eigen_residual < 1e-8
        actual_smooth, _, _ = rational_filter(H, psi, smooth_width)
        overlap = np.vdot(actual_smooth, J @ reference)
        smooth_error = np.sqrt(max(0., np.vdot(actual_smooth, actual_smooth).real
                                  + np.vdot(reference, reference).real-2*overlap.real))
        actual_motion = expm_multiply(-1j*H, flat*np.sqrt(2), start=-.4,
                                      stop=.4, num=3, traceA=-1j*H.diagonal().sum())
        motion_rows = []
        for t, actual, ref in zip(times, actual_motion, ref_motion):
            err2 = (np.vdot(actual, actual).real+np.vdot(ref, ref).real
                    - 2*np.vdot(actual, J@ref).real)
            motion_rows.append({'t': float(t), 'state_norm_error': float(np.sqrt(max(0., err2))),
                                'finite_norm_squared': float(np.vdot(actual, actual).real)})
        row = {'S': S, 'eta': eta, 'physical_dimension': len(words),
               'sharp_width': float(width), 'sharp_width_over_eta': float(width/eta),
               'selected_eigenvalue_count': len(values), 'eigen_residual_Frobenius': eigen_residual,
               'accepted_norm_squared': float(np.vdot(selected, selected).real),
               'selected_vector_error_to_F_first_output': float(np.linalg.norm(selected-flat)),
               'selected_bright_norm_squared': float(np.vdot(selected_bright, selected_bright).real),
               'flat_rejection_norm_squared': float(np.linalg.norm(selected_flat-flat)**2),
               'smooth_filter_vector_error_to_reference': float(smooth_error),
               'pure_Hamiltonian_motion': motion_rows, 'elapsed_seconds': time.monotonic()-started}
        rows.append(row)
        print(json.dumps(row), flush=True)
    return {'parameters': {'K': m.K, 'delta': m.delta, 'kappa_in_unitary_control': m.kappa},
            'smooth_filter': 'g(x)=16^2/(x^2+16^2)', 'flat_reference_cut': cut,
            'flat_reference_filter_error_norm_bound': reference_error_bound,
            'flat_reference_filter_bound_scope': 'Analytic truncation bound; floating-point solve and roundoff errors are separate diagnostics, not interval certified.',
            'reference_numerical_interior_resolvent_residual_norms': interior_residuals,
            'reference_numerical_omitted_boundary_residual_norms': residuals,
            'flat_reference_motion_Dyson_tail_norm_bound': motion_tail,
            'sharp_width_sequence': '2 sqrt(eta); this is expanding and subfast asymptotically',
            'rows': rows,
            'limitations': 'Finite sizes corroborate the ring claims; no cube propagation, full filtered finite-spin count process, or convergence rate is inferred.'}


if __name__ == '__main__':
    out = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'reused_sources': SOURCES, 'exact': exact_grams(), 'numerical': numerical_controls()}
    target = D / 'ENERGY_FILTER_RESULTS.json'
    assert not target.exists()
    target.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2), flush=True)
