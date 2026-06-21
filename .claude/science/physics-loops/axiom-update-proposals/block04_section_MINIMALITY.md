# block04 — Section: MINIMALITY + RESIDUAL-ISOLATION — is the unified operational axiom STRICTLY WEAKER, POLICY-PREFERRED, and INDEPENDENT of the residual data primitives? does C3 fold?

**Date:** 2026-06-21
**Lane / branch:** `axiom-update-proposals`,
`physics-loop/axiom-update-proposals-block04-20260620`.
**Type:** AXIOM MINIMIZATION / UNIFICATION analysis (minimality + residual-isolation leg).
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

**Sibling leg (the prerequisite):**
`.claude/science/physics-loops/axiom-update-proposals/block04_section_SUFFICIENCY.md`
established, with runner
`scripts/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.py`
(**TOTAL: PASS=39 FAIL=0**), that the candidate unified axiom **MEAS-REC-READOUT**
*partially* collapses **C1** (dynamics/arrow) + the **C2 basis/identification
half**, leaving two residuals that do **not** collapse — the equal-block `(1,1)`
sector-MEASURE **weight** (`C2-WEIGHT`) and the time-edge **spacing** `a_tau/a_s`
(`SPACING`).

**Primary runner (this leg):**
`scripts/axiom_update_unified_axiom_minimality_independence_2026_06_21.py`
**Cached output:**
`logs/runner-cache/axiom_update_unified_axiom_minimality_independence_2026_06_21.txt`
(**TOTAL: PASS=28 FAIL=0**, deterministic — re-run identical; clean under
`python3 -W error`; numpy + stdlib `fractions` only; no empirical import; no RNG
draw is load-bearing).

> **Runner caught a real bug (load-bearing-residual pattern held).** The first
> draft hand-coded the `[SU(3)]²U(1)_Y` LH anomaly trace with a spurious extra
> factor of `n_color` (double-counting color on top of the `T(fund)=1/2` trace
> normalization), returning `Tr[SU3²Y]=1` instead of the banked `+1/3`. The
> `[FOLD] (ii)` leg **FAILed** and exposed it; fixed by dropping the extra `nc`
> (the color sum is already in `T(fund)`), after which all three banked LH traces
> reproduce exactly (`Tr[Y³]=-16/9`, `Tr[SU3²Y]=+1/3`, `SU3³=+2`). This is the
> documented runner-exposes-load-bearing-residuals pattern (memory:
> `feedback_runner_load_bearing_residuals`).

---

## 0. The five minimization questions (what this optimizes)

`AXIOM_MINIMALITY_POLICY.md` targets the **weakest sufficient, non-redundant,
independent** extension with **no laundering**. The sufficiency leg showed the
*fold* exists; this leg proves the *minimality properties of the folded set*:

1. **Strictly weaker.** Is the single operational axiom strictly weaker than
   C1 + C2 stated as **two** separate axioms (logical content + consequence sets)?
2. **Policy preference.** Does `AXIOM_MINIMALITY_POLICY.md` **prefer** it — by
   which admissibility/minimality criteria?
3. **Independence.** Are the unified axiom + the residual data primitives
   (`C2-WEIGHT`, `SPACING`) **mutually independent** — none derivable from the
   others + `A_min`?
4. **C3 fold.** Can `PIN-GAUGE-CONTENT` (gauge group / particle content) **also**
   fold into the operational axiom? (Expect **NO** — categorically distinct.)
5. **Final minimal set.**

The post-unification candidate set (all UNADOPTED), in the notation used below:

| id | candidate | gate(s) | strength |
|---|---|---|---|
| **U** | **MEAS-REC-READOUT** — one measurement-with-readout existence slot (folds C1 dynamics/arrow + C2 basis/identification half) | 1 (dynamics) + 2 (readout-context), basis part | weak–medium |
| **W** | **C2-WEIGHT** — the equal-block `(1,1)` sector-measure weight `t=1` (indifference / max-objective-information-over-labels datum) | 2 (sector measure), weight part | weak |
| **S** | **SPACING** — one dimensionless time-edge spacing `a_tau/a_s` | (Lattice spacing; declared open) | weak |
| **G** | **PIN-GAUGE-CONTENT (C3)** — gauge group + chirality template | 3 (gauge / particle content) | heavy |

---

## 1. STRICTLY WEAKER — logical content / consequence-set comparison (runner PART [0])

**Measure used: the consequence set (logical content).** An axiom `P` is
*logically weaker* than `Q` iff `Cons(P) ⊆ Cons(Q)` and *strictly* weaker iff
`Cons(P) ⊊ Cons(Q)` — equivalently, the weaker axiom **constrains less** and so
admits **more models**. This is the standard, decidable comparison and it is
exactly what "weakest sufficient" in the policy means.

The runner encodes each axiom by the **set of atomic load-bearing consequences**
it entails (the 10 distinct, separately-checkable claims drawn verbatim from the
two block01 notes — arrow existence, single-clock N5, registration-direction N4,
step-exists N2b, record floor, pointer basis, objective alphabet, det-readout
identification, P-REC pointer, **equal-block weight**):

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
  axioms do not (no over-reach).
- **`Cons(U) ⊊ Cons(C1 ∧ C2)`** — the two-axiom conjunction entails **strictly
  more**; the single witnessing extra atom is **`equal_block_weight`**. So U is
  **strictly weaker by consequence-set content**, and the *exact* content
  difference is isolated to the one residual `C2-WEIGHT` (the prior finding's
  weight-blindness, made precise as a single missing atom).
- **Model-count corroboration:** U fixes 9 atoms vs the two-axiom 10, so U admits
  `2¹ ≥ 2⁰` models — the weaker axiom admits at least as many (here strictly more)
  models, i.e. constrains less.
- **The converse FAILS:** `Cons(C1 ∧ C2) ⊄ Cons(U)` because `U ⊬ equal_block_weight`.
  So U is **strictly weaker, not equivalent** to the two-axiom conjunction.

**Why this is genuinely weaker (the physics).** C1 and C2-stated-separately are
**two independent existential posits** — "there exist record-producing dynamics"
AND "there is a sector-measure that counts outcomes (and its equal-block face
fixes `t=1`)". U is a **single** existential — "there is one measurement
interaction" — whose *one* witness `(L, pointer basis, broadcast structure)`
yields both the dynamics/arrow and the pointer-basis/objectivity content **as
consequences of the same object**. A single premise `P` with `P ⊨ A` and `P ⊨ B`
carries `|Cons(P)| ≤ |Cons(A)| + |Cons(B)|`, and here it is **strictly fewer**
because the unified interaction provably does **not** carry the independent
weight atom (it is weight-blind, sufficiency leg PART 3). **Strictly weaker by
both the consequence-set and the model-count measures.**

---

## 2. POLICY PREFERENCE — does `AXIOM_MINIMALITY_POLICY.md` prefer U? (runner PART [4])

The policy's stated target is the **weakest sufficient, non-redundant,
independent** extension that does **not launder** premises (§1 disallowed moves;
§2 allowed "bounded compositions with explicit named residuals"; §6
admissibility/no-laundering tests). U is preferred on **every** criterion:

| Policy criterion (source) | Verdict for U | Evidence |
|---|---|---|
| **Weakest sufficient** (policy intent; "weakest sufficient" framing) | **U is weakest** for gates 1+2 | PART [0] strict-subset: U entails the dynamics+basis content and **nothing more**; dropping any clause loses a discharge (sufficiency leg §1), strengthening it (adding a weight/kernel) over-reaches AND would clash with weight-blindness. |
| **Non-redundant** (§2 "bounded compositions with explicit named residuals") | **non-redundant** | PART [1] countermodels: U does **not** subsume W or S, so {U, W, S} is a non-redundant generating set with the two residuals **explicitly named** — exactly the §2 "bounded composition with named residuals" shape. |
| **Independent** (policy intent) | **independent** | PART [1] mutual-independence countermodels (below) + PART [3] C3 categorical separation. |
| **No laundering** (§1 final bullet; §6 no-laundering test; precedent of `kinetic_isotropy_primitive`) | **no laundering** | U adds content the `MINIMAL_AXIOMS_2026-06-05.md` memo declares **outside** axiom content (gates 1+2), recorded as an **unmade science-level decision** (§1/§4) — it does **not** reword Lattice/Quantum/Record (§1 disallowed) and edits no registry. Record verbatim declines "measurement/decoherence dynamics … weighting … or occupancy rule"; U supplies the dynamics + basis as a *separate* recorded decision, never folded into Record. |

**Decisive policy point.** The unification is precisely the move the policy
**rewards**: it takes the block01 count `{C1, C2}` (two weak axioms in two gates)
to **one** weak–medium axiom **U** (one act spanning both gates) **plus the two
explicitly-named residuals** it provably cannot supply. Fewer independent axioms,
each weaker or equal, with all residuals named — the weakest-sufficient /
non-redundant / no-laundering target. The §3/§6 precedent (`kinetic_isotropy`
admitted as a *structural, dimensionless, binary, no-fitted-number* primitive) is
the template for the two residual data `W` and `S`; the route is §6 owner
approval, not in-lane adoption.

---

## 3. INDEPENDENCE by COUNTERMODEL — {U, W, S} mutually independent (runner PART [1]–[2])

**Method.** Independence is proved the standard model-theoretic way: for each
primitive `P ∈ {U, W, S}`, exhibit a model on the `A_min` surface that satisfies
`A_min` + **the other two** primitives but **violates** `P`. A countermodel proves
`P` is **not** derivable from `A_min` + the others. The runner builds all three,
reusing the **exact** load-bearing objects of the block01/sufficiency runners.

### 3.1 U is independent of {A_min, W, S}

The **record-formation no-record witnesses** are the countermodel: the `H = 0`
(no-dynamics) baseline is `A_min`-consistent and supplies **no** record floor
(`|coh|` frozen at `0.5` for all `#env = 1,2,4,16,64`). This holds for **any**
weight value `W` and **any** spacing value `S` — neither a static weight nor a
spacing datum sources a CPTP einselecting generator. So `{A_min, W, S} ⊬ U`: the
unified axiom adds **genuinely new dynamics content** that no static data supply.

### 3.2 W (equal-block weight) is independent of {A_min, U, S}

This is the **load-bearing reuse of koide weight-blindness** (the KEY PRIOR
FINDING). With the **full** measurement axiom U in force — pointer basis fixed,
objectivity present, einselection running — the weight ratio `t` is **still
free**, by *two* independent countermodels:

- **(i) objectivity is weight-blind.** The SBS objectivity plateau equals
  `H(weights)` and is positive/objective for **both** `t=1` (`H=1.000` bit) and
  `t=2` (`H=0.918` bit). Clause (c) **reports** the supplied weights; it does not
  **select** them (koide block02 R2; `FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT`
  N6/N7).
- **(ii) the dynamics horn gives the wrong value.** The einselection **fixed
  point** in the pointer basis is the maximally mixed `I/3`, which through the
  (rank-1, rank-2) singlet/doublet split gives the **rank** weights `(1/3, 2/3)`
  ⇒ `r = 1` ⇒ **`t = 2`**, **not** the equal-block `t = 1` (koide R3 countermodel
  `W_t`: `r*(t)=t/2` free under `A_min`).

So the model `{U on, S any, weight = rank face (t=2)}` satisfies `A_min + U + S`
and **violates** `W` (`t ≠ 1`). Hence `{A_min, U, S} ⊬ W`: **the measurement
dynamics does NOT fix the equal-block weight** — exactly the prior finding,
re-derived here as a formal independence countermodel.

### 3.3 S (spacing `a_tau/a_s`) is independent of {A_min, U, W}

The adjacency predicate `|dx|+|dy|+|dz| = 1` is **metric-blind**: the 6-NN edge
set is **identical** for `a_tau/a_s = 1, 10, 0.137` (Lattice axiom verbatim
disavows "metric scale, lattice spacing"; block02 **SK-1** and block03 **NODIAG**
both walled). The measurement rate `γ` (U clause a) fixes a half-life in
**dynamics ticks**, not the dimensionful metric edge `a_tau`. So a model with
`U + W` on at **any** `a_tau/a_s` satisfies `A_min + U + W` and the value of
`a_tau/a_s` is unconstrained. Hence `{A_min, U, W} ⊬ S`.

### 3.4 Mutual independence + ORTHOGONAL DIALS (runner PART [2])

Each of `{U, W, S}` has a countermodel, so the three are **mutually independent**,
none derivable from `A_min` + the others. The runner then confirms the two data
dials are **orthogonal**, and both are orthogonal to the measurement act:

- vary the **weight** dial `t ∈ {1/2, 1, 2, 7/3}`: the **spacing** witness
  (adjacency edge set) is **unchanged** — `t` does not leak into the spacing.
- vary the **spacing** dial `a_tau/a_s ∈ {1, 10, 0.137, 3.3}`: the **weight**
  witness `Koide r* = w_p/(2 w_s)` at `t=1` is **unchanged** (`= 0.5`) — spacing
  does not leak into the weight.
- vary **both** dials arbitrarily: the **measurement** witnesses are **unchanged**
  — arrow monotone, einselection floor `→ 0`, pointer alphabet `= 2` outcomes —
  the measurement axiom reads **neither** dial.

**Each observable depends on exactly ONE primitive's datum and is blind to the
other two: clean residual isolation, no cross-leakage.** This is the
"spacing/weight are orthogonal dials" claim, verified as a grid sweep.

---

## 4. C3 FOLD TEST — does PIN-GAUGE-CONTENT fold into U? **NO** (runner PART [3])

**Expected and confirmed: NO.** Gauge group / particle content is a **different
KIND of datum** — a *choice of gauge group + chiral matter representations* — from
a *measurement-interaction existence* datum. The runner tests categorical
distinctness **both ways** with explicit countermodels:

- **(i) the MEASUREMENT structure is blind to the gauge content.** The
  einselection / arrow / floor witnesses are computed from the dephasing dynamics
  + the central decomposition **only**; they do **not** read the chirality grading
  `E` or any anomaly trace. And the four published **gauging-selection
  discriminators** stay blind regardless of any measurement (e.g. the chirality
  grading **commutes** with the color generators, `‖[E, λ₃]‖ = ‖[E, λ₈]‖ = 0`):
  adding U changes **none** of them — the gauging gate stays open under U.
- **(ii) the GAUGE content is blind to the measurement act.** The LH
  one-generation anomaly traces are **fixed rationals** (`Tr[Y³] = -16/9`,
  `Tr[SU3²Y] = +1/3`, `SU3³ = +2`) computed with **no** measurement object; and
  the **chirality** of the completion (the load-bearing P-COMP word) is a pure
  content fact — the SM chiral RH template `(4/3, -2/3, -2, 0)` cancels all six
  **and** is genuinely chiral (not vector-like), decided with **no** pointer
  basis / einselection / objectivity.

**Decisive.** Neither's witnesses move the other's. A single "operational
measurement" axiom **cannot entail a choice of gauge representations** (no
measurement interaction fixes `Tr[Y³]` or whether a completion is chiral), and the
gauge content **cannot entail a measurement interaction**. They live in
**different gates** of `MINIMAL_AXIOMS_2026-06-05.md` (gates 1/2 vs gate 3).
Folding C3 into U would be a **category error** and **policy-laundering** (it would
smuggle a particle-content choice into an operational axiom). So
**PIN-GAUGE-CONTENT stays a separate gate-3 candidate** — the unification touches
only gates 1+2, exactly as expected.

---

## 5. THE FINAL MINIMAL PROPOSAL SET (runner PART [4])

After unification, minimality, and residual isolation, the **minimal axiom-update
proposal set** (all UNADOPTED; `hypothetical_axiom_status` throughout) is:

1. **U = MEAS-REC-READOUT** — the unified operational measurement-with-readout
   axiom. One existence slot for the realized state supplying *at once* the
   einselecting CPTP dynamics + orientation (= C1's arrow / N4 registration
   direction / N5 single clock / N2b-step / record floor) **and** the pointer
   basis = central/`K`-CPT decomposition + SBS objectivity-**basis** (= C2's
   T1-d det-readout identification + P-REC pointer + Koide objectivity-basis /
   2-outcome alphabet). **Strictly weaker** than C1+C2 stated separately (§1);
   **weakest sufficient** for gates 1+2; existence/slot only (no kernel/rate, no
   weight, no probability, no spacing, no arrow *sign*); weaker than a past
   hypothesis. *Strength: weak–medium.*
2. **W = C2-WEIGHT** — the equal-block `(1,1)` sector-measure weight `t=1` (the
   indifference / max-objective-information-over-labels datum). A single
   dimensionless binary choice; **independent** of U (objectivity weight-blind;
   the dynamics horn gives `t=2`). *Strength: weak; same category as
   `kinetic_isotropy_primitive` (structural, dimensionless, binary, no fitted
   number).*
3. **S = SPACING** — one dimensionless time-edge spacing `a_tau/a_s`.
   **Independent** of U and W (metric-blind adjacency; orthogonal dial).
   *Strength: weak; one dimensionless ratio.*
4. **G = PIN-GAUGE-CONTENT (C3)** — gauge group + opposite-chirality RH template.
   **Categorically separate** (gate 3); does **not** fold (§4). *Strength: heavy;
   unchanged from block01.*

**Net of the whole campaign.** block01 `{C1, C2, C3}` → block04
`{U, W, S, C3}` in which the **measurement act is one axiom** and the **two things
it provably cannot supply** (the sector weight; the metric spacing) are isolated
as their **own weakest data**, with C3 left standing as the one categorically
distinct (gate-3) addition. Each member is **mutually independent** of the others
(none derivable from `A_min` + the rest), and the whole set is the
**weakest-sufficient / non-redundant / independent / no-laundering** target
`AXIOM_MINIMALITY_POLICY.md` asks for — recorded as **unmade science-level
decisions** (policy §1/§4; approval routes through §6). Nothing adopted; no
verdict set.

> **Residual-isolation, in one line:** the *measurement interaction* is one weak
> existence axiom (U); the *sector weight* (W) and the *metric spacing* (S) are
> two separate dimensionless data, each one datum, mutually independent and
> orthogonal; the *gauge content* (C3) is a categorically different content choice
> that does not fold.

---

## 6. Falsifiers (what would defeat this minimality leg)

- **A no-new-axiom derivation** of the weight `t=1` (a missed symmetry; or the
  einselection horn shown to give `t=1` not `t=2`) would **fold `W` back in** and
  shrink the set to `{U, S, C3}` — and refute the §3.2 independence countermodel.
  (The runner exhibits the opposite: weight-blind; dynamics horn at `t=2`.)
- **A demonstration that the measurement act necessarily fixes a metric spacing**
  (refuting SK-1 + NODIAG) would fold `S` in.
- **A model where the consequence sets are NOT strictly nested** (e.g. U shown to
  entail a consequence outside `Cons(C1 ∧ C2)`, or C2-sep shown not to carry the
  weight atom) would break the §1 strict-weaker comparison.
- **A measurement-structure observable shown to move under a gauge-content change
  (or vice versa)** would break the §4 categorical-distinctness and reopen the C3
  fold — the runner shows neither moves the other.
- **A consumer needing the axis *label*** (not just the count `d_t`) would
  re-weight the C1 fanout inside U but does **not** defeat the *minimality* of the
  set.

---

## 7. Status (audit-lane handoff)

```yaml
proposed_artifact_type: axiom minimization / unification analysis (minimality + residual-isolation leg)
proposal_allowed: false        # owner governance decision required; this section REQUESTS it
adopts_axiom: false
sets_audit_verdict: false
edits_axiom_premise_nodes: false
status_authority: independent audit lane / owner only
hypothetical_axiom_status: "conditional on accepted new axiom; not retained on the actual current surface"
unified_axiom_id: MEAS-REC-READOUT
strictly_weaker_than_C1_plus_C2: true
strictly_weaker_measure: "consequence set (logical content) + model count: Cons(U) STRICT subset of Cons(C1-sep AND C2-sep); the single extra atom is the equal-block weight; U admits strictly more models; converse derivation fails"
policy_prefers_unified: true
policy_criteria_met:
  - weakest_sufficient   # U entails the dynamics+basis content and nothing more
  - non_redundant        # U does not subsume W or S (named residuals; policy section 2 bounded composition)
  - independent          # {U,W,S} mutually independent + C3 categorically separate
  - no_laundering        # adds content the memo declares OUTSIDE axiom content; no reword of Lattice/Quantum/Record (policy section 1/4/6)
independence_check: "{U, W, S} mutually independent -- each has a countermodel on A_min satisfying A_min + the other two but violating the target; none derivable from A_min + the others"
independence_method: countermodel (model-theoretic); reuses koide weight-blindness (U does NOT fix the equal-block weight) and metric-blind adjacency (U/W do NOT fix the spacing); weight and spacing verified ORTHOGONAL dials
c3_folds: "no"
c3_reason: "gauge group + chiral matter REPRESENTATIONS are a content-choice datum (gate 3), categorically distinct from a measurement-interaction EXISTENCE datum (gates 1/2); measurement witnesses blind to gauge content and vice versa; folding would be a category error / laundering"
residual_primitives:
  - "C2-WEIGHT: equal-block (1,1) sector-measure weight t=1 (one dimensionless indifference datum)"
  - "SPACING: time-edge spacing a_tau/a_s (one dimensionless ratio)"
final_minimal_set:
  - MEAS-REC-READOUT   # unified operational measurement-with-readout axiom (folds C1 + C2-basis); weak-medium
  - C2-WEIGHT          # equal-block/indifference sector-measure weight t=1; weak
  - SPACING            # a_tau/a_s; weak
  - PIN-GAUGE-CONTENT  # C3; categorically separate; does NOT fold; heavy; unchanged
runner: scripts/axiom_update_unified_axiom_minimality_independence_2026_06_21.py
runner_cache: logs/runner-cache/axiom_update_unified_axiom_minimality_independence_2026_06_21.txt
runner_total: "PASS=28 FAIL=0"
runner_bug_caught: "first draft double-counted color in Tr[SU3^2 Y] (extra n_color factor); FOLD(ii) FAILed and exposed it; fixed -> banked LH traces reproduce (-16/9, +1/3, +2)"
reproduced: true            # re-run identical; clean under python3 -W error; numpy + stdlib (fractions) only; no empirical import
sibling_leg: .claude/science/physics-loops/axiom-update-proposals/block04_section_SUFFICIENCY.md
```

**Not in scope.** Adopting any candidate; deriving any kernel/rate/weight/value;
deriving the arrow's sign (past hypothesis), Born weights, the equal-block weight,
the spacing `a_tau/a_s`, `n_color`, generation count, or any coupling/mass/mixing;
folding C3; editing `docs/audit/data/` or any axiom file; setting any audit
verdict.

---

## 8. Load-bearing sources

- sibling sufficiency leg (the fold this leg analyzes):
  `.claude/science/physics-loops/axiom-update-proposals/block04_section_SUFFICIENCY.md`,
  `scripts/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.py`.
- block01 cluster proposals (the candidates folded / tested):
  `docs/AXIOM_UPDATE_PROPOSAL_RECORD_PRODUCTION_DYNAMICS_2026-06-20.md` (C1),
  `docs/AXIOM_UPDATE_PROPOSAL_READOUT_CONTEXT_OBJECTIVITY_2026-06-20.md` (C2),
  `docs/AXIOM_UPDATE_PROPOSAL_GAUGE_CONTENT_2026-06-20.md` (C3).
- weight-blindness (the KEY PRIOR FINDING / the W-independence countermodel):
  `docs/FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md` (N6/N7),
  `docs/KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md` (R3 countermodel `W_t`).
- spacing residual (the S-independence countermodel):
  `.claude/science/physics-loops/axiom-update-proposals/block03_section_NODIAG.md`,
  `.claude/science/physics-loops/axiom-update-proposals/block02_section_SK1.md`.
- surface / policy:
  `docs/MINIMAL_AXIOMS_2026-06-05.md` (Record/Lattice non-supply; open gates list),
  `docs/audit/AXIOM_MINIMALITY_POLICY.md` (§1 disallowed/no-laundering; §2 bounded
  composition with named residuals; §3/§6 admissibility precedent
  `kinetic_isotropy_primitive`; §4 unmade-decision workflow; §6 owner approval).
- consolidated set + map:
  `docs/AXIOM_UPDATE_PROPOSALS_CONSOLIDATED_2026-06-20.md`,
  `.claude/science/physics-loops/axiom-update-proposals/WALL_TO_GATE_MAP.md`.
