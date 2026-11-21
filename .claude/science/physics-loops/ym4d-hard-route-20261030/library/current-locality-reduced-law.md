# The midpoint current: a regular-law gap and an extension implication

Source: 7f414ab5f181599118a4fd0cda7679da46c8e7df, continuation of queue
item 10 on 2026-11-01. Author: Codex, configured model and effort unchanged.
**Status: gap** for (I-K3) for the specified Wilson current.
The implications below have author proofs, **unchecked** independently.
This is not an audit or a counterexample to Yang--Mills. No numerical
experiment was run. Source hashes are in
[the source manifest](../checks/upper-chain-codex/current-locality-7f414ab5f-source.json).

## 1. Attack first: what cannot pay this estimate

Write x=x_j, x'=x_(j+1), t=x'/x, eta=iota^new_j and U=eta x'^(3/2).
The regular function whose extension is in question is exactly

    f(W)=t [E_W^r G_W - E_1^r G_1],
    G_W=G^cur_(j;c',c'')(W,xi),                         (CUR)

with the linear and quadratic polynomial of Lemma 14.16. When c'=c'',
antisymmetry makes the current zero; below the nontrivial case is d>0.
The subscript on G matters: both its coefficients and its law depend on W.
The full extension is F=x'I. No other current is substituted for it here.

**Discharged algebra / necessary regular test.** If regular W and Wtilde
agree on Q_m(c'), the law nu=(delta_W+delta_Wtilde)/2 belongs to LL_(j+1).
Its conditioning variable is constant, so

    E_nu|F-E_nu(F|Q_m)|=|f(W)-f(Wtilde)|/2.             (PAIR)

Every coarse-field nonregular-shell event has probability zero in this
test. Rarity cannot replace a bound on this difference. This observation
does not rule out using screening to prove the regular-law estimate.

**Discharged arithmetic / rate test.** An exponential tail at an
unspecified rate is insufficient. At the terminal level let x' tend to
infinity in (FLOW-END), so lambda' is comparable to x'. Suppose the only
offered tail envelope, divided by U at a fixed endpoint distance, is
x'^(-b) exp(-rho m), with b fixed and 0<rho<kappa. Choose

    0<a<1,  a (kappa-kappa_s)_+ < C_Z,   m=floor(a lambda').

In the single tier omit the condition involving C_Z. In the two tiers
zeta'=exp(-C_Z lambda'), and this choice gives
Phi'(m)<=2 exp(-kappa m). Consequently

    x'^(-b) exp(-rho m)/(B' Phi'(m))
      >= [1/(2 C_B)] x'^(-b-1/2) exp((kappa-rho)m),

which is unbounded. Thus a slow tail with only a power of g as prefactor
does not fit the stated profile by increasing a fixed constant. This is
an envelope test, not a constructed SU(2) current or a counterexample
under all the one-step premises. It is the quantitative issue in mapped
interface gate D5. An exponentially small second-tier amplitude
can pass this test; the sufficient conditions below retain it.

**Gap / law test.** (C2_j) is stated for E^good. Equation (CUR) uses E^r,
the same good-sector domain/cut with Q^s removed. Neither a small additive
error nor the first covariance term printed in Lemma 14.16 gives a far
difference in that law. At a fixed finite volume, whenever the common-cut
interpolation has the requisite integrability, define

    E_(W,s) T = int T exp(-S_W^r-s Q_W^s) / int exp(-S_W^r-s Q_W^s),
    0<=s<=1.

Differentiating numerator and denominator gives exactly

    E_W^r G_W-E_W^good G_W
      = int_0^1 Cov_(W,s)(G_W,Q_W^s) ds.                (LAW)

Bounded cuts and bounded integrands suffice to justify this differentiation;
otherwise domination is an additional hypothesis. Subtracting (LAW) at
Wtilde gives the full correction, not its first-order approximation.
An estimate at s=0 alone is not a bound on the integral.

The size bound on each q_c in (Q_j) does not supply this mixed far
difference. Even on a finite cut, a comparison using the oscillation of
sum_c q_c carries the number of cells in its exponent. No volume-free
comparison of E^r and E^good is proved by that argument. A distance-free
error exp(-C lambda') would also be far above the floor at
M'=floor(exp(lambda'/5)), whose exponent is of order
-sqrt(lambda') exp(lambda'/10).

The two exact decompositions relevant to the attempted proof are

    E_W^r G_W-E_Wtilde^r G_Wtilde
      = E_W^r(G_W-G_Wtilde)
          +(E_W^r-E_Wtilde^r)G_Wtilde,                  (SPLIT)

and (LAW). In (SPLIT), one must use a specified common coordinate/gauge
identification. Invariant contraction of the whole polynomial is enough;
no unjustified invariance of each frozen-coefficient monomial is assumed.
The first term reads the response of the actual current coefficients.
The second reads normalized, inserted moments under E^r, including its
cut. (SCR_j) reads a fixed function of the fine field under the full
kernel, not this W-dependent polynomial under a changed law. (MD*_j)
and rarity can produce the former screening statement; no statement
here transfers it to every interpolated law E_(W,s).

## 2. The exact sufficient strengthening of (C2_j)(c)

**Proposed clause (RC_j) [gap, not adopted as a proved input].**
All constants below are independent of j, K and volume. For every pair of
coarse cells, put d=d(c',c'') and choose the same unordered-pair midpoint
o as the actual extension. The geometry is measured in coarse cells;
the conservative containment used below is
Q_n(o) subset Q_(n+d+2)(c'). For every regular W, require

    |f(W)| <= C U sum_(v in tiers) a_(v,j) exp(-sigma_v d).       (RC-size)

For every two globally regular W,Wtilde agreeing on Q_n(o), n>=d,
require, for the G and the law of (CUR),

    t |E_W^r G_W-E_Wtilde^r G_Wtilde|
      <= C U sum_v a_(v,j) exp(-sigma_v d)
                           exp(-rho_v (n-d)).                  (RC-far)

The comparison is required for every non-full read cube Q_n(o), including
n>=T/4 if it occurs. It does not require a pullback at n. At a full-field
read the difference is zero. For the single tier v=f, set a_(f,j)=1 and
kappa_f=kappa. For the two tiers add v=s, with kappa_s as in Text 21.7,
and require

    a_(s,j)<=C_s zeta_(j+1),
    rho_v>=kappa_v,   sigma_v-c_*>=2 kappa_v,   c_*>0.           (RC-rates)

The same fixed c_* must be used in the current budget and in c_r<c_*.
These are explicit sufficient margins, not consequences of the word
"exponential". Strict margins allow polynomial losses to be absorbed.
For example, if a raw bound has (1+n+d)^p times exponentials with rates
rho_v+epsilon and sigma_v+2epsilon, write n=d+h; then
(1+2d+h)^p exp(-epsilon(h+2d)) has a finite supremum, by the power
series of exp. This reduces it to the displayed bound, with a fixed
constant. No polynomial in the radius is simply discarded.

A raw slow amplitude C(L) x_j^P z_j^(1/2) can meet RC-rates if the
producer's z_j is the cut activity of Text 21.7 (not the mark coefficient).
Indeed z_j^(1/8)<=zeta_j gives z_j^(1/2)<=zeta_j^4. If
C(L)x_j^P zeta_j^3<=1, then this amplitude is <=zeta_j<=zeta_(j+1).
The latter smallness follows at large X from the linear flow envelopes
and zeta_j=exp(-C_Z lambda_j), for fixed P>=0 and C_Z>0: put D=K-j,
use x_j<=2X+B D and lambda_j=alpha X+l_1 D, and bound

    C(L)x_j^P zeta_j^3
      <= C(L)(2X)^P exp(-3 C_Z alpha X)
           exp[(P B/(2X)-3 C_Z l_1) D].

Choose X so the last exponent is nonpositive and the first factor is
<=1. This proves the required uniformity in D. The argument does not
upgrade a slow amplitude C(L) g_j^2 to z_j^(1/2).

RC-far is the precise missing regular estimate, with the endpoint and
profile rates specified. One sufficient proof bounds both terms in
(SPLIT) by its right side. Another first proves the total good-law
version and then the following exact transfer estimate:

    t | int_0^1 [
          Cov_(W,s)(G_W,Q_W^s)
          -Cov_(Wtilde,s)(G_Wtilde,Q_Wtilde^s) ] ds |
      <= C U sum_v a_(v,j) exp(-sigma_v d)
                           exp(-rho_v(n-d)).                  (RC-transfer)

The analogous size comparison is needed for RC-size if its chosen
tierwise endpoint envelope is not already supplied. RC-transfer is zero
when Q^s=0 with the same cut and domain. It is not zero merely because
Q^s is small. RC_j demands a stronger regular estimate than (PAIR).
Together with MC it is a sufficient repair, not a claimed necessary
characterization of all ways to prove (I-K3).

## 3. What the midpoint extension preserves

**Regular-completion premise (MC) [supplied recipe, finite-volume caveat].**
Read "at the first nonregular distance" in Lemma 14.16 as pullback at
n_0-1, as in (CF_j), never at the nonregular cube itself. If n_0<d the
value is zero; if d<=n_0<infinity it is f(pi^*_(n_0-1) W); at a globally
regular W it is f(W). The extension must be measurable and every
nonzero pullback must be globally regular, depend only on that regular
cube, and agree with W there. These are precisely the properties of
Lemma 14.14 on its stated domain.

There is a finite-volume qualification: Lemma 14.14 explicitly constructs
pi_n for n<T/4 only. No completion for a nonregular field whose first
bad cube is beyond that domain is constructed here. If the intended
torus convention has such cases, (MC) must be supplied for those cases
too, or their actual remainder must be estimated. The current is not
silently changed to a capped or zero extension. The implication below
is at full scope only with a well-defined completion having (MC).

**Extension lemma [implication; author proof].** Under (MC), RC-size,
RC-far and RC-rates imply (I-K3), for every probability law of W, hence
for every arbitrary mixture in LL_(j+1).

First suppose W,Wtilde agree on Q_m(c') and m>2d+4. Set
n=floor(m-d-2), so n>=d and Q_n(o) is a common read cube.
If a first nonregular cube occurs by n, its first radius is the same
for both fields. The zero decision is the same; in the nonzero case
their pullbacks are identical functions of the same smaller cube.
Their extended values are therefore equal.

Otherwise both first radii exceed n (infinity is allowed). Their
regular completions agree on Q_n(o). Neither can be set to zero,
and RC-far applies to those two completions. Since n-d>=m-2d-3,
the result is bounded with the weaker exponent (m-2d-4)_+ below.
For m<=2d+4, RC-size bounds the difference by twice its right side,
whether a zero decision changes or not. Thus in all cases

    |F(W)-F(Wtilde)|
      <= C_0 U sum_v a_(v,j) exp(-sigma_v d)
                      exp[-rho_v (m-2d-4)_+].                 (EXT)

For each tier, put u=(m-2d-4)_+. Since m<=2d+4+u,

    sigma_v d+rho_v u
      >= c_* d+kappa_v m-4 kappa_v.

This proves, without a sum of stretched-exponential increments,

    |F(W)-F(Wtilde)|
      <= C_1 U exp(-c_*d)
           [exp(-kappa m)+zeta' exp(-kappa_s m)]
      <= C_1 U exp(-c_*d) Phi'(m).                            (EXT-profile)

Omit the second term in the single tier. The last inequality uses
g'(m)=min(min(m,M'),sqrt(min(m,M') lambda'))<=m; it includes the cap.
For a full-field read F(W)=F(Wtilde). Provided (MC) and RC-far cover the
other consumed cubes, no unproved limit over larger tori is used.

For completeness, take an arbitrary probability law nu. Finite lattice
configuration spaces with the stated auxiliary labels are standard
Borel, and the recipe assumes measurable kernels. Let W,Wtilde be
conditionally independent copies given W on Q_m(c'). Conditional
Jensen and then (EXT-profile) give

    E_nu|F-E_nu(F|Q_m)|
      <= E|F(W)-F(Wtilde)|
      <= C_1 U exp(-c_*d) Phi'(m).

Since B'>=1 after the prescribed choice of C_B and X, this is (I-K3)
with C_loc=C_1. It is stronger for this source by a factor B'.
No good set, output K2/K3, rarity estimate or conditioned-law membership
in LL was used. This is why there is no circular use of HS in this
extension lemma.

This proof also identifies its limitations: generic K1 gives only the
stretched profile of the bounded-shell countertest, not RC-far. The lemma
does not prove RC_j or remove the finite-volume completion qualification.
It does not certify the transport margins of section 4 of
[history-budget-sum.md](history-budget-sum.md).

## 4. Producer obligations and the first honest stop

**Gap / statement coverage, not a nonimplication theorem for Wilson.**
No derivation of RC-far for (CUR) is supplied by the excerpts checked
here. (C2_j)(c) must either be proved in the following strengthened form,
or an alternative proof of (I-K3) must be given. Its required additional
scope is: the actual background-dependent current, the normalized
reduced law E^r with its actual cut, the two far-difference terms, and
the endpoint/radius rates and amplitudes of RC_j. In particular,
"exponential tails" without those comparisons is not a certificate.

| Producer | What it would have to deliver, using its own construction |
|---|---|
| Independent | Identify the action split, cut and coordinates that give the E^r in (CUR). If its analytic N_good is exactly this reduced law, prove that equality and work directly there; RC-transfer is then unnecessary. Otherwise supply RC-transfer, including the normalization, uniformly over the interpolation. Prove RC-size and RC-far from its coefficient and inserted-moment estimates for this current, retaining the p(g)^3 normalization where used. The chart is now based at V^# with mean b^*, as its Requests and interface gate D9 state; the older Text 18 chart cannot be used unchanged. The two backgrounds may be in different global sectors: the requested estimate does not assume a regular path between them. |
| Mapped | Its Text 5.8 states Q^s=0. Verify the same cut/domain identification so that E^r=E^good, removing RC-transfer. Prove RC-size and RC-far for the actual G, including coefficient response, polynomial moment control and normalization. If the slow cut tier is present, give its endpoint and radius rates and an amplitude meeting RC-rates, e.g. the z_j^(1/2) type with the polynomial absorption above. The stated C(L)g_j^2 slow tails do not meet this contract. The interface gate's HS-T proposal is a proposed source for that estimate, not a proof for this inserted current. |
| Either, for the extension | Give the same measurable midpoint/zero convention under c' and c'' exchange, and complete (MC) at every radius that its finite tori can require. Alternatively estimate the actual exceptional completion term in (I-K3); setting it to zero or changing the current would change Lemma 14.16 and the source recipes. |

No proof from one attempt is supplied to the other. The table is a
consumer specification, not a gate on either producer's derivation.
Theorem 18.3 uses its own chart/projector expression; to use it for (CUR)
one must match the current under the current chart, not just observe that
both antisymmetric sums vanish. A different current plus a changed h
can preserve the total identity while changing the local source being
estimated. That replacement is not made.

**Conditional result.** RC_j and (MC) imply exactly (I-K3), without a
rarity or screening premise for this particular extension step. The
regular K1 bound and the sharper estimate for h are not consequences
of RC_j. Rarity, (SCR_j), lower-level moments and locality remain inputs
to the separate transport and history arguments.

**Stop.** Step 1 has not closed for the specified current. Step 2 was
not entered: no new theorem replaces Lemma 14.15(c) or Lemma 20.5, no
regular z/beta induction is certified, and the weights, second-tier
transport margins and cap factor two remain unchecked. Step 3 was not
entered: no Q(n), sharper mu moments, intermediate-level cumulant bound
or all-partition level sum was proved.

**Reading and execution limits.** Read GOAL and FINISH; sections 7--8
and the recipe/source/consumer sections of generated-observable-history;
all of history-budget-sum; the upper-chain clauses and proofs at
14.14--14.16, 14.13, Text 18, 20.3--20.4, 21.1--21.2 and 21.7--21.8.
Compared the producer statements in mapped Text 5.8, independent I(k)
and its current Requests/coordinate and N_good statements, and interface
gate D5 (mapped) and D9 (independent). Some bounded producer excerpts
also contained surrounding explanations; none was imported as a proof,
and no producer library proof was checked. The fourth-form cumulant
findings were not rechecked at this step. Workflow/skill guidance was
read from the same pinned Git tree; the user's narrower scope overrides
its campaign, external-landing and delegation procedures.

All new mathematics here is analytic author work. Earlier numerical
results were not rerun; only file/hash bookkeeping and textual checks
were run. No numerical lock was needed. No subagents, audit, commit,
push, PR or edits outside the authorized output paths were used.
