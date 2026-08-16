---
claim_id: l1_minkowski_light_match_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Whether displayed L1 arrival `t=ℓ¹` on the radius-4 integer ball matches Euclidean-isotropic `c` and the discrete `ℓ²` null cone is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/l1_minkowski_light_match_2026_08_15.py
---

# Displayed L1 Arrival Does Not Match Observed Minkowski Light

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact integer comparison of the already-displayed origin-seed
arrival `t(v)=|v|_1` on the radius-4 ball in `Z^3` against Euclidean-isotropic
unit `c` and the discrete `ℓ²` null set. No occupancy step is re-run. No new
spatial patch is grown. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/l1_minkowski_light_match_2026_08_15.py`](../scripts/l1_minkowski_light_match_2026_08_15.py)

## Result Up Front

The displayed first-arrival function from an origin seed on the cubic lattice
is the taxicab / `ℓ¹` arrival

```text
t(v) = |v_1| + |v_2| + |v_3|
```

on `Z^3`. This note scores that already-displayed function on the finite set
of nonzero integer vectors with `|v|_1 ≤ 4`. It does not attach `ℓ¹` as a
primitive, does not write Minkowski structure or a boost into Admissibility,
and does not adopt a Wick map.

Observed light, used here only as an external comparison object, has one
Euclidean-isotropic speed, discrete null relation `t^2 = |v|_2^2`, and
Lorentz boosts that mix the time coordinate with a spatial axis.

On the scored ball the displayed arrival matches none of those three
properties.

| census | value |
|---|---:|
| `N_ball` | `128` |
| `N_null` | `24` |
| `N_both` | `24` |

`N_ball` is the number of nonzero `v ∈ Z^3` with `|v|_1 ≤ 4`. `N_null` is
the number of those vectors with `t(v)^2 = |v|_2^2`. `N_both` is the same
set, because the null comparison is evaluated only on the scored ball.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

Those sentences supply the cubic graph and its 24 proper cube rotations. They
do not supply a Minkowski metric, a Lorentz boost, an isotropic Euclidean
speed, or an arrival law. The arrival `t=ℓ¹` is a displayed graph-distance
function on that nearest-neighbor adjacency, scored here and not adopted.

The scored object is taxicab arrival. It is not Hamming weight. An occupancy
face of the form `n≠0` is not used and is not re-run.

## Exact Objects

For `v=(v_1,v_2,v_3) ∈ Z^3` write

```text
t(v) := |v_1| + |v_2| + |v_3|,
|v|_2^2 := v_1^2 + v_2^2 + v_3^2.
```

The scored set is

```text
B := { v ∈ Z^3 : v ≠ 0 and t(v) ≤ 4 }.
```

The discrete null set on that ball is

```text
N := { v ∈ B : t(v)^2 = |v|_2^2 }.
```

All comparisons are integer. No continuum interpolant and no new occupancy
propagation on a `4×4×4` or any other spatial patch is introduced.

## Theorem 1 — Euclidean-Isotropic Unit `c` Fails

A Euclidean-isotropic unit speed would require the ratio

```text
t(v)^2 / |v|_2^2
```

to be constant on `B`. It is not. The axis witness `(1,0,0)` gives

```text
t=1,   |v|_2^2=1,   t^2 / |v|_2^2 = 1.
```

The face-diagonal witness `(1,1,0)` gives

```text
t=2,   |v|_2^2=2,   t^2 / |v|_2^2 = 2.
```

A common positive rescaling `t ↦ k t` cannot equalize those two ratios,
because both numerator and the comparison remain homogeneous of degree two
and the ratio `2/1` is invariant. Therefore displayed `ℓ¹` arrival is not
one Euclidean-isotropic `c`.

## Theorem 2 — Discrete `ℓ²` Null Is A Proper Subset

The identity `t(v)^2 = |v|_2^2` expands to

```text
2(|v_1 v_2| + |v_1 v_3| + |v_2 v_3|) = 0,
```

so at most one coordinate is nonzero. On `B` those axis vectors are exactly
the `6×4=24` points `±r e_i` for `r=1,2,3,4` and `i=1,2,3`. The
face-diagonal witness `(1,1,0)` lies in `B` with arrival `2` and
`|v|_2^2=2`, but `t^2=4 ≠ 2`. Hence `N` is a proper subset of `B`, with

```text
N_ball=128,    N_null=24,    N_both=24.
```

Displayed `ℓ¹` arrival is therefore not the discrete `ℓ²` null cone.

## Theorem 3 — Cube Rotations Do Not Mix Time And Space

Observed Lorentz boosts mix a time coordinate with a spatial axis. The
standard rational boost with `γ=5/4` and `β=3/5` sends

```text
(t,x) ↦ ((5t-3x)/4, (5x-3t)/4)
```

and therefore mixes `t` with `x`.

The Lattice axiom's 24 proper cube rotations act on `Z^3` alone. Each is a
signed permutation of determinant `+1`. Every such map preserves every `ℓ¹`
sphere `{v : t(v)=r}` and every Euclidean length-squared `|v|_2^2`. The
arrival value `t(v)` is unchanged because it is a function of the spatial
vector only; no rotation manufactures a mixed `(t,x)` pair.

Displayed L1 light is therefore not observed Minkowski light. The comparison
is displayed, not adopted. This note does not write Minkowski structure, a
boost, or a Wick map into Admissibility.

## Representative Witnesses

| `v` | `t=|v|_1` | `|v|_2^2` | `t^2/|v|_2^2` | in `N`? |
|---|---:|---:|---:|---|
| `(1,0,0)` | `1` | `1` | `1` | yes |
| `(2,0,0)` | `2` | `4` | `1` | yes |
| `(1,1,0)` | `2` | `2` | `2` | no |
| `(1,1,1)` | `3` | `3` | `3` | no |
| `(2,1,0)` | `3` | `5` | `9/5` | no |

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer comparison of displayed t=ℓ¹ on the radius-4 ball against isotropic-c constancy, the discrete ℓ² null set, and the 24 cube rotations. Observed Minkowski structure is an external comparison object, not a derived or adopted law."
trace_class: negative_route_pruning
target_claim_id: displayed_l1_matches_observed_minkowski_light
target_blocker_text: "displayed L1 arrival is taxicab; observed light is Euclidean-isotropic with an ℓ² null cone and boosts"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Keep t=ℓ¹ displayed and unattached. Do not adopt a Wick map or write a boost into Admissibility. Any Lorentzian reconstruction is a separate bridge."
conditional_surface_status: "exact on the scored radius-4 integer ball; no occupancy re-run and no adopted Minkowski law"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Proof-Obligation Boundary

| Obligation | Disposition |
|---|---|
| identify displayed arrival as `t=ℓ¹` | scored displayed function; not attached |
| Euclidean-isotropic unit `c` on `B` | closed by Theorem 1; ratios `1` and `2` |
| discrete `ℓ²` null census | closed by Theorem 2; `128/24/24` |
| 24 proper cube rotations preserve `ℓ¹` spheres | closed by Theorem 3 |
| cube rotations mix `t` with a spatial axis | closed in the negative; they do not |
| observed boosts mix `t` and `x` | external comparison identity only |
| re-run occupancy or grow a new patch | outside the claim |
| adopt Minkowski, a boost, or a Wick map | outside the claim; not written into axioms |

The proof boundary is **CONDITIONAL** on treating `t=ℓ¹` as the already
displayed arrival and treating Minkowski light as an external comparison
object. Displayed, not adopted.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Lattice / Admissibility wording | cubic graph and 24 proper rotations | approved `minimal_axioms`; no Minkowski content |
| displayed arrival `t=ℓ¹` | scored function | displayed graph distance; not attached |
| radius-4 integer ball | finite comparison domain | declared; integer enumeration only |
| Euclidean-isotropic `c` and `t^2=|v|_2^2` | external comparison objects | not derived, not adopted |
| Lorentz boosts | external comparison objects | not derived, not adopted |
| occupancy / `n≠0` face | unused | not re-run |
| Hamming weight | unused | not the arrival function |
| observational data | input | none fitted |

## Boundary And Non-Claims

- The note does not attach `ℓ¹` as a primitive or as axiom content.
- It does not write Minkowski structure, a Lorentz boost, or a Wick map into
  Admissibility or any other axiom.
- It does not re-run an occupancy step and does not grow L1 on a `4×4×4` or
  any new spatial patch.
- It does not identify Hamming weight with arrival.
- It does not claim that a later, separately derived Lorentzian reconstruction
  is impossible.
- It does not edit an axiom or install a framework primitive.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | It scores whether displayed `t=ℓ¹` matches Euclidean-isotropic `c` and the discrete `ℓ²` null cone. |
| V2 | New content? | The durable content is the exact radius-4 census and the three closed mismatch theorems. |
| V3 | Independently checkable? | Yes. The ball, ratios, null set, and 24 rotations are exact integers. |
| V4 | More than a restatement? | Yes. Prior display of taxicab arrival is not itself a comparison to observed light. |
| V5 | One-step relabel? | No. Constancy, null membership, and boost-versus-cube-rotation are distinct checks. |

## No-Go Discipline Gate

The only negative shipped is: the displayed arrival `t=ℓ¹` on the radius-4
integer ball is not Euclidean-isotropic unit `c`, is not the discrete `ℓ²`
null cone, and is not mixed by the 24 cube rotations the way a Lorentz boost
mixes `t` and `x`. No global Lorentzian non-derivability is claimed.

### N1 — Materially distinct routes

| Route | Attempt and outcome | Marker |
|---|---|---|
| Constant rescaling of `t` | `t ↦ k t` leaves the ratio of `(1,0,0)` to `(1,1,0)` equal to `2` | **ATTEMPTED** |
| Restrict the domain to axes | Then `t^2=|v|_2^2` holds, but `(1,1,0)` is excluded from the scored ball comparison | **ATTEMPTED** |
| Replace arrival by Hamming / support count | `(2,0,0)` has support-count `1` and taxicab arrival `2`; that is a different function | **ATTEMPTED** |
| Replace arrival by Euclidean `|v|_2` | That is not the displayed function being scored | **ATTEMPTED** |
| Adopt a Wick map or boost | Exits the claim; Minkowski is not written into Admissibility | **ATTEMPTED** |
| Re-run occupancy on a new patch | Exits the claim; the arrival function is scored as already displayed | **ATTEMPTED** |

### N2 — Wall independence

For a later Lorentzian reconstruction the open set is not collapsed by this
mismatch:

- `W1`: a physical clock / time-metric bridge;
- `W2`: an isotropic Euclidean spatial form at the comparison interface;
- `W3`: a boost or mixing law relating time and space.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---:|---:|---:|
| `W1/W2` | no | no | yes |
| `W1/W3` | no | no | yes |
| `W2/W3` | no | no | yes |

Scoring displayed `ℓ¹` against those objects does not attach any of them.

### N3 — Hidden-condition scan

| Phrase/object | Classification |
|---|---|
| displayed `t=ℓ¹` | explicit scored function; not attached |
| radius-4 integer ball | explicit finite domain |
| Euclidean-isotropic `c` | external comparison object |
| discrete `ℓ²` null | external comparison object |
| 24 proper cube rotations | Lattice axiom content |
| Lorentz boosts | external comparison identity; not adopted |
| occupancy / Hamming | unused, not hidden premises |

### N4 — Residual matching

| Witness | Witness residual | Current residual | Match? |
|---|---|---|---:|
| displayed taxicab arrival | `t(v)=|v|_1` from an origin seed | score that function, do not re-derive it | yes |
| observed Minkowski light | isotropic `c`, `ℓ²` null, boosts | report the mismatch on the radius-4 ball | yes |

This is not leftover character of a prior occupancy or first-arrival display.
Those displays supply the function being scored; they do not already compare
it to observed Minkowski light.

### N5 — Rhetoric audit

- per-element: every nonzero integer vector with `|v|_1 ≤ 4` is enumerated;
- per-site: only the origin-seed displayed arrival is used; no new site law;
- per-mode: no spectral decomposition is used or excluded;
- per-block: the radius-4 ball is the only comparison block;
- lattice-wide: no new lattice dynamics, occupancy growth, or adopted
  Minkowski law is claimed.

### N6 — Partial-closure path

A separately supplied or derived Lorentzian reconstruction, clock map, or
continuum comparison remains live. Closing any such bridge would be new
structure, not a match of the displayed `ℓ¹` arrival. The axioms need not be
edited to keep that route open.

### N7 — Hostile steelman

> Graph distance on `Z^3` is only a discrete stand-in. After a Wick rotation
> or a large-scale Euclidean-to-Lorentzian map, the same cubic symmetry could
> present as Minkowski light. The mismatch is an artifact of scoring the
> raw taxicab function.

**Answer.** The claim scores the displayed function, not a hypothetical later
map. Theorem 1 and Theorem 2 fail on that function with integer witnesses.
Theorem 3 records that the 24 cube rotations already present in the Lattice
axiom do not mix `t` with `x`. A Wick map or boost would be additional
adopted structure, which this note refuses to write into Admissibility.

### N8 — Cross-cycle echo

Kinetic-form isotropy, when approved, equalizes Euclidean temporal and
spatial quadratic coefficients. Linear temporal reparameterization of such a
form is a coordinate identity and does not select a physical clock. The
present note agrees with that boundary: displayed `ℓ¹` arrival is not itself
Minkowski light, and no clock or boost is adopted here.

**No-Go Discipline status: PASS** for the narrowed displayed-versus-observed
comparison.

## Primary Runner

The paired runner enumerates the radius-4 integer ball, computes the three
census integers, checks the two ratio witnesses, classifies the discrete
null set, generates the 24 proper cube rotations, compares them to a
rational boost identity, and pins the note/axiom contract. It writes no
cache and no governance surface.
