# Incumbent Axioms + Primitives — CLEAN First-Principles Physicist Panel

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the canonical
> source-of-truth doc.

**Date:** 2026-06-20 (synthesis authored 2026-06-21)
**Type:** meta / governance review (blind expert-panel synthesis — CLEAN run)
**Slug:** `incumbent-axiom-panel` (block02, clean)
**Status authority:** independent audit lane / owner only. This note carries
**no** `audit_status` and promises **no** `effective_status`. It sets no audit
verdict, adopts/demotes/splits no axiom or primitive, and edits no machine
registry. Any change recommended below routes through
`docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6 and is the owner's sole call.

```yaml
artifact_type: blind physicist-panel review synthesis (meta / governance, CLEAN)
proposal_allowed: false        # owner governance decision required
adopts_axiom: false
demotes_axiom: false
splits_axiom: false
sets_audit_verdict: false
edits_axiom_premise_nodes: false
status_authority: independent audit lane / owner only
```

## Scope and method — what makes this run CLEAN

A single blind panel of **ten physicists** (lattice gauge theory; quantum
foundations / decoherence; mathematical physics / operator algebras; Standard
Model phenomenology; hard-skeptic Bayesian-Occam minimalist; GR / causal
structure / arrow-of-time; condensed-matter RG & emergence; quantum information
/ quantum Darwinism; axiomatic / constructive QFT; philosopher of physics)
judged the framework's **EXISTING foundation** — the three named axioms and the
three approved primitives:

- **A1 Lattice**, **A2 Quantum**, **A3 Record**
- **P1 scale-reference** (`a^{-1}=M_Pl`, units only, zero dimensionless content)
- **P2 kinetic-isotropy** (`c_t = c_s`)
- **P3 realized-state** (evaluation-at-the-realized-state slot)

**The defining difference from the block01 anchored run:** panelists in *this*
run saw **only the bare statements** of the six items. They were given **no**
`AXIOM_MINIMALITY_POLICY`, **no** machine registry (`axiom_premise_nodes.json`,
`tier_a_admissions.json`), **no** source / adoption notes, and **no** repo files.
Every verdict here is a **first-principles physics judgment** of the bare text,
not a judgment mediated by the framework's own self-justification. This is
deliberate: it produces verdicts suitable for *informing a policy rewrite*,
because they cannot be circular with the policy. See the **DELTA** section for
where a clean verdict differs from, or no longer leans on, the framework's own
policy language.

## Per-item tally (10 reviewers, clean run)

| Item | pass | concern | fail | correctly-tiered (yes / no) | bottom line |
|------|:----:|:-------:|:----:|:---------------------------:|-------------|
| **A1 Lattice** | 8 | 2 | 0 | 10 / 0 | PASSES (two concerns: own the cubic point group + d=3 selector) |
| **A2 Quantum** | 9 | 1 | 0 | 10 / 0 | PASSES (concern: the `Cl(3,0)` reading is not a neutral relabel) |
| **A3 Record** | 0 | 2 | 8 | 0 / 10 | FAILS / DOES NOT PASS — split required (unanimously mis-tiered) |
| **P1 scale-reference** | 10 | 0 | 0 | 10 / 0 | PASSES CLEANLY (unanimous) |
| **P2 kinetic-isotropy** | 0 | 6 | 4 | 0 / 10 | DOES NOT PASS — demote / re-tier (unanimously mis-tiered) |
| **P3 realized-state** | 0 | 10 | 0 | 4 / 6 | PASSES with reservations (every panelist a concern; selection ambiguity) |

System verdict across the 10 panels: **10 `needs_revision`, 0
`sound_with_concerns`, 0 sound, 0 unsound.** Unlike the block01 anchored run
(8 `needs_revision`, 2 `sound_with_concerns`), the clean run is **unanimous
`needs_revision`** — the two seats that returned `sound_with_concerns` when they
could see the policy (GR/arrow; philosopher of physics) both return
`needs_revision` here once the policy's framing is removed. The synthesized
verdict is **`needs_revision`**, driven by **A3**, **P2**, and a sharpened
**P3** ambiguity, plus a system-level **missing-dynamics / missing-time-axis**
finding that the clean run surfaces more forcefully than the anchored run.

### Smuggling flags (consensus, >= 2 panelists, with counts)

| Flag | Item | count | nature |
|------|------|:----:|--------|
| **A3's `K/CPT-orbit of the realized central sector` USES a fixed K/CPT conjugation + a finite central-sector decomposition while the same statement disclaims supplying them** — a definition cannot disclaim its own ingredients | A3 | **10/10** | internal contradiction |
| **P2 `c_t=c_s` IS the emergent-Lorentz / light-cone-isotropy answer installed as a free premise** — it disclaims the very result it asserts | P2 | **10/10** | output-as-axiom / circularity |
| **A3's `central-sector decomposition` presupposes superselection / a nontrivial center** — but `M_2(C)` is a factor (trivial center); a finite product of factors has no nontrivial sectors without a gauge/constraint or coarse-graining map A1+A2 do not supply | A3 | **9/10** | structure smuggled under "given" |
| **A3's `durable = fixed once registered` smuggles irreversibility / an arrow of time** — a thermodynamic/decoherence one-way map, despite "no dynamics / no time metric" | A3 | **9/10** | arrow of time by fiat |
| **P2 presupposes an emergent TIME DIRECTION that nothing supplies** — A1 is spatial-only `Z^3`; A2/A3 add no time axis | P2 | **9/10** | unsupplied prerequisite |
| **P3's `the realized state` presupposes a single actualized state** (definite-outcome / branch selection) with no measure/typicality supplied | P3 | **9/10** | objectification assumed |
| **A3 imports CPT as a primitive** though CPT is a *theorem* of Lorentz-invariant local QFT — no Lorentz/locality is established yet, so it is either an illegitimate import or a mislabel for a generic antiunitary K | A3 | **8/10** | Lorentz-theorem imported as datum |
| **A2's `=Cl(3,0)` real-algebra reading fixes a real form / conjugation / grading** (`so(3)/su(2)` bivectors, pseudoscalar/chirality) beyond bare `M_2(C)` — plausibly the very conjugation A3 re-posits as "fixed" | A2 | **8/10** | spinor / real-structure pre-loading |
| **P3 + A3 jointly install a single-actual-history selection / double-use the word `realized`** | P3/A3 | **8/10** | redundancy / circularity |
| **P1 naming the anchor `M_Pl` pre-loads a Planck-scale identification the disclaimer must walk back** (cosmetic, non-substantive) | P1 | **8/10** | suggestive labeling only |
| **A1's cubic nearest-neighbor adjacency supplies the cubic point group `O_h`/`B_3`, NOT continuous isotropy** (and a combinatorial `L1` graph metric despite "NOT a metric") | A1 | **7/10** | discrete-vs-continuous; metric-under-disclaimer |
| **A3's `realized outcome` presupposes objectification** (a single realized branch) with no selection rule | A3 | **6/10** | definite-outcome assumed |
| **A3's finite additivity of `I`, `I(empty)=0`** is a measure/Born skeleton presented as mere bookkeeping | A3 | **6/10** | measure backbone under "no probability" |
| **P2 `c_t=c_s` is a renormalized-anisotropy / dynamical tuning condition (`xi_R=1`)**, not a free structural datum | P2 | **6/10** | mis-classification |
| **Missing load-bearing posit: a DYNAMICS** (transfer matrix / Hamiltonian / action) presupposed by P2 and A3 but posited nowhere | system | **6/10** | missing axiom |
| **A1 fixes spatial dimension `d=3` by fiat** (`Z^3`) — an empirical-looking selector dressed as "only the site set" | A1 | **5/10** | dimension selector |
| **P2 invokes OS / reflection-positive (OS0) kinetic scaffolding** not supplied by A1-A3 | P2 | **5/10** | continuum-QFT structure imported |
| **A2/A1 silently identify Clifford grade 3 with spatial dimension 3** (undeclared spin-space linkage) | A1/A2 | **4/10** | dimension-matching coincidence |
| **Missing posit: a many-site COMPOSITION / quasi-local tensor structure** (A2 disclaims composition beyond placement) | system | **3/10** | missing axiom |
| **A2 undeclared complex structure `i`** (R-via-Cl(3,0) vs C-via-M_2(C)): the imaginary unit is load-bearing for phase/Born/CPT and never declared | A2 | **3/10** | hidden scalar-field choice |

## Items that did NOT cleanly pass

### A3 Record — FAILS / DOES NOT PASS (8 fail, 2 concern; 10/10 say mis-tiered)

This is the single most serious finding and the **only item that draws no `pass`
vote in either run.** Every panelist endorses the **additivity half** —
`I` finitely additive over finite pairwise-disjoint records, `I(empty)=0`,
durable registration as a bookkeeping fact — as genuinely axiom-class. The defect
is bundling and self-contradiction: A3 welds that clean valuation to a structural
identification of a different epistemic class, "the realized outcome is the
`K/CPT` orbit of the realized central sector," which:

- **defines** the outcome using a finite central-sector decomposition and a
  fixed `K/CPT` conjugation while the same statement disclaims supplying either —
  a definition cannot disclaim its own ingredients (**10/10**);
- presupposes a **nontrivial center** that the supplied algebra does not have:
  `M_2(C)` is a factor; a finite product of factors has center generated only by
  tensor-factor identities, so a "finite central-sector decomposition" with
  nontrivial sectors requires a gauge/constraint commutant or a coarse-graining
  map that **nothing in A1+A2 provides** (**9/10**, led by the operator-algebra
  seat);
- smuggles an **arrow of time** via "durable = fixed once registered" — a one-way
  (second-law / decoherence) statement despite "no dynamics / no time metric"
  (**9/10**);
- imports **CPT** as a free datum although CPT is a *theorem* of Lorentz-invariant
  local QFT (locality + Lorentz + spectrum condition); with no causal cone (A1 is
  spatial-only) and no signature yet, "CPT" is either an illegitimate Lorentz
  import or a mislabel for a generic antiunitary `K` whose existence/uniqueness
  is unstated (**8/10**);
- presupposes **objectification** — a single realized sector — which decoherence
  does not deliver (**6/10**), and uses the finitely-additive `I` as the skeleton
  of a measure/Born rule while disclaiming probability (**6/10**).

The "given a readout context …" conditionalization makes A3 a **schema
parametrized by an unsupplied (decomposition, conjugation) pair**, not a
free-standing axiom. Note the cross-axiom seam (operator-algebra + several other
seats): A2's silent `Cl(3,0)` real form is the unacknowledged supplier of the
very antilinear conjugation A3 re-posits as "fixed."

### P2 kinetic-isotropy — DOES NOT PASS (4 fail, 6 concern; 10/10 say mis-tiered)

Not one panelist accepts P2 as a free structural primitive; all ten say it is the
wrong tier. The reasoning is identical across the lattice, OS-reconstruction,
condensed-matter-RG, SM-pheno, QI, GR, axiomatic-QFT, skeptic, and philosopher
seats:

- `c_t = c_s` is the equality of the temporal and spatial kinetic-form
  coefficients — i.e. a single isotropic light cone, which **is** the kinematic
  core of emergent local Lorentz invariance. Calling it a "free structural datum"
  while disclaiming "NO Lorentz-closure theorem" is having it both ways: the
  result is asserted and the having-of-the-result denied in one breath
  (**10/10**).
- P2 references "the emergent time direction," but **A1 is spatial-only `Z^3`**
  and A2/A3 add no time axis. The existence and singling-out of a time direction
  (a 1+3 split, a Wick/OS reflection axis) is a major result that **nothing in
  the set supplies** (**9/10**). This is the single biggest unstated load-bearing
  element.
- From the anisotropic-lattice trenches, `c_t/c_s` is a **renormalized**
  quantity: bare spatial and temporal kinetic coefficients run differently
  (Klassen/Karsch renormalized-anisotropy), so `c_t=c_s` is the *end-state of a
  one-parameter tuning* whose solution depends on couplings — exactly the
  dynamics P2 says it supplies none of (**6/10**).
- The "(OS0) kinetic form" tag imports Osterwalder-Schrader reflection-positivity
  / transfer-operator / Hilbert-space-reconstruction machinery (a whole
  continuum-QFT structure) that A1-A3 do not provide (**5/10**).

On a cubic lattice, `c_t=c_s` is generically *not* automatic; it is either a
tuned point (an admitted empirical/normalization input) or a derived IR-fixed-
point result, never a cost-free primitive.

### P3 realized-state — PASSES with reservations (0 pass, 10 concern; 4/10 say mis-tiered)

The clean run is **harsher on P3 than the anchored run** (anchored: 5 pass / 5
concern; clean: 0 pass / 10 concern). Without the source note's counterfactual
test and laws-vs-state framing in front of them, every panelist flags the same
dilemma from first principles:

- As a bare evaluation slot ("permit derivations to evaluate at the realized
  state") P3 is harmless but near-contentless — a notational convenience, not a
  foundational datum.
- The word **"realized"** is where content enters: it presupposes that a *single*
  state has been actualized/selected, which is a stance on the definite-outcome
  problem, while P3 disclaims the very tools (measure, typicality, probability,
  past hypothesis) any account of "realized" would need (**9/10**).
- P3 and A3 share "realized"; together they install a single-actual-history
  selection that neither admits, so the datum is **encoded twice** (**8/10**).

So P3 is either empty (then it is notation, not a primitive) or it is the de
facto supplier of an outcome-selection/initial-condition posit. The four
"correctly-tiered yes" votes treat the bare slot as acceptable primitive syntax;
the six "no" votes want it merged with A3 or upgraded to an owned actualization
posit. P3 is **not unsound** — it is honest about what it withholds — but it is
not clean as written. (The mechanical counterfactual test that the anchored
panel credited as P3's strongest firewall is **invisible in this run**; see
DELTA.)

### A1 Lattice — PASSES (8 pass, 2 concern)

A1 is well-posed as a combinatorial substrate and unanimously correctly tiered.
Two concerns: (i) cubic nearest-neighbor adjacency supplies the cubic point group
`O_h`/`B_3` and a combinatorial `L1`/graph metric — so "NOT a metric" overstates,
and continuous isotropy must be *earned*, not assumed (7/10); (ii) `d=3` is fixed
by fiat (5/10). Recommended hygiene, not a failure: own the discrete symmetry and
the dimension selector; forbid downstream notes from citing A1's cubic symmetry
as an `a_x=a_y=a_z` isotropy precedent.

### A2 Quantum — PASSES (9 pass, 1 concern)

The carrier `A_x ~= M_2(C)` (one qubit) is unanimously axiom-class and its
dynamics/Born/gauge/species disclaimers are honest. The shared concern (8/10) is
the parenthetical `= Cl(3,0)`: the real-Clifford reading is **not** a neutral
relabel — it fixes a real form / conjugation / grading (`so(3)/su(2)` bivectors,
pseudoscalar/chirality) that is the spinor/real-structure scaffold A2 disclaims
and that A3's `K/CPT` clause later consumes. Minor seats also flag the
undeclared complex structure `i` (R vs C primitive scalar, 3/10) and the silent
`3 = 3` Clifford-grade / spatial-dimension match (4/10). Recommended hygiene:
keep `M_2(C)` at axiom grade; move `Cl(3,0)` to a labeled downstream
identification row and let A3 cite A2 as the single source of its conjugation.

### P1 scale-reference — PASSES CLEANLY (unanimous)

The only unanimous clean pass in the set, in both runs. A single dimensionful
anchor carrying zero dimensionless content is exactly what a primitive should be,
and the explicit refusal to assert `a/l_Planck = 1` is correct hygiene. The sole
note (8/10) is cosmetic: naming the anchor `M_Pl` pre-loads a Planck-scale
identification the disclaimer then walks back; rename to a neutral symbol
(`a^{-1}=M_0`/`mu_0`) to make "zero dimensionless content" airtight.

## System verdict: minimal? independent? non-redundant?

**Minimal — NO.** Two structural defects, both repairable:

1. **A3 is internally non-minimal**: it bundles a clean additivity axiom with a
   `K/CPT`-orbit + central-sector identification of a different epistemic class
   (several seats count *four* separable posits inside A3: additivity; the
   decomposition; the conjugation; durability/irreversibility). One "Record" row
   is multiple premises.
2. **P2 is mis-tiered**: a dimensionless dynamical coupling / emergent-Lorentz
   output occupying primitive grade.

The set is also **under-complete**: a **dynamics / time-evolution** posit
(transfer matrix / Hamiltonian / action) is presupposed by P2 ("kinetic form",
"emergent time") and A3 ("durable", superselection) yet **posited nowhere**
(6/10), and a **many-site composition / quasi-local tensor** rule is left
implicit under A2's "lattice placement" (3/10). So the foundation is
simultaneously over-bundled (A3) and under-stated (missing dynamics, missing
time axis, missing composition).

**Independent — NO.** A1, A2-carrier, P1 are mutually independent (graph /
algebra / dimensionful ruler are orthogonal). The violations:

- **P2 is not an independent premise**: by its own content it is the
  emergent-Lorentz output of `A1+A2+A3 + an emergent time direction + reflection
  positivity` — an un-derived conclusion of a derivation over the others, not an
  irreducible datum.
- **A3's `K/CPT`-orbit clause is not self-standing**: it depends on a central
  decomposition and an antilinear conjugation no other item supplies, and the
  conjugation it treats as "fixed" is the one A2's `Cl(3,0)` real form silently
  selects.
- **P3 is not independent of A3**: both rest on the same unstated actualization
  ("realized") fact.

### Redundancy findings (the two explicitly-asked pairs, plus one unasked)

- **kinetic-isotropy vs scale-reference: NOT redundant.** P1 is a **dimensionful**
  units anchor (`a^{-1}=M_Pl`), P2 a **dimensionless** ratio (`c_t/c_s`). They are
  orthogonal. (Distinctness from P1 does **not** rescue P2's tier — it makes P2 a
  separate *admitted input*, not a primitive.)
- **realized-state vs Record: NOT redundant in content** (Record = what a
  registration *is* / readout coarse-graining; P3 = which state obtains), **but
  they double-use the word "realized,"** and the single-realized-world datum is
  encoded twice (A3 "realized outcome / realized central sector" + P3 "the
  realized state"). Fix: split A3, cross-link A3<->P3, supply the datum once.
- **Unasked third: P2 partially overlaps A1.** Two seats note P2 markets itself
  as the time-direction analogue of A1's cubic adjacency — one
  regulator-symmetry posit priced across an axiom and a cheaper primitive tier;
  but the analogy is a category error (A1's cubic symmetry is within-axiom
  combinatorics on given spatial edges, whereas P2's time direction is emergent
  and unsupplied).

### System-level smuggling consensus (clean run)

- **A3 Record** smuggles a superselection/central decomposition, an antilinear
  `K/CPT` conjugation (a CPT *theorem* installed as a definition), an **arrow of
  time** ("durable"), and a **measure backbone** (finite additivity), all under a
  disclaimer that denies supplying exactly these. The disclaimer-vs-definition
  contradiction is **unanimous (10/10)**.
- **P2** installs the emergent-Lorentz answer `c_t=c_s` into the dynamics-free
  premise tier and presupposes an emergent time direction the set never produces.
  **Unanimous (10/10)** that it is the wrong tier.
- **A2's `=Cl(3,0)`** silently fixes the real form / conjugation A3 re-posits as
  "fixed" (8/10).
- **A1's cubic point symmetry** is real, discrete (`O_h`), not continuous
  isotropy, and the graph carries a combinatorial metric despite "NOT a metric"
  (7/10).
- **System ontology / missing posits**: a single-outcome (non-Everettian)
  commitment is load-bearing across A3+P3 but never stated; a **dynamics** and a
  **time axis** are presupposed but never posited.

## Recommended changes (owner governance decision; this note adopts none)

1. **SPLIT A3 Record** into (A3a) the **axiom** — durable registration + finite
   scalar additivity of `I` over disjoint records, `I(empty)=0`; and (A3b) a
   **conditional identification** — "realized outcome = `K/CPT` orbit of the
   realized central sector" — that explicitly names (finite central decomposition,
   `K/CPT` conjugation) as external inputs, accounts for their
   existence/finiteness/atomicity, cites the actualization posit for the single
   realized sector, names centrality as an assumed superselection input, replaces
   "CPT" with a neutral antiunitary `K` until Lorentz+locality are earned, and
   records "durable/once-registered" as a **separately-justified irreversibility
   posit**. Remove the disclaimers the body falsifies.
2. **DEMOTE / RE-TIER P2 kinetic-isotropy** from free primitive to an **admitted
   empirical/tuning input** (the observed light-cone isotropy / renormalized-
   anisotropy condition `xi_R=1`) **or** a derived IR-fixed-point target, with the
   radiative-stability / marginal-LV residual on its face. Drop the "free
   structural datum / analogue of cubic adjacency" framing.
3. **ADD a dynamics + time-emergence posit.** A transfer matrix / Hamiltonian /
   action (with reflection positivity) and an explicit emergent-time-direction /
   1+3-split posit are load-bearing for P2 and A3 but currently unstated. Without
   them, P2 is not even statable and A3's "durable" / superselection has no basis.
4. **AMEND A2**: keep `M_2(C)` at axiom grade; relocate the `Cl(3,0)`
   real-algebra reading to a labeled downstream identification row (or enumerate
   its load-bearing exports so A3's `K/CPT` is not double-disclaimed). Declare the
   primitive scalar field (R vs C) so the complex structure `i` is owned.
5. **ANNOTATE A1**: it supplies the cubic (`O_h`) point group + coordinate-axis
   orientation + dimension three, **NOT** continuous rotational isotropy and
   **not** "no metric" (a combinatorial graph metric is supplied); forbid
   downstream citation as the `a_x=a_y=a_z` isotropy source.
6. **DISAMBIGUATE P3**: either strip "realized" and treat as pure
   evaluation-at-a-point notation, **or** own an explicit single-realized-world /
   actualization (initial/boundary-condition) posit; cross-link A3<->P3 so the
   single-realized datum is supplied once. (Optionally add a many-site
   composition / quasi-local tensor posit.)
7. **P1**: keep unchanged (passes cleanly). Optional hygiene: name the anchor
   abstractly (`a^{-1}=M_0`).

## Overall bottom line

The **clean core holds**: A1 (a kinematic graph carrier), A2's qubit carrier
`M_2(C)`, A3's finite scalar-additivity readout, P1 (the one irreducible
dimensionful ruler — unanimous clean pass), and P3's bare evaluation slot are
legitimate, well-posed premises. **But judged purely from first principles —
with no policy, registry, or source note in front of them — ten of ten
panelists return `needs_revision`.** Three load-bearing problems are
unanimous-or-near: (i) **A3** welds a clean additivity axiom to a `K/CPT`-orbit +
central-sector identification that uses (and so cannot disclaim) a superselection
decomposition, a CPT antiunitary, an arrow of time, and a measure backbone —
the disclaimer-vs-definition contradiction is 10/10; (ii) **P2** installs the
emergent-Lorentz answer `c_t=c_s` as a free, dynamics-free primitive while
presupposing an emergent time direction the spatial-only set never supplies
(10/10 mis-tiered); (iii) the system **omits a dynamics and a time axis** that
P2 and A3 lean on. P3 is honest but ambiguously empty-or-selection-rule, and
P1 alone is clean. The honest synthesized verdict is **`needs_revision`**: split
A3, re-tier P2, add the missing dynamics/time posit, with A2/A1/P3 hygiene and
P1 unchanged.

## DELTA — clean run vs the block01 anchored run

This run carried **NO policy / registry / self-justification context**. Its
verdicts are therefore first-principles physics judgments suitable for informing
a **policy rewrite** (they cannot be circular with the policy they would inform).
Where a clean verdict differs from, or no longer relies on, the framework's own
policy language:

- **The two headline findings survive the removal of the policy — and harden.**
  A3's disclaimer-vs-definition contradiction (10/10) and P2's mis-tier (10/10)
  reproduce *exactly* without any policy in view. In the anchored run the P2
  finding was partly *expressed in the policy's own vocabulary* ("policy §1/§4
  'accept X so lane Y closes'", "§6 kinetic-isotropy primitive-eligibility
  boundary"). **Here the same conclusion is reached from bare physics** — `c_t=c_s`
  is the emergent-Lorentz answer and presupposes an unsupplied time axis — with
  **no** appeal to §1/§4/§6. **Flag for the rewrite:** the P2 verdict is robust,
  not a policy artifact; the policy can cite first-principles emergent-Lorentz /
  renormalized-anisotropy reasoning rather than self-referential "lane-closure"
  language.

- **A3's `M_2(C)` has trivial center is a NEW first-principles teeth** that the
  anchored run did not foreground. The clean operator-algebra reasoning (a factor
  has no nontrivial central decomposition; a finite product of factors needs a
  gauge/coarse-graining map) makes the superselection smuggle **sharper** than the
  anchored run's "presupposes a finite atomic center" phrasing. **Flag:** the
  rewrite should ground the A3-split requirement in this algebraic fact, not in
  the registry's "superselection input" label.

- **System verdict moved from 8/2 to 10/0 `needs_revision`.** The two
  `sound_with_concerns` seats in the anchored run (GR/arrow; philosopher)
  return `needs_revision` here. **Flag:** their anchored leniency was at least
  partly the policy framing reassuring them that the recommended repairs were
  already routed; with the policy removed they judge the *bare statements*
  unsound-as-written. The policy was doing pacifying work — a sign the underlying
  text, not just the tiering, needs editing.

- **P3 is HARSHER clean than anchored (0 pass/10 concern vs 5 pass/5 concern).**
  This is the largest single delta and it is **entirely policy-dependent**: the
  anchored panel credited P3's **counterfactual test** and its routing of the
  past hypothesis to a separate input — guards that live in the *source note*,
  invisible here. From the bare statement alone, "the realized state" reads as a
  smuggled definite-outcome selection. **Flag for the rewrite:** P3's good
  standing genuinely *depends on the counterfactual-test mechanism being in the
  primitive's own statement*, not only in a companion note. The first-principles
  verdict is that the bare text under-discloses; the fix is to fold the guard
  into the statement (or accept P3 is notation + a separate owned actualization
  posit). Do **not** read P3's clean concern count as contradicting the anchored
  pass — it isolates exactly which load-bearing content lives outside the bare
  text.

- **What the clean run does NOT add that the anchored run had:** the explicit
  governance-symmetry argument ("held to the same standard as the four rejected
  block05 adds") is a *policy/registry* construct and is **absent here by design**
  — this run had no block05 companion in view. **Flag:** that argument remains
  valid but is a policy-level overlay, not a first-principles finding; keep it in
  the governance note, not in the physics rationale.

- **Net:** every substantive anchored finding (split A3, re-tier P2, amend A2,
  annotate A1, P1 clean) is **independently reproduced from first principles**,
  and two are *strengthened* (P2 robustness; A3 trivial-center). The clean run
  **adds** an unstated-dynamics / unstated-time-axis system finding that the
  anchored run underweighted. The clean run **removes reliance** on §1/§4/§6
  vocabulary and on the block05 governance-symmetry framing. A policy rewrite can
  therefore restate the A3 and P2 requirements on bare-physics grounds and treat
  the counterfactual-test guard for P3 as something that must appear *in the
  primitive's statement*, not only in its source note.

---

*Meta / governance review (CLEAN, no-context run). Sets no audit status. The
independent audit lane / owner is the sole authority for any of the changes
above; nothing here adopts, demotes, splits, or re-grades any axiom or primitive.*
