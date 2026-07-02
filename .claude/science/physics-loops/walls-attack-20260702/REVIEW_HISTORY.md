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
