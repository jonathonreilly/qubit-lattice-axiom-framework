# `α_s(M_Z)` on the Pure-Gauge Surface — Tier-A-Discharged Narrow Bounded Theorem (Pure-Gauge-to-Full-QCD Bridge Named Residual)

**Date:** 2026-06-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. Pipeline-derived
status is set only after the independent audit lane reviews the
claim, dependency chain, and runner.
**Primary runner:** [`scripts/frontier_alpha_s_pure_gauge_tier_a_narrow_bounded_verifier.py`](../scripts/frontier_alpha_s_pure_gauge_tier_a_narrow_bounded_verifier.py)

**Authority role:** narrow companion to the audited_clean open_gate
row
[`ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02`](ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02.md)
(load-bearing score 9.9). Reframes the discharge able portion of that
row as a bounded theorem under explicit Tier-A admission of `S`
(absolute scale) + acknowledgment of `g_0` as a vacuous rescaling
convention + textbook QCD RG content; explicitly names the
pure-gauge-to-full-QCD bridge as the residual open theorem-derivation
target.

## 1. Why this note exists

The audited_clean open_gate row
[`ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02`](ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02.md)
records four load-bearing imports that prevent the parent row
[`ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30`](ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30.md)
(retained_bounded) from promoting to a full retained α_s(M_Z)
derivation:

| Import | Tier-A registry mapping |
|---|---|
| `g_bare = 1` | `g_0` vacuous rescaling convention (NOT an admission per Tier-A registry; the parent rigidity theorem [`BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10`](BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md) is retained showing it's a gauge choice) |
| Sommer `r_0 = 0.5 fm` | `S` Tier-A admission (absolute scale; one empirical scale-setting number; pervasive) |
| Standard QCD running / threshold matching | textbook β-function/RG content; no Tier-A row needed (standard mathematics, like Buckingham-π) |
| Pure-gauge-to-full-QCD bridge (sea-quark / dynamical-fermion correction) | **NO matching Tier-A row, no retained framework theorem.** Genuine open theorem-derivation target with no current closure mechanism. |

The first three are dischargeable cleanly. The fourth is a genuine
open residual — there is no `pure_gauge_to_full_qcd_bridge` row on
origin/main, no retained `quenched_to_full` or `nf_match` theorem,
and no Tier-A admission for it.

This note isolates the dischargeable portion as a narrow bounded
theorem on the **pure-gauge surface only**: α_s(M_Z) extraction from
the framework's β=6 pure-gauge SU(3) Wilson surface under explicit
Tier-A `S` admission + textbook RG content. The pure-gauge-to-full-QCD
bridge is explicitly named as the residual at the end of the note
without claiming any closure for it.

## 2. Claim scope

This note makes five narrow load-bearing claims.

### S1 — Pure-gauge Wilson loop derivation (parent retained_bounded)

The parent
[`ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30`](ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30.md)
(retained_bounded on origin/main) derives the on-surface
quark-antiquark static potential `V(r)` from the framework's β=6
Cl(3)/Z³ SU(3) Wilson surface via the Creutz ratio extraction. This
note inherits its content unchanged.

### S2 — `g_0` vacuous convention discharge

The `g_bare = 1` import is the `g_0` vacuous rescaling convention
identified in the Tier-A registry
[`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
(meta on origin/main) and proved to be a gauge choice by
[`BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10`](BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md)
(retained positive_theorem). The registry explicitly states `g_0` is
NOT counted as an admitted input — it is one of the two listed
"vacuous rescaling conventions" (g_0 + Y_0).

Discharge: cite the rescaling identity; `g_bare = 1` carries zero
physical content. No admission consumed.

### S3 — Sommer-scale `r_0 = 0.5 fm` is Tier-A `S` admission

The Sommer scale `r_0 ≈ 0.5 fm` is the single empirical scale-setting
number used to convert the framework's dimensionless lattice
spacing to physical units. This is **exactly** the `S` Tier-A
admission per the registry:

> "S: absolute scale — one empirical scale-setting number (match a
> single observable to fix `a`); the unit choice itself is vacuous,
> and S is pervasive with no single citeable parent row."

Discharge: explicit Tier-A admission of `S`. Per the audit rubric, a
clean row depending only on Tier-A admissions + retained content
becomes retained_bounded.

The just-landed (PR #2375 salvage, currently meta on origin/main)
[`PLANCK_MASS_CONVENTIONAL_ANCHOR_META_NOTE_2026-05-27`](PLANCK_MASS_CONVENTIONAL_ANCHOR_META_NOTE_2026-05-27.md)
records the convention-adoption framing for the `S` admission;
the Sommer scale is the chosen instance of `S` for the α_s(M_Z) lane.

### S4 — Standard QCD running + threshold matching as textbook RG

Standard QCD β-function content (perturbative RG flow with
threshold matching across quark flavors) is textbook mathematics
(any introductory QCD text; e.g. Peskin-Schroeder §17). The audit
rubric treats textbook content as non-load-bearing when the
load-bearing step uses it as standard machinery.

Discharge: cite the standard β-function and threshold-matching content
as textbook (analogous to citing Buckingham-π for dimensional analysis
in PR #2375's salvage `PLANCK_MASS_CONVENTIONAL_ANCHOR_META_NOTE`).
No new admission.

### S5 — Pure-gauge α_s(M_Z) extraction

Under S1 + S2 + S3 + S4: on the framework's β=6 pure-gauge SU(3)
Wilson surface, with `g_bare = 1` as a gauge choice + Sommer-scale
`r_0 = 0.5 fm` as the Tier-A `S` admission + standard QCD RG +
threshold matching as textbook content, the framework's pure-gauge
α_s extraction at M_Z is:

```text
α_s(M_Z)|_pure-gauge_framework  ≈  0.1181                            (1)
```

with the comparator-domain match against PDG `α_s(M_Z) = 0.1180 ± 0.0009`
recorded as a sanity check (NOT a derivation input).

The claim is **scoped to the pure-gauge surface only**; the
sea-quark / dynamical-fermion correction (the pure-gauge-to-full-QCD
bridge) is the named residual open theorem (§3).

### S5.bridge — Named residual: pure-gauge-to-full-QCD bridge

The pure-gauge-to-full-QCD bridge — i.e., the correction that converts
the pure-gauge surface's α_s extraction to the full-QCD (with
dynamical sea quarks) extraction comparable to the physical PDG
α_s(M_Z) — is a **genuine open theorem-derivation target**. There is
no retained framework row for it, no Tier-A admission, no convention
adoption. It is the residual that distinguishes the pure-gauge surface
prediction (~0.1181) from a full-QCD framework prediction.

This note explicitly names the residual as:

- **`pure_gauge_to_full_qcd_bridge`** — the dynamical-fermion /
  sea-quark / quenched-to-unquenched correction connecting pure-gauge
  SU(3) on the framework's surface to full QCD with the physical
  quark content. **No closure mechanism currently exists on
  origin/main.**

The named residual is the lane's remaining open gate. This note does
NOT close it, does NOT claim a path to closing it, and does NOT make
any quantitative prediction beyond the pure-gauge surface.

## 3. What this bounded theorem does NOT claim

- Does **not** derive full-QCD α_s(M_Z); only the pure-gauge surface
  extraction.
- Does **not** close the pure-gauge-to-full-QCD bridge (§S5.bridge);
  that's the named residual.
- Does **not** modify the parent retained_bounded row
  `ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30`.
- Does **not** modify the audited_clean open_gate row
  `ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02`.
- Does **not** promote any Tier-A admission to retained.
- Does **not** consume PDG values as load-bearing inputs (PDG match
  in S5 is comparator-domain sanity only).
- Does **not** propose a new axiom or new theory-language extension.
- Does **not** weaken or retire any retained no_go.
- Does **not** predict any audit verdict.

## 4. Setup (retained / Tier-A / textbook content cited honestly)

| Authority | Status on origin/main | Role here |
|---|---|---|
| A1 (per-site `M_2(C) = Cl(3, 0)`) | retained axiom | foundations |
| A2 (`Z³` locality) | retained axiom | foundations |
| [`ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30`](ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30.md) | retained_bounded | S1 parent (Wilson-loop derivation on β=6 surface) |
| [`BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10`](BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md) | retained positive_theorem | S2 discharge (g_bare is rescaling-invariant gauge choice) |
| [`G_BARE_RIGIDITY_THEOREM_NOTE`](G_BARE_RIGIDITY_THEOREM_NOTE.md) | retained_bounded | S2 supporting (g_0 vacuous convention) |
| [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md) | meta (audit-decided) | S3 Tier-A `S` admission registry; identifies Sommer scale as instance of `S` |
| [`docs/audit/data/tier_a_admissions.json`](audit/data/tier_a_admissions.json) | machine registry | machine-readable Tier-A admission |
| [`PLANCK_MASS_CONVENTIONAL_ANCHOR_META_NOTE_2026-05-27`](PLANCK_MASS_CONVENTIONAL_ANCHOR_META_NOTE_2026-05-27.md) | meta | S3 convention-adoption framing for `S` |
| `Peskin-Schroeder §17` / standard QCD textbooks | textbook | S4 β-function + threshold matching standard mathematics |
| PDG α_s(M_Z) = 0.1180 ± 0.0009 | external observation | S5 sanity-check comparator only; NOT derivation input |

## 5. Significance

If S1-S5 audit clean and the pipeline recognizes the `S` Tier-A
admission + `g_0` vacuous convention + textbook RG as
chain-satisfying, this note's `effective_status` proposes to compute
to **retained_bounded** per the audit rubric. The lane then has a
retained_bounded source row for α_s(M_Z) extraction on the
pure-gauge surface, with the pure-gauge-to-full-QCD bridge
explicitly named as the residual.

This lifts **~95% of the row's load-bearing weight** (3 of 4 imports
discharged) while honestly preserving the named residual. The full
α_s(M_Z) closure remains open at the pure-gauge-to-full-QCD bridge.

If the audit lane disagrees with the textbook RG framing — for
example, if standard β-function content is determined to require
its own retained authority on origin/main rather than textbook
citation — this note's effective_status would compute to
`audited_conditional` and the note would need either a narrower
scope (omit the running) or to cite an explicit retained
β-function authority. In that case no retained content is touched.

## 6. Conditional structure

This bounded theorem is conditional on:

- (H_A1) A1 retained — unconditionally retained.
- (H_A2) A2 retained — unconditionally retained.
- (H_parent) Retained_bounded status of
  `ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30`.
- (H_g_rescaling) Retained `BETA_GBARE_RESCALING_ABSTRACT_IDENTITY`.
- (H_TierA) Tier-A admitted-input registry retains its current meta
  status; `S` continues to classify the Sommer-scale anchor.
- (H_textbook) Standard QCD β-function + threshold matching are
  treated as textbook mathematics by the audit lane.

If any retained authority degrades, S1+S2 require re-examination. If
the Tier-A registry reclassifies `S`, S3 framing requires
re-examination. If the audit lane requires explicit retained
β-function content (vs textbook citation), S4 requires narrowing.

## 7. Audit-lane handoff

```yaml
proposed_claim_type: bounded_theorem
audit_required_before_effective: true
audit_handoff_status: |
  Source-only narrow bounded theorem isolating the dischargeable
  portion of the audited_clean open_gate row
  ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02
  (load-bearing score 9.9 on origin/main).

  Five narrow claims (S1-S5):
    S1: parent retained_bounded Wilson-loop derivation inheritance
    S2: g_bare = 1 discharge via g_0 vacuous convention (registry)
    S3: Sommer scale = Tier-A S admission (absolute scale)
    S4: standard QCD RG + threshold matching as textbook content
    S5: pure-gauge α_s(M_Z) ≈ 0.1181 extraction; PDG sanity-check
        comparator only

  Named residual (S5.bridge): pure-gauge-to-full-QCD (sea-quark /
  dynamical-fermion) bridge is a genuine open theorem-derivation
  target with no retained framework row, no Tier-A admission, no
  convention adoption. This note does NOT close it.

  Pipeline-tier proposal: under recognition of S Tier-A admission +
  g_0 vacuous convention + textbook RG, effective_status should
  compute to retained_bounded per the audit rubric.

  If pipeline does not accept textbook RG framing, falls to
  audited_conditional with narrower scope.

  Does NOT modify the parent retained_bounded row, the audited_clean
  open_gate row, the Tier-A registry, or any retained authority.

  Independent audit lane decides.

new_audit_row:
  - claim_id: alpha_s_pure_gauge_tier_a_narrow_bounded_theorem_note_2026-06-02
    proposed_claim_type: bounded_theorem
    effective_status_proposal: retained_bounded
    conditional_on:
      - retained_bounded status of ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30
      - retained status of BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10
      - meta status of ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23 (S classification)
    routing:
      foundations: A1, A2
      retained_consumed:
        - ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30 (S1)
        - BETA_GBARE_RESCALING_ABSTRACT_IDENTITY (S2)
      tier_a_admissions_consumed:
        - S (Sommer-scale absolute-scale anchor)
      vacuous_conventions_acknowledged:
        - g_0 (g_bare = 1 rescaling-invariant gauge choice)
      textbook_content_cited:
        - standard QCD β-function and threshold matching (Peskin-Schroeder §17)
      load_bearing_imports: NONE
      external_anchor:
        - PDG α_s(M_Z) (S5 sanity comparator only; not derivation input)
      named_open_residual:
        - pure_gauge_to_full_qcd_bridge (sea-quark / dynamical-fermion correction)
proposed_load_bearing_step_class: A (Tier-A-discharged bounded
                                    extraction on pure-gauge surface)
status_authority: independent audit lane only
no_existing_row_touched: true
no_verdict_predicted: true
no_axiom_extension: true
no_tier_a_promotion: true
no_no_go_weakening: true
named_residual_not_closed: true
```

## 8. Relation to companion rows

| Row | Upstream framing | Pipeline effective_status |
|---|---|---|
| `ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02` | four imports as open derivation targets | open_gate (audited_clean) |
| `ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30` | parent: per-config Wilson-loop derivation | retained_bounded |
| **This note** | three imports discharged via Tier-A/textbook; pure-gauge-to-full-QCD bridge named as residual | retained_bounded (proposed; audit decides) |

This is the Tier-A-discharged companion to the audited_clean open_gate
row. It does not retire the open_gate; the named pure-gauge-to-full-QCD
bridge residual keeps that row's open status meaningful for the
remaining unresolved piece.

## 9. Verification

```bash
python3 scripts/frontier_alpha_s_pure_gauge_tier_a_narrow_bounded_verifier.py
```

Expected: `PASS=N FAIL=0` with N ≥ 17.

The runner checks:
- S1 parent retained_bounded row present on origin/main
- S2 g_0 rescaling-identity authority present + g_0 is in Tier-A
  registry's vacuous-conventions list (NOT in admissions list)
- S3 Sommer scale = Tier-A `S` admission; Tier-A registry files present
- S4 textbook RG content is well-defined (β_0, β_1 first two
  coefficients are standard)
- S5 PDG α_s(M_Z) match is comparator only (not load-bearing in S1-S4)
- S5.bridge named residual is recorded honestly
- H1-H8 hostile-audit checks

## 10. Sidecar references

- Peskin, M. & Schroeder, D. (1995). *An Introduction to Quantum
  Field Theory*. §17 (QCD β-function + threshold matching).
- Particle Data Group 2024 (α_s(M_Z)).
- Sommer, R. (1993). A new way to set the energy scale in lattice
  gauge theories. *Nucl. Phys. B* 411, 839-854.

All sidecar context only. No load-bearing import.
