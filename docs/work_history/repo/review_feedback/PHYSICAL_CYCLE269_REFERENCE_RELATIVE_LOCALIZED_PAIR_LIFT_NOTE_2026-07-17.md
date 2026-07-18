# Physical Cycle-269 reference-relative localized pair lift — 2026-07-17

Type: constructive physical stabilizer-state component

Status: exact localized two-column state lift relative to a supplied
fixed-sector vacuum; absolute preparation, position superposition, coin, and
full-Fock compilation remain open

Authority: none

Audit: unset

Constitutional effect: none

Runner:
`scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py`

## Result

There is an exact physical Cycle-269 state lift for a localized
one-carrier/one-source even-pair orbit, provided one fixed global reference
state is supplied.

Use the fixed +++ Wilson sector. The complete family consisting of all local
checks, all three positive Wilsons, and all `B_v=+1` vacuum occupations has
rank equal to the number of Cycle-269 face M2s. It therefore specifies one
unique stabilizer vacuum ray `|Omega_+++>`. Add the six auxiliary port M2 per
cell in their zero-tag state; the combined physical reference tableau again
has full rank.

Choose one ordered pair `(s,m)` of adjacent intracell half-edge modes joined
by an internal triangular face. The role names are “source” and “carrier,”
but source/carrier roles are not independent species: reversing them changes
the bounded `A(s,m)` representative by a minus sign and gives the same
identical-fermion physical ray. The runner checks that reversal multiplies both
columns by the same `-1`, leaves both tag patterns unchanged, and preserves the
stream phase. The lift is for one localized pair ray, not two distinguishable
matter species.

Let `s'` and `m'` be the unique outer-stream partners. Define the two encoded
columns by bounded physical Pauli/tag representatives:

```text
E_(s,m)|0> = A(s,m)|Omega_+++> tensor |tags=s,m>

E_(s,m)|1> = alpha A_(m,m') A_(s,s') A(s,m)|Omega_+++>
                     tensor |tags=s',m'>,
```

where each occupied-to-empty outer FSWAP contributes `+i A_e` or `-i A_e`
according to its stored edge orientation and `alpha` is the product of the
two factors. Thus `alpha=+1` or `-1` and is derived from the actual mapped
FSWAP polynomial, not fitted.

The columns have distinct complete `B_v` and port-`Z` eigenvalue patterns, so
their physical inner product is exactly zero. Each is a unitary Pauli image
of a normalized unique stabilizer state. Therefore

```text
E_(s,m)^dagger E_(s,m) = I_2
```

exactly. This is an exact isometry, not a decoded-label proxy.

On this two-dimensional slice orbit, let `G_coarse=X`, exchanging the local
pair and its streamed image. The restricted physical operator word consists of
the two actual mapped outer-FSWAP polynomials followed by the collision-safe
auxiliary-port gates. The runner evaluates its exact occupied-to-empty Pauli
branches and tag action on both columns; the reverse word restores the full
Pauli/tag representative and FSWAP phase. Consequently

```text
E G_coarse = G_physical E
```

on the declared two-column code space.

Here `G_physical` means the restriction of that supplied physical operator
word to these two columns. It is not an assembled full-Hilbert-space matrix, a
coin/contact update, or a complete physical macrostep.

## What is physically encoded

The runner keeps decoded action and encoded stabilizer state separate.

Encoded and checked physically are:

- the unique full-rank face-code vacuum in one fixed Wilson character;
- zero auxiliary port tags;
- the bounded physical `A` representatives that create the two even matter
  occupations;
- the signed `B_v` eigenvalue pattern of each column;
- all local-check and Wilson eigenvalues;
- the local port constraints `B_v Z_port(v)=+1`;
- orthogonality and normalization of the two columns; and
- the mapped FSWAP/catch-up action between those columns.

Decoded labels are used only to enumerate the source port, carrier port,
arrival ports, occupation masks, and expected auxiliary tag masks. The proof
does not identify a decoded permutation table with a physical ket.

## Reference-relative operator support and overhead

The input column differs from the supplied reference by one internal `A` word
and two tag flips. Its relative Pauli/tag representative support varies with
the local framing but is at most eleven M2. The output column uses the internal
word, two outer-edge `A` factors, and two tag flips. Across `L=3,4,5,6` its
maximum relative representative support is nineteen-M2. Both bounds are
independent of volume.

The physical allocation remains the auxiliary-port result:

```text
15 Cycle-269 face M2/cell
+6 auxiliary port M2/cell
=21 M2/cell.
```

No extra state-lift M2 is added. The +++ Wilson vacuum is global supplied
state structure, not hidden in the local support count.

## Exact stabilizer rank and preparation boundary

For every tested size, local checks plus three Wilsons plus all vacuum `B_v`
have full face rank. Appending one `Z` stabilizer for every auxiliary port has
full rank `21 L^3`, with no phase inconsistency. This is an explicit unique
physical stabilizer-state specification.

At `L=3,4,5,6`, the face ranks are 405, 960, 1875, and 3240; after adding the
ports the full reference ranks are 567, 1344, 2625, and 4536. All generator
commutator, Hermiticity, and phase-inconsistency counts are zero.

Deleting the three Wilson stabilizers leaves rank deficit three. Therefore
the local-check and occupation data alone do not pick one vacuum ray. The
current construction supplies the +++ character and does not prepare it.
Global vacuum preparation remains open; no finite-depth or bounded-support
preparation circuit is inferred from full stabilizer rank.

Deleting each Wilson separately gives deficit one, while deleting all three
gives deficit three, on every tested size. Thus every fixed positive Wilson
stabilizer row is an explicit, independently load-bearing import for this
reference ray.

Accordingly, “bounded lift” here means that each column is a bounded physical
operator image of the supplied reference. It does not mean an absolute
bounded preparation from an unentangled face state, a common encoder across
Wilson sectors, or an address-controlled superposition over all locations.
This reference-relative boundary is load-bearing.

## Isometry, intertwining, inverse, and held size

At each `L`, there are `12 L^3` undirected internal triangular faces and
`24 L^3` ordered source/carrier descriptions. The runner tests the localized
two-column lift for every ordered description at training `L=3,4,5` and held
`L=6`.

For every lift it checks:

- exactly the source and carrier `B` occupations in column zero;
- exactly their two distinct outer arrivals in column one;
- matching port tags and zero local port-constraint leakage;
- exact Gram matrix `[[1,0],[0,1]]`;
- actual restricted two-edge FSWAP Pauli action and collision-safe tag
  catch-up on both columns;
- `E X = G_physical E` on both columns;
- exact inverse, including the fermionic phase; and
- the common minus-sign equality of both columns under source/carrier role
  reversal.

Held `L=6` contains `5,184` ordered localized lifts. The support, rank,
phase, occupation, auxiliary constraint, isometry, intertwining, and inverse
acceptance conditions are frozen from `L=3,4,5`.

The tested lift counts at `L=3,4,5,6` are 648, 1536, 3000, and 5184. All
occupation, port-constraint, Gram, restricted physical face-action,
full-representative intertwining, inverse, and role-reversal failure counts are
zero. Input relative supports range from 3 through 11 M2 over the observed
framing classes; output relative supports range from 7 through 19 M2, with no
volume growth.

## Proper-cubic and translation covariance

At `L=3`, the complete family is tested under all 24 proper-cubic frames and
all L=3 translations. The inherited bounded incident-order Clifford repair is
applied to the physical `A` words. Each transformation maps `(s,m)` to
`(Rs,Rm)`, maps both tag masks, and maps both encoded columns with one common
scalar phase. Equality of the two column phases is the state-level covariance
condition needed for the intertwiner; checking the rays separately would be
too weak.

The fixed +++ vacuum ray is preserved because frames and translations map the
local stabilizer family, Wilson span, all positive `B` occupations, and zero
tags to themselves. One coordinate ordering is used to print Pauli words, but
the tested repaired group action maps the physical ray family without a
preferred source direction, frame, or origin. Enumeration-order freedom of the
catch-up product is inherited from and tested in the separate auxiliary-port
artifact.

The runner performs 24 frame-level and 27 translation-level phase-aware
reference-tableau tests, plus 15,552 two-column frame tests and 17,496
two-column translation tests. All tableau, common-column-phase, tag-map, and
representative failures are zero.

## Constraint leakage, deletion, and lawful domain

Every input and output representative commutes with all inherited local checks
and all three Wilsons. Its `B` eigenvalue pattern matches its port tags, so
every `B_v Z_port(v)=+1` constraint holds.

Two deletions are decisive. The catch-up deletion and stream-factor deletion
are tested separately:

1. deleting catch-up leaves the matter occupations at `s',m'` and the port
   tags at `s,m`, outside the target auxiliary constraint column;
2. deleting either one of the two outer stream factors produces a different
   `B` pattern orthogonal to both code columns.

Both stream-factor deletions are tested separately for every lift, giving
1296, 3072, 6000, and 10,368 deletion tests at `L=3,4,5,6`. Local-check,
Wilson, port-constraint, catch-up-deletion, and stream-deletion failure counts
are all zero.

The lawful domain rejects coincident source/carrier ports, mismatched tag
masks, opposite intracell ports lacking an internal triangle, intercell pairs,
out-of-range labels, and periodic `L<3`.

## Exact boundary and remaining routes

This supplies a state-level `E` in the physical Cycle-269 catch-up lane, but it
is deliberately smaller than the missing compiler.

Open structure is:

- bounded preparation of the fixed-Wilson global vacuum;
- one coherent encoder spanning different pair positions or Wilson sectors;
- a distinguishable source role or second matter species;
- odd one-particle states, which are outside Cycle 269’s total-even algebra;
- the actual six-mode Cycle-219 coin and coherent auxiliary-port routing;
- local contact on an encoded multiparticle superposition;
- the complete full-Fock update and rank-73 sea; and
- any energy, inertia, source, gravity, time, Record, or Born semantics.

The stabilizer reference is not a Record, a compiler slice is not physical
time, and the auxiliary tag is not a source law. There is no no-go claim, and
there is no axiom pressure.

## Disposition

```text
unique fixed-sector physical vacuum tableau:       PASS
bounded reference-relative two-column E:           PASS
exact isometry:                                     PASS
restricted physical-word intertwining and inverse:  PASS
all frames/translations and held L=6:               PASS
constraint leakage and deletion controls:          PASS
assembled full-Hilbert-space G matrix:              NOT CONSTRUCTED
absolute bounded vacuum preparation:                OPEN
coherent position/source-role encoder:               OPEN
coin/contact/full-Fock compiler:                     OPEN
shared obstruction or axiom pressure:               NONE IDENTIFIED
```
