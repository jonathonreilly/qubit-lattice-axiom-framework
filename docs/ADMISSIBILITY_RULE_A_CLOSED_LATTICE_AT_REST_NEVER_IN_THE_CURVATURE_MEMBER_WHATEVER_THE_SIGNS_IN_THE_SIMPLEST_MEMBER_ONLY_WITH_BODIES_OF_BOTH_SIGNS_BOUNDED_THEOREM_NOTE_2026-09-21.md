---
claim_id: admissibility_rule_a_closed_lattice_at_rest_never_in_the_curvature_member_whatever_the_signs_in_the_simplest_member_only_with_bodies_of_both_signs_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "On a finite connected closed symmetric graph the positive-function divided-difference identity excludes nonzero net diagonal sources in the supplied curvature equations, with uniform zero-source fields as an explicit exception. Nonconstant positive solutions of the simplest supplied equation require both source signs. A distinct-site pair on a translation-invariant torus has the stated exact tuning condition."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_strong_field_exactly_bodies_at_rest_make_the_clock_law_linear_in_the_root_of_the_rate_the_ledger_is_a_surface_term_bounded_by_a_capacity_bounded_theorem_note_2026-09-21
  - admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
  - admissibility_rule_amplitudes_of_negative_energy_fall_like_the_others_and_source_the_opposite_field_a_negative_body_at_rest_has_a_largest_size_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_a_closed_lattice_at_rest_curvature_member_never_simplest_member_both_signs_2026_09_21.py
---

# Closed positive field equations: a uniform exception and a tuned signed pair

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

Let Delta f(x)=sum_(y adjacent x)(f(y)-f(x)) on a finite connected undirected closed graph; positive symmetric edge weights may be included in every sum. There is no boundary forcing. For the simplest member supply phi=sqrt(w)>0, gamma>0,
`(2/gamma)(-Delta phi)_x+m_x phi_x=0`,
`F=(2/gamma)sum_edges(phi_x-phi_y)^2`.
For the other member supply chi>0,N>0,
`Delta chi=-mu/chi=-Q`, `Delta N=(Q/chi)N`, w=N/chi.
The source arrays m and mu are prescribed net per-site diagonal coefficients, not full matter wavefunctions.

For the pair result only, use a periodic translation-invariant connected torus. Define G by -Delta G=delta_0-1/V and sum G=0. Write G0 for its common diagonal and Gd at the nonzero separation, with h=G0-Gd>0. The runner uses the unweighted four-sided three-dimensional torus and its 192 edges.

## Theorem T1 — an identity

*Statement.* For `f > 0` on a closed lattice: `Σ_z(Δf)_z/f_z = Σ_bonds(f_x − f_y)²/(f_xf_y)`. It is positive unless `f` is uniform.

*Proof.* `Σ_z(Δf)_z/f_z = Σ_bonds[(f_y − f_x)/f_x + (f_x − f_y)/f_y] = Σ_bonds(f_y − f_x)(1/f_x − 1/f_y)`. The lattice is connected. ∎

## Theorem T2 — only the uniform zero-net-source solution

*Statement.* Let `χ > 0` satisfy the lengths' equation on a closed lattice for some bare energies of any signs, and let `N > 0` be any function. Then `Σ_z[(ΔN)_z − (Q_z/χ_z)N_z]/N_z = Σ_bonds(N_x − N_y)²/(N_xN_y) + Σ_bonds(χ_x − χ_y)²/(χ_xχ_y)`. Hence the rates' equation holds at every site only if `N` and `χ` are uniform, and then every `μ_z = 0`.

*Proof.* By T1 for `N`, the first part of the left side is the first sum of squares. `Σ_zQ_z/χ_z = −Σ_z(Δχ)_z/χ_z`, which by T1 is minus the second sum of squares. If `χ` is uniform, `Q = −Δχ = 0`. ∎

The uniform positive chi,N with mu_x=0 at every site are actual solutions. Opposite signed coincident source labels can cancel in mu_x: the result excludes nonzero net diagonal sources, not every possible underlying record label. With held walls the sum identity includes boundary terms, so the closed-graph conclusion does not extend unchanged to grounded models.

## Theorem T3 — the simplest member: both signs, on a surface

*Statement.* (a) If phi>0 is a NONCONSTANT solution of the supplied static equation on a finite connected closed graph and gamma>0: `Σ_zm_z = (2/γ)Σ_bonds(φ_x − φ_y)²/(φ_xφ_y) > 0`; `Σ_zm_zw_z = −F < 0`; the ledger's total is zero; bodies of both signs are present. (b) Conversely, every positive `φ` is at rest for the bare energies `m_z = (2/γ)(Δφ)_z/φ_z`. (c) On a translation-invariant finite connected torus, two nonzero point sources at DISTINCT sites separated by d admit a positive solution iff `m_A > 0 > m_B` (or the reverse) and `1/|m_B| − 1/m_A = γ(G_0 − G_d)`; then for any c>0, `φ = c − p(G_A − G_B)`, `p = (γ/2)m_Aφ_A > 0`, `φ_A = c/(1 + (γ/2)m_A(G_0 − G_d))`, and the clock at the negative body is the faster.

*Proof.* (a) Divide the law by `φ_z` and sum: `(γ/2)Σm_z = Σ(Δφ)_z/φ_z`; T1. Multiply the law by `φ_z` and sum: `Σm_zφ_z² = (2/γ)ΣφΔφ = −(2/γ)Σ_bonds(dφ)² = −F`. A sum that is positive with weights `1` and negative with weights `w_z > 0` has terms of both signs. (b) Definition. (c) The right side of `−Δφ = −p_Aδ_A − p_Bδ_B`, `p_i = (γ/2)m_iφ_i`, must sum to zero: `φ = c − p(G_A − G_B)`. Then `p(1 + (γ/2)m_Ah) = (γ/2)m_Ac` and `−p(1 + (γ/2)m_Bh) = (γ/2)m_Bc` with `h = G_0 − G_d`; for `c ≠ 0` their ratio gives `m_A + m_B = −γhm_Am_B`, which needs opposite signs and is the stated condition; `c = 0` gives `φ_A = −φ_B`. `G_A − G_B` is largest at `A`, so `φ ≥ φ_A > 0`. ∎

The condition ties the scale of the bodies to their separation: at each separation a one-parameter family of pairs is at rest. Whether such a configuration is stable is not examined.


If phi is constant then every m_x=0 and both strict inequalities become equalities. For nonconstant solutions the inequalities imply a comparison of aggregate signed weighted mean rates; they do not order every positive-source clock below every negative-source clock. The two-source pair formula uses equal diagonal values of the torus inverse on the mean-zero subspace and is not asserted for arbitrary nonhomogeneous graphs. None of these diagonal-source static solutions proves a stationary quantum body, a formation process or dynamical stability.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Uniform zero-source fields are valid closed solutions. Strict sign inequalities require nonconstant phi. Pair tuning assumes distinct sites and a homogeneous torus. Static diagonal field equations do not establish stationary matter or dynamics.

### N2 — Wall independence
No repository no-go wall is used.

### N3 — Supplied structure
The operators, domains, boundary conditions and state assumptions stated above are explicit mathematical hypotheses. They do not add a framework axiom or primitive.

### N4 — Dependencies
The dependencies below identify the actual supplied inputs; earlier stronger conclusions are not imported.

### N5 — Resolution
The canonical runner checks the finite examples and identities stated above using exact arithmetic. General conclusions require the displayed arguments, not extrapolation from samples. Historical simulations are deferred.

### N6 — Primitive boundary
No new primitive, species selection, filling rule or physical interpretation is adopted.

### N7 — Strongest objection
Uniform zero-source fields are valid closed solutions. Strict sign inequalities require nonconstant phi. Pair tuning assumes distinct sites and a homogeneous torus. Static diagonal field equations do not establish stationary matter or dynamics.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8571; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_strong_field_exactly_bodies_at_rest_make_the_clock_law_linear_in_the_root_of_the_rate_the_ledger_is_a_surface_term_bounded_by_a_capacity_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8573; no premise adoption or retained grade is inferred.
- [admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8590; no premise adoption or retained grade is inferred.
- [admissibility_rule_amplitudes_of_negative_energy_fall_like_the_others_and_source_the_opposite_field_a_negative_body_at_rest_has_a_largest_size_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_AMPLITUDES_OF_NEGATIVE_ENERGY_FALL_LIKE_THE_OTHERS_AND_SOURCE_THE_OPPOSITE_FIELD_A_NEGATIVE_BODY_AT_REST_HAS_A_LARGEST_SIZE_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8603; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8608 head `7fcef163e2cc2499ebe16a9aa2da54c42371aa0e`, branch `physics-loop/admissibility-induced-law-block75-a-closed-lattice-at-rest-20260921`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_closed_lattice_at_rest_curvature_member_never_simplest_member_both_signs_2026_09_21.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
