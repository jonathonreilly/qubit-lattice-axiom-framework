---
claim_id: f_cutmin_two_site_fill_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the unique support-36 F_cut 1-site filler does not fill from the face-diagonal 2-site seed. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cutmin_two_site_fill_2026_08_15.py
---

# The Unique Support-36 `F_cut` Filler Does Not Fill From The Face-Diagonal 2-Site Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** occupancy-to-lock dynamics of the unique support-36 member of the
eight `F_cut` 1-site fillers on the twelve-vertex two-cube from the
face-diagonal seed `{(0,0,0),(1,1,0)}` with off-patch occupancy `0`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cutmin_two_site_fill_2026_08_15.py`](../scripts/f_cutmin_two_site_fill_2026_08_15.py)

## Result up front

On the two-cube `{0,1,2}×{0,1}×{0,1}` the three cuts
`f(empty)=f(full)=0` and `f(c)=f(1-c)` leave `|F_cut|=32`. Exactly four
members fill from the face-diagonal 2-site seed `S={(0,0,0),(1,1,0)}`.
Those four remaining-bit tuples, listed by #6415, are

```text
(wt1, opp2, adj2, vertex3, mixed3)
  = (1, 0, 1, 1, 0), (1, 0, 1, 1, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1).
```

Each has `vertex3=1`. The unique support-36 `F_cut` 1-site filler is the
remaining-bit tuple

```text
(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 0, 0).
```

Call that map `f_cutmin`. Complements of the named remaining orbits are
forced by the three cuts. Because `vertex3=0`, the tuple is **not** among
the four listed fillers.

From `S` with off-patch occupancy `0`, `f_L1` fills and is one of those
four: `|locks_halt|=12`, halt tick `T = 3`, lock history `(2, 7, 11, 12)`,
remaining-bit tuple `(1, 0, 1, 1, 1)`. The same run of `f_cutmin` does
**not** fill: `|locks_halt| = 11`, halt tick `T = 4`, lock history
`(2, 7, 9, 10, 11)`. The unlocked remainder is the single site `(0,1,1)`,
which from the first wave onward sees a `vertex3` neighborhood that
`f_cutmin` silences.

Displayed, not adopted. Do not write f_cutmin into Admissibility.

Not leftover-character of #6415 (that listed fillers). Not leftover-character of #6418 (that is the 1-site halt history). `f_L1` is `n≠0`, not Hamming. The definition is never Hamming.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Whether the unique support-36 F_cut 1-site filler fills the twelve-vertex two-cube from the face-diagonal 2-site seed is an exact finite computation. The map is displayed, not adopted as the physical Admissibility rule."
trace_class: upstream_support
target_claim_id: admissibility_nearest_neighbor_rule
target_blocker_text: "display whether f_cutmin fills from the face-diagonal 2-site seed without writing it into Admissibility"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "keep f_cutmin displayed; do not adopt it or identify it with f_L1 from one seed"
conditional_surface_status: "exact for the twelve-vertex two-cube, face-diagonal 2-site seed, and off-patch occupancy 0; no Z^3-wide formation law"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared objects

The only scientific dependency is the current four-axiom authority
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). That memo
supplies the cubic lattice `Z^3`, proper cubic rotations about each site, and
one fixed nearest-neighbor admissibility rule covariant under lattice
translations and those rotations. Records form; a present record locks exactly
one admissible local possibility. A site with no record cannot be read.

The following are declared finite scaffolding, not a physical-law selection:

- the two-cube `V = {0,1,2}×{0,1}×{0,1}` (twelve vertices);
- the face-diagonal 2-site seed `S = {(0,0,0),(1,1,0)}`;
- off-patch occupancy `0` (a neighbor outside `V` is unread; a blank-block is a different rule);
- the six-direction nearest-neighbor stencil
  `{±e_x, ±e_y, ±e_z}`;
- cube-covariant predicates on occupancy 6-tuples `c ∈ {0,1}^6`.

For each axis `μ`, write `n_μ = c_{+μ} − c_{-μ}`. An axis is **unbalanced**
when `n_μ` is nonzero, **both-occupied** when `c_{+μ}=c_{-μ}=1`, and **empty**
when `c_{+μ}=c_{-μ}=0`. The axis type of `c` is the triple
`(n_unbalanced, n_both, n_empty)`. The 24 proper cube rotations partition the
64 cells into ten axis-type orbits. The named remaining bits are

```text
wt1=(1,0,2), opp2=(0,1,2), adj2=(2,0,1), vertex3=(3,0,0), mixed3=(1,1,1).
```

`F_cut` is the class of cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. The empty/full pair is forced to `0`. Complements of the five
named remaining orbits are forced, so `|F_cut|=32`.

`f_L1(c)=1` if and only if some axis is unbalanced, equivalently
`n_μ = c_{+μ} − c_{-μ}` is nonzero for at least one axis. This is **not** Hamming parity `|c|_1 mod 2`. The definition is never Hamming. Its remaining-bit
tuple is `(1, 0, 1, 1, 1)` and `supp(f_L1)=56`.

`f_cutmin` is the unique `F_cut` 1-site filler with remaining-bit tuple
`(1, 0, 1, 0, 0)`: it fires `wt1` and `adj2` (and their complements) and
silences `opp2`, `vertex3`, and `mixed3`. Support is exact:

```text
supp = 12·wt1 + 6·opp2 + 24·adj2 + 8·vertex3 + 12·mixed3 = 36.
```

A **tick** locks every unlocked site of `V` whose current 6-neighbor occupancy
tuple has predicate value 1. The process starts from `S` and halts at the
first tick `T` with `locks_{T} = locks_{T-1}` (or at `T=0` if the first wave
is empty). Fill means `|locks_halt|=12`. The **lock history** is the sequence
of lock cardinalities from the seed through halt, including the seed count.

## Exact statements

**Theorem 1.** `f_L1` fills `V` from `S` and is one of the four #6415
`F_cut` 2-site fillers. Its remaining-bit tuple is `(1, 0, 1, 1, 1)`, halt
tick `T = 3`, lock history `(2, 7, 11, 12)`. The `f_cutmin` tuple
`(1, 0, 1, 0, 0)` is not among those four: every listed filler has
`vertex3=1`.

**Theorem 2.** Run `f_cutmin` from `S` with off-patch occupancy `0`. The
process halts with `|locks_halt| = 11`, `T = 4`, lock history
`(2, 7, 9, 10, 11)`. Reported lock history (2, 7, 9, 10, 11). It does not
fill. The single unlocked site at halt is `(0,1,1)`.

**Theorem 3.** The non-fill and the lock history `(2, 7, 9, 10, 11)` are
displayed. Do not adopt `f_cutmin`. Do not write `f_cutmin` into
Admissibility. A 1-site fill with a different history (#6418) does not
license an identity of members, and exclusion from the four 2-site fillers
does not write a selector into Admissibility.

### Computed values

| object | value |
|---|---|
| `\|V\|` | 12 |
| seed | `{(0,0,0),(1,1,0)}` |
| off-patch occupancy | `0` |
| `\|F_cut\|` | 32 |
| `N_cut2` | 4 |
| listed #6415 tuples | `(1,0,1,1,0)`, `(1,0,1,1,1)`, `(1,1,1,1,0)`, `(1,1,1,1,1)` |
| `f_cutmin` named tuple | `(1, 0, 1, 0, 0)` |
| `f_cutmin` among the four | no (`vertex3=0`) |
| `supp(f_cutmin)` | 36 |
| `f_cutmin ∈ F_cut` | yes |
| `f_cutmin` halt locks | 11 |
| `f_cutmin` halt tick `T` | 4 |
| `f_cutmin` lock history | `(2, 7, 9, 10, 11)` |
| `f_cutmin` fills | no |
| stuck site | `(0,1,1)` |
| `f_L1` named tuple | `(1, 0, 1, 1, 1)` |
| `f_L1` lock history | `(2, 7, 11, 12)` |
| `f_L1` fills | yes |

On this seed the first wave coincides with L1: the pair `S`; then the five
sites `(0,0,1)`, `(0,1,0)`, `(1,0,0)`, `(1,1,1)`, `(2,1,0)` (cardinality 7).
At the next tick `f_L1` locks four further sites (cardinality 11), including
`(0,1,1)` and `(1,0,1)`, both of which then see a `vertex3` neighborhood.
`f_cutmin` silences `vertex3`, so those two sites stay unlocked at
cardinality 9 while `(2,0,0)` and `(2,1,1)` lock on `adj2`. Tick 3 locks
`(2,0,1)` (cardinality 10). Tick 4 locks `(1,0,1)` once its neighborhood
has left `vertex3` (cardinality 11). The site `(0,1,1)` keeps the occupancy
word `(1,0,0,1,0,1)` — three on-patch neighbors locked, three off-patch
slots unread — which is `vertex3` forever, so the process halts short of
fill.

## No-Go Discipline

The note is a displayed finite history of one named map on one seed, not a
no-go against other members or against a later derived Admissibility
selector.

No-Go Discipline disposition: **PASS**

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| adopt `f_cutmin` because it is the unique support-36 `F_cut` 1-site filler | **ATTEMPTED** | support uniqueness is a prior identity; this lane only runs the 2-site history |
| treat exclusion from the four #6415 tuples as leftover-character of that list | **ATTEMPTED** | #6415 listed the fillers; it did not run `f_cutmin` or report its halt |
| treat the 1-site fill of #6418 as this residual | **ATTEMPTED** | #6418 is the 1-site history `(1, 4, 8, 10, 11, 12)`; this seed is the face-diagonal pair |
| treat Hamming-parity formation as this residual | **ATTEMPTED** | Hamming is a different member and does not fill |
| identify `f_cutmin` with `f_L1` because both fill from 1-site | **ATTEMPTED** | the 2-site histories differ; `vertex3` still differs |
| write `f_cutmin` into Admissibility | **ATTEMPTED** | the history is displayed; no axiom or approved primitive is added |

### N2 — wall independence

One computational wall is claimed: this named map does not fill this seed.
The four-tuple list of #6415 is a prior census, not a second impossibility
wall.

### N3 — hidden-wall scan

The two-cube, seed, off-patch occupancy `0`, six-direction stencil, three
cuts, and axis-type orbits are declared. No `Z^3`-wide formation law, physical
Admissibility selector, Hamming identification, or continuum extension is
imported.

### N4 — residual matching

The residual after #6415 is the executable lock history of the support-36
member that was *not* on the filler list. The residual after #6418 is a
different seed. This note reports only the face-diagonal 2-site halt of
`f_cutmin`.

### N5 — certificate granularity

```text
per-element: executed — each of the 64 neighbor 6-tuples is assigned its axis-type orbit
per-site: executed — each of the twelve two-cube vertices uses the same six-direction stencil
per-mode: executed — every F_cut map is classified as a 2-site filler or not
per-block: executed — f_cutmin is run to a fixed point from the face-diagonal 2-site seed
lattice-wide: not executed — no Z^3-wide formation law or Admissibility rewrite is claimed
```

### N6 — partial-closure paths

A later derivation could still select `f_L1`, select `f_cutmin`, or select
neither. A non-fill on this seed leaves those routes live. A different seed
or a later selector can still prefer either map.

### N7 — steelman

The strongest objection is that `(0,1,1)` is a patch-corner artifact of
off-patch occupancy `0`, so `f_cutmin` remains interchangeable with the
four fillers for every later argument. Incorrect on the stated objects:
the predicates differ on `vertex3`, the lock *sets* differ from tick 2
onward, and the stuck neighborhood is exactly the silenced type. Changing
the off-patch default would be a different declared rule.

### N8 — cross-cycle echo

#6415 named the four `F_cut` 2-site fillers and stopped at the list.
#6418 named the 1-site halt of `f_cutmin`. Hamming and `f_min` 2-site
lanes execute other members. This note adds only the face-diagonal 2-site
halt of the already-named support-36 `F_cut` member.

## Boundaries and explicit non-claims

- The theorem is conditional on the two-cube, the face-diagonal 2-site seed,
  and off-patch occupancy `0`.
- A non-fill on this seed is not an identity of members, and a fill on
  another seed would not be an identity either.
- `f_cutmin` is displayed, not adopted.
- Do not write `f_cutmin` into Admissibility.
- No `Z^3`-wide formation process, rate, or physical-law selection is claimed.
- No axiom, approved primitive, registry, or audit verdict is edited.

## Verification

Run:

```bash
python3 scripts/f_cutmin_two_site_fill_2026_08_15.py
```

The runner rebuilds the 24 proper rotations and ten axis-type orbits,
recomputes the 32-element `F_cut` and its four 2-site fillers, isolates
`f_cutmin` as the remaining-bit tuple `(1, 0, 1, 0, 0)`, and runs
`f_cutmin` and `f_L1` from `S`. Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
