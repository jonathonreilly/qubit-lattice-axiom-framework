#!/usr/bin/env python3
"""Finite author controls. No analytic convergence or physical-model certificate."""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/COMPACT_DETECTOR_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md",
]
if not __debug__:
    raise RuntimeError("Run without -O: exact control assertions must be enabled")

from fractions import Fraction as F
import cmath
import json
import math


def record(name, **data):
    print(json.dumps({"check": name, "scope": "finite algebra only", **data}, sort_keys=True))


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def adj(a):
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def diag(v):
    return [[v[i] if i == j else 0j for j in range(len(v))] for i in range(len(v))]


def delta(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def scale(c, a):
    return [[c * z for z in row] for row in a]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


N = 11
p = [2 * math.pi * k / N for k in range(N)]
dft = [[cmath.exp(-1j * p[k] * x) / math.sqrt(N) for x in range(N)] for k in range(N)]
omega = [math.sin(z) + 0.2 * math.cos(2 * z) for z in p]
t, s = 1.7, 4.25


def u(r):
    return diag([cmath.exp(1j * r * e) for e in omega])


# Multiplication by exp(+2 pi i X/N) shifts the e^{-ipx} transform by p -> p-2 pi/N.
emod = diag([cmath.exp(2j * math.pi * x / N) for x in range(N)])
observed = mul(mul(u(t), mul(mul(dft, emod), adj(dft))), u(-t))
expected = [[cmath.exp(1j * t * (omega[k] - omega[j]))
             if j == (k - 1) % N else 0j for j in range(N)] for k in range(N)]
wrong = [[cmath.exp(-1j * t * (omega[k] - omega[j]))
          if j == (k - 1) % N else 0j for j in range(N)] for k in range(N)]
good_error, wrong_error = delta(observed, expected), delta(observed, wrong)
assert good_error < 1e-11 and wrong_error > 0.1
record("free_Heisenberg_Fourier_sign", dimension=N, max_error=good_error,
       reversed_phase_error=wrong_error, tolerance=1e-11)

# The identity used before the reversed integral retains g before h.
h = mul(mul(dft, diag([1 + (x % 3) / 5 for x in range(N)])), adj(dft))
g = diag([1 + k / (2 * N) for k in range(N)])
kt = mul(mul(mul(u(t), g), h), u(-t))
left = mul(kt, u(s))
right = mul(mul(mul(u(t), g), h), u(s - t))
wrong_order = mul(mul(mul(u(t), h), g), u(s - t))
assert delta(left, right) < 1e-11 and delta(left, wrong_order) > 1e-3
record("two_time_operator_order", exact_identity_error=delta(left, right),
       commuting_g_through_h_error=delta(left, wrong_order), tolerance=1e-11)

# Exact finite-time Duhamel sign: w(r)=a+r b and R(r)=exp(-ir omega)b.
a = [[complex(k + 1, 0.2)] for k in range(N)]
b = [[complex(0.3, (k + 1) / 7)] for k in range(N)]
wt, ws = add(a, scale(t, b)), add(a, scale(s, b))
actual = mul(kt, wt)
integral = scale(s - t, mul(kt, b))
recovered = add(mul(kt, ws), scale(-1, integral))
bad_sign = add(mul(kt, ws), integral)
phase_errors = []
for r in [t, (t + s) / 2, s]:
    rr = mul(u(-r), b)
    phase_errors.append(delta(mul(mul(kt, u(r)), rr), mul(kt, b)))
assert delta(actual, recovered) < 1e-11 and max(phase_errors) < 1e-11
assert delta(actual, bad_sign) > 1
record("reversed_Duhamel_sign", identity_error=delta(actual, recovered),
       phase_cancellation_error=max(phase_errors), wrong_sign_error=delta(actual, bad_sign))

# Source qR=R does not permit deleting q after a spatial multiplication.
q = diag([1 if k < 3 else 0 for k in range(N)])
v = [[1 + 0j if k == 1 else 0j] for k in range(N)]
chi = mul(mul(dft, diag([1 if x < 5 else 0 for x in range(N)])), adj(dft))
filtered_after = mul(q, mul(chi, v))
unfiltered_after = mul(chi, v)
assert delta(mul(q, v), v) == 0 and delta(filtered_after, unfiltered_after) > 0.1
record("source_filter_after_spatial_cutoff", qR_error=delta(mul(q, v), v),
       invalid_filter_deletion_error=delta(filtered_after, unfiltered_after))

# Rational stationary geometry, including zero and very small propagation times.
intervals = [(F(-4, 5), F(-3, 10)), (F(3, 10), F(4, 5))]
ratios = [F(1), F(999, 1000), F(1, 2), F(1, 100)]
count = 0
for lam in ratios:
    for lo, hi in intervals:
        for av in [lo, (lo + hi) / 2, hi]:
            for vel in [lo, (lo + hi) / 2, hi]:
                y = lam * av + (1 - lam) * vel
                assert lo <= y <= hi
                count += 1
# At s=2t, x/t=v=+/-1/2 the wrong stationary sign puts both coordinates at zero.
wrong_y = [F(1, 2) * vv - F(1, 2) * vv for vv in [F(-1, 2), F(1, 2)]]
right_y = [F(1, 2) * vv + F(1, 2) * vv for vv in [F(-1, 2), F(1, 2)]]
assert wrong_y == [0, 0] and right_y[0] != right_y[1]
record("convex_stationary_geometry", rational_cases=count,
       includes_s_equal_t=True, wrong_sign_hits_collision=True,
       limit="Finite cases discriminate signs; the all-point convex proof is in C20.")

# A cubic checks the third derivative algebra exactly; sin checks a periodic instance.
z = F(2, 5)
actual_cubic_remainder = (z / 2) ** 3 - (-z / 2) ** 3
correct_cubic_remainder = z ** 3 * F(1, 16) * (F(6) + F(6)) * F(1, 3)
printed_difference_remainder = z ** 3 * F(1, 16) * (F(6) - F(6)) * F(1, 3)
assert actual_cubic_remainder == correct_cubic_remainder
assert actual_cubic_remainder != printed_difference_remainder
sin_remainder = 2 * math.sin(float(z) / 2) - float(z)
assert abs(sin_remainder) > 1e-4
record("third_derivative_sum_not_difference", cubic_actual=str(actual_cubic_remainder),
       cubic_corrected=str(correct_cubic_remainder), printed_cubic=str(printed_difference_remainder),
       periodic_sin_remainder=sin_remainder,
       limit="This source typo is not used in the convergence proof.")

record("summary", checks=6, outcome="all six finite controls met their declared criteria",
       analytic_convergence_certified=False, independent_review=False,
       physical_realization_certified=False)

print("per_element: complete original finite algebra controls checked")
print("per_site: finite lattice fixtures only; no infinite-volume inference")
print("per_mode: Fourier and source signs checked at the stated finite scope")
print("per_block: ordered products and finite projections checked")
print("lattice_wide: checked and not executed — convergence and exhaustion require the written proofs")
print("TOTAL: PASS=6 FAIL=0")
print("SCOPE: Finite Fourier, ordering, convex-geometry and source-typo controls only; infinite-lattice kernel decay and detector convergence rest on C1-C28.")
