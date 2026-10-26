# Attempt: exact twisted-pair branch selection and exclusion (J:derive:review-20261016-twisted-pair-exact-branches:a1)

Worker: Claude Sonnet 5.5, same family as the source work, unrefereed. Nothing here is accepted science, a
replacement PR or an audit verdict. Labels: PROVED (full argument in this file), CHECKED (executed by
`check.py`), CHECKED-scratch (executed by me in scratch scripts that are not part of `check.py`), ASSUMED
(premise), READING (interpretation).

## Plain-language summary

The campaign asked whether a one-tick walk on the cubic grid, built from a two-component spin-1/2 coin
plus a sign-twisted copy of it (the "twisted pair" E1/2 + E5/2), can have a massless moving ("Dirac")
copy. The earlier evidence was: nine candidate "line branches" chosen by a numerical test, eight of which
a computer-algebra program (modular, then multi-prime) reported as impossible, and one (axis-flat) as
leaving a 4-dimensional family. Two gaps were open: the nine branches were chosen numerically, and
"impossible" was reported without an explicit written proof.

What this attempt does: (1) it rebuilds the whole setting from the group generators with exact
arithmetic and shows by exact linear algebra that the nine branches are all that exist; (2) for each of
the eight moving branches it produces an explicit certificate, a chain of exact polynomial combinations
of the unitarity equations ending in the constant 1, and replays it from scratch; (3) it shows that
corrupting a certificate, or mis-naming variables the way the old converter did, makes the check fail.
Result in the supplied setting: every such walk with U(0)=1 is flat along the axes, so it has no linear
(Dirac) term at k = 0. The axis-flat branch is non-empty and is left undescribed beyond a few exact facts.

## Sources read (stated as required)

- Read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md` and
  `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (current main checkout,
  `.../scratchpad/main_wt`). The axiom memo says explicitly that Admissibility does not choose a
  Hamiltonian or transfer operator and that a kinetic branch is downstream content (section "Relation To
  Dynamics And Kinetic Branch Selection"). So the unitary tick, the 27-point cell, the coin and U(0)=1
  below are lane-supplied, not axioms. No registered primitive (scale reference, kinetic isotropy, realized
  state) is used.
- Source branch `main` frozen at `2bb6c1a54721e70512922fb10d4495adf8ea3042` (an ancestor of the current
  checkout; `git diff` of the cell note and the campaign directory between that commit and the checkout is
  empty, so the frozen notes are also the current-main notes). All 36 listed objects were fetched with
  `git show` and their sha256 verified (36 of 36 match; see `RECOVERY_STATUS.json`).
- Read in full: the twisted-branch README, `build_branches.py`, `tosing_branch.py`, `spinj_exact.py`,
  `exact_extensions/README.md`, `REVIEW_AGENT_WORK.json`, `HANDOFF.md`, the B7 cell note, and the saved
  Singular inputs/outputs `b*_p.sing`, `b*_Q.out`, `b*_p.out` (the `b0_Q.sing` input was read; hashes of all
  verified).
- Prior-art search: no landed note or open PR on main addresses this obligation (`git grep` for
  `twisted_branches` hits only the campaign directory; `gh pr list --search twisted` returned only
  unrelated candidate-law PRs; `probes/work` has no attempt under this id). Related tasks J-9658-1,2,3,5
  (nearest-site families, signed conventions, torus census) are different objects and are not touched.

## Setting and premises

S1. ASSUMED (lane-supplied). Cell walk on Z^3: A_n in M_4(C), n in {-1,0,1}^3, tick U(k) = sum_n A_n
exp(i k.n). Unitarity of U(k) for all k is equivalent to sum_n A_n A_{n-m}^dag = delta_{m,0} 1 for every
m (a Laurent-polynomial identity). Covariance: A_{Rn} = D(R) A_n D(R)^dag for the 24 proper cubic
rotations R, with D = E1/2 (+) (E1/2 x sign), where sign = -1 on the C4 generators (the character of
S3 = O/V4). Normalisation U(0) = sum_n A_n = 1.

S2. ASSUMED. Reading of "exact exhaustive selection": every walk in S1 is assigned to a branch by its
axis data (below); the branches cover all walks; a branch is excluded when its ideal over Q is the unit
ideal. Characteristic zero follows because the certificates have rational coefficients.

## Steps

1. CHECKED. The group, lifts and block structure. `check.py` builds D by closure from
   (RZ, Dz (+) -Dz), (RX, Dx (+) -Dx) in an exact hand-written Q(zeta_8) class, gets 24 rotations,
   verifies D(R1)D(R2) = +-D(R1R2) for all 576 pairs with one sign for both blocks (so the sign twist is a
   genuine character), exact unitarity, and (1/24) sum |tr D|^2 = 2 (two inequivalent 2-dim blocks).
2. PROVED (Schur). U(0) = sum_n A_n commutes with D, hence U(0) = diag(c1 1_2, c2 1_2) with |c_i| = 1.
   Setting U(0) = 1 is the premise S1 (it removes the relative phase c1/c2; the c1/c2 != 1 case is not
   treated here).
3. CHECKED. Covariant family: `check.py` embeds 22 basis tables M_{n,j} (generated by me from stabiliser
   commutants), verifies exact covariance and one-orbit support, computes dim = (1/24) sum_R fix(R)|tr D_R|^2
   = 22 independently from the character formula, and verifies rank 22 over Q(i). So the tables span the
   whole covariant family: 44 real unknowns (x_j, y_j with p_j = x_j + i y_j).
4. PROVED (line lemma on the x axis). Put z = e^{ik}, k along x. U(z e_x) = sum_{r=-1}^{1} z^r B_r,
   B_r = sum_{n_x = r} A_n. The C4(x) lift D_4 fixes the direction e_x, so D_4 U D_4^dag = U. D_4 has four
   distinct eigenvalues on the four eigenlines of J_x (CHECKED in `check.py`), so U(z e_x) = sum_k u_k(z) P_k
   with P_k the rank-1 projectors, u_k a Laurent polynomial with exponents in {-1,0,1}. Unitarity on |z|=1
   gives u_k(z) conj(u_k(1/z)) = 1 as a Laurent identity; if u_k had lowest exponent a and highest b, the
   coefficient of z^{b-a} in the product is c_b conj(c_a) != 0, so b = a: u_k = c_k z^{m_k}. U(0) = 1 gives
   c_k = 1. Hence B_r = sum_{k: m_k = r} P_k.
5. PROVED + CHECKED (pairing). The rotation C2(y) maps k_x -> -k_x, so covariance gives
   B_{-r} = D B_r D^dag. `check.py` verifies that its lift swaps lines 0<->1 and 2<->3 exactly, so
   m_{pi(k)} = -m_k: m = (a, -a, b, -b), a, b in {-1,0,1}. This alone leaves nine exponent vectors without
   any numerical input.
6. CHECKED. Exact exhaustive selection (replaces the numerical prefilter). For all 81 vectors m in
   {-1,0,1}^4, `check.py` solves the linear system {B_r = sum P_k} over Q by exact elimination in the 44
   real unknowns: exactly 9 are consistent, exactly the vectors of step 5, each with 12 independent
   constraints (32 free unknowns). The 72 others are inconsistent, so they carry no walk. This agrees with
   the nine branches of the saved README, and with 32 free unknowns per branch.
7. CHECKED. No body-diagonal lemma exists for this coin: the C3 lift satisfies D^2 - D + 1 = 0 and tr D = 2,
   so both eigenvalues exp(+-i pi/3) have multiplicity 2 and U on the body diagonal is a 2x2 block per
   eigenvalue, not a monomial. The source pipeline's "body traces" are vacuous for this pair; the branch
   family is the axis family and nothing else was used to choose it.
8. PROVED. Coverage. By steps 4-6 every walk of S1 lies in the affine space S_m of exactly one of the nine
   exponent vectors m = (a,-a,b,-b) (the vector is determined by the walk). The remaining unknowns satisfy
   the unitarity quadrics. Therefore the solution set of S1 is the disjoint union of the nine branch
   varieties, and it is empty on every branch whose quadric ideal is the unit ideal.
9. CHECKED (core new item). For each of the eight branches m with (a,b) != (0,0), `check.py` re-derives
   the 32-unknown branch space by its own exact elimination, forms the needed unitarity quadrics f_i (72 to
   76 per branch, labelled by (m_vec, a, b, Re/Im) from the table embedded in the file) directly from
   products of the matrices A_n(t), and replays an embedded layered certificate: a straight-line list of 29
   to 31 levels, each output being sum_i q_i(t) * (previous-level polynomial i), with q_i explicit
   rational-coefficient polynomials (about 2.2k to 8.4k terms per branch). Level kinds are constant-matrix
   echelon steps (4 or 5 per branch), extension steps (multiplication by single unknowns; one or two, in six of the eight branches) and one-variable
   eliminations (p -> p - q * l with l an affine-linear member). Every replay ends in exactly the constant 1.
   Composition of the levels is an explicit cofactor identity 1 = sum_i c_i(t) f_i(t) over Q; I did not
   expand it flat in `check.py` (CHECKED-scratch: for the two branches with exponents (-1,1,1,-1) and
   (1,-1,-1,1), I expanded it flat, degree 4, 45515 and 10675 cofactor terms, and the identity held;
   I did not expand the other six, so the layered form is the delivered certificate).
   Conclusion: the quadric ideal of each of the eight moving branches is the unit ideal in Q[t_1..t_32],
   hence also over C and over every field of characteristic zero. Meaning for the old record: the saved
   `modStd` "unit ideal" outputs are now backed by explicit, replayable lifts.
10. CHECKED. Mutation controls. (a) Perturbing one cofactor coefficient, (b) swapping two unknowns in the
    generators, (c) applying the certificate of one branch to another branch, (d) flipping the sign of every
    generator's constant, (e) applying a moving-branch certificate to the same-labelled equations of the
    surviving flat branch: all five make the replay return a value different from 1 at a random rational
    point (while the unmutated replay returns exactly 1). Converter controls: with the free unknowns of the
    flat branch named x_i, y_i (the collision situation of the old converter bug), a converter using
    `subs(..., simultaneous=True)` passes the self-test (vanishes at the mapped constant walk), is a
    faithful renaming (converting back reproduces all equations) and its Singular text parses back to the same
    polynomials, whereas a sequential-substitution converter with targets y0, y1, ... is caught: most
    converted equations no longer vanish at the mapped constant walk and variables are merged.
11. PROVED (scoped proposition; proof = steps 4 to 9, finite parts verified by `check.py`). In the setting
    S1 every walk has B_{+1} = B_{-1} = 0, B_0 = 1, i.e. U(t e_x) = 1 for all t, and likewise on the other
    axes by covariance. In particular dU/dk(0) = i(B_1 - B_{-1}) = 0 along every axis, so there is no linear
    term at k = 0 in any direction (the three velocity matrices are rotations of each other). The
    unadopted "doubler at X" of the older numerical solution is the same statement (X = (pi,0,0) lies on
    an axis).
12. CHECKED. The survivor (0,0,0,0) is non-empty and not reduced to one point. (i) The constant walk
    A_0 = 1 lies on it (exact). (ii) The Zariski tangent space of the 336 equations at the constant walk has
    dimension 16 (exact rank over Q); this is an upper bound on the local dimension at that point and is not
    a dimension claim. (iii) Unitarity implies 14 independent affine-linear equations on the 32 unknowns
    (replayed exactly from an embedded straight-line list), so the survivor lies in an 18-dimensional affine
    subspace. (iv) CHECKED-numerical: unrestricted least-squares searches on the 44 real unknowns from random
    starts converge only to axis-flat walks (every converged solution in the run), and they include
    non-constant walks; searches forced into moving branches never converge. This is corroboration, not a
    proof of anything, and its counts depend on the run.
13. CHECKED-scratch. Alignment with the saved files. The span of the 336 quadrics per branch has rank
    72, 74, 76, 74, 72, 74, 76, 74, 72 in `check.py`'s ordering of (a,b); the same ranks (with 62 independent
    quadrics and 10, 12 or 14 independent affine-linear combinations) appear in the saved `b0..b8_p.sing`
    in the order 76, 74, 72, 74, 72, 74, 72, 74, 76. The multisets agree; the saved labels b0..b8 correspond
    to `check.py`'s (a,b) with the block-2 orientation reversed (b -> -b). This does not matter for the union
    of branches. The branch with exponents (0,0,0,0) and rank 72 is the one the saved run reports as dim 4.
14. READING. In this supplied range-one E1/2 + E5/2 setting with U(0) = 1, a massless moving copy at k = 0
    does not exist, because the velocity matrices vanish. The earlier note's statement that "no universal
    axis-flatness or cone exclusion follows" referred to the lack of exact selection and certificates; with
    them, axis-flatness does follow inside S1. It still does not follow outside S1 (other cells, ranges,
    U(0) with c1 != c2, other coins).

## What is new relative to the sources

New: exact (not numerical) branch selection with the C2(y) pairing and an exhaustive 81-vector exact
check; explicit replayable characteristic-zero cofactor-type certificates for all eight moving branches;
mutation controls including the simultaneous-variable converter; the consequence step 11; the exact
facts in step 12 (14 linear consequences, tangent dimension 16); the observation in step 7 that the body
diagonal gives no monomial lemma here.

Not new: the nine-branch list, the 32 unknowns / 336 distinct quadrics count (reproduced in scratch, CHECKED-scratch; `check.py` verifies the 32 and the used subset), the unit-ideal and dim-4 outputs
(reproduced, not extended), the existence of the constant walk, the formula for the line lemma.

## First unresolved step

Step 12 is where the route stops. The exact description of the survivor is open: its irreducible components,
dimension, reducedness over Q (the saved mod-p/modStd output says dimension 4; this attempt shows only 14
linear consequences and tangent dimension 16 at the constant walk), and whether any of its members has band
touching or a Dirac-type point away from k = 0. Closing it needs a Groebner or primary-decomposition
computation on the 18 remaining unknowns (54 independent quadrics after elimination in the scratch run),
which no installed tool here provides. Also uncovered: U(0) with c1/c2 != 1, ranges above one, other cells,
and a flat expansion of the layered certificates. The layered certificates were generated by my own scratch
code; `check.py` verifies them but a referee should treat equality of my reconstruction with the lane's
(same equations up to linear change of variables) as supported by steps 3, 6, 13, not proved.

## Files

`check.py` (self-contained, embeds the covariant tables and certificates), `RECOVERY_STATUS.json`, and
`gen/` (scratch generators: the code that produced the tables and certificates; not needed by `check.py`).

## Run record

`python3 check.py`: `TOTAL: PASS=41 FAIL=0`, runtime about 200 s (3.3 min, one process, well under 1.5 GB), exit code 0. The
numerical section uses a fixed seed but time-capped loops, so the count of converged random starts varies with machine load (4 to 9 seen); its
pass condition is only 'at least one converged and all converged ones axis-flat'.
