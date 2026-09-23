---
claim_id: hybrid_generators_integrated_rates_and_curvature_witness_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
runner: scripts/hybrid_generator_check_2026_09_15.py
upstream_dependencies: ["docs/FINITE_CLOCK_GAUSSIAN_SMOOTHING_POSITIVE_LOCAL_ELECTRIC_EXTENSION_AND_FLUX_SCALING_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-09-15.md"]
claim_scope: "Bounded conditional hybrid-generator and curvature lemmas; supplied hypotheses and limit order retained in full proofs."
---

# Hybrid-generator and curvature lemmas

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Scope and actual premises

The complete mathematical arguments below retain their supplied model, representation, parameters and limit quantifiers. Original dates, personal-review statements and recorded numerical outcomes are historical provenance, not current cache or independent-review claims. This package does not certify five independent exclusion routes. Full-field, native-phase, kinetic-interpretation and joint-limit targets remain open wherever the proofs say so.

Actual mathematical dependencies:

- [FINITE_CLOCK_GAUSSIAN_SMOOTHING_POSITIVE_LOCAL_ELECTRIC_EXTENSION_AND_FLUX_SCALING_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-09-15](FINITE_CLOCK_GAUSSIAN_SMOOTHING_POSITIVE_LOCAL_ELECTRIC_EXTENSION_AND_FLUX_SCALING_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-09-15.md).

<a id="owned-argument-1"></a>
## Owned argument 1: BLOCK1_BOUNDED_RATE_ALTERNATIVE

Original source identity: `BLOCK1_BOUNDED_RATE_ALTERNATIVE.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### A bounded-rate alternative and the response it still needs

Personal derivation, 2026-09-15. Keep the same actual filtered clock measure
and the same exact-fiber diffusion as in BLOCK1_POSITIVE_HYBRID_GENERATOR.md.
Only the auxiliary proof dynamics changes. No physical law is changed.

For an oriented move v, put Delta S_v=v.Az+v.Av/2 and define

 b_v(z)=1/(1+exp(Delta S_v))=c_v(z)^2/(1+c_v(z)^2).

Then b_-v(z+v)=1-b_v(z), and

 exp[-S(z)]b_v(z)=exp[-S(z+v)]b_-v(z+v).

Thus L_b=L_c+sum_v b_v Delta_v is another reversible generator for the
same measure. In finite volume, its jump rate is bounded by the number
of oriented moves, so standard Poisson thinning and the Lipschitz fiber
SDE give a conservative construction directly.

The elementary inequality c/(1+c^2)<=1/2 implies b_v<=c_v/2. Therefore

 E b_v^p <= E b_v <= (1/2)exp[-q_v/8], p>=1.          (1)

The second-moment anomaly of the square-root rates is absent. If a=A v,
then the first three derivatives are

 D b_v[t]=-b_v(1-b_v)(a.t),
 D^2 b_v[t,u]=b_v(1-b_v)(1-2b_v)(a.t)(a.u),
 D^3 b_v[t,u,w]=-b_v(1-b_v)(1-6b_v+6b_v^2)
                         (a.t)(a.u)(a.w).

The absolute scalar coefficient in each line is at most b_v. Thus these
derivatives, when measured along specified directions, inherit (1) after
multiplication by the displayed deterministic factors. Their pointwise
suprema need not be small in beta: Delta S_v=0 is allowed.

For exp(i t.z), the expected absolute cubic remainder in the jump
generator is at most

 (h^3/6)exp[-pi^2 beta(1+4tau)/2] ||t||_3^3.          (2)

This again vanishes for four-dimensional diffuse tests, but is only a
generator Taylor remainder. The drift correlations and the fluctuation of
the quadratic intensity still need a volume-uniform response argument.

The two Dirichlet forms obey E_b(f,f)<=E_c(f,f)/2 for their jump parts.
There is no positive uniform reverse comparison: b_v/c_v tends to zero
both at very small and at very large c_v. Therefore a future gap proof
for the original rates would not automatically transfer by this comparison.

The mean jump drift has derivative

 D[sum_v v b_v(z)] = -sum_v b_v(1-b_v) v v^T A.

Its quadratic form is nonpositive in the A metric. This fact controls the
mean drift, not sample-path separation: unmatched jumps in a coupling also
contribute to the distance. No pathwise contraction, source differentiability
of jump paths, or stationary Gaussianity follows from this sign alone.

This is a concrete alternative that removes one identified obstacle. The
remaining weighted response problem is substantial; repeatedly introducing
rates without proving such an estimate would not advance the field target.

<a id="owned-argument-2"></a>
## Owned argument 2: BLOCK1_CURVATURE_TEST_DESIGN

Original source identity: `BLOCK1_CURVATURE_TEST_DESIGN.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Test the actual hybrid curvature before using it

Personal continuation of block 1. The proposed mechanism is a pointwise
Bakry-Emery estimate Gamma2(f)>=k Gamma(f), k>0, for the exact hybrid
generator in BLOCK1_POSITIVE_HYBRID_GENERATOR.md. Such a bound could support
response estimates; it has not been established. The test below targets
that sufficient criterion, not existence of a spectral gap or a field limit.

Use the actual single free four-cube, all 24 plaquettes and rank-17 exact
projection P. Keep tau=1/64 and A=I+tau DD*. The initial diagnostic sets
V_e=0 to calculate the reference exactly. Then use the actual small real
Hessian bound on V_e and its periodicity to check whether the result persists
for the supplied fixed-clock law. Do not identify this reference as the
finite-clock law by fiat.

For a face p set h=2pi sqrt(beta), z0=h e_p, q=h^2 A_pp, mu=exp(q/4),
lambda=exp(-3q/4), r=exp(-q/2). Choose a smooth compactly supported function
of z_p only. Its values at z_p/h= -1,0,1,2,3 are respectively 2,1,0,0,0.
At z_p=0,h,2h its first derivative is a0=h mu/2 and second derivative is
zero; at h its third derivative is also zero. Disjoint smooth bumps, equal
to one near these five points, realize these jets with compact support.

Evaluate Gamma=|P grad f|^2+(1/2)sum c_v(Delta_v f)^2 and
Gamma2=(1/2)L Gamma-Gamma(f,Lf) directly from the generator. Independently
derive a scalar expression using the cube's incidence and translation
symmetries. A negative value at this admissible point rejects a global
positive pointwise-curvature argument. It says nothing against an integrated
Bochner estimate, a weighted large-field argument, or another exact dynamics.

The calculation must retain changes of the p jump rate under other face
jumps; ignoring them changes Gamma2 even when f depends only on z_p.
The actual electric correction must also be bounded, not simply omitted.

<a id="owned-argument-3"></a>
## Owned argument 3: BLOCK1_INTEGRATED_IDENTITIES_AND_RATE_MOMENTS

Original source identity: `BLOCK1_INTEGRATED_IDENTITIES_AND_RATE_MOMENTS.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Integrated identities and exact non-small rate fluctuations

Personal derivation, 2026-09-15; exploratory support for the fixed-clock
campaign. These identities do not prove a spectral gap or a Gaussian limit.
Use exactly the carrier, potential, and generator in
BLOCK1_POSITIVE_HYBRID_GENERATOR.md, with oriented moves v=+/-h e_p.
Write q_v=v.A v and a_vw=v.A w. Expectations below are under the actual
centered filtered clock law, not the unrestricted Gaussian reference.

#### 1. Exact rate moments

For any real k, let m_k(v)=E[c_v^k]. The Gaussian tails and bounded periodic
potential in a fixed box ensure finiteness. The exact carrier translation
identity for M(t)=E exp(t.z) gives

 M(t-A v)=exp[q_v/2-t.v] M(t),
 m_k(v)=exp[-k q_v/4] M(-k A v/2).

Therefore

 m_(k+2)(v)=exp[k q_v/2] m_k(v).                      (1)

In particular, for every integer n>=0,

 m_(2n)=exp[q_v n(n-1)/2],
 m_(2n+1)=exp[q_v n^2/2] m_1.                        (2)

The previously derived bound m_1<=exp[-q_v/8] coexists with

 E c_v^2=1,       E c_v^4=exp(q_v),
 Var(c_v)=1-(E c_v)^2 >= 1-exp[-q_v/4].              (3)

Thus these rates do not become small in L2 as beta grows, even though
their mean vanishes. This is an exact property of the proposed dynamics,
not evidence that the equilibrium model has a large defect density.
The exceptional large rates compensate their small probabilities.

For 0<=k<=2, the centered MGF bound gives

 m_k <= exp[q_v k(k-2)/8].                            (4)

More generally (4) holds for all real k, but its right side grows when
k lies outside [0,2]. For any 1<=k<2 it provides a decaying Lk norm.
Evenness and translation also imply m_k=m_(2-k). Neither (3) nor (4)
supplies a multiplication-operator bound for c_v on arbitrary functions.
Indeed c_v is unbounded on the carrier, already along exact directions
with P A v nonzero. On compactly supported functions concentrated at such
points, E[c_v f^2]/E[f^2] can be arbitrarily large. This rejects only a
specific unweighted perturbation estimate. A weighted argument remains open.

#### 2. Mixed diffusion/jump identity

Let g=P grad f. For smooth compactly supported tests on the carrier,
integration by parts in the exact fibers and jump detailed balance give

 E[(L_c f)(L_j f)]
   = (1/2) sum_v E[c_v |g(z+v)-g(z)|^2]
     +(1/2) sum_v E[c_v g(z).(P A v) Delta_v f].       (5)

To verify the signs, differentiate the jump generator:

 P grad L_j f=sum_v c_v[Delta_v g-(P A v)Delta_v f/2].

Pairing the first term with -g and using reversibility yields the first
term in (5). Applying reversibility to the second term gives the equivalent
form with g(z) replaced by [g(z)+g(z+v)]/2. Its sign is not fixed.
Consequently the small mean-rate bound alone cannot discard this coupling.
The full integrated identity E Gamma2(f)=E(Lf)^2>=0 still holds; a positive
lower bound by E Gamma(f) is the separate spectral-gap obligation.

#### 3. An admissible jump-pair weight

For two moves define r(v,w)=exp[-a_vw/4] and

 R(dz,v,w)=pi(dz)c_v(z)c_w(z)r(v,w).

All translations commute. The measure is invariant under exchanging v,w,
and under (z,v,w)->(z+v,-v,w). In fact

 c_w(z+v)/c_w(z)=exp[-a_vw/2],
 r(-v,w)=exp[+a_vw/4].

These identities, together with detailed balance, prove admissibility.
No sign assumption on the off-diagonal entries of A is necessary. The
usual four-corner change of variables then gives the exact identity

 E[(L_j f)^2]
   =(1/4) sum_(v,w) E[c_v c_w r(v,w)(Delta_v Delta_w f)^2]
     +sum_(v,w) E[c_v c_w(1-r(v,w))Delta_v f Delta_w f]. (6)

This is verified by expanding the squared second difference and applying
the two invariances to its terms. The second term is not manifestly positive.
The centered MGF nevertheless gives the volume-independent mean bound

 E[c_v c_w r(v,w)] <= exp[-(q_v+q_w)/8].              (7)

Indeed the exponent before taking the MGF is
-(q_v+q_w+a_vw)/4, and its MGF argument is -A(v+w)/2.
The quadratic upper bound adds (q_v+q_w+2a_vw)/8,
so the cross term cancels exactly. Equation (7) does not bound the
same weight multiplied by arbitrary squared derivatives of f.

#### 4. Literature match and next obligation

Dai Pra and Posta, *Entropy Decay for interacting systems via the
Bochner-Bakry-Emery approach*, arXiv:1205.4599v3,
https://arxiv.org/html/1205.4599v3, section 2.3, supplies the general
admissible-move identity behind (6). Its sufficient estimate uses a
pointwise bound on weighted off-diagonal rates. Sections 3.1-3.2 treat
repulsive birth/death systems with a low-density condition, and one
special two-coordinate convex example. Those example hypotheses do not
match this hybrid constrained gauge law. Equations (1)-(7) above were
derived for this law; the paper does not establish its mixing or response.

A useful next result must control the residual in (5)-(6), or find an
alternative dynamics/representation with controlled source response.
Merely assuming that response, or replacing weighted expectations by
products of separate means, would reintroduce the original hard problem.

#### Finite source challenge

The companion `../evidence/block1_integrated_rate_check.py` checks the exact
second/third/fourth rate moments, moment reflection, the admissible pair-weight
bound, and the integrated jump identity for four Fourier tests. It uses the
original clock-link/image source evaluator on three free three-cubes.
Maximum moment relative error is 5.12e-14; maximum integrated-identity relative
error is 2.33e-16. No sampling of the generator, asymptotic phase calculation,
or independent review is used.

<a id="owned-argument-4"></a>
## Owned argument 4: BLOCK1_POINTWISE_CURVATURE_WITNESS

Original source identity: `BLOCK1_POINTWISE_CURVATURE_WITNESS.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### A negative pointwise-curvature witness for the actual hybrid generator

Personal derivation and finite check, 2026-09-15. This rejects one sufficient
proof criterion for the generator in BLOCK1_POSITIVE_HYBRID_GENERATOR.md.
It does not reject a spectral gap, integrated Bochner estimate, a Gaussian
field limit, another dynamics, the clock model, or the framework axioms.
No public no-go or independently reviewed theorem is being submitted here.

#### Geometry and test function

Take the single free four-dimensional unit cube: 32 edges, 24 faces, and
rank(D)=17. Its signed coordinate symmetries act transitively on faces,
so the exact orthogonal projection P has P_pp=17/24. Direct incidence gives
H=DD*, H_pp=4 and (H^2)_pp=24: each face shares an edge with eight others,
with off-diagonal H entries +/-1. Put tau=1/64 and A=I+tau H. Therefore

    p0=P_pp=17/24,
    d=(PAP)_pp=37/48,
    e=(APA)_pp=1289/1536,
    A_pp=17/16.                                         (1)

Fix beta>=1, h=2pi sqrt(beta), a face p, and the allowed carrier point
z0=h e_p. Put q=h^2 A_pp, mu=exp(q/4), lambda=exp(-3q/4),
r=exp(-q/2). The p-directed jump rates at z0 are c_-=mu and c_+=lambda.

Let f(z)=F(z_p), choosing the following finite jets:

| z_p | -h | 0 | h | 2h | 3h |
|---|---:|---:|---:|---:|---:|
| F | 2 | 1 | 0 | 0 | 0 |
| F' | 0 | a0 | a0 | a0 | 0 |
| F'' | 0 | 0 | 0 | 0 | 0 |

Here a0=h mu/2, and also F'''(h)=0. Finite disjoint smooth bumps, each
equal to one near its center, times the displayed constant/linear local
polynomial realize these jets with compact support. Thus f is an actual
smooth bounded test on the carrier, not inconsistent independent values.

At z0,

    Gamma(f)=p0 a0^2 + mu/2.                            (2)

#### Direct scalar reduction with V_e=0

Write L=L_c+L_j and Gamma=Gamma_c+Gamma_j. For the Gaussian reference,
the continuous contribution to Gamma2=(L Gamma)/2-Gamma(f,Lf) is
d a0^2. The mixed contribution from the p jumps is

    -d h mu a0 - e h^2 mu/16.                           (3)

The terms involving F'(z_p+/-h)-F'(z_p) vanish by the chosen jets; the
second term in (3) comes from L_c acting on the p jump rate. It must not
be omitted even though the second derivatives of F at these points vanish.

For a one-dimensional paired exponential jump, minimizing over the second
neighbor values with Delta_+f=u and Delta_-f=v gives the local expression

 (1/4)[(1-r)(lambda^2 u^2+mu^2 v^2)
          +lambda mu(3/r-1)(u^2+v^2)+4lambda mu u v].   (4)

It follows by substituting the rates at the two neighboring points in
the definitions of Gamma and Gamma2. The minimizing second-neighbor
values are 2u and 2v relative to f(z0). Our u=0,v=1 uses precisely these
values. Since lambda mu=r and mu^2 r=1, its contribution is

    mu^2(1-r)/4+(3-r)/4.                               (5)

Other face jumps also change the p jump rate. Their differences of f are
zero, but their contribution to (L_j Gamma_j)/2 is not zero. For any of
the eight neighboring faces k it is

    (1/2)mu exp(-q/4)[1-cosh(h^2 A_pk/2)].

Since A_pk=+/-tau and mu exp(-q/4)=1, these terms sum to
4[1-cosh(tau h^2/2)]<=0. All other faces contribute zero.

Combining (3)-(5) with a0=h mu/2 gives the exact reference value

 Gamma2_0(f)(z0)
   =mu^2(1-r-d h^2)/4+(3-r)/4
       -e h^2 mu/16 +4[1-cosh(tau h^2/2)].              (6)

The negative mixed term in (3) is the reason convexity of the continuous
quadratic action does not give a positive pointwise curvature bound for
this sum of diffusion and jump generators.

#### Keep the actual finite-clock correction

The exact electric extension is even and h Z^faces-periodic. Its gradient
therefore vanishes at z0 and all one- and two-jump points used above.
The jump rates are unchanged by the correction. Only the continuous
curvature Hessian term changes:

 Gamma2(f)(z0)-Gamma2_0(f)(z0)
     =-a0^2 (P e_p).Hess V_e(0)(P e_p).                 (7)

If ||Hess V_e||_op<=delta_e, then its absolute value is at most
delta_e p0 h^2 mu^2/4. Main's smoothing construction supplies

    delta_e=3 g^2 C0 exp(-g^2/1024),
    g^2=N^2/beta, C0=58,320,000,000,
    g^2>=65536 ==> delta_e<2e-12.                      (8)

This is a theorem input with its supplied law, free-cube and extension
hypotheses kept. It is not a numerical evaluation of the full potential.
No new primitive is used. For beta>=1 and N^2/beta>=65536 one has
h^2(d-delta_e p0)>4 and q>4. Equations (6)-(8) then give

    Gamma2(f)(z0) <= -3 mu^2/4+3/4 < 0.                (9)

The two remaining explicit terms in (6) are nonpositive. Thus a uniform
positive pointwise Gamma2/Gamma estimate for this particular generator
is unavailable in the intended small-electric-correction range, including
arbitrarily large fixed beta with sufficiently large fixed N.

#### Independent calculation path and the preserved numerical issue

`../evidence/block1_hybrid_curvature_check.py` builds the full four-cube D
and P, then evaluates L Gamma and Gamma(f,Lf) using their vector/tensor
definitions and the bump-compatible jets. It separately compares with (6).
For beta=1,2,4 the ratios Gamma2_0/Gamma are about -1.05248, -1.07036,
and -1.07930. The finite-clock Hessian allowance leaves all three negative.
The direct/scalar relative differences are at most 4.04e-16.

An initial floating-point evaluation failed at beta=2: forming the full
Gamma before subtracting neighboring values erased its exponentially
smaller jump component. The original source, output and failure are
preserved under `../review/block1_curvature_initial/`. The corrected
evaluation subtracts the continuous and jump components separately; no
tolerance was loosened. This is an arithmetic implementation repair,
not a change to the analytical expression or its target.

These are author checks. They do not independently review the upstream
extension theorem, certify all infinite-volume claims, or establish the
absence of other functional inequalities.

#### Consequence for the campaign

Keep the positive generator and its mean-rate identity. Drop only the
unqualified pointwise positive-curvature route. A rare high-energy point
can spoil that criterion even though its invariant probability is tiny.
An integrated estimate can still exploit the actual probability weights.
In particular integral Gamma2 = integral (Lf)^2 is nonnegative under
reversibility; (9) does not contradict it or prove that its positive
spectral-gap strengthening fails. Weighted large-field control, a different
reversible dynamics, and the signed defect expansion remain live routes.

<a id="owned-argument-5"></a>
## Owned argument 5: BLOCK1_POSITIVE_HYBRID_GENERATOR

Original source identity: `BLOCK1_POSITIVE_HYBRID_GENERATOR.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### A positive dynamics that keeps the magnetic carrier

Personal derivation, 2026-09-15. Provisional research; no independent review,
full-field limit, native law, or axiom amendment is claimed.

#### Exact starting measure

Use the finite free-cube smoothing identity on main
6ad6a2184b7c2067e597528e0964753874493b4a, with D=d1, B=d2,
P the orthogonal projection onto im D, h=2pi sqrt(beta), and
K=(I+tau DD*)^-1. Write A=K^-1. The actual filtered field has law

    pi(dz)=Z^-1 exp[-S(z)] m_C(dz),
    S(z)=z.Az/2 - V_e(z),
    C=im D + h Z^faces.

The measure m_C is counting measure on the discrete quotient of C by im D,
times Euclidean Lebesgue measure on each exact affine fiber. Uniform
normalizing constants cancel. The proven electric extension V_e is real,
even, smooth through order three, and periodic under every z -> z+h n,
n an integer face field. Its real Hessian and third derivative are small
in the stated large fixed-N parameter range. The discrete magnetic
condition Bz in h B Z^faces is retained.

For the specific construction tau=1/64, but the identities below hold
at any fixed tau>0 for which this exact periodic extension is used.
The sign of h Z is immaterial because the integer group is symmetric.

#### A candidate reversible generator

For each oriented face p put v_p=h e_p. Define

    c_p^+(z)=exp[-(S(z+v_p)-S(z))/2],
    c_p^-(z)=exp[-(S(z-v_p)-S(z))/2].

Periodicity removes V_e from these differences exactly:

    c_p^+(z)=exp[-v_p.Az/2-v_p.Av_p/4],
    c_p^-(z)=exp[+v_p.Az/2-v_p.Av_p/4].                 (1)

The formal generator on smooth test functions on the fibers is

    L f = tr(P Hess f) - (P grad S).grad f
        + sum_p [c_p^+(z)(f(z+v_p)-f(z))
                 +c_p^-(z)(f(z-v_p)-f(z))].           (2)

All moves preserve C. The diffusion acts only within a magnetic fiber;
the jumps change Bz by +/-h B e_p and connect the magnetic quotient.
This is an auxiliary proof dynamics, not a selected physical clock.

Fiber integration by parts gives the diffusion Dirichlet form. Translation
invariance of m_C and the exact balance identity

    exp[-S(z)]c_p^+(z)=exp[-S(z+v_p)]c_p^-(z+v_p)       (3)

give the jump form. Thus, wherever the integrations are justified,

    -<f,Lg>_pi = E_pi [(P grad f).(P grad g)]
      + (1/2) sum_(p,sigma) E_pi[c_p^sigma
                    (f(z+sigma v_p)-f(z))
                    (g(z+sigma v_p)-g(z))].            (4)

This establishes algebraic reversibility on a test-function core. The
finite conservative realization is supplied below. A volume-uniform
mixing or parameter-response theorem remains open.

#### A uniform bound on stationary jump intensity

The original centered clock flux X has E exp(t.X)<=exp(||t||^2/2).
The exact coupling z=K(X+sqrt(beta)D xi), with independent edge Gaussian
xi of covariance s^2 I and tau=beta s^2, gives

    E_pi exp(t.z) <= exp(t.Kt/2).                       (5)

Indeed K^2+tau K DD* K=K. Apply (5) to t=+/-Av_p/2 in (1):

    E_pi c_p^+ , E_pi c_p^- <= exp[-v_p.Av_p/8].        (6)

This is independent of volume and uses the centered law only. On a free
cubic face D has four signed boundary edges, so (DD*)_pp=4, including
boundary faces. Consequently

    E_pi(c_p^+ + c_p^-)
      <= 2 exp[-pi^2 beta(1+4tau)/2].                  (7)

The expected total jump intensity in a finite box is finite, bounded
by its number of faces times (7). This is not a mixing bound.

#### Finite-volume nonexplosion, without a uniform response claim

The drift in (2) is globally Lipschitz on each fiber, since Hess V_e is
bounded. The jump rates are locally bounded and smooth. Construct the
diffusion and jump clocks up to exits from bounded sets by the usual
finite-dimensional SDE and thinning construction. For W(z)=1+z.Az,

    L_cont W=2 tr(PA)-2|PAz|^2+2(PAz).(P grad V_e)
             <=2 tr(PA)+|P grad V_e|^2.

The last quantity is bounded by a finite constant proportional to the
number of faces, using the uniform per-coordinate first derivative bound.
For one paired jump direction put x=v.Az and q=v.Av>0. Its contribution is

    2 exp(-q/4)[q cosh(x/2)-2x sinh(x/2)].             (9)

This is bounded above for all real x. Explicitly, if R=max(q,2), then
for |x|>=R one has tanh(|x|/2)>=1/2, so the bracket is nonpositive;
inside that interval it is at most q cosh(R/2). Therefore LW<=C times
the number of faces, with a finite parameter-dependent C. Stopped Dynkin
estimates and W>=1+|z|^2 rule out escape to infinity in finite time.
Inside any bounded set the finite total jump rate rules out accumulation
of jump times. Thus the finite-dimensional construction is conservative.

The integration-by-parts identities, applied first to compactly supported
core functions and then localized, identify the invariant reversible
probability pi. Equivalently its symmetric Dirichlet form has the above
conservative realization. No volume-independent convergence rate follows
from this Lyapunov estimate: its upper constant scales with volume and
can grow rapidly with beta. No infinite-volume process has yet been constructed.

#### Diffuse-source jump remainder

For a real face test t, apply the jump part of (2) to exp(i t.z) and
divide by that exponential. Its linear and quadratic terms are

    i sum_p (t.v_p)(c_p^+-c_p^-)
       - (1/2) sum_p (t.v_p)^2(c_p^++c_p^-).

The real-argument Taylor remainder |exp(iu)-1-iu+u^2/2|<=|u|^3/6
and (6) give the expectation bound

    E_pi |R_jump(t,z)|
      <= (h^3/3) exp[-pi^2 beta(1+4tau)/2] ||t||_3^3. (8)

For four-dimensional smooth tests t_a(p)=a^2 f_p(a x),
||t_a||_3^3=O(a^2). Therefore this generator's microscopic jump
Taylor remainder vanishes at macroscopic scaling, with N and beta fixed.
This is a statement about the generator expression, not about the third
cumulant of the stationary field.

#### Exact residual and next discriminator

The potential advantage of (2) is that it keeps a positive law and the
actual quantized support, while placing the electric correction in a small
continuous drift perturbation. No mixed electric/magnetic complex weights
have been interpreted as probabilities. The rare jumps remain present.

The stationary equation E_pi L exp(i t.z)=0 still contains nonlinear drift
correlations and the random quadratic jump intensity. Bound (8) does not
control either term, prove ergodicity, or imply a Gaussian stationary law.
In fact the diffusion and jump parts are separately invariant under pi;
their zero stationary expectations cannot be treated as two independent
constraints that by themselves determine pi. Discarding the jumps leaves
every magnetic fiber invariant and loses control of the mixture of fibers.
The missing theorem is a uniform response/homogenization estimate for this
specific hybrid generator (or a different exact reversible dynamics).
As a bare assumption that theorem is comparable to the original target;
the generator is a possible mechanism for proving it, not a completed
reduction that moves the target near closure.

Next examine the mixed diffusion/jump coupling rather than infer contraction
from convexity of S. Even a convex extension does not automatically supply
convexity inequalities for a constrained discrete measure. First verify (1),
(3), (5)-(8) by direct finite source/density calculations, then test a proposed
coupling or Dirichlet estimate on actual magnetic fibers. If it fails, preserve
the concrete failure and try a materially different estimate.

#### Finite source challenge

`../evidence/block1_hybrid_generator_check.py` enumerates 32, 243 and 1024
tree-gauge clock configurations on a free three-cube for (N,beta) equal to
(2,.25), (3,.5), (4,.8). It sums image integers separately and uses the exact
Gaussian convolution to compute the filtered complex source. This route
does not evaluate the proposed electric potential or its derivatives.

The carrier translation identity independently predicts

    M(t-Av)=exp[v.Av/2-t.v] M(t),                      (10)

for the actual filtered moment function. Direct source sums verify (10),
the separate stationary jump identity, all six per-face rate bounds and
the integrated absolute Taylor bounds at four source amplitudes. Maximum
relative error in (10) was 1.268e-14; image cutoffs 8 and 10 agreed to
floating precision. The cutoff comparison is not an interval certificate.
These finite parameters challenge algebra and normalization, not the
large-parameter all-volume phase theorem. The analytic potential-existence
hypotheses and the open response bound remain separate.


## Canonical evidence and N1–N8 boundary

The route/proof appendices preserve the actual attempts, assumptions, residuals and surviving alternatives. Their components are not independent physical walls (N1/N2). Hypotheses and limits stay as written (N3/N4). N5 stdout distinguishes finite executed elements, sites, modes and blocks from unexecuted analytical limits. N6–N8 remain open to the positive routes and prior-result comparisons described above. No broad negative-certification PASS is asserted.

- [Program: hybrid_curvature_check_2026_09_15](../scripts/hybrid_curvature_check_2026_09_15.py); [current cache](../logs/runner-cache/hybrid_curvature_check_2026_09_15.txt).
- [Program: hybrid_generator_check_2026_09_15](../scripts/hybrid_generator_check_2026_09_15.py); [current cache](../logs/runner-cache/hybrid_generator_check_2026_09_15.txt).
- [Program: integrated_rate_check_2026_09_15](../scripts/integrated_rate_check_2026_09_15.py); [current cache](../logs/runner-cache/integrated_rate_check_2026_09_15.txt).

[Exact source recovery](work_history/review_loop/pr8159/README.md).
