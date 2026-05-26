# Goal

Repair `translation_covariance_local_op_theorem_note_2026-05-02` after
audit found that its previous proof imported a full one-site
`H_phys` translation representation from the lattice Noether row.

The repair target is a narrowed positive theorem on the retained
finite tensor-product translation surface:

- replace the stale Noether dependency with the retained tensor-product
  translation/fermion bridge;
- narrow from arbitrary `H_phys` local operators to one-site and
  finite-support tensor-product operators on `H_Lambda`;
- keep independent audit as the only source of effective retained status.
