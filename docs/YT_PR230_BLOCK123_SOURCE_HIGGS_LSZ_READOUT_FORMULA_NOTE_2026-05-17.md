# PR230 Block123 Source-Higgs LSZ Readout Formula

Status: exact-support plus open premise / source-Higgs LSZ readout formula
derived; current PR230 surface lacks strict `C_ss/C_sH/C_HH` pole rows and
canonical `O_H`/action authority.

## Scope

Block123 is the constructive route after the Block120-122 boundaries.  It does
not try to promote the finite Hamming axis or source-only FH/LSZ rows.  It
asks what strict same-surface pole-row packet would actually remove the
`kappa_s` ambiguity without setting `kappa_s = 1`.

## Result

For a same-pole source-Higgs packet with overlaps

```text
z_s = <0|O_s|phi>,    z_H = <0|O_H|phi>,
```

and source response `dE_top/ds`, the invariant canonical-Higgs readout is

```text
y_H = (dE_top/ds) * sqrt(Res C_HH) / Res C_sH.
```

If Gram purity holds,

```text
Res C_sH^2 = Res C_ss Res C_HH,
```

then this reduces to the source-normalized formula

```text
y_H = (dE_top/ds) / sqrt(Res C_ss),
```

up to the pole sign convention.  The runner verifies that this is invariant
under source-coordinate rescaling, while the forbidden `kappa_s = 1` readout
varies.  It also records the necessary orthogonal-top-coupling premise: an
orthogonal neutral scalar contribution can change `dE_top/ds` without being
fixed by source-Higgs residues unless a Gram/covariance/top-coupling
certificate excludes or measures it.

## Current Boundary

The current PR230 surface still lacks:

- accepted same-surface canonical `O_H`/action/LSZ normalization;
- same-pole `Res C_ss`, `Res C_sH`, and `Res C_HH` rows with uncertainties;
- source-Higgs Gram purity or controlled orthogonal leakage;
- contact subtraction, FV/IR, threshold/model-class authority;
- retained-route and campaign gates with `proposal_allowed=true`.

No retained or `proposed_retained` closure is claimed.

## Verification

```bash
python3 -m py_compile scripts/frontier_yt_pr230_block123_source_higgs_lsz_readout_formula.py
python3 scripts/frontier_yt_pr230_block123_source_higgs_lsz_readout_formula.py
# SUMMARY: PASS=12 FAIL=0
```

## Exact Next Action

Use the Block123 formula as the readout contract.  The next positive artifact
must either produce strict same-surface `C_ss/C_sH/C_HH` pole rows with
canonical `O_H`/action/LSZ authority, or pivot to W/Z response rows with
allowed absolute `g2` authority and matched top-W covariance.
