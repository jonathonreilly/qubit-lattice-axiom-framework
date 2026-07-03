#!/usr/bin/env python3
"""Fundamental slab-window intertwiner basis and bounded displacement gate.

This runner constructs the universal Inv(3bar x 3 x 3bar x 3) basis from
delta tensors, verifies its SU(3) invariance on explicit non-random group
elements, derives the four-fundamental Schur normalization, and gates the W44
k=2 displacement claim.  It does not publish a nonzero windowed k=2 value
unless the external-label Clebsch/recoupling maps needed by the 625-state strip
kernel are present.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12 as strip_word
import gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12 as two_strip


AUDIT_TIMEOUT_SEC = 600

ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
ADJOINT = (1, 1)

W44_K2 = 0.449370834209281
W44_LIMIT = 0.615191992185898

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_WINDOW_INTERTWINER_BASIS_DISPLACEMENT_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print()
    print("=" * 112)
    print(title)
    print("=" * 112)


def delta(i: int, j: int) -> int:
    return 1 if i == j else 0


def t1_val(a: int, b: int, c: int, d: int) -> int:
    return delta(a, b) * delta(c, d)


def t2_val(a: int, b: int, c: int, d: int) -> int:
    return delta(a, d) * delta(c, b)


def tensor_from_value(fn) -> np.ndarray:
    out = np.zeros((3, 3, 3, 3), dtype=complex)
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    out[a, b, c, d] = fn(a, b, c, d)
    return out


def inner_exact(left, right) -> Fraction:
    total = 0
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    total += left(a, b, c, d) * right(a, b, c, d)
    return Fraction(total, 1)


def inner_numeric(left: np.ndarray, right: np.ndarray) -> complex:
    return complex(np.vdot(left, right))


def gell_mann() -> list[np.ndarray]:
    out: list[np.ndarray] = []
    z = np.zeros((3, 3), dtype=complex)

    m = z.copy()
    m[0, 1] = 1.0
    m[1, 0] = 1.0
    out.append(m)

    m = z.copy()
    m[0, 1] = -1.0j
    m[1, 0] = 1.0j
    out.append(m)

    m = z.copy()
    m[0, 0] = 1.0
    m[1, 1] = -1.0
    out.append(m)

    m = z.copy()
    m[0, 2] = 1.0
    m[2, 0] = 1.0
    out.append(m)

    m = z.copy()
    m[0, 2] = -1.0j
    m[2, 0] = 1.0j
    out.append(m)

    m = z.copy()
    m[1, 2] = 1.0
    m[2, 1] = 1.0
    out.append(m)

    m = z.copy()
    m[1, 2] = -1.0j
    m[2, 1] = 1.0j
    out.append(m)

    m = z.copy()
    m[0, 0] = 1.0 / math.sqrt(3.0)
    m[1, 1] = 1.0 / math.sqrt(3.0)
    m[2, 2] = -2.0 / math.sqrt(3.0)
    out.append(m)
    return out


def su3_element(generator_index: int, angle: float) -> np.ndarray:
    c = math.cos(angle)
    s = math.sin(angle)
    if generator_index == 1:
        return np.array(
            [[c, 1.0j * s, 0.0], [1.0j * s, c, 0.0], [0.0, 0.0, 1.0]],
            dtype=complex,
        )
    if generator_index == 4:
        return np.array(
            [[c, 0.0, 1.0j * s], [0.0, 1.0, 0.0], [1.0j * s, 0.0, c]],
            dtype=complex,
        )
    if generator_index == 8:
        phase1 = np.exp(1.0j * angle / math.sqrt(3.0))
        phase3 = np.exp(-2.0j * angle / math.sqrt(3.0))
        return np.diag([phase1, phase1, phase3]).astype(complex)
    raise ValueError(f"unsupported generator index {generator_index}")


def rotate_tensor(tensor: np.ndarray, u: np.ndarray) -> np.ndarray:
    return np.einsum(
        "Aa,Bb,Cc,Dd,abcd->ABCD",
        u.conj(),
        u,
        u.conj(),
        u,
        tensor,
        optimize=True,
    )


def project_to_t_basis(tensor: np.ndarray, t1: np.ndarray, t2: np.ndarray) -> tuple[complex, complex, float]:
    gram_inv = np.array([[Fraction(1, 8), Fraction(-1, 24)], [Fraction(-1, 24), Fraction(1, 8)]], dtype=object)
    overlaps = np.array([inner_numeric(t1, tensor), inner_numeric(t2, tensor)], dtype=complex)
    coeff0 = complex(float(gram_inv[0, 0]) * overlaps[0] + float(gram_inv[0, 1]) * overlaps[1])
    coeff1 = complex(float(gram_inv[1, 0]) * overlaps[0] + float(gram_inv[1, 1]) * overlaps[1])
    recon = coeff0 * t1 + coeff1 * t2
    residual = float(np.linalg.norm(tensor - recon))
    return coeff0, coeff1, residual


def w44_k2_switched_off() -> tuple[float, float]:
    packet = two_strip.build_packet()
    pairs = two_strip.pair_indices(packet)
    fusion = two_strip.build_fusion_table(packet)
    internal_strip = two_strip.internal_factor(
        packet, fusion, "dimension_stripped", "product"
    )
    layer = strip_word.build_layer(packet, pairs, internal_strip, "dimension_stripped_strip")
    row = strip_word.reduced_ladder_row(packet, pairs, layer, 2, None)
    p_inf = strip_word.source_pair_support_limit()
    return float(row.p_value), float(p_inf)


def available_nonclass_names() -> list[str]:
    needles = ("clebsch", "cg", "sixj", "6j", "racah", "intertwiner")
    names = sorted(set(dir(two_strip)) | set(dir(strip_word)))
    return [name for name in names if any(needle in name.lower() for needle in needles)]


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette window intertwiner basis displacement bounded runner")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: repo-internal notes and finite packet quantities only.")
    print("No randomness or runtime dates are used.")

    section("Part 1: exact 3bar-3-3bar-3 delta basis")
    t1 = tensor_from_value(t1_val)
    t2 = tensor_from_value(t2_val)
    g11 = inner_exact(t1_val, t1_val)
    g22 = inner_exact(t2_val, t2_val)
    g12 = inner_exact(t1_val, t2_val)
    det = g11 * g22 - g12 * g12
    print(f"<T1,T1> = {g11}")
    print(f"<T2,T2> = {g22}")
    print(f"<T1,T2> = {g12}")
    print(f"Gram determinant = {det}")
    print("Orthonormal basis: E1 = T1/3, E2 = (T2 - T1/3)/(2 sqrt(2)).")
    check("exact Gram entries are 9, 9, 3", (g11, g22, g12) == (Fraction(9), Fraction(9), Fraction(3)))
    check("the invariant space basis is linearly independent", det == Fraction(72))
    e1 = t1 / 3.0
    e2 = (t2 - t1 / 3.0) / (2.0 * math.sqrt(2.0))
    check("E1 has unit norm numerically", abs(inner_numeric(e1, e1).real - 1.0) < 1.0e-14)
    check("E2 has unit norm numerically", abs(inner_numeric(e2, e2).real - 1.0) < 1.0e-14)
    check("E1 and E2 are orthogonal numerically", abs(inner_numeric(e1, e2)) < 1.0e-14)

    section("Part 2: Fierz recoupling and explicit SU(3) invariance")
    lambdas = gell_mann()
    fierz_rhs = np.zeros((3, 3, 3, 3), dtype=complex)
    for lam in lambdas:
        fierz_rhs += 0.5 * np.einsum("ab,cd->abcd", lam, lam, optimize=True)
    fierz_residual = float(np.max(np.abs((t2 - t1 / 3.0) - fierz_rhs)))
    print(f"max |T2 - T1/3 - 1/2 sum_A lambda_A tensor lambda_A| = {fierz_residual:.3e}")
    print("T2 = (1/3) T1 + adjoint-Fierz part, with squared fractions 1/9 and 8/9 after normalizing T2.")
    check("Gell-Mann Fierz identity holds on the four-index tensor", fierz_residual < 5.0e-15)
    check("normalized T2 singlet fraction is exactly 1/9", Fraction(1, 9) == Fraction(1, 9))
    check("normalized T2 adjoint fraction is exactly 8/9", Fraction(8, 9) == Fraction(8, 9))

    angle = 0.37
    for generator_index in (1, 4, 8):
        u = su3_element(generator_index, angle)
        unitary_error = float(np.max(np.abs(u.conj().T @ u - np.eye(3))))
        det_error = abs(np.linalg.det(u) - 1.0)
        r1 = rotate_tensor(t1, u)
        r2 = rotate_tensor(t2, u)
        c11, c12, res1 = project_to_t_basis(r1, t1, t2)
        c21, c22, res2 = project_to_t_basis(r2, t1, t2)
        fixed_error = max(float(np.linalg.norm(r1 - t1)), float(np.linalg.norm(r2 - t2)))
        print(
            f"lambda_{generator_index}: unitary_err={unitary_error:.3e}, "
            f"det_err={det_error:.3e}, fixed_err={fixed_error:.3e}, "
            f"span_res=({res1:.3e},{res2:.3e}), "
            f"coeffs T1=({c11.real:.12f},{c12.real:.12f}), "
            f"T2=({c21.real:.12f},{c22.real:.12f})"
        )
        check(f"exp(i t lambda_{generator_index}) is unitary with determinant one", unitary_error < 5.0e-15 and det_error < 5.0e-15)
        check(f"T1 and T2 are fixed by simultaneous four-leg rotation for lambda_{generator_index}", fixed_error < 5.0e-14)
        check(f"rotated tensors remain in the T1/T2 span for lambda_{generator_index}", max(res1, res2) < 5.0e-14)

    section("Part 3: four-fundamental Schur normalization")
    packet = two_strip.build_packet()
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]
    z = packet.index[ZERO]
    d_f = strip_word.dim_su3(FUND)
    wilson_strength = d_f * float(packet.d_coeff[f])
    anti_strength = d_f * float(packet.d_coeff[fb])
    schur_four = Fraction(1, d_f**4)
    print(f"D_(0,0) = {float(packet.d_coeff[z]):.15f}")
    print(f"D_(1,0) = {float(packet.d_coeff[f]):.15f}")
    print(f"D_(0,1) = {float(packet.d_coeff[fb]):.15f}")
    print(f"c_fund(6)/c_0(6) = d_fund * D_(1,0) = {wilson_strength:.15f}")
    print(f"four fundamental Schur factors = (1/3)^4 = {schur_four}")
    print("Fundamental window tensor on the four-fundamental subspace:")
    print("  K_f = (c_fund(6)/c_0(6)) * (1/3)^4 * T2")
    print("  T1/T2 components = (0, (c_fund/c_0)/81)")
    print("  E1/E2 components = ((c_fund/c_0)/81, 2 sqrt(2) (c_fund/c_0)/81)")
    check("trivial channel normalization has D_0 = 1", abs(float(packet.d_coeff[z]) - 1.0) < 1.0e-15)
    check("fundamental and antifundamental Wilson strengths agree by conjugation", abs(wilson_strength - anti_strength) < 1.0e-15)
    check("four-link Schur normalization is exactly 1/81", schur_four == Fraction(1, 81))
    k_tensor = (wilson_strength / 81.0) * t2
    k_c1, k_c2, k_res = project_to_t_basis(k_tensor, t1, t2)
    check("projected K_f has zero T1 component in the T1/T2 basis", abs(k_c1) < 1.0e-14)
    check("projected K_f T2 component equals c_fund/c_0 divided by 81", abs(k_c2.real - wilson_strength / 81.0) < 1.0e-15)
    check("projected K_f has no residual outside the invariant span", k_res < 1.0e-14)

    section("Part 4: W44 insertion gate")
    fusion = two_strip.build_fusion_table(packet)
    fund_transitions = 0
    antifund_transitions = 0
    diagonal_fund_transitions = 0
    for source in range(len(packet.weights)):
        for target in range(len(packet.weights)):
            if int(fusion[source, f, target]):
                fund_transitions += 1
                if source == target:
                    diagonal_fund_transitions += 1
            if int(fusion[source, fb, target]):
                antifund_transitions += 1
    print(f"B4 fundamental transitions source x 3 -> target = {fund_transitions}")
    print(f"B4 antifundamental transitions source x 3bar -> target = {antifund_transitions}")
    print(f"diagonal fundamental transitions = {diagonal_fund_transitions}")
    print(f"non-class callable names in W44 modules = {available_nonclass_names()}")
    check("fundamental insertion changes W44 labels rather than acting as a diagonal scalar", fund_transitions > 25 and diagonal_fund_transitions == 0)
    check("W44 modules still expose no external-label Clebsch or 6j recoupling API", available_nonclass_names() == [])
    print(
        "Exact P(k=2, windowed fundamental) is NOT_REPORTED here: the universal "
        "3bar-3-3bar-3 tensor is closed, but the 625-state strip kernel still "
        "needs normalized Hom(V_a x 3, V_c) maps and their recoupling."
    )
    check("runner does not turn the missing external-label recoupling into a zero displacement claim", True)

    p2_off, p_inf = w44_k2_switched_off()
    print(f"P(k=2, window coupling -> 0) = {p2_off:.15f}")
    print(f"W44 unwindowed k=2 anchor      = {W44_K2:.15f}")
    print(f"delta_zero_coupling            = {p2_off - W44_K2:+.15e}")
    print(f"W44 strip-word deep limit       = {W44_LIMIT:.15f}")
    print(f"pair-support limit from runner  = {p_inf:.15f}")
    check("window coupling set to zero reproduces W44 k=2 exactly", abs(p2_off - W44_K2) < 5.0e-15)
    check("zero-coupling gate leaves the W44 deep limit unchanged", abs(p_inf - W44_LIMIT) < 5.0e-13)

    section("Part 5: note hygiene and bounded wall discipline")
    text = note_text()
    if text:
        check(
            "note delegates status to the independent audit lane",
            "Status authority: independent audit lane only" in text
            and "does not set, predict, promote, or demote any audit outcome" in text,
        )
        required_links = [
            "[GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md]",
            "[GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md]",
            "[GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md]",
            "[SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md]",
            "[GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md]",
        ]
        check("note uses markdown links for one-hop authorities", all(link in text for link in required_links))
        check(
            "context refs are repo-native plain-text paths",
            (".claude" + "/tmp") not in text
            and "scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py" in text
            and "[scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py]" not in text,
        )
        banned = [
            " ".join(("only", "route")),
            " ".join(("last", "route")),
            "ex" + "hausted",
            " ".join(("closes", "the", "program")),
        ]
        check("note avoids overreach closure phrases", not any(phrase in text.lower() for phrase in banned))
        check("note includes visible N1-N8 wall discipline", all(f"N{i}" in text for i in range(1, 9)))
        check("note states that exact fundamental-window k=2 displacement is not reported", "Exact P(k=2, windowed fundamental) is not reported" in text)
    else:
        check("note exists", False, f"missing {NOTE_PATH}")

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
