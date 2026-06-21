# Axiom-Update Proposal — Unified Operational Measurement Axiom (block04, 2026-06-20)

**Date:** 2026-06-20 (synthesis authored 2026-06-21)
**Type:** meta / governance proposal — AXIOM MINIMIZATION / UNIFICATION analysis
(FOR the owner's governance decision — adopts nothing).
**Lane / branch:** `axiom-update-proposals`,
`physics-loop/axiom-update-proposals-block04-20260620`.
**Status authority:** the independent audit lane / owner is the **sole** status
authority. This note sets **no** audit verdict, promotes **no** axiom, edits **no**
axiom registry, and writes **nothing** to `docs/audit/data/` (read-only this lane).

```yaml
proposal_allowed: false   # owner governance decision required; this note REQUESTS it, does not make it
adopts_axiom: false
sets_audit_verdict: false
edits_axiom_premise_nodes: false
status_authority: independent audit lane / owner only
hypothetical_axiom_status: "conditional on accepted new axiom; not retained on the actual current surface"
```

> **`hypothetical_axiom_status` (carried throughout):** *"conditional on accepted
> new axiom; not retained on the actual current surface."* Every "derives" /
> "discharges" / "collapses" claim attached to the candidate below is a consequence
> of an **UNADOPTED** primitive. Labeling a consequence "conditional" does **not**
> promote it; only an external owner / governance decision can
> (`docs/audit/AXIOM_MINIMALITY_POLICY.md` §1/§4/§6). No bare `retained` /
> `promoted` appears anywhere in this note.

---

## 0. What this synthesizes (the minimization move)

`AXIOM_MINIMALITY_POLICY.md` targets the **weakest sufficient, non-redundant,
independent** extension with **no laundering**. Block01 delivered three candidate
axiom-update proposals; block02/03 confirmed the C1-N2b and C3-P-ABJ residuals
genuinely wall (no no-new-axiom crack landed). The remaining minimization move not
yet tested was **unification**: block01's

- **C1 (RP-DYN)** — a record-production / decoherence-**dynamics** primitive
  (one CPTP einselecting generator + record-monotone + orientation; existence
  only), in the memo's *arrow / measurement / decoherence / record-production
  dynamics* gate, and
- **C2 (READOUT-MEASURE)** — a readout-context / objectivity / **sector-measure**
  primitive, in the memo's *readout context / sector measure / objectivity /
  occupancy* gate,

sit in two *different* open gates of `MINIMAL_AXIOMS_2026-06-05.md`, but they are
arguably two faces of **one physical act**: a system–environment **measurement
interaction that produces durable records with a readout**. If a single such axiom
subsumes both discharge sets, the candidate **count** drops (2 weak axioms → 1) —
exactly the minimization the policy rewards.

This note records the result of testing that unification across two runner legs:

1. **SUFFICIENCY** (does one axiom derive *both* discharge sets?) —
   runner `scripts/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.py`,
   **PASS=39 FAIL=0**;
2. **MINIMALITY + INDEPENDENCE** (is the one axiom strictly weaker than C1+C2,
   policy-preferred, and independent of its residuals; does C3 fold?) —
   runner `scripts/axiom_update_unified_axiom_minimality_independence_2026_06_21.py`,
   **PASS=28 FAIL=0**.

Both runners reuse the **exact** load-bearing legs of the two block01 cluster
runners (same staggered `W`-exchange surface, same chirality grading, same
controlled-broadcast dephasing/einselection, same Koide capacity lever
`r* = w_p/(2 w_s)`, same SBS plateau `= H(weights)`, same `I/3` fixed point, same
2:1 occupancy fiber), so the fold is a genuine fold of the **same** objects, not a
fresh toy that merely happens to pass. Both reproduce deterministically (re-run
2026-06-21; clean under `python3 -W error`; numpy + stdlib only; no empirical
import; no RNG draw load-bearing).

**Headline result: PARTIAL COLLAPSE.** One unified operational axiom folds C1's
full discharge set **and** C2's basis/identification half, is **strictly weaker**
than C1+C2 stated separately, and is preferred by `AXIOM_MINIMALITY_POLICY.md` on
all four of its criteria — but it provably **cannot** supply two things, which are
isolated as their own weakest data: the **equal-block `(1,1)` sector-measure
weight** and the **time-edge spacing `a_tau/a_s`**. C3 (gauge content) does **not**
fold; it stays a categorically separate gate-3 candidate.

---

## 1. The unified candidate axiom (precise statement, UNADOPTED)

> **(MEAS-REC-READOUT) — candidate unified measurement-with-readout primitive.**
> There is a system–environment **measurement interaction that produces durable
> records**, and — *for the realized state* — it supplies **at once**:
>
> - **(a) DYNAMICS + ARROW.** An einselecting completely-positive trace-preserving
>   (CPTP) dynamics `Φ_t = e^{tL}` (`t ≥ 0`) with an **orientation**: along the
>   semigroup, pointer-basis coherence is monotonically suppressed and a durable,
>   redundantly-broadcast record forms; the orientation is the **registration
>   direction** (which lattice axis carries the produced event order). *(= C1's
>   dynamics + arrow + registration direction.)*
> - **(b) POINTER BASIS = THE CENTRAL-SECTOR / `K`-CPT DECOMPOSITION.** The basis
>   the dynamics einselects is the framework's central-sector / `K`-CPT
>   decomposition — the **alphabet of distinguishable record outcomes** (one slot
>   per irreducible `K`/CPT orbit / irreducible Dirac–record factor). *(= C2's
>   readout context.)*
> - **(c) OBJECTIVITY / SBS BROADCAST CRITERION (BASIS ONLY).** The objective
>   record observable is the one **redundantly broadcast** to many environment
>   fragments (spectrum-broadcast / quantum-Darwinism): objectivity is what makes
>   the einselected pointer basis the *objective* alphabet. *(= C2's objectivity
>   selector, **basis** part.)*
>
> It asserts **EXISTENCE only** — one `(L, pointer basis, broadcast structure)`
> for the realized state. It is a **slot** (the measurement-gate analogue of
> `realized_state_primitive`), **not content**: it supplies **no** kernel/rate,
> **no** weight/probability/normalization/Born rule, **no** spacing, and **no**
> arrow *sign* (no past hypothesis).

**Why this is the weakest single statement spanning both gates.** Weaken any clause
and one of the two discharge sets fails: drop (a) → no arrow / N4 / N5; drop (b) →
no pointer alphabet / no T1-d identification target; drop (c) → no *objective*
alphabet. Strengthen it with a weight / probability / kernel and it over-reaches —
and would clash with the load-bearing **weight-blindness** finding (§4). So it is
exactly the weakest single axiom that could discharge what both gates need.

**Strength: weak–medium** (one existence slot spanning the dynamics and
readout-context gates; weaker than a past hypothesis).

---

## 2. Conditional derivations it supplies — C1's full set (leg A)

All lines `hypothetical_axiom_status: conditional`. Runner
`…sufficiency…` PART [1]; the surface is the periodic staggered Kogut–Susskind hop,
recomputed exactly `W`-invariant (`||W M W^T − M|| = 0.0`) so the axis-label wall
is genuine here.

| C1 wall | Discharged by clause | Conditional derivation (runner witness) |
|---|---|---|
| **arrow** (existence as a direction) | **(a)** | the einselecting dynamics' orientation **is** the record-monotone direction; the record proxy rises monotonically as `|coh|` falls; a unitary step has no monotone. |
| **B-AXIS N5** (single clock) | **(a)** | **one** generator ⇒ one monotone record order even across two factors with *distinct* rates (joint `|coh|/0.5` monotone) ⇒ a single production clock. |
| **B-AXIS N4** (registration direction) | **(a)** | the orientation **is** the registration direction (PIN-REG); the realized antiperiodic-`τ`/periodic-space datum breaks the exchange **exactly** (`||W M_ap W^T − M_ap|| = 8.0 > 0`); **falsification leg**: symmetric BCs **restore** `W` (residual `0.0`), so the selecting content is the per-axis registration *asymmetry*. |
| **B-AXIS N2b-step** (a step exists) | **(a)** | the generator carries a rate `γ` ⇒ a well-defined record half-life (`t≈0.415`) — the *dynamics-side* existence of a tick; **not** the dimensionful value (see §4.2). |
| **record-formation floor** | **(a)+(c)** | `|coh|(N=1,2,4,16,64) → 0` monotonically as #env copies grows ⇒ a durable, redundantly-broadcast record (einselection / quantum Darwinism). |

**Leg A verdict (runner PASS): the single unified axiom derives all of C1** — N4 +
N5 + arrow + N2b-step + floor. **C1 collapses into MEAS-REC-READOUT**; no separate
dynamics axiom is needed beyond it.

---

## 3. Conditional derivations it supplies — C2's basis / identification half (leg B)

All lines `hypothetical_axiom_status: conditional`. Runner PART [2]. This leg
delivers exactly the part of C2 that is a *pointer-basis / readout-context /
objective-alphabet* fact. (The *weight* part is the residual; see §4.1.)

| C2 wall | Discharged by clause | Conditional derivation (runner witness) |
|---|---|---|
| **R4 — observable T1-d det-readout identification** | **(b)+(c)** | the det **FORM** is already a no-new-axiom theorem (SKb: `det` is a multiplicative character, `tr` is not). Clauses (b)+(c) supply only the **identification** "a record reads out its central-sector scalar; disjoint blocks = disjoint records"; with Record-additivity this gives `W(Z₁Z₂)=W(Z₁)+W(Z₂)` on `R_{>0}` ⇒ Cauchy ⇒ **`W = c log det`** (`c=1`; Cauchy residual `8.88e-16`). |
| **R5 — P-REC single-taste pointer** | **(b)** | per-site `γ₅` is impossible (`ω = σ₁σ₂σ₃ = iI` central in `M₂(C)`; exhaustive search finds **no** on-site anticommutant of the Pauli triple) ⇒ the taste/chirality pointer **must** be the measurement **pointer basis** = clause (b)'s central decomposition ("one outcome per irreducible Dirac/taste factor"). |
| **Koide OBJECTIVITY-BASIS** (the alphabet) | **(b)+(c)** | clauses (b)+(c) fix the pointer **alphabet** = the **two** `K`-real outcomes (singlet \| doublet). SBS broadcast (clause c) gives full redundant objectivity (plateau `= H(weights)`) over those two outcomes — establishing them as the **objective** alphabet = **#blocks = 2** (the "two terms" in the capacity lever `r* = w_p/(2 w_s)`), **not** the weight ratio. |

**Leg B verdict (runner PASS): the single unified axiom derives the basis /
identification half of C2** — T1-d det-readout + P-REC pointer + Koide
objectivity-BASIS. This half of C2 collapses into MEAS-REC-READOUT.

> **CRITICAL — this is the BASIS only.** The equal-block `(1,1)` sector-measure
> **weight** is **not** supplied by clauses (b)+(c) (or by (a)); it is the
> load-bearing residual of §4.1.

---

## 4. WHAT DOES NOT COLLAPSE — the residual data primitives

The honest core of the unification. There are **two** independent residuals, both
recomputed as real walls.

### 4.1 The equal-block `(1,1)` sector-MEASURE WEIGHT (C2-WEIGHT)

Per the **KEY PRIOR FINDING** (koide block02 R2/R3;
`FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02` N6/N7;
`KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31` route R3): **SBS /
quantum-Darwinism objectivity is WEIGHT-BLIND.** It fixes the pointer **basis**,
not the sector **weight**. The unified axiom's clause (c) is exactly an SBS /
broadcast clause — so it supplies the objective **alphabet** (2 outcomes) but
**not** the equal-block `(1,1)` weight `t = w_p/w_s = 1` that pins Koide
`r = 1/2`, `Q = 2/3`. Two independent runner legs make this **decisive**:

- **R2 weight-blindness (runner PART [3]).** The SBS objectivity plateau equals
  `H(weights)` for **both** `(1/2,1/2)` (`1.000` bit) and `(1/3,2/3)` (`0.918`
  bit). Objectivity is *present for every weight*; clause (c) **reports** the
  supplied weights, it does not **select** them. The capacity maximizer
  `r* = w_p/(2 w_s)` is a **continuous function of the free ratio `t`** (the
  pointer alphabet fixes #blocks = 2, never `t`).
- **R3 countermodel (runner PART [3]).** The clause-(a) **dynamics** does **not**
  pin the weight *either*: the einselection **fixed point** in the pointer basis is
  the maximally mixed `I/3`, which through the (rank-1, rank-2) split gives the
  **rank** weights `(1/3, 2/3)` ⇒ `r = 1` (`t = 2`), **not** `r = 1/2`. So the
  dynamics horn lands at the *wrong* value for Koide.

**Decisive conclusion.** *Neither* clause (a) (dynamics → `t=2`) *nor* clause (c)
(objectivity → weight-blind) supplies the equal-block `t=1`. The `(1,1)` weight is
a **separate max-entropy / indifference datum** the unified measurement axiom
**omits** — the *indifference / maximum-objective-information over LABELS* rule
(uniform `= 1` bit `> H(rank)`), which `FLAVOR_QD` N7 names as a "coherent possible
additional principle" *outside* QD-objectivity, and which Record verbatim declines
("weighting … or occupancy rule";  `MINIMAL_AXIOMS_2026-06-05.md`). So the
equal-block measure is a **separate science-level decision** — the **C2-WEIGHT**
residual — not subsumed by MEAS-REC-READOUT and not by Record. One dimensionless
binary choice, same category as the approved `kinetic_isotropy_primitive`
(structural, dimensionless, binary, no fitted number).

### 4.2 The N2b time-edge SPACING primitive `a_tau/a_s` (SPACING)

Independently, the dimensionful **time-edge spacing** is not supplied. The
measurement rate `γ` (clause a) gives the *existence* of a step (a half-life in
dynamics ticks), **not** the metric edge `a_tau`. The Lattice axiom verbatim
disavows "metric scale, lattice spacing"; block02 **SK-1** (the
`scale_reference × kinetic_isotropy` join) and block03 **NODIAG** (the no-diagonal
adjacency clause) both **walled**. The runner recomputes the metric-blindness
directly: the 6-NN edge set is **identical** for `a_tau/a_s = 1, 10, 0.137` (the
adjacency predicate `|dx|+|dy|+|dz| = 1` carries no `a_tau, a_s`). So `a_tau/a_s`
remains a **separate minimal spacing primitive** (one dimensionless ratio),
strictly weaker than the unified axiom and disjoint from its dynamics content.

---

## 5. Minimality — STRICTLY WEAKER than C1+C2, and POLICY-PREFERRED

### 5.1 Strictly weaker (consequence-set + model-count; runner `…minimality…` PART [0])

**Measure used: the consequence set (logical content).** An axiom `P` is logically
weaker than `Q` iff `Cons(P) ⊆ Cons(Q)`, and *strictly* weaker iff
`Cons(P) ⊊ Cons(Q)` — equivalently, the weaker axiom **constrains less** and so
admits **more models**. The runner encodes each axiom by the set of atomic
load-bearing consequences it entails (the 10 distinct, separately-checkable claims
drawn verbatim from the two block01 notes):

```text
Cons(U)        = {arrow, N5, N4, N2b-step, floor, pointer_basis,
                  objective_alphabet, det_readout_id, prec_pointer}     (9 atoms)
Cons(C1-sep)   = {arrow, N5, N4, N2b-step, floor}                       (5)
Cons(C2-sep)   = {pointer_basis, objective_alphabet, det_readout_id,
                  prec_pointer, equal_block_weight}                     (5)
Cons(C1 ∧ C2)  = Cons(C1-sep) ∪ Cons(C2-sep)                            (10 atoms)
```

The runner verifies:

- **`Cons(U) ⊆ Cons(C1 ∧ C2)`** — U entails **no** consequence the two separate
  axioms lack (no over-reach).
- **`Cons(U) ⊊ Cons(C1 ∧ C2)`** — the two-axiom conjunction entails **strictly
  more**; the single witnessing extra atom is **`equal_block_weight`**, which U
  provably does **not** entail (it is weight-blind, §4.1). So U is **strictly
  weaker by consequence-set content**, and the exact difference is isolated to the
  one residual `C2-WEIGHT`.
- **Model-count corroboration:** U fixes 9 atoms vs the two-axiom 10, admitting
  `2¹ ≥ 2⁰` models (weaker = constrains less = more models).
- **The converse FAILS:** `Cons(C1 ∧ C2) ⊄ Cons(U)` because
  `U ⊬ equal_block_weight`. So U is **strictly weaker, not equivalent**.

*Physics:* C1+C2-separate are **two independent existential posits**; U is **one**
existential whose single witness `(L, pointer basis, broadcast structure)` yields
both the dynamics/arrow and the pointer-basis/objectivity content **as consequences
of the same object** — carrying strictly fewer consequences because the unified
interaction does not carry the independent weight atom.

### 5.2 Preferred by `AXIOM_MINIMALITY_POLICY.md` on all four criteria (PART [4])

| Policy criterion (source) | Verdict for U | Evidence |
|---|---|---|
| **Weakest sufficient** (policy's stated target) | **U is weakest** for gates 1+2 | PART [0] strict-subset: U entails the dynamics+basis content and **nothing more**; dropping any clause loses a discharge, strengthening it over-reaches and would clash with weight-blindness. |
| **Non-redundant** (§2 "bounded compositions with explicit named residuals") | **non-redundant** | PART [1] countermodels: U does **not** subsume W or S, so `{U, W, S}` is a non-redundant generating set with the two residuals **explicitly named** — exactly the §2 shape. |
| **Independent** (policy intent) | **independent** | PART [1] mutual-independence countermodels (§6) + PART [3] C3 categorical separation. |
| **No laundering** (§1 final bullet; §6 test; precedent `kinetic_isotropy_primitive`) | **no laundering** | U adds content the `MINIMAL_AXIOMS_2026-06-05.md` memo declares **outside** axiom content (gates 1+2), recorded as an **unmade science-level decision** (§1/§4); it does **not** reword Lattice/Quantum/Record (§1 disallowed) and edits no registry. Record verbatim declines "measurement/decoherence dynamics … weighting … or occupancy rule"; U supplies the dynamics+basis as a *separate* recorded decision, never folded into Record. |

**Decisive policy point.** The unification is precisely the move the policy
**rewards**: block01 `{C1, C2}` (two weak axioms, two gates) → **one** weak–medium
axiom **U** (one act spanning both gates) **plus its two explicitly-named
residuals** it provably cannot supply. Fewer independent axioms, each weaker or
equal, all residuals named. The §3/§6 precedent (`kinetic_isotropy` admitted as a
*structural, dimensionless, binary, no-fitted-number* primitive) is the template
for the two residual data `W` and `S`; the route is §6 owner approval, not in-lane
adoption.

---

## 6. Independence by countermodel — `{U, W, S}` mutually independent (PART [1]–[2])

**Method.** For each primitive `P ∈ {U, W, S}`, exhibit a model on the `A_min`
surface that satisfies `A_min` + **the other two** but **violates** `P`. A
countermodel proves `P` is **not** derivable from `A_min` + the others.

- **U independent of `{A_min, W, S}`.** The record-formation `H = 0` no-record
  baseline is `A_min`-consistent and supplies **no** record floor (`|coh|` frozen
  at `0.5` for `#env = 1,2,4,16,64`) for **any** weight and **any** spacing — a
  static weight/spacing datum sources **no** CPTP einselecting generator. So
  `{A_min, W, S} ⊬ U`.
- **W independent of `{A_min, U, S}`** — the load-bearing reuse of koide
  weight-blindness. With the **full** measurement axiom U in force, the weight `t`
  is **still free**, by two countermodels: **(i)** objectivity is weight-blind
  (plateau `= H(weights)` positive for both `t=1`, `H=1.000` bit, and `t=2`,
  `H=0.918` bit); **(ii)** the einselection fixed point `I/3` through the
  (rank-1, rank-2) split gives `(1/3, 2/3)` ⇒ `r=1` ⇒ `t=2`, not the equal-block
  `t=1` (koide R3 `W_t`). So `{U on, S any, weight = rank face t=2}` satisfies
  `A_min + U + S` and violates W ⇒ `{A_min, U, S} ⊬ W`: **the measurement dynamics
  does NOT fix the equal-block weight**.
- **S independent of `{A_min, U, W}`.** The adjacency predicate
  `|dx|+|dy|+|dz| = 1` is metric-blind (6-NN edge set identical for
  `a_tau/a_s = 1, 10, 0.137`); the rate `γ` fixes a half-life in **dynamics
  ticks**, not the metric edge `a_tau`. So `{A_min, U, W} ⊬ S`.

**Orthogonal dials confirmed (PART [2]).** Vary the **weight** dial
`t ∈ {1/2, 1, 2, 7/3}` → the **spacing** witness is unchanged; vary the **spacing**
dial `a_tau/a_s ∈ {1, 10, 0.137, 3.3}` → the **weight** witness `Koide r*=0.5` at
`t=1` is unchanged; vary **both** → the **measurement** witnesses (arrow monotone,
floor `→0`, alphabet `=2`) are unchanged. **Each observable depends on exactly one
primitive's datum and is blind to the other two: clean residual isolation, no
cross-leakage.**

---

## 7. C3 does NOT fold — gauge content is categorically separate (PART [3])

**Expected and confirmed: NO.** Gauge group / particle content is a **different
KIND of datum** — a *choice of gauge group + chiral matter representations* — from a
*measurement-interaction existence* datum. The runner tests categorical
distinctness **both ways**:

- **(i) the MEASUREMENT structure is blind to the gauge content.** The
  einselection / arrow / floor witnesses are computed from the dephasing dynamics +
  the central decomposition **only**; they do **not** read the chirality grading
  `E` or any anomaly trace. The four published gauging-selection discriminators
  stay blind regardless of any measurement (e.g. the chirality grading **commutes**
  with the color generators, `‖[E, λ₃]‖ = ‖[E, λ₈]‖ = 0`): adding U changes **none**
  of them — the gauging gate stays open under U.
- **(ii) the GAUGE content is blind to the measurement act.** The LH
  one-generation anomaly traces are **fixed rationals** (`Tr[Y³] = -16/9`,
  `Tr[SU3²Y] = +1/3`, `SU3³ = +2`) computed with **no** measurement object; the
  **chirality** of the completion (the load-bearing P-COMP word) is a pure content
  fact — the SM chiral RH template `(4/3, -2/3, -2, 0)` cancels all six **and** is
  genuinely chiral (not vector-like), decided with **no** pointer basis /
  einselection / objectivity.

**Decisive.** Neither's witnesses move the other's. A single "operational
measurement" axiom **cannot entail a choice of gauge representations**, and the
gauge content **cannot entail a measurement interaction**. They live in **different
gates** (gates 1/2 vs gate 3). Folding C3 into U would be a **category error** and
**policy-laundering**. So **PIN-GAUGE-CONTENT stays a separate gate-3 candidate** —
the unification touches only gates 1+2.

> **Runner caught a real bug (load-bearing-residual pattern held).** The minimality
> runner's first draft hand-coded the `[SU(3)]²U(1)_Y` LH anomaly trace with a
> spurious extra factor of `n_color` (double-counting color on top of the
> `T(fund)=1/2` trace normalization), returning `Tr[SU3²Y]=1` instead of the banked
> `+1/3`. The `[FOLD] (ii)` leg **FAILed** and exposed it; fixed by dropping the
> extra `nc`, after which all three banked LH traces reproduce exactly
> (`Tr[Y³]=-16/9`, `Tr[SU3²Y]=+1/3`, `SU3³=+2`).

---

## 8. THE FINAL MINIMAL PROPOSAL SET (all UNADOPTED)

After unification, minimality, and residual isolation, the minimal axiom-update
proposal set (`hypothetical_axiom_status` throughout) is:

1. **U = MEAS-REC-READOUT** — the unified operational measurement-with-readout
   axiom. One existence slot for the realized state supplying *at once* the
   einselecting CPTP dynamics + orientation (= C1's arrow / N4 registration
   direction / N5 single clock / N2b-step / record floor) **and** the pointer basis
   = central/`K`-CPT decomposition + SBS objectivity-**basis** (= C2's T1-d
   det-readout identification + P-REC pointer + Koide objectivity-basis / 2-outcome
   alphabet). **Strictly weaker** than C1+C2 stated separately; **weakest
   sufficient** for gates 1+2; existence/slot only (no kernel/rate, no weight, no
   probability, no spacing, no arrow *sign*); weaker than a past hypothesis.
   *Strength: weak–medium.*
2. **W = C2-WEIGHT** — the equal-block `(1,1)` sector-measure weight `t=1` (the
   indifference / max-objective-information-over-labels datum that pins Koide
   `r=1/2`, `Q=2/3`). A single dimensionless binary choice; **independent** of U
   (objectivity weight-blind; the dynamics horn gives `t=2`). *Strength: weak; same
   category as `kinetic_isotropy_primitive`.*
3. **S = SPACING** — one dimensionless time-edge spacing `a_tau/a_s`.
   **Independent** of U and W (metric-blind adjacency; orthogonal dial).
   *Strength: weak; one dimensionless ratio.*
4. **G = PIN-GAUGE-CONTENT (C3)** — gauge group + opposite-chirality RH SU(2)-singlet
   template. **Categorically separate** (gate 3); does **not** fold (§7).
   *Strength: heavy; unchanged from block01.*

> **Residual-isolation, in one line:** the *measurement interaction* is one weak
> existence axiom (U); the *sector weight* (W) and the *metric spacing* (S) are two
> separate dimensionless data, each one datum, mutually independent and orthogonal;
> the *gauge content* (C3) is a categorically different content choice that does
> not fold.

---

## 9. Coverage comparison vs the 3-axiom (block01) version

| | block01 set `{C1, C2, C3}` | block04 set `{U, W, S, C3}` |
|---|---|---|
| **# axioms** | 3 | 4 *(but U is one act folding two; the two extra entries W, S are tiny dimensionless DATA, each isolated as the weakest separate datum, not a second/third operational axiom)* |
| **# OPERATIONAL axioms** | 2 (C1 dynamics + C2 readout) | **1** (U) |
| **C1's discharge set** (arrow / N4 / N5 / N2b-step / floor) | C1 | **U** (full) |
| **C2 basis half** (T1-d det-readout id; P-REC pointer; Koide objectivity-basis / 2-outcome alphabet) | C2 | **U** (full) |
| **C2 weight half** (equal-block `t=1` → Koide `r=1/2`) | C2 (folded **into** C2, conflated with the basis) | **W** (ISOLATED as its own datum — the honest split required by weight-blindness) |
| **N2b spacing** `a_tau/a_s` | implicit residual under C1-N2b (block02/03 walled) | **S** (ISOLATED as its own datum) |
| **C3 gauge content** | C3 | C3 (unchanged; does not fold) |
| **logical strength of the operational core** | C1 ∧ C2 | **U, strictly weaker** (`Cons(U) ⊊ Cons(C1∧C2)`; missing atom = equal-block weight) |
| **policy fit** | two weak axioms in two gates | weakest-sufficient / non-redundant / independent / no-laundering on all four criteria |

**Same coverage, sharper structure.** The block04 set discharges the **identical**
set of walls as the block01 `{C1, C2}` pair (C1's full set + C2's basis half +
C2's weight via the isolated W), with **no loss of coverage** and **no
over-reach**. The difference is purely structural and is the improvement the policy
asks for:

- the two block01 operational axioms become **one strictly-weaker** operational
  axiom (U), and
- the two things that axiom provably **cannot** supply — which block01's C2
  silently bundled into the readout-measure axiom (the equal-block weight) and which
  block01's C1 left as an implicit N2b residual (the spacing) — are **named and
  isolated** as the weakest separate dimensionless data (W, S), exactly the §2
  "bounded composition with explicit named residuals" shape.

**Which the owner should prefer.** The block04 set is the more honest and more
minimal presentation of the *same* physics: it does not over-claim (it does not let
the measurement act smuggle in the weight or the spacing, which it provably cannot
give), and it minimizes the **operational** axiom count to one. If the owner's goal
is the weakest-sufficient / non-redundant / independent / no-laundering target the
policy states, **the block04 `{U, W, S, C3}` set should be preferred over the
block01 `{C1, C2, C3}` set.** (C3 is identical in both; the comparison is entirely
about the C1+C2 → U+W+S refactor.) Adoption of any member remains an unmade
science-level decision for the owner / audit lane.

---

## 10. Falsifiers (what would defeat the unification / minimality)

- A no-new-axiom derivation of record-producing dynamics **or** of the pointer
  basis from Lattice+Quantum+Record would moot the corresponding clause of U.
- A demonstration that SBS/quantum-Darwinism objectivity **does** fix the sector
  weight (refuting R2 weight-blindness, or the R3 einselection horn shown to give
  `t=1` not `t=2`) would **fold the C2-WEIGHT residual back in** — making the
  unification *fuller* than partial and shrinking the set to `{U, S, C3}`. (The
  runner exhibits the opposite: weight-blind; dynamics horn at `t=2`.)
- A demonstration that the measurement act *necessarily* fixes a metric spacing
  (refuting block02 SK-1 + block03 NODIAG) would fold the SPACING residual in.
- A model where the consequence sets are **not** strictly nested (U shown to entail
  a consequence outside `Cons(C1 ∧ C2)`, or C2-sep shown not to carry the weight
  atom) would break the §5.1 strict-weaker comparison.
- A measurement-structure observable shown to move under a gauge-content change (or
  vice versa) would break the §7 categorical distinctness and reopen the C3 fold.
- A consumer needing the axis *label* (not just the count `d_t`) or a sharpened
  charged-lepton `Q` materially off `2/3` would, respectively, re-weight the C1
  fanout inside U or disfavor the equal-block `W` — neither defeats the
  *unification* of the basis content.

---

## 11. Consistency with retained results (the governance check)

- No retained no_go in scope asserts the discharged target is **impossible** or
  **symmetry-forbidden** — each asserts only **not forced from the current
  surface**. U supplies the imports those boundaries name (PIN-REG; the readout
  context; the objective alphabet) and **respects weight-blindness** (it does not
  claim objectivity forces the weight, so it does not collide with
  `FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02`).
- U does **not** reword Lattice / Quantum / Record (policy §1) — it adds content the
  `MINIMAL_AXIOMS_2026-06-05.md` memo declares **outside** axiom content, recorded
  as an unmade science-level decision (§1/§4), with approval routed through §6
  exactly as `kinetic_isotropy_primitive` was.
- Nothing is written to `docs/audit/data/` (read-only this lane); no
  `axiom_premise_nodes.json` entry is added; no audit verdict is set.

---

## 12. Status (audit-lane handoff)

```yaml
proposed_artifact_type: axiom minimization / unification synthesis (sufficiency + minimality + residual-isolation)
proposal_allowed: false        # owner governance decision required; this note REQUESTS it
adopts_axiom: false
sets_audit_verdict: false
edits_axiom_premise_nodes: false
status_authority: independent audit lane / owner only
hypothetical_axiom_status: "conditional on accepted new axiom; not retained on the actual current surface"
unified_axiom_id: MEAS-REC-READOUT
collapse_verdict: partial_collapse
collapses:
  - C1 full set (B-AXIS N4 registration-direction + N5 single-clock + arrow + N2b-step + record-formation floor)
  - C2 basis/identification half (observable T1-d det-readout + P-REC pointer + Koide objectivity-BASIS / 2-outcome alphabet)
does_not_collapse:
  - C2-WEIGHT: equal-block (1,1) sector-MEASURE weight t=1 (objectivity WEIGHT-BLIND per R2; dynamics horn gives t=2 per R3) -> separate max-entropy/indifference datum
  - SPACING: N2b time-edge spacing a_tau/a_s (Lattice disavows spacing; SK-1 + NODIAG walled) -> separate minimal spacing primitive
strictly_weaker_than_C1_plus_C2: true
strictly_weaker_measure: "consequence set + model count: Cons(U) STRICT subset of Cons(C1-sep AND C2-sep); single extra atom = equal-block weight; U admits strictly more models; converse fails"
policy_prefers_unified: true
policy_criteria_met: [weakest_sufficient, non_redundant, independent, no_laundering]
independence_check: "{U, W, S} mutually independent by countermodel; W and S orthogonal dials; none derivable from A_min + the others"
c3_folds: "no"
final_minimal_set: [MEAS-REC-READOUT, C2-WEIGHT, SPACING, PIN-GAUGE-CONTENT]
runners:
  - {path: scripts/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.py, total: "PASS=39 FAIL=0"}
  - {path: scripts/axiom_update_unified_axiom_minimality_independence_2026_06_21.py, total: "PASS=28 FAIL=0"}
aggregate_runner_total: "PASS=67 FAIL=0 (39 + 28); deterministic; -W error clean; numpy + stdlib only; no empirical import"
```

**Not in scope.** Adopting any candidate; deriving any kernel/rate/weight/value;
deriving the arrow's sign (past hypothesis), Born weights, the equal-block weight,
the dimensionful tick `2a_tau` / `a_tau/a_s`, `n_color`, generation count, or any
coupling/mass/mixing; folding C3; editing `docs/audit/data/` or any axiom file;
setting any audit verdict.

---

## 13. Load-bearing sources

- **block01 cluster proposals (the candidates folded / tested):**
  `docs/AXIOM_UPDATE_PROPOSAL_RECORD_PRODUCTION_DYNAMICS_2026-06-20.md` (C1),
  `docs/AXIOM_UPDATE_PROPOSAL_READOUT_CONTEXT_OBJECTIVITY_2026-06-20.md` (C2),
  `docs/AXIOM_UPDATE_PROPOSAL_GAUGE_CONTENT_2026-06-20.md` (C3).
- **consolidated set + block02/03 resolutions:**
  `docs/AXIOM_UPDATE_PROPOSALS_CONSOLIDATED_2026-06-20.md`,
  `docs/AXIOM_PROPOSALS_OPEN_CRACKS_RESOLUTION_NOTE_2026-06-20.md`.
- **weight-blindness (the KEY PRIOR FINDING / W-independence countermodel):**
  `docs/FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md` (N6/N7),
  `docs/KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md` (R3 countermodel `W_t`).
- **spacing residual (S-independence countermodel):**
  `.claude/science/physics-loops/axiom-update-proposals/block03_section_NODIAG.md`,
  `.claude/science/physics-loops/axiom-update-proposals/block02_section_SK1.md`.
- **section legs (this synthesis consolidates):**
  `.claude/science/physics-loops/axiom-update-proposals/block04_section_SUFFICIENCY.md`,
  `.claude/science/physics-loops/axiom-update-proposals/block04_section_MINIMALITY.md`.
- **surface / policy:** `docs/MINIMAL_AXIOMS_2026-06-05.md` (Record/Lattice
  non-supply; open gates list), `docs/audit/AXIOM_MINIMALITY_POLICY.md`
  (§1 disallowed/no-laundering; §2 bounded composition with named residuals;
  §3/§6 admissibility precedent `kinetic_isotropy_primitive`; §4 unmade-decision
  workflow; §6 owner approval).
- **runners + caches:**
  `scripts/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.py`,
  `scripts/axiom_update_unified_axiom_minimality_independence_2026_06_21.py`
  (+ matching `.txt` caches under `logs/runner-cache/`); both reuse the block01
  cluster runners
  `scripts/axiom_update_record_production_dynamics_cluster_2026_06_20.py` and
  `scripts/axiom_update_proposal_readout_context_objectivity_runner_2026_06_20.py`.
