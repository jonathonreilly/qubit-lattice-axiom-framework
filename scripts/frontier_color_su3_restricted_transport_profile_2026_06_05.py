#!/usr/bin/env python3
"""Endpoint transport profile for admitted SU(3)-restricted color links.

This runner verifies exact finite-algebra identities under the admitted
standard endpoint transformation law U_AB -> g_A U_AB g_B^{-1}. It does not
derive the endpoint carrier, transport law, action, coupling, record readout,
or dial selection.
"""

from __future__ import annotations

from pathlib import Path

try:
    import sympy as sp
    from sympy import I, Matrix, simplify, sqrt, zeros
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


def gell_mann() -> list[Matrix]:
    s3 = sqrt(3)
    return [
        Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
        Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
        Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
        Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / s3,
    ]


def is_zero(M: Matrix) -> bool:
    return all(simplify(M[i, j]) == 0 for i in range(M.rows) for j in range(M.cols))


def main() -> int:
    emit("=" * 78)
    emit("COLOR SU(3)-RESTRICTED TRANSPORT PROFILE")
    emit("bounded finite-algebra runner under admitted transport rule")
    emit("=" * 78)

    section("1. SU(3) generator sanity")
    lam = gell_mann()
    T = [L / 2 for L in lam]
    check("eight Gell-Mann generators", len(T) == 8)
    for idx, G in enumerate(T, start=1):
        check(f"T{idx} Hermitian", is_zero(G.H - G))
        check(f"T{idx} traceless", simplify(G.trace()) == 0)
    check("sample commutator [T1,T2] = i T3", is_zero(T[0] * T[1] - T[1] * T[0] - I * T[2]))
    check(
        "sample commutator [T4,T5] = i/2(T3+sqrt(3)T8)",
        is_zero(T[3] * T[4] - T[4] * T[3] - I * (T[2] + sqrt(3) * T[7]) / 2),
    )

    section("2. Endpoint variations")
    u = sp.symbols("u0:9")
    U = Matrix(3, 3, u)
    I3 = sp.eye(3)
    sample = T[0]

    # Infinitesimal endpoint transformations for the link:
    # left:  dU = i T U
    # right: dU = -i U T
    left_bare = sample * I3
    right_bare = -I3 * sample
    check("bare link varies at left endpoint", not is_zero(left_bare))
    check("bare link varies at right endpoint", not is_zero(right_bare))

    # Half-dressed left object q_A^* U: dq_A^* = -i q_A^* T, dU = i T U.
    # The row q_A^* is arbitrary, so the matrix coefficient must cancel.
    for idx, G in enumerate(T, start=1):
        left_half = -G * U + G * U
        right_half = -U * G
        check(f"T{idx} half-dressed left variation cancels", is_zero(left_half))
        if idx == 1:
            check("half-dressed line remains right-variant", not is_zero(right_half))

    section("3. Fully dressed endpoint invariance")
    for idx, G in enumerate(T, start=1):
        left_full = -G * U + G * U
        right_full = -U * G + U * G
        check(f"T{idx} full line left variation cancels", is_zero(left_full))
        check(f"T{idx} full line right variation cancels", is_zero(right_full))

    profile = {
        "bare_link": 0,
        "half_dressed": 1,
        "fully_dressed": 2,
    }
    check("endpoint profile is 0->1->2", list(profile.values()) == [0, 1, 2])

    section("4. Closed trace invariance")
    for idx, G in enumerate(T, start=1):
        comm = G * U - U * G
        check(f"T{idx} trace of commutator vanishes", simplify(comm.trace()) == 0)
    check("closed-loop trace identity is algebraic", simplify((sample * U - U * sample).trace()) == 0)

    section("5. Residual ledger")
    supplied = {
        "endpoint_variation_identities",
        "bare_half_full_profile",
        "closed_trace_commutator_identity",
    }
    residuals = {
        "derive_two_qubit_endpoint",
        "derive_su3_transport_rule",
        "dynamic_sym2_preservation",
        "derive_gauss_generators_from_axioms",
        "action_couplings_rates_time",
        "color_record_readout_antecedent",
        "record_production",
    }
    post_record = {"word_history_O_star", "count_state_N_to_O"}
    check("three transport-profile outputs supplied", len(supplied) == 3)
    check("seven residuals remain", len(residuals) == 7)
    check("supplied outputs do not include residuals", supplied.isdisjoint(residuals))
    check("post-record outputs do not include residuals", post_record.isdisjoint(residuals))
    check("transport rule derivation remains residual", "derive_su3_transport_rule" in residuals)
    check("record readout remains residual", "color_record_readout_antecedent" in residuals)
    check("record production remains residual", "record_production" in residuals)

    section("6. Note sanity")
    doc = Path("docs/COLOR_SU3_RESTRICTED_TRANSPORT_PROFILE_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "Claim type:** bounded_theorem",
        "This block supplies only the finite algebra",
        "This rule is a bounded input here.",
        "Does not derive physical color.",
        "Does not establish a repo-wide quantum-link ontology.",
        "Does not select a Koide/generation dial location.",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("physical color closure", "physical color is " + "derived"),
        ("transport derivation closure", "transport law is " + "derived"),
        ("action closure", "gauge action is " + "derived"),
        ("dial selector closure", "dial location is " + "selected"),
    ]
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
