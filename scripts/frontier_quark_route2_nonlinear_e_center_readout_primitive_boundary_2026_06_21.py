#!/usr/bin/env python3
"""Boundary check for the Route-2 nonlinear E-center readout primitive.

The runner is intentionally finite and exact. It verifies the endpoint
arithmetic, the inverse-square target sieve, and source-note guardrails saying
that current nonlinear/log/determinant/tensor surfaces do not derive the
missing E-center primitive.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"PASS: {label}{suffix}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"FAIL: {label}{suffix}")


def read_rel(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def contains_all(path: str, tokens: list[str]) -> None:
    text = read_rel(path)
    check(f"{path} exists", bool(text.strip()))
    for token in tokens:
        check(f"{path} contains marker: {token}", token in text)


def row_outputs(rho_e: Fraction) -> dict[str, Fraction]:
    """Reduced P(rho_E) outputs on the four endpoint columns."""
    return {
        "E_shell_E": Fraction(1),
        "E_center_E": Fraction(1) + rho_e / 6,
        "T_shell_T": Fraction(-2),
        "T_center_T": Fraction(-2) + Fraction(2, 6),
    }


def pow_fraction(base: Fraction, exponent: int) -> Fraction:
    if exponent >= 0:
        return base**exponent
    return Fraction(1, 1) / (base ** (-exponent))


def main() -> int:
    print("=== Route-2 nonlinear E-center readout primitive boundary ===")

    note_path = (
        "docs/QUARK_ROUTE2_NONLINEAR_E_CENTER_READOUT_PRIMITIVE_BOUNDARY_NOTE_2026-06-21.md"
    )
    runner_path = (
        "scripts/frontier_quark_route2_nonlinear_e_center_readout_primitive_boundary_2026_06_21.py"
    )
    contains_all(
        note_path,
        [
            "**Actual current-surface status:** no-go / exact negative boundary",
            "q_X w_X^2 = 5/24",
            "none of the checked named surfaces derives that law",
            "not a claim that no future nonlinear observable",
            "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
        ],
    )
    contains_all(
        runner_path,
        [
            "Fraction",
            "inverse-square target sieve",
            "current nonlinear/log/determinant/tensor surfaces",
        ],
    )

    print("\n=== Authority boundary markers ===")
    authority_markers = {
        "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md": [
            "endpoint dimensionless triple",
            "not derived by the current exact stack",
            "readout-map endpoint triple",
        ],
        "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": [
            "irreducible missing map entry",
            "beta_E / alpha_E = 21/4",
            "exact missing-map obstruction",
        ],
        "docs/QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md": [
            "E-center-blind",
            "cannot derive those values",
            "must supply a genuine E-center lift",
        ],
        "docs/ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md": [
            "fix the readout **norm**",
            "readout **direction**",
            "does **not** fix `rho_E`",
        ],
        "docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md": [
            "quadratic route is closed",
            "inverse-square characterization",
            "No named functional produces an",
        ],
        "docs/S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md": [
            "membership-but-not-uniqueness",
            "selection freedom",
            "not a derived physical primitive",
        ],
        "docs/S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_NOTE.md": [
            "exact tensor carrier is still absent",
            "bounded tensorized Schur/Dirichlet primitive",
            "does **not** claim",
        ],
        "docs/S3_TIME_CONSTRUCTED_SUPPORT_TENSOR_PRIMITIVE_NOTE.md": [
            "bounded support-response theorem",
            "not an exact tensor observable",
            "does not claim",
        ],
        "docs/OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md": [
            "not determinant-only",
            "determinant-only readout quotient",
            "it is not derivable",
        ],
        "docs/OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md": [
            "context bridge, not an axiom reduction",
            "does not derive the context from Record",
            "supplied context",
        ],
        "docs/REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md": [
            "It does not derive the determinant-character/log-character boundary",
            "separate physical-readout identifications",
            "does not set or predict an audit outcome",
        ],
        "docs/SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md": [
            "does not by itself select the physical logarithmic",
            "source-scale freedom",
            "does not close Y_T",
        ],
        "docs/POST_RECORD_SELECTOR_TANGENT_READOUT_WEIGHT_PROTOTYPE_2026-06-06.md": [
            "not selector/tangent/readout authority",
            "Does not derive a selector",
            "Record-derived selector/readout/tangent authority remains open",
        ],
    }
    for path, tokens in authority_markers.items():
        contains_all(path, tokens)

    print("\n=== Exact Route-2 endpoint algebra ===")
    rho_t = Fraction(-1)
    mu = Fraction(-2)
    rho_e = Fraction(21, 4)
    q_t = Fraction(1) + rho_t / 6
    q_e = Fraction(1) + rho_e / 6
    c_te = mu * q_t / q_e
    lam = q_e / q_t
    check("q_T from rho_T=-1 is 5/6", q_t == Fraction(5, 6), str(q_t))
    check("q_E from rho_E=21/4 is 15/8", q_e == Fraction(15, 8), str(q_e))
    check("c_TE is -8/9", c_te == Fraction(-8, 9), str(c_te))
    check("lambda=q_E/q_T is 9/4", lam == Fraction(9, 4), str(lam))
    check(
        "rho_E recovered from q_E=15/8",
        6 * (Fraction(15, 8) - 1) == rho_e,
        str(6 * (Fraction(15, 8) - 1)),
    )

    print("\n=== E-center freedom witness ===")
    candidates = [Fraction(-1), Fraction(0), Fraction(1), Fraction(21, 4)]
    outputs = {rho: row_outputs(rho) for rho in candidates}
    e_shell_values = {out["E_shell_E"] for out in outputs.values()}
    t_shell_values = {out["T_shell_T"] for out in outputs.values()}
    t_center_values = {out["T_center_T"] for out in outputs.values()}
    e_center_values = {out["E_center_E"] for out in outputs.values()}
    check("all candidate rho_E values agree on E-shell", len(e_shell_values) == 1, str(e_shell_values))
    check("all candidate rho_E values agree on T-shell", len(t_shell_values) == 1, str(t_shell_values))
    check("all candidate rho_E values agree on T-center", len(t_center_values) == 1, str(t_center_values))
    check("candidate rho_E values differ on E-center", len(e_center_values) == len(candidates), str(sorted(e_center_values)))
    for rho, out in outputs.items():
        check(
            f"rho_E={rho} preserves q_T=5/6",
            out["T_center_T"] / out["T_shell_T"] == Fraction(5, 6),
            str(out["T_center_T"] / out["T_shell_T"]),
        )

    print("\n=== Inverse-square center-lift sieve ===")
    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    target_ratio = Fraction(9, 4)
    ratio_base = w_e / w_t
    hits = []
    for exponent in range(-8, 9):
        ratio = pow_fraction(ratio_base, exponent)
        if ratio == target_ratio:
            hits.append(exponent)
    check("unique small-integer monomial exponent hits q_E/q_T=9/4", hits == [-2], str(hits))
    c_norm = q_t * w_t * w_t
    q_e_from_inv_sq = c_norm / (w_e * w_e)
    rho_e_from_inv_sq = 6 * (q_e_from_inv_sq - 1)
    c_te_from_inv_sq = mu * q_t / q_e_from_inv_sq
    check("inverse-square normalization C=q_T*w_T^2 is 5/24", c_norm == Fraction(5, 24), str(c_norm))
    check("inverse-square law gives q_E=15/8", q_e_from_inv_sq == Fraction(15, 8), str(q_e_from_inv_sq))
    check("inverse-square law gives rho_E=21/4", rho_e_from_inv_sq == Fraction(21, 4), str(rho_e_from_inv_sq))
    check("inverse-square law gives c_TE=-8/9", c_te_from_inv_sq == Fraction(-8, 9), str(c_te_from_inv_sq))

    scaling_ratios = {
        "constant": Fraction(1),
        "linear_weight": w_e / w_t,
        "inverse_weight": w_t / w_e,
        "quadratic_weight": (w_e / w_t) ** 2,
        "inverse_square_weight": (w_t / w_e) ** 2,
    }
    for name, ratio in scaling_ratios.items():
        expected = target_ratio if name == "inverse_square_weight" else None
        if expected is None:
            check(f"{name} scaling does not hit target", ratio != target_ratio, str(ratio))
        else:
            check(f"{name} scaling hits target", ratio == target_ratio, str(ratio))

    print("\n=== Boundary classification ===")
    check("actual status is not a retained/proposed-retained claim", "proposed_retained" not in read_rel(note_path))
    check("note leaves future nonlinear positive route open", "future genuinely nonlinear tensor observable could still" in read_rel(note_path))
    check("note names direct consumer gate", "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md" in read_rel(note_path))
    check("note forbids observed/fitted values as proof inputs", "observed quark masses, CKM/J fits" in read_rel(note_path))
    check("note identifies exact next positive law", "derive q_X w_X^2 = 5/24" in read_rel(note_path))

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    print(
        "VERDICT: current named nonlinear/log/determinant/tensor routes do not derive "
        "the E-center primitive; inverse-square center-lift remains the sharp target."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
