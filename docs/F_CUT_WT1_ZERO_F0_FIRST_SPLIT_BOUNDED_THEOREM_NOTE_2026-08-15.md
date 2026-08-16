---
claim_id: f_cut_wt1_zero_f0_first_split_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed of size at most 3 at which F_cut (1,1,1,1,0) fills and (0,1,1,1,0) does not is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_wt1_zero_f0_first_split_2026_08_15.py
---

# First |S|≤3 Seed Where F_cut (1,1,1,1,0) Fills and Its wt1=0 Sibling Does Not

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** occupancy-to-lock dynamics on the twelve-vertex two-cube with
off-patch occupancy `0`. The displayed pair is the mixed3-silent F_cut map
`(1, 1, 1, 1, 0)` and its wt1=0 sibling `(0, 1, 1, 1, 0)`. The first split
seed of size at most 3 is reported. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_wt1_zero_f0_first_split_2026_08_15.py`](../scripts/f_cut_wt1_zero_f0_first_split_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

`F_cut` is the cube-covariant class of occupancy predicates with
`f(empty)=f(full)=0` and `f(c)=f(1-c)`. Its five free remaining bits are
ordered as `(wt1, opp2, adj2, vertex3, mixed3)`. Write `f0 = (1, 1, 1, 1, 0)`
for the mixed3-silent maximizer and `fwt = (0, 1, 1, 1, 0)` for the same
tuple with the wt1 bit cleared.

On the two-cube, `Max(k)` is the set of `F_cut` maps that maximize the number
of unordered `k`-site seeds from which the map fills all twelve vertices.

- `f0` is in `Max(1)` and `Max(2)`.
- `fwt` is in neither Max(1) nor Max(2). Independently, `fwt` attains
  `Max(11)` (twelve of the twelve eleven-site seeds fill).
- Searching seeds in size-then-lex order with `|S| ≤ 3`, the first seed at
  which `f0` fills and `fwt` does not is the singleton `S = {(0, 0, 0)}`,
  so `|S| = 1`.
- From that seed, `f0` reaches the full twelve-site halt lock set in four
  ticks. `fwt` never leaves `{(0, 0, 0)}`.

The pair and the seed are displayed. Do not adopt wt1. Do not write them
into Admissibility.

Not leftover-character of the Max(11) listing: that listing only placed
`(0, 1, 1, 1, 0)` among the four extras that attain `Max(11)` and miss
`Max(1)`. The new object is the first dynamical split of the mixed3-silent
line from its wt1=0 sibling.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact occupancy-to-lock enumeration on the two-cube names the lex-first |S|<=3 seed at which F_cut (1,1,1,1,0) fills and (0,1,1,1,0) does not."
trace_class: frontier_discovery
target_claim_id: f_cut_wt1_zero_f0_first_split
target_blocker_text: "is wt1 free on the mixed3-silent line?"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the twelve-vertex two-cube with off-patch occupancy 0; no physical selector is asserted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice, Admissibility, and Record
  sentences quoted below supply the repository's `Z^3` vocabulary, covariant
  nearest-neighbor rule, and unread-absence lock rule. They are quoted
  without rewrite.
- **Explicit theorem-domain condition:** the two-cube
  `{0,1,2} × {0,1} × {0,1}`, off-patch occupancy `0` (a blank-block is a
  different rule), and the five remaining-bit coordinates of `F_cut` are
  supplied mathematical data.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selecting `f0`, `fwt`, or the wt1 bit as a
  physical Admissibility rule remains a separate, open obligation.

## Exact Objects

A neighbor configuration is a 6-tuple `c ∈ {0,1}^6` indexed by the ordered
directions `(+x,-x,+y,-y,+z,-z)`. Axis type is
`(n_unbalanced, n_both, n_empty)`, where an axis is unbalanced when
`c_{+μ} ≠ c_{-μ}`, both-occupied when both bits are 1, and empty when both
are 0. Complement swaps `n_both` with `n_empty`. Cube-covariance forces a
constant value on each of the ten axis-type orbits. The `F_cut` conditions
`f(empty)=f(full)=0` and `f(c)=f(1-c)` leave five free bits.

Those bits, in remaining order, are:

| bit | axis type | complement |
|---|---|---|
| wt1 | `(1,0,2)` | `(1,2,0)` |
| opp2 | `(0,1,2)` | `(0,2,1)` |
| adj2 | `(2,0,1)` | `(2,1,0)` |
| vertex3 | `(3,0,0)` | self |
| mixed3 | `(1,1,1)` | self |

`f_L1(c)=1` if and only if some axis is unbalanced: equivalently,
`n_μ = c_{+μ} − c_{-μ}` is nonzero for some axis `μ`. This is **not** Hamming parity `|c|_1 mod 2`. The L1 remaining-bit tuple is
`(1, 0, 1, 1, 1)`. It is used only as a contrast predicate, not as a
selector.

The two-cube has the twelve vertices
`(x,y,z)` with `x ∈ {0,1,2}` and `y,z ∈ {0,1}`. Sites are ordered
lexicographically. Seeds of size at most 3 are searched size-first, then
in that site order. Off-patch occupancy `0` means a neighbor outside the
twelve vertices contributes 0. At each tick every unlocked ready site locks
simultaneously. Fill means the halt lock set has cardinality 12.

## Exact Target And Proof Obligations

The exact target is the lex-first seed of size at most 3 at which `f0`
fills and `fwt` does not, together with both lock histories from that seed.

The obligation graph is:

1. rebuild the 24 proper cube rotations and the 10 axis-type orbits;
2. confirm `f0 ∈ Max(1) ∩ Max(2)` and `fwt` in neither;
3. enumerate `|S| ≤ 3` seeds in size-then-lex order and report the first
   split;
4. display both occupancy-to-lock histories from that seed.

All four obligations are closed below and in the runner. Larger patches,
other remaining-bit pairs, and any physical adoption of wt1 are outside
this theorem.

## Theorem 1 — Membership in Max(1) and Max(2)

There are 24 proper cube rotations and 10 axis-type orbits partitioning the
64 cells of `{0,1}^6`. `|F_cut| = 32`. The two-cube has 12 vertices, so
there are 12 one-site seeds and `C(12,2) = 66` two-site seeds.

Scoring every `F_cut` map:

- `Max(1)` has `m = 12` and `N_max = 4`. The maximizers are
  `(1, 0, 1, 1, 0)`, `(1, 0, 1, 1, 1)`, `(1, 1, 1, 1, 0)`, and
  `(1, 1, 1, 1, 1)`. Thus `f0` is in `Max(1)`, with coverage 12.
- `Max(2)` has `m = 66` and `N_max = 2`. The maximizers are
  `(1, 1, 1, 1, 0)` and `(1, 1, 1, 1, 1)`. Thus `f0` is in `Max(2)`,
  with coverage 66.
- `fwt = (0, 1, 1, 1, 0)` has one-site coverage 0 and two-site coverage 0,
  so it is in neither `Max(1)` nor `Max(2)`.
- For completeness of the parent listing: `fwt` has eleven-site coverage 12,
  so it is in `Max(11)`.

Every one-site first wave on the two-cube is a wt1 neighborhood: a neighbor
of the unique locked site sees exactly one occupied opposite pair. Clearing
the wt1 bit therefore freezes every one-site seed, and every two-site seed
whose first wave is still only wt1. That is the membership split.

## Theorem 2 — Lex-first |S|≤3 split seed

Search all unordered seeds with `|S| ≤ 3` in size-then-lex order of their
sorted site tuples. The first seed at which `f0` fills and `fwt` does not
is

```text
S = {(0, 0, 0)},    |S| = 1.
```

No earlier seed exists: the search begins at the lex-first one-site seed,
and that seed already splits. Independently, all 12 one-site seeds split
the same way (`f0` fills each; `fwt` fills none). The theorem reports the
lex-first representative, not a census.

## Theorem 3 — Histories from S

Write `L_t` for the lock set after `t` simultaneous ticks.

For `f0` from `S`:

```text
L_0 = {(0, 0, 0)}
L_1 = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0)}
L_2 = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (2, 0, 0)}
L_3 = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 0, 1), (2, 1, 0)}
L_4 = the twelve-vertex two-cube
```

The halt lock set of `f0` is the full two-cube, so `f0` fills. Halt tick
`T = 4`.

For `fwt` from the same `S`:

```text
L_0 = {(0, 0, 0)}
```

already a fixed point. The first wave is empty because every neighbor of
`(0, 0, 0)` presents a wt1 configuration and `fwt` has wt1 `= 0`. The halt
lock set has cardinality 1, so `fwt` does not fill.

These histories are displayed. Do not adopt wt1.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility.

> A site with no record cannot be read.

Their dependency role is limited to the repository's lattice vocabulary,
covariant nearest-neighbor rule, and unread-absence lock rule. This theorem
separately supplies the two-cube, the `F_cut` pair, and the occupancy ticks.
Off-patch occupancy `0` is an explicit default; a blank-block is a different
rule.

## No-Go Discipline

The result is a finite split on one displayed pair. It is not a universal
selector theorem and not a no-go against other remaining-bit lines.

No-Go Discipline disposition: **PASS**

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| adopt Hamming parity in place of `f_L1` | **ATTEMPTED** | Hamming differs from unbalanced-axis `n_μ ≠ 0` on `{0,1}^6` and is not the remaining-bit coordinate used here |
| treat `Max(11)` membership as 1-site filling | **ATTEMPTED** | `fwt` attains `Max(11)` and has one-site coverage 0 |
| take any 3-site seed as the first split | **ATTEMPTED** | size-then-lex search returns the one-site seed `{(0, 0, 0)}` |
| identify the pair with `f_L1` | **ATTEMPTED** | `f_L1` is `(1, 0, 1, 1, 1)`, not `(1, 1, 1, 1, 0)` |
| write the wt1 bit into Admissibility | **ATTEMPTED** | the bit is displayed; no axiom or approved primitive is added |
| replace off-patch `0` by a blank-block | **ATTEMPTED** | a blank-block is a different rule and is outside the theorem domain |

### N2 — wall independence

One dynamical wall is claimed: on this pair, the first `|S| ≤ 3` seed that
splits fill is the lex-first one-site seed. Membership of `fwt` in `Max(11)`
is a separate coverage fact, not a second impossibility wall.

### N3 — hidden-wall scan

The two-cube, the off-patch default, the remaining-bit coordinates, and the
size-then-lex seed order are all declared. No full-lattice formation law,
physical Admissibility selector, Hamming substitute for `f_L1`, or other
`F_cut` pair is imported.

### N4 — residual matching

The residual after the `Max(11)` listing was whether wt1 is dynamically free
on the mixed3-silent line. This note answers that residual by a first split
seed. It neither closes a physical selector nor enlarges the axiom set.

### N5 — certificate granularity

```text
per-element: executed — each neighbor 6-tuple is scored by axis type
per-site: executed — each of the twelve two-cube vertices uses the same stencil
per-mode: executed — Max(1) and Max(2) are scored over all 32 F_cut maps
per-block: executed — lex search of |S|<=3 seeds reports the first split
lattice-wide: not executed — no Z^3-wide formation law is claimed
```

### N6 — partial-closure paths

A physical rule could still adopt a different remaining-bit tuple, a
different seed class, or a derived dynamics on a larger patch. Every such
route remains live and need not alter the axioms if derived from separately
supported structure.

### N7 — steelman

The strongest objection is that a later seed, or a different lex convention,
might be the intended first split. Correct that convention is part of the
hypothesis: size-then-lex on the declared site order. Under that order the
first split is uniquely `{(0, 0, 0)}`. Another order would be another
theorem.

### N8 — cross-cycle echo

Earlier coverage work named `f0` as a two-site maximizer and placed `fwt`
in `Max(11)` minus `Max(1)`. This note agrees with those listings and
contributes only the first dynamical split of that mixed3-silent pair.

## Boundaries and explicit non-claims

- The theorem is conditional on the two-cube and off-patch occupancy `0`.
- It does not classify all `|S| ≤ 3` split seeds; it reports the lex-first
  one.
- It does not adopt `f0`, `fwt`, or the wt1 bit as a physical rule.
- Hamming parity is not a substitute for `f_L1`.
- No axiom, primitive, registry, or audit verdict is edited.
- Do not write them into Admissibility.

## Verification

Run:

```bash
python3 scripts/f_cut_wt1_zero_f0_first_split_2026_08_15.py
```

The runner rebuilds the orbits, scores `Max(1)` and `Max(2)` over all 32
`F_cut` maps, searches `|S| ≤ 3` seeds in size-then-lex order, and checks
both lock histories from the reported seed. Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
