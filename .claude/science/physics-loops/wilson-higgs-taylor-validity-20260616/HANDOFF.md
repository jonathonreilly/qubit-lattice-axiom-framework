# Handoff

This branch tightens the Wilson/Higgs perturbative-validity runner check.

Added runner checks:

- closed form versus Taylor at `r=0.100`: relative error about `1.97e-4`;
- closed form versus Taylor at displayed matching `r=0.235`: relative error
  about `7.34e-3`, sub-percent;
- near-edge `r=0.500`: Taylor truncation visibly breaks down, with relative
  error about `2.17`.

The physical Higgs-pole readout, uniform-`N_taste = 16` admission, and Wilson
coefficient normalization remain outside this repair.

No audit ledger, publication matrix, or front-door status file is edited.
