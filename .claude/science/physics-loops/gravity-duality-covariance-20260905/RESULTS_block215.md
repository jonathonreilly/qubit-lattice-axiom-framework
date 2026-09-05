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
