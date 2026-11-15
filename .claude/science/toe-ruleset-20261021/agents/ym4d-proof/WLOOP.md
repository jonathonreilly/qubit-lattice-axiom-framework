# WLOOP — an extended-observable target for the Yang–Mills construction

Author: Codex. Research note for `briefs_q/WLOOP/AUTHOR.md`.
**Verdict: UNDECIDED as a replacement for the full local-field target;
UNDECIDED for a completed combined theory.** Bounded loops offer a real
moment-bound advantage and a useful conditional witness. They do not remove
the common-algebra, continuum covariance, physical-identification or infrared
obligations. Keeping the local core and investigating a bounded spatial-loop
extension is the proposed next route, not a claim that its estimates exist.

PROVEN means the displayed mathematical implication is proved below;
ARGUED means a proposal; OPEN marks an unsupplied estimate or identification.
These labels do not confer retained status. Independent review and source
identities are recorded in [WLOOP_LOG.md](WLOOP_LOG.md) and
[checks/wloop_sources.json](checks/wloop_sources.json).

## 1. Target, source boundary and observable choices

ASSEMBLY55 §3 **N0** asks for one E(4)-covariant gauge-invariant observable
system on R^4, with OS0–OS3 and a specified non-free identification. Its §4
**N6 (ALG)** requires the regularity, positivity, symmetries and witness to
refer to that SAME system. `MASS_GAP_TARGET.md` additionally requires a local
physical theory, a unique vacuum and a positive finite physical mass threshold
with nonzero excited space. Choosing another observable family does not change
that expanded target. Here N>=2, the group is SU(N), and the finite Wilson
regulator and any tuned trajectory are supplied premises.

For an oriented closed lattice contour C, set

    w_a(C)=N^(-1) Tr product_(e in C) U_e,
    w_a(C)^*=w_a(C^(-1)),             |w_a(C)|<=1.           (1)

The product follows the path, including repeated edges. A change of base
point conjugates its holonomy; reversal takes its inverse. These facts prove
gauge invariance, the star identity and the bound, since the holonomy is
unitary. For N>2 retain complex traces and their conjugates, or both real
components; replacing all traces by their real parts changes the algebra.
Degenerate retraced loops are allowed but can equal 1 and supply no signal.

There are four different choices, not one interchangeable loop variable:

| Choice | Definition and actual support | Immediate advantage | Remaining issue |
|---|---|---|---|
| Thin renormalized loops | Specified cutoff contour approximation and perimeter/cusp/intersection renormalization; intended support is the contour | Compact geometric support can match an OS cone | Nonperturbative renormalization and all required products OPEN |
| Four-dimensional flowed loops | Holonomy of the Wilson-flowed bare links at fixed physical flow time s>0 | Bound (1) persists at every cutoff | Dependence reaches both time halves; RP is not inherited from contour location |
| Spatially flowed loops | Spatial holonomy after three-dimensional flow in its own time slice | Bound (1), exact aligned temporal half-support | Spatially nonlocal; sharp-time identification and arbitrary rotations need work |
| Fixed-resolution block loops | Holonomy of specified deterministic or soft block variables | Bounded finite-resolution functions; existing compactness machinery | Identify the chosen block law, support and continuum physical observable; soft noise cannot be counted as interaction |

Smooth curves alone are not a UV regulator. Smearing a loop's center is not
the same as smoothing the connection before taking its holonomy. Nor is the
coupling RG flow in FLOW.md the parabolic Wilson/gradient flow of a gauge
field. The latter two uses of “flow” are kept separate below.

**Loop test space, proposed contract.** Start with compact, piecewise C^2
contours, with explicitly bounded length, curvature on smooth pieces, number
of corners and corner angles on each compact label set. Use smooth embedded
contours first; intersections and winding contours are separate strata. A
label includes representation, orientation, contour shape, center, and any
positive flow time or regulator. A finite-dimensional chart q -> C_q and a
chosen smooth chart density define

    W_a(f)=integral f(x,q) w_a(x+C_q) dx dq.                 (2)

Finite sums of such charts and compact smooth tests specify a concrete
smearing operation; no nonexistent Lebesgue measure on all loop space is
assumed. At finite a, the approximating paths and measurable rounding rule
must be fixed. Their limiting independence from that rule is an estimate,
not a definition. Choose a separable family of charts, their reflected
copies and motions; the completion and determining family are part of
H_reg^W. Products are words of loop variables and adjoints. Any trace
relations imposed must actually hold for the chosen, possibly renormalized,
variables. Raw Mandelstam identities need not retain their original form
after separate renormalization of different contours.

For a compactly supported local regularization, its localization set is the
union of ALL underlying field supports appearing in (2), not its set of
centers. Four-dimensional heat flow generally has support all of spacetime;
full spatial flow has support the whole slice. A temporal Polyakov loop on a
time circle winds through both halves. A spatial Polyakov loop at positive
time can belong to the positive half but wraps the spatial torus. These last
two observables have different roles.

## 2. Loop versions of OS0–OS3 and exact cutoff statements

Use the convention OS0=regularity, OS1=Euclidean covariance,
OS2=reflection positivity, OS3=bosonic permutation symmetry, as in OSLEAF55.
No clustering axiom or unique vacuum is added without a proof.

- **H_reg^W / OS0 (OPEN for the desired physical continuum family).** All
  required joint loop and mixed local-field functionals converge on ONE
  countable determining family along ONE cutoff/volume sequence, with
  uniform estimates extending them to the declared test completion. For a
  distributional route require a specified growth bound
  `|S_(r,n)(F)|<=A^(r+n)((r+n)!)^b p_(c(r+n))(F)` on mixed words of r local
  insertions and n loops, with fixed A,b,c and a defined seminorm including
  loop labels. Its suitability for reconstruction is a separate match.
  A bounded-algebra route uses a state plus continuity of
  `g -> omega(A alpha_g(B) D)` for all algebra elements, instead. The
  unflowed e-variables retain OSLEAF55's ordered/flat-test domain: this does
  not create an ordinary moment of e(f)^2. For thin loops specify allowed
  intersection/contact strata or prove their renormalized extension.
- **H_Euc^W / OS1 (OPEN).** The action sends C to RC+b, s to s, and a
  spatial-flow normal n to Rn. Require invariance on ALL joint words,
  continuity in this action, and vanishing lattice symmetry defects on a
  dense group/test family. Translation and orientation smearing can supply
  continuity in their test variables, but neither supplies state invariance
  nor a nontrivial limit. A fixed spatial-slice family has only its stabilizer
  subgroup until the differently oriented copies and their joint laws exist.
- **H_RP^W / OS2.** For theta(t,x)=(-t,x), define
  `Theta F(U)=overline{F(theta U)}`. On generators this is
  `Theta w(C)=w((theta C)^(-1))`. Require
  `q(F,F)=omega((Theta F)F)>=0` for every finite positive-half word sum;
  membership uses its actual support. Complex conjugation occurs once.
- **OS3 and reality.** Products of classical trace variables commute, so
  simultaneous permutations of labels and tests leave their moments
  unchanged. Conjugation reverses each contour. These identities pass to
  any common moment limit; they do not prove Minkowski locality at the
  centers of extended objects.

**Lemma W1 — bounded moments and subsequences (PROVEN).** For any finite
list of bounded loops, including fixed-positive-flow loops, and any joint
test F in the chart variables,

    |E product_i w_a(C_i)^(epsilon_i)|<=1,
    |S_(a,n)(F)|<=||F||_1,                                 (3)

where epsilon denotes either the variable or its conjugate, not a negative
power of the trace. The same bounds hold conditional on any coarse field
under a positive probability kernel. This follows by integrating the
pointwise bound. For centered traces replace 1 by 2^n. All joint laws of
a countable list are supported on the product of closed unit disks. That
product is compact: successive coordinate extraction and a diagonal
subsequence give convergence in the metric
`sum_l 2^(-l) min(1,|z_l-z'_l|)`. For the measures, separately enumerate
the countably many monomials in coordinates and conjugates and diagonalize
their bounded expectations. Every polynomial expectation then converges,
is bounded by its supremum on the product, and is positive on P^*P.
Normalization and this bound extend the limit to a state on the uniform
closure of the cylinder-polynomial algebra. No moment-uniform-
integrability problem occurs for these bounded coordinates. This rederives
the compactness mechanism of EXISTENCE X-ALG/X-FLOW, without importing RG
estimates. It does not prove continuity in unsmeared curve labels, E(4)
invariance, uniqueness, nontriviality or identification with continuum
holonomy. It also gives no bound for unbounded renormalized traces or mixed
e-products merely from (3). ∎

**Lemma W2 — site RP, including loops and mixed cutoff fields (PROVEN).**
Use an even periodic time lattice and the geometric half-arc [0,T/2].
Keep distinct periodic edges distinct even at temporal extent two, as
required by HRP §§1,3.2. Let B be spatial links on BOTH fixed planes and
X_+,X_- the other links in the two halves. The nearest-neighbor Wilson
action with reflection-paired real coefficients splits as

    S=S_boundary(B)+S_+(X_+,B)+S_+(theta X_-,B).
    Z q(F,F)=integral e^(-S_boundary(B))
        |integral F(X_+,B)e^(-S_+(X_+,B)) dX_+|^2 dB>=0.    (4)

Every plaquette is in one closed half or on a boundary, which proves the
split; invariance of product Haar measure proves the second line by
reflecting X_-. Every finite-cutoff loop polynomial supported there is
bounded and covered. So are compact positive-time e-tests with their
entire clover stencil in that half, and spatial-flow loops on its slices.
No extra loop term has been added to the action. Formula (4) proves the
site version needed here; the distinct link-reflection proof and its
nonnegative crossing couplings are HRP §3.1's separate result.

If gamma is an open half-path with endpoints on the reflection boundary,
write M=Hol(gamma). The reflected closed contour formed from theta gamma
in reverse and gamma has trace
`Tr[Hol(theta gamma)^* Hol(gamma)]`.
Its expectation is `sum_ij E[(Theta M_ij) M_ij]>=0` by (4).
This explains the familiar crossing-loop positive kernel. It does not put
an arbitrary contour crossing the plane into the positive-half algebra;
the half-path matrix elements, though not gauge invariant individually,
are legitimate functions in the stronger finite-lattice RP statement. ∎

**Lemma W3 — renormalization and limit passage (PROVEN implication).**
Suppose each renormalized half-word is an actual half-supported function
F_a, with the reflection/conjugation of that same function on the other
side. Its Gram matrix is positive by W2. Linear renormalization of a finite
basis replaces Q by `Z_a^* Q Z_a`, also positive. If every needed entry
converges along one common sequence, each finite quadratic form remains
nonnegative. A continuous test-space bound then extends it from dense
tests. Thus support-preserving renormalization is compatible with RP;
diverging Z_a does not by itself invalidate it, but destroys the simple
bound (3). Independently subtracting contact terms from a two-loop kernel
without realizing a common half-observable map is not this operation and
need not preserve positivity. ∎

## 3. Renormalization, smearing and the flow-support issue

The following UV analysis diagnoses required estimates. It is not an
all-orders nonperturbative SU(N) renormalization theorem.

**Library calculation W4 (PROVEN in a regulated Gaussian model).** For a
real centered Gaussian connection and a closed current J_C, let
`X_C=integral_C A`. The elementary one-dimensional Gaussian integral gives

    E exp(iq X_C)=exp(-q^2 Q_epsilon(C)/2),
    Q_epsilon(C)=integral_C dx_mu integral_C dy_nu
                         D_epsilon,mu,nu(x-y).             (5)

On an arclength-parametrized smooth arc in four dimensions, use the
short-distance regulator `D_mu,nu(z)=delta_mu,nu/[4 pi^2(|z|^2+epsilon^2)]`.
The near-diagonal tangent contraction is 1+O(u^2), and the squared distance
is u^2+O(u^4). The leading term per unit length is
`(4 pi^2)^(-1) integral_(-delta)^delta du/(u^2+epsilon^2)
=1/(4 pi epsilon)+O(1)`.
Thus even a smooth curve has a length/epsilon divergence in this model.
At two rays meeting at a corner, the cross integral has a homogeneous
degree-minus-two denominator in the two ray parameters. Polar scaling
gives an angular coefficient times `integral d rho/rho`; after comparison
with the smooth continuation this is the possible angle-dependent cusp
logarithm. This identifies the geometry and does not calculate a general
SU(N) cusp coefficient. Translating or rotating the whole contour before
averaging does not remove its same-contour diagonal. ∎

For an unsmoothed SU(N) program, specify a perimeter factor, a cusp factor
for each fixed corner, and a mixing prescription for intersections or
products that share segments. These are OPEN nonperturbative constructions
here. Intersection mixing is already motivated algebraically: with Hermitian
generators `Tr(T^a T^b)=delta_ab/2`, completeness on traceless matrices gives

    sum_a T^a_ij T^a_kl=(delta_il delta_jk
                                      -delta_ij delta_kl/N)/2. (6)

Indeed the right side is one half the matrix kernel of the orthogonal
projection `X -> X-Tr(X)I/N`; expansion in the orthonormal basis
`sqrt(2) T^a` gives the left side. A contraction between two segments
therefore reconnects color indices as well as preserving the original
routing. This establishes why a single scalar counterterm must not be
assumed to handle every intersecting loop. Brandt, Neri and Sato's
[perturbative treatment](https://doi.org/10.1103/PhysRevD.24.879) provides
attribution for this renormalization program, not a missing proof here.

Rounding a macroscopic cusp removes that cusp while leaving the line
self-energy. A lattice staircase approximation can create a growing
number of microscopic corners: convergence cannot be inferred from an
estimate for one fixed polygon. Required controls include the approximation
rule, contour deformation, corner proliferation and any mixing matrix,
uniformly along the chosen continuum trajectory. Smearing contour shapes
does not automatically cancel a perimeter factor of each member.

At fixed s>0 the cutoff Wilson flow is a smooth ODE on a finite product
of compact groups. Its vector field is smooth and complete; invariance of
the action and metric, and uniqueness, prove gauge and lattice-symmetry
equivariance. Its outputs remain unitary, proving W1 for flowed loops.
Continuum smoothing/renormalization is a method suggested by
[Lüscher](https://arxiv.org/abs/1006.4518),
[Lüscher–Weisz](https://arxiv.org/abs/1101.0963) and
[Lohmayer–Neuberger](https://arxiv.org/abs/1110.3522).
Their perturbative or proposed continuum descriptions are not used as a
construction of this nonperturbative law.

**Library calculation W5 — time smoothing does not generally preserve RP
(PROVEN counterexample to automatic inheritance).** Start with the
reflection-positive Gaussian time covariance `C_0(t)=e^(-m|t|)/(2m)`, m>0.
For positive times its reflected kernel is
`C_0(t_i+t_j)=e^(-mt_i)e^(-mt_j)/(2m)`, a positive rank-one matrix.
Heat-smear in time by s>0. The resulting covariance is

    C_s(t)=integral_R dp/(2 pi)
                 exp(ipt) exp(-2s p^2)/(p^2+m^2).

It is smooth and even, with a=C_s(0)>0, C_s'(0)=0 and
`b=C_s''(0)=-integral dp/(2 pi) p^2 exp(-2s p^2)/(p^2+m^2)<0`.
At t_1=epsilon,t_2=2epsilon, Taylor expansion gives

    det [C_s(t_i+t_j)]_(i,j=1,2)=a b epsilon^2+O(epsilon^4)<0. (7)

This is a genuine negative reflected direction. Bounded functions do not
repair it: for the smoothed Gaussian field Y, the reflected correlation
matrix `E[sin(lambda Y(-t_i)) sin(lambda Y(t_j))]` is
`lambda^2 C_s(t_i+t_j)+O(lambda^4)`.
Gaussian moment bounds justify the expansion. At the fixed small epsilon
in (7), its determinant is `lambda^4 det C_s+O(lambda^6)<0` for small
lambda. This is a bounded Gaussian counterexample, not a theorem that
every Yang–Mills flowed Wilson loop violates RP. ∎

The linearized curvature flow has the positive heat kernel with spatial
and temporal tails. Thus a contour geometrically above zero need not be a
function of the positive bare links after four-dimensional flow. This
matches EXISTENCE **X-FLOW-NL**, which correctly distinguishes support
failure from proof of RP failure. If a proposed localization gives a
half-function G_a with `||F_a-G_a||_2<=delta_a` in a reflection-invariant
probability state, Cauchy–Schwarz and W2 yield

    q(F_a,F_a)>=-2 delta_a ||G_a||_2-delta_a^2.              (8)

Expand F_a=G_a+(F_a-G_a) to prove (8). To recover exact limiting RP one
needs the right side to tend to zero for every required polynomial.
A bound `delta_a<=C exp(-c d^2/s)` at FIXED distance d and FIXED physical
s is only a small constant, not an error vanishing as a->0. A joint s->0
localization/renormalization limit, compact support smoothing, or a direct
positivity theorem remains possible, with its own estimates.

Three-dimensional flow avoids temporal tails for a spatial loop on an
aligned slice, so (4) holds. It still has spatial tails. Compact support
of the center test does not make it a compactly localized field, and a
tilted infinite slice has points of both signs of the original time
coordinate. Covariance in the normal label alone does not make all such
observables admissible in one fixed positive-half cone.

## 4. Reconstruction: what extends, what must replace the library

**Lemma W6 — bounded-loop Hamiltonian reconstruction (PROVEN implication).**
Assume a normalized positive state omega on the bounded loop algebra,
an isometric Euclidean action preserving it, a support-defined A_+,
RP, and continuity of all group-transformed pairings. Define
`q(F,G)=omega((Theta F)G)`, quotient by its null space and complete to H_W.
The vacuum is [1]. Cauchy–Schwarz for the positive form makes the quotient
legitimate. Positive-time translation T_t preserves A_+. Invariance and
reflection covariance give

    q(F,T_t G)=q(T_(t/2) F,T_(t/2) G)=q(T_t F,G).

Also `|q(F,T_u F)|<=||F||_infinity^2` for all u>=0 by ordinary state
positivity and the isometric action. Iterated Cauchy–Schwarz gives

    ||[T_t F]||<=||[F]||^(1-2^(-k))
                         ||[T_(2^k t)F]||^(2^(-k)).

The final norm is uniformly bounded. Let k->infinity; null vectors are
preserved and T_t induces a contraction P_t. The first identity gives
self-adjointness and `q(F,T_t F)>=0`. Continuity of pairings gives strong
continuity from
`||[T_t F-F]||^2=q(F,F)-2 Re q(F,T_t F)+q(F,T_(2t)F)`.
The semigroup law follows from translations. The spectral theorem then
gives `P_t=e^(-tH)`, H>=0; explicitly P_1 has no kernel by repeated positive
square roots and strong continuity at zero, so H=-log P_1, first on
dyadic times and then all times. Spatial motions preserve q, giving
strongly continuous spatial unitaries. This is the loop version of the
OSLEAF55 REC(a)–(c)/REC_LIB L-HILB argument. It proves neither Lorentz
covariance nor local Wightman fields by itself. ∎

**Lemma W7 — a bounded boundary extension (PROVEN implication).** Suppose
the original ordered e-test RP forms converge, with their stated continuous
extension bounds. Adjoin a countable algebra of bounded boundary spatial
loops, |b|<=M_b independently of cutoff, closing under products, star and
rational linear combinations. In (4), boundary b factors out of the inner
integral, so for any finite mixed half-word sum F,

    q_a(bF,bF)<=M_b^2 q_a(F,F).                             (9)

Initially this bounds each b times an e-test; Cauchy–Schwarz bounds every
mixed Gram entry and finite sum. Diagonalize these countably many entries
together with the e-core entries and pure-loop moments. Positivity and (9)
pass to the limit. The bounds extend in the e-test topology. Completing
the quotient embeds H_e isometrically in H_mix and realizes boundary b as
a bounded multiplication operator of norm at most M_b. Its vacuum vector
has `||[b]||^2=lim E|b_a|^2`, and
`<Omega,[b]>=lim E b_a`.

All those limits are genuine bounded mixed/subsequence limits; no delta
test of an e-distribution was used. This sharp boundary extension need
not yet be the limit of positive-time translated continuum vectors:
`||[T_epsilon b]-[b]||->0` and the common action are additional inputs.
Full mixed words away from the boundary, rotations, compact spatial
localization, and equality H_mix=H_e are not supplied by (9).
Unlike W_T0's magnetic energy, bounded loop traces require no new
MOM2-B-type bound for their pure second moments. ∎

**REC_LIB/REC_CONT interface.** Their actual current producer is completed
abstractly, subject to E0'–E3, reality and normalization on one hierarchy
of finitely many real scalar/Cartesian tensor POINT fields. REC_LIB §15
has a finite tensor reflection/Wick dictionary; REC_CONT §§1,10,11 keeps
that class. A fixed translated loop is not a scalar point field: rotations
change its contour, its support is extended, and an ordered center need
not order its entire support. Loop intersections are not just center
coincidences. The infinite shape/orientation family is not the printed
finite tensor representation. Therefore no verbatim application of
REC_CONT's point-tube/locality conclusion is justified. This is a domain
mismatch of that theorem, not a nonexistence theorem for loop theories.

Two possible replacements remain OPEN here:

1. **A Euclidean net route.** Build algebras A(O) generated by genuinely
   O-supported bounded observables, with isotony, locality, full covariant
   action, invariant RP state and continuous three-factor group matrix
   elements. Establish a nontrivial, suitably localized time-zero algebra,
   and prove the analytic rotation/domain and causal-commutativity steps
   which reconstruct its Minkowski net. Schlingemann's
   [C*-algebraic reconstruction](https://arxiv.org/html/hep-th/9802035v1)
   explicitly treats extended variables and distinguishes regularity
   (Definition 2.3) from the nontrivial time-zero condition (TZ). It is a
   method candidate, not a theorem imported to close this lane. W6–W7
   rebuild only its elementary Hilbert/boundary ingredients. Local
   generation and equality to the desired physical theory need separate
   checks; a net need not already supply the required point-field hierarchy.
2. **A local-core route.** Keep the e/tensor hierarchy and its existing
   REC_LIB/REC_CONT theorem, prove the common mixed extension of W7 with
   its translations and covariances, and either realize loops as operators
   in that same local theory or reconstruct local fields as controlled
   shrinking-loop limits. For example the classical smooth-connection
   expansion of `1-Re w(C_ell)` starts at order ell^4 for a small planar
   contour, but extending this to a random YM field needs normalization,
   subtractions and ALL mixed distributional remainder estimates. A
   classical expansion is not an operator-product theorem. No source
   proves this limit or cyclic completeness here.

The gauge-invariant loop-axiom work of Ashtekar and collaborators
([two-dimensional construction](https://arxiv.org/abs/hep-th/9605128)) is
another formulation precedent; its dimension and measure are not those of
this task. No two-dimensional estimate is used for four-dimensional YM.

## 5. What the existing RG/source producers actually deliver

The table records the inspected sources' stated domains. It does not
certify all their upstream arguments or every historical status label.

| Producer and locator | Usable scope for loops | Missing estimate/identification |
|---|---|---|
| HRP §§3–4, bare-marginal identity | Exact finite Wilson half-link RP applies to bare half-supported loops; normalized auxiliary kernels integrate to 1 | Continuum joint limits and support of any smoothed/block maps |
| SRCCD55 §3.2–3.3, SRC-κ/SRC-poly | Sources for e, plus specified local insertions; conditional bounds on separated local fields | Extended holonomy insertion is not that finite local list; no contour-renormalization or loop source theorem follows |
| SRCCD55 §5.0; SRC2_55 §1.2–1.3 | Exact tower/conditional-source identities apply to any finite bounded loop family | Quantitative geometric continuity, fine-to-coarse matching and nonzero signal |
| SRCAN55 coupling-source route; SRC2_55 §3.2–3.3 | Frozen-plus-top representation and Flow-pos conditionally supply e-source regularity | Coupling derivatives do not insert an arbitrary path-ordered holonomy; a loop-dependent source representation must be built |
| SRC2_55 §5.3, Rep^O | Explicitly requires a strictly local insertion and a canonical-size rooted representation | Replace point roots by controlled contour/tube geometry; repeated segments, growing fine-link count and intersection mixing cannot be hidden in a fixed local constant |
| FLOW §§7–8; FLOW55 §1 | Conditional F-flow/F-tune supplies a shared real trajectory and coupling brackets | No holonomy moment, Wilson-gradient-flow transport or area-law bound is produced by the beta function |
| W_T0 §§2,4–6 | Spatial support, boundary extension and the two-scale strategy; ALG-B exposes mixed/covariant obligations | Its observable is unbounded magnetic energy, not a holonomy; neither TS bound for B is a TS bound for loops |
| EXISTENCE ES5, X-ALG/X-FLOW | Bounded fixed-resolution/flowed loop subsequences already exist at their compactness scope | X-FLOW-NL/X-ARP/H-cont show the additional RP/continuity tasks; X-RAW's bare-loop degeneration is ARGUED, not a theorem assumed here |
| EXISTENCE H-cont^S-red, especially (iii)–(iv) | Products of block loops reduce to single-loop continuity estimates within the stated soft construction | H-SYN, H-corr^S, H-lin^S and physical identification remain named inputs; gauge-orbit separation on a finite graph does not establish continuum local-field completeness |
| EXISTENCE §18, NT-pol | Conditional fixed-torus winding-loop OS nontriviality | Local R^4 observables, positive-energy weight and a volume-uniform mass gap |

**Lemma W8 — universal bounded source identity (PROVEN).** For finitely
many real/imaginary loop coordinates X_i with |X_i|<=1, a positive normalized
soft chain and its original bare marginal, define

    M_k(z;V)=E[exp(sum_i z_i X_i(U_0)) | U_k=V].

Then `|M_k(z;V)|<=exp(sum_i |z_i|)` and
`|M_k(z;V)-1|<=exp(sum_i |z_i|)-1`.
On `sum_i |z_i|<log 2` the function is zero-free, with the log branch zero
at z=0. Differentiating under the bounded finite integral is justified by
the same exponential majorant. The tower property gives
`M_(k+1)=E[M_k|U_(k+1)]` and hence the log recursion and its cumulant
derivatives. No large-field exception is required for these elementary
real-law absolute bounds. On a uniform coordinate polydisc this sufficient
radius shrinks as 1/n; it is not SRC2's n-independent spatially local
complex-source theorem. More fundamentally it contains no decay,
renormalization, contour continuity or comparison with a coarse holonomy. ∎

For an actual program the new estimates are:

- **Contour limit/regularity:** chosen cutoff paths or flows converge in
  the joint hierarchy, continuously under the specified geometry tests;
  for thin loops supply perimeter/corner/mixing counterterms and required
  collision extensions. For bounded smeared loops (3) handles degree growth,
  leaving these identifications and mixed local moments.
- **Loop insertion RG and matching:** construct a source functional with
  insertions `sum_i z_i w_a(C_i)` and a scale decomposition rooted along
  the contour/tube. Control its normalization, shape derivatives, all
  required mixed orders, full histories and all coarse fields (or actual
  integrable local envelopes). A sufficient real-law matching estimate is
  `E|E[w_a(C)|U_k]-w_k^matched(C_k)|<=epsilon_(a,k,C)` with a stated
  vanishing regime. Boundedness alone gives no such small error. Complex
  tilted ratios require their own bounds; real conditional contraction
  cannot be used as a complex-law positivity argument.
- **Support and common covariance:** quantify finite-support approximation
  errors in the L^2 forms (8), (9), including reflected, rotated and mixed
  words. For a local witness a growing-support limit must retain a fixed
  compact approximation with a signal margin, uniformly over its free
  comparison class as well as YM.
- **Dynamics:** prove the loop-specific lower/upper bounds in §6, and the
  large-distance decay in §7 if a gap is sought. Existing fixed source
  radius, finite-coupling remainder, coercivity and tail lanes are only
  possible upstream inputs. Their completion is not asserted or attempted
  by this lane.

Balaban and Dimock are credited for the constructive RG methods behind the
source program. Dimock's
[Balaban-method convergence paper](https://arxiv.org/abs/1304.0705) treats
a three-dimensional scalar model; its methods are not a four-dimensional
nonabelian loop theorem. No literature stability theorem is substituted
for any row above.

## 6. Non-freeness: an explicit comparator and a conditional loop witness

**Why a loop cumulant or an informal area/perimeter comparison is inadequate.**
If X is Gaussian of variance v, `E exp(iqX)=exp(-q^2v/2)`, but the third
cumulant of Y=exp(iqX) is

    kappa_3(Y)=exp(-9q^2v/2)-3exp(-5q^2v/2)+2exp(-3q^2v/2), (10)

which is not identically zero. This follows by substituting its first
three Gaussian moments in the definition of a cumulant. Nonlinear loop
variables can therefore have nonzero higher cumulants in a free theory.
Equation (5) also shows the UV perimeter subtraction is distinct from a
large-distance perimeter law. At fixed smoothing length, a shrinking loop
in a smooth Gaussian field can start with its area SQUARED, already without
interaction. A short-distance diagnostic needs fixed shape, smoothing
ratio, normalization and a quantitative free expectation, not just the
word “area”. Large-loop area law is discussed separately in §7.

**Lemma W9 — canonical Gaussian spatial-loop comparator (PROVEN).** Fix
a nontrivial smooth closed spatial contour C in R^3, a smoothing ratio
eta>0, and C_ell=ell C. For one centered free Abelian vector field with
mass m>=0 and nonnegative covariance amplitude c, its transverse equal-time
covariance, after spatial heat smoothing s=eta ell^2 on each field, gives
the loop flux variance

    V_m(ell)=c integral_R^3 d^3k/(2 pi)^3
       exp(-2 eta |k|^2) |J_C(k)|^2/[2 sqrt(|k|^2+(m ell)^2)],
    J_C(k)=integral_C dy exp(i k.y).                        (11)

Here the model is DEFINED by the usual free Fourier covariance
`c/(p_0^2+|p|^2+m^2)` on transverse spatial currents. Longitudinal terms
drop since `k.J_C(k)=0`, by integrating the derivative of the exponential
around the closed curve. Integrating p_0 gives `1/(2 sqrt(|p|^2+m^2))`.
The scaled current is `J_(C_ell)(p)=ell J_C(ell p)`; substituting k=ell p
gives (11). The UV integral is finite because eta>0; at k=0,
`J_C(k)=O(|k|)` since `integral_C dy=0`, so the massless integral is finite.
This directly verifies the formula and its domain.

For m=0 the variance is ell-independent. For m>0 it is nonincreasing in
ell by its pointwise nonnegative integrand. Allow finitely many independent
such fields A^a, with masses m_a and amplitudes c_a, and real diagonal
traceless Hermitian matrices H_a=diag(h_(a,1),...,h_(a,N)). Define the marked
Cartan-valued free holonomy by

    w_G(C_ell)=N^(-1) Tr exp(i sum_a H_a X_a(C_ell)).
    E w_G(C_ell)=N^(-1) sum_(j=1)^N
                   exp[-(1/2) sum_a h_(a,j)^2 V_(m_a)(ell)]. (12)

This is an SU(N)-valued, commuting embedding; its covariance conventions
and loop map are explicit. Set `D_G(ell)=1-Re E w_G(C_ell)`.
For ell_0>ell_1, (11)–(12) give

    D_G(ell_0)<=D_G(ell_1).                                 (13)

The conclusion is preserved by probability mixtures of this marked family,
with the same scale-independent observable definitions; every D is bounded.
This is a comparator of canonical Abelian Gaussian/Cartan holonomies,
including massive modes, not every free theory or a noncommuting
path-ordered color-Gaussian class. No identification of that larger class
with (12) is made. ∎

**Proposed YM observable and hypotheses (OPEN).** On an aligned time
slice use the same geometric contour C_ell and the actual three-dimensional
Wilson-flowed bare links at s=eta ell^2, with lattice flow time s/a^2.
Let `D_(K,R)(ell)=E[1-Re w_(K,R,s)(C_ell)]`, so `0<=D<=2` exactly.
Fix odd L>=3, integers m_0,d_0>=0, g_ref>0 and R_F>=0. Work on even
temporal tori of physical size R>=R_0 large enough to contain the selected
contours without spatial winding. Use ell_m=L^(-m), a=L^(-K), k=K-m,
and the SAME trajectory as the local core, in FLOW/W_T0's convention

    u_k=g_k^(-2),
    U_-(m)<=u_(K-m)<=U_+(m),
    U_±(m)=g_ref^(-2)+beta_± m log L ± R_F,
    beta_->0, beta_+>=beta_-, U_-(m_0)>0.                  (14)

The Wilson coefficient is u; if using the usual action coefficient
2N/g_std^2, then g_std^2=2N g^2. There is no imported perturbative
coefficient or prefactor fitted to a loop value. Require constants c_->0,
C_+>0, 0<=vartheta<1 and d_0, independent of K,R, such that

    D_(K,R)(ell_(m_0))>=c_- / u_(K-m_0),
    D_(K,R)(ell_m)<=C_+ u_(K-m)^(vartheta-1),
                       K>=m+d_0, m>=m_0.                 (15)

Require convergence and a common reconstructed realization of these marked
boundary loop variables as in §4, including strong sharp-time
identification if they are to belong to the translated continuum system.
Full local T_OS also needs compact localization and the correct OWN-free
identification; (12) is only a proposed specified null class.

**Theorem W10 — two-scale separation (PROVEN implication).** Under those
hypotheses, let A=c_-/U_+(m_0)>0. Choose a fixed m_1>m_0 with
`C_+ U_-(m_1)^(vartheta-1)<=A/2`; it exists because U_- diverges and
vartheta<1. Before the continuum limit fix both physical scales. Set

    W_loop(omega)=[D_omega(ell_(m_0))-D_omega(ell_(m_1))]_+.

Equations (14)–(15) give `W_loop(omega_YM)>=A/2` at every sufficiently
fine cutoff, uniformly in volume. Bounded coordinate moment convergence
preserves the two inequalities. Equation (13) gives `W_loop(mu)=0` for
every marked comparator mixture. The positive-part operation is
1-Lipschitz, so this is a continuous witness in its two moment coordinates;
at least one of the two moment discrepancies is >=A/4. In the common
boundary realization, D is the vacuum pairing of `1-Re w`, by W7.
A vacuum-preserving equivalence that preserves these specified observables
cannot identify the two systems. ∎

This replaces W_T0's unbounded energy moment task by automatic bounded
loop moments. It does NOT produce (15), continuum sharp-time continuity,
compact locality or separation from every admissible free identification.
Those are the substantive remaining inputs, not consequences of W10.
If desired one can first test nonzero time-dependent reflected loop
correlations; a nonzero boundary mean alone is not a proof of an excited
sector. A two-scale marked witness can even distinguish a deterministic
observable assignment, so its physical interpretation must stay explicit.

## 7. Mass gap, confinement and the Polyakov route

The target is unchanged:
`ker H=C Omega`, `spec(H|Omega^perp) subset [m_*,infinity)`, m_*>0 in
fixed physical units, and a nonzero excited subspace. With a Poincaré
covariant physical reconstruction the Hamiltonian gap has the invariant-
mass interpretation of REC_LIB §14. Loop-only W6 does not supply that
Poincaré reconstruction.

**Lemma W11 — the same dense-family spectral criterion (PROVEN).** Suppose
centered loop/mixed vectors v_F span a dense subspace of the intended
Omega-perpendicular Hilbert space, and for ONE m_*>0 each obeys

    0<=<v_F,e^(-tH)v_F><=A_F exp(-m_*t),  t>=t_F.           (16)

For 0<=b<m_*, spectral positivity bounds the left side below by
`exp(-bt)||E_H([0,b])v_F||^2`. Send t to infinity to obtain zero projection.
Density and boundedness of the spectral projection extend this to all
Omega-perp; taking b up to m_* proves the claim, including absence of
extra vacuum vectors. Nonzero excited space remains an additional input.
At cutoff/finite volume, A_F,t_F and m_* must have uniform physical values
on a time window tending to infinity. First take the common continuum/
volume limit at each fixed t, and only then the large-t limit. ∎

If H_e embeds as a proper invariant subspace in H_mix, a gap on H_e says
nothing about new orthogonal states. For example append to a gapped
Hamiltonian multiplication by x on L^2((0,1)); all old correlations stay
gapped while the larger spectrum reaches zero. If loops are instead
proved to lie in the same reconstructed local vacuum sector, no new
physical gap target is introduced. In either case the density/identity
of the sector must be shown.

**Confinement is a different observable limit (ARGUED route, OPEN
estimate).** A positive string tension would concern suitably renormalized
large rectangular loops, schematically
`-log <w(R,T)>/(RT) -> sigma>0`, with positivity, shape/large-time limit
order and perimeter/cusp subtractions specified. Static-source transfer
representations associate long temporal rectangles or temporal Polyakov
correlators with external-charge energies/free energies. Establishing that
representation and limit in this continuum construction is an additional
task. It is not the vacuum dense-family estimate (16). A string tension has
dimension mass squared; dimensional analysis alone supplies no equality
between sqrt(sigma) and a glueball mass. Strong-coupling lattice confinement
cannot simply be transported through a weak-coupling continuum limit.

The **actual existence-lane Polyakov result is spatial**:
`../ym4d-existence/EXISTENCE.md` §18.1 uses level-j spatial holonomies
W_mu around the torus at positive time, and f_n=N^(-1)Tr product W_mu^n_mu.
They are observables of the SOFT block law, not an already identified
renormalized bare-continuum loop. Center symmetry gives E f_n=0 for
charged n. §18.4 NT-pol combines near-flat plaquette estimates with a
deterministic holonomy inequality. For SU(2), with
`F_2=f_(e1)+f_(e2)+f_(e1+e2)`, its conditional fixed-box conclusion is
`Cov(theta F_2,F_2)>=3/8`. Inputs include (O1)–(O3), H-coer/CLS-cone and
H-up/(a3-q). §18.5's fixed-spatial-torus/infinite-time version also consumes
ASSEMBLY (III)'s inputs and K9-req. Its sufficient smallness condition
contains `n_s^2+4 n_s d_t`, and is not uniform as spatial size grows.

This is a useful conditional nonzero OS norm, not proof of interaction,
confinement or a mass gap. In particular positive variance can reside
entirely in ker H: on C^2 with H=0, Omega=(1,1)/sqrt(2) and
v=(1,-1)/sqrt(2), `<v,e^(-tH)v>=1` for every t. This rebuilds the
zero-energy distinction made in EXISTENCE §18.7 (WC_infinity^sp).
Winding loops have increasing support as the spatial torus grows; no
bounded-contractible-support R^4 observable follows. Recovering one needs
a new local infinite-volume signal and, for the gap, (16). An auxiliary
RG fluctuation gap is likewise not the physical H gap.

## 8. Comparative verdict and the next discriminating task

These are judgments about the named obligations, not complexity theorems.
The local-field reference is the current qualified OSLEAF55/REC library,
with its unresolved actual Yang–Mills inputs. “Same” does not mean solved.

| Top input | Thin renormalized loop replacement | Bounded spatial-loop replacement | Adding loops to the local core |
|---|---|---|---|
| H_reg | **HARDER:** line/corner/mixing and geometry domain replace point-contact estimates | **EASIER** for pure moment growth by (3); **HARDER** for the full reconstruction interface, sharp-time/geometry and locality | **HARDER overall:** local regularity remains and mixed estimates are new; bounded boundary module is easier than unbounded B |
| H_RP | **SAME** conditional mechanism: half-supported maps and convergent Gram entries | **SAME** for aligned time reflection; rotated/localized completion still OPEN | **SAME** finite-cutoff half-support mechanism; mixed continuum limits are part of H_reg/ALG |
| H_Euc | **HARDER** interface: contour approximations and renormalization must transform coherently | **HARDER:** all normal/shape copies and their joint action; the slice subgroup is insufficient | **HARDER:** local covariance does not establish mixed covariance |
| H_int | **SAME** unresolved dynamics, with additional scheme/comparator matching | **EASIER** bounded-moment witness bookkeeping; **SAME** unsupplied upper/lower dynamics; broader free-class exclusion OPEN | **SAME** signal obligation, with an additional same-theory/locality identification |

For four-dimensional flowed loops H_reg's pure bounded-moment advantage is
the same, but **H_RP is HARDER**: W2 does not apply to their nominal contour
support, and (8) requires an actual vanishing-error regime. Formal covariance
of the flow helps define labels, not prove full H_Euc of the limit. A claimed
shorter route obtained by treating those flowed centers as point fields is
not supported by the stated reconstruction hypotheses.

- **Loops alone, full T_OS plus mass gap: UNDECIDED.** W1 and W6 are
  conditional/compactness ingredients, not the requested physical theory.
- **Local core plus loops, full target: UNDECIDED.** W7 shows a genuine
  bounded boundary extension is possible under its premises; the full
  mixed/covariant/local system and infrared estimate are still OPEN.
- **No universal NO-GO is established.** Renormalized thin loops, a
  bounded Euclidean net, compact support smearing and shrinking-loop
  local limits remain possible routes.

The most focused next task is to specify one smooth spatial contour and
eta, two physical scales and the precise lattice maps, then produce either
the uniform original-law comparisons (15) with a same-system localization
bound, or a counterexample to one of those comparisons. Boundedness has
already removed the pure-loop second-moment obstacle; repeating that bound
would not advance the missing dynamics. An alternate priority is the
continuum net/time-zero reconstruction contract if the owner chooses a
loop-first target. Both are research directions; this note makes no new
physical axiom or owner choice of OWN-alg/OWN-free.

## 9. No-Go Discipline Gate — scoped boundary audit

**N1 — alternative routes.** Six genuine families were examined, all
`ATTEMPTED` at the level of definitions, source matching and written
derivations: thin contour renormalization (W3–W4); four-dimensional flow
with localization (W5,(8)); spatial flow and a boundary algebra (W7–W10);
fixed-resolution block-loop compactness/source transport (W1,W8 and
EXISTENCE); a bounded Euclidean net (§4); shrinking-loop reconstruction of
local fields (§4). Each has its stated terminal estimate; none is claimed
ruled out by prior authority. These are materially different supports,
reconstruction mechanisms or limits, not six failed numerical searches.
There is no exhaustive no-go packet and no packet PASS.

**N2 — dependence of conditions.** The labels below group tasks rather
than count independent obstructions: A=common analytic/covariant/RP
reconstruction, I=marked loop separation, M=dense-family spectral decay.
For the matching YM premises, the implication status is:

| Pair | First alone implies second? | Second alone implies first? | Independence established? |
|---|---|---|---|
| A,I | Unresolved for actual YM; abstract reconstruction alone has free examples | No reconstruction supplied by two numbers; W10 assumes the realization separately | No claim |
| A,M | Unresolved for actual YM; abstract reconstruction admits gapless examples | (16) presupposes a Hilbert system and does not construct its YM law | No claim |
| I,M | W10 supplies no long-time estimate | A gap supplies no prescribed comparator separation | No claim |

Within A, W3's limiting RP consumes convergence; it is not counted as an
independent extra wall after all its half-supported Gram limits are proved.
W1 bounds pure-loop moments but not mixed local-field moments. No inflated
wall count is used in the verdict.

**N3 — hidden premises.** Re-read all PROVEN entries: finite Wilson/Haar
setting in W2; matching half maps/convergence in W3; Gaussian model in
W4/W5/W9; normalized state, action and continuity in W6; convergent e-core
in W7; positive normalized chain in W8; trajectory, (15), comparator and
same-system realization in W10; full density/uniform rate in W11. They
are printed premises, not adopted axioms. No “standard reconstruction” or
recalled `[m]` theorem closes an unproved step. The spectral theorem and
elementary Gaussian integration are the mathematical background used.

**N4 — residual matching.** W_T0 §6.1 and EXISTENCE X-FLOW-NL concern
actual support, matching only this note's support warning, not an RP-failure
theorem for YM. REC_LIB/REC_CONT's finite Cartesian scope matches only the
domain mismatch, not a prohibition on net reconstruction. EXISTENCE §18.5
matches only fixed-spatial-torus nontriviality, not R^4 local gap. The
point-field variance obstruction in OSLEAF55 FS is not applied to bounded
loop traces. No mismatched prior no-go is used.

**N5 — resolution/rhetoric.** Per-element trace bound: W1, exact at each
cutoff. Per-site half support: W2, using geometric edges. Per-mode temporal
Gaussian example: W5, not an SU(N) measure theorem. Per-block loop laws:
existing source identities/conditional estimates only. Lattice-wide and
continuum: W3/W6/W7/W10/W11 are implications with their printed uniform
inputs; no full YM construction or gap was checked. These are written
proof assessments, not a numerical runner's executed certificate.

**N6 — partial closure.** Bounded boundary loops already remove an
unbounded-observable moment requirement. A label/topology choice can make
the proposed target precise; it cannot supply its state or estimates.
Reconstruction via a net or local shrinking limits is new mathematics,
not necessarily a new physical axiom. No claim that the primitive registry
forbids any of these routes is made.

**N7 — steelman.** A loop-first construction could bypass the singular
point-field contact problem: use bounded gauge-invariant variables,
support-compatible spatial regularizations, actual group-continuous mixed
limits and a nontrivial time-zero net; reconstruct the physical net and
only later obtain local fields. W1/W2/W7 and Schlingemann's method identify
concrete ingredients. The decisive missing tasks are uniform continuum
localization/covariance and the physical-sector identification, not a
logical contradiction. This viable mechanism is why the whole-route
verdict is UNDECIDED rather than NO-GO.

**N8 — prior-cycle echo.** The inspected W_T0/EXISTENCE work already
separates bounded compactness from regularity and flow support. A previous
REC_LIB continuation obligation has since acquired the REC_CONT producer;
this note does not repeat that obsolete missing-lemma diagnosis. The same
lesson applies here: an absent loop reconstruction lemma is a task, not
evidence of impossibility. This search was limited to the directly relevant
YM/reconstruction sources; it is not an exhaustive repository audit.

Delivery is limited to the author allowlist. No numerical experiment was
run after the sandbox rejected nice. The uncommitted scope checks above
are not represented as a landed no-go certificate, and no audit/ledger
status is changed.
