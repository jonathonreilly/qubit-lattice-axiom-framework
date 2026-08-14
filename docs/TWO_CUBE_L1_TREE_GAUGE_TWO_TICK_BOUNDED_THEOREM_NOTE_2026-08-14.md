---
claim_id: two_cube_l1_tree_gauge_two_tick_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "Conditional on the displayed two-site two-face incidence and the displayed L1 source ticks, the tree-gauge assignment φ(F*)=ρ(A), φ(F_B)=ρ(A)+ρ(B) solves g=ρ after tick 1 with integers (4,1) and after tick 2 with integers (7,4). The 2×2 incidence is invertible, so that assignment is the unique integer solution at each tick. No third face and no −x ray are introduced. The four axioms supply none of the incidence, the decoder, or the tick values."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_tree_gauge_two_tick_2026_08_14.py
---

# Two-Site Tree Gauge Stays Source-Complete After Two L1 Ticks

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact integer incidence algebra on one displayed two-site tree
with two faces. The L1 ticks are displayed source values, not an axiom
consequence.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_tree_gauge_two_tick_2026_08_14.py`](../scripts/two_cube_l1_tree_gauge_two_tick_2026_08_14.py)

Framework context on `origin/main`: the axiom memo
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
Lattice names sites of `Z^3`; it does not name this two-face incidence, the
Gauss decoder, or an L1 source tick. This cycle writes no runner cache and no
citation manifest.

## Result Up Front

Investment: composition of the Gauss decoder. Gauge-fix uniqueness for a
fixed source `ρ` is a static linear-algebra fact on this tree. This note
checks the update: after each displayed L1 tick the same assignment

```text
φ(F*) = ρ(A)
φ(F_B) = ρ(A) + ρ(B)
```

still solves `g = ρ`.

The displayed incidence, the same two-site tree used by the recurrent
gravity decoder, is

```text
g_A := φ(F*)
g_B := −φ(F*) + φ(F_B)
```

Substituting the tree gauge gives `g_A = ρ(A)` and `g_B = ρ(B)` for every
integer pair `(ρ(A), ρ(B))`. After tick 1 the displayed source is `(4, 1)`.
After tick 2 it is `(7, 4)`. In both cases `g = ρ` holds with those integers.

This is not a two-cube-gauge clone: the tested object has two faces only.
There is no third face and no `−x` ray.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer identities show the displayed tree gauge solves g=ρ after each of two displayed L1 source ticks, and the 2×2 incidence is invertible. No physical gravity identification is supplied."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "after each L1 tick, does the same tree-gauge assignment still solve g=ρ on the two-site two-face incidence?"
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "test whether a separately supplied longer tick sequence or a larger tree still has a unique source-complete decoder; no physical consumer is claimed here"
conditional_surface_status: "exact for the displayed two-site incidence and the two displayed integer ticks; other complexes, gauges, and physical identifications remain separate"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Support Boundary

- **Framework context:** Lattice names the cubic site set. Qubit names
  one-site `M_2(C)`. Admissibility names one nearest-neighbor rule. Record
  names content-only readout. None of these supplies a face incidence, a
  flux `φ`, a source `ρ`, a Gauss decoder, or an L1 tick.
- **Explicit bounded mathematical input:** two sites `{A, B}`, two faces
  `{F*, F_B}`, the displayed incidence, the tree-gauge decoder, and the two
  integer source ticks `(4, 1)` then `(7, 4)`.
- **External physics inputs:** none. There is no measured, fitted,
  literature, normalization, scale, or observational constant.
- **Physical-identification boundary:** no map from this decoder to a
  physical gravitational constraint, Newtonian kernel, or continuum Gauss
  law is supplied.

## Exact Objects

Write integer sources `ρ(A), ρ(B) ∈ Z` and integer face fluxes
`φ(F*), φ(F_B) ∈ Z`. The Gauss readout is the displayed incidence

```text
g_A := φ(F*)
g_B := −φ(F*) + φ(F_B)
```

In matrix form, with column order `(φ(F*), φ(F_B))` and row order
`(g_A, g_B)`,

```text
M = [[ 1, 0],
     [-1, 1]]
```

so `(g_A, g_B)^T = M (φ(F*), φ(F_B))^T`. The determinant is `1`, and the
unique inverse is

```text
M^{-1} = [[1, 0],
          [1, 1]]
```

The tree-gauge decoder is exactly that inverse applied to `ρ`:

```text
φ(F*) = ρ(A)
φ(F_B) = ρ(A) + ρ(B)
```

An L1 tick is a separately supplied update of the integer pair `ρ`. This
note displays two ticks and does not derive a tick law:

| tick | `ρ(A)` | `ρ(B)` |
|---|---:|---:|
| 1 | 4 | 1 |
| 2 | 7 | 4 |

The face set is `{F*, F_B}`. No third face is named. No `−x` ray is named.

No axiom is edited. The incidence, decoder, and ticks are displayed
mathematical inputs, not a proposed Lattice rewrite and not a registered
primitive.

## Exact Target And Obligation Graph

**Exact target.** After each displayed L1 tick, decide whether the tree
gauge still solves `g = ρ`, and whether that solution is unique on this
incidence.

| Obligation | Role | Disposition |
|---|---|---|
| displayed incidence `g_A = φ(F*)`, `g_B = −φ(F*) + φ(F_B)` | definition | used as written |
| tree gauge `φ(F*)=ρ(A)`, `φ(F_B)=ρ(A)+ρ(B)` | decoder | used as written |
| `g = ρ` for every integer `ρ` | Theorem 1 | proved; runner checks a finite integer sample including both ticks |
| after tick 1, `g = ρ = (4, 1)` | Theorem 2 | proved |
| after tick 2, `g = ρ = (7, 4)` | Theorem 2 | proved |
| uniqueness of `φ` given `g` | Theorem 3 | `det M = 1` |
| third face or `−x` ray | out of scope | not introduced |
| physical gravity identification | out of scope | no such map is supplied |

## Theorem 1 — Tree gauge solves the incidence identically

For every integer pair `(ρ(A), ρ(B))`, the tree-gauge assignment satisfies
`g = ρ`.

Proof. Substitute `φ(F*) = ρ(A)` and `φ(F_B) = ρ(A) + ρ(B)` into the
displayed incidence:

```text
g_A = φ(F*) = ρ(A)
g_B = −φ(F*) + φ(F_B) = −ρ(A) + (ρ(A) + ρ(B)) = ρ(B)
```

The identity is algebraic and does not use the numerical values of a tick.

## Theorem 2 — Source-completeness after two L1 ticks

After tick 1 and after tick 2, `g = ρ` holds with the displayed integers
`(4, 1)` then `(7, 4)`.

Proof. Theorem 1 applies to every integer pair, so it applies to both
displayed ticks. Explicitly:

Tick 1. `ρ = (4, 1)`, so `φ(F*) = 4` and `φ(F_B) = 5`. Then
`g_A = 4` and `g_B = −4 + 5 = 1`.

Tick 2. `ρ = (7, 4)`, so `φ(F*) = 7` and `φ(F_B) = 11`. Then
`g_A = 7` and `g_B = −7 + 11 = 4`.

The decoder is therefore source-complete after each of the two updates. The
same assignment rule is reused; only the source values change.

## Theorem 3 — Uniqueness survives the update

Given any integer pair `g`, there is exactly one integer pair `φ` on
`{F*, F_B}` with that Gauss readout. In particular the tree gauge is the
unique solution of `g = ρ` after each displayed tick.

Proof. `det M = 1 · 1 − 0 · (−1) = 1`, so `M` is invertible over `Z`. The
unique solution is `φ = M^{-1} g`, which is the tree gauge when `g = ρ`.
Invertibility does not depend on the value of `ρ`, so uniqueness is
preserved by any source update, including the two displayed L1 ticks.

Static uniqueness given one `ρ` is this invertibility. Composition with the
update is Theorem 2 plus the same invertibility at the new `ρ`.

## Not A Two-Cube-Gauge Clone

A two-cube gauge problem would introduce at least one further face and a
`−x` ray. The object tested here has exactly the two faces `F*` and `F_B`
and the two sites `A` and `B`. The runner checks that the note and the
decoder domain name no third face and no `−x` ray.

## Physical-Identification Boundary

The four axioms do not name a Gauss decoder or an L1 tick. Hosting a unique
source-complete tree gauge on this two-face incidence is a type fact about a
displayed integer map. No claim about continuum gravity, a Newtonian
kernel, or a physical constraint algebra is made.

## Falsifiers And Mutation Targets

The predicate `g == ρ` after tick 1 must hold for `(4, 1)`.
The predicate `g == ρ` after tick 2 must hold for `(7, 4)`.
The predicate `det M == 1` must hold.
The predicates “a third face is used” and “a `−x` ray is used” must fail.

All five are runner-checked by constructing `M` and the two decoded ticks.

## No-Go Discipline Gate

There is no universal negative claim. The only local negative boundary is
that a third-face or `−x`-ray reading is outside the tested object. Routes
below try to defeat `g = ρ` after the two ticks or to smuggle a two-cube
clone.

### N1 — materially distinct routes

| Route family | Exact attack | Exact outcome | Marker |
|---|---|---|---|
| Drop the minus on `F*` | use `g_B := φ(F*) + φ(F_B)` | tick 1 would give `g_B = 9 ≠ 1` | **ATTEMPTED** |
| Swap the tree assignment | set `φ(F*)=ρ(B)`, `φ(F_B)=ρ(A)` | tick 1 would give `g = (1, 3) ≠ (4, 1)` | **ATTEMPTED** |
| Freeze the tick-1 flux | reuse `φ = (4, 5)` at tick 2 | `g` would stay `(4, 1) ≠ (7, 4)` | **ATTEMPTED** |
| Attribute uniqueness to one `ρ` only | recompute `det M` after both ticks | `det M = 1` at both sources | **ATTEMPTED** |
| Import a third face | search the decoder domain for a third face name | domain is `{F*, F_B}` | **ATTEMPTED** |
| Import a `−x` ray | search the tested object for a `−x` ray | none is named | **ATTEMPTED** |

These are routes against one local identity. They do not enumerate routes to
a physical gravitational theory, because no such negative claim is made.

### N2 — wall independence and collapse

There is no multi-wall claim. Incidence, decoder substitution, and
invertibility are independent checks of the same source-completeness fact,
not three walls.

| Raw pair | First closes second? | Second closes first? | Collapse |
|---|---:|---:|---|
| Theorem 1 identity / tick-1 numbers | yes | no | the tick is a specialization |
| Theorem 1 identity / tick-2 numbers | yes | no | the tick is a specialization |
| `det M = 1` / unique tree gauge | yes | yes | invertibility definition |

Collapsed obstruction set: `{g = ρ after each displayed tick}`. No physical
identification is counted as a wall.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| two sites `{A, B}` and two faces `{F*, F_B}` | explicit bounded mathematical input |
| displayed incidence `M` | explicit test matrix, not attributed to the axioms |
| tree-gauge decoder | explicit inverse of `M` |
| L1 ticks `(4, 1)` and `(7, 4)` | explicit displayed integers, not a derived tick law |
| integer coefficient ring `Z` | explicit; runner uses exact integers |
| third face, `−x` ray, two-cube gauge | scope non-claims; not part of the object |
| observations or fitted constants | none |

The scan found no hidden condition beyond the now-explicit incidence,
decoder, and ticks. No continuum limit, Newtonian kernel, or empirical mass
is used.

### N4 — source residual matching

| Source and locator | Residual addressed there | Residual here | Match and limit |
|---|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), Lattice and Record clauses | cubic sites and content-only readout | displayed two-face incidence | no residual match; used only for framework context |
| this note, Theorems 1–3 and paired runner | displayed `M`, decoder, and two ticks | `g = ρ` after each tick | exact match; self-contained current-cycle calculation |

No prior no-go is used as authority. The incidence identities, the two
ticks, and invertibility are proved here.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | entries of `M`, `M^{-1}`, and the two decoded flux pairs | no classification of every integer matrix |
| per site | the two displayed sites `A` and `B` only | no lattice-wide source law |
| per mode | the two faces `F*` and `F_B` | no third-face or ray mode |
| per block | one two-site tree after two ticks | no physical constraint identification |
| lattice-wide | checked and not executed: the theorem supplies no lattice-wide decoder | no lattice-wide existence or no-go |

The wording is therefore restricted to the displayed tree. The paired
runner prints the five canonical resolution-certificate lines with the same
boundary. This cycle writes no cache file.

### N6 — live partial-closure paths

1. A longer tick sequence with a separately supplied update rule is a
   separate question and remains open here.
2. A larger tree, a loop, or a two-cube complex would change `M`; this note
   tests only the displayed two-face tree.
3. A different gauge slice could solve `g = ρ` on a larger complex with a
   kernel; this incidence has trivial kernel.
4. A separate retained derivation or explicitly approved primitive could
   supply a physical Gauss-law identification; this theorem neither assumes
   nor forecloses such work.
5. Merely naming the decoder “gravity” would be a labeling convention, not
   a derivation, so this note does not use that retirement path.

Scale reference, kinetic isotropy, and realized state were checked in the
premise registry. None is load-bearing here, and none is counted as a wall.
No new axiom is claimed to be necessary.

### N7 — concrete-mechanism steelman

The strongest objection says that static uniqueness already gives `g = ρ`
at every `ρ`, so a two-tick check is empty. The objection correctly
identifies that Theorem 1 is `ρ`-independent, but it does not defeat the
scoped claim. The investment is composition of the decoder with an update:
the same assignment must be re-evaluated on the new integers, and a frozen
tick-1 flux fails at tick 2. The terminal obligation is exactly that
re-evaluation, which the N1 routes close. Steelman disposition: **CLOSED**.

### N8 — cross-cycle echo

| Echo | Status/mechanism checked | Could it retire this identity? |
|---|---|---|
| [`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md) | endpoint dressing of link operators against model Gauss generators | no; that surface is an operator commutant profile, not this integer tree decoder |
| two-cube gauge with a third face and a `−x` ray | a larger complex, not the tested object | no; cloning that complex would change `M` |

The search found no convention that makes `g ≠ ρ` on this incidence after
the displayed ticks. It did find live alternative complexes, so no broader
no-go is asserted.

N1–N8 disposition: **PASS** for the exact source-completeness of the
displayed tree gauge after the two L1 ticks. The packet grants no standing
to any broader negative claim.

## Excluded Broader Claims

This note makes none of the following claims:

- “the axioms derive a physical Gauss law”
- “this is a two-cube gauge theorem”
- “a third face or `−x` ray is required”
- “an L1 tick law is derived from Admissibility or Record”
- “an axiom update is necessary”
- “this constructs continuum gravity”

The shipped claim is only: conditional on the displayed two-site two-face
incidence, the tree-gauge decoder solves `g = ρ` after tick 1 with integers
`(4, 1)` and after tick 2 with integers `(7, 4)`, and that solution is
unique.

## Provenance

Framework context on `origin/main`: the axiom memo only. The runner binds

`AUDIT_INPUT_PATHS = (this note, docs/MINIMAL_AXIOMS_2026-06-29.md)`

as a string-literal tuple. This cycle writes no citation manifest and no
runner cache. Neither omitted artifact is a scientific premise.
