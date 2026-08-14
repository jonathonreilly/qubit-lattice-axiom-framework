---
claim_id: one_executable_axiom_class_member_displayed_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "A displayed local-law comparator L0 is executed on a finite plus-shaped patch. Occupancy six-tuple c_d in {0,1} determines Bloch n_μ=(c_{+μ}-c_{-μ})/3. For every n≠0 the law is the unique covariant spectral measure of ρ=(I+n·σ)/2 on its two rank-1 eigenprojectors, with formation probability 1. For n=0 the formation probability is 0 and there is no rank-1 menu. A realized draw plus permanence gives the Record update. Clock a=1 and pairing B=xy are disconnected extra tables, not this local law. L0 is an unselected comparator, not the unique member, not axiom text, not adopted, not Born, not QCD."
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

The center has formation probability `f = 1` iff `n ≠ 0`, else
`f = 0`. For every nonzero `n` the outcome measure is the unique
spectral PVM of `ρ`: two rank-1 eigenprojectors with probabilities
`(1 ± |n|)/2`. That includes the 32 two- and three-axis cells that
previously had no menu. For `n = 0` there is no rank-1 menu. A
realized draw together with permanence is the Record update.

Proper cubic rotation of the occupancy six-tuple rotates `n` and
the spectral measure. The clock table `a = 1` and the pairing
`B(x,y)=xy` are disconnected extra tables. They are not this local
law. `L0` is an unselected comparator, not a TOE, and is not adopted.

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

## Theorem 6 — total spectral measure on every nonzero `n`

Of the `64` occupancy six-tuples, eight have `n = 0` and fifty-six
are formation-ready. Each of those fifty-six, including the
thirty-two with two or three nonzero Bloch components, carries the
unique spectral measure of `ρ`. For `n` with integer direction
`(a,b,c)` and `k = a^2+b^2+c^2 ∈ {1,2,3}`,

```text
p_± = (3 ± √k) / 6.
```

Then `p_+ + p_- = 1` and both are positive. This is a probability
measure on the two rank-1 eigenprojectors, not merely a density
matrix. It does not pick a coordinate axis and does not pick an
Aut of a reconstruction. For `n = 0` the measure is absent.

## Theorem 6b — formation probability, draw, Record update

Formation probability is `f(c) = 1` if `n ≠ 0` and `f(c) = 0`
otherwise. The realized draw is a pick from `{+,−}` with law
`(p_+, p_-)` when `f = 1`. The Record update on the center is:

- if a record is already present, keep it (permanence);
- if `f = 0`, the site stays unread;
- if `f = 1` and the draw is `s`, lock the corresponding spectral
  projector.

A second update after a lock is the identity. That is the
composition check for this comparator.

## Theorem 7 — clock and pairing are disconnected extras

The tables `a = 1` and `B(x,y)=xy` still execute, but they are
not coupled to the local NN law of Theorems 1–6b. They are not
an autonomous clock or gravity law. Live Admissibility and Record
do not name them.

## Theorem 9 — the axioms do not name these tables

Quoted Admissibility says the distribution is determined by, and
varies with, nearest-neighbor conditions. Quoted Record says a
record locks one admissible possibility. Neither sentence names the
tables of Theorems 1–7. `L0` is one member. It is not the unique
member. It is not adopted. It is an unselected comparator, not a TOE.

## Mutations

1. Predicate “`ρ(empty) == ρ(+x)`” must fail.
2. Predicate “opposite pair is formation-ready” must fail.
3. Predicate “two-axis `n` has no spectral measure” must fail.
4. Predicate “live memo names `L0`, Born, or Wick `a = 1` as axiom content” must fail.
5. Predicate “note adopts `L0` as axiom text” must fail.
6. Predicate “note claims a Lattice name for the kernel” must fail.

Identity gates call `bloch_of(c)`, `formation_ready(c)`,
`spectral_measure(c)`, `formation_prob(c)`, `record_update(...)`,
`pairing(x, y)`, and `wick_a()`.

## Honest-auditor / Boundary

The algebra is finite: `64` occupancy tuples, `24` integer matrices,
and `2 × 2` Pauli arithmetic over `Q`. The runner reconstructs `G`,
evaluates `n` exactly, checks the spectral measure on all 56
nonzero cells, checks Record update permanence, and checks the
mutation predicates against the live axiom memo rather than a
working-tree paraphrase.

Boundary, stated positively. The theorem executes one displayed
local-law comparator. Clock and pairing stay disconnected extras. It does not classify all cube-covariant laws. It does not
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
- No Born rule is derived. The spectral measure is the instrument of this comparator.
- No SWAP-corner Aut element is selected.
- No color or QCD identification is supplied.
- No Newton force, `G_N`, or `1/r^2` law is supplied.
- Whether some other member is the physical one remains open.

## Runner Contract

The companion runner evaluates `n` and `ρ` on the listed configs,
checks variation, checks cube covariance of `n` on all of `G` and
all occupancy tuples, checks that all 56 nonzero cells have a spectral measure,
checks formation probability and Record-update permanence, checks
that clock and pairing are marked disconnected, rejects the
mutation predicates, and verifies the live axiom quotes used above
are present while a Lattice name for the kernel is absent from that
memo. Declared audit inputs are this note and the axiom memo.
