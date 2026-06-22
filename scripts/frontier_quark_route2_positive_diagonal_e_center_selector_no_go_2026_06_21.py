#!/usr/bin/env python3
"""Route-2 positive-diagonal E-center selector no-go.

This is a first-principles stretch attempt on an E-center-sensitive route:
apply the positive-diagonal / Record-additive readout classifier to the
normalized Route-2 E endpoint pair (1, q_E). The classifier sees q_E, but it
does not select q_E=15/8 without an extra selector equation.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(ok)
    FAIL += int(not ok)
    return ok


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def q_from_rho(rho: Fraction) -> Fraction:
    return Fraction(1, 1) + rho / 6


def rho_from_q(q: Fraction) -> Fraction:
    return 6 * (q - 1)


def w_sum(entries: tuple[Fraction, ...], which: str) -> Fraction:
    if which == "identity":
        return sum(entries, Fraction(0))
    if which == "square":
        return sum(x * x for x in entries)
    if which == "affine":
        return sum(2 * x + 3 for x in entries)
    raise ValueError(which)


def det(entries: tuple[Fraction, ...]) -> Fraction:
    out = Fraction(1)
    for entry in entries:
        out *= entry
    return out


def positive_rhos(max_num: int = 36, max_den: int = 18) -> set[Fraction]:
    vals: set[Fraction] = set()
    for den in range(1, max_den + 1):
        for num in range(-6 * den + 1, max_num + 1):
            rho = Fraction(num, den)
            if q_from_rho(rho) > 0:
                vals.add(rho)
    return vals


def main() -> int:
    print("ROUTE-2 POSITIVE-DIAGONAL E-CENTER SELECTOR NO-GO")
    print("=" * 78)

    paths = {
        "new_note": DOCS / "QUARK_ROUTE2_POSITIVE_DIAGONAL_E_CENTER_SELECTOR_NO_GO_NOTE_2026-06-21.md",
        "readout": DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        "positivity": DOCS / "ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md",
        "classifier": DOCS / "OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md",
        "axioms": DOCS / "MINIMAL_AXIOMS_2026-06-05.md",
        "primitive_chain": DOCS / "S3_TIME_PRIMITIVE_CHAIN_NOTE.md",
        "theta_slice": DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
    }

    print()
    print("A. Source surfaces")
    print("-" * 78)
    for label, path in paths.items():
        check(f"{label} exists", path.exists(), str(path.relative_to(ROOT)))

    note = read(paths["new_note"])
    readout = read(paths["readout"])
    positivity = read(paths["positivity"])
    classifier = read(paths["classifier"])
    axioms = read(paths["axioms"])
    primitive_chain = read(paths["primitive_chain"])
    theta_slice = read(paths["theta_slice"])

    check(
        "readout authority supplies E-row endpoint algebra",
        "q_E" in readout
        and "gamma_E(center)" in readout
        and "beta_E / alpha_E = 21/4" in readout,
    )
    check(
        "positivity note says rho_E remains direction data",
        "readout's **direction**" in positivity
        and "left free" in positivity
        and "one-sided bound" in positivity
        and "rho_E > -6" in positivity,
    )
    check(
        "positive-diagonal classifier supplies one-site and determinant/log forms",
        "one-site function" in classifier
        and "determinant-only" in classifier
        and "c log" in classifier,
    )
    check(
        "Record axiom does not supply readout context or weighting",
        "record supplies no readout context" in axioms
        and "weighting, normalization, probability" in axioms,
    )
    check(
        "S3 primitive-chain and theta-slice consumers remain open gates",
        "beta_E / alpha_E = 21/4" in primitive_chain
        and "open primitive" in primitive_chain
        and "unique exact `Theta_R -> Lambda_R` coupling theorem" in theta_slice,
    )

    print()
    print("B. Exact E-row endpoint algebra")
    print("-" * 78)
    target_rho = Fraction(21, 4)
    target_q = Fraction(15, 8)
    check("rho_E=21/4 maps to q_E=15/8", q_from_rho(target_rho) == target_q, str(q_from_rho(target_rho)))
    check("q_E=15/8 maps back to rho_E=21/4", rho_from_q(target_q) == target_rho, str(rho_from_q(target_q)))
    check("positivity domain is rho_E > -6", q_from_rho(Fraction(-6)) == 0 and q_from_rho(Fraction(-599, 100)) > 0)

    witnesses = {
        "no_lift": Fraction(0),
        "same_as_T": Fraction(-1),
        "unit_lift": Fraction(1),
        "target": target_rho,
        "integer_four": Fraction(4),
    }
    for name, rho in witnesses.items():
        q = q_from_rho(rho)
        check(f"{name} witness is positive and exact", q > 0, f"rho={rho}, q={q}")

    print()
    print("C. Positive-diagonal additive readouts see q_E but do not select it")
    print("-" * 78)
    left = (Fraction(1), target_q)
    right = (Fraction(1), Fraction(5, 6))
    concat = left + right
    for which in ("identity", "square", "affine"):
        check(
            f"{which} one-site readout is direct-sum additive",
            w_sum(concat, which) == w_sum(left, which) + w_sum(right, which),
            f"W(left+right)={w_sum(concat, which)}",
        )

    check("determinant of normalized E pair is q_E", det((Fraction(1), target_q)) == target_q, str(det((Fraction(1), target_q))))
    check("determinant quotient distinguishes target from no-lift", det((1, target_q)) != det((1, Fraction(1))))
    check("determinant quotient distinguishes target from same-as-T", det((1, target_q)) != det((1, Fraction(5, 6))))
    check(
        "distinguishing q_E is not selecting q_E",
        "They still do not select a value of" in note
        and "do not supply the missing E-center selector" in note,
    )

    print()
    print("D. Continuum of admissible positive E rows")
    print("-" * 78)
    rhos = positive_rhos()
    qs = {q_from_rho(rho) for rho in rhos}
    check("bounded rational scan has many positive rho_E values", len(rhos) > 300, f"count={len(rhos)}")
    check("bounded rational scan includes target rho_E", target_rho in rhos)
    check("bounded rational scan includes non-target positive witnesses", all(w in rhos for w in (Fraction(0), Fraction(-1), Fraction(1), Fraction(4))))
    check("positive q_E values are likewise non-unique", len(qs) == len(rhos), f"q-count={len(qs)}")
    check(
        "target is one classifier-admissible member, not a forced value",
        q_from_rho(target_rho) in qs
        and q_from_rho(Fraction(0)) in qs
        and q_from_rho(Fraction(-1)) in qs,
    )

    print()
    print("E. Firewalls")
    print("-" * 78)
    check(
        "new note states the route pruned",
        "This prunes the route" in note
        and "positive-diagonal / Record-additive classifier alone is not that selector" in note,
    )
    check(
        "new note preserves future fixed-carrier primitives",
        "does not rule out those future routes" in note
        and "fixed-carrier E-center primitives" in note,
    )
    check(
        "new note denies endpoint closure",
        "No derivation of `rho_E = 21/4`" in note
        and "No derivation of `q_E = 15/8`" in note
        and "No derivation of the endpoint triple" in note,
    )
    check(
        "new note denies audit or status changes",
        "No audit verdict or ledger/status change" in note,
    )
    check(
        "new note has no forbidden retained-status wording",
        not any(
            bad in note
            for bad in (
                "retained " "branch-local",
                "would " "become retained",
                "promoted " "to retained",
                "retained on " "the actual surface",
                "endpoint triple " "derived",
                "unique exact Theta_R -> Lambda_R theorem " "is closed",
            )
        ),
    )

    print()
    print("Summary")
    print("-" * 78)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: positive-diagonal E-center readouts see q_E but do not select q_E=15/8.")
        return 0
    print("VERDICT: positive-diagonal selector checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
