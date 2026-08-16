---
claim_id: f_cut_qstar_nontot_cov2_first_split_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first 2-site seed at which F_cut (1,1,1,0,0) fills and (1,0,1,0,0) does not is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_qstar_nontot_cov2_first_split_2026_08_15.py
---

# Lex-First Two-Site Split Of Non-Total `Q_*` Coverage 32 Versus 36

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 2-site coverage on the twelve-vertex
two-cube with off-patch occupancy `0`, restricted to the two
cube-covariant cut maps `F_cut` with remaining bits `(1,0,1,0,0)` and
`(1,1,1,0,0)`. Both lie in `Q_*` and both have `vertex3=0`. The scored
object is the lex-first two-site seed that the second map fills and the
first map misses.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_qstar_nontot_cov2_first_split_2026_08_15.py`](../scripts/f_cut_qstar_nontot_cov2_first_split_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

The tot2q census on the eight `Q_*` maps (`wt1=1` and `adj2=1`) already
named two-site totality as a proper subset of `vertex3=1`. The four
`vertex3=0` maps are the non-total slice: they have `cov2` in `{32,36}`,
with `opp2=0` scoring `32` and `opp2=1` scoring `36`. That census names
coverages. It does not name a seed.

This note stays inside that non-total slice and takes the two remaining-bit
tuples that differ only by `opp2` at `mixed3=0`:

```text
f_lo = (1, 0, 1, 0, 0)   # cov2=32
f_hi = (1, 1, 1, 0, 0)   # cov2=36
```

New split inside non-tot `Q_*`, not leftover-character of the tot2q
coverage table.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`. That tuple lies in `Q_*` and has
`vertex3=1`; it is a control, not a scored non-total map.

On the two-cube with off-patch `o=0`, write `cov2(f)` for the number of
two-site seeds from which `f` fills. There are `C(12,2)=66` two-site
seeds. Totality means `cov2(f)=66`. Both maps below fail totality.

Sites of the two-cube, in lexicographic order:

`(0,0,0)`, `(0,0,1)`, `(0,1,0)`, `(0,1,1)`,
`(1,0,0)`, `(1,0,1)`, `(1,1,0)`, `(1,1,1)`,
`(2,0,0)`, `(2,0,1)`, `(2,1,0)`, `(2,1,1)`.

Two-site seeds are the sixty-six unordered pairs, listed as combinations
of that site list.

**Theorem 1.** Both maps are `Q_*` with `vertex3=0`. Direct evolution on
the sixty-six two-site seeds gives

```text
cov2(f_lo) = 32
cov2(f_hi) = 36.
```

**Theorem 2.** The lex-first two-site seed that `f_hi` fills and `f_lo`
does not is

`S={(0,0,0),(2,0,0)}`.

Exactly four two-site seeds split this way; none reverse. From `S`,
`f_hi` has lock history `(2, 7, 9, 10, 12)` and fills, while `f_lo` has
lock history `(2, 6, 8)` and halts at size `8`.

**Theorem 3.** Display. Do not adopt a bit. Do not adopt the seed. Do not
write `opp2` or this seed into Admissibility.

Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The two non-total Q_* maps (1,0,1,0,0) and (1,1,1,0,0) are scored exactly on the sixty-six two-site seeds. The lex-first seed that splits fill from miss is a finite pair on this patch. Not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_qstar_nontot_cov2_first_split
target_blocker_text: "lex-first 2-site seed at which F_cut (1,1,1,0,0) fills and (1,0,1,0,0) does not"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded non-tot Q_* first-split seed; do not adopt a bit"
conditional_surface_status: "exact for occupancy-to-lock on the twelve-vertex two-cube with off-patch occupancy 0; no Z^3-wide formation law"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Current premise boundary

The only scientific dependency is the current four-axiom authority linked
above. The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

The axiom memo says the distribution concerns which possibility a forming
record locks, conditional on formation at that site; it does not supply the
formation site, probability, or rate.

Admissibility is not a dynamics axiom.

The current Record boundary is:

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Record supplies no formation-site selector and no occupancy-to-lock
predicate. The seed and the `opp2` bit below are displayed remaining-bit
data, not axiom content.

## Exact objects

The two-cube is `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices). Off-patch
occupancy `0` is the explicit default: a neighbor of a site in `T` that is
not itself in `T` is treated as unoccupied. A blank-block is a different
rule and is not used.

A configuration `c ∈ {0,1}^6` is a six-tuple of neighbor occupancies in
direction order `(+x,-x,+y,-y,+z,-z)`. Axis type is
`(n_unbalanced, n_both, n_empty)`, where an axis is unbalanced if its two
bits differ, both if both bits are 1, and empty if both bits are 0.
Complement swaps `n_both` with `n_empty`. The five remaining bits of
`F_cut`, in the order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values
on orbit types `(1,0,2)`, `(0,1,2)`, `(2,0,1)`, `(3,0,0)`, `(1,1,1)`.
Complement partners are forced equal; empty and full are fixed at 0. Thus
`N_free = 5` and `|F_cut| = 32`.

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

The two-site seeds are the sixty-six pairs `{x,y}` for distinct `x,y ∈ T`,
in combination order of the lexicographic site list. Then `cov2(f)` is the
number of those pairs from which `f` fills.

`Q_*` is the remaining-bit predicate `wt1=1` and `adj2=1`. It holds on
exactly eight of the 32 maps. Non-total `Q_*` here means the four of those
eight with `vertex3=0`. The two scored maps are the `mixed3=0` pair in
that four-map slice.

`f_lo` fires on axis types with remaining bits `(1,0,1,0,0)`: `wt1` and
`adj2` and their complements, and not on `opp2`, `vertex3`, or `mixed3`.
`f_hi` is the same except `opp2=1`.

## Theorem 1 — both maps are non-total `Q_*`; report both `cov2`

Both remaining-bit tuples have `wt1=1` and `adj2=1`, so both lie in
`Q_*`. Both have `vertex3=0`. Direct evolution on the sixty-six two-site
seeds scores

```text
(1, 0, 1, 0, 0)  cov2=32  vertex3=0
(1, 1, 1, 0, 0)  cov2=36  vertex3=0
```

Neither attains `cov2=66`. This reconfirms the tot2q scores for these two
rows. The new object is not those two integers.

## Theorem 2 — lex-first two-site seed that splits fill from miss

Search the sixty-six two-site seeds in lex order. The first seed that
`f_hi` fills and `f_lo` does not is

`S={(0,0,0),(2,0,0)}`.

These are the two `x`-ends of the line `y=z=0`. The middle site
`(1,0,0)` sees occupancy `(1,1,0,0,0,0)`, which is axis type `opp2=(0,1,2)`.
So `f_hi` locks `(1,0,0)` at tick `1` and `f_lo` does not.

Exactly four two-site seeds split this way, all four long-`x` opposite
pairs:

```text
{(0,0,0),(2,0,0)}
{(0,0,1),(2,0,1)}
{(0,1,0),(2,1,0)}
{(0,1,1),(2,1,1)}
```

No two-site seed is filled by `f_lo` and missed by `f_hi`. The coverage
gap `36-32=4` is exactly this four-seed set.

From `S`, `f_hi` has lock history `(2, 7, 9, 10, 12)` and fills. From the
same `S`, `f_lo` has lock history `(2, 6, 8)` and halts at eight sites:
the two `x`-faces, with the middle slice empty.

## Theorem 3 — display, not adoption

The seed `S` and the `opp2` contrast that splits these two maps are
displayed data. Do not adopt a bit. Do not adopt `opp2`. Do not adopt
`Q_*`. Do not adopt `f_L1`. Do not adopt this seed. Do not write `opp2`
or a seed into Admissibility. Admissibility does not name this
remaining-bit formula and is not a dynamics axiom.

The split is a finite fact about occupancy-to-lock on this two-cube with
off-patch `o=0`. It is not a physical formation-site selector and not an
axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q_*` as `wt1=1` and `adj2=1` | both scored maps lie in it |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, sixty-six two-site seeds, off-patch `o=0` | declared finite patch |
| both maps `vertex3=0`; `cov2` in `{32,36}` | `32` and `36` |
| lex-first 2-site seed `f_hi` fills and `f_lo` misses | `{(0,0,0),(2,0,0)}` |
| leftover of the tot2q coverage table | refused; that named scores, not a seed |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of tot2q: that named `cov2` in `{32,36}` on the
four `vertex3=0` maps. The present object is the lex-first two-site seed
at which `(1,1,1,0,0)` fills and `(1,0,1,0,0)` does not.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers which lex-first two-site seed `f_hi` fills and `f_lo` misses. |
| V2 | Current main has the axiom memo and the tot2q `32`/`36` scores, but no landed first-split seed inside non-tot `Q_*`. |
| V3 | The two maps and sixty-six seeds are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it names a declared finite seed. |
| V5 | The seed is displayed, not adopted, and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: a pair of coverage integers is not a
split seed, and a displayed remaining-bit seed inside non-tot `Q_*` is
not axiom content. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of tot2q | treat the seed as already named by the `32`/`36` scores | **ATTEMPTED** |
| leftover Max(2) | treat a non-total split as a rename of `cov2=66` | **ATTEMPTED** |
| adopt the bit | write `opp2` or the seed into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch seed to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the tot2q coverage table, the two-map Max(2)
set, and the off-patch convention are distinct. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The two-cube, the sixty-six pairs, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, the `Q_*`
cut `wt1=1` and `adj2=1`, and the two scored tuples are declared.
Unique selection of `f_L1` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is the
lex-first two-site seed that splits `(1,1,1,0,0)` from `(1,0,1,0,0)`,
not leftover-character of the tot2q scores.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the two scored maps on 66 seeds | no physical law selection |
| per block | the lex-first split seed on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include the `mixed3=1` pair in the same four-map slice, a
different seed family, a different off-patch rule, a selector outside
`Q_*`, and any independently derived physical map from `F_cut` into
Admissibility.

### N7 — hostile steelman

**Steelman:** tot2q already scored `32` versus `36` on these two maps,
so the four extra seeds are leftover and `opp2` may be written as the
rule.

**Answer:** A coverage integer does not name a seed. The lex-first
splitter is `{(0,0,0),(2,0,0)}`. That pair is displayed data. Admissibility
does not name `opp2` or this seed. Do not adopt a bit.

### N8 — cross-cycle echo

The tot2q census already showed that the four `vertex3=0` maps have
`cov2` in `{32,36}`. Echoing those two integers is not a substitute for
naming the lex-first two-site seed that splits fill from miss.

No-Go Discipline disposition: **PASS** for the finite first-split seed
and the displayed `opp2` contrast. FAIL / DO NOT SHIP for “adopt a
bit,” “write this seed into Admissibility,” or “the `32`/`36` scores
already are the seed.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, restricts to the
two remaining-bit tuples `(1,0,1,0,0)` and `(1,1,1,0,0)`, reconfirms both
are `Q_*` with `vertex3=0`, scores both `cov2` on the sixty-six two-site
seeds, and names the lex-first seed that the second fills and the first
misses. Declared audit inputs are this note and the axiom memo; the
runner writes no cache and authors no audit verdict.
