# β=6 SU(3) Wilson Plaquette — Consolidated No-Go / Ruled-Out Ledger

Seeded from the attack-surface frontier map (PR #2245,
`docs/BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md`).
**Do NOT re-explore these routes.** Statuses are 2026-05-29 read-offs from
`docs/audit/data/audit_ledger.json`; re-verify before citing as authority.

## The doubly-walled lane-killer (THE central obstruction)

The single missing object is uniformly **ρ_{p,q}(6)** (boundary character
measure / Perron eigenvector of the unmarked 3D spatial Wilson environment).
It is walled on two independent axes; no route escapes BOTH:

- **W-ALG. Algebraic underdetermination by local data.** Local character +
  intertwiner data + any 1-parameter ρ-family do not select ρ_{p,q}(6)
  (Theorem-3, `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note`,
  retained_bounded; combined Perron spread ≥ 0.1937 straddling 0.5934). The
  finite jet + analyticity + monotonicity do not force β_eff(6)
  (`gauge_vacuum_plaquette_framework_point_underdetermination_note`,
  retained_no_go). One scalar sample cannot recover the N-dim vector
  (`gauge_vacuum_plaquette_beta6_scalar_value_insufficiency_note_2026-04-17`,
  audited_conditional no_go).
- **W-COMP. Computational infeasibility of exact multi-link data.** Exact L_s≥3
  spatial-environment contraction has treewidth ≥ 29 → 8^30 intermediate
  (~1e19 GB), ~20 orders over budget
  (`su3_wigner_l3_treewidth_infeasible_2026-05-04`, audited_conditional);
  naive Haar-MC is sign-problem-bound (integrand ~1e-100, needs ~1e200 samples)
  (`su3_wigner_l3_cube_haar_mc_negative_result_2026-05-04`, retained_bounded).

## 20 ruled-out routes (frontier-map catalog)

### Closed-form / single-frame (all far-miss; su3_wilson_closed_form_fanout, retained_bounded)
1. M1 single-plaquette Haar character expansion = 0.4225 (no inter-plaquette correlation).
2. M2 leading strong-coupling β/(2N²) = 0.3333 (strict leading order).
3. M4 Drouffe-Itzykson mean-field self-consistency (z=6) = 0.8740 (β_eff→31.5, overshoots).
4. M5 weak-coupling 1-loop 1−4/54 = 0.9259 (not asymptotic at β=6).

### V=1 Picard-Fuchs (solved, wrong observable)
5. V=1 single-plaquette PF ODE / Frobenius → 0.4225 only; not the thermodynamic limit
   (`plaquette_v1_picard_fuchs_ode_note_2026-05-05`, retained_bounded).

### Finite L_s=2 cube (cannot host the correlation length)
6. L_s=2 APBC full-ρ Perron d^(-16) = 0.4291 (over-suppresses large ρ).
7. L_s=2 Z3 center-twist APBC variants (twists cancel globally; stay 0.4291).
8. L_s=2 Schur 0-parameter cube = 0.4291 (finite volume, ξ>2a not hostable).

### K-tube product / target-fit exponents
9. ρ=(c/c_00)^12 clean K-tube = 0.5888 (closest near-miss 0.78%, correction NOT
   from primitives; `su3_bridge_clean_tube_k12_support_2026-05-04`, unaudited).
10. Target-fit exponent closures "12+2/π" / "(N²−1)/(4π)" for the 0.78% gap
    (imports unproved correction; rejected as source authority).

### Exact L_s≥3 contraction / sampling (computationally foreclosed)
11. L_s=3 PBC naive Haar Monte-Carlo (sign-problem; P=0.108 noise).
12. Importance-sampled standard Wilson MC at L_s=3 (imports 0.5934 — forbidden).
13. Exact L_s=3 tensor-network by naive node-elimination (treewidth ≥ 29; 8^30).

### Transfer-operator / source-sector underdetermination (retained no-gos)
14. Fix ρ_{p,q}(6) from c_λ(6) + intertwiners + 1-parameter ρ ansatz (Theorem-3
    spread ≥ 0.1937).
15. Re-derive P(6)/β_eff(6) from the factorized source-sector Perron-Jacobi stack
    (`...perron_jacobi_underdetermination_note`, `...framework_point_underdetermination_note`).
16. Observable bridge <P>_full = R_O(β_eff) from current Wilson primitive packet
    (`gauge_scalar_temporal_observable_bridge_no_go_theorem_note_2026-05-03`): BRIDGE
    only pins the missing number; escape needs a NEW independently-audited primitive.
17. Spatial-environment transfer underdetermination
    (`...spatial_environment_transfer_underdetermination_note_2026-04-17`).
18. Constant-lift closed-form guess β_eff^can ≈ 9.3295 (closeness is coincidence,
    not a theorem; `...constant_lift_obstruction_note`).

### Scalar reuse / finite-order truncation
19. Reuse a fixed scalar P(6) to recover the class-sector vector v_6 / ρ_{p,q}(6)
    (two distinct positive 3-weight vectors share L(v)=1 but differ in M(v)).
20. Close from a FINITE-ORDER truncation of the connected hierarchy (log Z_L is
    non-polynomial; no finite-order truncation closes the thermodynamic value;
    `...infinite_hierarchy_obstruction_note`, retained_no_go).

## Five analytic routes — all dead (frontier-map Section 5)

| # | Route | feasibility | fatal obstruction |
|---|---|---|---|
| 1 | d-log-Padé / conformal resummation of the connected-shell series | long-shot | high-order exact engine collides with W-COMP beyond d_5; complex-pair analyticity unproven. **This loop attacks the in-runway sub-kernel.** |
| 2 | Finite-volume holonomic (Picard-Fuchs) continuation of L_s≥3 Z(β) | infeasible | needs 10^36–10^72 connected supports; no a-priori D-finite bound (R ≤ 3^81). |
| 3 | Collective-field large-N_c saddle | infeasible | saddle lands on ruled-out 0.4225 / 0.8740; core is the unsolved d>2 master field. |
| 4 | Transverse-slab κ self-consistency | infeasible / ruled-out | invalid axis-swap of temporal-gauge factorization; ρ=κ/a^4 retarget is circular (audited_renaming). |
| 5 | Nested-transfer-matrix slab | long-shot / ruled-out | slab dim 8^(2L⊥²) = 8^32 (= the wall); ξ~2–3 never reaches asymptotic regime. |

## This loop's NEW finite-geometry no-go (cycle 1, 2026-05-30)

**No order-β⁶ distinct connected support contributes to Δ(β).** Exhaustive
GF(3) link-balance enumeration over the radius-1 candidate patch: of all 5966
connected leaf-free distinct supports of total size 6 (= p_0 + 6 distinct
action faces), **zero** are SU(3) color-closable. Hence d_6 receives
contributions ONLY from the four order-5 cube shells via order-6 multiplicity
(one face doubled, or the marked plaquette inserted twice). This is a
bounded finite-enumeration fact (companion to the retained order-5 four-shell
classification), not a closure. (See cycle-1 PR / bounded note.)

## Standing policy reminders

- No new axioms; A_min is fixed. Legitimate path: import → bounded retained → retire import.
- No new repo vocabulary / tags / meta-framings in PRs.
- Framework PRs land science/fixes only; never audit-lane data (`docs/audit/**`).
- Verify ledger `effective_status` before citing any status from memory.
