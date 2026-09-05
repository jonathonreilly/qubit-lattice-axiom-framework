# RESULTS — block 217, the other assembly at the covariant cells, and the bench (Fable primary seat)

Runner: `scripts/admissibility_dirac_kahler_overlap_assembly_covariant_cells_2026_09_05.py`
Note: `docs/ADMISSIBILITY_DIRAC_KAHLER_OVERLAP_ASSEMBLY_COVARIANT_CELLS_BOUNDED_THEOREM_NOTE_2026-09-05.md`
Exact arithmetic only (SymPy integers, rationals, symbols, `QQ(sqrt 6)` and `QQ(sqrt 6, i)`; fraction-free determinants;
lex Groebner bases with their radicals; factorization over `QQ(sqrt 6)`; signed permutation matrices; exact charpolys of
`8 x 8` and `16 x 16` matrices over algebraic number fields); gate I measures zero `sp.nsimplify`, zero float literals
and zero float call sites in the runner's own source.

## Headline

At each of Block 216's 8 rule-A cells, with Block 213's curve witness transported by class, the overlap fold
`H0 = H0(0) + (s/4) P111` sees the four duality parameters only through their sum `s` — measured at SYMBOLIC face
signs and moduli, so a lemma at every cell, with the parity block `(s/4) P111` and the twelve two-flip couplings
`-(s_f0 g0 v0 v1 + s_f1 g1)/(4 v0)` (Block 213's `h_f`) at `s = 0` — and its `s = 0` locus does NOT meet covariance
there the way the onsite plane does: the fold's strict stabiliser is the identity alone for every `s` (under the
cell's own `S3_body` the order-3 elements force `g0 = g1 = 0` at symbolic moduli, the order-2 elements force
`g0 v0 v1 + g1 = 0` with a shear killed or with `g0 v0 v1 - g1 = 0`, and the curve gives `g0 v0 v1 +- g1 = 3/4, -1/4`
where `pi0 = +1` and `7/9, 1/9` where `pi0 = -1` — no variant is satisfied), its twisted stabiliser is a `D4_face` about
the `x` axis for EVERY `s` (no rotation forces `s = 0`; the `S3_body` is not inside it; the two assemblies share one
twisted `C2_edge`), so the TWO ASSEMBLIES DIFFER IN COVARIANCE AT THE COVARIANT CELLS (the exact negative of the
contract's (e), N1-N8 in the note). The union locus (`det M = det B^2` in `kappa`) is exactly `s = 0` at all 10
witnesses (`det M` of degree 4 in `s`, `det B` `s`-free). The overlap cone at `s = 0` is a pair of DISTINCT rational
quadrics differing in the sign of the `kt ky` term alone (`c_xx, |c_1|, |c_ty| = 59701/57109, 24516/57109, 2988/57109`
at `pi0 = +1`; `64961/61889, 27664/61889, 2192/61889` at `pi0 = -1`), proportional to neither the onsite `k^T G1 k` nor
each other — Block 213's non-Hodge pair, now at the covariant cells, NOT one metric's cone and NOT the onsite cone —
and for symbolic `s` it is ONE irreducible polynomial (degree 2 in `s`, 4 in `kappa`) squared: the pair merges into an
irreducible quartic off `s = 0`. On Block 213's `(4,2,2)` bench at L+-'s own cell (mask 2) with the parameters on the
star line at `1/4`: sixteen exact degree-16 charpolys with Bloch union = direct at every one; the onsite pencil
multiset `{0 x8, 9/8 x2, 16/11 x2, 18/11 x4}` is `G1_tt = 9/8` times Block 216's four branch constants
`{1, 128/99, 16/11 x2}`, because the onsite pencil bench charpoly is EXACTLY `lam^8` times the charpoly of
`(H0^-1 M(e_t))^2` (an identity at the witness, the all-plus control and the flat cell) — the bench reads the principal
part at ONE direction and the cone's shape is invisible to it; the onsite form is `lam^8` times an irreducible quartic
squared; the overlap form `{0 x8, 36481/55296 x4, 89401/55296 x4}` and pencil `{0 x8, 1 x8}` (R5's) EQUAL their
zero-parameter values, because the overlap Bloch fold at the bench's nonzero point `z = (i, 1, 1)` is parameter-free
at symbolic everything — the bench does not see the overlap sum. At the all-plus `W1` control the fold is twisted-`O`
for every `s` with a trivial strict stabiliser, the onsite bench pencil is `lam^8 (15 lam - 16)^2` times an irreducible
cubic squared and the overlap form is Block 214's `OVERLAP_FORM_W1`; at the flat cell both assemblies give `H = I`,
the fold `I + (s/4) P111` is strictly `D4_face`-covariant for every `s`. Nothing selected; the covariance antecedent
stays a reading; no continuum or light-cone reading of the bench.

## Run record (every run's summary line)

| run | command | summary | exit |
| --- | --- | --- | :---: |
| probe 1 (scratch, 18:24Z) | `probe1.py` | the fold sees only `s` at symbolic signs; `(s/4) P111`; the twelve couplings; the shear relation at symbolic moduli at all 8 cells (order-3: `g0, g1`; order-2: `g0, g0 v0 v1 + g1, g1` twice and `g0 v0 v1 +- g1` once) with the curve values `3/4, -1/4` / `7/9, 1/9`; at cells 2, 11, 38: strict stabiliser `(0,)`, twisted `{0,1,2,3,20,21,22,23}` for all `s`; union locus `(s,)` (0.8 s each); `det M(s)` one `(2,4,4,4)` factor squared (2.9 s); `det B(0)` two distinct rational quadrics; bench at L+- and W1 (8 charpolys, 0.1-0.4 s each, Bloch = direct); onsite pencil at `e_t` = the bench multiset; the overlap Bloch fold at `(i,1,1)` parameter-free — 59 s total | 0 |
| probe 2 (scratch, 18:33Z) | `probe2.py` | the identity bench pencil = `lam^8` charpoly((H0^-1 M(e_t))^2) True at L+-, W1, flat (onsite); False for the form reading and the overlap assembly; overlap multisets at the line point = zero-parameter ones; Bloch fold `(i,1,1)` vs `H0(0)`: 16 entries differ; W1 all-plus: strict `{0}`, twisted all 24 for all `s`, union `(s,)`, `det B(0)` two quadrics; flat: strict `{0,1,2,3,20,21,22,23}` all `s` + 16 at `s = 0`, twisted all 24, union `(s,)`, `det B(0)` one quadric squared; the twisted set is the class `D4_face` — 23 s | 0 |
| harness run 1 (d1f4415d5c, 18:23Z) | full runner | `TOTAL: PASS=26 FAIL=3` in 87 s: `D-3` (axis literal `(1,0,0)`, measured `(0,1,0)` — defect 1), `E-1` (`ky -> -ky` relation False — defect 2), `I-1` (note not yet written) | 1 |
| harness run 2 (9fcd400b9e, 18:25Z) | full runner | `TOTAL: PASS=28 FAIL=1` in 86 s: only `I-1` (the note's fence appended after the run started) | 1 |
| certified baseline (781f00c0fe) | `runner_cache.execute_and_write_cache(..., 600)` | see "Certified baseline" below | see below |
| mutations (781f00c0fe) | `--mutation <name>` x 29, one helper invocation per mutation, 4-way parallel, concurrent with the certification | see the table below | see below |

## Defects found in this seat's own drafts (before certification) and fixed

1. The declared axis of the overlap fold's twisted `D4_face` was written as `(1, 0, 0)`, which in the lane's `(t, x, y)`
   coordinates is the `t` axis; the measured axis is `(0, 1, 0)`, the `x` axis, as the note's argument (the odd face is
   `ty`, the 4-fold about `x` exchanges `tx` and `xy`) requires. Literal corrected; no mathematics changed.
2. The pair of overlap quadrics was declared "related by `ky -> -ky`"; that reflection also flips the `kx ky` term, which
   the pair shares. The measured relation is that `Q+ - Q-` is a multiple of `kt ky` alone (the pair differs in the sign
   of the `kt ky` coefficient, Block 213's "t-y plane terms"). Fact and literal corrected; no mathematics changed.

## Modelling choices not forced by the landed chain

- The witnesses: Block 216's — Block 213's curve points transported by class of `pi0`; W1's moduli at the all-plus
  cell; the flat moduli. The loci and the cone are measured at all 8 rule-A cells (not one per class).
- The overlap parameter: `s` symbolic for the loci, the stabilisers and the cone (`(s, 0, 0, 0)` placed on `D07`,
  which is exact by the fold lemma); the bench at the numeric star-line point `(D16, D25, D34) = (1/4, -1/4, 1/4)`,
  `D07 = 0`, i.e. `s = 1/4` — and at zero parameters for the overlap comparison.
- The bench: L+-'s own cell (mask 2) as the covariant witness, the all-plus W1 and the flat cell as controls; the
  direct `16 x 16` charpoly over `QQ(sqrt 6)` and the Bloch union over `QQ(sqrt 6, i)` — Block 213's `domain_symbol`
  re-implemented over algebraic number fields (its own runs were at rational witnesses in `QQ(i)`).
- The stabilisers in `s`: feasibility per (rotation, sign vector) from the entries of `T H0(s) T^T - H0(s)` (a nonzero
  constant = infeasible; a multiple of `s` = `s = 0` forced; zero = free), rather than Block 215's `constraints`,
  whose forced-set bookkeeping assumes symbolic moduli.
- The shear relation: the non-volume factors of the residual entries at symbolic moduli at each cell's own signs,
  under the cell's own onsite `S3_body` (Block 216's stabiliser), then evaluated on the curve.
- The small-`k` statement is an exact polynomial identity between two charpolys (bench and principal part at `e_t`),
  not a limit; the cone at `e_t` is reported as the number `c G1_tt^4`.

## What could NOT be established (honest list)

- The bench at the other seven rule-A cells, at symbolic parameters, at other line multiples or with `D07 != 0`: not
  run (one witness, one numeric point, as contracted; the overlap charpolys at the line point equal those at zero
  parameters, so for the overlap assembly the point does not matter on this bench).
- The two-direction `(4,4)` bench at a covariant witness: not run; the `x`-axis distinction of the overlap `D4` and of
  `Q+-` is measured on the principal part only.
- The flat cell's onsite form charpoly on the bench: measured (Bloch = direct, degree 16) but its factor shape is not
  declared as a literal.
- The overlap loci symbolically in the moduli at the rule-A cells (the stabilisers at symbolic `g0, g1, v0, v1` with
  `s` symbolic): only the shear relation (the `S3_body`'s forced conditions) is symbolic in the moduli; the twisted
  `D4_face` and the union locus are at the 10 exact witnesses.
- Whether the overlap cone's `Q+-` at the rule-A cells has a closed form in the moduli (Block 213's
  `OVERLAP_CONE_PLUS/MINUS` in `h0, h_f`): not compared symbolically; the rational coefficients are declared per class.
- The refuting checker: pending (`CHECK_VERDICT = "FABLE-PRIMARY-REFUTING-CHECKER-PENDING"`); the independence class
  is left to the supervisor.

## Certified baseline (cache receipt ``, exit 0, status ok, 180.74 s wall — the first 90 s of the group phase under the transient 29-way contention disclosed in the run record, 87 s alone in harness runs 1 and 2; runner sha256 `60bb268ae73c068d...`, git blob `25b0714ef9`; input fingerprint `644e1595561de3e0...` over the ten declared `AUDIT_INPUT_PATHS`, this note first; timeout 600)

Header pins (runner sha256, input fingerprint, timeout 600, exit 0, status ok) are in the receipt; the full stdout (measured facts, 29 checks, the N5 fence) is its stdout section. The check lines, the gate line and the total:

```text
timings_ms: {'authority': 629, 'group': 89745, 'census': 11070, 'fold': 489, 'loci': 39448, 'cone': 30248, 'bench': 4143, 'smallk': 1116}  elapsed_ms: 176893
[PASS] A-1: FIVE PINS RE-RESOLVED LIVE: origin/main, axiom and registry blobs on origin/main and in the worktree
[PASS] A-2: PARENT PIN IS THE BLOCK 216 TIP, an ancestor of HEAD, with its note and runner content-bound by blob
[PASS] A-3: STALE PARENT (the Block 215 tip) is a real ancestor carrying NEITHER Block 216 artifact; machinery imported; inputs readable
[PASS] B-1: NOTHING REGISTERED, NOTHING ADOPTED: six imposed objects, zero registered, zero adopted
[PASS] B-2: NO GRAVITY IS SUPPLIED: nine structures enumerated as not supplied
[PASS] B-3: THE AXIOM CLAUSE IS QUOTED VERBATIM AND GOVERNS THE RULE; that the cell form inherits it is a READING, asserted nowhere (the theorem is the conditional)
[PASS] B-4: NO CELL, NO SUBGROUP, NO ASSEMBLY, NO READING, NO PARAMETER VALUE IS SELECTED, AND NO METRIC IS SUPPLIED: the difference between the assemblies is measured, not a selector
[PASS] B-5: THE WORDS COVARIANCE, CONE, CELL, ASSEMBLY AND BENCH ARE SCOPED; six readings enumerated, none licensed; no continuum, no light cone, no spacetime cone
[PASS] C-1: THE CELLS ARE BLOCK 216's: the census reproduces its 8 rule-A masks (2, 11, 16, 25, 38, 47, 52, 61) among its 16 star-pattern cells, indexings agreeing
[PASS] C-2: THE WITNESSES ARE BLOCK 216's: at every rule-A cell the transported curve point has the S3_body as onsite strict stabiliser, both shears nonzero, v0 v1 = 3/4 or 8/9
[PASS] C-3: THE FOLD LEMMA AT SYMBOLIC FACE SIGNS AND MODULI: the overlap H0 sees the parameters only through s at every cell, its parity block is (s/4) P111, it is linear in s, and at s = 0 it is h0 I plus twelve two-flip couplings -(s_f0 g0 v0 v1 + s_f1 g1)/(4 v0), one magnitude per face
[PASS] C-4: THE FLAT CONTROL: both assemblies give H = I at zero parameters (Block 213's D-1) and the flat fold is I + (s/4) P111
[PASS] D-1: THE UNION LOCUS IN s IS EXACTLY s = 0 at all 10 witnesses (the 8 rule-A curve witnesses over QQ(sqrt 6), the all-plus W1 and the flat cell): det M has degree 4 in s and det B is s-free
[PASS] D-2: THE STRICT STABILISER OF THE OVERLAP FOLD IS TRIVIAL at every rule-A witness for every s (the identity is the only feasible rotation); at the all-plus W1 control it is trivial too
[PASS] D-3: THE TWISTED STABILISER OF THE OVERLAP FOLD IS A D4_face OF ORDER 8 ABOUT THE x AXIS FOR EVERY s at every rule-A witness, the S3_body is not inside it, the two assemblies share exactly one twisted C2_edge; the all-plus W1 fold is twisted-O for every s; the flat fold is strictly D4_face for every s and strictly covariant under the other 16 only at s = 0, twisted-O for every s
[PASS] D-4: THE SHEAR RELATION AT SYMBOLIC MODULI under each cell's own S3_body: the order-3 elements force g0 = g1 = 0, the order-2 elements force g0 v0 v1 + g1 = 0 with g0 = g1 = 0 or with g0 v0 v1 - g1 = 0 -- the same at all 8 cells; no shear-alive strict locus exists
[PASS] D-5: THE CURVE VIOLATES EVERY VARIANT: g0 v0 v1 + g1 = 3/4 and g0 v0 v1 - g1 = -1/4 where pi0 = +1, 7/9 and 1/9 where pi0 = -1, both shears nonzero -- the overlap fold at a rule-A witness is NOT strictly S3-covariant, and the two assemblies differ in covariance at the covariant cells
[PASS] E-1: THE OVERLAP CONE AT s = 0 IS A NON-HODGE PAIR at every rule-A witness: det M(0) = det B(0)^2, det B(0) = Q+ Q- with two DISTINCT rational quadrics differing in the sign of the kt ky term alone, the declared coefficient magnitudes per class; the same shape at the all-plus W1, one quadric squared at the flat cell
[PASS] E-2: THE OVERLAP CONE IS NOT THE ONSITE CONE: at no rule-A witness is det B(0) proportional to (k^T G1 k)^2, and neither quadric is proportional to k^T G1 k -- not one metric's cone
[PASS] E-3: THE OVERLAP CONE AT SYMBOLIC s IS ONE IRREDUCIBLE POLYNOMIAL SQUARED, of degree 2 in s and 4 in kappa, at all 10 witnesses -- the pair merges into an irreducible quartic off s = 0
[PASS] F-1: THE BENCH AT THE COVARIANT WITNESS (L+-'s cell, line point 1/4): onsite pencil {0 x8, 9/8 x2, 16/11 x2, 18/11 x4}, onsite form lam^8 times an irreducible quartic squared, overlap form {0 x8, 36481/55296 x4, 89401/55296 x4}, overlap pencil R5's
[PASS] F-2: BLOCH UNION = DIRECT BENCH at every one of the 16 degree-16 charpolys (Block 213's E-gate over QQ(sqrt 6) and QQ(sqrt 6, i))
[PASS] F-3: THE CONTROLS ON THE BENCH: at the all-plus W1 the onsite pencil is lam^8 (15 lam - 16)^2 times an irreducible cubic squared, the onsite form lam^8 times an irreducible quartic squared, the overlap form Block 214's OVERLAP_FORM_W1; at the flat cell the onsite pencil is {0 x8, 1 x2, 16/15 x6}; the overlap pencil is R5's everywhere
[PASS] G-1: THE BENCH READS THE PRINCIPAL PART AT ONE DIRECTION, EXACTLY: the bench momenta are z = (1,1,1) and (i,1,1); the onsite pencil bench charpoly equals lam^8 times the charpoly of (H0^-1 M(e_t))^2 at the witness, the control and the flat cell; at the witness that is G1_tt = 9/8 times Block 216's four branch constants; the onsite cone at e_t is the number 64/81 G1_tt^4; the identity fails for the form reading and for the overlap assembly -- no continuum reading
[PASS] G-2: THE BENCH DOES NOT SEE THE OVERLAP SUM: the overlap Bloch fold at z = (i,1,1) is parameter-free at symbolic signs, moduli and parameters, differs from H0 in 16 entries at the witness, and the overlap bench charpolys at the line point equal those at zero parameters
[PASS] H-1: SCOUT-GRADE FENCE, inherited verbatim from Blocks 211, 213, 214, 215 and 216
[PASS] H-2: THE INSTANCE SCOPE IS ENUMERATED: six restrictions
[PASS] I-1: THE NOTE IS PRESENT AND CARRIES THE N5 FENCE BYTE-IDENTICALLY
[PASS] I-2: NO nsimplify, NO float literal, NO float call in this runner's source
GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS
TOTAL: PASS=29 FAIL=0
```

## Mutation census (29 declared mutations at the certified runner sha `60bb268a...` / blob `25b0714ef9`; one helper invocation per mutation (`run_mutation.sh <name>`), batches of four (at most 4 concurrent), launched after the certification run; every run exits 1 through `main()`'s own-gate assertion path, i.e. each mutation fails EXACTLY its declared family and no other)

Disclosed: a first census driver launched all 29 at once (zsh `jobs -r` does not track background jobs in a non-interactive script); it was stopped after ~80 s, its outputs discarded, and the census re-run with the batch-of-four driver; the certification run that overlapped its first 80 s finished `exit 0` in 180.7 s (the group phase absorbed the contention) and is superseded by the recertification below.

| mutation | declared gate | failing check(s) | TOTAL | exit |
| --- | :---: | --- | --- | :---: |
| `stale_main_authority` | A | A-1 | TOTAL: PASS=28 FAIL=1 | 1 |
| `stale_parent_authority` | A | A-2 | TOTAL: PASS=28 FAIL=1 | 1 |
| `claim_objects_registered` | B | B-1 | TOTAL: PASS=28 FAIL=1 | 1 |
| `claim_gravity_supplied` | B | B-2 | TOTAL: PASS=28 FAIL=1 | 1 |
| `claim_covariance_inherited` | B | B-3 | TOTAL: PASS=28 FAIL=1 | 1 |
| `claim_assembly_decided` | B | B-4 | TOTAL: PASS=28 FAIL=1 | 1 |
| `claim_cell_selected` | B | B-4 | TOTAL: PASS=28 FAIL=1 | 1 |
| `claim_metric_supplied` | B | B-4 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_cell_census` | C | C-1 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_witness_reproduction` | C | C-2 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_fold_sees_sum` | C | C-3 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_flat_control` | C | C-4 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_union_locus_s` | D | D-1 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_strict_stabiliser` | D | D-2 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_twisted_stabiliser` | D | D-3 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_shear_relation` | D | D-4 | TOTAL: PASS=28 FAIL=1 | 1 |
| `claim_curve_satisfies_shear_relation` | D | D-5 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_overlap_cone_pair` | E | E-1 | TOTAL: PASS=28 FAIL=1 | 1 |
| `claim_overlap_cone_is_onsite_cone` | E | E-2 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_overlap_cone_symbolic_s` | E | E-3 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_bench_multisets` | F | F-1 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_bloch_equals_direct` | F | F-2 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_bench_control` | F | F-3 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_bench_reads_principal_part` | G | G-1 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_bloch_fold_sees_parameters` | G | G-2 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_scout_grade_fence` | H | H-1 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_instance_scope` | H | H-2 | TOTAL: PASS=28 FAIL=1 | 1 |
| `drop_n5_fence` | I | I-1 | TOTAL: PASS=28 FAIL=1 | 1 |
| `break_float_absence` | I | I-2 | TOTAL: PASS=28 FAIL=1 | 1 |

Summary: 29/29 mutations each fail exactly their own gate family (A 2 B 6 C 4 D 5 E 3 F 3 G 2 H 2 I 2); no mutation changed any other family; no `AssertionError` ("mutation did not fail exactly its own gate") anywhere.

## Recertification after the note's timing correction (2026-09-05, after the census)

The note's bench-timing sentence was corrected to the receipt (`0.25 s` / `0.35 s`, the flat form shape recorded as
measured) at `1366a5b1ec`; no check, literal or mutation changed and the runner blob `25b0714ef9` (sha `60bb268a...`)
is unchanged, so the 29-mutation census above stands. Because the note is the first fingerprinted input of the
receipt, the baseline was recertified alone after the census: `exit 0`, `status ok`, `90.40 s` wall
(`elapsed_ms: 86856`; phases authority 0.5 s, group 11.9 s, census 2.3 s, fold 0.05 s, loci 36.6 s, cone 30.3 s,
bench 4.1 s, smallk 1.1 s), `TOTAL: PASS=29 FAIL=0`, `GATES A..I = PASS`, the same 29 check lines as above; the cache
is re-pinned to input fingerprint `5636802122f2aea3...`. The certified baseline is under the 600 s budget by a factor
of six with the bench included.

## Fix pass (supervisor fold, 2026-09-05, after the refuting checker's PASS-NO-BLOCKER)

The Opus refuting checker (`CHECKER_block217_findings.md`) reproduced every priority claim on its own machinery (the fold lemma, the stabilisers at three values of `s`, the parity-block separation behind the `s`-classifier, the shear relation, the union locus and the cone, the bench with Bloch = direct and the `e_t` identity, the Bloch fold, the controls) and corrected one wording: the quadric pair is not related by `ky → −ky` (`CK-04b`, the supervisor's F-A217-1 and the primary's own draft defect 2) — the one-sentence summary now says "differing in the sign of the `kt ky` term alone". Applied with the Review record, `CHECK_VERDICT` and the fence's DECISION_CUT sentence; the fence synced byte-identically. No check, literal or mutation changed, so the 29-mutation census above (certified sha `60bb268a...`) stands; the baseline was recertified after the fold (`TOTAL: PASS=29 FAIL=0`, 90 s) and the cache re-pinned to runner sha `6b9b996a...` because the note is the first fingerprinted input of the receipt.
