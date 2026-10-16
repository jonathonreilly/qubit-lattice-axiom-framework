"""Conditional shape envelopes on exposed processed records; no likelihood or gravity fit."""
import csv
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
checks = []


def check(name, condition, **values):
    checks.append(dict(name=name, passed=bool(condition), **values))


def digest(name):
    return hashlib.sha256((HERE / name).read_bytes()).hexdigest()


def solve_shape(s, y, sigma, separation_sigma=None, convex=False):
    """Minimize torque-box multiplier. Positive ordered latent values, no offset fit."""
    s, y, sigma = map(lambda a: np.asarray(a, dtype=float), (s, y, sigma))
    assert len(s) == len(y) == len(sigma) and np.all(sigma > 0)
    if separation_sigma is None:
        positions, assignment = np.unique(s, return_inverse=True)
    else:
        positions, assignment = s, np.arange(len(s))
        separation_sigma = np.asarray(separation_sigma, dtype=float)
        assert not convex and np.all(separation_sigma >= 0)
    count = len(positions)
    rows, bounds, labels = [], [], []

    def add(coefficients, bound, label):
        row = np.zeros(count + 1)
        for index, value in coefficients.items():
            row[index] = value
        rows.append(row); bounds.append(bound); labels.append(label)

    for j, index in enumerate(assignment):
        add({int(index): 1., count: -sigma[j]}, y[j], f"data_upper:{j}")
        add({int(index): -1., count: -sigma[j]}, -y[j], f"data_lower:{j}")
    if separation_sigma is None:
        for i in range(count-1):
            add({i: -1., i+1: 1.}, 0., f"decrease:{i}:{i+1}")
        if convex:
            for i in range(count-2):
                dl, dr = positions[i+1]-positions[i], positions[i+2]-positions[i+1]
                # Positive multiple of slope_left - slope_right <= 0.
                add({i: -dr/(dl+dr), i+1: 1., i+2: -dl/(dl+dr)},
                    0., f"convex:{i}:{i+1}:{i+2}")
    else:
        for i in range(count):
            for j in range(count):
                if s[i]+separation_sigma[i] < s[j]-separation_sigma[j]:
                    add({i: -1., j: 1.}, 0., f"interval_decrease:{i}:{j}")
    A, b = np.asarray(rows), np.asarray(bounds)
    objective = np.zeros(count+1); objective[-1] = 1.
    result = linprog(objective, A_ub=A, b_ub=b, bounds=(0., None), method="highs",
                     options={"dual_feasibility_tolerance": 1e-9,
                              "primal_feasibility_tolerance": 1e-9})
    if not result.success:
        raise RuntimeError(f"shape LP failed: {result.status}: {result.message}")
    x = result.x
    slack = b-A@x
    dual = result.ineqlin.marginals
    reduced = objective-A.T@dual
    dual_objective = b@dual  # Bounds are all zero; no omitted nonzero bound term.
    metrics = {
        "primal_violation": float(max(0., -np.min(slack), -np.min(x))),
        "dual_violation": float(max(0., np.max(dual), -np.min(reduced))),
        "duality_gap": float(abs(objective@x-dual_objective)),
        "constraint_complementarity": float(np.max(abs(dual*slack))),
        "bound_complementarity": float(np.max(abs(reduced*x))),
    }
    residual = (x[assignment]-y)/sigma
    return {
        "k": float(x[-1]), "dual_objective": float(dual_objective),
        "status": int(result.status), "message": result.message,
        "positions_um": positions.tolist(), "latent_values_fNm": x[:-1].tolist(),
        "assignment": assignment.tolist(), "row_latent_fNm": x[assignment].tolist(),
        "row_standardized_residual": residual.tolist(),
        "constraints": [{"label": lab, "slack": float(sl), "dual": float(d)}
                        for lab, sl, d in zip(labels, slack, dual)],
        "active_constraints": [lab for lab, sl in zip(labels, slack) if abs(sl) < 1e-8],
        "active_nonnegative_bounds": [int(i) for i, v in enumerate(x) if abs(v) < 1e-8],
        "reduced_costs": reduced.tolist(), "numerical_certificate": metrics,
        "certificate_status": "Floating primal/dual diagnostics; not certified intervals",
    }


def monotone_closed_form(s, y, sigma, separation_sigma=None):
    """Exact pair-obstruction formula for the transitive order used above."""
    answer = max(0., max(-y/sigma))
    witness = {"type": "nonnegative", "row": int(np.argmax(-y/sigma))}
    if answer == 0:
        witness = {"type": "zero"}
    for i in range(len(s)):
        for j in range(len(s)):
            ordered = (s[i] <= s[j] if separation_sigma is None else
                       s[i]+separation_sigma[i] < s[j]-separation_sigma[j])
            if ordered:
                lower = (y[j]-y[i])/(sigma[i]+sigma[j])
                if lower > answer:
                    answer = float(lower)
                    witness = {"type": "pair", "earlier_row": i, "later_row": j}
    return {"k": float(answer), "witness": witness}


# Direct positive-measure identities, independent of any optimizer.
q = np.array([0., .3, 1.7, 4.])
weight = np.array([.2, 1.3, .7, .1])
for d in [.1, .7, 2.]:
    moments = [float(np.dot(weight*q**p, np.exp(-q*d))) for p in range(7)]
    for p, value in enumerate(moments):
        check(f"positive signed derivative {d}:{p}", value >= 0.)
    determinant = moments[0]*moments[2]-moments[1]**2
    direct = .5*sum(weight[i]*weight[j]*(q[i]-q[j])**2*np.exp(-d*(q[i]+q[j]))
                    for i in range(4) for j in range(4))
    check(f"logconvex identity {d}", abs(determinant-direct) < 1e-13)
    for h in [.15, .8]:
        # A shifted positive measure is equivalent to changing the common zero.
        shift, gain = .23, 2.4
        shifted = gain*weight*np.exp(-q*shift)
        for p in range(1, 6):
            import math
            signed_diff = sum((-1)**j*math.comb(p, j)
                              *np.dot(shifted, np.exp(-q*(d+j*h))) for j in range(p+1))
            integral = np.dot(shifted*np.exp(-q*d), (1-np.exp(-q*h))**p)
            check(f"finite difference {d}:{h}:{p}", abs(signed_diff-integral) < 1e-12
                  and integral >= 0.)

# Signed cross weights defeat positivity, even without a wrong propagator.
signed = np.array([1., -2.])
sq = np.array([1., 2.])
check("signed measure negative at origin", np.sum(signed) < 0.)
check("signed measure increasing near origin", -np.dot(signed, sq) > 0.)
for d in [.2, 1.1]:
    k = np.linspace(.01, 6., 101)
    R = np.sin(k)/(1+k*k)
    ea = .12*np.cos(2*k)/(1+k*k)
    eb = -.17*np.sin(3*k)/(1+k*k)
    for p in range(5):
        w = k**p*np.exp(-k*d)/(1+k)
        norm = lambda z: np.sqrt(np.dot(w, z*z))
        error = abs(np.dot(w, (R+ea)*(R+eb)-R*R))
        bound = norm(R)*(norm(ea)+norm(eb))+norm(ea)*norm(eb)
        check(f"mismatch weighted bound {d}:{p}", error <= bound+1e-13,
              error=float(error), bound=float(bound))

# Analytically known cone cases. No measured rows used in these controls.
synthetics = [
    ("positive Laplace", [0., 1., 2., 3.], (2*np.exp(-np.arange(4))).tolist(),
     [1., 1., 1., 1.], False, 0.),
    ("order reversal", [0., 1.], [1., 3.], [1., 1.], False, 1.),
    ("negative values", [0., 1.], [-2., -1.], [1., 1.], False, 2.),
    ("duplicate central position", [0., 0., 1.], [1., 3., 0.], [1., 1., 1.], False, 1.),
    ("decreasing concave", [0., 1., 2.], [3., 3., 0.], [1., 1., 1.], True, .75),
    ("unequal spacing convex", [0., .5, 2.], [4., 3., 0.], [1., 1., 1.], True, 0.),
]
for name, s, y, sig, convex, target in synthetics:
    output = solve_shape(s, y, sig, convex=convex)
    check(f"synthetic LP {name}", abs(output['k']-target)<1e-8,
          expected=target, actual=output['k'])
    for key, value in output["numerical_certificate"].items():
        check(f"synthetic certificate {name}:{key}", value<1e-7, residual=value)
for intervals, target in [([0., 0.], 1.), ([2., 2.], 0.)]:
    out = solve_shape([0., 1.], [1., 3.], [1., 1.], intervals)
    check(f"interval order {intervals}", abs(out['k']-target)<1e-9)

# Development records: every printed run, each channel, no selective exclusions.
with (HERE/"LEE2020_APPENDIX_A1_v1.csv").open(newline="") as file:
    records = list(csv.DictReader(file))
assert len(records) == 95
s = np.array([float(r['separation_um']) for r in records])
ss = np.array([float(r['separation_sigma_um']) for r in records])
development = {}
for channel in ("N120", "N18", "N54"):
    y = np.array([float(r[channel+"_fNm"]) for r in records])
    sig = np.array([float(r[channel+"_sigma_fNm"]) for r in records])
    outputs = {}
    for mode in ("central_monotone", "central_convex", "interval_monotone_relaxation"):
        out = solve_shape(s, y, sig, ss if mode.startswith("interval") else None,
                          convex=mode == "central_convex")
        for key, value in out["numerical_certificate"].items():
            check(f"development solver {channel}:{mode}:{key}", value<1e-7, residual=value)
        if mode != "central_convex":
            formula = monotone_closed_form(s, y, sig,
                                          ss if mode.startswith("interval") else None)
            check(f"development closed form {channel}:{mode}",
                  abs(formula["k"]-out["k"])<1e-7, error=abs(formula["k"]-out["k"]))
            out["pair_obstruction_formula"] = formula
        outputs[mode] = out
    check(f"nested shape cones {channel}",
          outputs["central_convex"]["k"]+1e-7 >= outputs["central_monotone"]["k"]
          and outputs["central_monotone"]["k"]+1e-7 >=
          outputs["interval_monotone_relaxation"]["k"])
    development[channel] = outputs

output = {
    "author": "/root", "role": "Synthetic support and exposed development diagnostics",
    "source_hashes": {n: digest(n) for n in ("LAB_SHAPE_PLAN_v1.json",
        "LAB_SHAPE_DERIVATION_v1.md", "LEE2020_APPENDIX_A1_v1.csv", Path(__file__).name)},
    "counts": {"checks": len(checks), "passed": sum(c["passed"] for c in checks),
               "failed": sum(not c["passed"] for c in checks)},
    "checks": checks, "records": records, "development": development,
    "empirical_validation": False,
    "limits": ["Not a likelihood, significance, exclusion, or independent empirical test.",
               "Necessary shape conditions only; actual unequal apparatus patterns and changing positions are not certified in this class.",
               "Printed marginal sigmas are not joint deterministic bounds.",
               "Data already phase-aligned, calibrated and systematics-corrected.",
               "The interval-only relaxation does not assert a compatible global position assignment."]
}
print(json.dumps(output, indent=2, sort_keys=True, allow_nan=False))
if output["counts"]["failed"]:
    raise SystemExit(1)

