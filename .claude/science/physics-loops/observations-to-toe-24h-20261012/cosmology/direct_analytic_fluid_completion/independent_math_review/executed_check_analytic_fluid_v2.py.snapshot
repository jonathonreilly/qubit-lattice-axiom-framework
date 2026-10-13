#!/usr/bin/env python3
"""Independent exact checks of the frozen handwritten three-field candidate.

No author implementation is imported or executed.  The metric connection and
equations are reconstructed by differentiation, with s=sqrt(a)>0.  An actual
failed assertion records the omitted repeated-root u solution at nu=9/4.
V2 factors before simplification, retaining D>0 in a perfect-square radical.
The original v1 radical-simplification failure remains preserved unchanged.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as S


ROOT = Path(__file__).resolve().parent
checks = []


def zero(label, expression):
    residual = S.factor(S.simplify(S.factor(expression)))
    checks.append({"name": label, "pass": residual == 0, "residual": str(residual)})


def predicate(label, passed, evidence):
    checks.append({"name": label, "pass": bool(passed), "evidence": evidence})


s, hv, nu, H = S.symbols("s hv nu H", positive=True)
u, x, y = q = S.symbols("u x y", real=True)
vu, vx, vy = vv = S.symbols("vu vx vy", real=True)
sigma, rad = S.symbols("sigma rad", nonnegative=True)
v = S.Matrix(vv)
D = 1 + S.Rational(2, 3) * (1 + s**2) * (x**2 + y**2)
K = S.diag(1, 4 * s**2 / (9 * D), s**2 / (3 * D))
Ki = K.inv()
f = s**2 / 2 - s * u + 2 * u**2
V = hv**2 * (S.Rational(3, 2) + f * x**2 + s**2 * y**2 / 3 + nu * u**2 / 2)
gradV = S.Matrix([S.diff(V, z) for z in q])
Gamma = [[[S.factor(sum(Ki[i, l] * (S.diff(K[l, j], q[k]) + S.diff(K[l, k], q[j]) - S.diff(K[j, k], q[l])) / 2 for l in range(3))) for k in range(3)] for j in range(3)] for i in range(3)]
expected = {}
dx, dy = S.diff(D, x) / D, S.diff(D, y) / D
expected[1, 1, 1] = -dx / 2
expected[1, 1, 2] = expected[1, 2, 1] = -dy / 2
expected[1, 2, 2] = S.Rational(3, 8) * dx
expected[2, 2, 2] = -dy / 2
expected[2, 1, 2] = expected[2, 2, 1] = -dx / 2
expected[2, 1, 1] = S.Rational(2, 3) * dy
for i in range(3):
    for j in range(3):
        for k in range(3):
            zero(f"connection_{i}{j}{k}", Gamma[i][j][k] - expected.get((i, j, k), 0))


def connection_acc(velocity):
    return S.Matrix([sum(Gamma[i][j][k] * velocity[j] * velocity[k] for j in range(3) for k in range(3)) for i in range(3)])


hb = hv * S.sqrt(D)
vbar = S.Matrix([0, -S.Rational(3, 2) * hb * x, -2 * hb * y])
sigbar, rbar = hv**2 * x**2, hv**2 * y**2
Tbar = S.factor((vbar.T * K * vbar)[0])
Vbar = V.subs(u, 0)
bare_acc = vbar.jacobian(q) * vbar
cov_acc = bare_acc + connection_acc(vbar)
source_bar = S.Matrix([s * sigbar, 0, 0])
kgbar = cov_acc + 3 * hb * vbar + Ki * (gradV.subs(u, 0) + source_bar)
for i in range(3):
    zero(f"full_covariant_KG_exact_branch_{i}", kgbar[i])
zero("exact_branch_kinetic_norm", Tbar - s**2 * (sigbar + 4 * rbar / 3))
zero("exact_branch_friedmann", 3 * hb**2 - 2 * (sigbar + rbar) - Tbar - 2 * Vbar)
hdot = (S.Matrix([S.diff(hb, z) for z in q]).T * vbar)[0]
zero("exact_branch_raychaudhuri", hdot + sigbar + 4 * rbar / 3 + Tbar)
zero("exact_branch_dust_conservation", S.diff(sigbar, x) * vbar[1] + 3 * hb * sigbar)
zero("exact_branch_radiation_conservation", S.diff(rbar, y) * vbar[2] + 4 * hb * rbar)
eta = s**2 / (1 + s**2)
covector = K * vbar
P = Tbar / 2
gradH = S.Matrix([S.diff(hb, z) for z in q])
hessH = S.Matrix(3, 3, lambda i, j: S.diff(hb, q[i], q[j]) - sum(Gamma[k][i][j] * gradH[k] for k in range(3)))
for i in (1, 2):
    zero(f"gradient_covector_{i}", covector[i] + eta * gradH[i])
    dt_covector = sum(S.diff(covector[i], q[j]) * vbar[j] for j in range(3)) - sum(Gamma[k][i][j] * covector[k] * vbar[j] for k in range(3) for j in range(3))
    zero(f"covariant_Hessian_velocity_{i}", dt_covector + eta * (hessH * vbar)[i])
    zero(f"gradient_kinetic_identity_{i}", S.diff(P, q[i]) - dt_covector)
    zero(f"gradient_flow_KG_{i}", S.diff(P + Vbar, q[i]) + 3 * hb * covector[i])
zero("P_plus_V_identity", P + Vbar - S.Rational(3, 2) * hb**2 + hv**2 * (x**2 + y**2))

# Derive the energy balance off the exact trajectory, in proper time.
T = (v.T * K * v)[0]
source = S.Matrix([s * sigma, 0, 0])
acc = -connection_acc(v) - 3 * H * v - Ki * (gradV + source)
sigmadot = (-3 * H + s * vu) * sigma
raddot = -4 * H * rad
Tdot = sum(S.diff(T, q[i]) * v[i] + S.diff(T, vv[i]) * acc[i] for i in range(3))
Edot = Tdot / 2 + (gradV.T * v)[0] + sigmadot + raddot
dissipation = -3 * H * (T + sigma + 4 * rad / 3)
zero("off_trajectory_exchange_energy", Edot - dissipation)
zero("drop_matter_mass_change_residual", Edot - s * vu * sigma - dissipation + s * vu * sigma)
zero("drop_scalar_matter_force_residual", Edot + s * vu * sigma - dissipation - s * vu * sigma)
for label, change in (("omit_mass_change", -s * vu * sigma), ("omit_scalar_force", s * vu * sigma)):
    mutant = S.factor((Edot - dissipation + change).subs({s: S.Rational(1, 10), hv: 1, nu: 1, H: 2, u: S.Rational(1, 3), x: 1, y: S.Rational(1, 2), vu: S.Rational(2, 5), vx: S.Rational(1, 4), vy: -S.Rational(1, 7), sigma: S.Rational(3, 2), rad: S.Rational(1, 3)}))
    predicate(f"mutation_detects_{label}", mutant != 0, {"balance_residual": str(mutant)})

# The displayed coercive inequality is stronger than nonnegativity alone.
lower = hv**2 * (S.Rational(3, 2) + 3 * s**2 * x**2 / 8 + s**2 * y**2 / 3 + nu * u**2 / 2)
zero("coercive_potential_remainder", V - lower - 2 * hv**2 * (u - s / 4)**2 * x**2)
zero("f_strictly_positive_square", f - 2 * (u - s / 4)**2 - 3 * s**2 / 8)
Q = S.symbols("Q", nonnegative=True)
Dmax = 1 + 34 * (1 + s**2) * Q / (9 * s**2)
zero("compact_sublevel_D_bound", Dmax - (1 + S.Rational(2, 3) * (1 + s**2) * (8 * Q / (3 * s**2) + 3 * Q / s**2)))
zero("unique_stationary_u_after_xy_zero", gradV[0].subs({x: 0, y: 0}) - nu * hv**2 * u)

# Pull the proper-time system through v=H*p to reconstruct the N chart.
pu, px, py = pp = S.symbols("pu px py", real=True)
p = S.Matrix(pp)
kp2 = (p.T * K * p)[0]
hn2 = 2 * (sigma + rad + V) / (3 - kp2)
zero("N_friedmann_elimination", 3 * hn2 - hn2 * kp2 - 2 * (sigma + rad + V))
h = -(sigma + 4 * rad / 3) / hn2 - kp2
pn = -(3 + h) * p - connection_acc(p) - Ki * (gradV + source) / hn2
proper_from_N = hn2 * (pn + h * p)
proper_direct = (-connection_acc(v) - 3 * H * v - Ki * (gradV + source)).subs(dict(zip(vv, H * p)))
for i in range(3):
    zero(f"N_proper_time_equivalence_{i}", proper_from_N[i] - proper_direct[i].subs(H**2, hn2))
physical_H2 = (2 * (sigma + rad + V) + T) / 3
zero("positive_N_denominator_identity", 3 - T / physical_H2 - 2 * (sigma + rad + V) / physical_H2)

# Canonical vacuum masses and all homogeneous eigenvalue classes.
origin = {u: 0, x: 0, y: 0}
mass = (Ki * S.hessian(V, q)).subs(origin)
target_mass = hv**2 * S.diag(nu, S.Rational(9, 4), 2)
for i in range(3):
    for j in range(3):
        zero(f"vacuum_mass_{i}{j}", mass[i, j] - target_mass[i, j])
lam = S.symbols("lam")
zero("vacuum_characteristic_polynomial", (lam**2 * S.eye(3) + 3 * hv * lam * S.eye(3) + mass).det() - (lam**2 + 3 * hv * lam + nu * hv**2) * (lam + S.Rational(3, 2) * hv)**2 * (lam + hv) * (lam + 2 * hv))
t = S.symbols("t", real=True)
uplus = S.exp((-3 + S.sqrt(9 - 4 * nu)) * hv * t / 2)
uminus = S.exp((-3 - S.sqrt(9 - 4 * nu)) * hv * t / 2)
for label, mode in (("plus", uplus), ("minus", uminus)):
    zero(f"generic_u_mode_{label}", S.diff(mode, t, 2) + 3 * hv * S.diff(mode, t) + nu * hv**2 * mode)
wronskian = S.det(S.Matrix([[uplus, uminus], [S.diff(uplus, t), S.diff(uminus, t)]]))
critical_W = S.simplify(wronskian.subs(nu, S.Rational(9, 4)))
predicate("SOURCE_FINDING_v1_u_modes_span_critical_nu", critical_W != 0, {"nu": "9/4", "displayed_pair_wronskian": str(critical_W), "missing_solution": "t*exp(-3*hv*t/2)"})
critical_mode = t * S.exp(-3 * hv * t / 2)
zero("corrected_critical_u_mode", S.diff(critical_mode, t, 2) + 3 * hv * S.diff(critical_mode, t) + S.Rational(9, 4) * hv**2 * critical_mode)
corrected_W = S.det(S.Matrix([[S.exp(-3 * hv * t / 2), critical_mode], [S.diff(S.exp(-3 * hv * t / 2), t), S.diff(critical_mode, t)]]))
zero("corrected_critical_u_basis_W", corrected_W - S.exp(-3 * hv * t))
for label, mode, m2 in (("x_critical", t * S.exp(-3 * hv * t / 2), S.Rational(9, 4)), ("y_slow", S.exp(-hv * t), 2), ("y_fast", S.exp(-2 * hv * t), 2)):
    zero(f"vacuum_mode_{label}", S.diff(mode, t, 2) + 3 * hv * S.diff(mode, t) + m2 * hv**2 * mode)
sig0 = S.symbols("sig0", real=True)
siglin = sig0 * S.exp(-3 * hv * t)
upart = -s * siglin / (nu * hv**2)
zero("linear_dust_forced_u_particular", S.diff(upart, t, 2) + 3 * hv * S.diff(upart, t) + nu * hv**2 * upart + s * siglin)
zero("relative_y_slow_growth", S.exp(-hv * t) / S.exp(-2 * hv * t) - S.exp(hv * t))

# Calibration identity; m and omega are nonnegative fractions with sum<1.
h0, m, omega = S.symbols("h0 m omega", positive=True)
hv2cal = h0**2 * (1 - m - omega)
x02 = 3 * m / (2 * (1 + s**2) * (1 - m - omega))
y02 = 3 * omega / (2 * (1 + s**2) * (1 - m - omega))
zero("calibration_H0", hv2cal * (1 + S.Rational(2, 3) * (1 + s**2) * (x02 + y02)) - h0**2)
zero("calibration_dust_term", S.Rational(2, 3) * (1 + s**2) * hv2cal * x02 - h0**2 * m)
zero("calibration_radiation_term", S.Rational(2, 3) * (1 + s**2) * hv2cal * y02 - h0**2 * omega)

result = {
    "method": "SymPy exact differentiation of the field metric/action-derived proper-time system; no author implementation imports",
    "source_file_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "parameterization": "s=sqrt(a)>0; hv>0; nu>0; dimensionless fields; c=1",
    "checks": checks,
    "summary": {"total": len(checks), "passed": sum(c["pass"] for c in checks), "failed": sum(not c["pass"] for c in checks)},
    "exact_connection": {"".join(map(str, key)): str(value) for key, value in expected.items()},
    "scope": "Mathematical verification only. One preserved source-finding failure is intentional evidence, not silently reclassified as a pass.",
}
(ROOT / "EXACT_CHECKS_v2.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result["summary"], sort_keys=True))
for c in checks:
    if not c["pass"]:
        print(json.dumps(c, sort_keys=True))
raise SystemExit(1 if result["summary"]["failed"] else 0)
