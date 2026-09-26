# Does relay propagation evade the lifetime activity bounds?

Primary extension, 2026-09-21; separate pre-source check completed below. This question is
stronger than tagged-record fixation. Even if every carrier stops, its
influence could in principle be relayed to later records. We therefore test
an initially finite change under the actual coupled stochastic dynamics.

## Model and coupling

Use the fixed positive insertion and vacancy-only heatbath hopping model of
`LOCAL_ACTIVITY_DERIVATION.md`, on Z^d. Set z=2d,
alpha=6 epsilon min(1,min W)^z>0, beta=6 epsilon max(1,max W)^z,
lambda=z kappa, gamma=alpha/2 and A=(1+4lambda/alpha)^d.
The conservative weaker choice gamma=alpha/2 is also valid when kappa=0.
For arbitrary initial configurations the already checked vacancy-label
argument gives a uniform late-update estimate at each site:

E[J_x(T,infinity)]<=C exp(-gamma T),
C=(beta+2lambda)A/gamma.

Start two copies in configurations that agree outside a fixed finite set K.
The initial pair may be random and spatially correlated, but is independent
of future clocks. Use identical marked site and edge clocks, the same birth
content choices and the same acceptance uniforms in both copies. State-dependent
acceptances may differ, so this is a basic graphical coupling, not an
assumption that the records follow the same paths.

Let D_x be the event that the copies ever differ at x at any time t>=0.
It concerns content/vacancy observables; use consistent event identifiers if
record tags themselves are added to the observable. The finite perturbation
need not disappear or make the two final patterns identical.

## Forward dependence cone

A local disagreement can affect a later update only when it is in that map's
input footprint. A birth map has one output and reads its center and z
neighbors. For a given input site, at most z+1 birth clocks can use it, each
with rate beta. A hop reads the union of the two endpoint neighborhoods and
updates two endpoints. At most z(z+1) edge clocks have the input site in
that footprint, each at rate kappa with two possible descendant outputs.
Every such dependence step has graph length at most two. Thus the total
weighted rate of possible forward descendant steps per site is at most

Lambda=(z+1)(beta+2z kappa).

This counts potential dependence, including rejected clocks and duplicated
paths; it does not assert independence between paths. For a fixed path of
m clock steps, the ordered-time simplex has measure T^m/m!. Summing paths
from K bounds the expected number of chronological prefixes of length m by

|K|(Lambda T)^m/m!.

If a discrepancy reaches graph distance D from K by time T, it must have a
prefix of m=ceil(D/2) such steps. The same bound therefore controls the
probability of any such early influence. Repeated occurrences of one Poisson
clock are covered by its factorial moment measure at distinct event times.
Bounded local rates exclude finite-time explosion.

## All-time influence bound

For x outside K, split according to whether its first discrepancy is before
or after T. The early part is bounded by the forward-path count. If the
first discrepancy is later, at least one of the copies must update x after T.
The two late-update bounds therefore give

Pr(D_x) <= |K|(Lambda T)^m/m!+2C exp(-gamma T),
m=ceil(dist(x,K)/2).

Choose T=m/(2e Lambda). Since m!>=(m/e)^m and gamma<=Lambda,

Pr(D_x) <= min{1,(|K|+2C)exp[-gamma dist(x,K)/(4e Lambda)]}.

This controls an entire site trajectory, not only its terminal state. Put
c=gamma/(4e Lambda). Summing over Z^d, using
exp[-c dist(x,K)]<=sum_(y in K) exp[-c|x-y|_1], yields

E[number of sites ever affected]
 <= |K|(|K|+2C)[(1+exp(-c))/(1-exp(-c))]^d < infinity.

Consequently only finitely many sites are ever affected almost surely, and
the set of affected sites has finite random radius. Each such site undergoes
finitely many updates in either copy, so the coupled difference eventually
becomes a static finite pattern. Neither coalescence nor a deterministic
influence radius follows.

The same constants give volume-uniform bounds for simple periodic tori
(with all periods at least three), using graph distance and a shortest
coordinate representative. A finite change introduced at a stopping time
has the same restarted bound if the future clocks remain fresh. Continuous
external forcing or infinitely many interventions are different questions.

## What this establishes and what it does not

For this generator at fixed positive epsilon and weight floor, passing an
initial local difference to successive newborn records does not produce an
unbounded influence set. This closes a relay possibility left open by the
statement that each individual tag stops. A history statistic at a distant
site has total-variation response no larger than the displayed coupling
probability. The constants may be enormous and do not set a practical,
experimentally calibrated signal length.

This is not an exact finite coding-radius construction for the whole terminal
random field: it does not supply a finite stopping certificate that a local
output is immune to all changes in external clocks. It also does not constrain
a background initially containing long-range shared correlations, except for
the response to the specified finite alteration under common future clocks.

The positive floor, bounded finite-range rates, fixed site capacity and
vacancy-only moves matter. With epsilon=0 a single record in otherwise empty
Z has an indefinitely moving nearest-neighbor continuous-time random walk;
its difference from the all-vacant process visits unboundedly many sites.
Occupied exchanges, changing carriers, extra variables, context changes or
singular parameter limits are outside the fixed generator. No TOE exclusion
or prohibition on other physical signal mechanisms is claimed.

## Separate reconstruction and sharper shell bounds

The separate same-model checker sealed its derivation before reading this
source, at 2026-09-21 03:17:46 UTC. `independent_finite_influence/REPORT.md`
has SHA-256 `d3a8aa4163934492e5620c29242e749e59038ca553bdb4db1e6c449270c76678`.
The primary author read its complete argument and checker, verified all five
sealed evidence identities, and reconstructed the following additions. They
are credited to that separate calculation, not retroactively to this source.

A shell count improves the displayed quadratic dependence on |K| to linear.
Let k=|K|>=1, m_r=ceil(r/2), T_r=m_r/(2e Lambda),
eta=1/[1-1/(2e)], a=gamma/(4e Lambda), and s_d(r) the L1 shell size.
Distinct sites first affected before T_r require distinct ending paths of
length at least m_r. Their expected number is bounded by the full path tail

`k sum_(n>=m_r) (Lambda T_r)^n/n! <= k eta 2^(-m_r)`.

For sites first affected later, there are at most k s_d(r) sites in the shell
and the two late-update bounds apply. Thus, if D_r counts ever-affected sites
at distance r from K,

`E[D_r] <= k eta 2^(-ceil(r/2)) + 2C k s_d(r) exp(-a r)`.

With `G_d(b)=[(1+exp(-b))/(1-exp(-b))]^d`, summing gives

`E[#ever affected] <= k {1+2 eta+2C[G_d(a)-1]}`,

`Pr(radius>=R) <= min{1,k[4 eta+2C G_d(a/2)] exp(-a R/2)}`.

The latter uses the geometric path-tail bound and splits each spatial
exponential into two factors. These estimates are uniform for each allowed
initial-pair law, including spatially correlated laws independent of future
clocks. They do not assert one probability-one event simultaneous for an
uncountable class of backgrounds chosen after seeing those clocks. K empty
gives identical trajectories by pathwise uniqueness.

The checker also constructed a useful counterexample to a deterministic
radius. On Z with kappa=0 and W(a,b)=1+j v_a dot v_b, 0<j<1, let the copies
initially contain +e_1 versus -e_1 at zero and be vacant elsewhere. Fix n>=1.
In a guard interval {-1,0,...,n,n+1} during [0,T], require exactly the n
site proposals at 1,...,n in that order, no other guard proposals, and proposed
content +e_1 each time. Put U=1+j, beta=6 epsilon U^2. Shared acceptance
uniforms in ((1-j)/U^2,(1+j)/U^2) at site 1, and in
(1/U^2,(1+j)/U^2) subsequently, make the first copy accept and the other
reject at every step. The favorable event has exact positive probability

`2 (epsilon j T)^n exp[-(n+3) beta T]/n!`.

This follows by multiplying the ordered Poisson event probability, the
six-content mark probabilities and the uniform-interval lengths. No original
record moves: newborns relay the difference. Guard sites prevent influence
from outside events. The almost surely finite radius therefore has unbounded
support in this example; no deterministic cutoff follows from fixation.

The report also distinguishes last-update certificates from arbitrary coding
representations. For W=1, kappa>0 and empty start, at every finite time there
are almost surely vacancies somewhere: infinitely many separated sites have
had no site or incident-edge clock by any given integer time. At a finite
stopping time, a finite sequence of accepted hops along a shortest path from
an occupied queried site to its closest vacancy can bring that vacancy to
the queried site before births, with positive conditional probability.
A vacant queried site can also update later. Hence no finite stopping time
can certify that its last accepted update has occurred, even though that
last update is finite almost surely. This does not exclude every possible
finitary representation; at kappa=0 a site's accepted birth already is such
a terminal-content certificate. The distinction prevents a stronger coding
claim from being smuggled into the finite-response conclusion.

## Publication status

The all-time result now has a separate derivation, including forward footprint
enumeration, path-tail controls and six explicit newborn relays. It remains a
campaign result without a complete publication-source review or formal audit.
The original lifetime PR #8552 remains frozen; no influence extension was added
to that reviewed source. Preserve the distinctions between actual trajectory
response, a syntactic dependency cone and an exact finite coding certificate.
