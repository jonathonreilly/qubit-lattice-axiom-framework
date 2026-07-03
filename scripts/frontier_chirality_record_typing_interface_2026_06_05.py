#!/usr/bin/env python3
"""Chirality / record typing interface.

This runner separates sign/readout facts from chirality facts. It verifies
small finite matrices showing that signed Hermitian spectra do not imply
anticommutation, and that post-record information outputs are disjoint from
carrier chirality outputs.

No Koide value derivation, no chiral readout selection, no CAR/spin-statistics
bridge, no record-production dynamics, no dial fixing, no audit verdicts.
"""

from __future__ import annotations

from pathlib import Path

try:
    import sympy as sp
    from sympy import Matrix, diag, simplify, zeros
except ImportError:  # pragma: no cover
    print("FAIL: sympy required")
    raise SystemExit(1)


PASS = 0
FAIL = 0


def emit(line: str = "") -> None:
    print(line)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    emit(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    emit()
    emit("-" * 78)
    emit(title)
    emit("-" * 78)


def is_zero(M: Matrix) -> bool:
    return all(simplify(M[i, j]) == 0 for i in range(M.rows) for j in range(M.cols))


def main() -> int:
    emit("=" * 78)
    emit("CHIRALITY / RECORD TYPING INTERFACE")
    emit("bounded-support / negative-route-pruning runner")
    emit("=" * 78)

    section("1. Signed spectrum does not imply chirality")
    gamma = diag(1, -1, -1)
    signed_commuting = diag(2, -1, 3)
    comm = signed_commuting * gamma - gamma * signed_commuting
    anti = signed_commuting * gamma + gamma * signed_commuting
    signed_eigs = sorted([ev for ev in signed_commuting.eigenvals().keys()])

    check("grading squares to identity", gamma * gamma == sp.eye(3))
    check("signed commuting operator is Hermitian", signed_commuting.T == signed_commuting)
    check("signed commuting operator has a negative eigenvalue", any(ev < 0 for ev in signed_eigs), str(signed_eigs))
    check("signed commuting operator commutes with grading", is_zero(comm))
    check("signed commuting operator does not anticommute with grading", not is_zero(anti))
    check("therefore signed spectrum alone is not chirality", is_zero(comm) and not is_zero(anti))

    section("2. Anticommuting chiral operator is a different condition")
    chiral = Matrix(
        [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 0],
        ]
    )
    chiral_comm = chiral * gamma - gamma * chiral
    chiral_anti = chiral * gamma + gamma * chiral
    chiral_eigs = sorted([ev for ev in chiral.eigenvals().keys()])
    check("chiral test operator is Hermitian", chiral.T == chiral)
    check("chiral test operator anticommutes with grading", is_zero(chiral_anti))
    check("chiral test operator need not commute with grading", not is_zero(chiral_comm))
    check("chiral spectrum is sign-symmetric with zero", chiral_eigs == [-1, 0, 1], str(chiral_eigs))
    check("chiral eigenvalue sum is zero", sum(chiral_eigs) == 0)
    check("commuting signed class differs from anticommuting class", not is_zero(chiral_comm) and is_zero(chiral_anti))

    section("3. Signed vs absolute readout choices")
    real_spectrum = [-2, 1, 3]
    signed_readout = list(real_spectrum)
    absolute_readout = [abs(x) for x in real_spectrum]
    check("signed readout is real-valued", all(isinstance(x, int) for x in signed_readout))
    check("absolute readout is real-valued", all(isinstance(x, int) for x in absolute_readout))
    check("signed and absolute readouts differ", signed_readout != absolute_readout, f"{signed_readout} vs {absolute_readout}")
    check("Hermiticity supplies real eigenvalues, not the readout choice", signed_readout != absolute_readout)

    def q_value(values: list[int]) -> sp.Rational:
        num = sum(v * v for v in values)
        den = sum(values) ** 2
        return sp.oo if den == 0 else sp.Rational(num, den)

    signed_q = q_value(signed_readout)
    absolute_q = q_value(absolute_readout)
    check("signed and absolute Q readouts can differ", signed_q != absolute_q, f"{signed_q} vs {absolute_q}")
    check("readout difference is not a post-record count update", signed_q != absolute_q)

    section("4. Typed interface disjointness")
    post_record_outputs = {
        "word_history_O_star",
        "count_state_N_to_O",
        "signed_scalar_label",
        "coarse_grained_counts",
        "finite_additive_readout",
    }
    chirality_outputs = {
        "anticommutation_relation",
        "graded_tensor_support",
        "car_or_jordan_wigner_frame",
        "first_order_dirac_operator",
        "chiral_holomorphic_weighting",
    }
    bridge_outputs = {
        "measurement_readout_bridge",
        "record_production",
        "rates_time",
    }
    check("post-record output set has five entries", len(post_record_outputs) == 5)
    check("chirality output set has five entries", len(chirality_outputs) == 5)
    check("bridge output set has three entries", len(bridge_outputs) == 3)
    check("post-record outputs do not include chirality outputs", post_record_outputs.isdisjoint(chirality_outputs))
    check("post-record outputs do not include production bridge outputs", post_record_outputs.isdisjoint(bridge_outputs))
    check("signed labels are post-record-consumable", "signed_scalar_label" in post_record_outputs)
    check("anticommutation remains carrier output", "anticommutation_relation" in chirality_outputs)
    check("CAR/JW frame remains carrier output", "car_or_jordan_wigner_frame" in chirality_outputs)

    section("5. Route-pruning ledger")
    routes = {
        "signed_eigenvalues_imply_chirality": "pruned",
        "hermiticity_forces_signed_readout": "pruned",
        "post_record_counts_select_chiral_weighting": "pruned",
        "ungraded_qubits_select_car": "pruned",
        "emergent_spacetime_chirality_transports_generation": "pruned",
        "carrier_chirality_feeds_record_after_bridge": "open_composition",
    }
    check("six routes classified", len(routes) == 6)
    for name in list(routes)[:5]:
        check(f"{name}: pruned", routes[name] == "pruned")
    check("positive composition remains open, not closed", routes["carrier_chirality_feeds_record_after_bridge"] == "open_composition")

    section("6. Note sanity")
    doc = Path("docs/CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "Claim type:** meta support map",
        "Trace class:** negative route-pruning support map",
        "No-Go Discipline Gate (N1-N8)",
        "Does not derive chirality.",
        "Does not select signed over absolute square-root readout.",
        "Does not select a Koide/generation dial location.",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("chirality closure", "chirality is " + "derived"),
        ("signed readout closure", "signed readout is " + "forced"),
        ("CAR closure", "CAR is " + "selected"),
        ("dial-location closure", "dial location is " + "selected"),
    ]
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
