---
claim_id: positive_wilson_villain_mixture_and_weak_region_bounds_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
runner: scripts/positive_wilson_villain_mixture_and_weak_region_bounds_check_2026_09_16.py
upstream_dependencies: []
claim_scope: "07: positive Wilson/Villain Hartman-Watson mixture, partition reweighting domination, weak-region tails and diluted comparison. Infinite first mixing-time moment is retained; no finite-variance auxiliary field or thin-slice phase conclusion."
---

# Positive Wilson–Villain mixtures and weak-region bounds

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

## Scope and provenance

07: positive Wilson/Villain Hartman-Watson mixture, partition reweighting domination, weak-region tails and diluted comparison. Infinite first mixing-time moment is retained; no finite-variance auxiliary field or thin-slice phase conclusion.

The complete original mathematical argument follows. Its personal reading, timing, proposal and review statements describe historical work, not a new review or current execution. Model parameters are supplied. No PR8160, PR8162 or PR8163 result is implicitly a premise. Narrow quantitative bounds and explicit witnesses do not supply a broad negative certificate or a physical phase. No five-route no-go PASS is asserted.

The supplied model and proof are redeclared here; other campaign mentions are context.

## Complete argument

# Positive Wilson mixtures and control of weak regions

Working derivation, 2026-09-16. Standard Hartman-Watson and Ginibre machinery
is used explicitly and credited below. The result is an exact positive
representation of the supplied Wilson angle law, an exponentially small
bound on specified sets of weak auxiliary plaquettes at large Wilson
coupling, and a comparison with a diluted Villain model. It is not a
Hamiltonian Coulomb-phase theorem or a new derivation from the axioms.

## 1. Known machinery and what is checked here

The Hartman-Watson representation is classical. We use Matsumoto and Yor,
[Exponential functionals of Brownian motion, I, math/0511517v1](https://arxiv.org/abs/math/0511517),
section2, in particular(2.8)-(2.13), and independently spell out its
application to normalized plaquette factors. PDF pages1-8 were read;
the 36-page PDF has SHA256
`7f1b50b9ecc5b3aedb486f25e276fe9406cd4cea3dc2418ce15ccb1e57431f6b`.
Hariya's arXiv1904.00595v3, equation(1.3), provides the same transform;
the reading receipt records the limited part read.

Villain Wilson-loop monotonicity is an existing theorem: Chevyrev and
Garban, [Villain action in lattice gauge theory, arXiv2404.09928v2](https://arxiv.org/abs/2404.09928v2),
Corollary1.6. All18 extracted PDF pages were read; SHA256
`89720d61bd0c0ebc2ac7e27d0d808de7ed8c13fc73f863c79302d38293cb2ae4`.
Section5 below also gives a direct Abelian character construction to check
the comparison used here.

The annealed-to-quenched comparison method is also known. Dario, van
Engelenburg and Garban, [arXiv2604.24743v1](https://arxiv.org/abs/2604.24743v1),
section3.5, apply positive Fourier sums and product-measure association to
spin models. The pages containing that proof were read. We apply the same
argument to a finite gauge incidence matrix and retain its domain: the
paper's percolation phase theorem for vertex spins is not a phase theorem
for four-dimensional gauge plaquettes.

## 2. Exact mixture, including the normalization

Use normalized Haar measure dtheta/(2pi) on the circle. Set

    W_a(theta)=exp(a cos theta)/I_0(a), a>0,
    V_t(theta)=sum_n exp(-t n^2/2) exp(i n theta)
              =sqrt(2pi/t) sum_k exp[-(theta-2pi k)^2/(2t)], t>0.

Both factors have Haar integral1. There is a probability measure mu_a on
(0,infinity) with

    integral exp(-nu^2 t/2) mu_a(dt)=I_|nu|(a)/I_0(a), nu real.       (1)

Therefore

    W_a(theta)=integral V_t(theta) mu_a(dt).                        (2)

One rigorous justification is by Fourier coefficients: both sides are
nonnegative integrable densities with the same coefficients. In fact the
identity is pointwise: the Fourier series may be interchanged since

    sum_n integral exp(-t n^2/2)mu_a(dt)=exp(a)/I_0(a)<infinity.

The Brownian meaning of mu_a is especially useful. Let R be a
two-dimensional Bessel bridge from radius1 to radius1 over time T=1/a.
Then mu_a is the law of

    A=integral_0^T R_s^(-2) ds.                                  (3)

The bridge conditions on the endpoint radius, not a fixed planar
endpoint. Its planar realization first samples an endpoint angle Phi
with density W_a(Phi) relative to Haar, then a planar Brownian bridge
from(1,0) to(cos Phi,sin Phi) in time T. Taking the norm yields the
required radial bridge. This distinction is needed for the next bound.

For completeness,(1) follows by dividing the Bessel heat kernels of
indices nu and0 after the absolute-continuity insertion
exp[-nu^2 integral R^(-2)/2]. Their common radial Gaussian factors cancel,
leaving I_|nu|(1/T)/I_0(1/T). This uses nonnegative indices and positive
end radii, exactly the range stated in the primary source.

## 3. An elementary large-a concentration bound

Suppose a>=1, set r=(sqrt(3)-1)/2, and define

    epsilon(a)=min{1, pi exp(1/2) sqrt(a) exp(-a/2)
                         +4 exp(-r^2 a)}.                       (4)

Then

    mu_a((4/a,infinity)) <= epsilon(a),
    mu_a((0,1/(4a))) <= min{1,4 exp(-a)}.                        (5)

Here is the full probabilistic bound. For |Phi|<=pi/3 the straight chord
between the endpoints has distance at least sqrt(3)/2 from the origin.
Write the planar bridge as that chord plus a centered planar bridge B.
If sup_s|B_s|<=r, its radius is at least1/2 throughout, giving A<=4/a.
The one-dimensional reflection formula gives
P(sup B_s>=u)=exp(-2u^2/T). Taking both signs and two coordinates shows

    P(sup_s|B_s|>r)<=4 exp(-r^2/T).

The residual centered bridge is independent of its endpoint. Also

    I_0(a)>=[exp(a-1/2)]/[pi sqrt(a)],
    P(|Phi|>pi/3)<=pi exp(1/2)sqrt(a)exp(-a/2).

The first estimate integrates only0<=Phi<=1/sqrt(a) and uses
cos Phi>=1-Phi^2/2. The second bounds the numerator by exp(a/2).
These observations prove the first part of(5). For the second, every
endpoint chord has norm at most1. If sup|B|<=1, then R<=2 and A>=1/(4a).
The same bridge estimate finishes the proof. Constants are conservative;
their role is a volume-independent exponential smallness parameter.

## 4. Coupling the plaquettes improves the upper-tail comparison

Let C be the integer edge-to-plaquette curl matrix of a finite free cubic
box. More generally the next argument holds for any finite integer
matrix. Give plaquette p a Wilson coupling a_p>0. Formula(2) gives an
exact joint positive law of angles theta and auxiliary variances t_p,
with unnormalized density

    product_p V_(t_p)((C theta)_p) product_p mu_(a_p)(dt_p) dtheta.

After the angles are integrated, the density of t relative to the product
prior mu=product_p mu_(a_p) is Z_V(t)/E_mu Z_V, where

    Z_V(t)=sum_{q in Z^P: C* q=0} exp[-sum_p t_p q_p^2/2].         (6)

Every coefficient is nonnegative, so Z_V decreases in every t_p. The
partition function is integrable because the original finite Wilson
density is bounded. Association of a product measure now gives, for
every bounded coordinatewise increasing F,

    E_joint F(t)=E_mu[F Z_V]/E_mu Z_V <= E_mu F.                 (7)

For clarity, association here follows by the one-variable identity
Cov(f(X),g(X))=E[(f(X)-f(X'))(g(X)-g(X'))]/2 and induction over the
independent coordinates. Apply it to F and -min(Z_V,M), then let M grow.
Thus the use of a possibly unbounded Z_V is justified.

In particular, for any specified set S of plaquettes with a_p>=1,

    P_joint(t_p>4/a_p for every p in S)
                <= product_(p in S) epsilon(a_p).              (8)

This controls the coupled law, not just an isolated plaquette. It holds
uniformly in the volume and for sets of any size. It does not say that
all plaquettes in an infinite volume are good.

For example, join plaquettes that share an edge, in dimension d. The
degree of this graph is at most D=4(2d-3). If all a_p>=a>=1, the
probability that the bad component of a specified plaquette contains
at least n plaquettes is at most

    D^(2n-2) epsilon(a)^n.                                    (8a)

Indeed any such component contains a connected n-element set through
that plaquette. A fixed choice of spanning tree and its depth-first
traversal encodes each such set by a walk of length2n-2, giving at most
D^(2n-2) choices. Apply(8) and the union bound. Thus sufficiently large
a gives an exponential component-size bound without assuming independent
bad indicators in the coupled law. This is a geometric statement about
the auxiliary weak plaquettes; a dilute-defect gauge-phase argument is
still required.

The partition comparison(6)-(8) also holds for uniform finite-clock link
variables: the condition C*q=0 becomes C*q=0 modulo N and every term
remains nonnegative. The Wilson-loop monotonicity used in the next
section is stated here for continuous Haar links only.

## 5. The needed Villain correlation monotonicity

For Haar angles and nonnegative cosine couplings, the classical Ginibre
inequality holds for all integer characters. A direct proof uses two
copies and theta=v-u, theta'=v+u on the compact covering torus. The
product measure pulls back to Haar measure and

    cos(b theta)+cos(b theta')=2cos(bu)cos(bv),
    cos(j theta)-cos(j theta')=2sin(ju)sin(jv).

Expanding each exp[2J_b cos(bu)cos(bv)] gives nonnegative coefficients.
The doubled covariance integral is a sum of squares of real integrals.
Hence increasing a nonnegative J_b increases every cosine-character
mean. This is the classical argument, distinct from the quantum
ground-state covering argument in BLOCK05.

To transfer it to V_t, replace each V_t(b theta) by m convolutions of
W_(m/t), introducing m-1 auxiliary circle angles. All new terms are
cosines of integer characters with nonnegative couplings. The Fourier
coefficient is [I_n(m/t)/I_0(m/t)]^m, which tends to exp(-tn^2/2).
This convergence is uniform in the circle variable, as can be checked
without a weak-convergence shortcut. A contour shift and I_0'/I_0<=1 give

    I_n(beta)/I_0(beta)
       <=exp[-n asinh(n/beta)+sqrt(beta^2+n^2)-beta]
       <=exp[-n^2/(2(beta+n))], n>=0.                           (9)

For beta=m/t, the m-th power is at most exp(-t n^2/4) when n<=beta,
and at most exp(-m n/4) otherwise. It is thus bounded by the summable
envelope exp[-min(t,1)|n|/4], uniformly in m>=1. The fixed-n limit follows
from the usual local Gaussian limit for one von Mises step; it can also
be obtained by rescaling theta by sqrt(beta) in its defining integral.
Dominated Fourier summation proves the claimed uniform convergence.

Increasing the inverse variance1/t increases every coupling m/t of the
approximating character model. Passing through uniform convergence
therefore shows that every Villain cosine-character mean increases with
1/t. Setting t=infinity deletes that interaction by the uniform limit
V_t->1. This reproduces the needed Abelian monotonicity, which is already
established for gauge Wilson loops in the cited Corollary1.6.

## 6. Reduction to a diluted Villain comparison

Let W_j(t)=<cos(j dot theta)> for the normalized Villain model with
variances t. It is nonnegative and decreases coordinatewise in t. For a
given t define the set B={p:t_p>4/a_p}. Replace t_p by4/a_p off B and
delete the interactions on B. Monotonicity gives

    W_j(t)>=W_j^dil(B; beta_p=a_p/4).

The right side decreases when B grows. Applying(7), and then increasing
the independent bad probabilities from their actual values to(4), gives

    <cos(j dot theta)>_Wilson
      >= E_Bernoulli[ W_j^dil(B; beta_p=a_p/4) ],               (10)

where the plaquettes are deleted independently with probabilities
epsilon(a_p). This is a finite-volume comparison with explicit constants.
It requires no assumed independence under the coupled mixture law.

It still needs a gauge-phase theorem robust to these deleted plaquettes.
A percolation theorem for vertex-spin two-point functions cannot simply
be relabeled as a theorem for gauge Wilson loops. Moreover even a useful
Wilson perimeter bound needs a separate spectral/source argument before
it establishes the Hamiltonian photon target in BLOCK02.

## 7. The auxiliary variance has an infinite mean

The mixture is not a uniformly elliptic Gaussian replacement. For every
finite a>0, E_mu_a[t]=infinity. Indeed the Bessel connection formula gives
partial_nu I_nu(a)|_(nu=0)=-K_0(a)<0, and(1) implies

    1-E exp(-lambda t)
        =sqrt(2lambda) K_0(a)/I_0(a)+O(lambda), lambda down to0.

The difference quotient divided by lambda diverges; monotone convergence
of (1-exp(-lambda t))/lambda proves the assertion. The source also gives
the corresponding t^(-3/2) density tail in its equation(2.11).

Consequently an unwrapped normal variable X conditional on t, with law
N(0,t), has E[X^2]=infinity, although its wrapped law is exactly W_a.
It would be wrong to identify that auxiliary unwrapped field with the
finite-variance physical field in the existing fixed-Haar Villain source
theorem. The exact equivalence here is for compact angle observables.
The exponential probability estimate(5) is compatible with an extremely
rare but sufficiently long tail to make the mean infinite.

## 8. Match to physical time: remaining obligation

In the Hamiltonian time slicing, a single spatial Wilson factor has
a=delta/g^2. This tends to zero, so(4) supplies no small bad-region
parameter uniformly in delta. For isolated magnetic jumps, convolution
over a fixed physical time T gives the Bessel coefficients with a=T/g^2,
as proved in BLOCK01. The actual coupled transfer has intervening
electric kinetic factors; those do not commute with magnetic jumps.
Replacing its block by the isolated W_(T/g^2) is therefore not justified.

The concrete next obligation is to obtain a positive comparison of the
actual physical-time block that preserves a bound such as(8), or another
uniform defect estimate after blocking. No Hamiltonian phase conclusion
is being imported through an unproved interchange of these operations.

## Review and proposal status

The [claim-status contract](work_history/review_loop/pr8164/README.md) and
[premise inventory](work_history/review_loop/pr8164/README.md) apply to this author
proposal. The [negative-claim checklist](work_history/review_loop/pr8164/README.md)
records the scoped comparison restrictions and untested alternatives.
Independent review, formal registration and retained landing are pending.


## Canonical evidence boundary

[Program](../scripts/positive_wilson_villain_mixture_and_weak_region_bounds_check_2026_09_16.py); [current stdout cache](../logs/runner-cache/positive_wilson_villain_mixture_and_weak_region_bounds_check_2026_09_16.txt). The canonical TOTAL counts 4 completed finite control families, not each loop iteration or an analytical theorem. All original assertion expressions and tolerances are retained. No canonical capture has run during preparation. Historical outputs, failed refinements and mutations remain in the [exact recovery archive](work_history/review_loop/pr8164/README.md).
