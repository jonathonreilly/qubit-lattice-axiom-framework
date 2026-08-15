---
claim_id: f_l1_six_site_miss_orbit_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the four 6-site seeds that f_L1 does not fill form N_orb orbits under two-cube-preserving rotations. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_l1_six_site_miss_orbit_2026_08_15.py
---

# Six-Site `f_L1` Misses Are One Three-Long-Axis-Edge Orbit

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock census of all six-site seeds on the
twelve-vertex two-cube with off-patch occupancy `0`, together with the
orbit type of the miss set under two-cube-preserving rotations. No seed
is adopted. No Admissibility selector is written.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_l1_six_site_miss_orbit_2026_08_15.py`](../scripts/f_l1_six_site_miss_orbit_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The two-cube is the twelve-site block `{0,1,2} × {0,1} × {0,1}`. The
off-patch occupancy is the explicit default `0`; a blank-block is a different rule.
There are exactly `C(12,6) = 924` unordered six-site seeds.

The map `f_L1` fires at a site if and only if some cubic axis of its
nearest-neighbor occupancy is unbalanced: `n_unbalanced ≠ 0`, equivalently
`n_μ ≠ 0` on at least one axis. This is not Hamming parity of the six
neighbor bits.

Starting from a seed as the locked set and iterating occupancy-to-lock with
off-patch occupancy `0`, `f_L1` fills the two-cube from `920` of those
seeds. The miss set `M` therefore has `|M| = 4`. This reconfirms the count
`cov6(L1) = 920`; the object here is not that count.

The eight proper cubic rotations about the two-cube barycenter that send the
two-cube to itself act on six-site seeds. They partition `M` into
`N_orb = 1` orbit. One lexicographic representative of that orbit is

```text
R_tri = {(0,0,0), (0,0,1), (0,1,0), (2,0,0), (2,0,1), (2,1,0)}     (orbit size 4)
```

This is the first `N_orb` at `|S| = 6`. The earlier four-site orbit type
`#6463` was `k = 4`. These are displayed, not adopted. Do not adopt a seed.
They are not written into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exhaustive six-site census and the two-cube-preserving rotation action determine |M|=4 and N_orb=1 with one lex representative per orbit."
trace_class: frontier_discovery
target_claim_id: f_l1_six_site_miss_orbit
target_blocker_text: "geometric type of the four six-site seeds f_L1 does not fill"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the two-cube with off-patch occupancy 0; no seed or map is adopted"
hypothetical_axiom_status: "none; f_L1 and the miss orbit are displayed occupancy data, not axiom content"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded census and orbit type"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice, Admissibility, and Record
  sentences quoted below supply cubic nearest-neighbor wording and the lock
  rule. They are quoted without rewrite.
- **Explicit theorem-domain condition:** the two-cube, off-patch occupancy
  `0`, the unbalanced-axis predicate `f_L1`, and the two-cube-preserving
  rotation action are supplied finite data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selection of a seed or of `f_L1` by
  Admissibility or Record remains a separate, open obligation.

## Exact Objects

Sites are points of `Z^3`. The two-cube is

```text
V = {0,1,2} × {0,1} × {0,1},    |V| = 12.
```

On-patch occupancy of a site is the lock bit. Off-patch occupancy is `0`.
For a locked set `L ⊂ V` and a site `x ∈ V`, each cubic axis `μ` contributes
one pair `(c_{μ+}, c_{μ-})` of neighbor occupancies. Write

```text
n_unbalanced = |{μ : c_{μ+} ≠ c_{μ-}}|.
```

Then `f_L1(x; L) = 1` if and only if `n_unbalanced ≠ 0`. Hamming parity of
the six neighbor bits is a different map: the opposite-axis pair
`(c_{μ+}, c_{μ-}) = (1, 1)` has Hamming weight `2` and `n_unbalanced = 0`,
so `f_L1` refuses it.

A six-site seed is an unordered 6-subset of `V`. Occupancy-to-lock starts
from `L_0 = S` and at each tick adds every unlocked two-cube site at which
`f_L1` fires. The seed fills when some `L_t = V`. Coverage is

```text
cov6(L1) = |{S ⊂ V : |S| = 6 and S fills under f_L1}|.
```

Two-cube-preserving rotations are the eight proper cubic rotations about the
barycenter `(1, 1/2, 1/2)` that send `V` to `V`. Equivalently, they are the
rotational symmetries of the `3 × 2 × 2` prism: the long axis stays the
long axis. They act on six-site seeds by acting on sites.

The four long-axis corner edges of the prism are the pairs
`{(0,y,z), (2,y,z)}` for `(y,z) ∈ {0,1}^2`. This is a derived description
of `M`, not a selector.

## Exact Target And Proof Obligations

The exact target is the cardinality of `M` and its orbit type under
two-cube-preserving rotations.

1. enumerate all `924` six-site seeds and reconfirm `cov6(L1) = 920`,
   hence `|M| = 4`;
2. generate the eight two-cube-preserving rotations from the `24` proper
   cubic rotations and compute `N_orb` together with one lex representative
   per orbit;
3. display that representative and refuse to adopt a seed.

All three obligations are closed below and in the runner. There is no
missing lemma for this bounded census. Adopting a seed, writing a selector
into Admissibility, or promoting the count `#6465` to a leftover table
would be a different claim.

## Theorem 1 — `|M| = 4`

There are exactly `924` six-site seeds. Independent occupancy-to-lock
runs with off-patch occupancy `0` give `cov6(L1) = 920`. Therefore
`|M| = 4`.

Every miss seed locks exactly the eight end-face sites
`{0,2} × {0,1} × {0,1}` and halts with history `(6, 8)`. The middle layer
`x = 1` never locks. That common halt is supporting geometry for the
orbit type; it is not a fourth leftover row.

## Theorem 2 — `N_orb = 1`

The two-cube-preserving rotation group has order `8`. It preserves `M`.
The action has one orbit:

- the three-of-four long-axis edge type, size `4`, lex representative
  `R_tri = {(0,0,0), (0,0,1), (0,1,0), (2,0,0), (2,0,1), (2,1,0)}`.

Thus `N_orb = 1`. Each miss is the six endpoints of three of the four
long-axis corner edges. Those four choices of the omitted edge form a
single orbit. This three-long-axis-edge type is the geometric object. It is
not a 4-row leftover table. Not leftover-character of `#6465`, which named
only the count `cov6(L1) = 920`. First `N_orb` at `|S| = 6`; `#6463` was
`k = 4`.

The identity-only action would give four singleton orbits and would be
exactly that leftover table. The two-cube-preserving action is not the
identity-only action.

## Theorem 3 — display, do not adopt

The lex representative and the value `N_orb = 1` are displayed
occupancy-to-lock data. Do not adopt a seed. Do not adopt `R_tri`. Do not
write a seed, an orbit representative, or `f_L1` into Admissibility.
Displayed, not adopted.

## Physical-Interpretation Boundary

The proved output is the displayed orbit type of a finite miss set on a
supplied two-cube. This note neither assigns those seeds a physical label
nor changes the Lattice, Qubit, Admissibility, or Record sentences.
`f_L1` is displayed occupancy data, not axiom content, and no additional
axiom is proposed.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. `f_L1` is not Hamming parity of the six neighbor bits;
2. the identity-only action on `M` has four orbits, not `N_orb = 1`;
3. a 4-row leftover list of seeds is not the claimed object.

## What This Does Not Claim

- `f_L1` is not selected by Admissibility or Record.
- No six-site seed is a preferred physical initial condition.
- Coverage on other patches, other occupancy defaults, or other maps in
  `F_cut` is not computed here.
- The common halt at the two end cubes is not promoted to a dynamics law.
- Independent class-`C` leftovers are not used as parents.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

> When present, a record locks exactly one admissible local possibility.

> A readout value is determined by record content alone.

> A site with no record cannot be read.

> does not supply the formation site, probability, or rate

Their dependency role is limited to cubic nearest-neighbor vocabulary and
the lock rule. This theorem separately supplies the two-cube, the
off-patch default `0`, and the unbalanced-axis predicate.

## Runner Contract

The companion runner re-enumerates all `924` six-site seeds, recomputes
`cov6(L1)` and `M`, generates the eight two-cube-preserving rotations from
the `24` proper cubic rotations, and reports `N_orb` with one lex
representative per orbit. It checks the three mutations, quotes the live
axiom sentences, and records the import boundary. Declared review inputs
are this note and the axiom memo only.
