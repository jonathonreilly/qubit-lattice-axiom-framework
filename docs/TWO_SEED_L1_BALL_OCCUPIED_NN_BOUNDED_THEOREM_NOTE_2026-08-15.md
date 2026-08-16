---
claim_id: two_seed_l1_ball_occupied_nn_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Whether the union of two ℓ¹ balls of radii 0..2 at the listed separations ever gives an unread site 4 or more occupied 6-NN is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_seed_l1_ball_occupied_nn_2026_08_15.py
---

# Occupied 6-NN Bound For The Union Of Two Small ℓ¹ Balls

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact taxicab geometry of two finite ℓ¹ balls on `Z^3`. The
census reports whether an unread site in a declared box can see four or more
occupied six-neighbors. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_seed_l1_ball_occupied_nn_2026_08_15.py`](../scripts/two_seed_l1_ball_occupied_nn_2026_08_15.py)

## Result Up Front

Let `B_r(c) = { x in Z^3 : ||x-c||_1 ≤ r }` be the closed ℓ¹ ball of radius
`r` about `c`. For radii `r,s ∈ {0,1,2}` and a listed separation
`p ∈ {(1,0,0),(1,1,0),(1,1,1),(2,0,0)}`, write

`U = B_r(0) ∪ B_s(p)`.

A site is **unread** for this scoring if it lies in the finite box
`|x|,|y|,|z| ≤ 6` and is not in `U`. Its **occupied-NN count** is the number
of its six axial neighbors that lie in `U`. Occupied here means membership
in the constructed set `U`. It is not a new occupancy member, not a Record
formation event, and not a pair-slot label.

Across the 36 declared unions, the unread occupied-NN maximum is `4`, and
that value occurs for exactly one pair `(p,r,s) = ((2,0,0),2,2)`. The
lex-first unread witness is `(1,-1,-1)`, whose occupied neighbors are
`(2,-1,-1)`, `(0,-1,-1)`, `(1,0,-1)`, and `(1,-1,0)`. Every other declared
union has unread maximum at most `3`.

A single ball of radius `2` has unread occupied-NN maximum `3`. The
four-neighbor witness is therefore a two-center effect: the unread site sits
off the axis between two radius-`2` balls separated by two lattice steps and
sees two neighbors from each ball. That is not leftover-character of a
one-center next-shell bound, and it is not a pair-member slot census. The
note scores geometry of two ℓ¹ balls only.
Do not grow a new occupancy member — score geometry of two ℓ¹ balls only.

The census is **Displayed, not adopted**. Do not write two-seed geometry into
Admissibility. Do not attach L1.

## Current Premise Boundary

The Lattice premise is quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The only use of Lattice is the cubic site set and its six-neighbor adjacency.
Admissibility is not used as a supplier of two-seed geometry. Record is not
used as a supplier of occupancy. The word **unread** in this note is a
scoring tag for sites outside `U` inside the declared box; it is not a
readout value and does not assign content to absence.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 36-union occupied-NN census is a finite exact listing on a declared box. The four-neighbor witness is exhibited. Two-seed geometry is displayed, not adopted, and is not written into Admissibility."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "score whether two small ℓ¹ balls can present four occupied six-neighbors to an unread site"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the two-ball census displayed. Do not grow an occupancy member, do not attach L1, and do not write the geometry into Admissibility."
conditional_surface_status: "exact on the declared radii, separations, six-neighbor graph, and box; not a lattice-wide occupancy law"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `0 = (0,0,0)` and `N(x) = {x±e_1, x±e_2, x±e_3}` for the open
six-neighbor set. Graph distance is the taxicab metric `||·||_1`. The
executed radii are `{0,1,2}`. The executed separations are

`p ∈ {(1,0,0), (1,1,0), (1,1,1), (2,0,0)}`.

The occupied set of a triple `(p,r,s)` is `U = B_r(0) ∪ B_s(p)`. The unread
box is

`{ x ∈ Z^3 : max(|x_1|,|x_2|,|x_3|) ≤ 6 } \ U`.

Every site of every executed `U` satisfies `max(|x_i|) ≤ 4`, so every
occupied neighbor of a site that can touch `U` lies well inside the box.
The reported maxima are therefore the same as on the infinite lattice for
these radii.

## Theorem 1 — Per-Union Occupied-NN Maxima

For each declared `(p,r,s)`, the maximum occupied-NN count over unread
sites in the box is the entry below. Rows are `r = 0,1,2` and columns are
`s = 0,1,2`.

`p=(1,0,0)`: max occupied-NN by `(r,s)` is `[[1,2,3],[2,2,3],[3,3,3]]`

`p=(1,1,0)`: max occupied-NN by `(r,s)` is `[[2,2,3],[2,3,3],[3,3,3]]`

`p=(1,1,1)`: max occupied-NN by `(r,s)` is `[[1,3,3],[3,2,3],[3,3,3]]`

`p=(2,0,0)`: max occupied-NN by `(r,s)` is `[[2,2,3],[2,3,3],[3,3,4]]`

Thus some declared union reaches occupied-NN count `≥ 4`, and exactly one
does: `(p,r,s) = ((2,0,0),2,2)` with maximum `4`. The other 35 unions stay
at most `3`.

As a one-center control, `U = B_r(0)` alone has unread maxima `1,2,3` for
`r = 0,1,2`. In particular the next shell of a radius-`2` ball never
presents four occupied six-neighbors.

Cardinalities `|U|` for the same order of `(r,s)` are

| `p` | `|U|` by `(r,s)` |
|---|---|
| `(1,0,0)` | `[[2,7,25],[7,12,25],[25,25,38]]` |
| `(1,1,0)` | `[[2,8,25],[8,12,29],[25,29,38]]` |
| `(1,1,1)` | `[[2,8,26],[8,14,29],[26,29,44]]` |
| `(2,0,0)` | `[[2,8,25],[8,13,30],[25,30,43]]` |

## Theorem 2 — Lex-First Four-Neighbor Witness

The unique declared union with maximum `≥ 4` is

`p = (2,0,0)`, `r = 2`, `s = 2`,

so `U = B_2(0) ∪ B_2((2,0,0))` and `|U| = 43`. Exactly four unread box
sites reach occupied-NN count `4`:

`(1,-1,-1)`, `(1,-1,1)`, `(1,1,-1)`, `(1,1,1)`.

The lex-first unread witness is `(1,-1,-1)`. Its occupied-NN list, in the
axial order `+e_1,-e_1,+e_2,-e_2,+e_3,-e_3` restricted to `U`, is

`(2,-1,-1)`, `(0,-1,-1)`, `(1,0,-1)`, `(1,-1,0)`.

Each of those four neighbors lies in `U`, and the remaining two axial
neighbors `(1,-2,-1)` and `(1,-1,-2)` do not. The witness itself has
`||(1,-1,-1)||_1 = 3` and `||(1,-1,-1)-(2,0,0)||_1 = 3`, so it lies in
neither closed ball.

The same four-neighbor pattern is the orbit of `(1,-1,-1)` under the
sign-flip of the two transverse coordinates. No other unread site in the
box reaches count `4` on this union, and no unread site on any other
declared union reaches count `4`.

## Theorem 3 — Displayed, Not Adopted

Displayed, not adopted. The two-ball census is a finite geometric report. It
does not enlarge Admissibility, does not select a formation rule, and does
not install an occupancy primitive. Do not write two-seed geometry into
Admissibility. Do not attach L1.

The current Admissibility wording determines, for each site, a probability
distribution from nearest-neighbor conditions. That wording does not name a
seed, a grown ball, a two-center union, or an occupied-NN threshold. The
present listing is therefore not an axiom edit and not a candidate L1
attachment.

## Proof-Obligation Boundary

| Obligation | Disposition |
|---|---|
| cubic sites and six-neighbor adjacency | source-bound Lattice wording |
| declared radii `{0,1,2}` and listed separations | explicit finite domain |
| unread box `|x_i| ≤ 6` | explicit finite domain; large enough for these radii |
| occupied-NN count | defined here as `|N(x) ∩ U|` |
| 36-union maxima | proved here |
| unique four-neighbor union and lex-first witness | proved here |
| one-center next-shell maximum `3` | proved here as a control |
| two-seed geometry as Admissibility content | refused |
| L1 attachment | refused |
| new occupancy member | refused |
| pair-member slot census | not this claim |

The proof boundary is **DISPLAYED**: the exact listing closes on the declared
family, while any later physical use remains unadopted.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Lattice wording | site set and six-neighbor adjacency | approved `minimal_axioms` |
| current Admissibility wording | exclusion boundary only | not a two-seed supplier |
| current Record wording | unused as occupancy | no readout assigned to absence |
| two-ball sets `B_r(0) ∪ B_s(p)` | mathematical input | constructed here |
| unread box and occupied-NN count | scoring convention | defined here |
| L1 | not attached | out of scope |
| observational data | input | none |

## Boundary And Non-Claims

- The note does not grow a new occupancy member.
- It does not score leftover-character of a one-center next-shell bound as
  the present claim; that control is used only to isolate the two-center
  witness.
- It is not a pair-member slot census.
- It does not write two-seed geometry into Admissibility.
- It does not attach L1.
- It does not claim a bound for radii larger than `2` or for unlisted
  separations.
- It does not replace six-neighbor adjacency by a larger stencil.
- It assigns no readout value to a site outside `U`.
- It does not edit an axiom or install a framework primitive.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | It answers whether two small ℓ¹ balls can present four occupied six-neighbors to an unread site. |
| V2 | New content? | The durable content is the 36-union listing and the unique `(p,r,s)=((2,0,0),2,2)` witness. |
| V3 | Independently checkable? | Yes. The balls, box, and six-neighbor counts are finite integer geometry. |
| V4 | More than a restatement? | Yes. One-center next-shell maxima stay at `3`; the four-neighbor site is a two-center saddle. |
| V5 | One-step relabel? | No. The claim is a two-ball unread 6-NN census, not a renamed one-center or pair-slot count. |

## No-Go Discipline Gate

The only negative shipped is: on the 35 declared unions other than
`((2,0,0),2,2)`, no unread box site has four occupied six-neighbors. No
global non-derivability, no occupancy no-go, and no axiom obstruction are
claimed.

### N1 — Materially distinct routes

| Route | Attempt and outcome | Marker |
|---|---|---|
| One-center ball | `B_2(0)` has unread occupied-NN maximum `3`; the four-neighbor site requires the second ball | **ATTEMPTED** |
| Closer axial pair `p=(1,0,0)` | even at `r=s=2` the unread maximum stays `3` because the balls overlap too much to leave a four-sided saddle | **ATTEMPTED** |
| Face-diagonal or space-diagonal `p` | all nine radii pairs stay at maximum `≤ 3` | **ATTEMPTED** |
| Smaller radii at `p=(2,0,0)` | `r=s=1` reaches `3` at `(1,-1,0)` but not `4` | **ATTEMPTED** |
| Larger unread box | the witness and all of `U` already sit inside `|x_i| ≤ 4`; enlarging the box cannot add a nearer occupied neighbor | **ATTEMPTED** |

### N2 — Wall independence

This note ships a census, not a closure wall. The only independent
distinctions used are:

- `W1`: one-center versus two-center occupied sets;
- `W2`: listed separations versus unlisted ones;
- `W3`: displayed geometry versus adopted Admissibility content.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---:|---:|---:|
| `W1/W2` | no | no | yes |
| `W1/W3` | no | no | yes |
| `W2/W3` | no | no | yes |

### N3 — Hidden-condition scan

| Phrase/object | Classification |
|---|---|
| radii `{0,1,2}` | explicit finite domain |
| listed four separations | explicit finite domain |
| box `|x_i| ≤ 6` | explicit finite domain |
| six-neighbor stencil | current Lattice adjacency |
| unread as `not in U` | explicit scoring tag |
| occupied as `in U` | explicit scoring tag |
| L1 | named only to refuse attachment |
| Admissibility two-seed write | named only to refuse it |

### N4 — Residual matching

| Witness | Witness residual | Current residual | Match? |
|---|---|---|---:|
| one-center next-shell maximum `3` | a single ball never presents four occupied six-neighbors | isolate the two-center increment | yes |
| pair-member slot census | every listed pair member has a four-slot character of a different kind | refuse to treat this unread 6-NN count as that census | yes |

The residual scored here is whether the union of two small balls can present
four occupied six-neighbors to an unread site. That is the two-ball geometry
question, not a leftover one-center or pair-slot character.

### N5 — Rhetoric audit

- per-element: each unread site in the box is scored by an exact six-neighbor count;
- per-site: the lex-first unread witness and its four occupied neighbors are listed;
- per-mode: no spectral or harmonic claim is used or excluded;
- per-block: each of the 36 declared two-ball unions is scored independently;
- lattice-wide: no lattice-wide occupancy member or axiom write is claimed.

### N6 — Partial-closure path

No partial closure into Admissibility is available from this listing. A later
construction may use the displayed saddle as a geometric example, but that
use would still have to supply its own formation, content, and readout
bridges. Those bridges are not opened here.

### N7 — Hostile steelman

> The site `(1,-1,-1)` is just seeing three neighbors from one ball and one
> leftover from the other, so the result is the one-center bound in disguise.
> Two radius-`2` balls should never be counted as a new residual.

**Answer.** The one-center bound is `3`, and `(1,-1,-1)` is at taxicab
distance `3` from both centers, so it is outside both closed balls. Two of
its occupied neighbors lie in `B_2(0)` and two lie in `B_2((2,0,0))`, with
overlap on the transverse pair `(1,0,-1)` and `(1,-1,0)`. The count `4` is
therefore a two-center saddle, not a renamed next-shell count. The residual
remains the two-ball unread 6-NN question.

### N8 — Cross-cycle echo

A one-center next-shell bound and a pair-member slot census answer different
questions: the first counts neighbors of sites just outside one ball, and
the second counts slots on a listed pair member. The present listing counts
occupied six-neighbors of unread sites for a two-ball union. The analogous
earlier bounds are therefore not imported as this claim, and no L1
attachment is made.

**No-Go Discipline status: PASS** for the narrowed two-ball unread 6-NN
census.

## Primary Runner

The runner constructs the 36 declared unions, scores unread occupied-NN
counts in the box, checks the one-center control, exhibits the lex-first
four-neighbor witness, and checks that the note keeps the census displayed
rather than adopted.
