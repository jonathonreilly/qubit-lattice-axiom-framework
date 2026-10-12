#!/usr/bin/env python3
"""Finite author controls only; no certification of analytic convergence."""
import cmath

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/ISOLATED_CENTRE_FILTERING_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md",
    "docs/COMPACT_PATCH_FOCK_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/COMPACT_DETECTOR_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-10-12.md"
]
if not __debug__:
    raise RuntimeError("Run without -O: finite control assertions must be enabled")

from fractions import Fraction as F
import itertools
import json
import math


def emit(name, **fields):
    print(json.dumps(dict(check=name, status="pass", **fields), sort_keys=True))


def matmul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def star(a):
    return [[z.conjugate() for z in col] for col in zip(*a)]


def err(a, b):
    return max(abs(x-y) for ar, br in zip(a, b) for x, y in zip(ar, br))


def diag(values):
    return [[z if i == j else 0j for j in range(len(values))]
            for i, z in enumerate(values)]


def value(coeff, theta):
    return sum(c*cmath.exp(1j*j*theta) for j, c in coeff.items())


def filtered(coeff, phases, b):
    out = [[0j for _ in phases] for _ in phases]
    for j, c in coeff.items():
        u = diag([cmath.exp(1j*j*t) for t in phases])
        term = matmul(matmul(u, b), star(u))
        out = [[x+c*y for x, y in zip(ar, br)] for ar, br in zip(out, term)]
    return out


coeff = {-2: 0.23-0.11j, 0: 0.8+0.07j, 1: -0.31+0.19j, 3: 0.09-0.13j}
ngrid = 17
nodes = [2*math.pi*k/ngrid for k in range(ngrid)]
recovered = {j: sum(value(coeff, x)*cmath.exp(-1j*j*x) for x in nodes)/ngrid
             for j in range(-5, 6)}
wrong = {j: sum(value(coeff, x)*cmath.exp(1j*j*x) for x in nodes)/ngrid
         for j in range(-5, 6)}
fourier_error = max(abs(recovered[j]-coeff.get(j, 0)) for j in recovered)
wrong_gap = max(abs(wrong[j]-coeff.get(j, 0)) for j in recovered)
assert fourier_error < 1e-13 and wrong_gap > 0.2
emit("central_fourier_sign", nodes=ngrid, maximum_error=fourier_error,
     wrong_sign_gap=wrong_gap, limit="finite trigonometric polynomial")

phases = [0, 0.41, -1.17, 2.02, 0.89]
b = [[complex((a+1)*(k+2)/13, (2*a-k+1)/11) for k in range(5)] for a in range(5)]
actual = filtered(coeff, phases, b)
oracle = [[value(coeff, x-y)*b[a][k] for k, y in enumerate(phases)]
          for a, x in enumerate(phases)]
outgoing_only = [[value(coeff, x)*z for z in b[a]] for a, x in enumerate(phases)]
vacuum_error = max(abs(actual[a][0]-value(coeff, x)*b[a][0])
                   for a, x in enumerate(phases))
adjoint_error = err(star(actual), filtered({j: c.conjugate() for j, c in coeff.items()},
                                         phases, star(b)))
real_odd_coeff = {-1: 0.15j, 0: 1, 1: -0.15j}  # 1 + 0.3 sin(theta)
wrong_star_gap = err(star(filtered(real_odd_coeff, phases, b)),
                     filtered(real_odd_coeff, phases, star(b)))
assert err(actual, oracle) < 1e-13 and vacuum_error < 1e-13
assert err(actual, outgoing_only) > 0.1 and adjoint_error < 1e-13
assert wrong_star_gap > 0.1
emit("transition_difference_and_adjoint", matrix_size=5,
     transition_error=err(actual, oracle), vacuum_error=vacuum_error,
     outgoing_only_gap=err(actual, outgoing_only), adjoint_error=adjoint_error,
     real_phi_star_preservation_gap=wrong_star_gap,
     limit="finite diagonal-unitary representation, not a lattice model")

other = {-1: 0.2+0.1j, 0: 0.4, 2: -0.3j}
product = {}
for j, c in coeff.items():
    for k, d in other.items():
        product[j+k] = product.get(j+k, 0) + c*d
composition_error = err(filtered(coeff, phases, filtered(other, phases, b)),
                        filtered(product, phases, b))
assert composition_error < 1e-13
emit("composition_product_multiplier", maximum_error=composition_error)

# Exact diagonal spectral masks: the other nearby centre is outside the
# covered K patch; a same-centre point at a different mass must also be removed.
mass = [F(0), F(1), F(1), F(1), F(0)]
momentum = [F(1, 2), F(4, 5), F(1), F(0), F(9, 10)]
phi = [F(1, 5), F(1), F(1), F(4, 5), F(1)]
point = [F(0), F(1), F(1), F(0), F(1)]
selected = [a*h*p for a, h, p in zip(mass, momentum, phi)]
exact = [a*h*p for a, h, p in zip(mass, momentum, point)]
assert selected == exact
assert [a*p for a, p in zip(mass, phi)] != [a*p for a, p in zip(mass, point)]
assert [h*p for h, p in zip(momentum, phi)] != selected
emit("patch_and_mass_selection_masks", exact=True,
     global_isolation_inference_rejected=True, omitted_mass_filter_rejected=True,
     limit="spectral-mask algebra only; no existence or smooth-filter construction test")


def pmul(p, q):
    out = {}
    for a, x in p.items():
        for bkey, y in q.items():
            k = tuple(u+v for u, v in zip(a, bkey))
            out[k] = out.get(k, F(0)) + x*y
    return out


def peval(p, z):
    return sum(c*math.prod(w**a for w, a in zip(z, power))
               for power, c in p.items())


torsion = list(itertools.product((F(1), F(-1)), repeat=2))
checked = 0
for a, za in enumerate(torsion):
    poly = {(0, 0): F(1)}
    for bidx, zb in enumerate(torsion):
        if a == bidx:
            continue
        coord = next(k for k in range(2) if za[k] != zb[k])
        unit = tuple(int(k == coord) for k in range(2))
        denom = za[coord]-zb[coord]
        poly = pmul(poly, {unit: 1/denom, (0, 0): -zb[coord]/denom})
    for c, zc in enumerate(torsion):
        assert peval(poly, zc) == int(a == c)
        checked += 1
counts = [len({z[0]**j[0]*z[1]**j[1] for z in torsion})
          for j in itertools.product(range(2), repeat=2)]
assert max(counts) == 2
simple_selector = [(1+z[0])*(1+z[1])/4 for z in torsion]
assert simple_selector == [F(1), F(0), F(0), F(0)]
emit("finite_multivariate_interpolation", exact_character_pairs=checked,
     direction_parity_cases=len(counts), maximum_single_direction_values=max(counts),
     all_integer_directions_reduce_mod_two=True)

angles = [(0.2, -0.4), (0.2, 0.7), (1.1, 0.7), (-0.9, 1.4)]
characters = [tuple(cmath.exp(1j*t) for t in row) for row in angles]
interpolation_error = 0
for a, za in enumerate(characters):
    for c, zc in enumerate(characters):
        result = 1
        for bidx, zb in enumerate(characters):
            if a == bidx:
                continue
            coord = next(k for k in range(2) if abs(za[k]-zb[k]) > 1e-10)
            result *= (zc[coord]-zb[coord])/(za[coord]-zb[coord])
        interpolation_error = max(interpolation_error, abs(result-int(a == c)))
assert interpolation_error < 1e-13
emit("non_torsion_specific_interpolation", numeric_character_pairs=16,
     maximum_error=interpolation_error, limit="no finite test of irrationality or infinite spectra")

radius_cases = 0
for d in range(1, 13):
    for v in (F(0), F(1, 3), F(1), F(4), F(10)):
        c = 1/(8*d*(1+v))
        assert F(1, 4)+c+F(1, 2) <= F(7, 8)
        assert F(1, 2*d)-v*c >= F(3, 8*d)
        # If one instead spends the whole R on seed+flow padding before
        # accounting for the geometric displacement, the final radius exceeds R.
        assert F(1, 2)+c+F(1, 2) > 1
        radius_cases += 1
emit("uniform_locality_radius_arithmetic", exact_cases=radius_cases,
     geometric_shift_omission_rejected=True,
     limit="checks dimension/velocity arithmetic, not the LR inequality or tails")

p, theta, lift = 0.37, 0.42, -1
k = p+theta+2*math.pi*lift
k_wrong = p-theta+2*math.pi*lift
graph_error = max(abs(cmath.exp(-1j*j*p)-cmath.exp(-1j*j*k)*cmath.exp(1j*j*theta))
                  for j in range(-4, 5))
graph_wrong = max(abs(cmath.exp(-1j*j*p)-cmath.exp(-1j*j*k_wrong)*cmath.exp(1j*j*theta))
                  for j in range(-4, 5))
assert graph_error < 1e-13 and graph_wrong > 0.5
gap = math.sqrt(2)-1
derivative_norm = gap/math.sqrt(2)
one_time_error = abs(cmath.exp(1j*gap)-1)/math.sqrt(2)
assert derivative_norm > 0.2 and one_time_error > 0.2
emit("chart_sign_and_unresolved_clock", exact_phase_comparisons=9,
     maximum_chart_error=graph_error, opposite_chart_sign_gap=graph_wrong,
     unresolved_derivative_norm=derivative_norm, unresolved_t1_error=one_time_error,
     limit="finite spectral algebra; no infinite-lattice scattering model")

emit("summary", controls=8, independent=False, analytic_convergence_certified=False,
     physical_realization_certified=False)

print("TOTAL: PASS=8 FAIL=0")
print("SCOPE: Eight finite algebra groups; no analytic convergence or microscopic realization certificate.")
