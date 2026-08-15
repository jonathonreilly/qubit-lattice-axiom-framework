---
claim_id: hamming_parity_formation_dynamics_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Hamming-parity formation on the twelve-vertex two-cube from a 1-site seed with off-patch o=0 reaches a fixed point with reported (T, |locks|). Distinct from L1. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/hamming_parity_formation_dynamics_2026_08_15.py
---

# Hamming-Parity Formation Dynamics On The Two-Cube

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** occupancy-lock ticks of the displayed Hamming-parity ready rule
`f_H(c) = |c|_1 mod 2` on one twelve-site two-cube carrier, from one
1-site seed, with off-patch occupancy `o = 0`. The pair `(T, |locks_T|)`
is a finite halt census. Distinct from L1. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/hamming_parity_formation_dynamics_2026_08_15.py`](../scripts/hamming_parity_formation_dynamics_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The two-cube patch has twelve vertices. Off-patch occupancy is `o = 0`.
The displayed seed locks the origin corner `(0,0,0)`. Each tick locks
every unlocked site whose six-neighbor occupancy 6-tuple `c` has
`f_H(c) = |c|_1 mod 2` equal to 1.

The first wave is the three axis sites. The process reaches a fixed
point at halt tick `T = 4` with `|locks_4| = 9`. The twelve-vertex
patch does not fill.

Displayed contrast only (not an identity table): L1 from the same
1-site seed fills, with horizon 4 and 12 locks. That is a different
member. Hamming parity is never the unbalanced-axis rule. Do not call
Hamming `f_L1`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact occupancy-lock halt census of displayed Hamming parity on one twelve-site two-cube carrier from a 1-site seed."
trace_class: frontier_discovery
target_claim_id: hamming_parity_formation_dynamics
target_blocker_text: "whether displayed Hamming-parity occupancy ticks from a 1-site seed fill the twelve-site two-cube"
source_of_blocker_text: handoff
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independent audit of the bounded halt census"
conditional_surface_status: "exact on the supplied two-cube Hamming-parity patch and seed; other members and complexes remain separate"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

`cache_write: false`

## Inputs And Import Boundary

- **Framework dependency:** live Lattice and Record sentences, quoted without rewrite.
- **Explicit theorem-domain condition:** displayed Hamming-parity ready rule
  `f_H(c) = |c|_1 mod 2`, two-cube patch, off-patch occupancy zero,
  1-site seed `(0,0,0)`, simultaneous lock of every unlocked ready site.
- **External empirical or literature inputs:** none.

This note is occupancy-lock dynamics of one displayed member. It is not
a static membership count of a cut class.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> Records form.

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone.

Their dependency role is limited to the cubic site set, lock permanence, and
the unreadability of absence. The occupancy kernel, the two-cube patch, the
seed, and the tick index are separately supplied.

## Exact Objects

All runner values are exact integers. No float is used.

Cubes `A = {0,1} × {0,1} × {0,1}` and `B = {1,2} × {0,1} × {0,1}`.
Patch `V = A ∪ B`, so `|V| = 12`. Occupancy of a site is `1` if the
site is locked and `0` otherwise, including every off-patch neighbor.

At an unlocked site `v`, write `c(v) ∈ {0,1}^6` for the occupancy of
the six nearest neighbors `(v±e_x, v±e_y, v±e_z)`. The displayed
ready rule is

```text
f_H(c) = |c|_1 mod 2.
```

A site is ready iff it is unlocked and `f_H(c(v)) = 1`. One tick
replaces the lock set `L` by `L ∪ { v ∈ V \ L : f_H(c(v)) = 1 }`.
Locked sites stay locked. Halt is at most 12 ticks.

Displayed contrast member (not used as the ready rule here):

```text
f_L1(c) = 1  iff  some axis has c_{+μ} ≠ c_{-μ}
         iff  n ≠ 0.
```

Weight-1 tuples are odd, so they are Hamming-ready. They are also
L1-ready. Weight-2 tuples with two unbalanced axes are even, so they
are Hamming-blank and L1-ready. The first waves therefore coincide;
later waves do not.

## Exact Target And Proof Obligations

Check that the first wave is the three axis sites, that the iteration
reaches a fixed point in at most 12 ticks, and report the exact pair
`(T, |locks_T|)` together with whether `|locks_T| = 12`.

## Theorems

### Theorem 1 — first wave is the three axis sites

At `L = {(0,0,0)}` the on-patch neighbors of the seed are
`(1,0,0)`, `(0,1,0)`, and `(0,0,1)`. Each of those sites has a
weight-1 occupancy 6-tuple (one occupied neighbor, the seed; every
off-patch slot is 0). Weight 1 is odd, so `f_H = 1`. Every other
unlocked patch site has weight 0. The first wave is

```text
{(1,0,0), (0,1,0), (0,0,1)}.
```

### Theorem 2 — a fixed point in at most 12 ticks

The site set is finite of size 12, locks are permanent, and each
non-halt tick adds at least one lock. The iteration therefore reaches
a fixed point in at most 12 ticks.

The computed orbit is

```text
t=0:  |locks| = 1   seed
t=1:  |locks| = 4   three axis sites
t=2:  |locks| = 5   add (2,0,0)
t=3:  |locks| = 7   add (2,1,0), (2,0,1)
t=4:  |locks| = 9   add (1,1,0), (1,0,1)
t=5:  ready set empty.
```

So a fixed point is reached.

### Theorem 3 — halt pair and fill boolean

```text
T = 4,   |locks_4| = 9,   locks_4 ≠ V.
```

The three remaining unlocked sites are `(0,1,1)`, `(1,1,1)`, and
`(2,1,1)`. Each has even Hamming weight on its 6-tuple, so none is
ready. The twelve-vertex patch does not fill.

Displayed contrast only: L1 from the same seed fills, horizon 4,
`|locks_4| = 12`. Those numbers are not an identity between the two
rules.

## What Is Not Claimed

- No unique member of the axiom class, and no adoption of Hamming parity.
- Hamming parity is not L1 and is not the unbalanced-axis rule.
- No leftover-character classification of a static cut class.
- No clock identity, no source identity, and no formation-count table.
- No 4x4x4, torus, or line complex.
- No axiom edit and no replacement of the live Record sentences.
- Qubit remains `M_2(C)`.
- No inverse-square law and no Newtonian identification.

## Runner Contract

The companion runner reconstructs the occupancy-lock ticks on the
displayed patch and checks the theorems with exact integer arithmetic.
It evaluates `f_H` on computed 6-tuples. It prints
`TOTAL: PASS=... FAIL=...` and writes no cache. Declared review inputs
are this note and the axiom memo only.
