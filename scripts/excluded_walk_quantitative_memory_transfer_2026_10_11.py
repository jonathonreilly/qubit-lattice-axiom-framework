#!/usr/bin/env python3
"""Literal author consistency controls for quantitative memory transfer.

Three complete frozen helpers execute in separate global namespaces. This
replay checks their exact finite algebra and explicitly floating comparators;
it is not independent proof of the continuum or final publication review.
Runtime dependencies: SymPy and mpmath. No helper file is read or imported.
"""
import hashlib
import json
import platform
import time

AUDIT_TIMEOUT_SEC = 180
CLAIM_ID = "excluded_walk_quantitative_memory_transfer_bounded_theorem_note_2026-10-11"
AUDIT_INPUT_PATHS = [
    "docs/EXCLUDED_WALK_QUANTITATIVE_MEMORY_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-11.md",
    "docs/EXCLUDED_WALK_MEMORY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md",
    "docs/EXCLUDED_WALK_PROJECTED_FREE_BAND_CANONICAL_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md",
    "docs/EXCLUDED_WALK_LOW_ENERGY_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md",
]

EDGE_CONTROLS_SOURCE = r'''"""Exact author controls for the spectral-edge proof.

The finite cubic orbit checks compression and spectral-projection algebra;
it is not quadrature certification of the continuum spectral measure.
No earlier runner is imported. Runtime dependency: SymPy.
"""
import json
import platform
import time

import sympy as sp


began = time.monotonic()
checks = 0


def zero(value):
    entries = list(value) if isinstance(value, sp.MatrixBase) else [value]
    return all(sp.simplify(x) == 0 for x in entries)


def check(name, condition, detail=None):
    global checks
    assert bool(condition), name
    checks += 1
    print(json.dumps({"check": name, "detail": detail}, sort_keys=True))


def cross(v):
    x, y, z = v
    return sp.Matrix([[0, -z, y], [z, 0, -x], [-y, x, 0]])


# Three antipodal pairs q=+/-arcsin(3/5)e_j, each pair weight 1/3.
# Odd fields are represented by their positive member divided by sqrt(3).
# This is an exact finite model with I0_fixture=25/36, not an estimate of
# the continuum I0. Both signs of each q pair are included by odd parity.
sine, cosine = sp.Rational(3, 5), sp.Rational(4, 5)
axes = [sp.eye(3)[:, j] for j in range(3)]
I0_fixture = 1 / (4 * sine**2)
F = sp.diag(*[sp.eye(3) - e*e.T for e in axes])
zeta = sp.Matrix.vstack(*axes) / sp.sqrt(3)
Pz = zeta * zeta.H
Pi = F + Pz
identity = sp.eye(9)
check("physical_zero_projection",
      zero(Pi*Pi-Pi) and zero(Pi-Pi.H) and Pi.rank() == 7
      and zero((zeta.H*zeta)[0]-1) and zero(F*zeta),
      {"rank": Pi.rank(), "I0_fixture": str(I0_fixture)})


def build(kappa):
    b2 = (kappa.T*kappa)[0]
    ds = []
    for j in range(3):
        dj = kappa.copy()
        dj[j] *= cosine
        ds.append(dj)
    B = sp.diag(*[sp.I*cross(dj) for dj in ds])
    W = sp.diag(*[sine**2*kappa[j]**2*sp.eye(3) for j in range(3)])
    dd = sp.diag(*[dj*dj.T for dj in ds])
    A = Pi*B*Pi
    c = b2/(12*I0_fixture)
    return b2, B, W, dd, A, c


kappa = sp.Matrix([sp.Rational(2, 3), -sp.Rational(3, 7), sp.Rational(5, 4)])
b2, B, W, dd, A, c = build(kappa)
check("pointwise_cross_square_defect", zero(b2*identity-B*B-W-dd))
check("bounded_compression_is_selfadjoint", zero(A-A.H))
compression_defect = Pi*B*(identity-Pi)*B*Pi
check("compression_square_keeps_positive_defect",
      zero(Pi*B*B*Pi-A*A-compression_defect)
      and not zero(compression_defect))
check("scalar_weight_preserves_transverse_longitudinal_orthogonality",
      zero(F*W*Pz) and zero(Pz*W*F))
check("exact_cubic_dressing_coefficient", zero((zeta.H*W*zeta)[0]-c))
C = b2*Pi-A*A
check("rank_one_defect_gram_identity",
      zero(C-c*Pz-(F*W*F+Pi*dd*Pi+compression_defect)))
raw = sp.Matrix([sp.Rational(j+1, 11)+sp.I*sp.Rational((-1)**j, 13) for j in range(9)])
psi = Pi*raw
alpha = (zeta.H*psi)[0]
u = F*psi
check("actual_weighted_vector_decomposition",
      zero((psi.H*W*psi)[0]-(u.H*W*u)[0]-c*sp.conjugate(alpha)*alpha))
positive_remainder = sp.simplify((psi.H*(C-c*Pz)*psi)[0])
check("nontrivial_form_vector_control", positive_remainder > 0, str(positive_remainder))


# A literal combined two-edge spectral projection in the finite diagonal
# model: positive and negative high eigenvalues are +/-sqrt(66)/5.
# The remaining physical eigenvalues are 0 and +/-4/5.
b2, B, W, dd, A, c = build(sp.ones(3, 1))
C = b2*Pi-A*A
f2, high2 = sp.Rational(16, 25), sp.Rational(66, 25)
Pedge = A*A*(A*A-f2*Pi)/(high2*(high2-f2))
check("combined_edge_projector_is_exact",
      zero(Pedge*Pedge-Pedge) and zero(Pedge-Pedge.H)
      and zero(A*A*Pedge-high2*Pedge) and Pedge.rank() == 2)
edge_mass = sp.simplify((zeta.H*Pedge*zeta)[0])
edge_vector = Pedge*zeta
check("two_edge_mass_and_longitudinal_coefficient",
      edge_mass == sp.Rational(25, 33)
      and zero((edge_vector.H*edge_vector)[0]-edge_mass)
      and zero((zeta.H*edge_vector)[0]-edge_mass), str(edge_mass))
edge_energy = sp.simplify((edge_vector.H*C*edge_vector)[0])
check("projection_uses_squared_overlap",
      zero(edge_energy-(b2-high2)*edge_mass)
      and sp.simplify(edge_energy-c*edge_mass**2) == sp.Rational(8, 121),
      {"c": str(c), "edge_energy": str(edge_energy),
       "rank_one_form": str(c*edge_mass**2)})

# Only this finite fixture is invertible on all of its physical space.
# The continuum proof instead uses a regulator and monotone convergence.
inverse_moment = sp.simplify((zeta.H*(C+identity-Pi).inv()*zeta)[0])
check("finite_inverse_moment_direct_matrix_check",
      inverse_moment == sp.Rational(649, 297) and inverse_moment <= 1/c,
      {"inverse_moment": str(inverse_moment), "bound": str(1/c)})
check("symmetric_measure_removes_odd_inverse_part",
      zero((zeta.H*A*(C+identity-Pi).inv()*zeta)[0]))


# Exact scalar certificate for the Poisson-resolvent edge bound.
x, delta = sp.symbols("x delta", positive=True)
poisson_majorant = delta/(2*x)
positive_difference = delta*(x-delta)**2/(2*x*(x*x+delta*delta))
check("poisson_bound_factor_two",
      zero(poisson_majorant-delta**2/(x*x+delta*delta)-positive_difference))
b = sp.symbols("b", positive=True)
chi = sp.symbols("chi", positive=True)
check("edge_spectral_defect_exact",
      zero((b*b-(b-delta)**2).subs(delta,b*chi)-b*b*(2*chi-chi*chi)))


# Reconstruct the mean-survival optimization from the actual coefficient
# in the inherited E20/E25 density bound, retaining its logarithm.
I0, q = sp.symbols("I0 q", positive=True)
H_coefficient = 256*sp.sqrt(sp.pi*I0)
bound_root = 24*I0*chi + H_coefficient*q*chi**(-sp.Rational(3, 4))
q_at_optimizer = chi**sp.Rational(7, 4)/(8*sp.sqrt(sp.pi/I0))
check("mean_bound_optimizer_stationary",
      zero(sp.diff(bound_root,chi).subs(q,q_at_optimizer)))
check("mean_bound_optimizer_value",
      zero(bound_root.subs(q,q_at_optimizer)-56*I0*chi)
      and 56**2 == 3136)
tau = sp.symbols("tau", positive=True)
L = 1+sp.log(2*tau)
check("optimizer_domain_monotonicity",
      zero(sp.diff(L/tau,tau)+sp.log(2*tau)/tau**2))
universal_domain_certificate = sp.Rational(64)*sp.Rational(22,7)*12*18/(2**16)
check("universal_large_horizon_domain",
      universal_domain_certificate < 1,
      {"tau_at_least": 2**16, "upper_bound_for_Q_at_threshold": str(universal_domain_certificate),
       "elementary_inputs": "pi<22/7, log(2)<1, I0>=1/12; L/tau decreases for tau>=1/2"})

print(json.dumps({"checks": checks, "python": platform.python_version(),
                  "sympy": sp.__version__, "elapsed_seconds": time.monotonic()-began,
                  "scope": "Exact finite compression/projection and scalar proof controls; author evidence, not independent review or continuum quadrature certification."},
                 sort_keys=True))
'''

RATE_CONTROLS_SOURCE = r'''"""Author controls for the L^(5/3) mean-survival estimate.

No prior helper is imported. Exact identities use SymPy. Continuous-density
comparators use 50-digit mpmath arithmetic without certified error bounds.
The parabolic density is an unrelated comparator, not a torus quadrature.
"""
import json
import platform
import time

import mpmath as mp
import sympy as sp


started = time.monotonic()
mp.mp.dps = 50
checks = 0


def check(name, condition, detail=None):
    global checks
    assert bool(condition), name
    checks += 1
    print(json.dumps({"check": name, "detail": detail}, sort_keys=True))


def zero(expr):
    return sp.simplify(expr) == 0


# C has a genuine kernel, but zeta has a finite inverse-form moment.
# The rank-one bound is checked as a Gram identity, not by assigning an
# inverse-moment value. This fixture does not model the entire torus.
eta = sp.symbols("eta", positive=True)
C = sp.Matrix([[1, 1, 0], [1, 2, 0], [0, 0, 0]])
zeta = sp.Matrix([1, 0, 0])
c = sp.Rational(1, 2)
gram = sp.Matrix([[1/sp.sqrt(2), sp.sqrt(2), 0]])
check("singular_C_rank_one_gram_bound",
      C.det() == 0 and C-c*zeta*zeta.T == gram.T*gram)
xeta = (C+eta*sp.eye(3)).inv()*zeta
teta = (zeta.T*xeta)[0]
check("regulated_inverse_form_identity",
      zero((xeta.T*C*xeta)[0]-teta+eta*(xeta.T*xeta)[0])
      and zero(teta-(eta+2)/(eta*eta+3*eta+1)))
check("regulated_bound_and_finite_limit_without_C_inverse",
      zero(1/c-teta-eta*(2*eta+5)/(eta*eta+3*eta+1))
      and sp.limit(teta, eta, 0, dir="+") == 1/c)


# The L^(5/4) kernel mass comes from an actual integral on the whole line.
x, duration = sp.symbols("x duration", positive=True)
kernel_power_integral = 2*(sp.integrate(1, (x, 0, 1/duration))
    +sp.integrate((duration*x)**(-sp.Rational(5, 4)),
                  (x, 1/duration, sp.oo)))
kernel_coefficient = sp.Integer(10)
check("kernel_L5over4_mass_exact", zero(kernel_power_integral-kernel_coefficient/duration),
      str(kernel_power_integral))


# An unrelated absolutely continuous probability law rho=(3/4)(1-E^2)
# on [-1,1]. Compute its Fourier transform and difference density directly.
E, u = sp.symbols("E u", real=True)
rho = sp.Rational(3, 4)*(1-E*E)
amplitude = sp.integrate(rho*sp.cos(duration*E), (E, -1, 1))
amplitude_closed = 3*(sp.sin(duration)-duration*sp.cos(duration))/duration**3
check("parabolic_probability_and_Fourier_transform",
      sp.integrate(rho, (E, -1, 1)) == 1 and zero(amplitude-amplitude_closed)
      and sp.limit(amplitude, duration, 0, dir="+") == 1)
h = sp.factor(sp.integrate(rho.subs(E,u)*rho.subs(E,u-x), (u, x-1, 1)))
check("difference_density_from_actual_convolution",
      zero(2*sp.integrate(h,(x,0,2))-1)
      and zero(h.subs(x,0)-sp.integrate(rho*rho,(E,-1,1))), str(h))
qpoly = sp.cancel((h-h.subs(x,0))/x)
mean_from_sinc = 2*(h.subs(x,0)*sp.Si(2*duration)
    +sp.integrate(qpoly*sp.sin(duration*x),(x,0,2)))/duration
check("one_sided_sinc_mean_has_correct_derivative_and_origin",
      zero(sp.diff(duration*mean_from_sinc,duration)-amplitude_closed**2)
      and sp.limit(mean_from_sinc,duration,0,dir="+") == 1)


# The interpolation uses a weighted first inverse moment. The comparator's
# envelope rho(E) <= (3/4)*(1-|E|)^(-3/2) is elementary on [-1,1].
inverse_moment = sp.integrate(sp.cancel(rho/(1-E*E)), (E,-1,1))
check("parabolic_inverse_moment_direct_integral", inverse_moment == sp.Rational(3,2))
rho_mp = lambda energy: mp.mpf(3)/4*(1-energy*energy)
rho_p_mass = mp.quad(lambda energy: rho_mp(energy)**(mp.mpf(5)/3), [-1,0,1])
interpolation_bound = 2*(mp.mpf(3)/4)**(mp.mpf(2)/3)*mp.mpf(3)/2
check("continuous_density_weighted_moment_interpolation", rho_p_mass < interpolation_bound,
      {"L5over3_power_integral": str(rho_p_mass), "moment_bound": str(interpolation_bound)})

# A nontrivial direct continuous-density check of the special Young bound.
convolution_L5_power = sp.integrate(2*h**5, (x,0,2))
convolution_L5 = mp.mpf(str(sp.N(convolution_L5_power,60)))**(mp.mpf(1)/5)
young_rhs = rho_p_mass**(mp.mpf(6)/5)
check("continuous_convolution_Young_bound", convolution_L5 <= young_rhs,
      {"L5_convolution": str(convolution_L5), "L5over3_density_squared": str(young_rhs),
       "exact_convolution_fifth_power_integral": str(convolution_L5_power)})

# Compare the spectral difference expression with an independently
# integrated time-domain Fourier amplitude; then test the nontrivial bound.
mean_mp = sp.lambdify(duration, mean_from_sinc, "mpmath")
def amplitude_mp(t):
    if abs(t) < mp.mpf("0.0001"):
        return mp.fsum([(-1)**n*3*t**(2*n)/(mp.factorial(2*n+1)*(2*n+3))
                        for n in range(10)])
    return 3*(mp.sin(t)-t*mp.cos(t))/t**3

for horizon in (mp.mpf("0.5"),mp.mpf(2),mp.mpf(12),mp.mpf(80)):
    cutoffs = [mp.mpf(0)] + [mp.pi*n for n in range(1,int(horizon/mp.pi)+1)] + [horizon]
    direct = mp.quad(lambda t: amplitude_mp(t)**2,cutoffs)/horizon
    spectral = mean_mp(horizon)
    estimate = young_rhs*(mp.mpf(int(kernel_coefficient))/horizon)**(mp.mpf(4)/5)
    check("continuous_time_and_difference_mean_T_"+str(horizon),
          abs(direct-spectral)<mp.mpf("1e-35") and spectral <= min(mp.mpf(1),estimate),
          {"direct_time_mean":str(direct),"sinc_mean":str(spectral),"Lp_bound":str(estimate)})


# Homogeneity is checked from the separately derived moment and kernel
# formulas. bT is dimensionless; no fitted horizon or torus I0 is supplied.
I0, b, tau = sp.symbols("I0 b tau", positive=True)
K = 32768*sp.pi*I0
R = 24*I0*K**sp.Rational(2,3)*b**(-sp.Rational(2,3))
from_norms = R**sp.Rational(6,5)*(10/duration)**sp.Rational(4,5)
rate_constant = 24**sp.Rational(6,5)*(327680*sp.pi)**sp.Rational(4,5)*I0**2
check("rate_scaling_and_literal_constant",
      zero(sp.powdenest(from_norms-rate_constant*(b*duration)**(-sp.Rational(4,5)),force=True)))

print(json.dumps({"checks":checks,"python":platform.python_version(),
                  "sympy":sp.__version__,"mpmath":mp.__version__,
                  "elapsed_seconds":time.monotonic()-started,
                  "scope":"Author algebra/continuous-comparator controls; no continuum torus quadrature, independent review, or certified floating error."},sort_keys=True))
'''

OCCUPATION_CONTROLS_SOURCE = r'''"""Exact finite controls for A2-A9; these do not prove the continuum inputs."""
from fractions import Fraction as F
import sympy as s

checks=0
def check(name,condition):
    global checks
    assert bool(condition), name
    checks+=1
    print('EXACT',name)

l=s.symbols('lambda',positive=True)
g=s.symbols('gamma',real=True)
E,A=s.symbols('E A',nonnegative=True)
# Universal interval reductions used by the analytic A2-A3 proof.
check('Jacobian derivative bound at larger endpoint',F(9,4)*F(16,15)**5<4)
check('Jacobian upper bound below two',1+2*F(1,16)**2<2)
check('contact projection coefficient',F(49*2,128*9)<F(1,3))
check('band remainder rational margin',4-F(1,48)-2*F(1,16)**3>0)
# Collinear vectors attain the full squared-norm difference. Omitting the
# quadratic term or half the cross term violates this exact identity.
a=s.Matrix([A,0]);err=s.Matrix([A*E,0])
diff=((a+err).T*(a+err)-a.T*a)[0]
check('full amplitude-sensitive probability difference',s.expand(diff-A*A*(2*E+E*E))==0)
normalized_budget=8*E+4*E**2
check('normalized probability coefficients',s.expand(normalized_budget-4*(2*E+E**2))==0)
comparison_exponent=s.Rational(1,2)-g
survival_exponent=s.Rational(4,5)*g
balance=s.solve(comparison_exponent-survival_exponent,g)[0]
check('allowed balanced gamma',0<balance<s.Rational(1,2))
check('balanced gamma value',balance==s.Rational(5,18))
check('survival and comparison exponents',comparison_exponent.subs(g,balance)==survival_exponent.subs(g,balance)==s.Rational(2,9))
check('physical time clock',3+balance==s.Rational(59,18))
check('packet error faster than leading error',1-balance>comparison_exponent.subs(g,balance))
check('state preparation occupation at initial time',32**2==1024)
# Unequal contact factors must be retained in one global normalization.
weights=[F(1,6),F(1,3),F(1,2)];normsq=[F(9,10),F(4,5),F(7,10)]
N=sum(w*n for w,n in zip(weights,normsq));actual=[w*n/N for w,n in zip(weights,normsq)]
check('single normalization exact probability',sum(actual)==1 and actual!=weights)
values=[F(1,4),F(1,3),F(2,5)];center=F(1,3);bound=max(abs(x-center) for x in values)
check('uniform estimate survives exact weights',abs(sum(w*x for w,x in zip(actual,values))-center)<=bound)
print('Complete exact finite controls:',checks)
'''

AUTHOR_BLOCKS = [
    ('spectral_edge/edge_controls.py', '22bf0002efc0c7f188eaf789e86848f5e02051e37070a61231ed121a5c7999ee', 20, EDGE_CONTROLS_SOURCE),
    ('spectral_edge/rate_controls.py', 'a3b6b61e17b0deaeced2e0d267e47b583cdbe219cd9d0004b89f184405f945a5', 15, RATE_CONTROLS_SOURCE),
    ('averaged_transverse_occupation/occupation_controls.py', 'a81f727a4d2f813e6c58515127fa9836179e24180f90c50224d42bc7368237a1', 14, OCCUPATION_CONTROLS_SOURCE),
]


def main():
    started = time.monotonic()
    total_checks = 0
    for name, expected_sha256, expected_checks, source in AUTHOR_BLOCKS:
        actual = hashlib.sha256(source.encode("utf-8")).hexdigest()
        assert actual == expected_sha256, (name, actual, expected_sha256)
        print(json.dumps({"author_block": name, "sha256": actual, "phase": "begin"}), flush=True)
        namespace = {"__name__": "__main__", "__file__": "<frozen-author:" + name + ">"}
        exec(compile(source, namespace["__file__"], "exec"), namespace, namespace)
        assert namespace["checks"] == expected_checks, (name, namespace["checks"], expected_checks)
        total_checks += namespace["checks"]
        print(json.dumps({"author_block": name, "checks": namespace["checks"], "phase": "complete"}), flush=True)
    print(json.dumps({"status": "PASS", "claim_id": CLAIM_ID,
                      "isolated_author_blocks": len(AUTHOR_BLOCKS), "author_checks": total_checks,
                      "python": platform.python_version(), "elapsed_seconds": time.monotonic()-started,
                      "scope": "author consistency replay; no independent continuum or final publication proof"}), flush=True)


if __name__ == "__main__":
    main()
