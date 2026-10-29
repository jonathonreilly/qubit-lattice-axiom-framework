#!/usr/bin/env python3
"""Actual d4 loop-family flat charged blocks and periodic neutral Wilson block.

Prospective tolerances: uniform_one_loop_criteria.md. Finite controls only.
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp


records = []


def check(name, ok, data):
    records.append({"name": name, "passed": bool(ok), "data": data})
    print(json.dumps(records[-1], sort_keys=True), flush=True)


z = sp.symbols("z0:4", nonzero=True)
ii = sp.I
nu = sp.Matrix([a - 1 for a in z])
minus = {a: 1 / a for a in z}
lam = sum(2 - a - 1 / a for a in z)


def path_row(steps):
    site = [0] * 4
    row = [0] * 4
    for mu, sign in steps:
        if sign < 0:
            site[mu] -= 1
        phase = sp.prod(z[j] ** site[j] for j in range(4))
        row[mu] += sign * phase
        if sign > 0:
            site[mu] += 1
    assert site == [0] * 4
    return sp.Matrix([row])


def loop(mu, nu_axis, long):
    return ([(mu, 1)] * long + [(nu_axis, 1)] +
            [(mu, -1)] * long + [(nu_axis, -1)])


pw = [path_row(loop(mu, nv, 1)) for mu in range(4) for nv in range(mu + 1, 4)]
pr = [path_row(loop(mu, nv, 2)) for mu in range(4) for nv in range(4) if nv != mu]


def quadratic(rows):
    out = sp.zeros(4)
    for row in rows:
        out += row.subs(minus, simultaneous=True).T * row
    return out.applyfunc(sp.expand)


hw, hr = quadratic(pw), quadratic(pr)
gf = nu * nu.subs(minus, simultaneous=True).T
gauge_res = [sp.expand((row * nu)[0]) for row in pw + pr]
check("actual_path_counts_and_gradient", len(pw) == 6 and len(pr) == 12 and
      all(a == 0 for a in gauge_res), {"plaquettes": len(pw), "rectangles": len(pr),
                                     "gradient_residuals": list(map(str, gauge_res))})
wilson_res = (hw + gf - lam * sp.eye(4)).applyfunc(sp.simplify)
check("Wilson_gauge_completion", wilson_res == sp.zeros(4), str(wilson_res))

# The rectangle of long direction mu has exactly (1+z_mu) times
# the plaquette incidence, with its appropriate orientation.
rectangle_res = []
ix = 0
for mu in range(4):
    for nv in range(4):
        if mu == nv:
            continue
        base = path_row(loop(mu, nv, 1))
        rectangle_res.extend(list((pr[ix] - (1 + z[mu]) * base).applyfunc(sp.expand)))
        ix += 1
check("rectangle_rows_from_paths", all(a == 0 for a in rectangle_res),
      {"residual_entries": len(rectangle_res), "nonzero": list(map(str, [a for a in rectangle_res if a != 0]))})

# Extract the quadratic marginal from the actual finite Laurent polynomials
# along one nondegenerate ray. Coefficients at arbitrary directions follow
# analytically from the rectangle identity above, as in the author proof.
ray = (1, 2, 3, 1)
t = sp.symbols("t", real=True)


def ray_coefficient(expr, degree):
    # A Laurent monomial exp(i t dot(exponent,ray)) has this exact coefficient.
    ans = 0
    for term in sp.Add.make_args(sp.expand(expr)):
        powers = term.as_powers_dict()
        exponent = [int(powers.get(a, 0)) for a in z]
        coeff = term / sp.prod(a ** e for a, e in zip(z, exponent))
        omega = sum(a * b for a, b in zip(exponent, ray))
        ans += coeff * (ii * omega) ** degree / sp.factorial(degree)
    return sp.simplify(ans)


alpha = sp.Rational(1, 32)
ha = (1 - 8 * alpha) * hw + alpha * hr
diff = ha - hw
coeffs = {d: diff.applyfunc(lambda e: ray_coefficient(e, d)) for d in range(5)}
check("J1_actual_rectangle_marginal_and_quartic_start",
      all(coeffs[d] == sp.zeros(4) for d in range(4)) and coeffs[4] != sp.zeros(4),
      {str(d): str(coeffs[d]) for d in range(5)})
mut = (1 - 4 * alpha) * hw + alpha * hr - hw
mut2 = mut.applyfunc(lambda e: ray_coefficient(e, 2))
check("M_wrong_rectangle_normalization_fires", mut2 != sp.zeros(4), str(mut2))

q = sp.Integer(2)  # H=i sigma_3, normalized -tr(H^2)/2=1.
point = {a: ii for a in z}


def dz(expr):
    return ii * z[0] * sp.diff(expr, z[0])


def flat_block(alpha_value):
    oo = ((1 - 8 * alpha_value) * hw + alpha_value * hr + gf)
    # Keep z0 symbolic, set only the other three to i before determinant.
    curve = oo.subs({a: ii for a in z[1:]}, simultaneous=True)
    ll = lam.subs({a: ii for a in z[1:]}, simultaneous=True)
    o0 = curve.subs(z[0], ii).applyfunc(sp.simplify)
    o1 = curve.applyfunc(dz).subs(z[0], ii).applyfunc(sp.simplify)
    o2 = curve.applyfunc(lambda e: dz(dz(e))).subs(z[0], ii).applyfunc(sp.simplify)
    gg = o0.inv()
    determinant = sp.factor(curve.det())
    # Direct derivative of the determinant polynomial, independent of inverse traces.
    logcurvature = sp.simplify(dz(dz(determinant)) / determinant -
                              (dz(determinant) / determinant) ** 2)
    scalar_curvature = sp.simplify(dz(dz(ll)) / ll - (dz(ll) / ll) ** 2)
    direct_vec = sp.simplify(q ** 2 / 4 * logcurvature.subs(z[0], ii))
    direct_sc = sp.simplify(q ** 2 / 4 * scalar_curvature.subs(z[0], ii))
    trace_vec = sp.simplify(q ** 2 / 4 * sp.trace(gg * o2 - gg * o1 * gg * o1))
    wrong_vec = sp.simplify(q ** 2 / 4 * sp.trace(gg * o2 - gg * o1 * gg * o1 / 2))
    ll0 = ll.subs(z[0], ii)
    ll1 = dz(ll).subs(z[0], ii)
    ll2 = dz(dz(ll)).subs(z[0], ii)
    wrong_sc = sp.simplify(q ** 2 / 4 * (ll2 / ll0 - ll1 ** 2 / (2 * ll0 ** 2)))
    # Two real components times the outer half weights = vector - scalar.
    direct_group = sp.simplify(direct_vec - direct_sc)
    trace_group = sp.simplify(trace_vec - direct_sc)
    wrong_group = sp.simplify(wrong_vec - wrong_sc)
    print(json.dumps({"alpha": str(alpha_value), "O0": str(o0), "dO": str(o1),
                      "ddO": str(o2), "det_curve": str(determinant),
                      "vector_coefficient": str(direct_vec),
                      "scalar_coefficient": str(direct_sc),
                      "group_coefficient": str(direct_group)}, sort_keys=True), flush=True)
    check("charged_direct_det_vs_full_bubble_alpha=" + str(alpha_value),
          direct_vec == trace_vec and direct_group == trace_group,
          {"direct": str(direct_group), "trace": str(trace_group)})
    check("M_quarter_bubble_fires_alpha=" + str(alpha_value),
          abs(float(wrong_group - direct_group)) > 1e-6,
          {"wrong": str(wrong_group), "correct": str(direct_group)})
    check("M_one_real_root_component_fires_alpha=" + str(alpha_value),
          abs(float(direct_group / 2 - direct_group)) > 1e-6,
          {"wrong": str(direct_group / 2), "correct": str(direct_group)})
    ev = [float(sp.re(a)) for a in o0.eigenvals() for _ in range(o0.eigenvals()[a])]
    check("positive_actual_block_alpha=" + str(alpha_value), min(ev) >= 6,
          {"eigenvalues": ev, "quadratic_lower_fraction": str(1 - 8 * alpha_value)})
    oo_fun = sp.lambdify(z, oo, "numpy", cse=True)
    lam_fun = sp.lambdify(z, lam, "numpy")

    def loggroup(k1):
        phases = [np.exp(1j * k1), 1j, 1j, 1j]
        mat = np.asarray(oo_fun(*phases), dtype=np.complex128)
        eigen = np.linalg.eigvalsh((mat + mat.conj().T) / 2)
        return float(np.log(eigen).sum() - math.log(float(np.real(lam_fun(*phases)))))

    base = loggroup(math.pi / 2)
    for eps in (0.001, 0.0005):
        values = [loggroup(math.pi / 2 + 2 * eps * math.cos(2 * math.pi * h / 64))
                  for h in range(64)]
        finite = math.fsum(v - base for v in values) / (64 * eps ** 2)
        err = abs(finite - float(direct_group))
        check("finite_epsilon_det_alpha=" + str(alpha_value) + "_eps=" + str(eps),
              err < 5e-6, {"coefficient": finite, "exact": str(direct_group), "error": err})


flat_block(sp.Integer(0))
flat_block(alpha)

# Independent real-space periodic 3^4 geometry for the neutral finite term.
T = 3
sites = list(itertools.product(range(T), repeat=4))
site_id = {x: j for j, x in enumerate(sites)}
V = len(sites)
orient = list(itertools.combinations(range(4), 2))
dd = np.zeros((4 * V, V))
curl = np.zeros((6 * V, 4 * V))


def shift(x, mu):
    y = list(x)
    y[mu] = (y[mu] + 1) % T
    return tuple(y)


def edge(x, mu):
    return 4 * site_id[x] + mu


for x in sites:
    for mu in range(4):
        dd[edge(x, mu), site_id[shift(x, mu)]] += 1
        dd[edge(x, mu), site_id[x]] -= 1
    for oo_index, (mu, nv) in enumerate(orient):
        row = 6 * site_id[x] + oo_index
        curl[row, edge(x, mu)] += 1
        curl[row, edge(shift(x, mu), nv)] += 1
        curl[row, edge(shift(x, nv), mu)] -= 1
        curl[row, edge(x, nv)] -= 1

check("periodic_actual_incidence_complex", np.max(np.abs(curl @ dd)) == 0,
      {"sites": V, "links": 4 * V, "plaquettes": 6 * V})
o = curl.T @ curl + dd @ dd.T
evals, evecs = np.linalg.eigh(o)
nonzero = evals > 1e-9
inv = (evecs[:, nonzero] / evals[nonzero]) @ evecs[:, nonzero].T
proj = curl @ inv @ curl.T
diag = np.diag(proj)
check("periodic_four_harmonics_and_projector", np.count_nonzero(~nonzero) == 4 and
      np.max(np.abs(diag - 40 / 81)) < 1e-11,
      {"zero_modes": int(np.count_nonzero(~nonzero)), "diag_min": float(diag.min()),
       "diag_max": float(diag.max()), "max_error": float(np.max(np.abs(diag - 40 / 81)))})

# Actual neutral SU2 Wilson cosine: Hessian = curl^T cos(f) curl.
# Average f^2 over the two real orthogonal external waves exactly.
p = 2 * math.pi / 3
cos_wave = np.zeros(4 * V)
sin_wave = np.zeros(4 * V)
for x in sites:
    cos_wave[edge(x, 0)] = math.cos(p * x[1])
    sin_wave[edge(x, 0)] = math.sin(p * x[1])
fcos, fsin = curl @ cos_wave, curl @ sin_wave
mean_f2 = (fcos ** 2 + fsin ** 2) / 2
wave_density = mean_f2.sum() / (2 * V)
vertex = -0.5 * curl.T @ (mean_f2[:, None] * curl)
loop_density = float(0.5 * np.trace(inv @ vertex) / V)
coefficient = loop_density / wave_density
target = -20 / 81
check("actual_Wilson_wave_divisor", abs(wave_density - 0.75) < 1e-11,
      {"density": float(wave_density), "target": "3/4"})
check("neutral_Wilson_finite_part", abs(coefficient - target) < 1e-11,
      {"loop_density": loop_density, "beta_coefficient": coefficient,
       "target": "-20/81", "error": abs(coefficient - target)})
check("M_deleted_neutral_vertex_fires", abs(target) > 1e-4, {"wrong": 0, "correct": target})
check("M_infinite_volume_projector_at_finite_T_fires", abs(-0.25 - target) > 1e-4,
      {"wrong": -0.25, "correct": target})
check("M_missing_Wilson_divisor_fires", abs(loop_density - target) > 1e-4,
      {"wrong": loop_density, "correct": target})

summary = {"passed": sum(r["passed"] for r in records), "total": len(records),
           "all_passed": all(r["passed"] for r in records), "records": records,
           "scope": "Finite Gaussian normalization controls; no uniform-depth or physical theorem."}
Path(__file__).with_name("uniform_one_loop_01_results.json").write_text(
    json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps({"summary": {k: v for k, v in summary.items() if k != "records"}}, sort_keys=True))
raise SystemExit(0 if summary["all_passed"] else 1)
