# Assumptions And Imports

## Allowed Inputs

- Lattice axiom: `Z^3`, standard translation action, nearest-neighbor
  cubic adjacency, and finite-range locality.
- Gate B packet supplies a forward layer axis as part of the still-open
  propagation/readout semantics.

## Retired Source-Side Import

- The label/offset-preserving `3x3` forward stencil is no longer treated
  as an arbitrary row-local graph import. It is a finite-range
  translation-local `Z^3` relation once the forward layer axis is
  supplied.

## Still Open

- `GB-S1b`: scalar normalization, finite-core regulator, and source
  strength.
- `GB-S2`: propagation/readout semantics.
- `GB-S3b`: physical/growth-rule selection of this stencil and embedding
  update as Gate B dynamics.
