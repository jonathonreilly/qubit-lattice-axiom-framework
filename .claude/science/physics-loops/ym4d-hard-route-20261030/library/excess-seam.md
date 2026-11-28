State of attack
==============

**Gap; honest stop at item 1, before (LC).** The mapped order fixes the
positive top weight rate nu, and the spatial rate mu read from DS, before
L. A finite shell coefficient A_s(L) alone does not establish (WAM) at
that rate. The missing quantitative condition is (RATE) below, or the
weaker exact absorption condition (RATE-exact). Neither is established
here for the proposed four-dimensional seam. Thus the shell route
survives as a conditional proposal; it does not yet supply the current
FALL/DS input. This is not a counterexample to Yang--Mills or to (LC).

Pinned source: `33ea3a9e32e9b0959f7a624e9812ffe278a0279b`.
Author: OpenAI Codex, 2026-11-01. Bounded author work; no independent
check or audit. No numerical computation. All paths below are relative
to `.claude/science/physics-loops/ym4d-hard-route-20261030/`.

**Discharged source inspection; unchecked mathematical inputs.** Read
`library/excess-shell-end.md` in full first. Its internal provenance is
an older commit; the text inspected here is its version at the pinned
commit above. Read GOAL, the required FINISH sections, mapped line 24,
FALL and DS with their intervening argument in `library/sector-values.md`
Section 3B, Theorem F and its setting in `library/fibre-propagator.md`,
the finite-range inverse in `library/excess-finite-range-repair.md`
Sections 1--2, and Theorems EX and EX-loc with their displayed proofs in
`parts/hard-core--excess.md` Sections 1.6--1.7 and setting 1.1.
Their cited antecedents have not been rederived here. In particular,
reading those statements does not discharge their proofs or applicability.
The following argument concerns the rate interface, not those theorems.

## 1. Which rate can be chosen when?

**Discharged: the written order.** Line 24 of
`parts/hard-core--mapped.md` orders

    delta_#, rho_1, rho_f, nu <= delta/4,
    delta'' := min(delta_#/2, nu), mu <= delta''/2;
    ...; L >= L_0; ...; q(L), C_F(L), rho_s(L), mu_c(L); ... .

Consequently nu and mu are pre-L choices in this contract. The later
quantities q(L) and C_F(L) are the depth contraction and its prefactor;
they are not spatial weight rates. Allowing their L dependence does not
allow nu to be chosen again after L.

**Implication: FALL considered by itself permits a smaller rate.** Its
stated weight hypothesis is only that log W is Lipschitz with rate
nu <= delta/4 in top cells (with the other source ceilings also enforced).
For a fixed L, a choice nu(L) obeying those ceilings is therefore in
that hypothesis. This observation is about substitution into a
conditional statement, not a proof of FALL. Uniformity over the required
weight family is still necessary. If a new proof has constants depending
on the chosen positive rate, these must be recorded; at fixed L and a
fixed nu(L) they are functions of L, not of depth or volume.

**Discharged: the top is the restrictive level.** In the sampled
convention, nu_l = nu L^(l-k), for 1 <= l <= k. Since L > 1,
0 < nu_l <= nu, with equality at l=k. For one common nonnegative
coefficient b_s, b_s nu_l <= b_s nu. Thus lower-level improvement does
not repair a failure at the top. The same statement follows for the
exact coefficient 2 A_s M_* sinh(nu_l r), since sinh is increasing on
the nonnegative axis: its derivative is cosh >= 1.

**Discharged source interface; implication for its use.** CRUDE uses
W_y(z)=exp(-nu d(z,y))/C_nu. DS states its first two derivative bounds
at rate

    alpha = delta''/2 = min(delta_#/2, nu)/2,

and says explicitly that this is the rate the closure reads and that
mu <= alpha. Hence keeping the current mu > 0 requires

    nu >= 2 mu,             delta_# >= 4 mu.                 (DS-rate)

These are just the two inequalities equivalent to
2 mu <= min(delta_#/2,nu). Shrinking nu below 2 mu changes the promised
output. A larger prefactor cannot generally restore a faster rate:
for alpha < mu, exp(-alpha R) <= C exp(-mu R) for every distance R
would imply exp((mu-alpha)R) <= C. The latter has no finite C as
R grows. This proves a limitation of the rate inference, not that
the actual DS kernels attain their stated bound.

**Discharged: the superseded objection must not be used.**
`library/one-step-closure.md` Sections 1 and 4 still use a spatial
profile and the high-order lift estimate. Section 10 explicitly
replaces Sections 5--6 and drops the old low-order requirement that
rho^(-4) L^(-2) contract. Thus that old requirement does not prove
that every possible nu(L) repair is impossible. The current Section 10
does, however, still read DS at its specified norm rates; orders 3 and
4 have further rate losses, and Section 4 supplies orders 5 and 6.
A new post-L choice of nu together with a new mu, and corresponding
profiles and source bounds, would be a revised interface needing a
joint constants argument. No such revision is made or proved here.

## 2. The precise absorption obligation

**Implication, with proof.** Assume (E-SHELL) for the relevant superlevel
sets, with coefficient A_s >= 0, radius r >= 0 in top units and a
symmetric probability kernel K. Fix a positive rate ceiling nu_req
equal to the required top rate, and suppose

    M_* := sup_(depth,volume) sum_z K(z) exp(nu_req d(z,0)) < infinity.

Write P=A_U(w), Q=A_T(w) for the normalized Wilson actions, and let
w have sampled rate 0 <= s <= nu_req.
For D_t={w>t}, the integral of its shell indicator at z is
w_r^+(z)-w_r^-(z), where the two values are the maximum and minimum
of w within radius r. This follows by integrating the interval
between those two values of t. The Lipschitz inequality gives

    w_r^+-w_r^- <= (exp(sr)-exp(-sr))w = 2 sinh(sr)w.

Also (K*w)(z) <= M_* w(z), term by term by the same Lipschitz
inequality. Integrate (E-SHELL) in t and interchange the finite sums
with the integral. Transfer K from the shell indicator to w by its
symmetry. This gives

    P-Q <= beta(s)(P+Q),       beta(s)=2 A_s M_* sinh(sr).

Since sinh(sr)=integral_0^(sr) cosh(t) dt and cosh is increasing
for t >= 0,

    beta(s) <= b_s s,
    b_s := 2 A_s M_* r cosh(nu_req r).

The sufficient requirement used in `excess-shell-end.md` is therefore

    2 A_s(L) M_*(L) r(L) cosh(nu_req r(L)) nu_req <= 1/2.  (RATE)

When (RATE) holds, (1-beta)P <= (1+beta)Q and

    P <= [1 + 2 beta/(1-beta)]Q <= [1+4 b_s s]Q.

This is (WAM) with D_A=4 b_s, uniformly for 0 <= s <= nu_req.
It includes s=0 without division by s or by Q. If Q=0, the same
positive coefficient 1-beta forces P=0.

**Implication: one can weaken the sufficient condition, but not omit
absorption.** The value 1/2 in (RATE) is convenient, not necessary for
this algebra. It suffices to prove

    beta_* := 2 A_s(L) M_*(L) sinh(nu_req r(L)) < 1.        (RATE-exact)

Then D_A=2 b_s/(1-beta_*) works by the preceding calculation. At
beta_* >= 1 the integrated inequality supplies no upper bound for
P/Q at the top rate: its coefficient of P is nonpositive. Failure
of (RATE) alone is consequently not a refutation of (WAM).

**Gap: quantitative data for the actual seam.** No values or estimates
for the actual A_s(L), r(L), M_*(L) proving (RATE) or (RATE-exact) at
the preselected nu_req have been supplied by the inspected statements.
Finiteness for each L is not such an estimate. With mu kept fixed,
even allowing nu to vary leaves the restriction nu >= 2 mu from
(DS-rate); there is no permission to make nu arbitrarily small.

**Implication: what an absolute coefficient would accomplish.** A
uniform bound on the entire effective coefficient is sufficient. For
example, suppose, before choosing nu, one proves

    A_s(L) <= A_0,   r(L) <= r_0,
    sup_(L,depth,volume) sum_z K(z) exp(bar_nu d(z,0)) <= M_0

at some fixed bar_nu > 0. Put
B_0=2 A_0 M_0 r_0 cosh(bar_nu r_0). Choose
0 < nu_req <= min(bar_nu,1/[2(1+B_0)],the source rate ceilings),
then choose mu <= min(delta_#/2,nu_req)/2, and only then L. This
proves (RATE), since b_s <= B_0 and B_0 nu_req <= 1/2.
It is a conditional order of choice, not an established seam bound.

**Discharged logical distinction.** A_s itself need not literally be
independent of L if the complete product in (RATE) is controlled at the
ultimately chosen admissible L. A uniform bound on A_s alone is also
insufficient without control of r and M_*. An explicit proof that the
eventually chosen L simultaneously meets L >= L_0 and (RATE-exact)
would suffice; uniform bounds in L are one way to provide it. An
unquantified C(L), followed by an instruction to shrink the already
fixed nu, is not that proof.

## 3. Hand diagnostic: finiteness alone cannot give the missing inference

**Discharged: scope and criterion.** Test only the algebraic inference
from nonnegative action densities, equal unweighted total actions, and
(E-SHELL) to (WAM) at a prescribed nu > 0. A counterexample to this
inference consists of such densities with common shell constants and
unbounded weighted energy ratio as volume grows. No assertion is made
that these densities are Wilson actions, curvatures, or class lifts.
Thus this test cannot refute the four-dimensional Yang--Mills claim;
it can exclude a purely scalar removal of the rate obligation.

**Discharged: construction and shell bound.** On the four-dimensional
periodic anchor set (Z/NZ)^4, write z=(i,y), 0 <= i < N, and let y
range over the other three coordinates. Put

    gamma := exp(-nu/2),       c_N := (1-gamma)/(1-gamma^N),
    u(i,y) := c_N gamma^i/N^3,  t(i,y) := 1_{i=0}/N^3.

Both densities are nonnegative and have total mass one. Indeed
(1-gamma) sum_(i=0)^(N-1) gamma^i = 1-gamma^N by cancellation,
and there are N^3 transverse sites. For every set D, consider each
line D_y={i:(i,y) in D} separately. If 0 is in D_y, then

    sum_(i in D_y) [u(i,y)-t(i,y)] <= 0,

since the total u-mass of that line is N^-3, equal to t(0,y).
If 0 is not in D_y, decompose D_y into maximal consecutive intervals
[a,b] inside {1,...,N-1}. For each interval, a-1 is outside D_y, so
(a,y) lies in S_1(D): it is in D and has a nearest neighbour outside.
Furthermore, multiplying the finite geometric sum by 1-gamma gives

    sum_(i=a)^b u(i,y)
        = u(a,y) (1-gamma^(b-a+1))/(1-gamma)
        <= u(a,y)/(1-gamma).

Sum this bound over intervals and lines without 0 in D_y, discarding
the nonpositive contributions of the other lines. Each interval start
is a distinct shell anchor. Consequently, for every D,

    sum_D(u-t) <= (1-gamma)^-1 sum_(S_1(D)) u
               <= (1-gamma)^-1 sum_(S_1(D)) (u+t).

This is (E-SHELL) for these densities with

    A_s^model=(1-gamma)^-1,       r=1,       K=delta_0,       M_*=1,

uniformly in N and in the set D. Periodicity causes no exception:
the distinguished coordinate 0 cuts the cyclic line into the finite
ordered interval used above. A translated construction obeys exactly
the same constants.

**Discharged: failure at the prescribed weight rate.** Take
w(i,y)=exp(nu d_N(i,0)), where d_N is the cyclic distance. For any
i,j, the triangle inequality gives
|d_N(i,0)-d_N(j,0)| <= d_N(i,j). This is at most the product torus
infinity distance between (i,y) and (j,y'), so w has log-Lipschitz
rate nu in that distance. Its t-energy is one. For N=2m, the slice
i=m alone gives

    sum_z w(z)u(z) >= c_(2m) gamma^m exp(nu m)
                    >= (1-gamma) exp(nu m/2).

The last inequality uses 1-gamma^(2m) <= 1. Its right side tends
to infinity, so no finite, volume-independent D_A gives
sum w u <= (1+D_A nu) sum w t. All shell constants above are finite
at the prescribed nu. They correctly fail the absorption test:
1-exp(-nu/2) < nu/2, by integration of exp(-s)<1, and
sinh(nu) >= nu, by integration of cosh(s)>=1. Thus
2 A_s^model sinh(nu)>4. This example does not contradict the proved
conditional implication: it fails the absorption hypotheses.

**Discharged scope.** Multiplying both densities by any positive
number preserves their shell bound and their weighted ratio; multiplying
w by a positive number also preserves the ratio. Hence the scalar
problem is not repaired by an amplitude or weight normalization choice.
This is a written finite geometric-series argument for every m, not
a computation or an enumeration. It supplies no gauge field H and is
not a kill test of (LC).

## 4. Constants and the stopping decision

**Discharged dependency accounting; missing bounds remain gaps.**
All sought Yang--Mills comparison constants must be free of coupling x,
depth, volume, position, sector, and multiplication of w by a positive
constant. The dimension, SU(2), blocking profiles and chosen fixed rate
margins may enter. Additional dependencies are as follows.

| Quantity | Dependence and status |
|---|---|
| nu_req, delta_#, mu | Pre-L choices in the mapped contract; their source theorem bounds are unchecked here. (DS-rate) is the discharged interface restriction. |
| L | The fixed odd block side, chosen after the preceding rates; not a depth or volume parameter. |
| A_s, r, M_* | May depend on L and fixed rate choices as proposed in (E-SHELL), but must meet (RATE-exact) at nu_req. Their existence with that property is a gap. The kernels themselves may vary with the lattice; their moment bound must not. |
| b_s, beta_*, D_A | The displayed formulas; may depend on L and nu_req. D_A is finite only under the stated absorption margin for this proof. |
| bar_nu, A_0, r_0, M_0, B_0 | Hypothetical uniform inputs and their displayed combination, independent of L as well as the other forbidden dependencies. Their actual seam bounds are gaps. |
| q(L), C_F(L) | The FALL depth contraction and prefactor, distinct from spatial rates. The scalar reduction permits L dependence; application to the chain remains conditional on its inputs. |
| gamma, A_s^model | Depend only on the fixed positive nu in the scalar diagnostic; independent of volume and location. |
| c_N, N^-3 | Volume-dependent density normalizations in the diagnostic, not comparison constants; the proof displays them and its volume-independent estimates explicitly. |

**Unchecked: the supplied linear tools do not fill this rate slot by
their statements alone.** Theorem F states an absolute decay rate for
the gauge-fixed tangent saddle inverse, with chart prefactors C(L).
It does not state (LC), (E-SHELL), or (WAM) for the endpoint pair.
The finite-range repair makes a near-identity correction invertible
by taking the flux threshold small after L; its moment construction
inverts a source of squared flux. Neither statement provides a bound
on the full seam coefficient at nu_req. Using either to construct and
estimate the seam would require additional work; no such applicability
is certified here.

**Gap: first stop and exact reopening conditions.** Under the existing
consumer rates, the shell proposal must establish (E-SHELL) together
with (RATE-exact), for the same admissible L and the required nu_req.
Proving uniform effective shell constants and then a compatible pre-L
rate choice is a sufficient way forward. Alternatively a direct proof

    A_U(w) <= [1+D_A(L) s] A_T(w),    0 <= s <= nu_req,     (WAM-req)

with one D_A(L) uniform over those weights and the other variables
would bypass shell absorption. A proof only at s <= nu_small(L)
does not give (WAM-req) if nu_small(L) < nu_req. A post-L rate repair
would have to restate DS at alpha(L), change mu and the consumers as
needed, and prove a consistent constants order. The superseded
low-order contraction argument does not rule out that repair; this
note does not establish it.

**Gap: items 2 and 3 are not reached.** Per the requested first-stop
rule, no parent-fixed representatives or cutoffs satisfying (LC) are
claimed, and no nonlinear X_D is constructed. A future (LC) proof
with an arbitrary finite C_seam(L) would still need to address the
rate slot above. The parent-fixed local gauge estimate for H, the
first-order [Q_n,chi]H term, intermediate class membership, and the
complete nonlinear replacement cost R_D all remain open. No zero-curl
increment has been assigned zero nonlinear action, and no locked
action at frozen fine data has been used as a payable budget.

**Discharged: work boundary.** Only `library/excess-seam.md` was
written. Additional source inspection for the rate question was
`library/one-step-closure.md` Sections 1, 4, 9--10 and
`library/sector-values.md` hostile points, especially (13), (17)--(18).
Some initial locator and combined outputs were truncated; consequential
mathematical ranges were then returned without truncation. No truncated
search output is used as proof coverage. The pinned workflow and
physics-loop procedure were inspected within the user's bounded scope;
no campaign or delivery workflow was launched. No forbidden-side file,
gate file, external proof account, or historical computation log was
opened. No numerical test, script, subagent, commit, push, post or audit
was run. The worktree status showed only this new file; the inspected
scientific sources match pinned HEAD. A whitespace check found no
errors. These mechanical checks are not mathematical verification.

**Discharged: what is proved.** The source's constants order fixes nu
before L; the rate substitution into DS imposes (DS-rate). The written
layer integration proves the conditional absorption formulas, including
the distinction between (RATE) and (RATE-exact). The scalar density
example proves that finite shell constants and equal unweighted totals
alone do not imply a volume-uniform (WAM) at a prescribed rate.

**Implication: what is conditional, and on exactly what.** (E-SHELL)
with its symmetric probability kernel, uniform exponential moment and
(RATE-exact) implies (WAM-req) with D_A as above. This supplies only the
weighted comparison slot in `excess-shell-end.md`: its trial estimate
(TR), class/minimality and fine-flux premises are still needed for
(UP), and its (INPUT) is still needed for FALL. DS additionally retains
its source, response, domain and spatial-rate hypotheses. None of those
other mathematical premises is newly discharged here.

**Gap: what is still open.** The first missing condition is the actual
four-dimensional seam bound with (RATE-exact) at the fixed consumer
rate, or a direct (WAM-req). A smaller-rate result would need a new,
proved consumer interface. (LC) and (GLUE-E) remain unattempted in this
session because that first dependency has not been resolved.
