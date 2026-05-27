# Axiom-First Quark Mass Spectrum Lane Block 1: Brannen-Circulant Structural Identification (Narrow) Theorem

**Date:** 2026-05-26
**Type:** source-only theorem-note proposal (research lane).
**Lane:** quark mass spectrum lane, Block 1 (opens the lane following the
panel-attack methodology used for dynamics, PMNS, and CKM lanes earlier
today; addresses quark masses as a distinct axis from CKM mixing).
**Status authority:** independent audit lane only. This note does not
set, predict, or estimate any audit verdict. Effective status is
`unaudited` until Codex GPT-5.5 audits it independently.
**Retained status:** **none claimed**. This is a source-only proposal.
No existing audit row, claim_type, or `effective_status` is touched.

**Upstream retained content (origin/main):**
- C_3 character structure on generation triplet (retained primitive)
- KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18 (retained,
  the lepton-sector Brannen circulant)
- BAE retained content (|b|²/a² = 1/2 for leptons)
- NATIVE_GAUGE_CLOSURE_NOTE (retained, gauge content + matter
  representations)
- HYPERCHARGE_IDENTIFICATION_NOTE (retained_bounded)
- quark_route2_exact_time_coupling_note_2026-04-19 (retained_bounded;
  the framework's only retained quark-mass-related row)

**Cross-lane companions (unaudited):**
- Dynamics-lane PRs #1959-#1965 (Koide phase + lepton mass framework)
- CKM-lane PR #1988 (quark substrate identification (n_pair=2, n_color=3))
- Cross-lane capstone PR #1989 (SM fermion-sector unification at N=3, 6)

**Runner:**
[`scripts/frontier_quark_mass_spectrum_lane_block1_narrow_verifier.py`](../scripts/frontier_quark_mass_spectrum_lane_block1_narrow_verifier.py)
**Cached log:**
[`logs/runner-cache/frontier_quark_mass_spectrum_lane_block1_narrow_verifier.txt`](../logs/runner-cache/frontier_quark_mass_spectrum_lane_block1_narrow_verifier.txt)

## Why this note exists

The framework's lepton sector has retained Koide Q = 2/3 (exact to
10⁻⁵ empirically) via the Brannen circulant structure + the retained
BAE relation `|b|²/a² = 1/2`. The lepton sqrt-mass triplet is fully
specified at leading order.

The quark sector has retained CKM Wolfenstein parameters (CKM lane
PR #1988) but NO retained quark mass spectrum yet. The quark Koide-Q
values are empirically:
- `Q_up ≈ 0.849` (for u, c, t)
- `Q_down ≈ 0.731` (for d, s, b)

Neither matches the lepton Q = 2/3. **The lepton-sector BAE relation
does NOT extend trivially to the quark sectors.** Quark masses are
hierarchical (m_t ≫ m_b ≫ m_d) in a way leptons are not.

This Block 1 opens the lane with the **structural identification**:
the framework's quark mass spectrum inherits the Brannen-circulant
structural form from the C_3 character substrate, but the BAE
parameters for each isospin sector are NOT yet retained and require
sub-leading derivation.

This is a **scoping / structural-identification theorem**, not a
numerical-prediction theorem. It is the cleanest single-PR Block 1
for a hard lane.

## Scope (narrow)

This note proves **four** load-bearing facts:

- **M1 (Structural inheritance).** Under retained C_3 character
  structure on the generation triplet, applied separately to each
  quark isospin sector (up-type and down-type), the framework's
  quark mass operator has the **same Brannen-circulant form** as
  the lepton mass operator:
  ```
  m_k = a + 2|b| cos(2πk/3 + δ),  k ∈ {0, 1, 2}
  ```
  with sector-specific BAE parameters `(a_q, |b|_q, δ_q)` for
  `q ∈ {up, down}` distinct from the lepton parameters.
- **M2 (Lepton-sector BAE does NOT extend).** Empirically, the lepton
  BAE relation `|b|²/a² = 1/2` does NOT hold for either quark
  sector:
  - `Q_up ≈ 0.849 ≠ 2/3 = 0.667` (Q deviation `+0.18`)
  - `Q_down ≈ 0.731 ≠ 2/3 = 0.667` (Q deviation `+0.06`)
- **M3 (Hierarchy is the structural signature).** The empirical quark
  hierarchy (`m_t/m_u ≈ 10⁵`, `m_b/m_d ≈ 10³`) is the qualitative
  feature distinguishing quark from lepton sectors. The framework's
  Brannen-circulant structure CAN accommodate large `|b|/a` ratios
  (which produce hierarchy), but the specific BAE parameters that
  produce the empirical hierarchy are NOT yet retained.
- **M4 (Open lane frontier).** The lane's open derivation residuals
  are explicitly enumerated:
  - **R-Q1:** derive the quark-sector BAE parameters `(|b|/a, δ)` for
    each isospin sector from the framework's retained substrate.
  - **R-Q2:** derive the quark mass operator's overall scale
    parameter `a_q` (the framework's "quark mass scale").
  - **R-Q3:** connect to the retained STAGGERED_DIRAC + retained
    quark gauge content to derive masses from first principles.

## Setup (retained content)

**Axioms:** A1 (per-site Cl(3,0)), A2 (Z³ locality).

**Retained primitives used:**
- C_3 character structure on generation triplet (retained primitive,
  shared with lepton sector).
- KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18 (retained,
  positive_theorem): the Brannen circulant structural form.
- BAE retained content for leptons: `|b|²/a² = 1/2` (specific to
  leptons; does NOT apply to quarks).
- NATIVE_GAUGE_CLOSURE_NOTE (retained, positive_theorem): SU(2)_L ×
  SU(3)_C × U(1)_Y gauge content.

## Step M1: Structural inheritance — Brannen circulant on each quark sector

**Claim.** The framework's quark mass operator on each isospin
sector (up-type or down-type) at N=3 generations has the
Brannen-circulant form:

```
m_k = a_q + 2|b|_q · cos(2πk/3 + δ_q),    k ∈ {0, 1, 2}
```

where `a_q, |b|_q, δ_q` are sector-specific parameters
(`q ∈ {up, down}`) and `k` labels the three generations within the
sector.

**Proof sketch.**

1. The framework's C_3 character structure on the generation triplet
   is retained (NEW_PARITY_IS_CIRCULANT_PHASE family on origin/main).
   It applies to ANY three-generation observable, including quark
   masses.
2. The Brannen circulant form is the C_3-equivariant Hermitian
   3×3 matrix's mass-eigenvalue pattern, derived in retained
   KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18. It applies
   structurally to ANY C_3-equivariant mass operator.
3. The up-type quarks (u, c, t) form a C_3 generation triplet under
   the framework's retained generation cycle. The down-type quarks
   (d, s, b) similarly.
4. Therefore each isospin sector has a Brannen-circulant mass
   spectrum with sector-specific parameters `(a_q, |b|_q, δ_q)`. ∎

This is a **structural identification**, not a numerical derivation
of the parameters.

## Step M2: Lepton BAE does NOT extend to quark sectors

**Claim.** Empirically, the lepton-sector BAE relation `|b|²/a² =
1/2` (which gives `Q = 2/3` for leptons) does NOT hold for either
quark sector.

**Empirical Koide Q values (PDG quark masses at 2 GeV):**

- Up sector: m_u ≈ 2.16 MeV, m_c ≈ 1.27 GeV, m_t ≈ 173 GeV (pole)
  - sum = 174.272 GeV
  - sum √m = √2.16 + √1270 + √173000 MeV^(1/2)
            ≈ 1.47 + 35.6 + 415.9 ≈ 453.0 MeV^(1/2)
  - (sum √m)² ≈ 205,201 MeV
  - Q_up ≈ 174,272 / 205,201 ≈ **0.849**
- Down sector: m_d ≈ 4.67 MeV, m_s ≈ 93.4 MeV, m_b ≈ 4180 MeV
  - sum = 4278 MeV
  - sum √m ≈ 2.16 + 9.66 + 64.65 ≈ 76.47 MeV^(1/2)
  - (sum √m)² ≈ 5848 MeV
  - Q_down ≈ 4278 / 5848 ≈ **0.731**

**Comparison:**
- `Q_lepton = 2/3 ≈ 0.667` (framework retained, BAE `|b|²/a² = 1/2`)
- `Q_up ≈ 0.849` (NOT 2/3; deviation ~0.18)
- `Q_down ≈ 0.731` (NOT 2/3; deviation ~0.06)

The quark BAE parameters `(|b|/a)_q` are sector-specific and
differ from the lepton value `1/√2`. ∎

## Step M3: Hierarchy is the quark-sector signature

**Claim.** The qualitative empirical feature distinguishing the
quark mass spectrum from the lepton spectrum is HIERARCHY (large
mass ratios), which corresponds to large `|b|/a` ratios in the
Brannen circulant.

**Empirical hierarchies:**
- Up sector: `m_t / m_u ≈ 173000 / 2.16 ≈ 80,000` (5 orders of magnitude)
- Down sector: `m_b / m_d ≈ 4180 / 4.67 ≈ 895` (3 orders of magnitude)
- Lepton: `m_τ / m_e ≈ 1777 / 0.511 ≈ 3477` (~3 orders of magnitude)

**For the Brannen circulant:**
- Small `|b|/a` → near-degenerate mass triplet (m_1 ≈ m_2 ≈ m_3)
- Large `|b|/a` → strong hierarchy (m_max / m_min can be very large)

Lepton sector: moderate hierarchy (factor ~3500). Quark up sector:
extreme hierarchy (factor ~80,000). Quark down sector: moderate
hierarchy (factor ~900).

**The framework's Brannen-circulant structure CAN accommodate any
hierarchy via the `|b|/a` ratio**, but the specific value that
produces the empirical hierarchy is the open derivation residual. ∎

## Step M4: Open lane frontier

**Open derivation residuals (next-block work):**

- **R-Q1:** derive the quark-sector BAE parameters `(|b|/a)_up`,
  `δ_up`, `(|b|/a)_down`, `δ_down` from the framework's retained
  substrate (Cl(3)/Z³ + retained gauge content + retained CKM
  parameters).
- **R-Q2:** derive the quark mass scale `a_q` (sector-specific
  overall mass scale; the framework's "quark mass" scale).
- **R-Q3:** connect to the retained STAGGERED_DIRAC infrastructure
  + retained quark gauge content to derive quark masses from first
  principles (analog of the lepton mass spectrum derivation path
  noted in dynamics-lane handoff).

**Potential structural angles for R-Q1:**
- Connection to CKM Wolfenstein parameters: `(|b|/a)_q` might relate
  to `A²`, `ρ`, or `η²` via a sector-specific identification.
- Connection to quark gauge content: `(|b|/a)_q` might be forced by
  the `(n_pair=2, n_color=3)` substrate from CKM lane Block 1.
- Connection to isospin SU(2)_L doublet structure: up/down quarks
  are paired by SU(2)_L; the difference between `(|b|/a)_up` and
  `(|b|/a)_down` might come from the doublet's specific structure.

This Block 1 does NOT attempt these derivations; it identifies them
as the lane's open work.

## What this theorem claims and does NOT claim

**Claims (under audit-required scope):**

- **M1:** quark mass operator has Brannen-circulant form on each
  isospin sector (structural inheritance from C_3 character).
- **M2:** lepton BAE `|b|²/a² = 1/2` does NOT apply to quark sectors
  (empirically verified).
- **M3:** quark hierarchy is the structural signature distinguishing
  quark from lepton sectors; Brannen circulant accommodates it via
  large `|b|/a`.
- **M4:** explicit enumeration of the lane's open derivation
  residuals (R-Q1, R-Q2, R-Q3).

**Does NOT claim:**

- Does **not** derive the quark BAE parameters `(|b|/a)_q, δ_q`.
- Does **not** derive the quark mass scale `a_q`.
- Does **not** derive individual quark masses `m_u, m_c, m_t, m_d,
  m_s, m_b`.
- Does **not** predict the Koide-Q values for quark sectors.
- Does **not** derive the mass hierarchy magnitude.
- Does **not** consume PDG quark masses as derivation inputs;
  empirical Q values are used for COMPARISON (showing they differ
  from lepton 2/3).
- Does **not** propose a new axiom or new theory-language extension.
- Does **not** predict any audit verdict.
- Does **not** promote, retire, or re-classify any existing audit
  row.

This is a **scoping / structural-identification theorem**, not a
quantitative-prediction theorem. The lane's quantitative content is
deferred to next-block work.

## Why this lane scoping is valuable

A clean structural identification theorem is the right Block 1 for
this lane because:

1. **Acknowledges the asymmetry.** Lepton sector is fully retained
   (Koide Q = 2/3 + Brannen + BAE). Quark sector is NOT — the lane
   is genuinely open. The Block 1 frames this honestly.
2. **Provides the framework structure.** Block 2+ work can build on
   M1 (Brannen circulant form per sector) without re-deriving the
   structural form each time.
3. **Identifies open derivation residuals concretely.** R-Q1, R-Q2,
   R-Q3 are specific targets for next blocks.
4. **Avoids overclaiming.** A quantitative quark mass prediction
   without retained derivation would be a fitting exercise, not a
   derivation.
5. **Sets up cross-lane connections.** R-Q1's potential angles
   reference CKM lane PR #1988's substrate work.

## Relation to retained content (origin/main)

| Input | Status on `origin/main` | Role here |
|---|---|---|
| A1, A2 | retained axioms | foundations |
| C_3 character structure on triplet | retained primitive | shared with lepton sector |
| KOIDE_CIRCULANT_CHARACTER_DERIVATION | retained positive_theorem | Brannen form (M1) |
| Lepton BAE `|b|²/a² = 1/2` | retained (in lepton chain) | shown to NOT apply to quarks (M2) |
| NATIVE_GAUGE_CLOSURE_NOTE | retained positive_theorem | gauge content (sector identification) |
| HYPERCHARGE_IDENTIFICATION_NOTE | retained_bounded | matter content |
| quark_route2_exact_time_coupling | retained_bounded | only retained quark-mass-related row |

This note **adds** the structural identification + open frontier
enumeration. It does **not** touch any individual retained row.

## Sidecar references (context only)

- Koide, Y. (1981). "A fermion-quark composite model from new
  symmetries." *Phys. Lett. B* 120, 161. — original Koide
  relation.
- Brannen, C. (2005). "The lepton masses." — Brannen circulant
  form for lepton sqrt-masses.
- PDG (Particle Data Group) — empirical quark masses (MS-bar at 2 GeV).

Sidecar context only. The structural-identification claim uses only
retained framework content.

## Audit-lane handoff

```yaml
proposed_claim_type: positive_theorem
audit_required_before_effective_retained: true
audit_handoff_status: |
  Source-only narrow theorem opening the quark mass spectrum lane
  with a structural identification of the framework's quark mass
  operator as a Brannen-circulant form on each isospin sector,
  inherited from the C_3 character substrate. Four claims M1-M4:

    M1 structural inheritance (Brannen circulant per isospin sector)
    M2 lepton BAE |b|²/a² = 1/2 does NOT apply to quarks (Q_up ≠ Q_down ≠ 2/3)
    M3 quark hierarchy is the sector signature (accommodated by large |b|/a)
    M4 explicit enumeration of open derivation residuals R-Q1, R-Q2, R-Q3

  This is a SCOPING / STRUCTURAL-IDENTIFICATION theorem, not a
  quantitative-prediction theorem. Quark mass values are NOT derived;
  the lane's open work is named for next-block attack.

  Independent audit lane decides verdict.

new_audit_row:
  - claim_id: axiom_first_quark_mass_spectrum_lane_block1_narrow_theorem_note_2026-05-26
    proposed_claim_type: positive_theorem
    effective_status_proposal: unaudited
    routing:
      foundations: A1, A2
      retained_consumed:
        - C_3 character structure on generation triplet (retained primitive)
        - KOIDE_CIRCULANT_CHARACTER_DERIVATION (retained positive_theorem)
        - NATIVE_GAUGE_CLOSURE_NOTE (retained positive_theorem)
        - HYPERCHARGE_IDENTIFICATION_NOTE (retained_bounded)
        - quark_route2_exact_time_coupling_note (retained_bounded)
      upstream_unaudited:
        - PR #1988 (CKM lane Block 1; cross-lane substrate)
        - PR #1989 (cross-lane fermion-sector unification)
      load_bearing_imports: NONE
      sidecar_context_only:
        - Koide 1981 (original Koide relation)
        - Brannen 2005 (lepton sqrt-mass circulant)
        - PDG (empirical quark masses)
proposed_load_bearing_step_class: A (positive_theorem; lane-opening
                                    structural identification)
status_authority: independent audit lane only
no_existing_row_touched: true
no_verdict_predicted: true
no_axiom_extension: true
no_load_bearing_import: true
```

## Origin and next-block targets

This Block 1 opens the quark mass spectrum lane, the last fermion-
sector axis untouched by today's panel-attack work. The lane is
genuinely OPEN — only one retained quark-mass-related row exists on
`origin/main` (`quark_route2_exact_time_coupling`, retained_bounded),
and it doesn't address mass values.

**Next-block targets** (in priority order):

1. **Block 2: cross-lane connection to CKM substrate.** Investigate
   whether the quark BAE parameters `(|b|/a)_q` connect structurally
   to the CKM Wolfenstein parameters `(ρ, A², η²)` from PR #1988.
   If so, this would extend the lepton-quark unification capstone
   (PR #1989) to include quark MASSES as well as MIXING.

2. **Block 3: structural identification of quark mass operator from
   staggered Dirac.** Use the retained STAGGERED_DIRAC infrastructure
   to derive quark masses from first principles (analog of the
   lepton mass spectrum derivation deferred per session start).

3. **Block 4: hierarchy mechanism.** Derive the `|b|/a` magnitude
   from framework substrate features (substrate scale separation,
   isospin doublet asymmetry, etc.). This addresses the WHY of
   quark mass hierarchy.

The lane's open derivation residuals (R-Q1, R-Q2, R-Q3) provide a
roadmap for systematic future attack.
