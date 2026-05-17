# Block 20 Brief: yt_p2_taste_staircase_transport (Block 20)

**Date:** 2026-05-17
**Branch:** `physics-loop/yt-p2-taste-staircase-transport-block20-2026-05-17`
**Lane:** yt (distinct P2 taste-staircase sub-cluster)
**Target:** `yt_p2_taste_staircase_transport_note_2026-04-17` — desc=390, unaudited
**Outcome:** POSITIVE — Per-Rung Ward Distributional Invariance Theorem

## Status

POSITIVE CLOSURE. The block lands a **strengthening** of the parent
PARTIAL transport theorem: under any positive distribution of the
per-rung gauge dressing satisfying the joint endpoint constraint, the
Ward ratio is preserved on every rung at machine precision. The open
matching coefficient at v is invariant across the entire family.

## Deliverables

1. **Source note:** `docs/YT_P2_TASTE_STAIRCASE_DRESSING_DISTRIBUTION_INVARIANCE_THEOREM_NOTE_2026-05-17.md`
2. **Runner:** `scripts/frontier_yt_p2_taste_staircase_dressing_distribution_invariance.py`
3. **Runner cache:** `logs/runner-cache/frontier_yt_p2_taste_staircase_dressing_distribution_invariance.txt`
4. **Block artifacts:** this directory
5. **PR:** `[physics-loop] yt-p2-taste-staircase-transport-block20: POSITIVE — dressing-distribution invariance`

## Result

**Runner output: 10 PASS / 0 FAIL** (machine precision, 0.12s)

Verification arms:

- (i) **Per-rung Ward preservation across 10 distributions** —
  uniform geometric (parent), front-loaded, back-loaded, sinusoidal,
  3 random log-normal samples, harmonic, linear-decrease, step pattern.
  Max deviation = `5.55e-17` (machine precision).
- (ii) **CMT endpoint invariance** — `g_s^{(16)} = 1/u_0 = 1.139` at
  machine precision for every distribution.
- (iii) **Matching coefficient invariance** — `M = 1.973355388918` for
  every distribution; spread across family = `2.22e-16`.
- (iv) **Ward identity homogeneity** — `(y_t, g_s) -> lambda(y_t, g_s)`
  leaves ratio invariant for all lambda > 0.

Cross-check against parent runner: reproduces `g_s(mu_16) = 1.139`,
`y_t(mu_16) = 0.465`, `M = 1.9734` exactly.

## Hard rules adhered to

- A_min only (Cl(3) + Z^3 + retained theorems)
- Source-only PR (note + runner + cache + block artifacts)
- No atlas / harness / audit-data / README / lane-registry touches
- No main push, no merge

## Time

~75 min (under 90 min budget).
