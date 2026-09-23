#!/usr/bin/env python3
"""Selective author challenges of annihilator algebra and characteristic ODE.

Full data are written to JSON. Finite checks do not prove the joint limit.
"""
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh_tridiagonal, expm

from rotor_integer_gaussian_positive_square_check_2026_09_16 import periodic_complex, psd_functions

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ROTOR_JOINT_LOCAL_GAUGE_CHARACTERISTIC_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/ROTOR_UNIFORM_COMPACT_FIELD_SOFT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/ROTOR_JOINT_GROUND_ENERGY_OSCILLATOR_DEFECT_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'scripts/rotor_integer_gaussian_positive_square_check_2026_09_16.py')
# Scientific helper: the declared package-local geometry and matrix functions.
# Integrity reads: this source and the helper source for hashes. No external data.

_REPO = Path(__file__).resolve().parents[1]
for _input_path in AUDIT_INPUT_PATHS:
    _input_bytes = (_REPO / _input_path).read_bytes()
    if _input_path.endswith('.md'):
        assert ('claim_id: ' + Path(_input_path).stem.lower()).encode() in _input_bytes

assert "chi'(t)=-(kappa_L/2)t chi(t)+epsilon(t)," in (_REPO / AUDIT_INPUT_PATHS[0]).read_text()

TOL = 2e-8
data = {}
checks = 0


def demand(condition, label):
    global checks
    if not bool(condition):
        raise AssertionError(label)
    checks += 1


def weighted_commutator():
    _, boundary, _ = periodic_complex(3)
    C = boundary.T.astype(float)
    e = np.tile([0.7, 1.1, 1.8], 27)
    b = np.tile([0.9, 1.4, 1.2], 27)
    S = np.sqrt(b)[:, None]*C*np.sqrt(e)[None, :]
    omega, _, _ = psd_functions(S.T@S)
    omega_p, omega_p_inverse, _ = psd_functions(S@S.T)
    M = S.T@omega_p_inverse
    rng = np.random.default_rng(3410)
    theta = rng.normal(scale=0.7, size=81)
    u, v = np.zeros(81), np.zeros(81)
    u[[0, 4, 8]] = [0.71, -0.22, 0.35]
    v[[1, 2, 7]] = [-0.32, 0.64, 0.28]
    xi = u+1j*(M@v)
    v_perp = v-M.T@M@v
    f = (S@u)*(M.T@u)+(omega_p@v)*v-1j*(S@u)*v_perp
    kappa = float(u@omega@u+v@omega_p@v)
    expression = kappa+f@(np.cos(C@theta)-1)
    g = 0.31
    # Differentiate the multiplication coefficients of literal differential
    # operators. The constant derivative-derivative terms commute.
    def z(angle):
        return np.sqrt(b)*np.sin(C@angle)/g
    def a_multiplication(angle):
        return v@z(angle)
    def b_multiplication(angle):
        return -1j*(M.T@xi)@z(angle)
    rows = []
    for h in [0.01, 0.005, 0.0025]:
        direction_b = np.sqrt(e)*xi
        direction_a = np.sqrt(e)*u
        first = -1j*g*(a_multiplication(theta+h*direction_b)
                         -a_multiplication(theta-h*direction_b))/(2*h)
        second = 1j*g*(b_multiplication(theta+h*direction_a)
                         -b_multiplication(theta-h*direction_a))/(2*h)
        direct = first+second
        rows.append(dict(h=h, real=float(direct.real), imaginary=float(direct.imag),
                         error=float(abs(direct-expression))))
    ratios = [rows[j]["error"]/rows[j+1]["error"] for j in range(2)]
    demand(min(ratios)>3.8, "directional derivative converges to weighted commutator")
    extrapolated = (4*complex(rows[-1]["real"], rows[-1]["imaginary"])
                    -complex(rows[-2]["real"], rows[-2]["imaginary"]))/3
    demand(abs(extrapolated-expression)<TOL, "commutator Richardson residual")
    wrong_f = (S@u)*(M.T@u)+(omega_p@v)*v+1j*(S@u)*v_perp
    wrong = kappa+wrong_f@(np.cos(C@theta)-1)
    demand(abs(wrong-expression)>0.001, "perpendicular cross-term sign discriminator")
    # Directly challenge the first-order transport rule. The multiplication
    # phase cancels under conjugation, leaving precisely an angle shift.
    r = 0.8
    displacement = r*g*np.sqrt(e)*u
    shifted_defect = f@(np.cos(C@(theta-displacement))-1)
    change = abs(shifted_defect-f@(np.cos(C@theta)-1))
    lipschitz = np.sum(np.abs(f))*abs(r)*g/np.sqrt(b.min())*np.linalg.norm(S@u)
    demand(change<=lipschitz+TOL, "translated commutator defect bound")
    data["weighted_cubic_commutator"] = dict(L=3, kappa=kappa,
        exact_real=float(expression.real), exact_imaginary=float(expression.imag),
        perpendicular_smear_norm=float(np.linalg.norm(v_perp)),
        directional_rows=rows, convergence_ratios=ratios,
        extrapolation_error=float(abs(extrapolated-expression)),
        wrong_perpendicular_sign_error=float(abs(wrong-expression)),
        translated_defect_change=float(change), lipschitz_bound=float(lipschitz))


def covariance_fourier_bound():
    L, components = 7, 2
    rng = np.random.default_rng(3411)
    raw = rng.normal(size=(L, components, components))+1j*rng.normal(size=(L, components, components))
    blocks = np.einsum("kji,kjl->kil", raw.conj(), raw)
    F = np.exp(-2j*np.pi*np.outer(np.arange(L), np.arange(L))/L)/math.sqrt(L)
    transform = np.kron(F, np.eye(components))
    diagonal = np.zeros((L*components, L*components), complex)
    for k in range(L):
        diagonal[k*components:(k+1)*components, k*components:(k+1)*components] = blocks[k]
    covariance = transform.conj().T@diagonal@transform
    smear = np.zeros((L, components), complex)
    smear[0] = [0.4, -0.7j]
    smear[2] = [-0.2, 0.3]
    value = float(np.vdot(smear.ravel(), covariance@smear.ravel()).real)
    hat = np.fft.fft(smear, axis=0)
    spectral = float(np.einsum("ki,kij,kj->", hat.conj(), blocks, hat).real/L)
    density = float(np.trace(covariance).real/L)
    bound = density*float(np.max(np.sum(np.abs(hat)**2, axis=1)))
    demand(abs(value-spectral)<TOL, "position/Fourier covariance normalization")
    demand(value<=bound+TOL, "Fourier trace bound")
    data["positive_covariance"] = dict(sites=L, direct=value, spectral=spectral,
        trace_density=density, upper=bound)


def one_rotor_ground(g):
    # This fixture is a single compact rotor, not the full charged theory.
    cutoff = math.ceil(11/g)
    n = np.arange(-cutoff, cutoff+1)
    dim = len(n)
    values, vectors = eigh_tridiagonal(g*g*n*n/2+1/g**2,
                                       np.full(dim-1, -0.5/g**2), select="i", select_range=(0, 0))
    psi = vectors[:, 0].astype(complex)
    shift = np.diag(np.ones(dim-1), -1).astype(complex)
    cosine, sine = (shift+shift.conj().T)/2, (shift-shift.conj().T)/(2j)
    P, Z = np.diag(g*n), sine/g
    Q = P-1j*Z
    u, v, t = 0.73, -0.46, 0.8
    A = u*P+v*Z
    B = (u+1j*v)*Q
    kappa = u*u+v*v
    U = expm(1j*t*A)
    chi = np.vdot(psi, U@psi)
    derivative = 1j*np.vdot(psi, A@U@psi)
    commutator = B@A-A@B
    comm_error = float(np.linalg.norm(commutator-kappa*cosine))
    demand(comm_error<TOL, "single rotor commutator including finite shift boundary")
    # This commutator uses only [E,U], which survives the hard boundary;
    # no false U U^*=I identity is used here.
    defect = kappa*(cosine-np.eye(dim))
    annihilator_norm = float(np.linalg.norm(B@psi))
    rho = float(np.vdot(psi, (np.eye(dim)-cosine)@psi).real)
    ode_residual = float(abs(derivative+kappa*t*chi/2))
    # The analytic transported estimate is compared with a literal matrix
    # exponential. Boundary mass must be negligible for rotor identification.
    bound = annihilator_norm+0.5*kappa*(t*math.sqrt(2*rho)+0.5*t*t*g*abs(u))
    demand(ode_residual<=bound+TOL, "characteristic ODE error bound")
    boundary_mass = float(np.sum(np.abs(psi[np.abs(n)>=cutoff-2])**2))
    demand(boundary_mass<1e-20, "ground-state Fourier boundary mass")
    # A finite matrix is sufficient to check the Duhamel identity itself.
    grid = np.linspace(0, t, 81)
    eig, basis = np.linalg.eigh(A)
    coeff = basis.conj().T@psi
    spectral_defect = basis.conj().T@defect@basis
    integrand = []
    for s in grid:
        left = coeff.conj()*np.exp(1j*s*eig)
        right = coeff*np.exp(1j*(t-s)*eig)
        integrand.append(left@spectral_defect@right)
    # Composite Simpson, avoiding a quadrature convention hidden in a library.
    integrand = np.asarray(integrand)
    integral = (grid[1]-grid[0])/3*(integrand[0]+integrand[-1]
                +4*integrand[1:-1:2].sum()+2*integrand[2:-1:2].sum())
    boundary = 0.5j*(np.vdot(psi, U@B@psi)+np.vdot(psi, B.conj().T@U@psi))
    predicted_derivative = -kappa*t*chi/2+boundary-integral/2
    duhamel_error = float(abs(derivative-predicted_derivative))
    demand(duhamel_error<TOL, "direct derivative versus Duhamel/annihilator decomposition")
    return dict(g=g, cutoff=cutoff, ground_energy=float(values[0]),
        plaquette_defect=rho, annihilator_norm=annihilator_norm,
        characteristic_real=float(chi.real), characteristic_imaginary=float(chi.imag),
        gaussian=float(math.exp(-kappa*t*t/4)),
        characteristic_error=float(abs(chi-math.exp(-kappa*t*t/4))),
        commutator_error=comm_error, ode_residual=ode_residual, analytic_ode_upper=bound,
        duhamel_error=duhamel_error, boundary_mass=boundary_mass)


def main():
    weighted_commutator()
    covariance_fourier_bound()
    data["single_rotor_ground_challenge"] = [one_rotor_ground(g) for g in [0.6, 0.4, 0.25, 0.16]]
    data["scope"] = "Author finite algebra and one-rotor challenges, not a charged-volume simulation or independent review."
    data["tolerance"] = TOL
    data["runner_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    dependency = Path(__file__).with_name("rotor_integer_gaussian_positive_square_check_2026_09_16.py")
    data["geometry_helper_sha256"] = hashlib.sha256(dependency.read_bytes()).hexdigest()
    data["checks"] = checks
    Path(__file__).with_suffix(".json").write_text(json.dumps(data, indent=2)+"\n")
    print("Weighted cubic commutator, Fourier normalization, and single-rotor characteristic challenge completed.")
    for row in data["single_rotor_ground_challenge"]:
        print(f"g={row['g']:.2f}: characteristic error={row['characteristic_error']:.6g}, ODE residual={row['ode_residual']:.6g}")
    print('per_element: executed — differentiated commutators, Fourier normalization and Duhamel quadrature')
    print('per_site: executed — 3-cube geometry and seven-site two-component covariance fixture')
    print('per_mode: executed — four single-rotor cutoffs at g=0.6,0.4,0.25,0.16')
    print('per_block: executed — finite weighted matrices, translated defects and rotor exponentials')
    print('lattice_wide: checked and not executed — uniform bounds and joint-limit/time arguments are written proofs; finite fixtures do not execute an infinite lattice')
    print(f"TOTAL: PASS={checks} FAIL=0")


if __name__ == "__main__":
    main()
