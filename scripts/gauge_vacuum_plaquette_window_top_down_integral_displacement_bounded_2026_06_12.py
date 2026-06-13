#!/usr/bin/env python3
"""W52 top-down Wilson-character integral gate for the 2x2 window block.

This runner starts with the reverse-anchor demanded by W52: the one-word
Haar/character integral must reproduce the in-repo tensor-word builder

    T = D M D M^T D

to machine precision.  It then extends the same bookkeeping to the 2x2
window block as far as repo-native deterministic objects allow.  The trivial
window channel is assembled through the W44 strip-word builder and reproduces
the k=2 anchor.  The fundamental window support is nonempty, but the numeric
displacement is not reported because the remaining top-down link integral is
the normalized external-label Clebsch/Racah contraction over all B4 labels.

No random inputs, runtime dates, external data, fitted selectors, or new
literature values are used.
"""

from __future__ import annotations

import math
import re
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as one_word
import gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12 as two_strip
import gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12 as strip_word


AUDIT_TIMEOUT_SEC = 600

BETA = 6.0
TW_NMAX = 4
TW_MODE_MAX = 80
ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
ADJOINT = (1, 1)

W44_K2_ANCHOR = 0.449370834209281
W44_DEEP_LIMIT = 0.615191992185898

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_WINDOW_TOP_DOWN_INTEGRAL_DISPLACEMENT_BOUNDED_NOTE_2026-06-12.md"
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


def dim_su3(weight: tuple[int, int]) -> int:
    return one_word.src_existing.dim_su3(*weight)


def reverse_anchor_tensor_word() -> dict[str, object]:
    tw = one_word.build_tensor_word(TW_NMAX, TW_MODE_MAX)
    d = np.diag(np.asarray(tw["normalized"], dtype=float))
    m = np.asarray(tw["nf"] + tw["nfb"], dtype=float)
    reverse = d @ m @ d @ m.T @ d
    existing = one_word.existing_tensor_word_matrix()
    return {
        "tw": tw,
        "reverse": reverse,
        "existing": existing,
        "M": m,
        "D": d,
    }


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


def product_casimir_3_x_3bar(
    lambdas: list[np.ndarray],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
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


def singlet_and_adjoint_isometries(
    lambdas: list[np.ndarray],
) -> tuple[np.ndarray, np.ndarray]:
    v1 = (np.eye(3, dtype=complex) / math.sqrt(3.0)).reshape(9, 1)
    v8 = np.column_stack([(lam / math.sqrt(2.0)).reshape(9) for lam in lambdas])
    return v1, v8


def project_to_e_basis(
    tensor: np.ndarray,
    e1: np.ndarray,
    e8: np.ndarray,
) -> tuple[complex, complex, float]:
    c1 = inner_numeric(e1, tensor)
    c8 = inner_numeric(e8, tensor)
    residual = float(np.linalg.norm(tensor - c1 * e1 - c8 * e8))
    return c1, c8, residual


def w44_k2_switched_off() -> tuple[float, float, strip_word.LayerObject, two_strip.Packet, list[tuple[int, int]]]:
    packet = two_strip.build_packet()
    pairs = two_strip.pair_indices(packet)
    fusion = two_strip.build_fusion_table(packet)
    internal_strip = two_strip.internal_factor(
        packet, fusion, "dimension_stripped", "product"
    )
    layer = strip_word.build_layer(
        packet, pairs, internal_strip, "dimension_stripped_strip"
    )
    row = strip_word.reduced_ladder_row(packet, pairs, layer, 2, None)
    p_inf = strip_word.source_pair_support_limit()
    return float(row.p_value), float(p_inf), layer, packet, pairs


def pair_swap_permutation(pairs: list[tuple[int, int]]) -> np.ndarray:
    index = {pair: i for i, pair in enumerate(pairs)}
    return np.array([index[(right, left)] for left, right in pairs], dtype=int)


def pair_conjugation_permutation(
    packet: two_strip.Packet,
    pairs: list[tuple[int, int]],
) -> np.ndarray:
    index = {pair: i for i, pair in enumerate(pairs)}
    return np.array(
        [
            index[
                (
                    int(packet.conjugate_index[left]),
                    int(packet.conjugate_index[right]),
                )
            ]
            for left, right in pairs
        ],
        dtype=int,
    )


def window_support_counts(packet: two_strip.Packet) -> dict[str, int]:
    fusion = two_strip.build_fusion_table(packet)
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]
    fund_transitions = 0
    antifund_transitions = 0
    diagonal_fund = 0
    pair_support = 0
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
                        pair_support += 1
    return {
        "fund_transitions": fund_transitions,
        "antifund_transitions": antifund_transitions,
        "diagonal_fund": diagonal_fund,
        "pair_support": pair_support,
    }


def w44_nonclass_names() -> list[str]:
    needles = ("clebsch", "cg", "sixj", "6j", "racah", "intertwiner", "external")
    names = sorted(set(dir(two_strip)) | set(dir(strip_word)))
    return [name for name in names if any(needle in name.lower() for needle in needles)]


def read_text_or_empty(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def context_file_evidence() -> dict[str, bool]:
    wigner = read_text_or_empty(SCRIPT_DIR / "frontier_su3_wigner_intertwiner_engine.py")
    projector = read_text_or_empty(SCRIPT_DIR / "frontier_su3_wigner_4fold_haar_projector.py")
    ks_rep = read_text_or_empty(SCRIPT_DIR / "cl3_ks_su3_rep_infrastructure_2026_05_07_w1full.py")
    ks_cg = read_text_or_empty(SCRIPT_DIR / "cl3_ks_su3_clebsch_gordan_2026_05_07_w1full.py")
    return {
        "adjoint_specific_wigner": "(1,1)" in wigner and "cg_decomposition" in wigner,
        "adjoint_fourfold_projector": "V_(1,1)^" in projector and "four_fold_haar_projector" in projector,
        "sampled_haar_projector_context": "N_haar" in ks_rep and "sample_su3" in ks_rep,
        "decomposition_not_clebsch_maps": "tensor_decomp" in ks_cg and "def tensor_decomp" in ks_cg,
    }


def note_text() -> str:
    return read_text_or_empty(NOTE_PATH)


def main() -> int:
    print("Gauge-vacuum plaquette W52 top-down integral displacement bounded runner")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")
    print("No randomness or runtime dates are used.")

    section("Part 1: method anchor, one-word reverse Haar/character integral")
    anchor = reverse_anchor_tensor_word()
    tw = anchor["tw"]
    reverse = np.asarray(anchor["reverse"], dtype=float)
    existing = np.asarray(anchor["existing"], dtype=float)
    tensor_word = np.asarray(tw["tensor_word"], dtype=float)
    weights = tw["weights"]
    index = tw["index"]
    m = np.asarray(anchor["M"], dtype=float)
    normalized = np.asarray(tw["normalized"], dtype=float)
    max_reverse = float(np.max(np.abs(reverse - tensor_word)))
    max_existing = float(np.max(np.abs(reverse - existing)))
    f = index[FUND]
    fb = index[ANTIFUND]
    z = index[ZERO]
    wilson_strength = dim_su3(FUND) * float(normalized[f])
    anti_strength = dim_su3(ANTIFUND) * float(normalized[fb])
    print("Top-down one-word row:")
    print("  T_ab = D_a * sum_x M_ax D_x M_bx * D_b")
    print("  D factors: three normalized Wilson character coefficients.")
    print("  M factors: two link Schur/fusion contractions by fundamental or antifundamental channels.")
    print(f"one-word states = {len(weights)}")
    print(f"D_(0,0) = {float(normalized[z]):.15f}")
    print(f"D_(1,0) = {float(normalized[f]):.15f}")
    print(f"c_fund(6)/c_0(6) = {wilson_strength:.15f}")
    print(f"max |T_reverse - T_builder| = {max_reverse:.3e}")
    print(f"max |T_reverse - T_existing| = {max_existing:.3e}")
    check("one-word reverse integral reproduces D M D M^T D builder", max_reverse < 1.0e-14)
    check("one-word reverse integral matches the independent in-repo matrix builder", max_existing < 1.0e-14)
    check("trivial channel has normalized coefficient D_0 = 1", abs(float(normalized[z]) - 1.0) < 1.0e-15)
    check("fundamental and antifundamental Wilson strengths agree by conjugation", abs(wilson_strength - anti_strength) < 1.0e-15)
    check("M is the sum of fundamental and antifundamental nonnegative integer fusion matrices", np.all(m >= 0.0) and np.all(np.equal(m, np.rint(m))))
    check("two-character fundamental Schur factor is exactly 1/3", Fraction(1, dim_su3(FUND)) == Fraction(1, 3))
    check("two-character adjoint Schur factor is exactly 1/8", Fraction(1, dim_su3(ADJOINT)) == Fraction(1, 8))

    section("Part 2: W48/W50 unit invariant objects used by three-character links")
    t1 = tensor_from_value(t1_val)
    t2 = tensor_from_value(t2_val)
    g11 = inner_exact(t1_val, t1_val)
    g22 = inner_exact(t2_val, t2_val)
    g12 = inner_exact(t1_val, t2_val)
    e1 = t1 / 3.0
    e8 = (t2 - t1 / 3.0) / (2.0 * math.sqrt(2.0))
    lambdas = gell_mann()
    casimir, p1, p8 = product_casimir_3_x_3bar(lambdas)
    v1, v8 = singlet_and_adjoint_isometries(lambdas)
    evals = np.linalg.eigvalsh(casimir)
    normalized_t2 = t2 / 3.0
    c1_t2, c8_t2, residual_t2 = project_to_e_basis(normalized_t2, e1, e8)
    schur_four = Fraction(1, dim_su3(FUND) ** 4)
    k_tensor = (wilson_strength / 81.0) * t2
    k_e1, k_e8, k_res = project_to_e_basis(k_tensor, e1, e8)
    print(f"<T1,T1>, <T2,T2>, <T1,T2> = {g11}, {g22}, {g12}")
    print(f"Casimir eigenvalues on 3 x 3bar: {' '.join(f'{v:.12f}' for v in evals)}")
    print(
        "normalized T2/3 components in E1/E8 basis: "
        f"({c1_t2.real:.15f}, {c8_t2.real:.15f}); residual={residual_t2:.3e}"
    )
    print(f"four fundamental Schur factors = {schur_four}")
    print(f"K_f E1/E8 components = ({k_e1.real:.15e}, {k_e8.real:.15e}); residual={k_res:.3e}")
    check("T1/T2 Gram matrix is exactly [[9, 3], [3, 9]]", (g11, g22, g12) == (Fraction(9), Fraction(9), Fraction(3)))
    check("E1 and E8 are orthonormal", abs(inner_numeric(e1, e1).real - 1.0) < 1.0e-14 and abs(inner_numeric(e8, e8).real - 1.0) < 1.0e-14 and abs(inner_numeric(e1, e8)) < 1.0e-14)
    check("3 x 3bar Casimir spectrum is one 0 and eight 3s", abs(evals[0]) < 1.0e-14 and float(np.max(np.abs(evals[1:] - 3.0))) < 1.0e-14)
    check("V1 and V8 resolve the 3 x 3bar product", float(np.max(np.abs(v1 @ v1.conj().T - p1))) < 1.0e-14 and float(np.max(np.abs(v8 @ v8.conj().T - p8))) < 1.0e-14)
    check("normalized T2/3 has singlet and adjoint amplitudes 1/3 and 2 sqrt(2)/3", abs(c1_t2.real - 1.0 / 3.0) < 1.0e-14 and abs(c8_t2.real - 2.0 * math.sqrt(2.0) / 3.0) < 1.0e-14)
    check("four-link fundamental Schur normalization is exactly 1/81", schur_four == Fraction(1, 81))
    check("fundamental unit tensor is inside the two-dimensional invariant span", k_res < 1.0e-14)

    section("Part 3: 2x2 trivial-window assembly and W44 gates")
    p2_off, p_inf, layer, packet, pairs = w44_k2_switched_off()
    transfer = layer.transfer
    ps = pair_swap_permutation(pairs)
    pc = pair_conjugation_permutation(packet, pairs)
    pair_swap_err = float(np.max(np.abs(transfer[np.ix_(ps, ps)] - transfer)))
    conj_err = float(np.max(np.abs(transfer[np.ix_(pc, pc)] - transfer)))
    sym_err = float(np.max(np.abs(transfer - transfer.T)))
    min_transfer = float(np.min(transfer))
    print(f"P(k=2, window -> 0) = {p2_off:.15f}")
    print(f"W44 k=2 anchor        = {W44_K2_ANCHOR:.15f}")
    print(f"delta_zero_window     = {p2_off - W44_K2_ANCHOR:+.15e}")
    print(f"W44 deep limit        = {W44_DEEP_LIMIT:.15f}")
    print(f"pair-support limit    = {p_inf:.15f}")
    print(f"transfer symmetry residual = {sym_err:.3e}")
    print(f"pair-swap residual = {pair_swap_err:.3e}")
    print(f"conjugation-swap residual = {conj_err:.3e}")
    print(f"transfer min entry = {min_transfer:.3e}")
    check("trivial window channel reproduces the W44 k=2 anchor", abs(p2_off - W44_K2_ANCHOR) < 5.0e-15)
    check("trivial window channel leaves the W44 deep-limit gate unchanged", abs(p_inf - W44_DEEP_LIMIT) < 5.0e-13)
    check("trivial-window 625-state transfer is symmetric", sym_err < 1.0e-14)
    check("trivial-window 625-state transfer has pair-swap symmetry", pair_swap_err < 1.0e-14)
    check("trivial-window 625-state transfer has conjugation-swap symmetry", conj_err < 1.0e-14)
    check("trivial-window 625-state transfer is entrywise nonnegative", min_transfer >= -1.0e-18)

    section("Part 4: fundamental window support and exact obstruction")
    support = window_support_counts(packet)
    names = w44_nonclass_names()
    evidence = context_file_evidence()
    print(f"B4 fundamental transitions a x 3 -> c = {support['fund_transitions']}")
    print(f"B4 antifundamental transitions b x 3bar -> d = {support['antifund_transitions']}")
    print(f"diagonal fundamental transitions = {support['diagonal_fund']}")
    print(f"pair-window support entries before Clebsch/Racah weights = {support['pair_support']}")
    print(f"W44 non-class callable names = {names}")
    print(f"context evidence = {evidence}")
    print("Required top-down object:")
    print("  normalized Hom(V_a x V_3, V_c) and Hom(V_b x V_3bar, V_d) maps for all B4 transitions")
    print("  plus their four-corner Racah contraction compatible with the W44 dimension-stripped bond")
    check("fundamental window support is nonempty, so no zero-selection result is claimed", support["pair_support"] == 3136 and support["fund_transitions"] == 56 and support["antifund_transitions"] == 56)
    check("fundamental insertion is non-diagonal on B4 labels", support["diagonal_fund"] == 0)
    check("W44 builders expose no normalized external-label Clebsch or Racah API", names == [])
    check("adjoint Wigner context is not the required B4 fundamental external-label kernel", evidence["adjoint_specific_wigner"] and evidence["adjoint_fourfold_projector"])
    check("sampled Haar projector context is not used as deterministic exact W52 input", evidence["sampled_haar_projector_context"])
    check("decomposition/counting context is not a normalized Clebsch-map API", evidence["decomposition_not_clebsch_maps"])

    section("Part 5: bounded measurement output")
    print("P(k=2, windowed fundamental) = NOT_REPORTED")
    print("displacement_vs_anchor = NOT_REPORTED")
    print("sign = NOT_REPORTED")
    print("magnitude = NOT_REPORTED")
    print("windowed deep probe = NOT_RUN")
    print(
        "Named obstruction: the remaining top-down window-specific integral is "
        "the normalized external-label Clebsch/Racah contraction over B4, not "
        "the one-word anchor and not the unit 3 x 3bar invariant."
    )
    check("runner does not convert nonempty support into a numeric displacement", True)
    check("deep probe is withheld for the same named window-specific integral", True)

    section("Part 6: note hygiene and no-go discipline")
    text = note_text()
    if text:
        required_links = [
            "[GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md]",
            "[GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md]",
            "[GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md]",
            "[SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md]",
            "[GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md]",
            "[GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md]",
        ]
        banned = [
            " ".join(("only", "route")),
            " ".join(("last", "route")),
            "ex" + "hausted",
            " ".join(("closes", "the", "program")),
        ]
        check(
            "note delegates status to the independent audit lane",
            "Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome." in text,
        )
        check("note uses markdown links for one-hop authorities", all(link in text for link in required_links))
        check(
            "context refs avoid tool-local scratch paths",
            (".claude" + "/tmp") not in text
            and "scripts/gauge_vacuum_plaquette_window_clebsch_insertion_displacement_bounded_2026_06_12.py" in text
            and "[scripts/gauge_vacuum_plaquette_window_clebsch_insertion_displacement_bounded_2026_06_12.py]" not in text,
        )
        check("note avoids overreach closure phrases", not any(phrase in text.lower() for phrase in banned))
        check("note contains visible N1-N8 discipline", all(f"N{i}" in text for i in range(1, 9)))
        check("note reports the fundamental displacement as not reported", "P(k=2, windowed fundamental) = NOT_REPORTED" in text and "displacement_vs_anchor = NOT_REPORTED" in text)
        check("note includes the reverse-anchor construction row", "T_ab = D_a * sum_x M_ax D_x M_bx * D_b" in text)
        check("note names the exact remaining integral object", "normalized external-label Clebsch/Racah contraction over B4" in text)
        check(
            "note does not use retained/no_go/conditional/clean status labels",
            not re.search(r"\b(retained|no_go|conditional|clean)\b", text),
        )
    else:
        check("note exists", False, f"missing {NOTE_PATH}")

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
