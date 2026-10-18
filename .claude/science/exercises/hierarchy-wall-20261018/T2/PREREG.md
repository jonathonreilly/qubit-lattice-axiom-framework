# T-LIGHTCONE pre-registration

Written 2026-10-18 between 18:39Z and 18:41Z, before any simulation, code or run in this folder (first timing run 18:41:19Z).
Readings are the ones fixed in ../TESTS.md (T-LIGHTCONE); nothing here changes them.
Same-family worker (Opus 5.5), unrefereed.

## Model (landed, as written)
Source: origin/main 584755767d, `docs/ADMISSIBILITY_RULE_LIGHT_CONE_FORMATION_KEEPS_MEMORY_IN_3PLUS1_..._BETA_0P5905_BOUNDED_THEOREM_NOTE_2026-09-23.md` (T1–T3), with its parent 09-20 note.
- Torus of even side L, contents s_x on the unit sphere S^2 with uniform base measure.
- Level update (the landed kernel): every site of the new level draws s'_x with density proportional to exp(beta s'_x . h_x), h_x = sum over d in N7 = {0, +-e_j} of s_{x+d} (previous level).
- Stationary pair law (T1): proportional to exp(beta sum_x sum_{d in N7} s'_x . s_{x+d}), the ferromagnetic O(3) model on the doubled graph (degree 7). T2 maps it to two cubic slabs with one rung per site.
- I simulate the doubled graph directly, not the relabelled bilayer, so T2 is not used as an input.
- beta is the only coupling. It is a free input of the landed model; no note fixes it.

## Symmetry statement (to be argued in the report, not simulated)
The kernel is invariant under one global O(3) acting on all contents, independently of the lattice. Any perturbation that breaks global O(3), such as a cubic spin anisotropy locked to the lattice axes, has coefficient exactly 0 in this model. Such directions are reported separately as outside the model, with their status labelled; they do not count toward any reading.

## Methods
**M0, model check.** At L = 8 and two couplings (beta = 0.50, 0.60), run the landed kernel tick by tick (exact von Mises–Fisher draws) and compare one level's <|m|^2> with the cluster sampler of M1. Pass: agreement within 3 combined sigma. If M0 fails, M1/M2 results are not used.

**M1, finite-size scaling.** Wolff single-cluster updates on the doubled graph. L in {8, 12, 16, 24, 32} (40 if time allows). Observables: m = (sum of all 2N contents)/(2N); Binder ratio R = <|m|^4>/<|m|^2>^2; second-moment correlation length xi_2 from the lowest torus momentum, ratio xi_2/L; chi = 2N <|m|^2>. Beta derivatives via covariance with the bond sum; single-histogram reweighting.
- beta_c: from the crossings of R and of xi_2/L for pairs (L, 2L) and (L, 1.5L). Extrapolate as beta_x(L) = beta_c + c L^(-(omega + y_t)).
- y_t: y_t(L) = log[Q'(sL)/Q'(L)]/log s at the crossing, for Q = R and Q = xi_2/L.
- y_h: (3 + log[chi(sL)/chi(L)]/log s)/2 at the crossing.
- omega (leading irrelevant, y = -omega): fit Q(L) at beta_c = Q* + a L^(-omega), and the crossing drift.

**M2, Monte Carlo RG (Swendsen linearised map).** Block b = 2: one block takes a 2x2x2 cube of sites on both levels (16 contents) to the normalised sum. After the first step the lattice is simple cubic, so the map is linearised between blocked levels n >= 1, where both have the same operator set. Run at the M1 estimate of beta_c with L = 32 and L = 16.
- Even sector (6 O(3)-invariant operators): nearest neighbour s.s; face diagonal; body diagonal; distance-2 axis; (s.s)^2 on nearest neighbours; nearest-neighbour plaquette (s1.s2)(s3.s4).
- Odd sector (3 vector operators): s; s (s.h_nn); s (s.h_face).
- T = C(n+1, n+1)^(-1) C(n+1, n), y = ln(lambda)/ln 2. Truncations 1..6 (even) and 1..3 (odd). Jackknife errors (20 bins).
- Matching check: L = 32 step 2->3 against L = 16 step 1->2 (both end on 4^3); L = 32 step 1->2 ends on 8^3.

**M3, level-time direction (secondary, "report also").** Autocorrelation time of |m|^2 under the landed kernel at the M1 beta_c, L = 8, 12, 16, to estimate the dynamic exponent z. It is reported, not used in a reading.

## Decision rules (map to the fixed readings)
- **Complex pair counts** only if, for the same pair: Im y differs from 0 by more than 3 jackknife sigma; it appears in at least 4 of the 6 even truncations (or 2 of 3 odd ones); and it appears in both matchings. Otherwise it is a truncation artefact and is listed as such.
- **LC-SPIRAL** if a counting pair has |Re y| <= 0.06 and |Im y| >= 1.
- **LC-MARGINAL** if a symmetry-allowed direction has |y| < 0.1 in both M1 (if accessible) and M2 at both matchings. Then report the sign of the first nonlinear coefficient if it can be measured, the bound u0 <= 1/(b . 38.4), and whether the model fixes u0.
- **LC-HYPERBOLIC** if every measured eigenvalue is real and has |y| >= 0.2: y_t, y_h and the leading irrelevant from M1, and all stable M2 eigenvalues. Then report the required distance delta <= exp(-38.4 y_t) and the fact that beta is supplied.
- **OPEN** otherwise. This includes the case where the leading irrelevant exponent cannot be separated from 0.2 within errors.
- Reference values from the 3D O(3) literature (comparator only, not a pass condition): y_t ≈ 1.41, y_h ≈ 2.48, omega ≈ 0.76. If M1 disagrees with them by more than 5 sigma, the model or the code is suspect, and that is reported, not hidden.

## Budget
One process at a time, `zsh scripts/capped.sh OUT ...`, 0.4 GB cap. Simulation code in C (clang -O2), analysis in Python. Total simulation time at most 60 min. Everything killed before the report. Deadline 20:35Z.

## Addendum, 2026-10-18T18:59Z (dated; written after stage-1 data and the L = 48 run had been analysed)
These additions do not change the readings or the decision rules above.
- **omega estimator added.** The joint fit (omega.py) was degenerate for L <= 32. I added R at fixed xi_2/L = Z, for Z in {0.565, 0.570, 0.575} (rbar.py). Each size is an independent run, so chi2 is meaningful. I fit omega free and with omega fixed at 0.2.
- **More statistics.** Stage 3 adds independent runs at L = 48 (30k) and L = 64 (15k) at the same beta = 0.5561.
- **Stability of real M2 eigenvalues (definition, made explicit).** The pre-registered 4^3 matching shows sign-flipping eigenvalues once the distance-2 operator enters. On a 4^3 torus, x + 2e and x − 2e are the same site. So "stable" now means: within 3 sigma across final lattices of 8^3 or larger, and across at least 4 truncations. The 4^3 and 6^3 results are reported, not hidden.

## Addendum 2, 2026-10-18T19:39Z (dated; after seeing the L = 64 MCRG)
In the second L = 64 run, the eigenvalue that enters with the distance-2 operator is y = −0.09(5) at step 2->3 (final 8^3). The first run gives −0.20(8). At fixed step it moves away from 0 as the final lattice grows. I add one L = 128 run (1,800 measurements, MCRG 4 levels) to test that: step 2->3 then ends on 16^3. This is a check only; the readings and the counting rules are unchanged.
