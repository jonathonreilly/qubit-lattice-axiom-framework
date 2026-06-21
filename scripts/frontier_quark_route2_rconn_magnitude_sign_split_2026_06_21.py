#!/usr/bin/env python3
"""Exact Route-2 R_conn magnitude/sign split support check.

This runner checks a narrow support theorem for the S3/Route-2 endpoint
residual.  The current bank does not derive the typed bridge

    |gamma_T(center) / gamma_E(center)| = R_conn = 8/9.

But if that typed magnitude bridge is supplied, the already-tested positivity
bound q_E > 0 forces the sign of the center T/E ratio.  The remaining bridge
can then be stated as a magnitude bridge, not as an independent signed bridge.
"""

from __future__ import annotations

from collections import defaultdict, deque
from fractions import Fraction
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0

SUPPORT_DENOMINATOR = 6
Q_T = Fraction(5, 6)
S_TE = Fraction(-2, 1)
NEGATIVE_NUMERATOR = S_TE * Q_T
R_CONN = Fraction(8, 9)
TARGET_Q_E = Fraction(15, 8)
TARGET_RHO_E = Fraction(21, 4)

NOTE_PATH = DOCS / "QUARK_ROUTE2_RCONN_MAGNITUDE_SIGN_SPLIT_EXACT_SUPPORT_NOTE_2026-06-21.md"


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def label(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def r_conn(n_c: int) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def q_from_rho(rho_e: Fraction, denominator: int = SUPPORT_DENOMINATOR) -> Fraction:
    return Fraction(1, 1) + rho_e / denominator


def rho_from_q(q_e: Fraction, denominator: int = SUPPORT_DENOMINATOR) -> Fraction:
    return denominator * (q_e - 1)


def center_te(q_e: Fraction, q_t: Fraction = Q_T, s_te: Fraction = S_TE) -> Fraction:
    return s_te * q_t / q_e


def endpoint_from_signed_center(
    c_te: Fraction,
    q_t: Fraction = Q_T,
    s_te: Fraction = S_TE,
    denominator: int = SUPPORT_DENOMINATOR,
) -> tuple[Fraction, Fraction]:
    q_e = s_te * q_t / c_te
    return q_e, rho_from_q(q_e, denominator)


def endpoint_from_positive_magnitude(
    magnitude: Fraction,
    q_t: Fraction = Q_T,
    s_te: Fraction = S_TE,
    denominator: int = SUPPORT_DENOMINATOR,
) -> tuple[Fraction, Fraction, Fraction]:
    """Use q_E > 0 to choose the sign of c_TE under |c_TE| = magnitude."""
    assert s_te * q_t < 0
    c_te = -magnitude
    q_e, rho_e = endpoint_from_signed_center(c_te, q_t, s_te, denominator)
    return c_te, q_e, rho_e


def endpoint_with_denominator(
    denominator: int,
    magnitude: Fraction = R_CONN,
    rho_t: Fraction = Fraction(-1, 1),
    s_te: Fraction = S_TE,
) -> tuple[Fraction, Fraction, Fraction]:
    q_t = Fraction(1, 1) + rho_t / denominator
    c_te = -magnitude
    q_e, rho_e = endpoint_from_signed_center(c_te, q_t, s_te, denominator)
    return q_t, q_e, rho_e


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_anchor(path: Path, snippets: tuple[str, ...]) -> None:
    text = read(path)
    for index, snippet in enumerate(snippets, 1):
        check(
            f"authority_anchor_{path.name}_{index}",
            snippet in text,
            snippet,
        )


def reachable(edges: tuple[tuple[str, str], ...], source: str, target: str) -> bool:
    graph: dict[str, list[str]] = defaultdict(list)
    for left, right in edges:
        graph[left].append(right)

    queue: deque[str] = deque([source])
    seen = {source}
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False


CURRENT_TYPED_EDGES: tuple[tuple[str, str], ...] = (
    ("route2_support_carrier", "route2_restricted_readout_family"),
    ("route2_restricted_readout_family", "route2_endpoint_algebra"),
    ("route2_t_side_candidates", "route2_q_T_5_6_and_shell_TE_minus_2"),
    ("route2_center_TE_minus_8_9", "route2_q_E_15_8"),
    ("route2_q_E_15_8", "route2_rho_E_21_4"),
    ("su3_color_trace_channel", "su3_R_conn_8_9"),
)

MISSING_SIGNED_BRIDGE = ("su3_R_conn_8_9", "route2_center_TE_minus_8_9")
MISSING_MAGNITUDE_BRIDGE = ("su3_R_conn_8_9", "route2_abs_center_TE_8_9")
POSITIVITY_SIGN_EDGE = ("route2_abs_center_TE_8_9", "route2_center_TE_minus_8_9")


def main() -> None:
    check("su3_adjoint_fraction_nc3", r_conn(3) == R_CONN, f"R_conn={label(r_conn(3))}")
    check("su3_adjoint_fraction_nc2_control", r_conn(2) == Fraction(3, 4), f"R_conn(Nc=2)={label(r_conn(2))}")
    check("su3_adjoint_fraction_nc4_control", r_conn(4) == Fraction(15, 16), f"R_conn(Nc=4)={label(r_conn(4))}")
    check("granted_q_T_exact", Q_T == Fraction(5, 6), f"q_T={label(Q_T)}")
    check("granted_shell_ratio_exact", S_TE == Fraction(-2, 1), f"s_TE={label(S_TE)}")
    check("center_ratio_numerator_negative", NEGATIVE_NUMERATOR == Fraction(-5, 3), f"s_TE*q_T={label(NEGATIVE_NUMERATOR)}")

    signed_q, signed_rho = endpoint_from_signed_center(-R_CONN)
    check("signed_bridge_forces_q_E", signed_q == TARGET_Q_E, f"q_E={label(signed_q)}")
    check("signed_bridge_forces_rho_E", signed_rho == TARGET_RHO_E, f"rho_E={label(signed_rho)}")
    check("target_q_to_rho_equivalence", rho_from_q(TARGET_Q_E) == TARGET_RHO_E, "rho_E=6(q_E-1)")
    check("target_rho_to_q_equivalence", q_from_rho(TARGET_RHO_E) == TARGET_Q_E, "q_E=1+rho_E/6")

    negative_branch_q, negative_branch_rho = endpoint_from_signed_center(-R_CONN)
    positive_branch_q, positive_branch_rho = endpoint_from_signed_center(R_CONN)
    check("magnitude_negative_branch_has_abs_R_conn", abs(center_te(negative_branch_q)) == R_CONN, f"c_TE={label(center_te(negative_branch_q))}")
    check("magnitude_positive_branch_has_abs_R_conn", abs(center_te(positive_branch_q)) == R_CONN, f"c_TE={label(center_te(positive_branch_q))}")
    check("magnitude_negative_branch_is_target", negative_branch_q == TARGET_Q_E and negative_branch_rho == TARGET_RHO_E, f"q_E={label(negative_branch_q)}, rho_E={label(negative_branch_rho)}")
    check("magnitude_positive_branch_is_wrong_sign", positive_branch_q == Fraction(-15, 8) and positive_branch_rho == Fraction(-69, 4), f"q_E={label(positive_branch_q)}, rho_E={label(positive_branch_rho)}")
    check("positive_branch_violates_q_positive", positive_branch_q < 0, f"q_E={label(positive_branch_q)}")
    check("positive_branch_violates_rho_bound", positive_branch_rho < Fraction(-6, 1), f"rho_E={label(positive_branch_rho)} < -6")
    check("negative_branch_satisfies_positivity", negative_branch_q > 0 and negative_branch_rho > Fraction(-6, 1), f"q_E={label(negative_branch_q)}, rho_E={label(negative_branch_rho)}")

    c_te, q_e, rho_e = endpoint_from_positive_magnitude(R_CONN)
    check("positivity_forces_negative_center_ratio", c_te == -R_CONN, f"c_TE={label(c_te)}")
    check("magnitude_plus_positivity_forces_q_E", q_e == TARGET_Q_E, f"q_E={label(q_e)}")
    check("magnitude_plus_positivity_forces_rho_E", rho_e == TARGET_RHO_E, f"rho_E={label(rho_e)}")

    q_positive_examples = (Fraction(1, 6), Fraction(1, 1), TARGET_Q_E, Fraction(7, 3))
    check(
        "sign_lemma_all_positive_q_examples_have_negative_center_ratio",
        all(center_te(q) < 0 for q in q_positive_examples),
        ", ".join(f"q={label(q)} -> c={label(center_te(q))}" for q in q_positive_examples),
    )
    check(
        "sign_lemma_algebraic_reason",
        NEGATIVE_NUMERATOR < 0,
        "c_TE=(s_TE*q_T)/q_E and q_E>0, so sign(c_TE)=negative",
    )

    rho_examples = (Fraction(0, 1), Fraction(1, 1), TARGET_RHO_E, Fraction(8, 1))
    q_examples = tuple(q_from_rho(rho) for rho in rho_examples)
    center_examples = tuple(center_te(q) for q in q_examples)
    check("positivity_bound_admits_multiple_rhos", len(set(rho_examples)) == 4 and all(q > 0 for q in q_examples), ", ".join(label(rho) for rho in rho_examples))
    check("positivity_alone_does_not_select_magnitude", len(set(center_examples)) == 4, ", ".join(label(c) for c in center_examples))
    check("only_target_example_has_R_conn_magnitude", [rho for rho, c in zip(rho_examples, center_examples) if abs(c) == R_CONN] == [TARGET_RHO_E], "among tested positive examples")

    bound_examples = (Fraction(-69, 4), Fraction(-7, 1), Fraction(-5, 1), Fraction(0, 1), TARGET_RHO_E)
    check(
        "rho_bound_equivalent_to_q_positive_on_controls",
        all((rho > Fraction(-6, 1)) == (q_from_rho(rho) > 0) for rho in bound_examples),
        ", ".join(f"rho={label(rho)} q={label(q_from_rho(rho))}" for rho in bound_examples),
    )

    wrong_nc_q, wrong_nc_rho = endpoint_from_signed_center(-r_conn(2))
    check("wrong_nc2_magnitude_changes_q_E", wrong_nc_q == Fraction(20, 9), f"q_E={label(wrong_nc_q)}")
    check("wrong_nc2_magnitude_changes_rho_E", wrong_nc_rho == Fraction(22, 3), f"rho_E={label(wrong_nc_rho)}")
    d5_qt, d5_qe, d5_rho = endpoint_with_denominator(5)
    check("wrong_denominator5_changes_q_T", d5_qt == Fraction(4, 5), f"q_T={label(d5_qt)}")
    check("wrong_denominator5_changes_endpoint", d5_qe == Fraction(9, 5) and d5_rho == Fraction(4, 1), f"q_E={label(d5_qe)}, rho_E={label(d5_rho)}")
    d12_qt, d12_qe, d12_rho = endpoint_with_denominator(12)
    check("wrong_denominator12_changes_q_T", d12_qt == Fraction(11, 12), f"q_T={label(d12_qt)}")
    check("wrong_denominator12_changes_endpoint", d12_qe == Fraction(33, 16) and d12_rho == Fraction(51, 4), f"q_E={label(d12_qe)}, rho_E={label(d12_rho)}")

    check("current_bank_lacks_signed_bridge_edge", MISSING_SIGNED_BRIDGE not in CURRENT_TYPED_EDGES)
    check("current_bank_lacks_magnitude_bridge_edge", MISSING_MAGNITUDE_BRIDGE not in CURRENT_TYPED_EDGES)
    check(
        "current_bank_has_no_R_conn_to_rho_path",
        not reachable(CURRENT_TYPED_EDGES, "su3_R_conn_8_9", "route2_rho_E_21_4"),
    )
    magnitude_only_edges = CURRENT_TYPED_EDGES + (MISSING_MAGNITUDE_BRIDGE,)
    check(
        "magnitude_without_sign_reduction_has_no_rho_path",
        not reachable(magnitude_only_edges, "su3_R_conn_8_9", "route2_rho_E_21_4"),
    )
    augmented_edges = CURRENT_TYPED_EDGES + (MISSING_MAGNITUDE_BRIDGE, POSITIVITY_SIGN_EDGE)
    check(
        "magnitude_plus_positivity_sign_edge_reaches_rho",
        reachable(augmented_edges, "su3_R_conn_8_9", "route2_rho_E_21_4"),
    )

    check_anchor(
        DOCS / "RCONN_DERIVED_NOTE.md",
        (
            "At `N_c = 3`, `F_adj = 8/9`.",
            "The exact `8/9` support remains available as `F_adj`, not as a",
        ),
    )
    check_anchor(
        DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md",
        (
            "The sign and endpoint orientation are not supplied by the color projection",
            "There is no current typed edge",
        ),
    )
    check_anchor(
        DOCS / "ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md",
        (
            "**one-sided bound** `rho_E > -6`",
            "Selecting `rho_E` requires a shell-vs-center **distinguishing** input.",
        ),
    )
    check_anchor(
        DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "c_TE  := gamma_T(center) / gamma_E(center) = s_TE * q_T / q_E.",
            "q_T = 5/6,  s_TE = -2,  c_TE = -8/9",
        ),
    )
    check_anchor(
        DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md",
        (
            "Use `F_adj = 8/9` as `|c_TE|`",
            "Needs the typed signed bridge `gamma_T(center)/gamma_E(center) = -R_conn`",
        ),
    )

    note_exists = NOTE_PATH.exists()
    check("paired_note_exists", note_exists, str(NOTE_PATH.relative_to(ROOT)))
    if note_exists:
        note = read(NOTE_PATH)
        check(
            "paired_note_states_not_magnitude_derivation",
            "not a derivation of the typed magnitude bridge" in note,
        )
        check(
            "paired_note_keeps_exact_support_status",
            "**Status:** exact support" in note and "not an endpoint derivation" in note,
        )
        banned_phrases = (
            "retained " "branch-local",
            "would become " "retained",
            "promoted to " "retained",
            "retained on the actual " "surface",
            "Nature-grade " "closure",
            "closes the " "parent",
        )
        check(
            "paired_note_avoids_banned_overclaim_phrases",
            all(phrase not in note for phrase in banned_phrases),
        )
        check(
            "paired_note_status_line_not_bare_retained",
            re.search(r"(?m)^(?:\\*\\*)?Status(?:\\*\\*)?:\\s*(retained|promoted)\\b", note) is None,
        )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: exact support only. If a typed magnitude bridge "
        "|gamma_T(center)/gamma_E(center)|=R_conn=8/9 is supplied, the "
        "existing q_E>0 positivity bound forces c_TE=-R_conn, hence "
        "q_E=15/8 and rho_E=21/4. The current bank still lacks the typed "
        "magnitude bridge, so this is not an endpoint derivation."
    )
    raise SystemExit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
