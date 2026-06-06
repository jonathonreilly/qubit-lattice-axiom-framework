# CLAIM_STATUS_CERTIFICATE — block-1 (generation-determinant-order)

```yaml
artifact: KOIDE_FIRST_ORDER_SELECTOR_IS_THE_CHIRAL_LR_COUPLING_NOT_A_SYMMETRY_NARROW_NOTE_2026-06-05.md
runner: scripts/audit_companion_koide_first_order_selector_is_chiral_lr_coupling_exact.py   # 9/9 exact
actual_current_surface_status: exact-support   # localization + correction; within-R^3 algebra exact
target_claim_type: narrow_theorem
trace_class: direct_blocker_closure            # targets AC_phi_lambda (Tier-A, leverage 41)
reachability_to_target: partially_closes       # localizes r=1/2 to the L-R coupling gate; does NOT derive it
conditional_surface_status: "r=1/2 reachable iff the corner-mass realization supplies the chiral L-R coupling M(b)(x)sigma_+"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: >
  The within-R^3 structural fact (C3-equivariance <=> commutes-with-Gamma_chi <=> second-order; comm(C) cap
  anticomm(Gamma_chi)={0}) is EXACT and cited from the retained KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_2026-05-16.
  The NEW content is exact too: (1) Q is delta-independent -> U(1)_b red herring; (2) discrete Z3-character index
  -> (1,1) -> r=1/2 with C^3=I respected; (4) the factor-crossing L-R coupling is the escape. None derive r=1/2;
  all localize the gate. No fitted/observed/PDG inputs; no new axiom.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Promotion value gate (V1-V5) — this is NOT a retained-promotion PR
This block does not claim retained promotion (r=1/2 stays gated). It is a localization + correction at
exact-support. The genuinely-new load-bearing content vs prior koide notes (#2713, #2743):
- **V2 new content:** Q-delta-independence => U(1)_b red herring (corrects KOIDE_REAL_REP "half-saw it" + my own
  cycle-1 ledger); the discrete Z3-character realization of the index (resolves #2743's "index vs continuous r");
  the precise "selector = chiral L-R coupling M(b)(x)sigma_+, framework supplies grading not coupling" unification.
- **V3:** the audit lane would NOT already have the U(1)_b-red-herring correction nor the unified L-R-coupling
  localization; the components are landed but their synthesis + the two corrections are new.
- **V5 (distinct from #2743):** #2743 = "index readout is non-SUSY"; this = "the selector is a chiral L-R coupling,
  not a symmetry/static-J; U(1)_b is a red herring." Structurally distinct (corrects, not relabels).

## No-go discipline (N1-N8) — the within-R^3 no-go is CITED, not newly asserted
The within-R^3 structural no-go is the retained KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_2026-05-16 (N1-N8
already satisfied there). This note REPROVES it as the foundation and adds positive localization. N7 steelman is
recorded in the note (CPT-fuses the anti-Hermitian +/-i pair -> r=1/2, conditional on first-order) — it does NOT
overturn the gate; it IS the gate. No new global no-go is asserted here.
```

---

# CLAIM_STATUS_CERTIFICATE — block-2 (the decisive conclusion)

```yaml
artifact: KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05.md
runner: scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py   # 6/6 exact
actual_current_surface_status: no-go   # BOUNDED (not a hard universal no-go)
target_claim_type: no_go
trace_class: direct_blocker_closure    # AC_phi_lambda (Tier-A 41)
reachability_to_target: partially_closes  # r=1 forced on current surface; r=1/2 foreclosed within A_min; corner gate not theorem-foreclosed
conditional_surface_status: "r=1/2 reachable only if the open corner realization supplies a bundle-curving coupling forbidden within R^3, OR if the signed-sqrt(m) readout is adopted (the un-forced residual)"
claim_type_reason: >
  Closes block-1's open route: the localized L-R coupling M(b)(x)sigma_+ is Berry-flat (does NOT reach r=1/2).
  Dirac determinant = |det M|^2 (second-order); physical masses = singular values (sign-blind) -> r=1 forced.
  Bundle-curving coupling forbidden by C^3=I. BOUNDED: corner realization (substep-4) not theorem-foreclosed;
  N7 steelman (signed-sqrt(m) gives Q=2/3) is real and unresolved -> demoted from hard no-go to bounded.
  No fitted/observed/PDG inputs; no new axiom.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

**N1-N8:** recorded in the note's No-Go Discipline Gate section (12 routes named; 2 independent walls; N7 steelman
real -> bounded status, not hard no-go). **Value vs block-1/#2743:** new decisive premise (the specific L-R
coupling is Berry-flat; Dirac->singular-values->r=1) that CLOSES block-1's open localization route -- distinct
claim type (no-go vs localization).
