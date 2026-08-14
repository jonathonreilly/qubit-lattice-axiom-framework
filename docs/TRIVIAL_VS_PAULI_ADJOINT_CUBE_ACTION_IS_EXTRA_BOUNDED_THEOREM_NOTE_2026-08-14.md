---
claim_id: trivial_vs_pauli_adjoint_cube_action_is_extra_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On one-site M_2(C) over Q(i), the identity map φ0 and the displayed Pauli-adjoint cycle φAd both send the body-diagonal cube 3-fold to automorphisms of M_2, but φ0(σx)=σx ≠ σy=φAd(σx). Live Lattice names proper cubic rotations of Z^3 sites; live Qubit names the one-site algebra M_2(C). Neither sentence names φ0, φAd, Ad_U, or an intertwiner. Both maps are extras. φAd is displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/trivial_vs_pauli_adjoint_cube_action_is_extra_2026_08_14.py
---

# Trivial Versus Pauli-Adjoint Cube Action Is Extra

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact `Q(i)` identities for two displayed maps of one body-diagonal
cube 3-fold onto one-site `M_2(C)`. No pairing table, no 3-menu, no unital
`M_3` factor in `C`, no Qubit rewrite, and no adopted intertwiner.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/trivial_vs_pauli_adjoint_cube_action_is_extra_2026_08_14.py`](../scripts/trivial_vs_pauli_adjoint_cube_action_is_extra_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work in one-site `M_2(C)` with the Pauli matrices over `Q(i)` written below.
The body-diagonal cube 3-fold is the order-3 rotation of the unit cube about
the space diagonal. Two maps of that 3-fold onto `M_2` are displayed.

- Trivial action `φ0`: the identity on `M_2`. So `φ0(σx)=σx`, `φ0(σy)=σy`,
  `φ0(σz)=σz`. Physical cubic rotations still move sites of `Z^3`; they do
  not act on the one-site algebra. This is a lawful reading of Lattice+Qubit
  with no intertwiner.
- Pauli-adjoint action `φAd`: the unique unital `*`-linear map with
  `φAd(σx)=σy`, `φAd(σy)=σz`, `φAd(σz)=σx`. The matrix
  `U=(I-i(σx+σy+σz))/2` is an exhibit of this map by `Ad_U(X)=U X U*`. The
  matrix `U` is not axiom content.

Theorem 1 is the disagreement: `φ0(σx)=σx ≠ σy=φAd(σx)`. Same cube 3-fold,
two maps. The control that both maps have order dividing three does not
identify them.

Live Lattice names proper cubic rotations of the sites of `Z^3`. Live Qubit
names the one-site algebra `M_2(C)`. Those sentences do not name `φ0`,
`φAd`, `Ad_U`, or an intertwiner. Both maps are extras. This note displays
them. It does not adopt `φAd`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Q(i) identities exhibit two maps of one cube 3-fold onto M_2 that disagree on σx. Live Lattice and Qubit sentences are quoted and do not name either map. Neither map is adopted as axiom content."
trace_class: negative_route_pruning
target_claim_id: trivial_vs_pauli_adjoint_cube_action_is_extra
target_blocker_text: "whether a Lattice cubic rotation of Z^3 is the same map as a Pauli-axis adjoint action on M_2"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded algebra; no intertwiner is adopted"
conditional_surface_status: "exact for the two displayed maps on one-site M_2(C); no physical selector of φAd is claimed"
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
on `M_2` is therefore uniquely determined by the images of `σx`, `σy`, and
`σz`.

- `φ0` is the identity map of `M_2`.
- `φAd` is the unique unital `*`-linear map with
  `φAd(σx)=σy`, `φAd(σy)=σz`, `φAd(σz)=σx`.
- The exhibit `U = (I - i(σx + σy + σz))/2` is a displayed matrix in
  `M_2(Q(i))`. Write `Ad_U(X) = U X U*`.

Physical rotations of `Z^3` remain site permutations. They are not rewritten
as algebra maps.

## Theorem 1 — the two maps disagree on `σx`

`φ0(σx) = σx` and `φAd(σx) = σy`. The matrices `σx` and `σy` differ in
every off-diagonal entry (`1` versus `-i` in position `(1,2)`). Therefore

```text
φ0(σx) = σx ≠ σy = φAd(σx).
```

The same cube 3-fold therefore admits two distinct maps into the automorphism
picture of `M_2`. The identification of those maps is not an identity.

## Theorem 2 — live Lattice and Qubit do not name either map

The Lattice sentence quoted above names the sites of `Z^3` and the proper
cubic rotations about each site. It names a geometric action on the lattice.
It does not name `φ0`, `φAd`, `Ad_U`, or an intertwiner from site rotations
into `Aut(M_2)`.

The Qubit sentence quoted above names the one-site algebraic presentation
`M_2(C)`. It does not name a preferred action of the cube 3-fold on that
algebra, and it does not rewrite the presentation as `M_3`.

The live memo therefore supplies site rotations and the one-site algebra as
separate primitive sentences. It does not supply a map that identifies them.

## Theorem 3 — both maps are extras

An extra, in this note, is a map or identification that is not named by the
quoted Lattice or Qubit sentences and is not a registered approved primitive.
Both `φ0` (as an algebra action of the cube 3-fold) and `φAd` are extras.

`φ0` is a lawful reading of the two axioms with no intertwiner: Lattice
rotations move sites; Qubit still presents each site as `M_2(C)`; the algebra
is not required to transform. Displaying `φ0` does not add a primitive.

`φAd` is a displayed unital `*`-linear cycle of the Pauli axes. It is a
standard mathematical automorphism of `M_2`. Displaying it does not make it
axiom content. This note does not adopt `φAd`. The exhibit `U` is a lift of
`φAd`, not a Lattice object and not a Qubit rewrite.

## Control — order three is not the disagreement

Direct composition on the Pauli basis gives

```text
φAd(σx) = σy,   φAd(σy) = σz,   φAd(σz) = σx,
```

so `φAd³` is the identity on that basis, hence `φAd³ = id` on `M_2`. Also
`φAd(σx) = σy ≠ σx`, so `φAd ≠ id`. The identity map satisfies `φ0³ = id`.

Both maps therefore have order dividing three. The disagreement is the image
of `σx`, not the order.

The exhibit matches the cycle: `U*U = I` and `Ad_U(σx)=σy`,
`Ad_U(σy)=σz`, `Ad_U(σz)=σx`. That calculation identifies `Ad_U` with the
already-displayed map `φAd`. It does not promote `U` into the axiom memo.

## Mutations

1. Predicate `φ0(σx) == φAd(σx)` must fail.
2. Predicate “live memo names `Ad_U` or Pauli-adjoint” must fail.
3. Predicate “live memo contains Lattice-named” must fail.

## Honest-auditor / Boundary

The algebra is elementary: four `2 × 2` matrices over `Q(i)`, two maps, and
one displayed unitary exhibit. The runner reconstructs `φAd` from the three
Pauli images, reconstructs `Ad_U` from the displayed formula for `U`, and
checks the three mutation predicates against the live axiom memo rather than
against a working-tree paraphrase.

Boundary, stated positively. The theorem classifies two displayed maps of one
cube 3-fold onto one-site `M_2`. It does not classify every automorphism of
`M_2`, every cubic rotation, or every possible intertwiner. It does not select
a physical algebra action. It does not rewrite Qubit. It does not introduce a
pairing table, a 3-menu, or a unital `M_3` host. `G_N` and QCD are unused.

The independent audit lane sets status. This note records
`actual_current_surface_status: bounded-support` as the machine surface of
the present packet and authors no audit verdict.

## What This Does Not Claim

- Neither displayed map is adopted as axiom content.
- Qubit remains `M_2(C)`. It is not flipped to `M_3`.
- No pairing table of lattice rotations with Pauli axes is asserted.
- No 3-menu and no unital `M_3(C)` factor inside `C` is asserted.
- No color, QCD, or `G_N` identification is supplied.
- `U` is an exhibit of `φAd`, not a Lattice object.

## Runner Contract

The companion runner checks the Pauli matrices and the two maps over `Q(i)`,
checks `φAd³ = id` with `φAd ≠ id`, checks the `Ad_U` exhibit, rejects the
three mutation predicates, and verifies that the live axiom memo quotes used
above are present while `Ad_U`, Pauli-adjoint, and Lattice-named are absent
from that memo. Declared audit inputs are this note and the axiom memo.
