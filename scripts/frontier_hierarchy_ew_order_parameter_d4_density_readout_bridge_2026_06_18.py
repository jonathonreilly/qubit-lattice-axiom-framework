#!/usr/bin/env python3
"""EW order-parameter D=4 density readout bridge (bounded support).

Verifies the finite algebra behind one narrow source-side bridge for the
hierarchy dimensional-compression blocker: the defined neutral vector
coordinate v is the positive fourth-root coordinate of a positive quartic D=4
density, and holding that density fixed relates two endpoint coefficients by an
inverse fourth root.

Every step is exact rational arithmetic except the two real-root witnesses in
S2 (a genuine fourth root and a sixteenth root); those are floats and are
reported with measured residuals against the density equation itself, so the
negative controls are separations in the equation rather than in a label.

It does not derive the hierarchy endpoint coefficient surface, the absolute
EW scale, M_Pl, alpha_LM, or any observed value.

The section check counts below are mirrored in the paired note's Scorecard.
S5 is the gate holding the note's declared verification total and this runner's
actual check count in agreement; it must remain the final check.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "HIERARCHY_EW_ORDER_PARAMETER_D4_DENSITY_READOUT_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md"
)
PARENT_NOTE_PATH = ROOT / "docs" / "HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md"

AUDIT_INPUT_PATHS = (
    "docs/HIERARCHY_EW_ORDER_PARAMETER_D4_DENSITY_READOUT_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md",
    "docs/HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md",
)

SECTION_ORDER = ("S1", "S2", "S3", "S4", "S5")
SECTION_TITLES = {
    "S1": "order-parameter coordinate",
    "S2": "fixed-density fourth-root law",
    "S3": "formal scalar-readout compatibility",
    "S4": "source firewalls",
    "S5": "verification-total consistency",
}

PASS_COUNT = 0
FAIL_COUNT = 0
SECTION_COUNTS = {key: 0 for key in SECTION_ORDER}
CURRENT_SECTION = SECTION_ORDER[0]


def section(key: str) -> None:
    global CURRENT_SECTION
    CURRENT_SECTION = key
    print(f"\n{key} {SECTION_TITLES[key]}")


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    SECTION_COUNTS[CURRENT_SECTION] += 1
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{'PASS' if condition else 'FAIL'}] {name}")
    if detail:
        print(f"         {detail}")


def q_readout(v: Fraction) -> Fraction:
    """q(H) = 2 H^dagger H for the neutral vector H(v) = (0, v/sqrt(2))^T.

    The 1/sqrt(2) normalization squares to 1/2, so H^dagger H = (0^2 + v^2)/2
    stays exact in Fractions and q = 2 H^dagger H = v^2.
    """
    upper = Fraction(0)
    h_dagger_h = (upper * upper + v * v) / 2
    return 2 * h_dagger_h


def quartic_density(coeff: Fraction, v: Fraction) -> Fraction:
    """rho_* = A q(H(v))^2, built from the readout q rather than from v^4."""
    q = q_readout(v)
    return coeff * q * q


def positive_fourth_root(x: Fraction) -> Fraction | None:
    """Exact positive rational fourth root of x, or None when it is irrational.

    The candidate is taken from a float estimate and then CONFIRMED by exact
    exponentiation, so a wrong estimate returns None rather than an approximation.
    """
    if x <= 0:
        return None
    num = int(round(float(x.numerator) ** 0.25))
    den = int(round(float(x.denominator) ** 0.25))
    for n in (num - 1, num, num + 1):
        for d in (den - 1, den, den + 1):
            if n > 0 and d > 0 and Fraction(n, d) ** 4 == x:
                return Fraction(n, d)
    return None


def endpoint_coefficients(u0_sq: Fraction) -> tuple[Fraction, Fraction]:
    """Supplied endpoint quartic coefficients A_2 = 1/(8 u0^2), A_4 = 1/(7 u0^2)."""
    return Fraction(1, 8) / u0_sq, Fraction(1, 7) / u0_sq


def formal_readouts(g: Fraction, g_y: Fraction, v: Fraction):
    """Formal scalar labels of the defined quadratic form. No observed input."""
    mw_sq = g * g * v * v / 4
    mz_sq = (g * g + g_y * g_y) * v * v / 4
    cos_sq = g * g / (g * g + g_y * g_y)
    return mw_sq, mz_sq, mw_sq / (mz_sq * cos_sq)


def parse_note_scorecard(note: str) -> tuple[dict[str, tuple[str, int]], int | None]:
    """Read the paired note's Scorecard table: section key -> (label, declared checks)."""
    declared: dict[str, tuple[str, int]] = {}
    if "## Scorecard" not in note:
        return declared, None
    body = note.split("## Scorecard", 1)[1].split("\n## ", 1)[0]
    for line in body.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 3 or not cells[2].isdigit():
            continue
        head = re.match(r"^(S[1-5])\s+(.+)$", cells[0])
        if head:
            declared[head.group(1)] = (head.group(2).strip(), int(cells[2]))
    totals = re.findall(r"TOTAL: PASS=(\d+) FAIL=(\d+)", body)
    return declared, int(totals[0][0]) if totals else None


def main() -> int:
    print("Hierarchy EW order-parameter D=4 density readout bridge")
    print("=" * 78)

    # ---------------------------------------------------------------- S1
    section("S1")
    v_grid = [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1),
              Fraction(3, 2), Fraction(5, 3), Fraction(9, 2)]
    a_grid = [Fraction(1, 8), Fraction(1, 7), Fraction(7, 11), Fraction(3), Fraction(20, 3)]
    v = Fraction(3, 2)
    coeff = Fraction(7, 11)

    q_ok = all(q_readout(w) == w * w for w in v_grid)
    check(
        "q = 2 H^dagger H = v^2 for the neutral vector H(v), over a rational grid",
        q_ok,
        f"{len(v_grid)} values of v; sample v={v}: q={q_readout(v)}, v^2={v * v}",
    )

    rho = quartic_density(coeff, v)
    density_ok = all(
        quartic_density(a, w) == a * w**4 and quartic_density(a, w) > 0
        for a in a_grid
        for w in v_grid
    )
    check(
        "positive quartic density is exactly rho_* = A v^4 > 0, over an (A, v) grid",
        density_ok,
        f"{len(a_grid)}x{len(v_grid)} pairs; sample rho_*={rho}, A v^4={coeff * v**4}",
    )

    monotonic_factorization_ok = all(
        coeff * (v_grid[i + 1] ** 4 - v_grid[i] ** 4)
        == coeff
        * (v_grid[i + 1] - v_grid[i])
        * (v_grid[i + 1] + v_grid[i])
        * (v_grid[i + 1] ** 2 + v_grid[i] ** 2)
        > 0
        for i in range(len(v_grid) - 1)
    )
    check(
        "the strict-monotonicity factorization is positive for A>0 and 0<x<y",
        monotonic_factorization_ok,
        f"A(y^4-x^4)=A(y-x)(y+x)(y^2+x^2)>0 on {len(v_grid) - 1} exact rational pairs",
    )

    recovered = positive_fourth_root(rho / coeff)
    grid_recovered = all(
        positive_fourth_root(quartic_density(a, w) / a) == w for a in a_grid for w in v_grid
    )
    check(
        "the unique positive coordinate is recovered exactly as the fourth root of rho_*/A",
        recovered == v and grid_recovered,
        f"root(rho_*/A)={recovered}, v={v}; recovery exact on all {len(a_grid) * len(v_grid)} pairs",
    )

    check(
        "positivity of v is load-bearing: v -> A v^4 is NOT injective on all of R",
        quartic_density(coeff, -v) == rho and -v != v,
        f"rho_*(-v)={quartic_density(coeff, -v)} equals rho_*(v)={rho}; v > 0 selects the branch",
    )

    # ---------------------------------------------------------------- S2
    section("S2")
    u0_grid = [Fraction(1), Fraction(2, 5), Fraction(9, 4), Fraction(13, 7)]
    ratios = {endpoint_coefficients(u)[0] / endpoint_coefficients(u)[1] for u in u0_grid}
    a_ref, a_l = endpoint_coefficients(Fraction(1))
    check(
        "endpoint coefficient ratio A_ref/A_L = 7/8, independent of the common u0^2",
        ratios == {Fraction(7, 8)},
        f"A_2=1/(8u0^2), A_4=1/(7u0^2); ratio={ratios.pop()} for all {len(u0_grid)} values of u0^2",
    )

    # Exact witness: a coefficient pair whose ratio is a perfect fourth power,
    # so the fixed-density solve closes in exact rational arithmetic.
    ex_ref, ex_l = Fraction(16), Fraction(81)
    ex_v_ref = Fraction(1)
    ex_v_l = positive_fourth_root(ex_ref / ex_l)
    ex_rho_ref = quartic_density(ex_ref, ex_v_ref)
    ex_rho_l = quartic_density(ex_l, ex_v_l * ex_v_ref)
    check(
        "exact witness: solving A_ref v_ref^4 = A_L v_L^4 gives (v_L/v_ref)^4 = A_ref/A_L",
        ex_v_l == Fraction(2, 3)
        and ex_rho_ref == ex_rho_l
        and ex_v_l**4 == ex_ref / ex_l,
        f"A_ref/A_L={ex_ref / ex_l}, v_L/v_ref={ex_v_l}, rho_*={ex_rho_ref}={ex_rho_l} (exact)",
    )

    # Endpoint solve at the actual 7/8 ratio: the fourth root is irrational here,
    # so the density equation is closed numerically and the residual is measured.
    v_ref = 5.0
    target_rho = float(a_ref) * v_ref**4
    x_true = float(a_ref / a_l) ** 0.25
    v_l = x_true * v_ref
    resid_true = abs(float(a_l) * v_l**4 - target_rho) / target_rho
    check(
        "endpoint solve at A_ref/A_L = 7/8 reproduces the fixed density to machine precision",
        resid_true < 1e-15 and abs(x_true**4 - 7 / 8) < 1e-15 and v_l < v_ref,
        f"v_L/v_ref={x_true:.12f}, density residual={resid_true:.2e}, A_L>A_ref so v_L<v_ref",
    )

    x_flip = float(a_l / a_ref) ** 0.25
    resid_flip = abs(float(a_l) * (x_flip * v_ref) ** 4 - target_rho) / target_rho
    x_d16 = float(a_ref / a_l) ** (1 / 16)
    resid_d16 = abs(float(a_l) * (x_d16 * v_ref) ** 4 - target_rho) / target_rho
    check(
        "wrong-direction and D=16 exponents both MISS the same fixed density by a wide margin",
        resid_flip > 0.05 and resid_d16 > 0.05,
        f"(A_L/A_ref)^(1/4): residual={resid_flip:.4f}; (A_ref/A_L)^(1/16): residual={resid_d16:.4f}",
    )

    # ---------------------------------------------------------------- S3
    section("S3")
    coupling_grid = [
        (Fraction(3), Fraction(4)),
        (Fraction(1), Fraction(1)),
        (Fraction(5), Fraction(2)),
        (Fraction(8), Fraction(11)),
    ]
    rho_tree_ok = all(
        formal_readouts(g, g_y, w)[2] == 1 for (g, g_y) in coupling_grid for w in v_grid
    )
    g0, g_y0 = coupling_grid[0]
    check(
        "formal rho readout stays exactly one at every coupling pair and every v",
        rho_tree_ok,
        f"{len(coupling_grid)}x{len(v_grid)} cases; sample g={g0}, gY={g_y0}: rho_tree="
        f"{formal_readouts(g0, g_y0, v)[2]}",
    )

    # (sqrt(MW2_L)/sqrt(MW2_ref))^4 = (MW2_L/MW2_ref)^2 for positive square roots,
    # so the note's displayed readout ratio is COMPUTED here, not restated.
    mw_ref, mz_ref, _ = formal_readouts(g0, g_y0, ex_v_ref)
    mw_l, mz_l, _ = formal_readouts(g0, g_y0, ex_v_l * ex_v_ref)
    check(
        "formal readout ratios carry the same fourth power: (MW2_L/MW2_ref)^2 = A_ref/A_L",
        (mw_l / mw_ref) ** 2 == ex_ref / ex_l and (mz_l / mz_ref) ** 2 == ex_ref / ex_l,
        f"(MW2_L/MW2_ref)^2={(mw_l / mw_ref) ** 2}, (MZ2_L/MZ2_ref)^2={(mz_l / mz_ref) ** 2}, "
        f"A_ref/A_L={ex_ref / ex_l}",
    )

    coupling_free = True
    for g, g_y in coupling_grid:
        w_ref, z_ref, _ = formal_readouts(g, g_y, ex_v_ref)
        w_l, z_l, _ = formal_readouts(g, g_y, ex_v_l * ex_v_ref)
        coupling_free = coupling_free and (w_l / w_ref) ** 2 == ex_ref / ex_l
        coupling_free = coupling_free and (z_l / z_ref) ** 2 == ex_ref / ex_l
    check(
        "that ratio is independent of (g, gY): no coupling-valued prefactor enters",
        coupling_free,
        f"identical fourth power {ex_ref / ex_l} at all {len(coupling_grid)} coupling pairs",
    )

    # ---------------------------------------------------------------- S4
    section("S4")
    note = NOTE_PATH.read_text(encoding="utf-8")
    parent = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    parent_flat = " ".join(parent.split())
    check(
        "bridge carries bounded-support status fields and no retained claim",
        "**Claim type:** bounded_theorem" in note
        and "**Type:** bounded_theorem" in note
        and "bounded support for the EW order-parameter D4 density readout" in note_flat
        and "actual_current_surface_status: bounded-support" in note
        and "trace_class: direct_blocker_closure" in note
        and "reachability_to_target: partially_closes" in note
        and "proposal_allowed: false" in note
        and "bare_retained_allowed: false" in note,
    )
    check(
        "bridge markdown-links load-bearing EW and D4 readout authorities",
        "[`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md)" in note
        and "[`HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md`](HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md)" in note,
    )
    check(
        "bridge explicitly leaves endpoint selection and absolute scale open",
        "does not derive that the hierarchy Matsubara endpoint coefficient is the physical Higgs density" in note_flat
        and "does not derive the absolute EW scale" in note_flat
        and "does not use an observed EW value" in note_flat,
    )
    check(
        "parent note cites the bridge while preserving the residual",
        "HIERARCHY_EW_ORDER_PARAMETER_D4_DENSITY_READOUT_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md" in parent
        and "endpoint-selection residual remains open" in parent_flat
        and "proposal_allowed: false" in parent,
    )

    # ---------------------------------------------------------------- S5
    section("S5")
    declared, declared_total = parse_note_scorecard(note)
    actual = dict(SECTION_COUNTS)
    actual["S5"] = SECTION_COUNTS["S5"] + 1  # this consistency check itself
    final_total = PASS_COUNT + FAIL_COUNT + 1
    note_totals = re.findall(r"TOTAL: PASS=(\d+) FAIL=(\d+)", note)
    labels_ok = all(declared.get(k, ("", -1))[0] == SECTION_TITLES[k] for k in SECTION_ORDER)
    counts_ok = all(declared.get(k, ("", -1))[1] == actual[k] for k in SECTION_ORDER)
    sum_ok = declared_total is not None and declared_total == sum(n for _, n in declared.values())
    # The note must carry the same total in BOTH the Scorecard and the
    # Verification block's Expected fence, and carry no stale total anywhere.
    fences_ok = len(note_totals) >= 2 and all(
        (int(p), int(f)) == (final_total, 0) for p, f in note_totals
    )
    check(
        "note Scorecard, note Expected fence, and this runner's check count all agree",
        labels_ok and counts_ok and sum_ok and declared_total == final_total and fences_ok,
        "declared "
        + ",".join(f"{k}={declared.get(k, ('', -1))[1]}" for k in SECTION_ORDER)
        + f" total={declared_total} | actual "
        + ",".join(f"{k}={actual[k]}" for k in SECTION_ORDER)
        + f" total={final_total} | note TOTAL lines={len(note_totals)}",
    )

    print("\n" + "=" * 78)
    print("per-section: " + "  ".join(f"{k}={SECTION_COUNTS[k]}" for k in SECTION_ORDER))
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        print("VERDICT: FAIL - EW order-parameter D=4 readout bridge needs repair.")
        return 1
    print(
        "VERDICT: bounded support passes for the EW order-parameter D=4 "
        "density readout bridge. Endpoint selection, absolute scale, and "
        "hierarchy-to-physical-Higgs-density identification remain open."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
