# Claim Status Certificate — block04 (Unified Operational Measurement Axiom — Minimization / Unification)

**Date:** 2026-06-20 (synthesis authored 2026-06-21)
**Block:** 04 — AXIOM MINIMIZATION / UNIFICATION: does ONE operational
measurement-with-readout axiom subsume BOTH block01 C1 (dynamics / arrow) AND C2
(readout-context / objectivity)? Is it strictly weaker, policy-preferred, and
independent of its residuals? Does C3 fold?
**Slug:** `axiom-update-proposals`
**Branch:** `physics-loop/axiom-update-proposals-block04-20260620`
**Synthesis note:**
[`docs/AXIOM_UPDATE_PROPOSAL_UNIFIED_OPERATIONAL_MEASUREMENT_2026-06-20.md`](../../../../docs/AXIOM_UPDATE_PROPOSAL_UNIFIED_OPERATIONAL_MEASUREMENT_2026-06-20.md)
**Consolidated note (additively updated):**
[`docs/AXIOM_UPDATE_PROPOSALS_CONSOLIDATED_2026-06-20.md`](../../../../docs/AXIOM_UPDATE_PROPOSALS_CONSOLIDATED_2026-06-20.md)
(dated `## BLOCK04 UNIFICATION` section appended, not a rewrite).
**Section legs:**
[`block04_section_SUFFICIENCY.md`](block04_section_SUFFICIENCY.md),
[`block04_section_MINIMALITY.md`](block04_section_MINIMALITY.md).

## Framework

Owner-authorized axiom-update-PROPOSAL lane optimizing exactly
`docs/audit/AXIOM_MINIMALITY_POLICY.md`'s target (the **weakest sufficient,
non-redundant, independent** extension with **no laundering**). This certificate
carries **no** `audit_status` and promises **no** `effective_status`; audit status
is set only by the independent audit lane. Each candidate primitive is recorded as
an **unmade science-level decision** per policy §1/§4/§6 — nothing here adopts an
axiom, sets a verdict, or edits the axiom registry.

```yaml
artifact_type: axiom minimization / unification synthesis (meta / governance proposal)
proposal_allowed: false   # owner governance decision required
adopts_axiom: false
sets_audit_verdict: false
edits_axiom_premise_nodes: false
status_authority: independent audit lane / owner only
hypothetical_axiom_status: "conditional on accepted new axiom; not retained on the actual current surface"
bare_retained_allowed: false
```

## Result (non-authoritative author hint to auditor)

```yaml
claim_type_author_hint: axiom_minimization_unification_partial_collapse
unified_axiom_id: MEAS-REC-READOUT
unified_axiom_statement: >
  One system-environment measurement interaction producing durable records that
  supplies AT ONCE, for the realized state: (a) an einselecting CPTP dynamics
  Phi_t = e^{tL} with an orientation = registration direction (C1 dynamics + arrow);
  (b) the pointer basis = central-sector / K-CPT decomposition (C2 readout context);
  (c) the SBS / quantum-Darwinism objectivity criterion, BASIS ONLY (C2 objectivity
  selector, basis part). Existence/slot only: no kernel/rate, no
  weight/probability/Born rule, no spacing, no arrow sign. Strength weak-medium.
collapse_verdict: partial_collapse
collapses:
  - "C1 full discharge set: B-AXIS N4 (registration-direction) + N5 (single-clock) + arrow + N2b-step + record-formation floor"
  - "C2 basis/identification half: observable T1-d det-readout identification (W = c log det) + P-REC single-taste pointer + Koide objectivity-BASIS (2-outcome alphabet)"
does_not_collapse:
  - id: C2-WEIGHT
    datum: "equal-block (1,1) sector-MEASURE weight t = w_p/w_s = 1 (pins Koide r=1/2, Q=2/3)"
    why: >
      objectivity is WEIGHT-BLIND (SBS plateau = H(weights) for both (1/2,1/2)=1.000 bit
      and (1/3,2/3)=0.918 bit) AND the einselection fixed point I/3 -> (1/3,2/3) -> r=1
      gives t=2, the wrong value; neither clause (a) nor (c) supplies t=1. A separate
      max-entropy / indifference datum (one dimensionless binary choice).
    strength: weak
  - id: SPACING
    datum: "time-edge spacing a_tau/a_s (one dimensionless ratio)"
    why: >
      Lattice axiom disavows lattice spacing; block02 SK-1 and block03 NODIAG both
      walled; 6-NN adjacency predicate |dx|+|dy|+|dz|=1 is metric-blind (edge set
      identical for a_tau/a_s = 1, 10, 0.137).
    strength: weak
strictly_weaker_than_C1_plus_C2: true
strictly_weaker_measure: >
  consequence set (logical content) + model count: Cons(U) (9 atoms) is a STRICT
  subset of Cons(C1-sep AND C2-sep) (10 atoms); the single distinguishing atom is
  equal_block_weight (U is weight-blind to it); U admits strictly more models;
  the converse derivation fails (Cons(C1 AND C2) not subset of Cons(U)).
policy_prefers_unified: true
policy_criteria_met:
  - weakest_sufficient   # U entails the dynamics + basis content and nothing more
  - non_redundant        # U does not subsume W or S (named residuals; policy section 2 bounded composition)
  - independent          # {U,W,S} mutually independent + C3 categorically separate
  - no_laundering        # adds content the MINIMAL_AXIOMS_2026-06-05 memo declares OUTSIDE axiom content; no reword of Lattice/Quantum/Record (policy section 1/4/6)
independence_check: >
  {U, W, S} mutually independent by countermodel (model-theoretic): each has a model
  on the A_min surface satisfying A_min + the other two but violating the target;
  none derivable from A_min + the others. W-independence reuses koide weight-blindness
  (objectivity weight-blind; dynamics horn at t=2 not t=1); S-independence reuses
  metric-blind adjacency. W and S verified ORTHOGONAL dials (grid sweep, no cross-leak).
c3_folds: "no"
c3_reason: >
  gauge group + chiral matter REPRESENTATIONS are a content-choice datum (gate 3),
  categorically distinct from a measurement-interaction EXISTENCE datum (gates 1/2);
  measurement witnesses blind to the anomaly traces / chirality template and vice
  versa; folding would be a category error / policy-laundering.
final_minimal_set:
  - MEAS-REC-READOUT   # unified operational measurement-with-readout axiom (folds C1 + C2-basis); weak-medium
  - C2-WEIGHT          # equal-block / indifference sector-measure weight t=1; weak
  - SPACING            # a_tau/a_s; weak
  - PIN-GAUGE-CONTENT  # C3; categorically separate; does NOT fold; heavy; unchanged from block01
coverage_vs_3axiom: >
  SAME coverage, MORE minimal. The block04 set {U, W, S, C3} discharges the IDENTICAL
  walls as block01 {C1, C2} (C1 full set + C2 basis half + C2 weight via isolated W),
  no coverage loss, no over-reach. Two operational axioms become ONE strictly-weaker
  operational axiom; the equal-block weight (C2 silently bundled) and the spacing
  (implicit C1-N2b residual) are NAMED and ISOLATED as the weakest separate data.
  C3 identical in both. Owner should PREFER block04 {U, W, S, C3} for the policy's
  weakest-sufficient / non-redundant / independent / no-laundering target.
verification:
  aggregate: "PASS=67 FAIL=0 across two block04 runners (39 + 28)"
  reproduced_utc: "2026-06-21"
  reproduced: true   # both re-run 2026-06-21: exit 0; clean under python3 -W error; numpy + stdlib (fractions) only
  no_empirical_import: true
  deterministic: true
  no_forbidden_file_touched: true   # docs/audit/data/ read-only; no axiom_premise_nodes.json edit; no git ops
  reuses_block01_runner_legs: true  # same W-exchange surface, dephasing/einselection, capacity lever, SBS plateau, I/3 fixed point, 2:1 fiber
  runner_bug_caught: >
    minimality runner first draft double-counted color in Tr[SU3^2 Y] (spurious extra
    n_color on top of T(fund)=1/2 normalization, returning Tr[SU3^2 Y]=1); FOLD(ii)
    leg FAILed and exposed it; fixed -> banked LH traces reproduce (-16/9, +1/3, +2).
    Documented runner-exposes-load-bearing-residuals pattern.
  runners:
    - {path: scripts/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.py, total: "PASS=39 FAIL=0", section: .claude/science/physics-loops/axiom-update-proposals/block04_section_SUFFICIENCY.md}
    - {path: scripts/axiom_update_unified_axiom_minimality_independence_2026_06_21.py, total: "PASS=28 FAIL=0", section: .claude/science/physics-loops/axiom-update-proposals/block04_section_MINIMALITY.md}
```

## Verification snapshot

| Runner | TOTAL | Reproduced 2026-06-21 |
|---|---|---|
| `scripts/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.py` | PASS=39 FAIL=0 | yes (exit 0, clean under `-W error`) |
| `scripts/axiom_update_unified_axiom_minimality_independence_2026_06_21.py` | PASS=28 FAIL=0 | yes (exit 0, clean under `-W error`) |

The sufficiency runner verifies (A) the unified axiom derives C1's full discharge
set and C2's basis/identification half on the **same** load-bearing objects the
block01 cluster runners use, AND (B) it provably does **not** supply the equal-block
weight (objectivity weight-blind; dynamics horn at `t=2`) nor the spacing
(metric-blind adjacency). The minimality runner verifies (A) `Cons(U) ⊊
Cons(C1 ∧ C2)` (strictly weaker), (B) `{U, W, S}` mutual independence by
countermodel + orthogonal dials, and (C) C3 categorical distinctness both ways.

## Consistency check (no contradiction with retained results)

The unification **respects** every retained no_go in scope:
`FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02` (the unified axiom does
**not** claim objectivity forces the weight — it is the source of the C2-WEIGHT
residual);
`KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31` (R3 `W_t` countermodel
reused);
`NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02` (P-REC pointer placed in the
measurement basis precisely because per-site `γ₅` is impossible);
`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` + block02 SK-1 + block03 NODIAG
(the SPACING residual stands). No primitive is mis-cited; no `A_min` axiom is
reworded; the unified axiom adds content the `MINIMAL_AXIOMS_2026-06-05.md` memo
declares **outside** axiom content (gates 1+2), recorded as an unmade science-level
decision (approval routes through policy §6, as `kinetic_isotropy_primitive` did).
C3 does not fold, so the gate-3 content choice is not laundered into an operational
axiom.

## Audit handoff

Audit status is set only by the independent audit lane. This certificate prefills no
`audit_status` and no `effective_status`. Recommended auditor focus: confirm
(1) both runners reproduce (PASS=39/0 and PASS=28/0, `-W error` clean); (2) the
consequence-set strict-subset comparison (`Cons(U) ⊊ Cons(C1 ∧ C2)`, single missing
atom = equal-block weight); (3) the three mutual-independence countermodels +
orthogonal-dial sweep; (4) the C3 categorical-distinctness (measurement witnesses
blind to anomaly traces / chirality and vice versa); (5) that the synthesis note and
the additive `## BLOCK04 UNIFICATION` consolidated section do not rewrite §1–§7;
(6) that the runner reuses the **exact** block01 cluster-runner load-bearing legs so
the fold is genuine (not a fresh toy).
