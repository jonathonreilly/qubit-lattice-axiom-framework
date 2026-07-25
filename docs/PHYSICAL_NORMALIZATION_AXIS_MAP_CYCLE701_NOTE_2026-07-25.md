# The normalization residuals are independent axes on three supplied surfaces, not one reference choice — Cycle 701

Date: 2026-07-25

Claim type: meta

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. **No convention is adopted, no value is
selected, and no ruling is made.** This note is a navigation and owner decision
surface, in the sense of
`CROSS_LANE_DEPENDENCY_MAP_NOTE_2026-04-30.md` (lane dependencies) and
`WALLS_ATTACK_20260702_ADJUDICATION_BRIEF_META_NOTE_2026-07-02.md` (campaign
adjudication); this one maps normalization parameters instead.

Runner: `scripts/physical_normalization_axis_map_cycle701_2026_07_25.py`
(8 PASS / 0 FAIL, exit 0; exact rational and exact symbolic arithmetic, with a
negative control on the decisive test).

## The question, and the wrong answer it is easy to give

Several lanes each terminate at "one free normalization parameter". It is
tempting to read those as the same object, so that one owner convention would
discharge them together and several flagship lanes would unblock at once.

**That reading is false, and this note's own campaign made the mistake before
checking.** An earlier handoff in this campaign asserted that the two live AC
routes and the reference-normalization object "terminate at the same object, a
selected reference". They do not. The correction is the content of this note.

## The axes

| axis | fixed by | supplied surface | what would discharge it |
|---|---|---|---|
| **A1** readout weight `w` | the C2 two-cell normal form `I_w(x_A,x_B) = x_A + w·x_B` | Record readout | a counting convention |
| **A2** electroweak weight `kappa_EW` | `Pi_phys = C + kappa_EW·S` — the *same* normal form, a *different* partition | Record readout | a counting convention, separately |
| **B** activation scale `a_act` | the AC event-rate match at `delta = 2/9` | occurrence / probability | a formation or rate law |
| **C** generator normalization `alpha` | hypercharge tracelessness plus a unit choice | gauge algebra | a unit convention |

The list is **not claimed complete**. `g_bare`, `c_iso`, and the
scale-reference primitive are further convention degrees of freedom recorded
elsewhere; `G_BARE_C_ISO_CONVENTION_ORBIT_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-17.md`
already treats three of them as independent within its own lane. This note maps
the four above because they are the ones the current flagship-lane obstructions
name.

## A — the readout weights, and why there is more than one

The C2 normal form is in exact bijection with the Koide flow coordinates. The
runner verifies `kappa = 2w/(1-w)` and `w = kappa/(2+kappa)` are mutually
inverse on six rational samples, that `kappa = 1/r` throughout, and that
`w = 0, 1` are genuine poles rather than silently mapped points.

The two declared counting conventions select different physics:

| `w` | `r` | `kappa` |
|---|---|---|
| 1/3 | 1 | 1 |
| 1/2 | **1/2** | 2 |

So the counting convention is load-bearing, not cosmetic.

The electroweak weighting `Pi_phys = C + kappa_EW·S` has the **same normal
form**: substituting the electroweak names into the Koide form reproduces it
identically, which the runner checks symbolically. That is exactly why it is a
*second* axis and not the same parameter — same shape, different partition. A
convention that fixes the weight on one partition says nothing about the other.

## B — the activation scale is not a readout weight

The AC event-rate route gives

```text
omega_clock / a_act = 2 sqrt(3) |b| sin(delta) / a_act.
```

Matching the target `Phi = 2/3` at `delta = 2/9` is solved exactly by the
runner and reproduces the landed relation
`|b| = a_act / (3 sqrt(3) sin(2/9))`. The runner then checks the structurally
important part: the *ratio* `|b|/a_act` is pinned and contains no `a_act`, so
what remains free is the **activation scale**, with `|b|` slaved to it.

`a_act` is an activation probability and `|b|` a coupling magnitude. Neither is
a weight on record content. This axis lives on the occurrence and probability
surfaces, which the axioms explicitly withhold — every formation rule is
downstream content. **No readout convention reaches it.**

## C — the generator normalization

On the hypercharge two-block surface, tracelessness `6α + 2β = 0` gives
`β = -3α`, fixing the ratio `+1 : -3` and leaving the entire line free — the
runner confirms that every point of the line, including `α = 0`, satisfies it.
Only the convention that the trivial block reads unit charge selects
`α = 1/3`. This is the gauge algebra surface, not the readout surface.

## The independence result

The decisive check is not that each axis is free — each lane already says so —
but that they are independent.

**D1.** The defining relations have pairwise-disjoint variable sets: no readout
weight occurs in the AC rate relation or the hypercharge relation, and neither
`a_act`, `|b|`, `α`, nor `β` occurs in the readout normal form.

**D2.** All eight combinations of representative choices across the three
classes are jointly satisfiable. The joint solution set is therefore a product,
and fixing any one coordinate leaves the others exactly as free as before.

**D3 — the negative control.** The same disjointness test applied to `kappa`
and `w`, which are the *same* axis in different coordinates, correctly detects
them as dependent. Without this row the test would prove nothing.

## The owner decision surface (stated, NOT adopted)

For each axis, what an adoption would buy and what it would not:

- **Adopt a counting convention for `w`.** Buys `r` and `kappa` on that
  partition — `w = 1/2` gives `r = 1/2`, `w = 1/3` gives `r = 1`. Buys nothing
  on `kappa_EW`, `a_act`, or `alpha`.
- **Adopt a counting convention for `kappa_EW`.** Buys the electroweak
  weighting. Independent of the above.
- **Adopt a unit convention for `alpha`.** Buys the normalized hypercharge
  assignment. Cheapest of the four: the structural ratio `+1 : -3` is already
  exact, so only a scale is at stake.
- **`a_act` cannot be discharged by convention in the same sense.** It is a
  rate on the occurrence surface. Fixing it is adopting a formation or rate
  law, which is a materially larger commitment than a counting or unit choice,
  and it is the one the axioms most explicitly withhold.

The practical consequence: **the flagship lanes do not unblock together.** Work
that discharges the readout axis leaves the AC obligations exactly where they
were.

## What this note does not do

- It adopts nothing, selects no value, and rules on no reading.
- It does not claim the axis list is complete.
- It does not derive any of the four parameters, or show any of them
  underivable in principle — each lane's own no-go owns that question.
- It changes no lane, row, or obligation status.
- It is `meta`: a navigation artifact, not a theorem about physics.

## Scope for independent review

Every quoted number is recomputed by the runner rather than copied: the
bijection and its poles, the `w -> (r, kappa)` table, the symbolic identity of
the two normal forms, the exact solution of the AC rate match, and the
hypercharge line. The independence claim is a statement about the *declared*
defining relations as quoted from the cited notes; if a lane's real defining
relation involves variables its note does not display, the disjointness
conclusion for that lane would need rechecking. That is the main way this map
could be wrong, and it is why D3 exists.

## Dependency citations

The runner imports nothing from the repository. Navigation context, not
load-bearing: `C2_WEIGHTING_NORMAL_FORM_ONE_PARAMETER_UNIQUENESS_BOUNDED_NOTE_2026-07-02.md`,
`KOIDE_KAPPA_FLOW_CLASS_IS_THE_FORMATION_WEIGHT_IN_FLOW_COORDINATES_BOUNDED_THEOREM_NOTE_2026-07-12.md`,
`EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`,
`ACPHILAMBDA_R_ETA_DOUBLET_CLOCK_RATE_NORMALIZATION_NO_GO_NOTE_2026-07-04.md`,
`HYPERCHARGE_IDENTIFICATION_NOTE.md`,
`G_BARE_C_ISO_CONVENTION_ORBIT_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-17.md`,
`CROSS_LANE_DEPENDENCY_MAP_NOTE_2026-04-30.md`, and
`WALLS_ATTACK_20260702_ADJUDICATION_BRIEF_META_NOTE_2026-07-02.md`.
