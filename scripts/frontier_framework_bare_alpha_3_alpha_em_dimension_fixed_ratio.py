#!/usr/bin/env python3
"""Verify the bare alpha_3 / alpha_em formal assumed-input identity theorem.

This runner verifies only the repaired current source packet:

1. the exact bare-coupling algebra under explicit formal hypotheses H1-H4, and
2. the source boundary that forbids retained EW-lane, minimal-stack, or
   low-energy phenomenology claims from this current row.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
D = 3


@dataclass
class Audit:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.passed += 1
            print(f"PASS: {label}" + (f" :: {detail}" if detail else ""))
        else:
            self.failed += 1
            print(f"FAIL: {label}" + (f" :: {detail}" if detail else ""))


def read(path: str) -> str:
    primary = ROOT / path
    if primary.exists():
        return primary.read_text(encoding="utf-8")
    # Fall back: notes archived as audited_failed (retained_no_go) live
    # under archive_unlanded/<bucket>/<filename>. Search for the basename.
    archive_root = ROOT / "archive_unlanded"
    if archive_root.exists():
        from pathlib import Path as _Path
        target_name = _Path(path).name
        for archived in archive_root.rglob(target_name):
            return archived.read_text(encoding="utf-8")
    raise FileNotFoundError(f"{path} not found in repo or archive_unlanded/")


def frac_eq(label: str, audit: Audit, actual: Fraction, expected: Fraction) -> None:
    audit.check(label, actual == expected, f"actual={actual}, expected={expected}")


def float_close(label: str, audit: Audit, actual: float, expected: float, tol: float = 1e-14) -> None:
    audit.check(label, abs(actual - expected) <= tol, f"actual={actual:.17g}, expected={expected:.17g}")


def audit_scope_boundary(audit: Audit) -> None:
    note_path = "docs/FRAMEWORK_BARE_ALPHA_RATIO_ASSUMED_INPUT_IDENTITY_SUPPORT_NOTE_2026-04-30.md"
    archived_note_path = (
        "archive_unlanded/framework-bare-alpha-assumed-input-salvage-2026-04-30/"
        "FRAMEWORK_BARE_ALPHA_3_ALPHA_EM_DIMENSION_FIXED_RATIO_SUPPORT_NOTE_2026-04-25.md"
    )
    archive_root = ROOT / "archive_unlanded"

    def _authority_exists(rel: str) -> bool:
        if (ROOT / rel).exists():
            return True
        if archive_root.exists():
            from pathlib import Path as _P
            for _ in archive_root.rglob(_P(rel).name):
                return True
        return False

    audit.check(f"source file exists: {note_path}", _authority_exists(note_path))
    audit.check(f"archived audited-failed wrapper exists: {archived_note_path}", _authority_exists(archived_note_path))

    note = read(note_path)
    archived_note = read(archived_note_path)
    flat_note = " ".join(note.split())
    flat_archived = " ".join(archived_note.split())

    audit.check(
        "note status is bounded formal identity theorem only",
        "bounded-support / formal assumed-input identity theorem" in flat_note
        and "not a live retained EW-normalization theorem" in flat_note,
    )
    audit.check(
        "note declares formal hypotheses H1-H4",
        all(marker in note for marker in ["H1:", "H2:", "H3:", "H4:"])
        and "formal hypotheses in this row, not physical authorities" in flat_note,
    )
    audit.check(
        "note states exact load-bearing theorem",
        "alpha_3(bare) / alpha_em(bare) = 2d + 3" in note
        and "sin^2(theta_W)(bare) = (d + 1)/(2d + 3)" in note,
    )
    audit.check(
        "note blocks retained EW-lane authority",
        "does not assert that a retained EW-normalization lane exists" in note
        and "does not derive the coupling inputs" in note,
    )
    audit.check(
        "note blocks minimal-stack promotion",
        "does not promote a `Cl(3) -> SM` support packet" in flat_note
        and "minimal-input stack" in note,
    )
    audit.check(
        "note blocks low-energy phenomenology",
        "does not claim direct low-energy phenomenology" in flat_note,
    )
    audit.check(
        "note records current 2026-04-30 source authority",
        "Date:** 2026-04-30" in note
        and "archive_unlanded/framework-bare-alpha-assumed-input-salvage-2026-04-30/" in note,
    )
    audit.check(
        "status boundary forbids bare retained",
        "actual_current_surface_status: bounded-support" in note
        and "bare_retained_allowed: false" in note
        and "proposal_allowed: false" in note,
    )
    audit.check(
        "archived failed wrapper points at canonical repair packet",
        "docs/FRAMEWORK_BARE_ALPHA_RATIO_ASSUMED_INPUT_IDENTITY_SUPPORT_NOTE_2026-04-30.md" in archived_note
        and "direct same-path handoff to the narrowed source boundary" in archived_note,
    )
    audit.check(
        "archived failed wrapper is non-authority conditional algebra only",
        "This file remains archived" in archived_note
        and "not a live retained theorem" in archived_note
        and "not retained-grade support authority" in flat_archived
        and "supplied inputs are hypotheses of the lemma" in flat_archived,
    )
    audit.check(
        "archived failed wrapper reproduction matches current runner verdict",
        "VERDICT: FORMAL ASSUMED-INPUT IDENTITY THEOREM VERIFIED" in archived_note,
    )

    forbidden = [
        "support corollary on a retained EW-normalization surface",
        "retained EW normalization lane remains the authoritative route",
        "candidate retained-grade support corollary on the retained EW surface",
        "Retained derivation theorem on main",
        "three independent retained inputs",
        "independent retained structural routes",
        "**Status:** retained",
        "physical use is closed by this row",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent from canonical note: {phrase}", phrase not in note)
        audit.check(f"forbidden overclaim absent from archived wrapper: {phrase}", phrase not in archived_note)


def audit_exact_algebra(audit: Audit) -> None:
    d = D
    g3_sq = Fraction(1, 1)
    g2_sq = Fraction(1, d + 1)
    gy_sq = Fraction(1, d + 2)

    inv_g3 = Fraction(1, 1) / g3_sq
    inv_g2 = Fraction(1, 1) / g2_sq
    inv_gy = Fraction(1, 1) / gy_sq
    inv_gem = inv_g2 + inv_gy
    gem_sq = Fraction(1, 1) / inv_gem

    frac_eq("input d fixed to 3", audit, Fraction(d, 1), Fraction(3, 1))
    frac_eq("H2 formal hypothesis: g3^2 = 1", audit, g3_sq, Fraction(1, 1))
    frac_eq("H3 formal hypothesis: g2^2 = 1/(d+1)", audit, g2_sq, Fraction(1, 4))
    frac_eq("H4 formal hypothesis: gY^2 = 1/(d+2)", audit, gy_sq, Fraction(1, 5))
    frac_eq("1/g2^2 = d+1", audit, inv_g2, Fraction(4, 1))
    frac_eq("1/gY^2 = d+2", audit, inv_gy, Fraction(5, 1))

    frac_eq("D1 inverse-EM sum = 2d+3", audit, inv_gem, Fraction(2 * d + 3, 1))
    frac_eq("D1 inverse-EM sum at d=3 = 9", audit, inv_gem, Fraction(9, 1))
    frac_eq("D2 g_em^2 = 1/(2d+3)", audit, gem_sq, Fraction(1, 9))

    sin2 = gy_sq / (g2_sq + gy_sq)
    cos2 = g2_sq / (g2_sq + gy_sq)
    frac_eq("D3 sin^2(theta_W) = (d+1)/(2d+3)", audit, sin2, Fraction(d + 1, 2 * d + 3))
    frac_eq("D3 sin^2(theta_W) at d=3 = 4/9", audit, sin2, Fraction(4, 9))
    frac_eq("cos^2(theta_W) at d=3 = 5/9", audit, cos2, Fraction(5, 9))
    frac_eq("weak-angle sum = 1", audit, sin2 + cos2, Fraction(1, 1))

    alpha_ratio = g3_sq / gem_sq
    frac_eq("D4 alpha3/alpha_em = g3^2/g_em^2", audit, alpha_ratio, Fraction(9, 1))
    frac_eq("D4 alpha3/alpha_em = g3^2*(2d+3)", audit, alpha_ratio, g3_sq * Fraction(2 * d + 3, 1))

    alpha_em = float(gem_sq) / (4.0 * math.pi)
    alpha3 = float(g3_sq) / (4.0 * math.pi)
    float_close("D5 alpha_em = 1/(36 pi)", audit, alpha_em, 1.0 / (36.0 * math.pi))
    float_close("alpha3/alpha_em float ratio = 9", audit, alpha3 / alpha_em, 9.0)

    inverse_alpha_sum_factor = inv_g3 + inv_g2 + inv_gy
    frac_eq("D6 inverse-alpha sum factor = 2d+4", audit, inverse_alpha_sum_factor, Fraction(2 * d + 4, 1))
    float_close(
        "D6 inverse-alpha sum = 40 pi",
        audit,
        float(inverse_alpha_sum_factor) * 4.0 * math.pi,
        40.0 * math.pi,
    )

    su5_sin2 = Fraction(3, 8)
    frac_eq("framework minus SU(5) sin^2 offset = 5/72", audit, sin2 - su5_sin2, Fraction(5, 72))
    audit.check("framework bare angle is not SU(5)", sin2 != su5_sin2)


def audit_dimension_fingerprint(audit: Audit) -> None:
    expected = {2: 7, 3: 9, 4: 11, 5: 13}
    for d, value in expected.items():
        ratio = 2 * d + 3
        audit.check(f"dimension fingerprint d={d}", ratio == value, f"ratio={ratio}")

    inverse = {2 * d + 3: d for d in range(1, 9)}
    audit.check("integer 9 uniquely maps to d=3 in checked range", inverse[9] == 3)
    audit.check("fingerprint sequence odd integers", all((2 * d + 3) % 2 == 1 for d in range(1, 9)))


def main() -> int:
    audit = Audit()
    print("=== Bare alpha_3 / alpha_em formal assumed-input identity theorem ===")
    audit_scope_boundary(audit)
    audit_exact_algebra(audit)
    audit_dimension_fingerprint(audit)
    print(f"TOTAL: PASS={audit.passed}, FAIL={audit.failed}")
    if audit.failed:
        print("VERDICT: FAIL")
        return 1
    print("VERDICT: FORMAL ASSUMED-INPUT IDENTITY THEOREM VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
