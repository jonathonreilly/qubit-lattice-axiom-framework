#!/usr/bin/env python3
"""Exact factor-signature no-go for determinant-only hierarchy B4 repairs.

The checked hierarchy support packet proves that the minimal-block
determinant carries u_0^16. The B4 coupling-power target is
alpha_LM^16 = alpha_bare^16 u_0^-16. This runner verifies, with exact
integer exponent bookkeeping plus numeric sanity checks at the canonical
surface, that determinant-only expressions cannot supply the missing
alpha_bare^16 coupling-power content.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs" / "HIERARCHY_B4_DETERMINANT_ONLY_FACTOR_SIGNATURE_NO_GO_NOTE_2026-06-17.md"
HIERARCHY_NOTE = REPO_ROOT / "docs" / "HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md"
OPEN_GATE_NOTE = REPO_ROOT / "docs" / "HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_2026-05-30.md"

PASS = 0
FAIL = 0
CLASS_COUNTS = {"A": 0, "B": 0, "C": 0}


@dataclass(frozen=True)
class FactorSignature:
    """Exponent pair for alpha_bare^a * u_0^b, constants stripped."""

    alpha_bare_exp: int
    u0_exp: int

    def __mul__(self, other: "FactorSignature") -> "FactorSignature":
        return FactorSignature(
            self.alpha_bare_exp + other.alpha_bare_exp,
            self.u0_exp + other.u0_exp,
        )

    def quotient(self, other: "FactorSignature") -> "FactorSignature":
        return FactorSignature(
            self.alpha_bare_exp - other.alpha_bare_exp,
            self.u0_exp - other.u0_exp,
        )

    def power(self, n: int) -> "FactorSignature":
        return FactorSignature(self.alpha_bare_exp * n, self.u0_exp * n)


def check(klass: str, name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
        CLASS_COUNTS[klass] += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}][{klass}] {name}{suffix}")
    return condition


def section(title: str) -> None:
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_factor_signatures() -> None:
    section("Exact factor-signature algebra")
    det = FactorSignature(0, 16)
    alpha_bare = FactorSignature(1, 0)
    u0 = FactorSignature(0, 1)
    alpha_lm = alpha_bare.quotient(u0)
    alpha_s = alpha_bare.quotient(u0.power(2))
    target = alpha_lm.power(16)

    check("A", "determinant side has signature (0, 16)", det == FactorSignature(0, 16), str(det))
    check("A", "alpha_LM has signature (1, -1)", alpha_lm == FactorSignature(1, -1), str(alpha_lm))
    check("A", "alpha_LM^16 has signature (16, -16)", target == FactorSignature(16, -16), str(target))
    check("A", "alpha_s has signature (1, -2)", alpha_s == FactorSignature(1, -2), str(alpha_s))
    check("A", "determinant times alpha_s^16 equals alpha_LM^16", det * alpha_s.power(16) == target, str(det * alpha_s.power(16)))

    transport = target.quotient(det)
    check(
        "A",
        "missing multiplier relative to u_0^16 is alpha_s^16",
        transport == alpha_s.power(16) == FactorSignature(16, -32),
        str(transport),
    )

    semiring = {det.power(k) for k in range(0, 7)}
    check(
        "A",
        "finite determinant products keep alpha exponent zero",
        all(sig.alpha_bare_exp == 0 for sig in semiring),
        str(sorted((sig.alpha_bare_exp, sig.u0_exp) for sig in semiring)),
    )
    check("A", "target is absent from determinant-product family", target not in semiring)

    quotient_family = {det.power(k) for k in range(-6, 7)}
    check(
        "A",
        "even determinant quotients keep alpha exponent zero",
        all(sig.alpha_bare_exp == 0 for sig in quotient_family),
        str(sorted((sig.alpha_bare_exp, sig.u0_exp) for sig in quotient_family)[:5]) + " ...",
    )
    check("A", "target is absent from determinant-quotient family", target not in quotient_family)
    check(
        "A",
        "determinant inverse has the right u_0 sign but still misses alpha_bare^16",
        det.power(-1) == FactorSignature(0, -16) and det.power(-1) != target,
        str(det.power(-1)),
    )


def check_canonical_numbers() -> None:
    section("Canonical-surface numeric sanity checks")
    plaquette = 0.5934
    u0 = plaquette ** 0.25
    alpha_bare = 1.0 / (4.0 * math.pi)
    alpha_lm = alpha_bare / u0
    alpha_s = alpha_bare / (u0 * u0)

    determinant_stripped = u0**16
    target = alpha_lm**16
    transport = target / determinant_stripped

    check("C", "u_0^16 equals <P>^4 at the B1 surface", math.isclose(determinant_stripped, plaquette**4, rel_tol=1e-15), f"{determinant_stripped:.12g}")
    check("C", "alpha_LM^16 equals alpha_bare^16 u_0^-16", math.isclose(target, alpha_bare**16 * u0**-16, rel_tol=1e-15), f"{target:.12e}")
    check("C", "target/determinant equals alpha_s^16", math.isclose(transport, alpha_s**16, rel_tol=1e-12), f"{transport:.12e}")
    check("C", "using u_0^16 instead of alpha_LM^16 displaces by more than 10^15", determinant_stripped / target > 1.0e15, f"ratio={determinant_stripped / target:.6e}")
    check("C", "alpha_bare^16 supplies the coupling-power magnitude scale", 1.0e-19 < alpha_bare**16 < 1.0e-17, f"alpha_bare^16={alpha_bare**16:.6e}")
    check("C", "u_0^-16 is order-unity rather than a hierarchy source", 1.0 < u0**-16 < 10.0, f"u_0^-16={u0**-16:.6f}")


def check_source_markers() -> None:
    section("Source-note boundary markers")
    note = read(NOTE)
    hierarchy = read(HIERARCHY_NOTE)
    gate = read(OPEN_GATE_NOTE)
    hierarchy_flat = " ".join(hierarchy.split()).lower()
    gate_flat = " ".join(gate.split()).lower()

    required_note = [
        "**Claim type:** no_go",
        "**Claim-strength label:** exact boundary theorem on open gate",
        "independent audit lane only",
        "determinant-only repair of B4",
        "sig(alpha_LM^16) = (16, -16)",
        "alpha_LM^16 / u_0^16",
        "alpha_s^16",
        "Non-determinant attachment-observable routes remain open",
        "does not edit the audit ledger",
        "exhaustion of every possible future B4 mechanism",
    ]
    for marker in required_note:
        check("B", f"new note contains marker: {marker}", marker in note)

    forbidden_note = [
        "This packet closes B4",
        "retained closure",
        "EW VEV prediction.",
        "audit verdict: " + "retained",
        "the only possible B4 route",
    ]
    for marker in forbidden_note:
        check("B", f"new note omits forbidden marker: {marker}", marker not in note)

    required_hierarchy = [
        "B4 is unchanged and remains open",
        "the determinant supplies `u_0^16`",
        "`alpha_LM^16 = alpha_bare^16 u_0^(-16)`",
        "not by the determinant power",
        "not a determinant identity",
    ]
    for marker in required_hierarchy:
        check("B", f"parent hierarchy note contains marker: {marker}", marker.lower() in hierarchy_flat)

    required_gate = [
        "named gap: B4 attachment-observable identification",
        "not a shipped global no-go",
        "does not claim that every possible future mechanism is closed",
        "Surviving routes run through beyond-mean-field link fluctuations",
        "Green-kernel",
        "non-link transport rule",
    ]
    for marker in required_gate:
        check("B", f"open-gate note contains marker: {marker}", marker.lower() in gate_flat)


def main() -> int:
    check_factor_signatures()
    check_canonical_numbers()
    check_source_markers()
    print()
    print(f"CLASS_COUNTS: {CLASS_COUNTS}")
    if FAIL:
        print("VERDICT: hierarchy B4 determinant-only factor-signature no-go checks failed.")
        print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
        return 1
    print("VERDICT: hierarchy B4 determinant-only factor-signature no-go checks pass.")
    print(f"TOTAL: PASS={PASS}, FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
