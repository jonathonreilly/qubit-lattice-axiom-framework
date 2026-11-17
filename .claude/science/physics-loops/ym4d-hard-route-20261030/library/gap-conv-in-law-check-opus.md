# Check of row 1118 (gap-conv-in-law-astra): FINISH row 1121

Written by Claude Opus 5.5 (reasoning effort max), laptop Claude subagent.
Cross-provider check: the writer of row 1118 is gpt-6-astra max.
No mass gap is claimed here. A run may only guide or refute.

## Plan (save protocol: one step per response, appended below)

1. Read `library/gap-conv-in-law-astra.md` in full. Record its sections and numbered displays.
2. Read row 1099 Proposition SW (`library/gap-pinu-ev.md` L208-214) and its check (`library/gap-pinu-ev-check-opus.md` L176-185). Read row 691 Theorem W (`library/gap-ds-gauge.md` L79-101), row 1119 Lemma TS2 (`library/gap-resp-in-law-sheet.md`), and the `parts/gap.md` entries the note relies on.
3. Try to open the cited sources at the named pages (new empty scratch directory per download). Say if not possible.
4. Check line by line: 3.1 and (3.1)-(3.3); the entrywise refutation (3.4)-(3.7), the reverse-martingale step, the absolute-continuity bound for the resampled law.
5. Check the ring density (4.2), the infinite-volume ring DLR claim, the ownership bounds (4.1), the definitions (4.3)-(4.5) and (4.4) implies (4.5).
6. Check Theorem CONV-swap, parts A-E: the marked extension (4.7) and its ring marginal; whole-cluster exchange and partly exchanged unmarked factors; the random exchange region; the path count and the degree bound 5^d - 1; (4.9)-(4.12); the constant.
7. Check 4.4 (states covered, mixtures, local limits) and 5.2.
8. Value question: can H-swap hold at the window couplings for any l, or does the junction cost D_c of order beta l^(d-2) force p_c near 1? Compare with Dobrushin-type criteria and row 691 Theorem W. Smoothed exchange or other ownership?
9. Novelty relative to the lane and the cited sources.
10. Verdict table and one RESULT line.

## Step log

(Steps are appended below as they finish.)

### Step 1 result (reading)

Read `library/gap-conv-in-law-astra.md` in full (354 lines). Its structure:

- L1-11: repo search and credits. It credits row 1099 Proposition SW for the replica swap, and Adhikari-Cao for the exchange cancellation. It claims as new the integrated compact-cell hyperedge construction (4.2)-(4.7), the joint-tail condition and the infinite-state statement.
- 3.1, L42-83: first-order model of van Enter-Shlosman; (3.1) mean two-sample TV lower bound, (3.2) tail bound, (3.3) variance lower bound for the mixture.
- 3.2, L85-134: H-ent-local (3.4); reverse martingale (3.5); one-pin bound (3.6); differential version (3.7).
- 4.1, L138-150: credits and two elementary failures.
- 4.2, L152-200: ownership (4.1); ring density (4.2); ring DLR claim; swap quantities (4.3); H-swap (4.4); path-moment form (4.5).
- 4.3, L202-270: Theorem CONV-swap (4.6), proof parts A-E, displays (4.7)-(4.12).
- 4.4, L272-280: states covered, local limits, nonvacuity, scope.
- 5.1-5.3, L284-335: D_c and (5.1); H-sup on a full-measure set; hand tests.
- Step 6, L337-354: disposition and RESULT line.

### Step 2 result (reading)

- Row 1099, Proposition SW (`library/gap-pinu-ev.md` L208-214), and check 1100 (`library/gap-pinu-ev-check-opus.md` L176-185). Pair interactions b_e sigma.sigma'. With d = (sigma - sigma')/2, a swap bond opens with probability 1 - exp(-4 b_e (d_x.d_y)_+). An exchange of whole swap clusters preserves the joint law. The covariance is bounded by swap connectivity. Check 1100 redid it and found it HOLDS. Its guide run (zero field, torus, b = 2.5, L = 24) has swap bond density 0.836 and spanning swap clusters. That density is the mean of the single-bond swap defect. I use it in Step 8 as a guide number only.
- Row 691, Theorem W (`library/gap-ds-gauge.md` L79-101). Hypothesis (W) at (R, delta): for each boundary link z of the cube V_R, a worst case over pairs of boundary values that differ at z only. The coupled expected Hamming distance k_z must have sum per direction at most delta N_R, with delta below 1. Conclusion: exponential decay at rate ln(1/delta)/(2(R+2)), uniqueness, torus covariance bounds. It is a supremum-over-boundaries, one-link-change criterion.
- Row 1119, Lemma TS2 (`library/gap-resp-in-law-sheet.md` L192-196). (H-two) in total variation bounds every core-outside covariance by 4 eta. So (H-two) already contains one-scale core-ring mixing.
- Row 1018 section 2.3 (`library/gap-short-step-max.md` L105-131). Cells are the cubes x + {0, ..., l}^4, x in l Z^4. Rings are the cell boundary links. Plaquettes carry the weights w_p. The cells are independent given the rings.
- `parts/gap.md` L177 records row 1118 as unchecked. L174 records reading row 1116 (law-averaged criteria exist only for quenched disorder; Adhikari-Cao is the nearest two-sample example).
