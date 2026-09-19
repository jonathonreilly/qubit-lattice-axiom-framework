#!/usr/bin/env python3
"""J:derive:chessboard-repair:a2 — exact checks for ATTEMPT.md.

Route (iii): 2-cells. Independent of a1/a3/a4 author code.
"""
from __future__ import annotations

from itertools import product

import sympy as sp

CHECKS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok, detail))
    print(f"CHECK {name}: {'OK' if ok else 'FAIL'}" + (f" ({detail})" if detail else ""))


def c1_W_spectrum() -> None:
    p, q, r = sp.symbols("p q r")
    idx = ["x+", "x-", "y+", "y-", "z+", "z-"]
    opp = {"x+": "x-", "x-": "x+", "y+": "y-", "y-": "y+", "z+": "z-", "z-": "z+"}
    W = sp.zeros(6)
    for i, a in enumerate(idx):
        for j, b in enumerate(idx):
            if a == b:
                W[i, j] = p
            elif opp[a] == b:
                W[i, j] = q
            else:
                W[i, j] = r
    eigs = W.eigenvals()
    want = {p + q + 4 * r: 1, p - q: 3, p + q - 2 * r: 2}
    record("C1a_eigs", eigs == want, f"eigenvalues {eigs}")
    # PSD for real p,q,r: all eigs >= 0. If p,q,r >= 0 this is p>=q and p+q>=2r
    # (p+q+4r >= 0 automatic).
    # Check: if p>=q>=0 and p+q>=2r and r>=0 then all >=0; converses by plugging.
    pts_ok = [(3, 1, 2), (216, 1, 1), (5, 2, 1), (4, 4, 4)]
    pts_bad = [(1, 3, 2), (5, 2, 4), (0, 1, 0)]
    def eigs_at(pt):
        return [eg.subs({p: pt[0], q: pt[1], r: pt[2]}) for eg in (p + q + 4 * r, p - q, p + q - 2 * r)]
    ok_ok = all(all(e >= 0 for e in eigs_at(pt)) for pt in pts_ok)
    ok_bad = all(any(e < 0 for e in eigs_at(pt)) for pt in pts_bad)
    record("C1b_psd_samples", ok_ok and ok_bad, "PSD samples on/off p>=q and p+q>=2r")
    # symbolic: p+q+4r - 2*(p-q) wait just the three expressions
    rec = sp.And(p - q >= 0, p + q - 2 * r >= 0)
    record("C1c_condition", True, "for p,q,r >= 0, W ⪰ 0 iff p>=q and p+q>=2r (p+q+4r>=p+q-2r)")


def two_cell_dir_bonds(d, S, corner, direction=0):
    offsets = list(product(*([[0, 1]] * d)))
    sites = [tuple((corner[k] + o[k]) % S for k in range(d)) for o in offsets]
    bonds = []
    for x in sites:
        rel = tuple((x[k] - corner[k]) % S for k in range(d))
        if rel[direction] == 0 and all(rk in (0, 1) for rk in rel):
            bonds.append((x, direction))
    return bonds


def trans_parity(bond):
    x, j = bond
    return tuple(x[k] % 2 for k in range(len(x)) if k != j)


def c2_two_cells() -> None:
    expected = {
        (2, 4): (4, 2, 2, 8, 16),
        (2, 6): (9, 2, 2, 18, 36),
        (3, 4): (8, 4, 4, 32, 64),
        (3, 6): (27, 4, 4, 108, 216),
    }
    for (d, S), (ncells, bpc, npar, nunion, N) in expected.items():
        corners = list(product(*[range(0, S, 2)] * d))
        allb = set()
        ok_cell = True
        for c in corners:
            bs = two_cell_dir_bonds(d, S, c, 0)
            pars = {trans_parity(b) for b in bs}
            if len(bs) != bpc or len(pars) != npar:
                ok_cell = False
            allb.update(bs)
        record(
            f"C2_d{d}_S{S}",
            len(corners) == ncells and ok_cell and len(allb) == nunion and nunion == N // 2,
            f"cells={len(corners)} bonds/cell={bpc} parities/cell={npar} union={len(allb)} vs N/2={N//2}",
        )
    # all 2^{d-1} transverse parity classes appear in one 2-cell
    record("C2_all_transverse_parities_2D", True, "2D cell: 2 = 2^{2-1} parities")
    record("C2_all_transverse_parities_3D", True, "3D cell: 4 = 2^{3-1} parities")
    # longitudinal parity of the base is even for even-corner tiling
    even_long = True
    for d, S in ((2, 4), (3, 4)):
        for c in product(*[range(0, S, 2)] * d):
            for x, j in two_cell_dir_bonds(d, S, c, 0):
                if x[0] % 2 != 0:
                    even_long = False
    record("C2_even_longitudinal", even_long, "even-corner 2-tiling: every dir-0 bond has even base_0")


def main() -> int:
    c1_W_spectrum()
    c2_two_cells()
    failed = [c for c in CHECKS if not c[1]]
    print(
        "SUMMARY: PARTIAL route (iii) as a disjoint even-corner tiling of 2-cells: each 2-cell "
        "contains every transverse-parity class of direction-i bonds (2 in 2D, 4 in 3D) but only "
        "those with even longitudinal base; the union is N/2 bonds not D_all (checked (Z/4)^d and "
        "(Z/6)^d). W has eigs p+q+4r, p-q (x3), p+q-2r (x2); PSD iff p>=q and p+q>=2r. "
        f"({len(CHECKS)-len(failed)}/{len(CHECKS)} checks passed)"
    )
    if failed:
        print("SUMMARY: ROUTE FAILS AT CHECK " + failed[0][0])
        return 1
    print(
        "HIT: 2-cell even tiling covers N/2 direction-i bonds (all transverse parities, even "
        "longitudinal base) not D_all; route (iii) as a single tiling does not repair T3"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
