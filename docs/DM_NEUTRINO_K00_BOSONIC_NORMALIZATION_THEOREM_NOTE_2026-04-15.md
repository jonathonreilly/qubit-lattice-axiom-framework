---
claim_id: dm_neutrino_k00_bosonic_normalization_theorem_note_2026-04-15
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
---

# DM Neutrino `K00` Restricted-Packet Normalization Identifiability No-Go

**Date:** 2026-04-15; first-principles obstruction repair 2026-07-12
**Claim type:** no_go
**Role:** exact negative boundary for the supplied `2 x 2` / `3 x 3` packet
**Status:** candidate exact negative boundary for independent audit; the prior
positive endpoint `K00 = 2` is withdrawn on the actual current surface
**Primary runner:**
[`scripts/frontier_dm_neutrino_k00_bosonic_normalization_theorem.py`](../scripts/frontier_dm_neutrino_k00_bosonic_normalization_theorem.py)
**Cached output:**
[`logs/runner-cache/frontier_dm_neutrino_k00_bosonic_normalization_theorem.txt`](../logs/runner-cache/frontier_dm_neutrino_k00_bosonic_normalization_theorem.txt)

## Claim boundary

On the restricted packet containing

- the target coefficient `K00 = (K_mass)00` and its rank-one projector
  `F00 = J3/3`;
- the source swap-even projector `P+ = J2/2`;
- swap symmetry on the two source coordinates;
- scalar-baseline log-determinant response;
- no independently constructed source-action map from the source coordinates
  to a physical `2 x 2` deformation; and
- no independently constructed typed map from that source deformation to the
  heavy-basis `F00` channel,

the value `K00 = 2` is not identifiable. The exact response equation is only

`K00 = c tau_+`,

where `c` is the source-operator embedding scale. Swap symmetry independently
fixes only `tau_E = tau_T`; it does not fix their common magnitude and hence
does not fix `tau_+`.

The previously advertised law `K00 = 2 tau_+` is the special choice `c = 2`,
equivalently the declaration that the physical source deformation is
`tau_+ J2 = 2 tau_+ P+`. The endpoint `K00 = 2` additionally chooses
`tau_+ = 1`. Neither choice follows from the restricted packet.

This is a no-go for that packet, not a no-go against a future framework
derivation of `K00`. A future source-action and cross-sector response theorem
can defeat it by constructing both `c = 2` and `tau_+ = 1` without using the
target value as input.

## Minimal premise set and forbidden imports

The foundation surface is the approved
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) node: Lattice,
Qubit, Admissibility, and Record. Its qualification explicitly leaves
normalization, source/action, log-determinant readout, and arbitrary physical
observable identification outside axiom content. The approved
[`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md),
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md),
and
[`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
nodes do not supply any of those missing maps.

The proof below uses no observed neutrino value, fitted selector, literature
number, unit convention, target `K00` value, or hard-coded source amplitude.
The old assignments `tau_E = tau_T = 1/2` and `K00 = 2` are test cases only;
they are not proof inputs.

## Exact proof

### 1. The target algebra leaves `K00` free

Let

`F00 = J3/3`.

Then `F00^2 = F00`, `rank(F00) = 1`, and `Tr(F00) = 1`. For every real
`kappa`, the aligned target matrix

`H_kappa = kappa F00`

obeys

`Tr(H_kappa F00) = kappa Tr(F00^2) = kappa`.

Thus the exact target identities admit every real value `K00 = kappa`. The
breaking-triplet independence proved by the earlier algebra does not remove
this aligned-core degree of freedom.

### 2. Swap symmetry fixes a ray, not the source magnitude

Let

`P_swap = [[0,1],[1,0]]`.

Solving `P_swap tau = tau` gives the full fixed space

`tau = a (1,1)`, with `a` real.

Therefore `tau_E = tau_T = a` and `tau_+ = 2a`, but swap symmetry supplies no
equation for `a`.

The sharp swap-even projector

`P+ = (I + P_swap)/2 = J2/2`

does not repair that coordinate ambiguity. A column of `P+` is
`(1/2,1/2)`, whereas the unit bright vector is
`(1/sqrt(2),1/sqrt(2))`. They are different normalizations of the same
swap-even ray. Selecting the projector column as the physical source
coordinate is an extra coordinate-extraction rule, not a consequence of swap
invariance.

### 3. The most general bright-ray response contains a free embedding scale

Any real source operator supported only on the swap-even bright ray is a
scalar multiple of `P+`. Parameterize the source deformation by

`S(c,tau_+) = c tau_+ P+`.

The target deformation is

`T(K00) = K00 F00`.

For a nonzero scalar baseline `m`, exact determinant algebra gives

`det(m I3 + K00 F00) / m^3 = 1 + K00/m`,

and

`det(m I2 + c tau_+ P+) / m^2 = 1 + c tau_+/m`.

Consequently equality of the baseline-subtracted log-absolute-determinant
responses for all nonsingular `m` is equivalent to

`K00 = c tau_+`.

This equation derives the coefficient relation once `c` is supplied; it does
not derive `c`.

### 4. Two exact countermodel pairs isolate two independent walls

Fix `tau_+ = 1`.

- With the sharp-projector embedding `S = P+`, one has `c = 1`, and exact
  response matching gives `K00 = 1`.
- With the row-sum embedding `S = J2 = 2P+`, one has `c = 2`, and exact
  response matching gives `K00 = 2`.

Both source operators are swap-even, rank one, and supported on the same
bright ray. Both admit an exactly response-matched target deformation. The
restricted packet contains no source-action construction that selects the
second embedding over the first.

Now fix `c = 2`.

- `tau_+ = 1/2` gives `K00 = 1`.
- `tau_+ = 1` gives `K00 = 2`.

Both source coordinate vectors are swap-even. Thus fixing the typed embedding
does not fix the source magnitude, and fixing the source magnitude does not
fix the typed embedding. These are two independent missing constructions.

### 5. The factor-of-two trap

The old packet used `tau_+` in two inequivalent roles:

1. as the sum of the coordinates of a column of `P+`, which gives
   `(tau_E,tau_T) = (1/2,1/2)` and `tau_+ = 1`; and
2. as the coefficient multiplying the full generator `J2` in the physical
   source deformation.

The first role concerns coordinates on the bright ray. The second is a typed
operator embedding and introduces the factor `J2 = 2P+`. Equating the two
roles is exactly the missing normalization map. Isospectrality of `F00` and
`P+` cannot supply it because isospectrality acts on the normalized projectors,
not on an independently scaled source coordinate.

This proves the scoped no-go. ∎

## What the runner independently checks

The exact SymPy runner constructs rather than assigns the load-bearing
objects. It checks:

1. projector, rank, trace, and swap identities for `F00` and `P+`;
2. the free target family `H_kappa` and `K00 = kappa`;
3. the complete swap-fixed source space `a(1,1)`;
4. the distinct projector-column and unit-vector coordinate normalizations;
5. both symbolic determinant polynomials;
6. symbolic solution of determinant and log-absolute response equality as
   `K00 = c tau_+`, including exclusion of an absolute-value sign branch;
7. the `c = 1` versus `c = 2` countermodel pair at fixed `tau_+`;
8. the `tau_+ = 1/2` versus `tau_+ = 1` countermodel pair at fixed `c`;
9. the approved-premise registry, every approved primitive source scope, and
   the minimal-axiom nonsupply boundary.

No PASS line assigns the disputed endpoint before testing it.

## Falsifier and exact repair target

This no-go is defeated by a self-contained theorem/runner pair that constructs
all three of the following from the approved premise surface or retained
dependencies:

1. a typed physical source deformation `S(tau)` and proves its bright-ray
   coefficient is `c = 2` rather than choosing `J2` by notation;
2. a sharp source-selection law that fixes `tau_E = tau_T = 1/2` as physical
   source coordinates rather than as a selected column convention; and
3. a source-to-heavy observable theorem that maps `S(tau)` to
   `K00 F00` and proves equality of the physical response, rather than merely
   comparing two already selected projectors.

If those constructions land with retained-grade dependencies, the runner's
general identity immediately specializes to `K00 = 2`.

## What this claims

- An exact two-parameter identifiability obstruction on the explicit
  restricted packet.
- The strongest response statement available without hidden normalization is
  `K00 = c tau_+`.
- The two missing constructions are independently testable.
- `K00 = 2 tau_+` and `K00 = 2` remain valid conditional specializations at
  `c = 2` and `(c,tau_+) = (2,1)`, respectively.

## What this does not claim

- It does not claim that no extension of the framework can derive `K00 = 2`.
- It does not exclude a future lattice source-action, Ward, variational,
  representation-theoretic, or Record-facing typed map.
- It does not change any downstream benchmark or publication surface.
- It does not set an audit verdict or effective status.
- It does not treat the broader observable-principle or source-amplitude notes
  as retained dependencies.

## No-Go Discipline summary

The full N1-N8 checklist is recorded in the branch-local physics-loop claim
certificate. Its scope is this explicit finite restricted packet only. Five
routes were attempted: determinant-response matching, equivariant bright-ray
transport, sharp-projector normalization, direct heavy-kernel reconstruction,
and Record/log-determinant closure. Each terminates at one of the two explicit
free parameters above. Conventionally declaring `c = 2` remains a valid
bounded route, so the result is not phrased as requiring a new axiom.

## Command

```bash
python3 scripts/frontier_dm_neutrino_k00_bosonic_normalization_theorem.py
```
