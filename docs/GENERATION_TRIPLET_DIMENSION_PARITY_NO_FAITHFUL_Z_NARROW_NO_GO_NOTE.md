# No Three-Dimensional SU(2) Rotation Carrier Has Faithful Center Action

**Date:** 2026-06-02
**Claim type:** no_go
**Review provenance:** source theorem candidate; post-landing audit decides the
ledger grade. This note introduces no axiom, primitive, Tier-A admission, or
generation-identification postulate.
**Primary runner:** `scripts/frontier_generation_triplet_dimension_parity_no_faithful_z.py`
(SCORECARD PASS=31)

## Claim

Let `z = -1` be the central element of `SU(2)`. In every finite-dimensional
`SU(2)` representation, the irreducible blocks have spin `j`, dimension
`2j + 1`, and central character

```text
z | spin-j = (-1)^(2j) I.
```

Thus faithful action of the center (`z = -1`) occurs exactly on half-integer
spin blocks, and every such block has even dimension. A three-dimensional
rotation carrier cannot be a direct sum of faithful-center blocks, because no
sum of even positive integers equals `3`.

Therefore a three-dimensional physical-rotation carrier cannot host the
faithful spinor-center / CAR-sign bit as an internal `SU(2)` representation
fact. The three-dimensional irreducible carrier is spin-1/vector/adjoint, on
which `z` acts as `+1`.

This is a narrow representation-theory no-go. It does not claim the actual
generation factor is fixed by this note, and it does not rule out spinor-state,
field-algebra, or non-representation-theoretic pairing routes.

## Computation

The runner verifies:

- left multiplication by `z = -1` is faithful on the even-dimensional spinor
  module;
- adjoint/vector action on `R^3` quotients the center (`z -> +1`);
- for `j = 0, 1/2, 1, 3/2, 2`, the explicit `2pi` operator matches
  `(-1)^(2j) I`;
- no faithful-center decomposition of dimension `3` exists;
- even target dimensions do admit faithful-center carriers;
- in tensor powers of spin-1/2 sites, spin-1 blocks occur only when the global
  center character is `+1`; when the global center character is `-1`, no
  three-dimensional block appears.

## No-Go Discipline Gate

**Gate result:** PASS for the scoped representation-theory no-go only.

### N1 - Alternative Route Enumeration

| route | what it would attempt | why it fails for this scoped no-go | marker |
|---|---|---|---|
| Adjoint/vector map | Carry `z` through the natural `SU(2) -> SO(3)` action on a three-vector. | The center is the kernel of this map, so `z` acts as `+1` on the vector carrier. | ATTEMPTED |
| Faithful left action | Use left multiplication by `z = -1`, which is genuinely faithful. | That action lives on the spinor module, whose complex dimension is even, not on a three-dimensional carrier. | ATTEMPTED |
| Three-dimensional invariant slice | Restrict the faithful left action to a three-dimensional invariant subspace. | The left spinor module has no such rotation-invariant three-dimensional slice; the runner checks the module structure used by this route. | ATTEMPTED |
| Multi-site tensor block | Build a three-dimensional block inside tensor powers of spin-1/2 sites while keeping faithful center action. | Spin-1 blocks occur only at even tensor power, where the global center character is `+1`; odd tensor powers have faithful center action but no three-dimensional block. | ATTEMPTED |
| Even-block partition | Decompose a three-dimensional carrier into half-integer-spin blocks. | Half-integer-spin blocks have even dimensions, and no sum of even positive integers equals `3`. | ATTEMPTED |
| Discrete or frame-selected pairing | Relate a spinor sign to a three-dimensional carrier by extra structure not represented as a single `SU(2)` module. | Out of scope; this note does not test non-representation-theoretic pairings. | OUT OF SCOPE |

### N2 - Wall-Independence Audit

The collapsed wall set has one wall: faithful center action forces even
dimension. The adjoint, left-action, invariant-slice, tensor, and partition
routes are different presentations of that single parity obstruction.

### N3 - Hidden-Wall Scan

The load-bearing inputs are standard finite-dimensional `SU(2)` representation
theory, the central-character formula, parity arithmetic, and the explicit
runner checks. The note does not assume CAR, observed masses, charge values,
generation identification, or a field-algebra law.

### N4 - Residual Matching

| context row | residual it names | residual attacked here | match? |
|---|---|---|---|
| `KOIDE_ADJOINT_MAP_QUOTIENTS_SPINOR_Z2_NARROW_NO_GO_NOTE_2026-06-02` | The adjoint/vector route quotients the spinor center. | This note tests whether a faithful-center three-dimensional rotation carrier exists by another representation route. | yes |
| `KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02` | A three-dimensional vector/grade-1 carrier is available, with the spinor sign still separate. | This note proves that no three-dimensional `SU(2)` carrier can make the center faithful. | yes |
| `BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28` | The spinor sign is central double-cover data. | This note applies the same center-action distinction to three-dimensional rotation carriers. | yes |

No value-side readout, charge, or empirical row is used as proof of this no-go.

### N5 - Rhetoric Audit

"Cannot host" means "cannot host as a three-dimensional `SU(2)` rotation
representation with faithful center action." It does not mean no algebra action
or future pairing can relate a spinor sign to a generation label. "Parity" means
even-versus-odd representation dimension, not spatial parity.

### N6 - Partial-Closure Path Scan

Open paths remain: a non-representation-theoretic vector/spinor pairing, a
discrete double-cover construction, or a second-quantized graded-locality route.
This note adds none of those as axioms and does not close them.

### N7 - Steelman

The strongest objection is that a faithful spinor sign plainly exists in the
framework's spinor representation, so it should be transferable to the
three-dimensional carrier. The reply is that transfer is not automatic inside a
single `SU(2)` representation: faithful center action is tied to half-integer
spin blocks, and those have even dimension. The steelman identifies a real open
pairing problem, but not a three-dimensional representation-theory escape.

### N8 - Cross-Cycle Echo

The overclaim risk is to turn one failed representation route into a claim that
all spinor/sign routes are impossible. This note avoids that by pruning only the
three-dimensional `SU(2)` carrier route and carrying the non-representation and
field-algebra routes forward as open.

## Cited Context

Context rows, not status claims:

- `KOIDE_ADJOINT_MAP_QUOTIENTS_SPINOR_Z2_NARROW_NO_GO_NOTE_2026-06-02`
- `KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02`
- `BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28`
- `PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02`

## Command

```bash
python3 scripts/frontier_generation_triplet_dimension_parity_no_faithful_z.py
```

Expected output: `SCORECARD: PASS=31 FAIL=0`.
