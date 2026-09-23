#!/usr/bin/env python3
"""Weyl-product sign and finite zero-mode ambiguity challenges.

These are auxiliary fixtures, not simulations of the full charged model.
"""
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh_tridiagonal, expm

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ROTOR_JOINT_EQUAL_TIME_WEYL_CAR_STATE_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/ROTOR_UNIFORM_COMPACT_FIELD_SOFT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/ROTOR_JOINT_GROUND_ENERGY_OSCILLATOR_DEFECT_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/ROTOR_JOINT_LOCAL_GAUGE_CHARACTERISTIC_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-16.md')
# Literal proof inputs are read below; the source self-hash is an integrity read.

_REPO = Path(__file__).resolve().parents[1]
for _input_path in AUDIT_INPUT_PATHS:
    _input_bytes = (_REPO / _input_path).read_bytes()
    if _input_path.endswith('.md'):
        assert ('claim_id: ' + Path(_input_path).stem.lower()).encode() in _input_bytes

assert 'sigma(G B)=sigma(G) omega_F(B).' in (_REPO / AUDIT_INPUT_PATHS[0]).read_text()

TOL = 2e-8
checks = 0
report = {}


def demand(condition, label):
    global checks
    if not bool(condition):
        raise AssertionError(label)
    checks += 1


def weyl_fixture(g):
    cutoff = math.ceil(11/g)
    n = np.arange(-cutoff, cutoff+1)
    dim = len(n)
    _, vectors = eigh_tridiagonal(g*g*n*n/2+1/g**2,
                                  np.full(dim-1, -0.5/g**2), select="i", select_range=(0, 0))
    psi = vectors[:, 0].astype(complex)
    shift = np.diag(np.ones(dim-1), -1).astype(complex)
    cosine, sine = (shift+shift.conj().T)/2, (shift-shift.conj().T)/(2j)
    P, Z = np.diag(g*n), sine/g
    u, v, up, vp = 0.7, 0.2, -0.3, 0.8
    u3, v3 = 0.4, -0.1
    W = lambda x, y: expm(1j*(x*P+y*Z))
    left = W(u, v)@W(up, vp)
    sigma = u*vp-up*v
    right = np.exp(0.5j*sigma)*W(u+up, v+vp)
    wrong = np.exp(-0.5j*sigma)*W(u+up, v+vp)
    rho = float(np.vdot(psi, (np.eye(dim)-cosine)@psi).real)
    remainder_coefficient = (abs(v)*u*u/6
        +abs(vp)*(u*u+u*up+up*up/3)/2
        +abs(v+vp)*(u+up)**2/6)
    root_error = float(np.linalg.norm((left-right)@psi))
    root_bound = abs(sigma)/2*(math.sqrt(2*rho)+g*abs(u+up))+g*remainder_coefficient
    demand(root_error<=root_bound+TOL, "Weyl ground-vector bound")
    excited = W(u3, v3)@shift@psi
    excited_error = float(np.linalg.norm((left-right)@excited))
    excited_bound = abs(sigma)/2*(math.sqrt(2*rho)+g*abs(u+up+u3))+g*remainder_coefficient
    demand(excited_error<=excited_bound+TOL, "Weyl bound after field and integer-charge excitation")
    wrong_error = float(np.linalg.norm((left-wrong)@psi))
    demand(wrong_error>0.4, "wrong Weyl phase fails")
    boundary = float(np.sum(np.abs(psi[np.abs(n)>=cutoff-2])**2))
    demand(boundary<1e-20, "negligible ground Fourier boundary")
    excited_boundary = float(np.sum(np.abs(excited[np.abs(n)>=cutoff-2])**2))
    demand(excited_boundary<1e-18, "negligible excited Fourier boundary")
    return dict(g=g, cutoff=cutoff, sigma=sigma, compact_defect=rho,
        root_error=root_error, root_upper=root_bound,
        excited_error=excited_error, excited_upper=excited_bound,
        wrong_sign_error=wrong_error, boundary_mass=boundary,
        excited_boundary_mass=excited_boundary)


def zero_mode_fixture(L):
    # A one-dimensional two-band auxiliary symbol has finitely many zero
    # momenta. It is used to expose why finite-volume uniqueness is not assumed.
    k = 2*np.pi*np.arange(L)/L
    energy = np.sin(k)
    zero = np.abs(energy)<1e-12
    h = np.zeros((L, 2, 2))
    h[:, 0, 0], h[:, 1, 1] = energy, -energy
    first, second = np.zeros_like(h), np.zeros_like(h)
    for j in range(L):
        if zero[j]:
            first[j, 0, 0], second[j, 1, 1] = 1, 1
        else:
            band = 0 if energy[j]<0 else 1
            first[j, band, band] = second[j, band, band] = 1
    e1, e2 = np.einsum("kij,kji->", h, first), np.einsum("kij,kji->", h, second)
    minimum = -np.abs(energy).sum()
    demand(abs(e1-minimum)<TOL and abs(e2-minimum)<TOL, "distinct exact free finite-volume minima")
    demand(abs(np.trace(first, axis1=1, axis2=2).sum()-L)<TOL, "half filling first zero-mode choice")
    demand(abs(np.trace(second, axis1=1, axis2=2).sum()-L)<TOL, "half filling second zero-mode choice")
    F = np.exp(-2j*np.pi*np.outer(np.arange(L), np.arange(L))/L)/math.sqrt(L)
    transform = np.kron(F, np.eye(2))
    def position(symbol):
        diagonal = np.zeros((2*L, 2*L), complex)
        for j in range(L):
            diagonal[2*j:2*j+2, 2*j:2*j+2] = symbol[j]
        return transform.conj().T@diagonal@transform
    c1, c2 = position(first), position(second)
    demand(np.linalg.norm(c1@c1-c1)<TOL and np.linalg.norm(c2@c2-c2)<TOL, "both filled-band covariances are projections")
    local_difference = float(np.linalg.norm((c1-c2)[:2, :2], 2))
    spectral_difference = float(np.linalg.norm(c1-c2, 2))
    demand(abs(local_difference-zero.sum()/L)<TOL, "zero-mode local ambiguity shrinks as zero-count over volume")
    demand(abs(spectral_difference-1)<TOL, "global zero-mode ambiguity does not shrink in operator norm")
    return dict(L=L, zero_momenta=int(zero.sum()), common_ground_energy=float(minimum),
        local_covariance_difference=local_difference,
        full_covariance_operator_difference=spectral_difference)


def nonprojection_discriminator():
    # Same nonprojection covariance does not determine four-point functions.
    # Basis: vacuum, second occupied, first occupied, both occupied.
    n1, n2 = np.diag([0, 0, 1, 1]), np.diag([0, 1, 0, 1])
    correlated = np.diag([0.5, 0, 0, 0.5])
    independent = np.eye(4)/4
    first = [float(np.trace(state@n)) for state in [correlated, independent] for n in [n1, n2]]
    pair = [float(np.trace(state@n1@n2)) for state in [correlated, independent]]
    demand(max(abs(x-0.5) for x in first)<TOL, "nonprojection covariances agree")
    demand(abs(pair[0]-pair[1])>0.2, "higher correlations differ without the projection premise")
    return dict(single_occupations=first, double_occupations=pair)


def main():
    report["compact_weyl_products"] = [weyl_fixture(g) for g in [0.6, 0.4, 0.25, 0.16]]
    report["finite_zero_mode_ambiguity"] = [zero_mode_fixture(L) for L in [8, 16, 32, 64]]
    report["projection_premise_discriminator"] = nonprojection_discriminator()
    report["scope"] = "Author auxiliary fixtures for Weyl signs and matter-state hypotheses; no interacting phase computation."
    report["tolerance"] = TOL
    report["runner_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report["checks"] = checks
    (_REPO / 'logs/runner-cache/rotor_joint_weyl_car_state_check_2026_09_16.json').write_text(json.dumps(report, indent=2)+"\n")
    for row in report["compact_weyl_products"]:
        print(f"g={row['g']:.2f}: Weyl error={row['root_error']:.6g}, wrong-sign error={row['wrong_sign_error']:.6g}")
    for row in report["finite_zero_mode_ambiguity"]:
        print(f"L={row['L']}: local zero-mode ambiguity={row['local_covariance_difference']:.6g}, global norm={row['full_covariance_operator_difference']:.6g}")
    print('per_element: executed — Weyl signs and nonprojection covariance discriminator')
    print('per_site: executed — local versus global covariance on finite rings L=8,16,32,64')
    print('per_mode: executed — single-rotor Fourier cutoffs and exact auxiliary zero momenta')
    print('per_block: executed — ground and excited rotor vectors, two-band and four-state fixtures')
    print('lattice_wide: checked and not executed — uniform bounds and joint-limit/time arguments are written proofs; finite fixtures do not execute an infinite lattice')
    print(f"TOTAL: PASS={checks} FAIL=0")


if __name__ == "__main__":
    main()
