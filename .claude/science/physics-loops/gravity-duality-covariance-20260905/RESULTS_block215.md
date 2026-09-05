# RESULTS — block 215, the covariance locus of the four duality parameters (Fable primary seat)

Runner: `scripts/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.py`
Note: `docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md`
Exact arithmetic only (SymPy integers, rationals and symbols; signed permutation matrices; row-reduced linear
ideals over QQ; the moduli symbolic on Block 211's ties); gate I measures zero `sp.nsimplify`, zero float literals
and zero float call sites in the runner's own source.

## Headline

Block 214's plane `D16 = D34 = -D25` is the star line of the lane's own Hodge star: the raising part `D(kappa)` is
exactly the ordered-monomial wedge `kappa ^` (twelve signs measured), the star derived from that wedge has pair
signs `(+, +, -, +)` on `(0,7), (1,6), (2,5), (4,3)`, squares to `+1` on every degree, satisfies `* D = eps_k D^T *`
with `eps = (+, -, +)`, and the `1 <-> 2` cross block is `lam *` exactly on the plane (Block 214's `PLANE` literal,
literal for literal), which is why the onsite `M_oo` vanishes there (its coefficient ideal IS the line). The 24
proper cubic rotations (Block 201's det = +1 signed permutations) lifted to the eight corners through that wedge form
a representation (orders 1/2/3/4 in counts 1/9/8/6; `L(R1 R2) = L(R1) L(R2)`) intertwining `D(kappa)`, and the
sign rule is measured: exactly `+-L(R)` intertwine among the 256 signed versions of each corner permutation. The
30 subgroups and 11 conjugacy classes are computed from the multiplication table with a completeness certificate.
THE CENSUS: twisted covariance (Block 211's 64 sign vectors as the twist) leaves both shears alive under every
rotation in every gauge class, and under `C3`, `S3`, `T`, `O` forces ONE shear-alive line that is NOT the star
line at any of the four class representatives — the diagonal `D16 = D25 = D34` at all-plus and `(-1,-1)`,
`D16 = D25 = -D34` at the mixed classes — meeting the star line only at the origin; the star line appears in the
twisted tables only with a shear killed. Strict covariance forces the star line only with `g1 = 0` (`C3`, all-plus),
`g0 = 0` (`S3`, all-plus) or `g0 = g1 = 0` (`T`, `O`, every class): THE PLANE AND THE FLAT CELL TOGETHER. Under the
full group the shear-alive twisted line is one sign line at every one of the 64 cells and the star line at exactly
16 of them. `D07` is free under everything (every proper lift is `+1` on the empty and the full corner). The
overlap fold sees only `s`, `P111` is the unsigned star and commutes with 8 of the 24 signed lifts (the star with
all 24), and NO subgroup's twisted covariance forces `s = 0`; strict covariance forces `s = 0` only with a shear
relation. Positivity (`W1 + D16 = 1/4`, PD off the plane) and onsite parity (exactly the four parameters) select
nothing. The theorem is the conditional; the antecedent (the cell form inherits the axiom's covariance) is a
reading, gated and not licensed.

## Run record (every run's summary line)

| run | command | summary | exit |
| --- | --- | --- | :---: |
| probe 1 (scratch, 11:29Z) | `probe1.py` (measure_group/star/census/overlap/controls) | 72 s; every group/star fact as expected; the census showed the diagonal, not the star line, as the twisted `O` line (headline changed accordingly); `gauge_congruence_in_field = False` (defect 1) | 0 |
| probe 2 (scratch, 11:34Z) | `probe2.py` | all-30-subgroup distinct counts; the 64-cell scan: one alive line per cell, the star line at 16; `gauge_congruence_in_field` still False (defect 2) | 0 |
| probe 3 (scratch, 11:38Z) | `probe3.py` (literal generator) | the compact tables generated; forced conditions carried signs and numeric factors (defect 3) | 0 |
| probe 3b/3c (scratch, 11:41Z) | `probe3.py` regenerated | forced conditions normalised (`g0`, `g1`, `g0*v0*v1 + g1`); `gauge_congruence_in_field = True` | 0 |
| measurement run 1 (11:45Z) | baseline | see below | see below |
| measurement run 1 (a391e88512^, 11:45Z) | baseline | `NameError: TWISTED_LOCI` — the declared census tables had been appended AFTER the `__main__` block (defect 4); `TOTAL: PASS=0 FAIL=1` | 1 |
| measurement run 2 (a391e88512, 11:48Z) | baseline | `TOTAL: PASS=29 FAIL=0`, 132 s (`GATES A..I = PASS`); every declared literal matched on the first complete run | 0 |
| certified baseline | `runner_cache.execute_and_write_cache(..., 600)` | see "Certified baseline" below | see below |
| mutations | `--mutation <name>` x 25, one helper script per mutation, 4-way parallel | see the table below | see below |

## Defects found in this seat's own drafts (before certification) and fixed

1. The in-field gauge-congruence check compared the all-plus family to Block 211's class REPRESENTATIVES
   (which are one-face flips, i.e. OTHER classes) — always False. Corrected to same-class two-face flips
   (reachable) and one-face flips (not reachable), at zero parameters because the gauge also flips
   `D16, D25, D34`.
2. The same check at symbolic parameters still failed for the reason just stated (the parameter entries
   flip under `E`); the zero-parameter comparison is the right statement of "the degree blocks are congruent".
3. Forced moduli conditions were recorded as signed, scaled expressions (`-2*g0*v1`, `2*g0*v1` as two
   conditions); normalised to the non-numeric, non-volume factors of the numerator (`g0`, `g1`,
   `g0*v0*v1 + g1`), which is what the condition means on Block 211's domain.
4. The declared census tables were appended after the `__main__` block, so `main()` ran before they
   existed (`NameError` at run 1); the block was moved to the end of the file.
5. The first probe reported the loci per CLASS REPRESENTATIVE only; the loci at a fixed cell are not
   conjugation-invariant (a conjugate subgroup sees a sign-image cell), so the census was extended to every
   member of every class (distinct-locus counts gated at `E-4`) and to the 64 sign cells under `O` (`G-3`).

## What could NOT be established (honest list)

- Whether Block 214's union locus (`det M = det B^2` iff the plane) at a sign cell other than its all-plus
  witnesses coincides with that cell's twisted-`O` line — no cone is computed here; the 16 cells where the
  twisted line is the star line are counted, not connected to the cone.
- The twisted census with a twist beyond Block 211's 64 sign vectors (`e0 e7 = -1`, or non-diagonal
  intertwiners): argued in `N1` (it can only add `D07 = 0`), not run.
- Improper cubic elements (`O_h`), translations, and any projective/staggered lift other than the
  wedge-multiplicative one: not run (the lift's uniqueness among MONOMIAL intertwiners is measured; other lifts
  are not searched).
- The strict overlap relation `g0 v0 v1 + g1 = 0` is reported as measured; whether it meets Block 211's ties
  at a positive-definite point is not examined.
- The note is 650-670 lines against the spec's 600 (Block 214's format needs its sections); the runner is
  1308 lines against 1300 after the compact tables — recorded, not hidden.

## Modelling choices not forced by the landed chain

- The lift: the multiplicative extension of the `3 x 3` action through the lane's wedge (then measured to be
  the only monomial intertwiner up to sign, with the empty corner fixed at `+1`).
- The twist: Block 211's 64 sign vectors (`e0 = e7 = +1`); the loci are reported at Block 211's four class
  representatives and, for `O`, at all 64 cells.
- The canonical form of a locus: the row-reduced linear ideal plus the forced moduli conditions, unions made
  irredundant by containment; the moduli symbolic on the ties with the volumes nonzero.
- The overlap census uses the fold with `(D07, D16, D25, D34) = (s, 0, 0, 0)`, licensed by the measured
  sum-only dependence.
- Two generators for the 64-cell scan (the signed lifts fixing `H` form a group; measured to generate `O`).

## Certified baseline (supervisor, post-fold; cache receipt `logs/runner-cache/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.txt`, exit 0, 181 s under 4-way census contention; runner sha `861bbf88...`)

The primary's delivered runner certified at TOTAL PASS=29 FAIL=0 (167 s, sha 94c114df... after the supervisor's G-4 extension: 30/0, 118 s). The final runner carries two supervisor gates added after delivery and measured — `G-4` (from the sealed blind seat's prediction) and `G-5` (from the refuting checker's CK-11) — and the folded verdict. Header pins (runner sha256, input fingerprint) are in the receipt; the full stdout (measured facts, 31 checks, the N5 fence) is its stdout section. The check lines, the gate line and the total:

```text
timings_ms: {'authority': 1337, 'group': 18596, 'star': 163, 'census': 43598, 'overlap': 67969, 'controls': 46650}  elapsed_ms: 178317
[PASS] A-1: FIVE PINS RE-RESOLVED LIVE: origin/main, axiom and registry blobs on origin/main and in the worktree
[PASS] A-2: PARENT PIN IS THE BLOCK 214 TIP, an ancestor of HEAD, with its note and runner content-bound by blob
[PASS] A-3: STALE PARENT (the Block 213 tip) is a real ancestor carrying NEITHER Block 214 artifact; machinery imported; inputs readable
[PASS] B-1: NOTHING REGISTERED, NOTHING ADOPTED: six imposed objects, zero registered, zero adopted
[PASS] B-2: NO GRAVITY IS SUPPLIED: nine structures enumerated as not supplied
[PASS] B-3: THE AXIOM CLAUSE IS QUOTED VERBATIM AND GOVERNS THE RULE; that the cell form inherits it is a READING, asserted nowhere (the theorem is the conditional)
[PASS] B-4: NO SUBGROUP IS SELECTED AS 'THE' SYMMETRY, NO ASSEMBLY DECIDED, NO PARAMETER VALUE SELECTED
[PASS] B-5: THE WORDS COVARIANCE, LOCUS, STAR, GAUGE AND PLANE ARE SCOPED; six readings enumerated, none licensed; no continuum, no spacetime cone
[PASS] C-1: THE CORNER ACTION IS A REPRESENTATION OF THE 24 PROPER ROTATIONS: Block 201's det = +1 signed permutations are 24; the lifts are 24 distinct orthogonal matrices, closed, containing the identity, L(R1 R2) = L(R1) L(R2), element orders 1/2/3/4 in counts 1/9/8/6
[PASS] C-2: THE SIGN RULE IS DERIVED, NOT GUESSED: the lane's D(kappa) is the ordered-monomial wedge (12 signs); the lift built through that wedge equals the orientation-sign rule; the only monomial intertwiners are +-L(R); every lift is +1 on the empty and on the full corner (det R = +1)
[PASS] C-3: THE LIFT INTERTWINES THE RAISING PART: L(R) D(kappa) L(R)^-1 = D(R kappa) for every R
[PASS] C-4: THE SUBGROUP CLASSES ARE COMPUTED FROM THE GROUP: 30 subgroups with a completeness certificate, 11 conjugacy classes with the declared (name, order, size) table
[PASS] C-5: THE FAMILY IS BLOCK 214's CELL: at W1 it equals cell_with_parameters with the four free names; the gauge congruence E D E holds in the field for same-class two-face flips and fails for one-face flips
[PASS] D-1: THE STAR FROM THE WEDGE: * e_c = sign e_{c-bar} with the declared signs, ** = +1 on every degree, * D(kappa) = eps_k D(kappa)^T * with eps = (+1, -1, +1) on 0-, 1-, 2-forms, and * commutes with every lift
[PASS] D-2: THE STAR LEMMA: the 1 <-> 2 cross block is lam * exactly on the line D16 = D34 = -D25 (the star's pair signs (+, -, +) on (y, x, t)), which IS Block 214's plane; D07 is the free 0 <-> 3 star multiple; the onsite M_oo vanishes exactly there (its coefficient ideal is the line)
[PASS] E-1: THE SHEARS SURVIVE TWISTED COVARIANCE UNDER EVERY ROTATION in all four gauge classes; strictly they survive only the identity and one edge rotation per class
[PASS] E-2: THE TWISTED CENSUS at the four class representatives is the declared table: O, T, S3, C3 force ONE shear-alive line (the diagonal D16 = D25 = D34 at all-plus and at (-1,-1); D16 = D25 = -D34 at the two mixed classes), never the star line; the star line appears only with a shear killed
[PASS] E-3: THE STRICT CENSUS is the declared table: O and T force the star line WITH g0 = g1 = 0 (the flat cell); C3 (S3) force the star line with one shear killed; the minimal strict class forcing the star line is C3
[PASS] E-4: EVERY MEMBER OF EVERY CLASS (30 subgroups): the loci at a fixed cell are not conjugation-invariant except for the normal subgroups; the distinct-locus counts per class are the declared literals
[PASS] E-5: D07 IS FREE UNDER EVERY SUBGROUP, twisted and strict: no locus generator carries D07
[PASS] F-1: P111 IS THE UNSIGNED STAR: it commutes with the unsigned corner permutation of every rotation but with only 8 of the 24 signed lifts (the twist is diag(s_c s_{R^-1 c})); the STAR commutes with all 24
[PASS] F-2: THE OVERLAP FOLD sees only s = D07 + D16 + D25 + D34, its parity block is (s/4) P111, and NO subgroup's TWISTED covariance forces s = 0 in any class (declared table); strict covariance forces s = 0 together with a shear relation (declared table)
[PASS] G-1: POSITIVITY DOES NOT SELECT THE PLANE: Block 214's witness W1 + D16 = 1/4 is off the plane and positive definite by exact leading minors
[PASS] G-2: ONSITE PARITY DOES NOT SELECT THE PLANE: the folded onsite parity block carries exactly the four parameters and vanishes iff all four vanish (the origin)
[PASS] G-3: THE FLAT CELL: strict O-covariance of the flat cell forces exactly the star line; twisted, the four sign lines (declared tables); the 64-cell scan under two generators of O finds ONE shear-alive line at every cell, the star line at exactly 16 cells and the diagonal at all-plus
[PASS] G-4: STRICT S3-COVARIANT CURVED CELLS: at exactly 16 of the 64 sign cells some S3_body keeps both shears alive under strict (E = 1) covariance, the shear-alive strict-S3 locus there is the star line, those 16 cells are exactly the cells whose twisted-O line is the star line, and strict T keeps the shears alive at no cell
[PASS] G-5: THE FACE-SIGN RULE FOR THE 16 CELLS: a sign cell is a star-line cell (twisted-O line = the star line) IFF its two-offset face-sign products (P_tx, P_ty, P_xy) follow the star's pair signs (+, -, +) on (tx, ty, xy) up to a global sign; exactly 16 cells do
[PASS] H-1: SCOUT-GRADE FENCE, inherited verbatim from Blocks 211, 213 and 214
[PASS] H-2: THE INSTANCE SCOPE IS ENUMERATED: six restrictions
[PASS] I-1: THE NOTE IS PRESENT AND CARRIES THE N5 FENCE BYTE-IDENTICALLY
[PASS] I-2: NO nsimplify, NO float literal, NO float call in this runner's source
GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS
TOTAL: PASS=31 FAIL=0
```

## Mutation results (27 declared; each must fail exactly its own family and exit nonzero) — supervisor census at the final runner sha `861bbf88...`, 2026-09-05T16:11–16:30Z, one helper script per mutation, 4-way parallel

The primary's own census never ran (the seat died after delivery); this table is the supervisor's, at the final runner (the primary's 25 mutations plus the two added with gates G-4 and G-5). **All 27 run; each fails exactly its own family, `TOTAL: PASS=30 FAIL=1`, exit 1; no run raised.**

| mutation | family | result | exit |
| --- | :---: | --- | :---: |
| `stale_main_authority` | `A` | `PASS=30 FAIL=1, GATES A=FAIL B=PASS C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS` | 1 |
| `stale_parent_authority` | `A` | `PASS=30 FAIL=1, GATES A=FAIL B=PASS C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS` | 1 |
| `claim_objects_registered` | `B` | `PASS=30 FAIL=1, GATES A=PASS B=FAIL C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS` | 1 |
| `claim_gravity_supplied` | `B` | `PASS=30 FAIL=1, GATES A=PASS B=FAIL C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS` | 1 |
| `claim_covariance_inherited` | `B` | `PASS=30 FAIL=1, GATES A=PASS B=FAIL C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS` | 1 |
| `claim_subgroup_selected` | `B` | `PASS=30 FAIL=1, GATES A=PASS B=FAIL C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS` | 1 |
| `claim_assembly_decided` | `B` | `PASS=30 FAIL=1, GATES A=PASS B=FAIL C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS` | 1 |
| `break_representation_orders` | `C` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=FAIL D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS` | 1 |
| `break_intertwining` | `C` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=FAIL D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS` | 1 |
| `break_subgroup_class_count` | `C` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=FAIL D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS` | 1 |
| `break_gauge_congruence` | `C` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=FAIL D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS` | 1 |
| `break_star_signs` | `D` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=FAIL E=PASS F=PASS G=PASS H=PASS I=PASS` | 1 |
| `break_star_line` | `D` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=FAIL E=PASS F=PASS G=PASS H=PASS I=PASS` | 1 |
| `break_twisted_census` | `E` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=FAIL F=PASS G=PASS H=PASS I=PASS` | 1 |
| `break_strict_census` | `E` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=FAIL F=PASS G=PASS H=PASS I=PASS` | 1 |
| `claim_shears_killed_by_twisted_covariance` | `E` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=FAIL F=PASS G=PASS H=PASS I=PASS` | 1 |
| `break_p111_commutation` | `F` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=FAIL G=PASS H=PASS I=PASS` | 1 |
| `break_overlap_locus` | `F` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=FAIL G=PASS H=PASS I=PASS` | 1 |
| `claim_positivity_selects_plane` | `G` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=FAIL H=PASS I=PASS` | 1 |
| `claim_parity_selects_plane` | `G` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=FAIL H=PASS I=PASS` | 1 |
| `break_flat_cell_loci` | `G` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=FAIL H=PASS I=PASS` | 1 |
| `break_strict_s3_cells` | `G` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=FAIL H=PASS I=PASS` | 1 |
| `break_star_pattern_cells` | `G` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=FAIL H=PASS I=PASS` | 1 |
| `break_scout_grade_fence` | `H` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=PASS H=FAIL I=PASS` | 1 |
| `break_instance_scope` | `H` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=PASS H=FAIL I=PASS` | 1 |
| `drop_n5_fence` | `I` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=FAIL` | 1 |
| `break_float_absence` | `I` | `PASS=30 FAIL=1, GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=FAIL` | 1 |

## Fix pass and seat provenance (supervisor)

The Fable primary delivered the runner, the note, this file's parts 1–2 and V1–V5 with a passing baseline (29/0) and then died at an expired OAuth token (401) at ~11:52Z (last commit 8f8ee67883). The supervisor: certified the delivered sha (29/0, 167 s); reviewed the runner and note line by line (REVIEW_HISTORY.md — F-A215-1 latent bookkeeping conflation in `constraints()`, no effect; F-A215-2 overlap wording fixed); opened the sealed blind seat (agreement at every point of contact) and folded its strict-`S3` prediction as gate `G-4` (measured 16/16, strict `T` at 0); launched the Opus refuting checker (PASS-NO-BLOCKER, CK-01..CK-11 confirm, CK-12 planted defects could not be run in budget) and folded its CK-11 face-sign rule as gate `G-5` (measured: the 16 star-line cells are exactly the cells with two-offset face products `(+,−,+)` or `(−,+,−)`); set `CHECK_VERDICT` and the fence's DECISION_CUT to the verdict; synced the fence; recertified (31/0) and re-pinned the cache; ran the census above. No measured value, gate or literal of the primary's was changed; two gates were added and measured.
