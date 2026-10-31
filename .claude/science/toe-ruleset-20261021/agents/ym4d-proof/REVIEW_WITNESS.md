# Independent hostile review of WITNESS.md

Reviewed manuscript: 659 lines, SHA-256
`f545b2b544234e9e2a133fb0957bee18cf2c290912897d5a5028ccadc484ecb8`.
All manuscript line numbers below refer to this version. Source locators refer
to the files in this exported working folder.

This is a fresh-context, same-family review: Codex reviewing Codex. I did not
author the manuscript. The existing review in `checks/witness_review.md` was
inspected as provenance; its verdict is not a premise of this review. I
independently checked the arguments and the cited source interfaces.

**Disposition: LAND as a contract recommendation, proved comparator results,
and conditional reductions.** Actual Yang–Mills non-freeness, reconstruction,
and the interacting observable estimates remain OPEN. Acceptance of OWN-alg,
OWN-free, or the proposed change to N5 is not supplied by this disposition.
There are no binding fixes at this scope.

The six required witness/class decisions are as follows. “Counterexample”
means a counterexample to the specified witness implication, not a model of
the unknown Yang–Mills limit.

| Item | Manuscript lines | Independent verdict | Fix |
|---|---|---|---|
| Separated e × F1 | 5–22, 33, 82–92, 118–201, 447–595 | CONFIRMED: AF-e excludes the defined finite canonical Wick class. Its YM application is OPEN, conditional on E-ALG/SEQ/TR/TS. | None. Keep the finite-polynomial and N5 qualifications. |
| Separated e × F2 | 34, 94–101, 218–288 | CONFIRMED PROVEN counterexample: the scalar GFF in E5–E7 satisfies AF-e. It is already a member of the class allowing arbitrary tensor GFFs. | None. Do not substitute the narrower Bianchi-curvature class. |
| Separated e × F3 | 35, 103–110, 218–283 | CONFIRMED PROVEN counterexample: the same construction is Gaussian on the separated e hierarchy. | None. AF-e is not a non-Gaussianity criterion. |
| Time-zero B × F1 | 36, 70–92, 344–388 | CONFIRMED PROVEN counterexample on the stated unmarked hierarchy: B4 is a canonical free realization, and B5 is a nonconstant alternative. | None. Do not apply it to an additional, unspecified quotient. |
| Time-zero B × F2 | 37, 94–101, 344–388 | CONFIRMED PROVEN counterexample: B4 is an affine Gaussian realization over a canonical scalar, hence also over a GFF. B5 additionally covers the composite-realization reading. | None. The canonical-curvature marking is extra structure. |
| Time-zero B × F3 | 38, 103–110, 344–365 | CONFIRMED PROVEN counterexample: deterministic positive B coordinates with a free Gaussian e sector form an affine Gaussian state. | None. B5 is not needed and is correctly excluded as an F3 example. |

**R1 — Common algebra, observable preservation, and the target boundary.**
Verdict: CONFIRMED, with reconstruction explicitly OPEN.
Locators: WITNESS 49–116, 447–472; ASSEMBLY55 128–146, 199–225,
390–408, 636–639; W_T0 563–607, 647–745.

For fixed m, the supports of the two tests lie in opposite open time halves
and have positive separation. Their tensor product is flat on the collision
diagonal. Centering identifies its two-point value with the one-field OS
norm squared, provided E-ALG reconstructs the stated hierarchy. This does
not require the forbidden coincident product e(f)^2. E-SEQ specifies one
sequence and uniform extension bounds, rather than selecting unrelated
limits for different inequalities.

The distinction between an observable-preserving equivalence and an
equivalence after forgetting the observable is essential and is retained.
The ID-natural objection is algebraic: a quadratic leading term q gives a
quartic leading term in q^2, whose second jet vanishes, whereas the square
of the second jet of q generally does not. The map therefore cannot supply
the product-preserving identification needed here.

The magnetic hierarchy is expressly unmarked and has no relation recovering
B from e or a curvature generator. Constants and their truncations are
legitimate representations of its stated operations. W_T0's common-map,
mixed-bound, support and completion requirements are additional YM
construction obligations, not an already proved curvature identity excluding
those constants. A stronger quotient would need its own analysis.

Fix: none. Neither the partial algebra nor its reconstruction is silently
promoted to a completed continuum construction.

**R2 — Finite canonical power/log lemma and AF-e exclusion.**
Verdict: PROVEN for the explicitly defined F1.
Locators: WITNESS 82–92, 118–201; NONFREE55 238–284;
CODEX_REVIEW_NONFREE 42–50, 154–166.

Integrating the four-dimensional Fourier Gaussian gives the factor
1/(16 pi^2) in E3. At zero mass, the substitution v=r^2/(4 tau) gives
G_0(r)=1/(4 pi^2 r^2). At positive mass, writing
G=Y(mr)/(4 pi^2 r^2) in G''+3G'/r-m^2G=0 gives
z^2Y''-zY'-z^2Y=0.

For z^(2n)(a_n+b_n log z), the first two differential terms contribute
z^(2n)[4n(n-1)(a_n+b_n log z)+(4n-2)b_n]. Matching the preceding
coefficient from -z^2Y gives exactly E4, including b_1=a_0/2 and
b_n=a_0/[2^(2n-1)(n-1)!n!]. The recurrence for a_n adds at most a
harmonic factor. Thus the series and its finite derivatives converge on
punctured compact intervals. The two stated solutions have Wronskian
asymptotic to 2z, so they span the actual heat-integral solution; no
unproved choice of its second integration constant is used.

Finite differentiation and Wick contraction preserve integer powers bounded
below and a finite nonnegative logarithmic degree. Scalar covariance removes
angular dependence. After cancellations, either the separated kernel is
zero or its first surviving power and highest logarithmic degree give E2.
Reflection positivity against tests concentrating at reflected points fixes
the leading sign. This permits masses to determine the leading coefficient
and even the surviving exponent; it avoids NONFREE55's superseded claim
that masses only affect subleading terms.

Uniformity on d<=|x-y|<=D gives a strictly positive smeared coefficient
C I_gamma. If gamma>=8, lambda^8 C_lambda cannot vanish. If gamma<=7,
lambda^(15/2) C_lambda tends to zero. These alternatives exhaust integer
gamma and contradict AF-e at eta=1/2. A separated-null field also fails the
lower clause. Fixed coefficients, finite derivatives, species and tensor
products do not escape the argument.

For mixtures, the connected covariance includes Var(mu_alpha). With that
finite term retained, positivity and Fatou exclude gamma_alpha>=8 almost
everywhere; the stipulated common ENV bound controls the rest by
O(lambda^-7 |log lambda|^J). The stated restriction on mixtures is necessary
and present.

Fix: none. This proves no classification of arbitrary local fields or free
nets beyond the specified finite-polynomial class.

**R3 — E5–E7 define an actual Gaussian counterexample.**
Verdict: PROVEN.
Locators: WITNESS 218–288; CODEX_REVIEW_NONFREE 98–116, 188–198.

Let A(u)=integral rho(ds)/[(1+s)^2(u+s)]. At u=0 its density is O(s)
near zero and O(1/(s log^2 s)) at infinity. Hence A(0)<infinity and
0<=A(u)<=A(0) for u>=0. The covariance (1-u)^2 A(u) is nonnegative,
continuous as a quadratic form on Schwartz tests, and polynomially bounded.
Its Gaussian finite-dimensional moment functionals therefore exist.

Multiplication by (1+s)^2(u+s) verifies the partial-fraction identity in
lines 236–237. At finite mass cutoff its difference from the mass-shell
integral is a polynomial of degree one in u, supported at coincidence in
position space. The cutoff covariances converge as tempered distributions
under the common polynomial bound. Off coincidence they give E5; in
reflected positive-time pairings the contact terms vanish. Integrating the
time momentum gives the nonnegative Laplace-transform square in lines
243–244. Gaussian RP follows by expanding the exponential of this positive
cross form into tensor-power Gram forms. Thus positivity and OS positivity
have both been checked, rather than assumed for a divergent spectral integral.

For the upper bound, s<=r^-1 contributes at most O(r^-5). Above that
threshold the logarithmic denominator is at least log^2(1/r). Direct
integration gives integral s^2 exp(-s tau) ds=2 tau^-3 and
integral tau^-5 exp(-r^2/(4 tau)) d tau=1536 r^-8, hence the coefficient
192/pi^2 in line 266. For the lower bound, the windows
s in [r^-2,2r^-2] and tau in [r^2,2r^2] supply respectively
c r^-6/log^2(1/r) spectral mass and c' r^-2 propagator size.
Positive separated smearing preserves these inequalities. Consequently
V_m is bounded above and below at logarithmic order, tends to zero, and
lambda_m^-eta V_m diverges for every eta>0. All higher connected Gaussian
functions vanish.

Fix: none. The scalar example does not satisfy the extra Bianchi-curvature
numerator and does not purport to refute that restricted tensor theorem.

**R4 — Finite-coordinate closure and the N5 decision.**
Verdict: CONFIRMED at the stated scope.
Locators: WITNESS 16–22, 203–216; ASSEMBLY55 199–202;
NONFREE55 168–192; CODEX_REVIEW_NONFREE 52–68, 234–240.

For each finite list of separated two-point tests, the mass-shell evaluation
is continuous in mass and integrable against the chosen tempered spectral
measure. Truncating the measure and taking positive atomic approximations
therefore converges in those finitely many coordinates. Atomic weights are
squares of coefficients of independent canonical free scalars. A continuous
functional vanishing on F1 must vanish at these closure points, including q.

This proves neither a no-go for every higher-moment witness nor a universal
mass-shell representation under OS0–OS3. A random invariant constant is an
extra possible sector without clustering. WITNESS explicitly avoids both
overextensions. Its countable asymptotic criterion is a proposed change to
N5, not fulfillment of N5's current continuous finite-moment requirement.

Fix: none. Owner acceptance is still required for the recommended contract;
this review does not make that decision.

**R5 — Marked magnetic comparator, domain, and gap.**
Verdict: PROVEN comparator result and conditional YM separation.
Locators: WITNESS 292–342; W_T0 220–308, 458–537;
HINT2_55 280–299.

The ordered trace of the spatial numerator is 4|p|^2. Combining the
equal-time denominator 2 sqrt(|p|^2+s), angular measure p^2 dp/(2 pi^2),
and t^2/4 gives B1 after v=sqrt(t)p. The integral of v^3 exp(-2v^2)
is 1/8. J is decreasing, comparable to a positive constant below argument
one and to sigma^-1/2 above it. This proves both the spectral-domain
criterion and b(t_0)<=b(t_1) when t_1<t_0.

For the observed finite Gaussian vector, diagonalizing the positive
quadratic form gives E B^2=(Tr AQ)^2+2Tr[(Q^(1/2)AQ^(1/2))^2]
<=3(E B)^2. The comparator therefore supplies finite vacuum vectors under
the stated domain condition. Integrable mixtures preserve the inequality.
The YM mean bounds imply W_B>=A/2, and subtracting the free inequality
forces a discrepancy of at least A/4 in one of the two means. The witness
is Lipschitz in those coordinates. B3 has observed total spectral mass
32 pi^2 y and exactly matches the one-point value y.

Fix: none. The assignment of B to this curvature square is a membership
condition, not a theorem covering unrestricted free assignments.

**R6 — The unmarked magnetic counterexamples preserve the needed operations.**
Verdict: PROVEN on the expressly stated hierarchy.
Locators: WITNESS 70–110, 344–388; W_T0 649–702;
HINT2_55 305–309.

In B4, the same substitution B(t)=ct times the identity in every product,
local approximation and bounded truncation is multiplicative and preserves
positivity. Constants belong to every local algebra. The Euclidean action
changes n,x but not t, so this assignment is covariant. The boundary vector
ct Omega has finite norm and is unchanged by normal time translation.
All mixed OS forms reduce to those of the canonical scalar. The centred B
covariance is zero, so the joint generator family is affine Gaussian.
Nevertheless W_B=c(t_0-t_1)>0. Smooth nonnegative interpolation can also
match arbitrary finitely prescribed nonnegative means, subject to the stated
label regularity.

For B5 the spatially smeared massless scalar has variance
(1/(4 pi^2)) integral_0^infinity p exp(-2tp^2) dp=1/(16 pi^2 t).
Its square has second moment three times the squared variance. Multiplying
by M_0^2 t^2 gives the stated mean and finite vacuum norm. Smooth spatial
cutoffs of the heat kernel converge in the one-particle norm; Gaussian
fourth-moment bounds transfer this to the squares. Normal time translations
converge strongly by the same integrable covariance bound. The construction
also exists jointly on rotated slices of the same free scalar field.

Fix: none. B5 is a quadratic free observable, not a Gaussian B generator
or a magnetic curvature square. B4 alone already proves all three broad
counterexample rows, so the conclusion does not depend on conflating these.

**R7 — Exact YM costs of the magnetic alternative.**
Verdict: CONFIRMED conditional reduction; the producer estimates remain OPEN.
Locators: WITNESS 390–439; F17 25–64, 70–164, 307–343, 386–392;
W_T0 124–153, 373–390, 647–745.

For the specified actual-history partition, nonnegativity gives exactly
E B=S+sum_r M_r. At fixed m_1, F17-SF-B bounds the first term by
C_sf/U_-(m_1), and B6 budgets the entire remaining limsup. Their sum
is at most A/2. Under the stronger all-grid hypothesis it is bounded by
C_sf/U_-(m)+H(U_-(m)) sum_r w_r, which tends to zero and permits a
fixed choice of m_1 before the limits. No probability-only exponent or
independence assumption is needed for this arithmetic.

Uniform second moments plus joint law convergence give uniform integrability
of first moments via E[X 1_(X>M)]<=E X^2/M. They do not give convergence
of second moments or identify a sharp-time vector. B-ALG/SEQ and SHARP-B
remain separate, as do mixed regularity, support-compatible positivity,
localization and class coverage. Non-freeness of an enlarged sector does
not imply non-freeness of the e-cyclic theory.

Fix: none binding. An optional wording clarification at lines 417–418 is to
say “all grid labels.” That is the conclusion actually supplied by F17
55–57 and 145–164. A continuous-time extension additionally uses the
inter-scale inequality and extended hierarchy described at W_T0 530–537;
it is not needed by this two-scale witness.

**R8 — Direct separated-e conditional proof and limit order.**
Verdict: PROVEN implication, with all four YM obligations OPEN.
Locators: WITNESS 447–503; TSE55 74–90;
CODEX_REVIEW_NONFREE 168–184.

The clover, Z=1, Wilson action and coupling convention match the cited
source. For each fixed m, E-SEQ passes E9 to the same continuum state.
The trajectory bracket then bounds V_m above by C_+ U_-(m)^-kappa
and below by c_- U_+(m)^-kappa'. The first vanishes as m grows; after
multiplication by L^(eta m), the second diverges for every eta>0 because
U_+ is affine in m. No exchange of the cutoff limit with m is used.

The dense-family extension uses a fixed test approximation, two uniform
seminorm error bounds and convergence on that approximation. It cannot
replace the hypotheses of the actual reconstruction theorem, which E-ALG
expressly retains. An upper bound alone, or a lower bound at one scale,
would not supply AF-e.

Fix: none. This proves the conditional witness, not any interacting estimate.

**R9 — PL-1L assembly, coupling weights, and the free normalization.**
Verdict: PROVEN conditional assembly; PL-1L itself remains OPEN.
Locators: WITNESS 505–595; TSE55 129–179, 185–238, 242–301,
421–441, 480–514, 639–643; CODEX_REVIEW_TSE 47–53, 118–144,
172–182; LGF 20–56, 189–345, 488–548.

The normalized Markov chain supplies the decreasing filtration
F_i=sigma(U_i,...,U_K). Its factorization gives
E[O|F_i]=E[O|U_i]. Orthogonal increments therefore telescope covariance,
with the terminal covariance retained. For the Gaussian model, write the
surviving field as c+z, where c is the coarser part and z the current
independent slice. The linear fluctuation term 2cz and quadratic term z^2
give respectively 4a_i sum_(j>i)a_j and 2a_i^2 after Wick contraction.
Summing gives 2(sum_i a_i)^2, without any per-level sign assertion.

To sum E12, write U=u_k and split the coarse displacement at
floor((U/2-R_F)/b_+). Before this point u_(k+n)>=U/2. Afterwards the
fixed positive lower bound on u and the L^-8n tail beat any specified
inverse power of U. The fine weights L^(4n) exp(-mu_1 d L^n) are summable.
The identical splitting with the inverse-coupling difference and L^-4n
kernel weights gives O(L^-4k U^-2). The coupling-one kernel is
O(L^-4k), so the bubble difference is O(U^-3) after using
lambda^8 a^-8 L^-8k=1. These conclusions use FLOW-pw and K-dec exactly
as named inputs; they do not produce their interacting counterparts.

I checked the free-kernel input's normalization and the consumed estimates.
The forward exterior derivative and its counting adjoint give
dd*+d*d=Delta on each component. On a nonzero Fourier mode,
d Delta_1^-1 d* is the orthogonal projection onto exact two-forms.
LGF's Gaussian subtraction and shell estimates give the differentiated
lattice remainder O(r^-6) at order two, its torus correction O(T^-6),
and a smoothed continuum torus correction O(T^-4). Comparing finite
differences with derivatives costs O(r^-5). These give exactly the
O(r^-5)+O(T^-4) curvature estimate consumed here. Squaring produces
O(r^-9+r^-4 T^-4), using 1<=r<=T/4. The lower-order torus corrections
are not silently replaced by T^-4.

For the source coefficient, four corners and two ordered orientations give
O(f)=sum_p[(1/2)sum_corners f]s(U_p). With
X=sqrt(2N) sum_a F^a t^a and tr(t^a t^b)=delta_ab/2,
s(exp(iX))=(1/2)sum_a(F^a)^2+O(F^4). Thus the quadratic source weights
are (1/4)sum_corners f and the quadratic action is u/2 times the
curvature norm squared. At separation r on the time axis the six unordered
curvature components have three eigenvalues +1/(pi^2 r^4) and three
-1/(pi^2 r^4). Their squared sum is 6/(pi^4 r^8); rotations preserve it.
The two Wick contractions and N^2-1 colors give 12(N^2-1)/pi^4.
This independently checks the normalization without fitting a coefficient.

The separated lattice-sum errors are bounded by a constant times
a/lambda+(lambda/R)^4. Fixed sufficiently large depth and radius therefore
give B_0/2<=L_free<=3B_0/2. Each remaining error is at most
B_0/(8u_k^2) at sufficiently large fixed m_0, giving the stated constants
1/4 and 7/4. Taking maxima of all input thresholds avoids losing a
producer's domain.

Fix: none. The six proposed production tasks are not discharged by a
first-image upper bound, a scalar coupling identification, or LGF. Lines
586–595 correctly preserve that distinction and the ARGUED status of the
P1–P6 mechanism. E11 or E12 is the precise open estimate being consumed.

**R10 — Fourth-cumulant alternative and its limits.**
Verdict: PROVEN conditional separator for elementary Gaussian generators;
YM C4-sep remains OPEN.
Locators: WITNESS 602–631; CODEX_REVIEW_NONFREE 118–140.

Four derivatives of a centred Gaussian generating functional give exactly
the three pairings subtracted in E14, including degenerate and tensor
covariances. Convergence of the finitely many moments and the liminf gap
therefore pass W4>=delta to the common limit. Pairwise separated test
supports make these legitimate hierarchy values without contact products.

For a centred scalar Gaussian of variance v,
log E exp(z X^2)=-(1/2)log(1-2vz), whose fourth derivative at zero is
48v^4. Thus composites are not covered by the Gaussian-generator exclusion.
There is also a direct separated free-Maxwell check: at four distinct
collinear points, each curvature covariance is the same orthogonal
six-component inversion matrix times a positive scalar; every connected
four-cycle has positive trace. Small disjoint nonnegative smearings retain
a nonzero connected four-point value. The cited R8's nonzero example is
consistent with this independent check. AF-e plus a nonzero fourth cumulant
is not proved to exclude every GFF composite.

Fix: none. The note does not turn the failure of these particular witnesses
into an impossibility theorem about future witnesses.

**R11 — Source fidelity, imports, status, and execution.**
Verdict: CONFIRMED at the scope above.
Locators: WITNESS 31–45, 633–659; briefs_q/WITNESS/AUTHOR.md;
PROCESS_LIGHT.md; WITNESS_LOG.md 79–115.

The ASSEMBLY55 N0/N5/N6/N15/F1 locators support the target, common-domain
and missing-input descriptions. W_T0 and F17 support the marked comparator,
two-scale budget and separate sharp-time/moment obligations. The NONFREE55
review's mass, mixture, zero-mode and Gaussianity corrections are incorporated.
TSE55's coefficient, PL-1L sum and production caveats are accurately carried
over, including E5's sixth matching task. LGF (37)–(41) supplies the specified
free curvature kernel, not an interacting lower bound.

The attribution to Watson and Olver is supported by
[NIST DLMF §10.31](https://dlmf.nist.gov/10.31), whose integer-order series
agrees with the independently checked recurrence. That page is attribution
and comparison only; no literature citation replaces a proof step. The
supplied KL measures, finite propagator class and marked magnetic numerator
are definitions or exhibited constructions, not hidden classification
theorems. The remaining reconstruction and YM estimates are named premises.

No audit status is conferred. The report's LAND concerns the recommendation
and its conditional mathematics; it is not GO for completed Yang–Mills
non-freeness or a mass gap. No numerical experiment or formal proof-assistant
verification was used or claimed. File-identity bookkeeping ran serially
under nice with BLAS/OpenMP thread counts set to one; the pre-write check
reported load 3.026, 51% free memory and peak RSS 28,688,384 bytes. Only this
review file is written, and no commits are made.

Fix: none. The optional grid-label clarification in R7 does not change the
two-scale theorem or the recommended separated-e contract.

**Binding fixes: none.** The explicit OPEN hypotheses and owner decisions
remain part of the reviewed scope, not completed work certified by LAND.

VERDICT: LAND
