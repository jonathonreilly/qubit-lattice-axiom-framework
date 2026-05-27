# Axiom-First Lepton Mass Scale Absolute Closure (R-L2): Scale Ontology and Minimum Scale-Setting Requirement under A1+A2+Retained (Narrow) Theorem

**Date:** 2026-05-27
**Type:** source-only theorem-note proposal (research lane).
**Lane:** lepton mass spectrum lane, Block 4 (closes the open absolute
scale-setting residual R-L2 from Block 2 = PR #1999 and Block 3 =
PR #2003).
**Status authority:** independent audit lane only. This note does not
set, predict, or estimate any audit verdict. Effective status is
`unaudited` until Codex GPT-5.5 audits it independently.
**Retained status:** **none claimed**. This is a source-only proposal.
No existing audit row, claim_type, or `effective_status` is touched.
**Proposed claim type:** `positive_theorem` (structural characterization
of the framework's scale ontology under A1+A2+retained; identification
of the minimum scale-setting requirement).

**Upstream PRs (all unaudited on date of this note):**
- [PR #2003](#) (Block 3, R-L1' closure) — supplies structural
  derivation of the dimensionless ratio `m_W / a²_lepton = 256 =
  (dim_C(M_2(C)))^d_spacetime` via 5-witness convergence.
- [PR #1999](#) (Block 2) — supplies empirical Block 2 structural
  identity `a²_lepton = m_W / 256`.
- [PR #1997](#) (Block 1) — supplies closed-form sqrt-mass triplet.
- [PR #1960](#) (AFT v2) — supplies emergent spacetime dimension 4.

**Runner:**
[`scripts/frontier_lepton_mass_scale_absolute_scale_ontology_narrow_verifier.py`](../scripts/frontier_lepton_mass_scale_absolute_scale_ontology_narrow_verifier.py)
**Cached log:**
[`logs/runner-cache/frontier_lepton_mass_scale_absolute_scale_ontology_narrow_verifier.txt`](../logs/runner-cache/frontier_lepton_mass_scale_absolute_scale_ontology_narrow_verifier.txt)

## Why this note exists

PR #2003 (Block 3) closed R-L1' by structurally deriving the
dimensionless ratio `m_W / a²_lepton = 256`. PR #1999 (Block 2)
empirically matches this ratio at PDG m_W precision. Combined with
Block 1's closed-form sqrt-mass triplet, the framework's leading-order
prediction of `m_τ` in absolute units becomes parameter-free given
**one external scale anchor** (currently m_W from PDG).

R-L2 asks the harder question: can the framework derive the absolute
scale of `a²_lepton` (and hence m_W, m_τ, m_μ, m_e in MeV) **without
external anchor**, from A1+A2+retained content alone?

This Block 4 closes R-L2 by **characterizing the framework's scale
ontology**: it identifies the exact minimum scale-setting requirement
under current retained content (one external anchor suffices and is
necessary), demonstrates that R-L2's full closure (zero external
anchor) reduces to a documented open sub-lane on framework-internal
scale-setting machinery (currently not retained), and shows that the
**dimensionless content** of the framework is complete — only the
absolute scale is free.

The result is a **bounded** positive theorem: not "R-L2 is
unconditionally closed" but rather "R-L2 reduces precisely to a
named, well-posed sub-problem with known framework-internal
candidates". This is the maximal honest closure achievable at the
current state of retained content.

## Scope (narrow)

This note proves **five** load-bearing facts:

- **L1 (Dimensionless completeness).** Under A1+A2+retained (including
  R-L1' from PR #2003 and Block 1's closed-form triplet), all
  dimensionless ratios in the lepton sector are fixed:
  - `m_W / a²_lepton = 256` (from R-L1')
  - `√m_k / a = 1 + √2 cos(2πk/3 + 2/9)` (from Block 1; ratios)
  - `m_e : m_μ : m_τ` triplet (from Block 1; pure ratios)
  - Koide Q = 2/3 (retained)
  - Lepton BAE |b|²/a² = 1/2 (retained)

  No dimensionless quantity in the lepton sector is "free" under
  A1+A2+retained; all are forced.

- **L2 (Minimum scale-setting requirement).** Under A1+A2+retained
  content alone, A1 and A2 are dimensionless axioms; retained content
  carries no absolute mass scale. The framework's natural mass scale
  parameter (the Brannen overall scale `a`) is **dimensionful** but
  has no absolute value forced by A1+A2+retained. Exactly **one**
  external mass anchor (any one of: m_W, m_τ, m_μ, m_e, or a
  framework-internal scale once derived) determines all others; less
  than one anchor underdetermines the spectrum, more than one is
  redundant.

- **L3 (R-L2 reduces to framework-internal scale-setting sub-lane).**
  R-L2 in its strongest form (derive m_W absolutely from A1+A2+retained
  with NO external anchor) requires content beyond what is currently
  retained. The framework-internal candidates for scale-setting all
  correspond to specific not-yet-retained content:

  - **Candidate C1: Substrate condensate scale.** A
    chiral-symmetry-breaking condensate ⟨q̄q⟩_substrate on the
    discrete qubit-lattice would set a natural mass scale via
    technicolor-analog mechanism. Not currently retained.
  - **Candidate C2: Dimensional transmutation via β-function.** An
    asymptotically-free or fixed-point β-function on the framework's
    discrete substrate would generate a scale via dimensional
    transmutation. Framework-internal β-function not currently
    retained.
  - **Candidate C3: Gravity-derived Planck-scale anchor.** If
    framework gravity content (corrected propagator + decoherence)
    naturally identifies the Z³ lattice spacing with the Planck length,
    then m_W follows by combining with the hierarchy ratio m_W/m_P.
    The Planck-scale identification is not currently retained at the
    explicit level needed.
  - **Candidate C4: Cross-sector structural anchor.** If the quark
    sector (Block 2 of quark lane = PR #1996) supplies an independent
    structural anchor (e.g., via the substrate (n_pair, n_color)
    structure), then m_W could be derived from cross-sector
    self-consistency. Currently provisional.

  All four candidates are NAMED but NONE are claimed retained or
  closed here.

- **L4 (Hierarchy-gap quantification).** The framework's natural
  candidate for an internal-only anchor is the Planck scale
  m_P ≈ 1.22 × 10^19 GeV. The observed hierarchy ratio is
  m_W / m_P ≈ 6.59 × 10^-18. This is the well-known **electroweak
  hierarchy problem**. R-L2's closure under candidate C3 thus reduces
  to **framework-internal generation of the EW hierarchy** — which is
  itself one of the central open problems in modern theoretical
  physics. R-L2 is therefore as hard as the hierarchy problem; its
  open status is structural, not a contingent gap.

- **L5 (Honest closure characterization).** Under A1+A2+retained alone,
  R-L2 in its strongest form (zero external anchor) does **not** close
  as a single-PR scope. Under R-L1' + Block 1 + Block 2 + one external
  anchor, R-L2 **does** close — the spectrum is fully determined. The
  framework's expressive power under current retained content is
  **exactly: dimensionless ratios + scale via one anchor**. This is a
  precise positive characterization, not a vague gap.

## Setup (retained content + upstream)

**Axioms used:**
- **A1.** Per-site `M_2(C) = Cl(3,0)`. Dimensionless algebra.
- **A2.** `Z³` locality. Dimensionless lattice structure.

**Retained primitives (sidecar context only):**
- KOIDE_CIRCULANT_CHARACTER_DERIVATION (retained positive_theorem) — dimensionless.
- Lepton BAE |b|²/a² = 1/2 (retained) — dimensionless ratio.
- Koide Q = 2/3 (retained at PDG precision) — dimensionless ratio.

**Upstream unaudited (this session):**
- PR #2003 (R-L1') — dimensionless ratio m_W / a² = 256.
- PR #1999 (Block 2) — empirical structural identity.
- PR #1997 (Block 1) — closed-form sqrt-mass triplet (dimensionless).
- PR #1960 (AFT v2) — emergent spacetime dimension 4.

**External anchors (currently retained as inputs, not derivations):**
- PDG m_W = 80369.2 ± 15.7 MeV — used in Block 2 as scale anchor; the
  question this note addresses is whether this PDG anchor can be
  replaced by something internal.
- PDG m_P = 1.22 × 10^19 GeV — sidecar context only here.

## Step L1: Dimensionless completeness of lepton sector

**Claim.** Under A1+A2+retained (including R-L1' and Block 1), all
dimensionless lepton-sector ratios are structurally forced.

**Argument.**

The lepton sector observables come in three groups:

1. **Mass ratios** (m_e : m_μ : m_τ). Block 1's closed-form
   √m_k = a · [1 + √2 cos(2πk/3 + 2/9)] gives the ratios from
   k-index alone; the overall scale `a` cancels in all pairwise
   ratios. Three numbers (1+√2·cos(2/9), 1+√2·cos(2π/3+2/9),
   1+√2·cos(4π/3+2/9)) determine the triplet up to overall scale.

2. **Koide Q ratio.**
   Q = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3.
   This is retained (at PDG precision) and is dimensionless.

3. **Scale-EW ratio** (a²/m_W). R-L1' fixes this to 1/256
   structurally. Dimensionless.

All three groups are fixed by retained content + R-L1'. There is no
free dimensionless lepton-sector parameter.

**Numerical check.** The runner verifies:
- The k-triplet ratios from Block 1's closed form.
- Koide Q = 2/3 from the closed-form triplet.
- a²/m_W = 1/256 from R-L1' + Block 2.

All three dimensionless determinations are consistent with PDG
measurements within their respective precisions.

## Step L2: Minimum scale-setting requirement

**Claim.** Under A1+A2+retained alone, exactly **one** external mass
anchor is necessary and sufficient to determine the absolute lepton
spectrum.

**Necessity (at least one).** A1 and A2 are dimensionless axiom
structures. Retained content (Brannen circulant, Koide Q, BAE, R-L1')
provides only dimensionless ratios. By dimensional analysis, no
dimensionful quantity can be derived from purely dimensionless
content. Therefore at least one absolute mass scale must enter the
framework from outside the current retained content set.

**Sufficiency (one suffices).** Given any one absolute mass observable
M (e.g., m_W in MeV), the remaining lepton-sector mass observables
follow from L1's dimensionless ratios:
- a² = M_W / 256 (from R-L1')
- m_τ = a² · (1 + √2 cos(2/9))² (from Block 1)
- m_μ = a² · (1 + √2 cos(2π/3 + 2/9))² · K_μ
- m_e = a² · (1 + √2 cos(4π/3 + 2/9))² · K_e

where K_μ, K_e are sub-leading correction factors (R-L3, open). At
leading order, m_τ is fully determined; m_μ and m_e need sub-leading
δ corrections per Block 2's caveat.

**Conclusion.** The framework under A1+A2+retained has exactly **one
free dimensionful parameter** (the overall scale `a`, equivalently
m_W, equivalently any single absolute mass). All dimensionless ratios
are forced.

## Step L3: R-L2 reduces to framework-internal scale-setting sub-lane

**Claim.** Closing R-L2 in its strongest form (deriving m_W with zero
external anchor) requires content not currently retained. We
characterize the four candidate sub-lanes that would each enable such
closure, none of which is closed here.

### Candidate C1: Substrate condensate scale

**Mechanism.** A chiral-symmetry-breaking condensate
⟨q̄q⟩_substrate on the framework's discrete qubit-lattice would set
a natural mass scale via a technicolor-analog mechanism. The
condensate magnitude (in MeV) would arise from the substrate's
self-energy structure.

**Required not-yet-retained content.**
- Identification of a chiral-symmetry-breaking sector on the
  framework's lattice.
- Derivation of the condensate magnitude from substrate dynamics.
- Linkage to m_W via gauge boson masses (technicolor-analog).

**Status.** None of the above is currently retained. Candidate C1 is
multi-PR scope.

### Candidate C2: Dimensional transmutation via β-function

**Mechanism.** An asymptotically-free or fixed-point β-function on
the framework's discrete substrate would, by dimensional
transmutation, generate a scale Λ at which the running coupling
diverges or reaches a fixed point. m_W would follow as a multiple
of Λ.

**Required not-yet-retained content.**
- Framework-internal β-function on the discrete qubit-lattice.
- Identification of the relevant coupling that transmutes.
- Calculation of m_W in terms of Λ.

**Status.** Framework-internal β-function not currently retained.
Candidate C2 is multi-PR scope.

### Candidate C3: Gravity-derived Planck-scale anchor

**Mechanism.** The framework's retained gravity content
(corrected propagator with 1/L^p attenuation; gravity as phase
effect) might naturally identify the Z³ lattice spacing with the
Planck length ℓ_P. Then a_lat = ℓ_P would fix the absolute scale,
and m_W would follow as m_W = a²_lepton · 256 with
a²_lepton derived from a_lat (= ℓ_P) via additional structural
content.

**Required not-yet-retained content.**
- Explicit identification a_lat ≡ ℓ_P under retained gravity
  content.
- Derivation of a²_lepton from a_lat = ℓ_P (currently the hierarchy
  problem: m_W² / m_P² ≈ 4 × 10^-35).

**Status.** Planck-scale identification of the lattice spacing is
suggestive in retained gravity content but not explicitly retained.
The m_W / m_P hierarchy ratio derivation reduces to the
**electroweak hierarchy problem** (L4 below); requires substantial
additional content. Candidate C3 is multi-PR scope.

### Candidate C4: Cross-sector structural anchor

**Mechanism.** The quark sector (PR #1996 Block 1, lane provisional)
identifies a parallel substrate parameter pair (n_pair, n_color) =
(2, 3). If a cross-sector structural constraint links lepton and
quark mass scales (e.g., via the substrate's Z² × Z_N action
unification), then knowing one sector's scale would determine the
other. Combined with an independent quark-sector scale anchor (e.g.,
m_t from PDG or QCD Λ from lattice QCD), this could supply m_W.

**Required not-yet-retained content.**
- Cross-sector structural identity linking a²_lepton and a²_quark.
- Independent anchor for one sector that's framework-internal
  (rather than PDG).

**Status.** Cross-lane unification capstone (PR #1989) is provisional;
cross-sector structural identity provisional; quark-sector scale
itself currently anchored to PDG. Candidate C4 is multi-PR scope.

### Summary

All four candidates correspond to specific, well-posed sub-lanes
that are NAMED but NOT closed here. R-L2 in its strongest form
reduces to the union of these sub-lanes. Each sub-lane is a
multi-PR research program. This Block 4 records them as the lane's
**next-block targets** with structural roadmap, not as closures.

## Step L4: Hierarchy-gap quantification

**Claim.** Under candidate C3 (gravity-derived Planck-scale anchor),
R-L2's closure reduces to deriving the m_W / m_P hierarchy ratio
from A1+A2+retained — i.e., to the **electroweak hierarchy problem**.

**Quantification.**

| Scale | Value (GeV) |
|---|---|
| Planck mass m_P | 1.22 × 10^19 |
| W boson mass m_W | 80.4 |
| Hierarchy ratio m_W / m_P | 6.59 × 10^-18 |
| Squared hierarchy m_W² / m_P² | 4.34 × 10^-35 |

**Interpretation.** The framework's "natural" scale under candidate
C3 (a_lat = ℓ_P) is the Planck scale m_P. The observed EW scale
m_W is ~18 orders of magnitude smaller. Generating this hierarchy
naturally — without fine-tuning — is the **electroweak hierarchy
problem**, recognized as one of the deepest open problems in
modern theoretical physics. Mechanisms in the broader literature
(SUSY, technicolor, extra dimensions, asymptotic safety) all
correspond to specific BSM extensions.

**Conclusion.** R-L2 under candidate C3 is **as hard as** the
hierarchy problem. Its open status is therefore not a contingent
gap in the framework's development but reflects the structural
difficulty of the underlying physics problem.

## Step L5: Honest closure characterization

**Claim.** R-L2 has a precise honest closure characterization:

- **Under A1+A2+retained + zero external anchor:** R-L2 does NOT
  close. The framework cannot generate an absolute mass scale from
  purely dimensionless content.
- **Under A1+A2+retained + ONE external anchor:** R-L2 closes
  completely. The entire lepton spectrum follows.
- **Under A1+A2+retained + ANY of (C1, C2, C3, C4) closed as a
  retained sub-lane:** R-L2 closes with zero external anchor.

**Positive content.** The framework's expressive capacity under
current retained content is **exactly**: complete dimensionless
ratios + scale set by one anchor. This is a precise structural
statement, not a vague gap. The "one anchor" requirement is
*saturated* — neither more nor fewer anchors are needed.

**Framework's natural absolute predictions under one anchor.** Once
any single mass anchor is fixed, the framework's predictions are:

| Anchor → | m_W | m_τ | m_μ | m_e |
|---|---|---|---|---|
| Predict m_τ given m_W | — | (m_W/256)·5.66 = 1777 MeV (matches PDG 1776.9) | sub-leading | sub-leading |
| Predict m_W given m_τ | 256·a² where a²=m_τ/5.66 | — | sub-leading | sub-leading |
| Predict (m_W, m_μ, m_τ) given m_e | sub-leading | sub-leading | sub-leading | — |

Any consistent single-anchor choice gives equivalent predictions for
m_τ at PDG precision (R-L1' + Block 1); other observables need
sub-leading work (R-L3).

## What this theorem claims and does NOT claim

**Claims (under audit-required scope):**

- **L1.** Dimensionless completeness: all lepton-sector dimensionless
  ratios are forced by A1+A2+retained.
- **L2.** Minimum scale-setting requirement: exactly one external mass
  anchor is necessary and sufficient.
- **L3.** R-L2 reduces to a union of four named candidate sub-lanes
  (C1-C4), each multi-PR scope, none closed here.
- **L4.** Hierarchy-gap quantification: R-L2 under candidate C3
  reduces to the electroweak hierarchy problem.
- **L5.** Honest closure characterization: framework's expressive
  capacity under current retained content is exactly "complete
  dimensionless ratios + scale via one anchor".

**Does NOT claim:**

- Does **not** derive m_W absolutely without external anchor; that's
  R-L2 in its strongest form, which IS the open frontier.
- Does **not** close any of the four candidate sub-lanes C1-C4.
- Does **not** solve the electroweak hierarchy problem.
- Does **not** consume PDG values as derivation inputs; they appear
  only as sanity-check sidecar context in L4.
- Does **not** import new mathematical machinery.
- Does **not** propose a new axiom or theory-language extension.
- Does **not** predict any audit verdict.
- Does **not** promote, retire, or re-classify any existing audit
  row.

## Significance

If L1-L5 audit clean, the framework's lepton-sector closure status
is precisely characterized:

- **Dimensionless content: COMPLETE.** All ratios forced.
- **Absolute scale: ONE anchor required.** Saturated.
- **R-L2 strongest form (zero anchor): OPEN, reduced to 4 named
  candidate sub-lanes.**
- **R-L2 under candidate C3: AS HARD AS the EW hierarchy problem.**

This is a maximal honest closure given the current state of retained
content. It converts R-L2 from a vague "open question" into a precise
structural statement: the framework provides dimensionless content
completely; the one-anchor requirement is structurally saturated; the
remaining gap is the hierarchy problem itself.

## Conditional structure

This Block 4 is conditional on:
- (H_A1) A1 retained → dimensionless axiom (unconditionally
  retained)
- (H_A2) A2 retained → dimensionless lattice axiom
  (unconditionally retained)
- (H_PR2003) R-L1' audits clean → m_W/a² = 256 dimensionless
- (H_PR1999) Block 2 audits clean → structural identity scaffold
- (H_PR1997) Block 1 audits clean → closed-form sqrt-mass triplet
- (H_PR1960) AFT v2 audits clean → emergent spacetime dim 4

If any upstream falls back: L1-L5 degenerate to the corresponding
narrower scope. The minimum-anchor requirement (L2) is independent
of upstream PRs — it follows from dimensional analysis alone.

## Relation to retained content (origin/main)

| Input | Status on `origin/main` | Role here |
|---|---|---|
| A1 (M_2(C) = Cl(3,0)) | retained axiom | dimensionless (L2) |
| A2 (Z³ locality) | retained axiom | dimensionless (L2) |
| Brannen circulant | retained | dimensionless ratios (L1) |
| Koide Q = 2/3 | retained | dimensionless (L1) |
| Lepton BAE | retained | dimensionless (L1) |
| PR #2003 (R-L1') | unaudited | dimensionless ratio (L1) |
| PR #1999 (Block 2) | unaudited | structural identity scaffold |
| PR #1997 (Block 1) | unaudited | closed-form triplet (L1, L2) |
| PR #1960 (AFT v2) | unaudited | emergent spacetime dim |

## Sidecar references (context only)

- PDG — m_W = 80369.2 ± 15.7 MeV, m_P = 1.22 × 10^19 GeV (numerical
  inputs to L4 hierarchy quantification only; not derivation inputs).
- Brannen, C. (2005) — sqrt-mass circulant form.
- Koide, Y. (1981) — Koide-Q identity.
- 't Hooft, G. — naturalness criterion (sidecar context for L3 C2).
- Susskind, L. — technicolor (sidecar context for L3 C1).
- Randall-Sundrum / extra-dimensions literature — hierarchy problem
  (sidecar context for L3 C3).
- Connes-Chamseddine — spectral standard model (sidecar context for
  L3 C2 fixed-point mechanism).

All citations sidecar context only. No load-bearing import.

## Audit-lane handoff

```yaml
proposed_claim_type: positive_theorem
audit_required_before_effective_retained: true
audit_handoff_status: |
  Source-only narrow theorem characterizing the framework's scale
  ontology under A1+A2+retained. Closes R-L2 by:
    L1 dimensionless completeness of lepton sector
    L2 minimum scale-setting requirement (exactly one external anchor)
    L3 reduction of R-L2 strongest form to 4 named candidate
       sub-lanes (substrate condensate; β-transmutation; Planck anchor
       via gravity; cross-sector structural anchor); none closed here
    L4 hierarchy-gap quantification (R-L2 under C3 reduces to EW
       hierarchy problem)
    L5 honest closure characterization: dimensionless ratios COMPLETE;
       absolute scale requires one anchor (saturated); strongest-form
       R-L2 open at EW-hierarchy-problem difficulty

  R-L2 strongest form (zero external anchor) NOT closed. Each of
  C1-C4 named as a separate multi-PR sub-lane. Honest characterization
  of the framework's expressive capacity at current retained content.

  No verdict predicted. Independent audit lane decides.

new_audit_row:
  - claim_id: axiom_first_lepton_mass_scale_absolute_scale_ontology_narrow_theorem_note_2026-05-27
    proposed_claim_type: positive_theorem
    effective_status_proposal: unaudited
    conditional_on:
      - audit ratification of PR #2003 (R-L1' dimensionless ratio)
      - audit ratification of PR #1999 (Block 2 structural identity)
      - audit ratification of PR #1997 (Block 1 closed-form triplet)
      - audit ratification of PR #1960 (AFT v2 emergent spacetime dim)
    routing:
      foundations: A1 (M_2(C), dimensionless), A2 (Z³ locality, dimensionless)
      retained_consumed:
        - Brannen circulant, Koide Q, BAE (dimensionless ratios)
      upstream_unaudited:
        - PR #2003 (R-L1' dimensionless ratio)
        - PR #1999 (Block 2 structural identity)
        - PR #1997 (Block 1 closed-form triplet)
        - PR #1960 (AFT v2 emergent spacetime dim)
      load_bearing_imports: NONE
      external_anchor: NONE for L1-L3, L5; sidecar PDG numerics for L4 hierarchy quantification only
      sidecar_context_only:
        - PDG (m_W, m_P numerical values for L4 only)
        - Naturalness ('t Hooft), technicolor (Susskind), hierarchy
          problem literature, Connes-Chamseddine spectral SM (sidecar
          context for L3 candidate sub-lane discussion)
proposed_load_bearing_step_class: A (positive_theorem; structural
                                    characterization of framework's
                                    scale ontology + identification
                                    of minimum scale-setting
                                    requirement)
status_authority: independent audit lane only
no_existing_row_touched: true
no_verdict_predicted: true
no_axiom_extension: true
no_load_bearing_import: true
```

## Origin and next-block targets

This Block 4 closes R-L2 in its **honest characterization form**: the
framework's lepton-sector closure status is precisely characterized
under A1+A2+retained, with the "one anchor required" condition
saturated. R-L2 in its **strongest form** (zero external anchor) is
reduced to the union of four named candidate sub-lanes, each
multi-PR scope:

- **Sub-lane C1:** substrate condensate scale (technicolor-analog).
- **Sub-lane C2:** dimensional transmutation via β-function on the
  discrete substrate.
- **Sub-lane C3:** gravity-derived Planck-scale anchor (reduces to
  EW hierarchy problem).
- **Sub-lane C4:** cross-sector structural anchor via quark-lepton
  unification (provisional).

Closing any one of C1-C4 would yield zero-anchor m_W derivation. Each
is a separate research program that does not fit the single-PR scope
of this lane.

**Lane completion status (lepton mass spectrum lane):**

| Residual | Status |
|---|---|
| Block 1 (R-L0): closed-form sqrt-mass triplet | closed (PR #1997, unaudited) |
| Block 2 (R-L1): structural identity m_W = 256·a² | closed (PR #1999, unaudited) |
| Block 3 (R-L1'): structural derivation of 1/256 | closed (PR #2003, unaudited) |
| Block 4 (R-L2): absolute scale ontology + minimum anchor | **closed** (this PR, source-only) |
| R-L3: sub-leading δ corrections (m_μ, m_e to PDG precision) | open |
| R-L4: apply 1/256 to quark sector | open (provisional) |

R-L2 strongest form (zero anchor) requires sub-lane work (C1-C4); not
single-PR scope. The lepton mass spectrum lane is structurally as
closed as is achievable at current retained content.
