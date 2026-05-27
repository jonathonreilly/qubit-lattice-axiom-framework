# Handoff

## What Moved

The block proves that the scaled source family

```text
S_h^(lambda) = S_0 - h lambda O_top
```

has Fisher metric `lambda^2`, so the intrinsic arclength coordinate is
`ell = lambda h` at the origin.  The derivative per unit arclength is
therefore `-O_top`, and the top component is `1/sqrt(6)` independent of
`lambda`.

## Honest Status

`exact-support / narrowed bridge`.

This is not retained Y_T closure.  The next hard bridge is:

```text
physical top Yukawa readout = Fisher/LSZ-normalized source coefficient
```

or else strict same-source top/W response evidence must measure the
coefficient.

## Verification

Run:

```text
python3 scripts/frontier_yt_primitive_physical_source_fisher_arclength_invariant.py
python3 scripts/frontier_yt_primitive_unit_source_action_physical_premise_no_go.py
python3 scripts/frontier_yt_lsp_source_scale_boundary_and_strict_response_contract.py
python3 scripts/frontier_yt_fh_top_w_response_ratio_gate.py
```
