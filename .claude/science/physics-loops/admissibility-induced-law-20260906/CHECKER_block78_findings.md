# Block 78 — control and findings (2026-09-22)

1. Disjoint machinery (`specs/supervisor_control_block78_hard_core.py`): full spectra by dense diagonalisation where the runner has exact traces; a two-dimensional torus and a three-record sector the runner does not reach.
2. **A wrong test caught before the gates (supervisor).** The first T3 compared expectations of `H²` on the pair; `(H⊗1 + 1⊗H)²` has the two-body cross term `2H⊗H`, so additivity had no reason to hold even for the free pair, and the check failed. Rebuilt with complex one-record states and the generator itself; the free pair is then exactly additive and the hard-core pair is not.
3. **T2 sharpened by the control (supervisor).** The fourth traces agree on N = 6 but the full spectra differ; the sixth trace was added to the exact runner (differs on N = 6), and the statement now attributes the sign's visibility to the ring's parity.
4. Finding folded: the closed forms `(N − 2)/(N − 1)` etc. are read off four rings and stated as such, not proved.
5. Finding folded: a name in the machine-status block caught by the scan; reworded.
