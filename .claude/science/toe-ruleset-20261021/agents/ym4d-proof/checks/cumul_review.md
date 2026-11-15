# Independent hostile review of CUMUL

This is a fresh, separate-context Codex review of Codex author work:
**same-family review**, not cross-family review or an audit. I did not
write the author files or inherit the author's derivation conversation.
The reviewed `CUMUL.md` has SHA-256
`a1c239775904835e44fb906a6137c82552e48d64071a6ab775d4f1e4597241a2`.
Line references below refer to that version. Only this review file was
created; no source, audit, ledger or existing check file was changed, and
no commit was made.

I read the CUMUL brief, PROCESS_LIGHT, CUMUL, its criteria, exact-check
implementation and results, the run wrapper/receipt and author log, and
the precise WITNESS, TSE55, REC_LIB, REC_CONT, ASSEMBLY55, PANEL_P1 and
HINT55 clauses identified below. I re-derived the new mathematics. I
checked the reconstruction library's input/output contract; I did not
re-audit all of REC_CONT's upstream proof or any interacting YM producer.
No scientific numerical workload or new numerical probe was run during
this review. File hashes and filesystem metadata were inspected only.

## Findings and dispositions

1. **Comparator and OS transfer: accepted at the stated scope.**
   `CUMUL.md:78-107,109-159`; source contracts
   `REC_LIB.md:149-154,330-349,388-403,437-452,849-864,1082-1119` and
   `REC_CONT.md:43-64,982-1004`.
   In the commutative ring with `z_i^2=0`, Gaussian raw moments are the
   coefficients of `exp(sum mu_i z_i + sum_(i<j) Cij z_i z_j)`.
   The coefficient of a set of n distinct indices in its logarithm is
   the partition cumulant, since k ordered blocks contribute
   `k! (-1)^(k-1)/k`. Hence it vanishes for n>=3 without requiring
   invertibility, zero means or a restriction on spectral support.
   For continuation, each subtuple of an ordered forward-tube tuple is
   admissible because future-cone gaps add. Block products involve
   disjoint slots, so their boundaries are tensor products of tempered
   distributions. Their polynomial tube bounds persist under the finite
   products and sums. Vanishing on the full-dimensional totally real
   ordered Euclidean slice implies analytic vanishing; conversely,
   L-BV's boundary uniqueness transfers a Gaussian Wightman identity
   back to that slice. Tensor Wick conversion contributes the same
   invertible `C^(tensor n)` to every partition term. This is a valid
   conditional use of the landed scalar/finite Cartesian tensor library,
   not a proof that actual YM satisfies its hypotheses. Equivalence
   here is the field-and-vacuum-preserving equivalence of REC_LIB §18.

2. **Free normalization and covariance: accepted.**
   `CUMUL.md:171-212`; `TSE55.md:74-95,129-144`;
   `WITNESS.md:474-486,566-573`.
   With `tr(t^a t^b)=delta_ab/2` and link exponent `sqrt(2N) B`,
   the plaquette term has quadratic coefficient `1/2`.
   The four corners and two orientations, followed by the clover factor
   `1/4`, give `q_u=u^-1 sum_(a,mu<nu) :F^a_mu,nu^2:`.
   Differentiating `D=1/(4 pi^2 |z|^2)` with opposite derivatives at
   the two endpoints gives exactly (C9), including the negative
   electric and positive magnetic entries on the time axis.
   The six-dimensional covariance is
   `Lambda^2(I-2zz^T/|z|^2)/(pi^2 |z|^4)`.
   Orthogonality gives trace square six, and the two pairings give
   `K2=12d/(pi^4 u^2 |z|^8)`. No factor of `2N`, two-form ordering,
   or colour multiplicity is missing.

3. **The rejected cubic candidate really vanishes.**
   `CUMUL.md:216-253`.
   A connected pairing of three quadratic vertices is the triangle,
   with eight leg assignments and one common colour. On two-forms in
   four Euclidean dimensions, `star Lambda^2 H = -Lambda^2 H star`
   for every reflection H, while `star^2=1`. Thus the trace of any
   three covariance matrices equals its negative. This holds at every
   separated triple, not merely the two tested geometries. The free
   scalar `F^2` cubic coefficient is zero. Its explicit treatment as a
   failed proposed nonzero leading term is correct; a nonzero interacting
   cubic function would need a different leading calculation.

4. **Fourth coefficient and actual smooth smears: accepted.**
   `CUMUL.md:224-227,255-322`.
   Four quadratic vertices have three undirected cycles, each with
   sixteen labelled-leg pairings. At the stated collinear centres,
   the inverse fourth-power edge products are
   `1/81, 1/256, 1/20736`; the matrix traces multiply each by six.
   Consequently `96(1/81+1/256+1/20736)=169/108`, and the point ratio
   is `169/(15552d)`. The text correctly does not identify this point
   value with the smeared coefficient A. Equation (C14), with the
   specified bump, defines that coefficient exactly.

   I also rechecked the independent support bound. Each displacement
   error has norm at most `4 epsilon`; the radial-factor error is less
   than `1/500`, and the exterior-square reflection error is less than
   `1/600`. Hence each normalized edge matrix differs from J0 by less
   than `1/250`. Telescoping four factors gives error less than `1/60`
   in operator norm and less than `6/60` in trace. Multiplying the
   positive centre edge weights gives exactly
   `9971/6480 < A < 10309/6480`, contained in `(3/2,5/3)`.
   The distance bound gives `11 < B0 < 13`. Nonnegative unit-integral
   bumps preserve all these inequalities without quadrature. Thus
   `3/(338d) < A/(d B0^2) < 5/(363d)` is proved for genuine smooth
   separated tests; positivity does not rest on floating-point output.

5. **N5 and rescaling: accepted, with the printed distinction essential.**
   `CUMUL.md:53-74,337-372`; `ASSEMBLY55.md:143-152,205-208`;
   `PANEL_P1.md:63-65,87`.
   The general cumulant is a polynomial in fifteen subset moments;
   after centring it uses one fourth and six second moments. Scalar
   products of those moment values do not adjoin coincident field
   products to the separated hierarchy. Therefore fixed-test moment
   convergence passes a strict K4 lower bound as required by N5/N1F.
   Reflection exchanges f2 and f3, so B is the centred OS norm square.
   Under an affine scalar change, `K4 -> a^4 K4` and `B -> a^2 B`.
   The ratio is invariant for a nonzero denominator, while the polynomial
   excludes also degenerate and zero Gaussian fields. The argument
   correctly refuses a globally continuous scale-invariant extension
   through the zero field. N5 consumes K4, not an undefined ratio.
   This preserves N5's analytic form while naming its comparator as
   Gaussian on e; it does not settle the broader OWN-free choice.

6. **Conditional YM implication: accepted; every dynamical input stays OPEN.**
   `CUMUL.md:374-472,474-556`.
   C-ALG, C-SEQ/MOM, C-TR, C-4MATCH, C-2MATCH/UP and C-ORIGINAL specify
   the same actual law, observable, sequence and normalization. The
   separated moment convergence is requested explicitly rather than
   inferred from bounded moments or weak convergence. Equations
   (C18)-(C19) are genuine relative-error matching obligations for the
   connected function and its denominator. The text does not infer the
   four-source logarithmic derivative from orthogonality of covariance
   increments or from PL-1L. The running free-cycle formula has the
   correct factor sixteen; its reference error and interacting error
   are separately left open.

   Fixing a sufficiently large m before the cutoff/volume limit makes
   each total relative error at most one half. The finite upper bracket
   U_+(m) then supplies the positive fixed constants c and b in (C24).
   Dividing the lower P bound by the square of the upper Q bound gives
   `R4 >= 2 A4/(9 A2^2) > 1/(507d)`, as printed. There is no moving
   final witness or hidden separate subsequence. This proves the
   implication from the inputs, not any of those inputs, YM existence,
   a mass gap, unique vacuum, or a uniform large-N statement.

7. **Finite checks and resource provenance: accepted as author evidence,
   not independently rerun evidence.**
   `checks/cumul_criteria.md:19-65`;
   `checks/cumul_exact.py:50-168,171-223,229-313`;
   `checks/cumul_results.json:7-162`;
   `checks/cumul_run.py:20-24,39-78`.
   The pairing enumerator and matrix-cycle evaluation are distinct
   calculations of the contraction. The exact interval operations
   enclose their arguments; lost dependencies only widen bounds.
   The checks have rational endpoints, and the Gaussian subtraction,
   cycle-omission and wrong-factor controls test their stated defects.
   The 25 recorded successes and the separately reported failed
   nonzero-cubic candidate are consistent with the criteria.
   Criteria and script hashes match the result file; its hash matches
   the run receipt. Observed creation times put the criteria before
   the script and the first result. This is supporting provenance,
   not an immutable historical proof in this snapshot without `.git`.
   The wrapper and receipt show an exclusive lock, nice 20, all five
   thread settings one, load below eight, free memory 48%, and a
   combined RSS peak below 1 GB. I did not rerun or overwrite them.

8. **Missing NG-ax primary source: limitation honestly disclosed.**
   `CUMUL.md:560-586`; `CUMUL_LOG.md:12-16,54-58`;
   `HINT55.md:415-419,434`.
   I confirmed that `../ym4d-existence/E/EXISTENCE.md` is absent at
   the requested location. HINT55 supports only an indirect report
   of the decimal and its different corner observable/null class.
   CUMUL explicitly marks the decimal, exact coupling dictionary and
   source formula unverified; it imports none into its coefficient.
   The new free coefficient has one colour loop and order
   `d g_FLOW^8`, unlike the reported `N d g^4` expression. The
   distinction is justified, but it is not a verification of NG-ax.
   Missing that verification does not invalidate the self-contained
   calculation or conditional theorem actually presented here.

9. **The conclusion has the correct comparator and cost boundary.**
   `CUMUL.md:9-16,161-165,588-609`;
   `WITNESS.md:94-110,610-630`.
   The very free-Maxwell composite used to produce K4 is a counterexample
   to interpreting this as exclusion of every free underlying theory.
   The author expressly retains that limitation and excludes only
   elementary generalized-free/Gaussian generators in F2/F3. Arbitrary
   mixtures need not be Gaussian and are not smuggled into that null
   class. Fewer final witness coordinates do not establish fewer YM
   estimates; the comparative verdict is appropriately ARGUED.

## Binding fixes and landing scope

**Binding fixes: none.** No blocking mathematical, normalization,
domain, sequence or source-attribution defect was found in the reviewed
version. No author-file correction is required for this disposition.

LAND applies to the Gaussian comparator, the free cubic cancellation,
the exact fourth-cycle calculation and smooth-smear bounds, the N5
interface, and the expressly conditional YM implication. It does not
promote any OPEN matching, growth, common-hierarchy, trajectory or
original-law estimate, does not verify NG-ax, and does not prove
non-freeness of an arbitrary underlying net. Those existing restrictions
must remain attached to any downstream use.

Credit for the broader constructive Yang-Mills program remains with
Balaban and Dimock; none of their unproved bounds is used to discharge
an input in this review.

VERDICT: LAND
