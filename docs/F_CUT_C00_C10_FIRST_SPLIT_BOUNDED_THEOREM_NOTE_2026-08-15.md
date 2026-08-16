---
claim_id: f_cut_c00_c10_first_split_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed of size at most 3 at which F_cut (1,0,0,0,0) and (1,1,0,0,0) disagree on fill is reported, or they agree on every such seed. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_c00_c10_first_split_2026_08_15.py
---

# First |S|≤3 Fill Split of the Two cov2=0 wt1=1 Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock dynamics on the displayed twelve-vertex
two-cube with off-patch occupancy 0. The two F_cut maps with remaining-bit
tuples `(1,0,0,0,0)` and `(1,1,0,0,0)` are compared on every seed of size at
most 3. The first fill disagreement is reported. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_c00_c10_first_split_2026_08_15.py`](../scripts/f_cut_c00_c10_first_split_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write the two-cube as the lex-ordered twelve-site patch
`{0,1,2} × {0,1} × {0,1}` of `Z^3`. Off-patch neighbors have occupancy 0.
A cube-covariant complement-even predicate that vanishes on the empty and
full six-neighbor cells is an F_cut map, coded by the five remaining bits
`(wt1, opp2, adj2, vertex3, mixed3)`.

The maps

```text
f00 = (1,0,0,0,0),    f10 = (1,1,0,0,0)
```

both have two-site coverage `cov2=0` on this patch. They agree on fill for
every seed of size at most 2 (neither fills any such seed). The lex-first
seed of size at most 3 at which they disagree on fill is

```text
S = {(0,0,0), (1,1,1), (2,0,0)}.
```

From `S`, `f00` halts at history `(3, 11)` and does not fill; `f10` halts at
history `(3, 12)` and fills. The maps differ only on the opp2 remaining bit.
The split is displayed. Do not adopt opp2.

The predicate `f_L1` used only as vocabulary is `n ≠ 0` (some axis
unbalanced). It is not Hamming parity.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact two-cube occupancy ticks locate the lex-first |S|<=3 fill disagreement of the two cov2=0 wt1=1 F_cut maps."
trace_class: frontier_discovery
target_claim_id: f_cut_c00_c10_first_split
target_blocker_text: "are the two cov2=0 wt1=1 maps dynamically one object"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied two-cube with off-patch o=0; opp2 is displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice, Admissibility, and Record
  sentences below supply the repository's site, nearest-neighbor, and lock
  vocabulary. They are quoted without rewrite.
- **Explicit theorem-domain condition:** the twelve-vertex two-cube, off-patch
  occupancy 0, the six-neighbor occupancy cell, the F_cut remaining-bit
  coding, and the simultaneous lock tick are supplied mathematical data for
  this theorem. The axioms do not by themselves name this finite patch or
  the F_cut subclass.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selection of a remaining bit by Record or
  Admissibility, and any physical reading of opp2, remain separate open
  obligations outside the target proved here.

## Exact Objects

Sites are the lex-ordered tuples

```text
(0,0,0), (0,0,1), (0,1,0), (0,1,1),
(1,0,0), (1,0,1), (1,1,0), (1,1,1),
(2,0,0), (2,0,1), (2,1,0), (2,1,1).
```

The six-neighbor cell of a site `v` relative to a lock set `L` is the
`{0,1}^6` occupancy of `v ± e_i`, with any off-patch neighbor scored 0.
A tick locks every unlocked site whose cell is sent to 1 by the predicate,
all at once, and halts at a fixed point. Fill means the halt lock set is
the whole twelve-site patch. The lock-history of a run is the tuple of
lock-set cardinalities, beginning with `|S|`.

The 24 proper cube rotations partition `{0,1}^6` into 10 orbits. The class
`F_cut` consists of the cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. Complement-evenness leaves five free bits on the remaining
orbit pairs, in the order `(wt1, opp2, adj2, vertex3, mixed3)`, so
`|F_cut|=32`.

`f_L1` is the map with remaining bits `(1,0,1,1,1)`. Equivalently,
`f_L1(c)=1` if and only if some axis is unbalanced (`n_μ = c_{+μ} − c_{-μ}`
is nonzero). This is **not** Hamming parity `|c|_1 mod 2`, which is the
different remaining-bit tuple `(1,0,0,1,1)`.

`cov2(f)` is the number of unordered two-site seeds on this patch from
which `f` fills. There are `C(12,2)=66` such seeds. Seeds of size at most
3 are enumerated by increasing cardinality and, within each cardinality,
lexicographic order of the lex-sorted site tuple.

All runner quantities are exact integers. No float is used.

## Exact Target And Proof Obligations

The exact target is to recompute `cov2(f00)` and `cov2(f10)`, and to name
the lex-first seed of size at most 3 at which those two maps disagree on
fill, or else to report that they agree on every such seed.

The obligation graph is:

1. recompute two-site coverage of both displayed maps;
2. scan every seed of size at most 3 in the stated order and report the
   first fill disagreement, together with both halt histories;
3. display the opp2 cell that separates the first wave, without adopting
   opp2.

All three obligations are closed below and in the runner. Larger seeds,
other remaining-bit pairs, and any adoption of opp2 are outside this
theorem. There is no missing lemma for the bounded target.

## Theorem 1 — both maps have cov2=0

Recomputing two-site coverage on this patch gives

```text
cov2(f00) = 0,    cov2(f10) = 0.
```

Neither map fills any of the 66 two-site seeds, and neither fills any of
the 12 one-site seeds. By contrast the vocabulary map `f_L1=(1,0,1,1,1)`
fills 62 of the 66 two-site seeds. The identity `cov2(f00)=cov2(f10)=0` is
an independent recomputation on the supplied patch. It is not imported as a
hypothesis.

## Theorem 2 — lex-first `|S| ≤ 3` fill disagreement

Every seed of size at most 2 produces the same fill bit on `f00` and on
`f10` (both miss). The first three-site seed in lex order at which the fill
bits differ is

```text
S = {(0,0,0), (1,1,1), (2,0,0)}.
```

No earlier three-site seed disagrees on fill. Eight earlier three-site
seeds already differ in lock history, but both maps miss fill on each of
those seeds. The target of this note is fill, not history, so those triples
are not the reported split. The map `f00` fills none of the 220 three-site
seeds; `f10` fills exactly four of them.

## Theorem 3 — which map fills

From `S` the two runs are:

```text
f00 : history (3, 11), fill = false,
f10 : history (3, 12), fill = true.
```

At tick 0 the unlocked midpoint `(1,0,0)` sees the six-neighbor cell
`(1,1,0,0,0,0)`, the `opp2` representative with both `±e_1` occupied. The
other eight unlocked sites each see a `wt1` cell. Both maps have `wt1=1`,
so those eight sites lock. The first wave of `f00` therefore reaches eleven
locks and misses only `(1,0,0)`. After that wave the leftover site sees an
`adj4` cell, which `f00` also rejects, so the process halts unfilled. The
first wave of `f10` includes the extra lock `(1,0,0)` and saturates the
patch in one tick.

This exhibits a seed on which the opp2 bit is dynamically visible inside
the `wt1=1`, `cov2=0` pair. Do not adopt opp2. The exhibition is not an
adoption of opp2, and no Admissibility sentence is rewritten.

## Physical-Interpretation Boundary

The proved output is the displayed seed and the two fill bits. This note
neither installs opp2 as a selected remaining bit nor changes the live
Admissibility or Record sentences. Remaining-bit tuples are displayed
predicate data, not axiom content, and no additional
axiom is proposed.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. a map does not disagree with itself on any seed of size at most 3;
2. Hamming parity is not `f_L1` and is neither displayed map;
3. the swapped claim "`f00` fills `S` and `f10` misses" is false.

## What This Does Not Claim

- The two-cube is not claimed to be a physically derived finite world.
- The opp2 bit is not adopted, and `f10` is not selected as a physical law.
- No claim is made that Record locks on opp2 cells, or that Admissibility
  prefers either displayed map.
- Agreement on fill for `|S| ≤ 2` is not a claim that the two maps are
  dynamically identical: they already differ in history on earlier
  three-site seeds.
- Seeds of size greater than 3 are not classified.
- Independent class leftovers are not used as parents.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> When present, a record locks exactly one admissible local possibility.

> A site with no record cannot be read.

Their dependency role is limited to the repository's site, nearest-neighbor,
and lock vocabulary. This theorem separately supplies the two-cube, the
F_cut coding, and the seed census; physical interpretation of opp2 remains
outside its target.

On the two-cube with off-patch o=0, the lex-first seed of size at most 3 at
which F_cut (1,0,0,0,0) and (1,1,0,0,0) disagree on fill is reported, or they
agree on every such seed. Displayed, not adopted.

## Runner Contract

The companion runner checks Theorems 1–3 with exact integer occupancy
ticks. It recomputes `cov2` for both maps, scans every seed of size at most
3 in lex order, and rejects the three mutations. It quotes the live axiom
sentences and records the import boundary. Declared review inputs are this
note and the axiom memo only.
