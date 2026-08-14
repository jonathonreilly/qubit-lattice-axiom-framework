---
claim_id: one_executable_axiom_class_member_displayed_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "A displayed attached law L0 is executed on a finite plus-shaped patch. Occupancy six-tuple c_d in {0,1} determines Bloch n_μ=(c_{+μ}-c_{-μ})/3 and state ρ=(I+n·σ)/2. Empty neighborhood yields I_2/2. Formation at the center is ready iff n≠0; when n is parallel to a coordinate axis the displayed menu is the two spectral projectors of ρ with exact Tr(ρ P) probabilities. Cube covariance of n is checked on the 24 proper cubic matrices. Clock table is the single displayed tick a=1. Pairing table is ordinary multiplication on Q. L0 is one member of the axiom class, not the unique member, not axiom text, not adopted, not Born, not QCD."
upstream_dependencies:
  - minimal_axioms
runner: scripts/one_executable_axiom_class_member_displayed_2026_08_14.py
---

# One Executable Member Of The Axiom Class (Displayed)

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact `Q` tables for one displayed attached law `L0` on a
finite plus-shaped patch. `L0` is **one member** of the axiom class,
**not the unique member**. No table is adopted as axiom text.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/one_executable_axiom_class_member_displayed_2026_08_14.py`](../scripts/one_executable_axiom_class_member_displayed_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The four axioms define a class of theories. A TOE is one member of
that class. Live Admissibility names existence, covariance, and
variation of a nearest-neighbor law; it does not name the law's
form or values. This note therefore does not derive a unique `L`.
It **displays** one executable member `L0` whose tables a runner
executes.

Work on the plus-shaped patch whose sites are the origin and its six
nearest neighbors, labeled

```text
(+x, −x, +y, −y, +z, −z).
```

A displayed occupancy six-tuple `c_d ∈ {0,1}` is the occupied/blank
retract of records on those neighbors. It is not adopted site-indexed
readout.

The displayed state-kernel is

```text
n_μ = (c_{+μ} − c_{−μ}) / 3
ρ(c) = (I_2 + n_x σ_x + n_y σ_y + n_z σ_z) / 2.
```

The empty neighborhood has `n = 0` and `ρ = I_2/2`. A single occupied
`+x` neighbor has `n = (1/3, 0, 0)`. An opposite pair `+x` and `−x`
cancels to `n = 0`. For every `c ∈ {0,1}^6` one has `|n|^2 ≤ 1/3 ≤ 1`,
so `ρ(c)` is a density matrix. The scale `1/3` is displayed member
data, not a uniqueness theorem.

The center is formation-ready iff `n ≠ 0`. When `n` is parallel to a
coordinate axis and nonzero, the displayed menu is the two spectral
projectors of `ρ`, with probabilities `Tr(ρ P)`. When `n` has two or
more nonzero components, `L0` still outputs `ρ` and does not select a
rank-1 menu.

Proper cubic rotation of the occupancy six-tuple rotates `n`. The
clock table is the single displayed value `a = 1`. The pairing table
is ordinary multiplication on `Q`. None of these tables is axiom
content. `L0` is not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Q/Fraction tables execute one displayed member L0 of the axiom class on a finite plus-shaped patch. The statement is that the tables run, not that the axioms select them."
trace_class: frontier_discovery
target_claim_id: one_executable_axiom_class_member_displayed
target_blocker_text: "a symbol L without equation, table, or runner is not adoptable"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed tables; owner may attach L0 or reject it; no axiom text is proposed"
conditional_surface_status: "exact executable tables for one displayed member; uniqueness of L0 is not claimed"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

From [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md),
Admissibility:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

From the same memo, Record:

> When present, a record locks exactly one admissible local possibility.

> Only records are readable.

From the same memo, Qubit:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone.

Those sentences name a covariant varying nearest-neighbor law, a lock,
and the one-site algebra. They do not name `n_μ = (c_{+μ}-c_{-μ})/3`,
the formation predicate `n ≠ 0`, the face menu, Wick `a = 1`, or the
product pairing. Qubit remains `M_2(C)`.

## Exact Objects

```text
σ_x = ((0, 1), (1, 0))
σ_y = ((0, −i), (i, 0))
σ_z = ((1, 0), (0, −1))
I_2 = ((1, 0), (0, 1))
```

Occupancy slots and direction vectors:

```text
+x ↔ (1, 0, 0),   −x ↔ (−1, 0, 0)
+y ↔ (0, 1, 0),   −y ↔ (0, −1, 0)
+z ↔ (0, 0, 1),   −z ↔ (0, 0, −1)
```

Proper cubic group `G`: the `3 × 3` signed-permutation matrices of
determinant `+1`. `|G| = 24`. A matrix `R ∈ G` acts on a six-tuple by
sending the occupant of direction `v` to direction `R v`.

## Theorem 1 — displayed states on listed configs

Write `c` as a six-tuple in slot order `(+x, −x, +y, −y, +z, −z)`.

| `c` | `n` | `ρ` |
|---|---|---|
| `(0,0,0,0,0,0)` | `(0,0,0)` | `I_2/2` |
| `(1,0,0,0,0,0)` | `(1/3,0,0)` | `(I_2 + σ_x/3)/2` |
| `(0,1,0,0,0,0)` | `(−1/3,0,0)` | `(I_2 − σ_x/3)/2` |
| `(0,0,1,0,0,0)` | `(0,1/3,0)` | `(I_2 + σ_y/3)/2` |
| `(1,1,0,0,0,0)` | `(0,0,0)` | `I_2/2` |
| `(1,0,1,0,0,0)` | `(1/3,1/3,0)` | `(I_2 + (σ_x+σ_y)/3)/2` |

Every `c ∈ {0,1}^6` obeys `|n|^2 ≤ 1/3`, so `ρ(c)` is a state.
`Tr ρ = 1` identically.

## Theorem 2 — the law varies with nearest neighbors

`ρ(0,0,0,0,0,0) = I_2/2` is not equal to `ρ(1,0,0,0,0,0)`. The
displayed law therefore varies with the nearest-neighbor occupancy.
This is a check that `L0` fits the Admissibility *shape*. It is not
a derivation of the values.

## Theorem 3 — cube covariance of the Bloch vector

For every `R ∈ G` and every `c ∈ {0,1}^6`,

```text
n(R · c) = R n(c).
```

In particular the right-handed `90°` turn

```text
R_z = ((0, −1, 0), (1, 0, 0), (0, 0, 1))
```

sends a lone `+x` occupant to a lone `+y` occupant and sends
`n = (1/3, 0, 0)` to `(0, 1/3, 0)`. The displayed Bloch action is
used only as this covariance check. It is not adopted, and it is
not written as a Lattice name.

## Theorem 4 — formation-ready iff `n ≠ 0`

The displayed instrument marks the center formation-ready exactly
when the directed kernel is nonzero. Empty occupancy is not ready.
An opposite pair is not ready. A lone `+x` occupant is ready. A
two-axis occupant is ready.

## Theorem 5 — axis-aligned lock table

When `n` is parallel to `ê_μ` and nonzero, the displayed menu is

```text
P_{μs} = (I_2 + s σ_μ) / 2,    s ∈ {+1, −1},
p(P_{μs}) = Tr(ρ P_{μs}) = (1 + s n_μ) / 2.
```

Lone `+x` gives `p(P_{x+}) = 2/3` and `p(P_{x−}) = 1/3`. Lone `−x`
swaps those two values. These are exact `Q` identities. They are
the instrument of `L0`, not a derivation of Born.

## Theorem 6 — two-axis `n` has no selected rank-1 menu

For `c = (1,0,1,0,0,0)` one has `n = (1/3, 1/3, 0)`. `L0` outputs
that state and does not select a rank-1 menu. Selecting one axis, or
one automorphism of a reconstruction, would privilege a possibility.
Qubit forbids writing that selector as axiom content. The leftover
inside `L0` on this cell is named, not filled.

## Theorem 7 — displayed clock table

One formation event on this patch is one tick. The displayed Wick
factor is `a = 1`. Live Admissibility and Record do not name a Wick
factor. The approved kinetic-isotropy primitive names `c_t = c_s`
and does not name `a`. The value `1` is member data.

## Theorem 8 — displayed pairing table

On `Q`, the displayed pairing is ordinary multiplication
`B(x, y) = x y`. In particular

```text
B(0, 0) = 0,    B(1, 1) = 1,    B(2, 3) = 6,    B(−1, 4) = −4.
```

This is not a source law, not a Newton force, and not a pairing on
a site-indexed readout.

## Theorem 9 — the axioms do not name these tables

Quoted Admissibility says the distribution is determined by, and
varies with, nearest-neighbor conditions. Quoted Record says a
record locks one admissible possibility. Neither sentence names the
tables of Theorems 1–8. `L0` is one member. It is not the unique
member. It is not adopted.

## Mutations

1. Predicate “`ρ(empty) == ρ(+x)`” must fail.
2. Predicate “opposite pair is formation-ready” must fail.
3. Predicate “two-axis `n` selects a rank-1 menu” must fail.
4. Predicate “live memo names `L0`, Born, or Wick `a = 1` as axiom content” must fail.
5. Predicate “note adopts `L0` as axiom text” must fail.
6. Predicate “note claims a Lattice name for the kernel” must fail.

Identity gates call `bloch_of(c)`, `formation_ready(c)`,
`axis_menu(c)`, `pairing(x, y)`, and `wick_a()`.

## Honest-auditor / Boundary

The algebra is finite: `64` occupancy tuples, `24` integer matrices,
and `2 × 2` Pauli arithmetic over `Q`. The runner reconstructs `G`,
evaluates `n` and `ρ` exactly, checks covariance on every pair
`(R, c)`, and checks the mutation predicates against the live axiom
memo rather than a working-tree paraphrase.

Boundary, stated positively. The theorem executes one displayed
member. It does not classify all cube-covariant laws. It does not
select a physical algebra action. It does not rewrite Qubit. It does
not introduce a pairing table of lattice rotations with Pauli axes.
It does not pick an automorphism of a two-site corner. QCD is unused.

The independent audit lane sets status. This note records
`actual_current_surface_status: bounded-support` as the machine surface of
the present packet and authors no audit verdict.

## What This Does Not Claim

- `L0` is not adopted as axiom content and is not the unique member.
- Qubit remains `M_2(C)`. It is not flipped to `M_3`.
- The displayed kernel is not a Lattice name.
- No Born rule is derived. `Tr(ρ P)` is the instrument of this member.
- No SWAP-corner Aut element is selected.
- No color or QCD identification is supplied.
- No Newton force, `G_N`, or `1/r^2` law is supplied.
- Whether some other member is the physical one remains open.

## Runner Contract

The companion runner evaluates `n` and `ρ` on the listed configs,
checks variation, checks cube covariance of `n` on all of `G` and
all occupancy tuples, checks the formation predicate, checks the
axis-aligned lock table, checks that a two-axis `n` selects no
rank-1 menu, checks the clock and pairing tables, rejects the
mutation predicates, and verifies the live axiom quotes used above
are present while a Lattice name for the kernel is absent from that
memo. Declared audit inputs are this note and the axiom memo.
