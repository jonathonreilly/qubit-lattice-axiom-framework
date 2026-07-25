# The named normalization residuals, recomputed, and which pairs the corpus does not link — Cycle 701

Date: 2026-07-25

Claim type: meta

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. **No convention is adopted, no value is
selected, no identification between parameters is asserted, and no ruling is
made.** This is a navigation artifact, in the sense of
`CROSS_LANE_DEPENDENCY_MAP_NOTE_2026-04-30.md` (which maps lane dependencies)
and `WALLS_ATTACK_20260702_ADJUDICATION_BRIEF_META_NOTE_2026-07-02.md` (which
indexes a campaign); this one inventories normalization residuals.

Runner: `scripts/physical_normalization_axis_map_cycle701_2026_07_25.py`
(7 PASS / 0 FAIL, exit 0; exact rational and exact symbolic arithmetic).

## What this note is, and what an earlier draft got wrong

Several lanes each terminate at "one free normalization parameter". It is
tempting to read those as one object, so that a single owner convention would
discharge them together and several flagship lanes would unblock at once. **An
earlier handoff in this campaign asserted exactly that**, saying the live AC
routes and the reference-normalization object "terminate at the same object, a
selected reference".

The first attempt to correct that went too far in the other direction. It
claimed the residuals are provably *independent*, on the grounds that their
transcribed defining equations use disjoint symbols. A cluster-cap evaluator
judged that largely true by construction — separately transcribed equations
trivially use different symbols, and that cannot rule out a semantic
identification. **That claim is withdrawn and does not appear below.**

What is left is deliberately narrower and is two things:

1. a **recomputed inventory** — every number quoted here is recomputed by the
   runner from the relation its source states, not transcribed; and
2. a **recorded corpus search** — which pairs of residuals no landed note
   links. That is a statement about the repository at a named commit, not a
   theorem about physics.

## The recomputed inventory

| residual | relation recomputed | surface its source places it on |
|---|---|---|
| `w_readout` | C2 two-cell weighting `I_w(x_A,x_B) = x_A + w·x_B` | Record readout |
| `w_formation` | Koide flow weight, `kappa = 2w/(1-w)`, `r = (1-w)/(2w)` | formation |
| `kappa_EW` | `Pi_phys = C + kappa_EW·S`, with supplied map `K_EW = 1/(8/9 + kappa_EW/9)` | Record readout / EW channel |
| `a_act` | AC event-rate match at `delta = 2/9` | occurrence and probability |
| `alpha` | hypercharge tracelessness `6α + 2β = 0` plus a unit choice | gauge algebra |

The list is **not claimed complete**. `g_bare`, `c_iso`, and the
scale-reference primitive are further convention degrees of freedom recorded
elsewhere; `G_BARE_C_ISO_CONVENTION_ORBIT_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-17.md`
already treats three of them within its own lane.

What the runner recomputes:

- **A1** — `kappa = 2w/(1-w)` and `w = kappa/(2+kappa)` are mutually inverse on
  six rational samples, `kappa = 1/r` throughout, and `w = 0, 1` are genuine
  poles rather than silently mapped points.
- **A2** — the declared counting values: `w = 1/2` gives `r = 1/2, kappa = 2`;
  `w = 1/3` gives `r = 1, kappa = 1`. The choice changes the answer.
- **A3** — the electroweak weighting has the same two-cell *shape*: substituting
  the electroweak names into the C2 form reproduces it identically. Shared
  shape is recorded; **no identification is asserted**.
- **A4** — the supplied `K_EW` map recomputes to `9/8` at `kappa_EW = 0`, has
  its pole at `kappa_EW = -8`, and is not the A1 bijection in disguise.
- **B1** — matching the AC event-rate ratio to `2/3` at `delta = 2/9` pins the
  ratio and reproduces the landed relation `|b| = a_act/(3√3 sin(2/9))`; the
  ratio contains no `a_act`, so the **activation scale** is what stays free,
  with `|b|` slaved to it.
- **C1** — tracelessness gives `β = -3α`, fixing the ratio `+1 : -3` and leaving
  the whole line free, including `α = 0`; only the unit convention that the
  trivial block reads unit charge selects `α = 1/3`.

## Two different objects are both written `w`

The C2 note's `w` weights a two-cell **readout**. The Koide flow note's `w` is a
**formation** weight — that note's title says so, and it states that the kappa
bookkeeping residual and the formation/equipartition residual are one scalar
object in two coordinates, under its own named conditional identifications.

Both satisfy `kappa = 2w/(1-w)`. The runner records that this is the whole of
what the arithmetic establishes: **satisfying a shared relation is not identity
of the objects.** They are carried as distinct symbols here, and the earlier
draft's slide from one to the other is the specific error this section exists to
prevent.

## The recorded corpus search

Searched at `origin/main` `a17b5e74a8b0ea5926553579cdf20115e93ea1c2`.

| # | question | command | result |
|---|---|---|---|
| Q1 | is the C2 readout weight identified with the Koide formation weight? | `git grep -n -iE "C2.{0,40}formation weight\|formation weight.{0,40}C2\|readout weight.{0,30}(is\|equals).{0,20}formation weight" origin/main -- 'docs/*.md'` | **no hits** |
| Q2 | does any landed note link `kappa_EW` to `w` or `kappa`? | `git grep -n -iE "kappa_EW.{0,60}(kappa[^_]\|w\b)\|..." origin/main -- 'docs/*.md'` | hits are `kappa_EW`'s own supplied map and index rows; `CANONICAL_TWO_CELL_CONTEXT_C3_EW_INSTANCE_BOUNDED_NOTE_2026-07-02.md` verifies the EW frame as a two-cell instance and **explicitly declines** to set `kappa_EW` |
| Q3 | does any landed note link `a_act` to a weighting parameter? | `git grep -n -iE "a_act.{0,70}(weight\|kappa\|alpha)\|..." origin/main -- 'docs/*.md'` | **no hits** |

So, as of that commit, **no landed note links the readout weighting, the
formation weight, the activation scale, and the generator normalization to one
another.** That is the honest form of the observation. It is a fact about what
has been written, and it is exactly the kind of fact a later note could
overturn by supplying an identification.

## What follows for planning, and what does not

**Follows.** There is no landed basis for expecting one convention to discharge
these together. A plan that plugs the readout weighting and then treats the AC
obligations as unblocked is, at present, unsupported by anything in the corpus.

**Does not follow.** That they are *incapable* of being linked. The absence of a
landed identification is not a proof of independence, and this note does not
claim one. Supplying such an identification is a legitimate and potentially
high-value target; if it exists, it would be worth more than any single
convention adoption.

## What this note does not do

- It adopts nothing, selects no value, asserts no identification, rules on no
  reading.
- It does not claim the residual list is complete.
- It does not claim the residuals are independent, and it withdraws an earlier
  draft's claim to that effect.
- It does not derive any of the parameters, or show any underivable — each
  lane's own no-go owns that question.
- It changes no lane, row, or obligation status. It is `meta`.

## Scope for independent review

Every quoted number is recomputed rather than copied: the bijection and its
poles, the `w -> (r, kappa)` table, the symbolic shape match of the two
weightings, the `K_EW` map with its value at zero and its pole, the exact
solution of the AC rate match, and the hypercharge line. The corpus claims are
searches at a named commit with the commands displayed, and they are negative
results about the repository — the standard caveat for a negative search
applies, and a differently-phrased search could find a link these three missed.
The surface attributions come from each source's own words; where a source
attaches conditional identifications, as the Koide flow note does, that
conditionality is preserved rather than flattened.

## Dependency citations

The runner imports nothing from the repository. Navigation context, not
load-bearing: `C2_WEIGHTING_NORMAL_FORM_ONE_PARAMETER_UNIQUENESS_BOUNDED_NOTE_2026-07-02.md`,
`KOIDE_KAPPA_FLOW_CLASS_IS_THE_FORMATION_WEIGHT_IN_FLOW_COORDINATES_BOUNDED_THEOREM_NOTE_2026-07-12.md`,
`EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`,
`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`,
`CANONICAL_TWO_CELL_CONTEXT_C3_EW_INSTANCE_BOUNDED_NOTE_2026-07-02.md`,
`ACPHILAMBDA_R_ETA_DOUBLET_CLOCK_RATE_NORMALIZATION_NO_GO_NOTE_2026-07-04.md`,
`HYPERCHARGE_IDENTIFICATION_NOTE.md`,
`G_BARE_C_ISO_CONVENTION_ORBIT_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-17.md`,
`CROSS_LANE_DEPENDENCY_MAP_NOTE_2026-04-30.md`, and
`WALLS_ATTACK_20260702_ADJUDICATION_BRIEF_META_NOTE_2026-07-02.md`.
