# Foundation Revision Proposal — Claim Status Certificate (block01)

**Loop slug:** `foundation-revision-proposal`
**Campaign:** `foundation-revision-proposal-block01-20260620`
**Block:** block01
**Cycle:** 1
**Date:** 2026-06-21
**Branch:** `physics-loop/foundation-revision-proposal-block01-20260620`

## Output type

**Governance PROPOSAL** (not an adoption, not a retained claim, not a derivation
to be promoted). `hypothetical_axiom_status: proposed`; `proposal_allowed=false`.
The owner plus the independent audit lane are the **sole authority** to adopt.

## What was produced

Corrected foundation language for the qubit-on-`Z^3` framework, resolving the
clean first-principles panel's 10/10 `needs_revision` findings:

- **A1 Lattice** — annotate (axiom kept): name `O_h`/`B_3` point group + `L1`
  graph metric (`O_h`-not-`SO(3)`); citation guard against continuous-isotropy
  over-citation.
- **A2 Quantum** — amend (axiom kept): keep `M_2(C)`; declare scalar field `C`;
  relocate `Cl(3,0)` real-algebra reading to a labelled downstream identification
  enumerating the three structures (generators, chirality, conjugation) it would
  otherwise smuggle.
- **A3 Record** — SPLIT: **A3a** finite-additivity valuation (axiom; "durable"
  removed; carrier weakened to disjoint-union-closed with `0`); **A3b**
  realized-outcome identification (conditional/derived, NOT an axiom) with `E`
  (center via G-SECT), bare antiunitary `K` (not CPT), K–E compatibility,
  sector count `m`, realized config exposed as hypotheses.
- **P1 scale-reference** — optional hygiene (passes cleanly): abstract anchor
  `M_0`, `=M_Pl` moved to a separate open gravity gate.
- **P2 kinetic-isotropy** — DEMOTE primitive → Tier-A admitted input (primary)
  or derived IR-fixed-point target (alternative): `xi_R=c_t/c_s=1` is a
  renormalized dynamical condition; carries B4-consistent tuning/dim-6 residual;
  "free datum / cubic-adjacency analogue" withdrawn. **DECISION REVERSAL** of the
  logged 2026-06-09 owner approval.
- **P3 realized-state** — primitive kept: consolidate counterfactual guard into
  the statement; own one-world/actualization commitment; cross-link to A3 to
  disambiguate realized STATE vs realized OUTCOME.
- **SYSTEM** — NEW required OPEN GATE (not a new axiom): G-DYN / G-SECT / G-TIME /
  G-ARROW absorb the smuggled dynamics, center-producing map, emergent time axis,
  and arrow. Flag-not-axiomatize per `AXIOM_MINIMALITY_POLICY` sec 1/4.

## V1-V5 promotion-value gate (proposal variant)

| # | Question | Answer |
|---|---|---|
| V1 | What specific finding does this narrow? | The panel's 10/10 `needs_revision` on the incumbent foundation; specifically the A3 disclaim-while-use / factor-center / CPT-import / arrow-smuggle, the P2 primitive mis-tier, and the SYSTEM dynamics/time under-completeness. |
| V2 | What new content does this contain? | A clean A3a/A3b split with all A3b hypotheses exposed (incl. K–E compatibility and sector-count-as-supplied); a renormalized-vs-bare (Karsch) re-tier of P2 with B4-theorem-consistent residual; a four-sub-gate flag (G-DYN/G-SECT/G-TIME/G-ARROW) that replaces silent presuppositions; nine first-principles admissibility criteria. |
| V3 | Could the audit lane already produce this? | No — it is a wording/governance proposal that requires owner authority to adopt; the audit lane sets effective statuses but does not author premise-surface wording. |
| V4 | Non-trivial marginal content? | Yes: a decision-reversal of a logged owner approval (P2), a genuine premise-count reduction (primitives 3→2), and the conversion of silent presuppositions into auditable gates. |
| V5 | One-step variant of a landed cycle? | No — first foundation-revision proposal cycle on this panel. |

**V-gate result:** PASS for `proposal` output type.

## Status fields

```yaml
actual_current_surface_status: proposal
target_claim_type: governance_proposal
hypothetical_axiom_status: proposed
proposal_allowed: false
conditional_surface_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
owner_and_audit_lane_sole_authority: true
claim_type_reason: |
  This is corrected foundation LANGUAGE offered for the owner's governance
  decision. It edits no canonical/registry surface (verified empty diff against
  docs/MINIMAL_AXIOMS_2026-06-05.md and docs/audit/data/axiom_premise_nodes.json).
  P2's re-tier reverses a logged owner approval and therefore cannot land
  without explicit owner reversal + audit-lane re-audit.
```

## Re-check fixes applied (four adversarial lenses, all `revision_sound_with_notes`)

- **A1:** added `O_h`-not-`SO(3)` `L1`-metric anisotropy clause (no
  rotational-distance citation). [lattice-gauge]
- **A3a:** weakened carrier from full Boolean algebra to disjoint-union-closed /
  orthocomplemented poset with `0`. [philosopher]
- **A3b:** added K–E compatibility hypothesis (2′); flagged sector finiteness/
  count `m` as supplied; barred silent reuse of A2's withdrawn conjugation;
  flagged `K^2=±1` sign as downstream-audited orbit-size consequence.
  [operator-algebras + GR/arrow]
- **P2:** corrected "tuned not protected" to B4-theorem-consistent residual
  (one-loop `Sigma_t=Sigma_s` on surface; tuning-to-surface + dim-6, not generic
  instability); specified Euclidean/OS branch; tightened gate citation to
  G-TIME (G-DYN upstream); named admitted-input route as registry-of-record;
  surfaced the decision reversal. [lattice-gauge + GR/arrow]
- **P3:** corrected diagnosis to "consolidate and make explicit" (guard already
  in canonical note); added boundary-vocabulary watch. [philosopher]
- **§8 gate:** G-DYN no longer over-claims continuous real-time `U(t)` from bare
  RP; split out G-SECT as sole home of center-producing map `E`; flagged G-TIME
  undischarged; G-ARROW locates arrow in the initial condition. [all four]
- **Adoption consequences:** added tier-honesty re-audit obligation (8a);
  threaded G-SECT through gate dependencies. [philosopher]

## Independent audit + owner approval required

YES. Adoption requires explicit owner approval recorded in
`docs/audit/AXIOM_MINIMALITY_POLICY.md` and the machine registry, plus
independent audit-lane review. Nothing here applies an audit verdict or promotes
any downstream surface.

## What this does NOT do

- Does not edit `docs/MINIMAL_AXIOMS_2026-06-05.md` (canonical axiom memo).
- Does not edit `docs/audit/data/axiom_premise_nodes.json` (machine registry).
- Does not adopt, retire, or re-grade any premise; does not set any audit status.
- Does not add a dynamics axiom (the gap is a flagged open gate).
