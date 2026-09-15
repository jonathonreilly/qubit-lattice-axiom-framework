---
claim_id: preconditioned_extended_gradient_gaussian_remainder_and_free_cubic_riesz_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For an even finite-dimensional Gaussian measure perturbed by a C3 interaction with the stated uniform Schur Hessian and third-influence bounds, preconditioned source variation gives a volume-uniform cubic log-MGF remainder; a free-cube reflection and discrete Riesz argument supply the required cochain ell3 bound, and the declared carrier hypotheses satisfy the derivative conditions at sufficiently large fixed beta."
upstream_dependencies:
  - carrier_preserving_closed_integer_charge_gas_convexification_bounded_theorem_note_2026-09-15
  - free_cubic_magnetic_local_fillings_and_positive_electric_current_convex_extension_bounded_theorem_note_2026-09-15
runner: scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py
---

# Gaussian remainders for extended gradient interactions on free cubes

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** proposed_retained

For an even finite-dimensional Gaussian measure perturbed by a C3 interaction with the stated uniform Schur Hessian and third-influence bounds, preconditioned source variation gives a volume-uniform cubic log-MGF remainder; a free-cube reflection and discrete Riesz argument supply the required cochain ell3 bound, and the declared carrier hypotheses satisfy the derivative conditions at sufficiently large fixed beta.

This is an author theorem proposal. The written proof and its provisional
upstream sources await independent mathematical review and formal audit.
The supplied continuous-angle law is an explicit model input; it is not
derived from the framework axioms, and no axiom or primitive is changed.

## Status, scope and proof obligations

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Establish a fixed-law full physical-score limit while preserving the probability law, observable and state."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently check this fixed-Haar proof chain, then address the separate quantized electric defects before making a finite-clock inference."
conditional_surface_status: "The explicitly supplied law, cubic exhaustion, carrier conditions and operator smallness conditions in the proof."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A quantified analytic theorem proposal with finite challenges of distinct calculation paths; the supplied-law and independent-review boundaries remain explicit."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The single-sentence claim above is the target contract. An auxiliary
Langevin time below is a proof parameter, distinct from all four Euclidean
coordinates. Finite calculations challenge the argument; they do not
execute an infinite-volume theorem or ratify its status.

## Imports and obligation graph

| Input or obligation | Provenance and role | Proof status |
|---|---|---|
| Finite Gaussian perturbation and ambient coordinate norms | Supplied mathematical data, with all hypotheses stated below | Cubic remainder proved here |
| Free-cube Hodge operator and ell3 norm | Counting-inner-product cubical incidence | Reflection and periodic Riesz proof here |
| [Carrier expansion](CARRIER_PRESERVING_CLOSED_INTEGER_CHARGE_GAS_CONVEXIFICATION_BOUNDED_THEOREM_NOTE_2026-09-15.md) | Provisional parent source at f8e7219b5e79bcb271bb3c1df635ecdeeb57dbe8; full carrier mass and root estimates | Explicit upstream proof awaiting review |
| [Boundary-compatible integer fillings](FREE_CUBIC_MAGNETIC_LOCAL_FILLINGS_AND_POSITIVE_ELECTRIC_CURRENT_CONVEX_EXTENSION_BOUNDED_THEOREM_NOTE_2026-09-15.md) | Same parent revision, sections1-2; actual free-cube Hodge kernel and local fillings | Explicit upstream proof awaiting review |
| Standard SDE existence, spectral theorem and interpolation | Mathematical machinery, with finite-dimensional Lipschitz and kernel hypotheses checked below | No model-specific phase theorem imported |
| Physical state and covariance identification | Separate companion derivation; not assumed by this finite lemma | Outside this note's target |

The strongest additional physical obligation is the matched infinite-state
covariance limit. The finite theorem does not assume that limit. The two
parent sources must land before this child is reviewed separately, or be
included in the same frozen cumulative review unit. Their unreviewed status
is not converted to an established premise by this source.

## 1. Finite-dimensional assumptions

Let Gamma be a linear subspace of R^M. Let K be a real symmetric matrix
with kernel Gamma-perp and positive definite restriction K_Gamma to Gamma.
Use unnormalized coordinate ell^p norms in the ambient R^M and positive
upper bounds k2,k3. If Gamma={0}, the law is a point mass and the conclusion
is immediate; the following proof treats the nonzero subspace. Assume

 ||K||_(2->2)<=k2, ||K||_(3->3)<=k3.

Self-adjointness gives ||K||_(3/2->3/2)=||K||_(3->3). Let R:R^M->R be C3
with, uniformly for all real omega,

 ||R''(omega)||_(p->p)<=delta, p=2,3,3/2,
 ||R'''(omega)[a,b]||_(3/2)<=M3 ||a||_3 ||b||_3.       (1)

In the second line, R'''[a,b] is a vector obtained by contracting two
arguments. Suppose k2 delta<1 and k3 delta<1. Define

 C3=k3/(1-k3 delta).

All hypotheses and constants are finite-dimensional, and may be supplied
uniformly for a family. The potential may contain interactions among many
coordinates. No independent-coordinate or scalar-field assumption is used.
Define on Gamma the tilted probability law

 mu_h(domega) proportional to
 exp[-(omega,K_Gamma^-1 omega)/2+R(omega)+(h,omega)] domega,
 F(h)=log integral_Gamma exp[-(omega,K_Gamma^-1 omega)/2
                              +R(omega)+(h,omega)] domega.             (2)

The Hessian in Gamma of the negative exponent is at least
(1/k2-delta)I. Hence(2) is proper for every real h, all linear exponential
moments exist, and F is smooth in h. R itself need not be convex. If R is
even, mu_0 is centered.

## 2. Claimed conclusion and why it is enough

For all real h and all ambient real a,b,c, the bound is

 |D^3F(h)[a,b,c]|<=M3 C3^3 ||a||_3 ||b||_3 ||c||_3.   (3)

Taylor's theorem then gives

 |F(h)-F(0)-DF(0)[h]-D^2F(0)[h,h]/2|
 <=M3 C3^3 ||h||_3^3/6.                              (4)

Consequently, for a family with bounded M3 C3^3, suppose h_n^1,...,h_n^r
satisfy ||h_n^j||_3->0, and the covariance matrix of their centered linear
statistics under mu_0 converges to a finite matrix Sigma. Applying(4) to
every fixed real linear combination shows convergence of their real MGFs
to exp[t^T Sigma t/2], for all fixed t in R^r. This implies joint convergence
to N(0,Sigma). It establishes Gaussianity once the covariance converges;
it does not identify that covariance or ensure a unique limit.

A uniform covariance upper bound suffices to extract Gaussian subsequential
limits for a finite set of tests. That is weaker than the named Maxwell
limit and must not be substituted for covariance homogenization.

## 3. Proof through a finite-time preconditioned flow

On Gamma, starting at omega_0=0, consider the SDE

 d omega_t =[-omega_t+K grad R(omega_t)+K h]dt
             +sqrt(2K)dB_t.                          (5)

The noise and drift preserve Gamma. The density(2) is invariant by direct
integration by parts in Gamma: the drift equals K times the gradient of
its log density. Global boundedness of R'' makes the drift globally
Lipschitz. The positive Hessian lower bound in section1 supplies all
stationary moments. With synchronous Brownian noise, variation of
constants and Gronwall give

 ||omega_t-omega'_t||_p
 <=exp[-(1-kp delta)t]||omega_0-omega'_0||_p.

In particular the p=2 bound, applied with a stationary initial condition
having law mu_h, proves E omega_T^h -> E_mu_h omega as T tends to infinity.
This is for each finite dimension and fixed h. Neither a uniform bound
on the Brownian path nor a dimension-uniform mixing theorem is assumed.

For finite T the first source derivative v_a(t)=D_a omega_t^h obeys

 v_a(t)=(1-exp[-t])K a+integral_0^t exp[-(t-s)]
                    K R''(omega_s^h) v_a(s) ds.      (6)

The time-integral operator has norm at most k3 delta on the normed space
sup_(0<=t<=T)||v(t)||_3. Thus

 sup_(0<=t<=T)||v_a(t)||_3<=C3||a||_3.               (7)

This holds for every noise realization and every T. A second derivative
w_bc(t)=D_bD_c omega_t^h obeys

 w_bc(t)=integral_0^t exp[-(t-s)] K
   [R''(omega_s^h)w_bc(s)+R'''(omega_s^h)[v_b(s),v_c(s)]] ds.            (8)

The same contraction in ell^(3/2), using self-adjointness of K and(1),(7),
gives

 sup_(0<=t<=T)||w_bc(t)||_(3/2)
 <=M3 C3^3 ||b||_3 ||c||_3.                          (9)

Finite-time source differentiation follows from the usual difference-
quotient equations for a finite-dimensional SDE with additive noise and
C2 drift. Here it is simply differentiation of a random integral equation;
(1),(7),(9) supply deterministic bounds on the derivatives. Thus, putting
m_T(h)=E omega_T^h, Holder gives

 |D_bD_c(a,m_T(h))|<=M3 C3^3||a||_3||b||_3||c||_3.

To pass this bound to stationarity, no interchange of an infinite-time
limit with a derivative is needed. Integrate the displayed bound over a
source rectangle h+s b+t c,0<=s<=u,0<=t<=v. The resulting four-term
finite-difference bound passes to the limit T->infinity because each
m_T at a rectangle corner converges to m(h)=E_mu_h omega. Divide by uv
and let u,v decrease to zero. The function m(h)=DF(h) is already smooth
by the proper Gaussian tails in(2), so its mixed derivative has the same
bound. This proves(3).

The limiting step does not assume convergence of derivatives of stationary
stochastic solutions.

## 4. Checkable sufficient conditions for extended carrier interactions

Suppose R has an absolutely convergent rank-one interaction expansion

 R(omega)=sum_lambda r_lambda(u_lambda dot omega),

with derivatives through order3 convergent on bounded sets. Assume
|r_lambda''|<=b_lambda and |r_lambda'''|<=b_lambda (different bounds can
also be used). Set

 delta=sup_i sum_lambda b_lambda |u_lambda,i| ||u_lambda||_1,
 M3=sup_i sum_lambda b_lambda |u_lambda,i| ||u_lambda||_1^2.             (10)

The absolute Hessian has row and column sums at most delta, so its norm
on every ell^p,1<=p<=infinity, is at most delta. For the third derivative
let T_ijk=sum_lambda b_lambda|u_i u_j u_k|. Each one-index marginal sum
of this nonnegative symmetric tensor is at most M3. Holder on the measure
T_ijk, followed by summing the marginal, gives

 sum_ijk T_ijk |a_i b_j c_k|<=M3||a||_3||b||_3||c||_3.

Duality proves the bilinear bound in(1). This argument retains the entire
carrier index and total variation; regrouping disconnected net charges is
not needed. A sine/cosine polymer term has the required bounded real
second and third derivatives, with the frequency included in u_lambda.

Uniform small Hessian norm alone is not enough. For example let K=I_M,
a_M=M^-1/2(1,...,1), R(omega)=zeta cos(a_M dot omega),0<zeta<1. The
normalized collective coordinate a_M dot omega has the same non-Gaussian
one-dimensional density proportional to exp[-z^2/2+zeta cos z] for every M.
Its test has ||a_M||_3^3=M^-1/2->0, but M3 in(10) grows as zeta sqrt(M).
The hypotheses correctly refuse to infer a Gaussian limit for this model.
A dimensional Hessian bound cannot replace the uniform third-order
influence condition.

## 5. Three-form preconditioner and compatible gradient variables

In dimension four put H=H_3, G=H^(-1), c=1/32.
For the intended cochain application choose the local Hodge derivative
Dcal phi=(d_2*phi,d_3 phi), so Dcal*Dcal=H. Let

 omega=beta^-1/2 Dcal phi,
 K=Dcal(G-cI)Dcal*, Gamma=range(Dcal).

This K is positive on Gamma, has k2<=1 and the nonzero spectrum in
[1-c||H||,1]. The Gaussian pushforward of phi~N(0,beta(G-cI)) is gamma_K.
Every closed charge with a declared local integer filling q=d_2 n obeys

 2pi(q,phi)=2pi sqrt(beta)(n,omega_first).

The carrier expansion gives a cosine extension R. Section8 verifies its
Schur Hessian and third-influence bounds using the two declared upstream
carrier and filling estimates. A quadratic-form estimate alone would not
supply the required ell3 bound.

## 6. Free-cube reflection removes the boundary mismatch

There is an explicit reflection that intertwines both d and d* for the
free cubical boundary convention. In one dimension put N=L+1, with N
vertices0,...,N-1 and N-1 edges0,...,N-2. Extend to the periodic cycle
of length2N. For vertex data f define

 (E0 f)(x)=f(x),0<=x<N;
 (E0 f)(x)=f(2N-1-x),N<=x<2N.

For edge data g define

 (E1 g)(x)=g(x),0<=x<N-1;
 (E1 g)(N-1)=(E1 g)(2N-1)=0;
 (E1 g)(x)=-g(2N-2-x),N<=x<2N-1.

For delta f(x)=f(x+1)-f(x) and its unweighted adjoint, direct substitution
at interior and endpoint coordinates gives

 delta_per E0=E1 delta_free,
 delta_per* E1=E0 delta_free*.                       (11)

Each input value occurs twice with the same absolute value, so
||Ej f||_p=2^(1/p)||f||_p. Tensor the extensions along the d coordinate
axes, choosing E1 on axes contained in the cell orientation and E0 on the
other axes. The usual alternating cochain signs occur identically in the
periodic and free differentials. Thus for every degree r,

 d_per E_r=E_(r+1) d_free,
 d_per* E_r=E_(r-1) d_free*,
 ||E_r f||_p=2^(d/p)||f||_p.                         (12)

For r>=1 the extension has zero mean in at least one coordinate direction,
because it is odd in an edge direction. Hence H_per^+ E_r=E_r H_free^-1;
there is no imported harmonic zero mode. Apply(12) also to the direct sum
of degree2 and degree4 outputs of Dcal. It follows that the free Hodge
projection Dcal H_free^-1 Dcal* is the restriction, by this isometric-up-
to-a-common-factor embedding, of Dcal_per H_per^+ Dcal_per*. Its ell^p
norm is therefore bounded by the periodic projection norm, with no factor
that grows with L.

The periodic scalar second-order
Riesz bound proved in section7, uniformly in the period, is for

 delta_mu H_0,per^+ delta_nu* on ell^p,1<p<infinity.  (13)

Using that bound, each matrix entry of the degree3 Hodge
projection is a sum of at most4 shifted copies of operators(13). There
are7 output components (six two-form components and one four-form
component). If each scalar entry has bound kappa_p, a deliberately loose
coordinate-norm bound for the whole projection is28 kappa_p. Forward and
backward differences differ only by signs and translations, which are
ell^p isometries. The zero Fourier mode is assigned zero. The local
correction c Dcal Dcal* has norm at most64c in every ell^p, since Dcal has
row and column absolute sums at most8. In particular one may take

 k3 <=28 kappa_3+64c,                               (14)

uniformly in every free four-cube. Only finiteness matters for choosing a
sufficiently large fixed beta.

## 7. Direct periodic Riesz proof

Here is a direct proof of(13).
For m>0 on Z^d write delta_j(k)=exp(i k_j)-1 and
lambda(k)=sum_j |delta_j(k)|^2. The scalar multiplier is

 M_mu,nu,m(k)=delta_mu(k) conjugate(delta_nu(k))/(lambda(k)+m^2),
 k in [-pi,pi]^d.                                    (15)

Its absolute value is at most1, hence its ell2 norm is at most1 by
Plancherel. In a fixed coordinate chart around0, differentiation of the
rational expression, using lambda(k) comparable to |k|^2, shows

 |partial^alpha M_mu,nu,m(k)|<=C_(alpha,d)|k|^(-|alpha|), k!=0,          (16)

uniformly in m>0. Each derivative either differentiates a smooth numerator
vanishing quadratically or a denominator bounded below by const|k|^2+m^2;
rescaling k=r u on an annulus r/2<=|k|<=2r makes all such derivatives
uniformly bounded in m/r. Away from0 the bounds are uniformly smooth.

Use a smooth dyadic partition of unity into annuli of radii r=2^-j near0
and finitely many smooth periodic coordinate charts away from0. A localized
multiplier on an r-annulus has derivatives of order n bounded in L1 by
C r^(d-n). Repeated integration by parts in its compact coordinate chart
therefore bounds its Fourier coefficient K_r(x) by

 |K_r(x)|<=C r^d(1+r|x|)^(-d-2).

The same argument after differentiating the Fourier transform with respect
to its real argument gives C r^(d+1)(1+r|x|)^(-d-2). Integrating this latter
bound along the segment from x to x-y, with |x|>=2|y|, yields the difference
bound C |y| r^(d+1)(1+r|x|)^(-d-2). The finitely many away-from-zero
charts satisfy the same estimates with r comparable to1. Summing over
annuli gives the uniform kernel estimates

 |K_m(x)|<=C(1+|x|)^(-d),
 |K_m(x-y)-K_m(x)|<=C |y|(1+|x|)^(-d-1), |x|>=2|y|.                  (17)

In particular the discrete Hormander sum over |x|>=2|y| of the second
absolute difference is bounded by a dimension-dependent constant. The
case y=0 is zero. These estimates also follow as limits of finite annular
sums; their ell2 multiplier norms are uniformly bounded by the finite
overlap of the partition.

For clarity, the standard discrete Calderon-Zygmund step can be carried
out on dyadic cubes in Z^d. Given a summable function f and threshold a>0,
choose maximal dyadic cubes Q whose average |f| exceeds a. Their total
cardinality is at most ||f||1/a, and each cube average is at most2^d a.
Write f=g+sum_Q b_Q, with g equal to the cube average on each Q and f
elsewhere. Then ||g||infinity<=2^d a, ||g||1<=||f||1, each b_Q has zero
sum, and sum_Q||b_Q||1<=2||f||1. The ell2 bound controls the exceptional
set for Tg by const||f||1/a. Outside fixed enlargements of the cubes,
subtract the kernel value at a chosen cube center and use the Hormander
sum in(17) to get

 sum_(outside enlarged cubes)|T sum_Q b_Q|<=C||f||1.

The enlarged cubes themselves also have cardinality at mostC||f||1/a.
Chebyshev's inequality proves a uniform weak(1,1) bound. Marcinkiewicz
interpolation with the ell2 bound gives a uniform strong ell^(3/2) bound.
The adjoint swaps mu and nu and obeys the same bounds, so duality gives
a uniform strong ell3 bound. This argument uses the standard interpolation
inequality between weak(1,1) and strong(2,2), not an assumption about the
unknown gauge measure.

For fixed m>0 the multiplier(15) is smooth on the whole torus and its
kernel is absolutely summable. Periodizing that kernel on a finite cycle
product gives the corresponding finite-period multiplier. Its ellp norm
is no larger than the infinite-lattice norm: first truncate the summable
kernel, apply the infinite-lattice operator to a periodic test repeated
on an increasing union of periods, divide the pth power norm by the
number of periods, and let the union grow. Finite kernel range makes the
boundary fraction vanish. Then remove the kernel cutoff using its ell1
tail. Finally let m decrease to zero on the fixed finite torus. Each
nonzero Fourier mode converges to the multiplier with denominator lambda;
the zero mode remains zero. Finite-dimensional norm convergence preserves
the same uniform bound. This proves(13), in particular at3 and3/2, with
finite constants depending only on dimension and exponent.

The proof checks the inverse, the zero mode, the mass-uniform derivatives,
and the finite-period transfer separately. The reflection proof
then supplies the intended free-cube estimate; it does not assume that
an arbitrary boundary-value projection enjoys the same bound.

## 8. Carrier bounds in the required operator norms

Set d=4, p=3, Delta=2(d-p)(2p+1)=14, t=pi^2 beta/(4d),
u_t=2 exp(-t/2)/(1-exp(-3t/2)), and
R_t=e u_t/(1-Delta^2 e u_t). Require Delta^2 e u_t<1 and
(Delta+1)R_t<=1. These are precisely the parent carrier smallness
conditions. The full theorem additionally requires delta<1/2 and
k3 delta<1, using the constants below.

Keep every cluster C with its full carrier and total individual charge
mass S, as in the declared carrier and free-cube filling sources.
Let a_C be its real source-independent coefficient, so pairing charge
reversal allows the real representation

 R(omega)=sum_C a_C cos[2pi sqrt(beta)(n_C,omega_first)].

The sum here still runs over the original paired cluster index; it does
not aggregate clusters by net charge. Assume the previously stated
carrier and local-filling estimates, with d=4:

 sum_(C:x in U(C),S(C)=S)|a_C|<=R_t exp[-tS/2],
 ||n_C||_infinity<=d S,
 #support(n_C)<=K0 S^d, K0=2^d 6^d,
 #possible carrier anchors within a filling box at y<=C1 S^d,
 C1=2^d 11^d.

These imply ||n_C||_1<=d K0 S^(d+1). Substituting
u_C=2pi sqrt(beta)n_C into(10), and summing over anchors before clusters,
gives the explicit bounds

 delta <=(2pi)^2 beta d^2 K0 C1 R_t
                   sum_(S>=1) S^(2d+2)exp[-tS/2]
        = beta epsilon_t,

 M3 <=(2pi)^3 beta^(3/2) d^3 K0^2 C1 R_t
                   sum_(S>=1) S^(3d+3)exp[-tS/2].     (18)

Both are uniform in volume and real omega. The mass reserve proves
absolute convergence of all derivatives involved. Delta tends to zero
exponentially in beta; M3 is finite for each fixed beta in the expansion
regime and also tends to zero as beta grows. M3 need not be small to apply
the lemma: only k3 delta<1 is a contraction requirement.

With(13) proved above and the declared provisional carrier estimates,
there exists a finite beta0 such that for every fixed beta>=beta0 the
actual auxiliary linear sources have Gaussian log-MGF remainder bounded
by const(beta)||h_a||_3^3=O_beta(a^2). This establishes the finite cubic remainder under the stated hypotheses.
The covariance and physical-state conclusions require the companion
thermodynamic and observable arguments; no periodic-state match is used
by this finite lemma.

## Method context

The preconditioned source-variation strategy is motivated by
[Conlon and Dabkowski (2025), sections4-5](https://link.springer.com/article/10.1007/s10955-025-03478-x).
All39pages were personally read. Its scalar nearest-neighbor theorem is
not imported for the extended cochain interaction; the required vector
operator assumptions and finite-time limiting argument are given here.
No novelty is claimed for Gaussian perturbation or Riesz machinery.

## Finite evidence and No-Go Discipline Gate

The paired runner reads no repository scientific input or package-integrity
file and writes only stdout. It constructs integer cochains, compares
independent positive Gaussian/image integrations and Poisson sums, inverts
Gaussian precision on an independently chosen compatible basis, and solves
symmetry commutants exactly. Floating errors and quadrature cutoff changes
are reported as observed comparisons, not rigorous interval certificates.
The all-volume assertions are carried by the written proof and await
independent review. One shared runner supplies the complete finite packet
for the three companion notes; no undeclared helper is required.

### N1 — Attempted inference controls

| Honesty | Attempted inference | Witness and actual conclusion |
|---|---|---|
| ATTEMPTED | Treat the auxiliary factor as a characteristic function | `three_cube` compares the original magnetic sum, Poisson comb and positive integral; the wrong-sign factor disagrees for nonclosed sources. The exact map uses a real MGF. |
| ATTEMPTED | Use the same zero-extension rule for closed charges and co-closed gradients | `nested_projection` embeds exact finite cochains: codifferentials extend, while the specified closed three-charge develops a nonzero exterior derivative. The proof uses the appropriate space. |
| ATTEMPTED | Infer diffuse-source Gaussianity from a small Hessian alone | `collective_control` has a dimension-independent non-Gaussian collective coordinate; its third-influence constant grows. The uniform third-order hypothesis is retained. |
| ATTEMPTED | Substitute the mean Hessian for the effective covariance response | `layered_checks` compares full Gaussian precision with the response and its Schur limit; the mean-Hessian shortcut has a persistent discrepancy. The fluctuation term is retained. |
| ATTEMPTED | Obtain an ergodic Gaussian limit by averaging a global anisotropic orientation | `invariant_mixture_control` has a positive fourth cumulant, computed as three times the variance of component variances. The actual proof symmetrizes the potential and constructs an ergodic factor. |
| ATTEMPTED | Infer theta upper domination from small uniform convexity | `theta_upper_hypothesis_control` gives variance greater than the Gaussian reference. The physical theta inequality is a separately derived structural fact. |
| ATTEMPTED | Count four reflected current components as photon polarizations | `image_score_and_reflection` imposes current conservation and obtains a positive rank-two projector; the unreduced time metric has a negative direction. |

These are explicit positive counterexample witnesses and proof-hypothesis
checks. None is a no-go for a physical phase or an axiom update. No route
is marked RULED OUT BY PRIOR.

### N2 — Dependencies and collapse

There is no asserted collection of independent physical walls, so the
pairwise physical-wall table is empty and the physical-wall count is zero.
The controls are not added as independent evidence of phase failure.
Source unfolding, finite cumulant control, thermodynamic identification,
replica concentration and spectral response instead form one dependent
positive proof chain. Failure of a linked input invalidates its dependents;
it does not prove a separate axiom obstruction. The two averaging controls
challenge different steps of that same state/covariance chain and are not
counted as two independent phase exclusions.

### N3 — Hidden-hypothesis scan

The law, continuous link domain, counting metric, free cubic boundaries,
integer topology, order of limits, real sources, smallness conditions and
carrier bounds are explicit. The auxiliary time is distinguished from
physical Euclidean time. Standard SDE, interpolation, spectral and Gaussian
machinery is mathematical input with checked domains, not an imported
photon phase. The source has no assumed Maxwell covariance or Gaussian
limit at a terminal step. The provisional parent proofs and independent
review requirement remain explicit. No framework primitive is introduced.

### N4 — Residual matching

| Packet witness | Residual tested | Match and limit |
|---|---|---|
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:180` (`exact_hodge`), `three_cube` | Actual source, sign, Gaussian split and covariance normalization | Yes, exact finite cochains and the same normalized three-cube flux; no all-volume proof is executed |
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:63` (`reflection`), `nested_projection` | Boundary incidence and compatible-space embedding | Yes, finite instances of the specified free-box construction |
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:115` (`positive_integrals`), `collective_control` | Finite source derivatives and the third-influence hypothesis | Yes, positive finite measures with the stated comparison geometry |
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:306` (`layered_checks`), `symmetry_commutant`, `invariant_mixture_control` | Fiber convention, fluctuation elimination and invariant sector | Yes, explicitly quadratic comparison models and exact group algebra; not simulations of the nonlinear Gibbs state |
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:404` (`image_score_and_reflection`) | Local score/image normalization and conserved continuum reflection form | Yes, the supplied image kernel and exact finite momentum algebra |

No numerical witness is cited as executing the nonlinear thermodynamic
or continuum theorem. Written lemmas supply those obligations.

### N5 — Resolution and rhetoric

The primary cached stdout contains substantive per_element, per_site,
per_mode, per_block and lattice_wide certificates. Finite cochains,
quadratures, spectra and algebra are executed. Uniform Riesz estimates,
carrier expansions, state matching, ergodic averaging and continuum
reconstruction are checked and not executed; their analytic proofs are
the evidence at that resolution. No number of PASS lines supplies
independent review. The actual score's nonsummability conclusion, when
used in the companion physical theorem, follows from its nonconstant
low-frequency covariance symbol, not from a finite numerical tail fit.

### N6 — Remaining positive paths

The supplied Haar law is a concrete positive comparison route. Its finite-
clock counterpart retains quantized electric defects, which can be studied
through the exact coupled representation, its positive integer marginal,
or a direct physical-score argument. None is excluded by this theorem.
A new axiom is not requested or inferred. No primitive inadequacy claim
is made, so no primitive-registry exclusion is needed.

### N7 — Strongest objection

A hostile reviewer can correctly reject a full physical conclusion if the
carrier extension fails the uniform local bounds, if an averaged state is
misidentified, or if the source map loses a defect or noise term. The proof
therefore gives each of those steps explicitly and keeps the parent
sources in the reviewed dependency closure. The finite checks cannot settle
the remaining independent examination of the infinite-state argument.
Even a correct Haar theorem would leave finite-clock electric defects and
the native-law identification as distinct open targets. A broad TOE or
axiom-wall claim would be unsupported and is not made.

### N8 — Prior-route comparison

The parent carrier/filling argument supplied uniform convexity and exact
source control, while leaving a physical infrared limit open. This proposal
adds source-derivative control, an actual mixing-state construction,
replica concentration and spectral response. Earlier growing-coupling
constructions remove entire defect sectors by changing their parameters;
that is not used here. The image-noise distinction is retained and proved
for this Haar law. No previous failed route is promoted to an impossibility
claim, and no claim is made that this method includes finite clocks.

## Review record

All derivation and checks were performed personally without subagents.
This is an author check, not independent review, audit or main landing.
The parent f8e7219b5e79bcb271bb3c1df635ecdeeb57dbe8 and all three companion
notes form a provisional dependent chain. Hard review/landing condition:
review the needed parent content in the same frozen cumulative unit or
wait for it to land, and independently examine the complete final source.
Focused execution, mutation, cache and conformance receipts are recorded
in the branch-local handoff. Combined current-main pipeline, strict lint
and changed-evidence validation remain required at authorized integration.
