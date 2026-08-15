---
claim_id: f_two_three_site_seed_fill_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the twelve-vertex two-cube with off-patch o=0 and a displayed 3-site seed, f_two occupancy ticks reach a fixed point with a reported (T, |locks|). Displayed, not adopted. No clock/source identities."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_two_three_site_seed_fill_2026_08_15.py
---

# f_two Three-Site Seed Fill On The Two-Cube

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** occupancy-lock ticks of the displayed f_two ready rule
(form iff `u >= 2`) on one twelve-site two-cube carrier, from one
displayed 3-site seed. The pair `(T, |locks_T|)` is a finite halt
census. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_two_three_site_seed_fill_2026_08_15.py`](../scripts/f_two_three_site_seed_fill_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The two-cube patch has twelve vertices. Off-patch occupancy is `o = 0`.
The displayed seed is the axis triple of the origin corner,

```text
S0 = {(1,0,0), (0,1,0), (0,0,1)}.
```

That triple has a nonempty first wave, so it is the working seed (the
same algebra as the f_two minimal-seed census). Each tick locks every
unlocked ready site at once. Ready means `u(v) >= 2` with `v` unlocked,
where `u(v)` is the number of axes at `v` with `o_{+μ} ≠ o_{-μ}`.

The process reaches a fixed point at halt tick `T = 2` with
`|locks_2| = 8`. The twelve-vertex patch does not fill.

Displayed contrast only (not a clone table): L1 from a 1-site seed
halts at diameter 4 with 12 locks. That is a different member. Here
f_two from this 3-site seed stops short of the patch.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact occupancy-lock halt census of displayed f_two on one twelve-site two-cube carrier from one 3-site seed."
trace_class: frontier_discovery
target_claim_id: f_two_three_site_seed_fill
target_blocker_text: "whether displayed f_two from the axis-triple seed fills the twelve-site two-cube"
source_of_blocker_text: handoff
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independent audit of the bounded halt census"
conditional_surface_status: "exact on the supplied two-cube f_two patch and seed; other members and complexes remain separate"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

`cache_write: false`

## Inputs And Import Boundary

- **Framework dependency:** live Lattice and Record sentences, quoted without rewrite.
- **Explicit theorem-domain condition:** displayed f_two ready rule
  `u >= 2`, two-cube patch, off-patch occupancy zero, axis-triple seed,
  simultaneous lock of every unlocked ready site.
- **External empirical or literature inputs:** none.

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

For each site `v` and axis `μ ∈ {x,y,z}`,

```text
u(v) = |{ μ : o(v+e_μ) ≠ o(v−e_μ) }|.
```

A site is ready iff it is unlocked and `u(v) >= 2`. One tick replaces
the lock set `L` by `L ∪ { v ∈ V \ L : u(v) >= 2 }`. Locked sites stay
locked.

Seed locks `S0`. First wave is the ready set at `L = S0`.

## Exact Target And Proof Obligations

Check that the first wave is nonempty, that the iteration reaches a
fixed point in at most 12 ticks, and report the exact pair
`(T, |locks_T|)` together with whether `|locks_T| = 12`.

## Theorems

### Theorem 1 — first wave is nonempty

At `L = S0` the origin `(0,0,0)` has all three axes unbalanced, so
`u = 3`. The sites `(0,1,1)`, `(1,0,1)`, and `(1,1,0)` each have
`u = 2`. The first wave is

```text
{(0,0,0), (0,1,1), (1,0,1), (1,1,0)}.
```

It is nonempty.

### Theorem 2 — a fixed point in at most 12 ticks

The site set is finite of size 12, locks are permanent, and each
non-halt tick adds at least one lock. The iteration therefore reaches
a fixed point in at most 12 ticks.

### Theorem 3 — halt pair and fill boolean

After two ticks the lock set equals cube `A`:

```text
T = 2,   |locks_2| = 8,   locks_2 = A ≠ V.
```

The four `x = 2` sites remain unlocked, each with `u = 1`. The
twelve-vertex patch does not fill. That boolean is the member
difference versus L1 from a 1-site seed, which is displayed only as
halting at diameter 4 with 12 locks.

## What Is Not Claimed

- No unique member of the axiom class, and no adoption of f_two.
- No clock identity, no source identity, and no formation-count table.
- No leftover-character classification.
- No 4x4x4, torus, or line complex.
- No axiom edit and no replacement of the live Record sentences.
- Qubit remains `M_2(C)`.
- No inverse-square law and no Newtonian identification.

## Runner Contract

The companion runner reconstructs the occupancy-lock ticks on the
displayed patch and checks the theorems with exact integer arithmetic.
It prints `TOTAL: PASS=... FAIL=...` and writes no cache. Declared
review inputs are this note and the axiom memo only.
