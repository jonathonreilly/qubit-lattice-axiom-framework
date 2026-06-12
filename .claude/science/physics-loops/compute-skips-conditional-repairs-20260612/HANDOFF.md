# Handoff

This PR is ready for reviewer extraction.

What changed:

- Higgs-channel effective `N_taste` now uses the current parent
  `u_0 = 0.877681381`, updates the rounded `k=1,3` display values from
  `280.6` to `280.5`, and refreshes the cache.
- Wilson-corrected `V_taste` no longer has stale source comments asserting
  `+40 r^2/u_0^4`; the runner still includes `40` as a negative-control
  comparison and verifies the correct `60` coefficient.
- Observable-principle Shannon/Khinchin bridge now states the exact-additive
  Cauchy conclusion as `W=c log r`, adds a runner guard that an offset `b`
  violates exact additivity unless `b=0`, and updates labels/expected count.

Checked but not changed:

- The historical compute-required rows for asymmetry/wave and the beta6
  maxorder-7 source packet already have completed current source/cache evidence
  in this checkout. This branch leaves those source packets unchanged.

Independent audit/review is still required.
