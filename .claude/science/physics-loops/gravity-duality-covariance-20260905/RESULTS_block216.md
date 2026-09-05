# RESULTS — block 216, the covariant curved cell and its cone (Fable primary seat)

Runner: `scripts/admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05.py`
Note: `docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_CURVED_CELL_CONE_BOUNDED_THEOREM_NOTE_2026-09-05.md`
Exact arithmetic only (SymPy integers, rationals, symbols and `QQ(sqrt 6)`; fraction-free determinants; lex Groebner
bases with their radicals; signed permutation matrices; exact charpolys over `QQ(sqrt 6)(lam_line)[kappa]`); gate I
measures zero `sp.nsimplify`, zero float literals and zero float call sites in the runner's own source.

## Headline

At every one of Block 215's 16 star-pattern cells the union locus of the cone (`det M = det B^2` as an identity in
`kappa`) is EXACTLY the star line `D16 = D34 = -D25` — the line twisted-`O` and strict-`S3` covariance select there
with both shears alive — so covariance and the cone agree at exactly those 16 cells. Sufficiency is a lemma at every
cell: with the six face signs SYMBOLIC the odd-odd block of the onsite principal part carries no shear, no volume, no
face sign and no `D07` (its three entries are Block 214's `(D16 + D25) kt, (D34 - D16) kx, -(D25 + D34) ky`), and the
block identity `det [[A, B], [B^T, 0]] = det(B)^2` is verified at generic symbolic blocks; necessity is the measured
radical of the coefficient ideal of `det M - det B^2` at 26 positive-definite witnesses (W1's moduli at all 16 star
cells, at the all-plus control — where the union locus is still the star line while the covariant line is the diagonal
— and at the flat cell; Block 213's curve moduli over `QQ(sqrt 6)` at the 8 rule-A cells). The two 64-cell indexings
(Block 213's `FACES`, Block 211's `GAUGE_FACE_ORDER`) are the same tuple and both predicates are re-evaluated from the
sign dictionary; Block 213's Groebner census reproduces literal for literal. THE 16 STAR-PATTERN CELLS ARE EXACTLY
BLOCK 213's 16 COINCIDENCE-CURVE CELLS: rule A (`S1 = -E S0 E`) holds iff `(P_tx, P_ty, P_xy) = (+, -, +)` and rule B
iff `(-, +, -)`, because `P_f = -+ E_i E_j = +-E_k` and Block 213's `E = diag(1, -1, 1)` is the star's pair-sign
pattern; the intersection is all 16, the positive subset all 8 rule-A cells (four in each mixed gauge class; the 8
rule-B star cells are 3 face flips from the nearest rule-A cell). At each of the 8 rule-A cells Block 213's curve
point (L+-'s moduli for `pi0 = +1`, L-+'s for `pi0 = -1`) transported to the cell is positive definite, is Block 211's
own solve, and is strictly `S3`-covariant with both shears alive — its strict stabiliser IS an `S3_body`
(orders 1,2,2,2,3,3), the star line is its parameter locus with no forced condition, and the cell with the parameters
on the line is preserved — while the two readings are proportional (`mu = 32/27` / `27/32`), the graded cone is one
quadric squared and `det M = c(lam) (k^T G1 k)^4` on the star line with the multiple symbolic: ONE METRIC'S CONE FOR
EVERY LINE MULTIPLE AND, by the `D07` congruence at symbolic signs, EVERY `D07`. On the covariant line all four
pencil branches are `k`-free constants times `k^T G1 k`: the line multiple rescales the top-form and the transverse
constants and leaves the 0-form constant, `D07` rescales the 0-form constant only (Block 214's `128/119` re-measured
on the line). Block 213's symbol identity holds at every witness and its two quadrics and `det B` are invariant under
exactly the strict `S3` (each quadric in the two-dimensional `S3`-invariant space `span(|k|^2, (n.k)^2)`; the
`O`-invariant space is one-dimensional, the flat cone); a twisted rotation maps `det B` to the symbol of the GAUGED
raising part `E' D E'`, not to itself. Nothing selected; the covariance antecedent stays a reading.

## Run record (every run's summary line)

| run | command | summary | exit |
| --- | --- | --- | :---: |
| probe 1 (scratch, 16:40Z) | `probe1.py` | indexing `FACES == GAUGE_FACE_ORDER`; the 16 star masks = CK-11's list; rule A/B masks; `M_oo` lemma at symbolic signs; necessity 1 s per rational witness, 4.7 s over `QQ(sqrt 6)`; strict `S3` / twisted `O` at a star cell; the branches on the line at L+- (6 s each) | 0 |
| probe 2 (scratch, 16:45Z) | `probe2.py` | Block 213's Groebner census reproduced (1.3 s); Block 211's solve at a transported witness = `formal_cell`; the `D07` congruence at symbolic signs; the block identity at generic blocks (2.2 s); symbol invariance sets = the stabiliser; the symbolic-multiple pencil at L+- (33 s) | 0 |
| harness 1a (scratch, 16:49Z) | `harness1.py` (full `measure()`) | `IndexError` in `measure_witness` — the strict per-rotation table was built over the stabiliser only (defect 1); phases authority 0.5 s, group 12 s, census 1.4 s, covariance 6 s, union 59 s | 1 |
| harness 1b (scratch, 16:51Z) | `harness1.py` | `TypeError` in `measure_branches` — the `k`-free filter picked up the rescale Rationals (defect 2); witness phase 4 s | 1 |
| harness 2 / 1c (scratch, 16:55Z) | `harness2.py` (branches + symbol), `harness1.py` (full `measure()`) | every fact measured (193 s under 2-way contention); `twisted_symbol_is_gauged_symbol = False` because `det B` was compared without the twisted lift's sign `det T_e det T_o` (defect 3) — probe 3 confirmed `T^T M T = M_{E'}(R^-1 kappa)` and `det M(R kappa) = det M_{E'}(kappa)` exactly | 0 |
| measurement run 1 (d3df2da1c6, 17:02Z) | baseline | `TOTAL: PASS=27 FAIL=0`, 176 s (`GATES A..I = PASS`); every declared literal matched on the first complete run | 0 |
| certified baseline (b8568c8dab) | `runner_cache.execute_and_write_cache(..., 600)` | see "Certified baseline" below | see below |
| mutations (b8568c8dab) | `--mutation <name>` x 28, one helper script per mutation, 4-way parallel, concurrent with the certification | see the table below | see below |

## Defects found in this seat's own drafts (before certification) and fixed

1. `measure_witness` built the strict per-rotation locus table over the stabiliser's six members only, while Block
   215's `subgroup_locus` indexes that table by rotation index (0..23) — `IndexError`. Built over all 24.
2. `measure_branches` stored the rescale factors (Rationals) in the same table as the branch tuples and the
   `all_branches_k_free` filter selected keys by prefix, so it subscripted a Rational — `TypeError`. The filter now
   selects tuple entries.

## Modelling choices not forced by the landed chain

- The witness moduli: W1's `(15/16, 1/4, 1, 1/4)` at every star cell (positive definite in every sign cell because
  both triangles have `|g| = 1/4 < 1/2`); the curve points are Block 213's own two, transported by class of `pi0`.
- The line multiple: `(D16, D25, D34) = (lam, -lam, lam)` with `lam` symbolic; `D07 = 0` for the cone (the congruence
  makes `det M` `D07`-free) and `D07 = 1/4` at the declared branch points; the numeric line point is `lam = 1/4`.
- Masks: the enumeration index of `itertools.product((1, -1), repeat=6)` over `GAUGE_FACE_ORDER` (bit `5 - k` set
  when face `k` is `-1`) — the refuting checker's convention; the star pattern is symmetric under offset swap, so
  the other convention gives the same 16-set.
- The strict stabiliser is computed directly (`L H L^T = H` at zero parameters) rather than through the class table,
  then matched against Block 215's `S3_body` members.
- The symbol's invariance is tested as a function of `kappa` under `kappa -> R kappa` for all 24 rotations; the
  twisted statement is the identity `det B(R kappa) = det B_{E'}(kappa)` with `E' = L^T E L`, at one witness and one
  order-4 rotation, for every admissible twist.

## What could NOT be established (honest list)

- The overlap assembly at the 16 cells (its union locus `s = 0`, its cone on the covariant line): not computed —
  onsite only, as the contract scopes.
- The necessity half symbolically in the moduli (the coefficient ideal over `QQ[g0, g1, v0, v1]`): not attempted in
  the budget; the 26 witnesses are exact points, and the lemma half is symbolic in everything.
- The branch constants as functions of the line multiple are measured at the two named witnesses only (L+- and
  L-+ at their own cells); at the other six rule-A cells the cone on the line is measured (`det M = c (k^T G1 k)^4`)
  but the pencil is not factored.
- The bench, the dispersion, the `(4,2,2)` spectra with the parameters on the line: not computed.
- Any cell outside the 16 (other than the all-plus and flat controls): the union locus there is Block 214's at
  all-plus witnesses and the `M_oo` lemma everywhere; the necessity half at the other 47 cells is not run.
- The note is 603 lines against the spec's 600 (Block 214's format needs its sections); the runner is 1,202
  lines against 1,300 — recorded, not hidden; the note was not trimmed after certification because it is the
  first fingerprinted input of the receipt.
- The rescaling factors `1/(1 - lam^2/(v0 v1))` and `1/(1 - D07^2 v1/v0)` are stated as measured at the two
  named witnesses (their `v0 v1`, `v1/v0` declared) — not as a theorem along the curve.

## Defect found after the first complete harness run (disclosed with the two above)

3. The twisted-symbol identity compared `det B(R kappa)` with `det B_{E'}(kappa)` without the sign
   `det(T_e) det(T_o) = +-1` of the twisted lift's degree blocks, so it read False; probe 3 verified
   `T^T M(kappa) T = M_{E'}(R^-1 kappa)` entry by entry and `det M(R kappa) = det M_{E'}(kappa)` exactly, and
   the gate now compares `det M` exactly and `det B` up to that measured sign (gate `G-4`).

## Certified baseline (cache receipt `logs/runner-cache/admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05.txt`, exit 0, 269 s under 5-way census contention — 176 s alone; runner sha `472c5dd5b52f3360...`, git blob `b8568c8dab`; input fingerprint `616c767d375d7262...` over the nine declared `AUDIT_INPUT_PATHS`, this note first)

Header pins (runner sha256, input fingerprint, timeout 600, exit 0, status ok) are in the receipt; the full stdout (measured facts, 27 checks, the N5 fence) is its stdout section. The check lines, the gate line and the total:

```text
timings_ms: {'authority': 497, 'group': 17417, 'census': 2062, 'covariance': 9423, 'union': 92069, 'witness': 6266, 'branches': 131124, 'symbol': 6302}  elapsed_ms: 265165
[PASS] A-1: FIVE PINS RE-RESOLVED LIVE: origin/main, axiom and registry blobs on origin/main and in the worktree
[PASS] A-2: PARENT PIN IS THE BLOCK 215 TIP, an ancestor of HEAD, with its note and runner content-bound by blob
[PASS] A-3: STALE PARENT (the Block 214 tip) is a real ancestor carrying NEITHER Block 215 artifact; machinery imported; inputs readable
[PASS] B-1: NOTHING REGISTERED, NOTHING ADOPTED: six imposed objects, zero registered, zero adopted
[PASS] B-2: NO GRAVITY IS SUPPLIED: nine structures enumerated as not supplied
[PASS] B-3: THE AXIOM CLAUSE IS QUOTED VERBATIM AND GOVERNS THE RULE; that the cell form inherits it is a READING, asserted nowhere (the theorem is the conditional)
[PASS] B-4: NO CELL, NO SUBGROUP, NO ASSEMBLY, NO PARAMETER VALUE IS SELECTED, AND NO METRIC IS SUPPLIED: 'one metric's cone' names Block 213's statement only
[PASS] B-5: THE WORDS COVARIANCE, CONE, CELL, LOCUS AND METRIC ARE SCOPED; six readings enumerated, none licensed; no continuum, no spacetime cone
[PASS] C-1: THE TWO 64-CELL INDEXINGS AGREE: Block 213's FACES and Block 211's GAUGE_FACE_ORDER are the same declared tuple (tx0, ty0, xy0, tx1, ty1, xy1); both predicates are evaluated from the sign dictionary
[PASS] C-2: THE 16 STAR-PATTERN CELLS REPRODUCE BLOCK 215's G-5 RULE (the declared masks, four per gauge class, the checker's list) AND BLOCK 213's COINCIDENCE CENSUS REPRODUCES LITERAL FOR LITERAL (48 + 4 x 4 cells; rule A and rule B masks declared)
[PASS] C-3: THE COVARIANCE AT THE 16 CELLS, RE-MEASURED: the shear-alive twisted-O line is the star line at every star cell (one component), exactly one S3_body keeps both shears alive strictly there with the star line; at the all-plus control the line is the diagonal and no S3 keeps the shears alive
[PASS] C-4: THE WITNESSES ARE BLOCK 211's OWN SOLVES: at every rule-A cell the transported curve point solves Block 211's six-face system with the four parameters free, is on the curve and on both ties, has both shears nonzero and is positive definite; every union witness is positive definite
[PASS] D-1: THE M_oo LEMMA AT SYMBOLIC FACE SIGNS: the onsite H0 is the cell; the odd-odd block of M carries exactly Block 214's three entries, no shear, no volume, no face sign, no D07; its coefficient ideal is the star line; the block identity holds at generic symbolic blocks; det M = det B^2 on the line with the multiple symbolic at every witness
[PASS] D-2: THE NECESSITY HALF IS MEASURED, NOT ASSERTED FROM THE IDENTITY: at all 26 positive-definite witnesses (W1's moduli at the 16 star cells, the all-plus control and the flat cell; the curve moduli over QQ(sqrt 6) at the 8 rule-A cells) the radical of the coefficient ideal of det M - det B^2 is exactly the star line
[PASS] D-3: ONE WITNESS IN EVERY GAUGE CLASS AMONG THE 16: the class representatives are the declared masks and each carries a rational union witness
[PASS] E-1: THE INTERSECTION WITH BLOCK 213's COINCIDENCE CELLS IS ALL 16: the star-pattern cells ARE the coincidence-curve cells; rule A iff (P_tx, P_ty, P_xy) = (+, -, +), rule B iff (-, +, -), and that pattern is -E_i E_j = E_k, the star's pair signs
[PASS] E-2: THE POSITIVE SUBSET IS ALL 8 RULE-A CELLS, four in each mixed gauge class; the 8 rule-B star cells lie in the (+,+) and (-,-) classes, 3 face flips from the nearest rule-A cell
[PASS] F-1: THE COVARIANT WITNESS EXISTS AT EVERY ONE OF THE 8 RULE-A CELLS: positive definite, its strict stabiliser IS an S3_body (orders 1,2,2,2,3,3) so both shears are alive without any gauge, the star line is its parameter locus with no forced condition, and the cell with the parameters on the line is preserved
[PASS] F-2: ONE METRIC'S CONE AT THE COVARIANT WITNESS: the two readings are proportional (mu = 32/27 in class (+,-), 27/32 in class (-,+)), the graded cone is one quadric squared, and det M = c (k^T G1 k)^4 on the star line with the multiple symbolic, c = 64/81 and 9/16 -- for every line multiple, and by the D07 congruence for every D07
[PASS] G-1: THE BRANCHES ON THE COVARIANT LINE at L+- and L-+ are the declared table: with the multiple symbolic all four pencil branches are k-free constants times k^T G1 k; at lam = 1/4 the constants {1, 128/99, 16/11 x2} and {1, 108/119, 144/119 x2}; with D07 = 1/4 the 0-form constant alone moves (128/119, 12/11)
[PASS] G-2: THE TWO RESCALINGS: the line multiple rescales the top-form and transverse constants by 1/(1 - lam^2/(v0 v1)) (v0 v1 = 3/4, 8/9; 12/11 and 128/119 at lam = 1/4) and D07 rescales the 0-form constant by 1/(1 - D07^2 v1/v0) (v1/v0 = 9/8, 4/3; 128/119 and 12/11 at D07 = 1/4) -- Block 214's 128/119 re-measured on the covariant line
[PASS] G-3: THE D07 CONGRUENCE AT SYMBOLIC FACE SIGNS AND SYMBOLIC MODULI: U^T M U = M|_{D07 = 0} with U = I - (D07/D3) E_70, the H0 shift is -D07^2 v1 on the (0,0) entry and nothing else; holds at every star cell
[PASS] G-4: THE SYMBOL UNDER S3 AND UNDER A TWISTED ROTATION: Block 213's identity holds at every witness; the two quadrics and det B are invariant under kappa -> R kappa for exactly the strict S3; each quadric lies in the 2-dimensional S3-invariant space (the O-invariant space is 1-dimensional; the flat quadrics are |k|^2); the four body-diagonal axes occur; a twisted rotation maps det M to the gauged raising part's symbol (det B up to the twisted lift's sign) and det M moves
[PASS] H-1: SCOUT-GRADE FENCE, inherited verbatim from Blocks 211, 213, 214 and 215
[PASS] H-2: THE INSTANCE SCOPE IS ENUMERATED: six restrictions
[PASS] I-1: THE NOTE IS PRESENT AND CARRIES THE N5 FENCE BYTE-IDENTICALLY
[PASS] I-2: NO nsimplify, NO float literal, NO float call in this runner's source
GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS
TOTAL: PASS=27 FAIL=0
```

## Mutation census (28 declared mutations at the certified sha `472c5dd5...` / blob `b8568c8dab`; one helper script per mutation, 4-way parallel, concurrent with the certification run; every run exits 1 through `main()`'s own-gate assertion path, i.e. each mutation fails EXACTLY its declared family and no other)

| mutation | declared gate | failing check(s) | TOTAL | exit |
| --- | :---: | --- | --- | :---: |
| `stale_main_authority` | A | A-1  | TOTAL: PASS=26 FAIL=1 | 1 |
| `stale_parent_authority` | A | A-2  | TOTAL: PASS=26 FAIL=1 | 1 |
| `claim_objects_registered` | B | B-1  | TOTAL: PASS=26 FAIL=1 | 1 |
| `claim_gravity_supplied` | B | B-2  | TOTAL: PASS=26 FAIL=1 | 1 |
| `claim_covariance_inherited` | B | B-3  | TOTAL: PASS=26 FAIL=1 | 1 |
| `claim_assembly_decided` | B | B-4  | TOTAL: PASS=26 FAIL=1 | 1 |
| `claim_cell_selected` | B | B-4  | TOTAL: PASS=26 FAIL=1 | 1 |
| `claim_metric_supplied` | B | B-4  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_indexing_agreement` | C | C-1  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_star_pattern_masks` | C | C-2  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_coincidence_census` | C | C-2  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_witness_solves` | C | C-4  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_m_oo_lemma` | D | D-1  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_union_necessity` | D | D-2  | TOTAL: PASS=26 FAIL=1 | 1 |
| `claim_union_from_identity_alone` | D | D-2  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_intersection` | E | E-1  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_positive_subset` | E | E-2  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_covariant_witness` | F | F-1  | TOTAL: PASS=26 FAIL=1 | 1 |
| `claim_covariant_cell_empty` | F | F-1  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_one_metric_cone` | F | F-2  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_branch_table` | G | G-1  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_d07_rescale` | G | G-2  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_d07_congruence` | G | G-3  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_symbol_invariance` | G | G-4  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_scout_grade_fence` | H | H-1  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_instance_scope` | H | H-2  | TOTAL: PASS=26 FAIL=1 | 1 |
| `drop_n5_fence` | I | I-1  | TOTAL: PASS=26 FAIL=1 | 1 |
| `break_float_absence` | I | I-2  | TOTAL: PASS=26 FAIL=1 | 1 |

Summary: 28/28 mutations each fail exactly their own gate family (A 2, B 6, C 4, D 3, E 2, F 3, G 4, H 2, I 2); no mutation changed any other family; no `AssertionError` ("mutation did not fail exactly its own gate") anywhere.

## Fix pass (supervisor fold, 2026-09-05, after the refuting checker's PASS-NO-BLOCKER)

The Opus refuting checker (`CHECKER_block216_findings.md`) reproduced eleven load-bearing items on its own machinery and corrected two editorial points: the reason for `D07`'s absence from the odd–odd block is two-sided (column 7 AND row 0 of `D` are zero — `CK-02`) and the (−1, +1) class representative is mask 11, not 16 (`CK-04`, also the supervisor's F-A216-1). Applied with the supervisor's F-A216-2 (the "now measured" sentence qualified to the sufficiency half), the Review record, `CHECK_VERDICT` and the fence's DECISION_CUT sentence; the fence synced byte-identically. No check, literal or mutation changed, so the 28-mutation census above (certified sha `472c5dd5...`) stands; the baseline was recertified after the fold (`TOTAL: PASS=27 FAIL=0`, 179 s) and the cache re-pinned to runner sha `424df7d6...` because the note is the first fingerprinted input of the receipt.
