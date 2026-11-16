## Repo search

Written by OpenAI Codex, gpt-6-astra, xhigh (assigned runner), at
`eb05ae6aac1fd522df5ef7f917323e43a510ce4e`. Research check of row 1032,
Section 7 only; not an audit, no status grant, no mass gap claimed.
Not covered: the invention survey, its external literature claims, or row
1049 (not read). No new attack, numerical proof, or Lean run.

lead: openai/gpt-6-astra/xhigh gap-afield-b-check-astra
lease_until: 2026-11-17T00:00Z

The target-specific prior digest is absent. The supplied lead-search record
`prior/repo-search-2026-11-08.md` was read whole. It concerns thirteen earlier
RG targets, not this November 16 criterion. Its closest spectral hit is
`S/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`: positivity of one plaquette
correlation, not a bound on the whole thermal trace. Here S denotes
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/` on PR 10114.
That source was checked directly at PR 10114 commit
`f76f6c649cff7dffbab664d8976e680e8f287fe9`, lines 106–176. Its conclusion
is explicitly an upper bound on a spectral threshold, not a lower gap
bound. It supplies none of Section 7's seed criterion. The task supplies
no additional target-specific "Repo prior work" paths. No matching owner for afield,
GS-eq, or row 1050 was found in `library/open-registry.md`.

The existing suppliers being used, not re-attacked, are `gap-crux-restate.md`
(spectral inequalities), `gap-phys-seed.md` (ZD-c and Z3),
`gap-compact-rigidity-max.md` (CE and CR), `gap-dichotomy.md` (their repaired
contracts), and `gap-means-max.md` (the distinct even seed).

Credit: Claude Fable 5.2 max wrote the text checked here. Ethan Sussman and
Levent Alpoge, with Claude and Codex as authors of their text, supply the
account and trajectory; Tadeusz Balaban supplies the underlying RG work.
Those credits do not make the criterion an established property of SU(2).

## First hand tests

Write h = 61/100000 = 6.1 x 10^(-4). No numerical run supports these tests.

1. **The factor 15: HOLDS.** Put c_0 = c(a,a,a). Before the r-th
   doubling, r = 0,1,2,3, the time is still a, and the other sides have
   volume 2^r a^3. The monotonicity is of c(B)/|B|, giving
   c(B_r) <= 2^r c_0. Thus the four increments are bounded by
   a c_0, 2a c_0, 4a c_0, 8a c_0. Their sum is 15 Gamma_1(a).
   This does not use ZD-c. ZD-c supplies the later threshold h, not 15.

2. **At d = log(3/2), the supremum defining eps_*(d) is at s = 5:**

   eps_*(log(3/2)) = h/2^20 - log(1 + 2^(-32))/32.

   For 0 <= s <= 4, log(1+x) >= x/2 at x = 2^(-2^s) gives
   8^s log(1+x) >= 2^(3s-2^s-1). The five exponents are
   -2, 0, 1, 0, -5; every lower bound exceeds h. These terms in the
   supremum are negative. For s >= 6 each term is at most h/16^6.
   The s=5 term exceeds (h-2^(-17))/2^20, which exceeds h/16^6
   because (15/16)h > 2^(-17). This proves the maximizing index.
   The elementary bounds x-x^2/2 < log(1+x) < x give explicit rational
   lower and upper bounds by replacing the logarithm in the display.
   In particular the value exceeds 5.7 x 10^(-10):

   2^(-17) + 2^20 (57/10^11)
   = 0.00000762939453125 + 0.00059768832
   = 0.00060531771453125 < 0.00061.

   The source's rounded equality 2^(-17) = 7.63 x 10^(-6) should be
   an approximation or upper bound. Its stated sufficient threshold is safe.

3. **The boundary object E = log 2:** put two levels at zero and all
   others at +infinity in every box. Then the trace is 2, the normalized
   thermal sum is 1, the deficit is zero, and the gap is zero. It is
   symmetric and fixed under dilation. Thus no criterion that includes
   (D,Gamma_1) = (log 2,0) can force a seed in this limit class. This does
   not make the object a finite datum with a simple top eigenvalue, or a
   Wilson SU(2) realization. Its admissible realization is checked below.

## GS-dir and GS-eq: HOLDS, given ZD-c

The actual input is `gap-phys-seed.md:311–320`. Its threshold is precisely
h, with a strict upper-limit inequality at one size of P. It equates this
with (PHYS-SEED) and [(BDD-Delta) and (Z-UNB)]. The repaired wall (W) and
its equivalence with that seed are in `gap-dichotomy.md:117–174`. This is
an imported conditional theorem, not a fresh verification of its entire
dependency chain. The factor 15 is independent of it.

**AMP, lines 359–363: HOLDS.** Put r_i = lambda_i/lambda_0 for i >= 1.
For nonnegative sequences, sum r_i^(2k) <= (sum r_i^k)^2: the right
side also contains all cross terms. Iteration gives
S(2^s a;a^3) <= S(a;a^3)^(2^s). Monotonicity of M in the three spatial
sides then gives

D(2^s a) <= 2^(3s) Delta(2^s a,a,a,a)
<= 8^s [log(1 + S(a;a^3)^(2^s)) + 2^s Gamma_1(a)].

The volume ratio is 8^s, and the energy term thus has coefficient 16^s.
Also S(a;a^3) <= exp(D(a))-1 since Gamma_1 >= 0. All series inequalities
follow first for finite sums and then by monotone limits. Time a >= 3
suffices; trace-class at time 1 is not required for this use.

**GS-dir, lines 365–371: HOLDS.** Fix L and s before taking j large.
Let d = D^+(L) < infinity and gamma = Gamma_1^+(L); 0 <= gamma <= d.
For every eta > 0, both D_j(L/a_j) <= d+eta and
Gamma_(1,j)(L/a_j) <= gamma+eta eventually, with one common cutoff index.
Apply AMP and then let eta decrease to zero. Continuity and coordinatewise
monotonicity of its displayed right side prove the asserted limsup bound.
There is no interchange of a supremum over sizes with a cutoff limit.
(S0) makes L/a_j and every required half-time valid integers for all
large j. The enlarged size 2^s L still belongs to P. The strict bound
by h is exactly (PHYS-SEED-Delta), so ZD-c gives the seed and (W).

**GS-eq, lines 373–379: HOLDS.** For d < log 2 let q = exp(d)-1 < 1.
The quantities 8^s log(1+q^(2^s)) tend to zero: for 0<q<1, bound the
logarithm by q^(2^s), whose successive ratio after multiplication by
8^s is 8q^(2^s), eventually below 1/2. For q=0 it is immediate.
Thus some term in eps_*(d) is positive, and eps_*(d) <= h is finite.

If gamma < eps_*(d), the definition of supremum gives a finite s with

gamma < 2^(-s)[h 8^(-s)-log(1+q^(2^s))].

Multiplication by 16^s gives exactly GS-dir. No maximizing s is needed.
Conversely (W) gives (PHYS-SEED). Choose its uniform q' with 0<q'<1.
Lemma Z3 (`gap-phys-seed.md:283–294`) gives d = D^+(L) < h/2 at
some dyadic size L. Since gamma <= d and the s=0 term of eps_* is h-d,
gamma <= d < h-d <= eps_*(d). This proves the converse with strict
inequalities; it does not assert the same size as the original seed.

For the last "in particular" sentence, each term of eps_*(d) decreases
with d, so eps_*(d) >= eps_*(D_0)>0 when d<=D_0<log 2. A lower limit
zero of Gamma_1^+ supplies a sufficiently large size below this fixed
positive bound. This justifies the quantifier over arbitrarily large sizes.

**Worked instance, line 381: HOLDS AFTER CORRECTION of the rounding sign.**
Replace "2^(-17) = 7.63 x 10^(-6)" by
"2^(-17) = 0.00000762939453125 < 7.63 x 10^(-6)".
The rational calculation above verifies the non-strict hypotheses
d <= log(3/2), gamma <= 5.7 x 10^(-10) with a strict conclusion.
Alternatively one may assume limsup S_j(L/a_j;(L/a_j)^3) <= 1/2
directly and use AMP. That version does not require d <= log(3/2),
since d includes gamma. The thermal bound here is an upper-limit bound,
not necessarily an exact bound at each finite cutoff.

**Sharpness, line 383: HOLDS for limit objects only.** The cited
`gap-uv-rigidity-max.md:725–740` states Proposition CONST. Its explicit
supplier is `gap-compact-rigidity-max.md:253`: A_(m,epsilon),
Z(n)=1+(m-1)exp(-epsilon |n|), with f=0 and a simple top eigenvalue 1.
Use m=2, u_j=12*2^j (so S0 holds and a_j tends to zero),
epsilon_j=12^(-4)16^(-4j),
and the admissible sequence j_i=k_i=i. Then

Delta^(i,i)(x)=log(1+exp(-16^(-2i)|x|)) -> log 2.

H1 holds with D_0=log 2 for every i. For every fixed b in DD,
s^(i,i)(b)=exp(-16^(-2i)b^4/2) -> 1, so H2 holds eventually.
The deficits are identically zero. At every fixed physical size of this
family the upper-limit thermal sum is 1, so there is no (PHYS-SEED).
This repairs the supplier's irrelevant u_j=3 convention to S0 without
changing its construction. It verifies the obstruction at the boundary;
it is not a Wilson-model example or a proof of an optimal eps_*(d) among
all possible criteria below the boundary.

**Comparison with (ES): HOLDS as a comparison, not an identification.**
`gap-means-max.md:208–268` defines ES using S_ev(a;a^3) and
delta=a[8 log lambda_0(a^3)-log lambda_0((2a)^3)], both <=10^(-7).
Theorem R gives two of three sector seeds. R4 gives the centre-even gap;
R5 gives ES from any of those three seeds at a larger size. It does not
say that ES always supplies the full periodic seed. In contrast GS-eq
uses the full thermal spectrum and Gamma_1=a[log lambda_0(a^3)-fa^3].
Indeed delta=8 Gamma_1(a)-Gamma_1(2a)/2, a one-doubling defect, whereas
Gamma_1 uses the bulk f. Thus the "five lines" are a direct full-sector
variant in form only. No centre-even replacement of the full S in AMP or
GS-eq is licensed by this proof. ES is not a premise of GS-dir or GS-eq.

## BAR, CHAIN-4 and NUC

**M1 and M2, lines 271–272: HOLDS.** The decreasing power-sum norm gives
coordinatewise monotonicity of F/|n|, hence M. Its infimum after subtracting
f is zero. For a fixed box, write Delta(k,B)=g(k;B)+kc(B).
Each normalized excited eigenvalue lies in [0,1). Dominating its k-th
power by its third power gives S(k;B)->0 as k->infinity. Thus
c(B)=lim Delta(k,B)/k=inf Delta(k,B)/k>=0. This also validates the limit
in the abstract datum class, which initially assumes summability only at
integer times at least 3.

**Normalization correction, first failing identification at line 274.**
The parenthesis "it is kappa of Lemma K in two variables" is false in
general for this c(B). The cited K at `gap-crux-restate.md:174–180` fixes
two transverse sides c,d and subtracts
ell(c,d)b, where ell(c,d)=inf_(T,b) F(T,b,c,d)/(Tb). Section 7 instead
subtracts f bcd. The exact relation is

c(b,c,d)=kappa_(c,d)(b)+b[ell(c,d)-fcd], with ell(c,d)>=fcd.

Replace the parenthesis and any claim of monotonicity of this global
deficit itself by:

> Here c(B) is the deficit relative to the four-dimensional bulk f.
> The function c(B)/|B| is non-increasing in each side, by M1 and M2.
> Lemma K's fixed-transverse deficit uses its own bulk ell(c,d).

This is a real distinction. For 0<q<1 the symmetric datum
Z(n)=product_mu (1+q^(n_mu))^(|n|/n_mu) has f=0. In a time direction
its trace expands as a binomial with integer multiplicities and a simple
top eigenvalue. For B=(b,c,d), its global deficit is

cd log(1+q^b)+bd log(1+q^c)+bc log(1+q^d).

At fixed c,d it grows linearly with b. Thus global c need not decrease.
No proof in Section 7 uses that false identification: its spatial
comparison is consistently the valid comparison of c(B)/|B|.

**BAR, lines 280–290: HOLDS.** Theorem D(a) on file is
F((2a)^4)<=16F(a^4); subtracting 16fa^4 gives the claimed inequality
for D. Its upper-limit version is valid for nonnegative extended values.
If (BDD-Delta) holds, choose D_* strictly above its bound; the barrier
condition is vacuous. Conversely enlarge the barrier's starting size to
one above L_1 in P. Finitely many doublings carry finiteness there.
The bound max(D^+(L_2),16D_*) is preserved: above the barrier use BAR,
below it use the factor 16. All larger sizes in P are exactly successive
doublings, so this covers precisely the asserted domain.
For BAR-lat, at the i-th target size only i cutoff thresholds are needed.
Taking their finite maximum, then limsup_j, proves the same bound. No
common j_0 for infinitely many sizes is asserted or needed.

**CHAIN-4, lines 311–318: HOLDS.** Every m_i is finite and nonnegative.
The diagonal k_1=...=k_i=k is cofinal for decreasing M: given any tuple,
choose k at least its largest coordinate. Hence its limit is the full
infimum, and freeing a further side can only reduce it. m_4=0 by the
definition of f, so telescoping gives D=sum_(i=0)^3 G_i with G_i>=0.

For the potentially delicate exchange, set
H(T,k)=M(T,k,...,k,a,...,a), with i entries k. Then

lim_k inf_T H(T,k)=inf_k inf_T H(T,k)=inf_(k,T) H(T,k)=m_(i+1)(a).

The first equality uses monotonicity; the last uses cofinality in the i
free spatial coordinates. This is an equality of infima of a function
bounded below, not an exchange of an arbitrary limit with an infimum.
The two terms of k^(-i)g(a;B_(i,k)) have finite limits
a^(4-i)m_i and a^(4-i)m_(i+1). Multiplication by a^i yields the stated
G_i, with no missing factor of a. The endpoints give
G_0=log(1+S(a;a^3)), Gamma_1=ac(a^3), Gamma_3=G_3.
With p(1/a)=lim_k g(a;k^3)/(a k^3), the last term is a^4p(1/a),
the pressure normalization named at `gap-phys-seed.md:195`.

**NUC, line 320: HOLDS.** If D^+<=D_0 then every limsup G_i<=D_0.
In the reverse direction a common bound D_0' for the four limsups gives
D^+<=4D_0'. This is an equivalence of existence of finite bounds, not
an assertion that the optimal constants agree. The term "nuclearity"
here means the four stated numerical bounds; no operator-algebraic
nuclearity or split-property theorem is thereby proved.

**RISE and its summability consequence, lines 353–357: HOLDS.** The
first hand test supplies the four-sided calculation. At a fixed L, take
limsup and use limsup(A_j+B_j)<=limsup A_j+limsup B_j. Iterate at finitely
many sizes before bounding by the full nonnegative convergent series.
This proves (BDD-Delta) with the stated bound and with pointwise cutoff
limsup, exactly as defined. A contrapositive about nonsummability also
requires D^+(L_1)<infinity; if D^+ is already infinite at every size,
RISE gives no such conclusion.

## CAS-0 and GS: HOLDS, given CE and CR

The supplied contracts are `gap-compact-rigidity-max.md:170–196,225–243`,
with the repairs stated in `gap-dichotomy.md:127–202`. CE(ii) supplies
convergent rescaled levels after extraction, finite nonpositive e_0,
integer spectral multiplicities, and the critical-element properties.
CR uses Omega(D_0) of this particular family with a bound of (BDD-Delta).
Neither source proves (BDD-Delta) or the seed for Wilson SU(2). These
input theorems are taken conditionally, as requested.

**CAS-0, lines 330–336.** Each numbered step holds:

1. Let b=min B. The finite-value inequality
   E(T,B)/(T|B|)<=E(T,b^3)/(Tb^3) is inherited from M1.
   Taking T through DD to infinity gives -e_0(B)/|B|<=0.
   CE gives e_0(B)<=0, so e_0(B)=0. The direction is correct.
2. Every finite energy is now nonnegative. Each term of its spectral
   trace decreases with T; symmetry gives the other three directions.
3. For h(t)=E(2^t x), t in Z, monotonicity and the bounded-gap returns
   force h(t)=h(0). The definition quantifies over Z, so returns are
   unbounded on both sides. For any fixed t choose a return after t to
   bound h(t) below by h(0)-eps, and one before t to bound it above.
4. The sandwich between E(x) and E(2^s x) permits dilation of a single
   coordinate for s>=0. Reversing the comparison handles negative
   powers. Any two elements of DD differ by such a power, so E is
   constant on DD^4, not merely on the diagonal cubes.
5. At one fixed box, the trace at one positive time is finite. It
   dominates the terms at later times, so dominated convergence makes
   the constant trace equal the finite integer multiplicity m of zero.
   The critical thermal bound is m-1>=1/5041, hence m>=2.

Every E in Omega(D_0), rather than just a specially chosen limit, is
covered. Apply CE(ii) to its defining admissible sequence and extract the
levels. The pointwise limit remains E. The argument does not assume that
an arbitrary eternal datum is critical.

**GS, lines 338–347.** If (W) fails, CR supplies a recurrent element.
CAS-0 makes it constant unless some cube has negative ground energy.
Conversely a constant log m is recurrent, and either listed alternative
therefore contradicts (W) by CR. The disjunction is exact.

For n_i=2^(k_i)u_(j_i)b, the rescaled ground energy is exactly

e_0^(j_i,k_i)(b^3)
=-2^(k_i)u_(j_i)c_(j_i)(n_i^3)=-Gamma_(1,j_i)(n_i)/b.

CE(ii)'s level convergence, used also in its Step 4, gives the stated
limit along the extracted sequence. For fixed b in DD, the physical
sizes 2^(k_i)l_1 b eventually lie in P and tend to infinity. Since
j_i also tends to infinity, the single j_eps in GS-CAS applies along
every such sequence. Nonnegativity then forces every cube deficit in
the limit to vanish. NO-CONST excludes the sole remaining case.

The converse's uniform quantifier is valid. Under (PHYS-SEED) choose
0<q'<1 and one J such that the seed bound holds for all j>=J. For each
of those j apply Z3 with N_j=l/(2a_j). It bounds every integer cube side
at least 2^K l/a_j by 1024 q'^(2^K)/5041. Given eps>0, choose K so this
is <=eps. Then L_eps=2^K l and j_eps=J work simultaneously for all
L>=L_eps in P, since Gamma_1<=D. This does not try to infer uniformity
from pointwise limsups. OM/CR make Omega(D_0) empty, hence NO-CONST.

## NOCS, FP-U1, TRI, SPH and SPH-LC

**NOCS, lines 391–399: HOLDS on its stated smooth finite-dimensional
domain.** A product of SU(2) groups is simply connected. Path integration
of a closed real 1-form therefore gives a global smooth potential.
Averaging that potential over the compact gauge group commutes with d
and preserves its derivative when the form is invariant. Haar invariance
makes the averaged potential invariant, including at points with
stabilizers. No free action or smooth orbit-space assumption is needed.

There is also a direct check of part (2) that avoids the quoted heat-kernel
argument. With omega=dW, the smooth positive phi=exp(-W) satisfies Q phi=0.
The assumed quadratic form implies H>=c and H phi=c phi, so c=E_0.
Any other ground eigenfunction psi has Q psi=0 and therefore
d(exp(W)psi)=0. Connectedness makes psi a multiple of phi. Hence
omega=-d log Omega, including uniqueness. Compactness gives the usual
self-adjoint elliptic realization and smooth eigenfunctions. This proves
the asserted factorization statement, with no numerical spectral input.

**The broader sentence at line 399 needs a scope correction.** Replace
"the period ... the angle theta ... have no lattice counterpart" by:

> This smooth closed-form construction has no nonzero period on the full
> finite SU(2) link space, and cannot supply a theta term by that mechanism.

The lemma does not rule out definitions on restricted admissible fields,
singular constructions, or a continuum limit. It concerns the specified
Kogut-Susskind differential operator. For the Wilson transfer operator
the positive-eigenfunction uniqueness remark holds; no identity of its
logarithm with that differential operator is established here.

**FP-U1, lines 405–407: HOLDS.** Work on the fixed vector space of
mean-zero site functions. Positive conductances make M_c positive definite
there. Its derivative is R_l=D_l^T M_c^(-1)D_l>=0, while the second
directional derivative of log det is
-Tr(M_c^(-1) A M_c^(-1) A)<=0 for a symmetric variation A. Thus the
outer function is both concave and coordinatewise increasing. Componentwise
concavity of cos, followed by these two properties in that order, proves
the composition claim on the entire open cube.

At c=1, sum_l R_l=Tr_(1-perp) I=N-1. Translations and coordinate
permutations make all dN terms equal, even at n=3, with orientation
irrelevant to D_l D_l^T. Therefore R_l=(N-1)/(dN). Since
c_l-1=-theta_l^2/2+O(theta_l^4), the first-order determinant variation
has precisely the claimed quadratic coefficient. Its remaining terms
are O(||theta||^4) on this fixed finite lattice; no volume-uniform
remainder is claimed.

**Line 409: HOLDS AFTER CORRECTION of the sign and domain wording.**
Use:

> The Hessian of -log det' M at zero is +(N-1)/(dN) times the identity;
> the Hessian of log det' M has the opposite sign. M(theta) is the
> Hessian of the gauge functional at every theta in the cube. Its
> interpretation at a minimal Landau representative also requires that
> representative to satisfy the stationarity and minimization conditions.

The whole cube has not been proved to consist of minimal-gauge
representatives. The local determinant gain exists for compact U(1),
as claimed. No global gauge-fixed measure estimate, uniform LSI, or
SU(2) ghost-loop statement follows from this lemma.

**TRI, lines 413–419: HOLDS.** The Pauli identity gives
cos theta_12=cos theta_1 cos theta_2-sin theta_1 sin theta_2 t.
The area element on the unit sphere makes t uniform on [-1,1].
Both sines are positive, so the interval has length
2 sin theta_1 sin theta_2, with the endpoints in the stated order.
The change of variables cos theta_12 has absolute derivative sin theta_12.
The lower angle bound is |theta_1-theta_2|. The upper is
min(theta_1+theta_2,2pi-theta_1-theta_2). These give exactly T.
No boundary atom is introduced; the lemma assumes the two input angles
strictly between zero and pi.

**SPH, lines 421–427: HOLDS.** Condition successively on the previously
formed product and on the next independent Haar element's angle. The
next element is uniform on its conjugacy class. TRI's transition law
depends only on the two angles, not the previous product's orientation.
This justifies multiplication of the conditional kernels without assuming
the overlapping partial products are independent. For n=3 apply TRI
directly; there is no alpha_0. For n>=4 the stated fan recursion applies.

There are n-1 independent Weyl densities (2/pi)sin^2(theta_i) and
n-2 transition factors 1/2. Each internal sin(alpha_k) cancels once
in numerator and denominator. Each theta_i is left with one sine,
including theta_n from the last numerator. The coefficient is exactly
(2/pi)^(n-1)2^(-(n-2))=2/pi^(n-1). It normalizes automatically by
successive conditional integration. The intersection of the displayed
linear triangle constraints is convex. Uniformity in the diagonal
coordinates means uniform conditional density on their allowed fibre.

**SPH-LC, lines 429–431: HOLDS.** The Hessian on the polytope's interior
is diagonal in the theta coordinates, zero in the alpha coordinates.
Its theta entries are -csc^2(theta)-beta cos(theta). For u=-cos(theta)>0,
nonpositivity is precisely beta u(1-u^2)<=1. The maximum used in the
source follows without numerical optimization from

2/(3 sqrt(3))-(u-u^3)=(u-1/sqrt(3))^2(u+2/sqrt(3))>=0.

For necessity the source's proposed interior point is valid by exact
bounds: theta_*=arccos(-1/sqrt(3)) lies between pi/2 and 3pi/4<3.
Using 3<pi<4, theta_*+3<2pi and 9/2<2pi. Thus every inequality of
T is strict for (theta_*,3/2,3/2) and for (3/2,3/2,3/2).
A small change in theta_1 stays in P_n, and the second derivative there
is positive when beta>3sqrt(3)/2. The displayed decimal angles in the
source are unnecessary. Endpoints are handled by the zero extension of
the log-concave density on its convex support.

Prékopa's marginal theorem gives the stated forward implication for
the marginal, not an if-and-only-if threshold for that marginal. The
source's transport form is also on file in the Sussman–Alpoge outline,
GCB3–GCB5, lines 27149–27207, reached through chunk 25. The density here
is bounded with compact convex support, so the usual exhaustion form
applies. For sin^2(theta) instead, the negative second derivative term
is -2csc^2(theta), doubling the threshold to 3sqrt(3).

The identification of this ensemble with gauge theory on a sphere, its
extension or failure in four dimensions, and the Gram-determinant remark
at line 433 remain the author's ARGUED material. SPH itself only proves
the explicitly stated independent-Haar product ensemble. No verdict
here promotes those physical or geometric identifications.

## Source boundary and meaning

The outline and CA-I were each fetched once, at `31a47c543775`, into the
new directory `/tmp/sa-gap-afield-b-check-astra.qemSzU/`, never into /tmp
itself. The outline index README was read, and its chunks and obligations
were searched for Casimir energy, thermal sums, mass gaps, ground states,
Faddeev–Popov, Chern–Simons, class angles, nuclearity and log-concavity.
Neighbouring rows were read before the source excerpts used here.

The relevant source matches were:

| Index/source | What is already there | Relation to this check |
|---|---|---|
| chunk 01:63–74; obligations:21–29; outline 588–599 | Polynomial decay can coexist with spectrum reaching zero; further gap estimates are needed. | Scope warning, not a supply of the seed. |
| chunk 07:112–120,176–184; outline 7660–7681,7883–7895 | Compact-group gauge averaging, tree disintegration, and a background Faddeev–Popov determinant. | Different results from the compact-U(1) concavity coefficient; no duplicate of FP-U1 identified. |
| chunk 25:15–21; outline 27149–27212 | Transport proof of the marginal log-concavity implication, with its integrability and regularity domain. | Existing source for the Prékopa step; used with credit, not claimed as new. |

No CA-I lemma is a premise of Section 7's criterion. CA-I was downloaded
but no claim about its complete contents is made from a limited index
search, and its 4.12–4.19 proof corpus was not read. No Balaban paper was
imported. The target-specific prior digest was absent; the November 8
lead digest is not evidence of an exhaustive search for November 16
theorems. This check makes no global novelty claim. Rules were read from
main `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`; the checked science stays
at the task's pin. The planning branch supplied no mathematical evidence.

**Meaning of GS-eq.** It is a valid new presentation of the same wall,
conditional on ZD-c. It is useful as a certificate specification: one
fixed physical size, an explicit margin below one excited thermal state,
and an explicit permissible bulk-energy deficit. It proves neither
inequality for the account's SU(2) trajectory. The seed and its transport
engine already existed. Gamma_1 requires the infinite-volume f, so
"one size" does not make every quantity finite-volume data. No bound
here removes that supply problem or the (S0) trajectory-matching issue
recorded in `gap-dichotomy.md:98–115`.

Neither side is shown closer to a proof for SU(2). Logical equivalence
does not preclude a future advantage from the form, but no such estimate
is supplied here. In particular, the pair is target-equivalent; it is
not proved that either inequality alone is individually equivalent to
(W). The constant log 2 passes the zero-deficit test and still has no
seed. Given (BDD-Delta), GS-CAS plus NO-CONST is likewise a restatement
of the rigidity requirement, not its solution.

## Verdict record

| Statement | Verdict | First failing line or scope |
|---|---|---|
| M1, M2 | HOLDS | None. |
| Identification of c with Lemma K's kappa | HOLDS AFTER CORRECTION | Line 274; different bulk subtraction. Replacement above. |
| BAR, including BAR-lat | HOLDS | None; P is the single dyadic tail. |
| CHAIN-4 and NUC | HOLDS | None; the reverse NUC bound is 4D_0'. |
| CAS-0 and GS | HOLDS given CE/CR | None; levels are extracted and j_eps is uniform by Z3. |
| RISE and AMP | HOLDS | None; nonsummability inference presupposes a finite starting D^+. |
| GS-dir and GS-eq | HOLDS given ZD-c | None; full spectrum, strict limsup threshold. |
| Worked numerical instance | HOLDS AFTER CORRECTION | Line 381's rounded equality; 5.7 x 10^(-10) remains valid. |
| log 2 sharpness | HOLDS for limit objects | No claim of a Wilson realization or an optimal general epsilon function. |
| Comparison with ES | HOLDS as stated comparison | ES is a different sector criterion, not a premise or a substitute. |
| NOCS | HOLDS | Smooth forms on the full finite SU(2) link space. |
| NOCS's broad theta-language | HOLDS AFTER CORRECTION | Line 399; restrict to this smooth closed-form mechanism. |
| FP-U1 | HOLDS | Fixed finite lattice; no volume-uniform remainder. |
| FP-U1 consequence | HOLDS AFTER CORRECTION | Line 409; the positive Hessian is that of -log det, and a gauge minimum is an extra condition. |
| TRI, SPH, SPH-LC | HOLDS | None in the stated probability ensemble; Prékopa for the marginal. |

Verification was a written mathematical check, using nonnegative-series
arguments, exact rational inequalities, spectral limits, convexity and
finite-dimensional differential geometry. These are formalizable proof
steps, not a claim that a Lean file was produced or checked. No numerical
job, proof-search program, audit pipeline, or further review of this check
was run here. Only the assigned output file was written. The source author
has not applied the narrow corrections above.

RESULT: HOLDS for BAR, CHAIN-4/NUC, RISE/AMP, NOCS, FP-U1 and TRI/SPH/SPH-LC on their stated domains; CAS-0/GS HOLD given CE/CR, and GS-dir/GS-eq HOLD given ZD-c, including the factor 15, the 5.7 x 10^(-10) instance and log 2 sharpness for limit objects; HOLDS AFTER CORRECTION for the global-versus-transverse deficit identification, the rounded equality, the broad theta wording and the FP consequence's sign/domain; GS-eq restates (W) and supplies no new SU(2) estimate; research check only, no status grant and no mass gap claimed.
