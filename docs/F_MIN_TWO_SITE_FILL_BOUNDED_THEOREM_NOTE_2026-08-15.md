---
claim_id: f_min_two_site_fill_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the nonempty n_both=0 map f_min does fill from the face-diagonal 2-site seed. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_min_two_site_fill_2026_08_15.py
---

# The Nonempty n_both=0 Map Fills From The Face-Diagonal 2-Site Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact lock dynamics of two displayed cube-covariant maps on the
twelve-site two-cube `{0,1,2}×{0,1}×{0,1}` with off-patch occupancy `o=0`,
started from the face-diagonal seed `S={(0,0,0),(1,1,0)}`. The nonempty
`n_both=0` map `f_min` is displayed, not adopted. It is not written into
Admissibility.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_min_two_site_fill_2026_08_15.py`](../scripts/f_min_two_site_fill_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write the two-cube as the twelve lattice sites `{0,1,2}×{0,1}×{0,1}`. Off-patch
nearest-neighbor slots carry occupancy `0`. A site starts locked exactly when
it belongs to the seed. At each tick every unlocked site is inspected on its
six-neighbor occupancy word `c`. The word is scored by axis type
`(n_unbalanced, n_both, n_empty)` with
`n_unbalanced + n_both + n_empty = 3`. The process halts when a tick adds no
new lock.

The displayed maps are:

- `f_L1(c)=1` if and only if some axis is unbalanced (`n_unbalanced≥1`).
  f_L1 is n≠0, not Hamming.
- `f_min(c)=1` if and only if `n_both(c)=0` and some axis is unbalanced.

On this seed, `f_L1` fills: `T=3`, `|locks_halt|=12`, lock history
`(2, 7, 11, 12)`. The same run of `f_min` also fills: `T=3`,
`|locks_halt|=12`, lock history `(2, 7, 11, 12)`. The two maps therefore
have the same lock history on this seed. That agreement is a computed
comparison, not an identity of the maps: they still disagree on the mixed3
orbit `(1,1,1)`, and `f_min` is not in `F_cut`.

Do not adopt `f_min`. Displayed, not adopted.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Admissibility is not a dynamics axiom.

The only use of Admissibility is to identify the local nearest-neighbor
condition domain. The axiom does not specify lock-update values and
does not supply the formation site, probability, or rate.

The current Record boundary is:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Record supplies no scalar collection functional, no finite additivity, and no
value at absence. Using the computed locks as physical records would require a
formation rule and a content/readout identification; both remain open. The
lock process below is a displayed occupancy-to-readiness map on a finite
patch, not a Record derivation.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The face-diagonal 2-site halt histories of f_min and f_L1 are finite exact enumerations on a 12-site patch; f_min is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: f_min_two_site_fill
target_blocker_text: "whether the nonempty n_both=0 map fills from the face-diagonal 2-site seed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded fill comparison; do not adopt f_min"
conditional_surface_status: "exact on the twelve-site two-cube with off-patch o=0 and the displayed face-diagonal seed; no axiom edit and no physical formation compiler"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

The two-cube is the set

```text
V = {0,1,2} × {0,1} × {0,1},    |V| = 12.
```

Each site has six lattice neighbor slots, two per axis. A slot that lands
outside `V` is off-patch and carries occupancy `o=0`. For a lock set `L`, the
occupancy of a slot at `x±e_i` is `1` if that neighbor is in `L`, else `0` on
`V`, else `o`. An axis is empty, unbalanced, or both-occupied according as its
two slots contain `0`, `1`, or `2` locked neighbors.

The axis-type orbits used to name cube-covariant maps are

```text
wt1=(1,0,2), opp2=(0,1,2), adj2=(2,0,1), vertex3=(3,0,0), mixed3=(1,1,1).
```

Empty is `(0,0,3)` and full is `(0,3,0)`. Complement of occupancy bits sends
`(n_unbalanced, n_both, n_empty)` to `(n_unbalanced, n_empty, n_both)`. The
class `F_cut` consists of the cube-covariant maps with `f(empty)=f(full)=0`
and `f(c)=f(1-c)` for every six-bit word.

On those orbits, `f_min` has bits `(1,0,1,1,0)` and `f_L1` has bits
`(1,0,1,1,1)`. In particular `f_min(mixed3)=0` while `f_L1(mixed3)=1`, so
the maps are distinct. Complement takes `wt1` to `(1,2,0)`, where
`f_min=0`, so `f_min` is not complement-even and is not in `F_cut`. By
contrast `n_unbalanced` is complement-invariant, `f_L1(empty)=f_L1(full)=0`,
and `f_L1` does sit in `F_cut`.

The seed is the face-diagonal pair `S={(0,0,0),(1,1,0)}`. Graph distance
inside `V` is `2`; the pair is not a nearest-neighbor edge.

A run of a map `f` is the nondecreasing lock-count tuple starting from `|S|`,
updated synchronously by locking every unlocked site whose current six-neighbor
word has `f=1`, until a tick adds nothing. Fill means `|locks_halt|=12`. The
halt tick `T` is the last tick that added a lock.

## Theorem 1 — `f_L1` fills from the face-diagonal seed

Run `f_L1` from `S` with `o=0`. The first wave locks the five sites

```text
(0,0,1), (0,1,0), (1,0,0), (1,1,1), (2,1,0).
```

Each of those sites sees at least one unbalanced axis against the two seed
locks. The second wave locks four further sites; the third wave locks the
remaining site `(2,0,1)`. The run therefore has

```text
T=3,    |locks_halt|=12,    history (2, 7, 11, 12).
```

So `f_L1` fills from this seed. That is the same fill boolean previously
displayed for this seed; it is recomputed here and is not imported as a
status.

## Theorem 2 — `f_min` fills from the same seed

Run `f_min` from the same `S` with the same `o=0`. Every site that `f_L1`
locks on this run has `n_both=0` at the tick it becomes ready, so `f_min`
accepts the same words. The run has

```text
T=3,    |locks_halt|=12,    history (2, 7, 11, 12).
```

Therefore `f_min` fills from the face-diagonal 2-site seed. Fill is a
computed halt fact on this finite patch, not an identity of `f_min` with
`f_L1` and not a membership of `f_min` in `F_cut`.

The 1-site seed `(0,0,0)` and the 3-site long-axis seed
`{(0,0,0),(1,0,0),(2,0,0)}` are different seeds. Their lock histories
`(1, 4, 8, 11, 12)` and `(3, 9, 12)` are recovered by the same engine as a
sanity check; they are not this theorem.

## Theorem 3 — comparison is displayed; `f_min` is not adopted

On this seed the two halt records agree: same `T`, same `|locks_halt|`,
same lock history. The comparison is displayed.

The maps remain distinct. `f_L1` fires on mixed3 and is one of the
complement-even fillers of this seed. `f_min` kills mixed3, is the unique
support-26 1-site filler among cube-covariant maps with `f(empty)=0`, and
is not in `F_cut`. Hamming parity of the six-bit word is a third map:
from this seed it halts at `9` locks and does not fill. The `u≥2` map
from this seed locks only `4` sites. Those contrasts are mutation controls,
not adopted members.

Do not adopt `f_min`. Do not write `f_min` into Admissibility. Displayed,
not adopted.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice, Admissibility, and Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, face-diagonal seed | declared finite data |
| `f_L1` is n≠0, not Hamming | executed orbit contrast |
| `f_min` definition and `F_cut` non-membership | executed on axis-type orbits |
| `f_L1` fill from `S` | executed; fills |
| `f_min` halt locks, `T`, history, fill boolean | executed; fills |
| comparison without adoption | displayed; no axiom edit |
| physical formation / Record compiler | open |

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice, Admissibility, and Record
  sentences quoted above. They are quoted without rewrite.
- **Explicit theorem-domain condition:** the twelve-site two-cube, off-patch
  occupancy `0`, the face-diagonal seed, and the two displayed predicates.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** formation site, record content, and any writing of
  `f_min` or `f_L1` into Admissibility remain outside the target proved here.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether the already-named nonempty `n_both=0` map fills from the face-diagonal 2-site seed. |
| V2 | The 1-site and 3-site-line histories of `f_min` are different seeds; the `F_cut` census of this seed does not include `f_min`. |
| V3 | Both runs are independently finite and exact. |
| V4 | Agreement of histories on this seed is not an identity of the maps and does not place `f_min` in `F_cut`. |
| V5 | The map is not adopted and is not written into Admissibility. |

## No-Go Discipline Gate

The negative content is narrow: fill on this seed does not adopt `f_min`,
does not identify it with `f_L1`, and does not write a lock rule into
Admissibility. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| `f_L1` (`n≠0`) | run from `S` | fills; history `(2, 7, 11, 12)` |
| `f_min` (`n_both=0` and `n_unbalanced≥1`) | run from `S` | fills; same history |
| Hamming parity | run from `S` | does not fill; different history |
| `u≥2` | run from `S` | four locks; no fill |
| 1-site seed | same maps, different seed | history `(1, 4, 8, 11, 12)`; not this theorem |
| 3-site line seed | same maps, different seed | history `(3, 9, 12)`; not this theorem |
| off-patch occupancy `1` | change the off-patch selector | different `f_min` history |
| write `f_min` into Admissibility | treat the displayed bits as axiom content | refused; no edit |

### N2 — wall independence

Non-membership in `F_cut`, disagreement on mixed3, and the missing formation
mechanism are distinct residuals. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the off-patch value `0`, the seed, the synchronous lock update,
and both predicates are declared. Cube covariance of the predicates is the
restriction to axis-type orbits already used to name them. No continuum
limit, no Hamming-as-`f_L1` identification, and no physical readout are
assumed.

### N4 — source residual matching

The current axiom memo supplies the cubic nearest-neighbor substrate and the
local-law sentence. Admissibility is not a dynamics axiom and does not supply
the formation site, probability, or rate. The residual therefore matches
current sources: a displayed finite lock map, not an axiom clause.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | six-neighbor axis-type words | no exhaustive 64-bit naming beyond orbits |
| per site | readiness at each of the twelve sites | no physical record at those sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | face-diagonal runs of `f_min` and `f_L1` | no `F_cut` census in this note |
| lattice wide | checked and not executed | no infinite-lattice fill theorem |

### N6 — live partial-closure paths

Live routes are a derived formation mechanism, a content/readout
identification, and any later decision to adopt or reject `f_min` as a
named member. Distinguishing seeds on which the two histories part, if any,
are a separate map.

### N7 — hostile steelman

**Steelman:** Because `f_min` and `f_L1` share the 1-site history, the
3-site-line history, and now the face-diagonal history, they are the same
filler and `f_min` may be treated as the L1 member.

**Answer:** They disagree on mixed3, and `f_min` fails complement-evenness.
Shared halt history on three displayed seeds is a comparison of runs, not
an identity of predicates. Hamming and `u≥2` from the same seed already
produce different halt records.

### N8 — cross-cycle echo

Prior 1-site and 3-site-line runs of `f_min` are different seeds. Prior
`F_cut` fill counts on this seed do not include `f_min`. This note does not
retroactively enlarge those claims and does not write a seed or a predicate
into Admissibility.

**Gate disposition:** PASS for the finite fill comparison on the displayed
seed. FAIL / DO NOT SHIP for “`f_min` is adopted,” “`f_min` is `f_L1`,”
“`f_min` is in `F_cut`,” or “Admissibility now contains this lock rule.”

## Primary Runner

The primary runner recomputes axis-type bits, `F_cut` non-membership, the
1-site and line sanity histories, the face-diagonal runs of `f_min` and
`f_L1`, Hamming and `u≥2` mutation controls, the current premise boundary,
and the display-only contract. It authors no audit verdict.
