# Independent hostile review of WITNESS

Reviewed source: `WITNESS.md`, 658 lines, SHA-256
`cf5b346726e41a380ab75374c124f49cff35049121f28ad6e90ae52f2385ec81`.
All WITNESS locators below refer to this exact version.

This is **same-family, context-separated review: Codex reviewing Codex**.
I did not draft WITNESS and did not use the author's private reasoning or
previous verdicts as evidence. I rebuilt the arguments below, then checked
source interfaces against AUTHOR.md, PROCESS_LIGHT.md, ASSEMBLY55,
W_T0, F17, NONFREE55 and its review, HINT2_55, TSE55, and LGF.
The assignment overrides the generic reviewer filename: this review creates
only `checks/witness_review.md`.

**Disposition: LAND as a bounded recommendation and conditional comparator
analysis.** No actual Yang–Mills estimate, reconstruction, owner decision,
audit status, unrestricted free-net theorem, or mass-gap theorem is certified.
There are no binding fixes to this version at that scope.

## R1 — Common data and the quantifiers over assignments

**Verdict: PROVEN interface statement; reconstruction remains OPEN.**
Locators: WITNESS 49–116, 446–471; W_T0 563–607, 647–745;
ASSEMBLY55 128–146, 199–219.

For each fixed m, the product of the reflected and unreflected compact
supports stays off every collision. Thus `g_lambda tensor f_lambda` is an
allowed separated two-point test and its centred value is the squared
one-field OS norm, conditional on E-ALG. This does not adjoin `e(f)^2` at
coincidence. The separation is preserved by equivalences preserving the
chosen scalar field and its test action. Quantifying over every finite Wick
assignment in F1 is substantive; it is not a theorem classifying every
possible generator or every abstract free-net embedding.

I also checked the product obstruction directly: if q starts at quadratic
order, q squared starts at quartic order, so its second derivative at the
identity is zero while the square of q's quadratic contraction is not.
Consequently ID-natural cannot supply a unital product-preserving
identification. WITNESS does not use it to do so.

**Fix:** none. Preserve the partial-product domain and the explicit
reconstruction obligation.

## R2 — E-CAN, including E3/E4, cancellations, and mixtures

**Verdict: PROVEN for exactly the finite-polynomial F1 definition.**
Locators: WITNESS 82–92, 118–201.

The Fourier Gaussian integral with the Laplace representation of
`1/(p^2+s)` gives E3 with coefficient `1/(16 pi^2)`. At zero mass,
`v=r^2/(4 tau)` gives `1/(4 pi^2 r^2)`. For positive mass the radial
resolvent equation is `h''+3h'/r-m^2 h=0`, and substituting
`Y=4 pi^2 r^2 h`, `z=mr` gives `z^2Y''-zY'-z^2Y=0`.
For a term `(a_n+b_n log z)z^(2n)`, the differential operator without
`-z^2Y` contributes
`4n(n-1)(a_n+b_n log z)+(4n-2)b_n`, times `z^(2n)`.
The order-two coefficient therefore gives `2b_1=a_0`; higher orders give
exactly E4. Iteration gives
`b_n=a_0/[2^(2n-1)(n-1)!n!]`. The recurrence for a_n adds only a harmonic
factor to these factorial denominators. Both series and their fixed finite
derivatives converge on punctured compact intervals. The two displayed
choices of `(a_0,a_1)` have Wronskian asymptotic to `2z`, hence form a
fundamental system. This establishes the power/log structure of the actual
heat-integral solution without pretending to determine its free a_1.

Finite differential polynomials and finite Wick pairings preserve integer
powers bounded below and a bounded nonnegative log degree. Scalar covariance
makes the resulting kernel radial. A convergent nonzero series has a first
nonzero power and then a highest log degree at that power; if all coefficients
vanish, the separated kernel vanishes and cannot satisfy the lower AF-e
clause. Reflection positivity tested with approximate point supports at
opposite times gives nonnegativity of the continuous separated radial kernel,
and hence positivity of its nonzero leading coefficient. This argument permits
mass-dependent cancellations and masses in the leading coefficient.

On `d<=|x-y|<=D` the expansion is uniform, and positive f,g give `I_gamma>0`.
If gamma is at least 8, `lambda^8 C_lambda` does not tend to zero. If gamma
is at most 7, `lambda^(15/2) C_lambda` tends to zero. These exhaust the
integer exponents and contradict the two AF-e clauses. Arbitrary fixed
normalizations, finitely many species, derivatives, and finite tensor products
are included.

For the optional mixtures I independently obtain
`C_mix=integral C_alpha dnu+Var_nu(mu_alpha)`. Nonnegativity and Fatou
exclude components with gamma at least 8. The common ENV bound then bounds
the remaining mixture by `O(lambda^-7 |log lambda|^J)`, plus the finite
constant variance. This establishes precisely the stated optional extension,
not an extension to arbitrary unenveloped mixtures.

**Fix:** none. The repaired mass and connected-mixture qualifications are
necessary and are already present.

## R3 — E6 is an OS covariance; E7 proves the required counterexample

**Verdict: PROVEN for F2 and F3 on the separated e hierarchy.**
Locators: WITNESS 220–288.

With `rho(ds)=s^2/log^2(e+s) ds`, put
`A(u)=integral rho(ds)/[(1+s)^2(u+s)]`. This is finite at u=0:
the integrand is O(s) near zero and O(1/(s log^2 s)) at infinity.
For u>=0, `0<=A(u)<=A(0)`, so `(1-u)^2 A(u)` is a nonnegative
polynomially bounded Fourier covariance. This verifies ordinary Gaussian
positivity and temperedness, not merely a formal spectral integral.

Multiplying E6's partial-fraction identity by `(u+s)(1+s)^2` yields
`(1-u)^2` on both sides. At finite spectral cutoff the difference from
`integral G_s rho(ds)` consists of a constant and a linear polynomial in
u, hence contact distributions. The E6 cutoff covariances converge in
tempered distributions by their common polynomial bound; off coincidence,
the spectral kernels converge absolutely. The contacts vanish in all
reflected strictly positive-time cross pairings. Integrating p_0 gives the
positive form displayed at WITNESS 243–244. Its mass integral is finite on
these separated supports. The exponential reflection kernel has a positive
Gram form at every tensor power, establishing Gaussian polynomial RP as well.
Restriction to the separated hierarchy is therefore legitimate. No sharp-time
restriction or illicit unsubtracted divergent covariance is used.

For the upper bound, masses below r^-1 contribute at most
`G_0(r) integral_0^(r^-1) s^2 ds = O(r^-5)`.
Above r^-1, the denominator is at least `log^2(1/r)`. Directly integrating
`s^2 exp(-s tau)` gives `2 tau^-3`; then
`integral tau^-5 exp(-r^2/(4tau)) d tau=1536 r^-8`.
The coefficient is consequently exactly `192/(pi^2 r^8)`.
For the lower bound, the windows `s in [r^-2,2r^-2]` and
`tau in [r^2,2r^2]` give respectively spectral mass
`>=c r^-6/log^2(1/r)` and propagator `>=c' r^-2`.
This proves E7. Positive separated smearing preserves the bounds, so V_m
vanishes logarithmically while `lambda^-eta V_m` diverges for every eta>0.
Gaussian connected functions above order two vanish identically.

A scalar member suffices to disprove separation from a class also containing
tensor-valued GFFs. The Bianchi-curvature numerator is an additional
restriction and does not remove this scalar counterexample from broad F2.

**Fix:** none.

## R4 — The marked magnetic inequality and the one-scale failure

**Verdict: PROVEN on the defined marked curvature class only.**
Locators: WITNESS 292–342; W_T0 220–308.

Summing the three-dimensional ordered magnetic trace gives
`sum_ij T_ij,ij=4|p|^2`. The equal-time denominator is `2sqrt(p^2+s)`.
Combining this with t^2/4, the angular measure `p^2 dp/(2 pi^2)`,
and `v=sqrt(t)p` gives B1 exactly. Substitution `w=2v^2` gives
`J(0)=1/8`. J decreases in its argument and is comparable to 1 below
argument 1 and to its inverse square root above 1. This proves both the
stated finite-domain criterion and `b(t_0)<=b(t_1)` for `t_1<t_0`.
For a finite Gaussian quadratic form, the fourth-moment expansion gives
`E B^2=(Tr AQ)^2+2Tr[(Q^(1/2)AQ^(1/2))^2]<=3(E B)^2`.
Thus the comparison uses actual finite vacuum vectors.

The YM inequalities would give `b_YM(t_0)-b_YM(t_1)>=A/2`.
Subtracting the nonpositive free difference forces the sum of the two
absolute discrepancies to be at least A/2, hence their maximum at least A/4.
B3 has total observed spectral mass `32 pi^2 y`, giving mean y at every t;
it defeats any purported one-scale gap with unrestricted normalization.

The numerator and the rule assigning B its canonical curvature square are
part of membership. None of these calculations classifies all GFFs or all
free realizations of an unmarked B label.

**Fix:** none. Keep the marked qualifier in every use of this theorem.

## R5 — B4 really represents the stated unmarked hierarchy

**Verdict: PROVEN counterexample on WITNESS's expressly stated hierarchy;
no verdict about an unspecified stronger quotient.**
Locators: WITNESS 70–80, 87–110, 344–364, 383–387.

The relevant algebra here is generated by the separated e tests, positive B
labels and their local regularizations, truncations and permitted products,
with the given Euclidean action, reflection and completion. WITNESS explicitly
excludes a curvature generator and any relation fixing B from e. That
exclusion is essential; merely saying "some free theory has the same mean"
would not suffice.

On exactly these operations, substitute `e=phi` in one canonical free scalar
vacuum and every B label and its local approximants by `ct 1`. Products,
unit, conjugation, positivity, and bounded truncations are preserved because
this is the same scalar substitution in every occurrence, rather than a
separate matching of moments. A constant belongs to every local region.
The prescribed action changes n,x but not t, so it intertwines rotations,
translations and reflection. The approximants equal their limit, giving
zero localization error. The boundary vector is `ct Omega`; normal time
translation leaves it fixed. All mixed forms reduce to scalar free-field
forms times scalar coefficients, hence satisfy the permitted OS conditions.
The smooth profile ct also obeys the requisite locally uniform label bounds.

Its joint generator family is affine Gaussian: deterministic B coordinates
have zero centred covariance, while e has canonical scalar covariance.
Constants are degree-zero Wick polynomials. Thus it belongs to all three
broad readings explicitly defined in WITNESS, and
`W_B=c(t_0-t_1)>0` although `h(t)->0` in the ultraviolet.
It refutes the class-wide implication, not a statement that this state is
actual YM.

W_T0 649–702 requires specified common maps and mixed bounds for the YM
construction; those are not extra universal curvature identities in the
unmarked hierarchy defined here. If the owner instead imposes a quotient
encoding the canonical magnetic composite or another relationship to
underlying fields, this substitution must be checked anew. WITNESS 77–80,
363–386 and 429–433 already state that boundary. The table's three B rows
cannot be exported beyond it.

**Fix:** none binding. Optional precision at line 360: arbitrary prescribed
values on finitely many witness labels can be interpolated by a nonnegative
regular profile; an arbitrary nonregular function on a continuum of labels
need not satisfy the hierarchy's label regularity. The explicit h(t)=ct
counterexample has no such issue.

## R6 — B5 is a second, nonconstant free counterexample

**Verdict: PROVEN for the canonical-free realization reading, not for
Gaussianity of the B generators.** Locators: WITNESS 366–381.

For a massless canonical scalar restricted to a three-dimensional slice,
spatial heat smearing has variance
`(1/(4 pi^2)) integral_0^infinity p exp(-2tp^2) dp
 =1/(16 pi^2 t)`.
Thus the unnormal-ordered positive square in B5 has mean
`M_0^2 t/(16 pi^2)`, and its second moment is three times its squared mean.
This is a legitimate square of a spatially smeared random variable, not a
pointwise square of an unsmeared four-dimensional distribution. Truncating
the smooth heat kernel in space converges in the covariance norm; Gaussian
fourth moments give convergence of the squares in L2. Normal time
translation multiplies the one-particle spectral kernel by
`exp(-epsilon |p|)`. Dominated convergence gives the sharp-time limit;
the corresponding products converge by Gaussian moment identities.
Euclidean covariance supplies the joint rotated family with the
support-compatible cones, without placing tilted full slices in the
original positive-time cone.

The resulting mean increases with t, so the same two-scale witness is
positive. This square is a quadratic free observable and is not Gaussian
as a B generator. WITNESS correctly uses B4, not B5, for the F3 row.

**Fix:** none.

## R7 — Verdict on each of the six table decisions

Locators: WITNESS 31–45. Each row is tested as an implication about the
specified witness, not as a claim that a free state equals the unknown YM
state.

| Item | Independent verdict | Binding fix |
|---|---|---|
| Separated e / F1 | PROVEN comparator exclusion; YM application OPEN by R1, R2 and R8 | None |
| Separated e / F2 | PROVEN scalar GFF counterexample by R3 | None |
| Separated e / F3 | PROVEN Gaussian counterexample on the same separated e hierarchy by R3 | None |
| Time-zero B / F1 | PROVEN failure of the unmarked two-scale implication by R5; R6 is an additional nonconstant realization | None; preserve unmarked scope |
| Time-zero B / F2 | PROVEN failure for the stated unrestricted assignments by R5; a marked Bianchi-curvature class is narrower | None; preserve the assignment definition |
| Time-zero B / F3 | PROVEN failure for affine Gaussian states with degenerate covariance by R5 | None; do not substitute B5 |

A convention that only permits centred B generators changes the comparator
class; it cannot silently be substituted for the "all Gaussian" reading.
Likewise a rule fixing B to a curvature composite changes the B contract.

## R8 — The direct YM obligations really imply AF-e, conditionally

**Verdict: PROVEN reduction; every substantive YM input remains OPEN.**
Locators: WITNESS 440–502.

E-ALG fixes the original clover normalization, centring and Z=1, and retains
all reconstruction, regularity, symmetry, RP and permutation requirements.
E-SEQ requires the whole hierarchy and the specific witness tests on one
sequence, with uniform extension from its determining tests. For each fixed
m, the cutoff depth eventually satisfies `K>=m+d_0`, and the covariance
limit therefore carries both sides of E9. Since the inverse powers decrease
in u, E8 gives
`c_- U_+(m)^(-kappa') <= V_m <= C_+ U_-(m)^(-kappa)`.
The right side tends to zero, while multiplication of the left side by
`L^(eta m)` diverges. No exchange of the continuum and ultraviolet limits
is needed. The relation `0<kappa<=kappa'` has the correct orientation.

These four obligations are an honest sufficient contract, not produced
estimates. In particular a one-scale lower bound, an upper bound alone,
or two-point convergence alone would not prove the conclusion. The note
retains the necessary all-orders reconstruction and common-limit tasks.

**Fix:** none. The exact clover lower bound at every short scale remains
an essential unresolved YM task.

## R9 — PL-1L, its free inputs, and the constants in E13

**Verdict: PROVEN conditional assembly, with no promotion of P1–P6 to a
proved producer.** Locators: WITNESS 504–594; TSE55 129–179, 229–301,
422–439, 463–515, 639–643; LGF 42–52, 488–548.

For the actual normalized Markov chain, use the decreasing filtration
`sigma(U_i,...,U_K)`. The Markov property identifies its conditional image
of a bare observable with G_i. Its successive differences are orthogonal;
the cross covariance therefore telescopes to the D_i sum including D_K.
No coincident continuum e variance is invoked: at each cutoff the bare
observable is bounded.

For the Gaussian slices, write the quadratic source at level i as a
quadratic form in independent fine increment z and remaining field c.
Its conditional covariance gives `4 a_i sum_(j>i) a_j+2 a_i^2` entrywise,
with the terminal term `2 a_K^2`. Summing gives `2(sum_i a_i)^2` exactly.
Individual terms need not be positive. The source weights are
`w_f(p)=1/4 sum_(corners p) f_lambda`, from the ordered clover count and
`s(exp(iX))=(1/2) sum_a(F^a)^2+O(F^4)` in the specified Wilson convention.
Thus no undetermined matching coefficient enters E10.

E12 is an absolute envelope estimate, including the top level. For fine
levels its weights have a summable superexponential tail and the denominator
is u_k. At coarse displacement n satisfying
`n<=(u_k/2-R_F)/b_+`, FLOW-pw gives `u_(k+n)>=u_k/2`.
Beyond this range the fixed lower bound on u and the geometric tail
`L^-8n` yield `O(u_k^(-2-theta))`. Hence E12 implies E11 uniformly.
The positivity of mu_1 and the terminal small-coupling bound are essential;
they are included through the cited producer and E-TR.

For the running/free kernel comparison, expand
`sum_i (1/u_i-1/u_k) mathcal K_i`. Fine slices have bound
`L^-4k L^(4n) exp(-c L^n)` and `u_i>=u_k-R_F`.
Coarse slices have bound `L^-4k L^-4n` and admit the preceding split.
The pairwise coupling bracket bounds the numerator by `b_+ n+R_F`.
This gives `O(L^-4k u_k^-2)`, while the free kernel itself is
`O(L^-4k)`. Squaring, summing the nonnegative source weights, and using
`lambda^8 a^-8 L^-8k=1` gives the stated `O(u_k^-3)` bubble error.

I checked the LGF interface, rather than accepting a prior LAND verdict:
with counting norms `dd*+d*d=Delta I`, and at a nonzero Fourier mode
`d= q wedge`, so `d Delta_1^-1 d*` is precisely the projection onto exact
2-forms. Its entries are the four indicated second differences of G_T.
Only LGF's order-two estimate is consumed, yielding
`O(r^-5)+O(T^-4)`. Squaring gives
`O(r^-9+r^-4 T^-4)` on `1<=r<=T/4`. The test supports lie in this range
once the fixed depth/radius thresholds are enlarged. The resulting
Riemann-sum error is `O(a/lambda+(lambda/R)^4)`.
This verifies the cited interface; it does not re-audit all upstream LGF
or linear-response proofs.

The continuum curvature matrix equals the exterior-square reflection
`Lambda^2(I-2xx^T/r^2)/(pi^2 r^4)`. It is orthogonal on six components,
so its squared-entry sum is `6/(pi^4 r^8)`. The two Wick contractions and
N^2-1 colors give exactly `B_0=12(N^2-1)I_8/pi^4`.
The free interval `[B_0/2,3B_0/2]` minus/plus two errors each at most
`B_0/8` gives `[B_0/4,7B_0/4]`, proving E13.

The six producer tasks at WITNESS 585–594 match TSE55's P1–P5 plus E5/P6:
source-sensitive Gaussian control, background control, quantum image
coefficient tending to one and localization, coarse covariance matching,
summed two-insertion large-field control, and running-coupling matching.
An image upper bound alone supplies neither the coefficient nor the lower
bound. WITNESS explicitly leaves the proposed P1–P6 implication ARGUED
and uses the precise OPEN E11/E12 instead.

**Fix:** none.

## R10 — The marked alternative retains its other independent costs

**Verdict: PROVEN reduction, all listed YM estimates OPEN.**
Locators: WITNESS 389–438; F17 70–164; W_T0 122–214, 336–390.

For the actual-history partition, positivity and exact normalization give
`E B=S+sum_r M_r`. The regular-sector bound and the aggregate B6 budget
therefore give `limsup E B(t_1)<=A/2` on the same sequence.
The lower bound gives `E B(t_0)>=c_-/U_+(m_0)=A`.
The stronger summable all-grid insertion envelope produces a fixed m_1
because its total upper bound tends to zero; the two-scale B6 hypothesis
alone does not imply all-grid ultraviolet decay.

Uniform second moments imply uniform integrability of the means through
`E[X 1_(X>M)]<=E X^2/M`. They do not imply second-moment convergence or
identify a vector in the original e-cyclic Hilbert space. The separate
common-algebra, localization, mixed-order and SHARP-B obligations are thus
necessary and correctly retained. F17's first-moment estimate cannot supply
them or the free-assignment coverage. Tilted full slices also cannot enter
the original positive-half cone merely by translating their centers.

**Fix:** none.

## R11 — N5 is genuinely a separate owner decision

**Verdict: CONFIRMED qualification; current finite-moment N5 is not
satisfied by AF-e.** Locators: WITNESS 16–22, 203–216;
ASSEMBLY55 199–202.

N5 asks for a continuous function of finitely many moments with a positive
gap. AF-e uses a countable asymptotic family and is not that kind of witness.
WITNESS says so at the top and expressly conditions the recommendation on
accepting a changed witness contract. No acceptance is inferred here.

The finite-coordinate approximation statement also has the correct limited
scope. For the chosen separated supports, the mass-shell test kernels are
continuous in s and have integrable high-mass tails against the stated
positive KL measures. Truncate the measure and approximate its compact-mass
integrals by positive finite atomic sums simultaneously for the fixed finite
list of tests. Each sum is the covariance of a linear combination of finitely
many independent canonical scalars. A continuous functional vanishing on
those free finite-coordinate values also vanishes on their closure,
including q's such values. This establishes no universal impossibility
result for arbitrary higher-moment witnesses or every OS theory.
The independent constant Gaussian mode without clustering is also correctly
kept separate from a mass-shell-only KL representation.

**Fix:** none. If the owner keeps finite-moment N5 unchanged, the recommended
route remains an alternative proposal and cannot be represented as closing N5.

## R12 — The optional fourth-cumulant route and final scope

**Verdict: PROVEN comparator statement; C4-sep and broader composite
exclusion remain OPEN.** Locators: WITNESS 601–641.

Expanding a centred Gaussian generating functional gives exactly the three
pairings subtracted in E14, hence K4=0 for every elementary Gaussian/GFF
hierarchy. Convergence of those finitely many moments and the fixed positive
liminf give the stated gap in the limit. All four tests are separated, so
this introduces no forbidden contact product. Conversely
`log E exp(tX^2)=-(1/2)log(1-2 Var(X)t)` gives
`kappa_4(X^2)=48 Var(X)^4`. Separated free-field squares have connected
cycle contractions as well. Even free Maxwell provides nonzero examples:
on four distinct collinear points its curvature covariance has one common
orthogonal reflection matrix, and every four-cycle trace contains its
fourth power, giving a positive nonzero trace. Thus C4-sep would not exclude
all free Wick composites. The note states exactly this restriction and
does not obtain C4-sep from a two-point PL-1L estimate.

**Fix:** none. No broader GFF-composite or unrestricted free-net conclusion
is justified by combining the displayed witnesses.

## Binding fixes and execution record

**Binding fixes: none at the stated recommendation scope.** The existing
restrictions on F1, the unmarked B hierarchy, finite-moment N5, reconstruction,
and every YM-side input must remain attached to the conclusions. The only
optional wording refinement is the regularity qualification in R5; the
explicit counterexamples and all six table decisions do not depend on it.

No scientific numerics were needed or run. File reads and this single new
review write used nice priority 10 and single-thread BLAS/OpenMP settings,
with no pools and no setrlimit calls. Load and macOS available-memory gates
were checked before every invocation; measured process RSS remained far below
1 GB. No existing source, audit, ledger or axiom file was edited, and no
commit or publication action was taken. Balaban and Dimock's upstream gauge
RG methods remain attributed; no method attribution is used as proof.

VERDICT: LAND


## Affected-review addendum — regularity qualification after B4

This addendum reviews only WITNESS 359–361 in the revised 659-line source,
SHA-256 `f545b2b544234e9e2a133fb0957bee18cf2c290912897d5a5028ccadc484ecb8`.
The original review and its source fingerprint above remain the record for
the prior version. Reversing exactly this replacement reproduces the prior
SHA-256 `cf5b346726e41a380ab75374c124f49cff35049121f28ad6e90ae52f2385ec81`;
there are no other source changes in this review transition.

**Verdict: PROVEN; R5's optional wording refinement is resolved.**
The revised sentence restricts the general profile to the chosen label
regularity. For finitely many distinct positive witness times t_i and
prescribed finite values a_i>=0, choose nonnegative smooth bumps psi_i with
disjoint supports and psi_i(t_i)=1. Then `h(t)=sum_i a_i psi_i(t)` is a
nonnegative smooth interpolant. Thus the interpolation assertion is valid,
while the state claim retains the chosen hierarchy's regularity requirement.
The explicit counterexample `h(t)=ct` and its product, positivity, covariance,
localization and sharp-time checks are unchanged.

No new binding fixes arise. All six prior decisions and their unmarked,
finite-polynomial, owner-decision and OPEN-YM scope restrictions remain in
force. This is the same context-separated, same-family reviewer checking
only the affected passage; no other scientific item was re-reviewed.
Only this addendum was written, under the same resource guards.

VERDICT: LAND
