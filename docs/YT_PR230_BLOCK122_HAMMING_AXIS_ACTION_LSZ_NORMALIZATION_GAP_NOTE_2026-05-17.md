# PR230 Block122 Hamming-Axis Action/LSZ Normalization Gap

Status: exact negative boundary / base Block118 Hamming-Dirichlet `O_H` axis
support does not determine accepted action, scalar LSZ metric, source-overlap
normalization, or strict source-Higgs pole rows.

## Scope

Base Block118 is real progress: it selects the finite taste-radial `O_H` axis
as the unique lowest cyclic trace-zero Hamming-Dirichlet mode.  Block122 tests
the next possible shortcut: whether that finite axis selector also supplies the
action/LSZ/source-overlap normalization needed for the source-Higgs route.

## Result

It does not.  The runner constructs a one-mode quadratic family along the same
selected axis:

```text
S = 1/2 Z_H h^2 - kappa_sH s h + 1/2 c_ss s^2.
```

The selected axis and Hamming eigenvalue are unchanged.  By adjusting the local
source contact `c_ss`, the family keeps a source-source proxy fixed while
changing:

- `C_HH = 1/Z_H`;
- `C_sH = kappa_sH/Z_H`;
- `kappa_sH/sqrt(Z_H)`, the normalized source-overlap factor.

Therefore finite axis selection is exact support only.  The action-first route
still needs an accepted same-surface action/LSZ/source-overlap certificate and
strict physical `C_ss/C_sH/C_HH(tau)` pole rows with contact, threshold,
FV/IR, and covariance authority.

## Claim Boundary

This block does not claim retained or `proposed_retained` top-Yukawa closure.
It does not treat the Block118 axis selector as an accepted action, set
`kappa_s`, `c2`, `Z_match`, or contact terms by convention, relabel
`C_sx/C_xx` rows as physical `C_sH/C_HH` rows, or use `H_unit`,
`yt_ward_identity`, `y_t_bare`, observed targets, `alpha_LM`, plaquette, or
`u0`.

## Verification

```bash
python3 -m py_compile scripts/frontier_yt_pr230_block122_hamming_axis_action_lsz_normalization_gap.py
python3 scripts/frontier_yt_pr230_block122_hamming_axis_action_lsz_normalization_gap.py
# SUMMARY: PASS=11 FAIL=0
```

## Exact Next Action

Do not spend the next block on another finite-axis selector.  Either derive an
accepted same-surface action/LSZ/source-overlap certificate for the Block118
axis with strict `C_ss/C_sH/C_HH` pole rows, or pivot to W/Z, neutral H3/H4, or
a genuinely strict scalar pole authority route.
