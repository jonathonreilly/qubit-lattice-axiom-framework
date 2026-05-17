# PR230 Block120 Source-Reparametrization Invariant Minimal-Data Boundary

Status: exact negative boundary / the current PR230 head does not contain the
minimal same-surface invariant data packet needed for retained top-Yukawa
closure.

## Scope

Block120 compresses the post-Block118 route surface.  It does not repeat chunk
completion.  It asks what data are invariant under scalar-source
reparametrization and whether any current source-Higgs, W/Z, Schur, or neutral
route supplies a strict physical packet.

## Result

The runner verifies:

- the source-reparametrization gauge no-go remains active;
- the FH/LSZ invariant readout theorem remains exact support, not closure;
- raw `dE_top/ds` varies under source/operator rescaling, while
  `dE_top/ds / sqrt(Res_C_ss)` is invariant only if the physical scalar pole
  residue exists;
- a W/Z mass-plus-response dictionary can preserve top/W/Z masses and
  same-source responses while changing `y_t`, `g2`, and `gY`; an allowed
  absolute pin is still required;
- Blocks110/112/114 keep the accepted action/canonical `O_H` plus strict
  source-Higgs pole-row packet absent;
- Block115 keeps the strict W/Z physical-response packet absent;
- Blocks111/113 keep strict Schur/Feshbach pole authority absent despite the
  complete finite support packet;
- Block116 keeps strict neutral H3/H4 physical transfer and H4 coupling absent;
- Block117 keeps strict Schur/scalar-LSZ pole authority absent;
- Block118 supplies exact finite Hamming-Dirichlet support for the taste-radial
  `O_H` axis, but not accepted action, LSZ, source-overlap normalization, or
  strict pole rows;
- aggregate assembly, retained-route, campaign, and completion-audit gates
  remain open and deny proposal wording.

## Minimal Positive Packets

Any future positive closure must supply one strict same-surface disjunct:

- accepted EW/Higgs action with `dS/ds = sum O_H`, canonical `O_H`, and
  physical `C_ss/C_sH/C_HH(tau)` pole rows with Gram, FV/IR, contact, covariance,
  and scalar-LSZ/model-class authority;
- strict W/Z response packet with accepted action, production W/Z rows,
  same-source top rows, matched covariance, strict non-observed `g2` or another
  allowed absolute pin, `delta_perp`, and final W-response rows;
- strict Schur/Feshbach pole packet with pole coordinate, `K'(pole)` or exact
  equivalent, source projection numerator, canonical bridge, model-class,
  FV/IR, and contact authority;
- strict neutral H3/H4 packet with physical neutral transfer/off-diagonal
  primitive authority and source/canonical-Higgs coupling.

## Claim Boundary

This block does not claim retained or `proposed_retained` top-Yukawa closure.
It does not define `y_t_bare`, use `H_unit`, `yt_ward_identity`, observed
targets, `alpha_LM`, package hierarchy `v`, fitted selectors, unit
normalizations, smoke rows, finite-shell diagnostics, chunks, or support-only
rows as load-bearing proof inputs.

## Verification

```bash
python3 -m py_compile scripts/frontier_yt_pr230_block120_source_reparam_invariant_minimal_data.py
python3 scripts/frontier_yt_pr230_block120_source_reparam_invariant_minimal_data.py
# SUMMARY: PASS=16 FAIL=0
```

## Exact Next Action

Create one strict packet rather than another source-only promotion gate:
action/canonical `O_H` plus physical source-Higgs pole rows; W/Z production
response with matched covariance and an allowed absolute pin; Schur/Feshbach
pole derivative rows; or neutral H3/H4 physical transfer with
source/canonical-Higgs coupling.
