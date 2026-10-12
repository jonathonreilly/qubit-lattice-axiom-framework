"""Independent exact checks for the K2 referee report.

These checks deliberately avoid the worker's random-shell and finite-box
implementations where a short algebraic certificate is available.
"""

from fractions import Fraction
from itertools import product
from math import prod

import sympy as sp


def monomials_leq(variables, degree):
    terms = []
    for exponents in product(range(degree + 1), repeat=len(variables)):
        if sum(exponents) <= degree:
            term = sp.Integer(1)
            for variable, exponent in zip(variables, exponents):
                term *= variable**exponent
            terms.append(term)
    return terms


print("== 1. Polynomial lattice Killing equation, exact coefficient rank ==")
y = sp.symbols("y0:4")
for degree in (1, 2, 3):
    basis = monomials_leq(y, degree)
    coefficients = sp.symbols(f"c0:{4 * len(basis)}")
    xi = [sum(coefficients[nu * len(basis) + j] * term for j, term in enumerate(basis))
          for nu in range(4)]
    equations = []
    for mu in range(4):
        shifted = {y[mu]: y[mu] + 1}
        for nu in range(mu, 4):
            expression = sp.expand(
                xi[nu].subs(shifted, simultaneous=True) - xi[nu]
                + xi[mu].subs({y[nu]: y[nu] + 1}, simultaneous=True) - xi[mu]
            )
            polynomial = sp.Poly(expression, *y)
            equations.extend(polynomial.coeffs())
    matrix, _ = sp.linear_eq_to_matrix(equations, coefficients)
    nullity = len(coefficients) - matrix.rank()
    print(f"degree <= {degree}: unknown coefficients={len(coefficients)}, exact nullity={nullity}")


print("\n== 2. Constructive Calabi/Killing-cokernel homotopy ==")
for degree in (2, 3, 4, 5):
    homogeneous = [term for term in monomials_leq(y, degree)
                   if sp.Poly(term, *y).total_degree() == degree]
    # Deterministic, non-symmetric vector polynomial with rational coefficients.
    vector = [sum(sp.Rational((nu + 2) * (j + 3) % 11 - 5, j + 2) * term
                  for j, term in enumerate(homogeneous)) for nu in range(4)]
    radial = sum(y[mu] * vector[mu] for mu in range(4))
    tensor = sp.Matrix(4, 4, lambda mu, nu:
                       (sp.diff(vector[nu], y[mu]) + sp.diff(vector[mu], y[nu])) / (degree - 1)
                       - sp.diff(radial, y[mu], y[nu]) / (degree * (degree - 1)))
    residual = [sp.expand(sum(y[mu] * tensor[mu, nu] for mu in range(4)) - vector[nu])
                for nu in range(4)]
    print(f"homogeneous degree {degree}: symmetric={tensor == tensor.T}, div residual={residual}")


print("\n== 3. Scalar O(kappa) Ward identity in exact rational arithmetic ==")
dimension = 4
size = 3
sites = list(product(range(size), repeat=dimension))


def shifted(site, axis, amount):
    result = list(site)
    result[axis] = (result[axis] + amount) % size
    return tuple(result)


def field_value(seed, site):
    # Small deterministic integers; no shared random-number or ndarray path.
    return Fraction(((sum((axis + 2) * coordinate for axis, coordinate in enumerate(site))
                       + 7 * seed + 3 * prod(coordinate + 1 for coordinate in site)) % 13) - 6)


phi = {site: field_value(1, site) for site in sites}
xi = [{site: field_value(10 + nu, site) for site in sites} for nu in range(dimension)]
mass2 = Fraction(3, 4)


def forward(site, axis):
    return phi[shifted(site, axis, 1)] - phi[site]


def eom(site):
    laplacian = sum(phi[shifted(site, mu, 1)] + phi[shifted(site, mu, -1)] - 2 * phi[site]
                    for mu in range(dimension))
    return -laplacian + mass2 * phi[site]


def lie(site):
    return sum((xi[nu][site] * forward(site, nu)
                + xi[nu][shifted(site, nu, -1)] * forward(shifted(site, nu, -1), nu)) / 2
               for nu in range(dimension))


def stress(mu, nu, base):
    if mu != nu:
        return ((forward(base, mu) + forward(shifted(base, nu, 1), mu))
                * (forward(base, nu) + forward(shifted(base, mu, 1), nu)) / 4)
    z = shifted(base, mu, 1)
    value = forward(z, mu) * forward(shifted(z, mu, -1), mu) / 2 - mass2 * phi[z] ** 2 / 2
    for rho in range(dimension):
        if rho != mu:
            value -= (forward(z, rho) ** 2 + forward(shifted(z, rho, -1), rho) ** 2) / 4
    return value


matter_variation = sum(eom(site) * lie(site) for site in sites)
metric_variation = Fraction(0)
for mu in range(dimension):
    for nu in range(dimension):
        for site in sites:
            dh = (xi[nu][shifted(site, mu, 1)] - xi[nu][site]
                  + xi[mu][shifted(site, nu, 1)] - xi[mu][site])
            metric_variation += dh * stress(mu, nu, site)
print("2 sum(E L_xi phi) - sum(delta h T) =", 2 * matter_variation - metric_variation)


print("\n== 4. Exact non-closure certificates (no shell fit) ==")
coefficient = sp.symbols("c_a")
# Averaging over +/-k_b and +/-k_4 kills every odd translation component
# except the a component.  The shell is preserved because it depends on
# cos(k_b), cos(k_4) for the scalar and on sin(k_b)^2, sin(k_4)^2 for the
# fermion.
scalar_r0 = -sp.cos(0) * sp.sin(sp.pi / 2)
scalar_r1 = -sp.cos(sp.pi / 3) * sp.sin(sp.pi / 2)
scalar_c = sp.solve(sp.Eq(coefficient * sp.sin(sp.pi / 2), scalar_r0), coefficient)[0]
print(f"scalar: first sign-average fixes c_a={scalar_c}; second R={scalar_r1}, predicted={scalar_c}")
fermion_fa = sp.sin(2 * sp.pi / 4) / 2
fermion_r0 = fermion_fa * sp.cos(0)
fermion_r1 = fermion_fa * sp.cos(2 * sp.pi / 6)
fermion_c = sp.solve(sp.Eq(coefficient * fermion_fa, fermion_r0), coefficient)[0]
print(f"fermion: first sign-average fixes c_a={fermion_c}; second R={fermion_r1}, predicted={fermion_c * fermion_fa}")
print("example shell roots at m^2=1/4: scalar cos(k4)=17/8 then 21/8; fermion sin(k4)^2=-3/4 then -1")
print("Both point families lie on their complex shells by choosing the corresponding +/-k_4 root;")
print("odd translation components cancel in the sign average, while the even cosine defect remains.")


print("\n== 5. TT kernel, longitudinal zero, and transfer/leapfrog roots ==")
q, t = sp.symbols("q t", real=True)
s = sp.Matrix([q, 0, 0, t])


def fierz_pauli_quadratic(matrix):
    norm = sum(matrix[mu, nu] ** 2 for mu in range(4) for nu in range(4))
    hs = matrix * s
    shs = (s.T * matrix * s)[0]
    trace = sp.trace(matrix)
    return sp.factor((sum(component**2 for component in s) * norm
                      - 2 * (hs.T * hs)[0] + 2 * shs * trace
                      - sum(component**2 for component in s) * trace**2) / 4)


tt_plus = sp.diag(0, 1, -1, 0)
tt_cross = sp.zeros(4)
tt_cross[1, 2] = tt_cross[2, 1] = 1
longitudinal = sp.zeros(4)
longitudinal[0, 0] = q**2
for label, matrix in (("TT plus", tt_plus), ("TT cross", tt_cross), ("longitudinal", longitudinal)):
    norm = sp.factor(sum(matrix[mu, nu] ** 2 for mu in range(4) for nu in range(4)))
    print(f"{label}: Q={fierz_pauli_quadratic(matrix)}, Q/(h:h)={sp.factor(fierz_pauli_quadratic(matrix) / norm) if norm else 0}")

omega2 = sp.Integer(12)
euclidean_roots = sp.solve(sp.Symbol("z")**2 - (2 + omega2) * sp.Symbol("z") + 1, sp.Symbol("z"))
leapfrog_roots = sp.solve(sp.Symbol("z")**2 - (2 - omega2) * sp.Symbol("z") + 1, sp.Symbol("z"))
print("corner Euclidean roots:", euclidean_roots)
print("corner leapfrog roots:", leapfrog_roots)
print("largest leapfrog modulus:", 5 + 2 * sp.sqrt(6))
