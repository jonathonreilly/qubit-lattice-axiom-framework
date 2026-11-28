# Repo search

The target-specific prior file is absent at `11d4c8dc1`. The lead's
`prior/repo-search-2026-11-08.md` records older RG searches, not a check
of row 754. Its closest hit is PR 10114's
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`.
I fetched that PR and read its setting and Section 2 through line 165.
It proves a positive one-step loop correlation with a cutoff-dependent
bound. It supplies neither EP nor the flux-fusion bound checked here.
Credit that earlier Codex construction; it is not reproduced below.
Main's workflow was read at `a527a6fdaeb22ef8a0d1224cc2ba7bc42c48d3bc`;
PR 10114 is `f76f6c649cff7dffbab664d8976e680e8f287fe9`.

The direct prior work is already in the requested inputs. Claude Fable
5.2's `gap-means-max.md` constructs S_0 and supplies the sector algebra.
Codex's `gap-means-max-check.md:249–424` gives the hand proof of its
topology and Haar integral. `gap-means-astra.md:112–373` supplies the
earlier, different loop-cone obstruction and the local-density argument.
Claude Opus 5.5's `gap-es1-opus.md`, Sections 1, 2 and 5, supplies the
fusion consumer. These results are reused with their hypotheses.
The registry, open-core and l17c searches found no duplicate owner for
this check. No new attack on LOC, magnetic fusion or a seed is opened.

The outline/account indices were searched first for loop equations,
Schwinger–Dyson, association, Ginibre, projective surfaces, thermal sums
and fusion. No matching target statement was located. Nearby transfer,
quaternion and Ward rows concern different statements; exact source
ranges are recorded at the end. This is a bounded comparison, not a
claim of novelty. Credit Ethan Sussman and Levent Alpoge, with Claude
and Codex as authors of their outline/account text, for that framework.

Codex; task assignment `gpt-6-astra / max`, FINISH row 756. Checked text:
Claude Opus 5.5, `gap-loop-eq-opus.md:1–271`, at
`11d4c8dc15fd370a0c9829e7e93b082c068dcb93`.
Research check, not an audit; grants no status. All mathematical checks
below are written arguments. No script, enumeration or numerical value
discharges a step.

## Verdicts

Line numbers in this table refer to `gap-loop-eq-opus.md`.

| Statement | Verdict | Scope or correction |
|---|---|---|
| Lemmas 1.1–1.2, lines 41–61 | HOLDS | Coefficients 3 and m(m+2), with the printed splitting coefficient |
| U(1) equation, lines 63–67 | HOLDS | Real cosine Wilson loops; no splitting term |
| E1, E1', E2, rectangle/chair, figure-8 and E3, Section 2 | HOLDS | Under the stated symmetry; E3 is independent of clover ordering |
| Ordered clover equals the 2-by-2 loop, Section 2.5 | HOLDS AFTER CORRECTION | Reverse the order specified by “first leaves, second enters” |
| Lemma 3.1, lines 105–111 | HOLDS | Require finite, positive variance; this is a lower bound on the thermal sum |
| EP-NO(a)–(c), lines 119–131 | HOLDS | Given the existing hand proof of S_0; same bound for the positive even-state mixture |
| U(1) and Z_2 satisfy EP, line 135 | HOLDS | Ordinary periodic measures, nonnegative couplings; hand arguments below |
| Lemma 5.1, lines 147–153 | HOLDS AFTER CORRECTION | Declare the change from the imported action normalization |
| Corollary 5.2, lines 155–165 | HOLDS AFTER CORRECTION | Same normalization; the even insertion includes twist signs |
| Proposition VB, lines 171–175 | HOLDS AFTER CORRECTION | Common symmetries and a common local trivialization; conclusion is only about feasible-state diameter |
| Required radius about a/2, lines 177 and 244 | FAILS | Neither VB nor the stated exponential heuristic implies this |
| Proposition CR, lines 183–191 | HOLDS | Unweighted absolute row sums of the specified formal equations |
| No strict contraction of that raw map | HOLDS | Its rows with m at least 4 have norm at least one |
| Positivity cannot repair the method, line 193 | FAILS | Not a consequence of the row count or convexity |
| Remark 6.1, lines 199–201 | HOLDS | Conditional sufficiency for any fixed positive exponent, with small even sums at all required shapes |
| Product-rule Lemma 6.2, lines 203–207 | HOLDS | Given PK and the stated symmetry/positivity inputs |
| Corollary 6.3, displayed bound, lines 209–213 | HOLDS | The maximum, including its exponential term, must remain |
| Corollary 6.3 supplies pure F-h_gamma | FAILS | PK and LOC alone do not remove that term; explicit counterexample below |

## 1. Ward equations, shapes and the spectral inequality

Put \(f_A(U)=\tfrac12\operatorname{tr}(UA)\), and let
\(\Gamma_e(f,g)=\sum_a d_af\,d_ag\).
The Pauli completeness identity gives, directly in normalized units,

\[
 \Delta_e f_A=-3f_A,\qquad
 \Gamma_e(f_A,f_B)=\tfrac12\operatorname{tr}(B^{-1}A)-f_Af_B.
\]

Thus \(E(\Delta_e f+\beta\Gamma_e(f,h_e))=0\) proves Lemma 1.1.
Reversing the loop handles a single inverse passage. For m equally
oriented passages, a pair of distinct insertions in the second derivative
contributes \(-2W(C)-4W(XY^{-1})\). The m diagonal insertions give
\(-3mW(C)\). Consequently

\[
 \Delta_eW(C)=-m(m+2)W(C)-4\sum_{i<j}W(o_{ij}),
\]

and the drift is
\(\beta\sum_{p,i}[W(C\ominus_i p)-W(C)x_p]\).
This checks the sign, normalization and all m in Lemma 1.2. Here every
W, including the splitting loop, is a half trace. The coefficient is
the highest-spin Casimir; the general loop word is not a pure Casimir
eigenfunction, which is why the splitting terms remain.

For U(1), write the loop angle as \(m\theta+\alpha\).
Its second derivative is \(-m^2W\), and
\(m\sin(m\theta+\alpha)\sin(\theta+b)
=m[\cos((m-1)\theta+\alpha-b)-W\cos(\theta+b)]\).
This proves the printed Abelian equation. It is not the SU(2) equation
with its splitting terms discarded while retaining its Casimir.

For the shape checks, the useful separate calculation is

\[
 \Delta_e x_p^2=2-8x_p^2,\qquad
 \Gamma_e(x_p^2,x_{p'})
 =2x_p[W(R_{pp'})-x_px_{p'}].
\]

It gives E2 directly, including the self-plaquette term \(x_p-x_p^3\).
E1 follows from its one trivial, one rectangular and four chair
deformations. Summing before applying \(E h_e^2\ge(Eh_e)^2\) gives
E1' with the stated coefficients. At zero coupling the independent
Haar holonomies give \(E_0x_p^2=1/4\) and the other incident pair
moments zero; E1 therefore gives \(w_1=\beta/4+O(\beta^2)\).
The rectangle equation is the same replacement of its short-end link.
The figure-8 identities follow from Cayley–Hamilton in dimension two.

**The clover order needs correction.** For counterclockwise plaquette
paths, the source's “first leaves, second enters” condition orders the
quadrants NE, SE, SW, NW. Cancellation in the product instead needs
NE, NW, SW, SE: the first *enters* O on the shared link and the next
*leaves* O on it. Two factors hide this error because their traces
commute cyclically; four factors do not.

Set the four radial links to I. The two exterior edges of each quadrant
can realize its holonomy independently. Assign, in the printed order,
\(U_{\rm NE}=i\sigma_1\), \(U_{\rm SE}=i\sigma_2\),
\(U_{\rm SW}=i\sigma_3\), \(U_{\rm NW}=I\). Then

\[
 \tfrac12\operatorname{tr}(U_{\rm NE}U_{\rm SE}U_{\rm SW}U_{\rm NW})=1,
 \qquad
 \tfrac12\operatorname{tr}(U_{\rm NE}U_{\rm NW}U_{\rm SW}U_{\rm SE})=-1.
\]

The second trace is the outer boundary trace. In the corrected order,
successive radial edges cancel, leaving a stem and its inverse around
the boundary. The claimed traced equality then holds. E3 is unaffected:
writing the quaternion sum as
\(Q=q_0I+i\boldsymbol q\cdot\boldsymbol\sigma\) gives
\(\tfrac12\operatorname{tr}QQ^*=q_0^2+|\boldsymbol q|^2\ge q_0^2\),
which proves E3. That argument also works on the maximal torus.

For Lemma 3.1, the spectral measure of
\((O-E O)\Omega\), divided by its squared norm, is a probability
measure on the even excited ratios in [0,1). Its t-th moment is
\(C_O(t)/C_O(0)\). A convex combination is at most the unweighted
sum \(S_{\rm ev}(t)\), and Jensen bounds it below by its first moment
to the power t. This applies to \(O\in L^2(\Omega^2dU)\), with
\(0<C_O(0)<\infty\). The ES consequence at t=a has the correct direction.

## 2. EP-NO and the Abelian comparisons

**No re-enumeration of S_0 is needed.** The existing hand proof gives
92 faces, 184 edges, one vertex-link cycle everywhere, and

\[
 E_0\prod_{p\in S_0}x_p=-2^{-183}.
\]

The one-cycle hypothesis added in the previous check is satisfied.
The source uses that actual Haar integral, not just the sign of a
coefficient in a positive-coupling expansion.

The dual graph is connected. Its cut between M and A+C therefore
contains an edge. That link occurs exactly once in each partial
product. Integrating it against Haar gives \(E_0F=E_0G=0\).
Thus EP-NO(a) follows from the cited hand result.

For (b), at most \(6\cdot184=1104\) action terms meet those links.
Conditioning on the exterior gives log-density oscillation at most
\(u=2208\max_p|\beta_p|\). For each of F, G and FG the difference
from its Haar moment is at most \(d=e^u-1\). At the stated ceiling,
\(u<2^{-185}\) and \(d<2^{-184}\); for example use
\(e^u-1\le u/(1-u)\le2u\) when \(u\le1/2\). Hence

\[
 \operatorname{Cov}(F,G)
 \le-2^{-183}+d+d^2
 <-2^{-183}+2^{-184}+2^{-368}<0.
\]

The bound uses absolute couplings. Each electrically twisted measure
satisfies the same three moment bounds, and so does their positive
normalized mixture. Apply the covariance estimate *after* mixing.
Negative component covariances alone would not justify that step.
This verifies (c). All sides at least five supply a torus in EP's domain.

Here are hand checks of the two recalled Abelian comparisons. They
concern the untwisted EP statement, not arbitrary signed couplings.

For U(1), let H(θ)=sum_p β_p cos(k_p·θ), with integer vectors k_p.
For integer vectors A,B, put f(θ)=cos(A·θ), g(θ)=cos(B·θ).
The two-copy covariance numerator is

\[
 2Z^2\operatorname{Cov}(\cos(A\cdot\theta),
                        \cos(B\cdot\theta))
 =\int (f(\theta)-f(\theta'))(g(\theta)-g(\theta'))
             e^{H(\theta)+H(\theta')}\,d\theta\,d\theta'.
\]

The map \((u,v)\mapsto(u+v,u-v)\) is a surjective homomorphism of
the product torus and preserves normalized Haar measure by pushforward.
Each difference becomes \(-2\sin(A\cdot u)\sin(A\cdot v)\).
Expand the weight as
\(\prod_p\sum_{n_p\ge0}(2\beta_p)^{n_p}
 [\cos(k_p\cdot u)\cos(k_p\cdot v)]^{n_p}/n_p!\).
Each resulting integral is four times a nonnegative coefficient times
the square of one real integral. Absolute convergence justifies the
expansion. Finally, every product of plaquette cosines is a nonnegative
linear combination of cosines of integer linear forms. Covariance is
bilinear, so EP follows. This is Ginibre's duplicate-variable method.

For Z_2, every plaquette monomial is a character σ_A of the link spins.
In the same two-copy numerator set τ=σρ. It becomes

\[
 E_\rho\left[(1-\rho_A)(1-\rho_B)
 E_\sigma\left[\sigma_{A\triangle B}
  \exp\!\left(\sum_p\beta_p(1+\rho_p)\sigma_p\right)\right]\right].
\]

The outer factors are nonnegative. All inner couplings are nonnegative.
Expanding each factor as \(\cosh J_p(1+\sigma_p\tanh J_p)\)
gives nonnegative coefficients. Haar averaging a character gives zero
or one, so the inner expression is nonnegative. This proves the
Griffiths–Kelly–Sherman comparison needed here, including repeated powers.

EP-NO rules out the stated monomial association theorem. It does not
rule out restricted cones, cancellation-based arguments, or the still
open covariance inequality for two individual plaquettes.

## 3. Integrated plaquette shifts: two conventions must be fixed

**First correction: the imported partition function has a constant
action term.** `gap-crux-restate.md:29–35` and `gap-transfer.md:34–50`
use \(Z=\int e^{-s\sum_p(1-x_p)}dU\). For that convention,

\[
 e_B'(s)=6|B|(\bar w_\infty(s;B)-1).
\]

Lemma 5.1 instead uses \(\widehat Z=\int e^{s\sum_p x_p}dU\).
Declare this explicitly, with

\[
 \widehat Z(t,B)=e^{6st|B|}Z(t,B),\quad
 \widehat T_B=e^{6s|B|}T_B,\quad
 \widehat e_B=e_B+6s|B|.
\]

Then its formula holds for \(\widehat e_B\). With the original e,
replace the integrand by \(\bar w_\infty-1\). Neither choice changes
delta, Delta, eigenvalue ratios or eps: the volume constants cancel.

For completeness, the limiting derivative needs no unproved exchange
of limits. Put \(g_t=t^{-1}\log\widehat Z(t,B)\). The trace formula
gives \(g_t\to\widehat e_B\), and \(|g_t'|\le6|B|\).
Convexity bounds \(g_t'(s)\) between its backward and forward secant
slopes. First let t tend to infinity; then let the secant length tend
to zero at a differentiability point of \(\widehat e_B\).
This proves \(g_t'(s)\to\widehat e_B'(s)\) almost everywhere.
The common Lipschitz bound and \(g_t(0)=0\) justify integration by
dominated convergence. Thus Lemma 5.1's limit and integral are valid.

**Second correction: the even insertion is signed in a fixed seam
representation.** Write \(\sigma_p^k=\pm1\) for the electric twist
and \(q_k(s)=\widehat Z^k(s)/\sum_e\widehat Z^e(s)\). Then

\[
 \bar w_{\rm ev}^{\rm ins}(s)
 :=\frac{\partial_s\log\widehat Z_0(a;a^3)}{6a^4}
 =\frac1{6a^4}\sum_kq_k(s)
       \sum_p\sigma_p^k E_k x_p.                         \tag{3.1}
\]

It is not \((6a^4)^{-1}\sum_kq_k\sum_pE_kx_p\) in that fixed
representation. At a negatively signed plaquette the derivative
inserts \(-x_p\). In the original action convention the derivative
also contains −1. Calling (3.1) a mean plaquette is legitimate only
with this insertion convention, or after transporting each insertion
to a local chart with the seam outside it.

With these conventions the exact formulas are

\[
\begin{aligned}
 \delta&=48a^4\int_0^\beta(\bar w_a-\bar w_{2a})\,ds,\\
 \Delta(c,d)&=12a^2cd\int_0^\beta
  [\bar w_\infty(s;a,c,d)-\bar w_\infty(s;2a,c,d)]\,ds,\\
 \log(1+\epsilon)&=6a^4\int_0^\beta
       [\bar w_{\rm ev}^{\rm ins}(s)-\bar w_a(s)]\,ds.
\end{aligned}                                                   \tag{3.2}
\]

The last identity uses \(\widehat Z_0(0)=1\), including its factor
1/8. The first coefficient is \(a\cdot8\cdot6a^3\); the second
is \(a\cdot2\cdot6acd\). Section 7's two integral tests therefore
hold with (3.1). Their integrals are nonnegative by Lemma K and the
even spectral sum. This gives no pointwise sign for either integrand.
Also, the eps tolerance is \(\log(1+10^{-7})/(6a^4)\), not the
delta tolerance \(10^{-7}/(48a^4)\) repeated verbatim.

## 4. What VB and CR actually exclude

**VB has a valid common-constraint statement after specifying its
state class.** Use only symmetries shared by the states: translations,
coordinate reflections and spatial cubic permutations. An infinite-time
cylinder has a distinguished time direction. Full four-dimensional
axis exchange is not a symmetry supplied by its geometry. The even
projection also singles out time. Section 2's stronger equivalence of
all six incident plaquettes must not be imported here.

Use a common contractible patch and place electric seams outside it.
Equivalently transport both observables and twist signs under seam
changes. Moving a seam through an observable does not leave its raw
Wilson function unchanged. In this local convention every incident
action term is the ordinary Wilson term, so the local Ward identities
hold. The cylinder inherits them by the finite-time limit on fixed
supports.

The temporal Gram positivity can also be justified, rather than assumed
from the positivity of a twisted partition function. Integrate a
half-cylinder insertion F into its boundary-to-boundary operator A_F.
Simultaneous centre flips on its boundary fields leave contractible
loop insertions unchanged, so A_F commutes with P_0. Reflection gives
the adjoint operator. Unoccupied time intervals supply nonnegative
powers of T. Thus the even thermal reflection form has numerator

\[
 \operatorname{Tr}(P_0 A_F^*T^vA_FT^u)
 =\|T^{v/2}A_FT^{u/2}P_0\|_{\rm HS}^2\ge0,
\]

with boundary half-weights included in A_F. Linear combinations give
the full Gram matrix; the cylinder limit gives the vacuum version.
This uses the Wilson transfer representation, not positivity of an
arbitrary convex mixture of reflection-asymmetric measures.

A patch of radius r with its stated plaquette margin embeds when
the periods are at least 2r+3. These observations prove the corrected
inclusion of those states in the same local feasible set. A bound
using only two copies of that set must bound *every* pair in it.
That is VB's valid conclusion. It supplies no numerical lower bound
on the diameter and no impossibility theorem for a useful bound.

**The radius conclusion fails.** Even granting the unproved heuristic
that a relevant shift is comparable to \(C e^{-mL}\), comparison
with the stated tolerance would give

\[
 2r+3\ \gtrsim\ \frac1m\log(48C\beta\,10^7 a^4),
\]

not \(a+m^{-1}\log(48a^4\beta10^7)\). There is no source for the
extra a. For fixed m this expression grows logarithmically with a.
A lower comparison constant, control along the coupling integral and
any relation between m and the chosen seed size are also missing.
At beta zero the local one-passage equation even fixes every plaquette
mean to zero. Thus the unqualified assertion that local equations
cannot bound these shifts is false. No conclusion about the necessary
radius at order-one coupling follows from VB alone.

**CR's coefficient count holds for the specified formal map.** Before
absorbing products into the left side, the drift has 6m deformation
terms and 6m merger terms, each of absolute weight beta/2. The split
terms have total weight \(4\binom m2\). Dividing by m(m+2) gives

\[
 \theta_m=\frac{2(m-1)+6\beta}{m+2}.
\]

For U(1) the denominator is m² and the split terms are absent, giving
\(6\beta/m\). The listed values for m=1,2,3,4 follow. Rows with
m at least four prevent a strict contraction of this unweighted map
on unrestricted loop coordinates. This does not exclude elimination,
different equations, a weighted norm or restrictions to realizable
moments. The displayed equations also do not cover mixed orientations
without further identities. At beta zero no merger iteration occurs;
the splitting identities instead permit Haar degree reductions.

The assertion that positivity cannot improve a difference bound is
not justified. For example, the Gram constraint
\(\left(\begin{smallmatrix}1&w\\w&q\end{smallmatrix}\right)\ge0\)
with fixed \(0<q<1\) bounds the diameter of allowed w's by
\(2\sqrt q<2\), while leaving many allowed values. Small diameter
is not uniqueness, and need not be known before imposing positivity.
This example refutes the stated convexity inference; it proves no
Wilson contraction. CR does not settle a positive-solution bootstrap
at order-one coupling.

## 5. Fusion: the valid implication and the retained exponential term

**Remark 6.1 holds as a conditional estimate.** From the twelve heavy
and four light bounds one obtains
\(\eta_L\le6KS^\gamma+2KS\). Theorem V(b) then gives exactly

\[
 \Delta(c,d)\le12KS^\gamma+4KS+S'_{cd}
 \quad\text{when }6KS^\gamma+2KS\le\tfrac12.                \tag{5.1}
\]

Theorem V(b)'s lower trace estimate keeps the four light top
eigenvalues and uses \((1+s_z)^{-2}\ge1-2s_z\) and
\(p_z^2\ge2p_z-1\). There is no reversed trace inequality here.
Adding the three deficits with coefficients 4,2,1 yields seven times
the maximum of the right sides in (5.1).

Here is a precise version of “any positive exponent suffices.” Enlarge
K to at least one and take \(0<\gamma\le1\). If all six required
even sums are at most

\[
 \tau=\left[\frac{10^{-7}}{7(16K+1)}\right]^{1/\gamma},
\]

then \(\tau\le10^{-7}\), the smallness condition in (5.1) holds,
and \(\delta\le7(16K+1)\tau^\gamma=10^{-7}\).
Thus ES follows. An exponent larger than one can be replaced by one
when S≤1. This proves sufficiency, not existence of a size with such
small sums. “Only move that size” requires their separate uniform
smallness as size varies; neither a single bound S≤10^−7 nor the
product lemma supplies it. The constants and exponent must remain
uniform in the cutoff at the sizes used.

**PK is available for the finite Wilson transfer operator.** The
explicit kernel in `gap-transfer.md:108–140` is a gauge average of
the positive temporal Wilson kernel, multiplied by the two positive
spatial half-weights. It is continuous and bounded below on the finite
compact configuration space. Sections 2–4 there supply positivity,
trace class and the positive simple ground state. This reuses the
existing construction; its lower bound need not be cutoff uniform.
It must be the physical kernel \(Pe^{-V/2}C e^{-V/2}P\), rather
than inferring pointwise positivity from isospectrality with another
transfer representation.

For \(\widetilde P\), stationarity and reversibility give

\[
 \operatorname{Dir}(h)=\tfrac12\int(h(x)-h(y))^2
                              \pi(dx)\widetilde P(x,dy).
\]

The order-two character of f makes \(g=f^2-Ef^2\) even. Since
\(|f(x)+f(y)|\le2\|f\|_\infty\),
\(\operatorname{Dir}(g)\le4\|f\|_\infty^2\operatorname{Dir}(f)\).
The spectral bound on the even mean-zero space gives
\((1-r_1)\operatorname{Var}(f^2)\le\operatorname{Dir}(g)\).
This proves Lemma 6.2, including its constant. The U(1) comparison
uses its Z_2 electric-parity sectors; a real function cannot carry a
general nonreal U(1) charge character.

For Corollary 6.3, set \(u=1-r_\chi\) and \(c=4c_1c_2\).
The lemma gives \(1-r_1\le cu\). Spectral calculus gives

\[
 p_\chi\le\Theta_\chi r_\chi^{a/2}
           \le\Theta_\chi e^{-ua/2}.
\]

If cu≤1/2, then \(1-cu\ge e^{-2cu}\) and
\(S_{\rm ev}(a)\ge r_1^a\ge e^{-2cua}\). In the other case
\(e^{-ua/2}<e^{-a/(4c)}\). These prove its displayed bound, including
the fractional-time trace, which is well defined for a≥3.

**The maximum cannot be replaced by a pure power on these premises.**
Here is an explicit kernel counterexample, not a Wilson counterexample.
On Haar SU(2), put \(f(U)=\operatorname{tr}U\) and
\(h(U)=f(U)^2-1\). Their means vanish, \(\|f\|_2=\|h\|_2=1\),
and they are orthogonal. Indeed Haar integration gives
\(Ef^2=1\), \(Ef^4=2\), and odd moments vanish. For the fourth
moment, uniformity on S³ gives \(Ex_0^4=3Ex_0^2x_1^2=1/8\),
and f=2x_0. The centre flip makes f odd and h even.

For \(q=1/8\) and \(0\le\eta<1/36\), define the kernel

\[
 K_\eta(U,V)=1+q f(U)f(V)+\eta h(U)h(V).
\]

It is continuous, symmetric and Markov, with
\(K_\eta\ge1-4q-9\eta>1/4\). Its eigenvalues on 1,f,h are
1,q,η, and it is zero on their orthogonal complement. It is positive
and trace class, with a simple even top. Here
\(\operatorname{Dir}(f)=1-q\), \(\|f\|_\infty^2=4\), and
\(\operatorname{Var}(f^2)=1\). Thus LOC's two bounds hold with
\(c_1=1,c_2=4,c=16\), independently of η, while

\[
 S_{\rm ev}(a)=\eta^a,\qquad
 p_\chi=\frac{q^a}{1+\eta^a},\qquad
 \Theta_\chi=q^{a/2}\le1.
\]

At η=0, or by taking η down to zero with a fixed, no bound
\(p_\chi\le K S_{\rm ev}^\gamma\) with fixed finite K and positive
γ follows. If spatial gauge invariance is wanted, use f equal to
the trace of one spatial Polyakov holonomy on product Haar links;
the same construction and moments apply. It still is not a local
Wilson action or a model of the crossing assumptions. Its role is
to refute the pure-power implication from PK and the two trial-function
estimates alone, exactly where the printed proof retains an extra term.

The correct usable electric estimate is
\(p_\chi\le\Theta_\chi[S^{1/(4c)}+e^{-a/(4c)}]\).
Uniform bounds on c and Θ allow the exponential term to be made
smaller than a fixed tolerance at sufficiently large lattice a.
It must nevertheless be paid for, or compared with a power of S by
an additional input. For instance, assuming cu≤1/2 for the sectors
used would give the pure-power branch directly. No such hypothesis
is supplied. Light-sector thermal bounds at the three shapes, their
small even sums, and magnetic/dyonic heavy estimates remain separate.
Electric LOC alone proves neither ES nor the full F-h statement.

## 6. Read record and final checkpoint

The requested Opus note was read in full. Its script reports were
treated as GUIDE; no loop-opus script was run or used as evidence.
The earlier hand proofs were reused, not re-enumerated. In addition
to the input ranges named above, `gap-means-max.md` Section 4 and
`gap-means-max-check.md` were read in full; the relevant transfer
definitions and proofs are `gap-transfer.md:34–50,108–180`.

The upstream `YM4_sketch_500.tex` and
`theorem_0_complete_account_raw_I.tex` were each fetched once at revision
`31a47c543775`. The index searches included `README.md`, chunk files,
`obligations.md` and `ca-4.12-4.19/`. The neighboring rows actually
used were chunk 02:84–105, chunk 03:6–28 and chunk 29:118–137.
The bounded outline source reads were:

| Outline lines | What was checked | Relation to this task |
|---|---|---|
| 2195–2231 | GL3; positive one-bond coefficients, with a written proof | Existing transfer input; not fusion |
| 2313–2335 | GL8; gauge projection and the partition-function trace | Existing trace framework |
| 2773–2795 | Quaternion identity and the positive reflected Gram expansion | Reflected positivity, not EP association |
| 32326–32380 | CP10's additional rotation Ward inputs, explicitly required | Different Ward identity; not the one-link equations |

No CA-I theorem or Balaban-paper result is imported into this check;
no full upstream manuscript was read. The CA-I download was not needed
after the targeted index comparison. Historical literature claims and
the numerical crossover, flux-localization and photon heuristics in
the Opus note are not upgraded here.

All requested statement checks are complete. The remaining actions
are source corrections: fix the clover order; distinguish the partition
normalizations and twist insertion; restrict VB to its common-state constraints; remove
the radius and positivity impossibility claims; and retain the
exponential term in the fusion consumer. Only this output file changes.
No registry, source proof, audit record or status was edited. ES, F-h,
LOC and the magnetic/dyonic estimates at order-one coupling remain open.

RESULT: HOLDS: EP-NO, the Ward, spectral and product-rule identities, and conditional sufficiency of any fixed positive exponent; HOLDS AFTER CORRECTION: the clover order, plaquette formulas and VB; FAILS: the claimed seed-scale radius requirement, positivity no-go and pure-power consequence of Corollary 6.3; no mass gap or status is granted.
