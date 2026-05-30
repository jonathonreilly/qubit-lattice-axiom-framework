#!/usr/bin/env python3
"""Exact-rational audit-companion runner for the V=1 SU(3) Wilson Picard-Fuchs
ODE rank-exclusion narrow theorem note at the (r=2, d=12) cell:
`PLAQUETTE_V1_PICARD_FUCHS_ODE_RANK_EXCLUSION_R2_D12_NARROW_THEOREM_NOTE_2026-05-17.md`.

The parent minimality-proof companion runner
`scripts/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.py` runs the
lower-order exclusion certificate (B) at Taylor depth ORDER=40. The audit
verdict on its parent claim
`plaquette_v1_picard_fuchs_ode_minimality_proof_note_2026-05-06` is
`audited_conditional` because, at ORDER=40, the (r=2, d=12) cell has
39 unknowns but only `min(num_unknowns+8, ORDER-r-2) = min(47, 36) = 36`
equations available, so the matching matrix is silently skipped while the
load-bearing prose still asserts "rank equals number of unknowns for every
tested (r,d) in {1,2} x {0,...,12}". The (r=2, d=12) exclusion is therefore
not actually computed at the depth used by that runner.

This narrow audit-companion runner closes only the (r=2, d=12) cell:

  (R12) BUMP TAYLOR DEPTH AND RE-VERIFY THE RANK AT (r=2, d=12)
        Build the Bessel-determinant Taylor series J(beta) to ORDER=48 in
        exact rational arithmetic. At ORDER=48, num_eqs available is
        min(num_unknowns+8, ORDER-r-2) = min(47, 44) = 44, which exceeds
        num_unknowns=39, so the matching matrix is full size. Compute the
        rank via exact Fraction Gaussian elimination and verify
        rank == num_unknowns (equivalently kernel_dim == 0).

  (R12B) CROSS-CHECK AT ORDER=52
         Repeat the rank check at ORDER=52 (num_eqs=47) to confirm
         stability of the conclusion under increased depth.

  (R10) RE-CONFIRM (r=2, d=10) AT NEW DEPTH
        At ORDER=40, the (r=2, d=10) cell has 33 unknowns and 36 equations
        (legitimately passing). Re-confirm that the rank is still 33 (no
        kernel) at the bumped ORDER=48.

  (R11) RE-CONFIRM (r=2, d=11) AT NEW DEPTH
        At ORDER=40, the (r=2, d=11) cell has 36 unknowns and exactly 36
        equations (legitimately passing, but with no slack). Re-confirm
        that the rank is still 36 (no kernel) at the bumped ORDER=48 with
        more slack (44 equations vs 36 unknowns).

  (S1) NUM_EQS BOOKKEEPING AT ORDER=40 ARITHMETICALLY MATCHES THE AUDIT
       Explicitly compute the runner-internal `num_eqs` cap at ORDER=40
       for each (r=2, d) cell and confirm the cap is < num_unknowns
       exactly at d=12 (the audit's specific complaint).

  (S2) SAFETY MARGIN CONFIRMED AT ORDER=48
       Confirm `num_eqs >= num_unknowns + 5` for every (r=1..2, d=0..12)
       cell at ORDER=48, so the rank check has uniform headroom in the
       narrow window covered by this note.

This is a Pattern A narrow-rescope audit-companion. It does not:
  - alter the parent minimality-proof note,
  - modify the parent's runner,
  - claim all-order minimality (deeper bridge addressed by the
    `PLAQUETTE_V1_PICARD_FUCHS_ODE_ALL_ORDER_PROOF_NOTE_2026-05-09.md`
    row, audited separately),
  - promote the candidate operator's status.

It only verifies, in exact rational arithmetic, that the audit's specific
arithmetic complaint about the (r=2, d=12) cell is closed by bumping the
Taylor depth, without altering the candidate operator or any retained
upstream authority.
"""
from __future__ import annotations

from fractions import Fraction
import json
import sys
from pathlib import Path


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
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


# ---------------------------------------------------------------------------
# Bessel-determinant Taylor series build (pure Python Fraction polynomials).
# ---------------------------------------------------------------------------

def I_series_dict(n: int, order: int) -> dict:
    """Return the Taylor series of I_n(beta/3) in beta truncated at `order`
    as a {power: Fraction} dict (omitting zero coefficients).

      I_n(z) = sum_{m>=0} (z/2)^(n+2m) / (m! (n+m)!)
      With z = beta/3:
        I_n(beta/3) = sum_{m>=0} beta^(n+2m) / (6^(n+2m) m! (n+m)!).
    """
    n = abs(n)
    out = {}
    m = 0
    while n + 2 * m <= order:
        denom = 6 ** (n + 2 * m)
        for x in range(1, m + 1):
            denom *= x
        for x in range(1, n + m + 1):
            denom *= x
        out[n + 2 * m] = Fraction(1, denom)
        m += 1
    return out


def poly_add(a: dict, b: dict, order: int) -> dict:
    out = {k: v for k, v in a.items()}
    for k, v in b.items():
        if k > order:
            continue
        if k in out:
            new = out[k] + v
            if new == 0:
                del out[k]
            else:
                out[k] = new
        else:
            out[k] = v
    return out


def poly_sub(a: dict, b: dict, order: int) -> dict:
    out = {k: v for k, v in a.items()}
    for k, v in b.items():
        if k > order:
            continue
        if k in out:
            new = out[k] - v
            if new == 0:
                del out[k]
            else:
                out[k] = new
        else:
            out[k] = -v
    return out


def poly_mul(a: dict, b: dict, order: int) -> dict:
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            kk = ka + kb
            if kk > order:
                continue
            term = va * vb
            if kk in out:
                new = out[kk] + term
                if new == 0:
                    del out[kk]
                else:
                    out[kk] = new
            else:
                out[kk] = term
    return out


def det3x3_dict(M, order: int) -> dict:
    """Exact 3x3 determinant where each entry is a {power: Fraction} dict."""
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    ei = poly_mul(e, i, order)
    fh = poly_mul(f, h, order)
    ei_fh = poly_sub(ei, fh, order)
    a_ei_fh = poly_mul(a, ei_fh, order)

    di = poly_mul(d, i, order)
    fg = poly_mul(f, g, order)
    di_fg = poly_sub(di, fg, order)
    b_di_fg = poly_mul(b, di_fg, order)

    dh = poly_mul(d, h, order)
    eg = poly_mul(e, g, order)
    dh_eg = poly_sub(dh, eg, order)
    c_dh_eg = poly_mul(c, dh_eg, order)

    res = poly_sub(a_ei_fh, b_di_fg, order)
    res = poly_add(res, c_dh_eg, order)
    return res


def build_J_coeffs(order: int) -> list:
    """Compute the Bessel-determinant Taylor series

      J(beta) = sum_{k in Z} det[I_{i-j+k}(beta/3)]_{i,j=0,1,2}

    truncated to total degree `order`, returning the list of exact Fraction
    coefficients [a_0, a_1, ..., a_order].
    """
    k_max = order // 3 + 2
    J_total = {}
    for k in range(-k_max, k_max + 1):
        rows = [[I_series_dict(i - j + k, order) for j in range(3)] for i in range(3)]
        d = det3x3_dict(rows, order)
        J_total = poly_add(J_total, d, order)
    coeffs = [Fraction(0)] * (order + 1)
    for p, c in J_total.items():
        coeffs[p] = c
    return coeffs


# ---------------------------------------------------------------------------
# Rank-of-matching-matrix at the (r, d) ansatz over the Taylor coefficients.
# ---------------------------------------------------------------------------

def matrix_for_ansatz(coeffs: list, r: int, d: int, num_eqs: int):
    """Build the matching matrix for the ansatz

      sum_{k=0..r} sum_{m=0..d} p_{k,m} beta^m J^{(k)}(beta)  =  0,

    matched against the coefficient of beta^N for N = 0, 1, ..., num_eqs-1.

    Returns (rows, num_unknowns).
    """
    num_unknowns = (r + 1) * (d + 1)
    rows = []
    for N in range(num_eqs):
        row = [Fraction(0)] * num_unknowns
        skip = False
        for k in range(r + 1):
            for m in range(d + 1):
                if N - m < 0:
                    continue
                j = N - m
                if j + k >= len(coeffs):
                    skip = True
                    break
                factor = 1
                for ell in range(k):
                    factor *= (j + k - ell)
                idx = k * (d + 1) + m
                row[idx] = Fraction(factor) * coeffs[j + k]
            if skip:
                break
        if not skip:
            rows.append(row)
    return rows, num_unknowns


def rank_exact(rows) -> int:
    """Exact Gaussian elimination over Fraction; returns rank."""
    if not rows:
        return 0
    rows = [list(r) for r in rows]
    nrows = len(rows)
    ncols = len(rows[0])
    rk = 0
    pivot_col = 0
    r_idx = 0
    while r_idx < nrows and pivot_col < ncols:
        sel = -1
        for i in range(r_idx, nrows):
            if rows[i][pivot_col] != 0:
                sel = i
                break
        if sel == -1:
            pivot_col += 1
            continue
        rows[r_idx], rows[sel] = rows[sel], rows[r_idx]
        piv = rows[r_idx][pivot_col]
        for i in range(r_idx + 1, nrows):
            if rows[i][pivot_col] != 0:
                factor = rows[i][pivot_col] / piv
                for j in range(pivot_col, ncols):
                    rows[i][j] -= factor * rows[r_idx][j]
        rk += 1
        pivot_col += 1
        r_idx += 1
    return rk


def num_eqs_for(order: int, r: int, num_unknowns: int) -> int:
    """The original runner's (line 357) cap is min(num_unknowns + 8, depth - r - 2)
    where `depth` is the Taylor truncation order.
    """
    return min(num_unknowns + 8, order - r - 2)


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-rational) for")
    print("PLAQUETTE_V1_PICARD_FUCHS_ODE_RANK_EXCLUSION_R2_D12_NARROW_THEOREM_NOTE_2026-05-17")
    print()
    print("Goal: re-verify the (r=2, d=12) lower-order exclusion cell at bumped")
    print("Taylor depth (ORDER=48 and ORDER=52) so that num_eqs >= num_unknowns")
    print("for the matching matrix, closing the audit's arithmetic complaint")
    print("about the original ORDER=40 cap of 36 < 39 unknowns at that cell.")
    print("=" * 88)

    # ---------------------------------------------------------------------
    section("Part 0: arithmetic bookkeeping at ORDER=40 reproduces the audit's complaint")
    # ---------------------------------------------------------------------
    # At ORDER=40, r=2, d=12: num_unknowns = 39, num_eqs cap = min(47, 36) = 36 < 39.
    r = 2
    d = 12
    num_unknowns_target = (r + 1) * (d + 1)  # 39
    cap40 = num_eqs_for(40, r, num_unknowns_target)
    check(
        "[S1] num_unknowns at (r=2, d=12) is 39",
        num_unknowns_target == 39,
        detail=f"num_unknowns = (r+1)(d+1) = 3*13 = {num_unknowns_target}",
    )
    check(
        "[S1] At ORDER=40 the cap is 36, strictly less than num_unknowns=39",
        cap40 == 36 and cap40 < num_unknowns_target,
        detail=(
            f"min(num_unknowns + 8, ORDER - r - 2) = min({num_unknowns_target + 8}, {40 - r - 2}) "
            f"= {cap40}"
        ),
    )
    # And for all other tested d in {0,...,11}, the cap >= num_unknowns at ORDER=40
    print("    Per-cell cap at ORDER=40 for r=2:")
    short_cells_ok_at_40 = True
    for d_chk in range(11 + 1):
        u = 3 * (d_chk + 1)
        c = num_eqs_for(40, 2, u)
        ok = c >= u
        if not ok:
            short_cells_ok_at_40 = False
        print(f"      (r=2, d={d_chk}): unknowns={u}, cap={c} -> {'OK' if ok else 'SHORT'}")
    check(
        "[S1] Cells (r=2, d in {0,...,11}) at ORDER=40 each have cap >= num_unknowns",
        short_cells_ok_at_40,
        detail="exactly d=12 is the cell short of equations at ORDER=40",
    )

    # ---------------------------------------------------------------------
    section("Part 1: bumped Taylor depth ORDER=48 — confirm num_eqs >= num_unknowns")
    # ---------------------------------------------------------------------
    cap48_target = num_eqs_for(48, r, num_unknowns_target)
    check(
        "[S2] At ORDER=48 the (r=2, d=12) cap is 44, which exceeds num_unknowns=39",
        cap48_target >= num_unknowns_target and cap48_target == 44,
        detail=(
            f"min(num_unknowns + 8, ORDER - r - 2) = min({num_unknowns_target + 8}, {48 - r - 2}) "
            f"= {cap48_target}"
        ),
    )

    # Confirm every (r=1..2, d=0..12) cell has at least 5 slack equations at ORDER=48.
    all_slack_ok = True
    for r_chk in (1, 2):
        for d_chk in range(13):
            u = (r_chk + 1) * (d_chk + 1)
            c = num_eqs_for(48, r_chk, u)
            if c < u + 5:
                all_slack_ok = False
    check(
        "[S2] All cells (r in {1,2}, d in {0,...,12}) at ORDER=48 have num_eqs >= num_unknowns + 5",
        all_slack_ok,
        detail="uniform headroom of at least 5 across the narrow window of this note",
    )

    # ---------------------------------------------------------------------
    section("Part 2: build J(beta) Taylor coefficients to ORDER=48 (exact rationals)")
    # ---------------------------------------------------------------------
    coeffs48 = build_J_coeffs(48)
    print(f"    a_0 = {coeffs48[0]}")
    print(f"    a_2 = {coeffs48[2]}")
    print(f"    a_4 = {coeffs48[4]}")
    print(f"    a_10 = {coeffs48[10]}")
    check(
        "[J0] a_0 == 1 (normalization J(0) = 1)",
        coeffs48[0] == Fraction(1),
        detail=f"a_0 = {coeffs48[0]}",
    )
    check(
        "[J2] a_2 == 1/36 (known SU(3) lowest-nontrivial Bessel-det coefficient)",
        coeffs48[2] == Fraction(1, 36),
        detail=f"a_2 = {coeffs48[2]}",
    )

    # ---------------------------------------------------------------------
    section("Part 3: [R12] rank check at (r=2, d=12), ORDER=48")
    # ---------------------------------------------------------------------
    M48, num_unknowns = matrix_for_ansatz(coeffs48, r=2, d=12, num_eqs=44)
    print(f"    matching matrix: {len(M48)} rows x {num_unknowns} columns")
    rk48 = rank_exact(M48)
    kernel_dim_48 = num_unknowns - rk48
    check(
        "[R12] At ORDER=48 the (r=2, d=12) matching matrix has rank == num_unknowns",
        rk48 == num_unknowns,
        detail=f"rank = {rk48}, num_unknowns = {num_unknowns}, kernel_dim = {kernel_dim_48}",
    )
    check(
        "[R12] At ORDER=48 the (r=2, d=12) ansatz kernel is empty (no annihilator)",
        kernel_dim_48 == 0,
        detail=f"kernel_dim = {kernel_dim_48}",
    )

    # ---------------------------------------------------------------------
    section("Part 4: [R10] and [R11] re-confirm at the bumped depth")
    # ---------------------------------------------------------------------
    # (r=2, d=10): 33 unknowns. At ORDER=48 the cap is min(41, 44) = 41, full size.
    u10 = 3 * 11
    c10 = num_eqs_for(48, 2, u10)
    M10, _ = matrix_for_ansatz(coeffs48, r=2, d=10, num_eqs=c10)
    rk10 = rank_exact(M10)
    kd10 = u10 - rk10
    check(
        "[R10] At ORDER=48 the (r=2, d=10) matching matrix has rank == num_unknowns",
        rk10 == u10,
        detail=f"rank = {rk10}, num_unknowns = {u10}, kernel_dim = {kd10}",
    )

    # (r=2, d=11): 36 unknowns. At ORDER=40 there were exactly 36 equations
    # (no slack); confirm slack is now positive at ORDER=48.
    u11 = 3 * 12
    c11 = num_eqs_for(48, 2, u11)
    M11, _ = matrix_for_ansatz(coeffs48, r=2, d=11, num_eqs=c11)
    rk11 = rank_exact(M11)
    kd11 = u11 - rk11
    check(
        "[R11] At ORDER=48 the (r=2, d=11) matching matrix has rank == num_unknowns",
        rk11 == u11,
        detail=f"rank = {rk11}, num_unknowns = {u11}, kernel_dim = {kd11}, slack = {c11 - u11}",
    )

    # ---------------------------------------------------------------------
    section("Part 5: [R12B] cross-check at ORDER=52 (stability under depth)")
    # ---------------------------------------------------------------------
    coeffs52 = build_J_coeffs(52)
    check(
        "[J0-52] a_0 == 1 (re-normalized at ORDER=52)",
        coeffs52[0] == Fraction(1),
        detail=f"a_0 = {coeffs52[0]}",
    )
    check(
        "[J2-52] a_2 == 1/36 (re-normalized at ORDER=52)",
        coeffs52[2] == Fraction(1, 36),
        detail=f"a_2 = {coeffs52[2]}",
    )
    cap52 = num_eqs_for(52, 2, num_unknowns_target)
    M52, _ = matrix_for_ansatz(coeffs52, r=2, d=12, num_eqs=cap52)
    rk52 = rank_exact(M52)
    kernel_dim_52 = num_unknowns_target - rk52
    check(
        "[R12B] At ORDER=52 the (r=2, d=12) matching matrix has rank == num_unknowns",
        rk52 == num_unknowns_target,
        detail=f"rank = {rk52}, num_unknowns = {num_unknowns_target}, kernel_dim = {kernel_dim_52}",
    )
    check(
        "[R12B] Conclusion is stable under increasing Taylor depth (ORDER=48 and ORDER=52 agree)",
        kernel_dim_52 == kernel_dim_48 == 0,
        detail="both ORDER values yield kernel_dim = 0 at (r=2, d=12)",
    )

    # ---------------------------------------------------------------------
    section("Part 6: bookkeeping write-out")
    # ---------------------------------------------------------------------
    out_dir = Path("outputs")
    out_dir.mkdir(exist_ok=True)
    out_path = (
        out_dir / "audit_companion_plaquette_v1_picard_fuchs_ode_rank_exclusion_r2_d12_narrow_2026_05_17.json"
    )
    payload = {
        "claim_id": (
            "plaquette_v1_picard_fuchs_ode_rank_exclusion_r2_d12_narrow_theorem_note_2026-05-17"
        ),
        "parent_minimality_claim_id": (
            "plaquette_v1_picard_fuchs_ode_minimality_proof_note_2026-05-06"
        ),
        "audited_complaint": (
            "ORDER=40 gives only 36 usable equations for 39 unknowns at (r=2, d=12); "
            "the cell is silently skipped while the prose asserts exclusion holds."
        ),
        "narrow_resolution": (
            "Bump Taylor depth to ORDER=48 (and cross-check at ORDER=52). At ORDER=48 "
            "num_eqs = min(num_unknowns + 8, ORDER - r - 2) = min(47, 44) = 44 > 39 = num_unknowns, "
            "so the matching matrix is full size at the cell. Exact-rational rank check returns "
            "rank = num_unknowns = 39, hence kernel is empty and the (r=2, d=12) exclusion holds."
        ),
        "results": {
            "ORDER=40 (r=2, d=12) num_eqs_cap": cap40,
            "ORDER=40 (r=2, d=12) num_unknowns": num_unknowns_target,
            "ORDER=48 (r=2, d=12) num_eqs_cap": cap48_target,
            "ORDER=48 (r=2, d=12) rank": rk48,
            "ORDER=48 (r=2, d=12) kernel_dim": kernel_dim_48,
            "ORDER=48 (r=2, d=10) rank": rk10,
            "ORDER=48 (r=2, d=10) kernel_dim": kd10,
            "ORDER=48 (r=2, d=11) rank": rk11,
            "ORDER=48 (r=2, d=11) kernel_dim": kd11,
            "ORDER=52 (r=2, d=12) rank": rk52,
            "ORDER=52 (r=2, d=12) kernel_dim": kernel_dim_52,
        },
        "summary": {
            "pass": PASS,
            "fail": FAIL,
            "audit_status_authority": "independent audit lane only",
        },
    }
    with out_path.open("w") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")
    print(f"    Output written: {out_path}")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
