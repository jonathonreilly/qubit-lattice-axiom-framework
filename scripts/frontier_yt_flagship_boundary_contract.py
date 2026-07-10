#!/usr/bin/env python3
"""YT flagship boundary contract verifier.

This runner is a source-side audit unlock for
``docs/YT_FLAGSHIP_BOUNDARY_NOTE.md``.  It verifies the note's current
authority contract:

* the note is a supporting boundary note, not sole lane authority;
* the current central values and residual budgets agree with the YT authority
  notes on ``origin/main``;
* the positive statements stay scoped to derived central values and exact
  lattice-scale support;
* the note explicitly forbids fully-retained UV-to-IR closure, a native
  continuum-limit theorem, and a direct-lattice low-energy bypass claim;
* the zero-import authority conditions its low-energy package on the underived
  ``kappa_Y = 0`` selector (conditional connected-trace specialization).

It deliberately does not certify effective retained status.  Independent
audit owns that decision.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "YT_FLAGSHIP_BOUNDARY_NOTE.md"
ZERO_IMPORT = DOCS / "YT_ZERO_IMPORT_AUTHORITY_NOTE.md"
WARD = DOCS / "YT_WARD_IDENTITY_DERIVATION_THEOREM.md"
COLOR = DOCS / "YT_COLOR_PROJECTION_CORRECTION_NOTE.md"
BUDGET = DOCS / "YT_EXPLICIT_SYSTEMATIC_BUDGET_NOTE.md"
BOUNDARY = DOCS / "YT_BOUNDARY_THEOREM.md"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def norm(text: str) -> str:
    return " ".join(text.replace("\xa0", " ").split())


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def decimal_after(label: str, text: str) -> float | None:
    escaped = re.escape(label)
    m = re.search(escaped + r"\s*=\s*`?([0-9]+(?:\.[0-9]+)?)", text)
    return float(m.group(1)) if m else None


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    next_heading = re.search(r"\n##\s+", text[start + len(heading):])
    if next_heading:
        return text[start:start + len(heading) + next_heading.start()]
    return text[start:]


def main() -> int:
    print("=" * 78)
    print("YT FLAGSHIP BOUNDARY CONTRACT VERIFIER")
    print("=" * 78)

    paths = [NOTE, ZERO_IMPORT, WARD, COLOR, BUDGET, BOUNDARY]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())
    if any(not path.exists() for path in paths):
        return 1

    note = read(NOTE)
    note_n = norm(note)
    zero = read(ZERO_IMPORT)
    zero_n = norm(zero)
    budget = read(BUDGET)
    budget_n = norm(budget)
    boundary = read(BOUNDARY)
    boundary_n = norm(boundary)

    print("\nPart 1: graph and authority registration")
    check(
        "flagship note registers this primary runner",
        "scripts/frontier_yt_flagship_boundary_contract.py" in note,
    )
    check(
        "flagship note declares supporting-boundary role",
        "supporting boundary note" in note and "not the sole lane authority" in note,
    )
    for target in [
        "YT_ZERO_IMPORT_AUTHORITY_NOTE.md",
        "YT_WARD_IDENTITY_DERIVATION_THEOREM.md",
        "YT_COLOR_PROJECTION_CORRECTION_NOTE.md",
        "YT_EXPLICIT_SYSTEMATIC_BUDGET_NOTE.md",
    ]:
        check(f"flagship note links authority surface {target}", target in note)

    print("\nPart 2: current quantitative surface")
    yt = decimal_after("y_t(v)", note)
    mt3 = decimal_after("m_t(pole)", note)
    check("flagship y_t(v) central value is 0.9176", yt == 0.9176, str(yt))
    check("flagship 3-loop pole-mass central value is 173.10 GeV", mt3 == 173.10, str(mt3))
    check("flagship note carries retained 2-loop support value 172.57 GeV", "172.57 GeV" in note)
    check("zero-import authority agrees on y_t(v)=0.9176", "`0.9176`" in zero)
    check("zero-import authority agrees on 172.57/173.10 GeV mass pair", "172.57 GeV" in zero and "173.10 GeV" in zero)
    check("flagship note states standard-method residual budget about 1.95%", "~1.95%" in note)
    check("zero-import authority carries same standard-method residual budget", "~1.95%" in zero)

    print("\nPart 3: exact/support ingredients are present")
    exact_section = section(note, "## What is exact")
    check(
        "exact section contains Ward ratio identity",
        "y_t(M_Pl) / g_s(M_Pl) = 1 / sqrt(6)" in exact_section,
    )
    check(
        "exact section contains same-surface alpha_s/g_s input",
        "alpha_s" in exact_section and "g_s(M_Pl)" in exact_section and "plaquette chain" in exact_section,
    )
    check("exact section contains color projection sqrt(8/9)", "sqrt(8/9)" in exact_section)
    check(
        "exact section contains hierarchy/electroweak matching scale",
        "hierarchy / electroweak matching scale" in exact_section,
    )
    check(
        "Ward authority is present and labels independent audit status",
        "Status authority" in read(WARD) and "scripts/frontier_yt_ward_identity_derivation.py" in zero,
    )
    check(
        "color-projection authority is present and registered as additional primary runner",
        "scripts/frontier_yt_color_projection_correction.py" in zero and "sqrt(8/9)" in note,
    )

    print("\nPart 4: limitation and non-claim firewall")
    limited = section(note, "## What remains limited")
    cannot = section(note, "## Cannot claim")
    check(
        "limited section scopes caveat to standard-method route",
        contains_all(
            limited,
            [
                "standard lattice-to-continuum matching",
                "standard SM running",
                "standard pole-mass conversion",
            ],
        ),
    )
    check(
        "limited section refuses framework-internal theorem status",
        "not being claimed as a framework-internal theorem" in limited,
    )
    check(
        "cannot-claim section forbids fully-retained UV-to-IR closure",
        "that the `y_t` lane is fully retained from `M_Pl` to `v`" in cannot,
    )
    check(
        "cannot-claim section forbids native continuum-limit theorem claim",
        "framework-internal continuum-limit theorem" in cannot,
    )
    check(
        "cannot-claim section forbids direct-lattice y_t(v) bypass claim",
        "direct lattice extraction already delivers `y_t(v)`" in cannot,
    )
    check(
        "cannot-claim section preserves Schur bridge rather than discarding it",
        "Schur bridge is worthless or obsolete" in cannot,
    )
    check(
        "zero-import authority also refuses fully retained theorem-grade UV-to-IR closure",
        (
            "fully framework-internal retained theorem" in zero_n
            or "fully framework-internal continuum-limit theorem" in zero_n
        )
        and "from `M_Pl` to `v`" in zero_n,
    )
    check(
        "zero-import authority demotes sqrt(8/9) to a conditional connected-trace specialization",
        "conditional connected-trace specialization" in zero_n,
    )
    check(
        "zero-import authority conditions the low-energy package on the underived selector",
        "conditional on the underived Yukawa-side selector `kappa_Y = 0`" in zero_n,
    )
    check(
        "zero-import authority carries a conditionality section for the low-energy package",
        "## Conditionality of the low-energy package" in zero,
    )

    print("\nPart 5: bridge cross-check budget alignment")
    check("flagship note preserves conservative Schur budget 1.2147511%", "1.2147511%" in note)
    check("flagship note preserves support-tight Schur budget 0.75500635%", "0.75500635%" in note)
    check("budget note preserves conservative Schur budget 1.2147511%", "1.2147511%" in budget)
    check("budget note preserves support-tight Schur budget 0.75500635%", "0.75500635%" in budget)
    check(
        "budget note says Schur budget is not live primary classification",
        "no longer the package's load-bearing qualifier" in budget,
    )
    check(
        "flagship note classifies Schur route as independent cross-check",
        "independent cross-check path" in note,
    )

    print("\nPart 6: boundary theorem stays support-only")
    check(
        "boundary theorem explicitly does not close renormalized y_t lane by itself",
        "does **not** by itself close the renormalized `y_t` lane" in boundary_n,
    )
    check(
        "boundary theorem keeps exact subderivation status",
        "**Status:** exact subderivation; bridge-conditioned on the open lane" in boundary,
    )
    check(
        "boundary theorem states full low-energy transfer still not one promoted closure theorem",
        "not yet packaged as one promoted same-surface closure theorem" in boundary_n,
    )

    print("\nPart 7: no hidden observed-input promotion")
    forbidden_positive_phrases = [
        "fully retained from `M_Pl` to `v`.",
        "framework-internal continuum-limit theorem on this exact composite surface has been proved.",
        "direct lattice extraction already delivers `y_t(v)` on accessible lattices.",
    ]
    for phrase in forbidden_positive_phrases:
        check(
            f"forbidden phrase appears only inside the cannot-claim firewall: {phrase!r}",
            phrase not in note_n or phrase in norm(cannot),
        )
    check(
        "paper-safe wording keeps zero external SM observables on framework side",
        "zero external SM observables on the framework side" in note,
    )
    check(
        "paper-safe wording calls current values central values, not retained closure",
        "`y_t` and `m_t` central" in norm(section(note, "## Paper-safe claim"))
        and "values are strong and near observation" in norm(section(note, "## Paper-safe claim"))
        and "fully retained" not in section(note, "## Paper-safe claim"),
    )

    print("\n" + "=" * 78)
    print(f"RESULT: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
