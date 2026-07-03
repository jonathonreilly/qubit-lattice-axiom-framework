#!/usr/bin/env python3
"""Exact finite algebraic-sum evaluator for the Route-2 active t_balance row.

The active branch is fixed by the preceding step-free runner:

    eta_floor = |G_xx^TF(phi)| at probe0.

This runner evaluates that one branch without the floating sparse Green solve.
It uses the Dirichlet sine eigenbasis of the 13^3 interior Laplacian and a
separable exact representation of SciPy's cubic `mode="nearest"` interpolation:
edge prepad by 12, rational tridiagonal cubic-spline coefficient solve, then
rational cubic B-spline weights.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 600

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.ndimage import map_coordinates


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "QUARK_ROUTE2_T_BALANCE_EXACT_ALGEBRAIC_VALUE_BOUNDED_NOTE_2026-06-12.md"
PARENT_NOTE = (
    ROOT / "docs" / "QUARK_ROUTE2_ENDPOINT_STEP_FREE_ACTIVE_BRANCH_SLOPES_BOUNDED_NOTE_2026-06-12.md"
)
STEP_FREE_RUNNER = (
    ROOT / "scripts" / "quark_route2_endpoint_step_free_active_branch_slopes_bounded_2026_06_12.py"
)
TENSOR_RUNNER = ROOT / "scripts" / "frontier_tensorial_einstein_regge_completion.py"

N = 13
SIZE = 15
PAD = 12
PADDED = SIZE + 2 * PAD
H = Fraction(1, 25)
CENTER = Fraction(7, 1)
PROBE0 = (Fraction(0), Fraction(17, 4), Fraction(0), Fraction(0))

SUPPORT = (
    (7, 7, 7),
    (8, 7, 7),
    (6, 7, 7),
    (7, 8, 7),
    (7, 6, 7),
    (7, 7, 8),
    (7, 7, 6),
)

NEIGHBORS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)

EXPECTED_STEP_FREE = {
    ("center/e0", "E_x"): mp.mpf("-3.072011837258e-05"),
    ("center/e0", "T1x"): mp.mpf("+2.736190582996e-05"),
    ("shell/s_sqrt6", "E_x"): mp.mpf("-1.637317210303e-05"),
    ("shell/s_sqrt6", "T1x"): mp.mpf("+3.283448931862e-05"),
}
EXPECTED_T_BALANCE_STEP_FREE = mp.mpf("1.000030809474")
EXPECTED_ANCHOR = mp.mpf("8.143540299590e-02")

PASS_COUNT = 0
FAIL_COUNT = 0


@dataclass(frozen=True)
class BranchRow:
    label: str
    direction: str
    value_xx_tf: mp.mpf
    derivative_xx_tf: mp.mpf
    beta: mp.mpf


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    if detail:
        print(f"{tag}: {name} -- {detail}")
    else:
        print(f"{tag}: {name}")


def mpf_fraction(x: Fraction) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def q_vector(label: str) -> list[mp.mpf]:
    z = mp.mpf("0")
    q = [z for _ in range(7)]
    if label == "e0":
        q[0] = mp.mpf(1)
    elif label == "s_unit":
        for idx in range(1, 7):
            q[idx] = mp.mpf(1) / 6
    elif label == "ex":
        q[1] = q[2] = 1 / mp.sqrt(3)
        for idx in range(3, 7):
            q[idx] = -1 / (2 * mp.sqrt(3))
    elif label == "t1x":
        q[1] = 1 / mp.sqrt(2)
        q[2] = -1 / mp.sqrt(2)
    else:
        raise ValueError(label)
    return q


def add_axis(point: tuple[Fraction, ...], axis: int, delta: Fraction) -> tuple[Fraction, ...]:
    out = list(point)
    out[axis] += delta
    return tuple(out)


def interpolation_points(point: tuple[Fraction, ...]) -> list[tuple[Fraction, Fraction, Fraction]]:
    points: list[tuple[Fraction, Fraction, Fraction]] = []

    def add_adm(p: tuple[Fraction, ...]) -> None:
        points.append((p[1], p[2], p[3]))

    def add_christoffel(p: tuple[Fraction, ...]) -> None:
        for axis in range(4):
            add_adm(add_axis(p, axis, H))
            add_adm(add_axis(p, axis, -H))

    add_adm(point)
    add_christoffel(point)
    for axis in range(4):
        add_christoffel(add_axis(point, axis, H))
        add_christoffel(add_axis(point, axis, -H))
    return sorted(set(points))


def shell_mask(point: tuple[int, int, int]) -> bool:
    dx = point[0] - 7
    dy = point[1] - 7
    dz = point[2] - 7
    return dx * dx + dy * dy + dz * dz > 16


def orbit_key(point: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sorted((abs(point[0] - 7), abs(point[1] - 7), abs(point[2] - 7)), reverse=True))


def radius_squared(point: tuple[int, int, int]) -> int:
    return (point[0] - 7) ** 2 + (point[1] - 7) ** 2 + (point[2] - 7) ** 2


def sigma_coeff(point: tuple[int, int, int]) -> dict[tuple[int, int, int], Fraction]:
    coeffs: dict[tuple[int, int, int], Fraction] = {}
    if shell_mask(point):
        coeffs[point] = coeffs.get(point, Fraction(0)) + Fraction(6)
    for di, dj, dk in NEIGHBORS:
        neighbor = (point[0] + di, point[1] + dj, point[2] + dk)
        if shell_mask(neighbor) and all(1 <= coord <= 13 for coord in neighbor):
            coeffs[neighbor] = coeffs.get(neighbor, Fraction(0)) - Fraction(1)
    return coeffs


def anchor_coefficients() -> dict[tuple[int, int, int], Fraction]:
    """Linear functional for the reduced-shell anchor orbit (3,3,0)."""
    active: list[tuple[int, int, int]] = []
    for i in range(1, 14):
        for j in range(1, 14):
            for k in range(1, 14):
                point = (i, j, k)
                masks = [shell_mask(point)]
                masks.extend(shell_mask((i + di, j + dj, k + dk)) for di, dj, dk in NEIGHBORS)
                if any(masks) and not all(masks):
                    active.append(point)

    target_d2 = 18
    target_orbit = (3, 3, 0)
    d2_points = [point for point in active if radius_squared(point) == target_d2]
    orbit_points = [point for point in d2_points if orbit_key(point) == target_orbit]
    radial_factor = Fraction(len(orbit_points), len(d2_points))

    coeffs: dict[tuple[int, int, int], Fraction] = {}
    for point in orbit_points:
        for site, coeff in sigma_coeff(point).items():
            coeffs[site] = coeffs.get(site, Fraction(0)) + coeff
    for point in d2_points:
        for site, coeff in sigma_coeff(point).items():
            coeffs[site] = coeffs.get(site, Fraction(0)) - radial_factor * coeff
    return {site: coeff for site, coeff in coeffs.items() if coeff}


class ExactActiveBranchEvaluator:
    def __init__(self, dps: int) -> None:
        mp.mp.dps = dps
        self.dps = dps
        self.sinv = [[mp.mpf(0) for _ in range(N + 1)] for __ in range(N + 1)]
        self.cosv = [mp.mpf(0) for _ in range(N + 1)]
        for mode in range(1, N + 1):
            self.cosv[mode] = mp.cos(mp.pi * mode / (N + 1))
            for idx in range(1, N + 1):
                self.sinv[mode][idx] = mp.sin(mp.pi * mode * idx / (N + 1))
        self.spline_coeffs = self._build_spline_mode_coeffs()
        self.axis_cache: dict[Fraction, list[mp.mpf]] = {}
        self.mode_weights = {
            label: self._build_mode_weights(label)
            for label in ("e0", "s_unit", "ex", "t1x")
        }
        self.interp_cache: dict[tuple[str, tuple[Fraction, Fraction, Fraction]], mp.mpf] = {}

    def _solve_cubic_coeffs(self, rhs: list[mp.mpf]) -> list[mp.mpf]:
        diag = [mp.mpf(5) / 6] + [mp.mpf(2) / 3] * (PADDED - 2) + [mp.mpf(5) / 6]
        upper = [mp.mpf(1) / 6] * (PADDED - 1)
        lower = [mp.mpf(1) / 6] * (PADDED - 1)
        d = rhs[:]
        for idx in range(1, PADDED):
            w = lower[idx - 1] / diag[idx - 1]
            diag[idx] -= w * upper[idx - 1]
            d[idx] -= w * d[idx - 1]
        out = [mp.mpf(0) for _ in range(PADDED)]
        out[-1] = d[-1] / diag[-1]
        for idx in range(PADDED - 2, -1, -1):
            out[idx] = (d[idx] - upper[idx] * out[idx + 1]) / diag[idx]
        return out

    def _build_spline_mode_coeffs(self) -> dict[int, list[mp.mpf]]:
        coeffs: dict[int, list[mp.mpf]] = {}
        for mode in range(1, N + 1):
            rhs = [mp.mpf(0) for _ in range(PADDED)]
            for idx in range(1, N + 1):
                rhs[PAD + idx] = self.sinv[mode][idx]
            coeffs[mode] = self._solve_cubic_coeffs(rhs)
        return coeffs

    def _build_mode_weights(self, label: str) -> list[list[list[mp.mpf]]]:
        q = q_vector(label)
        out: list[list[list[mp.mpf]]] = []
        for a in range(1, N + 1):
            plane: list[list[mp.mpf]] = []
            for b in range(1, N + 1):
                row: list[mp.mpf] = []
                for c in range(1, N + 1):
                    qhat = mp.mpf(0)
                    for coeff, (i, j, k) in zip(q, SUPPORT):
                        qhat += coeff * self.sinv[a][i] * self.sinv[b][j] * self.sinv[c][k]
                    lam = 6 - 2 * self.cosv[a] - 2 * self.cosv[b] - 2 * self.cosv[c]
                    row.append(qhat / lam)
                plane.append(row)
            out.append(plane)
        return out

    @staticmethod
    def b3(u: mp.mpf) -> mp.mpf:
        u = abs(u)
        if u < 1:
            return mp.mpf(2) / 3 - u * u + u**3 / 2
        if u < 2:
            return (2 - u) ** 3 / 6
        return mp.mpf(0)

    def axis_l(self, coord: Fraction) -> list[mp.mpf]:
        if coord in self.axis_cache:
            return self.axis_cache[coord]
        c = mpf_fraction(coord) + PAD
        floor = int(mp.floor(c))
        js = (floor - 1, floor, floor + 1, floor + 2)
        out = [mp.mpf(0)]
        for mode in range(1, N + 1):
            total = mp.mpf(0)
            coeffs = self.spline_coeffs[mode]
            for j in js:
                jj = min(max(j, 0), PADDED - 1)
                total += coeffs[jj] * self.b3(c - j)
            out.append(total)
        self.axis_cache[coord] = out
        return out

    def interpolate(self, label: str, xyz: tuple[Fraction, Fraction, Fraction]) -> mp.mpf:
        key = (label, xyz)
        if key in self.interp_cache:
            return self.interp_cache[key]
        lx = self.axis_l(CENTER + xyz[0])
        ly = self.axis_l(CENTER + xyz[1])
        lz = self.axis_l(CENTER + xyz[2])
        weights = self.mode_weights[label]
        total = mp.mpf(0)
        for a in range(1, N + 1):
            ax = lx[a]
            plane = weights[a - 1]
            for b in range(1, N + 1):
                ab = ax * ly[b]
                row = plane[b - 1]
                for c in range(1, N + 1):
                    total += ab * lz[c] * row[c - 1]
        self.interp_cache[key] = total / (7**3)
        return self.interp_cache[key]

    def lattice_functional(
        self,
        label: str,
        coeffs: dict[tuple[int, int, int], Fraction],
    ) -> mp.mpf:
        weights = self.mode_weights[label]
        total = mp.mpf(0)
        for a in range(1, N + 1):
            plane = weights[a - 1]
            for b in range(1, N + 1):
                row = plane[b - 1]
                for c in range(1, N + 1):
                    lhat = mp.mpf(0)
                    for (i, j, k), coeff in coeffs.items():
                        lhat += (
                            mpf_fraction(coeff)
                            * self.sinv[a][i]
                            * self.sinv[b][j]
                            * self.sinv[c][k]
                        )
                    total += lhat * row[c - 1]
        return total / (7**3)

    @staticmethod
    def zero2() -> list[list[mp.mpf]]:
        return [[mp.mpf(0) for _ in range(4)] for __ in range(4)]

    @staticmethod
    def zero3() -> list[list[list[mp.mpf]]]:
        return [[[mp.mpf(0) for _ in range(4)] for __ in range(4)] for ___ in range(4)]

    @staticmethod
    def zero4() -> list[list[list[list[mp.mpf]]]]:
        return [
            [[[mp.mpf(0) for _ in range(4)] for __ in range(4)] for ___ in range(4)]
            for ____ in range(4)
        ]

    def adm_pair(
        self,
        base: str,
        direction: str,
        point: tuple[Fraction, Fraction, Fraction, Fraction],
    ) -> tuple[list[list[mp.mpf]], list[list[mp.mpf]]]:
        phi = self.interpolate(base, (point[1], point[2], point[3]))
        dphi = self.interpolate(direction, (point[1], point[2], point[3]))
        psi = 1 + phi
        alpha = (1 - phi) / (1 + phi)
        dalpha = -2 * dphi / (1 + phi) ** 2
        dgamma_diag = 4 * psi**3 * dphi

        g = self.zero2()
        dg = self.zero2()
        g[0][0] = -alpha**2
        dg[0][0] = -2 * alpha * dalpha
        for idx in (1, 2, 3):
            g[idx][idx] = psi**4
            dg[idx][idx] = dgamma_diag
        return g, dg

    def inv_diag(self, g: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
        out = self.zero2()
        for idx in range(4):
            out[idx][idx] = 1 / g[idx][idx]
        return out

    def d_inv_diag(
        self,
        g: list[list[mp.mpf]],
        dg: list[list[mp.mpf]],
    ) -> list[list[mp.mpf]]:
        out = self.zero2()
        for idx in range(4):
            out[idx][idx] = -dg[idx][idx] / g[idx][idx] ** 2
        return out

    def christoffel_pair(
        self,
        base: str,
        direction: str,
        point: tuple[Fraction, Fraction, Fraction, Fraction],
    ) -> tuple[list[list[list[mp.mpf]]], list[list[list[mp.mpf]]]]:
        g, dg = self.adm_pair(base, direction, point)
        g_inv = self.inv_diag(g)
        dg_inv = self.d_inv_diag(g, dg)
        h = mpf_fraction(H)

        dg_coord = self.zero3()
        ddg_coord = self.zero3()
        for axis in range(4):
            g_plus, dg_plus = self.adm_pair(base, direction, add_axis(point, axis, H))
            g_minus, dg_minus = self.adm_pair(base, direction, add_axis(point, axis, -H))
            for row in range(4):
                for col in range(4):
                    dg_coord[axis][row][col] = (g_plus[row][col] - g_minus[row][col]) / (2 * h)
                    ddg_coord[axis][row][col] = (dg_plus[row][col] - dg_minus[row][col]) / (2 * h)

        gamma = self.zero3()
        dgamma = self.zero3()
        for lam in range(4):
            for mu in range(4):
                for nu in range(4):
                    total = mp.mpf(0)
                    dtotal = mp.mpf(0)
                    for rho in range(4):
                        comb = (
                            dg_coord[mu][rho][nu]
                            + dg_coord[nu][rho][mu]
                            - dg_coord[rho][mu][nu]
                        )
                        dcomb = (
                            ddg_coord[mu][rho][nu]
                            + ddg_coord[nu][rho][mu]
                            - ddg_coord[rho][mu][nu]
                        )
                        total += g_inv[lam][rho] * comb
                        dtotal += dg_inv[lam][rho] * comb + g_inv[lam][rho] * dcomb
                    gamma[lam][mu][nu] = total / 2
                    dgamma[lam][mu][nu] = dtotal / 2
        return gamma, dgamma

    def ricci_einstein_pair(
        self,
        base: str,
        direction: str,
        point: tuple[Fraction, Fraction, Fraction, Fraction],
    ) -> tuple[list[list[mp.mpf]], list[list[mp.mpf]]]:
        g, dg = self.adm_pair(base, direction, point)
        g_inv = self.inv_diag(g)
        dg_inv = self.d_inv_diag(g, dg)
        gamma, dgamma = self.christoffel_pair(base, direction, point)
        h = mpf_fraction(H)

        dgamma_coord = self.zero4()
        ddgamma_coord = self.zero4()
        for axis in range(4):
            gamma_plus, dgamma_plus = self.christoffel_pair(
                base, direction, add_axis(point, axis, H)
            )
            gamma_minus, dgamma_minus = self.christoffel_pair(
                base, direction, add_axis(point, axis, -H)
            )
            for lam in range(4):
                for mu in range(4):
                    for nu in range(4):
                        dgamma_coord[axis][lam][mu][nu] = (
                            gamma_plus[lam][mu][nu] - gamma_minus[lam][mu][nu]
                        ) / (2 * h)
                        ddgamma_coord[axis][lam][mu][nu] = (
                            dgamma_plus[lam][mu][nu] - dgamma_minus[lam][mu][nu]
                        ) / (2 * h)

        ricci = self.zero2()
        dricci = self.zero2()
        for mu in range(4):
            for nu in range(4):
                term1 = term2 = term3 = term4 = mp.mpf(0)
                dterm1 = dterm2 = dterm3 = dterm4 = mp.mpf(0)
                for lam in range(4):
                    term1 += dgamma_coord[lam][lam][mu][nu]
                    dterm1 += ddgamma_coord[lam][lam][mu][nu]
                    term2 += dgamma_coord[nu][lam][mu][lam]
                    dterm2 += ddgamma_coord[nu][lam][mu][lam]
                    trace_lam = sum(gamma[rho][lam][rho] for rho in range(4))
                    dtrace_lam = sum(dgamma[rho][lam][rho] for rho in range(4))
                    term3 += gamma[lam][mu][nu] * trace_lam
                    dterm3 += dgamma[lam][mu][nu] * trace_lam + gamma[lam][mu][nu] * dtrace_lam
                    for rho in range(4):
                        term4 += gamma[rho][mu][lam] * gamma[lam][nu][rho]
                        dterm4 += (
                            dgamma[rho][mu][lam] * gamma[lam][nu][rho]
                            + gamma[rho][mu][lam] * dgamma[lam][nu][rho]
                        )
                ricci[mu][nu] = term1 - term2 + term3 - term4
                dricci[mu][nu] = dterm1 - dterm2 + dterm3 - dterm4

        scalar = sum(g_inv[i][j] * ricci[i][j] for i in range(4) for j in range(4))
        dscalar = sum(
            dg_inv[i][j] * ricci[i][j] + g_inv[i][j] * dricci[i][j]
            for i in range(4)
            for j in range(4)
        )
        einstein = self.zero2()
        deinstein = self.zero2()
        for row in range(4):
            for col in range(4):
                einstein[row][col] = ricci[row][col] - g[row][col] * scalar / 2
                deinstein[row][col] = dricci[row][col] - (
                    dg[row][col] * scalar + g[row][col] * dscalar
                ) / 2
        return einstein, deinstein

    def active_row(self, label: str, base: str, direction_label: str, direction: str) -> BranchRow:
        einstein, deinstein = self.ricci_einstein_pair(base, direction, PROBE0)
        spatial_trace = sum(einstein[idx][idx] for idx in (1, 2, 3))
        dspatial_trace = sum(deinstein[idx][idx] for idx in (1, 2, 3))
        value = einstein[1][1] - spatial_trace / 3
        derivative = deinstein[1][1] - dspatial_trace / 3
        beta = mp.sign(value) * derivative
        return BranchRow(
            label=label,
            direction=direction_label,
            value_xx_tf=value,
            derivative_xx_tf=derivative,
            beta=beta,
        )

    def rows(self) -> list[BranchRow]:
        return [
            self.active_row("center/e0", "e0", "E_x", "ex"),
            self.active_row("center/e0", "e0", "T1x", "t1x"),
            self.active_row("shell/s_sqrt6", "s_unit", "E_x", "ex"),
            self.active_row("shell/s_sqrt6", "s_unit", "T1x", "t1x"),
        ]


def scipy_axis_value(mode: int, coord: Fraction) -> float:
    vec = np.zeros(SIZE, dtype=float)
    for idx in range(1, N + 1):
        vec[idx] = np.sin(np.pi * mode * idx / (N + 1))
    return float(
        map_coordinates(
            vec,
            np.array([[float(mpf_fraction(coord))]], dtype=float),
            order=3,
            mode="nearest",
        )[0]
    )


def verify_axis_functionals(evaluator: ExactActiveBranchEvaluator) -> float:
    coords = sorted({CENTER + xyz[axis] for xyz in interpolation_points(PROBE0) for axis in range(3)})
    max_err = 0.0
    for mode in (1, 2, 7, 13):
        for coord in coords:
            exactish = evaluator.axis_l(coord)[mode]
            scipy_val = scipy_axis_value(mode, coord)
            max_err = max(max_err, abs(float(exactish) - scipy_val))
    return max_err


def t_balance_from_rows(rows: list[BranchRow]) -> mp.mpf:
    by_key = {(row.label, row.direction): row for row in rows}
    beta_center = by_key[("center/e0", "T1x")].beta
    beta_shell = by_key[("shell/s_sqrt6", "T1x")].beta
    return abs(6 * (beta_center - beta_shell) / beta_shell)


def recognition_checks(x: mp.mpf) -> tuple[bool, bool, str]:
    x_float = sp.Float(mp.nstr(x, 75), 75)
    constants = [
        sp.sqrt(2),
        sp.sqrt(3),
        sp.sqrt(6),
        2 * sp.cos(sp.pi / 7),
        2 * sp.cos(2 * sp.pi / 7),
        2 * sp.cos(3 * sp.pi / 7),
    ]
    ns = sp.nsimplify(
        x_float,
        constants,
        tolerance=sp.Float("1e-40"),
        rational=False,
        full=True,
    )
    ns_recognized = not isinstance(ns, sp.Float)

    pslq_found = False
    pslq_detail = "none"
    for degree in range(1, 7):
        rel = mp.pslq(
            [x**power for power in range(degree + 1)],
            tol=mp.mpf("1e-50"),
            maxcoeff=10_000_000,
            maxsteps=1000,
        )
        if rel is not None:
            pslq_found = True
            pslq_detail = f"degree={degree}, coeffs={rel}"
            break
    return ns_recognized, pslq_found, pslq_detail


def source_contract_checks() -> tuple[bool, bool, bool]:
    step_free = STEP_FREE_RUNNER.read_text(encoding="utf-8")
    parent_note = PARENT_NOTE.read_text(encoding="utf-8")
    tensor = TENSOR_RUNNER.read_text(encoding="utf-8")
    has_probe0 = "np.array([0.0, 4.25, 0.0, 0.0], dtype=float)" in step_free
    has_interp = 'order=3, mode="nearest"' in step_free and 'order=3, mode="nearest"' in tensor
    has_h = "h: float = 0.04" in step_free
    has_support_gap_authority = (
        "delta_A1(e0) - delta_A1(s/sqrt(6)) = 1/6" in parent_note
        and "endpoint support gap is the admitted 1/6 support scalar" in step_free
    )
    return has_probe0 and has_h, has_interp, has_support_gap_authority


def source_note_boundary_check() -> bool:
    note = NOTE.read_text(encoding="utf-8")
    required = (
        "**Type:** bounded_theorem",
        "**Claim type:** bounded_theorem",
        "60-digit evaluation of the exact\nfinite algebraic-sum object",
        "This note consumes that support gap from the comparison authority",
        "compact recognition\nremains an open target",
    )
    banned = (
        "closed form impossible",
        "no closed form exists",
        "no exact closed form",
    )
    return all(fragment in note for fragment in required) and not any(
        fragment in note for fragment in banned
    )


def print_rows(rows: list[BranchRow]) -> None:
    print("\nActive probe0:xx exact-sum endpoint rows")
    for row in rows:
        print(
            f"  q={row.label:13s} dir={row.direction:3s} "
            f"value={mp.nstr(row.value_xx_tf, 24)} "
            f"dE/dt={mp.nstr(row.derivative_xx_tf, 24)} "
            f"beta={mp.nstr(row.beta, 24)}"
        )


def main() -> int:
    print("Route-2 t_balance exact finite algebraic-sum evaluator")
    print("=" * 78)
    print("Exact-sum form:")
    print(
        "  Phi_q(xi) = 1/343 * sum_{a,b,c=1}^{13} "
        "L_a(xi_x)L_b(xi_y)L_c(xi_z) Q_abc / "
        "(6-2cos(a*pi/14)-2cos(b*pi/14)-2cos(c*pi/14))"
    )
    print(
        "  L_m is the cubic mode=nearest interpolation functional: "
        "edge prepad 12, rational tridiagonal spline solve, rational B-spline weights."
    )

    source_probe_ok, source_interp_ok, source_support_gap_ok = source_contract_checks()
    check(
        "source contract still fixes probe0 and coordinate stencil h=0.04",
        source_probe_ok,
        "active branch is probe0:xx from the step-free runner",
    )
    check(
        "source contract still uses cubic SciPy map_coordinates with mode nearest",
        source_interp_ok,
        "this runner exactifies that interpolation contract",
    )
    check(
        "source note keeps bounded metadata and scoped recognition language",
        source_note_boundary_check(),
        "bounded_theorem metadata, exact-object wording, and recognition-open caveat",
    )

    evaluator70 = ExactActiveBranchEvaluator(70)
    axis_err = verify_axis_functionals(evaluator70)
    check(
        "separable rational spline functional reproduces SciPy interpolation on sine modes",
        axis_err < 1.0e-12,
        f"max axis functional error = {axis_err:.3e}",
    )

    rows70 = evaluator70.rows()
    print_rows(rows70)
    t70 = t_balance_from_rows(rows70)

    evaluator90 = ExactActiveBranchEvaluator(90)
    rows90 = evaluator90.rows()
    t90 = t_balance_from_rows(rows90)
    anchor_coeffs = anchor_coefficients()
    anchor_center = evaluator90.lattice_functional("e0", anchor_coeffs)
    anchor_shell = evaluator90.lattice_functional("s_unit", anchor_coeffs)
    precision_drift = abs(t90 - t70)
    print(f"\nt_balance exact-sum eval at 90 dps = {mp.nstr(t90, 60)}")
    print(f"|t_balance - 1| = {mp.nstr(abs(t90 - 1), 40)}")

    by_key = {(row.label, row.direction): row.beta for row in rows90}
    max_beta_drift = max(
        abs(by_key[key] - expected)
        for key, expected in EXPECTED_STEP_FREE.items()
    )
    check(
        "four exact-sum active beta values agree with the tracked step-free double row",
        max_beta_drift < mp.mpf("3e-16"),
        f"max beta drift = {mp.nstr(max_beta_drift, 8)}",
    )
    check(
        "exact-sum t_balance agrees with the tracked 1.000030809474 row at the expected conditioning",
        abs(t90 - EXPECTED_T_BALANCE_STEP_FREE) < mp.mpf("2e-11"),
        f"drift = {mp.nstr(abs(t90 - EXPECTED_T_BALANCE_STEP_FREE), 8)}",
    )
    check(
        "70 dps and 90 dps exact-sum t_balance evaluations are stable past 50 digits",
        precision_drift < mp.mpf("1e-55"),
        f"drift = {mp.nstr(precision_drift, 8)}",
    )
    check(
        "reduced-shell anchor functional is common to center and shell endpoints",
        abs(anchor_center - anchor_shell) < mp.mpf("1e-60"),
        f"anchor drift = {mp.nstr(abs(anchor_center - anchor_shell), 8)}",
    )
    check(
        "exact-sum reduced-shell anchor agrees with the tracked shell-law constant",
        abs(anchor_center - EXPECTED_ANCHOR) < mp.mpf("2e-15"),
        f"anchor = {mp.nstr(anchor_center, 30)}",
    )
    check(
        "comparison authority supplies the admitted endpoint support gap 1/6",
        source_support_gap_ok,
        "1/6 is consumed from the comparison authority, not rederived here",
    )
    check(
        "t_balance near-miss remains positive in the exact-sum active branch",
        abs(t90 - 1) > mp.mpf("3e-5"),
        f"|t_balance - 1| = {mp.nstr(abs(t90 - 1), 12)}",
    )

    beta_e_center = by_key[("center/e0", "E_x")]
    beta_e_shell = by_key[("shell/s_sqrt6", "E_x")]
    beta_t_center = by_key[("center/e0", "T1x")]
    beta_t_shell = by_key[("shell/s_sqrt6", "T1x")]
    slope_e = 6 * (beta_e_center - beta_e_shell) / anchor_center
    intercept_e = beta_e_shell / anchor_center
    slope_t = 6 * (beta_t_center - beta_t_shell) / anchor_center
    intercept_t = beta_t_shell / anchor_center

    print("\nExact affine gamma assembly")
    print(
        "  beta_E(delta) = "
        f"{mp.nstr(beta_e_shell, 24)} + "
        f"({mp.nstr(6 * (beta_e_center - beta_e_shell), 24)}) delta_A1"
    )
    print(
        "  beta_T(delta) = "
        f"{mp.nstr(beta_t_shell, 24)} + "
        f"({mp.nstr(6 * (beta_t_center - beta_t_shell), 24)}) delta_A1"
    )
    print(f"  common anchor A = {mp.nstr(anchor_center, 30)}")
    print(
        "  gamma_E(delta) = "
        f"{mp.nstr(intercept_e, 24)} + ({mp.nstr(slope_e, 24)}) delta_A1"
    )
    print(
        "  gamma_T(delta) = "
        f"{mp.nstr(intercept_t, 24)} + ({mp.nstr(slope_t, 24)}) delta_A1"
    )
    print("  |b_T/a_T| = |6(beta_T(center)-beta_T(shell))/beta_T(shell)|")

    ns_recognized, pslq_found, pslq_detail = recognition_checks(t90)
    check(
        "nsimplify finds no expression in sqrt2/sqrt3/sqrt6 and the pi/7 cosine basis",
        not ns_recognized,
        "returned the high-precision Float, not a closed expression",
    )
    check(
        "PSLQ finds no minimal-polynomial relation through degree 6 with coefficients <= 1e7",
        not pslq_found,
        pslq_detail,
    )
    check(
        "no rational, quadratic-surd, or low-degree algebraic closed form is accepted by this runner",
        (not ns_recognized) and (not pslq_found),
        "exact finite algebraic sum is the source representation; recognition remains open",
    )

    print("=" * 78)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
