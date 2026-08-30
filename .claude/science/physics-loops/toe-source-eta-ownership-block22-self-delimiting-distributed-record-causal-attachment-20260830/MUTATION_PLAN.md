# Mutation plan

Every mutation must be generated from a committed frozen runner and fail for
the intended reason.  Both implementations must add independent mutations.

## POVM mutations

- test only product Bloch samples instead of full-Hilbert spectra;
- drop an outcome or merge the duplicate axis signs;
- alter one axis/corner coefficient or sign product;
- remove the trace-free subtraction;
- rotate sites without internal Pauli axes, or axes without sites;
- insert an H1/H2/source lookup;
- use an abstract Stinespring call without explicit positive square roots.

## Common-representation and radial-code mutations

- use computational `|0>,|1>` pointer bits under the live spin action;
- assign pointer sites a hidden trivial onsite representation;
- hold radial Bloch axes fixed while rotating their sites;
- reverse one radial sign or normalize one corner by the wrong length;
- delete or collide a status/front/outcome slot;
- use a noncovariant relative-site set;
- rotate labels without rotating every physical pointer qubit state;
- replace the complete Kraus covariance identity by a label census.

## Instrument and Record/live mutations

- identify the six consumable live inputs with permanent Block09 Records;
- report a nontrivial outcome while leaving every live state unchanged;
- use a rank-one projector onto a nonorthogonal Ready payload;
- restore or copy the post-measurement live state;
- omit one Ready front or incur a factor-of-six completeness error;
- omit STOP or change a Locked word on repeat;
- combine outcomes into one coherent branch;
- compute an outcome probability from the same event's poststate;
- claim the nonprojective Lueders POVM is repeatable rather than only the
  orthogonal output pointer.

## Scope mutations

- claim mixed-front arbitration, relay, or infinite history;
- claim radius-one/nearest-neighbor compilation;
- hide a fixed tiling, site role, epoch, tape, scheduler, or global clock;
- derive Ready preparation, a physical rate, or cadence;
- import Block19's marks, factor two, or beta;
- claim action/source ownership, conserved gravity source, axiom necessity,
  audit status, obligation retirement, or TOE movement.
