# Route Portfolio

## Route A: Register helper module itself

Selected and implemented. The note names
`scripts/lattice_3d_inverse_square_kernel.py` as the primary module, and it
runs within the cache timeout.

## Route B: Use downstream tail-stat runner as primary

Not selected. The downstream runner is a consumer; the helper wrapper's primary
authority is the helper module itself.
