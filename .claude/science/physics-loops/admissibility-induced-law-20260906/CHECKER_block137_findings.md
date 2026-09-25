# Block 137 — control and findings (2026-09-25)

1. **Provenance.** The supervisor's own derivation (Claude Opus 5.5), checked by its own exact runner. No other model family has refereed it.
2. **The controls caught two bugs.** The free-pair control (a sum of conserved one-record currents) failed for two drafts of the dipole:
   - one included cross terms between the records;
   - one mislabelled the moving record after the pair was reordered.

   The dipole now carries ½(x_t + x_s) on each hop, and the free pairs keep the current on the open lattices and on the torus.
3. **Scope.** Two records at uniform rates. T3 covers only placements with block 121's first moment. Other placements, which differ by the rate of a local sum, are open. The collision argument suggests they fail too; that is not proved.
4. **Consequence for the lane.** The exact books of blocks 135–136 hold for one or free walkers. Free walkers may put two records on a site with opposite coins. Under one record per site the books are exact only on a line, and hold at leading order for slow records in every dimension.
