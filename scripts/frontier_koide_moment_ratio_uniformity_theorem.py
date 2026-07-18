#!/usr/bin/env python3
"""
Frontier runner - Koide MRU theorem on the conditional SO(2)-quotient carrier.

Companion to `docs/KOIDE_MOMENT_RATIO_UNIFORMITY_THEOREM_NOTE_2026-04-19.md`.

Status note (2026-05-16 substantive repair):
  The original presentation of the SO(2)-quotient on the charged-lepton
  scalar lane as a *derived* object is withdrawn (see
  `docs/KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md` for the Path A failure
  proof: spectrum-native scalar observables tr(H^3) and det(H) carry an
  explicit cos(3 arg b) dependence under b -> e^{i theta} b on
  Herm_circ(3), so the SO(2)-quotient is NOT a corollary of the cited
  observable-principle proposal alone). Here the SO(2)-quotient is an
  explicitly supplied open premise, not a derivation or registry entry.

Load-bearing conditional claim verified here:
  *Given* the supplied SO(2)-quotient premise on the scalar lane, the carrier
  reduces from the unreduced (r_0, r_1, r_2) to the two-slot quotient

      (r_0, r_1, r_2)  ->  (rho_+, rho_perp),

  where

      rho_+^2    = E_+    = r_0^2 / 3,
      rho_perp^2 = E_perp = (r_1^2 + r_2^2) / 6.

  Applying the standard block log-volume / extremal law on this reduced
  carrier forces

      E_+ = E_perp  <=>  a^2 = 2 |b|^2  <=>  kappa = 2 on b != 0.

Independent unconditional fact verified here:
  The doublet radius r_1^2 + r_2^2 is SO(2)-invariant (Section 2.1 of
  the note). This is purely algebraic. It is NOT the load-bearing
  physical claim; the load-bearing claim is the supplied premise that the
  scalar lane observables physically factor through this radius, which
  is logged here as a conditional premise rather than verified.

The same-day obstruction theorem on the unreduced 3x3 determinant carrier
remains true unconditionally; this runner certifies (a) the conditional
quotient-carrier algebra after that premise and (b) the unconditional
algebraic radius-invariance identity.

Adjacent algebra notes do not remove the physical quotient/measure boundary:
  - docs/KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md
    proves only an abstract Fourier polynomial identity;
  - docs/KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md
    leaves the canonical physical scalar-measure choice open.
"""

from __future__ import annotations

import sys

import sympy as sp


ALGEBRA_PASS = 0
ALGEBRA_FAIL = 0
CONDITIONAL_PASS = 0
CONDITIONAL_FAIL = 0
SUPPLIED_PREMISES: list[str] = []


def check(
    label: str,
    cond: bool,
    detail: str = "",
    cls: str = "A",
    *,
    kind: str = "algebra",
) -> None:
    global ALGEBRA_PASS, ALGEBRA_FAIL, CONDITIONAL_PASS, CONDITIONAL_FAIL
    if kind not in {"algebra", "conditional"}:
        raise ValueError(f"unknown check kind: {kind}")
    status = "PASS" if cond else "FAIL"
    if cond:
        if kind == "algebra":
            ALGEBRA_PASS += 1
        else:
            CONDITIONAL_PASS += 1
    else:
        if kind == "algebra":
            ALGEBRA_FAIL += 1
        else:
            CONDITIONAL_FAIL += 1
    print(f"[{cls}/{kind.upper()}] {status}: {label}" + (f"  ({detail})" if detail else ""))


def supply(label: str, detail: str) -> None:
    """Record an open conditional premise without creating a registry entry."""
    SUPPLIED_PREMISES.append(label)
    print(f"[S] SUPPLIED CONDITIONAL PREMISE: {label}")
    print(f"      detail: {detail}")
    print(
        "      see: docs/KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md Section 1.2"
        " for the Path A failure proof showing this is NOT a corollary of"
        " the cited observable-principle proposal on Herm_circ(3)."
    )


def shift_matrix(d: int = 3) -> sp.Matrix:
    rows = []
    for i in range(d):
        row = [0] * d
        row[(i - 1) % d] = 1
        rows.append(row)
    return sp.Matrix(rows)


def real_trace(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.re(sp.trace(a * b.H)))


def cyclic_real_isotype_counts(d: int) -> tuple[int, int]:
    """Derive real singlet/doublet counts from k -> -k on Z/dZ."""
    if d < 2:
        raise ValueError("d must be at least 2")
    residues = set(range(d))
    singlets = {k for k in residues if (-k) % d == k}
    remaining = residues - singlets
    doublets: set[frozenset[int]] = set()
    for k in remaining:
        doublets.add(frozenset((k, (-k) % d)))
    return len(singlets), len(doublets)


def part0_geometry_and_uniqueness() -> None:
    print("\n=== Part 0: d=3 geometry and uniqueness (unconditional) ===")
    c = shift_matrix(3)
    i3 = sp.eye(3)
    b0 = i3
    b1 = c + c**2
    b2 = sp.I * (c - c**2)

    check("||B_0||^2 = 3", sp.simplify(real_trace(b0, b0) - 3) == 0)
    check(
        "||B_1||^2 = ||B_2||^2 = 6",
        sp.simplify(real_trace(b1, b1) - 6) == 0 and sp.simplify(real_trace(b2, b2) - 6) == 0,
    )
    check(
        "B_0, B_1, B_2 are pairwise orthogonal",
        sp.simplify(real_trace(b0, b1)) == 0
        and sp.simplify(real_trace(b0, b2)) == 0
        and sp.simplify(real_trace(b1, b2)) == 0,
    )

    check(
        "d=3 has exactly one singlet and one real doublet",
        cyclic_real_isotype_counts(3) == (1, 1),
    )
    check(
        "d=2 is singlet-singlet only, so no singlet-vs-doublet MRU form",
        cyclic_real_isotype_counts(2) == (2, 0),
    )
    m = sp.symbols("m", integer=True, positive=True)
    odd_total = 1 + (m + 1)  # d=2m+3 >=5: one singlet, m+1 doublets
    even_total = 2 + m  # d=2m+2 >=4: two singlets, m doublets
    derived_scan = all(
        cyclic_real_isotype_counts(d)
        == ((1, (d - 1) // 2) if d % 2 else (2, (d - 2) // 2))
        for d in range(2, 17)
    )
    check(
        "all d>=4 have more than two real isotypes by the parity formulas",
        derived_scan
        and sp.ask(sp.Q.positive(odd_total - 2)) is True
        and sp.ask(sp.Q.positive(even_total - 2)) is True,
    )


def part1_doublet_radius_invariance_and_supplied_premise() -> None:
    print(
        "\n=== Part 1: doublet radius invariance (algebraic) + load-bearing"
        " supplied premise ==="
    )
    print(
        "  Note: the algebraic radius invariance is unconditional and is"
        " NOT what carries the closure. The load-bearing claim is the"
        " supplied physical premise that the scalar charged-lepton lane reads"
        " only the radius and not the angle. It is logged below as conditional"
        " input rather than verified here."
    )

    r1, r2, theta = sp.symbols("r1 r2 theta", real=True)
    r1p = sp.cos(theta) * r1 - sp.sin(theta) * r2
    r2p = sp.sin(theta) * r1 + sp.cos(theta) * r2

    check(
        "The doublet radius r_1^2 + r_2^2 is SO(2)-invariant (algebraic)",
        sp.simplify(sp.expand(r1p**2 + r2p**2 - (r1**2 + r2**2))) == 0,
    )

    expr_noninv = sp.simplify((r1p**2 - r1**2).subs(theta, sp.pi / 3))
    check(
        "A single Cartesian coordinate is NOT invariant under the internal frame rotation",
        sp.simplify(expr_noninv) != 0,
        f"residual={sp.expand(expr_noninv)}",
    )

    x, y = sp.symbols("x y", real=True)
    xp = sp.cos(theta) * x - sp.sin(theta) * y
    yp = sp.sin(theta) * x + sp.cos(theta) * y
    check(
        "|b|^2 is frame-invariant on the non-trivial sector (algebraic)",
        sp.simplify(sp.expand(xp**2 + yp**2 - (x**2 + y**2))) == 0,
    )

    # Explicit counter-evidence: spectrum-native scalar observables on
    # Herm_circ(3) carry an arg(b) dependence and so do NOT factor
    # through (a, |b|) alone. This is what the demotion note's Section 1.2
    # makes precise. We exhibit it directly here so the runner cannot
    # quietly drift back into "SO(2)-quotient is derived".
    a, bmod, bphi = sp.symbols("a bmod bphi", real=True)
    c = shift_matrix(3)
    i3 = sp.eye(3)
    b = bmod * sp.exp(sp.I * bphi)
    H = a * i3 + b * c + sp.conjugate(b) * c**2
    tr_H3 = sp.expand(sp.trace(H * H * H))
    tr_H3_simpl = sp.simplify(sp.re(tr_H3))
    arg_dep = sp.diff(tr_H3_simpl, bphi)
    check(
        "tr(H^3) carries explicit arg(b) dependence on Herm_circ(3)"
        " (i.e. is NOT SO(2)-invariant): d/d(bphi) tr(H^3) != 0",
        sp.simplify(arg_dep) != 0,
        f"d/d(bphi) tr(H^3) = {sp.simplify(arg_dep)}",
        cls="A",
    )

    supply(
        "SO(2)-quotient on the charged-lepton scalar lane.",
        "The note's Section 3 closure depends on the *physical* claim that"
        " the scalar charged-lepton lane reads only the doublet radius"
        " rho_perp^2 = E_perp and erases the SO(2) angle arg(b). The"
        " preceding check exhibits that generic Herm_circ(3) scalar"
        " observables (such as tr(H^3)) do carry arg(b)-dependent"
        " content, so this premise is strictly stronger than"
        " 'scalar observables are spectrum-native' and is not derived"
        " in the restricted packet of this runner. It is not added to any"
        " premise registry.",
    )


def part2_conditional_quotient_carrier() -> None:
    print(
        "\n=== Part 2: conditional two-slot quotient carrier"
        " (uses Part 1 supplied premise) ==="
    )
    r0, r1, r2 = sp.symbols("r0 r1 r2", real=True)
    e_plus = sp.simplify(r0**2 / 3)
    e_perp = sp.simplify((r1**2 + r2**2) / 6)

    check("E_+ = r_0^2 / 3", sp.simplify(e_plus - r0**2 / 3) == 0, kind="conditional")
    check("E_perp = (r_1^2 + r_2^2) / 6", sp.simplify(e_perp - (r1**2 + r2**2) / 6) == 0, kind="conditional")

    theta = sp.symbols("theta", real=True)
    r1p = sp.cos(theta) * r1 - sp.sin(theta) * r2
    r2p = sp.sin(theta) * r1 + sp.cos(theta) * r2
    e_perp_rot = sp.simplify((r1p**2 + r2p**2) / 6)
    check("E_perp is constant on SO(2) orbits of the supplied quotient", sp.simplify(e_perp_rot - e_perp) == 0, kind="conditional")

    a, x, y = sp.symbols("a x y", real=True)
    e_plus_ab = sp.simplify(e_plus.subs(r0, 3 * a))
    e_perp_ab = sp.simplify(e_perp.subs({r1: 6 * x, r2: 6 * y}))
    check("In circulant variables E_+ = 3 a^2", sp.simplify(e_plus_ab - 3 * a**2) == 0, kind="conditional")
    check("In circulant variables E_perp = 6 |b|^2", sp.simplify(e_perp_ab - 6 * (x**2 + y**2)) == 0, kind="conditional")

    b_abs_sq = sp.symbols("b_abs_sq", positive=True, real=True)
    kappa_expr = a**2 / b_abs_sq
    e_plus_domain = 3 * a**2
    e_perp_domain = 6 * b_abs_sq
    check(
        "kappa is a quotient-carrier function of (E_+, E_perp): kappa = 2 E_+ / E_perp",
        sp.simplify(kappa_expr - 2 * e_plus_domain / e_perp_domain) == 0,
        kind="conditional",
    )


def part3_reduced_log_volume_extremum() -> None:
    print(
        "\n=== Part 3: reduced-carrier log-volume extremum"
        " (conditional on Part 1 supplied premise) ==="
    )
    rho_p, rho_perp, e_tot, lam = sp.symbols("rho_p rho_perp e_tot lam", positive=True, real=True)
    lagrangian = sp.log(rho_p) + sp.log(rho_perp) - lam * (rho_p**2 + rho_perp**2 - e_tot)
    sol = sp.solve(
        [
            sp.diff(lagrangian, rho_p),
            sp.diff(lagrangian, rho_perp),
            rho_p**2 + rho_perp**2 - e_tot,
        ],
        [rho_p, rho_perp, lam],
        dict=True,
    )
    check("Reduced log-volume has a unique positive stationary point", len(sol) == 1, f"sol={sol}", kind="conditional")
    stationary = sol[0]
    check(
        "Stationary point is rho_+ = rho_perp = sqrt(E_tot/2)",
        sp.simplify(stationary[rho_p] - sp.sqrt(e_tot / 2)) == 0
        and sp.simplify(stationary[rho_perp] - sp.sqrt(e_tot / 2)) == 0,
        kind="conditional",
    )

    rho = sp.symbols("rho", positive=True, real=True)
    reduced_profile = sp.log(rho) + sp.log(sp.sqrt(e_tot - rho**2))
    second = sp.simplify(sp.diff(reduced_profile, rho, 2).subs(rho, sp.sqrt(e_tot / 2)))
    check(
        "The stationary point is a strict maximum on the positive branch",
        sp.simplify(second) < 0,
        f"second={second}",
        kind="conditional",
    )

    e_plus, e_perp = sp.symbols("e_plus e_perp", positive=True, real=True)
    check(
        "rho_+ = rho_perp is equivalent to E_+ = E_perp",
        sp.simplify((rho_p**2 - rho_perp**2).subs({rho_p: sp.sqrt(e_plus), rho_perp: sp.sqrt(e_perp)}) - (e_plus - e_perp)) == 0,
        kind="conditional",
    )

    a, b_abs_sq = sp.symbols("a b_abs_sq", positive=True, real=True)
    check(
        "E_+ = E_perp pulls back to a^2 = 2 |b|^2",
        sp.simplify((3 * a**2 - 6 * b_abs_sq) / 3 - (a**2 - 2 * b_abs_sq)) == 0,
        kind="conditional",
    )
    check(
        "Therefore the conditional reduced-carrier extremum forces kappa = 2"
        " (conditional on the Part 1 supplied premise)",
        sp.simplify((a**2 / b_abs_sq).subs(a**2, 2 * b_abs_sq) - 2) == 0,
        kind="conditional",
    )


def part4_unreduced_vs_reduced_contrast() -> None:
    print(
        "\n=== Part 4: contrast with the unconditional unreduced determinant"
        " obstruction ==="
    )
    c = shift_matrix(3)
    i3 = sp.eye(3)
    p_plus = sp.simplify((i3 + c + c**2) / 3)
    p_perp = sp.simplify(i3 - p_plus)
    alpha, beta = sp.symbols("alpha beta", positive=True, real=True)

    d_unreduced = sp.simplify(alpha * p_plus + beta * p_perp)
    check(
        "Unreduced isotypic-scalar carrier has det = alpha beta^2 (unconditional)",
        sp.simplify(sp.factor(d_unreduced.det()) - alpha * beta**2) == 0,
    )

    d_reduced = sp.diag(alpha, beta)
    check(
        "Reduced real-isotype carrier has det = alpha beta (conditional on Part 1 supplied premise)",
        sp.simplify(d_reduced.det() - alpha * beta) == 0,
        kind="conditional",
    )

    mu, nu = sp.symbols("mu nu", positive=True, real=True)
    kappa_leaf = sp.simplify(2 * mu / nu)
    check("Unreduced weights (1,2) land at kappa = 1 (unconditional)", sp.simplify(kappa_leaf.subs({mu: 1, nu: 2}) - 1) == 0)
    check(
        "Reduced two-slot carrier carries equal weights and lands at kappa = 2"
        " (conditional on Part 1 supplied premise)",
        sp.simplify(kappa_leaf.subs({mu: 1, nu: 1}) - 2) == 0,
        kind="conditional",
    )


def main() -> int:
    part0_geometry_and_uniqueness()
    part1_doublet_radius_invariance_and_supplied_premise()
    part2_conditional_quotient_carrier()
    part3_reduced_log_volume_extremum()
    part4_unreduced_vs_reduced_contrast()

    print("\nInterpretation:")
    print("  The unreduced 3x3 determinant obstruction remains exact and")
    print("  unconditional. The doublet radius invariance is purely")
    print("  algebraic. The load-bearing step that turns those into MRU")
    print("  on the charged-lepton scalar lane is the SO(2)-quotient")
    print("  supplied premise of Part 1, which the demotion note proves is NOT")
    print("  a corollary of the cited observable-principle proposal on")
    print("  Herm_circ(3). This runner certifies the conditional algebra")
    print("  after the supplied premise; it does NOT derive that premise.")
    print("  The abstract Fourier-invariant theorem proves only a finite")
    print("  polynomial zero-locus equivalence. It supplies no physical")
    print("  mass carrier, P1 assignment, selector, or MRU closure.")
    total_pass = ALGEBRA_PASS + CONDITIONAL_PASS
    total_fail = ALGEBRA_FAIL + CONDITIONAL_FAIL
    print(
        f"\nSCORECARD ALGEBRA_PASS={ALGEBRA_PASS} ALGEBRA_FAIL={ALGEBRA_FAIL} "
        f"CONDITIONAL_PASS={CONDITIONAL_PASS} CONDITIONAL_FAIL={CONDITIONAL_FAIL} "
        f"SUPPLIED_PREMISES={len(SUPPLIED_PREMISES)}"
    )
    print(f"classified_pass={total_pass} fail={total_fail}")
    return 0 if total_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
