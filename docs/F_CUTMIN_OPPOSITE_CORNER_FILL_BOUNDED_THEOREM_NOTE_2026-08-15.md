---
claim_id: f_cutmin_opposite_corner_fill_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the unique support-36 F_cut 1-site filler does not fill from the opposite-corner 2-site seed. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cutmin_opposite_corner_fill_2026_08_15.py
---

# The Unique Support-36 `F_cut` Filler Does Not Fill From The Opposite-Corner 2-Site Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** occupancy-to-lock dynamics of the unique support-36 member of the
eight `F_cut` 1-site fillers on the twelve-vertex two-cube from the
opposite-corner seed `{(0,0,0),(2,1,1)}` with off-patch occupancy `0`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cutmin_opposite_corner_fill_2026_08_15.py`](../scripts/f_cutmin_opposite_corner_fill_2026_08_15.py)

## Result up front

On the two-cube `{0,1,2}×{0,1}×{0,1}` the three cuts
`f(empty)=f(full)=0` and `f(c)=f(1-c)` leave `|F_cut|=32`. The unique
support-36 `F_cut` 1-site filler is the remaining-bit tuple

```text
(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 0, 0).
```

Call that map `f_cutmin`. Complements of the named remaining orbits are
forced by the three cuts.

From the opposite-corner seed `S*={(0,0,0),(2,1,1)}` with off-patch occupancy
`0`, `f_L1` fills with lock history `(2, 8, 12)` (#6417). The same seed is
the first `|S|≤3` seed at which `f_min` and `f_L1` disagree: `f_min` does
not fill. The same run of `f_cutmin` does **not** fill: `|locks_halt| = 10`,
halt tick `T = 2`, lock history `(2, 8, 10)`. Reported lock history (2, 8, 10).
The unlocked remainder is the pair `{(0,1,1),(2,0,0)}`, the two sites that
from the first wave onward see a `vertex3` neighborhood that `f_cutmin`
silences.

Displayed, not adopted. Do not write f_cutmin into Admissibility.

Not leftover-character of #6421 (that is the face-diagonal 2-site, a
different seed). Not leftover-character of #6417 (that compared `f_L1`
with `f_min`). `f_L1` is `n≠0`, not Hamming. The definition is never Hamming.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Whether the unique support-36 F_cut 1-site filler fills the twelve-vertex two-cube from the opposite-corner 2-site seed is an exact finite computation. The map is displayed, not adopted as the physical Admissibility rule."
trace_class: upstream_support
target_claim_id: admissibility_nearest_neighbor_rule
target_blocker_text: "display whether f_cutmin fills from the opposite-corner 2-site seed without writing it into Admissibility"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "keep f_cutmin displayed; do not adopt it or identify it with f_L1 from one seed"
conditional_surface_status: "exact for the twelve-vertex two-cube, opposite-corner 2-site seed, and off-patch occupancy 0; no Z^3-wide formation law"
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
- the opposite-corner 2-site seed `S* = {(0,0,0),(2,1,1)}`;
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

`f_min(c)=1` if and only if `n_both=0` and some axis is unbalanced. That
map is outside `F_cut`. It is displayed only as the #6417 comparison
member, not adopted.

`f_cutmin` is the unique `F_cut` 1-site filler with remaining-bit tuple
`(1, 0, 1, 0, 0)`: it fires `wt1` and `adj2` (and their complements) and
silences `opp2`, `vertex3`, and `mixed3`. Support is exact:

```text
supp = 12·wt1 + 6·opp2 + 24·adj2 + 8·vertex3 + 12·mixed3 = 36.
```

A **tick** locks every unlocked site of `V` whose current 6-neighbor occupancy
tuple has predicate value 1. The process starts from `S*` and halts at the
first tick `T` with `locks_{T} = locks_{T-1}` (or at `T=0` if the first wave
is empty). Fill means `|locks_halt|=12`. The **lock history** is the sequence
of lock cardinalities from the seed through halt, including the seed count.

## Exact statements

**Theorem 1.** `f_L1` fills `V` from `S*` with lock history `(2, 8, 12)`
and halt tick `T = 2` (#6417). `f_min` does not fill from `S*`: it halts
with `|locks_halt| = 10`, lock history `(2, 8, 10)`, stuck pair
`{(1,0,1),(1,1,0)}`.

**Theorem 2.** Run `f_cutmin` from `S*` with off-patch occupancy `0`. The
process halts with `|locks_halt| = 10`, `T = 2`, lock history
`(2, 8, 10)`. Reported lock history (2, 8, 10). It does not fill. The
unlocked sites at halt are `(0,1,1)` and `(2,0,0)`.

**Theorem 3.** The comparison is displayed. `f_L1` fills; `f_cutmin` and
`f_min` both halt at cardinality 10 after a shared first wave of six `wt1`
locks, but they leave complementary stuck pairs. Do not adopt `f_cutmin`.
Do not write `f_cutmin` into Admissibility. A 1-site fill with a different
history (#6418) and a face-diagonal non-fill (#6421) do not license an
identity of members, and a split against `f_min` (#6417) does not write a
selector into Admissibility.

### Computed values

| object | value |
|---|---|
| `\|V\|` | 12 |
| seed | `{(0,0,0),(2,1,1)}` |
| off-patch occupancy | `0` |
| `\|F_cut\|` | 32 |
| `f_cutmin` named tuple | `(1, 0, 1, 0, 0)` |
| `supp(f_cutmin)` | 36 |
| `f_cutmin ∈ F_cut` | yes |
| `f_cutmin` halt locks | 10 |
| `f_cutmin` halt tick `T` | 2 |
| `f_cutmin` lock history | `(2, 8, 10)` |
| `f_cutmin` fills | no |
| `f_cutmin` stuck sites | `(0,1,1)`, `(2,0,0)` |
| `f_L1` named tuple | `(1, 0, 1, 1, 1)` |
| `f_L1` lock history | `(2, 8, 12)` |
| `f_L1` fills | yes |
| `f_min` lock history | `(2, 8, 10)` |
| `f_min` fills | no |
| `f_min` stuck sites | `(1,0,1)`, `(1,1,0)` |

On this seed the first wave coincides for `f_cutmin`, `f_L1`, and `f_min`:
the pair `S*`; then the six sites `(0,0,1)`, `(0,1,0)`, `(1,0,0)`,
`(1,1,1)`, `(2,0,1)`, `(2,1,0)` (cardinality 8). Each of those six sites
sees a single on-patch locked neighbor, a `wt1` neighborhood that all
three maps fire. Four sites remain: `(0,1,1)`, `(1,0,1)`, `(1,1,0)`,
`(2,0,0)`.

At the next tick `f_L1` locks all four remainders (cardinality 12): each
has at least one unbalanced axis. `f_cutmin` locks only `(1,0,1)` and
`(1,1,0)`, both of which see an `adj2`-complement neighborhood
`(n_unbalanced, n_both, n_empty)=(2,1,0)`. The pair `(0,1,1)` and
`(2,0,0)` each see a `vertex3` neighborhood — three on-patch neighbors
locked, three off-patch slots unread — which `f_cutmin` silences, so the
process halts at cardinality 10. Those two `vertex3` words are unchanged
by the two `adj2` locks, so the halt is a genuine fixed point.

`f_min` is complementary on the same four remainders: it fires `vertex3`
(`n_both=0` and three unbalanced axes) and silences `adj2`-complement
(`n_both=1`), so it locks `(0,1,1)` and `(2,0,0)` and leaves
`{(1,0,1),(1,1,0)}` stuck. Same history cardinalities as `f_cutmin`,
different lock sets.

## No-Go Discipline

The note is a displayed finite history of one named map on one seed, not a
no-go against other members or against a later derived Admissibility
selector.

No-Go Discipline disposition: **PASS**

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| adopt `f_cutmin` because it is the unique support-36 `F_cut` 1-site filler | **ATTEMPTED** | support uniqueness is a prior identity; this lane only runs the opposite-corner history |
| treat the face-diagonal non-fill of #6421 as leftover-character of that seed | **ATTEMPTED** | #6421 is `{(0,0,0),(1,1,0)}`; this seed is `S*={(0,0,0),(2,1,1)}` |
| treat the #6417 split of `f_L1` against `f_min` as this residual | **ATTEMPTED** | #6417 compared those two members; it did not run `f_cutmin` |
| treat Hamming-parity formation as this residual | **ATTEMPTED** | Hamming is a different member and does not fill |
| identify `f_cutmin` with `f_min` because both halt at cardinality 10 | **ATTEMPTED** | the stuck pairs are complementary; `vertex3` still differs |
| write `f_cutmin` into Admissibility | **ATTEMPTED** | the history is displayed; no axiom or approved primitive is added |

### N2 — wall independence

One computational wall is claimed: this named map does not fill this seed.
The #6417 fill of `f_L1` and non-fill of `f_min` are prior member
histories, not a second impossibility wall.

### N3 — hidden-wall scan

The two-cube, seed, off-patch occupancy `0`, six-direction stencil, three
cuts, and axis-type orbits are declared. No `Z^3`-wide formation law, physical
Admissibility selector, Hamming identification, or continuum extension is
imported.

### N4 — residual matching

The residual after #6421 is the executable lock history of the same
support-36 member on a different seed. The residual after #6417 is a
third member on the already-named distinguishing seed. This note reports
only the opposite-corner 2-site halt of `f_cutmin`.

### N5 — certificate granularity

```text
per-element: executed — each of the 64 neighbor 6-tuples is assigned its axis-type orbit
per-site: executed — each of the twelve two-cube vertices uses the same six-direction stencil
per-mode: executed — f_cutmin, f_L1, and f_min are classified as fill or non-fill from S*
per-block: executed — f_cutmin is run to a fixed point from the opposite-corner 2-site seed
lattice-wide: not executed — no Z^3-wide formation law or Admissibility rewrite is claimed
```

### N6 — partial-closure paths

A later derivation could still select `f_L1`, select `f_cutmin`, or select
neither. A non-fill on this seed leaves those routes live. A different seed
or a later selector can still prefer either map.

### N7 — steelman

The strongest objection is that `(0,1,1)` and `(2,0,0)` are patch-corner
artifacts of off-patch occupancy `0`, so `f_cutmin` remains interchangeable
with `f_L1` for every later argument. Incorrect on the stated objects: the
predicates differ on `vertex3`, the lock *sets* differ from tick 1 onward,
and the stuck neighborhoods are exactly the silenced type. Changing the
off-patch default would be a different declared rule.

### N8 — cross-cycle echo

#6417 named `S*` as the first `|S|≤3` seed that splits `f_min` from
`f_L1` and stopped at those two members. #6418 named the 1-site halt of
`f_cutmin`. #6421 named the face-diagonal 2-site halt of the same map.
This note adds only the opposite-corner 2-site halt of the already-named
support-36 `F_cut` member.

## Boundaries and explicit non-claims

- The theorem is conditional on the two-cube, the opposite-corner 2-site seed,
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
python3 scripts/f_cutmin_opposite_corner_fill_2026_08_15.py
```

The runner rebuilds the 24 proper rotations and ten axis-type orbits,
isolates `f_cutmin` as the remaining-bit tuple `(1, 0, 1, 0, 0)`, and runs
`f_cutmin`, `f_L1`, and `f_min` from `S*`. Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
