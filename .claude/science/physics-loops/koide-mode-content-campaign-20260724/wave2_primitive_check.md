# Wave 2 — primitive check: does approved foundation content already close the counting bit?

**Role:** adjudicate a possible campaign-ending finding about approved
foundation content. Exercise sector 2 reported that the registered
`realized_state_primitive`'s own State-Contingency Register, item 4, already
declares that "dial settings (`r = 0, 1/2, 1`) are sector data, never forced",
which — if accurate and in force — would contradict the campaign closure
obligation and answer the target negatively from owner-approved content.

**Baseline.** All quotations below are from `origin/main`
(`62826882ac`, fetched at session start). The worktree's `docs/` and
`docs/audit/data/ledger/` are **behind** `origin/main` (886 and 862 files
respectively), so every read was taken from a clean `git archive origin/main`
extraction. The five files I quote directly were byte-verified identical
between worktree and `origin/main` by md5:
`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`,
`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`,
`ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`,
`MINIMAL_AXIOMS_2026-06-29.md`,
`GENERATION_KOIDE_SINGLE_MODULUS_REDUCTION_2026-06-05.md`.

**Hard-rule compliance.** No commits, pushes, or PRs. Only this file written in
the repo. No audit verdict is set or predicted anywhere below — where a verdict
appears it is a *report of an already-landed ledger row*. No new axiom, no new
vocabulary. The one load-bearing algebraic step is rebuilt exactly in sympy
(section 0), with a construction-mutation probe.

**Framework refresher surfaces read (mandatory, all at `origin/main`):**
`docs/MINIMAL_AXIOMS_2026-06-29.md` (full);
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (full);
`docs/audit/data/axiom_premise_nodes.json` (full `realized_state_primitive`
node + registry description);
`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` (full — the source note of
the invoked primitive);
`docs/RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`
(full — the canonical statement item 4 defers to);
`docs/audit/AXIOM_MINIMALITY_POLICY.md` §6 including the 2026-06-11
realized-state approval entry;
`docs/audit/scripts/check_axiom_premise_clean.py` (the structural guard);
`docs/audit/data/derivation_obligations.json`;
`docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`;
`docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md`.

---

## 0. The one load-bearing identity, rebuilt natively

Everything in this adjudication turns on one factual bridge: **the `r` named in
item 4 is the campaign's `r`.** That is not a matter of interpretation, so I
rebuilt it exactly rather than citing it.

Source of the dial, `docs/GENERATION_KOIDE_SINGLE_MODULUS_REDUCTION_2026-06-05.md:19-28`:

> `Y` carries two real parameters — the modulus `r = |b|^2/a^2` and the phase
> `theta = arg(b)` — and the Koide ratio `Q = 1/3 + (2/3) r` depends on `r`
> **alone** … a single real modulus `r` on a derived axis with three
> distinguished settings `r = 0, 1/2, 1` (`Q = 1/3, 2/3, 1`).

Runner: `identity_gate.py` (scratchpad; exact sympy, `Rational`/`Integer`
inputs only, no floats). Displayed algebra:

```
dial map            Q(r) = 1/3 + (2/3) r
  Q(0)   = 1/3 + 0        = 1/3
  Q(1/2) = 1/3 + 1/3      = 2/3        <- Koide
  Q(1)   = 1/3 + 2/3      = 1
inverse             r = (3Q - 1)/2 ,      dQ/dr = 2/3 != 0   (bijective, monotone)
Koide solve         solve(1/3 + (2/3) r = 2/3, r) = [1/2]     (unique)
modulus             r = |b|^2 / a^2
HS block energies   E_+ = 3 a^2 ,  E_perp = 6 |b|^2
  equal energy      3 a^2 = 6 |b|^2  =>  |b|^2/a^2 = 1/2  =>  r = 1/2  =>  Q = 2/3
```

Construction-mutation probe (not an assertion probe): mutating the dial slope
`2/3 -> 1/3` breaks `r = 1/2 -> Q = 2/3`; mutating the block energy
`6|b|^2 -> 3|b|^2` moves the equal-energy point from `r = 1/2` to `r = 1`, i.e.
to the *other* horn. So the gates read the `3:6` structure rather than passing
vacuously.

`runner_check_breakdown = {A: 14, B: 0, C: 0, D: 0, total_pass: 14}` — **14/14 PASS.**

**Conclusion of section 0.** Item 4's `r`-list `{0, 1/2, 1}` is exactly the
campaign's dial: `r = 1/2` is the Koide horn `Q = 2/3`, `r = 1` is the
non-Koide horn `Q = 1`. Ex2's identification of the symbol is **correct**. The
question is therefore genuinely about the campaign's target and cannot be
dismissed on a symbol mismatch.

---

## (a) Item 4, verbatim, with scope-fixing surroundings

File: `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` (110 lines total).

**The section header — `:71`:**

```
71  ## Informative State-Contingency Register
```

**The register's own governing scope clause — `:73-77`:**

```
73  The register records current examples of realized-state data already separated
74  from derivation output. It is documentation, not an additional gate: the
75  primitive is policed by the counterfactual test above. (Statuses are
76  pipeline-derived and set by the independent audit lane; paths below are source
77  notes, not status claims.)
```

**Item 4 itself, verbatim — `:88-93`:**

```
88  4. **Per-sector registered weight patterns** (e.g. the charged-lepton block
89     weight `r`) — registered patterns of the realized state, matched like the
90     masses; canonical statement in
91     `docs/RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`
92     (guardrail G3). This primitive is the registry-level home of that
93     discipline: dial settings (`r = 0, 1/2, 1`) are sector data, never forced.
```

**The operative test the register defers to — `:43-45`:**

```
43  A row may evaluate an already-defined state functional at the supplied
44  realized state. A value that would change under a different law-admissible
45  realized state is registered data, not derivation output.
```

### Verdict on the paraphrase

**The quoted clause is CONFIRMED verbatim.** `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md:93`
contains, character for character, `dial settings (`r = 0, 1/2, 1`) are sector
data, never forced`. Ex2 did not invent or embellish it, and section 0 confirms
the `r` is the campaign's `r`.

**The paraphrase is nonetheless MATERIALLY INCOMPLETE in the one respect that
decides the campaign.** Ex2 reported it as an item of "the State-Contingency
Register". The register's actual name is the **Informative** State-Contingency
Register (`:71`), and its own first two sentences (`:73-74`) say it "records
current examples" and "is documentation, **not an additional gate**". Dropping
the word "Informative" and the not-a-gate clause converts a documented snapshot
into an apparent rule. That is the entire distinction the task asks me to
adjudicate, and it is resolved against the strong reading by the note's own
text.

---

## (b) What item 4 does and does not settle

**It settles:** that the realized-state primitive, and the corpus practice it
documents, currently treat `r` as supplied sector data on the same footing as
the measured masses — not as something the primitive hands you.

**It does NOT settle:** that `r` is underivable in principle. Six independent
grounds, each textual and each from approved or governing content.

### (b1) The register disclaims gate status in its own words

`:74` — "It is documentation, **not an additional gate**: the primitive is
policed by the counterfactual test above." The authority is the *test* at
`:43-45`; the register is a list of the test's current outputs. `:73` —
"**current** examples". A snapshot of what is presently classified as
registered data is not a proof that the classification can never change.

`:76-77` even disclaims the register's own entries as status carriers: "paths
below are source notes, **not status claims**."

### (b2) The counterfactual test is a classifier whose antecedent is a fact about `r`, not an axiom about `r`

The test (`:44-45`, and the registry restatement "a quoted number must be
invariant over the law-admissible family, else it is registered data"):

```
IF  a value would change under a different law-admissible realized state
THEN it is registered data, not derivation output
```

Contrapositive: **a value invariant over the law-admissible family is
derivation output, not registered data.** The primitive supplies the *test*.
Whether `r` satisfies the antecedent is a substantive fact that has to be
established by physics. Item 4 asserts the classification; it does not prove
the antecedent, and the note supplies no argument that `r` varies over the
law-admissible family.

Direction of entailment therefore runs the opposite way from the campaign-ending
reading: a theorem deriving `r` invariantly from the matter action would
**falsify item 4's entry** and require the register to be updated. The register
is downstream of the science, not upstream of it. A campaign cannot be stopped
by a document that its success would edit.

### (b3) "Never forced" is a corpus idiom meaning "not forced by the named supplied structure"

The sibling notes using the same construction make the idiom explicit.
`docs/KOIDE_REALITY_TYPE_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md:15-16`:

> Reality of the operator matrix `D` is necessary background for the real/Jcs
> face, but it **is not sufficient to select that face**.

That is a non-supply statement about one named structure, not a claim of
in-principle underivability. Read in place at `:92-93`, item 4's "never forced"
is scoped by its own antecedent — "**This primitive** is the registry-level home
of that discipline" — i.e. not forced *by this primitive*.

### (b4) The canonical statement item 4 defers to says the opposite of foreclosure — and is itself unaudited

Item 4 routes its authority to
`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`
"(guardrail G3)". Two findings.

First, **the label `G3` does not exist in that note.** Its guardrails are named,
not numbered (`:80`, `:84`, `:90`, `:94`): Decomposition-input, Named-predicate,
Within-sector-free, No-dynamics. Counting positionally, the third is the
Within-sector-free guardrail, which is the one naming `r`, so the citation
resolves — but by position only, and the target text is:

`:90-93` —
> **Within-sector-free guardrail.** Weights/measures inside a sector (e.g. the
> Koide block-weight `r`, the solar/`theta_13` angles) are *not* the record's
> content. **The principle gives the partition-level structure only**;
> conflating it with within-sector data is an overreach.

Scoped to *the principle*. And the recipe step it enforces contains an explicit
carve-out, `:72-73`:

> **Declare within-sector observables free/matched** (step 3 of the principle),
> not derived — **unless a separate pre-record argument supplies them**.

That clause is decisive: the guardrail item 4 leans on **explicitly contemplates
a separate argument deriving `r`**. It reserves the route the campaign is
taking. Likewise `:124-125`: "The Koide block-weight `r` is explicitly *not*
delivered (within-sector-free guardrail)" — *not delivered by this*, not
underivable.

Second, that canonical statement is a **proposal, not adopted content**. `:5-9`:

> **Status:** unaudited candidate. This note *proposes* a canonical reading of
> the RECORD axiom … adoption is decided by the independent audit lane, not
> self-declared here.

and `:146`: "effective status remains `unaudited` until then." Live ledger
confirms `record_outcome_observable_principle_canonical_proposal_note_2026-06-05`
= `meta` / `audit_status: unaudited`. So the "never forced" language traces to
an **unaudited proposal**, reached through a citation label that does not exist
in the target. That is not a load-bearing foreclosure chain.

### (b5) Reading item 4 as binding is precisely the laundering the repo's structural guard exists to prevent

`docs/audit/scripts/check_axiom_premise_clean.py:4-11` (docstring):

> An axiom/approved-primitive premise node … is granted an auditor carve-out:
> citing it does not, by itself, block a clean verdict … That carve-out is only
> safe while the source doc contains pure approved-premise content. **If a
> framework-rule / ratification clause is ever introduced into one of these
> docs, the carve-out becomes a laundering path: any rule dropped into the
> premise doc could then be "cleanly derived" by citing the premise.**

Treating a sentence inside the primitive note as a rule that forecloses a
physics question is exactly the failure mode the guard tripwires. The repo's
architecture is explicit that framework rules must **not** be readable out of a
premise doc. I ran the guard: it reports
`OK realized_state_primitive (docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md): pure premise content`
— i.e. the note currently passes *because* it carries no such rule.

### (b6) `PRIMITIVE_REGISTRY_CHECK` binds registry entries as non-supply, with derivation expressly reserved

`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md:5` (how entries bind):

> Do not grant more than the primitive source note declares. Any dimensionless
> quantity, selector, weighting rule, normalization rule, probability rule,
> readout bridge, dynamics, source/action, or empirical match remains separate
> **unless independently derived**.

"Unless independently derived" is the operative clause. The skill's binding rule
for a registered primitive is a *ceiling on what may be granted*, and it names
independent derivation as the standing route for exactly the class `r` belongs
to (weighting rule / normalization rule / selector).

`:11-12` also forbids the strong reading structurally: "Do not classify a
registered primitive as an axiom, imported value, missing premise, **no-go
wall**, or source of bounded status." Reading item 4 as a foreclosure is reading
the primitive as a no-go wall, which the check prohibits by name.

---

## (c) Registry grant and governing source

`docs/audit/data/axiom_premise_nodes.json` — `nodes.realized_state_primitive`:

- `current_path`: `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`
- `aliased_paths`: `["docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"]`
- `legacy_claim_ids`: `[]`
- listed in `canonical_ids` alongside `minimal_axioms`,
  `scale_reference_primitive`, `kinetic_isotropy_primitive`.

**Confirmed: the note is the governing source of the registered grant.** The
registry resolves the primitive to that exact path and no other.

**But the registered grant makes no mention of `r`, of dial settings, or of the
State-Contingency Register at all.** The full `note` field is:

> Explicitly approved framework primitive for the realized-state interface: the
> axioms select no state; a physical history fixes one law-admissible realized
> state, and derivations may evaluate at it POINTWISE only. **Supplies the slot,
> never the content**: no state, state-selection rule, measure,
> typicality/genericity assumption, weighting, probability rule,
> preferred/default state, or state-contingent value. Policing clauses: no
> averaging over alternatives; 'typical'/'generic' banned as specialization
> predicates; **the counterfactual test (a quoted number must be invariant over
> the law-admissible family, else it is registered data)**; law admissibility.
> The past hypothesis is explicitly NOT housed here … Dependencies on this
> primitive chain-satisfy without bounding downstream rows; the primitive itself
> carries no contingent content, and rows quoting data of a particular realized
> state remain conditional on that supplied data as supplied inputs always are.

The machine-readable grant is a pure non-supply declaration plus the
counterfactual test. Item 4 is not part of it.

The owner approval, `docs/audit/AXIOM_MINIMALITY_POLICY.md:605-613`, approves
exactly "the axioms select no state; a physical history fixes one law-admissible
realized state; derivations may evaluate at it pointwise only". Its "**No
laundering**" sub-entry (`:627-633`) restates "The primitive supplies the slot,
never the content", and §6's preamble (`:96-99`) governs the whole section:

> Entries below are the historical record of approvals … **They carry no premise
> or interpretive weight**: effect statements are informative summaries, and any
> load-bearing content must be carried by axiom text, approved primitives, or
> audited derivation.

**Nothing the owner approved mentions `r`.**

For completeness, the two other primitives are also non-supply with respect to
`r`: `kinetic_isotropy_primitive` "does not supply an absolute scale,
spacing-ratio theorem, dynamics, Lorentz-closure theorem, **mass ratio**,
coupling, mixing angle, phase, **selector**, readout bridge, probability rule,
**normalization rule**, or empirical match"
(`PRIMITIVE_REGISTRY_CHECK.md:33-36`); `scale_reference_primitive` is "units
conversion only" (`:23-28`).

---

## (d) VERDICT

> **NO. Approved foundation content does NOT answer the counting-bit question
> negatively. The campaign should NOT stop.**

Ex2's quote is real and correctly transcribed, and its identification of `r` is
correct (section 0). But item 4 is an entry in a register the note itself calls
**Informative** and **"documentation, not an additional gate"** (`:71`, `:74`),
recording **"current examples"** (`:73`), deferring for its canonical statement
to a note that is an **unaudited proposal** whose relevant guardrail explicitly
reserves derivation **"unless a separate pre-record argument supplies them"**
(`RECORD_OUTCOME…:72-73`), via a guardrail label (`G3`) that **does not exist in
the cited note**. The registered grant and the owner approval never mention `r`.
Reading item 4 as binding would make the primitive note a no-go wall, which
`PRIMITIVE_REGISTRY_CHECK.md:11-12` forbids by name and
`check_axiom_premise_clean.py:4-11` exists to tripwire.

**Item 4 records that the primitive does not supply `r`. It does not declare `r`
underivable.** Those are the two readings the task distinguishes, and the note's
own text picks the second.

### The dispositive positive evidence

The strong reading is not merely unsupported — it is **contradicted by a live
machine registry that post-dates the primitive note by a month and carries a
terminal audit verdict.**

`docs/audit/data/derivation_obligations.json`, node
`ac_orbit_occupancy_statistical_grain_derivation_obligation`:

```json
"label":  "AC occupancy statistical grain",
"target": "Derive from the retained framework chain whether the physical
           charged-lepton matter action counts the K/CPT orbit or holomorphic
           pair once rather than counting each sector or channel.",
"status": "open_gate",
"self_liquidation_condition": "A retained kappa/counting-rule theorem deriving
           this exact grain removes the obligation; until then it blocks
           dependent closure."
```

That `target` **is the campaign target, verbatim** — count the orbit once, or
count each sector/channel. The source note,
`docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`, is dated
**2026-07-11** (`:3`) — one month *after* the 2026-06-11 primitive note — and
states at `:19-24`:

> ## Closure criterion
>
> A closing theorem must derive the physical matter action and its measure, then
> distinguish the count-once `det_C`/holomorphic realization from the
> count-twice `|det_C|^2`/realified realization without inserting the desired
> charged-lepton value or readout dictionary.

That is the campaign's closure obligation, in the repo's own words, registered
as **live open work**. The registry description makes the standing explicit:
entries "may leave this registry only after a **retained derivation** closes the
named target".

The governance history is decisive on direction of travel.
`docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md:37-42` records that
the count-once horn was once **adopted by owner governance as a premise**
("the doublet contributes once per K/CPT orbit rather than once per sector or
channel"). `:4`, `:9-11` record that this was **superseded 2026-07-11** and the
premise channel **withdrawn**, and `:14-18` that the statement is now an "open
derivation obligation". So the repo did not conclude `r` is underivable — it did
the opposite: it **removed the free premise and demanded a derivation.**

Finally, that obligation row carries a **terminal** verdict on the live ledger
(reported, not predicted): `ac_orbit_occupancy_statistical_grain_derivation_obligation`
is `audited_renaming`, `effective_status_reason: terminal_audit`, audited
2026-07-11 by `gpt-5.6-sol` at `xhigh`, with the auditor's own scope line:

> "The note records, but does not discharge, **the obligation to derive** the
> physical charged-lepton determinant-counting grain."

An independent audit lane has therefore affirmed, terminally, that a live
*obligation to derive* the counting grain exists. That is flatly incompatible
with "approved foundation content already answers this negatively".

### What the registry entry DOES leave open — stated precisely

1. **Whether `r` is invariant over the law-admissible family.** The
   counterfactual test (`:44-45`) is a classifier; nothing in approved content
   establishes its antecedent for `r`. Establishing it either way is open, and
   is exactly the campaign's job.
2. **Whether the matter action forces the grain.** Registered live as
   `ac_orbit_occupancy_statistical_grain_derivation_obligation`, `open_gate`,
   with the closure criterion quoted above.
3. **The "separate pre-record argument" route**, expressly reserved at
   `RECORD_OUTCOME…:72-73`. Both Ex1 (associativity/Frobenius on the form) and
   Ex2 (mode-count factor) are attempts at that route; item 4 does not touch
   either.
4. **A negative closure is equally open and equally publishable.** If the
   campaign proves `r` genuinely varies over law-admissible states, that
   *derives* item 4's classification rather than quoting it — and it would be
   the campaign's result, not pre-existing content.

### One in-scope observation bearing on the Ex1/Ex2 tension

Not my adjudication to make, but it falls out of the sources I had to read and
the supervisor should see it. The landed synthesis note
`docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:66-69`
tabulates the two horns as:

| measure | weighting | r | Q |
|---|---|---|---|
| block-count `(1,1)` = `det_C` | equal weight / **equal HS energy per block** (`3a^2 = 6|b|^2`) | **1/2** | **2/3** |
| dimension `(1,2)` = `det_R` | real-dimension / Born / **trace** | **1** | **1** |

So the corpus already assigns "equal HS energy per block" to `r = 1/2` **and**
"trace" to `r = 1` — the two things Ex1 treats as one object ("the
Hilbert-Schmidt / trace form"). My section-0 gate reproduces the first row
exactly (`3a^2 = 6|b|^2 => r = 1/2`) and the mutation probe shows the second row
is what you get from a different block normalization, not from a different
metric ray. Ex1's claim that "diag(1,1,1) is a NEW framing" and Ex2's claim that
the metric factor alone is canonically fixed both need to be checked against
this landed table before either is relied on. Flagging only; adjudicating it is
the other wave's task.

---

## (e) Prose status labels vs the live ledger

**Method.** Indexed all 3,863 ledger shards from `origin/main`
(`docs/audit/data/ledger/*/*.json`), reading `effective_status` /
`intrinsic_status` / `audit_status` per row. **No prose status label was used as
input.** Then scanned every `.md` under `origin/main` `docs/` for machine
status vocabulary co-occurring with a lane row's claim_id or note basename,
keeping only lines carrying exactly one lane row and exactly one status label so
the label attaches unambiguously, excluding a note labelling itself and
excluding `docs/ai_methodology/raw/` transcripts. Every disagreement listed
below was then hand-inspected.

### (e1) The exercise sectors' headline claim is CONFIRMED

Of the **37** notes forming the counting-bit foreclosure scaffolding:

| live effective_status | count |
|---|---|
| `unaudited` | 31 |
| `meta` | 3 |
| `audited_conditional` | 1 |
| `retained_bounded` | 2 |

**33 of 37 (89%) carry no retained-grade audit standing on `origin/main`.**
Only `flavor_doublet_metric_default_is_detr_2026-06-02` (`retained_bounded`) and
`flavor_einselection_2sector_modulo_kreality_2026-06-02` (`audited_conditional`)
are audit-touched. The three `meta` rows are
`charged_lepton_value_reduces_to_one_counting_bit_synthesis_note_2026-06-05`,
`record_outcome_observable_principle_canonical_proposal_note_2026-06-05`, and
`realized_state_primitive`.

### (e2) Rows where note prose disagrees with the live ledger

Every row below is `origin/main`. "prose" = the label asserted in another
note's text.

**1. `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` — live
`unaudited` (`effective_status_reason: awaiting_audit`; 9 archived
`previous_audits`, i.e. audit reset by note-hash change).** The single most
load-bearing row in the lane, and the most mislabelled.

- `docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:72` — `retained_no_go`
- `…:140` — `retained_no_go`
- `…:151` — `retained_no_go`
- `…:188` — `retained_no_go`
- `docs/ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md:98` — `retained_no_go`
- `docs/ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md:315` — `retained_no_go`
- `docs/FLAVOR_LANE_PANEL_REDUCES_TO_DOUBLET_MODE_COUNT_2026-05-31.md:34` — `retained_no_go`
- `docs/FLAVOR_LANE_PANEL_REDUCES_TO_DOUBLET_MODE_COUNT_2026-05-31.md:109` — `retained_no_go`
- `docs/KOIDE_FINITE_BETA_WEIGHT_IS_THE_PARTITION_BIT_NOTE_2026-06-02.md:143` — `retained_no_go`
- `docs/FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_CANNOT_DERIVE_THE_KOIDE_DIAL_NARROW_NO_GO_NOTE_2026-06-15.md:186` — `retained no-go`
- `docs/THEOREM_BAE_NEWTON_GIRARD_UNIFIED_OBSTRUCTION_NOTE_2026-05-10_t2bae.md:426` — `already retained`

This confirms and extends the Wave 1 flag (which cited one line); there are
**eleven**. `…SYNTHESIS_NOTE…:140` calls it "The collapsed wall … Every route
above is an alternate face of it" — the lane's single wall is labelled retained
and is not.

**2. `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` — live
`unaudited`; prose `retained_bounded`/`retained` at 20 lines**, incl.
`docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:106`,
`docs/CHIRALITY_GATE_IS_TWO_INDEPENDENT_GATES_DIRAC_VS_GENERATION_SCOPING_NOTE_2026-06-08.md:27`,
`docs/FLAVOR_R_HALF_ASSUMPTIONS_AUDIT_NOTE_2026-05-30.md:46`,
`docs/KOIDE_FINITE_BETA_WEIGHT_IS_THE_PARTITION_BIT_NOTE_2026-06-02.md:148`,
`docs/REGISTRATION_REINSTATES_CHIRALITY_NO_GO_NOTE_2026-06-07.md:102`, `:161`,
`docs/FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31.md:75`, `:136`,
`docs/KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md:26`, `:87`,
`docs/FLAVOR_EQUIVARIANT_ETA_COMPLEMENTARITY_NOTE_2026-05-30.md:13`,
`docs/FLAVOR_GENERATION_SPACE_BRIDGE_REDUCES_TO_OPEN_GATE_2026-05-31.md:94`,
`docs/G2_BRIDGE_C3_CURRENT_CANNOT_BEAT_GAP_A_NO_GO_NOTE_2026-06-06.md:163`,
`docs/KOIDE_ADJOINT_MAP_QUOTIENTS_SPINOR_Z2_NARROW_NO_GO_NOTE_2026-06-02.md:127`,
`docs/KOIDE_CARRIER_SCORING_NEEDS_NONTRIVIAL_MODULAR_NOTE_2026-06-02.md:210`,
`docs/KOIDE_DELTA_PHASE_AND_GENERATION_COUNT_SHARE_ONE_Z2_ORIENTATION_NARROW_THEOREM_NOTE_2026-06-08.md:54`,
`docs/KOIDE_GAMMA5_FACTOR_BRIDGE_NO_GO_NOTE_2026-06-06.md:124`,
`docs/KOIDE_MATTER_ATTACHMENT_GATE_EXTRA_ASSUMPTIONS_REVIEW_NOTE_2026-06-02.md:144`,
`docs/KOIDE_SIGNED_READOUT_IS_NOT_CHIRALITY_NARROW_NO_GO_NOTE_2026-06-04.md:304`,
`docs/FLAVOR_DETR_DEFAULT_FULL_EXERCISE_NOTE_2026-05-30.md:130`.

**3. `charged_lepton_koide_cone_algebraic_equivalence_note` — live `unaudited`;
prose `retained` at 17 note lines** (all the `KOIDE_A1_PROBE_*` /
`KOIDE_A1_ROUTE_*` / `KOIDE_BAE_PROBE_*` families, e.g.
`docs/KOIDE_A1_PROBE_FLAVOR_ANOMALY_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe2.md:146`,
`docs/KOIDE_A1_ROUTE_E_KOSTANT_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_routee.md:158`).

**4. `charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem_note_2026-05-10`
— live `audit_in_progress`; prose `retained`** at
`docs/ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md:313`,
`docs/CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md:191`,
`docs/KOIDE_CARRIER_SCORING_NEEDS_NONTRIVIAL_MODULAR_NOTE_2026-06-02.md:207`,
`docs/KOIDE_FINITE_BETA_WEIGHT_IS_THE_PARTITION_BIT_NOTE_2026-06-02.md:145`.

**5. `koide_kappa_block_total_frobenius_measure_theorem_note_2026-04-19` — live
`unaudited`; prose `retained` at 7 lines.** This is the `E_+ = 3a^2`,
`E_perp = 6|b|^2` row — i.e. **the HS/block-total structure that section 0 shows
is what puts the `r = 1/2` horn at the equal-energy point, and therefore the
direct foundation of the Ex1 claim.** Cited as retained at
`docs/KOIDE_A1_PROBE_PLANCHEREL_PETER_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe12.md:140`,
`docs/KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md:141`,
`docs/KOIDE_A1_PROBE_RP_FROBENIUS_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe1.md:152`,
`docs/KOIDE_BAE_PROBE_F1_CANONICAL_FUNCTIONAL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe18.md:109`,
`docs/KOIDE_U_BAE_NCG_SPECTRAL_TRIPLE_NOTE_2026-05-08_probeU_bae_ncg.md:236`,
`docs/QUARK_BAE_ANALOG_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_quarkBAE.md:109`, `:151`.
**Ex1 must not cite this as retained.**

**6. `flavor_einselection_2sector_modulo_kreality_2026-06-02` — live
`audited_conditional`; prose `retained_bounded`** at
`docs/FLAVOR_HANDEDNESS_IS_RK_EVEN_TIME_ARROW_INSUFFICIENT_NARROW_NO_GO_NOTE_2026-06-08.md:41`,
`docs/G2_BRIDGE_C3_CURRENT_CANNOT_BEAT_GAP_A_NO_GO_NOTE_2026-06-06.md:159`,
`docs/PMNS_TM2_COLUMN_SITE_BASIS_KCPT_PREDICATE_BOUNDED_THEOREM_NOTE_2026-06-07.md:101`,
`docs/PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NARROW_THEOREM_NOTE_2026-06-05.md:102`,
`docs/REGISTRATION_REINSTATES_CHIRALITY_NO_GO_NOTE_2026-06-07.md:183`.
This is the `K`-reality 2-block predicate — load-bearing for the doublet split.

**7. `koide_q23_block_weight_frontier_bounded_note_2026-05-29` — live
`unaudited`; prose `retained_bounded`** at
`docs/FLAVOR_DETR_DEFAULT_FULL_EXERCISE_NOTE_2026-05-30.md:133`,
`docs/KOIDE_CARRIER_SCORING_NEEDS_NONTRIVIAL_MODULAR_NOTE_2026-06-02.md:208`,
`docs/KOIDE_FINITE_BETA_WEIGHT_IS_THE_PARTITION_BIT_NOTE_2026-06-02.md:146`,
`docs/KOIDE_HERMITIAN_RECORDS_IMPORT_REQUIRED_NARROW_THEOREM_NOTE_2026-06-02.md:132`.

**8. `action_normalization_note` — live `unaudited`; prose `retained_no_go`** at
`docs/FLAVOR_LANE_PANEL_REDUCES_TO_DOUBLET_MODE_COUNT_2026-05-31.md:35`.

**9. `koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29`
— live `unaudited`; prose `audited_failed`** at
`docs/KOIDE_ADJOINT_MAP_QUOTIENTS_SPINOR_Z2_NARROW_NO_GO_NOTE_2026-06-02.md:128`,
`docs/KOIDE_RECORDS_REALITY_SHRINKS_IMPORT_TO_SIGN_NOTE_2026-06-02.md:178`.
Disagreement in the *other* direction — prose asserts a terminal negative
verdict the ledger does not carry. A route treated as killed may not be.

**10. `koide_aps_c3_fixed_locus_weights_bridge_narrow_theorem_note_2026-06-05` —
live `retained`; prose `retained_bounded`** (×4). Prose *understates*; harmless
but recorded for completeness.

### (e3) Corpus-wide magnitude

Widening to all 539 ledger rows whose note filename matches the
Koide/charged-lepton/AC-phi-lambda/KCPT/occupancy lane, and keeping only
unambiguous single-row/single-label lines:

- **75 distinct rows** carry at least one prose status label that disagrees with
  their live `origin/main` status, across **279 lines**.
- **63 of those 75 are `unaudited` live**; prose calls them `retained` (200
  lines), `retained_bounded` (46), or `retained_no_go` (19).

The dominant mechanism is audit reset by note-hash change: e.g.
`koide_frobenius_isotype_split_uniqueness_note_2026-04-21` has 9 archived
`previous_audits` but `audit_status: unaudited`,
`effective_status_reason: awaiting_audit`. The prose was true when written and
went stale when the note was edited. This is the standing
`verify_ledger_before_citing` failure mode operating at lane scale.

### (e4) Verified NOT disagreements (checked and cleared)

- `docs/FLAVOR_R_HALF_ASSUMPTIONS_AUDIT_NOTE_2026-05-30.md:3` — "This note is
  retained for provenance" is English usage, not a status label.
- `docs/publication/ci3_z3/RESULTS_INDEX_EFFECTIVE_STATUS.md:112` — carries the
  correct inline tag `[audit:unaudited]` for the Frobenius note. The rendered
  publication surface **agrees** with the ledger.
- `docs/publication/ci3_z3/DERIVATION_ATLAS.md:96`, `:360` — "retained" is
  adjectival ("the retained `hw=1` triplet"), not a label.
- `docs/FLAVOR_LANE_PANEL_REDUCES_TO_DOUBLET_MODE_COUNT_2026-05-31.md:109` for
  `koide_real_rep_block_count_permitted_not_forced` — prose says `**unaudited**`
  and **agrees**.

Worth stating plainly: **the auto-rendered publication surfaces are correct.**
The drift is confined to hand-written note prose.

---

## Bottom line

The campaign is **not** foreclosed by approved foundation content, and should
continue. Item 4 is a real, correctly-quoted sentence in an explicitly
**informative** register that the primitive note itself calls "documentation,
not an additional gate"; it records non-supply by the primitive, defers to an
**unaudited** proposal note through a guardrail label that does not exist there,
and that guardrail expressly reserves derivation "unless a separate pre-record
argument supplies them". Meanwhile the repo's live machine registry, one month
younger than the primitive note and carrying a terminal audit verdict, registers
the campaign's exact target as an **open derivation obligation** with a stated
closure criterion — and the governance record shows the count-once horn was
**demoted from premise to obligation**, not concluded underivable.

The separate and genuine finding is (e): the lane's foreclosure scaffolding is
**89% unaudited** while note prose repeatedly calls it retained — including the
lane's single collapsed wall (11 mislabelled lines) and the HS/block-total row
that Ex1's argument rests on. Neither exercise sector's conclusion may cite any
of these as retained.
