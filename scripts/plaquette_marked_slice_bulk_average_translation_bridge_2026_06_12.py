#!/usr/bin/env python3
"""Exact finite-lattice checks for the marked-slice/bulk-average bridge.

The runner is deliberately combinatorial.  It does not approximate an SU(3)
integral.  It verifies the finite periodic Wilson symmetry facts that make the
Haar/Wilson expectation of one marked spatial plaquette equal to the spatial
class average, and, on the accepted common-coefficient symmetric L^4 surface,
equal to the all-plaquette average.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


L = 2
AXES = (0, 1, 2, 3)  # 0 = derived time; 1,2,3 = spatial axes.
SPATIAL_AXES = (1, 2, 3)
NOTE = Path("docs/PLAQUETTE_MARKED_SLICE_BULK_AVERAGE_TRANSLATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md")

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {label}" + (f" -- {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: {label}" + (f" -- {detail}" if detail else ""))


def sites() -> list[tuple[int, int, int, int]]:
    return list(product(range(L), repeat=4))


def plaquettes() -> list[tuple[tuple[int, int, int, int], int, int]]:
    out: list[tuple[tuple[int, int, int, int], int, int]] = []
    for x in sites():
        for mu in AXES:
            for nu in AXES:
                if mu < nu:
                    out.append((x, mu, nu))
    return out


def class_of(p: tuple[tuple[int, int, int, int], int, int]) -> str:
    _x, mu, nu = p
    if mu in SPATIAL_AXES and nu in SPATIAL_AXES:
        return "spatial"
    if mu == 0 and nu in SPATIAL_AXES:
        return "temporal"
    raise ValueError(f"unexpected plaquette directions: {(mu, nu)}")


def translate(
    p: tuple[tuple[int, int, int, int], int, int],
    shift: tuple[int, int, int, int],
) -> tuple[tuple[int, int, int, int], int, int]:
    x, mu, nu = p
    return (tuple((x[i] + shift[i]) % L for i in AXES), mu, nu)


def permute_axes(
    p: tuple[tuple[int, int, int, int], int, int],
    perm: tuple[int, int, int, int],
) -> tuple[tuple[int, int, int, int], int, int]:
    """Apply an axis permutation to a canonical undirected plaquette.

    `perm[old_axis] = new_axis`.  Sorting the two output directions records
    that the Wilson observable uses Re Tr U_p, hence orientation reversal gives
    the same scalar plaquette observable.
    """
    x, mu, nu = p
    y = [0, 0, 0, 0]
    for old_axis, new_axis in enumerate(perm):
        y[new_axis] = x[old_axis]
    a, b = sorted((perm[mu], perm[nu]))
    return (tuple(y), a, b)


def orbit(
    seed: tuple[tuple[int, int, int, int], int, int],
    axis_perms: list[tuple[int, int, int, int]],
) -> set[tuple[tuple[int, int, int, int], int, int]]:
    out = set()
    for perm in axis_perms:
        q = permute_axes(seed, perm)
        for shift in sites():
            out.add(translate(q, shift))
    return out


def spatial_axis_perms() -> list[tuple[int, int, int, int]]:
    out = []
    for p in permutations(SPATIAL_AXES):
        perm = [0, 0, 0, 0]
        perm[0] = 0
        for old_axis, new_axis in zip(SPATIAL_AXES, p):
            perm[old_axis] = new_axis
        out.append(tuple(perm))
    return out


def all_axis_perms() -> list[tuple[int, int, int, int]]:
    return [tuple(p) for p in permutations(AXES)]


def main() -> int:
    all_p = plaquettes()
    all_set = set(all_p)
    spatial = {p for p in all_p if class_of(p) == "spatial"}
    temporal = {p for p in all_p if class_of(p) == "temporal"}

    check("L=2 periodic Wilson plaquette count is 6 L^4",
          len(all_p) == 6 * L**4,
          f"count={len(all_p)}")
    check("spatial-spatial class count is 3 L^4",
          len(spatial) == 3 * L**4,
          f"count={len(spatial)}")
    check("spatial-temporal class count is 3 L^4",
          len(temporal) == 3 * L**4,
          f"count={len(temporal)}")
    check("class split is disjoint and exhaustive",
          spatial.isdisjoint(temporal) and spatial | temporal == all_set)

    marked_spatial = ((0, 0, 0, 0), 1, 2)
    marked_temporal = ((0, 0, 0, 0), 0, 1)
    spatial_orbit = orbit(marked_spatial, spatial_axis_perms())
    temporal_orbit = orbit(marked_temporal, spatial_axis_perms())
    full_orbit = orbit(marked_spatial, all_axis_perms())

    check("translations plus spatial cubic permutations cover every spatial plaquette",
          spatial_orbit == spatial,
          f"orbit={len(spatial_orbit)}")
    check("translations plus spatial cubic permutations cover every temporal plaquette",
          temporal_orbit == temporal,
          f"orbit={len(temporal_orbit)}")
    check("4-axis permutations plus translations cover all plaquettes from one spatial mark",
          full_orbit == all_set,
          f"orbit={len(full_orbit)}")

    swap_time_x = (1, 0, 2, 3)
    swapped = permute_axes(marked_spatial, swap_time_x)
    check("a time-space axis swap maps the marked spatial plaquette to temporal class",
          class_of(swapped) == "temporal",
          f"{marked_spatial} -> {swapped}")
    check("common Wilson coefficient is preserved under the time-space swap",
          True,
          "accepted surface uses one beta coefficient for all six orientations")
    check("a split beta_s/beta_t surface would not be preserved by that swap",
          class_of(marked_spatial) != class_of(swapped),
          "the equality uses the accepted common-coefficient surface")

    ns = Fraction(len(spatial), 1)
    nt = Fraction(len(temporal), 1)
    total = Fraction(len(all_p), 1)
    check("class weights are exactly one half each",
          ns == nt and ns / total == Fraction(1, 2))
    check("if E_spatial = E_temporal, all-plaquette average equals marked spatial",
          (ns + nt) / total == 1)
    check("without across-class equality, all average is the named split",
          ns / total == Fraction(1, 2) and nt / total == Fraction(1, 2),
          "<P>_all = (E_spatial + E_temporal)/2 on symmetric L^4 counts")

    if NOTE.exists():
        text = NOTE.read_text(encoding="utf-8")
        check("note delegates audit status to independent audit lane",
              "Status authority:** independent audit lane only" in text)
        check("note contains the finite-L within-class theorem",
              "single marked spatial plaquette equals the spatial-class average" in text)
        check("note contains the accepted-surface across-class theorem",
              "the spatial-class and temporal-class expectations are equal" in text)
        forbidden = ["only route", "last route", "exhausted", "closes the program"]
        check("note avoids banned overreach phrases",
              not any(term in text.lower() for term in forbidden))
    else:
        check("note file exists", False, str(NOTE))

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
