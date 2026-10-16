# Generations and neighbourhood cells (B6/B7 working files)

- `orbits.py`: induced (monomial) representations on the 6, 8 and 12 point
  cubic orbits, with their 2O decompositions. The note's runner is
  `scripts/cubic_cell_taste_content_axis_permutation_2026_10_16.py`.
- `blockrep.py`, `blockhom.py`: signed corner representations of the 2x2x2
  block and their intertwiners. `block_embed.py` builds the moving block
  Dirac walk.
- `blockNN.py`, `blockNN2.py`: nearest-site searches. Without a dispersion
  constraint they found flat-band hits only (`nn_analyze.py`); with one they
  found nothing (`blockNN2_*.log`, best residual 0.079).
- `twisted_hits.py`, `fast_E12_E52.log`: the E1/2 + E5/2 coin has moving,
  dispersive walks, all massive at k = 0. `twisted_massless.py`/`.log`: with
  U(0) = 1 imposed, only degenerate solutions were found (zero quasienergy on
  the axes).
- `faces_search.py`, `faces_repro.py`, `fast_E12_H.log`: the six-neighbour
  cell coin E1/2 + H. The first search's best residual was 4.8e-9 (trial 14
  of the seed-0 sequence), far below the frozen floor. Polishing is in
  progress; see `faces_repro.log`.
- `*.npy`: raw coefficient arrays A_n (stencil order of `coinrep.stencil('cube')`).
  They are the twisted-pair hits, the massless-constrained twisted hit, a
  flat-band nearest-site block hit and the moving block Dirac walk.
  `coinrep.py` and `coinfast.py` are the search code the scripts import.
- `twisted_branches/`: Singular line-branch ideals for the E1/2 + E5/2 coin
  with U(0) = 1. Every branch that moves along an axis is a unit ideal (mod
  32003 and over Q by modStd). Only the axis-flat branch has solutions.
  This is mod-p evidence; see its README.
