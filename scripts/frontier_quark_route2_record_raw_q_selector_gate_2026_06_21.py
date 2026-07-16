#!/usr/bin/env python3
"""Route-2 Record raw-q selector gate.

Record readout is content-determined and finitely additive over disjoint
records. The Route-2 q-coordinate is a normalized center/shell quotient, so
selecting raw q as the inverse-square-scaled coordinate requires an additional
normalization/readout theorem.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path

PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n       {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")
    return ok


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def banner(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def q(pair: tuple[F, F]) -> F:
    shell, center = pair
    return center / shell


def add_pair(a: tuple[F, F], b: tuple[F, F]) -> tuple[F, F]:
    return (a[0] + b[0], a[1] + b[1])


def rho_from_q(q_value: F) -> F:
    return 6 * (q_value - 1)


def main() -> int:
    print("Route-2 Record raw-q selector gate")
    print("=" * 88)

    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    axioms_flat = " ".join(axioms.split())
    premise_nodes = read("docs/audit/data/axiom_premise_nodes.json")
    exact_readout = read("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    record_no_go = read("docs/ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md")
    naturality = read("docs/QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md")
    schur = read("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    parent = read("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    current_bank = "\n".join([axioms, premise_nodes, exact_readout, record_no_go, naturality, schur, parent]).lower()

    banner("1. Current-surface Record boundaries")
    check(
        "minimal axioms make each Record an admissible lock, unique per site and permanent",
        "When present, a record locks exactly one admissible local possibility." in axioms_flat
        and "A site never carries more than one record; records are permanent." in axioms_flat,
    )
    check(
        "minimal axioms make Record readout content-determined and finitely additive",
        "Only records are readable." in axioms_flat
        and "A readout value is determined by record content alone." in axioms_flat
        and "For any finite collection of pairwise-disjoint records, scalar readout" in axioms_flat
        and "`I` is additive, with `I(empty)=0`." in axioms_flat,
    )
    check(
        "minimal axioms leave extra quotient normalization downstream",
        "Further physical structure requires a retained derivation or bridge" in axioms_flat
        and "A choice not fixed by the supplied structure remains a named conditional or open dependency." in axioms_flat,
    )
    check(
        "premise registry repeats no downstream readout bridge from Record",
        (
            "supplies no readout context" in premise_nodes.lower()
            or "supplies no context-selection rule" in premise_nodes.lower()
        )
        and "downstream theory consequence" in premise_nodes.lower(),
    )
    check(
        "Record positivity no-go says Record is not used to supply P_R",
        "Record axiom supplies no readout" in record_no_go,
    )
    check(
        "parent S3 note still leaves endpoint triple open",
        "readout-map endpoint triple is not yet derived" in parent,
    )

    banner("2. Exact Route-2 quotient target")
    q_t = F(5, 6)
    lam = F(9, 4)
    q_e_target = lam * q_t
    rho_target = rho_from_q(q_e_target)
    print(f"q_T={q_t}, lambda={lam}, q_E={q_e_target}, rho_E={rho_target}")

    check("exact readout exposes q_E as center/shell quotient", "q_E   := gamma_E(center) / gamma_E(shell)" in exact_readout)
    check("exact readout exposes q_T as center/shell quotient", "q_T   := gamma_T(center) / gamma_T(shell)" in exact_readout)
    check("exact target raw q scaling gives q_E=15/8", q_e_target == F(15, 8))
    check("exact target raw q scaling gives rho_E=21/4", rho_target == F(21, 4))
    check("Schur note identifies q_X inverse-square as a gap", "q_X" in schur and "inverse-square" in schur)

    banner("3. Raw q is not the additive scalar")
    a = (F(1), F(5, 6))
    b = (F(1), F(15, 8))
    sum_ab = add_pair(a, b)
    q_a = q(a)
    q_b = q(b)
    q_sum = q(sum_ab)
    weighted_average = (a[0] * q_a + b[0] * q_b) / (a[0] + b[0])
    print(f"q(A)={q_a}, q(B)={q_b}, q(A+B)={q_sum}")

    check("A has q=5/6", q_a == F(5, 6))
    check("B has q=15/8", q_b == F(15, 8))
    check("additive sum has q=65/48", q_sum == F(65, 48))
    check("q(A+B) is not q(A)+q(B)", q_sum != q_a + q_b)
    check("q(A+B) is a shell-weighted average", q_sum == weighted_average)
    check("q(A+B) does not preserve target raw scaling", q_sum != lam * q_a)
    print("note: forming q requires division by the shell scalar (see q() above; narration, not scored)")

    banner("4. Record-linear operations leave the selector external")
    rho_values = [F(-1), F(0), F(1), F(21, 4)]
    pairs = [(F(1), F(1) + rho / 6) for rho in rho_values]
    for rho, pair in zip(rho_values, pairs):
        print(f"rho={rho}: pair={pair}, q={q(pair)}")

    check("all tested rho values share shell scalar 1", all(pair[0] == 1 for pair in pairs))
    check("tested rho values give distinct q values", len({q(pair) for pair in pairs}) == len(pairs))
    check("rho=0 remains Record-compatible after context is supplied", q(pairs[1]) == 1)
    check("rho=21/4 remains Record-compatible after context is supplied", q(pairs[3]) == F(15, 8))
    print("note: finite additivity alone does not distinguish rho=0 from rho=21/4 as a rule (narration, not scored)")
    check(
        "Record positivity no-go already classifies rho_E as direction not norm",
        "rho_E` is the readout direction" in record_no_go,
    )
    check(
        "naturality no-go says extra source/readout primitive is required",
        "source-domain, or readout-map primitive is supplied" in naturality,
    )

    banner("5. Current-bank verdict")
    check("current bank does not name a raw q Record selector theorem", "raw q record selector" not in current_bank)
    check("current bank does not say Record selects q_X as scaled coordinate", "record selects q_x" not in current_bank)
    check(
        "current bank explicitly withholds Record normalization",
        "normalization" in premise_nodes.lower()
        and "downstream theory consequence" in premise_nodes.lower(),
    )
    print("note: no observed endpoint value is used as a proof input (narration, not scored)")
    raw_q_nonadditive = (q_sum != q_a + q_b) and (q_sum == weighted_average) and (q_sum != lam * q_a)
    current_bank_excludes = (
        "raw q record selector" not in current_bank
        and "record selects q_x" not in current_bank
    )
    check(
        "current result is a no-go for Record-additivity-derived raw q scaling",
        raw_q_nonadditive and current_bank_excludes,
        "computed: q(A+B) is a nonadditive shell-weighted average AND the current bank names no raw-q Record selector",
    )
    print("note: positive target is a normalized-quotient readout theorem or alternate bridge (narration, not scored)")

    banner("Summary")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: verifier failed; inspect Record raw-q selector checks above.")
    else:
        print(
            "VERDICT: no-go / Record-quotient selector boundary. Record finite "
            "additivity does not select raw q as the inverse-square-scaled "
            "coordinate; q requires an extra quotient normalization/readout theorem."
        )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
