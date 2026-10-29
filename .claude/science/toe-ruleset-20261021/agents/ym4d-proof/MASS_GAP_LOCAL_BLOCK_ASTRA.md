# Wilson ground-state block ratios and a physical-time strong-coupling endpoint

Author construction checkpoint, 29 October 2026. **The four-dimensional
continuum existence and physical mass-gap target remains open.** This unit
constructs volume-independent local ground-state comparisons and a positive
one-step plaquette witness at every finite beta>0. At 0<beta<=1/32 it also
derives contraction of the actual physical-time Doob kernel, including the
magnetic factor and ground-state ratio. The resulting fixed-spacing endpoint
has a unique vacuum and a finite, positive spectral threshold on its full
physical observable Hilbert space. Its cutoff dependence prevents using it
as the requested continuum theorem.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
independent_review: pending
MG_rows_closed: []
```

## 0. Exact premises and the consumer being filled

The target is [MASS_GAP_TARGET.md](MASS_GAP_TARGET.md), SHA256
`105440c10b9a2fc91b2be366f439053de05fd3d3497596f8f28993b0fe42de7b`.
Its common physical rate, cutoff/volume-independent prefactor and onset time,
complete observable algebra, and finite-energy witness remain mandatory.
The supplied action is [PROOF.md, Setting S1-S3](PROOF.md). Its normalized
S4' kernel and source chain are in [PROOF.md, Decision 4](PROOF.md) and
[HIST.md, sections 0 and 2](HIST.md); they enter only the unresolved RG
interface in section 7, not the endpoint proof.

The exact finite transfer definitions are inherited from
[MASS_GAP_CONSTRUCTION_ASTRA.md, section 1](MASS_GAP_CONSTRUCTION_ASTRA.md),
SHA256 `a5d31da82721607e0ba04fef84675706bd3f2c568644224cce7dc86b0bb968e2`.
Its [independent bounded review](REVIEW_MASS_GAP_CONSTRUCTION_ASTRA.md),
SHA256 `8ab911c6e8705c086b0fd4e12930a7a66f8ea0ad03be2bb1bff5a55a62f3c9c1`,
confirms the finite scope, not an infrared producer. In particular, this unit
uses its actual A k P A transfer, strictly positive Perron vector, and the
convolution eigenvalue c_R/(d_R c_0). The ground-state measure is psi^2 dU;
it is not the auxiliary A psi measure used in transition normalization.

The [handoff](HANDOFF.md) and [PROOF.md, S27 recovery](PROOF.md) retain the
open determinant, all-history return, uniform multiscale, reconstruction
and non-freeness obligations. None is assumed solved here. The group is
SU(N), N>=2. The SU(2) numerical diagnostic below has that narrower scope.
No compact-simple-group generalization, observed mass, fitted coupling or
new physical premise is imported.

Methodology, freshness, primitive-registry and prior-art reads use main
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`. Their exact sources and read scopes
are bound in the [manifest](checks/massgap_block_manifest.json). The installed physics-loop skill and its already-read same-revision
references govern this continuation; the portable
[repository entry](../../../../../docs/ai_methodology/skills/physics-loop/SKILL.md)
is linked for repository readers.
The prior-art endpoint notes are
[constrained-fiber Dobrushin control](../../../../../docs/WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md),
[raw-action Hessian decay](../../../../../docs/WILSON_STAGGERED_RAW_CONSTRAINED_ACTION_HESSIAN_DECAY_BOUNDED_THEOREM_NOTE_2026-07-12.md),
[native coefficient-transfer gap](../../../../../docs/NATIVE_GAUGE_TRANSFER_STRONG_COUPLING_GAP_NARROW_THEOREM_NOTE_2026-06-12.md),
and [fixed-lattice gap scope](../../../../../docs/FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md).
Their scope boundaries remain in force. Small-beta Dobrushin machinery and
strong-coupling mass gaps are established prior art. This unit's lane-local
advance is the explicit ground-state conditional kernel, its physical-time
contraction, and a volume-independent finite-energy witness for the actual
spatial Wilson environment. No global novelty claim is made.

## 1. Exact local ground-state ratios, without a small-beta assumption

Let Gamma be a periodic spatial cubic lattice of side at least four. All
spatial edges, spatial plaquettes and spatial holonomy sectors are retained.
The Wilson coupling is beta=2N/g_K^2 and the regulator spacing is a=L^-K.
Write X=SU(N)^E, normalized product Haar dU, w(V)=Re tr(V)/N, and

    A(U)=exp[-(beta/2) sum_p (1-w(U_p))],
    k(U,V)=product_e exp[beta w(U_e V_e^dagger)],
    K=k P_gauge,       T=A K A,       T psi=lambda_0 psi,
    integral psi^2 dU=1,             u=A psi.                       (1)

The inherited finite result gives continuous psi>0, simple lambda_0>0,
and a positive, injective physical transfer on the full invariant space.
For U,U' differing only on a set B of b edges, positivity of the gauge
integral and the bound |w|<=1 give pointwise

    exp(-2 beta b) <= K(U,V)/K(U',V) <= exp(2 beta b).                (2)

Thus the Perron equation gives the sharper, action-retaining comparison

    exp(-2 beta b) <= [psi(U)/psi(U')]/[A(U)/A(U')]
                  <= exp(2 beta b).                               (3)

Let p_B count spatial plaquettes touching B. Then |Delta_B log A|<=beta p_B
and, at each fixed exterior Z=U_(E\B),

    u_min(Z) <= u(U_B,Z) <= exp(D_B) u_min(Z),
    D_B=2 beta(p_B+b),       u_min(Z)=min_(U_B) u(U_B,Z)>0.           (4)

The actual conditional density of pi=psi^2 dU on B is proportional to
psi(U_B,Z)^2. Its log-density oscillation is at most
2 beta p_B+4 beta b, so its density relative to product Haar is at least
exp[-2 beta p_B-4 beta b]. This is local finite-energy comparability. It
contains no decay with distance and supplies no mixing theorem by itself.
A physical block of side ell has b of order (ell/a)^3; (4) therefore has no
useful cutoff-uniform interpretation just by declaring ell fixed.

## 2. A volume-independent, positive one-step plaquette witness

Normalize the one-link convolution by

    c_0(beta)=integral exp[beta w(V)] dV,
    r_f(beta)=c_f(beta)/(N c_0(beta))>0,                             (5)

where c_f is the coefficient of the fundamental character. The conjugate
coefficient equals c_f because the weight is real and invariant under
V -> V^dagger. For SU(2) fundamental and conjugate coincide; they must not
be counted twice as distinct irreducibles. In this case r_f=I_2(beta)/I_1(beta).
Let kbar=k/c_0^|E|, a positive operator with pointwise positive kernel and
kbar 1=1. These are two different positivity properties, both used below.

Let C be a simple spatial loop whose b distinct unoriented edges form B.
Set W_C=w(product_(e in C) U_e^(orientation)), m=integral W_C psi^2 dU,
and F=W_C-m. Independent Haar integration makes the loop holonomy Haar.
Schur orthogonality gives

    v_N=integral W_C^2 dU_B = 1/4                if N=2,
                            1/(2 N^2)          if N>=3.             (6)

Indeed W_C=(chi_f+chi_fbar)/(2N); the two characters are orthogonal for
N>=3, whereas chi_f is real and has norm one for SU(2). The local product
convolution satisfies kbar_B W_C=rho W_C, rho=r_f^b. Hence

    <F,kbar_B^(-1)F>_Haar = m^2+v_N/rho <= 1+v_N/rho,
    kbar_B >= c |F><F|,       c=(1+v_N/rho)^(-1).                    (7)

The last line is an OPERATOR quadratic-form inequality. It follows by
Cauchy-Schwarz with kbar_B^(1/2); F lies in the finite sum of the constant,
fundamental and conjugate tensor subspaces, so the inverse in the first
line has a finite, specified domain. No inverse on all of L2 is asserted.

Gauge invariance of u and uF removes P_gauge inside the following quadratic
forms, without discarding physical states. The actual centered correlation
at one time step a is

    C_F(a)=<F psi,(T/lambda_0)F psi>
          = <uF,kbar uF>/<u,kbar u>.                              (8)

Keep kbar_out on ALL exterior edges. Tensoring (7) with the positive
operator kbar_out yields

    <uF,kbar uF> >= c <b_F,kbar_out b_F>,
    b_F(Z)=integral dU_B u(U_B,Z) F(U_B)^2
          >= v_N u_min(Z).                                       (9)

The last inequality uses integral F^2=v_N+m^2>=v_N. Now use pointwise
nonnegativity of the exterior kernel, separately from (7), to obtain

    <b_F,kbar_out b_F> >= v_N^2 <u_min,kbar_out u_min>,
    <u,kbar u> <= exp(2D_B) <u_min,kbar_out u_min>.                 (10)

The denominator bound uses (4) and integral dU_B dV_B kbar_B(U_B,V_B)=1.
The exterior form is positive and cancels. Thus, for EVERY beta>0,

    C_F(a) >= eta_C(beta,N)
      := v_N^2 exp[-4 beta(p_B+b)]/(1+v_N/r_f(beta)^b) > 0.         (11)

This is independent of the total spatial volume. For an elementary
plaquette on the stated torus, b=4 and p_B=13, so the exponential is
exp(-68 beta). The estimate is deliberately conservative. It is a lower
bound for a correlation, not a lower bound for a gap.

Since C_F(0)=Var_pi(W_C)<=1, the finite-volume nonvacuum spectral threshold
satisfies m_Gamma <= -log eta_C/a. It is finite. At fixed beta and a the
same witness survives any matching thermodynamic limit of the two local
slices. At a->0, (11) concerns a time a that tends to zero, and the displayed
energy upper bound grows as 1/a. It is not MG4's continuum finite-energy
witness or a fixed-physical-time lower correlation estimate.

## 3. Open-time slabs expose the actual ground-state boundary response

Introduce the unprojected transfer T_hat=A k A. It commutes with spatial
gauge transformations and equals T on invariant functions. Starting with
1, every iterate remains invariant; therefore

    psi_n=T^n 1=T_hat^n 1.                                        (12)

Its integral representation has bottom factor A(U_0), full spatial factors
A(U_t)^2 for 1<=t<n, terminal factor A(U_n), and temporal factors
k(U_(t-1),U_t). Equivalently this is the OPEN Wilson slab after temporal
gauge fixing, with the bottom spatial field fixed and a free top cap.
One recursively changes variables using the temporal links, with identity
gauge transformation at the bottom; product Haar has unit Jacobian and the
integrated temporal gauge volume is one. All spatial holonomies remain.
There is no deletion of a spatial plaquette or of the terminal half factor.
A periodic time circle would retain a temporal holonomy twist: (12) is NOT
that gauge fixing. The open-slab Perron limit is the construction used here.

For fixed Gamma, lambda_0^(-n) psi_n -> <psi,1> psi uniformly. This follows
from the inherited compact Perron theorem in L2 followed by one continuous
integral-kernel application. No volume-uniform convergence rate is assumed.
Let R_n=psi_n/A(U_0). Changing one bottom link e from U_e to U'_e changes
only the first temporal factor and inserts the actual local function

    H_e(V)=beta [w(U'_e V_e^dagger)-w(U_e V_e^dagger)],
    |H_e|<=2 beta,       delta_(e,1) H_e<=4 beta.                   (13)

Here delta_i is the oscillation on one free link with all others fixed.
The source in (13) touches exactly ONE first-layer spatial link. This
one-site support is available because (12) was derived, not because a
projector or a temporal boundary sector was silently dropped.

For distinct boundary edges e,f, interpolate the two inserted log weights
by s H_e+t H_f, 0<=s,t<=1, in the normalized actual slab measure rho_(s,t).
Differentiating its finite partition function gives the exact identity

    Delta_e Delta_f log R_n
       = integral_0^1 ds integral_0^1 dt Cov_(rho_(s,t))(H_e,H_f).   (14)

All bulk spatial interactions and all slab depths are retained. The
interpolation affects only one-body boundary fields, so it changes no
free-variable interaction bound. At arbitrary beta, (14) is an identity,
but the covariance has not thereby been estimated at long distance.

## 4. Derive the small-beta boundary estimate and physical Doob contraction

For completeness the comparison tool is stated with its hypotheses. In a
finite product space with strictly positive continuous Gibbs density, let
C_ij bound the total-variation change of the conditional at i when j changes.
If a symmetric nonnegative majorant C has row sum q<1, write D=(I-C)^(-1).
Then

    |Cov(f,g)| <= (1/4) sum_ij delta_i f D_ij delta_j g.             (15)

A short proof uses the single-coordinate conditional-expectation generator
L=sum_i(E_i-I). Its semigroup has oscillation bound
 delta(P_s g)<=exp[s(C^T-I)] delta(g), obtained first by a positive Euler
step and then a limit. Integrate
 -d/ds mu[f P_s g]=sum_i mu[Cov_i(f,P_s g)]
from zero to infinity. Conditional covariance is at most one quarter the
product of the two oscillations, and q<1 gives uniform convergence to the
mean and integral exp[s(C-I)] ds=D. The same semigroup argument, comparing
two conditional specifications with defects b_i in total variation, gives

    |mu f-nu f| <= sum_ij delta_i f D_ij b_j.                       (16)

The log-likelihood lemma used to bound C is elementary: if the range of
a log density ratio is at most L, the two normalized probabilities have TV
distance at most tanh(L/4)<=L/4. Normalization is included in this bound.

Apply this to the open temporal-gauge slab. A spatial link is in four
spatial plaquettes, each with three other links, and has at most two
neighboring time copies. Each common plaquette or temporal pair has mixed
log oscillation at most 4 beta. Thus one may take

    C^+_((e,t),(f,s))
      = beta [m_ef 1_(t=s) + 1_(e=f) 1_(|t-s|=1)],
    q_+=14 beta,             D^+=(I-C^+)^(-1),                     (17)

with rows/columns restricted to the half-slab. Here m_ef counts common
spatial plaquettes for DISTINCT edges and has row sum 12. Top half-spatial
weights only reduce the influence. In the infinite half-time graph use the
convergent Neumann series; its row sum is at most 1/(1-14 beta). Finite-slab
entries are bounded by these entries. All spatial volumes and all bottom
fields obey the same majorant when beta<1/14.

Equations (13)-(15), followed by the finite-Gamma Perron limit, yield

    |Delta_e Delta_f log(psi/A)| <= 4 beta^2 D^+_((e,1),(f,1)),
    |Delta_e Delta_f log psi|
      <= 2 beta m_ef+4 beta^2 D^+_((e,1),(f,1)).                   (18)

If the two first-layer links have distance d in the graph of (17), the
resolvent entry is at most (14 beta)^d/(1-14 beta). This is an actual bound
on the spatial dependence of ground-state ratios, not just (3). The bound
is uniform in half-slab depth, external bottom fields and spatial volume.
It remains a small-beta result.

The physical Doob kernel is

    P_0(U,dV)=K(U,V) u(V) dV / integral K(U,W) u(W) dW.             (19)

Since u is invariant, for EVERY invariant observable F its expectation
under (19) equals its expectation under

    P_hat(U,dV)= k(U,V) u(V) dV / integral k(U,W) u(W) dW.          (20)

This follows by changing V to h.V in both numerator and denominator of
(19); it is not a replacement on gauge-variant observables. In fact
T_hat psi=lambda_0 psi and P_hat is reversible under pi=psi^2 dU.
The physical restriction of P_hat is exactly P_0, and its complete
invariant space is the one in the target. Gauge projection has thus been
accounted for before using a simpler conditional kernel.

For an output block B, the ACTUAL conditional in (20), at fixed output
exterior Z, is

    P_hat(dV_B | Z,U) proportional to
       A(V_B,Z) psi(V_B,Z)
       exp[beta sum_(e in B) w(U_e V_e^dagger)] dV_B.              (21)

All factors in (21) matter. There is no substitution of the bare Wilson
heat-bath law for this physical-time kernel. For distinct output links,
(18) and the additional log A give the uniform conditional majorant

    C^step_ef = beta m_ef+beta^2 D^+_((e,1),(f,1)),  e!=f,
    C^step_ee = 0,
    Q(beta)=12 beta+beta^2/(1-14 beta).                            (22)

The actual pi-block conditional similarly has majorant row at most
12 beta+2 beta^2/(1-14 beta). These estimates precede any comparison or
contraction; local finite-energy bounds alone would not give them.

Changing the INPUT link e of (20) changes only a one-body output weight at
e. Its conditional TV defect b_i is at most beta 1_(i=e). Applying (16) to
the complete output measures, and summing over input edges, gives

    sum_e delta_e(P_hat F)
      <= r(beta) sum_i delta_i F,
    r(beta)=beta/[1-Q(beta)].                                    (23)

For 0<beta<=1/32, all denominators are positive and

    q_+ <= 7/16,       Q <= 217/576,       r <= 18/359 < 1.         (24)

These constants are dimensionless and independent of N and Gamma. The
spatial comparison keeps the entire exterior and all spatial holonomies.
No tensorization of unestimated ground-state factors occurred.

Iterating (23), for any real bounded F on the finite spatial configuration
space, yields the physical-time covariance bound

    |Cov_pi(F,P_0^n F)| <= (1/4) [sum_e delta_e F]^2 r(beta)^n     (25)

when F is invariant. This uses the range covariance bound and
osc(g)<=sum_e delta_e g. Centering is with respect to the actual pi.
P_0 is the physical transfer divided by its Perron eigenvalue, so n in
(25) counts Euclidean time slices; it is not the auxiliary heat-bath time
s used only to prove (15)-(16). Continuous finite-volume eigenfunctions
have finite oscillation sums. Positivity and the spectral theorem therefore
give on the COMPLETE physical finite-volume Hilbert space

    spec(H_Gamma) subset {0} union [-log r(beta)/a,infinity),
    H_Gamma=-a^(-1) log(T/lambda_0),    ker H_Gamma=span{psi}.       (26)

Combining (11) and (26), its nonvacuum threshold lies in the nonempty finite
interval [-log r(beta)/a,-log eta_C(beta,N)/a]. The bound (26) is the new
consumer of (18)-(23); it is not an assumption made to estimate the ratios.

## 5. Fixed-spacing thermodynamic limit, full observables and finite energy

This section keeps beta in (0,1/32] and a>0 FIXED. The original unfixed
four-dimensional Wilson measure has the usual free-link row bound 18 beta:
six plaquettes per link, with three other links per plaquette. Strict
positivity, compactness and (16) construct its unique infinite-volume
Gibbs state. The influence of changed boundaries outside distance R tends
to zero as a Neumann-series tail, uniformly in their values. Free caps,
spatial tori tending to Z^3, and successive long open-time slabs therefore
have the same local limit. The finite-coordinate boundary comparisons are
in total variation, so bounded measurable local expectations also converge.
No infinite temporal circle was gauge fixed.

All bounded gauge-invariant local observables, including products of
intersecting loops and local spin networks, pass to this limit. There is
no restriction to separated plaquettes. Continuous invariant local functions
are uniformly approximated by gauge-averaged Peter-Weyl polynomials. Rational
real and imaginary coefficients supply a countable dense family; bounded
measurable local functions belong to its L2 closure. Finite products remain
local. A finite set of
bounded sources has an entire finite-volume generating function, locally
uniformly bounded by exp(sum |J_i| ||F_i||_infinity). Its local limits and
all finite source derivatives are therefore the actual Gibbs expectations.
No source-only constant or conditional covariance remainder is removed.
This concerns the original Wilson measure, not an inverse soft RG map.

Let pi_infinity be its spatial-slice marginal on the full spatial
configuration space. Conditioning on all spatial links on one time slice
separates the past and future interactions. Uniqueness of the corresponding
half-space specifications, uniform even in the fixed slice data, makes the
two conditional halves independent. Consequently the slice process is a
stationary reversible Markov chain with transition P_infinity. This also
follows by the locally uniform half-slab conditional comparisons above.
For invariant local F,G,

    <F,P_infinity^n G>_pi = lim_(Gamma) <F,P_0,Gamma^n G>_pi,Gamma.  (27)

Positivity of the finite transfer passes on this dense set, so P_infinity
is a positive self-adjoint contraction. Equation (25) passes to the limit
with its same local prefactor, without taking n->infinity first. By the
spectral measure argument on the dense invariant cylinder family,

    P_infinity|_(1 perpendicular) <= r(beta) I.                    (28)

Injectivity in infinite volume is proved separately in the
[finite-boundary tilt supplement](checks/massgap_block_injectivity.md).
It constructs the unprojected half-space kernel Q_U for every bottom field
and derives its exact finite-block tilt by uniqueness. The limiting pi
conditional density bounds, a countable Fubini full-measure set, strict
Peter-Weyl multipliers on each block, and L1 martingale convergence then
prove Q injective on all of L2(pi). Its restriction P_infinity is therefore
injective on the entire invariant slice space. Finite-volume injectivity
and the single witness (29) are not used as substitutes for this proof.

Construct the physical Hilbert space using reflection THROUGH A TIME LINK. A positive
half-space observable, after conditioning on the first positive spatial
slice, has a bounded invariant boundary function f. Its reflected norm is
<f,P_infinity f>_pi. Boundary cylinder functions themselves are allowed and
dense in the invariant slice L2 space. Thus the full OS completion is
canonically the closure of the range of P_infinity^(1/2), via
f -> P_infinity^(1/2) f. The injectivity argument shows that this closure is
the ENTIRE invariant slice Hilbert space. This is the ordinary
reflection null-space quotient for the full positive-time local algebra,
not a selection of one observable sector. Higher positive-time products
are included by the same Markov conditioning. Spatial gauge averaging on
compact finite supports gives density of invariant cylinders in the full
invariant slice space; temporal link observables are included before that
conditioning.

On this OS Hilbert space the physical time transfer is unitarily equivalent
to P_infinity on the entire invariant slice space. Its spectral logarithm defines
a densely defined nonnegative self-adjoint H at physical step a, and
exp(-t H) is strongly continuous for all real t>=0. This continuous-time
interpolation does not assert restoration of four-dimensional rotations.
Equation (28) gives a unique vacuum and gap at least -log r(beta)/a.

The centered local plaquette satisfies, by (11) and local convergence,

    <F,P_infinity F>_pi >= eta_C(beta,N)>0,
    <F,F>_pi <= 1,              <F,1>_pi=0.                        (29)

Its physical OS vector is therefore nonzero. Its spectral measure has
positive transfer support, and the supremum of that support is at least
eta_C. Combined with (28), this proves that the physical nonvacuum spectral
threshold is finite and positive, with

    -log r(beta)/a <= inf spec(H|_(Omega perpendicular))
                   <= -log eta_C(beta,N)/a < infinity.            (30)

In particular the construction is not a one-dimensional vacuum Hilbert
space at this fixed spacing. Local physical vectors have a common
positive decay rate; after spectral reconstruction their bounds hold for
all t>=0 with their Hilbert norms as prefactors. The construction covers
all invariant local products, not just the witness used to show the
excited space is nonzero. It is still a fixed-spacing lattice theory.

## 6. Checks and exact scope of the construction

Predeclared criteria are in [massgap_block_criteria.md](checks/massgap_block_criteria.md).
The [runner](checks/massgap_block_exact.py), [results](checks/massgap_block_results.json)
and [manifest](checks/massgap_block_manifest.json) record the exact arithmetic,
finite geometry, tensor inequalities, slab identities and SU(2) quadrature
controls. The final author run passes 108/108 checks, including 22 mutation
controls. They also mutate the actual implemented operators. The [injectivity supplement checks](checks/massgap_block_injectivity_results.json)
pass 23/23 additional finite tilt and signed-measure controls. Numerical
checks diagnose algebra and normalization; they do not prove (18), an
infinite-volume theorem, or any continuum estimate. Independent review is
pending and the source status is not an audit verdict.

The local inequalities have per-edge/block scope and constants involving
beta,b,p_B. The strong-coupling contraction has lattice-wide finite-volume
scope and is uniform in spatial volume and slab depth at FIXED beta,a.
Its thermodynamic endpoint concerns the full invariant local algebra.
Neither scope includes removal of the regulator on the ultraviolet
trajectory. No MG0-MG5 target row, global no-go or landing packet is closed.

## 7. Attempted continuations and the first remaining inequalities

Two distinct mechanisms were pursued. The all-beta local rank-one route
produces (11) because the exterior positive kernel cancels; it gives a
finite-energy upper bound and does not control decay. The actual
half-slab/Doob route produces (26)-(30), with a physical-time contraction,
because the boundary covariance in (14) is bounded in the small-beta
region. At general beta the exact identities remain valid but the
Neumann-series estimate (17) is unavailable. Failure of that majorant is
not a lower bound on the true response and not an impossibility theorem.

The first missing object for a large-beta local comparison is now precise:
a uniform, spatially summable bound on

    Cov_(rho_(s,t;Gamma,n,U))(H_e,H_f),                            (31)

for the ACTUAL Wilson half-slab, every depth n, spatial volume Gamma,
bottom field U and interpolation s,t. Its available strong-coupling bound
is 4 beta^2 D^+_((e,1),(f,1)). The physically sufficient block version must
control the corresponding actual conditional transition sensitivity on
blocks of a fixed physical radius, while retaining their all-sector
boundary data. Finite-energy ratio (3) alone provides no spatial tail.
Neither a block-minimum covariance gap nor a heat-bath spectral gap
substitutes for this physical-transition calculation.

For exact RG transport to the endpoint, an actual producer would have to
identify the integrated coarse action and its time transfer at a fixed
physical step ell, control its deviations from the endpoint class, and
transport the complete fine local source algebra including the source-only
and conditional terms in
[MASS_GAP_CONSTRUCTION_ASTRA.md, equations (21)-(23)](MASS_GAP_CONSTRUCTION_ASTRA.md).
This unit has not shown that the exact S4' output is a small-beta Wilson
action or even has the nearest-time factorization (1). An assumed
crossover would import the missing dynamics.

Finally, fixed beta and a->0 make the lower bound in (30) diverge as 1/a.
The finite-energy witness (29) is at a shrinking one-step time. The two
facts preclude presenting this endpoint as the requested nontrivial
continuum trajectory. The still-required estimate remains

    |C_F^(a,R)(t)| <= A_F exp(-m_* t),
    t_F <= t <= T_safe(R),

with m_*>0 in physical units, A_F and t_F independent of cutoff and volume,
T_safe(R)->infinity on the SAME existence hierarchy, and a nonzero finite-
energy continuum witness. No derivation of that estimate or that witness
has been supplied here. The endpoint is a concrete input for a future
transport construction, not a replacement target.
