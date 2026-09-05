# RESULTS — block 219, the cone's shape in three directions on the (4,4,4) bench at the covariant witness (Fable primary seat)

Runner: `scripts/admissibility_dirac_kahler_three_direction_bench_covariant_witness_2026_09_05.py`
Note: `docs/ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md`
Exact arithmetic only (SymPy integers, rationals, symbols, `QQ(sqrt 6)` and `QQ(sqrt 6, i)`; exact charpolys of `8 x 8`
and `64 x 64` matrices over algebraic number fields; factorization over `QQ` and `QQ(sqrt 6)`; leading minors; matrix
identities at symbolic Bloch phases); gate I measures zero `sp.nsimplify`, zero float literals and zero float call
sites in the runner's own source.

## Headline

The direct `64 x 64` charpoly was TIMED FIRST, as the spec required: the onsite pencil at the witness over `QQ(sqrt 6)`
takes under one second (Bloch union = direct True), the onsite form 21 s, the overlap form 27 s and the overlap pencil
79 s (all Bloch = direct in the probe) — the direct check FITS, no substitute consistency gate is needed. On Block 213's
`bench_matrix` at extent `(4,4,4)` (64 sites; Block 213's `bench_momenta` confirmed as the eight points `{1, i}^3`, the
triply-mixed point `(i,i,i)` present) the Bloch-point lemma holds in three directions: `d_B(z) = sum_mu (z_mu - 1/z_mu)/2
D(e_mu)` at symbolic `z` with `z_y` a live symbol of the Bloch block, so the raising block is `i D(kappa_z)` at all eight
points, `D(kappa_z)^2 = 0` at each, the onsite Hodge block is `Z^-1 H0 Z` at five cells, and the onsite pencil block
charpoly equals the charpoly of `(H0^-1 M(kappa_z))^2` at ALL EIGHT points — the triply-mixed point with
`M(e_t + e_x + e_y)` included — at the witness, W1, the flat cell and the two rescaled points; the form reading and the
overlap assembly fail at every nonzero point. At L+-'s covariant cell (mask 2, the curve moduli) with the parameters at
`(0, 1/4, -1/4, 1/4)` the onsite pencil block multisets are `{9/8 x2, 16/11 x2, 18/11 x4}` at the three pure points AND
at the triply-mixed point, and `{3/2 x2, 64/33 x2, 24/11 x4}` at the three doubly-mixed points; the seven `Q` values
COMPUTED from `G1 = D1/D0 = (3/8)[[3,-1,-1],[-1,3,-1],[-1,-1,3]]` are `9/8, 9/8, 9/8, 3/2, 3/2, 3/2` and `9/8` (the
goal's "compute, do not assume" resolved: `Q(e_t+e_x+e_y) = (3/8)(9 - 6) = 9/8`), and at every one of the seven points
every nonzero eigenvalue is a Block 216 branch constant `{1, 128/99, 16/11 x2}` times `Q` — THE CONE'S SHAPE IS VISIBLE
IN ALL THREE DIRECTIONS. `G1` IS READ OFF THE BENCH: the six entries from the pure and doubly-mixed points are
`(9/8, 9/8, 9/8; -3/8, -3/8, -3/8)` = the entries of `D1/D0`, and the triply-mixed point is the over-determined check,
predicted `3(9/8) + 6(-3/8) = 9/8` against measured `9/8` — CONSISTENT; `det M` on the line is `(64/81) Q^4` at all
seven points. BLOCK 216's TWO RESCALINGS ARE SEEN ON THE BENCH: at the second line multiple `lambda = 1/2` (positive
definite by its eight leading minors, checked BEFORE use; `1/4 < v0 v1 = 3/4`) the multisets at all seven points are
Block 216's symbolic constants at `lam_line = 1/2`, `{1, 16/9, 2 x2}` = `{1, (32/27) r, (4/3) r x2}` with
`r = 1/(1 - lambda^2/(v0 v1)) = 3/2` (`12/11 = LINE_RESCALE` at `1/4`), times `Q` (pure-t `{9/8 x2, 2 x2, 9/4 x4}`); at
`D07 = 1/4` they are `{128/119, 128/99, 16/11 x2}` times `Q`, `128/119 = D07_RESCALE` (pure-t `{144/119 x2, 16/11 x2,
18/11 x4}`), and the bench read-off of `G1` there returns `(128/119) G1` exactly — the constant-1 branch carries the
rescaling (a finding, declared). At the all-plus W1 the identity holds at all eight points but the shape fails at every
point: the rational branch `k^T G1 k` (`16/15` pure, `8/5` mixed and triply-mixed; W1's six entries read off and its
seventh point consistent) and otherwise an irreducible cubic at `t, y, tx, xy` or a linear times an irreducible quadratic
at `x, ty, txy` — at `(i,i,i)`: `(5 lam - 8)^2 (165 lam - 256)^2` times an irreducible quadratic squared, NOT a cubic
(the goal guessed "the rest irreducible"; measured: a linear times a quadratic), `256/165` no constant times `8/5`;
`det M` two quadrics squared (`256/225` pure, `1024/225` at `tx, xy`, `4096/225` at `ty`, `3136/225` at `txy`). The
overlap fold at symbolic signs, moduli and parameters is parameter-free at the three pure points AND at the
triply-mixed point and sees all four parameters at the three doubly-mixed points through three signed sums,
`(-D07 - D16 + D25 + D34)/4` at `(i,i,1)`, `(-D07 + D16 - D25 + D34)/4` at `(i,1,i)`, `(-D07 + D16 + D25 - D34)/4` at
`(1,i,i)` (`-1/16, 3/16, -1/16` on the star line), so the overlap bench at the line point equals the zero-parameter one
at the five parameter-free points and differs at the three doubly-mixed points; the overlap bench identifies `t` with
`y` and distinguishes `x` where the onsite bench identifies all three. Nine direct degree-64 charpolys certified with
Bloch union = direct (the onsite pencil at five cells, the onsite form at the witness, the flat cell under its other
three constructions); the flat cell at zero gives R5's `{0 x8, 1 x24, 2 x24, 3 x8}` = `expected_flat_multiset((4,4,4))`
under all four constructions. Nothing selected; the covariance antecedent stays a reading; no dispersion-law,
Lorentzian, light-cone or continuum reading.

## Run record (every run's summary line)

| run | command | summary | exit |
| --- | --- | --- | :---: |
| probe 1 (scratch, 20:04Z) | `probe_direct.py` | `(4,4,4)`: 64 sites, momenta `{1,i}^3` in Block 213's order; eight onsite-pencil Bloch blocks in 1.7 s with the multisets `{9/8, 16/11, 18/11}` at pure AND triply-mixed, `{3/2, 64/33, 24/11}` at doubly-mixed; DIRECT `64 x 64` onsite pencil charpoly 0.7 s, degree 64, Bloch = direct True, multiset `{0 x8, 9/8 x8, 16/11 x8, 3/2 x6, 18/11 x16, 64/33 x6, 24/11 x12}`; onsite form direct 20.7 s | 0 |
| probe 2 (scratch, 20:08Z) | `probe2.py` | leading minors at `lambda = 1/2` all positive; `G1` parameter-free at three points; `Q` at seven points; ratios `{1, 128/99, 16/11}` at all seven; `{1, 16/9, 2}` at `lambda = 1/2` and `{128/119, 128/99, 16/11}` at `D07 = 1/4` at all seven; symbolic-table constants at `1/4` and `1/2`; `G1` from the bench with the check `9/8 = 9/8`; `det M` `[(2,4)]`, values; W1 shapes at eight points; identity table (onsite pencil True x8 at three cells; form/overlap False at nonzero points); raising `= iD` x8; similarity at five cells; overlap fold at eight points; line = zero pattern; flat `(4,4,4)` R5 under four constructions (0.1 s each); DIRECT W1 onsite pencil 13.0 s, `lambda = 1/2` 1.1 s, `D07` 1.1 s, overlap pencil 78.5 s, overlap form 27.4 s, all Bloch = direct; Block 218's `(4,4,2)` and Block 217's `(4,2,2)` reproduce | 0 |
| harness run 1 (c4e5b711e9, 20:19Z) | full runner | `TOTAL: PASS=25 FAIL=4` in 75.5 s (bench 55.6 s): `D-1` (declared direct count 10, measured 9 — defect 1), `G-2` (the `D07` read-off is `(128/119) G1`, not `G1` — finding, literal changed), `G-3` (defects 2 and 3), `I-1` (the note not yet written) | 4 |
| harness run 2 (b27b62f88b, 20:23Z) | full runner | `TOTAL: PASS=28 FAIL=1` in 76.2 s: only `I-1` (the note was read before its fence was inserted at 20:25Z) | 1 |
| certified baseline | `runner_cache.execute_and_write_cache(..., 600)` | see "Certified baseline" below | see below |
| mutations | `--mutation <name>` x 30, one helper invocation per mutation (`run_mutation.sh`), batches of four (`census_driver.sh`), after the certification | see the table below | see below |

## Defects found in this seat's own drafts (before certification) and fixed

1. `DIRECT_COUNT` was declared 10; the bench plan carries nine direct charpolys (the onsite pencil at five cells, the
   flat one included; the onsite form at the witness; the flat cell's other three constructions). Literal corrected to
   9 in the runner, its `D-1` statement, `INSTANCE_SCOPE`, the fence and the note. No measurement changed.
2. `w1_triply_ratio_not_constant` excluded the smallest rational root instead of the quadric root, so it tested
   `8/5 / (8/5) = 1` (a branch constant) and was False; rewritten to exclude the root equal to `Q`. `256/165 / (8/5) =
   32/33` is no branch constant, as intended.
3. `w1_smallest_rational_is_quadric` was False at `(1,i,1)`, `(i,1,i)` and `(i,i,i)` — the extra rational roots
   `256/385` and `256/165` lie below `Q` there; the fact was wrong as a claim and removed (the claim that survives is
   `(Q, 2)` present in the rational roots at every point, `w1_rational_branch_is_quadric`).
4. Discipline: the first runner append was 271 lines in one tool call (cap 250); nothing was lost and every later
   append stayed under the cap; disclosed.

## Modelling choices not forced by the landed chain

- The bench plan: fourteen constructions of eight Bloch blocks each; the direct `64 x 64` check for nine of them.
  The two overlap direct charpolys at the witness (27 s and 79 s, Bloch = direct in probe 2) were left out of the
  certified baseline to keep the thirty-mutation census inside this seat's 110-minute budget (a ~80 s baseline
  against ~190 s) — they FIT the 600 s cap; this is a budget choice, recorded as a could-not, not a fit failure.
- The rescalings: Block 216's symbolic `BRANCH_TABLE` entry evaluated exactly at `lam_line = 1/2` (through `sympify`
  of its rational-function strings, exact), compared both to the bench ratios and to the closed form
  `{1, (32/27) r, (4/3) r x2}`; the `D07` constants read from Block 216's `line 1/4 + D07 1/4` entry.
- The `G1` read-off: the smallest nonzero eigenvalue at each point as the constant-1 branch (Block 218's reading),
  six entries from six points, the seventh point compared; at `D07 = 1/4` the read-off is compared to `(128/119) G1`
  after run 1 showed the constant-1 branch itself rescaled.
- The control's failure stated through factor shapes over `QQ` (rational roots and irreducible degrees) at all seven
  points, the triply-mixed shape declared coefficient for coefficient.
- The overlap fold at symbolic signs, moduli and parameters at all eight points; the star-line values of the signed
  sums as rationals at `lambda = 1/4`; the line-vs-zero comparison on the witness's Bloch blocks only (W1 zero not run).

## What could NOT be established (honest list)

- The overlap direct degree-64 charpolys (witness line, form and pencil): measured in probe 2 with Bloch = direct
  (27.4 s, 78.5 s), NOT in the certified runner — a could-not of the certified record, by budget.
- The identity "up to similarity" at the eight points: the runner gates the charpoly identity only (Block 218's
  checker verified the direct similarity on `(4,4,2)`); not re-measured here as a matrix identity.
- The other seven rule-A cells, symbolic parameters and symbolic line multiples on the bench, W1 at zero parameters
  on `(4,4,4)`, the constraint quotient: not run.
- The flat cell's line-parameter overlap identity pattern and its onsite pencil blocks (`{1 x2, 16/15 x6}` at the
  pure points, `{2 x2, 32/15 x6}` at the doubly-mixed): measured in probe 2 / run 1, recorded, not claimed.
- The `t`/`y` pairing at the control (branch degrees, `det M` values) and under the overlap fold: measured and
  declared, not explained.
- The refuting checker: pending (`CHECK_VERDICT = "FABLE-PRIMARY-REFUTING-CHECKER-PENDING"`); the independence class
  is left to the supervisor.
