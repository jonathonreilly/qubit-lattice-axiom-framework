# PR230 Block121 Schur Finite-Packet Pole-Derivative Nonidentifiability

Status: exact negative boundary / the complete finite Schur A/B/C packet does
not determine a strict Schur/Feshbach `K'(pole)` derivative.

## Scope

Block113 confirms a real complete `63/63` finite A/B/C inverse-block support
packet.  Blocks111 and 117 confirm that no strict Schur/Feshbach K-prime or
scalar-LSZ pole authority rows were emitted.  Block121 tests the remaining
promotion shortcut: whether exact finite A/B/C rows can fix the pole derivative
once a pole location is held fixed.

## Result

They cannot.  The runner constructs a finite-node vanishing perturbation:

```text
A_eps(x) = A_0(x) + eps (x - x_pole) prod_i (x - x_i)
```

with unchanged `B(x)` and `C(x)`.  At every finite row node `x_i`, and at the
declared pole `x_pole`, the perturbation vanishes.  Therefore all finite rows
and the pole location are unchanged.  But

```text
A_eps'(x_pole) = A_0'(x_pole) + eps prod_i (x_pole - x_i),
```

so `K'(pole)` and the source residue `Res C_ss = 1/K'(pole)` change.

The current packet is therefore bounded Schur support only.  It is not strict
pole-row authority, even though the finite inverse-block rows are complete and
schema-clean.

## Current Boundary

The Schur route remains open only if future work supplies one of:

- strict same-surface Schur/Feshbach pole rows with pole coordinate, `K'(pole)`
  or exact equivalent, source projection numerator, FV/IR/contact authority,
  and canonical bridge;
- an analytic/model-class theorem that fixes the pole derivative from the
  finite packet, with uncertainty and FV/IR/contact controls;
- a separate physical source-Higgs or W/Z route that supplies the canonical
  bridge and absolute readout.

## Claim Boundary

This block does not claim retained or `proposed_retained` top-Yukawa closure.
It does not turn finite A/B/C rows into pole rows, relabel `C_sx/C_xx` as
physical `C_sH/C_HH`, identify the taste-radial source with canonical `O_H`,
or use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed targets, `alpha_LM`,
plaquette, `u0`, or unit settings for `kappa_s`, `c2`, or `Z_match`.

## Verification

```bash
python3 -m py_compile scripts/frontier_yt_pr230_block121_schur_finite_packet_pole_derivative_nonidentifiability.py
python3 scripts/frontier_yt_pr230_block121_schur_finite_packet_pole_derivative_nonidentifiability.py
# SUMMARY: PASS=10 FAIL=0
```

## Exact Next Action

Do not extend finite A/B/C shells as if more finite rows could become
`K'(pole)` authority.  The next Schur-positive artifact must be a strict
pole-row packet or a certified analytic/model-class theorem fixing the pole
derivative, together with FV/IR/contact authority and a canonical `O_H`/source
bridge or W/Z physical-response bypass.
