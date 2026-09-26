# Referee: deferred-20260925-band-gauge a1

Attempt `w-jonathonsmac4f50-j7516`. The carvings and the inertia certificates are rebuilt here. The attempt's script is not imported.

N20 and N16 are the stated 20-site and 16-site subsets of the 4×4×4 torus. Compass bonds have strength 1. A record outside the carving is `(1, √2, √3)`, with a constrained axis zeroed and then normalised. Each dangling field is the sum of its two record contributions. The auxiliary matrix has bond entries `−2u e^{ik·off}` and field entries `±2h`. A translation-invariant sector sets `u = 1` on a spanning tree and `u = ±1` on the remaining bonds.

## Verdicts

**Structure.** Every nonzero entry joins the even-site side to the odd-site side. The two sides have equal size. The support of the off-diagonal block has maximum matchings 16 and 12, so N20 has at least two zero energies and N16 at least four, at every momentum. The quotient graphs have cycle ranks 4 and 3.

**Gauge and interlacing.** For each sector a spanning tree moves every momentum-dependent phase onto three winding bonds. Deleting one row or column through each of those bonds leaves a momentum-independent submatrix. Its ordered singular values are lower bounds for those of the full block. Square roots are bracketed by integer square roots at scale `10^40`, and the entry error is carried into the threshold.

**Lower bounds.** The exact inertia of `M′ᵀM′ − c²I` certifies, in all 16 sectors of N20, `|E| ≥ 0.6079` for eight sectors and `|E| ≥ 0.7858` for the other eight, for every momentum. All eight sectors of N16 satisfy `|E| ≥ 1.4333`. Together with the matching bound, the zero-band counts are exactly two and four.

**Upper bounds.** At `π(1,0,1)`, `π(0,1,1)` and `π(1,1,1)` a rational test space gives `|E| ≤ 0.6179`, `0.7959` and `1.4368` in the stated sectors. The floating values are `0.617873`, `0.795865` and `1.436791`.

**Lift.** The listed 28 sites of the N16 lift form a simple cycle of nearest neighbours, so the lift is not a tree.

## What stays open

Non-periodic gauge fields, the physical projection `D_j = 1`, and a certified minimum inside the enclosure were not treated.

## Result

HIT: confirmed. In every translation-invariant gauge sector, N20 has exactly two zero bands and every other energy at least `0.6079` or `0.7858`, and N16 has exactly four zero bands and every other energy at least `1.4333`.
