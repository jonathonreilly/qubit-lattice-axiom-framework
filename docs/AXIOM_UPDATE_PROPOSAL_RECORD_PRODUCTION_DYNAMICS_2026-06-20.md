# Axiom-Update PROPOSAL — A Minimal Record-Production-Dynamics Primitive as the Common Sink for the Single-Clock B-AXIS Walls (N2b / N4 / N5) and the Arrow

**Date:** 2026-06-20
**Type:** axiom-update PROPOSAL (owner-authorized; for a governance decision)
**Claim type:** proposal
**Cluster:** CLUSTER 1 of the axiom-update-proposals block01 wall→gate map — the
record-production / decoherence / arrow gate.
**Lane / branch:** `axiom-update-proposals`,
`physics-loop/axiom-update-proposals-block01-20260620`.
**Status authority:** independent audit lane / owner ONLY. This note sets no
audit verdict, promotes no axiom, and adopts nothing. It is a proposal FOR the
owner's governance decision, per the owner's explicit authorization to go beyond
the no-new-axiom rule and deliver either no-new-axiom cracks OR candidate
axiom-update proposals.

**CRITICAL STATUS DISCIPLINE.** Every conditional derivation below maps the
consequences of an **UNADOPTED** candidate primitive and therefore carries

> `hypothetical_axiom_status: "conditional on accepted new axiom; not retained on
> the actual current surface."`

No bare `retained` / `promoted` appears anywhere. Labeling a consequence
"conditional" does **not** promote the candidate; only an external owner /
governance decision can do that (`docs/audit/AXIOM_MINIMALITY_POLICY.md` §1, §4,
§6).

**Primary runner:**
[`scripts/axiom_update_record_production_dynamics_cluster_2026_06_20.py`](../scripts/axiom_update_record_production_dynamics_cluster_2026_06_20.py)
**Cached output:**
[`logs/runner-cache/axiom_update_record_production_dynamics_cluster_2026_06_20.txt`](../logs/runner-cache/axiom_update_record_production_dynamics_cluster_2026_06_20.txt)
(**TOTAL: PASS=34 FAIL=0**, deterministic, no RNG in any load-bearing leg, no
empirical import).

**Parent map (relocation analysis):**
[`.claude/science/physics-loops/axiom-update-proposals/WALL_TO_GATE_MAP.md`](../.claude/science/physics-loops/axiom-update-proposals/WALL_TO_GATE_MAP.md)
(CLUSTER 1).

---

## 0. Posture and the order of operations

The owner posture is "don't believe the no-gos." So this note does, in order:

1. **A genuine no-new-axiom skeptical re-attack** on the three single-clock
   B-AXIS walls (N2b clock unit, N4 axis label, N5 second clock): can the
   high-fanout consumer be satisfied **without** any dynamics axiom? (§2)
2. Only the residual that **still walls** after the re-attack is escalated to a
   proposal, and the proposal is the **weakest** primitive that discharges it
   (§3–§4).
3. A real runner verifies, on explicit finite surfaces, both that the residual
   genuinely walls AND that the candidate primitive discharges each walled
   bridge conditionally (§5).
4. Minimality: exactly what the primitive grants and what it does **not** (§6).

The headline result of the re-attack is that **most of the B-AXIS fanout does
not need a dynamics axiom at all** — it needs only the *count* `d_t ≤ 1`, which
is supplied by the (already-walled-but-algebraic) construction/second-clock/tick
clauses. The single genuinely-walling residual that no current structure
supplies is the **existence of record-producing dynamics at all** (the
record-formation floor). The proposed primitive supplies exactly that floor, and
— as a *consequence* of a single record-production generator — simultaneously
discharges the axis label (N4), the single-clock count (N5), the production rate
(N2b-step), and the arrow.

---

## 1. The walls (verbatim from the landed campaign notes)

The single-clock cluster is governed by two retained no-gos plus the
axis-conditional evolution theorem:

- **`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`** (retained_no_go).
  "Stone uniqueness is transfer-relative and τ-relative. No-second-clock
  requires a separate axis/transfer uniqueness premise." Its checklist clauses:
  - **N2** — "the physical time step / block spacing `τ`" (the B-AXIS.1 clock
    unit `2a_τ`; this note's **N2b**);
  - **N4** — "uniqueness of the reflection-positive axis or transfer
    construction" (splits into the *construction* choice and the *axis label*);
  - **N5** — "exclusion of independent commuting transfer factors if the claim
    says no second clock".
- **`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`**
  (retained_no_go). Every retained candidate axis anchor (OS/GNS reconstruction,
  record/durability, the CAP-K registration cone, the anomaly/chirality chain)
  is **exactly transported** by the conjugated exchange
  `W = P_{τ↔1} ∘ diag((-1)^{x_τ x_1})` onto an equivalent `x_1`-axis structure
  (transport residuals exactly 0, identical spectra, durability =
  unitary-invariant operator-order monotonicity). Its **sharpened pin**: the
  minimal axis-selecting input is one per-axis `Z_2` BC-asymmetry datum **or the
  record-shaped equivalent — "the realized record history's event order is
  parametrized by lattice axis `μ`" (PIN-REG)**, which it explicitly classifies
  as record-adjacent but *not* an axiom consequence.
- **`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`**
  (bounded_theorem). Proves the single-clock codim-1 evolution **conditional on
  the declared (B-AXIS)** premise (= N2 + N4-construction + N5), and **withdraws**
  the prior claim that the temporal axis is the unique RP-admissible axis (the
  exchange `W` is an exact symmetry). Its named future supplier for (B-AXIS) is
  "a Record-axiom registration-direction theorem, or a boundary-condition
  selection row."

The dynamics floor under all of these:

- **`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`**
  (retained_no_go). `H=0`, decoupled `H`, and energy eigenstates are
  baseline-consistent **no-record** witnesses. "Forcing record formation
  unconditionally would require an imported measurement/decoherence-dynamics
  premise, **exactly what Record excludes**." The Record axiom verbatim supplies
  "no … measurement/decoherence dynamics, time metric, … occupancy rule."

---

## 2. The skeptical no-new-axiom re-attack (attempted FIRST)

### 2.1 N4 axis-label is OVER-SPECIFIED for the fanout (partial crack, no axiom)

The B-AXIS cluster's ~959 fanout is realized almost entirely through one
consumer: `ANOMALY_FORCES_TIME_THEOREM.md` (node fanout ~1049). Read what that
consumer actually imports:

> SC row: "given the cited note's declared (B-AXIS) premise … exactly one
> generator `H` … is supplied, giving the imported cap **`d_t ≤ 1`**. The
> finite-speed propagation clause … is **not load-bearing for the dimension-count
> cap here**." And its non-circularity section: "the anomaly steps … constrain
> only the **count** `d_t` (parity and positivity), **not which axis is
> temporal**."

So the high-fanout consumer needs the **count** `d_t ≤ 1`, and is provably
**axis-label-blind**. The runner confirms the two objects the anomaly chain
reads — the staggered chirality grading `ε(x)=(-1)^{Σx_μ}` and the chiral
anticommutation `{D_hop, ε}=0` — are **exactly** `W`-invariant (residuals `0`),
so no part of the anomaly argument can tell the `τ` and `x_1` axes apart.

**Crack conclusion (no axiom):** the *axis-label* half of N4 is over-specified
for fanout. The campaign already flags this shape (the axis-label no_go is a
*correction* of the earlier over-strong "RP-selects-axis" claim, exactly like the
B-AXIS exercise's two corrected over-strong no_gos). The ~959 fanout therefore
hangs on the **count**, supplied by {N4-construction, N5, N2}, not on the label.
This is a genuine partial crack: it removes the *axis label* from the
axiom-bearing residual.

### 2.2 N5 and N2b genuinely wall — but in the *count*, not the *label*

Having reduced the fanout to the count `d_t ≤ 1`, re-attack the count's
ingredients with no dynamics axiom:

- **N5 (no independent commuting clock).** The scope boundary §3 shows two
  commuting tensor-factor transfers `T_A⊗I`, `I⊗T_B` lift to a product whose
  Stone generator is the *sum*, and the factor groups survive. The runner
  recomputes this exactly (`||H_prod − H_sum|| = 4.4e-16`, `[H_A,H_B]=0`): **no
  state-blind algebra removes the second commuting clock.** N5 does **not** crack
  algebraically.
- **N2b (clock unit `2a_τ`).** `T` fixes only `τ·H`, not `H` (runner: same `T`
  reconstructs for `τ=1,2,0.7` with `H∝1/τ`). The wall is real. **But this is
  flagged SK-1 in the parent map: the *dimensionful* tick value is a candidate
  no-new-axiom crack via `scale_reference_primitive × kinetic_isotropy_primitive`
  extended to the time edge — a different, already-approved-primitive question,
  NOT this dynamics cluster.** This note therefore does **not** propose anything
  for the dimensionful tick value; it only addresses the *dynamics-side*
  existence of a production step (§4(iv)).

### 2.3 What is left, and why it does not crack

After §2.1–§2.2 the residual that no current structure supplies, and that does
**not** crack, is the **existence of record-producing dynamics at all**:

- The record-formation no_go's witnesses (`H=0`, decoupled `H`, eigenstate) are
  *exact* baseline-consistent no-record points (runner re-confirms `|coh|`
  frozen at `0.5`). The Record axiom **verbatim** excludes decoherence dynamics.
- Both the single-clock-count clauses (N5: which transfer is the physical clock)
  and the axis label (N4: which direction carries the realized event order) are,
  on the current surface, choices among structures the static algebra cannot
  distinguish. The thing that *would* distinguish them is a **dynamical** fact:
  that there is a process that actually produces a record stream, with a
  direction and a single generator.

This is the genuine residual the proposal targets. It sinks into the
`MINIMAL_AXIOMS_2026-06-05.md` open gate **"arrow / measurement / decoherence /
record-production dynamics"** — the memo's largest open gate, declared **outside**
axiom content (so proposing content here is not a reword of an existing axiom,
which the policy forbids; it is content in a named open gate, recorded as an
unmade science-level decision).

---

## 3. The candidate primitive (minimal, UNADOPTED)

> **(RP-DYN) — candidate record-production-dynamics primitive.** There exists a
> single completely-positive trace-preserving (CPTP) **record-production
> generator** `L` — equivalently a one-parameter CPTP semigroup `Φ_t = e^{tL}`,
> `t ≥ 0`, on system ⊗ environment — together with a **record-monotone**
> functional `R` (non-decreasing along the semigroup), such that for the realized
> state the pointer-basis coherence is monotonically suppressed (einselection)
> and a durable record is produced. The **registration direction** — which
> lattice axis carries the produced event order — is **this same object** (the
> orientation of `L`'s record stream).

`(RP-DYN)` asserts only **existence** of one such `(L, R)` and its orientation.
It is the dynamics-gate analogue of the `realized_state_primitive` slot: a
**slot** (record-producing dynamics exist) rather than **content** (a specific
kernel, rate, weight, or boundary state).

This is strictly the **weakest** form that discharges the residual: it is
weaker than a *past hypothesis* (an atypicality/low-entropy boundary claim, which
`realized_state_primitive` explicitly classifies as a *stronger* input and
forbids — see
`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`), and
weaker than supplying any specific Kraus map / production kernel / rate (those
stay supplied, per the post-record dynamics row maps).

---

## 4. Conditional derivation — every walled bridge DISCHARGES given (RP-DYN)

All consequences below carry
`hypothetical_axiom_status: "conditional on accepted new axiom; not retained on
the actual current surface."` Runner block references are the section tags in the
cached output.

### (i) The ARROW = the record-monotone's direction  [runner §3]
Along `Φ_t = e^{tL}` (`t ≥ 0`) the record-monotone `R` is non-decreasing; its
*direction* is the semigroup's orientation. The runner exhibits a pure-dephasing
realization in which a record proxy rises monotonically as `|coh|` falls. A
*unitary* step (no `L`) has `|coh|` constant — **no monotone** — so the arrow
lives in `L`'s irreversibility, not smuggled from the static surface. This is
exactly consistent with the arrow residual note: the arrow's *sign* still comes
from a low-record boundary (NOT supplied here), but its *existence as a monotone
direction* comes from the existence of record-producing dynamics, i.e. from
`(RP-DYN)`.

### (ii) N5 (single clock = single generator)  [runner §3]
`(RP-DYN)` supplies **one** generator. Conditional on it, the second commuting
tensor-factor "clock" is **not** an independent record stream: a single `L`
produces a single monotone record order. The runner shows that two *distinct*
einselection rates on two factors still yield **one** joint monotone record (the
joint which-path coherence is monotone under the single `L`) — one production
clock, not two. This supplies scope-boundary **N5** ("no independent commuting
transfer factor as a second physical clock") in its physical (record-stream)
reading — and **nothing more**: it does not forbid commuting algebra, so
gauge/redundant commuting factors survive (scope-boundary N6 stays open).

### (iii) N4 (axis = the registration direction)  [runner §3]
`(RP-DYN)`'s registration direction **is** the produced event-order axis. This is
exactly the record-shaped pin **PIN-REG** that the axis-selection no_go names. The
runner verifies the computable witness that a per-axis registration datum selects
one axis: realized as antiperiodic-`τ`/periodic-space it **breaks the exchange
exactly** (`||W M_ap W^T − M_ap|| = 8.0 > 0`), with the **falsification leg** that
symmetric BCs **restore** `W` (residual `0`) — so the selecting content is the
per-axis registration **asymmetry**, precisely what one record-production
direction supplies — and a **relabeling-invariant** discriminator (the temporal
and spatial 1D hop kernels then have *different dimension*, `0` vs `2`), so **no
exchange map of any kind** can identify the axes once the direction is supplied.

### (iv) N2b (rate = the generator's step)  [runner §3]
`L` carries a production rate `γ`; the runner exhibits a well-defined record
half-life. The generator's **step** is the record-stream tick. This supplies the
*dynamics-side* existence of a production step — it does **not** supply the
*dimensionful* value of `2a_τ`, which remains the SK-1 question
(`scale_reference × kinetic_isotropy` + realized-state data). `(RP-DYN)` grants
that a step **exists**, not its number.

### (v) The record-formation floor itself  [runner §3]
Conditional on `(RP-DYN)`, `|coh| → 0` monotonically as the number of
environment copies grows (`|coh|(N=1,2,4,16,64) → 0`), i.e. a durable,
redundantly-broadcast record (einselection / Quantum Darwinism). This is the
floor the record-formation no_go names as requiring an import; `(RP-DYN)` is that
import in its weakest existence form.

**Net:** one weak existence axiom discharges N4 (label), N5 (count), N2b-step,
the record-formation floor, and the arrow's existence. The ~959 B-AXIS fanout —
and transitively the path into the anomaly cap (~1049) via the registration-
direction route — is unlocked conditional on `(RP-DYN)`.

---

## 5. Runner (what it proves, and that the wall is genuine)

`scripts/axiom_update_record_production_dynamics_cluster_2026_06_20.py`,
**TOTAL: PASS=34 FAIL=0**. Structure:

- **[0]** recomputes the B-AXIS exchange baseline (periodic surface exactly
  `W`-invariant, residual `0`; non-trivial — plain swap fails by `11.3`), so the
  N4 wall is genuine here.
- **[1]** the skeptical crack: chirality grading and chiral anticommutation are
  exactly `W`-invariant (anomaly chain axis-label-blind → axis-label
  over-specified for fanout); N5 commuting-clock and N2b tick walls recomputed
  exactly (they do NOT crack algebraically); N2b dimensionful value flagged SK-1
  (relocated, not proposed).
- **[2]** the record-formation floor recomputed (`H=0`/decoupled/eigenstate keep
  `|coh|=0.5`): does NOT crack.
- **[3]** the conditional derivation: arrow monotone + reversibility contrast;
  N5 single-clock discharge; N4 axis-label discharge with restoration
  falsification leg and relabeling-invariant kernel-dim discriminator; N2b-step
  discharge; einselection durability.
- **[4]** minimality guards (no past hypothesis, no kernel/weight, no Born
  weights, no dimensionful tick, no contradiction with any retained no-go,
  consistency with `realized_state_primitive`).
- **[5]** fanout bookkeeping carried from the parent map / `load_bearing_summary`.

Every `[COND]` line is conditional on the UNADOPTED `(RP-DYN)`; the runner adopts
nothing.

---

## 6. Minimality — what `(RP-DYN)` grants and does NOT grant

**Grants (existence only):** that record-producing dynamics exist, as one CPTP
generator with one record-monotone and one orientation. From that single object
follow N4-label, N5, N2b-step, and the arrow's existence.

**Does NOT grant:**

- a **past hypothesis** / low-entropy boundary (the arrow's *sign* still needs
  one; that is a strictly stronger input the `realized_state_primitive` clauses
  forbid this primitive from supplying);
- a specific **kernel / Kraus map / production rate / weight** (rates and kernels
  stay supplied per the post-record dynamics row maps);
- **Born weights / probability / normalization** (those live in the
  readout-context / sector-measure gate = CLUSTER 2, not here);
- the **dimensionful** tick value `2a_τ` (SK-1:
  `scale_reference × kinetic_isotropy`), nor a fourth spatial dimension;
- the exclusion of commuting algebra in general (scope-boundary N6 — whether
  tensor-factor clocks are gauge/redundant — stays open; `(RP-DYN)` only
  excludes a *second record-producing* stream).

**Weakest sufficient addition.** Any addition that discharges the record-formation
floor must assert that *some* record-producing dynamics exist; `(RP-DYN)` asserts
*exactly that and no more* (existence of one generator + monotone + orientation).
Removing the monotone/orientation would fail to supply N4/N5/arrow; adding a
kernel/rate/boundary would be strictly stronger and is explicitly declined.

---

## 7. Consistency with the RETAINED no-go surface (a new axiom must ADD, not contradict)

`(RP-DYN)` is **additive** and contradicts no retained result; it supplies the
very import those no-gos name as missing:

- **scope boundary (retained_no_go):** `(RP-DYN)` supplies its N4 (axis/transfer
  construction, via the registration direction) and N5 (no second physical clock)
  as *consequences of a single production generator*; it leaves N6 (gauge/redundant
  tensor factors) open, exactly as the boundary requires a "separate
  axis/transfer uniqueness premise."
- **axis-selection no_go (retained_no_go):** `(RP-DYN)` is the **PIN-REG**
  record-shaped supplier that note names; the runner reproduces its exact
  BC-asymmetry break, restoration falsification leg, and relabeling-invariant
  kernel discriminator. It does not contradict the W-transport result — it
  supplies the extra datum the no_go says is required.
- **record-formation no_go (retained_no_go):** `(RP-DYN)` is precisely the
  "separate record-production/decoherence model" the no_go's N6 partial-closure
  path calls for; the exact no-record witnesses remain valid for the *baseline
  without* `(RP-DYN)`.
- **boost-faith / cubic-anisotropy no_gos (retained_no_go):** untouched — no
  boost action, no Lorentz content, no SO(4) wording is consumed or derived.
- **`realized_state_primitive` (approved Tier-A):** consistent — `(RP-DYN)`
  supplies the production-dynamics *slot* evaluated at the realized state; it
  supplies no state, measure, or typicality, and houses no past hypothesis.

---

## 8. Falsifiers (what would defeat this proposal)

- **A no-new-axiom derivation of record-production existence** from
  Lattice+Quantum+Record (would moot the proposal). The record-formation no_go's
  exact witnesses currently defeat this; a future derivation would retire the
  floor.
- **A consumer that needs the axis LABEL (not just the count `d_t`)** with large
  fanout: if such a consumer exists, §2.1's partial crack is narrower than
  claimed and more of the fanout is genuinely axiom-bearing (still discharged by
  `(RP-DYN)`, but the "over-specified" framing weakens).
- **Failure of the restoration falsification leg** (symmetric BCs not restoring
  `W`) would mean the BC realization is not a clean per-axis datum; the runner
  shows it restores exactly (residual `0`).
- **A demonstration that one CPTP generator does NOT yield a single monotone
  record order across commuting factors** would break the N5 discharge; the
  runner shows the joint coherence is monotone under the single `L`.
- **A demonstration that `(RP-DYN)` smuggles a weight/probability** (beyond
  existence) would break minimality; the runner's §4 guards check it grants none.

---

## 9. Honest status (audit-lane handoff)

```yaml
proposed_claim_type: proposal
proposed_claim_scope: |
  Candidate axiom-update PROPOSAL (CLUSTER 1, record-production dynamics gate).
  After a no-new-axiom skeptical re-attack that (a) cracks the axis-LABEL half of
  single-clock N4 as over-specified for the ~959 fanout (the anomaly consumer
  imports only the count d_t<=1 and is provably axis-label-blind: chirality and
  chiral anticommutation are exactly W-invariant), (b) recomputes that N5 (second
  commuting clock) and N2b (clock unit) genuinely wall on the static surface, and
  (c) confirms the record-formation floor does not crack (H=0/decoupled/eigenstate
  no-record witnesses are exact; Record verbatim excludes decoherence dynamics),
  the residual that genuinely walls is the EXISTENCE of record-producing dynamics.
  The proposal is the weakest primitive (RP-DYN): there exists one CPTP
  record-production generator L (semigroup e^{tL}, t>=0) with a record-monotone R
  and an orientation (the registration direction). Conditional on (RP-DYN) the
  runner verifies, on explicit finite surfaces, that the arrow's existence, N5
  (one generator = one clock), N4 (axis = the registration direction, with exact
  BC-asymmetry break, symmetric-BC restoration falsification leg, and a
  relabeling-invariant kernel-dimension discriminator), and N2b-step (the
  generator's rate) all DISCHARGE. The dimensionful tick value 2a_tau is NOT
  proposed here (SK-1: scale_reference x kinetic_isotropy).
proposed_load_bearing_step_class: C (computed finite-surface witnesses: the
  W-exchange baseline and its chirality-invariance crack are class C; the Stone
  commuting-factor recomputation is class A; the conditional einselection /
  monotone / kernel-dimension discharges are class C on explicit toy systems).
status_authority: independent audit lane / owner only
actual_current_surface_status: no-go (record formation not forced; axis-label
  and second-clock underivable from the static surface) + proposal (RP-DYN as the
  weakest discharging primitive)
hypothetical_axiom_status: "conditional on accepted new axiom; not retained on the actual current surface"
admitted_observation_status: null
proposal_allowed: true
proposal_allowed_reason: |
  Owner explicitly authorized axiom-update proposals for this lane. This note
  records (RP-DYN) as an UNMADE science-level decision in a named open gate
  (arrow/measurement/decoherence/record-production dynamics) per
  AXIOM_MINIMALITY_POLICY sections 1 and 4; it adopts nothing, edits no axiom
  file, writes no audit data, and sets no verdict.
adopts_axiom: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

**Not in scope.** Adopting `(RP-DYN)`; deriving a production kernel/rate/weight;
deriving the arrow's sign (the past hypothesis); supplying Born weights; the
dimensionful tick value (SK-1); the gauge/particle-content and readout-context
gates (CLUSTERs 2 and 3); editing `docs/audit/data/`.

---

## 10. Citations

- governing boundaries (retained_no_go):
  [`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md),
  [`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`](SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md),
  [`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md)
- axis-conditional evolution theorem (bounded_theorem; declares B-AXIS, withdraws
  the unique-RP-axis claim):
  [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md)
- high-fanout consumer (imports only the count `d_t ≤ 1`; axis-label-blind):
  [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md)
- arrow residual (sign = boundary; existence = dynamics):
  [`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md)
- record-production interface and dynamics-needed row maps (kernels/rates stay
  supplied):
  [`RECORD_PRODUCTION_INTERFACE_PRINCIPLE_2026-06-06.md`](RECORD_PRODUCTION_INTERFACE_PRINCIPLE_2026-06-06.md),
  [`POST_RECORD_PRODUCTION_DYNAMICS_NEEDED_ROW_MAP_2026-06-06.md`](POST_RECORD_PRODUCTION_DYNAMICS_NEEDED_ROW_MAP_2026-06-06.md)
- axiom surface and policy:
  [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md),
  [`audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- parent relocation map (CLUSTER 1):
  [`../.claude/science/physics-loops/axiom-update-proposals/WALL_TO_GATE_MAP.md`](../.claude/science/physics-loops/axiom-update-proposals/WALL_TO_GATE_MAP.md)
- standard external references (theorem-grade, no numerical input):
  Zurek (2003) *Rev. Mod. Phys.* 75, 715 (einselection / pointer states);
  Lindblad (1976) *Comm. Math. Phys.* 48, 119 (CPTP semigroup generators);
  Stone (1932) *Ann. Math.* 33, 643.
