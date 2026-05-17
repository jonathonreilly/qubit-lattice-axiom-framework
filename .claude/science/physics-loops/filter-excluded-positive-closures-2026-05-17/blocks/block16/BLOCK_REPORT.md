# Block 16 Report — s3-time bilinear tensor primitive rank-1 factorization

**Branch:** `physics-loop/s3-time-bilinear-tensor-primitive-block16-2026-05-17`
**Target row:** `s3_time_bilinear_tensor_primitive_note` (482 desc, unaudited)
**Status delivered:** scope-bounded positive narrow theorem
(`positive_theorem`, class-A polynomial-identity arithmetic) on the
*internal algebraic structure* of the bilinear carrier symbol `K_R`.
Parent `open_gate` **not** closed; three named upstream gaps remain.

## What landed

1. **Source theorem note:**
   `docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_RANK1_FACTORIZATION_NOTE_2026-05-17.md`
   Positive narrow theorem: under the named admitted inputs of the
   parent definition note, the symbolic carrier `K_R(q)` factors
   algebraically as the rank-1 outer product
   `K_R(q) = (1, delta_A1(q))^T (u_E(q), u_T(q))`, and five structural
   properties (R1)-(R5) follow by polynomial identity.

2. **Paired runner:**
   `scripts/frontier_s3_time_bilinear_tensor_primitive_rank1_factorization.py`
   `PASS=11 FAIL=0`. Verifies the factorization identity and all five
   structural properties at machine precision on a 138-sample grid
   (canonical A1 family at 6 r-values x bright/dark/mixed perturbations
   at multiple amplitudes). Worst residual ~ 5.6e-17.

3. **Cached output:**
   `logs/runner-cache/frontier_s3_time_bilinear_tensor_primitive_rank1_factorization.txt`

4. **Block artifacts** (this directory):
   - `V1_V5_SCRATCH.md` — distinct-angle scratch (V1-V4 rejected, V5 chosen)
   - `BLOCK_REPORT.md` — this file

## V1-V5 chosen angle

- V1-V4 rejected: each would either attempt to close one of the three
  named upstream gaps (decoupling, aligned-bright identification, GR
  bridge — all forbidden under A_min without new primitives) or
  re-state the block 12 angle (sharpening the bounded readout).
- **V5 (chosen):** prove the rank-1 outer-product factorization of the
  carrier symbol itself, with five structural properties (R1)-(R5):
  rank-1 universality, determinant vanishing, row/column proportionality,
  channel separation of partial derivatives, singular-value collapse and
  factor separation.

## Distinct sub-problem (block-lane independence)

This block is on the **internal algebraic structure of the carrier `K_R`
itself**, distinct from:
- Block 02 (AC_phi_lambda C3-foreclosure): different downstream object.
- Block 07 (background uniqueness + Hessian no-go): different scope.
- Block 12 (`Xi_P = (P_R c) ⊗ V_R(t)` factor rigidity): downstream
  coupling family, factoring time vs. space; this block factors *within*
  the carrier between the scaling channel `w(q) = (1, delta_A1)^T` and
  the bright channel `v(q) = (u_E, u_T)^T`.

## Hard rules compliance

- A_min only: all ingredients (`delta_A1`, `u_E`, `u_T`, basis vectors)
  imported from cited audited authorities
  (`frontier_tensor_support_center_excess_law.py` from
  `TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE` retained_bounded,
  `frontier_same_source_metric_ansatz_scan.py` for the adapted basis).
  No new primitives.
- Source-only PR: theorem note + runner + cache + block artifacts only.
- No CANONICAL_HARNESS_INDEX, DERIVATION_ATLAS, DERIVATION_VALIDATION_MAP,
  audit-data, README, or lane-registry touches.
- No main push, no merge.

## Honest scope

- Parent row `s3_time_bilinear_tensor_primitive_note` remains `open_gate`.
- The three named upstream gaps remain explicitly open:
  (1) retained derivation of the `delta_A1`-decoupling fact;
  (2) retained derivation of the aligned-bright coordinate identification;
  (3) retained bridge theorem identifying `K_R` with a physical tensor
      primitive in the GR readout chain.
- The positive narrow theorem sharpens the picture from "definition only"
  to "definition with a derived rank-1 outer-product structure", but does
  NOT promote the parent row.
- R4 (channel separation) uses the admitted decoupling fact and is
  verified on the same finite grid as the parent runner's existing
  class-D shadow. The verification does not promote (1) beyond its
  current status; it inherits the same finite-grid status.

## SUMMARY (from runner)

```
PASS=11 FAIL=0 TOTAL=11
```

Worst residual across all 11 checks: 5.55e-17 (R4 partial-derivative
identities at amplitude 0.25). All other checks closer to 1e-16 or below.

## Verification command

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_time_bilinear_tensor_primitive_rank1_factorization.py
```

Expected: `PASS=11 FAIL=0`.
