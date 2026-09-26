# Primary derivation: a permanent formation clock and lifetime activity

2026-09-21. The primary author derived the following argument before reading
the separately commissioned local-activity calculation. This is a working
conditional theorem, not an axiom consequence, a physical lifetime prediction,
or a no-go statement about the TOE. The stochastic clock has been supplied.

## Domain and process construction

Use Z^d, z=2d, or a finite translation-invariant nearest-neighbor torus with
the same degree. A site is vacant or holds one of six immutable contents.
For each undirected edge, a rate-kappa proposal exchanges an occupied endpoint
with its vacant endpoint with the previously specified heatbath acceptance.
At a vacant site x, content a forms at rate

```
epsilon U_xa(s),   U_xa(s)=product_(occupied y~x) W_(a,s_y).
```

Here epsilon>0 and 0<=kappa<infinity are fixed. W is finite, strictly positive
and symmetric. Row normalization is unnecessary in this argument. The
initial law is translation invariant; it need not be independent, ergodic,
or invariant under reflection. Let v0 be its vacancy density. There are no
deletions, exits, occupied-occupied swaps, site creation, or other state
changes. All these restrictions describe this process, not every possible
reading of permanent records.

Put ell=min(1,min W), u=max(1,max W),
alpha=6 epsilon ell^z and beta=6 epsilon u^z. Conditional on vacancy the
total birth rate lies between alpha and beta, uniformly over configurations.

For an explicit infinite-volume construction place a rate-beta marked
Poisson process at each site: choose one of six contents uniformly, and a
uniform acceptance mark; insert it if vacant and the mark is at most
U_xa/u^z. Put independent rate-kappa marked proposals on undirected edges.
At a proposal, the heatbath ratio needs only the two endpoints and their
neighbors. These marked maps produce exactly the rates above.

To determine a finite set of sites at a finite time, explore the marks
backward. Only maps updating a currently needed site matter. Each needed
site sees at most beta+z kappa proposal rate and each encountered map adds
at most 2(z+1) dependency sites. This exploration is bounded by a branching
process with bounded offspring and rate proportional to its current size;
its expected size is bounded exponentially on each finite time interval,
so it has no finite-time explosion. Thus only finitely many marks and initial
sites are needed almost surely. Finite explorations are consistent and give
the infinite process, local finite-volume limits, and translation covariance.
The initial configuration can be sampled first independently of these clocks.
This is the usual graphical construction, spelled out here rather than
assuming a first event exists on the entire infinite lattice.

## Vacancy budget

Let v(t)=P(site 0 is vacant). For the bounded local vacancy observable, the
generator identity is justified by the construction and bounded update rate.
Translation invariance cancels the expected total incoming and outgoing hop
flux: the mean rate from y to 0 equals that from 0 to -y, after translation.
Reflection symmetry of the distribution or the individual current is not
needed. If r_0(s) is the total birth rate at 0, including its vacancy
indicator, then

```
v'(t)=-E[r_0(s_t)],
alpha v(t)<=E[r_0(s_t)]<=beta v(t),
v0 exp(-beta t)<=v(t)<=v0 exp(-alpha t).
```

The expected number of births at one fixed site after T is exactly

```
E[B_0(T,infinity)]=integral_T^infinity E[r_0(s_t)]dt=v(T).
```

In particular E[B_0(0,infinity)]=v0. From an empty initial law the expected
total births at a site is one. This is an ensemble identity: particular
sites can form several records, and some sites receive their final record
without forming one themselves. It does not prohibit the user's proposed
site reuse.

## Every site eventually stops changing

An accepted hop on {0,y} requires a vacancy at one endpoint, and its rate is
at most kappa. Hence the mean rate of accepted hop updates at site 0 is at
most 2 kappa z v(t). Let J_0 count all actual births and accepted hop updates.
Then

```
E[J_0(T,infinity)] <= v0 (1+2 kappa z/alpha) exp(-alpha T),
P(any actual update at site 0 after T)
                  <= v0 (1+2 kappa z/alpha) exp(-alpha T).
```

The expectation is finite at T=0, so the integer count is finite almost
surely. Each site therefore eventually has a constant state. Since v(t)
tends to zero, bounded convergence shows that constant state is occupied
almost surely. The lattice is countable, so all sites have this property
simultaneously almost surely. This is local fixation, not a common finite
time at which the entire infinite lattice fills or stops updating.

## Every record makes finitely many hops

Local fixation alone would not prove this: a particle could visit infinitely
many different sites only once each. The missing step uses translation
invariance again, through a nonnegative transport identity.

Give each initial record its initial site as origin and each subsequently
formed record its birth site as origin. These are bookkeeping labels carried
with the unchanged record; they add no state variable to the transition law.
Distinguish multiple births at the same site by their distinct birth times.
For every accepted hop, send one unit of abstract mass from that record's
origin to its departure site. Let T(x,y) be the total mass sent from x to y
over all times. This is a nonnegative translation-covariant random array,
possibly infinite before the following bound is applied. Tonelli and a
change of index give

```
E[sum_y T(0,y)] = sum_y E[T(0,y)]
                = sum_y E[T(-y,0)] = E[sum_y T(y,0)].
```

The last quantity is the expected total accepted departures from site 0.
A departure to a neighboring site y requires y vacant, so its mean rate is
at most kappa z v(t). Therefore

```
E[total lifetime hops of all records whose origin is 0]
            <= kappa z v0/alpha < infinity.
```

There are finitely many records of origin 0 almost surely, since its initial
record count is at most one and its expected birth count is v0. More strongly,
the displayed finite expectation already makes the aggregate hop count
finite almost surely. Countability of possible origins implies that every
initial or formed record makes finitely many hops almost surely. For a record
that exists its finitely many hop times are finite, so it eventually remains
at a final site. This conclusion is for the translation-invariant ensemble,
not a uniform lifetime estimate for every conditionally specified rare tag.

## Checks, surviving routes, and what the result does not decide

* W=1: alpha=beta=6 epsilon and v(t)=v0 exp(-6 epsilon t) exactly.
  For an initial homogeneous product law, the exact product evolution gives
  expected births v0 and expected departures
  `(kappa z/(12 epsilon))*(v0-v0^2/2)` per site. The factor one half is the
  heatbath acceptance; the occupation-vacancy probability is v(t)(1-v(t)).
  This sharper control obeys the general bound.
* kappa=0: every initial vacancy has exactly one eventual birth at its own
  site. Occupied sites never change. The birth budget is still v0.
* epsilon=0 violates the strict formation-clock premise. Uniform W with a
  nondegenerate stationary exclusion product law need not fixate. This
  argument supplies no claim for that process.
* Zero weights, vanishing or time-dependent formation intensity, additions
  of sites, exports or removals can destroy the positive-hazard argument.
  They require their own analysis and are not ruled out here.
* Occupied-occupied exchanges, coherent amplitude propagation, internal
  record dynamics, and persistent directional carriers are not the two
  update types above. Filling does not freeze an independently supplied
  dynamical layer. Fixed finite-time active regimes are also compatible.
* Translation invariance is used twice. The statement is not extended to
  arbitrary spatially inhomogeneous initial conditions by assertion.
* A homogeneous positive-density stationary law with vacancies cannot exist
  for these rates: stationarity would give E[r_0]=0 while r_0>=alpha 1_vacant.
  Stationary laws supported on fully occupied configurations do exist, with
  arbitrary content correlations. A frozen correlated final state is not
  the same as continued local record motion or formation.

Thus site reuse creates a finite transient record-production history at each
site under this clock, even with an infinite reservoir of other sites. A
physical model requiring indefinitely continuing local record activity needs
an additional mechanism or a different formation clock. The axiom memo does
not select this clock, its rate, or a physical time conversion; consequently
this is a discriminator among supplied mechanisms, not a failure of the
framework or a prediction of the universe's future.

The separate pre-source check sealed at 2026-09-21 01:00:18 UTC. Its report
SHA-256 is `7b4bad382af9d326a7de018db2bc8acd272fd960e16ac5c1a8cd4dba853e4ca4`;
checker SHA-256 is `b6e6e6e6748cad03d0de814c391bf081ba6e3d39ca4371d5b9154aa2a2f8c0c6`.
Its full report and code have now been read. It agrees with the graphical
construction, density and event bounds, and separate tagged-record proof.
Its 3,087 exact finite-generator cases, fourteen correlated translation-orbit
laws, and three absorption solves are preserved under
`independent_local_activity/`. They test the rate identities and conventions;
the infinite-time conclusions follow from the arguments, not a finite run.

The independent check also gives an exact repeated-birth example. On two sites
with one bond, uniform W, and an empty start, the probability of two births
at a specified site is kappa/[4(6 epsilon+kappa)]. The first record's lifetime
hop count is geometric with continuation probability kappa/(12 epsilon+kappa)
and mean kappa/(12 epsilon). To reconstruct this: before the second birth,
the first record alternates sites at rate kappa/2 while the remaining vacancy
forms at rate 6 epsilon; summing the odd-parity geometric series and the
one-half probability that the first birth was at the specified site gives
the repeated-birth probability. This demonstrates site reuse and unbounded
possible hop counts while their expectations are finite.

## A clock-independent birth budget (primary extension)

The mass-balance part has a broader implication than the positive-hazard
fixation theorem. Keep one-site capacity, permanent records, conservative
bounded local motion, and spatial translation invariance, but allow ANY
nonnegative locally bounded insertion rate, possibly varying with time.
There are still no removals, exits or site additions. Expected hop divergence
still cancels, so v(t) is nonincreasing and

```
E[B_0(0,infinity)]=v0-lim_(t->infinity) v(t)<=v0.
```

Thus the total number of births at every fixed site is finite almost surely
even without a uniform lower bound on formation. This does not make lifetime
hop counts finite: positive lower hazard was used to make the vacancy-time
integral finite, and motion may persist when vacancies remain. The argument
does not use reversibility, the heatbath acceptance formula, or the record
content menu. It is a capacity and spatial mass-balance statement. It also
does not set a common deterministic bound on births at a site. This broader
extension has a primary proof here; the sealed independent scope concerned
fixed positive formation rates, so its receipt must not be relabeled as a
check of every time-dependent clock.

## Uniform vacancy control beyond translation invariance

The independently sealed terminal-correlation report (2026-09-21 01:38:35 UTC,
SHA-256 `6249af1ec44d27467c3378641c225cadadda6fd4f9a794560dbf6a6991bf106e`)
adds a vacancy-label estimate. Its full report and code have been read, and
the following argument is reconstructed here. This removes translation
invariance from local fixation, without importing the homogeneous birth budget.

Label each initial vacancy by its initial position a. Vacancy labels move
opposite to record hops and are killed by births. No new vacancy label is
created. Let S_a(t) indicate survival and K_a(t) count its hops. Its killing
rate is at least alpha, and its hop rate is at most lambda=z kappa. Thus

```
E[S_a(t) exp(delta K_a(t))]
 <= P(a initially vacant) exp[(-alpha+lambda(exp(delta)-1))t].
```

This is a bounded-intensity exponential compensator estimate, not an
assumption that survival and position are independent. Stop K_a first and
use its Poisson exponential-moment domination to remove the stopping.
If the label is at x, it made at least dist(a,x) hops. Summing the bound
over initial labels, taking exp(delta)=1+alpha/(2 lambda) for lambda>0,
and bounding every initial vacancy probability by v_* gives

```
P(x vacant at t) <= v_* A exp(-gamma t),
A=(1+4 lambda/alpha)^d,             gamma=alpha/2.
```

The lattice sum is exactly the product of d geometric sums. For lambda=0
the direct bound v_* exp(-alpha t) is stronger and implies this formula.
The same upper bound works on tori by selecting minimal displacement vectors.
It holds for arbitrary initial laws, including correlated and spatially
inhomogeneous ones. Integrating the local event-rate upper bound
(beta+2 lambda) sup_x P(x vacant at t) proves local occupied fixation and
the uniform late-update estimate

```
E[J_x(T,infinity)] <= (beta+2 lambda) v_* A exp(-gamma T)/gamma.
```

The earlier homogeneous estimates remain sharper and identify the exact
per-site mean birth budget. The new estimate alone does not do that.

## Tagged records from arbitrary initial states (primary extension)

The uniform vacancy estimate also suggests a direct route around the
translation-invariance premise in the original tagged-record proof. The
argument below is new primary work after reading that estimate; the earlier
independent receipt does not certify this tagged extension.

Consider an initial tagged record at x0 in an arbitrary initial configuration,
or start the time origin immediately after a specified birth. Set v_*=1
in the universal vacancy bound. The tag's hop count N_t has intensity at
most lambda, regardless of its environment. Therefore

```
E[exp(N_t)] <= exp(lambda(e-1)t).
```

Let c=lambda(e-1)+gamma, in lattice steps per unit abstract time. Then
P(N_t>ct)<=exp(-gamma t). On the complementary event the tag lies within
distance ct of x0. Its hop requires a nearby vacancy, so summing the universal
vacancy bound over that ball, without any independence assumption between
the tag and vacancies, bounds its expected instantaneous hop intensity by

```
lambda [1+A(2ct+3)^d] exp(-gamma t).
```

The first term covers the event that the tag has traveled faster than ct;
the second covers all possible nearby vacant destinations in the remaining
ball. The bound is integrable, hence

```
E[N_infinity] <= lambda/gamma
 +lambda A sum_(k=0)^d binom(d,k) 3^(d-k) (2c)^k k!/gamma^(k+1).
```

In particular every specified record has finitely many lifetime hops almost
surely, uniformly over its starting configuration. The case lambda=0 is
trivial. For a later-born record, the strong Markov property of the marked
construction applies at its birth time, with the same bound independent of
the configuration then. Enumerate the initial sites and the countably many
births by site and local birth index. Countability gives the simultaneous
conclusion for every record, without a spatially homogeneous ensemble.

There is also an exponential tail with a polynomial prefactor. For integer
m>=1 and lambda>0 put T=m/(2e lambda). Poisson domination gives
P(N_T>=m)<=2^(-m). If the lifetime count exceeds m while this event fails,
there is at least one later hop. Thus

```
P(N_infinity>=m)
 <= 2^(-m)+lambda integral_T^infinity [1+A(2ct+3)^d]exp(-gamma t) dt.
```

The second term is an explicit polynomial in T times exp(-gamma T).
It bounds the total traveled path length as well as the maximal displacement.
These constants are very loose and diverge when the positive hazard floor
is lost. This is a proposed extension for the fixed positive-clock model,
not a physical travel-distance prediction. Its compensator, stopping-time,
and tag/vacancy union-bound steps require selective independent scrutiny
before a formal claim includes it.
