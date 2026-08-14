---
claim_id: two_cube_record_gauss_flux_step_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On two unit cubes that share a face, Record occupancy, the displayed cube 3-cochain ρ, and the displayed tree-gauge face flux φ are values of one function; one occupancy step from the corner seed sends φ(F*) from 1 to 4 as recoil through the shared face."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_record_gauss_flux_step_2026_08_14.py
---

# Two-Cube Record Gauss Flux Step

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** one source-complete update on two unit cubes that share a
face. Record occupancy, cube 3-cochain `ρ`, and tree-gauge face flux
`φ` are values of the same function. Shared-face flux is the recoil
into the adjacent cube. Displayed decoder and gauge. Not Newton. Not
a pairing. Not a three-site line. Not a TOE.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_record_gauss_flux_step_2026_08_14.py`](../scripts/two_cube_record_gauss_flux_step_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Cube `A = [0,1]^3` and cube `B = [1,2]×[0,1]×[0,1]` share the face
`F*` at `x=1`. Occupancy is a `{0,1}`-valued function on the twelve
vertices. The displayed source decoder is the cube 3-cochain
`ρ(C) = ∑_{v ∈ C} o(v)`. Shared vertices contribute to both cubes.
The displayed tree gauge sets `φ = 0` on every face except `F*` and
`B`'s outer face `F_B` at `x=2`, and solves `g = ρ` by
`φ(F*) = ρ(A)` and `φ(F_B) = ρ(A) + ρ(B)`.

One step is `step(o) = (o′, ρ, φ)`: `o′` is the occupancy step
reconstructed below; then `ρ` and `φ` are the decoder and gauge
solution on `o′`. Source and flux are not extra tables.

From the seed `o((0,0,0)) = 1` and `0` elsewhere, tick 0 has
`ρ(A)=1`, `ρ(B)=0`, `φ(F*)=1`, `φ(F_B)=1`. The occupancy step forms
exactly `(1,0,0)`, `(0,1,0)`, and `(0,0,1)`. Tick 1 has `ρ(A)=4`,
`ρ(B)=1`, `φ(F*)=4`, `φ(F_B)=5`. Shared-face flux changed. That is
recoil through `φ`.

This construction is displayed. It is not adopted as axiom text. Qubit
remains `M_2(C)`. This is still a comparator, not a TOE.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: two_cube_record_gauss_flux_step
target_blocker_text: "Gravity update has no equation; Record source is a counter that geometry does not read"
source_of_blocker_text: handoff
reachability_to_target: advances
next_trace_action: "independent audit; Pachner / perfect-action not in this note"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Support Boundary

- **Framework dependency:** the live axiom memo only. Record and
  Admissibility are quoted in Theorem 7. Those sentences do not name
  `ρ`, `φ`, the two-cube complex, or this gauge.
- **Displayed mathematical input:** the two-cube complex, the occupancy
  kernel reconstructed below, the cube-sum decoder `ρ`, and the tree
  gauge on `{F*, F_B}`. None of these is an approved primitive.
- **External physics inputs:** none.
- **Qubit:** quoted and not rewritten. The one-site algebra remains
  `M_2(C)`.

## Geometry

Twelve vertices:

```text
A-only:  (0,0,0) (0,0,1) (0,1,0) (0,1,1)
shared:  (1,0,0) (1,0,1) (1,1,0) (1,1,1)
B-only:  (2,0,0) (2,0,1) (2,1,0) (2,1,1)
```

Cube `A` uses the eight vertices with `x ∈ {0,1}`. Cube `B` uses the
eight vertices with `x ∈ {1,2}`. Shared vertices belong to both.

Eleven distinct faces. The six faces of `A` and the six faces of `B`
identify along `F*`, so that face is listed once:

```text
F*   = {x=1, y,z ∈ {0,1}}
F_B  = {x=2, y,z ∈ {0,1}}
A,x=0; A,y=0; A,y=1; A,z=0; A,z=1
B,y=0; B,y=1; B,z=0; B,z=1
```

Only `F*` and `F_B` carry flux in the displayed gauge. All other
faces exist in the listing and carry `φ = 0`.

## Occupancy Kernel (reconstructed, not cited)

`o : V → {0,1}`. Off-patch occupancy is `0`. Locked sites stay.
At an unread site

```text
n_μ = (o_{+μ} − o_{-μ}) / 3
```

with values in `Q`. An unread site forms if and only if `n ≠ 0`.
This is the displayed occupancy step, not a new kernel, and not a
uniqueness claim for the kernel.

## Displayed Source Decoder

```text
ρ(C) = ∑_{v ∈ C} o(v) ∈ {0,…,8}
```

`ρ(A)` counts the eight `A` vertices; `ρ(B)` counts the eight `B`
vertices. Shared vertices contribute to both. This is a 3-cochain on
the two cubes, not Record `I` at a single vertex.

## Displayed Tree Gauge

`φ = 0` on every face except `F*` and `F_B`. Incidence (displayed):

```text
g_A := φ(F*)
g_B := −φ(F*) + φ(F_B)
```

Source-complete solution of `g = ρ`:

```text
φ(F*)  = ρ(A)
φ(F_B) = ρ(A) + ρ(B)
```

Every pair `(ρ(A), ρ(B))` has exactly one flux in this gauge. That is
the executable update on this complex. Not Pachner. Not
perfect-action. Not a pairing.

## One Step

```text
step(o) = (o′, ρ, φ)
```

`o′` is the occupancy step. Then `ρ` and `φ` are the decoder and
gauge solution on `o′`.

Seed: `o((0,0,0)) = 1`, else `0`.

## Theorem 1 — two-cube listing

The complex has twelve vertices, two cubes, and eleven distinct
faces. `F*` is listed once.

## Theorem 2 — seed table

On the seed, before the occupancy step,

```text
ρ(A)=1  ρ(B)=0  φ(F*)=1  φ(F_B)=1
g_A=1   g_B=0
```

Gauss holds: `g = ρ`. In-patch neighbors of `(0,0,0)` are
`(1,0,0)`, `(0,1,0)`, `(0,0,1)`. Each has a single occupied opposite
neighbor, so `n ≠ 0`.

## Theorem 3 — occupancy step from the seed

The occupancy step from the seed forms exactly `(1,0,0)`, `(0,1,0)`,
and `(0,0,1)`, and no other of the twelve. Occupied set:

```text
{(0,0,0), (1,0,0), (0,1,0), (0,0,1)}
```

Locked sites stay occupied.

## Theorem 4 — tick-1 table and recoil

After the step:

```text
ρ(A)=4  ρ(B)=1  φ(F*)=4  φ(F_B)=5
g_A=4   g_B=1
```

Gauss holds. Shared-face flux changed `1 → 4` because three
`A`-incident sites formed, including the shared vertex `(1,0,0)`.
`ρ(B)` went `0 → 1` only because that shared vertex is in `B`.
`φ(F_B)` went `1 → 5`. Recoil is that change of `φ(F*)`.

## Theorem 5 — empty configuration

The empty seed is a fixed point of the occupancy step. It has zero
source and zero flux.

## Theorem 6 — `ρ` is not a single-vertex `I`

After the step, `ρ(A)=4`. Live Record gives at most one record per
site, so a site-local presence value `I` lies in `{0,1}`. Therefore
`ρ(A)=4` is not equal to Record `I` of any single vertex.

## Theorem 7 — live quotes; display, not adoption

Live Record (lock, permanence, and the one-record-per-site bound that
makes a site-local `I` take values in `{0,1}`):

```text
When present, a record locks exactly one admissible local possibility. A
site never carries more than one record; records are permanent.
```

Live Admissibility (nearest-neighbor-determined distribution):

```text
For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.
```

Live Qubit, quoted and not rewritten:

```text
The full one-site possibility domain has algebraic presentation `M_2(C)`.
```

Those Record and Admissibility sentences do not name `ρ`, `φ`, the
two-cube complex, or this gauge. Display. Do not adopt. Not a TOE.
Qubit remains `M_2(C)`.

## V1 — axiom quotes

V1 is Theorem 7. The quoted Record lock/permanence sentences and the
quoted Admissibility nearest-neighbor determination are the live memo
wording. They do not mention the displayed decoder or gauge.

## V2 — origin/main search

A search of `origin/main` for a two-cube Gauss flux step that uses
this occupancy kernel and this tree gauge on `{F*, F_B}` found no
landed source note or runner. Nearby two-cube language on
`origin/main` concerns Wilson plaquette supports, not Record occupancy
as a cube 3-cochain. Unmerged pull requests are not cited.

## V3 — textbook discrete Gauss

Textbook discrete Gauss on a cell says that the incidence of face
flux equals the enclosed source. That incidence is the displayed
`g = ρ`. Textbook discrete Gauss does not use this occupancy kernel
and does not select the tree gauge that sets `φ = 0` off `{F*, F_B}`
and solves `φ(F*) = ρ(A)`, `φ(F_B) = ρ(A)+ρ(B)`.

## V4 — exact `1 → 4` on `φ(F*)`

Exact integer arithmetic on the seed and its occupancy step gives
`φ(F*) = 1` before the step and `φ(F*) = 4` after the step. The
companion runner evaluates `rho`, `flux`, `gauss_holds`, `occ_step`,
and `seed` on those configurations.

## V5 — not a corollary of the axiom sentences alone

The quoted axiom sentences do not name `ρ`, `φ`, the two-cube
complex, or this gauge. The occupancy kernel, decoder, and tree gauge
are displayed mathematical input. The tick tables are not corollaries
of the axiom sentences alone.

## Mutations

The following predicates fail:

1. tick-1 `ρ(A)` equals a single-vertex `I`;
2. `φ(F*)` is unchanged by the occupancy step;
3. the empty seed forms a site or a nonzero flux;
4. this note adopts Newton or axiom text;
5. this note claims an axiom-named flux or a unique `L`.

## What This Does Not Claim

- Not Newton. No inverse-square coupling.
- Not a pairing.
- Not a three-site line recoil. The source is not a global counter.
- Not a leftover split of site occupancy versus cube source.
- Not uniqueness of the occupancy kernel.
- Not Aut-pick. Not color.
- Not Pachner. Not perfect-action.
- Not an axiom-named map. Not a unique `L`.
- Not a TOE. Qubit remains `M_2(C)`. QCD is unused.
- Displayed decoder and gauge. `ρ` and `φ` are functions of occupancy.
- Not adopted axiom text.

## Honest-auditor / Boundary

Twelve vertices, one gauge, exact `Z`. `ρ` and `φ` are functions of
occupancy. This note authors no audit verdict.

No N-gate no-go is authored. This is a construction.

## Runner Contract

The companion runner reconstructs the occupancy kernel, evaluates
`rho(o)`, `flux(o)`, `gauss_holds(o)`, `occ_step(o)`, and `seed()`,
checks Theorems 1–7, and rejects the five mutations. Declared audit
inputs are this note and the axiom memo. No cache is written.
Exact `Z` / `Q` arithmetic only.
