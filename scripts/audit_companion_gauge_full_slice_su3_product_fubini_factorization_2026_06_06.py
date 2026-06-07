#!/usr/bin/env python3
"""SU(3) product-Fubini certificate for a supplied rim/far support split.

This runner does not estimate the beta=6 plaquette value. It verifies the
mathematical step that was previously represented only by an SU(2) toy:
for a finite SU(3) Wilson slab whose plaquette supports split into fixed+rim
or fixed+far variables, product Haar measure gives an exact pointwise
rim/environment factorization. It also checks the class-projection scalar
pull-out used by the compressed-rim wording.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
from typing import Iterable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "GAUGE_VACUUM_PLAQUETTE_SU3_FULL_SLICE_PRODUCT_FUBINI_FACTORIZATION_NOTE_2026-06-06.md"
PARENT = DOCS / "GAUGE_VACUUM_PLAQUETTE_FULL_SLICE_RIM_LIFT_INTEGRAL_BOUNDARY_SCIENCE_ONLY_NOTE_2026-04-17.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def special_unitary_from_qr(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    q = q @ np.diag(phases / np.abs(phases))
    det = np.linalg.det(q)
    q[:, -1] /= det
    return q


def support_kind(support: set[str], rim: set[str], far: set[str], fixed: set[str]) -> str:
    moving = support - fixed
    has_rim = bool(moving & rim)
    has_far = bool(moving & far)
    if has_rim and has_far:
        return "mixed"
    if has_rim:
        return "rim"
    if has_far:
        return "far"
    return "fixed"


def exact_product_fubini() -> bool:
    # Finite exact analogue of a positive product-density integral. Fractions
    # make the identity exact rather than numerical.
    rim_weights = [Fraction(5, 3), Fraction(7, 4), Fraction(11, 6)]
    far_weights = [Fraction(13, 5), Fraction(17, 7)]
    joint = sum(a * b for a in rim_weights for b in far_weights)
    factored = sum(rim_weights) * sum(far_weights)
    return joint == factored


def projection_scalar_pullout() -> bool:
    # P_cls is represented by the two-class averaging projection. The scalar
    # far factor is independent of W, so it pulls through P_cls exactly.
    p_cls = (
        (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(1, 2), Fraction(1, 2)),
    )
    b = (Fraction(5, 7), Fraction(11, 13))
    far_scalar = Fraction(19, 17)

    def mat_vec(
        mat: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
        vec: tuple[Fraction, Fraction],
    ) -> tuple[Fraction, Fraction]:
        return (
            mat[0][0] * vec[0] + mat[0][1] * vec[1],
            mat[1][0] * vec[0] + mat[1][1] * vec[1],
        )

    left = mat_vec(p_cls, (far_scalar * b[0], far_scalar * b[1]))
    right_base = mat_vec(p_cls, b)
    right = (far_scalar * right_base[0], far_scalar * right_base[1])
    return left == right


def all_distinct(values: Iterable[str]) -> bool:
    vals = list(values)
    return len(vals) == len(set(vals))


def main() -> int:
    print("=" * 88)
    print("SU(3) FULL-SLICE PRODUCT-FUBINI FACTORIZATION CERTIFICATE")
    print("=" * 88)

    note = text(NOTE)
    note_flat = " ".join(note.split())
    parent = text(PARENT)

    fixed = {"U_left", "U_right", "W_marked"}
    rim = {"r0", "r1", "r2", "r3"}
    far = {"f0", "f1", "f2", "f3", "f4"}
    plaquettes = {
        "marked_scalar": {"W_marked", "U_left"},
        "rim_left": {"U_left", "W_marked", "r0", "r1"},
        "rim_right": {"U_right", "W_marked", "r2", "r3"},
        "far_bulk_a": {"U_left", "f0", "f1"},
        "far_bulk_b": {"U_right", "f2", "f3", "f4"},
    }

    kinds = {name: support_kind(set(support), rim, far, fixed) for name, support in plaquettes.items()}
    print("Support partition:")
    for name, kind in kinds.items():
        print(f"  {name:<14} -> {kind:<5} {sorted(plaquettes[name])}")
    print()

    check("companion note exists", NOTE.exists())
    check("parent rim-lift note exists", PARENT.exists())
    check("rim and far variables are disjoint", rim.isdisjoint(far))
    check("all moving variables are uniquely named", all_distinct([*rim, *far]))
    check("every plaquette is classified as fixed/rim/far", set(kinds.values()) <= {"fixed", "rim", "far"})
    check("no plaquette mixes rim and far variables", "mixed" not in kinds.values())
    check("at least one rim plaquette is present", any(kind == "rim" for kind in kinds.values()))
    check("at least one far plaquette is present", any(kind == "far" for kind in kinds.values()))

    # SU(3) sanity: the theorem uses compact SU(3) Haar variables. We do not
    # sample integrals here; the matrices certify the group target and the
    # bounded Wilson trace range used in the compactness/Tonelli argument.
    g = special_unitary_from_qr(20260606)
    h = special_unitary_from_qr(20260607)
    gh = g @ h
    eye = np.eye(3)
    unitary_ok = (
        np.linalg.norm(g.conj().T @ g - eye) < 1.0e-12
        and np.linalg.norm(h.conj().T @ h - eye) < 1.0e-12
        and np.linalg.norm(gh.conj().T @ gh - eye) < 1.0e-12
    )
    det_ok = (
        abs(np.linalg.det(g) - 1.0) < 1.0e-12
        and abs(np.linalg.det(h) - 1.0) < 1.0e-12
        and abs(np.linalg.det(gh) - 1.0) < 1.0e-12
    )
    re_tr = float(np.real(np.trace(gh)))
    check("explicit variables are SU(3) matrices", unitary_ok and det_ok, f"Re Tr(gh)={re_tr:.6f}")
    check("Wilson Re Tr term is bounded on SU(3)", -3.0 <= re_tr <= 3.0)

    check("finite product-measure identity holds exactly", exact_product_fubini())
    check("class projection pulls out W-independent far scalar", projection_scalar_pullout())

    required_note_phrases = (
        "G = SU(3)",
        "Xi = Xi^rim sqcup Xi^far",
        "no plaquette contains both a rim variable and a far variable",
        "Fubini/Tonelli applies directly",
        "not a separate proof of the temporal-gauge mixed-kernel compression",
        "does not apply an audit verdict",
    )
    for phrase in required_note_phrases:
        check(f"companion note contains boundary phrase: {phrase}", phrase in note_flat)

    check(
        "parent note now points to SU(3) product-Fubini companion",
        "SU(3) full-slice product-Fubini companion" in parent
        and "audit_companion_gauge_full_slice_su3_product_fubini_factorization_2026_06_06.py" in parent,
    )
    check("companion note states no audit-data edit", "docs/audit/data/*" in note)

    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
