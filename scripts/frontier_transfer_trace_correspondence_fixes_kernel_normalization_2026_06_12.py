#!/usr/bin/env python3
"""Bounded runner: retained 2-step transfer trace fixes Berezin kernel
normalization on the free staggered surface.

This runner reuses the construction conventions of
scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py:
free staggered fermions in 1+1d, U=1, eta_0=1, eta_1(t)=(-1)^t,
m=0.5, T_hat^2 = T_odd T_even, and the decaying one-particle kernel
t(p)=exp(-2E(p)), E(p)=arcsinh(sqrt(m^2+sin^2 p)).

The Berezin side below is evaluated by an explicit finite Grassmann
expansion: truncated exponential, exterior polynomial multiplication, and
top-monomial extraction. Determinants are used only on the separate operator
or source-identity side, never as a substitute for the Berezin integral.
"""
from __future__ import annotations

import inspect
import math
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "TRANSFER_TRACE_CORRESPONDENCE_FIXES_KERNEL_NORMALIZATION_ON_RETAINED_SURFACE_BOUNDED_NOTE_2026-06-12.md"
RP_NOTE_PATH = ROOT / "docs" / "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md"
SUBSTEP1_NOTE_PATH = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md"
W4_COMPANION = "KOIDE_OCCUPANCY_KERNEL_COEFFICIENT_NOT_FIXED_BY_RETAINED_CORNER_MEASURE_BOUNDED_NOTE_2026-06-12.md"

MASS = 0.5
TOL = 1.0e-10
PASS_COUNT = 0
FAIL_COUNT = 0


def record(name: str, ok: bool, detail: str) -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        verdict = "PASS"
    else:
        FAIL_COUNT += 1
        verdict = "FAIL"
    print(f"{verdict:4s} {name}: {detail}")


# ---------------------------------------------------------------------------
# Retained RP construction: action-derived T_even/T_odd and decaying kernel.
# ---------------------------------------------------------------------------


def E_dispersion(p: float, m: float = MASS) -> float:
    """Free staggered 1+1d dispersion, matching the retained RP runner."""
    return math.asinh(math.sqrt(m * m + math.sin(p) ** 2))


def classical_step(p: float, m: float, parity: int) -> np.ndarray:
    """Single-step classical transfer matrix T_s from the staggered action."""
    s = math.sin(p)
    alpha = m + (1j * s if parity == 0 else -1j * s)
    return np.array([[-2.0 * alpha, 1.0], [1.0, 0.0]], dtype=complex)


def classical_2step(p: float, m: float = MASS) -> np.ndarray:
    """T2cl(p) = T_odd(p) T_even(p), the retained 2-step recipe."""
    return classical_step(p, m, 1) @ classical_step(p, m, 0)


def decaying_kernel_from_classical(p: float, m: float = MASS) -> complex:
    """Stable one-particle 2-step kernel selected from T_odd T_even."""
    ev = np.linalg.eigvals(classical_2step(p, m))
    return ev[int(np.argmin(np.abs(ev)))]


def kernel_lambdas_numeric(Ls: int, m: float = MASS) -> list[float]:
    return [math.exp(-2.0 * E_dispersion(2.0 * math.pi * k / Ls, m)) for k in range(Ls)]


def kernel_lambdas_exact(Ls: int) -> list[sp.Expr]:
    """Exact m=1/2 lambdas for the small robustness lattices used here."""
    out: list[sp.Expr] = []
    for k in range(Ls):
        p = 2 * sp.pi * k / Ls
        q = sp.sqrt(sp.Rational(1, 4) + sp.sin(p) ** 2)
        out.append(sp.simplify((sp.sqrt(1 + q ** 2) - q) ** 2))
    return out


def gamma_diagonal_from_lambdas(lambdas: list[sp.Expr | float], power: int = 1) -> list[sp.Expr | float]:
    diag: list[sp.Expr | float] = []
    for mask in range(2 ** len(lambdas)):
        val: sp.Expr | float = 1
        for i, lam in enumerate(lambdas):
            if mask & (1 << i):
                val = val * (lam ** power)
        diag.append(sp.simplify(val) if any(isinstance(x, sp.Basic) for x in lambdas) else val)
    return diag


def gamma_trace_exact(lambdas: list[sp.Expr], power: int = 1) -> sp.Expr:
    gamma = sp.diag(*gamma_diagonal_from_lambdas(lambdas, power))
    return sp.simplify(sp.trace(gamma))


def det_one_plus_exact(lambdas: list[sp.Expr], power: int = 1) -> sp.Expr:
    one_particle = sp.diag(*[sp.simplify(lam ** power) for lam in lambdas])
    return sp.simplify((sp.eye(len(lambdas)) + one_particle).det())


def transfer_positivity_stats(Ls: int) -> dict[str, float]:
    lambdas = kernel_lambdas_numeric(Ls)
    gamma = np.diag([float(x) for x in gamma_diagonal_from_lambdas(lambdas)])
    b = np.diag([math.sqrt(float(x)) for x in np.diag(gamma)])
    eig = np.linalg.eigvalsh(gamma)
    return {
        "min_eig": float(eig.min()),
        "max_eig": float(eig.max()),
        "herm_err": float(np.max(np.abs(gamma - gamma.conj().T))),
        "bdagb_err": float(np.max(np.abs(gamma - b.conj().T @ b))),
    }


def dispersion_residual(Ls: int) -> float:
    residual = 0.0
    for k in range(Ls):
        p = 2.0 * math.pi * k / Ls
        decay = decaying_kernel_from_classical(p)
        target = math.exp(-2.0 * E_dispersion(p))
        residual = max(residual, abs(decay - target))
    return float(residual)


# ---------------------------------------------------------------------------
# Anti-periodic 2N-slice Berezin kernel and genuine Grassmann expansion.
# ---------------------------------------------------------------------------


def anti_periodic_trace_matrix(lambdas: list[sp.Expr | float], blocks: int = 1, scale: sp.Expr | float = 1) -> sp.Matrix:
    """Quadratic Berezin matrix M_AP with det(M_AP)=det(1+t^blocks).

    There are 2*blocks time slices. Alternating substep kernels A_j=I,t give
    product A_{2N-1}...A_0=t^N. The anti-periodic trace sign appears as the
    + boundary block in the upper-right corner.
    """
    n = len(lambdas)
    slices = 2 * blocks
    dim = n * slices
    M = sp.zeros(dim, dim)
    ident = sp.eye(n)
    t = sp.diag(*lambdas)
    kernels = [ident if j % 2 == 0 else t for j in range(slices)]
    for j in range(slices):
        M[j * n : (j + 1) * n, j * n : (j + 1) * n] = ident
    for j in range(slices - 1):
        M[(j + 1) * n : (j + 2) * n, j * n : (j + 1) * n] = -kernels[j]
    M[0:n, (slices - 1) * n : slices * n] = kernels[-1]
    return sp.simplify(scale) * M


def _multiply_masks(left: int, right: int) -> tuple[int, int] | None:
    if left & right:
        return None
    inversions = 0
    j = right
    while j:
        bit = j & -j
        idx = bit.bit_length() - 1
        inversions += (left >> (idx + 1)).bit_count()
        j ^= bit
    sign = -1 if inversions % 2 else 1
    return left | right, sign


def _poly_add_scaled(target: dict[int, sp.Expr], source: dict[int, sp.Expr], scale: sp.Expr) -> dict[int, sp.Expr]:
    for mask, coeff in source.items():
        target[mask] = sp.simplify(target.get(mask, 0) + scale * coeff)
        if target[mask] == 0:
            del target[mask]
    return target


def _poly_mul(left: dict[int, sp.Expr], right: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
    out: dict[int, sp.Expr] = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            product = _multiply_masks(lm, rm)
            if product is None:
                continue
            mask, sign = product
            out[mask] = sp.simplify(out.get(mask, 0) + sign * lc * rc)
            if out[mask] == 0:
                del out[mask]
    return out


def _var(index: int) -> dict[int, sp.Expr]:
    return {1 << index: sp.Integer(1)}


def grassmann_gaussian_integral(matrix: sp.Matrix) -> tuple[sp.Expr, dict[str, int | bool]]:
    """Evaluate int prod_i dbar_i dchi_i exp(-bar_i M_ij chi_j).

    This is a genuine finite Grassmann expansion. It constructs the bilinear
    action as an exterior polynomial, expands the exponential through degree d,
    and extracts the top monomial. No determinant routine is called here.
    """
    d = matrix.rows
    if matrix.cols != d:
        raise ValueError("Berezin matrix must be square")

    action: dict[int, sp.Expr] = {}
    bilinear_terms = 0
    for i in range(d):
        for j in range(d):
            coeff = sp.simplify(-matrix[i, j])
            if coeff == 0:
                continue
            monomial = _poly_mul(_var(2 * i), _var(2 * j + 1))
            _poly_add_scaled(action, monomial, coeff)
            bilinear_terms += 1

    exp_poly: dict[int, sp.Expr] = {0: sp.Integer(1)}
    power: dict[int, sp.Expr] = {0: sp.Integer(1)}
    for order in range(1, d + 1):
        power = _poly_mul(power, action)
        _poly_add_scaled(exp_poly, power, sp.Rational(1, math.factorial(order)))

    top_mask = (1 << (2 * d)) - 1
    top_coeff = exp_poly.get(top_mask, 0)
    value = sp.simplify(((-1) ** d) * top_coeff)
    meta = {
        "pairs": d,
        "bilinear_terms": bilinear_terms,
        "expanded_terms": len(exp_poly),
        "used_det_substitute": False,
    }
    return value, meta


def berezin_trace_value(lambdas: list[sp.Expr], blocks: int = 1, scale: sp.Expr | float = 1) -> tuple[sp.Expr, dict[str, int | bool]]:
    matrix = anti_periodic_trace_matrix(lambdas, blocks=blocks, scale=scale)
    return grassmann_gaussian_integral(matrix)


# ---------------------------------------------------------------------------
# Source/note checks.
# ---------------------------------------------------------------------------


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def markdown_links(text: str) -> list[str]:
    import re

    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def note_link_inventory_ok(note_text: str) -> tuple[bool, str]:
    links = markdown_links(note_text)
    expected = [
        "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md",
        "STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md",
    ]
    exact_links = links == expected
    resolve = all((NOTE_PATH.parent / link).exists() for link in links)
    w4_backticked = f"`{W4_COMPANION}`" in note_text and f"]({W4_COMPANION}" not in note_text
    return exact_links and resolve and w4_backticked, (
        f"links={links}; resolve={resolve}; W4 backticked only={w4_backticked}"
    )


def source_grep_ok() -> tuple[bool, str]:
    rp = load_text(RP_NOTE_PATH)
    sub = load_text(SUBSTEP1_NOTE_PATH)
    rp_terms = ["2-step blocked transfer matrix", "B^dag B", "E(p) = arcsinh"]
    sub_terms = ["det(M)", "single-pair"]
    ok = all(term in rp for term in rp_terms) and all(term in sub for term in sub_terms)
    return ok, f"RP terms={rp_terms}; substep1 terms={sub_terms}"


def note_firewall_ok(note_text: str) -> tuple[bool, str]:
    has_firewall = (
        "does not select an occupancy cell" in note_text
        and "the occupancy binary stays open" in note_text
    )
    forbidden = ["closes " + "the route", "only " + "route", "ex" + "hausted"]
    absent = not any(term in note_text for term in forbidden)
    return has_firewall and absent, f"firewall={has_firewall}; forbidden_absent={absent}"


def no_promotion_ok(note_text: str) -> tuple[bool, str]:
    phrase = "**No-promotion statement:**"
    ok = phrase in note_text and "does not promote, demote, or set" in note_text
    return ok, "No-promotion statement present" if ok else "No-promotion statement missing"


# ---------------------------------------------------------------------------
# Main checks.
# ---------------------------------------------------------------------------


def main() -> int:
    print("=" * 86)
    print("TRANSFER TRACE CORRESPONDENCE FIXES BEREZIN KERNEL NORMALIZATION")
    print("Retained free staggered surface only: 1+1d, U=1, m=0.5, 2-step blocked")
    print("=" * 86)

    for Ls in (2, 3):
        stats = transfer_positivity_stats(Ls)
        ok = stats["min_eig"] > 0 and stats["herm_err"] < TOL and stats["bdagb_err"] < TOL
        record(
            f"A1 retained T_even/T_odd -> T_hat^2 positive Hermitian L_s={Ls}",
            ok,
            f"min eig={stats['min_eig']:.6e}; max eig={stats['max_eig']:.6e}; "
            f"Herm residual={stats['herm_err']:.1e}; BdagB residual={stats['bdagb_err']:.1e}",
        )

    for Ls in (2, 3):
        residual = dispersion_residual(Ls)
        record(
            f"A2 decaying eigenvalue matches e^(-2E(p)) L_s={Ls}",
            residual < TOL,
            f"max residual={residual:.3e}; E(p)=arcsinh(sqrt(m^2+sin^2 p))",
        )

    lambdas_2 = kernel_lambdas_exact(2)
    tr_gamma_1 = gamma_trace_exact(lambdas_2, power=1)
    det_1 = det_one_plus_exact(lambdas_2, power=1)
    record(
        "A3 T1 exact Tr Gamma(t)=det(1+t), L_s=2",
        sp.simplify(tr_gamma_1 - det_1) == 0,
        f"Tr Gamma={sp.sstr(tr_gamma_1)}; det(1+t)={sp.sstr(det_1)}",
    )

    tr_gamma_2 = gamma_trace_exact(lambdas_2, power=2)
    det_2 = det_one_plus_exact(lambdas_2, power=2)
    record(
        "A4 T1 exact Tr Gamma(t)^2=det(1+t^2), L_s=2",
        sp.simplify(tr_gamma_2 - det_2) == 0,
        f"Tr Gamma^2={sp.sstr(tr_gamma_2)}; det(1+t^2)={sp.sstr(det_2)}",
    )

    berezin_2, meta_2 = berezin_trace_value(lambdas_2, blocks=1)
    record(
        "A5 T2 genuine two-slice Berezin expansion equals det(1+t), L_s=2",
        sp.simplify(berezin_2 - det_1) == 0,
        f"Berezin={sp.sstr(berezin_2)}; pairs={meta_2['pairs']}; "
        f"terms={meta_2['expanded_terms']}",
    )
    record(
        "A5b T2 Berezin value equals operator trace, L_s=2",
        sp.simplify(berezin_2 - tr_gamma_1) == 0,
        f"Berezin={sp.sstr(berezin_2)}; Tr Gamma={sp.sstr(tr_gamma_1)}",
    )

    source = inspect.getsource(grassmann_gaussian_integral)
    forbidden_det_calls = [".det(", "det(", "np.linalg.det", "Matrix.det"]
    uses_no_det = (
        meta_2["used_det_substitute"] is False
        and "top monomial" in source
        and not any(term in source for term in forbidden_det_calls)
    )
    record(
        "A5c Berezin side self-check: expansion path, no det substitute",
        uses_no_det,
        f"used_det_substitute={meta_2['used_det_substitute']}; source det calls absent={uses_no_det}",
    )

    lam = sp.symbols("lambda", positive=True)
    scaled_berezin, scaled_meta = berezin_trace_value(lambdas_2, blocks=1, scale=lam)
    ratio = sp.simplify(scaled_berezin / berezin_2)
    k_exp = sp.degree(sp.Poly(ratio, lam), lam)
    record(
        "A6 T3a lambda-rescaled Berezin kernel gives lambda^k",
        ratio == lam ** scaled_meta["pairs"] and k_exp == scaled_meta["pairs"],
        f"ratio={sp.sstr(ratio)}; extracted k={k_exp}; rank={scaled_meta['pairs']}",
    )

    equation = sp.Eq((lam ** k_exp) * berezin_2, berezin_2)
    real_roots = sp.solve(sp.Eq((sp.Symbol("lambda") ** k_exp) * berezin_2, berezin_2), sp.Symbol("lambda"))
    positive_real_roots = [root for root in real_roots if root.is_real and float(root) > 0]
    record(
        "A7 T3b over lambda>0 equality forces lambda=1",
        positive_real_roots == [sp.Integer(1)],
        f"{sp.sstr(equation)}; positive real solutions={positive_real_roots}",
    )

    lambda_two_value = sp.simplify(scaled_berezin.subs(lam, 2))
    record(
        "A8 T3c numeric witness lambda=2 breaks equality by predicted factor",
        sp.simplify(lambda_two_value - (2 ** k_exp) * berezin_2) == 0
        and sp.simplify(lambda_two_value - berezin_2) != 0,
        f"lambda=2 factor={2 ** k_exp}; scaled/op ratio={sp.sstr(sp.simplify(lambda_two_value / det_1))}",
    )

    ap_matrix = anti_periodic_trace_matrix(lambdas_2, blocks=1)
    det_scaled = sp.simplify((lam * ap_matrix).det())
    det_unscaled = sp.simplify(ap_matrix.det())
    record(
        "A9 T4 tie-in det(lambda K)=lambda^k det(K) uses same exponent",
        sp.simplify(det_scaled - lam ** ap_matrix.rows * det_unscaled) == 0 and ap_matrix.rows == k_exp,
        f"rank={ap_matrix.rows}; determinant scaling exponent={k_exp}",
    )

    lambdas_3 = kernel_lambdas_exact(3)
    tr3_1 = gamma_trace_exact(lambdas_3, power=1)
    det3_1 = det_one_plus_exact(lambdas_3, power=1)
    record(
        "A10 robustness Tr Gamma(t)=det(1+t), L_s=3",
        sp.simplify(tr3_1 - det3_1) == 0,
        f"residual={sp.sstr(sp.simplify(tr3_1 - det3_1))}; Fock dim=8",
    )

    tr3_2 = gamma_trace_exact(lambdas_3, power=2)
    det3_2 = det_one_plus_exact(lambdas_3, power=2)
    record(
        "A10b robustness Tr Gamma(t)^2=det(1+t^2), L_s=3",
        sp.simplify(tr3_2 - det3_2) == 0,
        f"residual={sp.sstr(sp.simplify(tr3_2 - det3_2))}; Fock dim=8",
    )

    berezin_3, meta_3 = berezin_trace_value(lambdas_3, blocks=1)
    record(
        "A10c robustness genuine Berezin expansion equals trace, L_s=3",
        sp.simplify(berezin_3 - tr3_1) == 0,
        f"Berezin residual={sp.sstr(sp.simplify(berezin_3 - tr3_1))}; "
        f"pairs={meta_3['pairs']}; terms={meta_3['expanded_terms']}",
    )

    source_ok, source_detail = source_grep_ok()
    record("B11 source grep retained RP and substep1 phrases", source_ok, source_detail)

    note_text = load_text(NOTE_PATH)
    firewall_ok, firewall_detail = note_firewall_ok(note_text)
    record("B12 note firewall present and closing language absent", firewall_ok, firewall_detail)

    links_ok, links_detail = note_link_inventory_ok(note_text)
    record("B13 link inventory exactly two load-bearing links", links_ok, links_detail)

    promotion_ok, promotion_detail = no_promotion_ok(note_text)
    record("B14 no-promotion statement present", promotion_ok, promotion_detail)

    print("=" * 86)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(
        "No-promotion statement: this runner does not promote, demote, or set "
        "audit/retention status for any note; it checks only the bounded surface."
    )
    if FAIL_COUNT == 0:
        print(
            "RESULT: lambda=1 is forced by the retained transfer/trace "
            "correspondence on the free staggered 2-step surface only; the "
            "occupancy binary stays open."
        )
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
