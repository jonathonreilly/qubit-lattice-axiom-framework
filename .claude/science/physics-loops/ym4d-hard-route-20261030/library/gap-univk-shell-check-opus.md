lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-23T11:55Z

# Check 1416 of row 1412 (`library/gap-univk-shell-astra62.md`)

Checker: Claude Opus 5.5, high effort, Mac mini worker 2. Cross-provider check of
row 1412 (written by gpt-6.2-astra max). Started 2026-11-22T23:55Z (date -u).
Pinned at commit 0ff18a68f. No numeric job run unless stated.

## Plan

1. Read row 1412 in full, and the consumer (check 1405, rows 1404/1400 as needed).
2. Check the binary-slot statement from the printed disc against III 17653-17692.
3. Check the one-link SU(2) counterexample: Haar radial masses, inclusions,
   bound on mu(P), the two lower bounds and exponents, printed hypotheses,
   companion torus, added labels.
4. Check the fixed-profile drift statement.
5. Check the common-interior contraction estimate (convexity, Jacobian
   (1-alpha)^3, injectivity, two uses of the map).
6. Consequence for the consumer of check 1405; next two rows.
7. Verdict, at most ten defects ranked.

## Step 1. Read (done 2026-11-22T23:58Z)

Row 1412 (206 lines) read in full. Printed source III 17630-17700
(Lemma 9.1:lem-ramp-comparison, statement and move (m3)) read in
`~/ym4d-papers/sa-ca/theorem_0_complete_account_raw_III.tex`. The slot bound
(III eq. 9.1:eq-ramp-comparison-3) reads, for each interpolated slot,
|eta^A + s(eta^B - eta^A)| <= (1 + 20 C_chi theta^k |s|) 1{f^B < (1+varpi_0) c};
the text states it without a range of s, and uses it on the disc
|s| <= (20 C_chi N_w^4 theta^k)^(-1) = R. Row 1412's reading ("grant it on the
disc of radius R") is the weaker of the two readings, so its conclusions hold
under either.

## Step 2. The binary-slot statement (section "What the printed disc decides")

Verdict: HOLDS.

Checked by hand. Write b = b_k = 20 C_chi theta^k, a, b' in [0,1] the native
slot values at a common point. For real s, |s| = R, sign chosen with
s(b'-a) >= 0, the left side is a + R|b'-a| >= 0, so the bound gives
R|b'-a| <= 1 - a + bR, i.e. |b'-a| <= b + (1-a)/R. Correct.

- a = 1, b' = 0: take s = -R: 1 + R <= 1 + bR, impossible when b < 1, for
  every R > 0, so "at any volume" is right.
- a = 0, b' = 1: R <= 1 + bR, i.e. b + 1/R >= 1; with R = 1/(V b) this is
  (V+1) b >= 1. So binary slots agree when (V+1) b < 1. Correct.
- Off the enlarged indicator: s = 0 gives a = 0; any s != 0 then gives b' = 0.
  (Row 1412 says "by the affine bound"; true for any nonzero s in the disc,
  not only s = 1.)
- Disc |s| <= 2 (Y 130293-130308 reading): a = 0, b' = 1 is excluded iff
  2 > 1 + 2b, i.e. b < 1/2. Correct. Slot bound for every s: |b'-a| <= b,
  so b < 1 forces equality. Correct.
- Consequences: b < 1 gives a = 1 => b' = 1, so S^A subset S^B when all
  changing factors are binary slots, hence s^A = 0; both shells vanish when
  (V+1) b < 1. On P every native indicator equals one at both ends, so a
  product of indicators has Theta^A = Theta^B on P and d_test = 0. Correct
  (this is CAP(c) of row 1404 as corrected by check 1405 at its scope).

Defect (nit, D-b1): the statement "if every changing outcome factor is such
a binary slot" presupposes that the failure outcome of a recorded failed test
is itself a slot obeying the same affine bound. Row 1412 flags this ("apply
this statement to its actual outcome factor, which may be a complement");
the printed display covers only the small production slots of P, so the
statement applies only to those. No error, a scope note.

Reading of the result: the printed bound is so strong for {0,1}-valued
slots that the moving small slots in the account cannot be literal changing
indicators in the range (V+1) b_k < 1; either they are smooth (positive,
nonconstant) or they do not change. Row 1412 draws this conclusion
correctly.

