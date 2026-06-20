# Axiom-Update Proposal — Readout-Context / Objectivity / Sector-Measure Primitive (Cluster 2)

**Date:** 2026-06-20
**Lane:** axiom-update-proposals, branch
`physics-loop/axiom-update-proposals-block01-20260620`.
**Claim type:** axiom-update PROPOSAL (candidate primitive), FOR owner/governance decision.
**hypothetical_axiom_status:** `"conditional on accepted new axiom; not retained
on the actual current surface."` This label appears on every conditional
derivation below. It does **not** promote the candidate. Only an external
owner/governance decision can promote it; the independent audit lane is the sole
status authority. This note adopts nothing and sets no audit verdict.

**Posture (owner-authorized).** The owner explicitly authorized going beyond the
no-new-axiom rule to deliver either no-new-axiom cracks OR candidate axiom-update
proposals ("don't believe the no-gos; keep working until we have a set of new
derivations or update proposals for the axioms"). Per that posture, for every
wall in this cluster I first run a genuine skeptical no-new-axiom re-attack
(could the campaign no_go be over-strong, like the two B-AXIS no_gos that were
already corrected?). Only where the wall survives do I design the **weakest
sufficient** candidate primitive and build a conditional derivation + runner.

**Primary runner:**
`scripts/axiom_update_proposal_readout_context_objectivity_runner_2026_06_20.py`
**Cached output:**
`logs/runner-cache/axiom_update_proposal_readout_context_objectivity_runner_2026_06_20.txt`
(**TOTAL: PASS=41 FAIL=0**). For each wall the runner (A) re-attacks the no_go
(confirms it genuinely walls the no-new-axiom route on the tested finite
surface, including a dedicated test that **no missed symmetry forces the
equal-block measure**), and (B) verifies that the single named readout-context
primitive discharges it.

**Policy conformance** (`docs/audit/AXIOM_MINIMALITY_POLICY.md` §1/§4,
`docs/MINIMAL_AXIOMS_2026-06-05.md`). Current `A_min` = {Lattice, Quantum,
Record}; approved primitives = {scale_reference, kinetic_isotropy,
realized_state}. The minimal-axioms memo's OPEN GATES list explicitly names
*readout context / sector measure / objectivity / occupancy* as **outside**
axiom content. This proposal lands in exactly that open gate — it is therefore
new content in a declared-open gate, **not** a reword of an existing axiom (which
§1 forbids), and it is recorded as an "unmade science-level decision" per §1/§4.
The candidate's approval, if any, routes through `AXIOM_MINIMALITY_POLICY.md` §6
exactly as the `kinetic_isotropy_primitive` did.

---

## 0. Sourcing note (read first)

The task prompt referenced 2026-06-20 campaign notes
(`KOIDE_RECORDS_OBJECTIVITY_DERIVATION_ATTEMPT_NOTE`, exercise packets, OWNER
DECISION PACKETs) that **do not exist in this checkout** (verified by exhaustive
`find`; the sibling cluster's `WALL_TO_GATE_MAP.md` records the same caveat).
This proposal is therefore reconstructed directly from the **landed** Koide /
observable-principle no_go / bounded-theorem notes that DO exist and that already
name the supplier shapes and the gate verbatim. The load-bearing sources are
listed in §8. Fanout magnitudes are cross-checked against
`docs/audit/data/load_bearing_summary.json` (`transitive_descendants`):
`observable_principle_from_axiom_note` = 887,
`charged_lepton_koide_cone_algebraic_equivalence_note` = 327,
`koide_circulant_q_two_thirds_algebraic_narrow_theorem_note` = 186; the Koide
`r=1/2` value node itself is near-leaf (~1 direct), but the **measure/objectivity
primitive** is shared with the whole Koide/flavor stack (the cone's 327
descendants and the flavor readout-context rows).

---

## 1. The cluster and its walls

This cluster is the **readout-context gate**: every wall here is a missing piece
of *which physical readout criterion / sector measure governs how a realized
central sector is read out as a record outcome*. The Record axiom supplies that a
record IS the `K`/CPT orbit of the realized central sector and that scalar
readout is finitely additive over disjoint records — but its text **explicitly
declines** to supply "readout context, decomposition, `K`/CPT structure,
sector-generation rule, weighting, normalization, probability, …, or occupancy
rule." The walls in this cluster are exactly the consequences of that declension:

| Wall | Walling no_go (landed) | What is missing | Open gate |
|---|---|---|---|
| **R1 — Koide `r=1/2` equal-block MEASURE** | `KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31`; `KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29` | the singlet/doublet sector measure — equal-block `(1,1)` vs rank/Born `(1,2)`. The two-block pointer fixes the **number** of blocks, not the weight ratio. | sector measure |
| **R2 — Koide `r=1/2` OBJECTIVITY selector** | `FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02` | the objectivity functional as the **physical readout criterion**; QD/SBS objectivity fixes the pointer **basis**, not the weight. | objectivity / readout context |
| **R3 — `W_t`-independence countermodel** | `KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31` route R3 (dephasing); `KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09` | the weight ratio `t = w_p/w_s` is a **free dial** independent of the record-PRODUCTION/decoherence axiom (Cluster 1). | sector measure / occupancy |
| **R4 — observable T1-d det-READOUT identification** | `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` Boundary T1-d | the **identification** that a record reads out the determinant scalar `Z = det(D+J)` (continuity in `Z` on `R_{>0}` + disjoint-block additivity). | readout context / P2-log-det |
| **R5 — P-REC single-taste POINTER** | `ANOMALY_FORCES_TIME_THEOREM` P-REC row + `NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02` | a selector picking "one record outcome per irreducible Dirac/taste factor"; per-site `gamma_5` is impossible, so the selector cannot be on-site. | species / readout context |

The central observation of this proposal (§4) is that **R1, R2, R3's pin, R4, and
R5 are the same structural binary choice expressed five ways**, so a single
readout-context primitive discharges all of them. That is what makes this the
weakest sufficient addition.

---

## 2. Skeptical no-new-axiom re-attacks (run FIRST)

Per the owner posture, before proposing anything I spend a genuine no-new-axiom
re-attack on each wall.

### SKa — Is the equal-block measure forced by a symmetry the campaign missed?

This is the decisive skeptical test, because if some symmetry already forces
`(1,1)` then the wall is a no-new-axiom crack and **no axiom is needed**. The
runner tests the three candidate symmetries:

- **`U(3)` invariance.** The unique `U(3)`-invariant density is the maximally
  mixed `I/3`. Pushed through the singlet (rank-1) / doublet (rank-2) split it
  gives the **rank** weights `(1/3, 2/3)` ⇒ `r=1`, **not** equal. The
  equal-block reference is verified to **break** `U(3)`. So the continuous
  symmetry, if anything, picks the *wrong* (rank) weights. (Runner SKa(U3).)
- **`K`-reality / CPT.** Conjugation fixes **both** sector projectors
  individually and induces **no** singlet↔doublet swap. It pins the basis, not
  the weight. (Runner SKa(K/CPT); this reproduces
  `FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02`'s K-real route.)
- **`Z_3`-equivariance.** A `Z_3`-equivariant (circulant) generation operator
  **commutes** with the singlet/doublet grading (runner: `||[C,P_s]||=0`), so it
  can never **split** the orbit to assign a weight. (This is exactly the
  counting-vs-splitting localization of
  `KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29`.)

**SKa verdict: the wall is real.** No `U(3)`, `K`/CPT, or `Z_3` symmetry forces
the equal-block measure. The weight ratio is a genuine free measure choice. A new
readout-context premise is required to pin it. (This is the honest difference
from the two B-AXIS no_gos that *were* over-strong: here the skeptical attack
confirms the wall rather than breaking it.)

### SKb — Is the T1-d determinant FORM a missing axiom?

No, and this **shrinks** the wall. The det-vs-trace **form** selection is already
a no-new-axiom theorem: a scalar character multiplicative under operator
composition is `det^k` by the `GL(n)` abelianization (commutator subgroup is
`SL(n)`), and the trace **fails** the character property
(`tr(A·S) ≠ tr(A)·tr(S)`) — see
`OBSERVABLE_PRINCIPLE_DET_UNIQUE_MULTIPLICATIVE_CHARACTER_FORM_SELECTION_NARROW_THEOREM_NOTE_2026-05-28`,
re-verified in the runner (det multiplicative under composition and direct sum;
trace neither). **Therefore the entire 887-descendant fanout of
`observable_principle_from_axiom_note` is NOT a missing axiom.** The genuine
residual is only the *identification* clause: that a record reads out `Z=det`,
and that disjoint blocks register as disjoint records. That clause is a
**readout-context** statement (it identifies Record's abstract additivity with
the determinant readout), and it is exactly the same gate as R1/R2. So R4's true
contribution to this cluster is the thin identification bridge, not a standalone
observable axiom.

---

## 3. The candidate primitive (weakest sufficient statement)

> **Readout-context / outcome-measure primitive (CANDIDATE; NOT adopted).** A
> supplied readout context comes with a central-sector decomposition whose
> statistical measure assigns **one atom (one statistical slot) per irreducible
> record OUTCOME** — i.e. per `K`/CPT orbit / per irreducible Dirac–record
> factor — rather than per central-sector real component. Equivalently: the
> physical readout criterion is **maximum objective information over the objective
> outcome alphabet** (count the objective `K`-real outcome **labels**, the
> indifference / atom-share measure), not the Born/rank/dimension weight. The
> scalar record readout of a sector is a single objective scalar of that sector
> (the determinant character on the matter block), and disjoint outcomes register
> as disjoint records.

This is a single **criterion/measure** statement. It is **dimension-blind**: it
counts irreducible outcomes, never their rank, dimension, or Born amplitude. It
supplies **no** weight, probability, normalization, Born rule, mixing angle,
phase, or mass number — it supplies only the *measure class*. In one line: **a
record counts OUTCOMES, not components.**

Its three equivalent faces (proved equivalent in §4 / runner SKc):
1. **equal-block `(1,1)` sector measure** (atom-share over the singlet/doublet
   `K`-real sectors) — the R1 face;
2. **maximum-objective-information / indifference selector** over the objective
   outcome alphabet (uniform over labels) — the R2 face;
3. **orbit-occupancy** (one slot per `K`/CPT outcome, not per real component) —
   the R3/R5 face and the `KOIDE_ORBIT_OCCUPANCY_..._2026-06-09` `ξ=1` candidate.

---

## 4. Conditional derivation (`hypothetical_axiom_status` throughout)

All statements in this section are **conditional on the candidate primitive of
§3 being accepted by owner/governance**; none is retained on the current surface.

### The lever (landed, no new axiom)

On the `C_3` generation surface the square-root mass vector splits into a
democratic singlet (`E_+ = 3a^2`) and a doublet (`E_perp = 6|b|^2`), giving the
landed identity
`Q = (Σ s_i²)/(Σ s_i)² = 1/3 + (2/3)·|b|²/a² = (1+2r)/3`, with `r = |b|²/a²`
(`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10`,
`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10`). The
sector-weighted capacity `w_s log E_+ + w_p log E_perp` at fixed total power
extremizes (Lagrange) at `E_perp/E_+ = w_p/w_s`, i.e.

> **`r* = w_p/(2 w_s)`** — the maximizer is a **continuous function of the free
> weight ratio `t := w_p/w_s`**.

The runner verifies this closed form against a numeric argmax at five weight
pairs. The two-block pointer fixes that there are **two** terms, never the value
of `t`.

### R1 (measure) discharges conditionally

The candidate's equal-block face supplies `t=1` (`w_s = w_p`), hence

> **`r* = 1/2` ⇒ `Q = 2/3`** (exact). `hypothetical_axiom_status: conditional`.

The contrasting rank/Born `(1,2)` face gives `t=2 ⇒ r*=1 ⇒ Q=1`. So the proposal
is **non-vacuous and falsifiable**: a different readout context gives a different,
empirically distinguishable value (runner R1; the `(1,2)` horn `Q=1` is excluded
by the charged-lepton data by ~50%).

### R2 (objectivity) discharges conditionally — and coincides with R1

A spectrum-broadcast/QD state has full redundant objectivity (observer plateau
`= H(weights)`) for **any** weights on the two-symbol objective alphabet, so
objectivity-as-broadcast is a readout of supplied weights, not a selector (runner
R2 NO-GO legs; reproduces `FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT`). The
candidate's **maximum-objective-information** face instead picks the **uniform**
distribution over the two objective **labels** (1 bit, `H(unif) > H(rank)`),
which is the equal-block weights — the **same `t=1` pin** as R1. So R1 and R2 are
one choice (§5 minimality), not two independent inputs.

### R3 (the `W_t`-independence countermodel — why the axiom must be exactly this)

The task asks specifically for the `W_t`-independence countermodel from the
conditional note's route R3, and it is the load-bearing demarcation. Consider the
**dephasing/relaxation (einselection) fixed point**: in the pointer basis it is
the maximally mixed `I/3`. Pushed through the singlet/doublet split it gives the
**rank** weights `(1/3, 2/3)` ⇒ `r = 1`, **not** `1/2` (runner R3). Therefore:

> **A record-PRODUCTION / decoherence-dynamics axiom (Cluster 1) does NOT pin
> `t=1`.** Same einselection, the value comes out `r=1` (`t=2`), not `r=1/2`. The
> weight-ratio dial `W_t` is **independent** of the existence of einselecting
> dynamics.

This countermodel is exactly why a *separate* readout-context measure primitive
is needed: what pins equal weights is a **readout criterion** (count outcomes),
not the existence of record-producing dynamics. It also pins down the **minimal**
content of the proposal: the candidate must be *precisely* the statement that the
weight ratio is `t=1` (outcome-counting), and nothing more — it must not be
smuggled in as a dynamics axiom (which would give the wrong value) and must not
carry a numeric weight (which would violate Record's non-supply clause). The
runner confirms `t=1` is the unique pin and that the dynamics route lands at
`t=2`.

### R4 (det-readout identification) discharges conditionally

With SKb the det **form** is already a theorem, so the residual is only the
identification. Record supplies additive scalar readout over disjoint records;
the candidate's "a record reads out the sector determinant scalar; disjoint
blocks = disjoint records" clause turns that record-additivity into generator
additivity `W(Z_1 Z_2) = W(Z_1) + W(Z_2)` on `R_{>0}` (the determinant is
real-positive on the staggered zero-source surface — runner R4). Continuity then
forces, by the Cauchy classifier,

> **`W = c·log det`, `c=1` conventional** (runner: Cauchy residual `4e-16`).
> `hypothetical_axiom_status: conditional`.

This is the same readout-context gate as R1/R2 (a "a record reads out a sector
scalar" clause), so R4 is discharged by the **same** primitive, not a fourth one.

### R5 (P-REC single-taste pointer) discharges conditionally

`NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02` proves the `Cl(3)` volume element
`ω = σ₁σ₂σ₃ = iI` is central in `M_2(C)`, so **no on-site operator anticommutes
with all three Pauli generators** — there is no per-site `gamma_5` (runner R5:
exhaustive search finds no anticommutant). Hence the single-taste / chirality
**pointer selector cannot be an on-site operator**; it must be supplied as a
*readout context* — "one record outcome per irreducible Dirac/taste factor." That
is the **same** "one slot per irreducible record outcome" choice as the
orbit-occupancy measure. So P-REC's taste selector is discharged by the candidate
primitive's readout-context clause (in its species face), tying the Koide measure
and the anomaly-chain P-REC residual to one decision. (Note: P-REC's full
discharge also needs the Cluster-3 gauge/particle-content axiom for the
*existence* of the irreducible Dirac factor; the candidate here supplies only the
**readout selection** of one outcome per factor — the part that lives in the
readout-context gate.)

---

## 5. Minimality — why this is the weakest sufficient addition

**It is ONE choice, not five.** The runner's SKc block exhibits the two
consistent generation models from `KOIDE_ORBIT_OCCUPANCY_..._2026-06-09`:

```
M_sector : one slot per REAL component (a; x; y)  -> Z_d = 2π/g -> r = 1   (Q=1)
M_orbit  : one slot per record OUTCOME (a; b)      -> Z_d =  π/g -> r = 1/2 (Q=2/3)
```

and verifies the **convention-free** identity `r_sector / r_orbit =
Z_sector / Z_orbit = 2` — the cell ratio **is** the 2:1 `K`/CPT occupancy fiber,
independent of any normalization. The five faces collapse:

- equal-block `(1,1)` measure (R1) = uniform-label objectivity selector (R2) =
  one-slot-per-outcome orbit-occupancy (R3 pin / R5) = the readout of one sector
  determinant scalar (R4). All assert **`t = 1` = count outcomes, not
  components.**

So the candidate is a **single binary structural choice** ("count objective
record outcomes, not central-sector real components"), of the same *category* as
the approved `kinetic_isotropy_primitive` ("the tick is grained like the spatial
edge"): dimensionless, structural, binary, no fitted number. This is why the
conditional note's N2 listing of "two independent inputs" is, on this reading, a
single readout-context choice (the task's SK-4 minimality crack on the wall-count;
the runner shows the atom-share measure and the label-count objectivity selector
**coincide**).

**What it does NOT grant.** The primitive supplies a *criterion/measure class*
only. It does **not** supply: any weight, probability, Born rule, normalization
constant, mixing angle, CP phase `δ` (which remains the separate radian-period
admission), any mass value, the record-PRODUCTION dynamics (Cluster 1 — and R3
shows those dynamics would give the *wrong* value, so the primitive is strictly
not a dynamics axiom), or the gauge/particle content (Cluster 3 — the *existence*
of the irreducible Dirac factor whose outcome R5 selects). It is consistent with
Record's verbatim non-supply clause: Record says "no occupancy rule"; this
primitive supplies that occupancy rule as a separately-recorded science-level
decision, never folded into Record.

**Strength ranking.** Per the sibling `WALL_TO_GATE_MAP.md` coverage table, this
cluster (C2) ranks **C2 ≈ C1 > C3** in fanout-per-unit-strength: it is a weak
addition (a readout criterion supplying no values) with large transitive reach
(Koide cone 327 + observable identification half of 887 + flavor readout-context
rows). Recommended owner sequence: weak high-leverage first (C1 then C2), with C3
deferred.

---

## 6. Tensions with retained no-gos

The proposal is an **addition**; it must be **consistent** with — not contradict
— every retained result. Checked:

- **`FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02` (no_go).** No
  tension. That no_go's *positive* content is "objectivity fixes basis not
  weight," and its own N6/N7 explicitly name "a maximum-objective-information /
  indifference rule over objective labels" as a **coherent possible additional
  principle** outside QD-objectivity-as-broadcast. The candidate IS that named
  additional principle. It does not claim QD-broadcast forces the weight (it
  agrees it does not); it adds the indifference criterion as a separate premise.
- **`KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31` (bounded_theorem).**
  No tension; the candidate supplies exactly its two named inputs, and the note's
  N6 states "this note does not call for a new axiom" — i.e. it leaves the door
  open for an explicit admission, which is what this proposal is.
- **`KOIDE_ORBIT_OCCUPANCY_..._2026-06-09` (bounded_theorem + premise
  candidate).** No tension; the candidate is precisely its stated (unadopted)
  orbit-occupancy premise, with the same `ξ=1` framing and the same
  convention-free factor-2 fiber.
- **`NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02` (no_go).** No tension; the
  candidate **respects** it (it places the taste/chirality selector in the
  readout context precisely *because* it cannot be on-site).
- **`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` Boundary T1-d.** No tension; the
  candidate supplies the declared bridge premise the note already isolates as
  "not derivable from `minimal_axioms`."
- **Record axiom non-supply clause.** No tension; the candidate supplies the
  occupancy/measure rule that Record verbatim declines to supply, as a separate
  recorded decision (not a reword of Record — §1, policy §1).

No retained no_go asserts that the equal-block measure is **impossible** or that
some symmetry **forbids** it; they assert it is **not forced** from the current
surface. Adding a premise that supplies it is therefore consistent with all of
them.

---

## 7. Falsifiers

This proposal is falsifiable in several independent ways:

1. **A no-new-axiom derivation of the weight ratio.** If a future theorem derives
   `t=1` (equal block) from the current premise surface (e.g. a symmetry the SKa
   re-attack missed, or a retained dynamics route that lands at `t=1` rather than
   the `t=2` of R3), the candidate is **unnecessary** and should be withdrawn —
   the wall would be a no-new-axiom crack, not an axiom.
2. **The `W_t`-independence countermodel failing.** If the einselection fixed
   point were shown to give `t=1` rather than the rank `(1/3,2/3)` (R3), then a
   Cluster-1 dynamics axiom would already pin the measure and a separate
   readout-context primitive would be redundant. The runner exhibits `t=2` for
   the dynamics route; a corrected dynamics calculation giving `t=1` would
   falsify the "separate primitive needed" claim.
3. **The five faces NOT coinciding.** If the equal-block measure, the
   label-count objectivity selector, and orbit-occupancy were shown to be
   genuinely independent choices (e.g. a model where atom-share `≠` label-count),
   the "one minimal choice" claim collapses and the proposal would be heavier
   (multiple inputs) than stated. The runner's SKc verifies they coincide on the
   exhibited surface; a counterexample falsifies minimality.
4. **Empirical.** Conditional on the candidate, `Q = 2/3` (the `(1,1)` horn). The
   `(1,2)` rank horn gives `Q=1`. The charged-lepton comparator (labeled,
   non-input) sits at `Q_PDG ≈ 0.66666`, on the `2/3` horn to `~6×10⁻⁶`; a
   future sharpened value materially off `2/3` would disfavor the equal-block
   face of the candidate.
5. **SKb wrong.** If the det **form** turned out NOT to be a no-new-axiom theorem
   (e.g. the multiplicative-character argument is found circular on the framework
   surface), then R4 would need more than the thin identification clause, and the
   cluster boundary would shift.

---

## 8. Load-bearing sources (landed)

- `docs/KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md` — the two-input
  conditional (`r* = w_p/(2 w_s)`; equal weights ⇒ `r=1/2`; route R3 dephasing
  countermodel).
- `docs/FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md` — objectivity
  fixes basis not weight; `I/3` `U(3)`-invariant; names the max-information rule
  as a coherent extra principle (N6/N7).
- `docs/KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md` — the three
  canonical weightings table `(1,0)/(1,1)/(1,2) → Q = 1/3, 2/3, 1`; counting-vs-
  splitting localization.
- `docs/KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`
  — the residual atom is the sector-vs-orbit slot count (ratio 2); the
  orbit-occupancy `ξ=1` premise candidate; the two consistent exhibited models.
- `docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` — Boundary T1-d (the declared
  readout-identification bridge premise).
- `docs/OBSERVABLE_PRINCIPLE_DET_UNIQUE_MULTIPLICATIVE_CHARACTER_FORM_SELECTION_NARROW_THEOREM_NOTE_2026-05-28.md`
  — the det-vs-trace FORM is a no-new-axiom theorem (SKb).
- `docs/NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md` — `ω = iI`; no per-site
  `gamma_5` (R5).
- `docs/MINIMAL_AXIOMS_2026-06-05.md`, `docs/audit/AXIOM_MINIMALITY_POLICY.md` —
  axiom surface, open-gates list, §6 approval mechanism.
- Sibling: `.claude/science/physics-loops/axiom-update-proposals/WALL_TO_GATE_MAP.md`
  (the three-cluster map; this note is the deep dive on Cluster 2).

---

## 9. One-paragraph summary

The Koide `r=1/2` measure and objectivity walls, the observable-principle T1-d
det-readout identification, and the anomaly-chain P-REC single-taste pointer all
sink into one open gate — *readout context / sector measure / objectivity /
occupancy*. A genuine skeptical re-attack confirms the central wall is real: no
`U(3)`, `K`/CPT, or `Z_3` symmetry forces the equal-block measure (`U(3)`-
invariance picks the *rank* weights, `K`/CPT and `Z_3`-equivariance fix only the
basis), and the det-readout **form** is already a no-new-axiom theorem so only the
thin identification clause remains. The `W_t`-independence countermodel (route R3)
shows the einselection fixed point gives `t=2` (`r=1`), so a record-production
dynamics axiom does **not** pin the measure — what is missing is exactly a
readout criterion. The weakest sufficient addition is a single dimension-blind
readout-context primitive — *a record counts objective OUTCOMES (`K`/CPT orbits /
irreducible Dirac factors), not central-sector real components* — whose three
faces (equal-block `(1,1)` measure, maximum-objective-information label-count
selector, orbit-occupancy slots-per-outcome) provably coincide and pin the free
weight ratio to `t=1`. Conditional on it (`hypothetical_axiom_status: conditional
on accepted new axiom; not retained`): `r=1/2`, `Q=2/3`; the T1-d Cauchy
identification `W = c log det`; and the P-REC outcome-per-factor selection. A
41/41-passing runner verifies, for every wall, that the no_go genuinely walls
(including that no symmetry forces the measure) and that the single primitive
discharges it, supplying no weight/probability/normalization number. This is a
proposal FOR the owner's governance decision; it adopts nothing and sets no audit
verdict.
