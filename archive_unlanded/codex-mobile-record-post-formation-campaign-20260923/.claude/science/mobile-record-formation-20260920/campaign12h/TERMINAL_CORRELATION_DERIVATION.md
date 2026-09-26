# Primary derivation: terminal connected correlations at fixed positive rates

2026-09-21. Personally derived before the new separate terminal-correlation
check. This follows the local-activity proof but adds a distinct spatial
dependence argument. Working conditional result; do not treat it as checked
until the latter has been independently scrutinized.

## Domain

Use the supplied nearest-neighbor birth/vacancy-hop model on Z^d or a cubic
torus. The initial law is spatially independent and identically distributed,
including the completely empty deterministic initial configuration. This
additional independence premise was not needed for local fixation. The
initial contents may have any common distribution; a nonzero one-site mean
is allowed. Connected correlations, rather than raw moments, are bounded.
All future proposal clocks and marks are independent of the initial law.

With z=2d, ell=min(1,min W), u=max(1,max W), put

```
alpha=6 epsilon ell^z>0,
beta=6 epsilon u^z,
Q=beta+z kappa,
K=2(z+1),
A0=v0(1+2 z kappa/alpha).
```

The locally fixed final configuration s_infinity exists by the earlier proof.
For every site x,
P(any actual update of x after T)<=A0 exp(-alpha T).
This bound by itself contains no spatial decorrelation assertion: a process
with an initially shared random bit could fix while retaining that bit at
every site. Independence of the initial state and finite propagation of
clock dependence are both needed next.

## Finite-time dependence radius

Use the same dominating marked graphical process: site clocks of total rate
beta and edge clocks of rate kappa. Birth maps inspect radius one. Hop maps
inspect the endpoints and their neighbors, so all new dependencies lie
within graph distance two of either updated site that is currently queried.

Trace one queried site's state at time T backward. A dependency path records
a sequence of local clock marks at strictly decreasing times and one selected
ancestor site at each mark. The sum of relevant clock rates for a selected
site is at most Q, and each mark has at most K choices of ancestor. Thus the
expected number of length-n dependency paths is at most

```
(K Q T)^n/n!.
```

This is a first-moment count of time-ordered marked paths. It does not assume
different paths are independent. Repeated use of one clock process uses its
Poisson factorial moments at distinct ordered times, giving the same bound.
Every step changes position by at most two. If the backward dependence set
exits the graph ball B_R(x), it contains a path of at least ceil(R/2) steps.
Counting its prefix of length n=ceil(R/2) and using
a^n/n!<=exp(e a-n) gives the conservative estimate

```
P(dependence of s_x(T) exits B_R(x))
       <= min{1, exp(e K Q T-ceil(R/2))}.
```

Couple the full evolution to one with all outside states fixed and only the
clocks touching B_R(x) retained. On the event of no exiting dependency path,
both values at x agree. The truncated value depends only on the initial
states in B_R(x), site clocks there and incident edge clocks, with a fixed
deterministic boundary. Balls at mutual graph distance greater than one use
disjoint such random inputs, and their truncated values are independent.
The construction remains local when a periodic torus is used and graph
distance means its periodic shortest distance.

## Terminal connected covariance

Let f and g be possibly complex single-site functions with absolute values
at most one. For sites x,y at graph distance D>=6, choose

```
R=floor(D/3)>=2,    T=R/(4 e K Q).
```

Their radius-R balls are separated by more than one, so the two truncated
time-T observables are independent. The probability that the final state at
either site differs from its respective truncated value is at most

```
p_R=A0 exp[-alpha R/(4 e K Q)]+exp(-R/4).
```

The first term is a late-update tail. The second follows from the dependence
bound, because e K Q T=R/4 and ceil(R/2)>=R/2. For bounded functions, changing
the state on an event of probability p changes its L1 norm by at most 2p.
Comparing both the joint moment and the product of means with the independent
truncated observables therefore gives

```
|Cov(f(s_x(infinity)), g(s_y(infinity)))| <= 8 p_R.
```

For complex observables the second variable may be conjugated with the same
bound. The trivial bound 2 can be substituted whenever it is tighter.
All constants are independent of volume, with rates, degree and W held fixed.
No stationarity, equilibrium representation or content-sector mixing is used.

This proves an exponentially decaying connected-correlation bound at the
locally fixed endpoint for the stated product initial condition. The length
estimate is very loose: its rate-controlled part scales like KQ/alpha, not a
claimed sharp diffusion length. When epsilon decreases or some W entries
approach zero the bound can become arbitrarily weak. It must not be used to
justify exchanging those limits with distance or volume.

## Consequences at the measured resolution

On the infinite lattice the sum over y of the absolute covariance is finite,
because a polynomial number of lattice sites lies at each graph radius and
the bound decays exponentially. The same sum has a uniform finite bound on
the torus family. Hence the variance per volume of a sum of bounded,
centered single-site observables is bounded uniformly in volume.

For the symmetric six-axis menus and the empty initial state, content
symmetry gives E[v(s_x(infinity))]=0. Summing the three coordinate bounds then
bounds E[|sum_x v(s_x(infinity))|^2]/V uniformly over tori. The argument rules
out an extensive zero-mode variance or an algebraic connected two-point tail
at fixed strictly positive rates and weights in this particular terminal
ensemble. It does not claim a numerical small bound on the structure factors
observed in modest finite volumes.

The theorem concerns bounded local content observables. It does not classify
nonlocal decoders, gauge-dependent fields, extended carriers, or every notion
of order. An explicit initial mean is not forbidden: centering removes its
disconnected contribution. Nor is an initially correlated ensemble covered
by the product-law proof. The theorem permits large finite correlations and
transient structure formation, and is consistent with different limiting
ensembles when formation vanishes before the volume or time limit.

## Stress tests and surviving alternatives

* The proof is not “local fixation implies clustering.” Its second premise
  is independent spatial input, and the marked path estimate is essential.
  A fully occupied initial state whose contents are all the same shared
  random orientation is a fixed correlated counterexample outside that premise.
* A time-dependent clock without exponential late-update control is outside
  this bound even if local fixation still holds by another argument.
* Zero pair weights, unbounded speeds, extra persistent field variables,
  occupied-occupied exchanges, record deletion or source/exit reservoirs
  require different activity or dependence estimates.
* Small positive epsilon and W_min can create enormous bounds. No physical
  exclusion follows without a physical rate and lattice-scale identification.
* Static critical Gibbs measures are not substituted for this growing process.
  If a different limit realizes one, the limiting procedure must be stated.

The useful campaign implication is a precise question: which admissible
mechanism could keep the correlation scale growing once these vacancy-only,
positive-clock dynamics would freeze? It is not a conclusion that permanent
records or the broader framework cannot support quantum fields or gravity.

The separate calculation is now sealed under `independent_terminal_correlations/`
at 2026-09-21 01:38:35 UTC. Report SHA-256:
`6249af1ec44d27467c3378641c225cadadda6fd4f9a794560dbf6a6991bf106e`;
checker SHA-256:
`c817b2703f03f27d638fc26ea9f4e0ec3118c33191dc60ec909268e5ad510fcf`.
The full report and code were read. Its independently chosen ball truncation
deletes crossing edges and yields a slightly sharper bound with
Lambda=(z+1)(beta+2z kappa), radius floor((D-1)/2), and depth ceil(D/4).
It also obtains a uniform fixation tail for arbitrary initial laws by a
vacancy-label exponential-moment estimate; therefore its clustering result
covers product initial laws with unequal site marginals. That extension is
reconstructed in `LOCAL_ACTIVITY_DERIVATION.md` with its provenance explicit.
Five exact absorption calculations and 1,519 vacancy-label drift inequalities
check controls and constants. Finite calculations do not certify the
asymptotic distance statement; the displayed arguments do that. No full
publication-source review or independent audit has occurred for this unit.
