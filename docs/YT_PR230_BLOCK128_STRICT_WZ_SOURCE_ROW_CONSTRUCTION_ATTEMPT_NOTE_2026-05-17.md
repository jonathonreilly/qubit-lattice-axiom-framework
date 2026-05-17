# PR230 Block128 Strict W/Z Source-Row Construction Attempt

Status: exact negative boundary / existing raw rows do not construct a strict
W/Z packet, and the source-Higgs pole-row fallback is still blocked by missing
accepted `O_H`/action authority plus missing pole residues.

## Scope

Block128 starts from the Block126/127 state rather than reopening a broad
inventory.  It asks whether the existing raw rows can supply the strict
positive disjunct now needed for PR230:

- W/Z production mass-fit rows matchable to the 1008 Block126 top-side
  configuration keys;
- strict non-observed `g2`;
- accepted same-source EW/Higgs action;
- matched top-W/Z covariance;
- or, on the source-Higgs pivot, accepted canonical `O_H`/action authority
  with nonempty numeric `C_ss/C_sH/C_HH` pole-residue rows.

## Result

The runner checks the Block126 raw production surface directly.  All 63 raw
files are present and carry the 1008 scalar/top configuration-slope rows used
by Block126, but their W/Z surface is only a disabled stub:
`wz_like_raw_file_count=0` and `disabled_wz_stub_file_count=63`.

The only W/Z-shaped row artifact remains the known smoke schema.  It fails the
strict join because it is `phase=scout`, uses synthetic contract correlators,
has no configuration keys matchable to Block126, has only three aggregate
source-shift rows, and has no matched covariance, strict `g2`, or identity
certificates.

The source-Higgs fallback is also not strict on the current surface.  The raw
two-source taste-radial files contain 252 finite `C_ss/C_sx/C_xx` rows, and
Block124's assembled support packet contains 693 finite rows, but the strict
pole-residue count is zero.  The 18 polefit8x8 raw files provide `C_ss`
support rows only, not `C_sH/C_HH` pole rows.  The canonical action/O_H closure
certificate still records the accepted same-surface primitive as absent.

## Claim Boundary

This block does not claim `proposed_retained` closure.  It does not use
observed W/Z, observed `g2`, observed top/Yukawa targets, package hierarchy
`v`, `alpha_LM`, plaquette, `u0`, `H_unit`, `yt_ward_identity`, `y_t_bare`,
smoke rows, finite chunks, or assumed top-W/Z factorization as closure input.

Actual current surface status: exact negative boundary.

Conditional surface status: null.

Hypothetical axiom status: null.

Admitted observation status: null.

Proposal allowed: false.

## Exact Next Action

Do not spend another block on W/Z row inventory unless a new production W/Z
mass-fit artifact appears.  Pivot to strict Schur/Feshbach pole authority or
neutral H3/H4 physical-transfer/source-coupling authority.  Reopen the
source-Higgs route only with accepted canonical `O_H`/action plus nonempty
numeric `C_ss/C_sH/C_HH` pole-residue rows.
