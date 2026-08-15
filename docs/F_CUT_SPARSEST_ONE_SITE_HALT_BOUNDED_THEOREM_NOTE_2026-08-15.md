---
claim_id: f_cut_sparsest_one_site_halt_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the unique support-36 F_cut 1-site filler (tuple (1, 0, 1, 0, 0)) halts at tick T = 5 with lock history (1, 4, 8, 10, 11, 12). Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_sparsest_one_site_halt_2026_08_15.py
---

# Halt Dynamics Of The Unique Support-36 `F_cut` One-Site Filler

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** occupancy-to-lock dynamics of the unique support-36 member of the
eight `F_cut` 1-site fillers on the twelve-vertex two-cube from the seed
`(0,0,0)` with off-patch occupancy `0`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_sparsest_one_site_halt_2026_08_15.py`](../scripts/f_cut_sparsest_one_site_halt_2026_08_15.py)

## Result up front

On the two-cube `{0,1,2}×{0,1}×{0,1}` the three cuts
`f(empty)=f(full)=0` and `f(c)=f(1-c)` leave `|F_cut|=32`. Exactly eight
members fill from the 1-site seed. Among those eight the unique minimal
support is 36, attained only at the remaining-bit tuple

```text
(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 0, 0).
```

Call that map `f_cutmin`. Complements of the named remaining orbits are
forced by the three cuts. From the 1-site seed `(0,0,0)` with off-patch
occupancy `0` it fills: `|locks_halt|=12`, halt tick `T = 5`, lock history
`(1, 4, 8, 10, 11, 12)`.

The L1 map `f_L1(c)=1` if and only if some axis is unbalanced fills from the
same seed with history `(1, 4, 8, 11, 12)` and support 56. The `f_cutmin`
history does **not** equal the L1 history: silencing `vertex3` and `mixed3`
delays the last two locks by one tick and changes the cardinality sequence.
Displayed, not adopted. Do not write f_cutmin into Admissibility.

Not leftover-character of #6414 (support only). Not leftover-character of #6411 (that is `f_min`, which is not in `F_cut`). `f_L1` is `n≠0`, not Hamming.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The unique support-36 F_cut 1-site filler, its halt tick, and its lock history on the twelve-vertex two-cube are exact finite computations. The map is displayed, not adopted as the physical Admissibility rule."
trace_class: upstream_support
target_claim_id: admissibility_nearest_neighbor_rule
target_blocker_text: "display the unique F_cut support-minimizer as an executable occupancy-to-lock history without writing it into Admissibility"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "keep f_cutmin displayed; do not adopt it or identify it with f_L1 from one 1-site history"
conditional_surface_status: "exact for the twelve-vertex two-cube, 1-site seed, and off-patch occupancy 0; no Z^3-wide formation law"
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
- the 1-site seed `S_0 = {(0,0,0)}`;
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

`f_min` is the unique support-26 filler among the 96 cube-covariant 1-site
fillers. Its tuple is `(1, 0, 1, 1, 0)`. It is not complement-even and is
not in `F_cut`.

A **tick** locks every unlocked site of `V` whose current 6-neighbor occupancy
tuple has predicate value 1. The process starts from `S_0` and halts at the
first tick `T` with `locks_{T} = locks_{T-1}` (or at `T=0` if the first wave
is empty). Fill means `|locks_halt|=12`. The **lock history** is the sequence
of lock cardinalities from the seed through halt, including the seed count.

## Exact statements

**Theorem 1.** Among the 32 members of `F_cut`, exactly eight fill `V` from
`S_0`. The unique support-36 filler among those eight is `f_cutmin`, the
remaining-bit tuple `(1, 0, 1, 0, 0)`. It fills: `|locks_halt|=12`,
`T = 5`, lock history `(1, 4, 8, 10, 11, 12)`.

**Theorem 2.** `f_L1` fills from the same seed with lock history
`(1, 4, 8, 11, 12)`. The `f_cutmin` history does not equal the L1 history.

**Theorem 3.** The history `(1, 4, 8, 10, 11, 12)` is displayed. Do not
adopt `f_cutmin`. Do not write `f_cutmin` into Admissibility. Unequal 1-site
histories do not license an identity of members, and neither does the
support-minimality of `f_cutmin` inside `F_cut`.

### Computed values

| object | value |
|---|---|
| `\|V\|` | 12 |
| seed | `(0,0,0)` |
| off-patch occupancy | `0` |
| `\|F_cut\|` | 32 |
| `N_fill_cut` | 8 |
| `supp(f_cutmin)` | 36 |
| `N_min_cut` | 1 |
| `f_cutmin` named tuple | `(1, 0, 1, 0, 0)` |
| `f_cutmin ∈ F_cut` | yes |
| `f_cutmin` halt locks | 12 |
| `f_cutmin` halt tick `T` | 5 |
| `f_cutmin` lock history | `(1, 4, 8, 10, 11, 12)` |
| `supp(f_L1)` | 56 |
| `f_L1` named tuple | `(1, 0, 1, 1, 1)` |
| `f_L1` lock history | `(1, 4, 8, 11, 12)` |
| histories equal | no |
| `f_min` named tuple | `(1, 0, 1, 1, 0)` |
| `f_min ∈ F_cut` | no |

On this seed the first two waves coincide with L1: the seed; then the three
axis neighbors; then the four weight-2 sites of the seeded cube together with
`(2,0,0)`. At the next tick `f_L1` locks three further sites (cardinality 11),
while `f_cutmin` locks only `(2,0,1)` and `(2,1,0)` (cardinality 10): the
space-diagonal site `(1,1,1)` first sees a `vertex3` neighborhood, which
`f_cutmin` silences. Tick 4 then locks `(2,1,1)` (cardinality 11). Tick 5
locks `(1,1,1)` once its neighborhood has left `vertex3`, completing the
two-cube.

## No-Go Discipline

The note is a displayed finite history, not a no-go against other members or
against a later derived Admissibility selector.

No-Go Discipline disposition: **PASS**

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| adopt `f_cutmin` because it is the unique support-36 `F_cut` filler | **ATTEMPTED** | uniqueness of support is the #6414 identity; this lane only runs the history |
| treat the 1-site history as identifying `f_cutmin` with `f_L1` | **ATTEMPTED** | the histories differ; `vertex3` and `mixed3` still differ |
| treat this residual as leftover-character of #6414 | **ATTEMPTED** | #6414 reported support only; it did not report `T` or the lock sequence |
| treat this residual as leftover-character of #6411 | **ATTEMPTED** | #6411 is `f_min`, the support-26 filler outside `F_cut` |
| treat Hamming-parity formation as this residual | **ATTEMPTED** | Hamming is a different member and does not fill |
| write `f_cutmin` into Admissibility | **ATTEMPTED** | the history is displayed; no axiom or approved primitive is added |

### N2 — wall independence

One computational wall is claimed: the halt tick and lock history of this
named map on this seed. Uniqueness of support 36 inside `F_cut` is a prior
identity, not a second impossibility wall.

### N3 — hidden-wall scan

The two-cube, seed, off-patch occupancy `0`, six-direction stencil, three
cuts, and axis-type orbits are declared. No `Z^3`-wide formation law, physical
Admissibility selector, Hamming identification, or continuum extension is
imported.

### N4 — residual matching

The residual after #6414 is the executable lock history of the named `F_cut`
minimizer, not a restatement of its support. The residual after #6411 is a
different member (`f_min`). This note reports only the 1-site halt history of
`f_cutmin`.

### N5 — certificate granularity

```text
per-element: executed — each of the 64 neighbor 6-tuples is assigned its axis-type orbit
per-site: executed — each of the twelve two-cube vertices uses the same six-direction stencil
per-mode: executed — every F_cut map is classified as a 1-site filler or not
per-block: executed — the unique support-36 F_cut filler is run to a fixed point from the 1-site seed
lattice-wide: not executed — no Z^3-wide formation law or Admissibility rewrite is claimed
```

### N6 — partial-closure paths

A later derivation could still select `f_L1`, select `f_cutmin`, or select
neither. Unequal 1-site histories leave those routes live. A different seed
or a later selector can still prefer either map.

### N7 — steelman

The strongest objection is that a one-tick delay on two sites is a patch
artifact of silencing `vertex3` on this seed, so the maps remain interchangeable
for every later argument. Incorrect on the stated objects: the predicates
differ on `vertex3` and `mixed3`, the lock *sets* differ from tick 3 onward,
and a neighborhood of either silenced type can split them on this patch or
another seed.

### N8 — cross-cycle echo

#6414 named the unique support-36 `F_cut` filler and stopped at support.
#6411 named `f_min`, which is not in `F_cut`. Hamming and `f_min` 1-site
lanes execute other members. This note adds only the 1-site halt history of
the already-named `F_cut` support-minimizer.

## Boundaries and explicit non-claims

- The theorem is conditional on the two-cube, the 1-site seed, and off-patch
  occupancy `0`.
- Unequal lock histories are not an identity of members, and equal histories
  on another seed would not be an identity either.
- `f_cutmin` is displayed, not adopted.
- Do not write `f_cutmin` into Admissibility.
- No `Z^3`-wide formation process, rate, or physical-law selection is claimed.
- No axiom, approved primitive, registry, or audit verdict is edited.

## Verification

Run:

```bash
python3 scripts/f_cut_sparsest_one_site_halt_2026_08_15.py
```

The runner rebuilds the 24 proper rotations and ten axis-type orbits,
recomputes the 32-element `F_cut` and its eight 1-site fillers, isolates the
unique support-36 map, and runs `f_cutmin` and `f_L1` from `(0,0,0)`.
Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
