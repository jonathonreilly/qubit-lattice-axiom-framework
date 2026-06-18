# Assumptions And Imports

| Item | Role | Status |
|---|---|---|
| Lattice axiom: `Z^3`, nearest-neighbor cubic adjacency, finite-range locality | Supplies the substrate on which the local stencil is defined | framework axiom surface |
| Gate B runner finite slab labels | Defines the bounded runner packet to compare against | row-local runner data |
| Fixed offset set `{(1,dy,dz): dy,dz in {-1,0,1}}` | The stencil under test | explicitly defined in this bridge |
| `GB-S1b` scalar normalization | Not used to prove the stencil | remains open |
| `GB-S2` propagation/readout | Not used to prove the stencil | remains open |
| `GB-S3b` physical stencil selection/generation | Not proved here | remains open |

No observed target value, fitted selector, new axiom, or audit verdict is used.
