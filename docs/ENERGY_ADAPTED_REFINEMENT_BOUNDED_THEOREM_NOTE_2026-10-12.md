---
claim_id: energy_adapted_refinement_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_type_reason: "Conditional analytic theorem in the supplied free-chain model; finite diagnostics are supporting evidence."
claim_scope: "For the supplied massive free one-dimensional chain, dispersion-coordinate even refinements preserve the actual chosen state and energy flow exactly while realizing the same intrinsic Cauchy sections, geometric local quotient and actual fixed mixed-flow limits as Haar refinement."
upstream_dependencies:
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
  - continuum_local_boost_bounded_theorem_note_2026-10-12
  - microscopic_local_boost_limit_bounded_theorem_note_2026-10-12
  - mixed_local_poincare_correlations_bounded_theorem_note_2026-10-12
  - dyadic_even_refinement_bounded_theorem_note_2026-10-12
runner: scripts/energy_adapted_refinement_2026_10_12.py
artifact_role: theorem
target_claim_id: null
target_blocker_text: "Compatibility of exact actual-state and energy refinement with intrinsic geometric sections and actual mixed-flow limits."
source_of_blocker_text: user_goal
next_trace_action: "Use the proved section-level equivalence while retaining finite-scale support, spatial, current and boost witnesses; no broader physical realization is claimed."
hypothetical_axiom_status: null
admitted_observation_status: null
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: "Exact real-CAR state and actual-energy refinement with the same geometric continuum sections; finite support, translation, current and boost compatibility fail for specified witnesses"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

**Publication chronology and recorder limit:** The scientific source below is frozen at SHA-256 `65d49c82eb14b88e4880983eb8b41ecb5141cb0ff00f4e5e4760bbb12a151b9d`. The final separate source review and root source-bound gate are accepted and archived at the stated bounded scope. Its pending-review language is historical. Section 9 is the post-execution E23 inverse-support sign and small-a clarification, preserved in full. Original recorders start separate nested sessions; the outer timeout cannot guarantee termination of the inner session. All three original jobs actually completed without a timeout. Original stronger timeout wording is retained as a historical statement and qualified here.


# Energy-adapted refinement of the supplied massive chain

**Author proposal, 2026-10-12.** A change from lattice momentum to the
exact dispersion coordinate gives real isometric refinements preserving
the actual chosen state and time evolution exactly. Their inductive limit
is the same continuum even CAR algebra. Their intrinsic Cauchy sections,
geometric local section quotient and actual fixed mixed-flow limits agree
with the original Haar construction. Exact finite-scale spatial, current
and boost compatibility does not follow; the specified maps fail those
equations. Local spin inputs acquire infinite tails.

The complete argument below is conditional on the explicitly supplied
one-dimensional free massive chain and pinned actual-spin implementation
theorems. It is not a framework-selected dynamics/state, physical axiom,
empirical prediction, generic renormalization novelty or retained audit result.

## 1. Sources, conventions and exact question

Write S for this note's directory and E=S/energy_adapted_refinement.
E/source_inventory.json pins and copies all sources. The mathematical
parents are LOCAL_EVEN_CONTINUUM (7be1a72e...), CONTINUUM_LOCAL_BOOST_REVISED
(59d34a51...), MICROSCOPIC_LOCAL_BOOST_LIMIT (70118e0b...),
MIXED_LOCAL_POINCARE_CORRELATIONS (8c3a308b...), CONCRETE_GAPPED_CHAIN
(0aebc2de...), and DYADIC_EVEN_REFINEMENT (646ad05e...). Full SHA-256 values
and paths are in the inventory. The exact STATE_ADAPTED_REFINEMENT source
is 459868fcd7f80fa3063c9e7f7a6d62df393eb80f2edc72b221ecda533ba2a971;
its fresh review is pending at dispatch. Its conjugacy argument is a
template rederived here, not an assumed accepted theorem. The frame and
actual-flow conventions are independently bound to the earlier parents.
The pending local-UCP-section proposal is not used.

Root coauthored ENERGY_ADAPTED_REFINEMENT_ROUTE_BRIEF.md and suggested
this route. It is an unverified proposal, not evidence for the result.
Applicable physics-loop, lane-builder, no-go and workflow instructions
are reused at the same verified campaign revision. Necessary current and
boost-domain passages were refreshed. Existing full reads at unchanged
hashes are reused; Concrete is not given a new complete review here.

Operator-algebraic renormalization and momentum/wavelet CAR inductive
systems are established prior art: Osborne--Stottmeister,
[Conformal Field Theory from Lattice Fermions](https://doi.org/10.1007/s00220-022-04521-8),
CMP 398 (2023). The official source was read in this campaign. No broad
novelty claim is made. The question is whether this exact supplied massive
dispersion transport meets the realness, state, geometry and actual-flow
requirements with all endpoints and normalizations checked.

Fix m,v,a_0>0 and a_n=a_0 2^{-n}. K_a=ell^2(Z;C^2), K=L^2(R;C^2),
with position-real subspaces and conjugate-linear first inner product.
The unitary Fourier transforms are

    (L_a z)(q)=sqrt(a/(2pi)) sum_j z_j exp(-iaqj),
    q in B_a=(-pi/a,pi/a),
    (L f)(p)=(2pi)^(-1/2) integral exp(-ipx) f(x) dx.    (E1)

The parent's actual coefficient frame, polarization and dispersion are

    sigma_a=sqrt(m^2/4+v^2/a^2),
    g_a=sigma_a/2+m/4, J_a=sigma_a/2-m/4,
    D_a(q)=-2J_a sin(aq) sigma_x-2(g_a-J_a cos(aq)) sigma_y,
    E_a(q)=sqrt(m^2+4v^2 sin^2(aq/2)/a^2),
    theta_a(q)=arg(g_a-J_a exp(-iaq)),
    F_a(q)=exp(-i theta_a(q) sigma_z/2), C_0=-sigma_y,
    F_a D_a F_a*=E_a C_0,
    P_a=F_a* P_0 F_a, P_0=(1+C_0)/2.                   (E2)

Here F_a is beta_a's action on coefficients, not its field-column action.
The actual selected state is omega_a=omega_0 beta_a and has covariance
2<z,P_a w>. The continuum convention is

    D(p)=-vp sigma_x-m sigma_y, E(p)=sqrt(m^2+v^2p^2),
    F(p)=exp(-i arctan(vp/m) sigma_z/2),
    F D F*=E C_0, P=F*P_0F.                            (E3)

These Fourier multipliers respect conjugation plus momentum reflection.
The continuum quasifree state omega has covariance 2<f,Pg>. All spin
claims concern the even algebra A_a under its compatible even JW
isomorphism. Odd fields are coefficient tools, not bilateral spin elements.

## 2. Exact change of measure, including the endpoints

Define the increasing smooth bijection of open intervals

    p_a(q)=2 sin(aq/2)/a, I_a=(-2/a,2/a),
    q_a(p)=2 arcsin(ap/2)/a,
    w_a(p)=sqrt(1-a^2p^2/4), q_a'(p)=1/w_a(p).          (E4)

Let U_a:L^2(B_a,dq;C^2)->L^2(I_a,dp;C^2) be

    (U_a phi)(p)=w_a(p)^(-1/2) phi(q_a(p)).             (E5)

For compactly supported continuous phi, the ordinary change of variables
gives ||U_a phi||^2=int_Ia q_a'(p)|phi(q_a(p))|^2 dp
=int_Ba |phi(q)|^2 dq. The inverse is
(U_a^-1 psi)(q)=sqrt(p_a'(q)) psi(p_a(q)), where
p_a'(q)=cos(aq/2)>0. Applying the same identity on compact continuous
psi proves that the isometric dense-domain map extends onto all L^2,
with this inverse. Endpoints are null sets; no finite endpoint value is
required to define U_a. Its multiplier diverges like distance^(-1/4),
but that fact does not contradict the exact L^2 change-of-measure identity.
No derivative-domain assertion follows from this L^2 extension alone.

Let i_a extend a function on I_a by zero. Define

    J_a=L^-1 M_(F*) i_a U_a M_(F_a) L_a : K_a -> K.    (E6)

Every factor is unitary or isometric, so J_a is an isometry. Reflection
q_a(-p)=-q_a(p), evenness of w_a and the reality relations for F_a,F show
that J_a maps real coefficient vectors to real functions. Its range is
exactly the continuum band subspace

    R_a=L^-1 L^2(I_a;C^2), Q_a^band=L^-1 1_(I_a) L,    (E7)

because the invertible pointwise matrix F* preserves that subspace.
For b<a these ranges are nested, and their union along a_n->0 is dense.

Set G_(b,a)=J_b*J_a for b<a and G_(a,a)=1. Then
G*G=1, J_b G_(b,a)=J_a, and G_(c,b)G_(b,a)=G_(c,a).
All these are exact real isometries. For |p|<2/a their explicit Fourier
formula is

    (L_b G_(b,a)z)(q_b(p))
      =sqrt(w_b(p)/w_a(p)) F_b(q_b(p))* F_a(q_a(p))
                            (L_a z)(q_a(p)),           (E8)

and it is zero on the remaining part of B_b. The square-root ratio
and the two different q coordinates are essential. Equation E8 also
checks composition directly, since the middle frames and weight ratios
cancel. No alias multiplicity factor occurs: p_a is one-to-one on B_a.

## 3. Exact actual-state and actual-time compatibility

Conjugation by U_a turns E_a(q) into E(p), exactly. Therefore

    D J_a=J_a D_a,
    J_a* P J_a=P_a,
    exp(+itD) J_a=J_a exp(+itD_a).                      (E9)

For the first equality there is no hidden unbounded domain: D is bounded
on R_a, with bound sqrt(m^2+4v^2/a^2), so J_a maps every K_a vector into
Dom D. The polarization equality follows instead from F P F*=P_0,
which commutes with the scalar change of variables and interval inclusion.

Use the actual even JW maps to define

    rho^E_(b,a)=jw_b CAR(G_(b,a)) jw_a^-1,
    Psi_a=CAR(J_a) jw_a^-1.                            (E10)

The real isometries induce injective unital isometric *-maps by finite
Clifford algebra and norm completion. Their images are nested and dense
in A=CAR(K_R)^even, since their one-body ranges exhaust K_R. Thus Psi_a
identifies the full even-CAR C*-inductive limit. Quasifree moments and
norm density, and respectively the pinned actual coefficient action of
time evolution, give

    omega Psi_a=omega_a,
    omega_b rho^E_(b,a)=omega_a,
    alpha_b^time(t) rho^E_(b,a)=rho^E_(b,a) alpha_a^time(t). (E11)

The time flow is the actual supplied spin energy flow, with coefficient
group exp(+itD_a). No replacement Hamiltonian or continuum current is
inserted. Group equality is proved first on finite field products and
then by norm completion; no claim that its generator is defined on every
C*-algebra element is needed.

## 4. The position-cell comparison, with its alias normalization

Retain the original physical cell maps

    (C_a f)_j=a^(-1/2) integral_[aj,a(j+1)] f,
    (j_a z)(x)=a^(-1/2)z_j on that cell,
    C_a j_a=1, Q_a^cell=j_a C_a ->1 strongly.           (E12)

For Schwartz f, inserting its inverse Fourier transform into the cell
integral and summing the lattice Fourier series gives

    (L_a C_a f)(q)=sum_(l in Z)
       exp(ia(q+2pi l/a)/2) sinc(a(q+2pi l/a)/2)
                     fhat(q+2pi l/a),                 (E13)

where sinc(u)=sin(u)/u with value 1 at zero. In particular the phase is
positive and no sqrt(a), sqrt(2pi), or extra alias factor remains.
One can first take smooth compact Fourier support, when only finitely
many aliases occur, and then justify the Schwartz identity by decay.
The cell integral itself is
sqrt(a) exp(iaq(j+1/2)) sinc(aq/2) on the plane wave exp(iqx).
This supplies a direct normalization check independent of the Poisson sum.

If fhat is smooth, supported in [-M,M] and aM<pi, only l=0 contributes
on B_a. Thus

    (L J_a C_a f)(p)=1_(I_a)(p) F(p)* w_a(p)^(-1/2)
      F_a(q_a(p)) exp(ia q_a(p)/2) sinc(a q_a(p)/2)
                                      fhat(q_a(p)).    (E14)

The expression is supported in [-p_a(M),p_a(M)] subset [-M,M]. On this
fixed compact interval q_a(p)->p, w_a->1 and F_a(q_a(p))->F(p) uniformly.
For the last assertion, g_a-J_a exp(-iaq_a(p)) has real part tending
m/2 and imaginary part tending vp/2 uniformly; its argument therefore
tends arctan(vp/m). The real part stays uniformly positive on this set.
Extending fhat by zero makes the remaining composition converge uniformly.
Uniform bounds on the fixed support and dominated convergence prove

    J_a C_a f ->f in L^2.                              (E15)

Smooth compact Fourier support is dense in L^2, and ||J_a C_a||<=1,
so E15 holds for every L^2 input, including real Haar indicators.
No H^1/H^2 regularity or rate is asserted for such indicators.

## 5. The same Cauchy sections and geometric local quotient

For each a_n, the real complements of j_n K_n,R and R_n,R are both
infinite-dimensional separable real Hilbert spaces. Choose any real
unitary V_n between them, for example by orthonormal bases. Then

    L_n=J_n C_n+V_n(1-Q_n^cell)                       (E16)

is a real unitary on K_R: its two isometric summands have orthogonal
initial and final spaces exhausting K_R. Equations E12 and E15 imply
L_n f->f for every f, regardless of the chosen complement unitary.
Its adjoints converge strongly too, since the limit is unitary.
Consequently gamma_n=CAR(L_n)|even tends point-norm to the identity,
as does its inverse, by field norm continuity and polynomial density.

The original Haar injection Phi_n=CAR(j_n) jw_n^-1 obeys
Psi_n=gamma_n Phi_n. Therefore a bounded same sequence x=(x_n) has
Phi_n x_n convergent iff Psi_n x_n converges, and the two limits agree.
For either exact inductive system, convergence of its images is equivalent
to its intrinsic norm Cauchy criterion. Hence

    Gamma_E=Gamma_Haar as subsets of product_b A_n,
    ev_infinity^E(x)=ev_infinity^Haar(x),
    Gamma_E/c0 = A isometrically.                      (E17)

This assertion concerns the same sequence, not equality of two different
sequences obtained by recursively refining a fixed finite-scale element.
Those have limits Psi_N x and Phi_N x and may differ.

For a bounded open interval I let Lambda_n(I) consist of cells wholly
inside I. Restrict Gamma_E to sequences x_n in A_n(Lambda_n(I)). The
quotient by its c0 ideal is exactly CAR(L^2(I;R^2))^even. To prove the
two directions, use E17: every Haar image of such a sequence lies in
that closed local algebra, while the nested inner-cell Haar algebras
exhaust it and furnish local approximating sections. This does not make
rho^E a map between those finite local algebras. For any fixed convergent
local sequence, dist(Psi_n x_n,A(I))<=||Psi_n x_n-Phi_n x_n||->0.
No uniform bound over all microscopic local unit balls follows.

The actual mixed word theorem also transfers. For any fixed finite word
of actual time, floor-rounded physical translations and scaled boosts,
with parameters continuous on a compact set P, the pinned parents give
j_n W_n(w,p) C_n ->W(w,p) strongly, uniformly on P at each vector.
The real unitary extension in the new embedding is

    J_n W_n J_n*+1-Q_n^band
      =L_n [j_n W_n C_n+1-Q_n^cell] L_n*.               (E18)

This tends strongly to W, uniformly on P, by E16 and a finite epsilon-net
on the compact continuum orbit W(P)f. Field continuity and norm density
give, for every x in Gamma_E with limit x_infinity,

    sup_p ||Psi_n alpha_n(w,p)x_n-alpha(w,p)x_infinity||->0. (E19)

Finite ordered joint moments converge uniformly too: E11 identifies every
finite-scale state with the same omega on its embedded image, and finite
product telescoping bounds the error. The limiting geometric spacetime
net is the pinned continuum net. No generator/graph convergence, growing
word length, growing rapidity or massless limit is inferred.

## 6. Exact finite-scale nonlocality and spatial/current failures

For b<a, the image in E8 vanishes on the nonempty open fine-momentum
arcs where |p_b(q)|>2/a. A nonzero finitely supported lattice vector has
a trigonometric-polynomial Fourier transform, which cannot vanish on an
open arc. Since G is an isometry, every nonzero image has infinite
coefficient support. In particular u=G e_(0,1) and v=G e_(0,2) occupy
separate nonzero component coordinates. The grade-two coefficients of
rho^E(Z_0)=-i c(u)c(v) include u_(j,1)v_(l,2); some index lies outside
every finite interval. Finite Clifford trace coefficients therefore
exclude membership in any finite local even spin algebra.

The maps still land in the quasilocal even spin algebra: truncating l^2
coefficient vectors converges in norm on every even field product.
For a delta input, E8 behaves like distance^(-1/4) at its interior fine
spectral cutoff, because w_a vanishes there and w_b does not. This is
integrable in squared modulus but unbounded, and rules out exponential
decay of that coefficient sequence (such decay would give a bounded
analytic Fourier series). No uniform physical-tail estimate is asserted.
Similarly a nonzero J_a z cannot have compact spatial support: its
compactly supported Fourier transform is L^1 and defines an entire
function of position; vanishing on an exterior open interval would force
it to vanish identically. E15-E19 are statements about limits of fixed
observables, not finite-scale support.

An actual physical displacement ell that is an integer multiple of both
a and b acts in the common p coordinate by exp(-i ell q_a(p)) and
exp(-i ell q_b(p)). For 0<p<2/a, q_a(p)>q_b(p), and their difference is
nonconstant. For any nonzero common ell the two phase functions cannot
agree identically on an interval. A number observable associated with
a wavepacket on an interval where their ratio is nonconstant has different
rank-one projections under the two actions. Thus even the common-integer
physical translations fail exact intertwining. The zero displacement
and continuum limit survive; rounded noninteger displacements have their
usual additional rounding defects.

The actual chain current, from Concrete C28, is the one-particle scalar
4J_a g_a sin(aq). Since 4J_a g_a=v^2/a^2, its physical normalization
K_cur,a=(a/v^2) P_actual,a is exactly

    kappa_a(p)=sin(aq_a(p))/a=p w_a(p).                 (E20)

This is the pushforward of the actual current, not its replacement by p.
For b<a, kappa_b-kappa_a=p(w_b-w_a) is nonzero on 0<p<2/a. A packet
where that difference is nonconstant gives an even number-flow witness
by the same rank-one phase argument. The continuum multiplier p is
recovered on compact p sets as a->0; no exact finite-scale identification
with geometric momentum or its translation group is asserted.

## 7. The actual boost: transported domain and a concrete failed equation

In the pinned parallel band frame, the positive-band actual scaled boost
has periodic domain H^1_per(B_a) and generator
b_a^q=i(E_a partial_q+E_a'/2)-aE_a/2; the other band has its negative.
The spin action is lambda^b_(-as). Applying the half-density U_a gives

    b_a^p=i(E w_a partial_p+(E w_a)'/2)-aE/2,
    Dom b_a^p=U_a H^1_per(B_a).                        (E21)

To check the first formula explicitly, write phi(q)=sqrt(w_a(p))psi(p).
Then partial_q phi=sqrt(w_a)[w_a psi'+w_a'psi/2], while
E_a'(q)=w_a E'(p). Dividing by sqrt(w_a) gives E21, including its
half-density and bond-origin terms. The domain in E21 is the unitary
transport of the already closed operator, not a newly assumed maximal
domain on the open interval. Equivalently,
sqrt(w_a(p_a(q)))psi(p_a(q)) must lie in periodic H^1 in q. Its two
q-endpoint traces are equal. The p-representative itself can diverge as
distance^(-1/4); setting it to zero at both endpoints would change the
operator. The characteristic travel time to an endpoint is finite because
int dp/(E w_a)=int dq/E_a is finite. The circle gluing must be retained.

In the common reference p coordinates the coarse embedding is extension
by zero from I_a to I_b. It does not preserve these boost domains. For
example a constant coarse reference q wavefunction is in H^1_per(B_a),
but its extension after U_a is singular at the interior points +-2/a
of I_b. Pulling back by U_b^-1 leaves that interior singularity, which
is not H^1. Thus no exact coefficient boost-group intertwining can hold.

There is also an even-observable witness independent of this domain test.
In the fine positive band, the actual boost transports support along
the circle characteristics dq/ds=E_b(q)>0; its Jacobian amplitude and
origin phase are nonzero. The coarse cutoff q_b(2/a) is an interior point
of B_b with nonzero velocity. Choose a nonzero smooth wavepacket just
below that cutoff. For a sufficiently small parameter of the sign that
moves its support upward, the fine boost moves part of its support into
|p_b(q)|>2/a. Its rank-one number projection consequently has support
outside the coarse band. Every coarse-then-embedded boost output remains
inside that band. The corresponding actual even quasilocal number
observable therefore witnesses failure of boost intertwining. A packet
compactly contained initially in the band gives no initial endpoint-domain
ambiguity. The same support argument works with the reality-related
negative band when expressed in real Majorana fields.

On compactly supported interior scalar test functions the difference is
also explicit:

    b_b^p i_(b,a)psi-i_(b,a)b_a^p psi
       =i E(w_b-w_a)psi'+i[E(w_b-w_a)]'psi/2
                                      +(a-b)E psi/2.  (E22)

This is not zero as an operator. Pointwise convergence of its coefficients
as a,b->0 alone would not prove flow convergence across the endpoint
domains. E19 supplies the actual limiting-flow theorem through the pinned
position-cell comparison instead. Exact state/time compatibility and
limiting mixed covariance therefore coexist with these finite-scale failures.

## 8. Honest scope, remaining work and frozen controls

The original Haar state and energy counterexamples, and the state-adapted
map's energy and support counterexamples, remain unchanged. This is a
different map. No negative result is generalized to every possible
refinement. The strongest positive claim is the complete conditional
construction E4-E19; E20-E22 delimit its actual finite-scale symmetry.

The No-Go Discipline scope answers are: N1, the three real approaches are
Haar, state-conjugated Haar and dispersion-coordinate embedding; they do
not meet or pretend to meet a five-family universal no-go packet. N2,
no count or independence of walls is asserted. N3, supplied chain/state,
positive m,v, even CAR, endpoint domains and fixed compact word parameters
are explicit. N4, earlier counterexamples retain their original maps and
are not witnesses against this new construction. N5, the local Z and
specified packet number observables witness failures; constants and
zero parameters survive. N6, no new physical axiom is required or proposed.
N7, a different momentum transport or modified symmetry action could
change the exact compatibility question and is not excluded. N8, the
earlier successful asymptotic remedy is explicitly retained through E17-E19.
No mechanical no-go PASS or exhaustive impossibility claim is made.

E/CONTROL_PROTOCOL.md specifies the selective diagnostics before their
execution. The complete argument and protocol are frozen together first;
source scripts and material variants are sealed before any mathematical
process. Every scientific process has true INNER/OUTER timeouts, full
streams and source-bound receipts. Failures and survivors remain visible;
no gate is changed in response to output. Same-author alternate arithmetic
does not constitute fresh review. Final acceptance of this new source and
formal audit remain open. No Git, worktree, publication, editable prompt,
audit verdict or physical axiom is changed by this worker.

## 9. Post-execution clarification and complete evidence disposition

This appendix is later than the frozen analytic core. Sections 1–8 were
frozen at 2026-10-12T14:10:22.159188Z with SHA-256
f442f32f6c40102d3378f0dc96145250b78c1c13275683ac2bc1f9125828bd80.
The frozen protocol hash is
6c8dd67039cf2ca110ddf2afdde7c7bed10491adae55ab9e276e2d2945ec12e8.
The execution manifest was sealed at 14:13:38.030119Z, before the first
INNER process began at 14:13:51.035041Z. The baseline INNER began at
14:13:51.038941Z and ended at 14:13:54.090364Z. This appendix is a
post-execution clarification and interpretation, not a preregistration.
The original note, protocol, scripts, variants, streams, receipts and
manifest are preserved. FINAL_APPENDIX.diff records every added line.

The support wording in section 7 needs a sign distinction identified by
root's first source read. Let phi_s solve d phi_s(q)/ds=E_a(phi_s(q)),
phi_0(q)=q. On a lift of the circle characteristic the actual positive
band coefficient group obeys

    (exp(-is b_a^q) psi)(q)
      =sqrt(E_a(phi_s(q))/E_a(q))
         exp(ia[phi_s(q)-q]/2) psi(phi_s(q)).           (E23)

This follows by differentiating at zero using E21; its composition law
and periodic continuation give the full group. The nonvanishing amplitude
and phase show that support moves by phi_(-s), although the pullback uses
phi_s. Thus the upward characteristic at s=+.1 in the diagnostic tests
upward support motion for the coefficient-group parameter -.1. The
frozen script already printed that opposite-sign interpretation before
any output was inspected. The literal wording "transports support along"
the positive characteristic is to be read with this correction. The
existence witness in section 7, which explicitly chooses the parameter
sign moving support upward, and formulas E21–E22 are unchanged.

There is also a harmless small-a quantifier to make explicit in E14–E15.
For a fixed M, alias elimination requires aM<pi. Uniform comparison of
q_a with the identity on all of [-M,M] can be taken after also requiring
aM<2, which holds eventually as a tends to zero. No assertion that q_a
is defined outside I_a is intended. Neither this clarification nor E23
changes a diagnostic threshold or any executed source.

All three original jobs finished within their true INNER60/OUTER70
process-group bounds. Every source before/after hash, all six receipts
and all twelve complete stdout/stderr files were verified before the
scientific output was interpreted. No timeout occurred; every stderr
was empty. The longest INNER run took 3.052 seconds. The complete record
contains 714 predicate rows and 30 additional diagnostic rows:

| Original job | True predicates | False predicates | Process return |
| --- | ---: | ---: | ---: |
| Baseline | 238 | 0 | 0 |
| Drop the Jacobian | 190 | 48 | 1 |
| Reverse the cell phase | 226 | 12 | 1 |

The baseline's largest residual among the fixed 2e-10 identity checks was
3.553e-15. Its delta normalization was 0.9999999999999434 by direct p
integration and 0.9999999999999999 after the theta substitution, at each
of the three spacings. The original compact-input geometric errors were
0.17818064895142657, 0.09281542186095239, 0.04740254745386309,
0.02395357176429774 and 0.012039964844247152 at a=1,1/2,1/4,1/8,1/16.
Every value is retained; no fitted convergence rate is claimed.

Dropping the Jacobian failed the nonzero-momentum composition and
weighted-state pullback rows and the norm/endpoint-weight rows. Its
delta norm-square was instead 0.6366197723675814=2/pi to displayed
accuracy. The two integration routes still agreed with one another.
Energy multiplication, reality, inverse coordinates, zero-mode
composition/state and the loose limiting geometry diagnostic survived.
In particular its finest geometric error was 0.012039812242609695.
Agreement between numerical routes and apparent continuum convergence
would therefore not identify the correct finite-scale isometry.

Reversing the cell phase failed exactly the twelve direct physical-cell
versus alias comparisons at the four nonzero test momenta and three
spacings. The zero-momentum alias rows survived, as did the unrelated
isometry, state and energy checks. Its finest geometric error,
0.004097686187857804, was smaller than the baseline's and passed the
unchanged .08 bound. This is a recorded limitation of that diagnostic,
not a reason to select the incorrect finite-scale phase. All 416 mutant
survivors and all 60 mutant failures remain individually indexed.

The positive fine characteristics starting at p=1.9 and 1.95 reached
2.093405436844285 and 2.145666855874639 at characteristic time .1;
independent travel-time quadratures returned .10000000000000002 and .1.
By E23 these are the opposite-sign coefficient-group support witnesses.
Continuity supplies small smooth packet neighborhoods with the same
strict crossing, beyond the pointwise diagnostic. The actual current
and common-displacement defects were nonzero at all three frozen
nonzero momenta; their zero-momentum survivors were retained.

Numerical quadrature and ODE error estimates here are not interval
certificates. These selective controls do not prove the endpoint domain,
infinite-support claim, all-L2 convergence, CAR norm limits or local-net
identification; those are the analytic arguments above with pinned
parent hypotheses. Same-author alternate arithmetic is not independent
review. Fresh source review and any formal audit remain separate and
open at this seal. No evidence is relabeled as retained science.

E/README.md gives recovery and reproduction instructions. The row and
diagnostic inventories give exact original stream paths and line numbers;
result_disposition.json retains each failure and survivor name. All eight
original parent/brief files and their copies still match their pinned
hashes in parent_final_refresh.json. This worker changed no editable
prompt, physical axiom, audit verdict, Git state or publication surface.


## Publication evidence, chronology and scope

**Author/checker pairing:** Same selected model family and reasoning effort; separate reviewer context with a neutral plan sealed before target exposure and independent evidence sealed before author helpers/results exposure. Target formulas were exposed after that plan. Root coauthored the route. This is not blinded or diverse-family review. Packaging and reproduction add no independent science or audit.

This construction preserves the supplied actual state and energy flow exactly. Its six direct mathematical parents are [Concrete Gapped Chain](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md), [Local Even Continuum](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md), [Continuum Local Boost](CONTINUUM_LOCAL_BOOST_BOUNDED_THEOREM_NOTE_2026-10-12.md), [Microscopic Local Boost Limit](MICROSCOPIC_LOCAL_BOOST_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md), [Mixed Local Poincare Correlations](MIXED_LOCAL_POINCARE_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-10-12.md), and [Dyadic Even Refinement](DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md). The state-adapted construction is referenced and rederived, not imported as a theorem. Its PR is the intended repository parent only. The local-even-net-sections theorem is not an input. General CAR, OAR and inductive-limit machinery remain established prior art.

The original baseline is 238/0. The two original material mutants are drop-Jacobian 190/48 and reverse-cell-phase 226/12. Their 60 failing predicates and 416 surviving predicates remain, with all 30 diagnostic rows across the three jobs and all six original receipts. Both mutants survive the deliberately loose geometric convergence gate; the wrong phase even gives a smaller finest-scale diagnostic error. These survivors delimit that diagnostic. No threshold, scientific helper or candidate source is changed. The [complete evidence map](../.claude/science/physics-loops/toe-energy-adapted-20261012/EVIDENCE_MAP.json) and [mutation source map](../.claude/science/physics-loops/toe-energy-adapted-20261012/MUTATION_SOURCE_MAP.json) retain the exact original bytes.

Section 9 and the original FINAL_APPENDIX.diff preserve the late E23 correction: the coefficient pullback uses the positive characteristic, while support moves by its inverse. The upward characteristic diagnostic therefore corresponds to the opposite coefficient-group parameter. The eventual aM<2 clarification is also post-execution. Neither clarification is relabeled as preregistered, and neither changes the executed helper.

The historical recorder uses nested new process sessions. Its outer timeout alone does not guarantee termination of the inner session or its scientific child. All original jobs actually completed without a timeout, and complete inner/outer receipts and streams are retained. Publication reproduction uses the already reviewed wrapper and actual child exit/stream checks; it does not claim to repair or retrospectively certify the original recorder. Original receipts establish interpreter and Python identity. The package inventory was collected afterward and is not a historical per-run library lock. The only permitted stream-comparison change is the exact candidate pathname token, once per job.

The specified maps fail finite-support locality, common-displacement spatial intertwining, actual-current compatibility and boost intertwining. The transported boost domain retains periodic circle gluing and endpoint singularities. Fixed-observable limits do not imply uniform microscopic-unit-ball estimates, Haar H2 rates, exponential delta tails, growing-word or massless limits, or an all-refinement impossibility theorem. Numerical quadrature and ODE diagnostics are not interval certificates or proofs of the infinite-dimensional domains.

The [execution contract](../.claude/science/physics-loops/toe-energy-adapted-20261012/EXECUTION_CONTRACT.md) separates canonical execution, the two original mutant jobs and source-only preparation. Canonical reproduction is pending root execution. Source N1–N8 and literal N5 output remain scoped to these specified maps, without a no-go PASS. Independent integrated validation, strict audit lint and formal audit remain landing obligations. No retained promotion, axiom, prompt or audit verdict is introduced.

The final separate review and root gate support the stated conditional construction; they do not confer retained status or a whole-tree landing PASS. The independent baseline was 15/0; five original reviewer variants retained 63 survivors and 12 failures. All twelve independent receipts and three copied tamper-guard rejections are archived. They are not rerun by this publication program, and the guards make no race-free security claim. The reviewer recomputed 699 numeric author predicates; 15 symbolic/solver booleans remain recorded outcomes rather than independent proofs.

The reviewer's final-clean assertion failed while concurrent state publication changed the shared worktree. Every immutable energy/parent source identity still matched. The original failed assertion, diagnostic and final source refresh are preserved; review coverage applies to those immutable sources, not the changing packaged tree. Root's first independent-evidence verifier also failed on a bookkeeping filename (stdout versus guard.stdout). Its original script, failure record and empty result directory remain, alongside the narrowly corrected v2 success; no first RESULT is invented and no science was rerun.

The review makes the source's conjugation shorthand precise: F(-p)=conj(F(p)), D(-p)=-conj(D(p)), and P(-p)=1-conj(P(p)). Frames and time groups preserve real data; the Hermitian generator anticommutes with real conjugation. The same-sequence section equivalence keeps different recursively refined seeds distinct.
