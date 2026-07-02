# Review history — walls-attack-20260702

## block01 — supervisor line-by-line review (2026-07-02, pre-PR)

Worker draft reviewed against spec and sources. Findings:

1. **F1 (substantive, fixed).** D2(iv) table row claimed S1 "invariant" under
   U(2) channel mixing, but the runner only checked invariance of the TOTAL
   channel energy; the S1 equal-split condition itself moves under the same
   Hadamard witness ((1/sqrt(2),1/sqrt(2)) -> (1,0)). Repair: reframed the
   fourth discriminator as partition provenance (S1's partition is
   algebra-canonical: unit + HS-orthocomplement; S2 needs an imported per-mode
   basis; S3 needs a Y-dependent idempotent frame); added an explicit honesty
   witness section; added 3 runner checks (equal-split moves under H; H-mixed
   pair is not {unit, orthocomplement}) — PASS total 36 -> 39. D4 item 4
   restated as the NO-IMPORTED-FRAME requirement; residuals split into two
   named items (no-imported-frame; equal-channel-energy clause).
2. **F2 (verified, no change).** D2(ii) complement-swap use of the
   ACPHILAMBDA HW complement equivalence checked against the authority note:
   its stated theorem ("Record-registrable scalar readout ... takes the SAME
   value on the two readings") covers exactly the use made. Scope-faithful.
3. **F3 (verified, no change).** S3 algebra checked by hand:
   (1+2t)^2 = 2(1-t)^2 -> 2t^2+8t-1=0 -> t = -2 + (3/2)sqrt(2);
   r = t^2 = 17/2 - 6 sqrt(2); Q = 6 - 4 sqrt(2). Matches parent table.
4. **F4 (verified).** Runner re-run independently by supervisor:
   TOTAL: PASS=39 FAIL=0. Output cache regenerated from the supervisor run.
5. **F5 (grounding).** Collision scan: open codex bridge PRs #4762/#4760/#4771
   touch readout normal-form territory but none contains the scoring
   discriminator or the partition-provenance separation; #4209 (Tier-A
   proposal) is orthogonal governance. No same-lane collision.

Disposition: **pass-after-repair**. V1–V5 value-gate record staged in
OPPORTUNITY_QUEUE.md (V1 quotes the parent obstruction; V2 = separation
structure + conditional selection; V3 = complement-equivalence and circulant
surface are framework-specific; V4 non-trivial; V5 first cycle of campaign).
No negative claim is shipped (conditional selection + discriminator), so
N1–N8 does not gate this block; the honesty-witness section covers the
self-steelman anyway.

## block02 — supervisor line-by-line review (2026-07-02, pre-PR)

1. **F1 (style, fixed).** Worker over-applied the hedge instruction: the
   "witness-level decomposition" clause was prefixed to all six T4 sentences,
   burying content. Restructured T4 to state the hedge once + four clean
   clauses. No mathematical change.
2. **F2 (verified).** All four kappa-wall quotes grep-verified verbatim at
   source (2/1/1 hits). Block01 quotes are from the sibling note on this
   branch stack — dependency class disclosed in Load-Bearing Inputs.
3. **F3 (verified).** Runner re-run independently: TOTAL PASS=29 FAIL=0;
   output cache regenerated from supervisor run. T2 witness algebra checked
   by hand (I_w additivity for w=1,2 trivially exact; frame unchanged);
   T3 reuses block01's verified Hadamard identities.
4. **F4 (scope).** Note claims no kappa value, no supplier derivation, walls
   not identical — consistent with the kappa note's scope ("baseline alone")
   and with N-gate avoidance (no repo-level negative claim; T2/T3 are
   witness-level facts about constructed objects).

Disposition: **pass-after-repair** (style-only repair).
