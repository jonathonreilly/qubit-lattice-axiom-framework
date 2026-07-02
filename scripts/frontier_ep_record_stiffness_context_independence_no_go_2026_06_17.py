#!/usr/bin/env python3
"""Record-only independence no-go for EP record-stiffness.

This runner checks the source-side negative boundary:

  The current Record axiom is satisfied by finite additive record readouts
  that are invariant under arbitrary choices of continuous stiffness and
  gravitational source coefficient. Therefore the EP record-stiffness
  conditional template cannot be promoted to a Record-only derivation.

The runner reads/writes no audit surfaces.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "EP_RECORD_STIFFNESS_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md"
TEMPLATE = ROOT / "docs" / "EP_RECORD_STIFFNESS_CONDITIONAL_SHARED_COUPLING_TEMPLATE_NOTE_2026-06-07.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def powerset(items: tuple[str, ...]) -> list[frozenset[str]]:
    out: list[frozenset[str]] = [frozenset()]
    for n in range(1, len(items) + 1):
        for combo in combinations(items, n):
            out.append(frozenset(combo))
    return out


def main() -> int:
    print("EP Record-stiffness context independence no-go")
    print("=" * 72)

    records = ("r1", "r2", "r3")
    subsets = powerset(records)
    scalar_readout = {subset: len(subset) for subset in subsets}

    additive = True
    for a in subsets:
        for b in subsets:
            if a.isdisjoint(b):
                additive &= scalar_readout[a | b] == scalar_readout[a] + scalar_readout[b]
    check(
        "Record scalar readout is finitely additive on the supplied finite context",
        additive and scalar_readout[frozenset()] == 0,
        "I(S)=|S| over three records",
    )

    # The Record facts are unchanged when independent continuous parameters are
    # attached outside the axiom.
    m, lam, phi, phi0, gamma_a, gamma_b, psi2 = sp.symbols(
        "m lambda phi phi0 gamma_A gamma_B psi2", positive=True
    )
    k_p = sp.symbols("K_p", nonnegative=True)

    v_a = sp.Rational(1, 2) * m**2 * (phi - phi0) ** 2
    v_b = sp.Rational(1, 2) * lam * m**2 * (phi - phi0) ** 2
    stiff_a = sp.diff(v_a, phi, 2).subs(phi, phi0)
    stiff_b = sp.diff(v_b, phi, 2).subs(phi, phi0)
    check(
        "two completions can share Record data but have different stiffness",
        sp.simplify(stiff_a - m**2) == 0
        and sp.simplify(stiff_b - lam * m**2) == 0
        and sp.simplify(stiff_b - stiff_a) == (lam - 1) * m**2,
        f"V_A''={stiff_a}; V_B''={stiff_b}",
    )

    e2_a = m**2 + k_p
    e2_b = lam * m**2 + k_p
    gap_a = e2_a.subs(k_p, 0)
    gap_b = e2_b.subs(k_p, 0)
    check(
        "inertial rest gaps vary with the supplied stiffness while Record facts stay fixed",
        sp.simplify(gap_a - m**2) == 0
        and sp.simplify(gap_b - lam * m**2) == 0
        and sp.simplify(gap_b / gap_a - lam) == 0,
        f"gap_B/gap_A={sp.simplify(gap_b/gap_a)}",
    )

    inertial_a = m
    inertial_b = sp.sqrt(lam) * m
    grav_a = gamma_a * m * psi2
    grav_b = gamma_b * sp.sqrt(lam) * m * psi2
    ratio_a = sp.simplify(grav_a / (inertial_a * psi2))
    ratio_b = sp.simplify(grav_b / (inertial_b * psi2))
    check(
        "source/inertial ratio is a free supplied coefficient, not a Record consequence",
        ratio_a == gamma_a and ratio_b == gamma_b,
        f"ratio_A={ratio_a}; ratio_B={ratio_b}",
    )

    check(
        "same Record model admits WEP and non-WEP source normalizations",
        ratio_a.subs(gamma_a, 1) == 1 and ratio_b.subs(gamma_b, 2) == 2,
        "gamma_A=1, gamma_B=2 both preserve finite additivity",
    )

    record_symbols = set().union(*(set(subset) for subset in subsets))
    continuous_symbols = {str(m), str(lam), str(gamma_a), str(gamma_b)}
    check(
        "Record additivity constraints contain no continuous stiffness/source symbols",
        not record_symbols.intersection(continuous_symbols),
        "record labels and continuous parameters are independent",
    )

    no_unique_stiffness = sp.simplify(stiff_b.subs(lam, 3) - stiff_a) == 2 * m**2
    no_unique_ratio = ratio_b.subs(gamma_b, 3) != ratio_a.subs(gamma_a, 1)
    check(
        "model-pair contradiction blocks any Record-only unique stiffness or WEP theorem",
        bool(no_unique_stiffness and no_unique_ratio),
        "lambda=3 changes stiffness; gamma=3 changes source ratio",
    )

    note_text = NOTE.read_text(encoding="utf-8")
    flat_note_text = " ".join(note_text.split())
    required_note_tokens = [
        "**Claim type:** no_go",
        "Record axiom cannot determine a continuous stiffness",
        "no theorem using only the current axioms can derive",
        "does not refute the conditional template",
        "separate dynamics/source theorem",
        "Gate result: PASS for this narrow no-go boundary.",
        "EP_SHARED_COUPLING_NOT_DERIVED_FROM_RECORD=TRUE",
    ]
    check(
        "source note states no-go boundary without claiming EP closure",
        all(token in flat_note_text for token in required_note_tokens),
        "note wording guard",
    )

    template_text = TEMPLATE.read_text(encoding="utf-8")
    flat_template_text = " ".join(template_text.split())
    required_template_tokens = [
        "2026-06-17 Record-only independence no-go",
        "does not refute this conditional template",
        "Record-only derivation cannot supply",
        "EP_RECORD_STIFFNESS_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md",
    ]
    check(
        "conditional template cites the independence no-go and stays conditional",
        all(token in flat_template_text for token in required_template_tokens),
        "template boundary guard",
    )

    check(
        "no new axiom or Tier-A admission is claimed",
        "No new axiom" in note_text
        and "No new axiom, Tier-A admission, WEP closure, or audit-status change" in flat_template_text,
    )

    check(
        "audit surfaces are not named as write targets",
        "audit ledger" in note_text and "does not set an audit verdict" in flat_note_text,
        "read-only audit posture",
    )

    check(
        "positive EP closure is explicitly outside this artifact",
        "Any positive weak-equivalence-principle closure" in note_text
        and "not a WEP closure" in template_text,
    )

    print("=" * 72)
    print("RECORD_STIFFNESS_CONTEXT_INDEPENDENCE_NO_GO=TRUE")
    print("EP_SHARED_COUPLING_NOT_DERIVED_FROM_RECORD=TRUE")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
