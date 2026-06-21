# block04 — Section: SUFFICIENCY — does ONE measurement-with-readout axiom subsume BOTH C1 (dynamics/arrow) AND C2 (readout-context/objectivity-basis)?

**Date:** 2026-06-21
**Lane / branch:** `axiom-update-proposals`,
`physics-loop/axiom-update-proposals-block04-20260620`.
**Type:** AXIOM MINIMIZATION / UNIFICATION analysis (sufficiency + derivation leg).
**Claim type:** proposal (meta / governance) — adopts nothing.
**Status authority:** independent audit lane / owner **only**. This section sets
no audit verdict, promotes no axiom, edits no axiom registry, and writes nothing
to `docs/audit/data/` (read-only this lane).

> **`hypothetical_axiom_status` (carried throughout):** *"conditional on accepted
> new axiom; not retained on the actual current surface."* Every "derives" /
> "discharges" claim below is a consequence of an **UNADOPTED** candidate
> primitive. Labeling a consequence "conditional" does **not** promote it; only
> an external owner / governance decision can
> (`docs/audit/AXIOM_MINIMALITY_POLICY.md` §1/§4/§6). No bare `retained` /
> `promoted` appears anywhere in this section.

**Primary runner:**
`scripts/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.py`
**Cached output:**
`logs/runner-cache/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.txt`
(**TOTAL: PASS=39 FAIL=0**, deterministic — re-run identical; clean under
`python3 -W error`; numpy + stdlib only; no empirical import; no RNG draw is
load-bearing).

---

## 0. The minimization question (what this optimizes)

`AXIOM_MINIMALITY_POLICY.md` targets the **weakest sufficient, non-redundant,
independent** extension. Block01 delivered three candidate additions; block02/03
confirmed the C1-N2b and C3-P-ABJ residuals genuinely wall. The remaining
minimization move not yet tested is **unification**: block01's C1 (RP-DYN —
dynamics + arrow) and C2 (READOUT-MEASURE — readout-context / objectivity /
sector-measure) sit in two *different* open gates, but they are arguably two
faces of **one physical act** — a system–environment **measurement interaction
that produces durable records with a readout**. If a single such axiom subsumes
both discharge sets, the candidate **count** drops (2 weak axioms → 1), which is
exactly the minimization the policy rewards.

This section (i) **precisely states** the candidate single axiom; (ii) **tests
sufficiency** with a runner — does it derive *both* C1's and C2's discharge sets;
(iii) **identifies what does NOT collapse**, which — per the load-bearing koide
block02 R2/R3 weight-blindness finding — is the **equal-block (1,1) sector-MEASURE
weight**, plus the **N2b spacing primitive `a_tau/a_s`**.

The two candidate gates are genuinely distinct on the current surface (runner
PART [0]): C1's gate is *arrow/measurement/decoherence/record-production
dynamics*; C2's gate is *readout context/sector measure/objectivity/occupancy*
(`MINIMAL_AXIOMS_2026-06-05.md`). And the unification is non-trivial precisely
because **neither gate's content is derivable from the other** on the current
surface (the R3 countermodel, §3, shows the dynamics does **not** pin the
measure). So folding both into one axiom is a real reduction of axiom count, not
a reword of an existing axiom (which policy §1 forbids).

---

## 1. The candidate UNIFIED axiom (precise statement, UNADOPTED)

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
>   decomposition — i.e. the **alphabet of distinguishable record outcomes** (one
>   slot per irreducible `K`/CPT orbit / irreducible Dirac–record factor). *(= C2's
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

This is strictly the **weakest** single statement that could span both gates:
weaken any clause and one of the two discharge sets fails (drop (a) → no
arrow/N4/N5; drop (b) → no pointer alphabet/no T1-d identification target; drop
(c) → no *objective* alphabet). Strengthen it with a weight/probability/kernel
and it over-reaches (and would clash with the weight-blindness finding, §3).

The runner reuses the **exact** load-bearing legs of the two block01 cluster
runners — same staggered `W`-exchange surface, same chirality grading, same
controlled-broadcast dephasing/einselection, same Koide capacity lever
`r* = w_p/(2 w_s)`, same SBS plateau `= H(weights)`, same `I/3` fixed point, same
2:1 occupancy fiber — so the unification is a genuine fold of the *same* objects,
not a fresh toy that merely happens to pass.

---

## 2. Sufficiency leg A — (MEAS-REC-READOUT) derives **C1's full discharge set**

All lines `hypothetical_axiom_status: conditional`. Runner PART [1]; the surface
is the periodic staggered Kogut–Susskind hop, recomputed exactly `W`-invariant
(`||W M W^T − M|| = 0.0`) so the axis-label wall is genuine here.

| C1 wall | Discharged by clause | Conditional derivation (runner witness) |
|---|---|---|
| **arrow** (existence as a direction) | **(a)** | the einselecting dynamics' orientation **is** the record-monotone direction; record proxy `[0.0, 0.0, …]→[1.0,…]` rises monotonically as `|coh|` falls; a unitary step has no monotone. |
| **B-AXIS N5** (single clock) | **(a)** | **one** generator ⇒ one monotone record order even across two factors with *distinct* rates (joint `|coh|/0.5` monotone) ⇒ a single production clock. |
| **B-AXIS N4** (registration direction) | **(a)** | the orientation **is** the registration direction (PIN-REG); the realized antiperiodic-`τ`/periodic-space datum breaks the exchange **exactly** (`||W M_ap W^T − M_ap|| = 8.0 > 0`); **falsification leg**: symmetric BCs **restore** `W` (residual `0.0`), so the selecting content is the per-axis registration *asymmetry*. |
| **B-AXIS N2b-step** (a step exists) | **(a)** | the generator carries a rate `γ` ⇒ a well-defined record half-life (the *dynamics-side* existence of a tick; **not** the dimensionful value — see §4). |
| **record-formation floor** | **(a)+(c)** | `|coh|(N=1,2,4,16,64) → 0` monotonically as #env copies grows ⇒ a durable, redundantly-broadcast record (einselection / quantum Darwinism). |

**Leg A verdict (runner [1], [6] part 1): the SINGLE unified axiom derives all of
C1 — N4 + N5 + arrow + N2b-step + floor.** C1 collapses into MEAS-REC-READOUT;
no separate dynamics axiom is needed beyond it.

---

## 3. Sufficiency leg B — (MEAS-REC-READOUT) derives **C2's basis / identification half**

All lines `hypothetical_axiom_status: conditional`. Runner PART [2]. This leg
delivers the **observable T1-d det-readout pointer**, the **P-REC pointer**, and
the **objectivity-BASIS part of Koide** — i.e. exactly the part of C2 that is a
*pointer-basis / readout-context / objective-alphabet* fact. (The *weight* part is
the residual; see §4.)

| C2 wall | Discharged by clause | Conditional derivation (runner witness) |
|---|---|---|
| **R4 — observable T1-d det-readout identification** | **(b)+(c)** | the det **FORM** is already a no-new-axiom theorem (SKb: `det` is a multiplicative character, `tr` is not). Clauses (b)+(c) supply only the **identification** "a record reads out its central-sector scalar; disjoint blocks = disjoint records"; with Record-additivity this gives `W(Z₁Z₂)=W(Z₁)+W(Z₂)` on `R_{>0}` ⇒ Cauchy ⇒ **`W = c log det`** (`c=1`; Cauchy residual `8.9e-16`). |
| **R5 — P-REC single-taste pointer** | **(b)** | per-site `γ₅` is impossible (`ω = σ₁σ₂σ₃ = iI` central in `M₂(C)`; exhaustive search finds **no** on-site anticommutant of the Pauli triple) ⇒ the taste/chirality pointer **must** be the measurement **pointer basis** = clause (b)'s central decomposition ("one outcome per irreducible Dirac/taste factor"). |
| **Koide OBJECTIVITY-BASIS** (the alphabet) | **(b)+(c)** | clauses (b)+(c) fix the pointer **alphabet** = the **two** `K`-real outcomes (singlet \| doublet). SBS broadcast (clause c) gives full redundant objectivity (plateau `= H(weights)`) over those two outcomes — establishing them as the **objective** alphabet. This is the **#blocks = 2** that the capacity lever uses (the "two terms"), **not** the weight ratio. |

**Leg B verdict (runner [2], [6] part 2): the SINGLE unified axiom derives the
basis / identification half of C2 — T1-d det-readout + P-REC pointer + Koide
objectivity-BASIS.** This half of C2 collapses into MEAS-REC-READOUT.

---

## 4. WHAT DOES NOT COLLAPSE — the residual the unified axiom does **not** supply

This is the load-bearing finding of the section. There are **two** independent
residuals, both recomputed as real walls in the runner.

### 4.1 The equal-block `(1,1)` sector-MEASURE WEIGHT (the C2-WEIGHT residual)

Per **koide block02 R2/R3** (
`FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02`, N6/N7;
`KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31` route R3): **SBS /
quantum-Darwinism objectivity is WEIGHT-BLIND.** It fixes the pointer **basis**,
not the sector **weight**. The unified axiom's clause (c) is exactly an SBS /
broadcast clause — so it supplies the objective **alphabet** (2 outcomes) but
**not** the equal-block `(1,1)` **weight** `t = w_p/w_s = 1` that pins Koide
`r = 1/2`, `Q = 2/3`. Two independent runner legs make this decisive:

- **R2 weight-blindness (runner [3]).** The SBS objectivity plateau equals
  `H(weights)` for **both** `(1/2,1/2)` (`1.000` bit) and `(1/3,2/3)` (`0.918`
  bit). Objectivity is *present for every weight*; clause (c) **reports** the
  supplied weights, it does not **select** them. The capacity maximizer
  `r* = w_p/(2 w_s)` is a **continuous function of the free ratio `t`** (runner
  reproduces `(1,0)→Q=1/3`, `(1,1)→Q=2/3`, `(1,2)→Q=1`, `(2,1)→Q=1/2`); the
  pointer alphabet fixes **#blocks = 2**, never `t`.
- **R3 countermodel (runner [3]).** The clause-(a) **dynamics** does **not** pin
  the weight *either*: the einselection **fixed point** in the pointer basis is
  the maximally mixed `I/3`, which through the (rank-1, rank-2) split gives the
  **rank** weights `(1/3,2/3)` ⇒ `r = 1` (`t = 2`), **not** `r = 1/2`. So the
  dynamics horn lands at the *wrong* value for Koide.

**Decisive conclusion (runner [3]).** *Neither* clause (a) (dynamics → `t=2`)
*nor* clause (c) (objectivity → weight-blind) supplies the equal-block `t=1`. The
`(1,1)` weight is a **separate max-entropy / indifference datum** the unified
measurement axiom **omits**: the *indifference / maximum-objective-information
over LABELS* rule (uniform `= 1` bit `> H(rank)`), which `FLAVOR_QD` N7 names as a
"coherent possible additional principle" *outside* QD-objectivity. Record's
verbatim non-supply clause ("weighting … or occupancy rule";
`MINIMAL_AXIOMS_2026-06-05.md`) puts the same datum outside Record. So the
equal-block measure is a **third, separate science-level decision** — call it the
**C2-WEIGHT residual** — not subsumed by MEAS-REC-READOUT and not by Record.

This is the honest core: the unification is **partial**. The measurement act
plausibly supplies *dynamics + pointer-basis + objectivity-basis*, but **not** the
sector weight, exactly as the prior finding requires.

### 4.2 The N2b spacing primitive `a_tau/a_s` (the C1-N2b metric residual)

Independently, the dimensionful **time-edge spacing** is not supplied. The
measurement rate `γ` (clause a) gives the *existence* of a step (a half-life in
dynamics ticks), **not** the metric edge `a_tau`. The Lattice axiom verbatim
disavows "metric scale, lattice spacing"; block02 **SK-1** (the
`scale_reference × kinetic_isotropy` join) and block03 **NODIAG** (the
no-diagonal adjacency clause) both **walled**. The runner [4] recomputes the
metric-blindness directly: the 6-NN edge set is **identical** for
`a_tau/a_s = 1, 10, 0.137` (the adjacency predicate `|dx|+|dy|+|dz| = 1` carries
no `a_tau, a_s`). So `a_tau/a_s` remains a **separate minimal spacing primitive**
(one dimensionless ratio), strictly weaker than the unified axiom and disjoint
from its dynamics content.

---

## 5. Sufficiency verdict and minimality bookkeeping

**Verdict: PARTIAL COLLAPSE.** (Runner [6]; PASS=39 FAIL=0.)

- **Collapses into the one unified axiom:** C1's full set (N4 + N5 + arrow +
  N2b-step + floor) **and** C2's basis/identification half (T1-d det-readout +
  P-REC pointer + Koide objectivity-basis). Two weak candidate gates → **one**
  measurement-with-readout primitive.
- **Does NOT collapse (independent residuals):** the **equal-block `(1,1)`
  sector-MEASURE weight** (`t=1`; the C2-WEIGHT residual — a separate
  max-entropy/indifference datum, because objectivity is weight-blind and the
  dynamics horn gives `t=2`); and the **N2b spacing primitive `a_tau/a_s`** (a
  separate metric datum).

**Minimality of the unification (runner [5]).** The unified axiom (i) **reduces
axiom count** (2 gates → 1); (ii) is **non-redundant** — it does *not* subsume
the two residuals, so it is the weakest sufficient *single* axiom for the
dynamics + pointer-basis + objectivity-basis content and **no more**; (iii) is an
**existence/slot** statement (no kernel/rate, no weight, no probability, no
spacing, no arrow sign), consistent with `realized_state_primitive` and **weaker
than a past hypothesis**; (iv) **contradicts no retained no-go** — it *supplies*
the imports those boundaries name (PIN-REG; the readout context; the objective
alphabet) and **respects weight-blindness** (it does not claim objectivity forces
the weight, so it does not collide with `FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT`).

**Net minimal post-unification candidate surface (all UNADOPTED):**

1. **MEAS-REC-READOUT** — the unified measurement-with-readout axiom (folds C1 +
   C2-basis). *Strength: weak–medium (one existence slot spanning the dynamics
   and readout-context gates).*
2. **C2-WEIGHT** — the equal-block / indifference sector-measure weight datum
   (`t=1`). *Strength: weak (a binary indifference choice, no fitted number;
   same category as `kinetic_isotropy_primitive`).*
3. **SPACING** — the single dimensionless time-edge spacing `a_tau/a_s`.
   *Strength: weak (one dimensionless ratio).*
4. **PIN-GAUGE-CONTENT (C3)** — unchanged and **categorically separate** (gauge
   group / particle content / species); not expected to fold and does not.

So the unification takes the **block01 count from {C1, C2, C3}** to a sharper
**{MEAS-REC-READOUT, C2-WEIGHT, SPACING, C3}** in which the *measurement act* is
one axiom and the two things it provably cannot supply (the sector weight; the
metric spacing) are isolated as their own weakest data. This is the
weakest-sufficient/non-redundant target `AXIOM_MINIMALITY_POLICY.md` asks for,
recorded as **unmade science-level decisions** (policy §1/§4; approval routes
through §6) — nothing adopted, no verdict set.

---

## 6. Falsifiers (what would defeat the unification)

- A no-new-axiom derivation of record-producing dynamics **or** of the pointer
  basis from Lattice+Quantum+Record would moot the corresponding clause (and
  shrink or retire MEAS-REC-READOUT).
- A demonstration that SBS/quantum-Darwinism objectivity **does** fix the sector
  weight (refuting R2 weight-blindness, or the R3 einselection horn shown to give
  `t=1` not `t=2`) would **fold the C2-WEIGHT residual back in** — making the
  unification *fuller* than partial. The runner exhibits the opposite
  (weight-blind; dynamics horn at `t=2`).
- A demonstration that the measurement act *necessarily* fixes a metric spacing
  (refuting block02 SK-1 + block03 NODIAG) would fold the SPACING residual in.
- A consumer needing the *axis label* (not just the count `d_t`) or a sharpened
  charged-lepton `Q` materially off `2/3` would, respectively, re-weight the C1
  fanout or disfavor the equal-block `C2-WEIGHT` — neither defeats the
  *unification* of the basis content.
- A demonstration that one CPTP generator does **not** give a single monotone
  record order across commuting factors would break the N5 leg of the C1 fold.

---

## 7. Status (audit-lane handoff)

```yaml
proposed_artifact_type: axiom minimization / unification analysis (sufficiency + derivation leg)
proposal_allowed: false        # owner governance decision required; this section REQUESTS it
adopts_axiom: false
sets_audit_verdict: false
edits_axiom_premise_nodes: false
status_authority: independent audit lane / owner only
hypothetical_axiom_status: "conditional on accepted new axiom; not retained on the actual current surface"
unified_axiom_id: MEAS-REC-READOUT
sufficiency_verdict: partial_collapse
collapses:
  - C1 full set (B-AXIS N4 registration-direction + N5 single-clock + arrow [+ N2b-step] + record-formation floor)
  - C2 basis/identification half (observable T1-d det-readout + P-REC pointer + Koide objectivity-BASIS / 2-outcome alphabet)
does_not_collapse:
  - C2-WEIGHT: the equal-block (1,1) sector-MEASURE weight t=1 (objectivity is WEIGHT-BLIND per R2; the dynamics horn gives t=2 per R3) -> a separate max-entropy/indifference datum
  - SPACING: the N2b time-edge spacing a_tau/a_s (Lattice disavows spacing; SK-1 + NODIAG walled) -> a separate minimal spacing primitive
post_unification_candidate_surface:
  - MEAS-REC-READOUT (folds C1 + C2-basis; weak-medium)
  - C2-WEIGHT (equal-block/indifference weight; weak)
  - SPACING (a_tau/a_s; weak)
  - PIN-GAUGE-CONTENT / C3 (unchanged; categorically separate; does not fold)
runner: scripts/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.py
runner_cache: logs/runner-cache/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.txt
runner_total: "PASS=39 FAIL=0"
reproduced: true            # re-run identical; clean under python3 -W error; numpy + stdlib only; no empirical import
```

**Not in scope.** Adopting any candidate; deriving any kernel/rate/weight/value;
deriving the arrow's sign (past hypothesis), Born weights, the equal-block weight,
the dimensionful tick `2a_tau` / `a_tau/a_s`, `n_color`, generation count, or any
coupling/mass/mixing; folding C3; editing `docs/audit/data/` or any axiom file;
setting any audit verdict.

---

## 8. Load-bearing sources

- block01 cluster proposals (the two folded):
  `docs/AXIOM_UPDATE_PROPOSAL_RECORD_PRODUCTION_DYNAMICS_2026-06-20.md` (C1),
  `docs/AXIOM_UPDATE_PROPOSAL_READOUT_CONTEXT_OBJECTIVITY_2026-06-20.md` (C2).
- weight-blindness (the residual constraint):
  `docs/FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md` (N6/N7),
  `docs/KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md` (R3 countermodel).
- spacing residual: `.claude/science/physics-loops/axiom-update-proposals/block03_section_NODIAG.md`,
  `.claude/science/physics-loops/axiom-update-proposals/block02_section_SK1.md`.
- surface / policy: `docs/MINIMAL_AXIOMS_2026-06-05.md` (Record non-supply;
  Lattice no-spacing; open gates), `docs/audit/AXIOM_MINIMALITY_POLICY.md` (§1/§4/§6).
- consolidated set + map:
  `docs/AXIOM_UPDATE_PROPOSALS_CONSOLIDATED_2026-06-20.md`,
  `.claude/science/physics-loops/axiom-update-proposals/WALL_TO_GATE_MAP.md`.
- runners reused (same load-bearing legs):
  `scripts/axiom_update_record_production_dynamics_cluster_2026_06_20.py`,
  `scripts/axiom_update_proposal_readout_context_objectivity_runner_2026_06_20.py`.
