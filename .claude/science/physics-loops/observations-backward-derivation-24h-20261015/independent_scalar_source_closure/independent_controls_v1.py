"""Independent exact controls; no import of author runner or author formulas.

The equations implemented here follow DERIVATION_BEFORE_CODE.md. Repository
reads below bind the exact sources, not supply numerical/mathematical inputs.
Run with Python -B under the 120-second external observer.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SOURCE_CLOSURE_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SOURCE_CLOSURE_v2.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SOURCE_PLAN_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SOURCE_FROZEN_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/check_scalar_source_closure_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SOURCE_CONTROLS_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SIREN_BRIDGE_v1.md",
]
import hashlib
import json
from pathlib import Path
import sys
import sympy as s

ROOT = Path(__file__).resolve().parents[5]
EXPECTED = [
    "ae27e3d7d819a69c2b15549444415cf9385d87af2e356ecc73a7a374ce9d6754",
    "c27e409e2c953b0a115569138e0b6357f246f8c14809b3c822789bd5869569bd",
    "7accf5f24d12abe6b231b2379e4167d706905ade4928f69573e5202b08039ed0",
    "673b8f30182af5d3927c937fe939d8c89872b95c495b69004ec68a93ff7b8d13",
    "df0f437428fdda2d1b001899f53a2236f5e2056b1a1d33bbb803b9b6e6ddc37e",
    "a6a0d53d65d054293b8bee455e6ef76b8b8cbbb651fb5f2ba77a63f8b335a342",
    "13d8b7b65a1bda41b20c228b54a2b7f9837ff5d875a24588981088f7d2951709",
]

def source_binding():
    return {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
            for p in AUDIT_INPUT_PATHS}

initial = source_binding()
rows = []
details = {}

def ck(name, result, detail=None):
    passed = bool(result)
    rows.append({"name": name, "passed": passed, "detail": detail})
    print(json.dumps({"progress": name, "passed": passed}), file=sys.stderr, flush=True)

def zero(name, expression):
    result = s.trigsimp(s.simplify(expression))
    ck(name, result == 0, str(result))

ck("initial_source_binding", list(initial.values()) == EXPECTED)

# Charge from the point-body action, with general reference normalization.
F, Fs, D, mass, radius, ms = s.symbols("F Fstar D mass radius ms", positive=True)
me = mass * s.sqrt(Fs / F)
phi_F = s.sqrt(Fs * D / 2) / F
beta = s.diff(me, F) / (me * phi_F)
zero("charge_sign_and_magnitude", beta + 1 / s.sqrt(2 * Fs * D))
alpha = s.sqrt(2 * Fs) * beta
zero("weak_dimensionless_charge", alpha + 1 / s.sqrt(D))
GT = 1 / (8 * s.pi * Fs)
a1, a2, m1, m2 = s.symbols("a1 a2 m1 m2", real=True)
q1, q2 = a1 * m1 / s.sqrt(2 * Fs), a2 * m2 / s.sqrt(2 * Fs)
potential = -q1 * q2 * s.exp(-ms * radius) / (4 * s.pi * radius)
zero("exchange_normalization", potential + GT * a1 * a2 * m1 * m2 * s.exp(-ms * radius) / radius)
force = -s.diff(potential, radius)
zero("finite_range_force", force + GT * a1 * a2 * m1 * m2 * (1 + ms * radius) * s.exp(-ms * radius) / radius**2)
ck("potential_force_identification_fails", s.simplify(force + GT * a1 * a2 * m1 * m2 * s.exp(-ms * radius) / radius**2) != 0)

# Gaussian radial/angular separation, independent of the author's quadrature.
X = s.symbols("X0:3", real=True)
dv = s.Matrix(s.symbols("d0:3", real=True))
s00, s11, s22, s01, s02, s12 = s.symbols("s00 s11 s22 s01 s02 s12", real=True)
S = s.Matrix([[s00, s01, s02], [s01, s11, s12], [s02, s12, s22]])
xv = s.Matrix(X)

def gaussian(expr):
    total = 0
    for powers, coefficient in s.Poly(s.expand(expr), *X).terms():
        term = coefficient
        for power in powers:
            if power % 2:
                term = 0
                break
            if power:
                term *= s.factorial2(power - 1) / 2**(power // 2)
        total += term
    return s.expand(total)

r2 = gaussian(xv.dot(xv))
r4 = gaussian(xv.dot(xv)**2)
zero("Gaussian_radial_second_moment", r2 - s.Rational(3, 2))
zero("Gaussian_radial_fourth_moment", r4 - s.Rational(15, 4))
angular_dip = gaussian(xv.dot(dv)**2) / r2
angular_quad = gaussian((xv.dot(S * xv))**2) / r4
zero("Gaussian_dipole_tensor", angular_dip - dv.dot(dv) / 3)
zero("Gaussian_quadrupole_tensor", angular_quad - (s.trace(S)**2 + 2 * s.trace(S * S)) / 15)
zero("odd_multipole_interference_vanishes", gaussian(xv.dot(dv) * xv.dot(S * xv)))
Pdip = 4 * s.pi * angular_dip / (16 * s.pi**2)
Pquad = 4 * s.pi * angular_quad / (64 * s.pi**2)
zero("dipole_flux_normalization", Pdip - dv.dot(dv) / (12 * s.pi))
zero("quadrupole_full_trace_formula", Pquad - (s.trace(S)**2 + 2 * s.trace(S * S)) / (240 * s.pi))
St = S - s.eye(3) * s.trace(S) / 3
zero("quadrupole_STF_plus_trace", Pquad - s.trace(St * St) / (120 * s.pi) - s.trace(S)**2 / (144 * s.pi))
ck("varying_trace_is_not_zero_flux", Pquad.subs({s00: 1, s11: 1, s22: 1, s01: 0, s02: 0, s12: 0}) == 1 / (16 * s.pi))

# Circular moment calculation at general phase, rather than evaluating t=0.
mu, sep, Om, time = s.symbols("mu sep Om time", positive=True)
da, aq, G = s.symbols("delta_alpha alpha_Q G", real=True)
rv = s.Matrix([sep * s.cos(Om * time), sep * s.sin(Om * time), 0])
I = mu * (rv * rv.T - s.eye(3) * sep**2 / 3)
I3 = I.diff(time, 3)
Inorm = s.trigsimp(sum(entry**2 for entry in I3))
zero("tensor_circular_norm_all_phases", Inorm - 32 * mu**2 * sep**4 * Om**6)
D2norm = 4 * s.pi * G * mu**2 * da**2 * rv.diff(time, 2).dot(rv.diff(time, 2))
tensor = G * Inorm / 5
zero("dipole_fraction_5_over_96", D2norm / (12 * s.pi) / tensor - s.Rational(5, 96) * da**2 / (sep * Om)**2)
zero("quadrupole_fraction_1_over_6", 4 * s.pi * G * aq**2 * Inorm / (120 * s.pi) / tensor - aq**2 / 6)
M = m1 + m2
mu12 = m1 * m2 / M
zero("COM_dipole_moment", a1 * m1 * m2 / M - a2 * m2 * m1 / M - mu12 * (a1 - a2))
zero("COM_quadrupole_moment", a1 * m1 * (m2 / M)**2 + a2 * m2 * (m1 / M)**2 - mu12 * (a1 * m2 + a2 * m1) / M)
zero("equal_charge_quadrupole_survives", (aq**2 / 6).subs(aq, -1 / s.sqrt(D)) - 1 / (6 * D))

# Varying Z(F) scalar equation plus the metric trace; eliminate R directly.
omega, omega_F, boxF, kinetic, traceT, pot, pot_F = s.symbols("omega omega_F boxF kinetic traceT pot pot_F", real=True)
Z = omega / F
Z_F = omega_F / F - omega / F**2
Rtrace = (-traceT + Z * kinetic + 4 * pot + 3 * boxF) / F
scalar_times_2F = F * Rtrace + 2 * F * Z * boxF + F * Z_F * kinetic - 2 * F * pot_F
zero("trace_scalar_elimination", scalar_times_2F - ((2 * omega + 3) * boxF - traceT - 2 * F * pot_F + 4 * pot + omega_F * kinetic))
V = s.Function("V")(F)
Df = s.Function("D")(F)
U = Fs**2 * V / F**2
canonical_derivative = lambda expr: s.diff(expr, F) * F * s.sqrt(2 / (Fs * Df))
Upp = canonical_derivative(canonical_derivative(U))
mJ2 = 2 * (F * s.diff(V, F, 2) - s.diff(V, F)) / Df
off = -Fs * (s.diff(V, F) - 2 * V / F) * (4 / (F * Df) + s.diff(Df, F) / Df**2)
zero("off_equilibrium_frame_mass_identity", Upp - Fs / F * mJ2 - off)
zero("equilibrium_frame_mass_conversion", (Upp - Fs / F * mJ2).subs(s.diff(V, F), 2 * V / F))
zero("trace_linearization_mass", s.diff(2 * F * s.diff(V, F) - 4 * V, F) / Df - mJ2)
ck("off_equilibrium_mass_equality_is_not_identity", s.simplify(off) != 0)

# An alternative analytic W family and arbitrary normalization, all exact.
u, C, x0, w0, coef, F0, L = s.symbols("u C x0 w0 coef F0 L", positive=True)
W = w0 * s.exp(u) + coef * (s.cosh(u) - 1)
Fof = C * s.exp(x0 + u)
Vof = Fof * W
dF = lambda expr: s.diff(expr, u) / Fof
zero("alternative_W_equilibrium", (Fof * dF(Vof) - 2 * Vof).subs(u, 0))
mass2 = 2 * (Fof * dF(dF(Vof)) - dF(Vof)) / D
zero("alternative_W_mass", mass2.subs(u, 0) - 2 * coef / D)
zero("alternative_W_C_independence", s.diff(mass2.subs(u, 0), C))
Wany = s.Function("W")(u)
Vany = Fof * Wany
zero("general_W_vacuum", (Fof * dF(Vany) - 2 * Vany) / Fof - (s.diff(Wany, u) - Wany))
zero("general_W_mass", 2 * (Fof * dF(dF(Vany)) - dF(Vany)) / D - 2 * (s.diff(Wany, u, 2) - Wany) / D)

# Massive Klein-Gordon field current: phasor current, without phase quadrature.
nu, kval, amp, kap, rad = s.symbols("nu k amp kappa rad", positive=True)
# -<phi_t phi_r> = -1/2 Re[(-i nu A)(i k A)*].
out_current = -s.re((-s.I * nu * amp) * s.conjugate(s.I * kval * amp)) / 2
zero("outgoing_KG_flux_current", out_current - nu * kval * amp**2 / 2)
evan_current = -s.re((-s.I * nu * amp) * s.conjugate(-kap * amp)) / 2
zero("evanescent_KG_flux_current", evan_current)
for ell in (0, 1, 2, 3):
    ratio = (out_current * kval**(2 * ell)) / (out_current * kval**(2 * ell)).subs(kval, nu)
    zero(f"multipole_threshold_power_l{ell}", ratio - (kval / nu)**(2 * ell + 1))
    zero(f"multipole_threshold_limit_l{ell}", s.limit(ratio, kval, 0, dir="+"))
    zero(f"multipole_massless_limit_l{ell}", ratio.subs(kval, nu) - 1)
ck("threshold_energy_not_massless_shortcut", s.simplify(nu**2 * amp**2 / 2 - out_current) != 0)
threshold_examples = []
for value in (s.Rational(0), s.Rational(3, 5), s.Rational(1), s.Rational(3, 2), s.Rational(2), s.Rational(5, 2)):
    chi1 = 0 if value >= 1 else (1 - value**2)**s.Rational(3, 2)
    chi2 = 0 if value >= 2 else (1 - value**2 / 4)**s.Rational(5, 2)
    ck(f"threshold_ordering_{value}", 0 <= chi1 <= chi2 <= 1)
    if 1 <= value < 2:
        ck(f"quadrupole_open_after_dipole_closes_{value}", chi1 == 0 and chi2 > 0)
    threshold_examples.append({"ms_over_Om": str(value), "dipole": str(chi1), "quadrupole": str(chi2)})
details["threshold_examples"] = threshold_examples

# First-order conformal multiplication gives the two Jordan potentials.
eps, A2, y = s.symbols("eps A2 y", real=True)
g00J = s.series((-1 + 2 * eps) / (1 + 2 * eps * A2 * y), eps, 0, 2).removeO()
giiJ = s.series((1 + 2 * eps) / (1 + 2 * eps * A2 * y), eps, 0, 2).removeO()
zero("Jordan_time_potential", g00J + 1 - 2 * eps * (1 + A2 * y))
zero("Jordan_spatial_potential", giiJ - 1 - 2 * eps * (1 - A2 * y))
gam = (1 - A2) / (1 + A2)
zero("PPN_charge_inverse", (1 - gam) / (1 + gam) - A2)
zero("PPN_omega_identity", gam.subs(A2, 1 / D) - (D - 1) / (D + 1))

# Concrete equal-conservative-product counterexample, rational masses/speed.
product = s.Rational(1, 9)
speed = s.Rational(1, 10)
charge_examples = []
for aa in (s.Rational(1, 3), s.Rational(2, 3), s.Rational(1)):
    bb = product / aa
    alphaQ = (2 * aa + bb) / 3  # m1=1, m2=2.
    etaD = s.Rational(5, 96) * (aa - bb)**2 / speed**2
    etaQ = alphaQ**2 / 6
    ck(f"fixed_product_{aa}", aa * bb == product)
    charge_examples.append({"a1": str(aa), "a2": str(bb), "etaD": str(etaD), "etaQ": str(etaQ), "total": str(etaD + etaQ)})
ck("same_product_different_scalar_losses", len({x["total"] for x in charge_examples}) == 3)
details["effective_charge_counterexamples"] = charge_examples
rho, chi, K, distance, freq = s.symbols("rho chi K distance freq", positive=True)
eta = chi / (6 * D)
H = 4 * K * freq**s.Rational(2, 3) * s.sqrt(rho) / distance
fdot = s.Rational(96, 5) * K * freq**s.Rational(11, 3) * (1 + eta)
dc = s.Rational(5, 24) * fdot / (H * freq**3)
zero("dependent_siren_substitution_only", dc / distance - (1 + chi / (6 * D)) / s.sqrt(rho))

# The curved-vacuum counterexample: derive the AdS4 radial KG operator.
# Metric L^2 sec^2(q)[-dt^2+dq^2+sin^2(q)dOmega^2].
q, omegaMode, massSquared, ell = s.symbols("q omegaMode massSquared ell", real=True)
psi = s.Function("psi")(q)
profile = psi / s.tan(q)
radial_box = s.cos(q)**4 / (L**2 * s.sin(q)**2) * s.diff(s.tan(q)**2 * s.diff(profile, q), q)
KG = radial_box + s.cos(q)**2 / L**2 * (omegaMode**2 - ell * (ell + 1) / s.sin(q)**2) * profile - massSquared * profile
reduced = KG * L**2 * s.tan(q) / s.cos(q)**2
expected = s.diff(psi, q, 2) + (omegaMode**2 - ell * (ell + 1) / s.sin(q)**2 - (massSquared * L**2 + 2) / s.cos(q)**2) * psi
zero("AdS_reduced_KG_operator", reduced - expected)
ads_operator = ell * (ell + 1) / s.sin(q)**2 + (massSquared * L**2 + 2) / s.cos(q)**2
zero("AdS_negative_mass_operator", ads_operator.subs(massSquared, -2 / L**2) - ell * (ell + 1) / s.sin(q)**2)
zero("AdS_regular_reflecting_mode", expected.subs({ell: 0, massSquared: -2 / L**2, omegaMode: 2, psi: s.sin(2 * q)}).doit())
zero("AdS_mode_center_endpoint", s.sin(2 * q).subs(q, 0))
zero("AdS_mode_boundary_endpoint", s.sin(2 * q).subs(q, s.pi / 2))
Wads = -3 * s.exp(u) / L**2 - D * u**2 / (2 * L**2)
zero("same_action_AdS_vacuum", (s.diff(Wads, u) - Wads).subs(u, 0))
zero("same_action_AdS_mass", (2 * (s.diff(Wads, u, 2) - Wads) / D).subs(u, 0) + 2 / L**2)
zero("same_action_AdS_curvature", 4 * Wads.subs(u, 0) + 12 / L**2)
details["AdS_scope"] = {
    "boundary": "regular center and reflecting fast-falloff branch, psi(0)=psi(pi/2)=0",
    "quadratic_form": "integral(|psi'|^2 + ell(ell+1)csc(q)^2 |psi|^2)dq >= 0 for integer ell>=0",
    "meaning": "negative local scalar mass does not alone prove curved-background scalar instability; no full nonlinear or body realization result",
}

final = source_binding()
ck("final_source_binding_unchanged", final == initial)
result = {
    "kind": "focused independent exact controls, no formal audit status",
    "python": sys.version,
    "sympy": s.__version__,
    "source_binding": initial,
    "final_source_binding": final,
    "summary": {"passed": sum(r["passed"] for r in rows), "failed": sum(not r["passed"] for r in rows)},
    "checks": rows,
    "details": details,
    "empirical_validation": False,
    "not_checked": ["broader siren tensor propagation", "actual compact-body response", "nonlinear stability", "real observations", "actual environment registration"],
}
print(json.dumps(result, indent=2))
assert result["summary"]["failed"] == 0
