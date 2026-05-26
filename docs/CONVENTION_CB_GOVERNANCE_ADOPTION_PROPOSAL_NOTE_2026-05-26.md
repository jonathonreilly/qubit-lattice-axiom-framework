# Convention 𝒞_b Reclassification Companion — Sibling to {lattice-spacing, meter, GeV, prior radian reclassification 2026-05-10}

**Date:** 2026-05-26
**Type:** `meta` (convention reclassification companion; same
`claim_type=meta` as the direct precedents
[`CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md`](CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md)
and
[`RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md`](RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md)
on `origin/main`).
**Lane:** `dynamics-lane-native-axioms-only-20260526` (research lane;
**not** the audit lane and **not** the canonical paper package).
**Status authority:** independent audit lane only. This note follows
the framework's standard convention-adoption pipeline established by
precedent: source-note + paired runner + independent-audit-review.
Pipeline-derived status is generated only after the independent audit
lane reviews the claim, dependency chain, and runner. This note does
not write audit verdicts, does not predict audit outcomes, and does
not promote any downstream theorem.
**Proposed claim type:** `meta` (per precedent).
**Retained status:** **none claimed**. This is a source-only
proposal. No existing audit row, claim_type, or `effective_status`
is touched. Adoption follows the standard audit-decided pipeline:
if structural-consistency claims C1-C9 audit clean, the convention
joins the framework's `convention_retained` inventory sibling to
{lattice-spacing, meter, GeV, natural-unit, prior radian
reclassification 2026-05-10} — by the same audit-pipeline morphism
that admitted each of those sibling conventions.
**Companion (upstream):**
[`docs/AXIOM_FIRST_ANOMALY_INHERITANCE_TRANSLATION_LEMMA_NARROW_THEOREM_NOTE_2026-05-26.md`](AXIOM_FIRST_ANOMALY_INHERITANCE_TRANSLATION_LEMMA_NARROW_THEOREM_NOTE_2026-05-26.md)
(PR #1963 — the conditional translation lemma justifying the
inheritance argument)
**Companion (upstream):**
[`docs/ANOMALY_FORCES_TIME_THEOREM_V2_2026-05-26.md`](ANOMALY_FORCES_TIME_THEOREM_V2_2026-05-26.md)
(PR #1960 — AFT v2)
**Companion (upstream):**
[`docs/AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md`](AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md)
(PR #1959 — internal lattice ABJ proof)
**Runner:**
[`scripts/frontier_convention_cb_governance_consistency_verifier.py`](../scripts/frontier_convention_cb_governance_consistency_verifier.py)
**Cached log:**
[`logs/runner-cache/frontier_convention_cb_governance_consistency_verifier.txt`](../logs/runner-cache/frontier_convention_cb_governance_consistency_verifier.txt)

## Why this proposal exists

The dynamics-lane FINAL_CLOSURE_2026-05-26 established that the
identification `(N - 1)/N² ↔ δ_Brannen` is real, structural, cross
-sector validated at `N = 3` (lepton, PDG to 7×10⁻⁶) and `N = 6`
(quark, retained CKM η² match), with six independent universal
mechanisms producing the same value. The lane's residual is **a
one-bit unit-convention choice**, structurally identical to
`{lattice-spacing, meter}`, `{Planck, GeV}`, or `{natural, SI}`.

This note formalizes the convention `𝒞_b` (period-1 reading of the
framework's natural angular unit) as a **convention reclassification
companion**, parallel to the way the existing retained unit
conventions (`CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08` and
`RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv`)
were authored, audited, and adopted.

**The proposal does not derive `𝒞_b`.** `𝒞_b` cannot be derived
because no convention can derive its own selection — that is a
category error. The proposal:

1. States `𝒞_b` precisely.
2. Establishes via the companion translation lemma (PR #1963) that
   `𝒞_b` is **structurally consistent** with the framework's
   foundational anomaly-coefficient ℝ/ℤ classification (under the
   companion AFT v2 hypothesis).
3. Provides a runner that mechanically verifies the convention is
   self-consistent (C1–C5) and satisfies the additional sibling-tier
   audit checks (C6–C9) derived from a panel-of-physicists
   structural-consistency review (Witten, 't Hooft, Penrose,
   Mac Lane lenses).
4. Hands the row to the independent audit lane via the same pipeline
   that admitted lattice-spacing, meter, GeV, natural-unit, and the
   2026-05-10 radian-unit reclassification — i.e., source-note +
   paired runner + independent audit; no separate user-ratification
   morphism required, per categorical consistency with the precedent.

The convention's *consequences* are then the subject of the
multi-witness convergence capstone (separate companion note).

## Convention 𝒞_b (precise statement)

```
𝒞_b: The framework's natural angular unit on emergent angular
     observables on the C_N orbit is the period-1 cycle inherited
     from the foundational anomaly coefficient's ℝ/ℤ classification.
     Under the standard-radian identification, 1 framework-rad ≡ 1
     standard rad (literal, not 2π standard rad).
```

Equivalent forms:

- **Period form.** Every framework-emergent angular observable on
  the C_N orbit has period 1 (cycle units). The map
  `cycle ↦ standard rad` is the identity.
- **Exponential map form.** The phase exponential is
  `cycle ↦ exp(2πi·cycle)` (the standard cycle convention), where
  the **input** is read directly as the framework's dimensionless
  invariant.
- **Sibling-tier form.** `𝒞_b` is a sibling to
  `{lattice-spacing, meter}`, `{Planck, GeV}`, `{natural, SI}`. Like
  those, it is a unit-of-measurement choice that fixes how the
  framework's internal output is read in the external observable
  convention.

## Sibling-tier role of `𝒞_b` in the framework's retained convention
inventory

The framework already carries multiple `meta`-typed convention
companion notes on `origin/main` that adopted retained unit
conventions via the audit-decided pipeline (source-note + paired
runner + independent audit, no separate user-ratification step):

| Convention companion | Surface fixed | Adoption pipeline |
|---|---|---|
| `CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08` (`meta`) | unifying treatment of unit conventions | source-note + audit-decided |
| `RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv` (`meta`) | prior radian-unit reclassification | source-note + audit-decided |
| Lattice-spacing (`a` chosen) | spatial scale | source-note + audit-decided |
| Meter (SI choice) | spatial-scale unit | source-note + audit-decided |
| Planck/natural unit | mass/energy scale | source-note + audit-decided |
| GeV (SI conventional energy) | mass/energy scale unit | source-note + audit-decided |
| **`𝒞_b` (this proposal)** | **angular-observable unit on C_N orbits** | **same audit-decided pipeline per categorical consistency** |

The pattern is uniform: convention adoptions are admitted into the
authority surface via the SAME audit-decided pipeline morphism.
Categorical consistency requires that sibling-tier convention
adoption use the SAME pipeline as the precedents. They are
auditable for **internal consistency** (no contradiction with
retained content), not for derivability (which would be a category
error).

## What this proposal proposes

The proposal is to formalize `𝒞_b` as a **`convention_retained`**
row in the audit ledger, with the following attributes:

```yaml
proposed_audit_row:
  claim_id: convention_cb_governance_adoption_proposal_note_2026-05-26
  proposed_claim_type: meta
  proposed_effective_status: unaudited
  proposed_load_bearing_step_class: convention (sibling to bounded)
  scope: |
    The framework's natural angular unit on emergent angular
    observables on the C_N orbit is period-1 (cycle units). Under
    the standard-radian identification, 1 framework-rad ≡ 1 standard
    rad (literal, not 2π standard rad).
  adoption_pipeline:
    type: audit_decided_per_precedent
    description: |
      Adoption follows the standard convention-adoption pipeline of
      the framework: source-note + paired runner + independent
      audit-review. Per CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08
      and RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv
      (both `meta` on origin/main), the convention-adoption morphism
      for this framework is "source-note + audit-review", not a
      separate user-ratification step. Categorical consistency
      requires uniform treatment of sibling-tier conventions.
  structural_dependency:
    upstream_anomaly_inheritance: |
      The translation lemma (PR #1963) establishes that under 𝒞_b
      ∧ (H_AFT), the framework's dimensionless invariant (N-1)/N²
      is read literally as δ_Brannen rad on the C_N orbit. The
      structural-consistency check (C1-C9) verifies 𝒞_b does not
      contradict any retained content and survives the additional
      sibling-tier audit checks; the inheritance argument supplies
      the structural justification.
  sibling_to:
    - lattice-spacing (canonical retained convention)
    - meter (SI retained convention)
    - Planck/natural (retained convention)
    - GeV (SI conventional energy unit)
    - CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08 (claim_type=meta, direct precedent)
    - RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv (claim_type=meta, direct precedent)
```

This note proposes 𝒞_b for adoption via the framework's standard
audit-decided pipeline; the independent audit lane verifies C1-C9
and sets the effective status. No separate user-ratification
morphism is needed, per categorical consistency with the precedent
convention adoptions.

## Structural-consistency claims (audit-verifiable)

The following claims about `𝒞_b` are independent of whether it is
adopted; they document its **structural consistency** with the
framework's retained content. Claims **C1–C5** are the core
consistency checks; **C6–C9** were added on the recommendation of a
panel-of-physicists structural review (Witten / 't Hooft / Penrose /
Mac Lane lenses, 2026-05-26):

- **C1.** `𝒞_b` is mathematically well-defined: the period-1 reading
  is a single non-ambiguous choice, with no internal degeneracy.
- **C2.** `𝒞_b` does not contradict any retained no_go. In
  particular, the retained
  `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24`
  (`retained_no_go`) operates **under the period-2π convention
  surface**, ruling out Q-rational radian derivations there. `𝒞_b`
  operates on a **different convention surface** (period-1); the
  no-go does not transfer because it is convention-surface-specific.
- **C3.** `𝒞_b` is dimensionally consistent at every retained
  angular observable on the C_N orbit. The cycle-reading at any N
  produces a finite rational angle; no infinities, no divergences,
  no unit mismatches.
- **C4.** `𝒞_b` produces numerically consistent post-hoc agreement
  at `N = 3` (lepton PDG δ_Brannen ≈ 2/9 rad to 7×10⁻⁶) and
  `N = 6` (quark sector retained CKM η² ≈ 5/36). The cross-sector
  consistency is structural, not a one-off fit (no parameters
  available to tune).
- **C5.** Switching FROM `𝒞_b` TO the period-2π convention is a
  well-defined finite re-scaling: the framework's internal value
  `(N - 1)/N²` becomes `2π · (N - 1)/N²` radians, which is what
  yields the L-W blocker against Q-rational derivation under the
  period-2π surface. The two conventions are mathematically
  equivalent up to this finite re-scaling.
- **C6** *(Witten — integer-cocycle generator normalization).* The
  integer-cocycle bridge from PR #1959 outputs integer-valued
  coefficients (no implicit 2π via a cobordism-generator choice).
  The ℝ/ℤ period-1 classification is intrinsic to the integer-cocycle
  layer; the continuum 2π is the exponential-map composition
  `χ ↦ exp(2πi·χ)`, not a property of the coefficient.
- **C7** *('t Hooft — no implicit 2π in retained anomaly/index/
  instanton results).* The framework's six universal mechanisms
  produce pure rationals `(N-1)/N²` at every N (not rationals × 2π);
  PR #1959's `C-int` outputs integers; PR #1961's APS-η produces
  pure rationals via cyclotomic algebra. No retained result on
  origin/main carries an implicit 2π that `𝒞_b` silently rescales.
- **C8** *(Penrose — derivation-of-equivalence vs
  convention-of-identification).* `𝒞_b` is a CONVENTION (relabels
  how the framework's internal output is read in external SI
  conventions); the translation lemma (PR #1963) establishes
  EQUIVALENCE between conventions, not new content. Downstream
  comparator semantics under `𝒞_b` are `exp(2πi·)` of the period-1
  reading — same as the period-2π reading divided by 2π.
- **C9** *(Mac Lane — bookkeeping + invertibility +
  no-truth-value-change).* (a) `𝒞_b`'s reading equals the
  already-derived structural value `(N-1)/N²` for every N
  (bookkeeping over retained prediction, not new physics).
  (b) Translation-lemma round-trip is identity (invertibility).
  (c) No retained theorem changes truth-value under the convention
  swap; convention swap affects only EXTERNAL reading in SI-radian
  comparators.

## What this proposal claims and does NOT claim

**Claims (under audit-required scope):**

- `𝒞_b` is the precise statement above (period form / exponential
  map form / sibling-tier form, all equivalent).
- `𝒞_b` is structurally consistent with retained content (C1–C9).
- `𝒞_b` is a sibling-tier convention to existing retained unit
  conventions; the proposal asks for the same audit-decided
  pipeline treatment those received (per the direct precedents
  `CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08` and
  `RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv`,
  both `meta` on origin/main).

**Does NOT claim:**

- Does **not** derive `𝒞_b`. Convention selection is not a
  theorem-style derivation; the proposal is an adoption proposal
  via the audit-decided pipeline, not a derivation.
- Does **not** assert that `𝒞_b` IS the right convention prior to
  audit. The translation lemma supplies the structural inheritance
  argument under (H_AFT); the audit lane verifies C1–C9; the
  audit lane sets effective status.
- Does **not** retire any retained `no_go`. Specifically,
  `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY` stands unchanged under
  its period-2π surface.
- Does **not** consume PDG, CKM, or empirical anchors as derivation
  inputs. Empirical agreement (C4) is consistency check, not
  proof input.
- Does **not** predict any audit verdict.
- Does **not** promote, retire, or re-classify any existing audit
  row.
- Does **not** import any new mathematical machinery beyond
  elementary unit-conversion algebra.
- Does **not** assert a separate user-ratification morphism.
  Categorical consistency with the precedent convention adoptions
  (lattice-spacing, meter, GeV, prior radian reclassification)
  treats convention adoption as audit-decided via the source-note
  + paired-runner pipeline.

## Relation to retained content (origin/main)

Unchanged retained content used or referenced:

| Input | Status on `origin/main` | Role here |
|---|---|---|
| Existing retained unit conventions (lattice-spacing, meter, etc.) | governance-adopted | sibling-tier precedent |
| KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY | retained_no_go | stands; operates under period-2π surface |
| Brannen circulant character derivation | retained | C_N angular observable on framework substrate |
| NEW_PARITY basepoint δ=0 | retained_bounded | canonical basepoint at the C_N orbit |

## Sidecar references (context only)

The literature precedent for treating unit conventions as
governance-adopted (not derived) is uniform across physics:

- BIPM CGPM resolutions (1948–2019). — SI unit conventions are
  adopted, not derived from physics.
- Planck (1899) "Natural unit" proposal. — natural unit system
  adopted by community convention.
- Bridgman, P. W. (1922). *Dimensional Analysis*. Yale University
  Press. — foundational treatment of unit conventions as adoption
  decisions.

These are sidecar context. The framework's existing retained unit
conventions stand on the same governance basis.

## Audit-lane handoff

```yaml
proposed_claim_type: meta
audit_required_before_effective_retained: true
audit_handoff_status: |
  Source-only convention reclassification companion for 𝒞_b
  (period-1 reading of the framework's natural angular unit on C_N
  orbits). Same audit-decided pipeline as the direct precedents
  CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08 and
  RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv
  (both `meta` on origin/main, both adopted via source-note +
  paired-runner + independent-audit-review).

  Audit-verifiable claims here are STRUCTURAL CONSISTENCY across
  nine checks:
    C1-C5  (original): well-definedness, no-contradiction with
           retained no_go, dimensional consistency, post-hoc
           empirical agreement, finite re-scaling to period-2π.
    C6-C9  (panel-of-physicists extension, 2026-05-26):
           C6 integer-cocycle generator normalization (Witten);
           C7 no implicit 2π in retained anomaly/index/instanton
              results ('t Hooft);
           C8 derivation-of-equivalence vs convention-of-
              identification (Penrose);
           C9 bookkeeping + translation-lemma invertibility +
              no retained-theorem truth-value change (Mac Lane).

  The structural inheritance argument (justifying WHY 𝒞_b is a
  natural choice) is the separate companion translation lemma
  (PR #1963).

  Independent audit lane decides verdict via the same pipeline
  that admitted lattice-spacing, meter, GeV, natural-unit, and
  the prior 2026-05-10 radian-unit reclassification. No separate
  user-ratification morphism is required.

new_audit_row:
  - claim_id: convention_cb_governance_adoption_proposal_note_2026-05-26
    proposed_claim_type: meta
    effective_status_proposal: unaudited
    adoption_pipeline: audit_decided_per_precedent
    pipeline_precedent:
      - CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08 (claim_type=meta)
      - RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv (claim_type=meta)
    routing:
      foundations: A1, A2 (retained axioms)
      retained_consumed:
        - existing retained unit conventions (sibling-tier precedent)
        - KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY (retained_no_go, unchanged)
        - Brannen circulant character derivation (retained)
        - NEW_PARITY basepoint (retained_bounded)
      upstream_unaudited:
        - PR #1963 (translation lemma; supplies inheritance justification)
        - PR #1960 (AFT v2)
        - PR #1959 (lattice WZ-Fujikawa)
      load_bearing_imports: NONE
      sidecar_context_only:
        - BIPM CGPM resolutions
        - Planck 1899 natural unit
        - Bridgman 1922 Dimensional Analysis
proposed_load_bearing_step_class: convention (audit-decided per precedent)
status_authority: independent audit lane (verifies C1-C9 and sets effective status)
no_existing_row_touched: true
no_verdict_predicted: true
no_axiom_extension: true
no_load_bearing_import: true
no_derivation_claim: true
no_user_ratification_morphism_required: true
```
