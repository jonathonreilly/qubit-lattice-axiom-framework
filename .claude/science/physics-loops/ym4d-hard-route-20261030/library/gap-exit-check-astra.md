# Repo search

Codex / gpt-6-astra / xhigh, 2026-11-13. Check of FINISH row 877 at
`3e30081686bd81f30bb08178500c3e28f94d3889`; author of the checked text:
Claude Fable 5.2 max, row 861. Research text, not an audit; grants no status.
The requested `prior/gap-exit-check-astra.md` does not exist. Read
`prior/repo-search-2026-11-08.md` in full. Its thirteen targets are different;
its warnings about normalization and block-law identification remain relevant.
No `gap-exit`, `PIN-MIX`, `Higgs`, `SEED-FP` or `EXIT(` owner was found in
`open-registry.md`. This is the assigned check, not a new attack on PATH.

Searched `/Users/jonreilly/Projects/Physics` with bounded `git grep -n -i -E`
on `*.md`, `*.tex`, across all five requested refs, outside this folder too:

| Ref | Resolved commit |
|---|---|
| origin/main | 993f5e4f6d11a7e20a1cab9612c5749a53bae073 |
| pr/10114 | f76f6c649cff7dffbab664d8976e680e8f287fe9 |
| pr/10133 | 89faef229ff6e6bde42baad15ed8270c2f4087d8 |
| pr/10134 | 1e70c7211a2cdbc39001e619f1dd89db45e25851 |
| pr/10141 | c73ad7b177d94f89ff37b77386936e3d52b48b05 |

Queries: `PIN-MIX|gap-exit|Higgs.line|Proposition FREE([^a-z]|$)|Theorem LAND([^a-z]|$)|noisy.{0,20}decimation|pinned.{0,15}covariance`
(head 45); `mass.preserving transformation|thermodynamic integration|von Mises.Fisher|noisy straight|vacuum.{0,10}constant.{0,30}(normaliz|mass)|block.law statements`
(head 45). Neither reached its line cap. Earlier broad `Theorem LAND` and
vacuum-normalization queries hit caps with unrelated material; they supply
no absence conclusion. The two narrow passes found no named FREE, STEP,
HL, PIN-MIX or gap-exit check. They did find these method relatives:

| Relevant hit, source range read | Exact statement and closeness |
|---|---|
| `origin/main:docs/WILSON_STAGGERED_JOINT_PRODUCT_REFERENCE_DETERMINANT_COUNTERTERM_OUTER_HAAR_COLORED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-07-12.md:31-78` (also hits on all four PR refs) | Equation (0.2) retains the configuration-dependent normalizer inside the outer integral; L65 says vacuum constants cancel from normalized ratios. Same normalization distinction used in VAC, but a fermionic determinant law, not a proof of this torus defect. Credit and reuse the distinction. |
| `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/REVIEW_SPURION.md:289`, pointing to `BFT_B.md:373-410` (primary range read; review hit also on pr/10133) | BB-loc constructs a one-step local pinned saddle expansion; its attempted general-depth extension is explicitly withdrawn because individual terms grow like L^(2k). Different pinned saddle, not the nonlinear Wilson conditional law of STEP. No import or re-derivation. |
| `origin/main:docs/work_history/repo/review_feedback/pr8170-evidence/kept/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_IN_LEVEL_TIME_GAIN_ONE_SPIN_WAVES_LOCAL_LIMIT_CONSTANT_FINITE_PLANES_FORGET_AND_THE_SIMULATED_ALGEBRAIC_DECAY_OF_THE_INITIAL_PLANE_MEMORY_BOUNDED_THEOREM_NOTE_2026-09-16-e50aaf4b6686e647.md:92,222` (hits on all refs) | Search lines describe sphere-law moments in a different level automaton. Not read as a proof or used; they do not state the S^3 chord-Lipschitz comparison consumed here. |

Local prior inputs used, not re-proved: `gap-vmf-lip.md` Theorem V
(L59-76), its mean identity (L94-99), Corollary V1 (L209-220);
`gap-handoff-opus.md` the norm/TC (L34-58), DC*, BOX, TRUNC and PHI
(L119-167), and the corrected O-SEED/HO premises where used below.
These are credited to their authors (Codex Astra for V/V1; Claude Opus
for the handoff) and to Dobrushin for the comparison method. Verdicts
below are conditional on these named inputs; they do not repeat their checks.

The SA-index README, matching chunk-01 rows L40-57 and neighbouring
obligations L7-25 lead to outline L394-416, read directly. It proves that
mass preservation preserves sourced partition functions, while identification
of a specified block observable needs a pushforward identity. This is already
Ethan Sussman and Levent Alpoge's distinction (their text authored with Claude
and Codex). It is reused, not claimed as new. CA source checks follow below.
Tadeusz Balaban's method is credited through the account's quoted hypotheses;
no unavailable Balaban paper is imported as a checked premise.

## Check scope and checkpoint

All line references headed X mean `library/gap-exit-max.md` at the pinned
checkout. The full 883-line source was read in bounded ranges. Requested
order: FREE; K1-K4 and K4'; STEP/threshold; VAC/VAC2; HL/HL2/HL3/(6.3);
TS; K5-K8/K9/LAND; R2 and the named CA passages.
All requested statement checks are complete below. No mathematical
conclusion rests on a program or numerical run. The surviving open suppliers
are PIN-MIX/POT and an independent absolute-normalization or PATH estimate;
this check makes no new attempt on those separately scoped problems.

## Proposition FREE — HOLDS (X186-199)

For a finite torus and finite a, normalization of every kernel gives equality
of masses. The pointwise density ratio lies between exp(plus/minus a times
the chord distance), so integration gives the logarithmic bound. For a real
1-Lipschitz phi on the unit ball, both phi and the unit linear readout have
oscillation at most 2. Cauchy-Schwarz and the range variance bound give
abs(Cov) <= 1. K4 therefore gives C'_ck <= a^2/4, and summing at most
|E'| terms gives the displayed weighted bound. At a=0 the output is the
constant Z and every influence is zero. For S^1 the elementary covariance
bound gives field-Lipschitz constant 1 and C'_ck <= a^2, as stated.

**Consumer correction (X201-207, X845-849 and RESULT).** This is a bound on
`delta_c(-log rho')`, not on `w_m` in HO L50. The latter sums the separate
interaction seminorms with |X| and exponential diameter weights. No reverse
inequality is proved. Nor is it a small perturbation of the fixed Wilson
coupling beta'=1/4: at a=0, such a representation has
sum_X W_X = (1/4) sum_p x_p + constant. On a torus of side at least 3, set
all links except one to 1. The six incident plaquettes then give one-link
Lipschitz constant 6/4. Thus any such decomposition has w_0 >= 3/2,
not 0.05. One can instead use beta'=0, but that changes the claimed
interpretation. Replace “gives the zone's per-link size for free” by
“gives the total action's one-link Lipschitz bound for free.” Locality,
the actual interaction norm, and normalization still require proof.

## Lemma K1 — HOLDS (X137-146)

Each denominator is the corresponding Haar integral, including u=0;
Tonelli proves (i). Every path has the prescribed endpoints, so its holonomy
transforms by the same left and right quaternion multiplications. Their
real-linear extensions are orthogonal, preserve the average's norm, and
preserve the kernel numerator. Haar change of variables proves (ii).
The stipulated covariance of path families and weights proves (iii),
including orientation reversal. Gauge and lattice symmetry are inherited
only when the input has them, as the statement says.

## Lemma K2 — HOLDS (X148-159)

The density-ratio argument is valid for arbitrary nonnegative integrable rho
of positive mass; no continuity of rho is needed. For continuity of rho',
which its written proof leaves implicit, use N(a|u|)>=1 and
K_a(V|U)<=exp(a|E'|), then dominated convergence against rho. Symmetry of
Haar gives N(r)=E cosh(r h_1), increasing for r>=0; thus each factor is
at least exp(-a)/N(a)>0. These bounds also justify the logarithm. The claim
is for finite a, not the singular deterministic-decimation limit.

## Lemma K3 — HOLDS (X161-169)

Integrating rho'(v,V_not_c) over v removes exactly the c-kernel. The remaining
strictly positive finite integral is Z^(c)(V_not_c). Dividing gives the stated
mixture; in particular the mixing measure does not contain the omitted
kernel or its normalizer. This verifies the conditional law at every exterior.

## Lemma K4 — HOLDS (X171-184), conditional on V1

V1 gives Lip(Psi)<=a/4. Along the straight interpolation of h_k, only
exp(a<h_k,Ubar_k>) changes. Its denominator N(a|Ubar_k|) is independent of
h_k, so differentiation of the normalized integral gives exactly the
covariance in X183. The two factors a and a/4 give a^2/4. Bounded integrands
on the finite torus justify differentiation; a=0 is handled separately by
the constant output. The displayed inequality is a sufficient influence
bound, not an equality or a converse mixing theorem despite the heading.

## Lemma K4' — HOLDS (X338-344), conditional on V1

For u,u' in S^3, choose a planar rotation carrying u to u'. Its displacement
operator has norm |u-u'|, and it pushes mu_(a u) to mu_(a u'). Coupling by this
rotation gives Lip(Psi)<=1, independently of V1's a/4 bound. An antipodal
pair permits any plane through u; the same bound holds. A shortest unit-speed
arc from V_k to V'_k has length theta and theta/(2 sin(theta/2))<=pi/2.
The differentiated covariance along that arc therefore gives exactly
(pi/2) a min(a/4,1) kappa^u_ck. All pinning fields remain unit vectors.

## Lemma V-inf and Theorem STEP — HOLDS (X391-422), given V and DC*

Write v(k) for VL's a(k), to distinguish it from the pinning strength a.
The identity E_F h=v(|F|)F and |E_F h|<=1 give v(k)<=1/k for k>0.
Integrating V along the stated segment proves V-inf. In STEP, every segment
of staple fields stays in the ball of radius 6 beta about a h_l. Its distance
from zero is at least r_0=a-6 beta; interpolating exterior links on the sphere
is unnecessary here.

Remove c, let C be the symmetric matrix beta n(l,j)/r_0 on the remaining
links, and q=18 beta exp(m)/r_0<1. The boundary change at c gives
b_j=C_jc |u-u'|. DC* with D empty gives Lip(g)<=sum_j G_kj C_jc,
G=(I-C)^(-1). Conditional covariance then gives the same bound for
kappa^u_ck: both oscillations are bounded by twice their Lipschitz constants.
By the triangle inequality for the circular midpoint metric,

    sum_k exp(m d(c,k)) (C^r C_.c)_k <= q^(r+1).

Summing r>=0 gives X_m<=q/(1-q), exactly (5.1). The six staples and eighteen
partners are valid when each period is at least 3; no repeated partner arises.
This proves locality at every beta with sufficiently large a. It proves
PIN-MIX only if the additional right side of (5.1) is below 1. The final
summary must not call locality alone a proof of PIN-MIX at every coupling.

## STEP threshold — HOLDS AFTER CORRECTION (X424-438)

Replace the strict decimal cutoff `beta < 0.0384` by

    beta < 1/sqrt(216 pi)

for existence of some a>0 and some m>0 making (5.1) strictly less than 1.
The decimal is a rounded description, not the exact admissible interval.
For a fixed m>=0, put p=exp(m), r=6+18p. For a<=4, the bound is
(9 pi/4) beta p a^2/(a-r beta), minimized at a=2r beta when admissible.
Its minimum is 9 pi p r beta^2. Thus the exact threshold is
[54 pi p(1+3p)]^(-1/2). At its boundary the optimizing a is below 4,
since r<36 pi p for p>=1. For a>=4 the bound is
9 pi beta p a/(a-r beta)>9 pi beta p; this cannot enlarge the overall
range, because 1/(9 pi p)<[54 pi p(1+3p)]^(-1/2). Continuity in m gives
the asserted strict m>0 criterion. At beta=0 all influences vanish.

Independent hand check: beta=3/80 and a=48 beta=9/5 give the m=0 bound
216 pi beta^2=243 pi/800<243(22/7)/800=2673/2800<1; a small positive m
still works. Conversely pi>157/50 gives
216 pi (0.0384)^2 > 19533312/19531250 > 1.
The rounded decimal is indeed slightly too large if read literally.
The large-a limit cutoff 1/(9 pi) is correct. These are limits of this
majorant, not impossibility results for an actual output or another block map.

## Proposition VAC — HOLDS (X662-669)

Let H_T(V)=beta' sum_p x_p(V)-sum_X W_X(V). Integrating
r'_T=exp(-E_T+H_T) gives log Z_T=-E_T+F_T. This proves (i), subtraction
proves (ii), and evaluation at V_0 proves (iii), with the printed signs.
The scalar E_T is fixed only after the potential H_T has been fixed.
No locality, decay, or constructive formula for E_T follows from this algebra.

## Corollary VAC2 and its EXIT equivalence — FAILS as written (X671-694, X750-762)

The displayed inequality and (a) HOLD, conditional on corrected O-SEED:
with Delta F=rho^4 F_n-F_(rho n) and Delta E=rho^4 E_n-E_(rho n),
Phi+Delta E=Delta F. O-SEED applied with E=0 bounds Delta F by delta_loc.
TC and the norm give |Delta E|<=8(rho n)^4 e_m exp(-mn/3).
Clause (c) also HOLDS for a fixed potential. Clause (b) is the valid
contrapositive only with a common positive rate and uniform constants along
the family, including the cutoff. Mere finiteness on each torus is insufficient.

The first unsupported reverse implication is X681, “clause (E2) ... is
equivalent to the conclusion.” A bound on one scalar difference is not the
termwise TC condition with its norm. X760 strengthens this to the literal
`EXIT <=> (POT) and Phi exponentially small`, without supplying the converse.
This stronger claim is false for EXIT as defined in HO L261-265.

Hand counterexample to that converse: take, for every cutoff K and torus T_n,
r_(K,T)=exp(K n^4), constant against Haar. Kernel (N), with any fixed finite
a>0, leaves this density constant, since each input-link kernel integrates
to 1. Then p'_T=1 satisfies POT with beta'=0, W=0 and uniform zone constants;
Phi=0 identically. Yet E_T=-K n^4 and

    |E_T| <= sum_X |E_X| <= 4 n^4 e_m

forces e_m>=K/4 in that representation. No alternative uniformly bounded
beta', w_m, e_m can cure this: |log Z_T|/n^4 is bounded by
6 beta'+4 w_m+4 e_m for any HO datum, whereas here it equals K. Thus the
uniform EXIT norm fails although the stated right side holds. The example
is a finite analytic density, not a numerical construction.

**Replacement that HOLDS.** Given POT, the absolute-normalization defect is
Delta E=Delta F-Phi. EXIT implies the small-defect conclusion. Conversely,
a small scalar defect alone does not establish the stated EXIT datum.
An independently proved bound on Delta E, or equivalently on the anchored
unnormalized integral's defect once POT is known, is still required by HO.
For normalized p', O-SEED bounds its identically zero partition defect;
it yields no bound on the original Phi. The equation in X757-758 follows
from A_T=Z_T p'_T(1), TC tails and the local F bound. Endpoint POT does not,
by itself, bound every intermediate pinning strength in X693-694.

This preserves the useful warning: normalized softening plus HO alone
cannot prove the seed. It does not show every “soft step then HO” proof is
circular. A separate normalization estimate could supply the missing input.
Indeed, the text's following path proposals aim to supply exactly that input.
Common extensive constants may be exempted in a weaker sufficient version
of HO, since they cancel, but that is not the literal EXIT equivalence printed.

## Theorem HL — HOLDS (X462-481)

Use the normalized product measure nu_a with one-link density
exp(a x(U_l))/N(a). Then A_T(a)=nu_a(exp(beta sum_p x_p)) and
A_T(0)=Z_T. Finite-volume differentiation gives
(log A_T)'=4|T|[mu_a(x(U_l))-N'/N]=4|T|e_T(a).
For every neighbourhood of 1, its nu_a one-link complement has exponentially
smaller weight than a smaller neighbourhood of 1; hence nu_a tends to delta_1.
Continuity of the bounded Wilson density gives log A_T(infinity)=6 beta |T|.
The fundamental theorem of calculus proves the improper integral and (6.1).
Subtraction at the two sizes gives the minus sign and coefficient
-4(rho n)^4 in (6.2). At beta=0, A_T=1 and e_T=0 identically.
This is a finite-volume identity; its limit gives no cutoff-uniform bound
without additional estimates.

## Lemma HL2 — HOLDS (X483-497), given V and DC*/BOX

For beta>0 and a>=78 beta choose exp(m)=(a-6 beta)/(36 beta)>=2.
The weighted influence sum is exactly bounded by 1/2. The added one-link
pinning does not change the plaquette interaction range. Under the box
marginal, every kernel outside the seam strip of width 2 agrees with the
small-torus kernel by the tower property. A link with midpoint within 1/2
of the seam's antipode has distance at least n/2-1/2-2=d_n from that strip.
Translation and direction symmetry permit this link for e_T. DC* gives

    |e_n(a)-e_(rho n)(a)| <= 2 [36 beta/(a-6 beta)]^(d_n).

Set x=(a-6 beta)/(36 beta); then da=36 beta dx and the lower endpoint is 2.
Integration is exactly 72 beta 2^(1-d_n)/(d_n-1). For n>=8, d_n>=3/2>1,
so the integral is finite. At beta=0 both means coincide for every a;
the bound is zero, handled separately before dividing by beta.

## Corollary HL3 — HOLDS (X499-509), given the same inputs

V1 bounds each single-plaquette partner by beta/4 uniformly in the pinning,
so the weighted sum is (18 beta/4) exp(m)=alpha. The same box comparison
bounds the integrand on [0,78 beta] by 2 alpha exp(-m d_n)/(1-alpha).
Multiply by this interval's length, add HL2's tail, and multiply by
4(rho n)^4 from (6.2). These are exactly the printed constants and signs.
Beta<2/9 permits m>0, with beta=0 again giving the zero identity.
The claim concerns the bare Wilson model, not the account's level-K density.

## Identity (6.3) — HOLDS (X707-712)

For the bare Wilson normalization used here, Z_T(0)=1 and
(d/db)log Z_T(b)=6|T| mu_(T,b)(x_p). Translation and hypercubic invariance
identify the six plaquette orientations. Integrate from 0 to beta and
subtract; the common volume factor is (rho n)^4 and the sign is the
small-torus mean minus the large-torus mean. This is HO's existing PHI
identity specialized to W=0, not a new estimate of its integrand.

## Lemma TS — HOLDS (X727-735), given the stated trace representation

Let q_j=lambda_j/lambda_0 in [0,1], counting the top eigenvalue once,
and assume the traces in the statement exist. Put A_t=sum_j q_j^t=1+S(t;B).
For integer rho>=2, sum_j(q_j^n)^rho <= (sum_j q_j^n)^rho and A_(rho n)>=1.
Therefore

    0 <= rho log A_n-log A_(rho n) <= rho log A_n <= rho S(n;B).

The lambda_0 terms cancel exactly. Apply this inequality to successive
lengthenings of the four sides, with telescope multipliers rho^3, rho^2,
rho, 1. The four resulting upper coefficients are rho^4, rho^3, rho^2, rho,
with precisely the three-dimensional boxes printed in TS. Degenerate top
eigenvalues cause no problem when included in S. Neither this inequality
nor the telescope supplies the required bound on the number of states.

## Lemma K5 — HOLDS (X214-224)

Centrality makes the matrix Fourier coefficient scalar. Expand exp(a chi_(1/2)/2)
in its uniformly convergent power series. Every tensor power has nonnegative
integer character multiplicities, and spin j occurs in the 2j-th power.
Thus its normalized coefficient lambda_j is strictly positive for a>0.
The character bound |chi_j|<=2j+1, strict on an open set of positive Haar
measure, gives lambda_j<1. The change v=w u then gives the claimed matrix
identity, and product conditional independence gives Lambda(A'). For a
trivial representation the coefficient is 1. The recalled Bessel quotient
is unnecessary and is not used in this check.

## Lemma K6 — HOLDS (X226-235)

Expand the trace of the ordered product into matrix elements. Each distinct
coarse link contributes its K5 coefficient once. Inverse orientations give
the same real coefficient by inversion symmetry of f_a. Disjoint link
supports make the conditional product factorize, and subtracting the two
means proves the covariance identity. The same reasoning covers linear
combinations such as the loop characters used in K9. Reused links or
overlapping observables are outside the statement and need not factorize.
The following decay-rate sentence is valid for fixed loop shapes, fixed
finite a>0 and fixed L, with distance measured in the corresponding units;
it is not a cutoff-uniform assertion when these quantities vary.

## Lemma K7 — HOLDS (X237-238)

Applying Tonelli and kernel normalization separately to each positive
centre-twisted density preserves its mass, and therefore its ratio to the
untwisted mass. This asserts nothing about whether the image is the usual
local twist of the untwisted output potential.

That distinction is essential for the later frozen-group argument in Steps 4
and 8. Untwisted Dobrushin mixing alone cannot force a twisted mass ratio to 1.
Multiplying a second input by any positive scalar changes its mass ratio
without changing either normalized law or any influence coefficient. Thus
that argued inference needs an additional identified twist family and its
absolute normalization; K7/LAND do not supply it. No conclusion about Q_8,
2T or U(1) phases is established by this check.

## Lemma K8 — HOLDS (X240-251)

The stipulated pair of planes through coarse sites requires an even coarse
period in the reflected direction. With that geometry, straight paths of
positive-half coarse links stay in the closed fine positive half. At fixed
V_0, integrate the independent positive and negative coarse links. Reflection
covariance identifies the negative integral with conjugate(theta G).
Boundary paths lie in the planes; hence P_0 is positive and theta-fixed.
Absorb its square root into G and apply the assumed fine reflection positivity,
then integrate V_0. This works for bounded measurable F', since the kernel
is bounded on the finite product. It proves precisely these site reflections.
It supplies no statement for tube averages or for an arbitrary account block law.

## Corollary K9 — HOLDS (X257-268), given DC*

Condition on D, the links of the second loop. Off D, the output kernels
are unchanged, so DC* applies with b=0 and delta_D(f)=0. It gives
2 alpha Delta(f) exp(-m d)/(1-alpha). For chi_(1/2), Delta(f)<=2|C_1|
and |g|<=2. Multiplication and expectation give
8 alpha |C_1| exp(-m d)/(1-alpha). K6 divides this by the two nonzero
loop factors, producing the printed bound. No column-sum assumption or
cardinality factor |C_2| is missing. For a=0 the division is unavailable;
the standing straight-kernel hypothesis here is a>0. At alpha=0 the
covariance vanishes, consistently with the formula.

## Theorem LAND — HOLDS AFTER CORRECTION (X354-360)

Add explicitly: each input rho_T is nonnegative, integrable, of positive mass,
and gauge invariant; the kernel is (N) or (D_a) with fixed finite a>0 and
straight paths; use the reflection geometry of K8 for (v). The intended
first-passage application needs this gauge premise verified for its actual
input. PIN-MIX alone, as literally named in the theorem, does not imply it.

To see the necessity, take L=1 and the product input
rho(U)=exp(b x(U_c)), b>0, on one distinguished link, Haar on the others.
All pinned cross-covariances vanish, so PIN-MIX holds. Its output on that
link is N(|a V_c+b 1|)/N(a), nonconstant, whereas a gauge-invariant density
on a single independent link must be constant. Thus (ii)'s gauge assertion
needs K1(ii)'s input hypothesis. This is an explicit analytic counterexample
to omitting that premise, not a counterexample to the intended gauge model.

With the added premise, (i)-(iii) follow from K1, K2 and K4'; (iv) follows
from K9 and (v) from K8. Smoothness follows by differentiating the finite
kernel integral: every derivative has an integrable bound against rho.
The theorem still proves neither POT nor the vacuum-consistency clause of
EXIT. Real covariance decay is not, without another argument, a convergent
complex cumulant expansion with the required interaction norm.

## Step R2: the imported witness — HOLDS as a conditional input (X609-625)

Directly read CA-I L2715-2826, after the SA-index witness rows and their
neighbours (chunk-06 L93-107); the outline's corresponding L6953-6962 was
read only to keep the two formulations distinct. CA-I uses the lattice
reference kernel K_s^star, not the continuum inverse-eighth-power kernel.
It explicitly states the two kernel bounds, zeta' in [2/3,4/3], |R|<=1/2,
and the positive lower bound with coefficient (2/9)b_0 c_K xbar_s^(-2).
Its constants are independent of K and g_0. Keep g and d fixed, theta fixed,
s=s(d) above all three depth floors, K-s>=k_W, and an admitted torus m.
The witness is not available outside those hypotheses.

The observable is exactly sum_p f(x(p))[1-x_p], by CA-I L101-102 and
L202-221; there is no extra a_K^4 factor. W-phys-CA in
`gap-sdcyl-ca-astra.md` L173-240 is reused as the already owned conditional
port. Its lower bound on S_ev and upper bound on the even gap do not prove
a positive gap. No outline/account first-passage dictionary is assumed here.
Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of the account; Balaban's hypotheses remain premises where the account says so.

## Step R2, Bearing 1 — HOLDS (X627-634), given W-phys-CA

The even sector is a sub-sum of the nonnegative full thermal sum. Hence
rho_CA^(2A/(3d))<=S_ev<=S<=t<1. Taking logarithms, with
rho_CA=c_K/(3C_K) in (0,1/3], gives the printed necessary lower bound on A.
For d<=1/40 its right side is at most (3/80)log(1/t)/log 3.
At t=1/5041, the exact integer comparison 5041<3^8=6561 makes this
strictly less than 3/10. The physical time at a post-first-passage landing
is at least one coarse spacing, hence at least one first-passage unit.
This particular necessary constraint is therefore nonbinding. It does not
supply an exit estimate or exclude other obstructions.

## Step R2, Bearing 2 — HOLDS AFTER CORRECTION (X636-648)

The stated exclusion of a cutoff-uniform bare-scale noise landing HOLDS,
conditional on the CA witness and on unbounded admitted cutoffs. The tents
in the existing port have height r=d/4 and supports separated in the time
coordinate by at least 5d/2. For a_K<=d/8, each support contains at most
6(d/a_K)^4 plaquette centres: enclose it in a cube of side d/2, count at
most d/(2a_K)+1<=d/a_K sites in each direction, and allow six orientations.
Each cross-support plaquette pair has disjoint links and midpoint distance
at least 5d/(2a_K)-2. K9 for two four-link loops, divided by four because
x=chi_(1/2)/2, gives 8 alpha/(1-alpha) times lambda^(-8) times the exponential.
Multiplying by the two point counts and by r^2 gives exactly X645's RHS.
The CA lower bound gives its LHS. With fixed admissible g,d,s, the LHS is
strictly positive and independent of K, while a_K^(-8) exp(-c/a_K) tends
to zero. The contradiction is valid; no numerical limit evaluation is needed.

**Correction at X647.** Delete “a landing must sit at a block scale that
grows like L^K in bare units.” The argument excludes only (N), L_block=1,
with cutoff-independent a, alpha<1 and m>0. It proves no quantitative lower
bound on a general decimation scale. K6 for L_block>1 controls coarse loop
holonomies, whereas this witness is a sum of bare plaquettes. The account
expressly withholds the needed block-observable identification. Even an
inequality involving a_K^(-8)exp[-c/(a_K L_block)] would not by itself
force L_block comparable to a_K^(-1), because of the polynomial prefactor.
The corrected conclusion is the bare-noise obstruction just proved.

## Step R2, Bearing 3 — HOLDS as a locator map (X650-654)

The named passages match: CA-I L98-112 and L406-420 give torus side 2L^m,
bare spacing L^(-K), and shifted sites; L678-686 gives the first-passage
window and its admitted quantifiers; L202-221 and L727-738 give the observable
and connected function. CA-II L140995-141056 states trace subadditivity for
mirror-periodic sources with even cell counts. L61205-61232 begins the
complex-cell chessboard estimate and explicitly invokes antipodal link-plane
reflection positivity. These are locators and stated inputs, not a new check
of those full account proofs. The account's site shift and bare-coupling
normalization have not been silently identified with the outline's notation.

## Account scope used by R2 and Step 7 — HOLDS AFTER CORRECTION

**CA-I L2555-2561, extended through L2595.** The account expressly excludes
block laws from Theorem 0 and says the block-law proofs are outstanding.
It nevertheless states them elsewhere: Remark 3.2, L3352-3392, defines
nu^B_(K,s) and states a block-law comparison. Thus replace “the account gives
no block-law statement” by “Theorem 0 supplies no proved block-law comparison
or pinned-mixing input for this application.” The exact mass identity at
L2582 and exact-insertion identity at L2583-2595 do not supply PIN-MIX,
reflection positivity of rho_K, or a global small interaction norm.
The representation in (i-a) is analytic only on its specified hereditary
domains and retains history operations. This supports the restricted reading
in X790-799, not a claim that block laws are absent from the book.

**CA-II L141276-141386, with the proof's opening L141387-141420.**
The ca-full index L1133-1139 labels the vacuum-density lemma PROVED; its
source explicitly assumes (a)-(c). It assumes the local E/R format,
exponential tree bounds and a half-rate summability constant; common running
g_j,z_j; and an exact bijection of non-wrapping domains carrying equal
numbers. It concludes a bound on the difference of vacuum-energy densities,
uniform in K,g_0,g,m,m'. These are precisely conditional premises, not
consequences of an arbitrary probability kernel. The non-wrapping threshold
is L^min(m,m') L^(K-j-1)/(2M)-2, as X811-812 records.

Retain a missing qualification from hypothesis (a): E_m is Balaban's bare
normalization constant **less the Gaussian normalizers of the K steps**.
Those Gaussian normalizers are compared by a separate determinant lemma.
The local terms are evaluated at U=1, and the count terms are exactly
extensive, but this passage alone does not identify the full output
normalization with VAC(iii) or furnish EXIT's particular link-set norm.
It also does not bound the remaining level-K integral's defect. The asserted
stronger exponentially decaying size variant in X809-813 is marked ARGUED
and unwritten; it is not a checked EXIT supplier here.

The cited Balaban format is credited to Tadeusz Balaban through these exact
account hypotheses and `lit-balaban.md` L139-147. The account's authors are
Ethan Sussman and Levent Alpoge, with Claude and Codex. No Balaban paper,
no account package behind these hypotheses, and no O(4), continuum gap,
or order-one mixing theorem was re-proved in this check.

## Provenance and limits

The source revision `31a47c543775` is supplied by the task. The source
directory is not a Git repository: `git -C .../sa rev-parse HEAD` failed,
so that revision was not independently verified. The exact on-disk texts
read are identified by these SHA-256 hashes (streamed bookkeeping only):

| File | SHA-256 |
|---|---|
| gap-exit-max.md | `40dff6cbeae21051ee6b5758ad4bacee47b9704f0b91f7686549ca254fa8efba` |
| gap-vmf-lip.md | `b920a387aa8da19e336f4efd62f84208df3f614de11223bbaa42aaf991786033` |
| gap-handoff-opus.md | `810d1d3c248f190cb4155d44e0cf5dcc56b9cb065c82bf669916f7b22c85e018` |
| gap-sdcyl-ca-astra.md | `c322bf1b7bf0f8635dd33d82f4ded6b0d1a5b82c678b4fe9ff21da908ae6b4e8` |
| YM4_sketch_500.tex | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| theorem_0_complete_account_raw_I.tex | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| theorem_0_complete_account_raw_II.tex | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |

Not covered: re-checks of V/V1, DC*, the full O-SEED/HO or W-phys-CA
proofs, the underlying CA packages, the unrequested Gaussian illustrations
and flat-pinned transfer construction, or the recalled phase claims.
No numerical proof computation, formal proof run, audit update, registry edit,
source repair, commit, push, or external post was performed. Only this
requested report was written in the checkout. The working branch and pinned
science text were preserved; the report is local and uncommitted.

RESULT: VAC2's literal EXIT equivalence FAILS; FREE, K1-K4', STEP, VAC, HL/HL2/HL3, (6.3), TS and K5-K9 HOLD under their stated inputs, with the STEP threshold corrected to beta < 1/sqrt(216 pi); LAND and R2 Bearing 2 HOLD AFTER CORRECTION; FREE's zone-size interpretation, the twisted-sector inference, and the account summaries require the corrections above. Normalized softening alone supplies no seed, and no order-one EXIT or mass gap is established.
