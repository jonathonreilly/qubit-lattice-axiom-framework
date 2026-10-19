# C3b worklog

- 2026-10-19 start. Read SCIENCE_WORKFLOW §2, no-go-discipline SKILL, C3 NOTE/REVIEW.
- Plan: (1) reduce record to a factor of (orientation field, marks) when ancestries are finite;
  (2) internal-symmetry no-SSB bound via ancestry overlap, valid for ANY clock law;
  (3) finite-ancestry theorem for clocks with non-interpolable local randomness (volume argument) -> covers (b),(c)+noise;
  (4) bounded-rate theorem with lambda_min=0 / history dependence (time-cutoff chain count) -> covers (a);
  (5) numerics with FSS for (a) KJMA, (b) fractional Gaussian clocks, (c) Voronoi two-stage level clocks (2D/3D, Toom-type majority rule).
- Observation recorded before numerics: literal question ("ergodic clock") is answered YES trivially by a
  checkerboard clock (ergodic, O_h-covariant, non-mixing): record copies the clock's crystal order. The real question is
  mixing clocks / internal symmetry breaking.
- s2 first run: sanity test s2.0 was MIS-SPECIFIED (I expected iid colours at eps->inf; wrong: order becomes iid but majority copying persists). Replaced by a cross-implementation comparison with the iid-clock model. Other s2 results unchanged in design.
- s4 first run (ns as low as 6 at the largest L) gave chi_L error bars too large to be informative at ell=12; rerun with ns>=24 (log overwritten; first-run numbers: xi/ell ~0.35, 0.31; all 5 checks passed).
- s4 rerun complete (5 PASS). NOTE drafted. Launching run_all.sh for the final aggregated log.
- run_all.sh final: TOTAL: PASS=50 FAIL=2 (the two s3 declared box-size-stability criteria for H=0.8, 0.95; kept as FAIL, explained in NOTE §7). Seeded reruns reproduce earlier numbers.
