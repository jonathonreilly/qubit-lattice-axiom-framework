# Repo search

Writer: Codex, task-configured gpt-6-astra xhigh (the runtime identifier is
not independently exposed); source commit
`6e4cfbfbf2aadaa6347ccb630130f7a947b9e9d7`. Research check of FINISH
1091 (Claude Fable 5.2 medium), not an audit; no scientific status or
Yang–Mills mass gap is claimed. No Lean formalization or computational
proof is performed. Row 1093 is excluded and will not be read. This check
does not supply any of the open stability hypotheses or start a new attack.

The task-specific prior file is absent at the pinned commit. The lead's
2026-11-08 digest searched main and PRs 10114, 10133, 10134 and 10141 for
earlier UV/RG targets. It reports no supplier of this later face-stability
statement. I checked the relevant method matches below, not every unrelated
file named by that digest. Main was fetched at
`8b11ae2bb95e641494fe75ed83d108ee712fa3a9`; PR 10114 was fetched at
`f76f6c649cff7dffbab664d8976e680e8f287fe9`.

| Actual source checked | Closeness and use |
|---|---|
| Main `research/ym4d/library/fp1.md:235–258` | Fixed-scale free Gaussian covariance and conditioning. Different law; not sheet-field stability. |
| PR 10114 `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/K4MATCH.md:530–555` | Interacting higher-cumulant matching remains open. A related consumer, not FST-T. |
| Same PR, `BOTTOM_SECOND_CURVATURE_ASTRA.md:353–364` in that folder | “Face lifts” cover momentum charts; a different use of “face”. |
| This lane `gap-ds-gauge.md:79–101` (row 691, Claude Fable 5.2 medium) | The prior averaged block mechanism. FST-BD adds arbitrary block families and its specific Newman covariance form; the mechanism is credited, not claimed anew. |
| Row 1077:106–178,318–356,537–602; row 1078:353–441,513–526 | Direct inputs: face law, Ward counterexample, target (17), and O7/J1. Reused at their stated scope. |

Exact face-stability/FST/neutral-pin label searches in `open-registry.md`,
`open-core.md` and `l17c.md` found no competing owner. This is the assigned
check of row 1091, not an attempt to take over its open proof. Row 1093 was
not read. The full-read outline index was searched first; neighbouring rows
`chunk-01.md:59–78` and `obligations.md:16–30` lead to outline 580–600.
Those source lines distinguish polynomial decay from a spectral gap.
The 4.12–4.19 index has no match under FST, face-stability, Dobrushin or
principal-chiral labels; its operator gaps are not a sheet-stability input.
CA-I 2700–2715 explicitly excludes a mass-gap assertion. This bounded search
finds no duplicate result; it is not a proof of exhaustive absence.

## Checkpoint

Source: pinned checkout above; Sussman–Alpoge outline and CA-I at
`31a47c543775`, fetched once into the new directory
`/tmp/sa-gap-face-stability-check-astra.gsRtcm`.
Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for their source material; further credits accompany uses.

Plan: (1) finish the bounded source and ownership checks; (2) check M1/M2
and FST-BD; (3) check FST-P/F and the periodic-limit claims; (4) check
FST-T and K3 against the posted paper; (5) redo G1/G2 by hand and check
7.4/FST-N; (6) collect corrected verdicts and one RESULT line.

Checkpoint: all six steps complete. Source row 1091 is unchanged. The
conditional implications survive with the corrections below; their physical
hypotheses remain open. No new proof attack, audit, runner, Lean check or
external post was made. Downloads and source-processing artifacts stay in
scratch. The next decision belongs to the lead: apply the textual corrections
and retain FST-F/FST-P/FST-T as open quantitative inputs.

## 1. M1, M2 and FST-BD

**M1 and M2: HOLDS.** Row 1077, lines 106–133, defines one positively
oriented edge per transverse bond and one elementary square per vertex,
with T >= 3. Quaternion inversion is real-linear and orthogonal; left and
right multiplication by unit quaternions are orthogonal. Each plaquette
trace is therefore a real linear functional of each of its four unit
quaternions, with coefficient vector of norm one. Exactly two squares
contain a fixed edge. Their remaining edge sets are disjoint for T >= 3,
each with three members. Thus there are six neighbours, at most one shared
square per pair, |H_u| <= 2 lambda, and
|delta H_u| <= lambda |q-q'| <= lambda rho(q,q'). This includes links
occurring inversely in the oriented word. The field description is a
conditional description, not a claim that the coupled sheets are independent.

**FST-BD (i)–(iv): HOLDS as a theorem; its printed proof needs one correction.**
Here S is nonempty, the block list covers S, and bounded observables are
real-valued (complex versions follow by the same direct covariance identity).
No boundary restriction or truncated-block hypothesis is hidden in it.

For clarity, write l_x(f)=Lip_x(f) and
A_xu = 1_{x=u}(1-n_x/N) + N^{-1} sum_{V: u in V, x not in V} k^V_{x->u}.
The one-block difference splits into change of the integrand and change of
the conditional measure. This gives exactly (BD1), and l(Pf) <= A l(f).
For an allowed weight, sum_x w(x) A_xu <=
w(u)[1-(1-gamma)n_u/N] <= theta w(u). This verifies every coefficient in
(i), including the direction of its weight inequality. Constant weights
give (ii), since invariance places mu(f) between the infimum and supremum
of P^n f. Nonnegative influences force gamma >= 0, hence 0 <= theta < 1.

A direct derivation checks the covariance normalization without a change
of measure. For h_n=P^n f, uniform convergence in (ii) and invariance give

    Cov_mu(f,g) = (1/N) sum_{n>=0} sum_V
                   mu[Cov_{mu_V^eta}(h_n,g)].                 (Q1)

This is a telescoping identity: each summand before the block average is
mu[(h_n-P_V h_n)g]. Conditional expectation turns it into the indicated
conditional covariance. The series converges absolutely by (i).
For (iii), blocks disjoint from B vanish. Bound each remaining summand by
||g|| D_0 sum_{u in V} l_u(h_n). The weight
w(x)=exp[-a d(x,B+)] obeys w(x)/w(u)<=exp[a d(x,u)], and equals one on
B+. The sum is at most ||g|| D_0 n_max theta^n Delta_w(f).
The factor (1/N) sum_n theta^n equals
1/[(1-gamma)n_min]. This even gives (iii) with ||g|| in place of
2||g||, so the printed constant is valid. Constant g is trivial if B is empty.
For (iv), put W(u)=sum_b l_b(g) exp[-a d(u,b)]. It is positive unless g
is constant, and satisfies the same weight inequality term by term.
(I) and the count of common blocks give at most
X n_max theta^n Delta_W(f) in (Q1). Summing gives exactly (iv).
This path verifies both 1/N factors independently of the tilted-measure proof.

The printed (BD2) is also correct for positive g. Its first faulty sentence
is Step E: “mu(g+c) tends to 2 ||g||”. The actual limit is
mu(g)+||g||, which is **at most** 2||g||. Replace that sentence by:
“Let c decrease to ||g||. Since mu(g+c) <= ||g||+c, the prefactor is
at most 2||g|| in the limit.” This preserves (iii). Step F's different
limit, mu(g+c)/inf(g+c) -> 1 as c -> infinity, is correct. Restrictions
of h_n and g to a block have the required one-site constants. The proof
uses only whole-block conditionals, even when a block meets only part of B.

**Application-domain correction.** S^3 with the Hamming metric is not
compact. Therefore the sentence in 5.1 “Apply FST-BD with the discrete
metric” does not literally satisfy its setting. The proof above only needs
bounded coordinate metrics, measurable block kernels, (C), (D_a), and
invariance. Replace the setting by “a finite product of standard Borel
spaces, equipped with bounded measurable coordinate metrics, with
specified invariant conditional kernels”; retain the compact continuous
positive-density case as a sufficient way to obtain those kernels. Haar
spaces with Hamming distance meet this corrected setting. No estimate changes.

## 2. FST-P, FST-F and their comparison

**FST-P: HOLDS AFTER CORRECTION of the application setting and the
finite-torus wording.** Use the measurable-kernel extension of FST-BD
just proved. Let A=e^{4 lambda l^2}-1 and B=e^{4 lambda}-1. The tilted
block energy has oscillation at most 4 lambda l^2. Its normalized density
relative to the untilted law is between e^{-4 lambda l^2} and
e^{4 lambda l^2}; centering a test at its infimum bounds the expectation
change by A osc(F). A pin change therefore costs k0+2A. Changing one
neighbouring link changes only one field vector, by at most 2 lambda,
so the difference of energies has oscillation at most 4 lambda. It costs
B osc(F). These verify all three influence terms in 5.1.

For a fixed target site, there are l^2 translated squares containing it.
Its positions in those squares exhaust Lambda once. Thus the untilted pin
sum is sum_{y,w} k0_{y->w} <= gamma_0 l^2, the tilt correction is
l^2(4l)(2A), and the transverse correction is l^2(6l^2)B. Division by
n_x=l^2 yields gamma_0+8lA+6l^2B. A pin and a target in the square have
longitudinal l1 distance at most l+(l-1)=2l-1. A transverse neighbour
costs at most 2(l-1)+1, the same value. Periodic distance can only reduce
these upper bounds. L,M >= l+2 keeps the square and its four outer strips
injectively embedded, including l=1. Hence the printed gamma(lambda,a)
is correct. B+ lies at distance at most 2(l-1) from B. The prefactor
2||g|| e^{2a(l-1)}/(1-gamma) is correct.

The displayed choice of a gives e^{a(2l-1)}=2/(1+gamma_0).
The stated upper bound on the perturbative bracket then gives exactly
(1+3gamma_0)/(2+2gamma_0)<1. Continuity at lambda=0 supplies a positive
eps. For a single bound on [0,eps], use gamma(eps,a) in the denominator.

For round-Lipschitz observables, osc_x(F)<=pi Lip_x(F); this proves the
printed constant in the corollary whenever the support distance is at
least n-r. **That inequality is not true for every n on a fixed periodic
torus.** The finite-volume estimate uses periodic distance. Replace the
corollary's finite-volume reading by: “For each fixed n, take periodic
sizes large enough to avoid wrapping the two supports; then pass to the
local limit.” The exponential-in-n assertion (17) is valid in that limit,
with the stated constant and uniformity. Round-Lipschitz local tests and
their products are continuous, so their expectations pass under local weak
convergence. The bounds then cover every such periodic local limit, not
arbitrary boundary Gibbs states or flat-holonomy sectors. If the summary
retains *bounded measurable* tests in the limit, it must add an argument:
for a fixed finite support U, its conditional density relative to product
Haar is continuous in the finitely many boundary spins, uniformly bounded,
and uniformly continuous in the interior spins. Mixing those densities
against the converging boundary marginals gives pointwise convergence of
the marginal densities, hence L1 convergence by their common bound. This
passes all bounded tests on U. This additional fact uses the finite-range
smooth face specification; it is not a consequence of weak convergence
alone. No truncated blocks are used in these torus arguments. Free-boundary
versions remain outside their scope.

**FST-F: HOLDS, with h_0,a,X positive and with the same local-limit
qualification.** The field interpolation is along a convex segment in
the sup-norm ball, not merely along a bound on |delta|. Differentiation
of the finite normalized exponential integral gives the printed covariance
identity. The inserted linear spin has round Lipschitz constant <=|delta|.
Thus k=lambda X exp(-2a|u-w|_1). The metric weight supplies
exp[a(|u-w|_1+1)] for each of the six neighbours, yielding
6 lambda X e^a sum_u exp(-a|u-w|_1). In one periodic direction there
are at most two sites at every positive distance, so the sum is at most
1+2 sum_{r>=1}e^{-ar}=(1+e^{-a})/(1-e^{-a}). The product of the two
bounds is exactly S_a. This is a hand geometric-series estimate, not an
enumeration. Within a sheet, e^{-2ad}<=e^{-ad}, proving (I) with X.
Here n_min=n_max=1, so (iv) gives the displayed face bound. The proposed
eps makes gamma<=1/2 and gives the printed 2X prefactor after absorbing
the fixed support extent. In transverse directions, graph distance between
edges sharing squares also grows at least linearly with spatial separation;
fixed edge orientations and support offsets change only the prefactor.

**The comparison claim requires correction: FST-P implies FST-F (with
new constants); FST-T also implies FST-F. No strictness or converse is
established.** This answers the requested comparison without a new route:
it follows from the already checked (iv) and the same tilt estimates.
For completeness the short missing implication is as follows. On one
sheet in an arbitrary field |H|<=h, use the translated l-squares alone
and Hamming seminorms. Choose alpha>0 and h>0 so that

    q=e^{alpha(2l-1)}[gamma_0+8l(e^{2h l^2}-1)]<1.             (Q2)

The untilted pin criterion and the two-tilt triangle inequality give (C)
and (D_alpha) uniformly for every such field. Within any conditional
square, Cauchy–Schwarz and Var(F)<=osc(F)^2/4 give

    |Cov(F,G)| <= (1/4) sum_{v,w in V} osc_v(F) osc_w(G)
      <= [e^{2alpha(l-1)}/4] sum_{v,w in V}
                      osc_v(F) osc_w(G)e^{-alpha|v-w|_1}.

Thus (I) holds for the Hamming metric without any further physical input.
Apply (iv), then osc_v<=pi Lip_v. This is FST-F with

    h_0=h,  a=alpha/2,
    X=pi^2 e^{2alpha(l-1)}/[4(1-q)],  L_0=l+2.               (Q3)

These constants are for real observables. For complex observables, apply
the real estimate to the four pairs of real and imaginary parts; 4X is
a valid constant in (Q3). This does not change the implication.

Existence of alpha,h follows from gamma_0<1 and continuity. This proves
non-strict logical weakness of FST-F relative to FST-P. It does not order
FST-P against FST-T. Replace “three forms of decreasing strength” in 3.4
by “two sufficient hypotheses FST-P and FST-T, each implying FST-F;
no comparison of FST-P with FST-T is proved.” FST-F is a covariance
inequality for *arbitrary observables*, including nonlocal ones; calling it
“two-point” must not suggest that spin-spin covariance decay alone suffices.

## 3. FST-T, K3 and the ARGUED higher-order discussion

**Proposition FST-T: HOLDS**, for finite positive C_T,X_T and a>0.
Every F,G with finite coordinate Lipschitz constants is bounded on the
finite product, after fixing one value and telescoping. W is bounded too.
The exponential moment in (t,s,r) is therefore entire by uniformly
convergent exponential series on compact parameter sets. At any real
triple it is positive for real F,G, hence nonzero in a complex neighbourhood. This
supplies a local holomorphic logarithm and proves real analyticity of g
at every real t; no global zero-free complex strip is assumed.
For complex F,G, the same argument uses positivity only at (t,0,0),
which still holds because W is real; that is enough for the mixed derivatives.
Differentiating the logarithm gives the joint cumulant with n copies of W.
At sites where H_u=0 choose a_u=0; elsewhere set a_u=H_u/|H_u|. Multilinearity
then gives the stated finite sum, including repeated insertion sites.
Taking absolute values before summing gives
|g^(n)(0)|/n! <= X_T K/2^n. Thus its Taylor series has radius at least 2
and defines a real-analytic function on (-2,2). It agrees with g near zero
by the local logarithm. The identity theorem for real-analytic functions
on the connected interval extends equality throughout (-2,2). In particular
at t=1 the absolute sum is <=2X_T K. This checks the radius, continuation,
and constant; there is no illicit extrapolation across a real singularity.

**K3: HOLDS with the paper's maximum-norm metric; HOLDS AFTER CORRECTION
if the preceding l1 convention is retained.** The open source read is
OpenAI's `preliminary.tex`, lines 1–66, at
`4eaee87548250b2682affda7d05d947c05554bae`. Its Theorem 3.1 explicitly uses
d_infinity (periodic on a torus), unpinned free subgraphs or tori with both
sides >= C Xi, and L_F=||F||+max Lip_x(F). It allows weakened nonnegative
bonds, not fields or arbitrary pins.

The three-covariance identity for kappa_3 is exact. The product estimate
L_{F_2 F_3}<=2L_{F_2}L_{F_3} is valid: its sup norm is at most the product
of the sup norms, and its individual Lipschitz constant is at most
||F_2|| max Lip(F_3)+||F_3|| max Lip(F_2). The factor 2 is conservative.
Each covariance contributes at most its coefficient (2,1,1) times
C'_beta(1+n)^20 product_i L_{F_i} exp[-c d_i/(2Xi)]. The support union
has size at most n; the inequality splitting 1+beta+n+d into three
factors is valid. The supremum defining C'_beta is finite because an
exponential dominates that fixed polynomial. Use the actual pair distance
in each polynomial before replacing its residual exponential by the
bound with d_i. Symmetry gives the maximum of the three d_i and the factor 4.
For three one-site supports with sorted pair distances r<=s<=t, d*=s
and the minimum spanning-tree length is r+s<=2d*. This gives exactly
c/(4Xi) for that tree, **in d_infinity**. If d_i and tree length instead
mean the l1 metric from 5.2, replace the two displayed rates by c/(4Xi)
and c/(8Xi), respectively, or explicitly rename c/2 as a new constant.
The theorem's original c cannot be kept under an unstated metric change.

**6.2 first-derivative consequence: HOLDS AFTER filling its stated
ARGUED steps; it is still only a derivative at zero.** For independent
sheets, the reverse martingale differences in the note are orthogonal.
Conditioning on later sheets expresses the matching difference product
as a single-sheet covariance of averages over earlier sheets. These
averages preserve support in that sheet, sup bounds and individual
Lipschitz bounds. Summing only over sheets intersecting both supports
therefore gives the paper's covariance estimate with one additional
factor bounded by the number of support sheets. This factor is independent
of T for fixed local tests. Apply the same three-covariance identity to
F,G,tau_p(u); tau_p is bounded by one and each coordinate Lipschitz constant
is at most one. If p has no sheet in either support, the third cumulant is
zero by independence. There are at most twice the number of support sheets
such squares p, because each edge belongs to two squares.

Here is the missing summability argument for fixed support shapes. Choose
longitudinal representative points v,w for F,G, and use u for the insertion.
Let R bound the diameters of both fixed supports. The largest isolation
distance for the three supports is at least half the minimum spanning-tree
length of {v,w,u}, minus 2R. This follows by applying the preceding
three-point argument to the representative distances and using that
changing an endpoint within a support changes distance by at most R.
Writing t(v,w,u) for that length, it is at least d(v,w) and at least d(v,u).
Consequently exp(-k t) <= exp[-k d(v,w)/2] exp[-k d(v,u)/2]. Summing the
last factor over a two-dimensional periodic lattice is bounded by a
convergent geometric series with linear shell counts, independently of
L,M. The finite p count above proves the claimed uniform derivative
bound and exponential decay in the separation, after decreasing the rate
and enlarging the support-dependent constant. The same argument covers
overlap by its fixed-support constant. It supplies no estimate at lambda>0.

**6.2 higher orders: the rate-loss mechanism HOLDS; the asserted
“of order” coefficient count is not proved as written.** For m=n+2
one-site entries, remove a longest edge of a minimum spanning tree.
The resulting two groups have all cross distances at least that edge
length (otherwise replacing the edge shortens the tree). That length is
at least t/(m-1)=t/(n+1). In the moment-partition formula for a cumulant,
replace every mixed-block moment by the product of its two group moments.
The resulting cumulant is zero by independence of the two groups. Each
difference is a covariance of products, controlled by Theorem 3.1, with
a finite constant depending on m. This gives decay at a rate proportional
to c/[(n+1)Xi], with an additional fixed rate loss to absorb the polynomial.
Fixed extended supports cost their diameters and constants as above.

For any *fixed labelled tree*, summing n insertion positions at rate alpha
costs at most [C(1+alpha^{-1})^2]^n. Delete one edge on the path between
the two fixed roots, bounding its exponential by one. The remaining
forest has one fixed root in each component; remove its free leaves
one at a time and use the two-dimensional geometric-series bound.
At alpha proportional to 1/(n+1) this grows like a constant^n (n+1)^{2n}.
But the full cumulant estimate also has the partition coefficients, product
Lipschitz factors and a sum over possible labelled trees. The note neither
tracks these nor proves an asymptotic “of order” for the full sum. Replace
its coefficient sentence by: “This method gives volume-uniform bounds at
each fixed order. Its available bounds lose rate with n and do not yield
a volume-uniform positive Taylor radius; no optimal growth rate is claimed.”
The conclusion is about this estimate, not a proof of zero analytic radius.
FST-T supplies both a rate uniform in n and the specified factorial/exponential
constants for all F,G; the rate alone is not the entire missing hypothesis.

## 4. G1, G2, the Ward statement and 7.4

**G1: HOLDS.** This is a check by hand of the two-site normalized integral.
At J=0 write c_i=cos(theta_i), s_i=sin(theta_i). The marginal densities
are proportional to e^{h c_1} and e^{-h c_2}. Reflection gives E s_i=0,
E c_1=r and E c_2=-r. Pairing positive and negative values of cos(theta)
in its integral shows r>0; nonconcentration shows r<1 and Var(c_1)>0.
Independence gives E cos(theta_1-theta_2)=-r^2. Differentiating the
normalized integral with respect to J gives

    Cov(c_1,c_1 c_2+s_1 s_2)
      = -r E c_1^2 - r(-r^2) = -r Var(c_1)<0.

The sine term vanishes by reflection. Compactness makes the integral and
its derivatives continuous in J; both strict inequalities persist for
some positive interval of J. This disproves the proposed extension of
zero-field cosine-character positivity and coupling monotonicity to
arbitrary directional fields. It is not a counterexample to mixing,
to Theorem 3.1, or to a statement restricted to J in [2.3,2.6]. A field
can also be produced by fixed boundary spins, but the claim must then
name the pinned interaction that produces it. No transfer to a uniform
high-coupling O(4) sheet is inferred here.

**G2: HOLDS.** Summing the first pair of signs gives
2 e^{Jc_1c_2}cosh[h(c_1-c_2)]+2 e^{-Jc_1c_2}cosh[h(c_1+c_2)];
summing the second pair gives 4cosh(Js_1s_2). Constant normalization of
the sign reference measure cancels. At J=0 the gamma law is a product
with marginal a(dgamma) proportional to cosh(h cos(gamma)) dgamma.
The second sign partition function has zero logarithmic derivative.
For the first, the sum/difference identities for cosh give exactly

    partial_J log(Z^1 Z^2)|_0
      = -c_1 tanh(hc_1)c_2 tanh(hc_2) = -psi(gamma_1)psi(gamma_2),
    psi(gamma)=cos(gamma)tanh[h cos(gamma)].

Let m=E_a gamma, z=E_a psi and t=E_a(gamma psi). Differentiating the
normalized covariance gives
-(t^2-m^2 z^2)-2m(-tz+m z^2)=-(t-mz)^2, exactly as printed.
The derivative of c tanh(hc) is tanh(hc)+hc sech^2(hc)>0 for c>0.
Thus psi is strictly decreasing on (0,pi/2). For independent X,Y with
law a,

    2 Cov_a(X,psi(X))=E[(X-Y)(psi(X)-psi(Y))]<0.

The density is positive, so strictness is justified. The covariance starts
at zero and has negative derivative, hence is negative for all sufficiently
small positive J. The increasing coordinate functions gamma_1,gamma_2
therefore violate association. This refutes that extended association
step only, with the same restricted scope as G1.

**7.3: HOLDS as a counterexample at the configuration specified in row
1077; the summary at line 308 FAILS for its pin-only reading.** A field
contributes partial_t^2[-H_u dot exp(ta f_u)q_u]|_0
=f_u^2 H_u dot q_u. At the all-identity face configuration the two adjacent
plaquettes supply H_u=2lambda(1,0,0,0), giving 2lambda sum f_u^2.
It is not that positive expression at every configuration. This suffices
to refute the field-free identity as a general identity for lambda>0.
But OpenAI's (3.6) itself **does hold with arbitrary pins**, provided the
rotation vanishes on the pinned boundary: the source sets up precisely
that case at preliminary.tex:74–110. Replace line 308 by:
“Fields add an on-site term to (3.6); arbitrary pins alone do not.
The field extensions of the Ginibre and amplitude-association steps fail
by G1/G2. Those examples do not refute the paper's pinned charged bound.”

**7.4: HOLDS for the stated uniform conditional-sign failure, with the
following hand justification of its cited Ising input.** At alpha=gamma=0,
the first sign species is the zero-field Ising model with edge coupling b.
To see nondecay on free boxes without relying on a numerical threshold,
use b>=23/10>2. A prescribed dual disagreement contour of length m has
probability at most e^{-2bm}: flip all spins on one side of the contour.
This is an injective map of the configurations containing that contour,
and removes exactly m disagreeing bonds. The same argument applies to
an open contour ending on a free boundary, since the boundary adds no bonds.
Resolve any degree-four dual vertex consistently into noncrossing paths.
There are at most 4m 3^m closed contours of length m surrounding a fixed
site: choose their first crossing of a fixed positive ray (at most m
locations), a direction, and successive nonbacktracking steps. This is an
upper count; the factor 4 permits both choices of orientation and start.
Closed contours have m>=4. Since e^{2b}>e^4>1+4+4^2/2=13>12,
q=3e^{-2b}<1/4. The probability of any enclosing contour is at most

    p <= 4 sum_{m>=4} m q^m
      < 4 sum_{m>=4} m/4^m = 13/144 < 1/4.                 (Q4)

If two fixed bulk sites have different signs, a dual disagreement path
separates them. A closed such path surrounds exactly one of them; an
open one must cross a fixed path joining them and reach the box boundary.
If that joining path is distance R from the boundary, the open path has
length at least R. A box of side N has at most C N starting boundary
edges, so its probability is at most C N sum_{m>=R}q^m, which tends to
zero along expanding boxes with the two sites fixed. The contour flip
bound applies to each such path; other disagreement paths do not affect
the injection. Hence every subsequential free-box limit obeys

    E(sigma_x sigma_y) >= 1-4p >= 23/36 > 0

for every fixed x,y. The free laws are spin-flip symmetric, so this is
also a nondecaying covariance. This proves the particular low-temperature
fact needed in 7.4 by hand, without using a critical-temperature value.
Endpoint angles have zero Haar probability, but a bound uniform almost
everywhere would extend to them by continuity of each finite conditional
Ising integral; nearby open angle sets also violate any proposed uniform
bound once the box and separation have been chosen. Thus the null set
does not rescue uniform-in-conditioning decay.

This does **not** disprove the Newman bound for the averaged O(4) law.
Nor is uniform conditional-sign decay proved necessary for that bound.
The correct scope is: it fails as one proposed way of strengthening the
paper's proof, which instead uses averaged correlations and L1 localization.
The source explicitly makes that distinction at preliminary.tex:1104–1129.

## 5. FST-N, the first missing input, and O7(b)

**FST-N as an exact sufficient input: FAILS at line 265 (its definition),
and the implication asserted at line 267 is unsupported.** This is a
failure of formulation and deduction, not a counterexample to boundary
mixing of the O(4) model. The pin clause does not specify the expectation
being subtracted, the support/norm prefactor, the volumes, or what part
of the boundary is allowed to change. The field clause allows a field
everywhere but refers to distance “to the pins”, which it does not have.
A small field acting on the observable's own support has no distance
suppression to any remote boundary. A response statement needs two fields,
the support of their difference, its norm, and uniformity in the background
field. FST-F supplies precisely quantified covariance information of this
kind for all observables. The current FST-N does not.

Moreover, exponential pin insensitivity without the quantitative
Hamming influence sum in FST-P does not itself supply that hypothesis by
any step in this note. Charged (3.61) controls the charged component of a
test's common-left-rotation decomposition with pins; it supplies no such
estimate in an arbitrary field. It cannot simply be added to an unspecified
neutral field assertion to obtain the all-observable Newman bound.
The three sufficient inputs FST-P, FST-F, FST-T remain unproved for the
sheet. Their implications do not depend on the wording of FST-N.

Replace 7.5's asserted reduction and 8.3's last clause by:
“Control of neutral observables under pins or fields is one unresolved
issue in extending this proof. The precise sufficient input still missing
from the sheet-to-sheet argument is FST-F, alternatively FST-P (or FST-T).
No theorem in this note reduces either quantitative hypothesis to FST-N
as presently formulated.” This is the correct first-missing-input statement.
It preserves the positive conditional implications and makes no new attack.

The symmetry remark in 7.5 needs the following scope correction. For a
single-sheet common-left-invariant F, Haar averaging a.Phi(u) proves
Cov_0(F,a.Phi(u))=0. The t^2 coefficient of E_{tH}F is
kappa_3(F,W,W)/2, the **first possibly nonzero** coefficient, not necessarily
a nonzero one. But a G_T-invariant face observable need not remain neutral
as a function of one sheet after the neighbouring sheets have been fixed.
For example, the plaquette trace is G_T-invariant; setting its other three
links to 1 leaves F(q)=Re(q), a charged single-sheet function. At zero
field its response to t Re(q) at the same site is Var(Re(q))=1/4: O(4)
invariance gives four equal coordinate second moments summing to one.
Thus this symmetry remark does not remove the all-observable requirement
from the conditional-sheet proof of (17). It must not be used to claim
that the first-order effect of the *face plaquette perturbation* vanishes.

**Compatibility with row 1078 O7(b): HOLDS; no conflict.** That statement
is a sharp limitation on a perturbation estimate using only a transfer
gap and the full oscillation norm. FST-BD uses uniform conditional
influences, and FST-F/FST-P require substantial additional response bounds.
Neither is deduced here from the gap and perturbation norm. The Ising
operator in O7(b), K_0=e^{-H_0}, is diagonal and preserves configuration
labels across a transfer step; its quoted inputs give neither the positive
finite-product Gibbs specification nor the sheet influences assumed here.
There is no implication from that counterexample's premises to (C),
(D_a), (I), FST-P or FST-F. Hence the new conditional theorem does not
claim to beat the O7(b) bound within its scope. O7(c)'s open issue is also
preserved: a bound at lambda=0 on a derivative is not stability on an interval.

**Other scope corrections.** The five-dimensional sentence at line 292
is correct about four incident squares and twelve neighbours, but “the
same theorems” requires all field-size substitutions: the full-block tilt
uses e^{8lambda l^2}-1 instead of e^{4lambda l^2}-1, and the FST-F field
restriction becomes lambda<=h_0/4. Its influence sum becomes
12lambda X e^a S_a, so its half-margin interval uses
1/(24X e^a S_a). The general compact-group sentence at line 289 is valid
only with an explicit finite-dimensional unit-vector representation making
the one-link plaquette term linear with the stipulated Lipschitz bounds;
the metric diameter and field constants must be replaced where appropriate.
None of these controls supplies an anchor hypothesis. The memory-only
literature claims in 7.6 and the model recollections in 7.7 are unverified
and remain so here. They carry no conditional proof in sections 1–3 above.

## 6. Verdicts, source receipt and limits

Line numbers in this table refer to row 1091 at the pinned commit.

| Statement | Verdict | Consequence |
|---|---|---|
| M1/M2, 38–40 | HOLDS | Conditional field norm, six neighbours and the one-link Lipschitz factor are correct. |
| FST-BD (i)–(iv), 67–127 | HOLDS | Every conclusion and constant holds. Step E's erroneous limit at 123 is replaced by an upper bound; (Q1) supplies a separate covariance derivation. |
| FST-P and corollary, 135–165 | HOLDS AFTER CORRECTION | Use the measurable-kernel setting and periodic distance before taking local limits. All three influence counts and constants are correct. |
| FST-F, 169–193 | HOLDS | Positive parameters, the convex field path, S_a, (I) and the interval are correct. State scope is periodic local limits. |
| FST-T, 201–211 | HOLDS | Multilinearity, radius >=2 and real-analytic continuation are valid. |
| K3, 215–223 | HOLDS AFTER CORRECTION | Specify d_infinity as in the paper, or halve the printed rates for d_1. |
| 6.2 derivative and higher-order discussion, 225–227 | HOLDS AFTER CORRECTION | The fixed-order conclusion and rate-loss mechanism hold; delete the unproved optimal/asymptotic coefficient count. |
| G1/G2, 233–253 | HOLDS | Both hand computations give strict failures for sufficiently small positive J, not failures of mixing. |
| 7.3, 257; summary 308 | HOLDS AFTER CORRECTION | The field counterexample holds at the stated configuration. The summary's inclusion of arbitrary pins as breaking (3.6) fails. |
| 7.4, 261 | HOLDS AFTER CORRECTION | Conditional sign nondecay holds by (Q4). It refutes a proposed strengthening, not a necessary condition for the averaged Newman bound. |
| FST-N and first-missing-input claim, 265–269,313 | FAILS | First failing line 265 is not a quantified field/pin response statement; line 267 does not prove the claimed sufficient implication. Replace by the precise open FST-F/FST-P inputs. |
| Strength ordering, 63,211 | HOLDS AFTER CORRECTION | FST-P implies FST-F by (Q2)–(Q3); FST-T implies FST-F. No strictness or P-versus-T ordering is proved. |
| O7(b) compatibility, 293 | HOLDS | Additional conditional-response hypotheses avoid, rather than contradict, its sharp norm-only limitation. |

The nine correction groups, in descending consequence, are: FST-N and its
symmetry scope; the unsupported strength ordering; the Hamming application
setting; periodic-distance/local-limit wording; the K3 metric convention;
higher-order coefficient accounting; the pin-versus-field Ward summary;
the g+c limit; and field-size constants in the dimension/group controls.
Their replacement text and hand arguments are above. None supplies the
still-open small-field estimate for the actual sheet.

At fixed higher order the transverse sum in 6.2 also needs connectivity,
not a sum over all plaquettes independently: the joint cumulant vanishes
if its entries split into two independent sheet sets. Thus every contributing
insertion belongs to a chain of overlapping sheet supports attached to the
fixed observable supports. Each transverse plaquette has four edges, each
in two plaquettes; for fixed order the number of such labelled chains is
bounded independently of T. This is another finite, order-dependent factor;
it does not justify the original claimed growth rate in n.

Primary posted source: [OpenAI, Sharp mass bounds for the two-dimensional
O(4) model, Section 3 source at the pin](https://raw.githubusercontent.com/openai/math/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/build/sections/preliminary.tex).
Read ranges: 1–115 (the theorem, metric and Ward setup) and 955–1178
(charged bound, association, XY and O(4) localization). Theorem 3.1 is a
named conditional input here; its whole proof was not rechecked. The
browser fetch of the GitHub directory failed; the pinned raw source was
successfully downloaded once with curl into the new OpenAI scratch folder.
No blocked access, sign-in or paywall was bypassed.

Credit OpenAI's authors for that theorem and method; Charles Newman and
Jean Ginibre for the named covariance and correlation inequalities;
Dobrushin and Shlosman for the block-criterion mechanism; and Peierls for
the contour mechanism used in the hand check of 7.4. Credit row 1091's
Claude Fable 5.2 medium for its conditional stability argument and its G1/G2
examples. Credit row 1077's Codex and row 1078's Claude for the face law
and the corrected scope of the target. Jian Ding, Fenglin Huang and Peng
Yang's separate two-dimensional mechanism and Tadeusz Balaban's ultraviolet
work were not used as premises or rechecked. Ethan Sussman and Levent
Alpoge, with Claude and Codex as authors of their text, supply the explicitly
limited outline/account context, not a gap theorem.

The source file's SHA-256 is
`3bef38fed38bdb56710be1246497fb3c60156c2ecfe9ca1f7e9e2a7832e7a95f`.
The full source receipt is in
`/tmp/sa-gap-face-stability-check-astra.gsRtcm/source-receipt.json`.
The outline and CA-I have 32,992 and 166,711 lines respectively; only the
bounded passages named above were read. No Balaban PDF/OCR was needed.
Row 1092's literature review and row 1093's parallel check were not read.
No general mixing-to-stability theorem from the memory-only literature
paragraphs was verified or used. There was no computational mathematical
verification; hashing, fetching and text processing only record provenance.
Only this output file changed. It remains local on branch
`check/gap-face-stability-astra-20261117`; no commit or push was made.

RESULT: FST-BD holds as stated, with one proof-sentence correction; FST-P, FST-F and FST-T give the claimed conditional positive interval after the setting, metric and local-limit corrections above; FST-P implies FST-F with changed constants, while strictness and an ordering of FST-P versus FST-T are not established; K3 and G1/G2 hold at their corrected stated scope; FST-N is not a precise sufficient first missing input, and the actual sheet hypotheses and (17) remain OPEN; no conflict with O7(b), no audit status, no Yang–Mills mass gap claimed.
