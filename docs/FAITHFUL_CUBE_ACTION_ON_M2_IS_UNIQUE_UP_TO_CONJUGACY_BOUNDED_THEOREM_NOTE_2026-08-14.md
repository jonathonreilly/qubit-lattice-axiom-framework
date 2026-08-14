---
claim_id: faithful_cube_action_on_m2_is_unique_up_to_conjugacy_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "Conditional on requiring a faithful unital *-action of the concrete proper cubic group G (|G|=24) on one-site M_2(C), those actions form one conjugacy class. G is isomorphic to S_4 via its action on the four space diagonals. A faithful image is therefore S_4, not C_24 or D_12 (G has eight order-3 elements). The only 3-dimensional real irrep of S_4 that lands in Aut(M_2)≅SO(3) is the standard 3, not 3⊗sgn. The runner conjugates α by every element of G. Live Lattice and Qubit do not require a faithful action and do not privilege a frame. α is displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/faithful_cube_action_on_m2_is_unique_up_to_conjugacy_2026_08_14.py
---

# Faithful Cube Actions On `M_2` Form One Conjugacy Class

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact integer/`Q(i)` identities for the concrete proper cubic
group `G` and two displayed unital `*`-actions on one-site `M_2(C)`.
Uniqueness is **conditional on requiring a faithful** action. No pairing
table, no 3-menu, no unital `M_3`, no SWAP-corner Aut-selection, no Qubit
rewrite, and no adopted intertwiner.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/faithful_cube_action_on_m2_is_unique_up_to_conjugacy_2026_08_14.py`](../scripts/faithful_cube_action_on_m2_is_unique_up_to_conjugacy_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write `G` for the concrete proper cubic rotation group: the `3 × 3`
signed-permutation matrices of determinant `+1`. Then `|G| = 24`. The
standard generators used below are the right-handed `90°` turns

```text
Rx = ((1,0,0),(0,0,-1),(0,1,0))
Ry = ((0,0,1),(0,1,0),(-1,0,0))
Rz = ((0,-1,0),(1,0,0),(0,0,1))
```

so `Rx` sends `y → z` and `z → −y`. Live Lattice names those site
rotations. Live Qubit names one-site `M_2(C)`. Neither sentence requires
an action of `G` on the algebra.

Two displayed actions and one excluded action:

- Trivial `φ0`: every `R ∈ G` acts as `id` on `M_2`. Not faithful.
- Standard Bloch action `α`: the unique unital `*`-linear family with
  `α_R(σ_j) = Σ_i R_{ij} σ_i`. Faithful. Explicitly
  `α_Rx(σx)=σx`, `α_Rx(σy)=σz`, `α_Rx(σz)=−σy`.
- Conjugate `β_R = α_{Sω} ∘ α_R ∘ α_{Sω}^{-1}` for the displayed
  `120°` cycle `Sω = ((0,0,1),(1,0,0),(0,1,0)) ∈ G`. Faithful, conjugate
  to `α`, and `β_{Rx} ≠ α_{Rx}`.

`G` is isomorphic to `S_4` by permuting the four space diagonals.
A faithful unital `*`-action is an injective hom `G → Aut(M_2) ≅ SO(3)`,
so its image is isomorphic to `S_4`. Cyclic `C_{24}` and dihedral
`D_{12}` are order-`24` subgroups of `SO(3)` and are **not** isomorphic
to `S_4` (`G` has eight order-3 elements; those groups have two).
The only 3-dimensional real irrep of `S_4` that lands in `SO(3)` is
the standard `3`; `3 ⊗ sgn` sends some cube rotations to determinant
`-1`. Therefore every faithful action is equivalent to the standard
inclusion `α`, and the leftover inside the class is a Bloch frame.
This note does not pick a representative and does not adopt `α`.
The runner conjugates `α` by every element of `G`, not by one
displayed `Sω`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact count |G|=24, exact Q(i) Pauli identities, and an explicit conjugator show faithful cube actions on M_2 form one conjugacy class conditional on requiring a faithful action. No action is adopted."
trace_class: frontier_discovery
target_claim_id: faithful_cube_action_on_m2_is_unique_up_to_conjugacy
target_blocker_text: "whether a faithful cube action on M_2 is unique up to conjugacy"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded algebra; no action is adopted"
conditional_surface_status: "exact for the concrete G and the displayed actions on one-site M_2(C); whether any action is required remains extra"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

From [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), Lattice:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

From the same memo, Qubit:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and
> adds no further primitive structure.

> No possibility is privileged. Possibilities are distinguished by the supplied
> algebraic structure alone.

The Qualification sentence of the same memo is quoted only as a parent
boundary, not as a derived lemma:

> These axioms state only their named primitive content. Further physical
> structure requires a retained derivation or bridge, or explicit approved-
> primitive registration, before use as a premise.

## Exact Objects

Entries live in the Gaussian field `Q(i)` with `i^2 = -1`. The companion
runner implements this as pairs `(a, b)` meaning `a + b i` with
`a, b ∈ Q`.

```text
σx = ((0, 1), (1, 0))
σy = ((0, -i), (i, 0))
σz = ((1, 0), (0, -1))
I  = ((1, 0), (0, 1))
```

The set `{I, σx, σy, σz}` is a `Q(i)`-basis of `M_2`. A unital linear map
on `M_2` is uniquely determined by the images of `σx`, `σy`, and `σz`.

A proper cubic matrix is a `3 × 3` monomial signed-permutation matrix
with exactly one nonzero `±1` in each row and column and determinant
`+1`. There are `3! × 2^3 = 48` signed permutation matrices and exactly
half have determinant `+1`, so `|G| = 24`. The three generators `Rx`,
`Ry`, `Rz` displayed above lie in `G`.

The standard action is

```text
α_R(σ_j) = Σ_i R_{ij} σ_i
```

extended unital-linearly. Equivalently, the Bloch vector transforms as
`n ↦ R n`. This is a group homomorphism because matrix multiplication
matches composition of the induced maps.

The displayed conjugator is

```text
Sω = ((0, 0, 1), (1, 0, 0), (0, 1, 0))
```

which cycles `x → y → z → x` and has determinant `+1`, hence lies in `G`.

## Theorem 1 — `|G| = 24` and the generators lie in `G`

Enumerate the `48` signed permutation matrices and keep determinant `+1`.
The count is `24`. Each of `Rx`, `Ry`, `Rz`, `Sω` is a signed permutation
of determinant `+1`.

## Theorem 2 — `φ0` is not faithful; `α` is faithful

`φ0` sends every element of `G` to `id`, so `ker(φ0) = G` and `φ0` is
not injective.

`Rx ≠ I_3`. The standard action satisfies `α_Rx(σy) = σz ≠ σy`, so
`α_Rx ≠ id`. Therefore `α` is not the trivial hom. Because `α_R` is the
Bloch action of the concrete matrix `R`, `α_R = id` if and only if
`R = I_3`. Hence `α` is injective: `is_faithful(α)` holds.

## Theorem 3 — `G ≅ S_4`; faithful images cannot be cyclic or dihedral

The four space diagonals of the unit cube are the lines through

```text
(1,1,1),   (1,1,−1),   (1,−1,1),   (1,−1,−1).
```

Each `R ∈ G` permutes these four lines (a vertex and its opposite
label the same line). The resulting map `G → S_4` is a group
isomorphism: the runner lists 24 distinct permutations.

Consequently a faithful hom `G → Aut(M_2)` has image isomorphic to
`S_4`. That already excludes the order-`24` subgroups `C_{24}` and
`D_{12}` of `SO(3)`. Independently, `G` has exactly eight elements
of order 3 (the 3-cycles of `S_4`). Cyclic and dihedral groups of
order 24 have two. A census that treats octahedral groups as the
sole order-24 finite subgroups of `SO(3)` is false, and is not used.

## Theorem 3b — only the standard `3` lands in `SO(3)`

`S_4` has two 3-dimensional real irreps, `3` and `3 ⊗ sgn`. Inner
automorphisms of `M_2` act as orientation-preserving Bloch rotations,
so `Aut(M_2) ≅ SO(3)` and every image matrix has determinant `+1`.

The standard inclusion `α` is the irrep `3`. For `3 ⊗ sgn`, an odd
permutation of the diagonals would flip the determinant. The runner
checks that `R_z` induces a 4-cycle on the diagonals (odd), while
`det(R_z) = +1`. Therefore `3 ⊗ sgn` does not land in `SO(3)`.
The only remaining 3-dimensional irrep is `3`, which is `α`.

Constructively, the same uniqueness is the right-handed frame of
`90°` axes: `ρ(R_x)`, `ρ(R_y)`, `ρ(R_z)` determine a unique
`S ∈ SO(3)` with `ρ = Ad_S ∘ α ∘ Ad_S^{-1}`.

Qubit says no possibility is privileged and the `Cl(3,0)` parenthetical
adds no further primitive structure. Those sentences forbid reading the
standard frame as axiom content. They do not create a second conjugacy
class.

## Theorem 3c — every `G`-conjugate of `α` is faithful and conjugate

For every `S ∈ G` the conjugate action

```text
β^S_R = α_S ∘ α_R ∘ α_S^{-1} = α_{S R S^{-1}}
```

is faithful, and the conjugator is `α_S`. That is the full discrete
orbit of frames named by `G` itself. Combined with Theorem 3b, every
faithful unital `*`-action lies in this one conjugacy class.

## Theorem 4 — a displayed distinct conjugate

Let `β_R = α_{Sω} ∘ α_R ∘ α_{Sω}^{-1}`. Because `α` is a hom this is
`α_{Sω R Sω^{-1}}`. In particular `β` is faithful and
`conjugator_exhibits_beta` holds by construction.

The axis of `α_{Rx}` is `ê_x`. The axis of `β_{Rx}` is `Sω ê_x = ê_y`.
Explicitly `α_{Rx}(σy) = σz` while `β_{Rx}(σy) ≠ σz`. So `β_{Rx} ≠ α_{Rx}`.
The two faithful actions are distinct representatives of the same class.

## Theorem 5 — live Lattice and Qubit do not require the action

The Lattice sentence names proper cubic rotations of the sites of `Z^3`.
The Qubit sentence names the one-site algebra `M_2(C)`. The `Cl(3,0)`
sentence says that presentation adds no further primitive structure.
“No possibility is privileged” forbids selecting a Bloch frame from the
algebra alone.

Those sentences do not require a faithful action of `G` on `M_2`. The
uniqueness in Theorems 3–4 is **conditional on requiring a faithful**
unital `*`-action. This note displays the class. It does not adopt `α`.
It does not call `α` a Lattice name.

## Theorem 6 — this is not an Aut of a SWAP corner

The theorem lives on one-site `M_2`. It does not name `p = (I+F)/2`,
does not name `Aut(p M_4 p)`, and does not select a color rotation.
Qubit remains `M_2(C)`.

## Mutations

1. Predicate “`φ0` is injective” must fail.
2. Predicate “`α_Rx == id`” must fail.
3. Predicate “`β_Rx == α_Rx`” must fail.
4. Predicate “no conjugator: `α_{Sω} ∘ α_R ∘ α_{Sω}^{-1} != β_R`” must fail.
5. Predicate “live memo names the standard action as axiom content” must fail.
6. Predicate “note claims a Lattice name for the action” must fail.

Identity gates call `proper_cubic_count()`, `is_faithful(phi)`,
`alpha_rx_on_sigmay()`, and `conjugator_exhibits_beta()`.

## Honest-auditor / Boundary

The algebra is finite: `24` integer matrices and four `2 × 2` matrices
over `Q(i)`. The runner enumerates `G`, proves `G ≅ S_4` on the four
space diagonals, counts eight order-3 elements, checks that `3 ⊗ sgn`
cannot land in `SO(3)`, and conjugates `α` by every element of `G`.
It does not import a census of all order-24 subgroups of `SO(3)`.

Boundary, stated positively. The theorem classifies faithful unital
`*`-actions of this concrete `G` on one-site `M_2` up to conjugacy. It
does not classify unfaithful actions beyond excluding `φ0`. It does not
select a physical algebra action. It does not rewrite Qubit. It does not
introduce a pairing table, a 3-menu, or a unital `M_3` host. It does not
pick an automorphism of a two-site corner. QCD is unused.

The independent audit lane sets status. This note records
`actual_current_surface_status: bounded-support` as the machine surface of
the present packet and authors no audit verdict.

## What This Does Not Claim

- No displayed action is adopted as axiom content.
- Qubit remains `M_2(C)`. It is not flipped to `M_3`.
- The `Cl(3,0)` parenthetical is not used as a frame.
- No pairing table of lattice rotations with Pauli axes is asserted.
- No SWAP-corner Aut element is selected.
- No color or QCD identification is supplied.
- Whether any faithful action is required remains extra.

## Runner Contract

The companion runner counts `|G|`, checks `Rx,Ry,Rz,Sω ∈ G`, checks
`φ0` is not faithful, checks `α` is faithful via `α_Rx(σy)=σz`, checks
`β` is the displayed conjugate and disagrees with `α` on `Rx`, rejects
the mutation predicates, and verifies the live axiom quotes used above
are present while a Lattice name for the action is absent from that memo.
Declared audit inputs are this note and the axiom memo.
