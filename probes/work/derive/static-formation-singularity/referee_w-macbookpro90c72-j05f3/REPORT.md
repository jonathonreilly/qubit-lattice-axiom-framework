# Referee: static-formation-singularity a2

Worker `w-macbookpro90c72-j05f3` (`grok-4.6`). Author `w-macbookpro90c72-j252c` (`claude-opus-5-5`). The attempt's script is not imported. The 2×3 strategies are the attempt's witness; their normalisations, total variations and Bellman value were recomputed.

## Verdict

Confirmed. At the class-(P) weights `(3,1,2)`, the total variation from the static law to the closed convex hull of adapted formation laws is exact on the `2×2` and the `2×3`, and the corner-order laws on the strips and the tube are singular to it.

## What was checked

- **Constants.** `Nf(∅) = 6`, `Nf(one) = 12`, pair values `26/24/22`, and the triple and quadruple ranges.
- **Plaquette.** `Z = 20784`. Every one of the 24 orders has `ν = W/Y`. The minimum total variation is `455/31176` and the maximum is `37/1299`. The diagonal event `E` has `μ(E) = 521/1732` and both corner laws equal `1619/5616`. The corner mixture attains `TV = 30457/2431728`, and the Bellman recursion gives the same supremum, so that is the distance to the whole adapted hull.
- **Disjoint copies.** The binomial total variation is at least `1/2` at `m = 2410` (`k = 710`) and not at `m = 2409`. The Bhattacharyya bound gives total variation below `1/2` through `m = 952`, so the threshold lies in `[953, 2410]`. `1 − β ≥ 9.43777·10⁻⁵`.
- **Strips and tube.** A path has `r2 = 1` and `K = 1`. The certificates give `1 − r2` at least `6.05795792·10⁻⁴`, `1.245343112·10⁻³` and `3.511679839·10⁻³`, and total variation at least `1/2` against the monotone hull from `L = 4624, 2272, 1019`.
- **Cube.** One corner law has total variation `1182193085/23402354976`. The uniform mixture of the eight corners, which is the closest point of the monotone hull, has `3205622113713065/81441318629518848`.
- **Ladder.** The four-corner mixture is at `812090431/41067000000`, and no fixed order puts more mass on that event. The witness mixture of 19 value-dependent strategies and the Bellman test meet at `4120449306433/238517136000000`, strictly below the fixed-order value.
- **Envelope.** On the `2×2` the pointwise bound is `2555/810576`, strictly weaker than the hull distance.

The half-infinite singularity is the Borel–Cantelli argument from these geometric bounds. The full adapted hull on a long connected strip remains open, as the attempt says: the envelope decays.
