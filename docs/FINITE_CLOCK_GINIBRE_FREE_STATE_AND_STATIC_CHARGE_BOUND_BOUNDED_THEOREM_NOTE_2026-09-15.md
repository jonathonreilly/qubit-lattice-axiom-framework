---
claim_id: finite_clock_ginibre_free_state_and_static_charge_bound_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the supplied finite-clock Villain law, character Ginibre inequalities identify a unique free-boundary exhaustion limit. At the explicit provisional free-cubic source smallness, two Wilson lower-bound derivations and a matched positive transfer representation bound the static spectral threshold reached by a test-charge path, uniformly in charge separation."
upstream_dependencies:
  - free_cubic_magnetic_local_fillings_and_positive_electric_current_convex_extension_bounded_theorem_note_2026-09-15
  - quantized_current_poisson_identity_centered_gaussian_domination_and_clock_wilson_cosets_bounded_theorem_note_2026-09-15
runner: scripts/finite_clock_ginibre_free_state_and_static_charge_bound_2026_09_15.py
---

# Finite-clock Ginibre inequalities and a matched static-charge energy bound

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** proposed_retained

For the supplied finite-clock Villain law, character Ginibre inequalities identify a unique free-boundary exhaustion limit. At the explicit provisional free-cubic source smallness, two Wilson lower-bound derivations and a matched positive transfer representation bound the static spectral threshold reached by a test-charge path, uniformly in charge separation.

These are author proof proposals awaiting independent review and formal audit.
The physical law is supplied; no native axiom, primitive or parameter is selected.
The spectral conclusion concerns external static test charges. Dynamical matter,
a full fixed-clock Gaussian field, and physical-law selection remain open targets.

## Status and proof obligations

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Match finite-clock Wilson control to a static-charge transfer spectrum in the same infinite-volume state."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the source-curvature and clock-pinning/state arguments, then seek dynamical charged matter in a supplied or derived physical law."
conditional_surface_status: "The supplied finite-clock Villain law and the explicit provisional free-cubic carrier/source smallness; monotonicity and free-state existence hold at all nonnegative couplings."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Analytic correlation, Green and transfer arguments with distinct direct-law and spectral finite challenges; physical extensions remain separately open."
```

| Input or obligation | Provenance and precise use | Status within this proposal |
|---|---|---|
| Supplied clock Villain probability law | Defined below on finite complexes; fixed N and couplings | A model choice, with native selection open |
| [Free-cubic magnetic source](FREE_CUBIC_MAGNETIC_LOCAL_FILLINGS_AND_POSITIVE_ELECTRIC_CURRENT_CONVEX_EXTENSION_BOUNDED_THEOREM_NOTE_2026-09-15.md) | Equations(4),(8)-(10), exact current extension and uniform curvature | Provisional source in the base PR; review the complete combined unit or land the base first |
| [Quantized current/Wilson identity](QUANTIZED_CURRENT_POISSON_IDENTITY_CENTERED_GAUSSIAN_DOMINATION_AND_CLOCK_WILSON_COSETS_BOUNDED_THEOREM_NOTE_2026-09-15.md) | Equation(10), actual external-character coset and alias normalization | Provisional source in the same base PR |
| [Chevyrev-Garban carpet theorem](https://link.springer.com/article/10.1007/s10955-025-03420-1) | Published total-variation convergence, checked with a bounded coarse pinning weight | Mathematical input; clock extension derived in Part II |
| [Lawler-Limic Green asymptotic](https://www.math.uchicago.edu/~lawler/srwbook.pdf) | Theorem4.3.1 with scalar Z3 Laplacian normalization | Standard asymptotic; the uniform energy bound also follows without it |
| Periodization, free-box Green limit, rectangle energy | Part I | Derived here |
| Clock inequalities, cofinal free state, charged transfer matching | Part II | Derived here; independent review pending |
| Fixed-clock full-field Gaussian law and dynamical matter | Separate physical targets | Open; not terminal premises of the static bound |

The two repository sources are pinned to PR8133 at
`f8e7219b5e79bcb271bb3c1df635ecdeeb57dbe8`. They are not independently
ratified by this application. The entire source unit must be reviewed before
landing this stacked consequence. The new runner constructs all its scientific
fixtures internally and reads its own source only for an integrity hash.

## Part I. Wilson curvature, cubic Green passage and rectangular rates

### 1. Target and source restrictions

The target is an actual Wilson-character lower bound for the finite
clock, and its consequence for long rectangular loops in a thermodynamic
limit. A stronger static charged-sector energy interpretation needs a
matched stationary reflection-positive state or transfer limit. That bridge
is a separate obligation, not assumed to follow from a covariance theorem.

Keep the supplied N-state clock Villain law on FREE FOUR-DIMENSIONAL CUBES,
beta>0, N a positive integer. Let C=ker d0* be the real conserved-current
space and Lambda=C intersect Z^edges. On C set G=H1^-1. The actual character
formula from the pinned source is

    W_N(J)=T(J/N)/T(0), T(s)=sum_(a in Lambda) exp[-V(a+s)],
    V(a)=N^2(a,G a)/(2beta)-F(N d1 G a), J in Lambda.       (1)

Under the source's large-beta carrier conditions, F is even, real and smooth
on all real two-form sources, and

    F(0)=0, F<=0, D2 F>=-epsilon I.

Consequently V is even, has Gaussian lower growth, and

    D2 V <= M:=N^2(beta^-1+epsilon) G.                    (2)

The upper curvature bound suffices below; positivity of D2 V is not needed.
It was derived in the source using the exact physical magnetic gas and a
fixed real interpolation, not by replacing the integer current measure
with a continuous one. Its values on the physical cosets in(1) are independent
of the chosen integer filling, although the interpolation itself need not be.

The source explicitly excludes arbitrary thin rectangles: a short relative
boundary carrier can require a long fill there. Thus it is invalid to obtain
a finite-spatial-box, infinite-time transfer estimate merely by applying(2)
to arbitrarily long slabs. Any proposed transfer extension must resolve that
boundary issue. The cubic thermodynamic limit below does not use that extension.

### 2. An elementary periodized curvature lemma

Let Lambda be any full-rank lattice in a finite Euclidean space, and V be
even and C2, with enough Gaussian lower growth to sum the following terms.
Suppose D2 V<=M for a fixed positive quadratic form M. Then for every s,

    T(s)/T(0) >= exp[-(s,M s)/2].                       (3)

Here is a proof without differentiating the lattice sum. Integrating the
second derivative along a+s t gives

    V(a+s)+V(a-s)-2V(a)<=(s,M s).

Hence sqrt(exp[-V(a+s)] exp[-V(a-s)]) is at least
exp[-V(a)]exp[-(s,M s)/2]. Sum over a and apply Cauchy-Schwarz. Evenness
and lattice reversal give T(-s)=T(s), so

    T(s)=sqrt(T(s)T(-s))
        >=sum_a sqrt(exp[-V(a+s)]exp[-V(a-s)])
        >=T(0)exp[-(s,M s)/2].

This proves(3), including s=0. It uses no continuous Brascamp-Lieb claim
about an integer law. It also holds for any translated representative
s+lambda, lambda in Lambda, because T is Lambda-periodic.

### 3. Alias-preserving finite-clock Wilson bound

Applying(3) with(1)-(2) yields

 exp[-(beta^-1+epsilon)/2 * min_(c in Lambda)(J+N c,G(J+N c))]
       <= W_N(J) <= 1.                                (4)

The upper bound follows either from the original probability characteristic
or the positive dual representation in the source. The lower bound proves
strict positivity. The minimum exists since G is positive definite and the
current lattice is discrete. In particular one may omit the minimization
and use the representative c=0. If J=N c, the minimum is zero and(4) gives
the exact alias W_N(J)=1. This retains the finite clock's character algebra.

For a simple oriented loop current J_C and integer charge q, one can choose
any representative q_eff=q mod N with |q_eff|<=N/2. Then

    W_N(q J_C)>=exp[-a q_eff^2 (J_C,G J_C)/2],
    a=beta^-1+epsilon.                                (5)

No lower bound on N is needed beyond the clock definition. This distinction
matters: a Wilson perimeter lower bound alone cannot distinguish a massless
Coulomb phase from a gapped deconfined finite-group phase. A claim of a photon
or of dynamical matter from(4) would be unsupported.

### 4. Cubic thermodynamic Green passage

For any fixed finite conserved J, the free-cube Coulomb energy (J,G_L J)
converges to the infinite-lattice energy (J,H1^-1 J) as the source recedes
from the boundary. Here is a direct projection proof. Choose a finitely
supported integer two-form S with d1*S=J; a finite cycle bounds in Z4.
In a box containing its support, let P_L=d1 G_1,L d1* and let Q_L be the
projection onto ker d1,L* on two-forms. Contractibility gives P_L=I_L-Q_L.
The zero extensions of the co-closed spaces defining Q_L are nested and
remain globally co-closed: every edge of an included face is included, so
d1* commutes with this extension. Their union is dense in ker d1* on ell2.
Indeed cut a co-closed Fourier field away from frequency zero, write it
as d2* H3^-1 d2 u there, approximate the three-form potential by finite
support, then remove the frequency cutoff. There is no ell2 harmonic
vector at the single zero Fourier point. Thus Q_L converges strongly to Q,
and P_L converges strongly to P. Moreover every receding rooted box contains
a growing centered box; the nesting sandwich makes the convergence uniform
over such placements. Therefore

    (J,G_1,L J)=(S,P_L S) -> (S,P S)=(J,H1^-1 J).      (6a)

This argument concerns co-closed zero extension. It does not assert that
a closed charge remains closed after extending a free box by zero.

Every local weak limit of centered free-cube clock laws, or uniformly
rooted free-cube laws, now inherits(5). For root averages most roots recede
from every face, the bound is uniform there, and the remaining fraction
vanishes. Compact finite-clock link configurations give subsequential
limits; no uniqueness or reflection positivity is inferred from compactness.
The finite nearest-neighbor Gibbs specification is strictly positive and
continuous, so its local conditional identity also passes to these limits.
Uniform root limits are stationary, but stationarity alone is not the
missing reflection-positive transfer identification.

### 5. Exact rectangular-loop Green energy

For a rectangular loop C_(R,T) in the 0-1 plane, let R be its fixed spatial
separation and T its temporal length. The Green calculation is

 lim_(T->infinity) (J_(R,T),H1^-1 J_(R,T))/T
       =2[G3(0)-G3(R e1)],                            (6)

where G3 is the scalar nearest-neighbor Laplacian Green function on Z3,
with Fourier denominator lambda(k)=sum_(i=1)^3 |exp(i k_i)-1|^2.
The following exact identity proves(6), and fixes its normalization. Put

    lambda_i=2-2cos k_i,
    r=(lambda+2-sqrt(lambda(lambda+4)))/2,
    D_R(k1)=sum_(x=0)^(R-1) exp(i k1 x),
    dmu(k)=d^3k/(2pi)^3 on [-pi,pi]^3.

For lambda>0 the scalar time Green function is
g_lambda(t)=r^|t|/sqrt(lambda(lambda+4)). The temporal sides of the
rectangle carry delta_0-delta_(R e1) for T consecutive links, while the
spatial sides carry a length-R path at times 0 and T with opposite signs.
The one-form Hodge Green kernel is diagonal in orientation, so the two
contributions have no cross term. Summing g_lambda(t-s) on the temporal
sides gives

    sum_(t,s=0)^(T-1) g_lambda(t-s)
      =T/lambda-2(1-r^T)/(lambda sqrt(lambda(lambda+4))).

The spatial sides contribute
2|D_R|^2(1-r^T)/sqrt(lambda(lambda+4)). Using
|1-exp(i R k1)|^2=lambda_1 |D_R|^2 therefore yields

 E(R,T):=(J_(R,T),H1^-1 J_(R,T))
   =2T[G3(0)-G3(R e1)]
    +2 integral |D_R|^2 (1-r^T)/sqrt(lambda(lambda+4))
                    * (lambda_2+lambda_3)/lambda dmu(k).   (6b)

The integrand is nonnegative and its singularity at k=0 is integrable.
Since |D_R|<=R and the last factor is at most 1, the remainder is bounded
between 0 and 2R^2 G4(0), uniformly in T. Here
G4(0)=integral [lambda(lambda+4)]^-1/2 dmu(k), obtained by integrating the
fourth Fourier coordinate. This proves(6) with the explicit bound

 0<=E(R,T)/T-2[G3(0)-G3(R e1)]<=2R^2 G4(0)/T.          (6c)

It also shows that E(R,T)/T decreases with T at fixed R, since
(1-r^T)/T decreases for 0<r<1. Two exact checks are E(1,1)=1/2, from the
four-dimensional Hodge projection's diagonal, and
lim E(1,T)/T=1/3, from 6[G3(0)-G3(e1)]=1. The scalar Laplacian convention
is essential for both constants. The exchanged rectangle has E(R,T)=E(T,R)
by four-dimensional cubic symmetry, an additional independent check.

The inherited Wilson bound now gives the actual rate statement

 limsup_(T->infinity) -log W_N(q C_(R,T))/T
       <=a q_eff^2 [G3(0)-G3(R e1)].                  (7)

It is an upper bound, not an equality or a derived Coulomb force. In
particular subtracting an unknown self energy from both sides does not
turn it into a two-sided interaction-potential estimate. Part II supplies a proposed matching
of the free-boundary state and its static insertion spectrum; its
independent review remains pending. Neither endpoint charges here nor
Wilson insertions construct dynamical charged particles.

The ordinary lattice Green asymptotic is G3(R e1)=1/(4pi R)+O(R^-3),
with G3>=0 and finite G3(0). Thus the right side of(7) is uniformly bounded
in separation. This is a bound on the rate, not a claimed asymptotic formula
for it. The Green asymptotic is standard mathematics; the normalization is
H_(Z3)=6(I-P_SRW), as in Lawler-Limic Theorem4.3.1. Even without the asymptotic,
positivity and finiteness of G3(0) give the uniform bound.

For growing rectangles of arbitrary aspect ratio, the four-dimensional
Green bound G4(x)<=C/(1+|x|^2) gives E(R,T)<=C' perimeter(C_(R,T)):
from a fixed edge, the sum over the two parallel sides is at most
2C sum_(n in Z)(1+n^2)^-1, independently of their lengths and separation.
Only parallel orientations couple. Summing over the rectangle's edges
proves the stated bound. Therefore these cubic-limit Wilson expectations
have a perimeter lower bound. The bound concerns this rectangle family in the stated free-boundary law.


## Part II. Clock correlations and static transfer matching

### 1. Domain, source, and claim separation

On a finite subcomplex of the cubic lattice, let the link variables belong to
Z_N, with positive plaquette weights

 w_beta(theta) = sum_(k in Z) exp[-beta(theta+2pi k)^2/2], beta>0.

Multiplicative constants do not affect the law. Set w_0=1 using the normalized
heat kernel's continuous beta-down-to-zero limit. Couplings may differ by
plaquette and be zero. N>=1 is fixed. Statements about monotonicity and the
free state below hold in every dimension and at every nonnegative coupling.
The later Wilson energy bound additionally assumes the pinned PR8133 large-beta
conditions and its explicit epsilon. These conditions are provisional inputs.

Published input: I. Chevyrev and C. Garban, *Villain Action in Lattice Gauge
Theory*, Journal of Statistical Physics192,38(2025), Theorem1.5, Example2.2,
Lemma3.3 and proof of Corollary1.6:
https://link.springer.com/article/10.1007/s10955-025-03420-1 .
Their U(1) carpet construction converges in total variation on coarse links;
microscopic Wilson plaquettes have coupling m^2 beta_p, and each coarse
plaquette is divided into m^2 pieces. Here m is refinement, N is clock order.
The source states Wilson-loop monotonicity for U(1); the pinned finite-clock
and arbitrary-character extensions below are proved here, not attributed to
its corollary verbatim. Its Remark1.7 rules out assuming that log w_beta has
nonnegative Fourier coefficients. The carpet construction avoids that false
shortcut.

### 2. Elementary cosine inequalities on a torus

Let theta belong to T^d with Haar measure and density proportional to
exp H(theta), where H=sum_alpha t_alpha cos(C_alpha.theta), t_alpha>=0 and
C_alpha are integer vectors. For every integer A, <cos(A.theta)> >=0: expand
each exponential in characters and use the nonnegative coefficients of
exp(t cos u). Its zero Fourier coefficient normalizes the measure.

For integer A,B, the following second inequality holds:

 Cov(cos(A.theta),cos(B.theta)) >=0.                         (1)

To prove it, write the covariance as the double integral of
[cos(A.theta)-cos(A.theta')][cos(B.theta)-cos(B.theta')]/(2Z^2)
against exp[H(theta)+H(theta')]. The torus map
(u,v) -> (theta,theta')=(u+v,u-v) is a surjective integer homomorphism;
it pushes normalized Haar measure to normalized Haar measure, despite its
multiple sheets. It need not have a single-valued inverse. The difference
of each cosine is -2sin(A.u)sin(A.v), while the weight is

 exp[2 sum_alpha t_alpha cos(C_alpha.u)cos(C_alpha.v)].

Expanding this exponential gives nonnegative coefficients multiplying squares

 [integral sin(A.u)sin(B.u) product_alpha cos(C_alpha.u)^n_alpha du]^2.

Uniform absolute convergence on the compact torus justifies integration
term by term. This proves(1). Differentiation in any t_alpha therefore makes
every cosine expectation nondecreasing. The proof uses continuous torus Haar
measure; it does not perform an invalid division by 2 on an even-order clock.

### 3. Pinning the coarse links and taking limits in the correct order

For finite h>=0 multiply the coarse U(1) measure by

 P_h(theta)=exp[h sum_(coarse edges e) cos(N theta_e)].

On a carpet graph its pullback by the coarse-edge product map pi_m is again
an exponential of positive cosines of integer forms in microscopic angles.
The pullback of any coarse character cos(J.theta) is a cosine of an integer
form as well. Section2 implies nonnegative expectation and monotonicity in
each microscopic Wilson coupling. If beta_p<=gamma_p, each microscopic
coupling m^2 beta_p<=m^2 gamma_p, with the same P_h.

For fixed h and a finite coarse complex, Theorem1.5 passes this comparison
to Villain weights: reweighting by a bounded strictly positive P_h preserves
convergence in total variation. One may see this directly from Lemma3.3:
integrating the interiors of the carpets leaves a product of the convolved
coarse plaquette weights, multiplied by P_h. Coarse-edge products of Haar
variables remain independent Haar variables. Different plaquettes may have
different couplings, as in the proof of Corollary1.6. Zero-coupling plaquettes
are constant1 and can be omitted or reached by continuity.

Next send h to infinity. The one-edge probability measure proportional to
exp[h cos(N theta)] dtheta converges weakly to uniform measure on the N roots
of unity. The finite product does too. Multiplication by the finite positive
continuous Villain weight and subsequent normalization preserve this weak
limit. Hence the limit is exactly the given finite-clock Villain law, with
no residual extra interaction. The comparison survives. For every integer
link vector J, its expectation phi(J)=<exp(i J.theta)> is real by global
inversion symmetry and obeys

 0 <= phi_beta(J) <= phi_gamma(J) <=1 if beta<=gamma.       (2)

The two-cosine covariance inequality(1) also survives, since products of
bounded continuous cosines converge in both limits. These are sequential
limits m->infinity at fixed h, followed by h->infinity. No uniform estimate
in h or interchange of these limits is claimed or needed.

#### A useful direct comparison with the continuous-angle law

The same proof also makes each character expectation nondecreasing in h,
because h multiplies positive cosine interactions on the carpet. Starting
at h=0 and ending at the clock limit gives, on the SAME finite complex,

 phi_(U1,beta)(J) <= phi_(Z_N,beta)(J).                    (2a)

Thus the Haar Wilson lower bound in the pinned free-cubic source directly
implies the finite-clock lower bound for any chosen integer representative.
The periodized upper-curvature argument in Part I is a separate
analytic route to the same estimate, explicitly displaying the full
current-lattice alias minimization (which also follows by applying(2a) to
every equivalent current). Neither proof uses a continuous variance
inequality on the integer-current law.

If M is a multiple of N, first pin to the M roots and then increase a
second positive term h sum_e cos(N theta_e). The remaining maxima are exactly
the N roots; passing the limits sequentially gives phi_(Z_M)(J)<=phi_(Z_N)(J).
The executed Z2/Z3 example has opposite orderings for charges2 and3:
the corresponding character is identically1 when its charge is a multiple
of the clock order. The theorem uses divisibility as its comparison condition. These comparisons also
pass to their free-boundary states. When both long-time rates exist, they
order the corresponding visible static energies in the opposite direction.

### 4. A unique free-boundary limit, independent of exhaustion

Embed two finite complexes in a common larger cubic box. Missing plaquettes
have coupling0 and extra links have independent clock Haar measure. For J
supported on the original links, adding plaquettes increases phi(J) by(2).
Thus phi(J) has a limit along the directed set of all finite plaquette sets
and edges containing its support, bounded between 0 and 1. Every cofinal
increasing exhaustion has this same limit.

Finite-clock Fourier characters determine each finite-dimensional marginal:
probabilities follow from the finite inverse Fourier transform. Compactness
therefore gives one limiting free-boundary measure mu_free, without choosing
a subsequence. At homogeneous coupling it is translation invariant and has
the lattice symmetries, because translating an exhaustion is cofinal. Its
finite Gibbs conditional identities pass by positivity and finite range.

This proves uniqueness of the free-boundary limit, NOT uniqueness among all
Gibbs states, clustering, ergodicity, or absence of broken symmetry. It also
does not prove a Gaussian continuum law.

For fixed spatial box L, let the time interval grow in both directions
around a fixed observable. That limit exists by the same monotonicity. Now
let L grow. For each character the resulting iterated limit is its supremum
over all finite space-time boxes, hence equals mu_free. Cubes are another
cofinal exhaustion, so their previously established Wilson lower bound
applies in this same state. Thin-slab curvature estimates were never used.

### 5. Explicit transfer matrix and external charge sector

Fix beta>0 and a finite connected spatial box, with spatial links E_s and vertices V_s.
Use counting Haar inner product on H_L=ell2(Z_N^E_s). For link a write

 V(a)=product_(spatial plaquettes p) w_beta((d1 a)_p),
 C(a,a')=product_(spatial links e) w_beta(a_e-a'_e),
 T=V^(1/2) C V^(1/2).                                  (3)

Angles in these formulas are2pi a/N. The kernel C is convolution with a
strictly positive function. Its Fourier eigenvalues are strictly positive:
each one-link coefficient is proportional to
sum_(r congruent k mod N) exp[-r^2/(2beta)]>0. Therefore T is positive definite
and self-adjoint. It is also strictly positive entrywise. Its largest
eigenvalue lambda_0 is simple, with a positive normalized eigenvector Omega_0.

Spatial gauge translations a->a+d0 eta commute with both C and V. Uniqueness
and positivity of Omega_0 imply gauge invariance. Let gamma be an oriented
spatial path from x to y, and U_gamma(a)=exp[2pi i q gamma.a/N]. With the
convention (R_eta f)(a)=f(a+d0 eta), the vector U_gamma Omega_0 is in the
character sector rho=q d0*gamma=q(delta_y-delta_x), modulo N. Call the
restriction of T to this sector T_rho. It is positive definite and its norm
is at most lambda_0. Only the total-zero charge sectors used here are needed.

For completeness the finite-time boundary vector is b=V^(1/2). Temporal
links can be put in temporal gauge on an open interval: recursively translate
the spatial link variables to remove each temporal link. This is an exact
bijection of finite clock variables up to the initial gauge freedom and a
constant multiplicity. Every temporal plaquette then has difference a-a',
each spatial plaquette keeps V, and the closed rectangular Wilson character
becomes U_gamma(a_0) conjugate(U_gamma(a_T)). The partition function is
<b,T^M b>. The square-root split in(3) gives full V on every time slice,
including the endpoint factors supplied by b.

Put the loop endpoints far from both free temporal boundaries. Perron-Frobenius
convergence T^n b/lambda_0^n -> <Omega_0,b> Omega_0 gives exactly

 W_L(R,T)=<U_gamma Omega_0,(T_rho/lambda_0)^T
                                  U_gamma Omega_0>.       (4)

Global inversion makes the sign-reversed convention identical. The spectral
measure nu_(L,R) of the normalized vector U_gamma Omega_0 is a probability
measure on(0,1]. Equation(4) is its Tth moment. This is the external static
charge sector of the isotropic clock Villain transfer matrix; it is not the
separate N=3 penalty Hamiltonian and contains no dynamical matter field.

### 6. Spatial limit, spectral meaning, and energy bound

For each nonnegative integer T, Section4 gives
W_L(R,T)->W_free(R,T) as L grows around gamma. Probability measures on[0,1]
are compact, and moments determine a measure there: polynomials are uniformly
dense in continuous functions. Consequently nu_(L,R) converges weakly to a
unique probability measure nu_R on[0,1], and

 W_free(R,T)=integral_[0,1] lambda^T nu_R(dlambda).         (5)

This alone constructs a positive-contraction representation on L2(nu_R),
with multiplication by lambda and cyclic vector1. A possible atom at 0 is an
infinite-energy component killed after one time step; no absence of such an
atom is inferred from weak convergence. On(0,1] the Hamiltonian is the
self-adjoint multiplication operator -log lambda.

Let lambda_*(R)=sup support(nu_R). The elementary moment argument gives
lim_(T->infinity) W_free(R,T)^(1/T)=lambda_*(R): the upper bound uses
lambda<=lambda_*, and the lower bound uses positive mass in every interval
(lambda_* -eta,lambda_*]. Applying the cubic Wilson lower bound and its
exact rectangle Green limit proves lambda_*>0 and

 E_visible(R):=-log lambda_*(R)
   =-lim_(T->infinity) log W_free(R,T)/T
   <= (beta^-1+epsilon) q_eff^2 [G3(0)-G3(R e1)],          (6)

with E_visible(R)>=0 and q_eff a smallest absolute representative of q mod N.
For q=0 mod N the observable is identically1, nu_R=delta_1 and E_visible=0.
For unit spatial separation,6[G3(0)-G3(e1)]=1 fixes the normalization.
Since0<=G3(R)<=G3(0)<infinity, the energy cost is uniformly bounded as the
test charges separate.

E_visible is the bottom of the spectral support reached by this path
insertion in the matched limiting transfer representation. It need not be
the bottom of every conceivable infinite-volume charged representation; nor
does weak convergence justify exchanging spatial limits with spectral
infima. Equation(6) bounds this specific physically defined static insertion
without making either claim. It does not give a Coulomb force equality,
propagating charged particles, a photon, or an axiom-selected law.

### 7. Completed author challenges and remaining review

The primary runner checks 16 finite three-cube coupling cases, each with
six separate plaquette increases and 4000 sampled arbitrary-character pairs.
Clock orders 2,3,4,5 include even orders. Fourier probabilities give minimum
cosine covariance and monotonicity increments no lower than -1e-15, within
floating error. Four integrated-carpet and three finite-pinning cases approach
their separately evaluated limits. Twelve Haar/clock comparisons, two
subgroup comparisons and a nondivisibility control challenge(2a).

Five spatial-square transfer systems have dimensions 16,16,81,81,256. They
compare explicit temporal-link sums with temporal gauge at three lengths and
four charge labels each. The maximum discrepancy is below 1.9e-15. Direct
spectral sums agree within 3.3e-15. Omitting the temporal charge phases or the
spatial endpoint weights changes the observable, as the controls verify.

Two initial convergence checks used approximations too coarse for their
stated tolerances; their frozen sources and failures are preserved. Increasing
carpet refinement 64->128 and pinning 128->512 resolves them without loosening
tolerances. A later nondivisibility control requested an arbitrary 0.1 numerical
separation that was too large at beta 0.6; its failure is preserved and a
beta 0.15 control resolves the two opposite signs with large margins. This is
a fixture change, not a change to the divisibility theorem.

These low-dimensional finite probes do not certify the four-dimensional
source theorem, infinite limits, or spectral identification. The written
proof and its source dependencies remain subject to independent review.


## No-Go Discipline Gate

The claimed result is an affirmative bound and a matched spectral
construction. The following checks delimit its scope; no universal phase,
method-impossibility or axiom-wall claim is submitted.

### N1 — Distinct inference checks

| Honesty | Attempted shortcut | Actual challenge and disposition |
|---|---|---|
| ATTEMPTED | Periodize without the evenness/upper-curvature hypotheses | The one-dimensional controls give explicit different ratios when the center or curvature is changed; Part I.2 retains both hypotheses. |
| ATTEMPTED | Replace the physical Wilson coset or omit its magnetic factor | Direct clock enumeration distinguishes both altered expressions; the exact coset and charge aliases are retained. |
| ATTEMPTED | Compute a rectangular current using only its long sides | The omitted-end control has nonzero divergence and a different Poisson energy; the full conserved current is used. |
| ATTEMPTED | Order finite-clock character laws by numerical clock size | The Z2/Z3 characters with charges2 and3 give opposite comparisons; the positive subgroup theorem assumes divisibility. |
| ATTEMPTED | Use a neutral or incorrectly weighted transfer formula for a charged insertion | Explicit temporal-link sums distinguish the omitted charge phases and endpoint weights; Part II.5 keeps both. |

These are different finite mathematical checks, not an exhaustive enumeration
of possible physical phases or methods. Twelve actual source mutations also
fail the corresponding assertions; their changed formulas and stderr are in
the committed author packet.

### N2 — Dependency relations

The Wilson bound uses the provisional source curvature; the static spectrum
also uses the separately derived free-state and transfer matching. The rate
estimate is downstream of both, so these are not counted as independent
physical walls. Physical law selection and dynamical matter are unproved
extensions, and no pairwise independence claim or wall count is assigned.

### N3 — Explicit hypotheses

The law and its parameters are supplied. The source's large-beta constants,
cubic boundary, fixed odd filling and all-real-source estimate are retained.
Clock pinning uses successive limits. Transfer positivity in Part II.5 uses
beta>0; zero coupling is included in the correlation and free-state comparison.
Free-boundary uniqueness is distinct from a statement about all Gibbs states.
No extra primitive is silently asserted by these mathematical constructions.

### N4 — Matched evidence

The current/clock fixture tests the actual external-character coset. The
Green fixture tests conserved rectangular currents with the stated scalar
Laplacian normalization. The temporal-link fixture tests the same finite
Villain transfer law, its spatial endpoint weights and its charge character.
The carpet and pinning probes concern the limiting mechanism in Part II.3;
they do not execute the published all-refinement theorem. No different
Hamiltonian or a prior no-go is used as a witness for the static bound.

### N5 — Resolution

The primary cache states all five resolution classes. Finite matrix elements,
vertex gauge characters, transfer spectra, finite current/clock sums and
periodic Poisson energies are executed. Infinite free-state matching and
static-rate existence are written proofs, checked and not numerically
executed. No stronger result is inferred from the finite fixture sizes.

### N6 — Affirmative alternatives

The thin-slab restriction was bypassed by a different state-matching proof,
not by changing the source's boundary domain. The direct Haar-to-clock
comparison and the periodized curvature lemma give two analytic routes to
the same Wilson estimate. The source is supplied mathematics; no approved
primitive is declared absent and no axiom update is requested.

### N7 — Strongest limitation

A bounded external static energy does not settle the remaining field or
matter question. The bound leaves the spectrum's detailed form and higher
field correlations undetermined. The matched spectral threshold is the one
reached by the displayed path insertion; neither a pole nor an unrestricted
infinite-volume charged-sector ground state is inferred. A full field or
matter construction must address those different observables directly.

### N8 — Relation to earlier work

Classical nonconfinement and transfer criteria predate this campaign. The
published carpet theorem is credited explicitly. The prior source's thin-box
control remains intact, while its associated static matching obligation is
addressed here. Earlier periodic covariance and continuous-Haar Gaussian
proposals keep their own hypotheses; this result does not promote them or
supply a full fixed-clock Gaussian law by terminology.

## Review record and reproduction

The primary runner combines the three private author probes into one
self-contained source. Its twelve finite check families retain the original
calculations and fault controls. All generated evidence is emitted in the
canonical cache; it writes no scientific input or audit status. Numerical
comparisons use floating arithmetic and do not provide interval certification.
The paper's uniform carpet theorem and this note's limit proofs carry the
infinite claims, rather than refinement counts or finite PASS lines.

The original approximation failures and their frozen scripts are durable at
campaign commit `677dac52fcb5cb31c682503bf2fa981620d3747b`; they are historical
author provenance, not a scientific input needed to reproduce this note.
The earlier four source notes and their runners are unchanged in this delta.
Independent review, a current-main combined validation, and the independent
formal audit path remain required before assigning retained authority.

Run the declared primary runner through `scripts/runner_cache.py` using its
`execute_and_write_cache` function and declared 300-second timeout. The author
packet records actual cache validation, mutation checks and source hashes.
No editable prompt, axiom, primitive, or authoritative audit record is changed.
