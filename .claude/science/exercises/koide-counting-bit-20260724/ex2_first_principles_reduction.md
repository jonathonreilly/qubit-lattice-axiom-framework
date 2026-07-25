# EXERCISE TWO — first-principles reduction (weaken, delete, minimize)

Sector report. Wall: selection of `r = g_0/g_1` on the `C_3`-invariant
symmetric-form cone `diag(g_0, g_1, g_1)`.
Date: 2026-07-24. Base: `origin/main` @ `1652deb63b` (fetched).

**Nothing here is a repo claim, an audit verdict, or a proposed note.** No repo
file outside this report was created or edited. All algebra below was rebuilt
natively (exact sympy) rather than cited; the scratch runner is at
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/ex2_reduction_probe.py`
(**SCORECARD PASS=57 FAIL=0**, includes 5 construction-mutation probes).
It is scratch, deliberately not landed.

---

## 0. Framework refresher — surfaces actually read before any conclusion

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (Lattice / Qubit / Admissibility / Record,
  in full, including the Qualification and the Open-Gates list)
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`
- `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` (in full — this turned out
  to be load-bearing for the sector, see §7)
- `docs/audit/data/axiom_premise_nodes.json` (all four registered nodes and
  their notes)
- `docs/ai_methodology/skills/review-loop/SKILL.md`
- Wall-specific surfaces: `CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md`,
  `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md`,
  `FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md`,
  `KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`,
  `KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md`,
  `KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md`,
  `KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`,
  `RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`,
  `FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md`,
  `ACTION_NORMALIZATION_NOTE.md`, plus the live `docs/audit/data/audit_ledger.json`.

Per the exercise instruction, axioms and approved primitives are treated as
ASSUMPTIONS below, and existing repo content is fair game for correction.

---

## 1. Bottom line

Deleting everything deletable leaves **one positive real number and no set to
count it with**. Specifically:

> `r = (g_0/g_1) · (w_1/w_0)` — a product of a **metric ratio** and a **weight
> (mode-count) ratio** — and **only the product is physical**. The framework
> canonically fixes the first factor (`g_0/g_1 = 1/2`, the trace-induced
> Hilbert–Schmidt form). It supplies *nothing* that fixes the second. Every
> object so far tested against this wall — including all eight lenses and the
> new Frobenius–Schur census — is an invariant of the `C_3`-module, and
> **every module invariant is provably constant along a group `Γ` that sweeps
> `r` across `(0,∞)`.** That is a one-line theorem, not a survey, and it
> subsumes the entire reality-type class.

The corollary that matters: a selector cannot be an *invariant* at all. It must
be a single object that supplies the metric **and** the mode set at once — i.e.
a **measure with atoms** (an action, a Berezin/CAR generator set, or a
counting of framework-supplied records). Everything else is provably powerless.

The second finding is that **the repo's own registered foundation already says
`r` is not derivable** (§7), which puts the campaign's stated closure obligation
in direct tension with an owner-approved primitive registration. Resolving that
tension is cheaper and more decisive than any further selector hunt.

---

## 2. The deletion ladder — what survives each amputation

Each rung states what is removed and what remains. Gate labels refer to the
scratch runner.

| # | Deleted | Does the bit survive? | Gate |
|---|---|---|---|
| 1 | The charged-lepton masses / the Koide readout `Q` | **Yes.** `Q = 1/3 + (2/3)r` exactly, monotone in `r`; `Q` is a relabeling of `r`, carries no independent content. | B3 |
| 2 | The equal-sector locus (equipartition) | **Yes, and it clarifies.** Equipartition is not a fact but a *weighting rule*: `E_0/w_0 = E_1/w_1` with `E_0 = g_0a²`, `E_1 = g_1\|b\|²` gives `r = (g_0/g_1)(w_1/w_0)`. | B4 |
| 3 | The mass-ratio bridge entirely | **Yes.** What is left is: *the ratio of the two isotype weights of an invariant form on a representation.* No physics words remain. | A1, B4 |
| 4 | `C_3` → arbitrary finite group `G` | **Yes, and it generalizes.** On a real-irreducible `G`-module the invariant symmetric form is unique up to positive scale; so for a multiplicity-free module with `k` real-irreducible summands the invariant-form moduli is the positive orthant of dimension `k−1`. The Koide case is `k = 2`. The freedom is **Schur's lemma**, nothing more. | A1, E1–E3, E5 |
| 5 | Three generations → `N` | **Survives as freedom for all `N ≥ 2`; survives as a _bit_ only for `N = 3`.** See §3 — this is the sharpest deletion result. | D1–D7 |
| 6 | The `Z³` lattice, the sites, the record dynamics | **Yes.** The minimal carrier is `Z_2` acting on `R²` — one two-dimensional real space with two distinguishable one-dimensional sectors. Two isotypes, one free ratio. No lattice, no masses, no dynamics. | E4 |
| 7 | Down to a **single record** | **No — and that localizes the gap.** With one record there is no ratio at all; the Record axiom's additivity says nothing until there are **two disjoint records of distinguishable type**. The bit is exactly the smallest nontrivial datum of a finitely-additive readout: its value on two atoms. | (argument, §5) |

**Minimum object carrying the bit:** two inequivalent isotypes, one additive
readout, no supplied cross-isotype normalization. Everything else in the wall
statement — `C_3`, three generations, `Z³`, the mass operator, Koide — is
scaffolding.

Two rungs deserve explicit honesty flags:

- Rung 5 is a *question* deletion, not a framework deletion. `FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md`
  derives the generation triplet as `K_1 = {(1,0,0),(0,1,0),(0,0,1)}`, the three
  weight-1 translation characters on the `2×2×2` cell, cycled by `C_3[111]`. The
  count 3 is welded to `d = 3`, which is a Lattice primitive. So the framework
  cannot have two generations; but the *question* can be posed at `N = 2`, and
  its answer there is decisive (§3).
- Rung 6's `Z_2` model has the freedom but **not** the fork (§3). It is the
  minimal carrier of the modulus, not of the binary.

---

## 3. Minimality theorem: `Z_3` is the unique `N` with a *bit*

Computed directly (gates D1–D7, cross-checked against a brute linear solve for
`N = 3,4,5,6`):

| `N` | real isotypes | free ratios | 2-dim isotype present | HS point ∝ flat point |
|---|---|---|---|---|
| 2 | 2 | **1** | no | **yes — the two horns COINCIDE** |
| 3 | 2 | **1** | yes | no — horns distinct |
| 4 | 3 | 2 | yes | no |
| 5 | 3 | 2 | yes | no |
| 6 | 4 | 3 | yes | no |
| 7–9 | 4,5,5 | 3,4,4 | yes | no |

- **`N = 2`: the modulus survives, the bit does not.** Both isotypes are
  one-dimensional, so "count the block once" and "count its real dimensions"
  agree; `HS = diag(2,2) ∝ diag(1,1)` and both horns give `r = 1`. There is
  still a free ratio — but no second named point to choose against.
- **`N ≥ 4`: the bit dissolves into a multi-parameter family.** Two or more
  free ratios, only some of which carry a doubling ambiguity.
- **`N = 3` is the unique cyclic case with exactly one free ratio AND a genuine
  1-vs-2 doubling fork** (gate D6).

**Consequence — a correction of the wall's own framing.** The "counting bit"
description is a *presentational artifact of `N = 3`*. What is actually free is a
**continuum**, a positive real modulus; the framework contains no landed content
forcing `r ∈ {1/2, 1}`. The repo already holds both framings and they are in
tension: `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05` (a `positive_theorem`)
correctly says `r(s) = 2^{s−1}` is a one-parameter dial whose position "is not
fixed by Lattice, Quantum, or Record"; `CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05`
(a `meta` note) calls it "one binary counting-measure bit."

The bit framing is only correct **if the weights are cardinalities of finite
sets** — integrality is the hidden premise that collapses the continuum to a
binary, and it is nowhere derived. Even a successful "derive the horn" theorem
would still owe a proof that `r ∉ (0,∞) \ {1/2, 1}`.

Corroborating arithmetic: the horn pair is not even closed under the
redundancy of §4. Flat metric + dimension weights gives `r = 2` (gate B5d), a
third value that no landed surface names.

---

## 4. The gauge-product reformulation, and why every lens failed

Rebuilt exactly (gates A1, B1–B6):

- The `C_3`-invariant symmetric forms on the coefficient space `(a, Re b, Im b)`
  are **exactly** `diag(g_0, g_1, g_1)` — 2 parameters (A1, A1b). Adding the
  `K`-conjugation reflection changes nothing (A2). Mutation probes: with no
  group the form space is 6-dimensional (A4); with a transposition instead of
  the 3-cycle it is 4-dimensional (A5). The gates are not vacuous.
- `Tr(H†H) = 3a² + 6x² + 6y²` — the HS point `diag(3,6,6)` (B1).
- `Q = Tr(H²)/(Tr H)² = 1/3 + (2/3)r` (B3).
- **`r = (g_0/g_1)·(w_1/w_0)`** (B4), and `(g_0/g_1, w_1/w_0) → (t·, t^{-1}·)`
  leaves `r` invariant (B6).

So the disputed datum has a **one-parameter redundancy**: it can be moved
freely between "the metric" and "the partition/mode count", and only the
product is physical. The four cells:

| metric | weights | `r` | name |
|---|---|---|---|
| HS `(3,6)` | block `(1,1)` | **1/2** | Koide horn |
| HS `(3,6)` | dimension `(1,2)` | **1** | default horn |
| flat `(1,1)` | block `(1,1)` | **1** | same as above, re-gauged |
| flat `(1,1)` | dimension `(1,2)` | **2** | unnamed third value |

**This diagnoses every prior failure at once.** Each tested lens fixed one
gauge-dependent *factor* and left the compensating factor free. It also shows
the wall statement's own presentation ("HS point `diag(3,6,6)` vs flat point
`diag(1,1,1)`") silently absorbs the partition choice into the metric; the
landed `FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02` derives *both* horns
from the *same* `diag(3,6,6)` by changing which partition is equipartitioned.
Both presentations are correct; conflating them is how "the metric is canonical
⇒ `r = 1/2`" becomes a trap.

**The sharpening this buys.** The metric factor *is* framework-canonical:
`g_0/g_1 = 1/2`, being the HS form induced by the trace on `End(V)`
(gate B1; landed independently as the coherent-state field-space metric). So
after gauge-fixing, the **entire residual is the single integer-or-not
`w_1/w_0`** — literally "is the doublet one thing or two things?" — and

```
r = (1/2) · (w_1 / w_0).
```

Deleted all the way down, the residual is the **conjugation-orbit question**
(gates F1–F6): the characters of `Z_3` are `{1, ω, ω̄}`; conjugation has orbits
`{1}` and `{ω, ω̄}`.

- counting measure on **characters** → `w = (1,2)` → `r = 1`;
- counting measure on **conjugation orbits** → `w = (1,1)` → `r = 1/2`;
- the two horns differ by *exactly* the orbit size `|{ω, ω̄}| = 2` (F6).

And this is precisely why `Z_2` has no bit: there, conjugation is trivial, so
the two counting measures coincide (F2). For `Z_5` there are two doubled orbits
and the single bit becomes two independent bits (F3). The structure of §3 is
explained, not merely tabulated.

---

## 5. The `Γ`-invariance theorem: a complete candidate list, not a survey

**Setup.** Let `W ≅ R³` be the coefficient space with its `Ẑ_3` action
(conjugation by `D = diag(1,ω,ω²)`, i.e. `b ↦ ωb`). Let

```
Γ = { T_{λ,μ} = diag(λ, μ, μ) : λ, μ > 0 }.
```

**Gated facts.** `T_{λ,μ}` commutes with the group action (C1) and with the
`K`-conjugation reflection (C1b); it pulls `diag(g_0,g_1,g_1)` back to
`diag(λ²g_0, μ²g_1, μ²g_1)` (C2); hence the metric ratio transforms as
`γ ↦ (λ/μ)²γ`, so **`Γ` acts transitively on `r ∈ (0,∞)`** (C3).

**Theorem (one line).** `Γ ⊆ Aut_{Ẑ_3}(W)`. Therefore any structure `S` that is a
function of the module `(W, Ẑ_3)` — or of the carrier module `(V, C_3)`, which
`Γ` does not touch at all — up to isomorphism satisfies `S(g) = S(Γ·g)`.
A transitive coordinate cannot be a non-constant function of an invariant. **∎**

**What this kills, by proof rather than by testing:** characters, all
Frobenius–Schur indicators, real/complex/quaternionic type, orientation classes,
isotype dimensions and multiplicities, `End_G` as an algebra, `K`/CPT real
structures, Schur indices, and any equivariant class of the module. This
*includes* the campaign's 95-gate FS census as a corollary and generalizes it
from `C_3` to every finite group and from FS to every module invariant.

**What it leaves.** A consistency audit of seven concrete structures (C4, C5):

| structure | `Γ`-invariant? |
|---|---|
| `C_3` action matrices | invariant |
| isotype projectors | invariant |
| doublet complex structure `J` | invariant |
| `K`-conjugation (real structure) | invariant |
| HS metric `diag(3,6,6)` | **NOT** invariant |
| trace functional `Tr H = 3a` | **NOT** invariant |
| operator product (algebra structure) | **NOT** invariant |

The three non-invariant entries are **all consequences of one object**: the
associative algebra `End(V)` with its canonical trace. And that object supplies
only the *metric* factor of §4. Independently gated: the `SO(2)` flow generated
by the doublet complex structure preserves the HS metric exactly (F7) and is
itself `Γ`-invariant (F7b) — mutation probe F8 confirms a singlet–doublet-mixing
rotation *does* move the metric, so F7 is non-vacuous. So the one module-level
object that could plausibly convert "2 real directions" into "1 complex mode" is
doubly disqualified.

**Corollary — the shape any selector must have.** The two factors of
`r = (g_0/g_1)(w_1/w_0)` are sourced by structures of opposite potency: the
metric by a `Γ`-breaking algebra object, the mode count by `Γ`-invariant module
data. Hence **`r` is free unless a single framework object supplies both
factors at once.** The only kinds of object that do are objects with *atoms*: a
Gaussian/Berezin measure (whose integration variables are the mode set and whose
covariance is the metric), or a counting measure on a framework-supplied finite
set. This derives — rather than intuits — why the action/CAR route is the right
shape, and why `KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04` has
to carry `POLARIZATION-SELECT` as a *named conditional premise*: choosing the
polarization **is** choosing `w_1`.

---

## 6. Where the gap actually lives (localization)

Rung 7 of the ladder localizes the missing structure precisely. The Record
axiom states: *"For any finite collection of pairwise-disjoint records, scalar
readout `I` is additive, with `I(∅)=0."* Additivity determines `I` on unions
given its values on atoms, and **says nothing about the relative normalization
of `I` across atoms of different type**. The counting bit *is* that silence —
not a hidden gap but the declared one, and the deletion shows nothing else in
the framework is involved.

This yields a clean well-posedness criterion, which I state as the sector's
named obligation:

> **(MODE-COUNT-IS-A-CARDINALITY.)** `w_1/w_0` is a *bit* if and only if the two
> isotype weights are cardinalities of framework-supplied finite sets of atoms;
> otherwise `w_1/w_0` is a free positive real and the binary framing is
> unfounded. The decisive question is therefore **not "which of 1/2 and 1", but
> "does the framework supply a finite SET whose cardinality is the isotype
> weight?"**

That is a decidable obligation: exhibit the set, or prove none exists. It is not
a reality-type invariant, it is not the multiplicative/`AC_φλ` bridge, it is not
the δ-pattern leg, and it is not a chirality argument. The one axiom-native
candidate for such a set is the **Admissibility** rule's per-site available-
possibility set — Admissibility is the only axiom that supplies finite sets that
*vary*, and Record's additivity is the only axiom-level object that turns a set
into a weight.

Note carefully what this would imply if the count turned out rule-dependent:
Admissibility asserts *"there is one fixed nearest-neighbor admissibility rule"*
but does **not** say which. If `w_1/w_0` depends on the rule, then `r` is neither
derivable-now nor free — it is **downstream of the admissibility-rule
identification gate**, a reclassification of the whole Koide value question.
That is a publishable structural outcome in its own right.

---

## 7. Findings against existing repo content

The exercise permits finding landed content wrong, overbroad, or misframed. Four
findings, in decreasing order of consequence.

**(F-1) The registered foundation already classifies `r` as non-derivable — this
contradicts the campaign's stated closure obligation.**
`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`, the owner-approved source
note for the registered `realized_state_primitive`, carries in its
State-Contingency Register, item 4:

> *"Per-sector registered weight patterns (e.g. the charged-lepton block weight
> `r`) — registered patterns of the realized state, matched like the masses …
> dial settings (`r = 0, 1/2, 1`) are sector data, never forced."*

and its policing clause is: *"A value that would change under a different
law-admissible realized state is registered data, not derivation output."*
`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05`
independently states, under its within-sector-free guardrail, that *"the Koide
block-weight `r` is explicitly not delivered."*

Against this, the wall statement says *"a closing theorem must DERIVE the
selection, not adopt it."* Both cannot stand. Either the register entry is
overbroad and should be corrected (which would unblock the lane), or the
campaign target is already answered negatively by registered foundation content
and the honest deliverable is the no-go. **This is a live, cheap, decisive
fork that appears never to have been adjudicated.** (Caveat, stated honestly:
the Register is explicitly "documentation, not an additional gate", so it is a
classification, not a theorem — but it sits on a registered foundation surface
and it is policed by a test that has apparently never been applied to `r`.)

**(F-2) The "one counting bit" framing is a continuum wearing a binary's
clothes** — see §3. The honest object is a one-parameter modulus; integrality of
the weight is an undischarged hidden premise; and the named horn pair is not
closed under the §4 redundancy (a third value `r = 2` is reachable, gate B5d).

**(F-3) The foreclosure structure is described as retained but is `unaudited`
on the live ledger.** Queried from `docs/audit/data/audit_ledger.json` at
`origin/main`:

| row | claim_type | audit_status | effective_status |
|---|---|---|---|
| `koide_circulant_q_two_thirds_algebraic…` | positive_theorem | audited_clean | **retained** |
| `flavor_doublet_metric_default_is_detr…` | bounded_theorem | audited_clean | **retained_bounded** |
| `flavor_r_half_is_a_stationary_point_not_forced…` | bounded_theorem | audited_clean | **retained_bounded** |
| `koide_frobenius_isotype_split_uniqueness…` | no_go | unaudited | unaudited |
| `koide_r_half_polarization_selector…` (the 8-lens no-go) | no_go | unaudited | unaudited |
| `koide_real_rep_block_count_permitted_not_forced…` | no_go | unaudited | unaudited |
| `action_normalization_note` | no_go | unaudited | unaudited |
| `koide_kahler_dirac_realization_gives_r_one…` | no_go | unaudited | unaudited |
| `koide_lightcone_primitive_theorem…` | positive_theorem | unaudited | unaudited |
| `generation_weight_dial_structure…` | positive_theorem | unaudited | unaudited |
| `koide_berezin_detc_vs_detr_fork_mechanism…` | bounded_theorem | unaudited | unaudited |

`CHARGED_LEPTON_VALUE…COUNTING_BIT…:72` calls `koide_frobenius_isotype_split_uniqueness`
`retained_no_go` (already flagged by the campaign) and
`KOIDE_REAL_REP_BLOCK_COUNT…` calls it and `ACTION_NORMALIZATION_NOTE` "two
retained no-go rows". **Only three rows in the whole lane are retained-grade,
and none of them is a no-go.** The wall's own foreclosure scaffolding is
source-note assertion, not ratified status. This does not license re-walking the
foreclosed routes; it does mean the lane's negative claims have not been
independently stress-tested.

**(F-4) A phase-conditionality in the `Q` identification.** `Q = Tr(H²)/(Tr H)²`
is exact and phase-independent, but its reading as Koide's `Σm/(Σ√m)²` needs all
eigenvalues of one sign. At `r = 1/2` with `arg b = 0` the spectrum is
`(2.414, 0.293, 0.293)` — all positive (B7a); at `arg b = π` it is
`(−0.414, 1.707, 1.707)` — one negative (B7b). So the identification holds only
on a phase-restricted arc at the Koide horn. The repo knows the signed-`√m`
issue in general terms; I did not find it stated as an explicit domain
condition on the `Q` identity. Minor, but it is a real premise.

---

## 8. Fastest falsifying artifacts (ranked; each with object, tool, first build)

### FALSIFIER-1 (highest value / lowest cost) — apply the registered counterfactual test to `r`

- **Concrete object:** the law-admissible realized-state family of the
  generation sector, and `r = |b|²/a²` evaluated on it.
- **Tool:** the `realized_state_primitive`'s own policing clause — *"A value that
  would change under a different law-admissible realized state is registered
  data, not derivation output."* Registered, owner-approved, not a new premise.
- **First artifact:** a runner that **exhibits two law-admissible realized states
  of the generation sector with different `r`**. Two witnesses suffice; a full
  family sweep is the strong version.
- **Decisiveness:** total, and *both* outcomes are valuable.
  - `r` varies over the family ⇒ `r` is registered data **by registered repo
    policy**; the campaign's closure target is unachievable-as-stated, and the
    honest deliverable is that statement plus the no-go. This is the publishable
    negative the exercise explicitly welcomes.
  - `r` is invariant over the whole law-admissible family ⇒ Register item 4 is
    **wrong**, `r` is a legitimate derivation target, and correcting the registry
    unblocks the entire lane. That is a one-page, high-leverage correction.
- **Cost:** an afternoon for the two-witness version.
- **Why nobody has done it:** the test lives on the primitive-registry surface,
  not on the Koide lane's surface, and the lane has been hunting selectors rather
  than auditing its own classification.

### FALSIFIER-2 — the `Γ`-invariance census (settles "is it already fixed and everyone missed it?")

- **Concrete object:** a declared census `S` of every structure the framework
  fixes on the generation sector — the `C_3` action, isotype projectors, `J_cs`,
  `K`/CPT `Θ`, the circulant algebra, the trace, the induced HS metric, the
  eigenvalue map, the `Q` functional, the coherent-state field-space metric, the
  Berezin/Grassmann generator set, the Record readout `I`.
- **Tool:** the §5 theorem plus mechanical `Γ`-invariance testing.
- **First artifact:** extend the scratch runner's Block C from 7 structures to the
  full census, with the theorem's one-line proof as the general clause and the
  mechanical check as the per-item audit. Include mutation probes on each item.
- **Output — and this is why it is decisive rather than another survey:** the
  result cannot be "0 of `n` lenses survived, maybe an `n+1`-th exists". It is
  either (i) *every* census member is `Γ`-invariant ⇒ `r` is free relative to `S`,
  with the **completeness of `S` as the explicit, falsifiable hypothesis; or (ii)
  a finite explicit list of `Γ`-breaking members — the complete candidate-selector
  list**. From Block C I already know (ii) is the outcome and the list reduces to
  one object (algebra + trace), which fixes only the metric factor.
- **Cost:** one to two days.

### FALSIFIER-3 — the cardinality test (the only constructive closure route left)

- **Concrete object:** for the landed/candidate admissibility rule class, the
  finite set of available one-site possibilities, graded by `C_3`-isotype content;
  `n_0`, `n_1` its singlet/doublet cardinalities.
- **Tool:** Record's finite additivity (a counting measure on atoms is the unique
  additive extension), with `w_1/w_0 = n_1/n_0` and `r = (1/2)(n_1/n_0)`.
- **First artifact:** a runner that enumerates the available-possibility set for
  an explicit admissibility rule on the `2×2×2` cell (the carrier is already
  landed as `K_1 = {(1,0,0),(0,1,0),(0,0,1)}`), computes its isotype grading, and
  reports `n_1/n_0`.
- **Four decisive outcomes:** `n_1/n_0 = 1` uniformly ⇒ `r = 1/2` **derived**
  (Koide closed); `= 2` uniformly ⇒ `r = 1` **derived** (Koide closed *against*);
  rule-dependent ⇒ `r` reclassified as downstream of the admissibility-rule
  identification gate; available-set not `C_3`-graded ⇒ Admissibility is powerless
  too and the §5 no-go stands with one more census member discharged.
- **Cost:** days, and it is the only route of the right *shape* per §5 that has
  not been walked. It is not the CAR/Berezin route (which Wave 1 showed hands you
  the polarization at declaration time); it is the counting route.

### Also worth one hour: the third-value check

Verify (already gated, B5d) that `r = 2` is reachable within the four
metric×weight cells and that no landed content excludes `r ∉ {1/2, 1}`. If
confirmed against the full lane, the "bit" language should be demoted to
"modulus" everywhere it appears — a pure-hygiene fix with real downstream value,
because a bit invites horn-picking and a modulus does not.

---

## 9. Specification: what "provably free" must mean here

The sector brief asks for this precisely. My proposed definition, in the form
that makes it buildable:

> **Definition (`Γ̂`-freeness).** Let `S` be a declared census of the structures
> the framework fixes on the generation sector, and let `M ≅ (0,∞)` be the
> moduli of admissible weight structures, coordinatized by `r`. Then `r` is
> **provably free** if there is a group `Γ̂` acting on `(S, M)` with:
> - **(F1)** `Γ̂` acts transitively on `M`;
> - **(F2)** every member of `S` is `Γ̂`-invariant;
> - **(F3)** the axioms and approved primitives are `Γ̂`-covariant — true at
>   `(S, g)` iff true at `(S, γ·g)`.
>
> Then no framework-definable function equals `r`: such a function would be
> `Γ̂`-invariant while equalling a `Γ̂`-transitive coordinate.

This is a symmetry ⇒ non-determination argument of exactly the kind used to show
a gauge quantity is unphysical. Three properties recommend it:

1. **It is decisive.** Unlike a lens survey, it cannot leave "maybe the next lens
   works" open — the theorem quantifies over all functions of `S`.
2. **Its load-bearing hypothesis is exactly the right one and is falsifiable.**
   The only soft spot is completeness of `S`; and *falsifying completeness means
   exhibiting a new framework structure*, which is precisely a closure route.
   The no-go therefore names its own escape hatch rather than foreclosing
   investigation. (This matters for the N1–N8 discipline the repo applies to
   negative claims: an under-tested no-go here would be worse than none.)
3. **Half of it is already proven.** §5 supplies `Γ` and (F1); the module-invariant
   theorem supplies (F2) for the entire module-level part of `S`; and the residual
   is the explicit finite list `{algebra, trace, HS metric}`, which fixes only the
   first of the two gauge factors.

The honest current status of the target: **`r` is proven free of every module-level
structure, and free of the algebra/trace for its second factor. What remains for
a full no-go is (F2) for measure-bearing structures** — i.e. exactly Falsifier-3's
question, and exactly Falsifier-1's question in state-contingent form.

---

## 10. Honest boundary — what this sector did NOT establish

- I did **not** derive `r`. No horn was adopted, and no fit to lepton masses was
  performed or consulted.
- I did **not** prove `r` is underivable. §5 proves it is not a module invariant;
  the measure-bearing part of the census is untested, and that is where a genuine
  selector could still live.
- The `Γ`-theorem is about the **generation sector as presented** (the `C_3`
  circulant carrier). A construction that changes the carrier — an off-circulant
  or first-order fermionic realization — is outside its scope, exactly as the
  8-lens no-go's own N7 steelman anticipates.
- Finding **(F-1)** is a reading of registered-surface text plus a live ledger
  query. It is a *tension* I am reporting, not an adjudication; adjudicating it is
  the owner's call, and Falsifier-1 is the computation that would settle it.
- Nothing here proposes new repo vocabulary. "Gauge product", "`Γ`-freeness", and
  "cardinality test" are descriptions in this report only; if any of this were
  ever landed it would need native repo naming per `CONTROLLED_VOCABULARY`.

---

## 11. Verification appendix

Scratch runner (not landed, exact sympy + one mpmath spectrum check):
`ex2_reduction_probe.py` in the scratchpad path given at the top.
**SCORECARD PASS=57 FAIL=0.**

Blocks: **A** invariant-form cone on the coefficient space and on the carrier,
with two construction-mutation probes (no group → 6 params; transposition → 4
params). **B** HS form `diag(3,6,6)`, `Tr H = 3a`, `Q = 1/3 + (2/3)r`, the
equal-sector solve giving `r = (g_0/g_1)(w_1/w_0)`, the four metric×weight cells
including the unnamed `r = 2`, the redundancy identity, and the eigenvalue-sign
phase check at `r = 1/2`. **C** `Γ ⊂` commutant, pullback law, transitivity, the
seven-structure invariance audit, and the non-invariant list. **D** the `Z_N`
sweep with a brute-force cross-check at `N = 3,4,5,6` and the `Z_3` minimality
gate. **E** general finite groups (`S_3` on `R³`, `S_4` on `R⁴`, Klein four-group
regular, `Z_2` on `R²` as the minimal carrier, and an irreducible module as a
zero-freedom mutation probe). **F** characters vs conjugation-orbits, the two
counting measures, the orbit-size factor 2, the `SO(2)`-flow metric preservation
and its non-vacuity probe.

Per campaign rule 3, every claimed constancy above is gated by a
construction-mutation probe, not by an assertion probe: A4, A5, E5, F8, and the
`N`-sweep cross-check D7 are the mutations. Per rule 4, this section was written
from the runner output, not from intent.
