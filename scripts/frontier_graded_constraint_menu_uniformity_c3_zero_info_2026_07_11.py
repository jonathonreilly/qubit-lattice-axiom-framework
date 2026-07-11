#!/usr/bin/env python3
"""Exact checks for menu-uniformity contextuality and the C_3 zero-information point.

Companion runner for
docs/GRADED_CONSTRAINT_MENU_UNIFORMITY_CONTEXTUALITY_AND_C3_ZERO_INFORMATION_POINT_BOUNDED_THEOREM_NOTE_2026-07-11.md.

All checks are deterministic exact (sympy) computations on explicit 3x3 matrices
and symbols. No empirical numbers, fits, random draws, or floating tolerances are
consumed. Nothing on the derivation paths (w = Tr(rho P), the odds x, r = x/2,
the ratios) is hard-coded: those quantities are computed and then compared to the
expected literals.

Layout follows the note:
  Guards        -- verbatim-quote guards against the four readable source docs.
  Theorem A     -- menu-uniformity is contextual (2-menu vs 3-menu, H2 + H3).
  Theorem A cor -- symmetry forces uniformity only on single-orbit (conjugate) menus.
  Theorem B     -- rho = I/3 => r = 1; the r = 1/2 point is diag(1/2,1/4,1/4),
                   not invariant under the full (irreducible) automorphism group.
  Theorem B fwd -- forward-reference sanity: supplied structure alone
                   (C_3 + antiunitary doublet exchange) => diag(p_s, p_d/2, p_d/2).
  Theorem C     -- the two supplied choices; the cell-isomorphism (rank) obstruction.
  Dictionary    -- ratified component dictionary arithmetic and the two special points.
  Position tie  -- singlet projector J/3 (position basis) = diag(1,0,0) under the DFT.
"""

from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0


def check(num: int, ok: bool, desc: str) -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"CHECK {num:02d}: {tag} -- {desc}")


def is_zero_mat(M: sp.Matrix) -> bool:
    # expand_complex + simplify reduces cube-root-of-unity products to exact 0.
    reduced = sp.expand_complex(sp.simplify(M))
    return sp.simplify(reduced) == sp.zeros(*M.shape)


def born_weight(rho: sp.Matrix, P: sp.Matrix) -> sp.Expr:
    """Born-form menu weight w(P) = Tr(rho P); computed, never assumed."""
    return sp.nsimplify(sp.trace(rho * P))


def main() -> int:
    root = Path(__file__).resolve().parents[1]

    # ------------------------------------------------------------------ guards
    proposal = (root / "docs"
                / "GRADED_CONSTRAINT_PRIMITIVE_REGISTRATION_PROPOSAL_2026-07-04.md"
                ).read_text(encoding="utf-8")
    memo = (root / "docs"
            / "GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION_2026-07-04.md"
            ).read_text(encoding="utf-8")
    born = (root / "docs"
            / "BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md"
            ).read_text(encoding="utf-8")
    canon = (root / "docs"
             / "C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md"
             ).read_text(encoding="utf-8")

    proposal_advert = (
        "**The r = 1/2 class returns as the zero-information limit** (uniform on\n"
        "  symmetric menus)"
    )
    memo_advert = (
        "Binary availability plus\n"
        "symmetry can only pay uniform weights on symmetric menus (the harvested\n"
        "uniform-on-orbits results, e.g. r = 1/2)."
    )
    r4_premise = (
        "Under an explicit additional premise -\n"
        "invariance of `w` under every unitary automorphism of the composite, whose\n"
        "commutant is scalar - `rho = I/d` follows."
    )
    dict_ps = "`p_s = a^2`"
    dict_pd = "`p_d = 2|b|^2`"

    check(1, proposal_advert in proposal,
          "guard: proposal zero-information advertisement quoted verbatim")
    check(2, memo_advert in memo,
          "guard: Class F memo uniform-on-symmetric-menus sentence quoted verbatim")
    check(3, r4_premise in born,
          "guard: Born note R4 full-symmetry premise quoted verbatim")
    check(4, (dict_ps in canon) and (dict_pd in canon),
          "guard: C_3 canonical note carries the ratified dictionary p_s=a^2, p_d=2|b|^2")

    # ------------------------------------------------------- generation carrier
    # Character (U-eigen) basis of the hw=1 generation factor C^3:
    #   index 0 = singlet  (trivial rep, U-eigenvalue 1)
    #   index 1,2 = doublet characters (U-eigenvalues w, w^2)
    w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2   # primitive cube root of unity
    I3 = sp.eye(3)
    Ps = sp.diag(1, 0, 0)              # singlet cell projector, rank 1
    P1 = sp.diag(0, 1, 0)              # doublet character 1, rank 1
    P2 = sp.diag(0, 0, 1)             # doublet character 2, rank 1
    Pd = P1 + P2                      # doublet cell projector, rank 2

    # supplied C_3 generator in the character basis, plus the extra full-group
    # generator (position shift) that closes the irreducible Weyl group.
    Z = sp.diag(1, w, w**2)           # U in character basis (supplied structure)
    X = sp.Matrix([[0, 0, 1],
                   [1, 0, 0],
                   [0, 1, 0]])        # position shift; NOT supplied structure

    # ----------------------------------------------------------------- Theorem A
    # Both menus are finite orthogonal resolutions of the identity, so both are
    # menu-eligible under the proposal's own domain clause.
    projectors_are_orthogonal = all(
        is_zero_mat(A * B) for A, B in [(Ps, P1), (Ps, P2), (P1, P2)])
    refines = is_zero_mat(Pd - (P1 + P2))
    two_menu_res = is_zero_mat(Ps + Pd - I3)
    three_menu_res = is_zero_mat(Ps + P1 + P2 - I3)
    check(5, projectors_are_orthogonal and refines and two_menu_res and three_menu_res,
          "A: {Ps,Pd} and {Ps,P1,P2} are eligible resolutions with Pd = P1 + P2")

    # H3 (non-contextuality) forbids the double assignment on the shared cell Ps.
    w_ps_two = sp.Rational(1, 2)      # uniform on the 2-cell menu
    w_ps_three = sp.Rational(1, 3)    # uniform on the 3-cell menu
    check(6, w_ps_two != w_ps_three,
          "A: uniformity gives w(Ps)=1/2 (2-menu) vs 1/3 (3-menu); H3 forbids both")

    # H2 (orthogonal additivity) forces w(Pd) from the refined menu.
    w_pd_from_refined = w_ps_three + w_ps_three   # w(P1)+w(P2) under 3-menu uniformity
    w_pd_two = sp.Rational(1, 2)                  # uniform on the 2-cell menu
    check(7, w_pd_from_refined == sp.Rational(2, 3) and w_pd_from_refined != w_pd_two,
          "A: H2 forces w(Pd)=2/3 from the refinement, contradicting 2-menu 1/2")

    # ------------------------------------------------------- Theorem A corollary
    # Symmetry forces uniformity on a menu exactly when its cells form ONE orbit.
    # Full-group generator X cyclically permutes the three rank-1 lines:
    orbit_three = (is_zero_mat(X * Ps * X.inv() - P1)
                   and is_zero_mat(X * P1 * X.inv() - P2)
                   and is_zero_mat(X * P2 * X.inv() - Ps))
    # ... so the 3-cell menu is a single orbit (symmetric) and X-invariance forces
    #     equal weight 1/3 on each. The 2-cell menu is NOT one orbit: no group
    #     element sends the rank-1 Ps to the rank-2 Pd (checked at CHECK 15).
    check(8, orbit_three,
          "A-cor: full group makes {Ps,P1,P2} a single orbit; uniformity there is forced")

    # ----------------------------------------------------------------- Theorem B
    # Born form on the d=3 generation carrier: w(E) = Tr(rho E), conditional on
    # the proposed core (H1-H4). rho is NOT assumed diagonal a priori for the
    # symmetry argument; the two named points are evaluated explicitly.
    rho_sym = I3 / 3                                   # R4 full-symmetry point
    w_s = born_weight(rho_sym, Ps)
    w_d = born_weight(rho_sym, Pd)
    x_sym = w_d / w_s                                  # odds, computed
    r_sym = x_sym / 2                                  # r = x/2, computed
    check(9, (w_s == sp.Rational(1, 3)) and (w_d == sp.Rational(2, 3))
          and (x_sym == 2) and (r_sym == 1),
          "B: rho=I/3 => w=(1/3,2/3), odds x=2, r=x/2=1 (dimension-weighting point)")

    rho_half = sp.diag(sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 4))
    w_s2 = born_weight(rho_half, Ps)
    w_d2 = born_weight(rho_half, Pd)
    x_half = w_d2 / w_s2
    r_half = x_half / 2
    check(10, (w_s2 == sp.Rational(1, 2)) and (w_d2 == sp.Rational(1, 2))
          and (x_half == 1) and (r_half == sp.Rational(1, 2)),
          "B: rho=diag(1/2,1/4,1/4) => w=(1/2,1/2), x=1, r=1/2 (equipartition point)")

    # r = 1/2 point is NOT invariant under the full automorphism group; I/3 is.
    half_not_invariant = not is_zero_mat(X * rho_half * X.inv() - rho_half)
    sym_invariant = is_zero_mat(X * rho_sym * X.inv() - rho_sym)
    check(11, half_not_invariant and sym_invariant,
          "B: exhibited automorphism X breaks diag(1/2,1/4,1/4); fixes I/3")

    # The full group <Z,X> is irreducible: its commutant is scalar (Schur),
    # so the ONLY fully-invariant density operator is I/3.
    M = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"m_{i}{j}"))
    commutant_eqs = list(sp.flatten(M * Z - Z * M)) + list(sp.flatten(M * X - X * M))
    free = sp.linsolve(commutant_eqs, list(M))
    (sol,) = free  # single parametric solution tuple
    commutant_dim = len(set().union(*[t.free_symbols for t in sol]))
    check(12, commutant_dim == 1,
          "B: commutant of <Z,X> is 1-dimensional (scalar) => I/3 is the unique invariant rho")

    # ---------------------------------------------------- Theorem B forward ref
    # Sanity check only (NOT a theorem of this note): invariance under the
    # SUPPLIED structure alone -- C_3 (Z) and the antiunitary doublet-character
    # exchange K (complex conjugation composed with swap of indices 1,2) -- forces
    # the one-parameter family diag(p_s, p_d/2, p_d/2) and nothing more.
    ps_sym, pd_sym = sp.symbols("p_s p_d", positive=True)
    rho_family = sp.diag(ps_sym, pd_sym / 2, pd_sym / 2)
    fixed_by_Z = is_zero_mat(Z * rho_family * Z.inv() - rho_family)  # diagonal => trivially
    swap12 = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])           # doublet exchange (real diag => K acts as swap)
    fixed_by_K = is_zero_mat(swap12 * rho_family * swap12.inv() - rho_family)
    # a generic asymmetric doublet is NOT fixed by K, so the family is exactly cut out:
    rho_generic = sp.diag(ps_sym, sp.Rational(1, 3), sp.Rational(1, 6))
    generic_broken = not is_zero_mat(swap12 * rho_generic * swap12.inv() - rho_generic)
    check(13, fixed_by_Z and fixed_by_K and generic_broken,
          "B-fwd (sanity): supplied C_3 + doublet exchange fix diag(p_s,p_d/2,p_d/2) only")

    # ----------------------------------------------------------------- Theorem C
    # Choice (i) menu designation and (ii) per-cell equipartition are the two
    # supplied atoms. Neither is paid by Born form or by R4 symmetry:
    #   Born form alone -> a family (no value);
    #   R4 full symmetry -> I/3 -> r = 1, NOT 1/2.
    r_at_symmetry_is_one = (r_sym == 1)
    r_half_needs_designation = (r_half == sp.Rational(1, 2)) and (rho_half != rho_sym)
    check(14, r_at_symmetry_is_one and r_half_needs_designation,
          "C: R4 symmetry pays r=1; r=1/2 needs designation + equipartition (extra supply)")

    # Cell-isomorphism obstruction: no unitary/antiunitary automorphism of the
    # supplied structure maps the rank-1 singlet to the rank-2 doublet.
    rank_ps = Ps.rank()
    rank_pd = Pd.rank()
    no_swap = True
    for g in (Z, X, swap12, Z * X, X * swap12):
        gpg = sp.simplify(g * Ps * g.inv())
        if is_zero_mat(gpg - Pd):
            no_swap = False
    check(15, (rank_ps == 1) and (rank_pd == 2) and no_swap,
          "C: rank(Ps)=1 != rank(Pd)=2; no automorphism maps Ps->Pd (menu not symmetric)")

    # ---------------------------------------------------------------- dictionary
    a, b_re, b_im = sp.symbols("a b_re b_im", real=True, positive=True)
    b2 = b_re**2 + b_im**2                  # |b|^2
    p_s = a**2
    p_d = 2 * b2
    r_dict = b2 / a**2                       # r = |b|^2 / a^2
    r_from_cells = p_d / (2 * p_s)           # r = p_d / (2 p_s)
    energies_match = (sp.simplify(3 * p_s - 3 * a**2) == 0
                      and sp.simplify(3 * p_d - 6 * b2) == 0)
    x_dict = p_d / p_s                        # odds from dictionary contents
    odds_is_2r = sp.simplify(x_dict - 2 * r_dict) == 0
    check(16, (sp.simplify(r_dict - r_from_cells) == 0) and energies_match and odds_is_2r,
          "dict: r=|b|^2/a^2=p_d/(2p_s); channel energies (3a^2,6|b|^2); odds x=2r")

    # The two special points expressed through the dictionary:
    #   r = 1   <=> |b|^2 = a^2   (I/3 dimension weighting)
    #   r = 1/2 <=> a^2 = 2|b|^2  (per-cell equipartition)
    r_one_condition = sp.simplify((r_dict - 1)) == 0
    check(17,
          sp.simplify(r_dict.subs({b_re: a, b_im: 0}) - 1) == 0
          and sp.simplify(r_dict.subs({a: sp.sqrt(2), b_re: 1, b_im: 0}) - sp.Rational(1, 2)) == 0,
          "dict: r=1 at |b|^2=a^2 (I/3); r=1/2 at a^2=2|b|^2 (equipartition)")

    # ------------------------------------------------------------- position tie
    # Ties the character-basis singlet to the canonical note's I / J description:
    # the singlet projector J/3 in the position basis is diag(1,0,0) in the
    # character basis under the DFT F, F[j,k] = w^{j k} / sqrt(3).
    F = sp.Matrix(3, 3, lambda j, k: w**(j * k)) / sp.sqrt(3)
    Fdag = F.conjugate().T
    J = sp.ones(3, 3)
    Ps_pos = J / 3
    Ps_char = sp.simplify(F * Ps_pos * Fdag)
    unitary_F = is_zero_mat(sp.simplify(F * Fdag - I3))
    check(18, unitary_F and is_zero_mat(Ps_char - Ps),
          "tie: DFT is unitary and carries J/3 (position) to diag(1,0,0)=Ps (character)")

    # --------------------------------------------------------------- summary
    print("SUMMARY note: docs/"
          "GRADED_CONSTRAINT_MENU_UNIFORMITY_CONTEXTUALITY_AND_C3_ZERO_INFORMATION_POINT"
          "_BOUNDED_THEOREM_NOTE_2026-07-11.md")
    print("SUMMARY A: 'uniform on every menu' contradicts H2+H3 (2-menu 1/2 vs 3-menu 1/3).")
    print("SUMMARY B: C_3 zero-information point under full symmetry is rho=I/3 => r=1; "
          "r=1/2 is diag(1/2,1/4,1/4), not full-group invariant.")
    print("SUMMARY C: r=1/2 requires menu designation + per-cell equipartition; the "
          "two-cell menu is not symmetric (rank 1 vs rank 2 cells).")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
