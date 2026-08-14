---
claim_id: two_cube_l1_hop_tick_scale_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the supplied two-cube carrier S={0,1,2}×{0,1}×{0,1} with seed (0,0,0), the saturated nearest-neighbor causal front determines occupancy ρ and first-lock times φ. Axis sites (1,0,0) and (2,0,0) are unread before ticks 1 and 2 respectively and locked at those ticks. The unique a in {1,2,3} such that each axis site at ℓ¹-distance d forms at tick a·d is a=1. This is not a five-site line and not a one-snapshot leftover comparison of a formation set to ρ."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_hop_tick_scale_2026_08_14.py
---

# Unique Hop-To-Tick Scale On The Two-Cube L1 Axis Is One

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact occupancy history and first-lock times on one supplied
two-cube carrier under a named saturated nearest-neighbor causal-front
rule. No physical clock metric, rate, or lattice-wide formation kernel is
asserted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_hop_tick_scale_2026_08_14.py`](../scripts/two_cube_l1_hop_tick_scale_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Take the two-cube site set

```text
S = {0,1,2} × {0,1} × {0,1}
```

with seed `s = (0,0,0)` and axis sites `p_1 = (1,0,0)`, `p_2 = (2,0,0)`.
The ambient lattice `ℓ¹` distances are `d(p_1)=1` and `d(p_2)=2`.

Occupancy `ρ` and first-lock time `φ` are computed from the saturated
nearest-neighbor causal front: the seed is locked at tick `0`; a previously
unread site locks at the first later tick at which a nearest neighbor is
already locked. The runner evaluates this update on `S`; it does not insert
the integers `1` and `2` as expected lock times.

The computed pair is:

```text
ρ_0(p_1)=0,  ρ_1(p_1)=1,  φ(p_1)=1,
ρ_0(p_2)=ρ_1(p_2)=0,  ρ_2(p_2)=1,  φ(p_2)=2.
```

Among `a ∈ {1,2,3}`, the only value satisfying `φ(p)=a·d(p)` at both axis
sites is `a=1`. The candidate `a=2` would require `p_1` to form at tick `2`,
which the computed history falsifies.

This member is not a five-site line: `S` has twelve sites and a transverse
`{0,1}×{0,1}` face, and the theorem uses the pair `(ρ,φ)` rather than a
scalar occupancy sequence. It is not a leftover-character comparison of a
formation set `F` to `ρ` on one snapshot: `φ` is the first-lock map of the
whole occupancy history.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite occupancy and first-lock times on one two-cube under a named causal-front rule; uniqueness of a in {1,2,3} is a finite census, not a physical clock derivation."
trace_class: frontier_discovery
target_claim_id: two_cube_l1_hop_tick_scale
target_blocker_text: "uniqueness of the hop-to-tick scale a on the two-cube L1 axis"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded two-cube uniqueness claim"
conditional_surface_status: "exact on the supplied two-cube and saturated nearest-neighbor causal-front rule; no physical clock, rate, or full Z^3 formation kernel is asserted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** Lattice supplies sites of `Z^3` and nearest-neighbor
  adjacency. Record supplies that records form, that a present record locks
  one admissible local possibility, and that a site with no record cannot be
  read. These sentences are quoted without rewrite. They do not, by
  themselves, select the saturated causal-front update used below.
- **Explicit theorem-domain condition:** the finite carrier `S`, the seed, and
  the saturated nearest-neighbor causal-front update that produces `ρ` and
  `φ`. This is named test dynamics on `S`, not a derivation of the physical
  formation kernel, formation probability, or rate.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** identifying the discrete tick with physical
  elapsed time, promoting `a=1` off this member, or replacing the named
  update by a derived full-lattice formation law remain separate obligations.

## Exact Objects

Write sites as integer triples. The two-cube is the union of the unit cubes
with corners in `{0,1}^3` and `{1,2}×{0,1}×{0,1}`. It has twelve sites.
Nearest neighbors are pairs in `S` at ambient `ℓ¹` distance one. No diagonal
step is an edge.

The seed is locked at tick `0`. Occupancy `ρ_t : S → {0,1}` is `1` exactly
when a record is present at that site by tick `t`. First-lock time is

```text
φ(x) = min{ t ∈ {0,1,2} : ρ_t(x) = 1 },
```

or unread if the minimum is empty. The update is

```text
ρ_0(s) = 1,   ρ_0(x) = 0 for x ≠ s,
ρ_{t+1}(x) = 1  if  ρ_t(x)=1 or some nearest neighbor y of x has ρ_t(y)=1,
ρ_{t+1}(x) = 0  otherwise.
```

A site is unread at tick `t` when `ρ_t(x)=0`. It is locked at tick `t` when
`ρ_t(x)=1`. Record unreadability is used only as this occupancy tag: absence
receives no scalar readout.

The hop-to-tick scale test on the axis is the finite predicate

```text
P(a) ⇔  φ(p_1)=a·d(p_1)  and  φ(p_2)=a·d(p_2)
```

for `a ∈ {1,2,3}`.

## Theorem 1 — axis site at distance one

The site `p_1=(1,0,0)` is a nearest neighbor of the seed, so it is unread at
tick `0` and becomes locked at tick `1`. Direct evaluation of the update
gives `ρ_0(p_1)=0`, `ρ_1(p_1)=1`, and `φ(p_1)=1`. It does not lock earlier
than its `ℓ¹` distance.

## Theorem 2 — axis site at distance two

The site `p_2=(2,0,0)` is not adjacent to the seed. Its unique two-cube
neighbor toward the seed is `p_1`. After Theorem 1, `p_1` is first locked at
tick `1`, so `p_2` remains unread at ticks `0` and `1` and locks at tick `2`.
Thus `φ(p_2)=2`. It does not lock earlier than its `ℓ¹` distance.

## Theorem 3 — unique scale in `{1,2,3}` is `a=1`

The two axis identities of Theorems 1 and 2 are `φ(p_1)=1·d(p_1)` and
`φ(p_2)=1·d(p_2)`, so `P(1)` holds.

If `a=2`, then `P(2)` requires `φ(p_1)=2`. Theorem 1 gives `φ(p_1)=1≠2`, so
`P(2)` fails. If `a=3`, then `P(3)` requires `φ(p_1)=3`, which is likewise
false.

The runner enumerates `{1,2,3}` and returns the singleton `{1}`. That is the
uniqueness statement of this note.

## Mutation Checks

1. Replacing the two-cube by the five-site line
   `{(k,0,0) : k=0,...,4}` removes the transverse face and the pair
   `(ρ,φ)` as used here. That carrier is a different object and is not this
   member.
2. Comparing a formation set `F_t={x : ρ_t(x)=1}` to `ρ_t` at a single
   tick is a leftover identity on one snapshot. At tick `1` one has
   `p_1 ∈ F_1` and `p_2 ∉ F_1`, which does not determine `φ(p_2)` or test
   `P(a)` at both distances.
3. The candidate `a=2` is rejected by the computed `φ(p_1)`.
4. No site of `S` locks at a tick strictly earlier than its ambient `ℓ¹`
   distance from the seed.

## What This Does Not Claim

- The saturated causal-front update is not claimed to be the unique physical
  formation law of the axiom memo.
- Discrete ticks are not identified with a physical time metric or rate.
- Uniqueness of `a` is only inside `{1,2,3}` on this two-cube axis, not a
  classification of all clock maps on `Z^3`.
- Locked content is not selected: Admissibility's conditional distribution
  is not evaluated, and `φ` is a first-lock tick, not a Bloch vector.
- Absence is unread and is assigned no scalar.
- No axiom, primitive, registry, or audit verdict is edited.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

> Records form.

> When present, a record locks exactly one admissible local possibility.

> A site with no record cannot be read.

Their dependency role is limited to the repository's lattice adjacency and
record unread/lock vocabulary. The two-cube, the seed, and the saturated
causal-front update are separately supplied theorem-domain data.

## Runner Contract

The companion runner builds `S`, runs the occupancy update through tick `2`,
derives `φ` from the full history of `ρ`, and enumerates `a ∈ {1,2,3}`. It
checks Theorems 1–3, the four mutations, the live axiom sentences, and the
import boundary. Declared review inputs are this note and the axiom memo
only. The runner writes no cache and no citation manifest.

## Verification

Run:

```bash
python3 scripts/two_cube_l1_hop_tick_scale_2026_08_14.py
```

Expected summary:

```text
TOTAL: PASS>=8 FAIL=0
```
