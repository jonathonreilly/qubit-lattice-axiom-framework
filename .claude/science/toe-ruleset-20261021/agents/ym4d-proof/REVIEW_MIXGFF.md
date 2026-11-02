# Independent hostile review of MIXGFF

No binding mathematical defect found in the final 703-line manuscript. The
conditional exclusions and constructed counterexamples support its printed
scope. This disposition accepts a research note; it establishes no actual
Yang–Mills estimate, unrestricted free-theory exclusion, audit status, or
physical mass gap.

This is a fresh-context, same-family Codex review. I did not author the note.
I read the complete manuscript and checker, reconstructed the calculations
below, and checked the relevant source passages. The earlier review was read
after these derivations to check provenance, not used to settle the mathematics.
The full REC_CONT/REC_LIB proof is a named mathematical input, not independently
re-audited here. Independence does not extend to that shared library.

## Source identity and coverage

All manuscript line references below are to MIXGFF.md at SHA-256:

    6978578119322af1c1161f3282c81055815e5f3cce098d5be78261cfe8e328d3

The working HEAD is 7329ec3d0bd57a8b07f90221839fca2900242bbe; the observed
local origin/main is 01589af3faf806b736c42dc2f3bd625e9edead9f. Remote-ref
freshness was not established. The review binds these local source bytes.
The applicable workflow and repository reviewer skill match local origin/main.
The explicit REVIEW.md restriction to this report controls over generic
instructions to make fixes, commit, or create audit/ledger artifacts.

The source and final-output manifests both verified without a mismatch:

- checks/mixgff_sources.sha256:
  2dca22155960f42331f0d097089d8b50a6b1813419abb2688d13c12fc57f739d.
- checks/mixgff_final_sources.sha256:
  1a3b8685fdf8ad5cf12af495c3e0d39edf7ab2e4793a1602a85049829cf7c0c5.
- Review brief:
  a8df759a289b404420d8eca68646d5b653c8ea18c869d0227c88151ea208c613.

I checked COMBO §§1–4 for the field, tests, normalization, prior union and
counterexamples; WITNESS §§1–2 for the precise canonical propagator class and
E-CAN proof; CUMUL §3 for the curvature normalization and connected contractions;
REC_CONT §§1,11 for the exact continuation input/output; and REC_LIB §§2–3,17–18
for separated-test determination, spatial unitaries and reconstruction scope.
These checks do not endorse unrelated claims elsewhere in those files.

## Item verdicts and independent calculations

### 1. Objects, reconstruction and comparison domain — SUPPORTED

**Lines 28–82, 225–233. Fix: none.**

The flat E_n spaces, deterministic centring, Z(a)=1 and reflected COMBO
bumps agree with COMBO lines 32–62. Equation (1) is the scalar restriction
of REC_CONT lines 54–64, with a single all-order triple. The ordered analytic
matching asserted at lines 49–53 is precisely the named continuation input;
REC_LIB lines 1082–1103 give its field- and vacuum-preserving reconstruction.
Its uniqueness is not uniqueness of the vacuum invariant sector.

The geometric ratio uses limits of separated bumps after the continuum limit,
not products of separately smeared H kernels. Its point values are determined
on the ordered analytic representative. Both proposed configurations can be
put in that domain; the stated B times are exactly 1, 8/5, 9/5 and 3.
No coincident product, new observable, or finite-coordinate N5 witness is
silently introduced. Non-invariant decompositions and unmarked ambient nets
are explicitly outside the comparison.

### 2. Gaussian-mixture identities and sign/ratio counterexamples — SUPPORTED

**Lines 86–134. Fix: none.**

After subtracting the common component mean, the mixture fourth moment is
the average of the three Gaussian pairing products. Subtracting the products
of averaged covariances yields exactly the three component covariances in
(3). For covariance VQ this is Var(V) times the pairing sum. The proposed
two-point law has E[V]=1 and E[V²]=1+v, so its ratio spans all positive
values at a fixed tuple with positive Qij. It does not match all geometries.

For the independent random shift, cumulants add and
kappa4(T)=E[T^4]-3E[T²]^2=1-3=-2. Its covariance adds only lambda^8 to V_m.
Neither example is removed by deterministic centring. Expanding
log E exp(Vt²/2) also gives kappa4(X)=3 Var(V) and kappa6(X)=15 kappa3(V);
the note correctly keeps these repeated-coordinate formulas outside A_e.

The elementary logarithmic covariance is admissible by positive atomic
approximation. In particular, integrating s first gives
integral s² G_s(r) ds=192/(pi² r^8). Splitting its logarithmic integral at
s=r^-1 and restricting a lower-bound integral to s of order r^-2 proves
AF-e. Gaussian n-point pairings have at most n/2 edges and hence singular
degree at most 4n, so the flat-test bound checked in item 7 applies.

### 3. Quadratic common-kernel rigidity — SUPPORTED

**Lines 136–165. Fix: none.**

Two quadratic insertions have two cross pairings, giving
Cij=2 tr(A²) H_ij². A connected contraction of four two-legged vertices
is a four-cycle. For each of its three unoriented cycles, each vertex has
two assignments of labelled legs, giving 16 pairings and species factor
tr(A^4). Thus (5) has the correct coefficient.

Positivity of H makes every denominator term in (6) equal to
4 tr(A²)^2 times the corresponding H-edge product. The ratio is therefore
4 tr(A^4)/tr(A²)^2 at every configuration. This cancellation does not require
homogeneity or a spectral envelope. Null A cannot meet AF-e. The common
scalar kernel, finite symmetric matrix, absence of derivatives and absence
of linear/mixed-degree additions are essential and explicitly retained.

### 4. Free curvature geometry and exact nonzero gap — SUPPORTED

**Lines 167–223. Fix: none.**

Differentiating D(z)=1/(4pi²r²) gives
pi² partial_mu partial_rho D=-delta_mu,rho/(2r^4)+2z_mu z_rho/r^6.
The derivative at the second insertion has the opposite sign. Applying the
four antisymmetric curvature terms produces the minors of
I-2zz^T/r² divided by pi²r^4. The quartic z terms cancel. On an axis the
two-form numerator has three eigenvalues +1 and three -1; hence tr(J²)=6.
The clover convention in CUMUL lines 173–212 then gives C=12d/(pi^4u²r^8).
Connected cycle counting gives the numerator coefficient 16d in (8).

Direct planar multiplication in B gives, in the printed cycle order:

    [ 4/5 -3/5 ]     [ 0 -1 ]     [ 3/5  4/5 ]
    [ 3/5  4/5 ],    [ 1  0 ],    [-4/5  3/5 ].

On two-forms each such rotation has trace 2+4 cos(phi). The traces are
26/5, 2, 22/5. The products of squared edge lengths are 40, 8, 20,
giving weights 1/1600, 1/64, 1/400. Their sum is 3/160; the weighted trace
sum is 91/2000; their quotient is 182/75. For A the average trace is 6.
The ratio is this average divided by 9d, so the difference is
(6-182/75)/(9d)=268/(675d)>0. This is an exact written calculation,
not a computational test result or an interacting-YM calculation.

### 5. GEO and its actual-YM obligation — SUPPORTED AS CONDITIONAL / OPEN

**Lines 225–252, 580–596. Fix: none.**

The limiting two-point values in (11) make each denominator positive at
sufficiently small scale. Since C scales as lambda^-8 u_m^-2,
D scales as lambda^-16 u_m^-4, exactly matching K4. Division yields the
gap in item 4. A sum of ratio errors below 134/(675d), half the free gap,
is sufficient. Uniform matching on collision-free neighborhoods is a
sufficient stronger formulation, not an estimate proved in this note.

CUMUL's collinear smeared coefficient does not establish this noncollinear
matching. The manuscript says so. A common u_m identification with the
fixed actual field remains necessary; GEO alone does not imply AF-e without
a growth condition on u_m. The restrictions prevent a hidden GO for YM.

### 6. Homogeneity restriction and logarithmic composite — SUPPORTED

**Lines 256–342. Fix: none.**

A finite sum of homogeneous separated scalar terms has a first nonzero
power. Reflection positivity fixes its positive sign on reflected points.
After positive separated smearing, gamma>=8 violates V_m tending to zero;
gamma<8 violates the lower AF clause for 0<eta<8-gamma. This argument does
not apply to arbitrary spectral measures, as the note explicitly recognizes.

For (12), heat-kernel scaling gives G_s(lambda r)=lambda^-2 G_(lambda²s)(r).
After sigma=lambda²s, the rescaled spectral multiplier is
ell_lambda/log(e+sigma/lambda²). Its integral on [lambda²,lambda] is bounded
by lambda ell_lambda G_0(r_min); on [lambda,infinity) it is at most 2 and
converges pointwise to 1. The integrable majorant 2G_sigma(r_min) proves
uniformity on compact radial intervals. Integrating sigma in the heat
representation gives 1/(pi²r^4), verifying (13) and its constant.

One independent pair 2psi chi has C=4H² and
K4=32 sum_cycle product H. Summing p=3d pairs gives positive reflected
V_m of order ell_lambda^-2 and positive K4, proving both AF clauses and W.
The quadratic matrix has balanced eigenvalues +1,-1: its even traces are
2p=6d and its odd traces vanish. These match every collinear Maxwell cycle
trace. With 2^n contractions per n-cycle (two at n=2), all stated connected
leading kernels match, and partitions give moment matching. The match uses
u=ell_lambda; no identification with the actual YM trajectory is established.

Integrating the s>=1 upper bound gives t^-3 exp[-r²/(4t)-t]. Splitting the
exponent into two halves and using r²/(8t)+t/2>=r/2 bounds H by
4 exp(-r/2)/(pi²r^4). In separated compact polynomial blocks every connected
cross-block Wick term has a decaying edge, whereas terms with no cross edge
factor. This proves the clustering claimed, including CL2. Logarithms plus
clustering therefore do not exclude this actual composite.

### 7. All-order growth, positivity and composite realization — SUPPORTED

**Lines 344–403. Fix: none.**

Right-endpoint atomic quadrature gives 0<=H_L<=H and pointwise convergence
away from zero. There are at most (2n-1)!!<=2^n n! contractions and n edges,
with species factors bounded by a fixed constant to the n. This gives (15)
uniformly in the number of spectral atoms.

Project a nearest pair onto its coincidence plane. Only two coordinate
slots move, by O(delta); Taylor order 4n and flatness cancel delta^-4n
with constants of the form C^n. The 9n seminorm has sufficient derivatives
and decay. The remaining weight obeys

    (1+sum_i |x_i|²)^(-5n/2)
        <= product_i (1+|x_i|²)^(-5/2),

whose integral is a fixed constant to the n. Finally D^n/n!<=exp(D).
This verifies one triple s=9, beta=2, alpha=exp(D), rather than unrelated
fixed-order estimates. S0 and S1 are treated separately as required.

The displayed one-particle Laplace square is nonnegative. Wick symmetric
tensor Gram forms, restriction to polynomial vectors, and limits of finite
OS quadratic forms preserve positivity. The same bounds cover the joint
Gaussian/composite hierarchy. For composite realization, use smooth
separated approximations to the displaced unlike-species pair; it has no
self-contraction. All contractions in norms and mixed inner products remain
separated and converge, proving the OS Cauchy identification. Thus this is
more than a prescribed covariance/fourth-moment example; no coincident
Euclidean random-field product has been assumed.

### 8. CL2 and the invariant-mixture variance lemma — SUPPORTED

**Lines 415–482. Fix: none.**

Spatial translations preserve the OS form, have inverses and are strongly
continuous on the test-vector core. For an independent check of the cube
average, its spectral multiplier is the product of sinc(R k_i), with value
1 at k=0. It is bounded by 1 and tends to zero at every nonzero momentum.
Dominated spectral integration therefore gives the invariant projection E_t,
in agreement with the note's direct translated-cube proof.

Since the normalized vacuum is invariant,
||E_t v_t||²=|S_t(P)|²+||E_t v_t-S_t(P)Omega_t||².
The assumed integrability of ||v_t||² dominates the matrix coefficients and
also |S_t(P)|². Subtracting the squared barycenter expectation gives exactly
(18), the sum of two nonnegative terms. CL2 forces S_t(P)=S(P) almost surely.

The countable determining family gives one common full-measure set.
Individual continuity, rotation/translation of off-diagonal pairs, a partition
of unity, and flat-test cutoff density extend the equality to all first and
second separated moments. There is no uncountable-null-set intersection.
Gaussian hierarchies with those identical moments are identical, so their
barycenter has K4=0. Component clustering and removal of Gaussian zero modes
are not premises of this argument. Degree-two P uses four-point data, not
just clustering of e's two-point function.

### 9. Canonical-class and finite-Q-mixture extensions — SUPPORTED

**Lines 486–531. Fix: none.**

Applying z²d²-zd-z² to z^(2n)(a_n+b_n log z) gives the coefficients
4n(n-1) and 4n-2 printed in the recurrence. Its factorial denominators
give convergent power/log series; finite derivatives and Wick products
preserve integer exponents bounded below and nonnegative finite log degree.
The exact finite-propagator hypothesis is present in WITNESS lines 82–86.
After cancellations a nonnull scalar covariance has the stated positive
leading coefficient. gamma>=8 fails the upper AF clause; integer gamma<=7
fails the lower clause at eta=1/2. The null case fails it as well.

CL2 makes every component covariance equal to the barycenter's, so AF-e
removes every F1 component on the full-measure set. The remaining G hierarchy
has K4=0. This proves (20) without a uniform spectral envelope.

For the finite Q extension, identical means and covariances make the fourth
cumulant affine in the mixture: all disconnected subtractions are common.
Finite sums commute with the point limits. Each Q term is r_t D(C;Z), while
G contributes zero, so the mixture ratio is configuration-independent.
GEO contradicts it. The note correctly avoids claiming an unproved interchange
for an arbitrary mixing measure in this extension.

### 10. Obligation accounting and recommendation — SUPPORTED / ARGUED

**Lines 533–596. Fix: none.**

At fixed R the integrated test is admitted and compact. Convergence of its
moments and the lower-degree centring terms passes (21) to the limiting
hierarchy; only then may R tend to infinity. A diagonal R(j) limit does not
supply this statement. Thus CL2 is an explicit additional family of original-law
two-/four-point estimates, not an inferred consequence of local source bounds.

The canonical massless scalar has decaying cross-block propagators and CL2
without a positive mass gap. This verifies the stated weaker infrared cost
at the specified level, without assuming an automatic gap-to-cluster theorem.
The recommendation compares added obligation families, not difficulty or
optimality. All three author-brief directions are addressed. The strongest
all-WGF exclusion, actual YM realization and mass gap remain explicitly OPEN.

### 11. Negative-claim scope and N1–N8 — SUPPORTED AT RESEARCH-NOTE SCOPE

**Lines 598–678. Fix: none.**

The five listed approaches concern different invariants and include successes;
they are not presented as exhaustive failed routes. The dependency statements
are supported by the given witnesses: the scale mixture violates CL2, a
massless Gaussian has CL2 but K4=0, and (12) has W and CL2 but fails GEO.
GEO without growth of u_m need not assert AF-e; GEO-to-CL2 is left unresolved.
No unsupported count of independent walls is made.

The hidden-premise scan retains ALG, invariant admissible components,
integrability, the countable determining family and Q's shared scalar kernel.
The COMBO/CUMUL/WITNESS citations concern their actual residuals; none is
silently promoted to arbitrary-WGF classification. Resolution and order of
limits are explicit. The steelman preserves noncollinear and nonleading
routes, with their classification/matching obligations. No new-axiom claim
or universal impossibility is justified or asserted. The note expressly
disclaims a formal no-go packet PASS; this review grants none.

### 12. Citations, prior status and computational evidence — SUPPORTED WITH LIMITS

**Lines 680–698; MIXGFF_LOG.md lines 121–151; checks/mixgff_exact.py. Fix: none.**

The local locators match the contents specified above. The two external
attributions were checked against the primary papers:
[Duetsch–Rehren](https://arxiv.org/pdf/math-ph/0209035), introduction, printed
pages 2–3, distinguishes Gaussian/Källén–Lehmann fields from their conformal
specializations; [Dolan–Osborn](https://arxiv.org/pdf/hep-th/0011040), §6,
compares free-field four-point functions. They carry attribution only, not
proof of GEO or a YM theorem. No load-bearing quotation was substituted
for a derivation. Balaban/Dimock credit is present.

The existing review really ends in LAND and binds the current manuscript
hash; the log correctly distinguishes this from landing, audit and retained
status. Historical preregistration chronology is author-reported, not newly
authenticated by this review. No calculation here depends on that chronology.

The prospective checker was read in full. Its partition recursion, Hessian
versus minor construction, and labelled-pairing enumeration address the
finite algebra. The identity-numerator, dropped-cycle and factor-eight
controls have discriminating reference values; none tests a continuum limit.
Independent AST parsing succeeded. This is syntax/source validation only.

My own preflight command, nice -n 10 true, emitted
"nice: setpriority: Operation not permitted". Its shell exit status was zero;
that does not establish a successful priority change. I did not run the
checker, create its lock/results, bypass its guard, or claim arithmetic PASS
counts. Numerical execution remains NOT RUN. The exact written calculations
above, not prospective test outcomes, support the mathematical verdict.

## Binding fixes and remaining limits

**Binding fixes: none for this source revision.** Preserve the stated scope:
field-preserving comparisons on A_e; invariant admissible barycenters;
the restricted Q theorem and finite-Q-mixture extension; named reconstruction
inputs; actual CL2/GEO estimates and all-WGF exclusion OPEN; no audit or
retained-status promotion; numerical checks NOT RUN.

Only REVIEW_MIXGFF.md was created by this review. No manuscript, log, checker,
editable prompt, other source, audit or ledger file was edited. No commit was
made. This report is the review checkpoint for the exact source hash above;
changes to that argument or its named inputs require affected-source review.

VERDICT: LAND
