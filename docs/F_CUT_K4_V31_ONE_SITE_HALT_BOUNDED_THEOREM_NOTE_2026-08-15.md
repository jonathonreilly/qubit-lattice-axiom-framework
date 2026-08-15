---
claim_id: f_cut_k4_v31_one_site_halt_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the F_cut map (1, 1, 1, 0, 1) has the reported 1-site lock history (1, 4, 8, 10, 11, 12). Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_k4_v31_one_site_halt_2026_08_15.py
---

# One-Site Halt Of The `k=4` Map `(1, 1, 1, 0, 1)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** occupancy-to-lock dynamics of the `F_cut` remaining-bit tuple
`(wt1, opp2, adj2, vertex3, mixed3)=(1, 1, 1, 0, 1)` on the twelve-vertex
two-cube from the seed `(0,0,0)` with off-patch occupancy `0`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_k4_v31_one_site_halt_2026_08_15.py`](../scripts/f_cut_k4_v31_one_site_halt_2026_08_15.py)

## Result up front

On the two-cube `{0,1,2}×{0,1}×{0,1}` the three cuts
`f(empty)=f(full)=0` and `f(c)=f(1-c)` leave `|F_cut|=32`. Remaining-bit
tuples are written in the order `(wt1, opp2, adj2, vertex3, mixed3)`. The
four maps with `(wt1, opp2, adj2)=(1, 1, 1)` are exactly the maps that fill
all four long-axis 2-site seeds (`k=4`). Among those four, the two
`vertex3=0` maps are `(1, 1, 1, 0, 0)` and `(1, 1, 1, 0, 1)`. Investment
#6445 reported the first of those: from `(0,0,0)` it fills with history
`(1, 4, 8, 10, 11, 12)`, not L1. This note runs the other vertex3=0
member

```text
f = (1, 1, 1, 0, 1)
```

(`mixed3=1`). Complements of the named remaining orbits are forced by the
three cuts.

Theorem 1. `f` fills the four long-axis 2-site seeds: `k(f)=4`. Its 1-site
coverage is `cov1(f)=8` (`#6444`).

Theorem 2. From the 1-site seed `(0,0,0)` with off-patch occupancy `0` the
map fills: `|locks_halt|=12`, halt tick `T = 5`, lock history
`(1, 4, 8, 10, 11, 12)`.

Theorem 3. The sibling `(1, 1, 1, 0, 0)` has the same history
`(1, 4, 8, 10, 11, 12)` and the same lock *sets* at every tick. The L1 map
`f_L1(c)=1` if and only if some axis is unbalanced fills from the same seed
with history `(1, 4, 8, 11, 12)`. The displayed history and the sibling
history agree; they do **not** agree with L1. On this 1-site trajectory
mixed3 is free: flipping the last remaining bit does not split the
`vertex3=0` pair dynamically. Displayed, not adopted. Do not write f into
Admissibility.

This is a new comparison. Not leftover-character of #6445 (that reported
only the `(1, 1, 1, 0, 0)` history and did not report the 1-site lock history of
`(1, 1, 1, 0, 1)`). Matching the sibling is a new comparison; the
history is not a restatement of L1. `f_L1` is `n≠0`, not Hamming.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The F_cut map (1, 1, 1, 0, 1) fills the four long-axis 2-site seeds, has cov1=8, and has an exact 1-site lock history on the twelve-vertex two-cube. That history matches (1, 1, 1, 0, 0) and disagrees with L1. The map is displayed, not adopted as the physical Admissibility rule."
trace_class: upstream_support
target_claim_id: admissibility_nearest_neighbor_rule
target_blocker_text: "display the 1-site lock history of the k=4 vertex3=0 sibling (1, 1, 1, 0, 1) without writing it into Admissibility"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "keep f displayed; mixed3 is free on this trajectory; do not adopt f or identify it with f_L1"
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
tuple is `(1, 0, 1, 1, 1)`.

The four long-axis 2-site seeds are

```text
M = {((0,0,0),(2,0,0)), ((0,0,1),(2,0,1)), ((0,1,0),(2,1,0)), ((0,1,1),(2,1,1))}.
```

`k(f)` is the number of seeds in `M` from which `f` fills `V`. The four maps
with `(wt1, opp2, adj2)=(1, 1, 1)` are exactly the maps with `k=4`.

A **tick** locks every unlocked site of `V` whose current 6-neighbor occupancy
tuple has predicate value 1. The process starts from `S_0` and halts at the
first tick `T` with `locks_{T} = locks_{T-1}` (or at `T=0` if the first wave
is empty). Fill means `|locks_halt|=12`. The **lock history** is the sequence
of lock cardinalities from the seed through halt, including the seed count.
Coverage `cov1(f)` is the number of one-site seeds of `V` from which `f`
fills.

## Exact statements

**Theorem 1.** The `F_cut` map `f` with remaining-bit tuple `(1, 1, 1, 0, 1)`
fills all four long-axis 2-site seeds: `k(f)=4`. Its 1-site coverage is
`cov1(f)=8`.

**Theorem 2.** Run `f` from `(0,0,0)` with off-patch occupancy `0`. It fills:
`|locks_halt|=12`, `T = 5`, lock history `(1, 4, 8, 10, 11, 12)`.

**Theorem 3.** The sibling `(1, 1, 1, 0, 0)` fills from the same seed with
the same history `(1, 4, 8, 10, 11, 12)` and the same lock sets at every
tick. `f_L1` fills from the same seed with lock history
`(1, 4, 8, 11, 12)`. The displayed history and the sibling history agree;
they do not agree with L1. On this trajectory `mixed3` is free. The history
`(1, 4, 8, 10, 11, 12)` is displayed. Do not adopt `f`. Do not write `f`
into Admissibility. Equal 1-site histories of the `vertex3=0` pair do not
license an identity of members, and they do not license writing `mixed3`
into Admissibility.

### Computed values

| object | value |
|---|---|
| `\|V\|` | 12 |
| seed | `(0,0,0)` |
| off-patch occupancy | `0` |
| `\|F_cut\|` | 32 |
| `f` named tuple | `(1, 1, 1, 0, 1)` |
| `f ∈ F_cut` | yes |
| `k(f)` on the long-axis four | 4 |
| `vertex3(f)` | 0 |
| `mixed3(f)` | 1 |
| `cov1(f)` | 8 |
| sibling | `(1, 1, 1, 0, 0)` |
| sibling lock history | `(1, 4, 8, 10, 11, 12)` |
| lock sets equal sibling | yes |
| `f` halt locks | 12 |
| `f` halt tick `T` | 5 |
| `f` lock history | `(1, 4, 8, 10, 11, 12)` |
| `f_L1` named tuple | `(1, 0, 1, 1, 1)` |
| `f_L1` lock history | `(1, 4, 8, 11, 12)` |
| histories equal sibling | yes |
| histories equal L1 | no |

On this seed the first two waves coincide with both the sibling and L1: the
seed; then the three axis neighbors; then the four weight-2 sites of the
seeded cube together with `(2,0,0)`. At the next tick `f_L1` locks three
further sites (cardinality 11), while `f` and the sibling lock only
`(2,0,1)` and `(2,1,0)` (cardinality 10): the space-diagonal site `(1,1,1)`
first sees a `vertex3` neighborhood, which both `vertex3=0` maps silence.
Tick 4 then locks `(2,1,1)` (cardinality 11). Tick 5 locks `(1,1,1)` once
its neighborhood has left `vertex3`, completing the two-cube. No locking
step on this trajectory uses a `mixed3` neighborhood, so the last remaining
bit is free here.

## No-Go Discipline

The note is a displayed finite history, not a no-go against other members or
against a later derived Admissibility selector.

No-Go Discipline disposition: **PASS**

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| adopt `f` because it is a `k=4` long-axis filler | **ATTEMPTED** | `#6443` names the filler; this lane only runs the 1-site history |
| treat matching `(1, 1, 1, 0, 0)` as leftover-character of #6445 | **ATTEMPTED** | #6445 reported only the sibling; matching it is a new comparison |
| treat the 1-site history as identifying `f` with `f_L1` | **ATTEMPTED** | the histories differ; `opp2`, `vertex3`, and `mixed3` still differ from L1 |
| treat `mixed3` freedom on this seed as a license to write `mixed3` into Admissibility | **ATTEMPTED** | freedom is a displayed 1-site fact; no axiom or approved primitive is added |
| treat Hamming-parity formation as this residual | **ATTEMPTED** | Hamming is a different member and does not fill |
| write `f` into Admissibility | **ATTEMPTED** | the history is displayed; no axiom or approved primitive is added |

### N2 — wall independence

One computational wall is claimed: the halt tick and lock history of this
named map on this seed, compared to the sibling and to L1. The `k=4`
identity and the `cov1=8` identity are prior identities, not a second
impossibility wall.

### N3 — hidden-wall scan

The two-cube, seed, off-patch occupancy `0`, six-direction stencil, three
cuts, long-axis four, and axis-type orbits are declared. No `Z^3`-wide
formation law, physical Admissibility selector, Hamming identification, or
continuum extension is imported.

### N4 — residual matching

The residual after #6445 is the executable 1-site lock history of the other
`vertex3=0` `k=4` map, not a restatement of the sibling history and not a
restatement of L1. This note reports only that 1-site halt history and the
new comparison.

### N5 — certificate granularity

```text
per-element: executed — each of the 64 neighbor 6-tuples is assigned its axis-type orbit
per-site: executed — each of the twelve two-cube vertices uses the same six-direction stencil
per-mode: executed — the named F_cut map is run from the 1-site seed and from the four long-axis seeds
per-block: executed — the named map is run to a fixed point from the 1-site seed
lattice-wide: not executed — no Z^3-wide formation law or Admissibility rewrite is claimed
```

### N6 — partial-closure paths

A later derivation could still select `f_L1`, select `f`, select the sibling,
or select none of them. Equal 1-site histories of the `vertex3=0` pair leave
those routes live. A different seed or a later selector can still prefer
either map.

### N7 — steelman

The strongest objection is that agreeing with `(1, 1, 1, 0, 0)` makes this
leftover-character of #6445, so the note only restates a named history.
Incorrect on the stated objects: #6445 did not run `(1, 1, 1, 0, 1)`;
whether `mixed3` is free or splits the pair is a new comparison; the history
still disagrees with L1; and the predicates still differ on `mixed3`.

### N8 — cross-cycle echo

#6443 named both `vertex3=0` maps as long-axis fillers. #6444 scored
`cov1=8` for both. #6445 reported the 1-site halt of `(1, 1, 1, 0, 0)`.
Hamming and L1 1-site lanes execute other members. This note adds only the
1-site halt history of the remaining `vertex3=0` sibling.

## Boundaries and explicit non-claims

- The theorem is conditional on the two-cube, the 1-site seed, and off-patch
  occupancy `0`.
- Equal lock histories of the `vertex3=0` pair are not an identity of
  members, and unequal histories on another seed would not be an identity
  either.
- `f` is displayed, not adopted.
- Do not write f into Admissibility.
- `mixed3` freedom on this trajectory is displayed, not adopted.
- No `Z^3`-wide formation process, rate, or physical-law selection is claimed.
- No axiom, approved primitive, registry, or audit verdict is edited.

## Verification

Run:

```bash
python3 scripts/f_cut_k4_v31_one_site_halt_2026_08_15.py
```

The runner rebuilds the 24 proper rotations and ten axis-type orbits,
recomputes the 32-element `F_cut`, confirms `k(f)=4` on the long-axis four
and `cov1(f)=8`, and runs `f`, the sibling `(1, 1, 1, 0, 0)`, and `f_L1`
from `(0,0,0)`.
Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
