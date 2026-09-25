# Block 111 — control and findings (2026-09-24)

1. **Provenance.** The probes attempt do-records-fall-with-a-universal-weight a1 (Claude Opus 5.5) derived the results, and a Grok referee (j17d3) confirmed them. The supervisor re-checked them with its own runner code.
2. **Fixes before shipping.**
   - A table was overwritten by the second gradient direction; values are now stored per direction.
   - A positivity test was undecidable symbolically; it is now zero at g = 0 with a positive derivative.
   - Classical names were moved out of the front matter and N3.
3. **Prior art placed.** Blocks 95 (T1, T3 as landed), 97, 99, 39 and 40. The drift–diffusion relation (Einstein–Smoluchowski) is named as a comparator.
