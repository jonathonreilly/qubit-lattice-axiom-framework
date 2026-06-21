# Incumbent Axioms + Primitives — Blind Physicist-Panel Review

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the canonical
> source-of-truth doc.

**Date:** 2026-06-20 (synthesis authored 2026-06-21)
**Type:** meta / governance review (blind expert-panel synthesis)
**Slug:** `incumbent-axiom-panel`
**Status authority:** independent audit lane / owner only. This note carries
**no** `audit_status` and promises **no** `effective_status`. It sets no audit
verdict, adopts/demotes/splits no axiom or primitive, and edits no machine
registry. Any change recommended below routes through
`docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6 and is the owner's sole call.

```yaml
artifact_type: blind physicist-panel review synthesis (meta / governance)
proposal_allowed: false        # owner governance decision required
adopts_axiom: false
demotes_axiom: false
splits_axiom: false
sets_audit_verdict: false
edits_axiom_premise_nodes: false
status_authority: independent audit lane / owner only
```

## Scope and method

A single blind panel of **ten physicists** (lattice gauge theory; quantum
foundations / decoherence; mathematical physics / operator algebras; Standard
Model phenomenology; hard-skeptic Bayesian-Occam minimalist; GR / causal
structure / arrow-of-time; condensed-matter RG & emergence; quantum information
/ quantum Darwinism; axiomatic / constructive QFT; philosopher of physics)
judged the framework's **EXISTING foundation** from first principles — the three
named axioms and the three approved primitives:

- **A1 Lattice**, **A2 Quantum**, **A3 Record** — `docs/MINIMAL_AXIOMS_2026-06-05.md`
- **P1 `scale_reference_primitive`** — `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`
- **P2 `kinetic_isotropy_primitive`** — `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`
- **P3 `realized_state_primitive`** — `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`

with `docs/audit/AXIOM_MINIMALITY_POLICY.md` and
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` available. Panelists
were instructed **not** to defer to the framework's self-justification or its
admissibility rulings, but to decide whether each item *actually* holds up. This
is the companion review to
`docs/AXIOM_PROPOSALS_PHYSICIST_PANEL_REVIEW_2026-06-20.md`, which cold-rejected
all four *proposed* additions (block05). The governance question this note
answers: **is the existing foundation held to the same standard that just
rejected the four adds?**

## Per-item tally (10 reviewers)

| Item | pass | concern | fail | correctly-tiered (yes / no) | bottom line |
|------|:----:|:-------:|:----:|:---------------------------:|-------------|
| **A1 Lattice** | 9 | 1 | 0 | 10 / 0 | PASSES (one concern: own the cubic point-group content) |
| **A2 Quantum** | 7 | 3 | 0 | 10 / 0 | PASSES (concern: the `Cl(3,0)` reading rides at axiom grade) |
| **A3 Record** | 0 | 9 | 1 | 3 / 7 | DOES NOT CLEANLY PASS — split required |
| **P1 scale_reference** | 10 | 0 | 0 | 10 / 0 | PASSES CLEANLY (unanimous) |
| **P2 kinetic_isotropy** | 0 | 2 | 8 | 1 / 9 | FAILS — demote to Tier-A |
| **P3 realized_state** | 5 | 5 | 0 | 10 / 0 | PASSES (5 concerns are usage/enforcement, not the primitive) |

System verdict across the 10 panels: **8 `needs_revision`, 2
`sound_with_concerns`, 0 sound, 0 unsound.** No panelist judged the foundation
sound as-is; the two `sound_with_concerns` panelists (GR/arrow; philosopher of
physics) still demand the same two repairs (split A3, demote/reframe P2). The
synthesized verdict is therefore **`needs_revision`**, driven entirely by **P2**
and the **A3 K/CPT-orbit clause** — not by the clean core.

### Smuggling flags (consensus, >= 2 panelists)

| Flag | Item | count | nature |
|------|------|:----:|--------|
| **P2 installs the emergent-Lorentz ANSWER (`c_t=c_s`) as a premise** — by the note's own "deriving it would be circular" admission; the policy §1/§4 "accept X so lane Y closes" pattern | P2 | **10/10** | output-as-axiom / circularity |
| **P2 is a dimensionless DYNAMICAL coupling (kinetic/transfer-coefficient ratio, RG-running, radiatively corrected — Karsch anisotropy), not a structural graining fact** — the cubic-adjacency analogy is a category error | P2 | **9/10** | mis-classification |
| **A3's K/CPT-orbit clause USES a fixed K/CPT conjugation while the disclaimer says Record supplies "no K/CPT structure"** — a definition cannot disclaim its own ingredients | A3 | **10/10** | internal contradiction |
| **A3's "finite central-sector decomposition" presupposes superselection / a finite atomic center / einselection conclusion not supplied by A1+A2** | A3 | **6/10** | structure smuggled under "given" |
| **A3's "realized central sector" presupposes objectification (a single realized outcome) that decoherence provably does not deliver** | A3 | **3/10** (decoherence, QI/Darwin, GR) | objectification assumed |
| **A3's K/CPT-orbit quotient imports a CPT antiunitary / charge-conjugation (particle~antiparticle) identification into the definition of "outcome"** | A3 | **5/10** | discrete-symmetry / species premise |
| **A2's `=Cl(3,0)` is a real-form / signature / grading CHOICE (distinguished generator basis, even-subalgebra SU(2), pseudoscalar, antilinear structure), not a neutral relabel of `M_2(C)`** | A2 | **7/10** | spinor/real-structure pre-loading |
| **A1's "cubic adjacency" supplies the cubic point group `O_h` (discrete orientation), NOT continuous isotropy — yet downstream notes cite it as the `a_x=a_y=a_z` isotropy precedent** | A1 | **6/10** | discrete-vs-continuous upgrade |
| **P2 free-rides on A1's "neutral geometry" framing to launder a dynamical tuning as the "time analogue of cubic adjacency"** | P2/A1 | **5/10** | false analogy / cross-tier pricing |
| **P3 "registered data" slot is an attractive hiding place for SM flavor content (sector weights `r in {0,1/2,1}`, register entry 4) unless the counterfactual test is enforced, not asserted** | P3 | **3/10** (SM-pheno, CM-RG, skeptic) | usage risk, not primitive content |

No panelist found any typicality / past-hypothesis / measure smuggling in **P3**
itself; multiple explicitly credited its counterfactual test and its routing of
the past hypothesis to a separate stronger input as the **strongest** firewall
in the set. **P1** drew zero substantive smuggling flags (the only note: name
the anchor abstractly to forestall a later `a/l_P=1` slip).

## Items that did NOT cleanly pass

### P2 `kinetic_isotropy` — FAIL (8 fail, 2 concern; 9/10 say wrong tier -> Tier-A)

This is the strongest consensus in the review. Across lattice gauge theory, OS
reconstruction, condensed-matter RG, SM marginal-LV phenomenology, QI, the
skeptic, the axiomatic-QFT and philosopher seats, the verdict is identical:

- `c_t/c_s` is the ratio of temporal-to-spatial kinetic coefficients in the
  action / transfer matrix — a **marginal coupling** that RG-runs and is
  radiatively corrected (Karsch renormalized-anisotropy). Setting it to 1 is a
  **tuned dynamical normalization**, not a combinatorial graph fact.
- The note **concedes** `c_t=c_s` "is itself the emergent-Lorentz output" and
  that deriving it "would be circular," then uses that circularity as the
  *license* to adopt it. That is precisely the **`AXIOM_MINIMALITY_POLICY` §1
  forbidden pattern** ("if we just accept X as primitive, lane Y closes") and §4
  (record as an unmade decision, do not adopt-and-proceed). Self-certifying via
  circularity is adopting the conclusion.
- The "time-direction analogue of cubic adjacency" analogy is a **category
  error**: spatial cubic adjacency is within-the-axiom combinatorics on already
  given edges, and even *it* yields isotropy only as an RG-irrelevant-operator
  consequence (a cube breaks `SO(3)` to `O_h`, exactly, never to isotropy). The
  framework's time is **emergent/derived** (single-clock theorem), so there is
  no time edge for the analogy to attach to; fixing the kinetic-form ratio of an
  emergent direction constrains a derivation output.
- The radiative-stability / fine-tuning cost (the marginal-LV naturalness
  problem) is nowhere accounted; emergent Lorentz invariance from a lattice is
  generically tuned, and the primitive presents it as cost-free.

**This fails the exact test that rejected the four adds.** The block05 companion
review demoted proposal **S** (`SPACING`, time-edge ratio) to a derivation
target, and the §6 Tier-A refinement already recorded that the `AC_phi_lambda`
reading selector is "a selector for dimensionless physics content and is
therefore **not** primitive-eligible under the kinetic-isotropy admissibility
boundary." By that same boundary, a kinetic-coefficient ratio that equals the
emergent-Lorentz output is on the Tier-A side of the line. The foundation is
**not** currently held to the standard it applies to newcomers: P2 was
grandfathered in.

### A3 Record — DOES NOT CLEANLY PASS (9 concern, 1 fail; 7/10 say split)

Every panelist endorses the **additivity half** as genuinely axiom-class:
durable registration; `I` finitely additive over finite pairwise-disjoint
records; `I(empty)=0`. The defect is bundling: A3 **welds** that clean
measure-theoretic axiom to a structural identification of a different epistemic
class — "the realized outcome is the K/CPT orbit of the realized central
sector." That clause:

- **defines** the outcome using a finite central-sector decomposition and a
  fixed K/CPT conjugation while the disclaimer says Record supplies "no
  decomposition / K-CPT structure." A definition cannot disclaim its own
  ingredients (10/10);
- presupposes a von Neumann structure (finite atomic center, type-I /
  separability) that A1+A2 do not furnish — they supply only a fiber algebra,
  no global algebra (operator-algebra seat);
- presupposes **objectification** (a single realized sector) — which decoherence
  provably does not supply (decoherence/QI seats) — and presupposes
  **einselection** (that records live in a *central*, i.e. commuting/pointer,
  algebra);
- quotients by a **CPT antiunitary**, importing a discrete-symmetry /
  charge-conjugation (particle ~ antiparticle) identification and, per the
  QI/Darwinism seat, an **orbit multiplicity** (a count / occupancy datum) that
  downstream count-twice / K-reality / Koide-occupancy lanes draw from — while
  the disclaimer denies "occupancy."

The "given a readout context …" conditionalization is honest as far as it goes,
but it makes A3 a **schema parametrized by an unsupplied (decomposition,
conjugation) pair**, not a free-standing axiom; the framework then owes a
separate accounting of where the finite atomic center and the CPT involution
come from. Note the cross-axiom seam (operator-algebra + SM-pheno seats): A2's
silent `Cl(3,0)` real form is the unacknowledged supplier of the very antilinear
conjugation A3 re-posits as "fixed."

### A2 Quantum — PASSES with a tiering caveat (7 pass, 3 concern)

The carrier (`A_x ~= M_2(C)`, one qubit) is unanimously axiom-class and its
dynamics/Born/gauge/species disclaimers are honest. The shared concern is the
parenthetical `= Cl(3,0)`: as a *complex*-algebra isomorphism it is true, but
the real-Clifford reading fixes a real involution / signature / grading
(generator basis, even-subalgebra SU(2), pseudoscalar) that is the spinor/species
scaffold A2 disclaims and that A3's K/CPT clause later consumes. Recommended
hygiene (not a failure): keep `M_2(C)` at axiom grade; move the `Cl(3,0)` reading
to a labeled downstream identification row.

### P3 realized_state — PASSES (5 pass, 5 concern; 10/10 correctly tiered)

The five "concern" votes are uniformly about **usage/enforcement and one latent
ontological commitment**, not about the primitive's content:

- the **single-realized-world (non-Everettian)** stance is load-bearing but
  unstated (decoherence/QI seats) — under a branch-relative reading "the
  realized state" is undefined; add one sentence;
- the **counterfactual test must be executed and logged**, and finite
  forced-looking dials (sector weights `r in {0,1/2,1}`, register entry 4) must
  be shown genuinely realizable, or SM flavor/Koide content can be laundered as
  initial conditions (SM-pheno, CM-RG, skeptic);
- the shared word **"realized"** with A3 invites conflation — cross-link the two
  senses.

The laws-vs-initial-conditions floor is irreducible (no state-blind structure
selects a state), the counterfactual test is a genuine mechanical guard, and the
past hypothesis is correctly excluded as a strictly stronger separate input. P3
is a legitimate, correctly-tiered, narrow dynamics-free datum.

## System verdict: minimal? independent? non-redundant?

**Minimal — NO (as tiered).** Two defects, both structural, both repairable:

1. **A3 is internally non-minimal**: it bundles a clean additivity axiom
   (axiom-class) with a K/CPT-orbit + central-sector identification
   (derivation/admission-class). One "Record" row is two premises.
2. **P2 is mis-tiered**: a dimensionless dynamical coupling / emergent-Lorentz
   output occupying primitive grade, where it **chain-satisfies without bounding
   dependents** — laundering the framework's central relativistic-invariance
   claim out of the audited/bounded column.

After the A3 split and the P2 demotion, the residual core
`{A1, A2-carrier, A3-additivity, P1, P3}` is a defensible minimal set, with the
K/CPT-orbit clause and `c_t=c_s` living in the Tier-A admissions ledger.

**Independent — NO (two coupling defects).** A1, A2-carrier, P1, P3 are mutually
independent (graph / algebra / dimensionful ruler / state slot are orthogonal,
and P1's and P3's irreducibility each rest on a genuine theorem — dimensional
analysis; laws-vs-state). The two violations:

- **P2 is not an independent premise**: by the note's own words it is the
  emergent-Lorentz **output** of `A1+A2+A3 + emergent-time + reflection
  positivity`, i.e. the (currently underived) conclusion of a derivation over
  the others — an "axiom that is the theorem you want." That is independence of
  the wrong kind: an un-derived answer, not an irreducible datum.
- **A3's K/CPT-orbit clause is not self-standing**: it depends on a central
  decomposition + an antilinear conjugation that no other item supplies, and the
  conjugation it treats as "fixed" is the one A2's `Cl(3,0)` real form silently
  selects (operator-algebra + SM-pheno seats).

### Redundancy findings (the two explicitly-asked pairs)

- **`kinetic_isotropy` vs `scale_reference`: NOT redundant.** Unanimous and
  correct: P1 is a **dimensionful** units anchor (`a^{-1}=M_Pl`), P2 a
  **dimensionless** ratio (`c_t/c_s`). They are orthogonal. (This non-redundancy
  does **not** rescue P2's tier — being distinct from P1 makes it a separate
  *admitted input*, not a primitive.)
- **`realized_state` vs Record: NOT redundant in content** (Record = readout
  coarse-graining / what a registration *is*; P3 = which law-admissible state /
  manifold point obtains), but **they double-use the word "realized,"** and two
  seats (decoherence; QI/Darwinism) flag that *after* P3 was admitted
  (2026-06-11) A3's own "realized" commitment is partly P3's job, so the
  single-realized-world datum is encoded twice. The fix is the A3 split + an
  explicit A3<->P3 cross-link, after which the datum is supplied once (in P3) and
  merely referenced by Record.

A third redundancy surfaced unasked: **P2 partially overlaps A1** — it markets
itself as "the time-direction analogue of cubic adjacency," i.e. A1+P2 are one
hypercubic-regulator-symmetry posit split across an axiom and a cheaper
primitive tier (priced across two tiers).

### System-level smuggling consensus

- **P2 launders the emergent-Lorentz answer (`c_t=c_s`) into the dynamics-free
  premise tier** under a false "structural, like cubic adjacency" label, via the
  policy-forbidden "accept X so lane Y closes" / self-certified-circularity move
  (§1/§4). It chain-satisfies without bounding, so every downstream Lorentz /
  isotropy claim resting on it is currently **unearned**. (10/10)
- **A3 Record smuggles von Neumann structure** — a finite atomic central
  decomposition and an antilinear K/CPT involution — and asserts **CPT
  invariance of outcome identity** (a theorem with hypotheses, here installed as
  a definition), plus an **orbit multiplicity / occupancy** datum, all under a
  long disclaimer that denies supplying exactly these. (>=6/10)
- **A2's `=Cl(3,0)` silently fixes a real form / conjugation / grading** that is
  the unacknowledged supplier for A3's "fixed K/CPT conjugation." (7/10)
- **A1's discrete cubic point symmetry is quietly upgraded to spatial isotropy**
  downstream and used as P2's precedent. (6/10)
- **System ontology**: a single-outcome (non-Everettian) commitment is
  load-bearing across A3+P3 but never stated. (2/10)
- **Pattern flag**: all three primitives were added later to unblock specific
  lanes (scale 2026-06-04; Lorentz 2026-06-09; state-contingency 2026-06-11).
  **P1 and P3 survive** as genuine irreducibles (dimensional analysis;
  laws-vs-state). **P2 does not** — its adoption note explicitly frames it as
  the structure needed to avoid circular emergent-Lorentz closure, which is the
  lane-closure smuggling pattern itself.

## Recommended changes (owner governance decision; this note adopts none)

1. **DEMOTE P2 `kinetic_isotropy` from the approved-primitive registry to a
   Tier-A admitted derivation target** in `docs/audit/data/tier_a_admissions.json`
   (alongside `AC_phi_lambda`, `theta`), with an explicit no-go portfolio
   (`c_t/c_s` undetermined by `A1+A2+A3 + reflection positivity + single-clock`;
   radiative-stability / marginal-LV-naturalness / Lorentz-restoration
   residuals). Dependents then chain-satisfy only at `retained_bounded` until a
   genuine emergent-Lorentz derivation retires it. If it is to remain a premise
   at all, restate it as the anisotropy renormalization condition `c_t/c_s = 1`
   with the radiative residual on its face, and **drop** the "structural graining
   / analogue of cubic adjacency" framing.
2. **SPLIT A3 Record** into (A3a) the **axiom**: durable registration + finite
   scalar additivity of `I` over disjoint records, `I(empty)=0`; and (A3b) a
   **conditional identification / Tier-A target**: "realized outcome = K/CPT
   orbit of the realized central sector," which explicitly takes (finite central
   decomposition, K/CPT conjugation) as named external inputs, accounts for their
   existence/finiteness/atomicity, cites P3 for the single realized sector, names
   centrality as an assumed superselection input, and records the CPT-orbit
   quotient (and its orbit size / occupancy) as a separate symmetry premise.
3. **AMEND A2**: keep `A_x ~= M_2(C)` at axiom grade; relocate the `Cl(3,0)`
   real-algebra reading to a labeled downstream identification row, OR enumerate
   its load-bearing exports in the supplies clause so A3's K/CPT is not
   double-disclaimed. Let A3 cite A2 as the single source of its conjugation.
4. **ANNOTATE A1's ledger**: it supplies the cubic (hyperoctahedral) point group
   / coordinate-axis orientation and dimension three, **NOT** continuous
   rotational isotropy; forbid downstream notes from citing it as the
   `a_x=a_y=a_z` isotropy source.
5. **TIGHTEN P3** (keep as primitive): state the single-realized-world
   commitment explicitly; require the counterfactual test to be executed and
   logged per realized-state-data claim (flag register entry 4, sector weights
   `r`); cross-link A3<->P3 to disambiguate the two senses of "realized" and route
   the single-realized datum through P3 once.
6. **P1**: keep unchanged (passes cleanly). Optional hygiene: name the anchor
   abstractly (`a^{-1}=M_0`) and relegate "identified with `M_Pl`" to the open
   gravity self-consistency gate.

## Overall bottom line

The **clean core holds**: A1 (a kinematic graph carrier), A2's qubit carrier
`M_2(C)`, A3's finite scalar-additivity readout, P1 (the one irreducible
dimensionful ruler — unanimous clean pass), and P3 (the laws-vs-initial-
conditions slot, well-guarded by its counterfactual test) are legitimate,
well-posed, honestly-scoped premises. **But the foundation does not pass muster
as currently tiered**, and the reason is governance symmetry: the same review
machinery that — in the block05 companion — cold-rejected all four *proposed*
additions for smuggling content the surface withholds finds **two incumbent
items that would fail the identical test**. (i) **P2 `kinetic_isotropy`** is a
mis-classified dimensionless dynamical coupling that installs the
emergent-Lorentz answer as a free, non-bounding primitive via the policy's own
forbidden "accept X so lane Y closes" / circularity move — it is exactly the
class of item the §6 Tier-A refinement already declared primitive-ineligible,
and it appears to have been grandfathered rather than held to that boundary.
(ii) **A3 Record** welds a clean additivity axiom to a K/CPT-orbit + central-
sector identification that presupposes superselection, objectification, a CPT
antiunitary, and an occupancy multiplicity — structure the axiom's own disclaimer
denies supplying. Held to the same standard as the rejected adds, the honest
verdict is **`needs_revision`**: demote P2 to Tier-A and split A3 (A3a axiom /
A3b admission), with A2/A1/P3 hygiene as supporting repairs. P1 and the
additivity core need no change.

---

*Meta / governance review. Sets no audit status. The independent audit lane /
owner is the sole authority for any of the changes above; nothing here adopts,
demotes, splits, or re-grades any axiom or primitive.*
