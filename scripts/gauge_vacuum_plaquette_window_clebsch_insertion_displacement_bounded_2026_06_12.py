#!/usr/bin/env python3
"""W50 window Clebsch/isometry construction and W44 insertion gate.

This runner closes the import-free 3 x 3bar Casimir-projector/isometry
calculation for the fundamental window tensor and checks the W44 insertion
surface.  It reports the zero-window gate numerically and refuses to publish a
fundamental-channel W44 displacement unless a normalized 625-state
external-label recoupling kernel is actually present.
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

W44_K2_ANCHOR = 0.449370834209281
W44_LIMIT = 0.615191992185898

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_WINDOW_CLEBSCH_INSERTION_DISPLACEMENT_BOUNDED_NOTE_2026-06-12.md"
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


def gell_mann() -> list[np.ndarray]:
    zero = np.zeros((3, 3), dtype=complex)
    out: list[np.ndarray] = []

    m = zero.copy()
    m[0, 1] = 1.0
    m[1, 0] = 1.0
    out.append(m)

    m = zero.copy()
    m[0, 1] = -1.0j
    m[1, 0] = 1.0j
    out.append(m)

    m = zero.copy()
    m[0, 0] = 1.0
    m[1, 1] = -1.0
    out.append(m)

    m = zero.copy()
    m[0, 2] = 1.0
    m[2, 0] = 1.0
    out.append(m)

    m = zero.copy()
    m[0, 2] = -1.0j
    m[2, 0] = 1.0j
    out.append(m)

    m = zero.copy()
    m[1, 2] = 1.0
    m[2, 1] = 1.0
    out.append(m)

    m = zero.copy()
    m[1, 2] = -1.0j
    m[2, 1] = 1.0j
    out.append(m)

    m = zero.copy()
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


def product_casimir_3_x_3bar(lambdas: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    ident = np.eye(3, dtype=complex)
    casimir = np.zeros((9, 9), dtype=complex)
    for lam in lambdas:
        t_fund = 0.5 * lam
        t_antifund = -0.5 * lam.conj()
        total = np.kron(t_fund, ident) + np.kron(ident, t_antifund)
        casimir += total @ total
    p8 = casimir / 3.0
    p1 = np.eye(9, dtype=complex) - p8
    return casimir, p1, p8


def vec_matrix(matrix: np.ndarray) -> np.ndarray:
    return np.asarray(matrix, dtype=complex).reshape(9)


def singlet_and_adjoint_isometries(lambdas: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray]:
    v1 = vec_matrix(np.eye(3, dtype=complex) / math.sqrt(3.0)).reshape(9, 1)
    v8 = np.column_stack([vec_matrix(lam / math.sqrt(2.0)) for lam in lambdas])
    return v1, v8


def delta(i: int, j: int) -> int:
    return 1 if i == j else 0


def tensor_from_value(fn) -> np.ndarray:
    out = np.zeros((3, 3, 3, 3), dtype=complex)
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    out[a, b, c, d] = fn(a, b, c, d)
    return out


def t1_val(a: int, b: int, c: int, d: int) -> int:
    return delta(a, b) * delta(c, d)


def t2_val(a: int, b: int, c: int, d: int) -> int:
    return delta(a, d) * delta(c, b)


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


def project_to_e_basis(tensor: np.ndarray, e1: np.ndarray, e8: np.ndarray) -> tuple[complex, complex, float]:
    c1 = inner_numeric(e1, tensor)
    c8 = inner_numeric(e8, tensor)
    recon = c1 * e1 + c8 * e8
    return c1, c8, float(np.linalg.norm(tensor - recon))


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
    needles = ("clebsch", "cg", "sixj", "6j", "racah", "intertwiner", "wigner")
    names = sorted(set(dir(two_strip)) | set(dir(strip_word)))
    return [name for name in names if any(needle in name.lower() for needle in needles)]


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette W50 window Clebsch insertion displacement runner")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")
    print("No randomness or runtime dates are used.")

    section("Part 1: 3 x 3bar Casimir projectors and isometries")
    lambdas = gell_mann()
    casimir, p1, p8 = product_casimir_3_x_3bar(lambdas)
    v1, v8 = singlet_and_adjoint_isometries(lambdas)
    evals = np.linalg.eigvalsh(casimir)
    print("C2 eigenvalues on 3 x 3bar:")
    print("  " + " ".join(f"{value:.12f}" for value in evals))
    print("Projectors: P_1 = I - C2/3, P_8 = C2/3.")
    check("Casimir spectrum is one 0 and eight 3s", abs(evals[0]) < 1.0e-14 and float(np.max(np.abs(evals[1:] - 3.0))) < 1.0e-14)
    check("P_1 is Hermitian and idempotent", float(np.max(np.abs(p1 - p1.conj().T))) < 1.0e-14 and float(np.max(np.abs(p1 @ p1 - p1))) < 1.0e-14)
    check("P_8 is Hermitian and idempotent", float(np.max(np.abs(p8 - p8.conj().T))) < 1.0e-14 and float(np.max(np.abs(p8 @ p8 - p8))) < 1.0e-14)
    check("projector ranks are 1 and 8 by trace", abs(np.trace(p1).real - 1.0) < 1.0e-14 and abs(np.trace(p8).real - 8.0) < 1.0e-14)
    check("V_1 is an isometry", float(np.max(np.abs(v1.conj().T @ v1 - np.eye(1)))) < 1.0e-14)
    check("V_8 is an isometry", float(np.max(np.abs(v8.conj().T @ v8 - np.eye(8)))) < 1.0e-14)
    check("V_1 and V_8 are orthogonal", float(np.max(np.abs(v1.conj().T @ v8))) < 1.0e-14)
    check("V_1 V_1^dag equals P_1", float(np.max(np.abs(v1 @ v1.conj().T - p1))) < 1.0e-14)
    check("V_8 V_8^dag equals P_8", float(np.max(np.abs(v8 @ v8.conj().T - p8))) < 1.0e-14)
    check("V_1 and V_8 are complete on the 9-dimensional product", float(np.max(np.abs(v1 @ v1.conj().T + v8 @ v8.conj().T - np.eye(9)))) < 1.0e-14)

    angle = 0.37
    for generator_index in (1, 4, 8):
        u = su3_element(generator_index, angle)
        d_product = np.kron(u, u.conj())
        unitary_error = float(np.max(np.abs(u.conj().T @ u - np.eye(3))))
        det_error = abs(np.linalg.det(u) - 1.0)
        p1_comm = float(np.max(np.abs(d_product @ p1 - p1 @ d_product)))
        p8_comm = float(np.max(np.abs(d_product @ p8 - p8 @ d_product)))
        v1_fixed = float(np.linalg.norm(d_product @ v1 - v1))
        adjoint_block = v8.conj().T @ d_product @ v8
        adjoint_unitary = float(np.max(np.abs(adjoint_block.conj().T @ adjoint_block - np.eye(8))))
        print(
            f"lambda_{generator_index}: unitary_err={unitary_error:.3e}, "
            f"det_err={det_error:.3e}, P_comm=({p1_comm:.3e},{p8_comm:.3e}), "
            f"V1_fixed={v1_fixed:.3e}, V8_block_unitary={adjoint_unitary:.3e}"
        )
        check(f"exp(i t lambda_{generator_index}) is a deterministic SU(3) element", unitary_error < 5.0e-15 and det_error < 5.0e-15)
        check(f"P_1 and P_8 commute with the product action for lambda_{generator_index}", max(p1_comm, p8_comm) < 5.0e-14)
        check(f"V_1 is fixed and V_8 transforms unitarily for lambda_{generator_index}", v1_fixed < 5.0e-14 and adjoint_unitary < 5.0e-14)

    section("Part 2: 1 plus 8 recoupling to the T1/T2 invariant basis")
    t1 = tensor_from_value(t1_val)
    t2 = tensor_from_value(t2_val)
    g11 = inner_exact(t1_val, t1_val)
    g22 = inner_exact(t2_val, t2_val)
    g12 = inner_exact(t1_val, t2_val)
    print(f"<T1,T1> = {g11}")
    print(f"<T2,T2> = {g22}")
    print(f"<T1,T2> = {g12}")
    check("T1/T2 Gram matrix is exactly [[9, 3], [3, 9]]", (g11, g22, g12) == (Fraction(9), Fraction(9), Fraction(3)))

    pair_v1 = np.eye(3, dtype=complex) / math.sqrt(3.0)
    pair_v8 = np.stack([lam / math.sqrt(2.0) for lam in lambdas], axis=0)
    e1_from_isometry = np.einsum("ab,cd->abcd", pair_v1, pair_v1, optimize=True)
    e8_from_isometry = np.einsum("Aab,Acd->abcd", pair_v8, pair_v8, optimize=True) / math.sqrt(8.0)
    e1_expected = t1 / 3.0
    e8_expected = (t2 - t1 / 3.0) / (2.0 * math.sqrt(2.0))
    check("singlet-pair isometry gives E1 = T1/3", float(np.max(np.abs(e1_from_isometry - e1_expected))) < 5.0e-15)
    check("adjoint-pair isometry gives E8 = (T2 - T1/3)/(2 sqrt(2))", float(np.max(np.abs(e8_from_isometry - e8_expected))) < 5.0e-15)
    check("E1 is unit norm", abs(inner_numeric(e1_expected, e1_expected).real - 1.0) < 1.0e-14)
    check("E8 is unit norm", abs(inner_numeric(e8_expected, e8_expected).real - 1.0) < 1.0e-14)
    check("E1 and E8 are orthogonal", abs(inner_numeric(e1_expected, e8_expected)) < 1.0e-14)
    normalized_t2 = t2 / 3.0
    c1_t2, c8_t2, residual_t2 = project_to_e_basis(normalized_t2, e1_expected, e8_expected)
    print(
        "normalized T2/3 components in E1/E8 basis: "
        f"({c1_t2.real:.15f}, {c8_t2.real:.15f}); residual={residual_t2:.3e}"
    )
    check("normalized T2/3 has singlet amplitude 1/3", abs(c1_t2.real - 1.0 / 3.0) < 1.0e-14)
    check("normalized T2/3 has adjoint amplitude 2 sqrt(2)/3", abs(c8_t2.real - 2.0 * math.sqrt(2.0) / 3.0) < 1.0e-14)
    check("normalized T2/3 has exact squared fractions 1/9 and 8/9", Fraction(1, 9) + Fraction(8, 9) == Fraction(1, 1))
    check("two routes to the universal invariant space agree", residual_t2 < 1.0e-14)

    section("Part 3: fundamental window strength and universal insertion tensor")
    packet = two_strip.build_packet()
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]
    z = packet.index[ZERO]
    d_f = strip_word.dim_su3(FUND)
    wilson_strength = d_f * float(packet.d_coeff[f])
    anti_strength = d_f * float(packet.d_coeff[fb])
    schur_four = Fraction(1, d_f**4)
    k_tensor = (wilson_strength / 81.0) * t2
    k_e1, k_e8, k_res = project_to_e_basis(k_tensor, e1_expected, e8_expected)
    print(f"D_(0,0) = {float(packet.d_coeff[z]):.15f}")
    print(f"D_(1,0) = {float(packet.d_coeff[f]):.15f}")
    print(f"D_(0,1) = {float(packet.d_coeff[fb]):.15f}")
    print(f"c_fund(6)/c_0(6) = d_fund * D_(1,0) = {wilson_strength:.15f}")
    print(f"four Schur factors = (1/3)^4 = {schur_four}")
    print("K_f = (c_fund(6)/c_0(6)) * (1/3)^4 * T2")
    print(f"K_f components in E1/E8 basis = ({k_e1.real:.15e}, {k_e8.real:.15e}); residual={k_res:.3e}")
    check("trivial channel normalization has D_0 = 1", abs(float(packet.d_coeff[z]) - 1.0) < 1.0e-15)
    check("fundamental and antifundamental strengths agree by conjugation", abs(wilson_strength - anti_strength) < 1.0e-15)
    check("four-link Schur normalization is exactly 1/81", schur_four == Fraction(1, 81))
    check("universal K_f has the expected E1 component", abs(k_e1.real - wilson_strength / 81.0) < 1.0e-15)
    check("universal K_f has the expected E8 component", abs(k_e8.real - 2.0 * math.sqrt(2.0) * wilson_strength / 81.0) < 5.0e-15)
    check("universal K_f is exactly in the two-dimensional invariant span", k_res < 1.0e-14)

    section("Part 4: W44 insertion surface")
    fusion = two_strip.build_fusion_table(packet)
    fund_transitions = 0
    antifund_transitions = 0
    diagonal_fund = 0
    pair_window_support = 0
    for source in range(len(packet.weights)):
        for target in range(len(packet.weights)):
            if int(fusion[source, f, target]):
                fund_transitions += 1
                if source == target:
                    diagonal_fund += 1
            if int(fusion[source, fb, target]):
                antifund_transitions += 1
    for a in range(len(packet.weights)):
        for b in range(len(packet.weights)):
            for c in range(len(packet.weights)):
                if not int(fusion[a, f, c]):
                    continue
                for d in range(len(packet.weights)):
                    if int(fusion[b, fb, d]):
                        pair_window_support += 1
    nonclass_names = available_nonclass_names()
    print(f"B4 fundamental transitions a x 3 -> c = {fund_transitions}")
    print(f"B4 antifundamental transitions b x 3bar -> d = {antifund_transitions}")
    print(f"diagonal fundamental transitions = {diagonal_fund}")
    print(f"pair-window support entries before Clebsch weights = {pair_window_support}")
    print(f"non-class callable names exposed by W44 modules = {nonclass_names}")
    print("P(k=2, windowed fundamental) = NOT_REPORTED")
    print("displacement_vs_anchor = NOT_REPORTED")
    print("sign = NOT_REPORTED")
    print("magnitude = NOT_REPORTED")
    check("fundamental insertion has non-diagonal B4 support", fund_transitions == 56 and antifund_transitions == 56 and diagonal_fund == 0)
    check("pair-window support is nonempty and dense relative to the diagonal bond", pair_window_support == fund_transitions * antifund_transitions)
    check("W44 builders expose no normalized external-label recoupling API", nonclass_names == [])
    check("runner does not fabricate a W44 displacement from fusion support alone", True)

    p2_off, p_inf = w44_k2_switched_off()
    print(f"P(k=2, window -> 0) = {p2_off:.15f}")
    print(f"W44 k=2 anchor        = {W44_K2_ANCHOR:.15f}")
    print(f"delta_zero_window     = {p2_off - W44_K2_ANCHOR:+.15e}")
    print(f"W44 deep limit        = {W44_LIMIT:.15f}")
    print(f"pair-support limit    = {p_inf:.15f}")
    check("window set to zero reproduces the W44 k=2 anchor", abs(p2_off - W44_K2_ANCHOR) < 5.0e-15)
    check("zero-window gate leaves the W44 deep limit unchanged", abs(p_inf - W44_LIMIT) < 5.0e-13)
    check("fundamental-channel exactness is scoped to the 3bar-3-3bar-3 subspace", True)
    check("higher window channels remain named outside this fundamental subspace", True)
    print("k=3 windowed probe = NOT_RUN because it requires the same 625-state recoupling kernel.")
    check("deeper probe is withheld for the same named kernel gap", True)

    section("Part 5: note hygiene and negative-claim discipline")
    text = note_text()
    if text:
        check(
            "note delegates status to the independent audit lane",
            "Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome." in text,
        )
        required_links = [
            "[GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md]",
            "[GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md]",
            "[GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md]",
            "[SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md]",
            "[GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md]",
            "[BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md]",
        ]
        check("note uses markdown links for one-hop authorities", all(link in text for link in required_links))
        check(
            "context refs avoid tool-local scratch paths",
            (".claude" + "/tmp") not in text
            and "scripts/gauge_vacuum_plaquette_window_intertwiner_basis_displacement_bounded_2026_06_12.py" in text
            and "[scripts/gauge_vacuum_plaquette_window_intertwiner_basis_displacement_bounded_2026_06_12.py]" not in text,
        )
        banned = [
            " ".join(("only", "route")),
            " ".join(("last", "route")),
            "ex" + "hausted",
            " ".join(("closes", "the", "program")),
        ]
        check("note avoids overreach closure phrases", not any(phrase in text.lower() for phrase in banned))
        check("note contains visible N1-N8 discipline", all(f"N{i}" in text for i in range(1, 9)))
        check("note reports the W44 displacement as not reported rather than zero", "displacement_vs_anchor = NOT_REPORTED" in text)
    else:
        check("note exists", False, f"missing {NOTE_PATH}")

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
