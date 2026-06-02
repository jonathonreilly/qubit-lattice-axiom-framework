# Koide Finite Pointer-Trace Channel Bookkeeping

**Date:** 2026-05-31
**Claim type:** bounded_theorem
**Claim boundary:** finite `C_3` pointer/trace algebra and functional-extremum
bookkeeping. This note does not prove records dynamics, objectivity, or selection of
`r=1/2`.
**Primary runner:**
`scripts/frontier_koide_records_pointer_grounds_block_channel_2026_05_31.py`
with cache
`logs/runner-cache/frontier_koide_records_pointer_grounds_block_channel_2026_05_31.txt`.

## Result

The runner checks a finite pointer-style algebra:

- `S=C+C^2` is real, `C_3`-equivariant, and has spectrum `{+2,-1,-1}`;
- the two complex character lines have the same `S` eigenvalue and are conjugate, so this
  real observable resolves a singlet block and a doublet block;
- `S` commutes with `Gamma_chi=2P_singlet-I`, so this block grading is outside the
  anticommuting-operator no-go's target;
- `Jcs=(C-C^2)/sqrt(3)` commutes with `C` and satisfies `Jcs^2=-P_doublet`;
- the full trace weights the doublet by dimension `2`;
- equal-weight log-capacity extremization gives `r=1/2`, while dimension-weighted
  extremization gives `r=1`, and the fixed-total trace is flat.

These facts support a bounded bookkeeping split between a two-block pointer-style
readout and a trace-style readout. They do not prove that an environment actually
monitors `S`, that dephasing dynamically reaches `I/3`, or that objectivity forces the
equal-energy extremum.

## Boundary

The remaining source question is a records/objectivity theorem: if the charged-lepton
lane uses the two-block pointer-style readout, what dynamics force the
equal-energy `r=1/2` extremum rather than the dimension-weighted `r=1` extremum?

## Load-Bearing Authorities

[KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
[CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md)
[KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
