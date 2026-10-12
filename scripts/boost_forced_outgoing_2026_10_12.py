#!/usr/bin/env python3
"""Finite Pauli, forced ODE and spectral-weight controls; analytic scope is in the note."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/EXCLUDED_WALK_MEMORY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md', 'docs/BOOST_FORCED_OUTGOING_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/EXCLUDED_WALK_BOOST_BRACKET_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-11.md']
if not __debug__:
    raise RuntimeError("Run without -O: control assertions must be enabled")

#!/usr/bin/env python3
"""Author controls by disjoint Pauli compression and inhomogeneous ODE routes.

The finite two-antipodal-pair model is not a torus quadrature. No continuum
absolute continuity, Fourier rate, or original-walk averaging rate is tested.
This helper imports no campaign/source helper. All test inputs are literal.
"""
import sys
import time
import sympy as sp
import numpy as np
import scipy
from scipy.linalg import expm, expm_frechet, eigh
from scipy.integrate import quad_vec

started = time.monotonic()
R = sp.Rational
ii = sp.I
checks = 0


def require(condition, name):
    global checks
    if not condition:
        raise AssertionError(name)
    checks += 1
    print(f"CHECK {name}: matched", flush=True)


def zero(matrix):
    return all(sp.simplify(x) == 0 for x in matrix)


def exact_scalar(x):
    return sp.simplify(sp.expand_complex(x))


pauli = [sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -ii], [ii, 0]]),
         sp.diag(1, -1)]
id2 = sp.eye(2)
p1 = [sp.kronecker_product(p, id2) for p in pauli]
p2 = [sp.kronecker_product(id2, p) for p in pauli]
c = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2)
triplets = sp.Matrix.hstack(*(p * c for p in p1))
spinbasis = sp.Matrix.hstack(c, triplets)
require(zero(spinbasis.H * spinbasis-sp.eye(4)), "orthonormal_actual_Pauli_basis")

# These are exact sines/cosines on two positive nodes. Their negative nodes
# have the opposite triplets and the same singlet; weights sum to one over
# the complete antipodal pairs. The sqrt weights implement the physical norm.
sines = [sp.Matrix([R(3, 5), 0, 0]), sp.Matrix([0, R(5, 13), R(12, 13)])]
cosines = [sp.Matrix([R(4, 5), 1, 1]), sp.Matrix([1, R(12, 13), R(5, 13)])]
weights = [R(1, 2), R(1, 2)]
kappa = sp.Matrix([R(1, 8), -R(1, 12), R(1, 16)])
direction = sp.Matrix([R(1, 16), -R(1, 20), R(1, 21)])
eps = [sp.sqrt(s.dot(s)) for s in sines]
I_fixture = sp.simplify(sum(w/(4*e**2) for w, e in zip(weights, eps)))
require(I_fixture > 0, "finite_fixture_I_positive")
print(f"FINITE_FIXTURE I={I_fixture}; not a continuum value", flush=True)

hblocks, bblocks, bpblocks, fblocks, zblocks = [], [], [], [], []
omegas, coupling_weights = [], []
for s, co, weight, epsilon in zip(sines, cosines, weights, eps):
    n = s/epsilon
    d = sp.Matrix([kappa[j]*co[j] for j in range(3)])
    dd = sp.Matrix([direction[j]*co[j] for j in range(3)])
    hblocks.append(sum(((p1[j]-p2[j])*s[j] for j in range(3)), sp.zeros(4)))
    bblocks.append(sum(((p1[j]+p2[j])*d[j]/2 for j in range(3)), sp.zeros(4)))
    bpblocks.append(sum(((p1[j]+p2[j])*dd[j]/2 for j in range(3)), sp.zeros(4)))
    fblocks.append(triplets*(sp.eye(3)-n*n.T)*triplets.H)
    zblocks.append(sp.sqrt(weight)*triplets*n/(2*epsilon*sp.sqrt(I_fixture)))
    omegas.append(sp.simplify(d.dot(n)))
    coupling_weights.append(sp.simplify(weight*(d.dot(d)-d.dot(n)**2)/(4*epsilon**2*I_fixture)))

H0 = sp.diag(*hblocks)
B = sp.diag(*bblocks)
Bprime = sp.diag(*bpblocks)
F = sp.diag(*fblocks)
zeta = sp.Matrix.vstack(*zblocks)
contact = sp.Matrix.vstack(*(sp.sqrt(weight)*c for weight in weights))
P = sp.eye(8)-contact*contact.H
Pi = F+zeta*zeta.H
Hstar = P*H0*P
require(zero(Pi*Pi-Pi) and zero(Pi.H-Pi), "full_physical_kernel_projection")
require(zero(Hstar*Pi) and zero(contact.H*Pi), "kernel_and_contact_exclusion")
require(sp.simplify((zeta.H*zeta)[0]) == 1, "dressing_normalization")
A = sp.simplify(Pi*B*Pi)
Aprime = sp.simplify(Pi*Bprime*Pi)
D = sp.simplify(F*B*F)
g = sp.simplify(B*zeta)
require(zero(F*g-g) and zero(zeta.H*g), "actual_Pauli_coupling_transverse")
require(zero(A-(D+g*zeta.H+zeta*g.H)), "direct_compression_equals_prior_block")
require(sp.simplify((g.H*g)[0]-sum(coupling_weights)) == 0, "full_measure_coupling_weights")
require(not zero(A*zeta), "source_reaches_transverse_fixture")

# Direct matrix inverse versus independently accumulated helicity bath data.
zvalue = R(2, 5)+ii*R(3, 7)
sigma = sum(weight*zvalue/(zvalue**2-omega**2)
            for weight, omega in zip(coupling_weights, omegas))
schur = 1/(zvalue-sigma)
direct_m = (zeta.H*(zvalue*sp.eye(8)-A).inv()*zeta)[0]
require(sp.simplify(direct_m-schur) == 0, "Schur_against_actual_Pauli_inverse")

# New forced identity: compute Taylor derivatives from an independent ODE
# recurrence, then compare the proposed real-resolvent formula through order 7.
frequencies = [R(7, 5), R(13, 8)]
amplitudes = [R(7, 11), R(4, 11)]
frequency_slopes = [R(1, 11), -R(1, 13)]
amplitude_slopes = [R(1, 9), -R(1, 8)]
require(sum(v*v for v in kappa) < R(1, 16), "fixture_kappa_in_packet_enclosure")
ode_derivative = sp.zeros(8, 1)
forced_resolvents = [(frequency*sp.eye(8)-A).inv().applyfunc(sp.simplify)
                    for frequency in frequencies]
power_a = sp.eye(8)
for order in range(8):
    candidate = sp.zeros(8, 1)
    for frequency, amplitude, resolvent in zip(frequencies, amplitudes, forced_resolvents):
        candidate += amplitude*resolvent*(power_a-(-ii*frequency)**order*sp.eye(8))*zeta
    require(zero(candidate-ode_derivative), f"forced_resolvent_ODE_derivative_{order}")
    source_derivative = sum(amplitude*(-ii*frequency)**order
                            for frequency, amplitude in zip(frequencies, amplitudes))
    ode_derivative = (-ii*A*ode_derivative+ii*source_derivative*zeta).applyfunc(sp.simplify)
    power_a = (-ii*A*power_a).applyfunc(sp.simplify)

# The lower gap constants and radial nonstationarity are checked as exact
# scalar inequalities independently of numerical matrix dynamics.
r, b = sp.symbols("radial radius", positive=True)
lower = 2*(r-b/2)/(r+b/2)
require(sp.simplify(sp.diff(lower, r)-2*b/(r+b/2)**2) == 0,
        "radial_lower_bound_increases_with_radius")
require(sp.simplify(sp.diff(lower, b)+2*r/(r+b/2)**2) == 0,
        "radial_lower_bound_decreases_with_kappa_norm")
require(lower.subs({r:R(5, 8), b:R(1, 4)}) == R(4, 3), "radial_nonstationarity_constant")
require(R(5, 4)-R(1, 4) == 1 and R(3, 2)+2*R(1, 4) == 2,
        "actual_forcing_gap_and_max_denominator")
require(R(1, 4)/2 == R(1, 8) and R(1, 2)/1 == R(1, 2),
        "spectral_reweighting_uniform_constants")

# Supplementary floating cross-check. The explicit formula uses dense expm;
# its comparator integrates the actual time source against an independently
# diagonalized propagator. No torus grid appears in either route.
AA = np.array(A.evalf(), dtype=complex)
AP = np.array(Aprime.evalf(), dtype=complex)
zz = np.array(zeta.evalf(), dtype=complex).reshape(-1)
freq = np.array(frequencies, dtype=float)
amp = np.array(amplitudes, dtype=float)
freqp = np.array(frequency_slopes, dtype=float)
ampp = np.array(amplitude_slopes, dtype=float)
ident = np.eye(8, dtype=complex)


def proposed(duration, theta=0.0):
    current_a = AA+theta*AP
    current_f = freq+theta*freqp
    current_c = amp+theta*ampp
    propagator = expm(-1j*duration*current_a)
    out = np.zeros(8, dtype=complex)
    for fval, aval in zip(current_f, current_c):
        out += aval*np.linalg.solve(fval*ident-current_a,
                                    (propagator-np.exp(-1j*duration*fval)*ident)@zz)
    return out


def direct_time_integral(duration, theta=0.0):
    values, vectors = eigh(AA+theta*AP)
    coeffs = vectors.conj().T@zz
    def integrand(source_time):
        source = np.sum((amp+theta*ampp)*np.exp(-1j*source_time*(freq+theta*freqp)))
        return 1j*source*(vectors@(np.exp(-1j*(duration-source_time)*values)*coeffs))
    return quad_vec(integrand, 0.0, duration, epsabs=2e-12, epsrel=2e-12)[0]


def proposed_derivative(duration):
    propagator, derivative = expm_frechet(-1j*duration*AA, -1j*duration*AP)
    out = np.zeros(8, dtype=complex)
    for fval, aval, fprime, aprime in zip(freq, amp, freqp, ampp):
        inverse = np.linalg.inv(fval*ident-AA)
        inverse_prime = -inverse@(fprime*ident-AP)@inverse
        phase = np.exp(-1j*duration*fval)
        phase_prime = -1j*duration*fprime*phase
        delta = propagator-phase*ident
        out += aprime*inverse@delta@zz + aval*inverse_prime@delta@zz
        out += aval*inverse@(derivative-phase_prime*ident)@zz
    return out


largest_value_error = 0.0
largest_derivative_error = 0.0
for duration in [-3.1, -0.3, 0.0, 0.7, 4.2]:
    err = np.linalg.norm(proposed(duration)-direct_time_integral(duration))
    largest_value_error = max(largest_value_error, float(err))
    require(err < 2e-10, f"finite_direct_Duhamel_t_{duration}")
    step = 2e-4
    derivative_fd = (-direct_time_integral(duration, 2*step)
                     +8*direct_time_integral(duration, step)
                     -8*direct_time_integral(duration, -step)
                     +direct_time_integral(duration, -2*step))/(12*step)
    derr = np.linalg.norm(proposed_derivative(duration)-derivative_fd)
    largest_derivative_error = max(largest_derivative_error, float(derr))
    require(derr < 2e-8, f"all_parameter_factors_t_{duration}")

# Spectral weighting: direct powers/resolvents versus the eigenspace measure.
values, vectors = eigh(AA)
source_coefficients = vectors.conj().T@zz
chi = sum(aval/(fval-values) for aval, fval in zip(amp, freq))
dressed = sum(aval*np.linalg.solve(fval*ident-AA, zz) for aval, fval in zip(amp, freq))
weighted_norm = np.sum(abs(source_coefficients)**2*chi**2)
require(abs(np.vdot(dressed,dressed)-weighted_norm) < 2e-12,
        "dressed_vector_spectral_chi_squared_weight")
require(np.linalg.norm(dressed-zz*np.vdot(zz,dressed)) > 1e-3,
        "resolvent_dressed_vector_not_artificially_scalar")

# An off-spectrum hypothesis cannot simply be removed: at exact resonance
# the true inhomogeneous solution grows linearly, while the resolvent fails.
t = sp.symbols("effective_time", real=True)
resonant_e = R(7, 5)
resonant_solution = ii*t*sp.exp(-ii*resonant_e*t)
require(sp.simplify(ii*sp.diff(resonant_solution,t)
                   -resonant_e*resonant_solution+sp.exp(-ii*resonant_e*t)) == 0,
        "resonant_counterexample_exact_ODE")
require(sp.simplify(sp.conjugate(resonant_solution)*resonant_solution-t**2) == 0,
        "resonant_counterexample_linear_norm")

print(f"FLOAT maximum_Duhamel_error={largest_value_error:.16g}", flush=True)
print(f"FLOAT maximum_parameter_derivative_error={largest_derivative_error:.16g}", flush=True)
print(f"RUNTIME python={sys.version.split()[0]} sympy={sp.__version__} "
      f"numpy={np.__version__} scipy={scipy.__version__}", flush=True)
print(f"TOTAL author_controls={checks}; continuum assertions proved analytically, not numerically", flush=True)
print(f"elapsed_seconds={time.monotonic()-started:.6f}", flush=True)

print("per_element: exact Pauli and Schur identities checked")
print("per_site: checked and not executed — no site-volume convergence inference")
print("per_mode: finite forced ODE, parameter derivatives and spectral-weight identities checked")
print("per_block: physical finite singlet/triplet compression checked")
print("lattice_wide: checked and not executed — continuum absolute continuity and outgoing limits require the written proof")
print("TOTAL: PASS=38 FAIL=0")
print("SCOPE: finite controls; no continuum proof, original-walk rate, physical selection or audit verdict from this runner")
