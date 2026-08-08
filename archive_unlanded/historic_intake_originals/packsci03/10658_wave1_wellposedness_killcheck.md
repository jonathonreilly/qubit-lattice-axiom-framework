# Wave 1 — Well-Posedness Kill-Check on the First Conjunct

**Date:** 2026-07-25
**Task:** try to shut the campaign down on day one. Is
`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md:21` conjunct 1
("derive the physical matter action and its measure") well-posed, or a
category error?
**Baseline:** `origin/main` at `e192e332f2` (fetched 2026-07-25). Every quote
below is from `git show origin/main:<path>`, not the working tree.
**Status authority:** none. This report sets, predicts, and estimates no audit
verdict. It adds no axiom, primitive, vocabulary, or premise.
**Runner (scratchpad, exact/sympy, no float inputs):**
`…/scratchpad/wave1_killcheck_runner.py` — **SUMMARY: PASS=37 FAIL=0**,
log at `…/scratchpad/wave1_killcheck_runner_log.txt`.

---

## 0. Headline

**The campaign is well-posed, but not as the brief states it, and not on the
reading the brief fears.** Three findings, in descending order of value:

1. **GOVERNANCE (highest value).** The obligation is **internally
   inconsistent**. Its `## Exact target` section (`:11-13`) and the machine
   registry `derivation_obligations.json` — the only non-prose surface — both
   record the target as the **grain question alone**. Its prose `## Closure
   criterion` (`:21`) additionally demands *deriving* an object that the
   obligation's own historical source
   (`TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md:40-44`)
   **presupposed rather than supplied**. Both sibling obligations attach
   "derive" to the target identity and "provide"/"construct" to the substrate
   carrier; only this one attaches "derive" to the substrate. This is a prose
   surface over-reaching its own registered target — precisely the failure mode
   the campaign's rule 6 warns about, occurring inside the campaign's own
   anchor document.

2. **THE CAMPAIGN BRIEF'S FACTUAL PREMISE IS FALSE.** The brief states the
   second conjunct "is already discharged" and that the first "has never been
   attempted". Both halves are contradicted by the corpus. The three most
   recent grain notes say verbatim that they engage **neither** part
   (`…GRAIN_MENU…2026-07-16.md:405-410`; `…GRAIN_SHARPENING…2026-07-16.md:443-448`;
   `KCPT…BEREZIN…2026-07-17.md:296-299`), and the axiom-surface attack on the
   action/measure question was already run on 2026-07-04 and 2026-07-10.

3. **PHYSICS.** Reading (i) — derive from the four axioms alone — is a
   category error at **two** independent layers, and I built the missing
   witness for the second layer natively and exactly. Reading (iii) is the only
   well-posed one, and I can now state the **first exact menu count**: on the
   maximally-constrained edge-wise class the menu is a **2-real-parameter
   space, `{a·I + b·SWAP}`**, which after quotienting the inert constant shift
   and positive rescaling is **exactly a 2-point set** — not a singleton. The
   surviving invariant is `sign(b)`, and it is physical: the two points put the
   one-excitation band minimum at `k=0` and at `k=(π,π,π)` respectively.

---

## 1. Surfaces read (mandatory framework refresher)

| Surface | What I took from it |
|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` (full, 193 lines) | axiom text, Qualification, dynamics section, open-gates list |
| `docs/audit/AXIOM_MINIMALITY_POLICY.md:1-200` | `A_min` fixture, allowed/disallowed moves, two premise types, policy-carries-no-premise-weight rule |
| `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (full, 46 lines) | the six-step check; the explicit "dynamics, source/action" exclusion |
| `docs/audit/data/axiom_premise_nodes.json` | 4 nodes: `minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive` |
| `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` | source note of an invoked primitive |
| `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` | source note of an invoked primitive |
| `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` | source note of an invoked primitive |
| `docs/audit/data/derivation_obligations.json` | the registered target text; 3 canonical obligations |
| `docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md` | the obligation under test |
| `docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md`, `docs/THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md` | sibling closure criteria, for comparison |
| `docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md` | the obligation's named historical source |
| `docs/audit/data/ledger/` — all **3867** shards, extracted from `origin/main` | every status claim below |

I invoke no approved primitive as a proof input. I cite all three only to
record what they exclude.

---

## 2. (a) Every sentence bearing on whether dynamics/action content can EVER be derived

### 2.1 The axiom text itself names no such object

`docs/MINIMAL_AXIOMS_2026-06-29.md:33-84` is the complete four-axiom block plus
Qualification. Mechanical check (`grep -inE "action|measure|hamilton|dynamic|
time|lagrangian|energy|integral|weight|probab|grassmann|fermion|transfer"`
restricted to lines 33-84): **zero matches.** The axiom vocabulary is: sites,
nearest-neighbor adjacency, translations, proper cubic rotations, a domain of
local possibilities with presentation `M_2(C)`, a fixed nearest-neighbor
admissibility rule, records (locking, one-per-site, permanence), and an
additive scalar readout `I`. Nothing else.

The two clauses that matter most:

> **Admissibility / Local Constraint**
>
> There is one fixed nearest-neighbor admissibility rule, covariant under
> lattice translations and proper cubic rotations.
>
> For each site, the available possibilities are determined by, and vary with,
> the nearest-neighbor conditions.
>
> — `docs/MINIMAL_AXIOMS_2026-06-29.md:55-61`

Note the quantifier: *there is one fixed rule*. The axiom is **existential over
rules**; it never names which rule. Any covariant nearest-neighbor rule yields
a model.

> ## Qualification
>
> These axioms state only their named primitive content. Further physical
> structure requires a retained derivation or bridge, or explicit approved-
> primitive registration, before use as a premise. A choice not fixed by the
> supplied structure remains a named conditional or open dependency.
>
> — `docs/MINIMAL_AXIOMS_2026-06-29.md:74-79`

This sentence is the pivot. It does **not** say action content is
underivable; it says it is not axiom content and must arrive by a *retained
derivation or bridge* or by *registration*. Read alone, it leaves reading (ii)
open.

### 2.2 The explicit dynamics disclaimer, in full context

> ## Relation To Dynamics And Kinetic Branch Selection
>
> Admissibility is not a dynamics axiom. It determines availability by a
> nearest-neighbor rule: for each site, the available possibilities are
> determined by, and vary with, the nearest-neighbor conditions. It does not
> choose a Hamiltonian or transfer operator, supply transition probabilities or
> weights, select a scalar or nonzero kinetic branch, assert a Dirac-square
> carrier, define a time metric, or provide a record-production process or
> physical persistence dynamics.
>
> Static spatial kinetic questions, probability/process questions, and temporal
> evolution questions should be tracked separately. A realized kinetic branch, if
> proposed, is downstream content: it needs a retained derivation or bridge, or
> an approved-primitive registry update, before audit rows may use it
> as load-bearing content. **The four axioms are compatible with such later
> content, but do not include it.**
>
> — `docs/MINIMAL_AXIOMS_2026-06-29.md:103-118` (emphasis mine)

The final sentence is decisive and is the sentence the campaign brief compressed
away. The memo disclaims **inclusion**, not derivability. "Compatible with" is
exactly a model-theoretic statement: the axioms admit extensions carrying such
content. That is a *consistency* claim, and — crucially — consistency with more
than one extension is what makes a *unique* action underivable (§5).

### 2.3 The source/action clause and the open-gates list

> Rows that require P2/modulus, log-det, **source/action**, measurement,
> Born weights, readout-context selection, central-sector decomposition, `K`/CPT
> structure, transition relations, record-production dynamics, physical
> persistence dynamics, local observability, or any other additional bridge must
> cite separate retained authorities or remain bounded/pending according to the
> audit ledger.
>
> — `docs/MINIMAL_AXIOMS_2026-06-29.md:128-134`

> ## Open Gates Outside The Axioms
>
> The four axioms do not close, import, or rename the framework's downstream open
> gates. In particular, the following remain outside axiom content:
>
> - the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`;      (:161)
> - …
> - context selection, measurement basis selection, Born weights, probability
>   rules, update laws, decoherence mechanisms, and formation rules …          (:164-167)
> - arrow, record-production dynamics, physical persistence dynamics, time metric,
>   and local observability of records;                                        (:168-169)
> - **source/action and physical-observable identification;**                   (:170)
> - …
>
> — `docs/MINIMAL_AXIOMS_2026-06-29.md:156-173`

`:170` is the campaign's anchor. In context it sits in a list headed "remain
**outside axiom content**" — again a scope statement about the axiom set, not
an impossibility theorem. But note what `:168` removes: **the time metric**.
An action is a functional on histories; a measure is a measure on histories.
Neither object has a domain until a temporal direction exists, and the memo
places the time metric outside axiom content too.

> Probability, dynamics, readout contexts, and physical observable bridges
> remain downstream.
>
> — `docs/MINIMAL_AXIOMS_2026-06-29.md:192-193`

### 2.4 Governing policy documents

> `A_min` is fixed for ordinary audit work as the four named framework axioms
> in `docs/MINIMAL_AXIOMS_2026-06-29.md` … **Lane closure must close from the
> current approved premise surface by derivation, identification, bounded
> composition, or no-go boundary**, not by amending that surface inside the lane.
>
> — `docs/audit/AXIOM_MINIMALITY_POLICY.md:18-23`

This sentence is the strongest textual authority *for* the campaign: it names
**"no-go boundary"** as a legitimate lane closure, on equal footing with
derivation. A sharp negative is not a failure mode here; it is a chartered
outcome. Reinforced at `:48-49`:

> - No-go boundary notes that state what is structurally unclosable from
>   the current axiom set.
>
> — `docs/audit/AXIOM_MINIMALITY_POLICY.md:48-49` (Allowed moves)

And at `:41-46`, the positive route is scoped narrowly:

> - First-principles derivations from `A_min` that close **without additional
>   assumptions**; these are the retained-tier path after class C audit.
>
> — `docs/audit/AXIOM_MINIMALITY_POLICY.md:45-46`

> The supplied foundation has exactly two premise types: **Axioms and approved
> primitives** … Everything else must be an audited derivation or remain
> conditional/open. `docs/audit/data/derivation_obligations.json` tracks exact
> open work but **carries zero premise weight**.
>
> — `docs/audit/AXIOM_MINIMALITY_POLICY.md:82-90`

> Axioms and approved primitives are the complete supplied foundation. … **No
> admission class exists**: every other scientific dependency must be
> retained-derived or remain conditional/open.
>
> — `docs/MINIMAL_AXIOMS_2026-06-29.md:97-101`

Finally, the primitive-registry check closes the last door on reading (ii):

> 5. **Do not grant more than the primitive source note declares.** Any
>    dimensionless quantity, selector, weighting rule, normalization rule,
>    probability rule, readout bridge, **dynamics, source/action**, or empirical
>    match remains separate unless independently derived.
>
> — `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md:13-16`

And each of the three registered primitives disclaims the exact objects the
conjunct asks for, in its own source note:

- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md:19-23,42-43` — "units conversion, not a
  physics axiom … carries zero dimensionless content".
- `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md:30-34` — "It carries no
  dimensionless dynamical content … not a new dynamics"; registry note adds
  "This primitive supplies only the kinetic form ratio, not an absolute scale,
  spacing-ratio theorem, **dynamics**, or downstream Lorentz theorem".
- `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md:37-41,60-63` — "It does not
  supply a state, state-selection rule, averaging over alternatives,
  **measure**, weighting, probability rule, typicality claim, genericity claim,
  preferred state, default state, boundary condition, normalization rule, or
  state-contingent value."

**Net of (a):** the axiom set and *all three* approved primitives —
i.e. the entire supplied foundation, per `MINIMAL_AXIOMS:97-101` — contain, by
explicit node-by-node disclaimer, **zero** action content and **zero** measure
content. None of these sentences asserts that action content is *underivable*;
what they establish is that the derivation, if it exists, must be a **retained
derivation from a foundation whose every node has certified it contains no such
content**.

---

## 3. (b) Is there a landed NO-GO stating the action is not derivable?

**No. And the reason is sharper than "not yet written."**

### 3.1 Full ledger census (read from `docs/audit/data/ledger/` shards, not prose)

Across all **3867** shards on `origin/main`:

| `claim_type: no_go` rows | count |
|---|---|
| `effective_status: unaudited` | **437** |
| `effective_status: audited_conditional` | **1** |
| `retained` / `retained_bounded` / any retained grade | **0** |

The single audited row is
`gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_full_…`
(`audited_conditional`) — a linear-algebra compression no-go about a Wilson
block, unrelated.

**There is not a single retained-grade no-go of any kind in this repository.**
Any wave that plans to "cite the landed no-go" for anything is planning on a
surface that does not exist.

### 3.2 The candidate notes, each with its live status

| Note | `effective_status` | Scope — does it foreclose the conjunct? |
|---|---|---|
| `STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md` | **unaudited** | **Route only.** Its §5 theorem denies that the axioms select *the staggered* law; it exhibits ONE alternative model. It does not deny that some *other* law is selected. |
| `ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md` | **unaudited** | **Grain only.** `:55-65`: axioms + primitives "do not choose … count-once over … count-twice". Silent on the action itself. |
| `ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md` | **unaudited** | **Explicitly disclaims the conjunct.** See §3.3. |
| `BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md` | **unaudited** | **Gauge action, stale stack.** Its premise list (`:203-207`) is the pre-reset "Quantum" axiom, `g_bare=1` open gate, accepted-premise vocabulary. Not the matter action; not the current surface. |
| `YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md` | **unaudited** | **One scalar only** (`λ`, the source *unit*), and it quotes a superseded axiom memo verbatim at `:48-56` ("Reality is a qubit at every lattice site"), citing `minimal_axioms` via `MINIMAL_AXIOMS_2026-05-20.md`. |
| `INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md` | **unaudited** | Route (kinetic order). |
| `QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md` | **unaudited** | Route (boost faithfulness); pre-reset axiom name. |
| `SINGLE_CLOCK_INDEPENDENT_COMMUTING_TRANSFER_FACTOR_N5_NO_GO_NOTE_2026-06-17.md` | **unaudited** | Route (transfer factorization). |

Adjacent positive rows for calibration:
`staggered_os0_supplied_action_ks_blocking_four_taste_module_narrow_theorem_note_2026-07-11`
is `retained_bounded` — and its own claim-scope in the ledger records the
mechanism as "the present theorem likewise **treats the action as supplied**".
That is the one retained-grade matter-action-adjacent surface in the repo, and
it is retained *because* it supplies the action rather than deriving it.

### 3.3 The most important prior-art sentence in the corpus

> The result grants an auxiliary complex carrier assignment and compares two
> determinant-style readout laws on it. … Since `F_R=2F_C`, this witness proves
> underdetermination of the raw determinant-power normalization; **it does not
> prove that two inequivalent matter actions or Gaussian measures exist.**
> Calling either functional a physical occupancy law would require the
> action/readout bridge that is absent from this construction.
>
> The result does not derive a physical matter action, Berezin measure, K/CPT
> structure, determinant line, polarization, orbit quotient, or physical
> record-to-action map.
>
> — `docs/ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md:110-121`

This is the exact gap in the corpus. The repo has a *readout-level*
non-entailment witness and explicitly declines to claim a *matter-law-level*
one. §5 of this report supplies the missing matter-law-level witness natively.

**Verdict on (b): no landed no-go forecloses the conjunct; nothing at retained
grade forecloses anything, anywhere. Every candidate is a route-level negative
at `unaudited` grade, and the closest one explicitly declines the conjunct.**

---

## 4. (c) Three readings — which does the obligation assert?

### 4.1 The three surfaces do not agree with each other

| Surface | Authority | What it demands |
|---|---|---|
| `derivation_obligations.json` → `nodes.ac_orbit_occupancy_statistical_grain_derivation_obligation.target` | machine registry; the non-prose surface | *"Derive from the retained framework chain whether the physical charged-lepton matter action counts the K/CPT orbit or holomorphic pair once rather than counting each sector or channel."* — **grain only.** No action-derivation clause at all. |
| `AC_…OBLIGATION.md:11-13` `## Exact target` | prose | Verbatim identical to the registry. **Grain only.** |
| `AC_…OBLIGATION.md:21-24` `## Closure criterion` | prose | *"A closing theorem must **derive the physical matter action and its measure**, then distinguish the count-once … from the count-twice … without inserting the desired charged-lepton value or readout dictionary."* — **grain PLUS a substrate derivation.** |
| ledger shard `…/ac/ac_orbit_occupancy_statistical_grain_derivation_obligation.json` | audit lane record | `load_bearing_step` = the closure-criterion sentence, class **E**; `effective_status` = `audited_renaming`; `notes_for_re_audit_if_any` = *"supply an independently auditable derivation of the physical matter action and measure **that selects** `det_C` rather than `|det_C|^2`, without inserting the target readout."* |

The audit lane's own re-audit instruction is the tiebreaker on *scope*: it
fuses the two clauses into **one instrumental demand** — a derivation of the
action and measure *that selects the grain*. Not a standalone universal
derivation of the matter action of the world. That is reading (iii)-shaped, not
reading (i)-shaped.

### 4.2 Reading (i) — derive from the four axioms alone

**Foreclosed, and at two independent layers.**

**Layer 1 (expressibility / category).** The axiom language (`:33-84`) has no
term denoting an action, a measure, a dynamics, an energy, an integral, a time
direction, or a Grassmann/fermionic carrier — verified by grep, zero matches
(§2.1). "The physical matter action" is therefore not a term of the axiom
language. A derivation of it from the axioms alone would first require a
definitional extension supplying that vocabulary, and the memo places exactly
that vocabulary outside axiom content at `:161`, `:163-167`, `:168-169`,
`:170`. So reading (i) is not a hard derivation problem — **it is not a
derivation problem at all.** It is a request to prove a sentence not in the
language.

**Layer 2 (semantic underdetermination), the fallback that survives if anyone
disputes Layer 1.** Grant the vocabulary by conservative extension. Then a
unique action would be entailed only if every model of the axioms carried the
same one. It does not: §5 constructs two extensions of *the same* axiom reduct
whose matter laws satisfy every symmetry constraint the axioms can impose and
still differ in a scale- and shift-invariant physical invariant.

**These two layers are not the same argument, and both are needed.** Layer 1 is
about the language; Layer 2 is about the models. Layer 1 alone is vulnerable to
"just define it"; Layer 2 alone is vulnerable to "you only tried two laws."

**Reading (i) is a category error. It is not what the obligation text asserts
(§4.4).**

### 4.3 Reading (ii) — axioms PLUS approved primitives PLUS landed theorems

**Foreclosed on the primitives half; vacuous on the theorems half.**

- *Primitives half.* All three registered primitives explicitly disclaim
  dynamics, source/action, and measure in their own source notes (§2.4), and
  `PRIMITIVE_REGISTRY_CHECK.md:13-16` forbids granting more than the source note
  declares. Adding the primitives to the axioms adds exactly nothing toward the
  conjunct. This is not an inference from silence — it is three explicit
  negative declarations plus a policy line forbidding the over-read.
- *Landed-theorems half.* No retained-grade row supplies matter-action content
  non-conditionally. The one retained-grade surface in the neighbourhood
  (`staggered_os0_supplied_action_…_2026-07-11`, `retained_bounded`) supplies
  the action as an explicit input. A `retained_bounded` row carries its own
  supplied inputs by definition; feeding one into the conjunct re-imports the
  supply the conjunct is trying to eliminate.

So reading (ii) is not *ill-posed* — it is **well-posed and, on the current
surface, empty**: it collapses onto reading (i) plus a certified-zero
increment.

### 4.4 Reading (iii) — derive up to a menu, then show the menu is a singleton

**This is the only well-posed reading, it is the one the obligation's own
authoritative surfaces support, and it is chartered by policy.**

- The registered target says "Derive **from the retained framework chain**"
  (`derivation_obligations.json`; `AC_…:11`) — not "from the four axioms."
- `AXIOM_MINIMALITY_POLICY.md:18-23` licenses closure "by derivation,
  identification, bounded composition, **or no-go boundary**", and `:48-49`
  licenses "no-go boundary notes that state what is structurally unclosable
  from the current axiom set."
- The audit lane's re-audit note (§4.1) asks for a derivation *that selects* —
  i.e. any construction sharp enough to decide the grain, of whatever menu size.
- Corpus usage already reads the criterion as two-part:
  `ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_…_2026-07-16.md:396` — "The grain
  derivation obligation's closure criterion is **two-part**".

Under reading (iii) the campaign has a definite deliverable: **state the menu,
name every framework-native condition that cuts it, and name the exact residual
datum that a point-selection would require.** §5 begins that at the most
constrained end.

### 4.5 Does the obligation as WRITTEN demand reading (i)?

**No — and this matters for (d).** `:21` says "must derive the physical matter
action and its measure"; it does **not** name a premise source. Read with `:11`
("from the retained framework chain") and with `AXIOM_MINIMALITY_POLICY:18-23`,
the criterion is a reading-(ii)/(iii) demand, not a reading-(i) demand. The
campaign brief's fear — that the obligation literally demands the impossible —
is **not** borne out by the text. The defect is a different and more specific
one.

---

## 5. Native exact algebra — the matter-law menu, rebuilt from primitives

Runner: `…/scratchpad/wave1_killcheck_runner.py`, **PASS=37 FAIL=0**, all
sympy-exact, no floats as inputs.

### 5.1 What is licensed as a constraint, and by which axiom clause

| Constraint | Axiom clause |
|---|---|
| edge-uniform, nearest-neighbor | Lattice, `:37-38` |
| invariant under translations and proper cubic rotations | Lattice `:37-38`; Admissibility `:57-58` |
| privileges no one-site possibility ⇒ commutes with the common one-site frame change `u ⊗ u` | Qubit, `:52-53` "No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone." (Skolem–Noether: `Aut(M_2(C)) = Inn`, so `u ∈ SU(2)` exhausts the frame group) |
| Hermitian, nonzero | the *additional* properties the 2026-07-10 theorem statement grants; not axiom content |

This is the same covariance test the landed note uses: "Because `SWAP` commutes
with every common one-site frame change `U ⊗ U`, the law privileges no one-site
possibility or Pauli axis"
(`STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md:202-206`).

### 5.2 Lemma (edge menu) — exact

> The real vector space of Hermitian operators `H` on `C² ⊗ C²` satisfying
> `[H, u ⊗ u] = 0` for every `u ∈ SU(2)` has **real dimension exactly 2**, and
> equals `span_R { I ⊗ I , SWAP }`.

Runner Block A solves the 16-real-parameter Hermitian ansatz against the three
diagonal generators `σ_a ⊗ I + I ⊗ σ_a` and returns exactly two free real
parameters (`d3`, `r_12`). Block B verifies `I` and `SWAP` both commute with
every generator, and solves the identification exactly:

```
a = d3 - r_12 ,   b = r_12          so   H = a·(I⊗I) + b·SWAP.
```

Also exact: `SWAP² = I`; `spec(SWAP) = {+1 (×3), −1 (×1)}`; both `I − SWAP` and
`I + SWAP` are positive semidefinite and nonzero.

### 5.3 The menu is a 2-point set, and the two points are physically distinct

The constant part `a·(I⊗I)` shifts every one-excitation energy by a common
constant (inert). Positive rescaling is a units choice. The surviving invariant
is `sign(b)`.

Runner Block C computes the one-excitation Bloch symbol on `Z³` exactly:

```
σ_b(k) = 2b ( cos k₁ + cos k₂ + cos k₃ − 3 ).
```

Block D evaluates it exactly at the two symmetric points:

| law | `σ(0)` | `σ(π,π,π)` | band minimum at |
|---|---|---|---|
| `b < 0`  (i.e. `Φ = I − SWAP`) | `0` | `+12` | `k = 0` |
| `b > 0`  (i.e. `Φ' = I + SWAP`) | `0` | `−12` | `k = (π,π,π)` |

and verifies that under **every** positive rescaling `s` and **every** constant
shift `c`, the separator `σ(corner) − σ(origin)` equals `+12s` and `−12s`
respectively — i.e. the sign difference is not absorbable by normalization or
by an energy offset.

**Both `I − SWAP` and `I + SWAP` satisfy every single property named in the
2026-07-10 theorem statement** — nonzero, Hermitian, number-conserving,
nearest-neighbor, translation-invariant, proper-cubic-invariant — and they
place the gapless point of the one-excitation band at opposite ends of the
Brillouin zone.

### 5.4 What this adds to the corpus (the delta, stated precisely)

- `…NONFORCING_NO_GO…2026-07-10.md` §5 proves *the staggered law is not
  selected*, using `Φ = I − SWAP` as the single witness. It leaves open — and
  its own §5 sentence "This no-go is about selection, not mathematical
  definability" does not address — whether the graph-Laplacian branch is itself
  forced.
- The result above closes that: within the licensed edge-wise class the
  axioms + all available symmetry demands leave **exactly two** inequivalent
  laws, and `I − SWAP` (the note's own witness) is only one of them.
- `…RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO…2026-07-04.md:112-116`
  explicitly says its witness "does not prove that two inequivalent matter
  actions or Gaussian measures exist". §5.2–5.3 supplies exactly that missing
  matter-law-level witness, natively.
- Prior-art sweep on this specific result (run before reporting it): `git grep`
  over `docs/` for `I - SWAP` / `I + SWAP` / qubit-exchange / diagonal-`SU(2)`
  commutant returns only `…NONFORCING…2026-07-10.md:197` (`I − SWAP` alone) and
  `HYPERCHARGE_IDENTIFICATION_NOTE.md:24-25` (`(I ± SWAP_23)/2` as
  symmetrizers on a different carrier). **`I + SWAP` as a competing matter law,
  and the dimension-2 commutant count, do not appear anywhere in the corpus.**

### 5.5 Rebuilt cited algebra + CONSTRUCTION-mutation probes

Block E rebuilds the 2026-07-10 note's cited identities natively and exactly:
`2Σ(1−cos k_μ) = 4Σ sin²(k_μ/2)`; corner values `= 4h` for Hamming weight
`h ∈ {0,1,2,3}`; zero set `= {k ≡ 0 mod 2π}` only.

Block F rebuilds the 2026-07-04 note's cited identity natively for a fully
symbolic complex `2×2`: `det_R R(A) = det_C(A)·conj(det_C(A)) = |det_C A|²`,
and the scale degrees `n` vs `2n`, `F_R = 2F_C`.

Block G mutates the **construction**, not the assertion:

| mutation | result |
|---|---|
| drop the no-privilege (frame-invariance) demand | dim jumps `2 → 16` |
| keep only the `σ_z` frame subgroup (privileges an axis) | dim `= 6` (`1+4+1`) |
| use `u ⊗ conj(u)` instead of `u ⊗ u` | dim `= 2`, but the basis is **not** `{I, SWAP}` |
| `d = 1,2,3,4` | corner value `= 4d = 4, 8, 12, 16` — the `12` tracks `d=3`, not hard-coded |
| `b = 0` | the two menu points coincide; separator vanishes |

The `σ_z`-subgroup probe **caught a wrong prediction of mine** (I predicted 8;
the exact answer is 6 = 1+4+1 from the `+2,0,0,−2` eigenspace split). Recorded
here rather than silently corrected.

### 5.6 Honest scope of §5 — what it does NOT show

- Scoped to **edge-wise two-site** laws. A genuinely six-neighbor joint local
  law, or a longer-range law, is outside the class; the menu there is larger,
  not smaller, so the non-singleton conclusion is not threatened, but the
  *count* 2 is class-specific.
- "Matter law" here is a local interaction, not a Euclidean action with a
  measure. Passing from a local interaction to an action-and-measure requires a
  temporal direction and a functional-integral measure, neither of which the
  axioms provide (`:168`, and `REALIZED_STATE_PRIMITIVE_NOTE:38,60-63`
  disclaiming "measure"). §5 therefore bounds the menu **from below** at the
  most-constrained end; it is not the full menu the campaign needs.
- It selects nothing, derives no `r`, `Q`, mass, phase, or grain, and changes no
  status.

---

## 6. (d) Is the obligation itself defective? — the governance finding

**Yes, but not in the way the campaign anticipated.** The obligation does not
demand reading (i) (§4.5). It is defective in a narrower, checkable way:
**its prose closure criterion over-reaches its own registered target and its own
named historical source.**

### 6.1 What the retired premise actually said

The obligation names one historical source (`:15-17`). That source's Historical
Candidate 1 reads, verbatim:

> For the AC_phi_lambda charged-lepton **matter-action surface**, the physical
> statistical grain is the K/CPT orbit or holomorphic-pair occupancy grain:
> the doublet contributes once per K/CPT orbit rather than once per sector or
> channel. **This premise supplies only the matter-action occupancy grain**
> needed to discharge the surviving AC(i) measure-side realization binary.
>
> — `docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md:39-45`

The retired premise **presupposed** a matter-action surface ("*For the …
matter-action surface*") and supplied **only** the grain on it. It never
supplied an action, so retiring it never created an obligation to derive one.

### 6.2 The mismatch, laid out

| Surface | Demands the grain? | Demands deriving the action+measure? |
|---|---|---|
| retired premise (`TIER_A…:39-45`) | supplies it as a premise | **no** — presupposes the surface |
| machine registry (`derivation_obligations.json`) | **yes** | **no** — clause absent |
| `AC_…OBLIGATION.md:11-13` "Exact target" | **yes** | **no** — clause absent |
| `AC_…OBLIGATION.md:21-24` "Closure criterion" | yes | **yes** |

A faithful replacement obligation demands exactly what the retired premise
supplied. This one's prose criterion demands strictly more, and the extra
demand appears in **no** other surface — including the registry that
`AXIOM_MINIMALITY_POLICY.md:82-92` designates as the tracking surface for exact
open work.

### 6.3 The sibling-obligation control

Both sibling obligations attach "derive" to the **target identity** and a
weaker verb to the **substrate carrier**:

- `AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md:21-24`: "must
  **provide** a physical carrier/source-action bridge … It must **derive** the
  density-to-angle equality".
- `THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md:23-25`:
  "must **construct** the quark mass/determinant carrier, **identify** the
  physical readout map, and **prove** the cross-sector correspondence".

Only `AC_ORBIT…:21` writes "must **derive** the physical matter action and its
measure" — attaching the strong verb to the substrate. Written in the sibling
register it would read "must **provide** a physical matter action and its
measure, then **derive** the count-once/count-twice distinction on it."

### 6.4 What is and is not implied

- This is a **prose-surface defect**, not an ill-posed obligation. Both readings
  of the criterion are formally answerable; they differ enormously in cost.
- **Nothing retained rides on it.** All 16 rows that depend on the obligation
  are `unaudited` or `meta`. The claim that "every matter-sector value in this
  framework sits behind this gate" over-states it: nothing in the AC lane is at
  retained grade at all, so no retained value currently sits behind it.
- The remedy is an **owner** decision about the prose, not a lane action.
  `AXIOM_MINIMALITY_POLICY.md:34-39` forbids resolving this by ruling:
  "ambiguity resolves by derivation or owner-approved axiom clarity, never by
  ruling." I record the discrepancy; I do not resolve it.

---

## 7. Correction to the campaign brief's factual premises

Both premises the campaign was opened on are contradicted by `origin/main`.

**(A) "The second conjunct is already discharged."** — Not supported. The three
most recent grain surfaces say the opposite, verbatim:

> This note does **not** engage EITHER part of that criterion. It does not
> derive the physical matter action or measure, and it does not identify its
> abstract 2-cell/3-cell menu arithmetic with the physical
> count-once/count-twice fork. … **No part of the obligation is weakened,
> localized, replaced, or discharged.**
>
> — `ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md:405-410`

> This note engages no part of that criterion. … **the obligation stands at its
> live grade.**
>
> — `ACPHILAMBDA_OCCUPANCY_GRAIN_SHARPENING_…_2026-07-16.md:443-448`

> It does not derive the physical action or its measure, and it **does not touch
> the closure criterion's "action and its measure" unknowns or narrow the grain
> obligation** — the criterion targets the physical matter action and measure,
> not this probe.
>
> — `KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:296-299`

Every one of these rows is `unaudited` in the ledger. The `r`-neutrality the
brief cites is real and is stated at
`CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md:129`
("`r` … remains a free dial") — but `r`-neutrality of a *coordinate theorem* is
not discharge of a conjunct.

**(B) "No wave of the previous campaign attempted the first conjunct."** — The
axiom-surface question was attacked twice already, on 2026-07-04
(`ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md:53-77`,
certifying that axioms + primitives do not supply the grain) and on 2026-07-10
(`…NONFORCING…2026-07-10.md` §5, an explicit model of all four axioms carrying a
different matter law). Both are route-level and both are `unaudited`, but the
ground is not virgin.

---

## 8. (e) VERDICT

**The campaign is WELL-POSED — under reading (iii) only — and should proceed
with a narrowed, corrected target.**

1. **Reading (i) is a category error** and should be struck from the campaign's
   option set. Not "hard": not expressible (§4.2 Layer 1), and not entailed even
   after granting the vocabulary (§4.2 Layer 2, witness in §5).
2. **Reading (ii) is well-posed and empty on the current surface.** All three
   registered primitives certify they supply no dynamics, no source/action, and
   no measure; `PRIMITIVE_REGISTRY_CHECK.md:13-16` forbids granting more. No
   retained-grade row supplies action content non-conditionally.
3. **Reading (iii) is the live target**, and it is what the obligation's
   registry entry, its `Exact target` section, and the audit lane's own
   re-audit instruction all support.
4. **No landed no-go forecloses any of this** — because *no no-go in this
   repository is at retained grade at all* (437 unaudited + 1
   audited_conditional + 0 retained).
5. **The obligation carries a real prose defect** (§6): its closure criterion
   demands *deriving* a substrate its own registered target and its own
   historical source *presuppose*. Owner-level, not lane-level.

### The well-posed replacement obligation

> **Registered target (unchanged):** derive from the retained framework chain
> whether the physical charged-lepton matter action counts the `K`/CPT orbit or
> holomorphic pair once rather than counting each sector or channel.
>
> **Closure criterion (repaired, in the sibling register):** A closing theorem
> must (1) **exhibit the admissible class** of physical matter actions and
> measures compatible with the four axioms, the approved primitives, and the
> retained chain — stating the class, not one member; (2) **name every
> framework-native condition it applies to cut that class** (proper-cubic
> covariance, reflection positivity, microcausality/Lieb-Robinson,
> record-compatibility, CAR/graded structure), each cited at its live ledger
> grade; and (3) **derive the count-once/count-twice distinction uniformly over
> the surviving class**, without inserting the desired charged-lepton value or
> readout dictionary. If the distinction is not uniform over the surviving
> class, the theorem must instead **name the exact residual datum** whose
> supply would cut the class to a point — and that datum is then the
> irreducible supply of the whole matter sector.

Clause (3) is the load-bearing repair: it makes the grain decidable *without*
first collapsing the action menu to a point, which is what the current prose
implicitly requires and what §5 shows cannot be done from the axioms. And it
makes a sharp negative — "the distinction is not uniform; here is the residual
datum" — a *closing* outcome rather than a failure, exactly as
`AXIOM_MINIMALITY_POLICY.md:18-23,48-49` already licenses.

### Recommended wave 2

Do **not** open a wave that tries to derive an action. Open one that computes
the menu properly: extend §5 from the two-site edge-wise class to (i) the full
six-neighbor local class, and (ii) the Euclidean action/measure level, where a
temporal direction and a functional-integral measure must be *supplied* and the
question becomes which supplied inputs are load-bearing for the grain. The
deliverable is the menu and the cut-list, not a selection.

---

## 9. Non-claims

This report selects no action, measure, grain, horn, `r`, `Q`, `delta`, mass,
mixing angle, phase, or sector weight. It adds no axiom, primitive, convention,
or vocabulary. It sets, predicts, and estimates no audit verdict, and grades no
row. It does not assert that any note is defective in its physics; the
2026-07-10 and 2026-07-04 notes are cited as prior art whose stated scope I
respect and whose declared gap I fill. Every status quoted is read from
`docs/audit/data/ledger/` shards on `origin/main`, never from note prose. No
file in the repository was modified except this report.
