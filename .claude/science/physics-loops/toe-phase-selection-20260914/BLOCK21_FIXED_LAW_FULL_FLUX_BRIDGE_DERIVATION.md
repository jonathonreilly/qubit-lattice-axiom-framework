# Full compact-U(1) flux from a positive auxiliary-field tilt

Personal derivation in progress, 2026-09-15. This is a private conditional
probe of the fixed-law physical-observable residual. No independent review,
retained claim, finite-clock Gaussian phase or axiom change is asserted.
The new target is the full local flux/score field, including its contact
part, rather than only closed/current tests. The required auxiliary-field
central limit theorem remains an explicit unproved obligation.

## 1. Exact finite free-box Hodge variables

Let the cell complex be a finite free cubic box in dimension four. Write
D=d_1, B=d_2, C=d_3, H=B B*+C* C on real three-cochains, and G=H^-1.
For this boundary convention H>0, cohomology in degrees1,2,3 is zero, and
integer coboundaries are saturated. Define orthogonal two-form projections

 P=D(D*D)^+D*, R=B*G B=I-P.

The supplied compact-U(1) Villain law has link Haar measure and positive
image weights exp[-beta||D theta-2pi k||^2/2], k integer two-cochains.
Its real lifted flux is X=sqrt(beta)(D theta-2pi k). Gauge fixing and
unfolding the exact integer shifts gives the positive decomposition

 X = P W - 2pi sqrt(beta) B*G q,                      (1)
 q in Q:=B Z^P=ker(C) intersect Z^C3,
 nu(q) proportional to exp[-2pi^2 beta(q,Gq)],

where W is a standard real Gaussian two-cochain independent of q.
To see the independence, fix any integer representative k_q with Bk_q=q.
Its orthogonal part is B*Gq. The exact part Pk_q is absorbed into the
unfolded real D theta integral. The remaining Gaussian density factorizes
between range(D) and its orthogonal complement. The gauge volume and
integer-lattice Jacobian are independent of q and cancel in normalization.
This uses continuous Haar integration. A finite clock sum does not unfold
into this Gaussian integral and retains the second electric-current gas.

For real h, define Z(s)=sum_q exp[-2pi^2 beta(q,Gq)+2pi i(q,s)]. Then

 E exp[i(h,X)] = exp[-(h,Ph)/2] Z(s)/Z(0),
 s=-sqrt(beta) G B h.                                 (2)

The full source h is arbitrary. Restricting to Bh=0 would erase the
magnetic factor and would not characterize the full field.

The original X also has the centered real-MGF bound
E exp[(h,X)]<=exp[||h||^2/2]. Complete the square in the centered q
lattice Gaussian in(1); its shifted theta is at most its centered value
by Poisson summation on span(Q). Its contribution is at most
exp[(h,Rh)/2], and the independent P Gaussian supplies exp[(h,Ph)/2].
Jensen gives the same bound for Y=E[X|theta]. This supplies uniform moments
for the finite-box linear sources, without assuming the clock proof also
holds for Haar integration merely by analogy.

## 2. A positive auxiliary measure and an exact real-tilt formula

Choose 0<c<1/||H||; on all free four-dimensional cubic boxes one may use
c=1/32, since ||H||<=16. Set

 A=beta(G-cI)>0, T=(I-cH)^-1,
 Theta_c(phi)=sum_(q in Q) exp[-2pi^2 beta c||q||^2+2pi i(q,phi)].

Q is a full-rank lattice in its real span. Poisson summation in that span
writes Theta_c as a strictly positive sum of shifted Gaussians. It is
constant in the orthogonal complement, hence is positive for every phi.
Absolute convergence follows from the positive scalar quadratic weight.
Define the proper positive probability measure

 mu(dphi) = Theta_c(phi) gamma_A(dphi) / E_gamma_A Theta_c.

Gaussian integration gives E_gamma_A Theta_c(phi+s)=Z(s). All exchanges
are justified by summability of exp[-2pi^2 beta c||q||^2]. Translating the
real Gaussian integration variable by s therefore gives the exact identity

 Z(s)/Z(0)=exp[-(s,A^-1s)/2] E_mu exp[(phi,A^-1s)].      (3)

Inserting(2), using A^-1=beta^-1 T H and GT=G+cT, gives

 E exp[i(h,X)]
 =exp[-||h||^2/2-c(Bh,T Bh)/2]
  E_mu exp[-beta^-1/2(phi,T Bh)].                      (4)

This is a REAL moment-generating function on the right. Replacing it by
an auxiliary characteristic function changes the sign of its contribution
to the flux covariance and is incorrect. Formula(4) is exact at fixed beta
and finite volume; no small-defect or asymptotic hypothesis is needed.

For any real j, a second completion of the square gives

 E_mu exp[(j,phi)]
 =exp[(j,Aj)/2] Z(Aj)/Z(0) <= exp[(j,Aj)/2].           (5)

The ratio is positive by the Gaussian-integrated theta representation and
at most one by the positive symmetric q weights. Thus mu is centered and
Cov_mu(phi)<=A<=beta G. This centered domination is not an all-tilt Hessian
bound. It yields uniform exponential integrability of the linear sources
used below. No convexity claim is smuggled into(5).

Differentiating(4) twice gives the finite covariance check

 Cov(X)=I+c B*T B-beta^-1 B*T Cov_mu(phi) T B.          (6)

Equivalently, differentiating(3) and the magnetic theta directly gives
Cov_mu(phi)=A-4pi^2 A Cov_nu(q) A and recovers(1). The minus sign in(6)
is consistent with Cov(X)=P+4pi^2 beta B*G Cov_nu(q)G B.

## 3. Precisely sufficient macroscopic hypothesis

Take finite boxes and smooth compactly supported real two-form tests f,
with cell-average lattice sources h_a=J_a f. Require their geometry to
satisfy, as a tends to zero and the boundary recedes in physical units,

 ||h_a||^2 -> ||f||_2^2, ||B h_a||=O(a),
 (B h_a,G B h_a) -> ||R_cont f||_2^2.                 (7)

Here P_cont and R_cont=I-P_cont are the continuum orthogonal exact and
coexact two-form projections on R4. These are analytic discretization and
boundary-limit hypotheses until checked for a chosen exhaustion. They do
not follow merely from having a finite box.

The proposed auxiliary-field obligation is the JOINT convergence

 U_a(f):=beta^-1/2(phi,B h_a)
    => centered Gaussian with covariance
       kappa (R_cont f,R_cont g),                    (8)

at fixed beta, for every finite set of tests, with a deterministic constant
kappa. A covariance estimate alone is not(8). A theorem for scalar rotator
spins is not(8) for this three-form measure. The positive local convex
representation in blocks15/17 is a proposed route toward it, not a proof.

By(5), Var[beta^-1/2(phi,(T-I)Bh)] is bounded by

 ((T-I)Bh,G(T-I)Bh)
 =c^2(Bh,H T^2 Bh)
 <=c^2 ||H|| ||T||^2 ||Bh||^2 ->0.                   (9)

Also c(Bh,T Bh)->0. Uniform exponential integrability follows from(5)
for every fixed multiple of the sources: their A quadratic norms are
bounded by (Bh,G T^2 Bh), which is uniformly bounded using(7),(9).
Thus weak convergence(8) also implies convergence of the real exponential
moments in(4), including after removing T via(9). For every finite linear
combination of tests, the characteristic function in(4) tends to

 exp[-(||f||^2-kappa||R_cont f||^2)/2].               (10)

Consequently the full lifted flux has Gaussian limit with covariance

 C_X=I-kappa R_cont=(1-kappa)I+kappa P_cont.          (11)

Equation(5) and(7) imply 0<=kappa<=1 whenever(8) holds. Formula(11)
separates a local white-contact term from a Maxwell term. It does not
require the full lifted flux to satisfy the continuum Bianchi identity.
No conclusion about kappa or Gaussianity is obtained without(8).

## 4. How a checked Hessian bound would make the Maxwell part nonzero

Suppose, additionally, the exact auxiliary action H_eff=-log density
satisfies the upper quadratic-form estimate

 Hess H_eff <= A^-1+epsilon H                       (12)

uniformly in volume and phi. This is the form proposed by the carrier
convexification work; its independent review is pending. For any fixed
vectors j,v, integration by parts and Cauchy-Schwarz give

 Var_mu(j,phi) >= (j,v)^2/E_mu(v,Hess H_eff v).

The identities used are Cov((j,phi),(v,grad H_eff))=(j,v) and
Var(v,grad H_eff)=E(v,Hess H_eff v). They follow by differentiating the
proper Gaussian-times-periodic density; finite-volume boundary terms at
infinity vanish. Set j=Bh, v=G Bh. Then, writing s=(Bh,G Bh),

 beta^-1 Var_mu(phi,Bh)
 >= s^2 / [(1+beta epsilon)s+c(Bh,T Bh)].             (13)

Under(7),(8), exponential domination gives convergence of variances. For
a test with R_cont f nonzero, (13) yields

 kappa >= 1/(1+beta epsilon)>0.                     (14)

This is a conditional positivity mechanism. It does not establish(8),
and its epsilon input must be checked on the exact auxiliary measure.
The upper Hessian bound is sufficient here; an independently checked lower
Hessian bound would be needed for the intended homogenization route.

## 5. Transfer to the actual local score still requires state matching

For the original angles define the actual bounded local score
Y=E[X|theta] and image noise xi=X-Y. At fixed beta, conditional image
labels are independent with uniform moments and strictly positive local
variance v_p(theta). The block13 elementary conditional characteristic
argument applies equally to continuous link angles: it needs the stated
image kernel, not a finite alphabet. In a translation-ergodic, hypercubic
state whose local image-variance average is the constant v_bar, it gives

 chi_X,a(f)-exp[-v_bar||f||^2/2] chi_Y,a(f) ->0.       (15)

The state/exhaustion used in(8) must match this actual angle state. Do not
combine unrelated free-boundary and periodic subsequences silently.
Assuming that match and the weighted variance averaging in(15), equations
(10),(15) give an actual-score Gaussian limit

 C_Y=(1-kappa-v_bar)I+kappa P_cont.                  (16)

The first coefficient must be nonnegative: choose a nonzero smooth
coexact test and use positive definiteness of the limiting characteristic
function (or the variance identity and uniform exponential moments).
Thus kappa<=1-v_bar for such a matched limit. The strict positive image
variance is consistent with the unavoidable contact term of the lift.

For deterministic nonnegative contact coefficient and kappa>0, the
Gaussian law in(16) is a Maxwell field plus independent white two-form
noise. Under the usual reflection-positive two-form convention, the
block13 positive-time conditional-averaging isometry removes this
independent contact noise from the OS Hilbert space. The Maxwell sector
then has the usual two transverse polarizations. Those reconstruction
hypotheses and the exact state match remain explicit, rather than being
inferred from the auxiliary measure alone.

## 6. What would still separate this from the native finite-clock TOE

The full chain is conditional on(7),(8), the bound(12) for a positive
Maxwell coefficient, the angle/auxiliary state match and image-variance
averaging. Its most difficult unresolved step is(8), a Gaussian scaling
theorem for the fixed-beta vector-valued, exponentially extended gradient
interaction with correct carrier bookkeeping. It is not just a limit of
already known two-point bounds.

Even completing that chain would be for supplied compact U(1) Haar link
variables. The actual finite-clock model has a quantized electric-current
factor as well as magnetic charges. Block18 centered current domination
neither removes that factor at fixed N nor proves its large-scale law.
The native Record formation, action selection, charged matter and gravity
bridges remain separate. No axiom is changed or declared contradictory.

Next: check(1)-(6) by distinct finite representations, read the precise
homogenization hypotheses in the primary source, and attempt the actual
three-form central-limit step or isolate a specific missing estimate.
Do not open a PR for a conditional restatement while that hard work is
still the next useful action.

## 7. First finite checks and their scope

The private runner block21_full_flux_tilt_check.py checks the rational
Hodge and source identities on actual single cubes in dimensions3 and4.
On the three-cube, where the magnetic charge lattice is one-dimensional,
it compares the magnetic-charge sum, an independent Poisson-comb formula
for the full lifted field, and positive Gaussian quadrature of mu. Twelve
source/beta cases agree to at most4.45e-16; increasing the integration
cutoff changes results by at most6.67e-16. Those are observed floating-point
agreements, not rigorous interval bounds or a large-volume theorem.
Replacing the real auxiliary MGF by a characteristic function changes the
eight nonclosed-source checks by at least0.00813, catching that sign error.

An exact signed-permutation calculation also confirms that the space of
invariant symmetric quadratic forms on Lambda^2(R4) is one-dimensional.
The elementary proof is that coordinate reflections eliminate every
off-diagonal pair entry, and permutations equate all diagonal entries.
This fact can constrain a homogenized codifferential energy after its
existence and dependence on that codifferential have been proved. Cubic
symmetry by itself does not prove either of those prerequisites.
