#!/usr/bin/env python3
"""Independent referee for deferred-20260924-transport a1.

The re-draw multipliers and the viscous operator are recomputed. The
attempt's script is not imported. The 200000-sample re-draw and the
historical creeping-flow ratios were not repeated.
"""
from __future__ import annotations

import sys

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


cosine, angle = sp.symbols("c theta", real=True)
pole = sp.Matrix([0, 0, 1])
partner = sp.Matrix([sp.sqrt(1 - cosine ** 2), 0, cosine])
total = pole + partner
difference = pole - partner
cross = pole.cross(partner)
speed = sp.sqrt(sp.simplify((total.T * total)[0]))
redrawn = total / 2 + sp.cos(angle) * difference / 2 - sp.sin(angle) * cross / speed
on_class = sp.simplify((redrawn.T * redrawn)[0] - 1) == 0 and sp.simplify((redrawn.T * total)[0] - (speed ** 2) / 2) == 0
averaged = (
    total * total.T / 4
    + difference * difference.T / 8
    + cross * cross.T / (2 * (total.T * total)[0])
)
reconstructed = (1 - cosine) / 4 * sp.eye(3) + (1 + 3 * cosine) / (8 * (1 + cosine)) * total * total.T
check(
    "E1 redraw",
    on_class and sp.simplify(averaged - reconstructed) == sp.zeros(3),
    "the circle average is (1-c)/4 I + (1+3c)/(8(1+c)) P P^T, and the redrawn vector stays on the momentum class",
)

harmonic = []
for degree in range(0, 9):
    chord = (1 + cosine) / 2 + (1 - cosine) / 2 * sp.cos(angle)
    direct = sp.integrate(sp.integrate(sp.legendre(degree, chord), (angle, 0, 2 * sp.pi)) / (2 * sp.pi), (cosine, -1, 1))
    radial = 4 * sp.integrate(sp.symbols("u") * sp.legendre(degree, sp.symbols("u")) ** 2, (sp.symbols("u"), 0, 1))
    harmonic.append((sp.nsimplify(direct), sp.nsimplify(radial)))
values = [item[1] for item in harmonic]
bound_ok = all(
    sp.Rational(4, 2 * degree + 1) - 4 * sp.integrate(sp.symbols("u") * sp.legendre(degree, sp.symbols("u")) ** 2, (sp.symbols("u"), 0, 1)) > 0
    for degree in range(2, 21)
)
check(
    "E2 multipliers",
    all(left == right for left, right in harmonic)
    and values[:6] == [2, 1, sp.Rational(1, 2), sp.Rational(3, 8), sp.Rational(9, 32), sp.Rational(15, 64)]
    and bound_ok
    and all(value < sp.Rational(4, 5) for value in values[2:]),
    "a_l = 4 int_0^1 u P_l(u)^2 du equals 2, 1, 1/2, 3/8, 9/32, 15/64, and a_l < 4/(2l+1) through l = 20",
)

azimuth, polar, phase = sp.symbols("alpha beta psi", real=True)
entries = sp.symbols("b11 b22 b12 b13 b23", real=True)
matrix = sp.Matrix(
    [
        [entries[0], entries[2], entries[3]],
        [entries[2], entries[1], entries[4]],
        [entries[3], entries[4], -entries[0] - entries[1]],
    ]
)
first = sp.Matrix([sp.sin(azimuth) * sp.cos(polar), sp.sin(azimuth) * sp.sin(polar), sp.cos(azimuth)])
east = sp.Matrix([sp.cos(azimuth) * sp.cos(polar), sp.cos(azimuth) * sp.sin(polar), -sp.sin(azimuth)])
north = sp.Matrix([-sp.sin(polar), sp.cos(polar), 0])
second = cosine * first + sp.sqrt(1 - cosine ** 2) * (sp.cos(phase) * east + sp.sin(phase) * north)
momentum = first + second
circle = sp.integrate(sp.expand((momentum.T * matrix * momentum)[0]), (phase, 0, 2 * sp.pi)) / (2 * sp.pi)
target = (first.T * matrix * first)[0] * (1 + cosine) * (1 + 3 * cosine) / 2
weight = sp.integrate((1 + 3 * cosine) ** 2 / 16, (cosine, -1, 1)) / 2
check(
    "E3 stress",
    sp.simplify(sp.expand(sp.expand_trig(circle - target))) == 0 and weight == sp.Rational(1, 4) and 2 * weight == sp.Rational(1, 2),
    "every traceless symmetric stress has circle average (1+c)(1+3c)/2, and the pair average is 1/4, so a_2 = 1/2",
)

sx, sy, sz = sp.symbols("sx sy sz", real=True)
direction = [sx, sy, sz]
polar_angle, azimuth_angle = sp.symbols("TH PH", real=True)
sphere = {
    sx: sp.sin(polar_angle) * sp.cos(azimuth_angle),
    sy: sp.sin(polar_angle) * sp.sin(azimuth_angle),
    sz: sp.cos(polar_angle),
}


def sphere_integral(expression):
    substituted = sp.expand(expression).subs(sphere)
    return sp.simplify(sp.integrate(sp.integrate(substituted * sp.sin(polar_angle), (azimuth_angle, 0, 2 * sp.pi)), (polar_angle, 0, sp.pi)))


coupling, density = sp.symbols("gamma rho", positive=True)
gradient = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"G{i}{j}"))
strain = (gradient + gradient.T) / 2 - sp.eye(3) * gradient.trace() / 3
source = sp.sqrt(3) / (4 * sp.pi) * sum(
    (direction[i] * direction[j] - (sp.Rational(1, 3) if i == j else 0)) * strain[i, j] for i in range(3) for j in range(3)
)
correction = -source / (3 * coupling * density)
stress_ok = True
for i, j in ((0, 0), (0, 1), (1, 2), (2, 2)):
    flux = sphere_integral(direction[i] * direction[j] * correction) / sp.sqrt(3)
    stress_ok = stress_ok and sp.simplify(flux + 2 * strain[i, j] / (45 * coupling * density)) == 0
wave_k = sp.Matrix(sp.symbols("kx ky kz"))
wave_g = sp.Matrix(sp.symbols("gx gy gz"))
wave_gradient = sp.I * wave_k * wave_g.T
wave_strain = (wave_gradient + wave_gradient.T) / 2 - sp.eye(3) * wave_gradient.trace() / 3
force = sp.Matrix([sum(sp.I * wave_k[j] * 2 * wave_strain[i, j] / (45 * coupling * density) for j in range(3)) for i in range(3)])
expected_force = (-(wave_k.dot(wave_k)) * wave_g - wave_k * wave_k.dot(wave_g) / 3) / (45 * coupling * density)
check(
    "E4 viscosity",
    stress_ok and sp.simplify(force - expected_force) == sp.zeros(3, 1),
    "Pi = -(2/(45 gamma rho)) S, and the force is (1/(45 gamma rho))(Laplacian g + (1/3) grad div g)",
)

third = sp.integrate(sp.cos(polar_angle) ** 3 * sp.sin(polar_angle), (polar_angle, 0, sp.pi / 2)) * 2 * 2 * sp.pi / (4 * sp.pi)
mixed = (
    sp.integrate(
        sp.integrate(sp.sin(polar_angle) ** 3 * sp.cos(polar_angle) * sp.cos(azimuth_angle) ** 2, (polar_angle, 0, sp.pi / 2)) * 2,
        (azimuth_angle, 0, 2 * sp.pi),
    )
    / (4 * sp.pi)
)
lattice = sp.simplify(3 / (2 * sp.sqrt(3)) * mixed)
check(
    "E5 lattice",
    third == sp.Rational(1, 4)
    and mixed == sp.Rational(1, 8)
    and sp.simplify(lattice - sp.sqrt(3) / 16) == 0
    and sp.simplify(3 / (2 * sp.sqrt(3)) * (third - mixed) - lattice) == 0,
    "<|s_z|^3> = 1/4 and <s_x^2 |s_z|> = 1/8, so both lattice coefficients equal sqrt(3)/16",
)

rate = sp.symbols("x", positive=True)
collision = 1 / (45 * rate)
weight_eta = sp.simplify(lattice / (lattice + collision))
closed = 45 * sp.sqrt(3) * rate / (45 * sp.sqrt(3) * rate + 16)
low = weight_eta.subs(rate, sp.Rational(1, 5))
high = weight_eta.subs(rate, sp.Rational(3, 10))
wavenumber = sp.symbols("k", positive=True)
axis_wave = sp.Matrix([wavenumber, 0, 0])
axis_flow = sp.Matrix([0, 1, 0])
diagonal_wave = sp.Matrix([wavenumber, wavenumber, 0]) / sp.sqrt(2)
diagonal_flow = sp.Matrix([1, -1, 0]) / sp.sqrt(2)


def damping(wave, flow):
    cubic = lattice * sp.Matrix([wave[i] ** 2 * flow[i] for i in range(3)])
    isotropic = (lattice + collision) * (wave.dot(wave)) * flow + collision / 3 * wave * wave.dot(flow)
    operator = isotropic + cubic
    return sp.simplify((flow.dot(operator)) / (flow.dot(flow)))


axis_rate = damping(axis_wave, axis_flow)
diagonal_rate = damping(diagonal_wave, diagonal_flow)
bulk = sp.simplify((collision / 3) / (1 / (135 * rate)) - 1)
check(
    "E6 mixing",
    sp.simplify(weight_eta - closed) == 0
    and sp.simplify(sp.diff(weight_eta, rate) - 720 * sp.sqrt(3) / (45 * sp.sqrt(3) * rate + 16) ** 2) == 0
    and sp.limit(weight_eta, rate, sp.oo) == 1
    and sp.limit(weight_eta, rate, 0) == 0
    and sp.limit(weight_eta / rate, rate, 0) == 45 * sp.sqrt(3) / 16
    and 0 < low < 1
    and 0 < high < 1
    and abs(float(low) - 0.4935) < 5e-5
    and abs(float(high) - 0.5937) < 5e-5
    and sp.simplify(axis_rate - (lattice + collision) * wavenumber ** 2) == 0
    and sp.simplify(diagonal_rate - axis_rate - lattice * wavenumber ** 2 / 2) == 0
    and bulk == 0,
    "eta = 45 sqrt(3) gamma rho/(45 sqrt(3) gamma rho + 16), about 0.4935 and 0.5937 at the two quoted points, and the diagonal excess is nu_lat k^2/2",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. The re-draw multipliers are 2, 1, 1/2, 3/8, 9/32, 15/64, and every l >= 2 is below "
    "4/(2l+1). The five second harmonics share a_2 = 1/2, so the stress relaxes at 3 gamma rho. The collisional force is "
    "(1/(45 gamma rho))(Laplacian g_i + (1/3) partial_i div g), and the lattice term is (sqrt(3)/16)(Laplacian g_i + "
    "partial_i^2 g_i). Their mixture has eta = 45 sqrt(3) gamma rho/(45 sqrt(3) gamma rho + 16) strictly between 0 and 1. "
    "A face-diagonal transverse wave decays faster than an axial one by (sqrt(3)/32) k^2. The sampled re-draw, the "
    "historical ratios, finite-density transfer, and block 51's curl obstruction were not re-proved.",
    flush=True,
)
print(
    "HIT: confirmed - collisions restore a first-harmonic local law, but the viscosity they add is isotropic, "
    "1/(45 gamma rho), so the lattice weight eta stays in (0, 1) at every finite gamma rho",
    flush=True,
)
