# PR230 Block130 Neutral H3/H4 Eta Nonidentifiability

Status: exact negative boundary / current H1/H2 neutral support does not
derive the H3 physical transfer or H4 source/canonical-Higgs coupling.

## Scope

Block130 follows the Block129 Schur boundary and attacks the next independent
positive route: neutral H3/H4 physical transfer/source coupling.

The route needs both:

- H3: a same-surface physical neutral transfer, off-diagonal generator,
  primitive-cone certificate, or irreducibility authority;
- H4: source-to-canonical-Higgs coupling authority, either directly through a
  canonical `O_H`/source-Higgs packet or through an allowed physical-response
  bridge.

## Witness

The runner constructs a same-H1/H2 matrix family on a basis
`{source_singlet, neutral_1, neutral_2, neutral_3}`.  It fixes the source
self block and the neutral triplet primitive block `K`, then varies the
off-block source-triplet coupling `eta`.

At `eta=0`, the source singlet and neutral triplet are reducible and the H4
coupling vanishes.  At `eta=0.07`, the same source self block and the same
triplet `K` are retained, but the full matrix is entrywise positive and the
source-triplet coupling is nonzero.  Thus the H1/H2 support currently present
does not determine H3/H4.

This is not a physical model claim.  It is an independence witness for what the
current PR230 artifacts fail to specify: `eta` is a separate transfer/coupling
datum.

## Current-Surface Check

The strict neutral route remains absent:

- Block116 already records no strict H3/H4 artifact;
- no expected strict sidecar exists for neutral primitive cone, off-diagonal
  generator, neutral irreducibility, physical neutral transfer, source-triplet
  coupling, canonical `O_H`, source-Higgs pole rows, or W-response rows;
- raw `ensemble_measurement.json` files contain no strict neutral transfer,
  primitive, irreducibility, H3, H4, or source-canonical-Higgs coupling keys;
- the heat-kernel support remains mathematical support only, with no derived
  physical time/scale or source-coupling `eta`;
- finite `C_sx/C_xx` rows and equal-time covariance rows remain finite support
  only, not OS transfer, pole residue, or H4 coupling authority.

## Claim Boundary

This block does not claim retained or `proposed_retained` closure.  It does
not use H1/H2 positivity support as H3/H4 authority, does not promote the
heat-kernel witness to physical transfer, does not treat finite `C_sx` rows as
canonical `C_sH`, and does not use observed targets or forbidden unit
shortcuts.

Actual current surface status: exact negative boundary.

Conditional surface status: neutral route can reopen only with a same-surface
physical neutral transfer/off-diagonal primitive certificate plus H4
source/canonical-Higgs coupling authority, or with an equivalent W/Z or
source-Higgs physical bridge.

Proposal allowed: false.

## Exact Next Action

Do not relaunch neutral H3/H4 from H1/H2, heat-kernel, or finite-row support
alone.  The next positive artifact must supply a strict same-surface transfer
or off-diagonal generator and the independent source/canonical-Higgs coupling
datum `eta`, with FV/IR/contact/model-class firewalls intact.
