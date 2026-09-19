# Refuting pass — block 25 (supervisor-run, disjoint machinery; 2026-09-16)

Routes compared (controls `specs/supervisor_control_block25_toom_core.py` and `specs/supervisor_control_block25_toom_stability.py`, refuting pass `specs/supervisor_control_block25_refuter.py`, outputs in `.out.txt`):

| item | runner's route | refuting route | result |
|---|---|---|---|
| the spanning lemma (T3) | asserted at every refinement of the automaton's explanation trees | 169 random abstract systems (random points of a level plane, random clusters, all cross-cluster sibling forks, random poles), the lemma's construction re-implemented from scratch, the identity checked with exact rationals | holds in every instance |
| the noise map (T0) | exact maximum over the `216` triples at integer weights | direct floating-point enumeration at 200 random real weights against the three closed forms | agrees to `4·10^{−16}` |
| the explanation tree (T4) | the embedded construction with its own tree check | an independent graph implementation (numpy predecessor and sibling tests) on 363 explained random cones of depth `3`–`7`: arrows and forks of `G`, one-sites only, marked nodes are noise sites, tree, `edges ≤ 4(n − 1)` | passes throughout |
| the series constant (T6) | the symbolic identity and the exact partial sums | direct summation of `Σ_{k≤K} 2·96^k/96^K` for `K ≤ 40`; the bound at `ε_0` in floats | `2.021052632 = 192/95`; `2.379538·10^{−8} = 1/42024960` |
| stability (T6, physics sanity) | — | the noisy automaton on a periodic `96×96` level plane from all-zero for 300 levels | final densities `0.011, 0.021, 0.033, 0.064` at `ε = 0.01, 0.02, 0.03, 0.05` and `1.000` at `ε = 0.08` |

Findings: one, before the contract, folded. The first draft of the construction made two forks sharing a point adjacent in the cause graph's search; the minimal tree then skipped the cluster between them, two noise sites were never counted, and the very first depth-2 configuration (four noise sites at level `−2`) gave `5` edges for `2` counted noise nodes. The cause graph must alternate clusters and forks (T3's bipartite hypothesis); with that, every configuration tested passes, and the observation is recorded in the note's Review record and Prior art.

Attempts to refute (nothing else refuted): a cluster added twice to the tree (impossible: a cluster's parents all lie in one cluster, by the definition of clusters through the past); a processed point receiving two arrows (one arrow per kept point, the least charge); a fork added twice (one fork per adjacent cluster pair, only in the parent's refinement); the marked nodes coinciding as sites (a subtree's nodes are distinct points); whether `n = 1` trees exist with edges (`x` itself a noise site: the one-node tree); the count's overlap of *up* arrows (the encoding allows any of the `12` incident edges at each step, so the direction of traversal is covered); the Cesàro limit's invariance (the kernel is a finite product at each cylinder, hence Feller); the distinctness at `δ = 1/42024960`. Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.

## Sharpening pass (2026-09-16, after the PR opened; `specs/supervisor_control_block25_sharpening.py`, `specs/supervisor_control_block25_sharpening_refuter.py`)

| item | control's route | refuting route | result |
|---|---|---|---|
| the refined T4 (one arrow to a predecessor per node; marks = nodes without one; `forks = n − 1`; `arrows ≤ 3(n − 1)`) | checked on `4308` explained trees (exhaustive depth-2 and depth-3 cases plus `1500` random cones); max `arrows/(n − 1) = 12/7` | — (the runner checks the same facts on its own `D1–D3` cases) | holds throughout |
| the candidate lemma "every arrow points away from the root" | counted on the same trees | an independent BFS recount on the exhaustive cases | **refuted**: `538` of `4308`; `32` of `3253` exhaustive — a kept pole is reached from below through its own arrow via the fork tree beneath; the count keeps six arrow letters |
| the tree count (T5) | `66103` subtrees of `G` with `≤ 4` edges, lifts pairwise distinct, each `(a, f)` count `≤` the recursion's coefficient; direct enumeration of admissible subtrees of the typed tree agrees for `≤ 3` edges | the crude binomial split `Σ_{a≤3f} C(a+f, a) 24^{a+f} ≤ (24/23)(96⁴/27)^f` as a second valid bound (threshold `1/6291456`) | consistent; the recursion's threshold is `44` times the split's |
| the certificate (T5–T6) | exact rational super-solution at `(91/1000, 1000/107653)`, slacks `10^{−5}`, `R̄ = 3.9073 < 3.91`, `ε_0 R̄ = 2.74·10^{−5} ≤ 3·10^{−5}` | the recursion iterated in floating point from `(1,1,1)`: fixed point `(3.290875, 2.058161, 3.774866)` below the certificate; the iteration diverges at `1.06 s` and is bounded at `1.03 s` | consistent; the certificate sits within `6 %` of the edge of the domain for this accounting |
| the bound at `ε_0` (T6) | `(391/100)ε` | the Peierls partial sum over the `64490` family trees with `≤ 4` edges at `ε_0`: `6.6·10^{−7}`; a `300×300` simulation at `ε = 7·10^{−6}` for `400` levels: density `8.3·10^{−6}` | both below `2.74·10^{−5}`; the bound is within a factor four of the simulated density at `ε_0` |
| the thresholds `p_0` (T7) | exact bisection at four weight pairs (`285718`, `142861`, `571436`, `428576`) | — | each with `ε(p_0 − 1) > ε_0` |

Finding: one, folded before the note was changed — the direction lemma above. Nothing else refuted. Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.
