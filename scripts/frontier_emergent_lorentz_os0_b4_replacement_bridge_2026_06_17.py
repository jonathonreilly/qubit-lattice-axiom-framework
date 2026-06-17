#!/usr/bin/env python3
"""Verify the OS0 B4 marginal-velocity replacement bridge.

The runner checks the finite invariant-space calculation and verifies that the
source note routes OS0 marginal-velocity protection through the landed
all-orders B4 theorem, not through the older supplied one-loop RG packet.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "EMERGENT_LORENTZ_OS0_B4_MARGINAL_VELOCITY_REPLACEMENT_BRIDGE_2026-06-17.md"
OLD = ROOT / "docs" / "EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md"
B4 = ROOT / "docs" / "ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md"
KIN = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
B4_ONE_LOOP = ROOT / "docs" / "EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")
    return ok


def rank(rows: list[list[Fraction]], ncols: int) -> int:
    mat = [row[:] for row in rows if any(x != 0 for x in row)]
    r = 0
    for c in range(ncols):
        pivot = None
        for i in range(r, len(mat)):
            if mat[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        pv = mat[r][c]
        mat[r] = [x / pv for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] != 0:
                f = mat[i][c]
                mat[i] = [a - f * b for a, b in zip(mat[i], mat[r])]
        r += 1
    return r


def invariant_dimension(n_axes: int, allowed_perms: list[tuple[int, ...]]) -> int:
    # Coefficients c_i are invariant under p iff c_i = c_{p(i)}.
    equations: list[list[Fraction]] = []
    for p in allowed_perms:
        for i in range(n_axes):
            row = [Fraction(0) for _ in range(n_axes)]
            row[i] += Fraction(1)
            row[p[i]] -= Fraction(1)
            equations.append(row)
    return n_axes - rank(equations, n_axes)


def squash(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    print("Emergent Lorentz OS0 B4 replacement bridge verifier")

    note = NOTE.read_text(encoding="utf-8")
    old = OLD.read_text(encoding="utf-8")
    b4 = B4.read_text(encoding="utf-8")
    kin = KIN.read_text(encoding="utf-8")
    one_loop = B4_ONE_LOOP.read_text(encoding="utf-8")
    note_flat = squash(note)
    old_flat = squash(old)
    b4_flat = squash(b4)

    spatial_perms = []
    for p3 in permutations([1, 2, 3]):
        spatial_perms.append((0,) + p3)
    b4_perms = list(permutations(range(4)))

    dim_oh = invariant_dimension(4, spatial_perms)
    dim_b4 = invariant_dimension(4, b4_perms)

    check("spatial O_h plus fixed time leaves two diagonal marginal coefficients", dim_oh == 2, f"dim={dim_oh}")
    check("B4 signed-permutation diagonal invariant space is one-dimensional", dim_b4 == 1, f"dim={dim_b4}")
    check("B4 theorem source contains all-orders perturbative protection", "all-orders" in b4_flat and "effective action" in b4_flat and "B4`-non-invariant marginal velocity operator" in b4_flat)
    check("B4 theorem source keeps supplied-regulator boundary explicit", "supplied regulated action" in b4_flat and "does not derive the choice of regulator action" in b4_flat)
    check("kinetic primitive supplies OS0 kinetic-form premise only", "OS0" in kin and "c_t = c_s" in kin and "does not supply" in kin)
    check("one-loop B4 predecessor is OS0 scoped", "OS0 kinetic-form surface" in one_loop and "dimension-6" in one_loop)
    check("older interacting row remains conditional on supplied one-loop dynamics", "supplied one-loop velocity-RG dynamics" in old and "conditional-support / open gate" in old)
    check("older interacting row names continuous-time/non-isotropic surface boundary", "continuous-time/non-isotropic" in old_flat and "remain conditional" in old_flat)
    check("new note declares exact support, not audit status", "**Claim type:** exact support theorem" in note and "independent audit lane only" in note)
    check("new note targets OS0 branch replacement rather than promotion", "does not promote that older row" in note and "continuous-time/non-isotropic horn" in note)
    check("new note retires supplied RG inputs for OS0 marginal-protection branch", "Retired for the OS0 marginal-protection branch" in note and "supplied one-loop velocity-RG dynamics" in note)
    check("new note keeps non-OS0 and physical-bound gaps open", "physical Standard-Model Extension bound comparison" in note and "continuous-time/non-isotropic horn" in note)
    check("new note gives downstream citation rule", "Rows that need OS0 marginal velocity protection should cite this bridge" in note)
    check("new note forbids bare retained Lorentz closure", "not a bare retained Lorentz theorem" in note_flat and "not a new axiom" in note_flat)
    check("bridge does not consume old supplied RG as proof input", "supplied one-loop velocity-RG equations" in note and "are not proof inputs" in note)

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
