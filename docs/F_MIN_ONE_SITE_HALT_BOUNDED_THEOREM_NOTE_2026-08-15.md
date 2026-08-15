---
claim_id: f_min_one_site_halt_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the unique support-26 1-site filler f_min (nonempty n_both=0) halts at tick T = 4 with lock history (1, 4, 8, 11, 12). Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_min_one_site_halt_2026_08_15.py
---

# Halt Dynamics Of The Unique Support-26 One-Site Filler

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** occupancy-to-lock dynamics of the unique support-26 cube-covariant
1-site filler on the twelve-vertex two-cube from the seed `(0,0,0)` with
off-patch occupancy `0`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_min_one_site_halt_2026_08_15.py`](../scripts/f_min_one_site_halt_2026_08_15.py)

## Result up front

On the two-cube `{0,1,2}×{0,1}×{0,1}` the unique support-26 1-site filler is
the nonempty `n_both=0` map

```text
f_min(c)=1  iff  n_both(c)=0 and some axis is unbalanced.
```

Its remaining-orbit tuple is `(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 0)`.
It is not in the complement-even class `F_cut`. From the 1-site seed `(0,0,0)`
with off-patch occupancy `0` it fills: `|locks_halt|=12`, halt tick `T = 4`,
lock history `(1, 4, 8, 11, 12)`.

The L1 map `f_L1(c)=1` if and only if some axis is unbalanced fills from the
same seed with the same lock history `(1, 4, 8, 11, 12)`. Equal histories on
this seed do not identify the maps: `f_min` silences the mixed3 orbit that
`f_L1` fires. Displayed, not adopted. Do not write f_min into Admissibility.

Not leftover-character of #6407 (identity only). Not Hamming-parity formation dynamics. Not vertex3-orbit indicator dynamics. Not f_two face-diagonal 2-site fill. Those lanes move other members or other seeds.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The unique support-26 1-site filler, its halt tick, and its lock history on the twelve-vertex two-cube are exact finite computations. The map is displayed, not adopted as the physical Admissibility rule."
trace_class: upstream_support
target_claim_id: admissibility_nearest_neighbor_rule
target_blocker_text: "display a named rival 1-site filler as an executable occupancy-to-lock history without writing it into Admissibility"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "keep f_min displayed; do not adopt it or identify it with f_L1 from one equal 1-site history"
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

`f_L1(c)=1` if and only if some axis is unbalanced, equivalently
`n_μ = c_{+μ} − c_{-μ}` is nonzero for at least one axis. This is **not** Hamming parity `|c|_1 mod 2`.

`f_min(c)=1` if and only if `n_both(c)=0` and some axis is unbalanced. That is
the indicator of the three orbits `wt1 ∪ adj2 ∪ vertex3`. Complements of those
orbits carry `n_both ≥ 1`, so `f_min` is not complement-even and is not in
`F_cut`.

A **tick** locks every unlocked site of `V` whose current 6-neighbor occupancy
tuple has predicate value 1. The process starts from `S_0` and halts at the
first tick `T` with `locks_{T} = locks_{T-1}` (or at `T=0` if the first wave
is empty). Fill means `|locks_halt|=12`. The **lock history** is the sequence
of lock cardinalities from the seed through halt, including the seed count.

## Exact statements

**Theorem 1.** Among the 512 cube-covariant maps with `f(empty)=0`, exactly 96
fill `V` from `S_0`. The minimal filler support is 26, achieved by exactly one
map, and that map is `f_min`. It fills: `|locks_halt|=12`, `T = 4`, lock
history `(1, 4, 8, 11, 12)`.

**Theorem 2.** `f_L1` fills from the same seed with lock history
`(1, 4, 8, 11, 12)`. The `f_min` history equals the L1 history. The maps
remain distinct: their named tuples differ at mixed3.

**Theorem 3.** The history `(1, 4, 8, 11, 12)` is displayed. Do not adopt
`f_min`. Do not write `f_min` into Admissibility. Equal 1-site histories do
not license an identity of members.

### Computed values

| object | value |
|---|---|
| `\|V\|` | 12 |
| seed | `(0,0,0)` |
| off-patch occupancy | `0` |
| `N_fill` | 96 |
| `supp(f_min)` | 26 |
| `N_min` | 1 |
| `f_min` named tuple | `(1, 0, 1, 1, 0)` |
| `f_min ∈ F_cut` | no |
| `f_min` halt locks | 12 |
| `f_min` halt tick `T` | 4 |
| `f_min` lock history | `(1, 4, 8, 11, 12)` |
| `supp(f_L1)` | 56 |
| `f_L1` named tuple | `(1, 0, 1, 1, 1)` |
| `f_L1` lock history | `(1, 4, 8, 11, 12)` |
| histories equal | yes |

On this seed the locked *site sets* also coincide at every tick: the seed; then
the three axis neighbors; then the four weight-2 sites of the seeded cube
together with `(2,0,0)`; then all remaining sites except `(2,1,1)`; then the
full two-cube. Mixed3 never appears as a first-locking neighborhood along that
trajectory, which is why silencing mixed3 does not change the 1-site history.

## No-Go Discipline

The note is a displayed finite history, not a no-go against other members or
against a later derived Admissibility selector.

No-Go Discipline disposition: **PASS**

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| adopt `f_min` because it is the unique support-26 filler | **ATTEMPTED** | uniqueness of support is the #6407 identity; this lane only runs the history |
| treat equal lock histories as `f_min = f_L1` | **ATTEMPTED** | mixed3 still differs; one seed does not identify the maps |
| treat Hamming-parity formation as this residual | **ATTEMPTED** | Hamming is a different member and does not fill |
| treat the vertex3-orbit indicator as this residual | **ATTEMPTED** | that indicator has empty 1-site first wave |
| treat `f_two` from a face-diagonal 2-site seed as this residual | **ATTEMPTED** | that lane moves a different member and a different seed |
| write `f_min` into Admissibility | **ATTEMPTED** | the history is displayed; no axiom or approved primitive is added |

### N2 — wall independence

One computational wall is claimed: the halt tick and lock history of this
named map on this seed. Uniqueness of support 26 is a prior identity, not a
second impossibility wall.

### N3 — hidden-wall scan

The two-cube, seed, off-patch occupancy `0`, six-direction stencil, and
axis-type orbits are declared. No `Z^3`-wide formation law, physical
Admissibility selector, Hamming identification, or continuum extension is
imported.

### N4 — residual matching

The residual after #6407 is the executable lock history of the named rival,
not a restatement of its orbit bits. This note reports that history.

### N5 — certificate granularity

```text
per-element: executed — each of the 64 neighbor 6-tuples is assigned its axis-type orbit
per-site: executed — each of the twelve two-cube vertices uses the same six-direction stencil
per-mode: executed — every cube-covariant empty-silent map is classified as filler or not
per-block: executed — the unique support-26 filler is run to a fixed point from the 1-site seed
lattice-wide: not executed — no Z^3-wide formation law or Admissibility rewrite is claimed
```

### N6 — partial-closure paths

A later derivation could still select `f_L1`, select `f_min`, or select
neither. Equal 1-site histories leave those routes live. A different seed
can separate the maps.

### N7 — steelman

The strongest objection is that matching site sets on the 1-site seed already
make `f_min` interchangeable with `f_L1` for every later argument. Incorrect
on the stated objects: the predicates differ on mixed3, so a neighborhood of
that type, on this patch or another seed, can split them.

### N8 — cross-cycle echo

#6407 named `f_min` and stopped at identity. Hamming, vertex3-indicator, and
`f_two` 2-site lanes execute other members. This note adds only the 1-site
halt history of the already-named support-26 rival.

## Boundaries and explicit non-claims

- The theorem is conditional on the two-cube, the 1-site seed, and off-patch
  occupancy `0`.
- Equal lock histories are not an identity of members.
- `f_min` is displayed, not adopted.
- Do not write `f_min` into Admissibility.
- No `Z^3`-wide formation process, rate, or physical-law selection is claimed.
- No axiom, approved primitive, registry, or audit verdict is edited.

## Verification

Run:

```bash
python3 scripts/f_min_one_site_halt_2026_08_15.py
```

The runner rebuilds the 24 proper rotations and ten axis-type orbits,
recomputes the 96 1-site fillers, isolates the unique support-26 map, and
runs `f_min` and `f_L1` from `(0,0,0)`. Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
