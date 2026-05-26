# Governance Proposal: Adopt Convention 𝒞_b as a Retained Convention Sibling to {lattice-spacing, meter}

**Date:** 2026-05-26
**Type:** governance proposal (source-only research-lane).
**Lane:** `dynamics-lane-native-axioms-only-20260526` (research lane;
**not** the audit lane and **not** the canonical paper package).
**Status authority:** independent audit lane decides the technical
audit row; user-side governance decides convention adoption. This
note proposes — it does not assert adoption, set audit verdicts, or
predict audit outcomes. Effective audit status is `unaudited` until
Codex GPT-5.5 audits it independently.
**Proposed claim type:** `governance_proposal` (subtype of
`bounded_theorem`: an authored governance-adoption proposal for an
independently-decided convention choice).
**Retained status:** **none claimed**. This is a source-only
proposal. No existing audit row, claim_type, or `effective_status`
is touched. No convention is adopted by this note — adoption
requires explicit user action recorded separately.
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
framework's natural angular unit) as a **governance-adoption
proposal**, parallel to the way the existing retained unit
conventions are governance decisions rather than derived theorems.

**The proposal does not derive `𝒞_b`.** `𝒞_b` cannot be derived
because no convention can derive its own selection — that is a
category error. The proposal:

1. States `𝒞_b` precisely.
2. Establishes via the companion translation lemma (PR #1963) that
   `𝒞_b` is **structurally consistent** with the framework's
   foundational anomaly-coefficient ℝ/ℤ classification (under the
   companion AFT v2 hypothesis).
3. Documents the user-side governance choice for explicit
   ratification (or not).
4. Provides a runner that mechanically verifies the convention is
   self-consistent at every retained sector (no internal
   contradiction).

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

The framework already carries multiple retained unit conventions as
governance-adopted (not derived) rows. `𝒞_b` would join them:

| Convention | Surface fixed | Derivation status |
|---|---|---|
| Lattice-spacing (`a` chosen) | spatial scale | governance-adopted, not derived |
| Meter (SI choice) | spatial-scale unit | governance-adopted, not derived |
| Planck/natural unit | mass/energy scale | governance-adopted, not derived |
| GeV (SI conventional energy) | mass/energy scale unit | governance-adopted, not derived |
| **𝒞_b (this proposal)** | **angular-observable unit on C_N orbits** | **governance-adopted, not derived** |

The pattern is uniform: convention adoptions select between
mathematically distinguishable representations of the same physical
content. They are auditable for **internal consistency** (no
contradiction with retained content), not for derivability (which
would be a category error).

## What this proposal proposes

The proposal is to formalize `𝒞_b` as a **`convention_retained`**
row in the audit ledger, with the following attributes:

```yaml
proposed_audit_row:
  claim_id: convention_cb_governance_adoption_proposal_note_2026-05-26
  proposed_claim_type: governance_proposal
  proposed_effective_status: unaudited
  proposed_load_bearing_step_class: convention (sibling to bounded)
  scope: |
    The framework's natural angular unit on emergent angular
    observables on the C_N orbit is period-1 (cycle units). Under
    the standard-radian identification, 1 framework-rad ≡ 1 standard
    rad (literal, not 2π standard rad).
  governance_dependency:
    type: user_side
    description: |
      Adoption requires explicit user ratification recorded
      separately in the audit lane (analogous to how other retained
      unit conventions are governance-adopted).
  structural_dependency:
    upstream_anomaly_inheritance: |
      The translation lemma (PR #1963) establishes that under 𝒞_b
      ∧ (H_AFT), the framework's dimensionless invariant (N-1)/N²
      is read literally as δ_Brannen rad on the C_N orbit. The
      structural-consistency check verifies 𝒞_b does not contradict
      any retained content; the inheritance argument supplies the
      structural justification but does NOT supply the adoption.
  sibling_to:
    - lattice-spacing (canonical retained convention)
    - meter (SI retained convention)
    - Planck/natural (retained convention)
    - GeV (SI conventional energy unit)
```

This note **does not adopt** the convention. Adoption is a
user-side governance act recorded separately.

## Structural-consistency claims (audit-verifiable)

The following claims about `𝒞_b` are independent of whether it is
adopted; they document its **structural consistency** with the
framework's retained content:

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

## What this proposal claims and does NOT claim

**Claims (under audit-required scope):**

- `𝒞_b` is the precise statement above (period form / exponential
  map form / sibling-tier form, all equivalent).
- `𝒞_b` is structurally consistent with retained content (C1–C5).
- `𝒞_b` is a sibling-tier convention to existing retained unit
  conventions; the proposal asks for the same governance treatment
  those received.
- Adoption is **not asserted** here; adoption is a user-side act.

**Does NOT claim:**

- Does **not** derive `𝒞_b`. Convention selection is not a
  theorem-style derivation; the proposal is an adoption proposal,
  not a derivation.
- Does **not** assert that `𝒞_b` IS the right convention. The
  translation lemma supplies the structural inheritance argument
  under (H_AFT); the convention choice itself is the user's.
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
proposed_claim_type: governance_proposal
audit_required_before_effective_retained: true
audit_handoff_status: |
  Source-only governance-adoption proposal for the convention 𝒞_b
  (period-1 reading of the framework's natural angular unit on C_N
  orbits). Proposal does NOT adopt; adoption is a user-side
  governance act recorded separately.

  Audit-verifiable claims here are STRUCTURAL CONSISTENCY ONLY
  (C1-C5): well-definedness, no-contradiction with retained no_go,
  dimensional consistency, post-hoc empirical agreement (consistency
  check only), and the well-defined re-scaling to the period-2π
  surface. The structural inheritance argument (justifying WHY 𝒞_b
  is a natural choice) is the separate companion translation lemma
  (PR #1963).

  Independent audit lane decides verdict on the structural-
  consistency claims; user-side governance decides adoption.

new_audit_row:
  - claim_id: convention_cb_governance_adoption_proposal_note_2026-05-26
    proposed_claim_type: governance_proposal
    effective_status_proposal: unaudited
    governance_status_after_audit: |
      Even if audit clears C1-C5, this row remains a PROPOSAL until
      a separate user-ratification event (analogous to existing
      retained convention adoptions).
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
proposed_load_bearing_step_class: convention (governance, not derivation)
status_authority: independent audit lane (structural consistency)
                  + user-side governance (adoption)
no_existing_row_touched: true
no_verdict_predicted: true
no_axiom_extension: true
no_load_bearing_import: true
no_derivation_claim: true
no_adoption_claim: true
```
