# Independent hostile review of CUMUL

**Disposition: LAND at the stated conditional scope. Binding fixes: none.**
This is a fresh-context, same-family Codex review under
`briefs_q/CUMUL/REVIEW.md`, dated 2026-10-30 UTC (2026-10-29 local).
I did not author CUMUL or inherit its author's conversation. The earlier
review was not used to establish any mathematical conclusion below; its
identity and verdict were inspected afterward as provenance.

All CUMUL line numbers refer to the 640-line file with SHA256
`50f337bffacc0e49b7e3bc737609190bd106d8b9210c2ab8f1059745cc1bcfd8`.
I read the reviewer and author briefs, PROCESS_LIGHT, CUMUL, its log and
check implementation, and the source passages identified below. I
re-derived the new mathematics and checked the exact contracts consumed
from the landed reconstruction library. This is not a new audit of all
upstream REC_CONT proofs or of any interacting Yang–Mills producer.
Only this review file was created or edited; no commits were made.

## Reviewer check registration

Registered before executing any scientific calculation in this review.
These are additional reviewer checks, designed after reading the author's
proof and existing results; they are not represented as blind predictions
or as the author's original preregistration. The reviewer brief restricts
writes to this file, so registration and results remain here.

1. Replay the unchanged `checks/cumul_exact.py` with stdout captured in
   memory. All 25 checks must pass, and their exact scientific records
   must equal the saved `checks/cumul_results.json`. Do not run the
   author's wrapper, which would write other files.
2. Independently enumerate all normal-ordered Wick matchings, including
   disconnected ones, and obtain the fourth cumulant by subtracting the
   three pair products. At the stated collinear centres, require the
   stripped two-point coefficient 12, third cumulant 0, fourth cumulant
   169/108, and ratio 169/15552 for one colour. Connected pairing counts
   must be 2, 8, 48, with four-cycle multiplicities 16, 16, 16.
3. At the additional rational configuration
   `(0,0,0,0), (1,2,0,1), (-1,1,2,0), (2,-1,1,2)`, check the
   differentiated curvature kernel against the exterior-square formula,
   its Hodge anticommutator, and the raw-moment-minus-pair-products
   fourth cumulant against the three-cycle formula. The first three
   points must have zero third cumulant. These finite samples supplement
   the general written derivations; they cannot establish a universal
   identity by themselves.
4. With exact rational arithmetic, verify every scalar threshold used in
   CUMUL lines 293–322: the radial 1/500 bound, angular 1/600 bound,
   kernel 1/250 bound, four-factor 1/60 bound, the stated interval
   9971/6480 to 10309/6480 inside (3/2,5/3), and the two-point bounds
   inside (11,13). Verify `(2/9)(3/338)=1/507`.

Execution must be serial with an exclusive lock on the existing numeric
lock file opened read-only, nice at least 10, all five documented library
thread settings equal to one, load1 below 8, native free memory at least
30%, combined RSS below 800 MiB, and a 90-second limit for each check
process. No bytecode or result files may be generated. A guard or check
failure must be retained as a failure, not relaxed or hidden.

## Itemized verdicts

1. **Fixed field, admitted tests and denominator — PASS.**
   CUMUL **lines 18–74**, compared with WITNESS **lines 49–68, 447–469**
   and REC_LIB **lines 114–130, 149–166**.

   The coordinate half-width is epsilon, so adjacent time supports have
   gap at least `1-2 epsilon>0`. Every distinct-subset tensor is a compact
   off-diagonal test in the stated flat space. The normalized product
   bump has integral one; its evenness gives `theta f3=f2` and
   `theta f4=f1`. Thus the centred `C23` really is the reflection-positive
   norm square of the positive-time one-insertion vector. Products in
   the cumulant formula are products of numerical moments, so the proof
   does not adjoin an inadmissible coincident power. A common translation
   puts the ordered tuple in positive time without changing an invariant
   limiting hierarchy's values.

   **Fix:** none. Retain the specified observable, centring, `Z(a)=1`
   and separated-domain restrictions.

2. **Gaussian comparator, including means and tensor components — PASS.**
   CUMUL **lines 78–107, 161–165**; comparator definitions checked against
   WITNESS **lines 94–110, 604–630**.

   In the ring `R[z1,...,zn]/(z1^2,...,zn^2)`, each coefficient of the
   Gaussian moment polynomial comes from a partition into singletons
   and pairs. Consequently it is exactly
   `exp(sum mu_i z_i + sum_(i<j) Cij z_i z_j)`. The coefficient of a
   partition with k blocks in its logarithm is
   `k! (-1)^(k-1)/k = (-1)^(k-1)(k-1)!`, the coefficient in (C3).
   The logarithm has no terms of degree three or higher. This does not
   use positive definiteness, an invertible covariance, convergence of
   an exponential moment, or a restricted KL spectral support. Tensor
   tests and affine combinations just give another mean vector and
   bilinear covariance. Setting every covariance to zero is included.

   This proves the requested null statement for elementary F2 and F3
   on the named generators. It does not prove it for Wick composites,
   or for mixtures that are no longer Gaussian; CUMUL states those
   limitations explicitly.

   **Fix:** none. Keep “elementary” and “on e” attached to the comparator.

3. **Transfer through OS reconstruction — PASS, conditional on the
   printed library hypotheses.** CUMUL **lines 109–159**; sources
   REC_LIB **lines 149–154, 330–349, 388–448, 847–864, 1082–1103** and
   REC_CONT **lines 43–64, 984–1004**.

   The input is the full common-triple E0' bound together with
   normalization, reality, covariance, permutation symmetry and RP.
   The sources do supply matching holomorphic functions and the stated
   boundary theorem under that contract; two-point estimates alone are
   not being substituted for it.

   For a subtuple, an imaginary gap is a sum of original future-cone
   gaps. Its cone margin is at least the sum of their margins, so the
   subtuple's polynomial tube bound is controlled by a bound on the full
   tube. Products associated with a partition use disjoint variable
   slots. Their boundaries are tensor products, so there is no illegal
   multiplication of singular distributions in the same variables.
   The resulting finite cumulant sum has the required growth.

   Gaussian Euclidean matching makes this analytic cumulant zero on an
   open totally real slice. Taylor uniqueness and connectedness give
   zero throughout the tube, hence zero boundary. Conversely, a
   Gaussian reconstructed state makes that boundary zero, and L-BV
   uniqueness forces the analytic cumulant, and then its Euclidean
   matching value, to vanish. This proves the needed contrapositive.
   Contact distributions annihilate the flat tests and do not alter
   the argument. The tensor dictionary contributes the same invertible
   `C^(tensor n)` to every partition term. Its scope is exactly the
   stated finite Cartesian tensor class. The equivalence used here
   preserves both the fields and the distinguished vacuum, as in
   REC_LIB's theorem.

   **Fix:** none. Reconstruction is a legitimate named library input;
   its actual YM hypotheses remain obligations.

4. **Wilson normalization and free curvature kernel — PASS.**
   CUMUL **lines 169–212**; TSE55 **lines 129–144, 185–199** and
   WITNESS **lines 474–480, 566–573**.

   Expanding `exp(i sqrt(2N) B^a t^a)` with
   `tr(t^a t^b)=delta_ab/2` gives `s(U_p)=(dB)^2/2+O(B^3)`.
   The action is therefore `u sum(dB)^2/2`. Each plaquette has four
   clover corners and two ordered orientations: its source coefficient
   is `sum_corners f/2`, and its quadratic coefficient is
   `sum_corners f/4`. After `B=A/sqrt(u)`, the continuum reference is
   `q=(1/u) sum_(a,mu<nu) :F_mu,nu^a F_mu,nu^a:`. This checks the
   ordered-index factor of two in (C8) and the coupling dictionary.

   Direct differentiation gives
   `pi^2 D_mu,rho = -delta_mu,rho/(2s^2)+2z_mu z_rho/s^3`.
   Applying the two exterior derivatives, with the minus sign from
   differentiating the second endpoint, gives (C9). Expanding the
   two-by-two minors of `H=I-2zz^T/s` gives the same kernel. Since H is
   an orthogonal reflection, `tr G(z)G(-z)=6/(pi^4 |z|^8)`.
   Two Wick pairings and d independent colours give exactly
   `12d/(pi^4 u^2 |z|^8)`, with no fitted matching factor.

   **Fix:** none. The calculation is for the free reference, as stated.

5. **Connected contractions and rejected cubic candidate — PASS.**
   CUMUL **lines 214–253**.

   Normal ordering removes self-edges. Every vertex has degree two, so
   a connected graph with n>=3 vertices is a single cycle. Each vertex
   assigns its labelled legs in two ways; an undirected cycle therefore
   contributes `2^n` pairings. There is one triangle and three four-cycles,
   hence 8 and 48 pairings; n=2 instead has two parallel-edge pairings.
   Colour conservation around a connected cycle gives one factor d,
   and the two-form sum is the ordered matrix trace. Reversing the cycle
   transposes the matrix product and leaves that trace unchanged.
   These facts give all factors in (C11).

   On middle-degree forms in four Euclidean dimensions,
   `star Lambda^2 H = det(H) Lambda^2 H star = -Lambda^2 H star`.
   Three such factors anticommute with star; conjugating their product
   by star changes its sign but preserves its trace. Thus the separated
   cubic coefficient is identically zero, not merely zero at the chosen
   collinear configuration. This is a failure of this proposed free
   leading term, not an obstruction to an interacting three-point
   witness. The author's rejection is correctly scoped.

   **Fix:** none. Preserve the explicit failed-candidate report.

6. **Fourth coefficient and smooth-test positivity — PASS.**
   CUMUL **lines 255–322**.

   At the four centres the three cycle traces, with pi factors removed,
   are `2/27`, `3/128`, and `1/3456`. Multiplication by 16 gives
   `169/108`; division by `12^2` gives `169/15552`. Restoring colour,
   coupling and scale gives exactly (C13), including `d/u^4` and
   `lambda^-16`.

   The genuinely smeared coefficient is the exact integral A in (C14),
   not the point coefficient. On each support edge,
   `|delta|<=4 epsilon`, and the radial factor differs from one by less
   than `1/500`. The projection-angle estimate gives
   `||H-H0||<=8 epsilon/(l-2 epsilon)`; telescoping the exterior square
   doubles that bound, giving `||J-J0||<=8/4999<1/600`.
   Hence `||l^4 Gtilde-J0||<1/250`. Telescoping four factors bounds the
   product error by `(251/250)^4-1<1/60`; the trace error is at most
   six times that. The resulting bounds are exactly
   `9971/6480 < integrand(A) < 10309/6480`, inside `(3/2,5/3)`.
   The distance bounds similarly put the B0 integrand between
   `12(2500/2501)^8` and `12(2500/2499)^8`, inside `(11,13)`.
   Positive unit-integral bumps preserve these bounds. No evaluation
   of the transcendental bump normalization is needed for the sign.

   Thus (C14) is an exact specification of the coefficient, and the
   rational bounds rigorously certify the part that is load-bearing.
   Positivity is specific to this test geometry: the independent
   noncollinear check below has a negative fourth cumulant. CUMUL
   does not claim positivity for arbitrary four-tuples.

   **Fix:** none. Retain the distinction between point and smeared values.

7. **Finite checks, controls and reported status — PASS.**
   CUMUL **lines 324–335, 626–631**; `checks/cumul_criteria.md`,
   `checks/cumul_exact.py:94–168,171–223,229–317` and the saved receipts.

   I inspected the pairing enumeration, independent derivative/minor
   kernels and exact interval operations. Each operation encloses its
   image; division excludes zero and the square operation treats
   intervals crossing zero correctly. Treating correlated edge
   displacements independently enlarges the enclosure rather than
   invalidating it. The error controls distinguish a factor-eight
   substitution, a missing cycle and an omitted Gaussian subtraction.
   The formal arbitrary-mean identity also covers zero covariance.

   The unchanged script reproduced all 25 saved scientific records
   exactly. My separate computation included disconnected Wick
   pairings and then subtracted them; it did not assume that the
   connected-cycle enumeration was the cumulant. Its results and
   resource receipt are recorded below. No reviewer check or guard
   failed. The nonzero cubic proposal remains a failed candidate;
   a successful check that its coefficient is zero is not evidence
   that the proposal succeeded.

   The criteria file, result-bound hashes and author log document the
   author's preregistration. A source snapshot alone cannot independently
   establish the historical order of file creation; no such inference
   is needed for the algebraic proof or this replay.

   **Fix:** none. Finite exact checks validate the stated free calculations,
   not any interacting estimate.

8. **Finite-moment N5 interface and scale-free display — PASS.**
   CUMUL **lines 337–372**; ASSEMBLY55 **lines 143–152, 205–208** and
   PANEL_P1 **lines 54–65, 85–87**.

   With general means, (C3) is a polynomial in 15 nonempty-subset
   moments. With centring, it uses one S4 and six S2 coordinates.
   Polynomial continuity passes a fixed positive K4 bound along their
   common convergent sequence. These are local separated data, and
   item 3 supplies the quotient argument. This is precisely N1F's
   finite-coordinate closure step. N5's analytic form needs no change;
   its named comparator must be the Gaussian e-field class. It cannot
   be left implicitly equal to all underlying free physical theories.

   Deterministic shifts change only the linear part of the logarithm;
   a scalar rescaling multiplies K4 by `a^4` and B by `a^2`. Therefore
   `K4/B^2` is invariant for nonzero a on B>0. Gaussian fields with
   B=0 still have K4=0 and are excluded by the polynomial witness.
   A nonconstant scale-invariant functional cannot be continuous at
   the zero moment tuple: scaling any tuple to zero would force all
   its values to coincide. The author correctly uses the polynomial
   for N5 and does not claim a continuous 0/0 extension.

   **Fix:** none. The denominator margin is essential for the ratio's
   limiting statement, even though K4 alone separates Gaussian fields.

9. **YM obligations and proposed PL-4C producer — PASS as an explicit
   OPEN contract.** CUMUL **lines 374–524**; WITNESS
   **lines 474–595**, TSE55 **lines 129–165, 200–212**.

   C-ALG asks for the actual common hierarchy and all reconstruction
   inputs. C-SEQ/MOM asks for convergence and test-space extension on
   one sequence. C-TR fixes the actual trajectory and two-sided coupling
   bounds. C-4MATCH and C-2MATCH/UP demand the normalized connected
   four-point and denominator estimates plus pair bounds. C-ORIGINAL
   retains every original-law normalization, background, terminal and
   large-field contribution. None is inferred from the free calculation.

   Dense-test convergence plus uniform seminorm bounds extends to
   the exact fixed bumps by approximating each test in that seminorm
   and applying the triangle inequality. The text correctly asks for
   actual moment convergence; weak convergence alone would not suffice.
   All-order reconstruction is separately required and is not supplied
   by these seven coordinates.

   At a finite regulator, differentiating the logarithm of the normalized
   source integral gives the fourth cumulant, including every disconnected
   subtraction. The free Gaussian trace formula (C20) follows from the
   same Wick combinatorics as item 5. Conditional-expectation
   orthogonality is a covariance identity and does not remove mixed
   terms in a fourth cumulant. No such incorrect slice reduction is used.
   Four-factor telescoping changes `O(u^-1)` kernels by `O(u^-2)`
   errors at order `O(u^-5)`, the power in (C22). The uniform separated
   kernel hypotheses and their application are still expressly required.
   The genuinely interacting difference in (C21) is not a consequence
   of LGF, FLOW-pw, K-dec, E-TS or PL-1L.

   **Fix:** none. All six named YM obligations and the proposed producer
   estimates must remain OPEN until independently supplied at this scope.

10. **Fixed-scale lower bound and passage to the limit — PASS
    conditionally.** CUMUL **lines 526–556**.

    First choose one m_star so both r-errors are small; then choose
    depth and volume thresholds so each full error bracket is at most
    one half. The definitions of the error limits suffice; monotonicity
    is unnecessary. With m_star fixed, K_j-m_star and R_j/lambda_star
    tend to infinity on the prescribed sequence.

    Equations (C18) and (C19) give (C23). Using `u_k<=U_+(m_star)`
    yields exactly the positive fixed constants c and b in (C24).
    For the ratio, the lower numerator and upper denominator give
    `(A4/2)/(3A2/2)^2 = 2A4/(9A2^2)`. The strict smooth-test bounds
    imply `2A4/(9A2^2)>1/(507d)`, since `(2/9)(3/338)=1/507`.
    The same coupling cancels; no convergence of the coupling itself
    is needed. Moment convergence and B>=b pass these inequalities
    to the limit. Item 3 then excludes a Gaussian reconstructed e.

    This is one fixed local witness, not a moving-scale test along the
    limit. It is a sufficient conditional theorem and discharges no
    actual YM estimate. There is no uniform-in-N claim.

    **Fix:** none.

11. **NG-ax comparison and missing primary source — PASS at the
    expressly unverified scope.** CUMUL **lines 558–586**; HINT55
    **lines 405–420, 423–434**.

    The requested `../ym4d-existence/E/EXISTENCE.md` is absent in this
    working snapshot. HINT55 line 417 reports the decimal coefficient
    as an unreverified lattice-corner calculation; line 434 supplies
    the f-odd, soft-variable and restricted-null-class qualifications.
    CUMUL's locators match those passages. HINT55 does not certify
    NG-ax, and neither does this review.

    The rebuilt object is instead a connected four-point composite
    correlation, with one colour loop and leading factor
    `(N^2-1) g_FLOW^8`. The reported `N(N^2-1)g^4` quantity is a
    different observable with an unverified coupling dictionary here.
    Its decimal is not used as A4, and its comparator is not imported.
    The brief's self-contained rebuild option has been fulfilled for
    the chosen witness; NG-ax itself remains unverified.

    **Fix:** none. Preserve the missing-source and unverified-value labels.

12. **Final comparison, GO/NO-GO discipline and nontriviality scope —
    PASS.** CUMUL **lines 3–16, 588–609, 639–640**; WITNESS
    **lines 94–110, 488–503, 604–630** and PANEL_P1 **line 87**.

    A fixed finite polynomial is a smaller final witness interface than
    AF-e's asymptotic hierarchy. It requires a new connected four-source
    matching estimate; the existing two-source contract does not imply
    that estimate. Thus “fewer interface requirements” is justified,
    while “fewer YM obligations” has not been established. The comparison
    of analytic difficulty is appropriately ARGUED, not a theorem that
    every possible route must be harder.

    The same free-Maxwell composite used to establish the positive
    reference coefficient defeats any inference from K4!=0 to exclusion
    of every Gaussian underlying theory or free net. CUMUL explicitly
    states that limitation. It also does not turn the failed cubic
    leading term or the missing NG-ax source into a universal obstruction.
    The comparator and free coefficient may be PROVEN; the YM implication
    is conditional; actual matching, existence and mass gap remain OPEN.

    **Fix:** none. Do not promote this scoped LAND into a completed
    physical non-freeness, existence or mass-gap result.

13. **Literature locator and review provenance — PASS with one
    nonbinding locator refinement.** CUMUL **lines 613–638**.

    I checked the cited primary
    [Dütsch–Rehren paper](https://arxiv.org/pdf/math-ph/0209035).
    Printed page 2 gives the Gaussian/truncated-function characterization
    of a generalized free generator. For its distinction from composite
    fields, the direct locators are page 3 and §2.1, especially equations
    (2.14)–(2.16) on pages 7–8. CUMUL's single “p.2” locator is therefore
    imprecise for the whole sentence, although the mathematical
    distinction is established independently in CUMUL itself.

    **Suggested fix (nonbinding):** cite “p.2 for Gaussian generators;
    §2.1, pp.7–8 for their Wick composites.” No literature theorem is
    needed to repair or complete a proof step.

    The current source and artifact hashes match their recorded manifests,
    every local CUMUL link resolves, and the earlier review exists with
    its recorded hash and terminal LAND verdict. Its same-family
    disclosure is present; neither that review nor this one is an audit
    grade. The earlier historical claims are not substitutes for the
    present independent derivations and exact replay.

## Reviewer execution evidence

Both registered processes passed at **2026-10-30T02:28:02 UTC**. They
ran serially, at nice 20, with OPENBLAS/OMP/MKL/VECLIB/NUMEXPR threads
all set to one, bytecode disabled, and an exclusive flock on the existing
lock file opened read-only. All start/runtime/end resource checks passed:
load1 **2.1044921875**, native free memory **49%**. The author replay's
sampled combined peak RSS was **41,451,520 bytes**, elapsed **0.134 s**;
the independent check's was **37,240,832 bytes**, elapsed **0.189 s**.
The watchdog limits were 800 MiB and 90 s per child. These are observed
resource measurements, not mathematical results.

The unchanged author script returned **25/25 passes** with scientific
records identical to `checks/cumul_results.json`. The additional exact
calculation used only Python integer/rational arithmetic and no author
calculation functions. For one colour, with pi and coupling factors
stripped, it obtained:

| Quantity | Collinear configuration | Registered noncollinear configuration |
|---|---|---|
| Two-point value C23 | `12` | `3/2500` |
| Third cumulant at the first three points | `0` | `0` |
| Raw centred fourth moment | `434726305/2985984` | `11037958483/1434890700000000` |
| Three disconnected products | `144`, `9/4096`, `16/729` | `1/944784`, `1/186624`, `9/6250000` |
| Fourth cumulant after subtraction | `169/108` | `-117853/717445350000` |
| Three cycle traces | `2/27`, `3/128`, `1/3456` | `481/39366000000`, `-43/7346640384`, `-97/5832000000` |

In both configurations the subtracted fourth cumulant equals 16 times
the sum of the cycle traces. Connected pairing counts were **2, 8, 48**;
the three four-cycle multiplicities were **16, 16, 16**. All registered
kernel identities, error controls and rational hand-bound thresholds
passed. The collinear ratio was exactly **169/15552**.

The independent inline check source SHA256 was
`6fd744816fdb1ea3ec70d94d10a0bb4753d090cf01b513fb81b19b80183f37b7`.
It ran from memory, with output captured in the tool record and summarized
here. The author wrapper was not run and no check artifacts were written.
The reviewed source, original criteria, script and result hashes were
unchanged before and after execution. All ten source hashes and all
eleven artifact hashes listed in the author's manifests matched.
The final directory inventory showed only `REVIEW_CUMUL.md` added;
all 3,474 pre-existing files retained their sizes and modification times.

## Binding fixes and landing boundary

**Binding fixes: none.** Item 13 is an optional bibliographic locator
refinement. There is no blocking coefficient, sign, combinatorial,
domain, reconstruction-interface, quantifier or comparator-scope defect
in the reviewed version.

LAND covers the Gaussian comparator, free cubic cancellation, exact
fourth-cumulant coefficient and smooth bounds, finite-moment witness,
and the conditional implication from the named YM inputs. All actual
YM growth, common-hierarchy, trajectory, matching and original-law
estimates remain OPEN. NG-ax is unverified here. Exclusion of arbitrary
free underlying nets, full YM existence and a physical mass gap are
not consequences of this review.

Credit for the constructive Yang–Mills program remains with Balaban and
Dimock; no bound from that program is silently used to discharge an input.

VERDICT: LAND
