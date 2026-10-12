#!/usr/bin/env python3
"""Author diagnostics for the frozen proof; finite tests do not prove it.

Methods: exact sparse Pauli algebra, direct phase-space Gaussian quadrature,
coordinate-space overlap quadrature, actual pullback finite differences,
and exact improper-integral/domain and central-measure calculations.
Mutations are made in full copied sources, not in the comparison data.
"""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/MASSIVE_BOOST_CARRIER_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/INTEGRATED_BOOST_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/MICROSCOPIC_BOOST_FLOW_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/CENTRE_REGULARITY_TO_GEOMETRIC_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/ISOLATED_CENTRE_FILTERING_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    ".claude/science/physics-loops/toe-massive-boost-carrier-20261012/EVIDENCE_MAP.json"
]
if not __debug__:
    raise RuntimeError("Run without -O: finite control assertions must be enabled")

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import sys

import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.integrate import quad
import sympy as sp

# These named implementation choices are the materialized mutation targets.
TRANSLATION_ENERGY_SIGN = -1
KERNEL_FACTOR = 2.0 / math.sqrt(math.pi)
KERNEL_SHIFT_SIGN = -1
FLAT_WEIGHT_COEFFICIENT = 0.5
BOOST_GENERATOR_SCALE = 1.0
MISMATCH_CURRENT_SIGN = 1
REQUIRE_ENERGY_IN_DIFFERENCE_DOMAIN = False
RN_USE_SQUARE_ROOT = True

ROWS = []

def exact(name, got, expected):
    residual = sp.simplify(got - expected)
    ok = residual == 0
    ROWS.append({"name": name, "method": "exact symbolic/rational", "got": str(got),
                 "expected": str(expected), "residual": str(residual), "passed": bool(ok)})

def close(name, got, expected, tolerance):
    error = float(abs(got - expected))
    ROWS.append({"name": name, "method": "numerical", "got": repr(got),
                 "expected": repr(expected), "error": error, "tolerance": tolerance,
                 "passed": bool(math.isfinite(error) and error <= tolerance)})

def pauli_mul(left, right):
    """Exact Pauli words indexed by integer sites; no finite boundary."""
    result = dict(left)
    phase = sp.Integer(1)
    for site, q in right:
        p = result.get(site, 0)
        if p == 0:
            result[site] = q
        elif p == q:
            result.pop(site)
        else:
            # XY=iZ, YZ=iX, ZX=iY; the reverse order changes sign.
            phase *= sp.I if (p, q) in [(1, 2), (2, 3), (3, 1)] else -sp.I
            result[site] = 6-p-q
    return tuple(sorted(result.items())), phase

def add(*terms):
    out = {}
    for scale, obj in terms:
        for word, coefficient in obj.items():
            out[word] = sp.expand(out.get(word, 0) + scale*coefficient)
    return {w: c for w, c in out.items() if c != 0}

def multiply(left, right):
    out = {}
    for a, ca in left.items():
        for b, cb in right.items():
            w, phase = pauli_mul(a, b)
            out[w] = sp.expand(out.get(w, 0) + ca*cb*phase)
    return {w: c for w, c in out.items() if c != 0}

def shift(obj, displacement):
    return {tuple((x+displacement, p) for x, p in w): c for w, c in obj.items()}

def density(x):
    return {((x, 3), (x+1, 1)): sp.Integer(1),
            ((x, 2),): sp.Rational(2, 5),
            ((x-1, 1), (x+1, 3)): sp.Rational(1, 7)}

def deriv(obj, weighted):
    sites = [x for w in obj for x, _ in w]
    if not sites:
        return {}
    terms = []
    # Every h_x touching the input is included; the two-site radius is one.
    for x in range(min(sites)-1, max(sites)+2):
        hx = density(x)
        comm = add((1, multiply(hx, obj)), (-1, multiply(obj, hx)))
        terms.append((sp.I * (x if weighted else 1), comm))
    return add(*terms)

def sparse_controls():
    for n, word in enumerate([
        ((0, 1),), ((0, 2),), ((0, 3),), ((0, 1), (1, 2)),
        ((-1, 3), (1, 1)), ((0, 3), (2, 2))
    ]):
        obj = {word: sp.Integer(1)}
        actual = shift(deriv(shift(obj, -1), True), 1)
        candidate = add((1, deriv(obj, True)),
                        (TRANSLATION_ENERGY_SIGN, deriv(obj, False)))
        delta = add((1, actual), (-1, candidate))
        coefficient_square_sum = sum(sp.conjugate(c)*c for c in delta.values())
        exact(f"weighted_geometric_reindex_{n}", coefficient_square_sum, 0)

def gaussian(x, center, phase):
    return np.exp(-0.5*(x-center)**2 + 1j*phase*x)

def direct_overlap(nu, center, phase):
    # Integral of conjugate g(y) h(y) in ordinary coordinate space.
    def integrand(y):
        return np.conjugate(gaussian(y, 0.0, nu))*gaussian(y, center, phase)
    real, er = quad(lambda y: float(integrand(y).real), -np.inf, np.inf,
                    epsabs=1e-12, epsrel=1e-12)
    imag, ei = quad(lambda y: float(integrand(y).imag), -np.inf, np.inf,
                    epsabs=1e-12, epsrel=1e-12)
    return real+1j*imag, er+ei

def phase_space_action(mu, nu, center, phase, x, order):
    """Direct two-variable integral of the actual modulation/shift action.

    For L=f(x) conjugate(g(y)), Fourier completion gives coefficient
    sqrt(pi) exp(-a²/4-(mu-nu-t)²/4+i*a*(mu+nu-t)/2).
    Substitutions t=mu-nu+2u, a=2v leave Hermite's Gaussian weights.
    No coordinate overlap or rank-one output is used here.
    """
    nodes, weights = hermgauss(order)
    u, v = np.meshgrid(nodes, nodes, indexing="ij")
    t, a = mu-nu+2*u, 2*v
    phase_factor = np.exp(1j*(a*(mu+nu-t)/2 + t*x))
    values = phase_factor*gaussian(x+KERNEL_SHIFT_SIGN*a, center, phase)
    return KERNEL_FACTOR*np.sum(weights[:, None]*weights[None, :]*values)

def kernel_controls():
    for family, pars in enumerate([(0.2, -0.4, 0.3, 0.7),
                                    (-0.3, 0.6, -0.25, -0.5)]):
        mu, nu, center, phase = pars
        overlap, error_estimate = direct_overlap(nu, center, phase)
        for x in [-0.7, 0.0, 1.1]:
            expected = gaussian(x, 0.0, mu)*overlap
            previous = phase_space_action(*pars, x, 64)
            actual = phase_space_action(*pars, x, 128)
            close(f"kernel_rank_one_{family}_{x}", actual, expected, 2e-10)
            close(f"kernel_quadrature_refinement_{family}_{x}", actual, previous, 2e-8)
        ROWS.append({"name": f"coordinate_quad_error_{family}",
                     "method": "quadrature error diagnostic", "estimated_error": error_estimate,
                     "passed": error_estimate < 1e-10})

def energy(k, mass, beta):
    return np.sqrt(mass*mass+beta*k*k)

def pulled_k(k, s, mass, beta):
    gamma = math.sqrt(beta)
    return k*np.cosh(gamma*s)-energy(k, mass, beta)/gamma*np.sinh(gamma*s)

def profile(k):
    return (1+1j*k/3)*np.exp(-k*k/2+1j*k/5)

def profile_derivative(k):
    return np.exp(-k*k/2+1j*k/5)*(1j/3+(1+1j*k/3)*(-k+1j/5))

def flat_flow(k, s, mass, beta):
    new = pulled_k(k, s, mass, beta)
    return np.sqrt(energy(new, mass, beta)/energy(k, mass, beta))*profile(new)

def candidate_B(k, mass, beta):
    e = energy(k, mass, beta)
    return 1j*BOOST_GENERATOR_SCALE*(e*profile_derivative(k)
                     + FLAT_WEIGHT_COEFFICIENT*beta*k/e*profile(k))

def d4(fun, step):
    return (fun(-2*step)-8*fun(-step)+8*fun(step)-fun(2*step))/(12*step)

def boost_controls():
    for mass, beta in [(0.75, 0.25), (1.0, 2.0), (2.0, 9.0)]:
        for k in [-0.8, 0.3, 1.7]:
            actual = d4(lambda s: flat_flow(k, s, mass, beta), 1e-4)
            close(f"actual_flat_boost_derivative_{mass}_{beta}_{k}",
                  actual, 1j*candidate_B(k, mass, beta), 3e-8)
            def conjugated(s):
                new = pulled_k(k, s, mass, beta)
                return np.exp(1j*(new-k))*flat_flow(k, s, mass, beta)
            actual_T = d4(conjugated, 1e-4)
            predicted_T = 1j*(candidate_B(k, mass, beta)
                              +TRANSLATION_ENERGY_SIGN*energy(k, mass, beta)*profile(k))
            close(f"actual_T_boost_derivative_{mass}_{beta}_{k}",
                  actual_T, predicted_T, 3e-8)
            for s in [-0.23, 0.19]:
                new = pulled_k(k, s, mass, beta)
                r = np.arcsinh(math.sqrt(beta)*k/mass)
                r_new = np.arcsinh(math.sqrt(beta)*new/mass)
                close(f"rapidity_Weyl_{mass}_{beta}_{k}_{s}",
                      np.exp(0.71j*r_new),
                      np.exp(-0.71j*math.sqrt(beta)*s)*np.exp(0.71j*r), 5e-14)
                # Compute V from actual T=e^(-ik+i theta), not as a fixed phase.
                def mismatch(momentum):
                    return np.exp(1j*MISMATCH_CURRENT_SIGN*momentum)*np.exp(-1j*momentum+0.37j)
                close(f"central_mismatch_commutation_{mass}_{beta}_{k}_{s}",
                      mismatch(new), mismatch(k), 5e-14)

def exact_domain_controls():
    k = sp.symbols("k", real=True)
    e = sp.sqrt(1+k*k)
    g = (1+k*k)**sp.Rational(-1, 4)
    psi = sp.exp(-sp.I*k)*g
    B = lambda f: sp.I*e*sp.diff(f, k)
    weighted_square = lambda f: sp.simplify(f*sp.conjugate(f)/(2*e))
    norm_density = weighted_square(psi)
    difference_density = weighted_square(B(psi)-e*psi)
    energy_density = weighted_square(e*psi)
    exact("domain_vector_density", norm_density, 1/(2*(1+k*k)))
    exact("domain_difference_density", difference_density, k*k/(8*(1+k*k)**2))
    exact("domain_energy_density", energy_density, sp.Rational(1, 2))
    # Actual conjugation predicts the graph density of g and Bg.
    actual_graph = sp.integrate(weighted_square(g)+weighted_square(B(g)),
                               (k, -sp.oo, sp.oo))
    candidate_density = norm_density+difference_density
    if REQUIRE_ENERGY_IN_DIFFERENCE_DOMAIN:
        candidate_density += energy_density
    candidate_graph = sp.integrate(candidate_density, (k, -sp.oo, sp.oo))
    exact("maximal_difference_graph_domain", candidate_graph, actual_graph)
    exact("unitary_conjugate_graph_integral", actual_graph, 9*sp.pi/16)

def central_measure_controls():
    mu = [{sp.Rational(-1, 3): sp.Rational(1, 3), sp.Rational(1, 2): sp.Rational(2, 3)},
          {sp.Rational(1, 2): sp.Rational(2, 5), sp.Rational(6, 5): sp.Rational(3, 5)}]
    coefficients = [sp.Rational(1, 2), sp.Rational(1, 4)]
    nu = {}
    for b, measure in zip(coefficients, mu):
        for theta, weight in measure.items():
            nu[theta] = nu.get(theta, 0)+b*weight
    values = [lambda theta: 1+sp.I*theta,
              lambda theta: sp.Rational(2, 3)-sp.I*theta/2]
    before = after = 0
    for j, measure in enumerate(mu):
        for theta, central_weight in nu.items():
            weight = measure.get(theta, 0)
            value = values[j](theta)
            before += weight*value*sp.conjugate(value)
            radon = weight/central_weight
            factor = sp.sqrt(radon) if RN_USE_SQUARE_ROOT else radon
            mapped = factor*value
            after += central_weight*mapped*sp.conjugate(mapped)
    exact("central_Radon_Nikodym_isometry", after, before)
    for n in [1, 4, 17, 103]:
        count = 57
        partial = sum(Fraction(1, j*(j+1)) for j in range(n, n+count))
        exact(f"central_tail_telescoping_{n}",
              sp.Rational(partial.numerator, partial.denominator)+sp.Rational(1, n+count),
              sp.Rational(1, n))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    sparse_controls()
    kernel_controls()
    boost_controls()
    exact_domain_controls()
    central_measure_controls()
    for row in ROWS:
        print(json.dumps(row, sort_keys=True))
    scope = {
        "per_element": "Exact Pauli coefficients and explicit operator-action values are checked; no general theorem follows from their finite count.",
        "per_site": "The Pauli fixtures use indexed sites with a proved local support collar; no infinite-lattice representation is constructed.",
        "per_mode": "Actual massive pullbacks, central phases and one exact infinite-tail domain witness are checked in an abstract representation.",
        "per_block": "The mathematical proof supplies the Weyl decomposition and complete domains; these author controls challenge its normalization and signs.",
        "lattice_wide": "Checked and not executed — no nontrivial finite-range spin model satisfying every supplied Lie/state/mass condition is established."
    }
    for label, description in scope.items():
        print(label+": "+description)
    failed = [r["name"] for r in ROWS if not r["passed"]]
    output = {"rows": ROWS, "scope": scope, "total": len(ROWS),
              "failed": failed, "pass_count": len(ROWS)-len(failed), "fail_count": len(failed),
              "versions": {"python": sys.version, "numpy": np.__version__, "sympy": sp.__version__}}
    # Publication suppresses the result-file write only; the complete output dictionary remains computed.
    print(f"TOTAL: PASS={output['pass_count']} FAIL={output['fail_count']}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
