---
claim_id: f_cut_wt1_zero_mix0_first_split_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed of size at most 3 at which F_cut (1,0,1,1,0) fills and (0,0,1,1,0) does not is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_wt1_zero_mix0_first_split_2026_08_15.py
---

# First `|S|≤3` Seed Where `f_mix0` Fills And Its `wt1=0` Sibling Does Not

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact lock-evolution coverage on the supplied twelve-site
two-cube `{0,1,2} × {0,1} × {0,1}` with off-patch occupancy `o = 0`.
The displayed pair is `f_mix0 = (1,0,1,1,0)` and
`fwt = (0,0,1,1,0)`. The lex-first nonempty seed of size at most `3`
at which the first map fills and the second does not is reported by
the seed, both fill bits, and both lock-count histories. Displayed,
not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_wt1_zero_mix0_first_split_2026_08_15.py`](../scripts/f_cut_wt1_zero_mix0_first_split_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work on the two-cube of twelve lattice sites
`{0,1,2} × {0,1} × {0,1}`. Off-patch occupancy is `0`. A seed locks its
sites. At each tick, every unlocked site whose six-neighbor axis type is
fired by the displayed map locks. The process fills when all twelve sites
are locked at halt.

`F_cut` is the family of cube-covariant `{0,1}`-maps on six-neighbor
occupancy with `f(empty) = f(full) = 0` and `f(c) = f(1-c)`. After those
constraints the remaining bits are
`(wt1, opp2, adj2, vertex3, mixed3)`. The displayed pair is

```text
f_mix0 = (1, 0, 1, 1, 0)
fwt    = (0, 0, 1, 1, 0)
```

They differ only on the remaining bit `wt1`. This is not leftover-character of #6476,
which listed `fwt` among the four extras in `Max(11)` minus `Max(1)` and did
not name a seed. It is not leftover-character of #6473, which placed
`f_mix0` in `Max(1)` and did not compare the pair. It is not leftover-character of #6437,
which split `f_mix0` from `f_L1` on a three-site seed.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}`
for at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor
contrast `n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is
`(1, 0, 1, 1, 1)`. Hamming parity has remaining bits `(1, 0, 0, 1, 1)`.

Nonempty seeds are searched by increasing size, then by lexicographic
order of the sorted site tuple, with sites ordered as `(x,y,z)` and
`TWO_CUBE` listed by `x ∈ {0,1,2}`, `y ∈ {0,1}`, `z ∈ {0,1}`. The
search is capped at `|S| ≤ 3`.

The lex-first such seed at which `f_mix0` fills and `fwt` does not is
the one-site seed

```text
S = {(0,0,0)}.
```

On that seed the lock-count histories are

```text
f_mix0 : (1, 4, 8, 11, 12)   fills
fwt    : (1)                 does not fill
```

Displayed, not adopted. The remaining bit `wt1` is not written into
Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact lock evolution on the twelve-site two-cube finds the lex-first seed of size at most 3 at which displayed f_mix0 fills and its wt1=0 sibling does not, and reports both halt histories."
trace_class: frontier_discovery
target_claim_id: f_cut_wt1_zero_mix0_first_split
target_blocker_text: "is wt1 free on the mix0 line?"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied two-cube with off-patch o=0 and the displayed pair; no selector or Admissibility edit is asserted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded first-split claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice, Admissibility, and Record
  sentences below supply site language, nearest-neighbor covariance, and
  the lock/unread rule. They are quoted without rewrite.
- **Explicit theorem-domain condition:** the twelve-site two-cube, off-patch
  occupancy `0`, the displayed `F_cut` bit tuples `f_mix0 = (1,0,1,1,0)`
  and `fwt = (0,0,1,1,0)`, simultaneous ready-lock evolution, and the
  lex order of nonempty seeds of size at most `3` are supplied
  mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selection of `f_mix0`, of `fwt`, or of the
  remaining bit `wt1` by Admissibility or Record remains a separate open
  obligation outside the target proved here. Do not adopt wt1.

## Exact Objects

Sites are the twelve points of `{0,1,2} × {0,1} × {0,1}`. A site outside
this set has occupancy `0`. The blank-block is a different rule and is
not used. For an unlocked site `v` the six neighbors
`v ± e_μ`, `μ ∈ {x,y,z}`, determine an axis type
`(n_unbalanced, n_both, n_empty)` with those three integers summing to
`3`. The named remaining types are

```text
wt1 = (1,0,2), opp2 = (0,1,2), adj2 = (2,0,1),
vertex3 = (3,0,0), mixed3 = (1,1,1).
```

Complement swaps empty with both and leaves unbalanced fixed, so
`mixed3` and `vertex3` are self-complementary. `F_cut` forces
`f(empty) = f(full) = 0` and equal values on each complementary pair.
The five remaining bits therefore label the `32` cut maps.

`f_mix0` fires `wt1`, `adj2`, and `vertex3`, and is silent on `opp2`
and `mixed3`. `fwt` is the same map with the `wt1` bit cleared: it
fires `adj2` and `vertex3` only.

A seed `S` starts locked. Each tick locks every currently unlocked site
whose axis type is fired. Halt is the first tick with no new lock. Fill
means the halt lock set is the whole two-cube.

One-site coverage is

```text
cov1(f) = |{ v : f fills from {v} }|.
```

`Max(1)` is the set of the `32` cut maps that attain `m_1 = max cov1`.
Independent recomputation on this patch gives `m_1 = 12` attained by
exactly four maps, so a map is in `Max(1)` here if and only if it fills
every one-site seed.

## Exact Target And Proof Obligations

The exact target is the lex-first nonempty seed `S` of size at most `3`
at which `f_mix0` fills and `fwt` does not, together with both
lock-count histories on that seed.

The obligation graph is:

1. recompute `Max(1)` among the `32` cut maps and locate the displayed
   pair in or out of that set;
2. enumerate nonempty seeds of size `1`, then `2`, then `3`, in lex
   order, and stop at the first seed `f_mix0` fills and `fwt` misses;
3. report both lock-count histories from that seed.

All three obligations are closed below and in the runner. The two-cube,
off-patch default, and displayed bit tuples are theorem hypotheses.
Other patches, other maps, and any selector among `F_cut` are outside
this theorem.

## Theorem 1 — `f_mix0` is in `Max(1)`; `fwt` is not

There are twelve one-site seeds. Direct lock evolution gives
`cov1(f_mix0) = 12` and `cov1(fwt) = 0`. Among all `32` cut maps the
maximum one-site coverage is `m_1 = 12`, attained by the four remaining-bit
tuples

```text
(1, 0, 1, 1, 0), (1, 0, 1, 1, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1).
```

Thus `f_mix0` is in `Max(1)` and `fwt` is not. The four maximizers are
`f_mix0`, `f_L1`, `f0 = (1,1,1,1,0)`, and `f1 = (1,1,1,1,1)`. This
reconfirms the membership recorded as #6473 for `f_mix0` and the
exclusion of `fwt` from `Max(1)` recorded as #6476. Hamming parity is
not among those four tuples.

## Theorem 2 — lex-first `|S|≤3` split seed is `{(0,0,0)}`

Enumerate nonempty seeds by increasing size, then lexicographic order of
the sorted site tuple. The first one-site seed is `{(0,0,0)}`. On that
seed `f_mix0` fills and `fwt` does not. No earlier nonempty seed of size
at most `3` exists, so this is the lex-first `|S|≤3` seed at which the
pair splits in the required direction.

The same search run to completion is not the claim: later two-site and
three-site splits are not listed. The claim is the first seed, not a
census of all seeds on which the pair disagrees.

## Theorem 3 — histories from `S`; display; do not adopt `wt1`

From `S = {(0,0,0)}` the lock-count histories are

```text
f_mix0 : (1, 4, 8, 11, 12)
fwt    : (1)
```

`f_mix0` reaches all twelve sites. `fwt` never leaves the seed: halt
locks equal `1`. The three on-patch neighbors of `(0,0,0)` have axis
type `wt1 = (1,0,2)`. Displayed `f_mix0` fires that type and locks
`(1,0,0)`, `(0,1,0)`, and `(0,0,1)` on the first tick. Displayed `fwt`
is silent on `wt1` and therefore has an empty first wave. That
neighborhood type is reported only to name the first split. The
remaining bit `wt1` is not adopted as an Admissibility selector, not
named as a physical sector, and not written into the axiom memo.

## Physical-Interpretation Boundary

The proved output is a first-split seed and two halt histories on a
supplied finite patch for a displayed pair of cut maps. This note
neither assigns `wt1` a physical label nor changes Lattice,
Admissibility, or Record. No additional axiom is proposed. Do not write the ranking into Admissibility.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. `fwt` is not in `Max(1)`: `cov1(fwt) = 0`, not `12`;
2. `f_mix0` is not `f_L1` and is not Hamming parity;
3. the first split is a one-site seed, not the three-site mix0/L1
   splitter `{(0,0,0),(0,0,1),(2,0,0)}` of #6437.

A fourth guard is that the pair is not leftover of the #6476 listing of
`Max(11)` extras: that listing named `fwt` and did not report a seed or
a history.

## What This Does Not Claim

- `f_mix0` and `fwt` are not adopted as physical nearest-neighbor rules.
- The remaining bit `wt1` is not adopted.
- No claim is made that Record locks `{(0,0,0)}` or that Admissibility
  selects `wt1` silence.
- Other `F_cut` tuples, later split seeds, and the infinite lattice
  outside the two-cube are not classified.
- Independent class-`C` leftovers are not used as parents.
- This note does not re-list `Max(11)` and does not census every
  `|S|≤3` disagreement.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under
> lattice translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility.

> A site with no record cannot be read.

Their dependency role is limited to site language, covariance of a
nearest-neighbor rule, and the lock/unread vocabulary. This theorem
separately supplies the two-cube, the displayed pair, and the first-split
seed; physical selection of `wt1` remains outside its target.

## Runner Contract

The companion runner checks Theorems 1–3 by recomputing `Max(1)` among
the `32` cut maps, searching nonempty seeds of size at most `3` in lex
order, and evolving both displayed maps from the first split. It also
checks the mutations, quotes the live axiom sentences, prints
substantive N5 scope certificates, and records the import boundary.
Declared review inputs are this note and the axiom memo only.
