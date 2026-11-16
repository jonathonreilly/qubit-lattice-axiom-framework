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

### Step 2 result: what the lane already holds (read only to avoid redoing work)

Read in full: `parts/gap.md` (257 lines) and `library/gap-direction3-max.md` (283 lines at this pin; it stops after its Section 4.2, so its Section 5 is not visible to me). Read in part, for idea titles only: `library/gap-next3-max.md` L255-300 (the inventory of rows 859, 876, 878, 899, 900) and `library/gap-global-reform-max.md` L506-605 (row 1016, candidates (GF), (HAM), (CMP)).

**What binds this row (from those files).**

- The wall is (W) on periodic tori. Every route ends at one selective inequality at order-one coupling (`parts/gap.md` L41-46, L256-257).
- The lane's idea lists are long: row 859 (52 ideas), row 876 (60), row 878, row 1004 (I1-I14), row 1013 (C1-C9), row 1016 (ten reformulations), rows 1031-1032 (A1-A10, B1-B15). A vector counts as new here only if its crux lemma is none of these.
- Row 1051 holds the port of OpenAI's one-annulus engine to the pin space of a gauge cell (its Section 3, last paragraph), and the "blind half" of every stiffness line (its 4.2). Rule 0a: I do not attack those.
- Route W (free-wall boxes, no flux sector) is on file (rows 858, 900; `gap-next3-max.md` C1). So row 1052's Q1 is found again in form; what Q1 lacks is a mechanism for the one-box estimate.

**Grep of the lane for my first candidate list (two wordings each; scope `library/` and `parts/` of this folder; counts are files).**

| Candidate | Grep words | Files | Verdict |
|---|---|---|---|
| Durhuus-Frohlich slab comparison, with the posted 2D O(4) gap as input | Durhuus; layer comparison | 29 | found again: rows 825-857 (area law below 2/3), `gap-brainstorm2-max.md` G8 (3D through the slab), row 1016 4.6 (FAILS in d = 4: the layer is 3D and orders) |
| Hyperbolic space or a sphere as infrared regulator | hyperbolic space; Callan; four-sphere | 12, 7 | found again: row 859 idea 42 (dropped), row 1004 I8 (FAILS) |
| Free-wall or simply connected boxes | free wall; Route W | many | found again: rows 858, 900, 910 |
| Transverse lattice as a gauge fixing with a rigid two-dimensional group | transverse lattice; Bardeen | 4, 1 | found again: row 1016 4.4, FAILS (Elitzur) |
| 1+3 anisotropy (path in beta_t from 0; beta_s = 0) | beta_t path; anisotropic | 64 | found again: rows 988, 992 (needs 3D mixing and (NOCRIT)); row 859 "anisotropic action from beta_s = 0" |
| Defect-angle class function (frame-averaged non-central twist) | defect-angle; w_phi | on file | found again: row 859 |
| Orbit-space curvature; Gribov region as a convex domain | Singer; Faddeev-Popov | 15 | found again: exercise 4 input 10; row 1032 B8 (not selective) |
| Twist free energy as a running coupling; gradient-flow transport | step-scaling; gradient-flow | on file | found again: row 859 |
| Z_2 x SO(3) variables, Nishimori line, planted Z_2 | SO(3) x Z_2; Nishimori | 38 | found again: rows 859, 876; K7 note in FINISH |
| Trace anomaly, low-energy theorems, a-theorem | trace anomaly; Komargodski | 14, 10 | found again: row 859 (exact scale identity), row 1031 (VIR) |
| **2+2 anisotropy: the point beta_long = infinity, beta_trans = 0, where the model is a product of 2D O(4) models** | 2+2; beta_perp; decoupled/independent chiral; product of chiral | 0 | **not found** (the transverse-lattice picture is on file only as a gauge fixing) |
| **Inverse order: fix the infrared measure first and refine (projective family)** | to be searched in step 3 | - | pending |

Next: step 3. For each top-fifteen assumption and each opener, a vector or "no vector", with the grep that backs each "found again".
