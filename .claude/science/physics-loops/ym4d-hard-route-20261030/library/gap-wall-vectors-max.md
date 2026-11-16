lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-17T02:36Z

# gap-wall-vectors-max (row 1053): new attack vectors from the first-principles assumptions file

Worker: Claude Fable 5.2, max effort, Mac mini worker 2. One session. Pinned at commit a31c990cd on `claude/ym4d-hard-route`. Checked by no one. Research-stage working state; it grants no status.

Lease written from `date -u` = 2026-11-16T14:36Z plus 12 h.

## Plan (eight steps; one step per response; each result is appended before the next)

1. Read `library/gap-wall-assumptions-opus.md` (row 1052) in full. Record its top fifteen assumptions and every assumption whose "what if wrong" opens something.
2. Read `parts/gap.md` and `library/gap-direction3-max.md` (row 1051), only to avoid redoing work. Grep the lane for each candidate idea before naming it.
3. Task (1), (2): for each listed assumption, say whether dropping or replacing it gives a vector. For each vector: exact statement, consumer in a chain to the mass gap, change against the current route, source, cheapest kill test.
4. Task (3): kill fast with the tests on file (Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, compact U(1), frozen Q_8 and 2T, the five-dimensional test, Lemma CEN+, Lemma WN, the four-test spec check). A vector that renames an open statement is a FAIL.
5. Task (4): rank the survivors by change divided by cost to find out.
6. Task (5): for the top one or two, invent the mechanism, write the first lemma and try it by hand, or build the counterexample.
7. Task (6): literature lens on any new path.
8. Task (7): one complete brief per surviving vector for a proof row. RESULT line.

## Step log

(Each step appends below.)

### Step 1 result: what row 1052 hands over (read in full, L1-630)

Source: `library/gap-wall-assumptions-opus.md` (Claude Opus 5.5 high, row 1052, unchecked). I read all 630 lines. Nothing below is new mathematics; it is the list this row must answer.

**Its top fifteen (its ranking, L372-388):** 1 e1 (the gap is true); 2 f1 (no computer steps); 3 a2 (R^4, no compact direction); 4 c3 (seed plus scale transport); 5 c4 (order-one coupling is the hard regime); 6 e4 (asymptotic freedom holds non-perturbatively); 7 b2 (Wilson action); 8 c1 (existence before gap); 9 b3 (Euclidean); 10 a3 (gap on all of Omega-perp); 11 c7 (effective actions near-Wilson at the crossover); 12 e9 (infrared easy once strong); 13 b1 (lattice at all); 14 c2 (RG frame at all scales); 15 d2, d3, d9 (discard tests that rest on gapped models or on beliefs).

**Other assumptions whose "if wrong" entry opens something (its tables, L280-368):** b6 (periodic tori; twisted, free or Dirichlet walls), b8 (observables: a total set of smoothed bounded observables suffices), b10 (isotropic spacing; anisotropic limit), b11 (pure gauge; heavy or Higgs matter), b12 (SU(2) fields only; explicit Z_2 x SO(3) and pi_3 variables), b13 (one-loop trajectory; free irrelevant couplings), c8 (small-field / large-field split; a hard admissibility constraint), c9 (one tool), c10 (clustering apart from gap), c11 (seed by hand; parametric seed), e7 (Gribov as obstruction), e8 (instantons irrelevant), e10 (strong coupling is the only rigorous source), e12 (universality), d4, d8.

**Its 5.4 list, S1-S6 (what (W) adds to the Clay gap):** S1 bare Wilson on one trajectory; S2 uniform on every lattice of the sequence; S3 periodic tori with every flux sector; S4 partition functions only; S5 (BDD-Delta); S6 the gap leg waits for T0's (H2), (TOT).

**Its own results that this row may consume (all unchecked):** fact A2 (a uniform rate on a total set gives the gap and passes to limits); Lemma FLUX-W ((W) forces every electric flux energy of large periodic cubes above the gap); the scope correction (frozen Z_2, Q_8, 2T bind periodic-box statements only, since flat fields on simply connected regions are pure gauge); the target form T_JW-lat (L485).

**Its five "most likely wrong" (L621):** (1) periodic all-sector seed; (2) uniformity on every bare lattice; (3) Wilson's action; (4) existence before gap; (5) a seed carried by a doubling engine.

**Its routes Q1-Q9 (L536-546) and their state there:** Q1 simply connected one-box estimate (held by rows 1051, 1053: this row); Q2 dead (band again); Q3 action choice (no mechanism named); Q4 ordering only; Q5 deformation FAILS (same crux); Q6 blocked-equivalent ((LIOU)); Q7 relabel to T_JW-lat (reading); Q8 no consumer; Q9 no candidate.

What is left for this row: row 1052 named no mechanism for Q1 or Q3 and attacked neither. This row's job is to find vectors with a mechanism. Next: step 2 (read `parts/gap.md` and `library/gap-direction3-max.md`; grep before naming).
