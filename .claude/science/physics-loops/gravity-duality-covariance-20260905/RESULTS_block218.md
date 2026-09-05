# RESULTS — block 218, the cone's shape on a two-direction bench at the covariant witness (Fable primary seat)

Runner: `scripts/admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05.py`
Note: `docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md`
Exact arithmetic only (SymPy integers, rationals, symbols, `QQ(sqrt 6)` and `QQ(sqrt 6, i)`; exact charpolys of `8 x 8`
and `32 x 32` matrices over algebraic number fields; factorization over `QQ` and `QQ(sqrt 6)`; matrix identities at
symbolic Bloch phases); gate I measures zero `sp.nsimplify`, zero float literals and zero float call sites in the
runner's own source.

## Headline

The contract's "(4,4) bench" for the eight-corner cell is Block 213's `bench_matrix` at extent `(4,4,2)` (32 sites, not
128: each site is one corner; the `y` direction at extent 2 carries no link), and its `bench_momenta` DO contain the
mixed fine point `(i, i, 1)` — said first, per (f). On it the raising Bloch block was MEASURED before any identity was
asserted: `d_B(z) = sum_mu (z_mu - 1/z_mu)/2 D(e_mu)` at symbolic `z`, so the block is `i D(kappa_z)` at every point —
the two fine momenta enter ADDITIVELY and at the mixed point the block is `i D(e_t + e_x)` exactly. The onsite Hodge
Bloch block is `Z^-1 H0 Z`, and with `d^2 = 0` (the `D(e_mu)` square to zero and anticommute) the onsite pencil block
charpoly equals the charpoly of `(H0^-1 M(kappa_z))^2` at EVERY point — `e_t`, `e_x` and, at the mixed point,
`e_t + e_x` — at the witness, the all-plus control and the flat cell: THE MIXED-POINT IDENTITY HOLDS EXACTLY (an exact
finite identity at the fine momentum `pi/2`, not a small-`k` limit). It fails for the form reading and for the overlap
assembly at every nonzero point. At L+-'s covariant cell (mask 2, the curve moduli) with the parameters at the
star-line point `(0, 1/4, -1/4, 1/4)` the onsite pencil block multisets are `{9/8 x2, 16/11 x2, 18/11 x4}` at both pure
points and `{3/2 x2, 64/33 x2, 24/11 x4}` at the mixed point: at each of the three points EVERY nonzero eigenvalue is a
Block 216 branch constant `{1, 128/99, 16/11 x2}` times `k^T G1 k` at `kappa_z` (`9/8, 9/8, 3/2`), the cross term
`G1_tx = (3/2 - 9/8 - 9/8)/2 = -3/8` is isolated from the three points and equals the entry of `G1 = D1/D0` — THE
CONE'S SHAPE RESTRICTED TO THE `(t, x)` PLANE IS VISIBLE TO A BENCH (Block 217's REOPEN item 3, answered at one
witness); `det M` on the line is one quadric to the fourth power (`81/64, 81/64, 4`). At the all-plus `W1` control the
identity still holds (it is structural) but the shape statement fails exactly thus: one rational branch `k^T G1 k`
(`16/15, 16/15, 8/5`, reading W1's `G1_tx = -4/15`) and the other three eigenvalues the roots of an irreducible cubic at
the pure-`t` and mixed points and `256/385` plus an irreducible quadratic at the pure-`x` point; `det M` on the line is
two distinct quadrics each squared. Under the overlap assembly the Bloch fold at symbolic signs, moduli and parameters
is parameter-free at both pure points and at the mixed point sees ALL FOUR parameters through the signed sum
`(-D07 - D16 + D25 + D34)/4` on the parity block (Block 217's `s` at the zero point; `-lam` on the star line), so the
overlap bench charpolys at the line point equal the zero-parameter ones at the pure points and differ at the mixed
point; and the overlap bench distinguishes `t` from `x` at the witness (form `{36481/55296, 89401/55296}` against
`{51529/55296, 69169/55296}`; pencil R5's `{1 x8}` against `{227/263, 263/227}`) where the onsite bench does not —
Block 217's `x`-axis `D4` seen by a bench (REOPEN item 4). All twenty degree-32 charpolys have Bloch union = direct;
every direct `32 x 32` charpoly under 2 s. Nothing selected; the covariance antecedent stays a reading; no
dispersion-law, Lorentzian, light-cone or continuum reading.

## Run record (every run's summary line)

| run | command | summary | exit |
| --- | --- | --- | :---: |
| probe 1 (scratch, 19:15Z) | `probe1.py` | momenta `(1,1,1),(1,i,1),(i,1,1),(i,i,1)`, 32 sites, 0 `y`-links, 64 raising entries; raising block `= i D(kappa_z)` at all four points and the symbolic sine identity True; `D_mu^2 = 0`, anticommute, `D(e_t+e_x)^2 = 0`; onsite `H_B = Z^-1 H0 Z` at all points (witness, W1); 14 bench charpolys, all Bloch = direct, direct `0.03-1.6 s`, union `0.2-0.8 s`; identity table (onsite pencil True at all four points at three cells; form/overlap False at nonzero points, flat overlap mixed); ratios `{1, 128/99, 16/11}` at all three points at the witness, `G1_tx = -3/8`; W1 shapes; `det M` factors `[(2,4)]` (witness) and `[(2,2),(2,2)]` (W1); overlap fold parity blocks per point — 35.7 s total | 0 |
| harness run 1 (1edb805ad4, 19:32Z) | full runner | measurement complete (`bench 17.6 s`, `shape 5.8 s`, `control 5.7 s`, 34 s); `INTERNAL-EXCEPTION: TypeError: keywords must be strings` in `build_claims` — defect 1 | 1 |
| harness run 2 (6fbbfa6ff3, 19:34Z) | full runner | `TOTAL: PASS=25 FAIL=1` in 33.7 s: only `I-1` (the note's fence not yet written) | 1 |
| certification 1 (d95234265a, 19:38Z) | `runner_cache.execute_and_write_cache(..., 600)` | on the 608-line note; superseded by the recertification on the note under the 600-line cap (below) | see below |
| certified baseline | `runner_cache.execute_and_write_cache(..., 600)` | see "Certified baseline" below | see below |
| mutations | `--mutation <name>` x 27, one helper invocation per mutation (`run_mutation.sh`), batches of four, after the certification | see the table below | see below |

## Defects found in this seat's own drafts (before certification) and fixed

1. Two mutation flips (`break_control_multisets`, `break_control_failure`) built their wrong dictionaries with
   `dict(base, **{tuple_key: value})`, which Python rejects (keyword keys must be strings); rewritten as
   dict-unpacking literals `{**base, tuple_key: value}`. No measurement or literal changed.
2. The note's first complete draft was 614 lines (cap 600); the one-sentence summary and the interpretations-fence
   word list were tightened. No number changed; the fence line untouched.

## Modelling choices not forced by the landed chain

- The bench: the contract's "(4,4)" read as Block 213's `bench_matrix` at extent `(4,4,2)` — the two-direction bench
  of the three-direction chain (Block 213's literal `(4,4)` is the two-direction lane on four-corner cells, which
  cannot carry the eight-corner cell form). Declared first and gated (`C-1`); the direct `32 x 32` charpoly fits,
  so no substitute consistency gate was needed; Block 217's `(4,2,2)` identity is re-run at the witness anyway (`C-2`).
- The cells: Block 217's `bench_cells` (the same function), plus the flat cell at zero parameters as the R5 control.
- The identity: the Bloch block charpoly against the charpoly of `(H0^-1 M(kappa_z))^2` with the principal part
  squared symbolically then evaluated at `kappa_z in {e_t, e_x, e_t + e_x, 0}` — an exact polynomial identity, the
  mechanism (`Z D Z^-1 = i D`, `d^2 = 0`) written in the note and the identity measured rather than derived.
- The shape test: the block multiset divided by `Q(kappa_z) = kappa_z^T G1 kappa_z` compared to Block 216's
  `BRANCH_TABLE[("L+-", "line 1/4")]`; the cross term read from the smallest nonzero eigenvalue at each point (the
  constant-1 branch), which is the bench-only reading.
- The control's failure stated through factor shapes over `QQ` (the rational roots and the irreducible degrees)
  rather than through a numerical comparison.
- The overlap fold at symbolic signs, moduli and parameters at each Bloch point (Block 214's `formal_cell` with
  Block 217's sign symbols), the parity block's nonzero entry declared as a string literal.

## What could NOT be established (honest list)

- The `y` direction: `G1_ty`, `G1_xy`, `G1_yy` are not read (the bench samples the `(t, x)` plane); the cone's shape
  in all three directions needs an extent with `N_y = 4` (64 sites), not run.
- The other seven rule-A cells, symbolic parameters on the bench, other line multiples or `D07 != 0`: not run.
- The flat cell's overlap identity pattern (True at `(1,i,1)` and `(i,i,1)` for the form, at `(i,i,1)` for the pencil):
  measured and recorded, not explained and not claimed.
- The overlap mixed-point charpolys at the line point (an irreducible quartic squared for the form,
  `(17837 lam^2 - 58604 lam + 48020)^4` for the pencil): declared by shape; no closed form in the signed sum.
- The refuting checker: pending (`CHECK_VERDICT = "FABLE-PRIMARY-REFUTING-CHECKER-PENDING"`); the independence class
  is left to the supervisor.

## Certified baseline (cache receipt `logs/runner-cache/admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05.txt`, exit 0, status ok, 36.65 s wall, `elapsed_ms: 33968`; runner sha256 `765d7389d8e69d4c...`, git blob `89f1d01ffe`; input fingerprint `58d8c71da4c51a3c...` over the eleven declared `AUDIT_INPUT_PATHS`, this note first; timeout 600; recertified after the note was trimmed under the 600-line cap — certification 1 on the 608-line note had the same runner sha, `TOTAL: PASS=26 FAIL=0`, 36.17 s, fingerprint `a954f6e5...`, and is superseded)

Header pins (runner sha256, input fingerprint, timeout 600, exit 0, status ok) are in the receipt; the full stdout (measured facts, 26 checks, the N5 fence) is its stdout section. The phase timings, the check lines, the gate line and the total:

```text
timings_ms: {'authority': 793, 'census': 1348, 'construction': 442, 'bench': 17668, 'identities': 2184, 'shape': 5724, 'control': 5804}  elapsed_ms: 33968
[PASS] A-1: FIVE PINS RE-RESOLVED LIVE: origin/main, axiom and registry blobs on origin/main and in the worktree
[PASS] A-2: PARENT PIN IS THE BLOCK 217 TIP, an ancestor of HEAD, with its note and runner content-bound by blob
[PASS] A-3: STALE PARENT (the Block 216 tip) is a real ancestor carrying NEITHER Block 217 artifact; machinery imported; inputs readable
[PASS] B-1: NOTHING REGISTERED, NOTHING ADOPTED: seven imposed objects, zero registered, zero adopted
[PASS] B-2: NO GRAVITY IS SUPPLIED: nine structures enumerated as not supplied
[PASS] B-3: THE AXIOM CLAUSE IS QUOTED VERBATIM AND GOVERNS THE RULE; that the cell form inherits it is a READING, asserted nowhere (the theorem is the conditional)
[PASS] B-4: NO CELL, NO SUBGROUP, NO ASSEMBLY, NO READING, NO PARAMETER VALUE IS SELECTED, AND NO METRIC IS SUPPLIED: that one assembly and one reading see the shape is measured, not a selector
[PASS] B-5: THE WORDS COVARIANCE, CONE, CELL, ASSEMBLY, BENCH AND SHAPE ARE SCOPED; six readings enumerated, none licensed; no dispersion law, no Lorentzian or light-cone reading, no continuum, no spacetime cone
[PASS] C-1: THE BENCH IS BLOCK 213's bench_matrix AT EXTENT (4,4,2): 32 sites, the y direction carrying no link (0 y-link entries, 64 raising entries), Bloch momenta (1,1,1), (1,i,1), (i,1,1), (i,i,1) -- the MIXED fine point exists; Block 217's (4,2,2) momenta are (1,1,1), (i,1,1)
[PASS] C-2: THE WITNESS AND THE CONTROL ARE BLOCKS 216/217's: Block 216's mask-2 rule-A cell carries Block 213's L+- signs (+,+,+,+,-,+), the parameters sit at (0, 1/4, -1/4, 1/4), Block 217's (4,2,2) onsite pencil multiset reproduces with Bloch = direct (the smaller-extent consistency gate), G1_tt = 9/8, W1's moduli are Block 211's
[PASS] C-3: THE FLAT CONTROL AT ZERO PARAMETERS GIVES R5's MULTISET {0 x8, 1 x16, 2 x8} = Block 213's expected_flat_multiset((4,4,2)) under both assemblies and both readings
[PASS] D-1: BLOCH UNION = DIRECT BENCH at every one of the 20 degree-32 charpolys over QQ(sqrt 6) and QQ(sqrt 6, i); the zero Bloch point contributes eight zeros everywhere
[PASS] D-2: THE WITNESS BLOCKS: onsite pencil {9/8 x2, 16/11 x2, 18/11 x4} at both pure points and {3/2 x2, 64/33 x2, 24/11 x4} at the mixed point; onsite form Block 217's irreducible quartic squared at the pure points and another at the mixed point; the overlap form and pencil at the pure points as declared; the overlap mixed-point shapes as declared
[PASS] D-3: THE CONTROL BLOCKS at the all-plus W1: onsite pencil (15 lam - 16)^2 times Block 217's irreducible cubic squared at (i,1,1), (15 lam - 16)^2 (385 lam - 256)^2 times an irreducible quadratic squared at (1,i,1), (5 lam - 8)^2 times an irreducible cubic squared at (i,i,1); overlap form Block 214's OVERLAP_FORM_W1 at both pure points; overlap pencil R5's at (i,1,1) and {55/71 x4, 71/55 x4} at (1,i,1)
[PASS] E-1: THE RAISING BLOCH BLOCK IS i D(kappa_z) AT EVERY POINT, MEASURED FIRST: d_B(z) = sum_mu (z_mu - 1/z_mu)/2 D(e_mu) at symbolic z (the fine momenta enter additively; at the mixed point i D(e_t + e_x)); D(e_mu)^2 = 0, the D(e_mu) anticommute, D(e_t + e_x)^2 = 0
[PASS] E-2: THE ONSITE HODGE BLOCH BLOCK IS Z^-1 H0 Z with Z = diag(z^c) at every point, at the witness, the control and the flat cell
[PASS] E-3: THE IDENTITY WITH THE PRINCIPAL PART: the onsite pencil block charpoly equals the charpoly of (H0^-1 M(kappa_z))^2 at EVERY point -- the MIXED point with kappa = e_t + e_x included -- at the witness, the control and the flat cell; it fails for the form reading and for the overlap assembly at every nonzero point of the witness and the control
[PASS] F-1: THE CONE'S SHAPE IS VISIBLE at the witness: at each of the three nonzero points every nonzero eigenvalue is a Block 216 branch constant {1, 128/99, 16/11 x2} times k^T G1 k at kappa_z, the quadric values 9/8, 9/8, 3/2; G1's (t, x)-plane restriction is (9/8, -3/8, 9/8)
[PASS] F-2: THE CROSS TERM IS ISOLATED FROM THE THREE POINTS: (Q_mixed - Q_t - Q_x)/2 = -3/8 = G1_tx read from the bench alone; the pure points coincide; det M on the line is one quadric to the fourth power with 81/64, 81/64, 4 at e_t, e_x, e_t + e_x, the ratio (Q_mixed/Q_t)^4
[PASS] G-1: THE CONTROL FAILS EXACTLY THUS: at the all-plus W1 the Bloch = principal identity holds at the mixed point too, but at every nonzero point only the rational branch k^T G1 k (16/15, 16/15, 8/5; G1_tx = -4/15 read from it) is a constant times the quadric -- the other three eigenvalues are the roots of an irreducible cubic at the pure t and mixed points and of a linear times an irreducible quadratic at the pure x point, the pure points differ, and det M on the line is two distinct quadrics each squared (256/225, 1024/225)
[PASS] G-2: THE OVERLAP FOLD'S PARAMETER DEPENDENCE, POINT BY POINT, at symbolic signs, moduli and parameters: parameter-free at both pure points; at the mixed point all four parameters through the signed sum (-D07 - D16 + D25 + D34)/4 on the parity block (Block 217's (D07 + D16 + D25 + D34)/4 at the zero point); the overlap bench at the line point equals the zero-parameter one at the pure points and differs at the mixed point, form and pencil, witness and control
[PASS] G-3: THE SECOND DIRECTION SEES THE x-AXIS DISTINCTION: at the witness the onsite blocks at (i,1,1) and (1,i,1) coincide while the overlap blocks differ (form {36481/55296, 89401/55296} against {51529/55296, 69169/55296}; pencil R5's against {227/263, 263/227}); at W1 the overlap form coincides and the overlap pencil differs
[PASS] H-1: SCOUT-GRADE FENCE, inherited verbatim from Blocks 211, 213, 214, 215, 216 and 217
[PASS] H-2: THE INSTANCE SCOPE IS ENUMERATED: six restrictions
[PASS] I-1: THE NOTE IS PRESENT AND CARRIES THE N5 FENCE BYTE-IDENTICALLY
[PASS] I-2: NO nsimplify, NO float literal, NO float call in this runner's source
GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS
TOTAL: PASS=26 FAIL=0
```

The baseline is under the 600 s budget by a factor of sixteen with all twenty direct `32 x 32` charpolys included (the slowest direct charpoly 1.6 s, the slowest Bloch union 0.9 s; bench phase 17.7 s).

## Mutation census (27 declared mutations at the certified runner sha `765d7389...` / blob `89f1d01ffe`; one helper invocation per mutation (`run_mutation.sh <name>`), batches of four (at most 4 concurrent, `census_driver.sh`), launched after the recertification finished (`CERT2 DONE 15:41:19` local); every run exits 1 through `main()`'s own-gate assertion path, i.e. each mutation fails EXACTLY its declared family and no other; no `AssertionError` ("mutation did not fail exactly its own gate") anywhere)

Disclosed: the first table generator read the failing-check column from the census log, where the helper's `tr -d '[]FAIL '` had stripped the letters A, F, I and L from the check keys (`A-1` logged as `-1`); the table below is rebuilt from the raw per-mutation stdout files (`mut_<name>.out`), with exit codes and assertion counts from the log. A driver-parsing artefact; no run was repeated and no runner output changed.

| mutation | declared gate | failing check(s) | TOTAL | exit |
| --- | :---: | --- | --- | :---: |
| `stale_main_authority` | A | A-1 | TOTAL: PASS=25 FAIL=1 | 1 |
| `stale_parent_authority` | A | A-2 | TOTAL: PASS=25 FAIL=1 | 1 |
| `claim_objects_registered` | B | B-1 | TOTAL: PASS=25 FAIL=1 | 1 |
| `claim_gravity_supplied` | B | B-2 | TOTAL: PASS=25 FAIL=1 | 1 |
| `claim_covariance_inherited` | B | B-3 | TOTAL: PASS=25 FAIL=1 | 1 |
| `claim_assembly_decided` | B | B-4 | TOTAL: PASS=25 FAIL=1 | 1 |
| `claim_cell_selected` | B | B-4 | TOTAL: PASS=25 FAIL=1 | 1 |
| `claim_reading_selected` | B | B-4 | TOTAL: PASS=25 FAIL=1 | 1 |
| `claim_continuum_read` | B | B-5 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_bench_momenta` | C | C-1 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_witness_reproduction` | C | C-2 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_flat_control` | C | C-3 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_bloch_equals_direct` | D | D-1 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_witness_multisets` | D | D-2 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_control_multisets` | D | D-3 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_raising_block_additivity` | E | E-1 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_onsite_similarity` | E | E-2 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_mixed_point_identity` | E | E-3 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_cone_shape_visible` | F | F-1 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_cross_term` | F | F-2 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_control_failure` | G | G-1 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_overlap_fold_dependence` | G | G-2 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_direction_distinction` | G | G-3 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_scout_grade_fence` | H | H-1 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_instance_scope` | H | H-2 | TOTAL: PASS=25 FAIL=1 | 1 |
| `drop_n5_fence` | I | I-1 | TOTAL: PASS=25 FAIL=1 | 1 |
| `break_float_absence` | I | I-2 | TOTAL: PASS=25 FAIL=1 | 1 |

Summary: 27/27 mutations each fail exactly their own gate family (A 2 B 7 C 3 D 3 E 3 F 2 G 3 H 2 I 2); no mutation changed any other family; every run `TOTAL: PASS=25 FAIL=1`, exit 1, zero assertion errors. Under 4-way contention each run took about 50 s (bench phase 27 s against 17.7 s alone); the census finished at 15:47:29 local, 6 min 10 s after launch.

## Probe 2 (scratch, after the supervisor's review checkpoint `0f27bb7d0b`; evidence for the checker, NOT in the certified runner)

The supervisor's F-A218-1 (the N2 mechanism's sign bookkeeping) and F-A218-2 ("up to similarity" is stronger than the
gated charpoly equality) were measured directly in a scratch probe (`probe2.py`, 2.3 s, exit 0) without touching the
certified runner, note or receipt: at the witness, the all-plus `W1` and the flat cell, at all four Bloch points,
(i) the Hermitian-transpose raising block is exactly `-i D(kappa_z)^T`; (ii) `Z op Z^-1 = -(D - H0^-1 D^T H0)` with
`op = d_B - H_B^-1 d_B^dagger H_B` and `Z = diag(z^c)` — the note's bookkeeping, sign for sign; (iii) the DIRECT
similarity `Z S_B(z) Z^-1 = (H0^-1 M(kappa_z))^2` holds as an `8 x 8` matrix identity (`S_B = -op^2`), the mixed point
included — twelve (cell, point) pairs, all True. So the statement "up to similarity" is the measured truth and the
gated charpoly equality (`E-3`) is its consequence; the checker's item 3 (direct similarity) is expected to CONFIRM.
Run record line: probe 2 (scratch, 19:50Z) | `probe2.py` | 12/12 direct similarities True, 12/12 operator identities
True, 12/12 dagger blocks `-i D^T` | exit 0. Not promoted into the runner: the certified sha, receipt and 27-mutation
census are left untouched after the supervisor's review; promotion (an `E-4` check) is a one-line fold if wanted.
