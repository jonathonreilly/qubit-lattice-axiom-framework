---
claim_id: mobile_records_lifetime_activity_and_terminal_correlations_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For the supplied nearest-neighbor permanent-record insertion and vacancy-only hopping process on Z^d or corresponding tori, fixed positive formation intensity, bounded mobility and positive bounded pair weights give explicit exponential vacancy and local late-update bounds. Every site eventually holds a fixed record. A tagged-record argument gives finite lifetime hopping for every record, including inhomogeneous initial configurations, with an explicit tail; the translation-invariant case also has sharper mass-transport and per-site birth-budget identities. Spatial product initial laws yield exponentially decaying terminal connected single-site correlations, uniformly in torus volume. These are bounds for this stated stochastic generator, not a physical clock, equilibrium identification, field theorem or exclusion of other moving-record dynamics."
upstream_dependencies:
  - mobile_records_rare_formation_event_law_and_six_site_witness_bounded_theorem_note_2026-09-20
runner: scripts/mobile_records_lifetime_activity_terminal_correlations_2026_09_21.py
---

# Lifetime activity and final correlations of moving permanent records

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** proposed_retained
**Author support:** conditional-support; no independent audit verdict.

A record can leave a site and another can form there. Under the particular
positive formation clock studied here, that reuse has a finite lifetime at
each site, even on an infinite lattice. This note quantifies the available
activity and proves a spatial correlation bound for the final record pattern.
The estimates depend on the supplied clock and vacancy-only motion. They do
not identify those rules with physical time evolution or close other routes
to mobile records, quantum fields, or a TOE.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Can site reuse under the stated positive formation clock sustain local activity or an unbounded terminal correlation scale?"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Compare dynamics that retain mobility after local capacity fills, and test the operational content and clock of formation."
conditional_surface_status: "Explicit lifetime and connected-correlation bounds for a supplied stochastic process; rates and weights held fixed."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Conditional probabilistic proofs with separate pre-source checks and finite-generator controls."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 1. Model, assumptions, and existence

Use Z^d, d>=1, or a simple nearest-neighbor periodic torus whose every
period is at least three. These graphs have degree z=2d.
A site is vacant or holds one of six permanent records. Its content moves
with it and never changes. At a vacant site x, content a is inserted at rate

```
epsilon product_(occupied y neighboring x) W_(a,s_y).
```

W is a finite symmetric matrix with strictly positive entries; its rows
need not sum to six. On each undirected nearest-neighbor edge a rate-kappa
proposal exchanges occupied and vacant endpoints, with heatbath acceptance
w(s')/[w(s)+w(s')], computed by cancelling unchanged occupied-edge factors.
No occupied-occupied swap, deletion, export, new site, or additional dynamical
variable is included. Fix epsilon>0 and finite kappa>=0. The initial law is
independent of all future proposal clocks. Its spatial hypotheses are stated
separately below; local fixation does not require spatial independence.

This restates the model of the [event-law note](MOBILE_RECORDS_RARE_FORMATION_EVENT_LAW_AND_SIX_SITE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-20.md),
a provisional checked but unmerged dependency in PR #8545 at
`689941783bea870e08458e079ddb208257d0083d`. Its rare-formation theorem is not
used to replace the present evolving distribution by equilibrium. The axiom
memo selects neither this clock nor this acceptance law, and supplies no
conversion of the abstract time parameter to seconds.

Define

```
ell=min(1,min W),       u=max(1,max W),
alpha=6 epsilon ell^z,  beta=6 epsilon u^z,  lambda=z kappa.
```

Every vacancy's total birth hazard lies in [alpha,beta]. The factors min(1,...)
and max(1,...) are necessary because some sites have fewer occupied neighbors.

For existence, put independent marked site clocks of total rate beta and
edge clocks of rate kappa. A site mark chooses a content uniformly and accepts
with probability its occupied-neighbor weight product divided by u^z, provided
the site is vacant. An edge mark implements the heatbath acceptance locally.
Birth maps read radius one; a hop reads the endpoints and their neighbors,
at most distance two from an updated site. No infinite product w is used.

Backward exploration from a finite set at finite time has per-needed-site
clock rate at most beta+z kappa and bounded offspring at each encountered mark.
It is dominated by a branching process with total rate proportional to its
size, hence has finitely many ancestors almost surely at every finite time.
The consistent finite explorations define the infinite process, its local
finite-volume limits, and its translation covariance. They also justify
the bounded local generator and compensator identities used below.

## 2. Sharper identities under spatial translation invariance

For a translation-invariant initial law let v(t)=Pr(site 0 vacant at t) and
v0=v(0). Incoming and outgoing expected hop flux cancel after translation,
without reflection symmetry or independence of the initial law. If r_0 is
the birth rate including the vacancy indicator, then

```
v'(t)=-E[r_0(s_t)],
alpha v(t)<=E[r_0(s_t)]<=beta v(t),
v0 exp(-beta t)<=v(t)<=v0 exp(-alpha t).
```

Consequently the expected number of births at a fixed site after T is exactly
v(T), and its expected total number of births is v0. From the empty state
the mean is one, although particular sites can form multiple records. Other
sites can receive their final record entirely by motion. This identity is
an ensemble budget, not a one-birth-per-site restriction.

An incident accepted hop requires a vacancy at one of its two endpoints,
so its expected contribution to site updates is at most 2lambda v(t).
If J_x(T,infinity) counts births and accepted hops that update site x, then

```
E[J_x(T,infinity)] <= v0(1+2lambda/alpha) exp(-alpha T).       (1)
```

Finite expected counts imply finitely many updates almost surely at every
site. Since v(t) tends to zero, the final state is occupied almost surely.
Countability makes this simultaneous at all sites. This is local fixation;
it is not a single finite time when the infinite lattice becomes full.

The translation-invariant birth budget has a clock-independent extension.
Consider a well-defined translation-covariant finite-range process, with
translation-invariant initial data, nonnegative insertion rates and
conservative local motion. Assume rates are uniformly bounded over sites
on every finite time interval, so the local compensator identities apply.
The rates may depend on time. Without removal, export, or new sites, the
same flux cancellation gives
E[total births at 0]=v0-lim_t v(t)<=v0. This statement alone does not give
finite lifetime hopping. The positive hazard floor in this note gives
the stronger integrable vacancy-time bounds.

## 3. Uniform local fixation for arbitrary initial laws

Label each initial vacancy by its starting site a. Hops transport that vacancy
label oppositely to a record; births kill the label. No new vacancy label is
created. Write S_a(t) for its survival indicator and K_a(t) for its hop count.
Its killing rate is at least alpha and its hop rate at most lambda. For delta>0,
the exponential compensator therefore gives

```
E[S_a(t) exp(delta K_a(t))]
 <= Pr(a initially vacant) exp[(-alpha+lambda(exp(delta)-1))t].    (2)
```

One can first stop the hop count and then use its bounded-intensity Poisson
exponential-moment domination to remove the stopping. No independence of the
path, survival event, or surrounding contents is assumed.

If this label occupies x at time t, it made at least dist(a,x) hops. For
lambda>0 choose exp(delta)=1+alpha/(2lambda), sum (2) over initial labels,
and bound their initial vacancy probabilities by v_*=sup_a Pr(a vacant at 0).
The product of d geometric sums yields

```
Pr(x vacant at t) <= v_* A exp(-gamma t),
A=(1+4lambda/alpha)^d,          gamma=alpha/2.                 (3)
```

For lambda=0 the stronger direct bound v_*exp(-alpha t) suffices. On a torus,
choose one shortest coordinate displacement for each site; its sum is no
larger than the Z^d geometric sum. Thus the constants are uniform in volume.

At site x the birth rate is at most beta times its vacancy indicator; incident
hop rates sum to at most kappa sum_(y~x)(V_x+V_y). Integration of (3) gives

```
E[J_x(T,infinity)] <= C exp(-gamma T),
C=(beta+2lambda) v_* A/gamma.                                (4)
```

This proves occupied local fixation for every initial law independent of
future clocks, including spatially correlated and inhomogeneous laws. It
does not extend the exact homogeneous per-site birth budget to each site of
an inhomogeneous configuration.

## 4. Tagged-record lifetime: two separate arguments

Local fixation alone would not prove that a record stops: it might keep
visiting previously unvisited sites. A separate estimate is needed.

For translation-invariant data there is a short mass-transport proof. Give
each initial record its starting site as origin and each new record its birth
site; distinguish multiple births by their local birth indices. For every
hop, send one unit of abstract mass from that record's origin to its departure
site. The resulting nonnegative translation-covariant array T satisfies,
by Tonelli and reindexing,

```
E[sum_y T(0,y)] = sum_y E[T(-y,0)] = E[sum_y T(y,0)].
```

The right-hand side counts departures from site 0, whose mean intensity is
at most lambda v(t). Therefore

```
E[all lifetime hops of records with origin 0] <= lambda v0/alpha. (5)
```

Countability proves finite hopping for every record. The bookkeeping labels
add no variable or transition to the actual dynamics.

There is also a uniform tagged bound that does not require translation
invariance. Start an initial tagged record at x0 in an arbitrary configuration,
or restart the clock at a specified birth time. Use v_*=1 in (3). Its hop
count N_t has intensity at most lambda, so E[exp(N_t)]<=exp(lambda(e-1)t).
Put c=lambda(e-1)+gamma. Then Pr(N_t>ct)<=exp(-gamma t). On the complementary
event the tag is within graph distance ct of x0. A further hop requires a
nearby vacancy. Sum (3) over all possible nearby destinations, without
assuming independence between the tag and vacancies, to bound the expected
instantaneous tagged hop intensity by

```
lambda [1+A(2ct+3)^d] exp(-gamma t).                         (6)
```

The first term covers the unusually fast tag; the second covers its whole
remaining search ball. Integration yields the uniform bound

```
E[N_infinity] <= lambda/gamma
 +lambda A sum_(k=0)^d binom(d,k) 3^(d-k)(2c)^k k!/gamma^(k+1). (7)
```

For lambda=0 the count is zero. For later births, apply the strong Markov
property of the marked construction at each site-indexed birth time. The
bound is independent of the configuration then. Initial sites and local
birth indices form a countable set, so every record makes finitely many
hops simultaneously almost surely for arbitrary initial data.

For m>=1 and lambda>0 take T=m/(2e lambda). Poisson domination gives
Pr(N_T>=m)<=2^(-m). If there are at least m lifetime hops otherwise, at least
one occurs after T. Consequently

```
Pr(N_infinity>=m)
 <= 2^(-m)+lambda integral_T^infinity [1+A(2ct+3)^d]exp(-gamma t)dt. (8)
```

The integral is an explicit polynomial in T times exp(-gamma T). This is
also a maximal-displacement bound. Its constants can be extremely large;
it is not a physical travel-distance prediction.

## 5. Dependence propagation and final connected correlations

Now impose a spatial product initial law. Its marginals can differ between
sites. This additional independence is essential for decorrelation, although
it was unnecessary for the activity bounds.

Set Lambda=(z+1)(beta+2z kappa). A queried site has birth-clock dependency
weight at most beta(z+1), and incident-edge dependency weight at most
2z kappa(z+1). A potential backward dependency step travels at most two.
The expected number of chronological dependency paths of m steps in a
time interval of length t is at most (Lambda t)^m/m!. This is the Poisson
factorial-moment count over the ordered time simplex. Repeated use of the
same clock at distinct times is included; paths need not be independent.

Couple the full process to the process on the induced graph ball B_R(x),
deleting crossing edges, using the same internal clocks and initial values.
If the potential dependency exploration does not leave the ball, the state
at x agrees in both constructions. A crossing edge or an acceptance rule
reading an outside neighbor is counted as an escape. Such an escape requires
a path prefix of m=floor(R/2)+1 steps, so the mismatch probability is at most
(Lambda t)^m/m!.

For sites x,y at graph distance D>=1 choose R=floor((D-1)/2). Their two
induced balls use disjoint random inputs and their truncated observables
are independent. Here m=ceil(D/4). Let f,g be bounded single-site content
functions, with sup norms M_f,M_g, and extend them to vacancies by zero.
Combine a local fixation tail C exp(-gamma t), from (1) or (4), with the
finite-ball mismatch. Comparing joint moments and products of means gives

```
|Cov(f(s_infinity(x)),g(s_infinity(y)))|
 <= 8 M_f M_g [C exp(-gamma t)+(Lambda t)^m/m!].               (9)
```

For the homogeneous case one may use gamma=alpha and
C=v0(1+2lambda/alpha); for general product data use (3)-(4).
Take t=m/(2e Lambda). Since m!>=(m/e)^m, the second term is at most 2^(-m).
Also gamma<=alpha<=beta<=Lambda, so gamma/(2e Lambda)<log 2. Cauchy-Schwarz
gives the trivial covariance bound M_f M_g. Altogether,

```
|Cov(f(s_infinity(x)),g(s_infinity(y)))|
 <= M_f M_g min{1,8(C+1)exp[-gamma D/(8e Lambda)]}.           (10)
```

For complex functions the second factor may be conjugated, with the same
argument. All constants hold uniformly over tori at their periodic graph
distance. The bound gives exponentially accurate local approximations. It
does not assert an exact finite coding radius or independence beyond some
fixed separation.

On Z^d, the number of sites at a graph radius grows polynomially, so the
absolute covariance sum is finite. Its torus counterpart is uniformly bounded.
The variance per volume of a sum of centered bounded local observables is
therefore bounded. For cubic content-symmetric weights and the empty initial
state, the vector mean is zero, and E[|sum_x v(s_infinity(x))|^2]/V has a
volume-independent finite bound. This does not give a practically small
bound on the structure factors measured in modest simulation volumes.

Finite-time local couplings and the uniform late-update tail also show that
terminal finite-dimensional torus marginals converge to the infinite-lattice
terminal law as the minimum periodic side length tends to infinity, for a
fixed homogeneous product initial distribution. Growing volume with a bounded
period is insufficient. One
does not substitute a finite global absorption time for the infinite system.

## 6. Controls and counterexamples that preserve the scope

For W=1 and homogeneous product initial data, the exact product evolution has
vacancy density v0 exp(-6epsilon t). It gives mean births v0 and departures
lambda(v0-v0^2/2)/(12epsilon) per site. From the empty state the terminal
contents are independent uniform marks. A nonconstant W can leave finite
nonzero terminal correlations; (10) is a decay bound, not a claim of no
correlations at finite separation.

On two sites, W=1, initially empty, the probability of two births at a
specified site is kappa/[4(6epsilon+kappa)]. Before the second birth the first
record alternates sites at rate kappa/2 while the remaining vacancy forms at
rate 6epsilon. Its lifetime hop count is geometric, with continuation
q=kappa/(12epsilon+kappa) and mean kappa/(12epsilon). Averaging its starting
site gives the repeated-birth probability. This shows actual site reuse and
arbitrarily large possible hop counts with finite means.

Fixation alone does not imply (10). A fully occupied initial configuration
with one shared random choice of +e_x or -e_x is already fixed; its first
coordinate has mean zero and covariance one at every separation. It is
translation invariant and a mixture of product laws, but is not itself a
spatial product law. The initial-independence hypothesis cannot be dropped.

The infinite system generally remains incompletely filled at every finite
time. For example, from an empty start choose infinitely many separated
sites. At any fixed finite time t, each has positive probability of no site
or incident-edge proposal before t, leaving it vacant. These events can use
disjoint clocks, so infinitely many occur almost surely. Intersect over
integer times to distinguish local fixation from finite global filling.

The fixed positive parameters matter. As epsilon tends to zero at fixed
mobility, or a positive weight floor is lost, the bounds can diverge. These
proofs do not exchange those limits with time, distance, or volume. Multiplying
both rates by the same positive constant only rescales time and leaves the
terminal law and dimensionless correlation bounds unchanged.

Occupied-occupied exchanges, persistent fields or internal carrier variables,
time-dependent clocks without a positive floor, deletion/export, and growing
site sets are other processes. Filling vacancies need not stop their activity.
Initial long-range correlations and nonlocal observables are also different
questions. A physical model can pursue such mechanisms; this theorem neither
selects them nor declares them unavailable.

## 7. Evidence and status

The general conclusions follow from the displayed probabilistic arguments;
finite tests do not certify an infinite-distance or infinite-time limit.
The primary runner checks local generator bounds, translation-orbit flux
balance, vacancy-label exponential drift, exact uniform-weight controls,
the repeated-birth witness, dependence geometry and finite terminal laws.
Declared mutations target specific load-bearing assumptions.

Separate pre-source evidence is preserved in
`.claude/science/mobile-record-lifetime-correlation-20260921/independent_local_activity/`
and `independent_terminal_correlations/`. The original activity report has
SHA-256 `7b4bad382af9d326a7de018db2bc8acd272fd960e16ac5c1a8cd4dba853e4ca4`;
the correlation report has SHA-256
`6249af1ec44d27467c3378641c225cadadda6fd4f9a794560dbf6a6991bf106e`.
They were read completely and their arguments reconstructed by the primary
author. The general vacancy-label extension and sharper covariance constants
are credited to the second independent calculation. The arbitrary-initial-data
tagged estimate (6)-(8) and the clock-independent budget extension are subsequent
primary derivations subsequently reconstructed in the complete-source review
under `final_source_review/`. Its exact tagged-state controls supplement the
proof; they do not certify the infinite-lattice conclusion. The reviewer
requested two torus qualifications. This revision states simple periods at
least three for degree z=2d, and requires every period to diverge for the
terminal local limit. The correction receipt and any subsequent narrow
acknowledgment preserve the reviewed and corrected source identities.

The review is selective scientific scrutiny, not independent retention. No axiom,
primitive, editable prompt, audit verdict, or effective-retention surface is
changed. Standard graphical constructions, compensator estimates, mass transport,
and finite-propagation bounds are used with explicit hypotheses; no novelty
is claimed for those general methods.
