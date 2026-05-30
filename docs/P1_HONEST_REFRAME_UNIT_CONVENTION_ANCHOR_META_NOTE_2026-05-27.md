# P1 Honest Reframe: One Anchor Is Universally Required (Buckingham-π); Adopt Convention via Established Pipeline

**Date:** 2026-05-27
**Type:** source-only meta proposal.
**Claim type:** `meta` (repo-semantics reclassification proposal; no
new physics theorem, no new audit row promotion, no axiom extension).
**Status authority:** independent audit lane only. Pipeline-derived
status is generated only after the independent audit lane reviews this
proposal, its dependency chain, and its runner. The `meta` label above
is a source-side classification, not an audit verdict.

**Authority disclaimer.** This is a source-note proposal. It does NOT:
- Write or predict any audit verdict.
- Promote any downstream theorem.
- Add an axiom or modify A1, A2, or any retained theorem.
- Change admission counts on the existing surface.
- Cite PDG as a derivation input.
- Make any new numerical claim about M_Planck, m_W, v_EW, α_LM, or
  any framework primitive.

This note's sole purpose is **semantic**: clarifying the kind of open
admission that "M_Pl as conventional anchor" (`P1` in the EW hierarchy
chain) actually is, and routing its disposition through the
established convention-adoption pipeline rather than the
theorem-audit pipeline.

## 0. Why this note exists

Two lanes on `origin/main` carry an open admission for M_Pl as an
external scale anchor:

- `PLANCK_FROM_STRUCTURE_PATH_OPENING_META_NOTE_2026-05-10.md` lists
  "conventional scale anchors" at "1 pre-round, 0 conditionally
  post-round" (the conditional being subject to independent audit
  ratification + substep-4 staggered-Dirac closure + G_Newton
  admissions).
- The EW hierarchy lane carries the bounded numerical match
  `v = M_Pl · (7/8)^(1/4) · α_LM^16 ≈ 246.28 GeV` against PDG
  `v_obs = 246.22 GeV` (Δ = +0.0255%), with M_Pl named as `P1` of four
  open primitives (`P1`-`P4`).

Recent panel work (2026-05-27) on the lepton mass spectrum lane
identified that the cross-chain consistency between the lepton chain
(R-L1' + R-L2 sub-leading) and the EW hierarchy chain absorbs `P2`,
`P3`, `P4`, leaving `P1` (= M_Pl anchor in the EW hierarchy chain
vocabulary) as the single remaining admission for an absolute m_W
prediction.

**Crucial alignment with the existing Tier-A registry.** The framework
already maintains `docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`
(meta, audit-lane sidecar) + `docs/audit/data/tier_a_admissions.json`
listing exactly four genuine non-axiom admitted inputs. One of them
is named **`S`** (= "absolute scale": one empirical scale-setting
number). The registry already states, verbatim: *"the unit choice
itself is vacuous and **not** an input; the genuine admission is the
scale-setting."*

This note's purpose is to align the EW hierarchy chain's reference to
"P1" with the Tier-A registry's classification of S, and to make
explicit a **vocabulary disambiguation** that has been latent:

- **EW-chain "P1"** (per `HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10`)
  = the M_Pl anchor in `v = M_Pl · (7/8)^(1/4) · α_LM^16`.
- **Tier-A registry "P1"** (per `ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23`)
  = the extensivity / observable-principle admission.
- These are DIFFERENT objects sharing the same label. They MUST NOT
  be conflated.

The EW-chain's P1 maps cleanly to the registry's **S** (M_Pl is the
particular observable chosen to set the scale). The registry already
identifies S as "pervasive, not a single citeable parent row" and
already classifies the unit-choice portion as vacuous. This note
formalizes the EW-chain ↔ registry mapping and proposes that
downstream lane references to "P1 = M_Pl anchor" route through the
convention-adoption pipeline already established by
`CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08` and
`RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv`,
consistent with the Tier-A registry's existing treatment of S.

The note does not predict the audit-lane verdict on this proposal. It
provides the structural argument and hands the question to the audit
lane.

## 1. Scope: four narrow meta-claims S1-S4

This note makes exactly four narrow meta-claims. None is a physics
theorem; all are repo-semantics statements.

- **S1 (Buckingham-π universal impossibility).** Deriving an
  absolute SI mass value from a system whose only inputs are
  dimensionless integers, ratios, and combinatorial data is forbidden
  by dimensional analysis (Buckingham-π theorem; standard textbook
  applied mathematics, ~1914). This is a mathematical impossibility,
  not a framework-specific research gap. Every physics theory that
  predicts SI values takes at least one dimensional anchor.

- **S2 (No published framework achieves zero-anchor SI prediction).**
  Survey of major theoretical frameworks shows that every one of them
  takes at least one dimensional anchor — Standard Model (~19 free
  parameters), Lattice QCD (Λ_QCD via m_π or m_proton), Connes-
  Chamseddine spectral SM (M_Pl + unification scale), asymptotic
  safety (M_Pl + fixed-point couplings), loop quantum gravity
  (M_Pl), causal dynamical triangulations (M_Pl), string theory
  (M_Pl + string scale + moduli, vacuum-dependent). This is consistent
  with S1; no observed exception.

- **S3 (Anchor-equivalence: many forms, all equivalent).** A single
  dimensional anchor can take any of these mathematically-equivalent
  forms — they all fix the same one piece of information:
  - "1 framework lattice site = ℓ_observed meters" (lattice-spacing-
    to-meter)
  - "M_Pl = 1.22 × 10¹⁹ GeV" (Planck mass in SI)
  - "ℏ = 1.054 × 10⁻³⁴ J·s" (Planck's constant in SI)
  - "speed of light c = 2.998 × 10⁸ m/s" (SI meter definition)
  Any one of these fixes all the others via standard dimensional
  conversions. The framework needs exactly one of them; the choice
  among them is convention.

- **S4 (Right disposition pipeline: convention-adoption per
  precedent; consistent with Tier-A registry).** The disposition of
  "M_Pl as conventional anchor" should follow the same pipeline as
  the framework's prior unit-convention adoptions, which are
  `claim_type=meta` and audit-decided (source-note + paired-runner +
  independent audit-review):
  - `CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md` — meter,
    second, kilogram, GeV unification companion (origin/main, meta).
  - `RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md`
    — radian unit reclassification (origin/main, meta).
  - `ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md` — Tier-A
    admitted-input registry (origin/main, meta); already lists S
    (absolute scale) as one of four genuine admissions and explicitly
    states the unit choice is vacuous.

  These precedents establish that unit-convention adoption in this
  repo is meta-tier and audit-decided, not user-ratified theorem
  promotion. Specifically, the Tier-A registry's existing treatment
  of S as "pervasive, not a node, unit choice vacuous, scale-setting
  is the genuine admission" is the operational pattern this note
  asks downstream EW-chain references to "P1" to adopt.

## 2. Setup (retained / meta content cited honestly)

The note cites only what's actually on `origin/main`, with current
audit status, and does NOT promote any cited status.

| Authority | Status on origin/main | Role in this note |
|---|---|---|
| `PLANCK_FROM_STRUCTURE_PATH_OPENING_META_NOTE_2026-05-10.md` | meta (audit-decided) | Source of "conventional anchor: 1 pre-round, 0 conditionally post-round" framing |
| `CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md` | meta (audit-decided) | Precedent for unit-convention adoption pipeline |
| `RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md` | meta (audit-decided) | Second precedent for unit-convention adoption pipeline |
| `ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md` | meta (audit-lane sidecar) | **Already names S as one of four Tier-A admitted inputs; explicitly states "unit choice is vacuous, scale-setting is the genuine admission." EW-chain "P1" (M_Pl anchor) maps to registry's S.** |
| `docs/audit/data/tier_a_admissions.json` | machine registry | Tier-A admissions data file referenced by `compute_effective_status.py` |
| Buckingham, E. (1914). *On Physically Similar Systems*. Phys. Rev. 4, 345. | textbook | Mathematical authority for S1 dimensional-analysis claim |
| Standard physics literature on SM / LQG / Connes-Chamseddine anchors | textbook | Sidecar reference for S2 survey |

Buckingham-π is standard applied mathematics — citing it as a
textbook fact does NOT count as a load-bearing import per the audit
rubric's accepted-premise rules (the claim is provable in any
introductory dimensional-analysis text).

## 3. What this proposal does NOT claim

- Does **not** derive M_Pl, m_W, v_EW, or any other dimensional value
  from A1+A2+retained content.
- Does **not** claim a new dimensionless structural identity between
  M_Pl and any framework primitive.
- Does **not** claim α_LM is defined at the SU(2) Landau pole = M_Pl,
  or at any specific scale. The retained `ALPHA_LM_GEOMETRIC_MEAN_IDENTITY_THEOREM`
  carries the explicit warning that it is NOT an authority for the
  numerical α_LM value or its scale of definition; this proposal
  respects that boundary.
- Does **not** cite `HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10`
  as retained. That note is at `unaudited` status on origin/main; it
  is consulted only as a source of the four open primitives `P1`-`P4`
  naming convention, not as an audit-grade authority for any
  numerical claim.
- Does **not** propose any change to A1, A2, or any retained
  theorem.
- Does **not** add a new admission, primitive, axiom, or repo
  vocabulary item.
- Does **not** predict any audit verdict on this proposal or on any
  other row.
- Does **not** promote, retire, or reclassify any existing audit
  row.

## 4. Significance (modest)

If S1-S4 audit clean (under audit-decided pipeline per S4), the
disposition of "P1" becomes clean:
- "P1" is classified as a unit-convention adoption slot, sibling of
  the meter/GeV/lattice-spacing/radian convention adoptions already
  on origin/main.
- Future lane work referring to "P1 as remaining admission" can route
  through the convention-adoption pipeline rather than treating it
  as an open theorem.
- The framework's cumulative anchor count is clarified: one anchor,
  universally required by Buckingham-π, no different from the choice
  any TOE makes.

This does NOT promote any existing claim or move any audit row's
status. It is a semantic clarification only.

If the audit lane disagrees and routes "P1" back to the theorem-audit
pipeline instead, the framework's lane status is unchanged — P1
remains an open theorem-derivation admission, and the lane carries it
as such. No retained content is touched either way.

## 5. Conditional structure

This proposal is conditional on:
- (H_Buckingham) Buckingham-π theorem is standard mathematics
  (universally accepted; no audit required).
- (H_CONVENTIONS) `CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08`
  retains its current meta status on origin/main.
- (H_RADIAN) `RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv`
  retains its current meta status on origin/main.
- (H_PATH_OPENING) `PLANCK_FROM_STRUCTURE_PATH_OPENING_META_NOTE_2026-05-10`
  retains its current meta status on origin/main.

If any precedent status changes downstream, the convention-adoption
argument requires reconsidering whether the pipeline still applies. The
S1 (Buckingham-π) claim is independent of all framework rows and
stands unconditionally.

## 6. Audit-lane handoff

```yaml
proposed_claim_type: meta
audit_pipeline: convention-adoption (audit-decided per precedent)
audit_required_before_effective: true
audit_handoff_status: |
  Source-only meta-tier proposal classifying "M_Pl as conventional
  anchor" (P1 of EW hierarchy chain) as a unit-convention slot
  rather than a theorem-derivation gap, per the universal
  dimensional-analysis (Buckingham-π) impossibility of zero-anchor
  SI prediction and per the established convention-adoption
  precedents on origin/main.

  Four narrow meta-claims:
    S1 Buckingham-π universal impossibility (standard mathematics)
    S2 No published framework achieves zero-anchor SI prediction (lit survey)
    S3 Single anchor takes many equivalent forms (a_lat, M_Pl, ℏ, c)
    S4 Disposition via convention-adoption pipeline (precedent: meter, GeV, lattice-spacing, radian)

  No new physics claim. No retained-row promotion. No axiom
  extension. No PDG load-bearing.

  Independent audit lane decides whether this disposition
  applies. If yes, downstream lanes can route P1 references through
  the convention-adoption pipeline. If no, P1 remains a
  theorem-derivation admission and lanes carry it as such.

new_audit_row:
  - claim_id: p1_honest_reframe_unit_convention_anchor_meta_note_2026-05-27
    proposed_claim_type: meta
    effective_status_proposal: meta
    conditional_on:
      - retained meta status of CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08
      - retained meta status of RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv
      - retained meta status of PLANCK_FROM_STRUCTURE_PATH_OPENING_META_NOTE_2026-05-10
    routing:
      foundations: A1 (M_2(C) = Cl(3,0)), A2 (Z^3 locality) — not modified
      retained_consumed: NONE (cites meta-tier precedents only; no retained promotion)
      load_bearing_imports: NONE
      external_anchor: NONE for the meta-claim itself; Buckingham-π is standard math
      sidecar_context_only:
        - Buckingham 1914 (dimensional-analysis impossibility)
        - Standard SM / LQG / Connes-Chamseddine anchor count literature
        - PDG (mentioned only as the comparator-domain on which other lanes work; not consumed here)
proposed_load_bearing_step_class: E (meta semantic reclassification proposal)
status_authority: independent audit lane only
no_existing_row_touched: true
no_verdict_predicted: true
no_axiom_extension: true
no_load_bearing_import: true
no_new_numerical_claim: true
```

## 7. Sidecar references

- Buckingham, E. (1914). *On Physically Similar Systems; Illustrations
  of the Use of Dimensional Equations*. Phys. Rev. 4, 345-376. —
  authority for S1.
- Standard introductory dimensional-analysis textbooks (any) —
  authority for S1.
- Particle Data Group 2024 — comparator-domain only; not consumed
  here.
- Connes, A. & Chamseddine, A. — spectral standard model literature;
  cited as part of S2 survey.

All sidecar context only. No load-bearing import.

## 8. Origin and what comes next

This proposal arose from convergent panel work (six-agent attack,
2026-05-27) on the P1 admission. All six lenses converged on the same
finding: P1 in its zero-anchor framing is dimensional-analysis
impossible to close, but its disposition as a unit-convention slot
follows existing repo precedent cleanly.

**If this proposal audits clean (under the convention-adoption
pipeline):**
- Downstream lane work cites P1 as a unit-convention slot, not an
  open theorem.
- The lepton mass spectrum lane's R-L2 strict zero-anchor framing
  retires; the lane's status becomes "structurally specified at PDG
  precision under one conventional unit anchor."
- The framework's cumulative anchor count is officially one,
  universally required by Buckingham-π.

**If this proposal does not audit clean:**
- No retained content is touched. The lane's existing status stays.
- P1 remains as an open theorem-derivation admission, and downstream
  lanes continue to carry it as such.
- The note remains as documented historical context.

In either case, the framework's actual physics content — the lepton
chain (PRs #1997, #1999, #2003, #2025, #2031), the EW hierarchy
chain (origin/main bounded), the gauge structure (retained), CPT
(retained), Koide (retained), Strong CP (retained_bounded), CKM
corollaries (retained), etc. — is unchanged. This proposal is a
semantic clarification of how to refer to an existing admission, not
a science update.
