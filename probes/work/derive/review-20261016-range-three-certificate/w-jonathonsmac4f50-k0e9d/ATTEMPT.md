# J:derive:review-20261016-range-three-certificate:a1 -- range-three cubic walk obstruction

Same-family (Claude Sonnet 5.5), unrefereed, computer-assisted. Nothing here is accepted
science, an audit verdict, or a replacement PR. No repository file was edited.

## Plain-language summary

The earlier campaign claimed that a one-qubit walk with hops of up to three sites per axis,
that looks the same after any proper cubic rotation (with the coin turned by the spin-1/2
lift), cannot move. The claim rested on archived scripts that mixed a numerical filter with
exact checks, and on a Singular run the repository cannot reproduce. This attempt rebuilds the
whole argument from the axioms' lattice data with exact arithmetic and no Singular:

1. It lists every exponent branch of the "line" stage (4,405,492 of them) and tests each one
   exactly. Only the trivial branch survives. No branch is discarded by a numerical filter.
2. For the trivial branch it finds a short explicit rational identity that forces one
   unknown (`y0`) to zero, and reduces the rest to 50 homogeneous quadrics in 20 unknowns.
3. It proves that every degree-5 monomial lies in the ideal of those quadrics, by an exact
   rank computation modulo a prime. Because rank over Q is at least rank modulo any prime,
   this is a characteristic-zero statement, and it covers all complex solutions.

What is NOT delivered: explicit cofactor identities `y_i^5 = sum h_j e_j` over Q (the
certificate is a rank statement, not a list of cofactors), a human-readable proof of step
S9, independent referee review, or anything about ranges four and above.

Verdict label: NEW RESULT (scoped), computer-assisted, same-family, unrefereed.

## Documents read first (as required)

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (all 233 lines, current main) and
  `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (all 130 lines). The four axioms
  give Z^3 with proper cubic rotations (Lattice), the one-site algebra M_2(C) (Qubit), a
  nearest-neighbour admissibility rule, and records. They state no dynamics, no walk, no tick
  and no coin action. The approved primitives (scale reference, kinetic isotropy, realized
  state) add nothing used here. So every item below is a mathematical hypothesis of a lane,
  not framework content (main_wt `docs/MINIMAL_AXIOMS_2026-06-29.md:33-83, 114-130`).
- Corrected current-main note `docs/CUBIC_COVARIANCE_FREEZES_A_ONE_QUBIT_TICK_CELL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-10-16.md`
  (current main, last touched by `c9a4b623ac`) and the scope checklist
  `.claude/science/review-fixes/review-drain-20261016/CUBIC_TICK_SCOPE.md:46-53`, which lists
  this obligation ("reproduce the range-three coefficient systems and all exact branch
  eliminations without a numerical discard; independently verify the radical certificate
  over Q"). The current-main note withdraws the range-three theorem (its section "Range-three
  extension -- archived proof candidate, not established here"). This attempt does not
  restore that theorem by citation.
- Frozen source branch `claude/toe-campaign-24h-20261015` at
  `b0178fa585cad5ac9e02e70dff2175593dbc5dab`. All five source objects were extracted with
  `git show` and their sha256 matched the task's values (see `RECOVERY_STATUS.json`).
  Frozen-commit note = Theorem 4' (the withdrawn statement); `fastR3.py` (line stage; the branch search discards
  branches by a float `lstsq` test with tolerance 1e-9, `fastR3.py:162-165`, and only the
  survivors are tested exactly, `fastR3.py:178`); `exact_recheck_R3.py` (exact recheck of the
  2548 choices on the other three lines with the three Gamma-line exponents fixed at 0,
  `exact_recheck_R3.py:10,23`; the exact Gamma-line check itself came from an earlier script,
  `fastR.py`, that is not among the frozen source objects); `r3_triv.sing` / `r3_triv_p.sing`
  (21 variables, 122 equations; `modStd` over Q resp. `slimgb` mod 32003).

## Setting and premises (all ASSUMED unless marked)

A1 (ASSUMED, lane model). Walk U(k) = sum_{n in {-3..3}^3} A_n e^{i k.n}, A_n in M_2(C),
unitary for real k (range three per axis; 343 hop sites).
A2 (ASSUMED, lane model). Full-soldered covariance U(Mk) = D(M) U(k) D(M)^dagger for all 24
proper cubic rotations M, D the spin-1/2 lift. Other coin actions and subgroups are not
treated here.
A3 (PROVED below, S1). Determinant reduction: U = e^{i theta} V, V = f + i g.sigma, f real
O-invariant, g real O-equivariant trig polynomial of range <= 3, f^2 + g.g = 1.
A4 (relaxation, ASSUMED for strength). The proof below uses only the polynomial identity
f^2 + g.g = 1 with complex coefficients, f O-invariant, g O-equivariant, range <= 3. So it
proves the statement for all complex SL(2,C)-valued covariant Laurent polynomials, which
contains every unitary walk. This is how "all algebraic branches" is covered.

## Numbered steps

**S1 (PROVED; also stated in the frozen note, Theorem 0).** det U is a Laurent polynomial
with det U . conj(det U) = 1 on the torus, hence a unit monomial c z^m of modulus-one c.
Covariance gives det U(Mk) = det U(k); O fixes no nonzero vector, so m = 0. Put V =
c^{-1/2} U. Then V in SU(2) pointwise, V = f + i g.sigma with real f, g of the same support,
f(Mk) = f(k), g(Mk) = M g(k), f^2 + |g|^2 = 1. Not new.

**S2 (CHECKED by check.py, new reconstruction).** Function spaces rebuilt by exact
Reynolds averaging over the 24 rotations on the 343 product basis {1, cos jk, sin jk}^3
(not using the repository's `cell` module): 21 invariant scalars, 42 equivariant vectors,
63 real unknowns. Dimension confirmed by the character formula and by exact rational
checks of f(Mk) = f(k), g(Mk) = M g(k) at random rational momenta (tan(k/2) rational) for all
24 rotations. Matches the counts quoted in the frozen note.

**S3 (PROVED; frozen note, Theorem 4' "line lemma" -- reproved here over C).** Let b be a
momentum in {0,pi}^3, e a direction, and suppose (i) the stabiliser (in O) of the line b + t e
fixes only multiples of e, and (ii) the stabiliser of the point b fixes no nonzero vector.
Then g(b + t e) = gamma(t) e/|e| and g(b) = 0, so f(b) = eps = +-1. With P = f + i gamma,
P (f - i gamma) = f^2 + gamma^2 = 1 in the Laurent ring C[z, 1/z], z = e^{it}. Both factors
are units, so P = lambda z^n, f - i gamma = lambda^{-1} z^{-n}; at z = 1, gamma = 0 gives
lambda = eps = +-1. Hence f = eps cos(n t), gamma = eps sin(n t), with |n| <= (range) |e|_1.
The argument is over C (lambda cannot be a non-real branch). The hypotheses (i), (ii) are
checked exactly for the six lines used (CHECKED).

**S4 (ASSUMED line list; CHECKED hypotheses).** Six lines: Gamma + t(1,0,0), (1,1,0), (1,1,1);
(0,0,pi) + t(1,0,0), (0,0,pi) + t(1,1,0); (0,pi,pi) + t(1,0,0). These are the lines of the
frozen note. A branch is (n_1..n_6, eps_X, eps_M) with eps_Gamma = +1 (absorbed in the global
sign, U -> -U). Exponent ranges 7, 13, 19, 7, 13, 7. Using only a subset of the lines is
sound (every line condition is necessary).

**S5 (CHECKED, exact; this removes the "numerical discard").** The line conditions are the
linear system L x = t(branch) for the 63 unknowns, 132 rows, rank L = 42 (left null space of
dimension 90, `N L = 0` verified exactly). Consistency of a branch is `N t = 0`. The irrational
lengths |e| in {1, sqrt2, sqrt3} are handled by splitting `N t = 0` over the Q-independent
numbers 1, sqrt2, sqrt3. All 1729 x 2548 = 4,405,492 branches are tested by an exact
meet-in-the-middle (hash join on exact rational vectors). Exactly one branch is consistent:
all exponents 0 and eps = +1. The old pipeline's float prefilter is not used, and the Gamma-line
exponents are not fixed in advance (they are enumerated jointly with the others). Positive controls (D4-covariant, range one, two lines): the same
machinery keeps the trivial branch and both axial-shift branches n_z = +-1 (it also keeps
other exponent pairs, since lines give only necessary conditions), and the known walk
exp(i k_z sigma_z) satisfies the exact line system of the branch n_z = 1 directly. So the
exact test does not reject genuine moving walks.

**S6 (CHECKED).** On the trivial branch the solutions of L x = t form an affine space of
dimension 21: f = 1 + y0 phi0 with phi0 = sum_sigma sgn(sigma) sin(k_s1) sin(2 k_s2) sin(3 k_s3)
(an O-invariant that vanishes on all six lines), and g = sum of 20 g-directions y1..y20.
This is a different parametrisation from the archived one but has the same dimension.

**S7 (CHECKED).** f^2 + g.g - 1 expanded exactly in the trigonometric basis of range 6
gives 459 nonzero mode equations, quadratic in the 21 unknowns, linear only in y0 (only
through 2 y0 phi0 on the six modes sin(a k1) sin(b k2) sin(c k3), {a,b,c} = {1,2,3}). The
expansion is verified exactly at random rational momenta against the direct evaluation.

**S8 (CHECKED, explicit rational identity).** y0 = sum_m c_m E_m with rational constants c_m
(E_m the 459 mode equations; the solve found a combination with 9 nonzero c_m). check.py
solves for the c_m by exact linear algebra over Q and verifies the polynomial identity
exactly (all quadratic terms cancel, only y0 remains). The identity is a consequence of
which modes carry y0 linearly, not of a numerical coincidence, but it is not printed in
the output; it is recomputed on every run. So y0 lies in the ideal
and f = 1.

**S9 (CHECKED, characteristic-zero by rank semicontinuity; NOT a cofactor identity).** With
y0 = 0 the 459 equations span 50 homogeneous quadrics in y1..y20 (exact RREF over Q, scaled
to primitive integer generators e_1..e_50). Let M_5 be the integer Macaulay matrix whose
rows are y^beta e_j (|beta| = 3) in the 42,504 monomials of degree 5. check.py computes, in
exact arithmetic mod p (p = 32003, and again p = 31991 with a different variable order and
different random overlaps), the Hilbert function of Q[y]/(e) by an incremental
standard-monomial method (resolving overlaps of leading monomials): HF(0..5) =
1, 20, 160, 577, 470, 0, total 1228. HF(5) = 0 says rank_p M_5 = 42,504 = number of columns. For an integer
matrix rank_Q >= rank_p, so rank_Q M_5 = 42,504: every degree-5 monomial, in particular
y_i^5, lies in the Q-ideal (e). Hence on the trivial branch the complex variety is {0}.
Cross-checks: dense Macaulay elimination (different algorithm) reproduces HF(3) = 577 in all
four class blocks and HF(4) = 112 in class block (1,0) (during development, all four degree-4
blocks, 124, 117, 112, 117, were reproduced densely; check.py repeats only one block to
save time); the sum 1228 equals the `vdim` printed by the archived Singular run
(`r3_triv.out`, a log read at the frozen commit, not an independent proof); the archived
`r3_triv.sing` itself reduces (one linear equation in one variable, 50 independent
quadrics) to an ideal with the same Hilbert function, which is evidence that the
reconstruction matches the archived system up to a change of variables; the first 40 of the
50 quadrics give HF(5) = 49 > 0 (non-vacuity control).

**S10 (assembly; PROVED only conditionally on the CHECKED steps S2, S5-S9 being correct).** Under A1-A2 (indeed A4) every range-three
O-covariant walk has V = 1, i.e. U = e^{i theta} (constant phase): any such walk has the
line exponents all zero (S5), then y0 = 0 (S8), then all quintic monomials vanish on the
solution set (S9), so g = 0 and f = 1. The only non-elementary inputs are the correctness of
check.py's exact computations (S2, S5, S7-S9). Treat this as a computer-assisted proof, not
as a human-verifiable proof.

## What is new relative to the sources, and what is not

Not new: S1, S3 (frozen note Theorems 0 and 4'); the six lines; the count 63 unknowns; the
conclusion "range three is frozen" (the frozen commit claimed it).

New in this attempt (CHECKED, all in check.py):
1. A Singular-free, source-code-free reconstruction of the range-three coefficient system
   from the stencil (S2, S6, S7).
2. An exhaustive exact line stage over all 4,405,492 branches with no numerical prefilter
   and no fixed-exponent shortcut on the Gamma lines (S5), with a positive control.
3. The observation that the trivial branch leaves a single f-direction phi0 and that
   `y0 = 0` follows from an explicit rational combination of the unitarity equations (S8).
4. A characteristic-zero ideal-membership certificate for the remaining 20-variable system
   that needs only mod-p linear algebra: m^5 is in the ideal (S9). Its Hilbert function
   (1, 20, 160, 577, 470) reproduces the archived Singular `vdim` 1228.

## First unresolved step

The ideal-membership certificate S9 is a rank certificate: it does not print cofactors
`h_j` with `y_i^5 = sum_j h_j e_j` over Q. The first unresolved step is therefore a
cofactor-level, independently re-checkable identity (for instance a p-adic lift of the
mod-p solution to Q), and a human-checkable argument for g = 0 given f = 1 and g.g = 0
(equivalently, why no isotropic equivariant vector field of range <= 3 vanishes on the six
lines but not everywhere). Beyond that: other coin actions, subgroups, range four and above
are untouched. An independent (different-family) re-run is not done. Range four (67 unknowns after the line
stage according to the frozen note) is untouched; whether the standard-monomial method scales
to it is not tested (suggested only: the quotient would be much larger).

## Run record

`python3 check.py` (this directory, `check_output.txt`): TOTAL: PASS=24 FAIL=0, wall 106 s on
a heavily loaded machine (user 39 s), peak RSS about 0.5 GB, one process. The run prints one
HIT line (scoped as above). Development observations not in check.py: sympy `groebner`
(f5b, mod 32003) on the 51 equations did not finish in about 7 CPU minutes, so the closure
uses the standard-monomial method of check.py instead.

## Overlap and related tasks

Searched: landed notes and scripts on current main (`docs/`, `scripts/cubic_covariant_*`),
`gh pr list` for range-three/cubic-walk terms (only the closed #9636, which landed the
corrected note and withdrew the range-three theorem, and an unrelated open scale-ladder PR),
and the ai/probes view (`probes/tasks/review-science-20261016.json`, `probes/TASKS.json`,
`probes/work/review-science-20261016/README.md` mention the obligation; no earlier attempt
for it). The sibling obligations in `CUBIC_TICK_SCOPE.md:46-53` (E, spin-1, spin-3/2 coin
eliminations; band-touching on the torus; signed-generator reconciliation) are separate and
untouched.

## Disjoint check

`check.py` shares no code with the archived scripts, does not import the repository's
`cell` module and does not call Singular. It reads `./src/r3_triv.sing` only for the
optional comparison with the archived input. Same-family limitation: the same model wrote
check.py and this note.
