#!/usr/bin/env python3
"""Reproducible synthetic controls for a conditional scalar reconstruction.

The note contains the general proofs. These checks exercise identities,
solutions, bounds and explicit functions; they are not empirical validation.
Repository reads: imported helper; note/helper bytes for integrity only.
Writes: outputs/scalar_observation_inverse.json. Cache is written externally
by runner_cache.execute_and_write_cache, which pins this runner as well.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "scripts/scalar_observation_inverse_math.py",
    "docs/SCALAR_OBSERVATION_INVERSE_AND_INPUT_BOUNDS_NOTE_2026-10-16.md",
)

import hashlib
import json
import platform
from pathlib import Path
import sys

import mpmath as mp
import sympy as s

from scalar_observation_inverse_math import (
    bin_lower_bound, dust_family, observation_parts, primitive_bound,
    sphere_transport_profile, spherical_geometry, vacuum_inverse,
)

ROOT = Path(__file__).resolve().parents[1]
checks = []


def reduce(expr):
    return s.factor(s.cancel(s.together(expr)))


def zero(name, expr, family):
    value = reduce(expr)
    checks.append({"name": name, "family": family, "ok": value == 0, "residual": str(value)})


def truth(name, value, family, **evidence):
    checks.append({"name": name, "family": family, "ok": bool(value), **evidence})


r, b, p, C, f, k, rho = s.symbols("r b p C f k rho", positive=True)
N, B = s.Function("N")(r), s.Function("B")(r)
u, om, W = vacuum_inverse(r, N, B)
ellp = s.diff(N, r) / N
y = 1 / r - ellp
integrated_slope = -s.diff(y, r) / y - 2 / r - ellp - s.diff(B, r) / (2 * B) + 1 / (B * y * r**2)
zero("general lower-derivative transport", u - integrated_slope, "vacuum_geometry")

# Exact independent power-metric identities, including the scalar equation.
up, op, wp = [reduce(x) for x in vacuum_inverse(r, r**p, b)]
c = (b * p**2 - b + 1) / (b * (1 - p))
zero("power metric scalar exponent", up - c / r, "vacuum_geometry")
u0, o0, w0 = [reduce(x) for x in vacuum_inverse(r, 1, b)]
c0 = (1 - b) / b
zero("constant-lapse kinetic function", o0 - (1 - c0) / c0, "vacuum_geometry")
zero("constant-lapse potential ratio", w0 + b * c0 * (c0 + 1) / (2 * r**2), "vacuum_geometry")
for bb, cc in ((s.Rational(1, 2), 1), (s.Rational(1, 3), 4)):
    exponent = (1 - bb) / bb
    profile = cc * r**exponent
    omega = (1 - exponent) / exponent
    potential = -bb * exponent * (exponent + 1) * cc**(2 / exponent) * f**(1 - 2 / exponent) / 2
    Z = omega / f
    fp = s.diff(profile, r)
    box = bb * (s.diff(profile, r, 2) + 2 * fp / r)
    curvature = 2 * (1 - bb) / r**2
    scalar = curvature / 2 + Z.subs(f, profile) * box + s.diff(Z, f).subs(f, profile) * bb * fp**2 / 2 - s.diff(potential, f).subs(f, profile)
    zero(f"direct vacuum scalar equation b={bb}", scalar, "vacuum_geometry")

# Pull back to a general increasing record label without inserting a profile.
z = s.symbols("z", positive=True)
rr, RR, BB = [s.Function(n)(z) for n in ("radius", "clock", "radial")]
q = s.diff(rr, z)
dr = lambda a: s.diff(a, z) / q
lp = dr(RR) / RR
gt = (BB - 1) / rr**2 + dr(BB) / rr
ga = BB * (dr(lp) + lp**2 + lp / rr) + dr(BB) * (lp + 1 / rr) / 2
transport = (ga - gt) / (BB * (1 / rr - lp))
P = q / (RR * s.sqrt(BB))
O = s.sqrt(RR * dr(RR) / rr)
E, J = observation_parts(rr, q, RR, P, O)
zero("general observation pullback from angular equation", s.diff(E, z) + J - q * transport, "observation_pullback")
Rr, Pp, qq, rad, Oo, h = s.symbols("Rr Pp qq rad Oo h", positive=True)
E1, J1 = observation_parts(rad, qq, Rr, Pp, Oo)
E2, J2 = observation_parts(rad, h * qq, Rr, h * Pp, Oo)
zero("relabeling integral density", J2 - h * J1, "observation_pullback")
zero("relabeling endpoint ratio", s.exp(E2 - E1).simplify() - 1, "observation_pullback")
rate = s.symbols("rate", positive=True)
rp = s.exp(rate * z)
Ep, Jp = observation_parts(rp, s.diff(rp, z), rp**p, s.diff(rp, z) / (rp**p * s.sqrt(b)), s.sqrt(p) * rp**(p - 1))
zero("nonlinear-label power metric", s.diff(Ep, z) + Jp - c * rate, "observation_pullback")
turn, emitted = s.symbols("turn emitted", positive=True)
zero("static coherent carrier turnaround", (emitted / Rr) * turn * Rr / emitted - turn, "observation_pullback")

# Derive dust equations from the material Lagrangian before taking its state.
Bd, F, Z, V = dust_family(r, f, k, rho, C)
Ad = 2 * k * C - rho
gtd, grd, gad, _ = spherical_geometry(r, 1, Bd)
for name, residual in (("time", gtd + 3 * k), ("radial", grd + k), ("angular", gad + k)):
    zero("dust metric compared with Cartesian curvature: " + name, residual, "vacuum_geometry")
N0, lam, Tt, Tr = s.symbols("N0 lam Tt Tr", positive=True)
X = -Tt**2 / N0**2 + Bd * Tr**2
Lm = -lam * (X + 1) / 2
chosen = {N0: 1, lam: rho, Tt: 1, Tr: 0}
zero("dust multiplier constraint", s.diff(Lm, lam).subs(chosen), "material_action")
zero("dust temporal stress", (-lam * Tt**2 / N0**2 + Lm).subs(chosen) + rho, "material_action")
zero("dust radial stress", (lam * Bd * Tr**2 + Lm).subs(chosen), "material_action")
zero("dust angular stress", Lm.subs(chosen), "material_action")
t = s.symbols("t")
rootg = N0 * r**2 / s.sqrt(Bd)
zero("dust continuity", s.diff((rootg * s.diff(Lm, Tt)).subs(chosen), t) + s.diff((rootg * s.diff(Lm, Tr)).subs(chosen), r), "material_action")
truth("wrong dust clock rejected", s.diff(Lm, lam).subs({**chosen, Tt: 2}) != 0, "material_action")

# Geometry for this family also follows from Cartesian constant-curvature space:
# g_ij=delta_ij+k*x_i*x_j/B, Ricci_ij=2*k*g_ij, R4=6*k.
# Use that independent curvature here, rather than the helper's Einstein tensor.
fp, fpp = s.diff(F, r), s.diff(F, r, 2)
box = Bd * fpp + (s.diff(Bd, r) / 2 + 2 * Bd / r) * fp
kinetic = Z.subs(f, F) * Bd * fp**2
pot = V.subs(f, F)
equations = {
    "time": -3 * k * F + rho + kinetic / 2 + pot + box,
    "radial": -k * F - kinetic / 2 + pot - Bd * fpp - s.diff(Bd, r) * fp / 2 + box,
    "angular": -k * F + kinetic / 2 + pot - Bd * fp / r + box,
    "scalar": 3 * k + Z.subs(f, F) * box + s.diff(Z, f).subs(f, F) * Bd * fp**2 / 2 - s.diff(V, f).subs(f, F),
}
for name, value in equations.items():
    zero("regular-center full " + name + " equation", value, "material_solution")
zero("known-source affine transport", fp - 2 * k * r * F / Bd + rho * r / Bd, "material_solution")
zero("Cartesian scalar Laplacian", box - 3 * Ad / Bd**2, "material_solution")
zero("center profile", F.subs(r, 0) - C, "material_solution")
zero("center first derivative", fp.subs(r, 0), "material_solution")
zero("center second derivative", fpp.subs(r, 0) - Ad, "material_solution")
zero("Einstein kinetic sign expression", 2 * f * Z + 3 - 3 * rho / (rho - 2 * k * f), "material_solution")
zero("fixed-action center potential slope", s.diff(V, f).subs(f, C) + 6 * k, "material_solution")
zero("potential curvature ratio only", (s.diff(V, f, 2) / Z).subs(f, C) - 4 * k, "material_solution")

chi, Achi = s.symbols("chi Achi", real=True)
sphereF = sphere_transport_profile(chi, k, rho, Achi)
zero("undivided sphere transport", s.trigsimp(2 * k * sphereF - rho - s.sqrt(k) * s.cot(s.sqrt(k) * chi) * s.diff(sphereF, chi)), "sphere_domain")
zero("equator divergent coefficient", (sphereF * s.cos(s.sqrt(k) * chi)**2).expand().subs(chi, s.pi / (2 * s.sqrt(k))) - Achi, "sphere_domain")
Fconst, Vconst = rho / (2 * k), rho / 2
zero("separate constant branch temporal equation", gtd * Fconst + rho + Vconst, "sphere_domain")
zero("separate constant branch spatial equation", grd * Fconst + Vconst, "sphere_domain")
zero("separate constant branch scalar slope", -(gtd + grd + 2 * gad) / 2 - 3 * k, "sphere_domain")

x, yy, H, K = s.symbols("x yy H K", positive=True)
fine = bin_lower_bound([x, yy], [H, K])
coarse = bin_lower_bound([x + yy], [H + K])
zero("exact bin refinement surplus", fine - coarse - (K * x - H * yy)**2 / (H * K * (H + K)), "radar_bins")
aa, width, amplitude = s.symbols("aa width amplitude", positive=True)
iw = width * (2 * aa + width) / 2  # b=a+width, so the bin is ordered.
zero("bin equality profile S=amplitude*r", amplitude**2 * iw - bin_lower_bound([amplitude * iw], [iw]), "radar_bins")
unfactored_integral = ((aa + width)**2 - aa**2) / 2
zero("unfactored positive bin integral", bin_lower_bound([x], [unfactored_integral]) - x**2 / iw, "radar_bins")
for invalid_integral in (0, -1, s.symbols("unknown_sign", real=True)):
    try:
        bin_lower_bound([1], [invalid_integral])
        rejected_bin = False
    except ValueError:
        rejected_bin = True
    truth("invalid or uncertified bin sign rejected: " + str(invalid_integral), rejected_bin, "radar_bins")

# High-precision functional comparisons use analytic, never grid-max, envelopes.
mp.mp.dps = 45
fmt = lambda a: mp.nstr(a, 30)


def channels(ar, aR, aO, aP):
    return lambda z: (1 + z + ar * z * (1 - z), 1 + ar * (1 - 2 * z),
                      1 + (mp.mpf(".1") + aR) * z,
                      mp.mpf(".12") + aO * mp.sin(mp.pi * z),
                      1 + mp.mpf(".2") * z + aP * mp.cos(2 * mp.pi * z))


def log_functional(fun):
    def endpoint(z):
        r, q, R, O, P = fun(z)
        return mp.log(P / q / r / (R**2 - r**2 * O**2)) + 2 * mp.log(R)
    def integrand(z):
        r, q, R, O, P = fun(z)
        return R**4 * P**2 / (q * r * (R**2 - r**2 * O**2))
    return endpoint(1) - endpoint(0) + mp.quad(integrand, [0, mp.mpf(".5"), 1])


baseline = log_functional(channels(0, 0, 0, 0))
for values in ((".002", ".002", ".003", ".004"), ("-.003", "-.004", "-.002", "-.006"),
               ("0", ".005", "0", "0"), (".003", "0", "0", "0"),
               ("0", "0", ".005", "0"), ("0", "0", "0", ".005")):
    ar, aR, aO, aP = map(mp.mpf, values)
    lower = dict(r=mp.mpf(1), R=mp.mpf(1), q=1 - abs(ar), P=1 - abs(aP))
    upper = dict(r=2 + abs(ar) / 4, R=mp.mpf("1.1") + abs(aR), O=mp.mpf(".12") + abs(aO), P=mp.mpf("1.2") + abs(aP))
    lower["D"] = lower["R"]**2 - upper["r"]**2 * upper["O"]**2
    error = dict(r=abs(ar) / 4, R=abs(aR), O=abs(aO), q=abs(ar), P=abs(aP))
    bound, _ = primitive_bound(lower, upper, error, 1)
    actual = abs(log_functional(channels(ar, aR, aO, aP)) - baseline)
    truth("analytic-envelope primitive perturbation " + str(values), actual <= bound, "primitive_error", actual=fmt(actual), bound=fmt(bound))

# A small positive D makes missing the shared-clock contribution detectable.
small = mp.mpf(".001")
Rlo, Rhi = mp.mpf(1), mp.mpf("1.001")
lower = dict(r=mp.mpf(1), R=Rlo, q=mp.mpf(1), P=mp.mpf(1), D=small)
upper = dict(r=mp.mpf(1), R=Rhi, O=mp.sqrt(1 - small), P=mp.mpf(1))
error = dict(r=mp.mpf(0), R=Rhi - Rlo, O=mp.mpf(0), q=mp.mpf(0), P=mp.mpf(0))
bound, eD = primitive_bound(lower, upper, error, mp.mpf(".1"))
actual = mp.mpf(".1") * abs(Rhi**4 / (Rhi**2 - upper["O"]**2) - Rlo**4 / small)
truth("shared clock dependence near positive D margin", actual <= bound, "primitive_error", actual=fmt(actual), bound=fmt(bound), eD=fmt(eD), scope="rational functional control, not an asserted radius trajectory")
try:
    primitive_bound({**lower, "D": 0}, upper, error, 1)
    rejected = False
except ValueError:
    rejected = True
truth("zero D margin rejected", rejected, "primitive_error")

truth("strict and refined constant-slowness bounds", mp.mpf(2) / 3 < mp.mpf(2) / 5 + mp.mpf(2) / 7 < mp.log(2), "radar_bins")
raw = lambda t: mp.exp(-1 / (1 - 4 * t**2)) if abs(t) < mp.mpf(".5") else mp.mpf(0)
norm = mp.quad(raw, [-mp.mpf(".5"), 0, mp.mpf(".5")])
psi = lambda t: 2 * raw(2 * t) / norm
psi2 = mp.quad(lambda t: psi(t)**2, [-mp.mpf(".25"), 0, mp.mpf(".25")])
normalization = mp.quad(psi, [-mp.mpf(".25"), 0, mp.mpf(".25")])
truth("smooth bump normalization and interior support", abs(normalization - 1) < mp.mpf("1e-38") and psi(mp.mpf(".3")) == 0, "radar_bins")
amp, wide, center = mp.mpf(".05"), mp.mpf(".5"), mp.mpf("1.5")
truth("positive spike baseline", 1 - amp / wide * psi(0) > 0, "radar_bins")
for eps in (mp.mpf(1) / 16, mp.mpf(1) / 64):
    slowness = lambda r: 1 - amp / wide * psi((r - center) / wide) + amp / eps * psi((r - center) / eps)
    points = [1, center - wide / 4, center - eps / 4, center, center + eps / 4, center + wide / 4, 2]
    delta = mp.quad(slowness, points)
    integral = mp.quad(lambda r: slowness(r)**2 / r, points)
    lower_spike = amp**2 * psi2 / (2 * eps)
    truth("positive finite-bin spike " + fmt(eps), abs(delta - 1) < mp.mpf("1e-35") and integral >= lower_spike and slowness(1) == slowness(2) == 1,
          "radar_bins", increment=fmt(delta), integral=fmt(integral), lower=fmt(lower_spike), support=[-0.25, 0.25])

result = {
    "kind": "author conditional mathematical controls",
    "scientific_inputs": "synthetic symbols, exact constants and analytic envelopes in the runner; no empirical data",
    "integrity_reads": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},
    "versions": {"python": platform.python_version(), "sympy": s.__version__, "mpmath": mp.__version__},
    "checks": checks,
    "passed": all(c["ok"] for c in checks),
    "scope": "Conditional local reconstruction, deterministic input bounds and explicit constructions. No fitted or tested physical theory, global completion or stability verdict.",
}
out = ROOT / "outputs/scalar_observation_inverse.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"checks": len(checks), "failures": [c["name"] for c in checks if not c["ok"]], "passed": result["passed"], "receipt": str(out.relative_to(ROOT))}, indent=2))
sys.exit(0 if result["passed"] else 1)
