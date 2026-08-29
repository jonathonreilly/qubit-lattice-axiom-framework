# Preflight Witnesses

No Block18 target runner, cache, or target mutation has been executed. The
identities below are analytical design witnesses and falsifiers; the runner
must rederive them after the preregistration commit.

## Mark-kernel witness

Each of six neighbors is blank or carries one of six signed-axis Records, so
there are exactly

```text
7^6 = 117,649
```

ordered local profiles. For counts `m_f in {0,...,6}` with
`sum_f m_f<=6`, the integer weights `w_f=2^m_f` are positive and

```text
p_f = w_f/sum_g w_g
```

normalize exactly. In a blank neighborhood every mark has probability `1/6`.
With one neighboring `rho_f`, the probabilities are `2/7` for `f` and `1/7`
for each other direction. Rotating the profile permutes the six counts and
therefore the probabilities.

For `rho_f=(I-(143/256)f dot sigma)/2`, Hermiticity and unit trace are
immediate and the runner must derive, rather than merely quote, the two exact
eigenvalues `113/512` and `399/512`. Thus all six marks are valid positive
elements of the full one-site possibility domain. This does not make them the
only possibilities in `M_2(C)`.

This is a conditional mark witness only. The foundation does not supply its
extensional formula or any activation hazard.

## Hazard-separation witness

For a blank candidate with `n` recorded neighbors,

```text
lambda^(0)/alpha = 1,
lambda^(1)/alpha = 1+n/6,
```

so the second lies in `[1,2]`. On `Lambda_7`, take `x_6=0`, record its six
neighbors, and take `x_0=(3,3,3)` with six blank neighbors. Conditioning on the
next finite-volume jump lying at one of those two blank sites cancels every
mark probability and the common scale `alpha`, leaving `1/2` versus `2/3`.
The same local intensity ratio is the ratio of right derivatives at `t=0` in
infinite volume, which is a semigroup discriminator rather than a directly
operational clock-free probability.

For a Record-order statistic, put
`U={x_0,x_6} union N(x_0)` and let `tau_U` be the first new Record in `U`.
Before `tau_U`, the tested rate pair remains `(alpha,alpha)` or
`(alpha,2 alpha)`. Conditional on `tau_U<=T` and its site lying in the tested
pair, the common survival factor from every competing local clock cancels and
the winner odds are `1/2` or `2/3` for every `T>0`. This uses only local
Record order and invokes no global infinite-volume next event or absolute
clock calibration.

## Finite-process witness

On a finite torus, every off-diagonal intensity in (7) is nonnegative and the
diagonal is its negative row sum. Each accepted jump decreases the number of
blank sites by one. Therefore every path has at most `L^3` accepted jumps and
the all-recorded configurations are absorbing. The standard ordered-jump
density gives equation (8).

The runner must instantiate these facts symbolically and on exact finite
fixtures; it must not attempt to enumerate the full `7^(L^3)` state space.
Conditional on a specified `R_0`, equation (8) is a density relative to
counting measure on sites/marks and Lebesgue measure on the ordered time
simplex. Its sum/integral over `k=0,...,#blanks(R_0)` is one. Histories that
name a site occupied in `R_0`, repeat a site, request an illegal mark/site or
recursively incompatible transition, or fail strict time ordering have
density zero. Random initial configurations are mixed against their initial
law.

## Infinite-process witness

Fix `0<alpha<infinity` and an arbitrary deterministic initial configuration
in the seven-state witness sector or a Borel law `mu` on that restricted
product space, sampled independently of the graphical field. Both hazards are
dominated by one shared independent rate-`2 alpha` proposal field. Each
proposal carries an independent
uniform acceptance key `U` and six independent unit-rate exponential keys
`E_f`; acceptance is `U<=lambda_x/(2 alpha)` and the mark is the minimizer of
`E_f/2^(m_f)`. A
backward query at one proposal can add the queried site and six nearest
neighbors. Counting at most seven choices at each of `k` ordered proposal
times gives the safe exponential-tail majorant

```text
|A| sum_(k>=m) (14 alpha T)^k/k!.
```

The factorial makes the tail vanish. Radius is nearest-neighbor graph distance,
equivalently cubic `L^1` distance. Bounded ancestor radius plus the finite
number of Poisson points in the resulting finite spacetime box gives the
measurable local construction at rational queries and its local cadlag
extension. The runner must make those steps explicit and verify shared-field
fixed-exterior/periodic convergence when the finite backward clan avoids the
boundary. Under a space-group relabeling, it must prove sample-map
equivariance almost surely and `g_*Law_mu=Law_(g_*mu)`; invariance is available
only for invariant `mu`. It may not substitute exact projective consistency
of finite-volume chains or infer a global jump process from finite-volume
nonexplosion.

Since every blank hazard is at least `alpha`, proposals with uniform key at
most `1/2` give a rate-`alpha` baseline. Therefore a fixed site remains blank
at time `t` with probability at most `exp(-alpha t)`. Every initially blank
site eventually records almost surely, including on one probability-one event
for all countably many sites, but there is no common finite completion time.

## Seed-arity witness

Starting with the three named sites blank, define the cylinder event that all
three carry the specified `rho_f` at time `t`, regardless of outside Records.
A uniform bound on the total one-site rates at those targets and one-site
event arity imply that three accepted target-site jumps are required, so there
is no constant, linear, or quadratic term. A declared compound jump with
finite `kappa_c(R)>0` has a nonzero linear coefficient `kappa_c(R)/6` only
when it is the sole direct transition into the cylinder and the local
generator gives an `O(t^2)` remainder. In general the linear coefficient is
the sum of every direct intensity into the cylinder. The short-time orders
separate event arity without identifying the cylinder with the complete
Block16 output state.

## Lumpability witness

Use `Lambda_L` with `L>=6`, and require the five neighbors of `y=c+2f` other
than `c+f` to be blank in both full states. The single seed `S_(c,f)` then
leaves `y` with no recorded neighbor, so `p_y(f)=1/6` and both hazards equal
`alpha`. The Block16 Record projection `C_(c,f)` gives `y` exactly one
neighboring `rho_f`, so `p_y(f)=2/7`, while
`lambda_y^(1)=7 alpha/6`. Hence

```text
q0(S,y:f)=alpha/6,   q0(C,y:f)=2 alpha/7,
q1(S,y:f)=alpha/6,   q1(C,y:f)=alpha/3.
```

Any quotient identifying the two full states while retaining this append as a
common distinguishable coarse future cell fails strong lumpability under the
witness processes. A constant projection remains trivially lumpable. This
does not rule out a different process, a coarser quotient, an explicit
compound event, or other transitions mapped into the target cell.

The runner must reproduce the wraparound falsifiers: at `L=3` the displayed
three-site seed collapses to two sites and has only `O(t^2)` one-site arity;
at `L=4` `y` is already recorded; and
at `L=5` two seed sites neighbor `y`, giving `p_y(f)=4/9`,
`q0=4 alpha/9`, and `q1=16 alpha/27`.

## Current/source witness

The oriented incidence matrix of a connected periodic graph has image equal
to the zero-sum vertex vectors and rank `L^3-1`. Every edge-current divergence
therefore sums to zero. A one-Record append changes raw occupancy by a vector
of total one; a Block16 compound append at three distinct sites changes it by
total three. Neither is a source-free divergence.

Adding an explicit source `sigma=e_x`, a reservoir debit `-1`, open-boundary
flux, a neutral paired event, signed content, or a worldline transition evades
the boundary. A three-Record compound birth at distinct sites has source total
`3` and requires debit `-3`. A scalar debit proves global balance, not a local
current, unless a reservoir incidence is supplied. The runner must prove the
connected-graph incidence image/rank over real currents for every `L>=3`;
`L=3,4,5` are regressions only. This boundary applies only to a join that
identifies raw cumulative Record occupancy with the conserved density.

## Principal risks frozen before execution

1. The Markov/exponential-clock ansatz is downstream process structure, not an
   axiom consequence.
2. Homogeneous infinite-volume nucleation has infinite global rate; only local
   graphical cylinders are meaningful.
3. One witness mark law cannot be renamed the framework's unique
   Admissibility law.
4. Two absolute rates differing only by a constant do not prove physical
   underselection.
5. Finite-volume existence does not prove the infinite process.
6. A single Record and the Block16 three-Record atom are different process
   states unless exact lumpability or an explicit event law says otherwise.
7. Raw cumulative Record count is not automatically a conserved gravitational
   source.
8. Underselection does not automatically establish that a fifth axiom is
   necessary.
9. Pure-Record closure, readable blank/Record status, atomic jumps, the
   Markov proposal law, and the six-mark support are downstream model inputs.
10. Covariance of the transition kernel does not make a noninvariant initial
    law invariant.
11. The sector-scoped model is not an executed full-`M_2(C)` occurrence law;
    a common full-domain extension remains a live technical completion.

## Hard falsifiers

- a subnormalized `p` or a hidden no-event mark;
- a noncovariant hazard, rate above `2 alpha`, or range beyond one;
- a zero-on-blank hazard that fails Record formation;
- an external next-site scheduler;
- a global holding-time claim on the infinite blank lattice;
- a failed ancestor/coupling proof advertised as an infinite process;
- an asymmetric point-mass initial law advertised as invariant;
- a fixed-label/tied-key rule advertised as covariant;
- two generators separated only by one constant factor;
- `O(t)` three-Record creation from bounded one-site jumps;
- use of the nominal lumpability fixture at `L=3,4,5`;
- a failed lumpability row called a quotient or a compensating transition
  hidden in its target cell;
- an invalid, repeated, initially occupied, or nonordered history assigned
  positive density;
- source-free conservation of positive Record-count births on a torus; or
- any axiom/TOE change inferred from one selected witness.
