---
claim_id: mobile_records_finite_rate_control_and_spatial_response_bounded_theorem_note_2026-09-20
claim_type: bounded_theorem
claim_scope: "Conditional on the supplied finite mobile-record model: a reversible motion class with positive hazard has an explicit finite-epsilon next-birth total-variation bound, a Poisson first-order correction with quadratic remainder, and a hazard-clock representation. For six-axis W=1+j v_a dot v_b on a connected triangle-free graph, the rare third-birth all-identical dynamic/static ratio is exactly M/[M+2j^2 S], where M=6(n-2)[binom(n,2)+j|E|] and S=sum_x binom(deg(x),2); its deficit is O(n^-2) on bounded-degree sequences at fixed j. For W=1 the vacancy expectation obeys exact diffusion with decay 6 epsilon, with the stated Fourier and integrated-response kernels. For W=1+j v_a dot v_b, the orientation generator equals (1/2)Delta m+2j epsilon A m on configurations with at most one occupied site in the radius-two neighborhood, with an explicit multiple-occupancy remainder elsewhere. For centered eigenfunctions of any positive symmetric row-sum-six six-content matrix, the same local birth term is epsilon theta A m, with the normalized vector and axis-population eigenvalues derived explicitly. For the j-family with 0<=j<1 on regular tori, the multiple-occupancy remainder yields the stated controlled Duhamel error; this does not establish an interacting finite-density closure, bulk order, gravity, relativistic dynamics or physical rate selection."
upstream_dependencies:
  - mobile_records_rare_formation_event_law_and_six_site_witness_bounded_theorem_note_2026-09-20
runner: scripts/mobile_records_finite_rate_spatial_bridge_2026_09_20.py
---

# Finite-rate control and spatial response of mobile permanent records

**Date:** 2026-09-20
**Type:** bounded_theorem
**Status:** proposed_retained
**Author support:** conditional-support; no independent audit verdict.

## Result and campaign decision

The [preceding event-law note](MOBILE_RECORDS_RARE_FORMATION_EVENT_LAW_AND_SIX_SITE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-20.md) establishes a fixed-window, slow-formation limit. The present question is how to use that limit without confusing it with a large-volume or finite-density law.

Three results make that distinction quantitative. First, motion relaxation, entrance distribution and variation in the birth hazard give an explicit next-event error bound. Second, the first-three-record discrepancy found on six sites shrinks as the window grows at fixed record number. Third, the spatial generator distinguishes damped vacancy response in the uniform-weight control from a bias-amplifying term in the dilute interacting orientation sector. The latter is a concrete mechanism to test for structure formation; its nonlinear remainder is displayed, not discarded.

No physical rates or new axioms are adopted. All results concern the stipulated stochastic model. Whether its interacting finite-density dynamics gives useful fields or stable structures remains open.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Can the mobile-record formation law support controlled calculations of spatial response beyond a fixed rare-event window?"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Control or measure the interacting orientation remainder at finite density, including relaxation and vacancy depletion, before inferring a bulk ordering or field law."
conditional_surface_status: "Explicit reversible-class estimate, fixed-three-record graph identity, exact W=1 response, and a local dilute orientation identity with quantified remainder."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Finite generator identities and bounds, with a stated algebraic lattice-mode extension and no physical identification."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Model and dependencies

The preceding note is a checked but unmerged provisional dependency in the same working branch, originally PR #8545 at `22e6df1c55c99434410b37d936991c7227bf591c`. Its scientific assumptions and conditional status are inherited explicitly. Its proof and independent check do not confer retained status on this continuation.

A site is vacant or contains one immutable content. For occupied neighbors the positive symmetric weight is `W(a,b)`; empty bonds weigh one. Write `w(s)` for the product over occupied edges. An occupied-vacant edge swaps at rate `w(s')/[w(s)+w(s')]`, with unit symmetric proposals in the spatial examples. Content `a` is born at a vacant `x` at rate `epsilon u_(x,a)`, where `u` is the product of its weights with the occupied neighbors. There is no deletion, replacement or export.

The finite-rate estimate needs only a finite reversible irreducible motion generator `Q`, invariant law `pi`, and positive total birth hazard `B(s)=sum_t A(s,t)`, before multiplication by `epsilon`. The spatial and graph examples specialize to six contents `v_a in {+/-e_1,+/-e_2,+/-e_3}` and

`W(a,b)=1+j v_a dot v_b`, with `|j|<1`.

Each row sums to six. The earlier example is `j=1/2`, giving equal/opposite/orthogonal weights `(3/2,1/2,1)`. These menu and rate choices are supplied conditions, not derivations from the axiom memo. The lattice dimension `d` below labels spatial directions; the content menu is the specified six-axis menu throughout.

## 1. An explicit finite-rate error bound

Use the inner product of `L^2(pi)`. Let `L=-Q`, and assume a certified gap `lambda>0` on the mean-zero subspace. Put

\[
 \mu=E_\pi B,\quad b_-=\min B>0,\quad b_+=\max B,\quad
 f=\alpha/\pi,\quad r=f-B/\mu,\quad \sigma_B^2=\operatorname{Var}_\pi B.
\]

Here `alpha` is the distribution on entry into the class. Let `nu_epsilon` be the configuration law immediately before the next birth and `nu_0=pi B/mu`. Then

\[
 \|\nu_\epsilon-\nu_0\|_{\rm TV}
 \le \min\left\{1,
 \frac{\epsilon\sqrt{\mu b_+}}{2(\lambda+\epsilon b_-)}\|r\|_\pi\right\}. \tag{1}
\]

For stationary entrance this becomes

\[
 \|\nu_\epsilon-\nu_0\|_{\rm TV}
 \le\frac{\epsilon\sigma_B\sqrt{b_+/\mu}}
 {2(\lambda+\epsilon b_-)}. \tag{2}
\]

The cap at one may also be applied to (2). Constant hazard and stationary entrance give zero error. More generally, entrance `alpha=nu_0` gives zero error at every positive epsilon. A singleton motion class also has zero error and requires no gap convention.

**Proof.** Reversibility converts the exact killed-generator occupation row into the density

`g=epsilon (L+epsilon diag(B))^-1 f`.

Its normalization is `E_pi(Bg)=1`. Write `g=1/mu+h-c`, where `E_pi h=0` and `c=E_pi(Bh)/mu`. Define

\[
 Sh=Bh-B\frac{E_\pi(Bh)}{\mu}.
\]

This operator preserves the mean-zero subspace and is self-adjoint. Its quadratic form is

\[
 \langle h,Sh\rangle_\pi
 =\min_c E_\pi[B(h-c)^2],\qquad
 b_-\|h\|_\pi^2\le\langle h,Sh\rangle_\pi\le b_+\|h\|_\pi^2. \tag{3}
\]

The lower bound follows by replacing `B` by `b_-` before minimizing and using `E_pi h=0`; the upper bound follows by choosing `c=0`. Substitution in the full equation, without commuting `L` and `S`, gives exactly

\[
 (L+\epsilon S)h=\epsilon r,\qquad
 \|h\|_\pi\le\frac{\epsilon\|r\|_\pi}{\lambda+\epsilon b_-}. \tag{4}
\]

Finally `nu_epsilon-nu_0=pi B(h-c)`. Weighted Cauchy--Schwarz bounds its total variation by `sqrt(mu <h,Sh>)/2`; combine (3) and (4). For `f=1`, `||r||=sigma_B/mu`, proving (2). Setting `r=0` proves the exact entrance-law control. The same calculation gives the waiting-time estimate

\[
 \left|\epsilon E_\alpha T_\epsilon-\frac1\mu\right|
 \le\frac{\epsilon\sigma_B\|r\|_\pi}
 {\mu(\lambda+\epsilon b_-)}. \tag{5}
\]

Indeed the expression on the left is `|E_pi g-1/mu|=|c|`; subtract the mean of `B` when bounding `E_pi(Bh)`.

Conditional on pre-birth `s`, the insertion channel has law `A(s,t)/B(s)` at every epsilon. Consequently the total-variation distance of the **joint prestate and insertion mark** equals the prestate distance; any post-birth state or class marginal is bounded by (1).

**A second exact representation.** Define `R=diag(B)^-1 Q`, a motion generator measured in accumulated hazard time. It is reversible for `nu_0` and

\[
 \nu_\epsilon=\epsilon\alpha(\epsilon I-R)^{-1}. \tag{6}
\]

This follows by factoring `epsilon diag(B)-Q`; it is not a constant-hazard assertion in physical time. If `gamma` is the gap of `-R`, its eigenmodes in the resolvent are attenuated by at most `epsilon/(epsilon+gamma)`. Thus

\[
 \|\nu_\epsilon-\nu_0\|_{\rm TV}
 \le\frac{\epsilon}{2(\epsilon+\gamma)}
 \sqrt{\chi^2(\alpha\Vert\nu_0)},\qquad
 \gamma\ge\lambda/b_+. \tag{7}
\]

For the gap comparison, the Dirichlet form for `R,nu_0` is that for `Q,pi` divided by `mu`, while `Var_(nu_0) a <=(b_+/mu) Var_pi a` by minimizing over constants. Also `chi^2(alpha||nu_0)=mu E_pi(r^2/B)`. Both estimates are conditional on the actual motion class; neither substitutes a color-interchange gap for a vacancy-only process.

## 2. A controlled first-order correction

Let `phi` be the unique mean-zero solution of `L phi=r`, and put `c_phi=E_pi(B phi)/mu`. Define the signed approximation

\[
 \nu^{(1)}_\epsilon=\nu_0+\epsilon\pi B(\phi-c_\phi).
\]

It has total mass one, but is not guaranteed nonnegative at large epsilon. The same resolvent identity gives

\[
 \tfrac12\|\nu_\epsilon-\nu^{(1)}_\epsilon\|_1
 \le\frac{\epsilon^2 b_+\sqrt{\mu b_+}}
 {2\lambda(\lambda+\epsilon b_-)}\|r\|_\pi. \tag{8}
\]

To see this, apply `(L+epsilon S)^-1-L^-1=-epsilon(L+epsilon S)^-1 S L^-1` on the mean-zero subspace. Equations (3)--(4) bound `||h-epsilon phi||` by `epsilon^2 b_+ ||r||/[lambda(lambda+epsilon b_-)]`. The weighted centering and Cauchy--Schwarz step from (1) proves (8).

For the earlier six-site two-identical-record class, the runner computes `mu=898/37`, `sigma_B^2=233/1369`, and certifies `lambda>=2/5` by an exact 14-dimensional positive LDL decomposition on the mean-zero subspace. This is a lower bound, not an equality claim for the spectral gap. Direct 15-state absorption solves test (1), (5), (7) and (8) for stationary, point and rate-weighted entrances at five positive rates.

At stationary entrance and `epsilon=1/1000`, the actual pre-birth distance from `nu_0` is about `4.98130e-05`, below the certified bound `4.93757e-4`. The first-order approximation error is about `6.14123e-7`. For the probability `P_epsilon` that the first three records agree, the Poisson calculation gives

\[
 P_\epsilon=\frac{2701}{53880}
 -\frac{16823}{29030544}\epsilon+O(\epsilon^2). \tag{9}
\]

The initial law after the second birth is exactly stationary within the identical-pair class for this model, as proved in the preceding note. Equation (8) bounds the remainder for the next-birth success observable; multiplying its bound by the probability `37/180` of entering this class bounds the remainder in (9).

These estimates apply to the next event. At growing volume, the gap, hazard fluctuations and entrance density may change. A positive-density history contains a growing number of events and also needs control of accumulated error and of each entrance law. A fixed finite-class estimate alone supplies neither.

## 3. The six-site difference has a dilute large-window limit

Let `G` be connected and triangle-free, with `n>=3` vertices, `e` edges, and

\[
 P=\binom n2,\quad S=\sum_x\binom{\deg(x)}2,\quad
 Z_{aa}=P+je,\quad M=6(n-2)Z_{aa}.
\]

Start empty with the six-axis weights above, and let `E_3` mean all three contents agree immediately after the third birth. Write `mu_3` for the full static product-weight law conditioned on exactly three occupied sites. Then

\[
 \frac{\lim_{\epsilon\downarrow0}\Pr(E_3)}{\mu_3(E_3)}
 =\frac{M}{M+2j^2 S}. \tag{10}
\]

**Proof and accessibility.** A single record has uniform stationary position. Every empty-site content normalizer is six, so the total second-birth hazard is the constant `6(n-1)`. The entrance law is uniform from the first birth. Insertion flux has exactly two predecessors for every two-record state, hence its post-second-birth law is its static law for every epsilon. The probability that the pair agrees is `Z_aa/(6P)`.

Two indistinguishable records can reach every two-site placement on any connected graph with a vacancy. One elementary proof restricts moves to a spanning tree and fixes the occupancy of a leaf to its target: slide a vacancy toward an occupied leaf that must be empty, or slide the nearest record toward an empty leaf that must be occupied. Freeze that leaf and continue on the smaller tree. A full remaining subtree has only one indistinguishable occupancy state. This establishes the identical-pair accessibility needed here. It makes no claim about two **different** contents, which can have distinct motion classes on a path.

For identical contents at two sites, an empty site with zero or one occupied neighbor has total insertion weight six; with both records as neighbors it has weight `6+2j^2`. Hence `B(s)=6(n-2)+2j^2 c(s)`, where `c` is the number of common neighbors. Triangle-freeness makes every common-neighbor pair nonadjacent, so its existing pair weight is one. Consequently

`sum_s w(s) B(s)=6(n-2) Z_aa+2j^2 S`.

Let `Z_aaa` be the weight summed over placements of three specified equal contents. Insertion/deletion counting gives success numerator `3 Z_aaa`. Every occupied triple induces a forest, and leaf summation using the row sum six gives total static partition function `216 binom(n,3)`. Therefore

\[
 \lim\Pr(E_3)=\frac{Z_{aa}}{6P}\frac{3Z_{aaa}}{M+2j^2S},\qquad
 \mu_3(E_3)=\frac{Z_{aaa}}{36\binom n3}.
\]

Their ratio is (10), since `3 binom(n,3)=P(n-2)`. On the six-site ladder at `j=1/2`, it is `444/449`.

For any bounded-degree sequence at fixed `j`, `S=O(n)`, `e=O(n)`, `Z_aa=Theta(n^2)` and `M=Theta(n^3)`. Thus the relative deficit in (10) is `O(n^-2)`. For cycles and `j=1/2`, it is exactly `1/[6n(n-2)+1]`, so `n^2` times the deficit tends to `1/6`. The runner checks direct insertion sums on eleven graphs at three weights, including paths, cycles, ladders and a star; it independently sums all triple contents on the cases with at most six vertices.

This is a fixed-three-record limit, where density tends to zero. It does not determine the distribution after `O(n)` births. More generally the earlier covariance identity gives local event/time bias `Cov_pi(F,B)/mu`. If `mu>=b n` and `sum_x |Cov_pi(F,b_x)|<=C_F` for local hazard terms `B=sum_x b_x`, then that bias is at most `C_F/(bn)`. These are stated concentration hypotheses; they have not been proved for the interacting candidate near a putative ordering transition.

## 4. Exact vacancy response in the uniform-weight control

Set `j=0`, so `W=1`. Put `eta_x=1` when occupied and `v_x=1-eta_x`. Applying the complete occupancy generator, before any expectation or factorization, gives

\[
 \mathcal L v_x=\tfrac12\sum_{y\sim x}(v_y-v_x)-6\epsilon v_x.
\]

An occupied-vacant edge contributes its vacancy difference at rate one-half; an occupied-occupied or empty-empty edge has zero difference. The six birth channels remove a vacancy at total rate `6 epsilon`. Therefore the exact expectation `u_x(t)=E v_x(t)` obeys

\[
 \dot u=\tfrac12\Delta_G u-\kappa u,\qquad \kappa=6\epsilon. \tag{11}
\]

No independence assumption on the initial state is needed. A difference between two initial expectation profiles obeys the same equation. On a periodic `d`-dimensional nearest-neighbor lattice of side at least three,

\[
 \delta\widehat u(k,t)=e^{-[\kappa+\sum_i(1-\cos k_i)]t}
 \delta\widehat u(k,0),\qquad
 \widehat G(k)=\frac1{\kappa+\sum_i(1-\cos k_i)}. \tag{12}
\]

Here `G` is the **time-integrated response to an initial vacancy perturbation**, obtained by integrating the decaying semigroup. It does not introduce a source of new vacancies or a steady physical field into the model. On the infinite chain the bounded nearest-neighbor operator has the exact kernel

\[
 G(x)=\frac{e^{-m|x|}}{\sinh m},\qquad \cosh m=1+\kappa,\qquad
 \sum_xG(x)=1/\kappa. \tag{13}
\]

The recurrence away from the origin, its unit impulse at the origin, and the convergent geometric sum prove (13); the positive decay rate gives uniqueness of the bounded inverse. Thus its decay length is `1/arcosh(1+kappa)`, asymptotic to `1/sqrt(2 kappa)` as kappa tends to zero. This operator statement requires no interacting infinite-volume theorem.

For a fixed Fourier index on a torus of side `ell`, observe at time `t=ell^2 tau`. If `kappa_ell ell^2 -> a`, its multiplier tends to `exp[-(a+2 pi^2 |index|^2) tau]`. If that product diverges, the perturbation decays before the diffusive window. This exhibits the formation/diffusion scaling that a long-distance interpretation must specify. It is a statement about the uniform-weight vacancy observable, not the interacting orientation field.

## 5. An interacting orientation mechanism, with its omitted terms exposed

Let `m_i(x,s)` be content component `i` at `x`, or zero when vacant. Return to `W=1+j v_a dot v_b`. If at most one site in the graph-distance-two neighborhood `B_2(x)` is occupied, direct generator application gives exactly

\[
 \mathcal Lm_i(x)=\tfrac12\Delta_G m_i(x)+2j\epsilon\sum_{y\sim x}m_i(y). \tag{14}
\]

To prove it, any record participating in a hop at `x` is isolated before and after that hop, so the hop rate is one-half. For birth at an empty `x`, zero occupied neighbors give zero vector sum. With one neighbor of content `b`,

`sum_a v_a [1+j v_a dot v_b]=2j v_b`,

using `sum_a v_a=0` and `sum_a v_a v_a^T=2I`. No mean-field factorization appears in this local identity.

For a finite graph of maximum degree `z`, define the residual `R_i(x,s)` by subtracting the right side of (14) from the exact generator at every state. Let

\[
 C_z=2z+2\epsilon(1+|j|)^z+2|j|\epsilon z.
\]

The following conservative bound is uniform over configurations:

\[
 |R_i(x,s)|\le C_z\,1_{\{N_{B_2(x)}(s)\ge2\}}. \tag{15}
\]

The exact hop contribution and the candidate linear hop contribution each have absolute value at most `z`: each hop involving `x` has rate at most one and changes its component by at most one, and the discrete difference bound gives the same limit for the linear term. Only the two contents on axis `i` contribute to the absolute birth-component sum, bounded by `2 epsilon(1+|j|)^z`. The linear birth term is bounded by `2|j| epsilon z`. The residual vanishes outside the indicated event by (14), proving (15).

On a regular `d`-dimensional torus, its dilute linear operator has multiplier

\[
 \omega(k)=-\sum_l(1-\cos k_l)+4j\epsilon\sum_l\cos k_l
 =4dj\epsilon-(1+4j\epsilon)\sum_l(1-\cos k_l). \tag{16}
\]

For the current `j=1/2`, `d=3` choice, the uniform tangent mode grows at rate `6 epsilon`. This is growth of a pre-existing orientation perturbation in the **dilute linear operator**. An exactly isotropic ensemble has zero mean orientation by symmetry; the formula by itself does not prove spontaneous ordering, a domain pattern, or macroscopic seed amplification throughout formation.

There is an explicit control on the approximation. For `0<=j<1`, write `K=(1/2+2j epsilon)Delta_G+2j epsilon z I`, with `z=2d`, and let `p_2(t)=sup_x Pr[N_(B_2(x))(t)>=2]`. Taking expectations in the exact generator and using Duhamel's formula gives

\[
 \|E m_i(t)-e^{Kt}E m_i(0)\|_\infty
 \le C_z\int_0^t e^{2j\epsilon z(t-s)}p_2(s)\,ds. \tag{17}
\]

The heat semigroup is a contraction in the maximum norm; the scalar growth factor supplies the exponential in (17). Thus the physical use of the dilute growth rate requires the right side to be small for the observable and interval at issue. No smallness bound on `p_2` at positive density is supplied here.

The runner checks (14)--(15) for all `7^4` states, all sites and all three components on the four-cycle. It also preserves a nonzero residual: at `j=1/2`, `epsilon=1/7`, state `(-1,-1,0,0)`, site zero and component zero, the remainder is `-1/10`. A nearby second record changes the hop acceptance. This prevents upgrading (14) into an exact interacting finite-density closure.

**Extension to the neutral six-axis menu.** The local argument also applies to any positive symmetric `W` with row sum six. For any centered content function `chi` satisfying `sum_a chi(a)=0` and `W chi=theta chi`, define `m_chi(x)=chi(s_x)` on occupied sites and zero on vacancies. On the same at-most-one-record radius-two domain,

`L m_chi=(1/2) Delta_G m_chi+epsilon theta A_G m_chi`.

Here the empty-neighbor sum is zero and the single-neighbor birth sum is exactly `theta chi(b)`; the isolated hop argument is unchanged. For positive raw equal/opposite/orthogonal weights `(p,q,r)` normalized by `c_0=6/(p+q+4r)`, the three vector modes and two centered axis-population modes have respectively

\[
 \theta_v=\frac{6(p-q)}{p+q+4r},\qquad
 \theta_a=\frac{6(p+q-2r)}{p+q+4r}. \tag{18}
\]

Direct multiplication verifies this: opposite-sign pairs span the vector modes; functions constant on each opposite pair with zero sum span the other two modes. Their spatial multipliers are `2d epsilon theta-(1/2+epsilon theta) 2 sum_l(1-cos k_l)`. At `(3,1,2)` the two eigenvalues are `(1,0)`; at `(6,1,2)` they are `(2,6/5)`; at `(12,1,2)` they are `(22/7,18/7)`. The runner verifies the five modes at these and two sign-changing parameter examples. These are local formation-feedback eigenvalues, not ordering thresholds or physical particle/field identifications. The quantitative remainder (15)--(17) was stated for the earlier `j` family; an extension of that bound to a general `chi` must also retain its amplitude and the maximum pair weight.

## Scientific disposition and remaining decisions

The finite-rate estimate, graph ratio and local-generator identities are proved within their stated domains. Their parameters carry the unresolved limits explicitly: the actual motion gap and entrance law for growing records; the difference between fixed record number and fixed density; and the multiple-occupancy probability in the orientation remainder.

The promising ingredient is a calculable mechanism for orientational feedback during formation, alongside transport. The uniform-weight vacancy response is a useful exact reference. Neither its decaying response kernel nor the dilute orientation growth rate has been identified with a gravitational potential, quantum amplitude or relativistic propagator. The next scientific discriminator is whether the interacting process develops persistent spatial correlations before vacancies become scarce, with its nonlinear terms and scales under control.

## Attribution, novelty boundary and reproduction

Finite reversible-chain projection, Poincare estimates, Poisson correctors and time changes are standard machinery. The independent checker separately derived (1) and the hazard-clock route before reading this primary source. The application here is to the specified moving-and-forming candidate, with exact graph and local-generator discriminators; novelty is not claimed for those mathematical tools.

The exclusion-process first-moment closure is also standard. Background primary literature: van Ginkel and Redig, *Hydrodynamic Limit of the Symmetric Exclusion Process on a Compact Riemannian Manifold*, Journal of Statistical Physics 178 (2020), 75--116, DOI `10.1007/s10955-019-02420-2`, introduction and section 4. The simple generator and lattice identities needed here are derived explicitly; no manifold or hydrodynamic theorem is imported. Caputo--Liggett--Richthammer's interchange-gap theorem was considered but is not applied: exchanging occupied colors differs from the specified vacancy-only moves.

A statement search of the current main and prior campaign sources found no matching finite-rate event-law or mobile-record spatial-response result. The exact source revisions, failed shortcuts and selective independent checks are recorded in the existing campaign checkpoint. All numerical claims required by this note are computed by the primary runner; independent evidence is supplementary scientific scrutiny, not an audit verdict.

During this continuation, PR `#8546` appeared at `361166e7eaccd7d80cd1e3d4cb94b4ad7fcdbc21`, proposing the neutral scale for general `(p,q,r)` and deriving content-summed static occupancy identities. Its complete note and motion-simulation source were inspected. The simulation conserves records and their contents at fixed density and includes no formation events. Its static identities and executed alignment observations are distinct from the growing-process statements here. Equation (18) restates and derives the needed normalized matrix modes locally; no claim from that open PR is an uncarried theorem dependency, and no choice of scale is adopted as an axiom.

`python3 scripts/mobile_records_finite_rate_spatial_bridge_2026_09_20.py`

`python3 scripts/mobile_records_finite_rate_spatial_bridge_2026_09_20.py --list-mutations`

The final-input canonical cache is `logs/runner-cache/mobile_records_finite_rate_spatial_bridge_2026_09_20.txt`.
