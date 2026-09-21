# Local activity and tagged records at fixed positive formation intensity

Independent pre-source check of the supplied stochastic dynamics on Z^d and
translation-invariant finite tori. The initial law is arbitrary and translation
invariant; it need not be independent, reflection invariant, or ergodic.

**Result.** Vacancy density decays exponentially. Every fixed site has only
finitely many successful births and accepted hops, and eventually remains
occupied by one fixed content. A separate mass-transport argument proves that
every individual record also makes only finitely many hops almost surely.
On the infinite lattice this local fixation generally has no finite global
absorption time: conditional on a non-full translation-invariant initial
configuration, infinitely many vacancies remain at every finite time.

## Rates and existence of the infinite process

Let z=2d on Z^d, or use a common degree bound on the tori. Write

\[
w_- =\min(1,\min_{a,b}W_{ab}),\quad
w_+ =\max(1,\max_{a,b}W_{ab}),\qquad
\alpha=6\epsilon w_-^z>0,\quad \beta=6\epsilon w_+^z<\infty.
\tag{1}
\]

The actual total birth rate at a vacant site lies between alpha and beta.
Each undirected edge has a proposal clock of rate kappa, and each accepted
occupied-vacant hop has rate at most kappa. These bounds do not use the
row-six normalization; the original symmetric pair matrix is retained.

An infinite product w(s) is unnecessary. In the heat-bath ratio, cancel all
unchanged factors. The resulting acceptance depends only on the two endpoints
and their neighbors, through finite, strictly positive local products.

A graphical construction uses independent Poisson clocks of rate
epsilon w_+^z for each site/content birth channel, thinned by the local product
divided by w_+^z, and rate-kappa edge clocks thinned by heat-bath acceptance.
Use future clocks independent of the initial law. To determine finitely many
sites up to a fixed time, explore their ancestors backward through these
clocks. If the current queried set has size q, relevant clock rate is at most
(beta+z kappa)q, and one event adds at most 2(z+1) sites. A linear-rate
finite-offspring branching process dominates this exploration; its expected
size is bounded by an exponential on every finite interval, so it has no
finite-time explosion. Thus only finitely many ancestors are needed almost
surely. This constructs a unique consistent local process; sufficiently large
finite boxes give the same answer for each such graphical query. Translation
invariance is preserved. No infinite-volume equilibrium measure is invoked.

All event counts below mean **successful configuration changes**. Null proposal
clock rings can continue forever.

## Vacancy density and exact expected birth count

Let V_x indicate vacancy and v(t)=E V_0(t), with v(0)=v_0. Let B_x count
births at x, D_x record departures from x, and A_x record arrivals at x.
The pathwise site balance is

\[
V_x(t)-V_x(0)=D_x(0,t]-A_x(0,t]-B_x(0,t].
\tag{2}
\]

Translation invariance gives equal expected arrival and departure intensities
at a site. Sum directed edges and translate an outgoing edge to its incoming
counterpart; reflection invariance is not required. Taking expectations gives

\[
v'(t)=-E\,[\hbox{birth rate at 0}],\qquad
-\beta v(t)\le v'(t)\le-\alpha v(t).
\]

The bounded local rates justify this equation, or equivalently its integrated
compensator form. Therefore

\[
v_0e^{-\beta t}\le v(t)\le v_0e^{-\alpha t},
\qquad E B_0(0,t]=v_0-v(t).
\tag{3}
\]

In particular **E B_0(0,infinity)=v_0**, even though a vacated site can form
another record. This is a statement about its expectation, not a prohibition
on repeated births at the same site. No factorization of local correlations
was used. When W=1, alpha=beta=6 epsilon and v(t)=v_0 exp(-6 epsilon t)
exactly for every translation-invariant initial law.

## Finite local activity and local fixation

A record departure from x requires a vacant neighbor, so its intensity is
at most kappa sum_(y~x) V_y. An arrival at x requires V_x=1, so its intensity
is at most z kappa V_x. For each deterministic T>=0, (3) consequently gives

\[
E B_0(T,\infty)=v(T),\qquad
E D_0(T,\infty)=E A_0(T,\infty)
\le z\kappa\int_T^\infty v(s)ds
\le\frac{z\kappa}{\alpha}v(T).
\tag{4}
\]

Thus the expected total number of future transitions involving site 0 is at
most (1+2z kappa/alpha)v(T), and the bound decays exponentially in T. For a
single undirected edge the expected future accepted-hop count is at most
2 kappa v(T)/alpha. The factor two in the site bound counts arrival and
departure events; each global hop has only one departure.

A nonnegative count with finite expectation is finite almost surely. Hence
every fixed site has a last successful transition, and countability makes
this true for all sites simultaneously. Its eventual vacancy indicator exists;
dominated convergence and v(t)->0 make that limit zero. Therefore the site
eventually stays occupied with a fixed content. If T_fix(x) is its time of
permanent occupied fixation, then

\[
\Pr(T_{\rm fix}(0)>T)
\le(1+2z\kappa/\alpha)v_0e^{-\alpha T}.
\tag{5}
\]

In particular, repeated formation does not sustain successful activity forever
at a fixed site under these hypotheses.

## Tagged-record conclusion requires a separate argument

Local fixation alone does not logically imply tagged fixation: a path moving
to the right forever visits each fixed site only finitely often. The following
additional argument rules that behavior out for the present law.

Label every initial record by its initial site, and every later record by its
birth site and birth index there. These labels are bookkeeping only and move
with the immutable records. A record's total instantaneous hop rate is at
most z kappa, so its trajectory has no finite-time explosion.

Let R_x be all records originating at x, including an initial record if
present. Let M_T(x,y) count hops after absolute time T departing from y whose
record originated at x. These nonnegative counts are translation covariant.
By translation invariance and Tonelli's theorem,

\[
E\sum_y M_T(0,y)
=\sum_y E M_T(-y,0)
=E\sum_x M_T(x,0)
=E D_0(T,\infty)
\le\frac{z\kappa}{\alpha}v(T).
\tag{6}
\]

The left side counts all future hops, anywhere, of all records from origin 0.
It is finite. At T=0 this proves that their combined lifetime hop count is
finite almost surely. Apply the same conclusion at every origin and use
countability: **every initial or subsequently born record makes finitely many
hops almost surely**, and hence eventually remains at one site forever.

There is also an explicit expected-count statement:

\[
E\,\#R_0=(1-v_0)+E B_0(0,\infty)=1,
\qquad
E\sum_{r\in R_0}\#\{\hbox{lifetime hops of }r\}
\le\frac{z\kappa v_0}{\alpha}.
\tag{7}
\]

For a specified origin-labelled record whose existence has probability p>0,
its conditional expected lifetime hops are at most z kappa v_0/(alpha p).
For an initial record at 0 one can take p=1-v_0, when that is positive.
This is not a common deterministic hop cap; hop counts can have unbounded
support. Equation (6), rather than an inference from site fixation, supplies
the tagged result. It uses translation invariance but not ergodicity or a
stationary-in-time law.

## Local limits versus global absorption

On a finite torus with V sites, let T_full be the first completely occupied
time. Full configurations are absorbing, and

`Pr(T_full>t) <= E[number of vacancies at t] <= V v_0 exp(-alpha t)`.

Thus T_full is finite almost surely. The factor V prevents interpreting this
as a finite global absorption-time result on the infinite lattice.

On Z^d, a translation-invariant initial vacancy set is almost surely either
empty or infinite. To prove this without ergodicity, restrict to the invariant
event of between one and M vacancies. The expected vacancy indicator on that
event is the same at every site; its sum can be finite only if each expectation
is zero, which also makes that event have probability zero. Take the union
over finite M.

Conditional on an infinite initial vacancy set, choose infinitely many of its
sites at pairwise distance at least three. For any fixed finite t, each remains
vacant if its birth proposal clocks and incident hop proposal clocks have not
rung by t. These events use disjoint clocks and each has probability at least
exp[-(beta+z kappa)t]>0. Almost surely infinitely many succeed. Applying this
at every integer t proves that infinitely many vacancies remain at every
finite time. Therefore on the non-full initial event there is **no finite
global absorption time**, despite almost-sure local fixation and tagged
fixation. No contradiction arises from a pointwise fully occupied limit.

## Finite checks, exceptions, and scope

The exact checker verifies local/global vacancy balance and birth/hop bounds
on 3,087 state cases: a three-cycle for two matrices and a four-cycle for a
general matrix. Correlated cyclic-orbit laws check mean flux cancellation.
One four-cycle law has individual-edge vacancy flux -1/76 while both mean
site arrival and departure rates are 35/228: the divergence cancels even
though the edge current does not. No initial product law is assumed.

A separate exact absorption solve uses the two-site graph with a single
undirected bond, W=1 and an empty start. It finds

* expected births at each site: 1;
* probability of two births at a specified site: kappa/[4(6 epsilon+kappa)];
* expected lifetime hops of the first record: kappa/(12 epsilon);
* expected departures from a site, and expected total lifetime hops of all
  records originating there: kappa/(24 epsilon).

Until the second birth, the first record hops at rate kappa/2 and the next
birth occurs at rate 6 epsilon. Its hop count is geometric with continuation
probability kappa/(12 epsilon+kappa), demonstrating finite expectation but
unbounded support when kappa>0. At epsilon=1/7 and kappa=2/3, the repeated-
birth probability is 7/64 and the first record's expected hops are 7/18.
All three exact absorption parameter checks and all generator checks pass.

The positive formation bound is essential to this proof. With epsilon=0,
one record at a uniformly random site of the same two-site graph is a
translation-invariant counterexample: vacancy density stays 1/2, the hop
rate is kappa/2 forever, and the record and both sites have infinitely many
hops when kappa>0. If zero weights destroy the uniform positive birth bound,
if removals create new vacancies, or if local rates cease to be bounded,
the present argument does not apply. No assertion for arbitrary non-translation-
invariant initial laws is made. If v_0=0, the configuration is already full
almost surely; kappa=0 simply removes all hops.

These conclusions concern the supplied dynamics at fixed positive epsilon
and finite kappa. They do not determine its limiting content correlations or
identify any physical field or law. `python3 check.py > RUN.log` reproduces the
exact finite checks. `RESULTS.json` and `SEAL.json` record outputs and hashes.
No new primary calculation was read before sealing. The model is the already
checked one at commit `689941783bea870e08458e079ddb208257d0083d`, whose original
note hashes are `8cc06519d7f3acc088b1e450c151f0870ab21d2987ef2b0224d40ba6a5e7e4e2`
and `423eba32f704e510331bfbb6dba78ea0a35db129854547b155fd76f27248d917`.
All files created in this check are confined to the assigned independent
directory; no other file or Git state was changed.
