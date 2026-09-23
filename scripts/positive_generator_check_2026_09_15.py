"""Bounded checks of the full-cone argument and the signed-stencil escape."""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/POSITIVE_ELECTRIC_GENERATOR_CONE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/FINITE_GRAPH_CYCLIC_WEAK_COUPLING_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'positive_electric_generator_cone_bounds_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/POSITIVE_ELECTRIC_GENERATOR_CONE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/positive_generator_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
import json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.linalg import eigh, expm

HERE = Path(__file__).resolve().parent
RNG = np.random.default_rng(18160915)


def generator(n, gamma):
    h = np.zeros((n, n))
    for j, coefficient in enumerate(gamma, 1):
        h += coefficient*np.eye(n)
        for q in range(n):
            h[(q+j) % n, q] -= coefficient/2
            h[(q-j) % n, q] -= coefficient/2
    return h


def continuum(ell, improved, modes):
    k = np.arange(-modes, modes+1)
    h = np.diag(2*np.pi**2*k*k/ell**2)
    if improved:
        h += np.eye(len(k))*5*ell**2/(4*np.pi**2)
        off1, off2 = -2*ell**2/(3*np.pi**2), ell**2/(24*np.pi**2)
    else:
        h += np.eye(len(k))*ell**2/np.pi**2
        off1, off2 = -ell**2/(2*np.pi**2), 0
    h += np.diag(np.full(len(k)-1, off1), 1)+np.diag(np.full(len(k)-1, off1), -1)
    h += np.diag(np.full(len(k)-2, off2), 2)+np.diag(np.full(len(k)-2, off2), -2)
    es, vs = eigh(h, subset_by_index=(0, 2))
    residual = np.linalg.norm(h @ vs[:, 0]-es[0]*vs[:, 0])
    assert residual < 1e-8
    return es, residual


def main():
    theta = sp.symbols('theta', real=True)
    f = sp.Rational(4, 3)*(1-sp.cos(theta))-sp.Rational(1, 12)*(1-sp.cos(2*theta))
    derivative_identity = sp.trigsimp(1-sp.diff(f, theta, 2)-sp.Rational(2, 3)*(1-sp.cos(theta))**2)
    assert derivative_identity == 0
    assert sp.expand(sp.series(f, theta, 0, 8).removeO()) == theta**2/2-theta**6/180
    xx = sp.symbols('x', real=True)
    moment6 = sp.simplify(sp.sqrt(2/sp.pi)*sp.integrate(xx**6*sp.exp(-2*xx**2), (xx, -sp.oo, sp.oo)))
    coefficient = sp.simplify(sp.Rational(16, 45)*sp.pi**4*moment6)
    assert coefficient == sp.pi**4/12
    positive, signed = [], []
    for n in [5, 7, 9, 15, 31]:
        s = n//2; jumps = np.arange(1, s+1)
        theta_grid = 2*np.pi*np.arange(n)/n
        # Dense positive weights cover every allowed jump; the theorem itself
        # is analytic and does not rely on these deterministic random draws.
        for fixture in range(3):
            raw = RNG.uniform(.05, 1, s)
            gamma = raw/np.dot(raw, jumps*jumps)
            h = generator(n, gamma)
            symbol = np.sum(gamma[:, None]*(1-np.cos(jumps[:, None]*theta_grid)), axis=0)
            envelope = 1-np.cos(theta_grid)
            assert np.max(symbol-envelope) < 1e-13
            fourier = np.exp(2j*np.pi*np.arange(n)[:, None]*np.arange(n)[None, :]/n)/np.sqrt(n)
            symbol_error = float(np.max(abs(fourier.conj().T @ h @ fourier-np.diag(symbol))))
            assert symbol_error < 2e-13
            kernels = []
            for time in [1e-5, .1, 3.]:
                heat = expm(-time*h)
                assert heat.min() >= -1e-13
                assert np.max(abs(heat.sum(axis=0)-1)) < 2e-13
                kernels.append(dict(time=time, minimum=float(heat.min())))
            positive.append(dict(N=n, fixture=fixture, curvature=float(np.dot(gamma, jumps*jumps)),
                                 fourth_moment=float(np.dot(gamma, jumps**4)),
                                 minimum_nonzero_envelope_margin=float(min(envelope[1:]-symbol[1:])),
                                 symbol_matrix_error=symbol_error, heat_kernels=kernels))
        gamma = np.zeros(s); gamma[0] = 4/3; gamma[1] = -1/12
        h = generator(n, gamma)
        symbol = (1-np.cos(theta_grid))+(1-np.cos(theta_grid))**2/6
        assert np.min(np.linalg.eigvalsh(h)) > -2e-13
        assert abs(h[2, 0]-1/24) < 1e-15
        time = 1e-5
        heat = expm(-time*h)
        closed_product = heat[2, 0]*heat[1, 2]*heat[0, 1]
        assert heat[2, 0] < 0 and heat[1, 2] > 0 and heat[0, 1] > 0
        assert closed_product < 0
        assert abs(heat[2, 0]/time+1/24) < 4e-6
        signed.append(dict(N=n, minimum_energy=float(min(np.linalg.eigvalsh(h))),
                           smallest_symbol=float(min(symbol)), phase_H_20=float(h[2, 0]),
                           time=time, heat_20=float(heat[2, 0]),
                           closed_history_product=float(closed_product)))
    spectra = []
    for ell in [2., 4., 8., 16., 24.]:
        nn, _ = continuum(ell, False, 90)
        imp, residual = continuum(ell, True, 90)
        refined, _ = continuum(ell, True, 130)
        error = float(max(abs(imp-refined)))
        assert error < 2e-9
        assert nn[0] <= imp[0]+1e-10 and imp[0] < 1
        spectra.append(dict(ell=ell, nearest_ground=float(nn[0]), improved_ground=float(imp[0]),
                            nearest_scaled_error=float((1-nn[0])*ell**2),
                            improved_scaled_error=float((1-imp[0])*ell**4),
                            improved_asymptotic_coefficient=float(np.pi**4/12),
                            refinement_error=error, residual=float(residual)))
    result = dict(status='personal_finite_checks_pass_no_independent_audit',
                  exact_symbol_series=str(sp.series(f, theta, 0, 8)),
                  exact_sixth_moment=str(moment6), exact_spectral_coefficient=str(coefficient),
                  positive_generators=positive, signed_improvement=signed,
                  periodic_spectral_comparison=spectra,
                  limits=['Single-link translation-invariant all-time phase positivity only.',
                          'A negative local-history weight is not an invalid Hamiltonian.',
                          'No unrestricted positive representation or photon no-go.',
                          'Continuum spectral error is not a joint finite-g,N rate.'])
    out = json.dumps(result, indent=2)
    _OUTPUT_JSON.write_text(out+'\n')
    print(out)


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: cyclic jump rates and signed-stencil moments')
    print('per_site: finite one-link generator fixtures')
    print('per_mode: finite clock-mode spectra and oscillator comparisons in the specified cone')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
