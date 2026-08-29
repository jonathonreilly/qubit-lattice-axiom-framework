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

This is a conditional mark witness only. The foundation does not supply its
extensional formula or any activation hazard.

## Hazard-separation witness

For a blank candidate with `n` recorded neighbors,

```text
lambda^(0)/a = 1,
lambda^(1)/a = 1+n/6,
```

so the second lies in `[1,2]`. On `Lambda_7`, take `x_6=0`, record its six
neighbors, and take `x_0=(3,3,3)` with six blank neighbors. Conditioning on the
next finite-volume jump lying at one of those two blank sites cancels every
mark probability and the common scale `a`, leaving `1/2` versus `2/3`. The
same local intensity ratio is the ratio of right derivatives at `t=0` in
infinite volume. This is not a global clock-rescaling comparison and does not
invoke a global infinite-volume next event.

## Finite-process witness

On a finite torus, every off-diagonal intensity in (7) is nonnegative and the
diagonal is its negative row sum. Each accepted jump decreases the number of
blank sites by one. Therefore every path has at most `L^3` accepted jumps and
the all-recorded configurations are absorbing. The standard ordered-jump
density gives equation (8).

The runner must instantiate these facts symbolically and on exact finite
fixtures; it must not attempt to enumerate the full `7^(L^3)` state space.
Histories that revisit an already recorded site, request an incompatible
state/mark transition, or fail strict time ordering have density zero.

## Infinite-process witness

Fix `0<a<infinity` and an arbitrary deterministic initial configuration or
initial product-space law. Both hazards are dominated by one shared
independent rate-`2a` proposal field. Each proposal carries an independent
uniform acceptance key `U` and six independent unit-rate exponential keys
`E_f`; acceptance is `U<=lambda_x/(2a)` and the mark is the minimizer of
`E_f/2^(m_f)`. A
backward query at one proposal can add the queried site and six nearest
neighbors. Counting at most seven choices at each of `k` ordered proposal
times gives the safe exponential-tail majorant

```text
|A| sum_(k>=m) (14aT)^k/k!.
```

The factorial makes the tail vanish. Radius is nearest-neighbor graph distance,
equivalently cubic `L^1` distance. Bounded ancestor radius plus the finite
number of Poisson points in the resulting finite spacetime box gives the
pathwise construction. The runner must make that final step explicit and
verify shared-field fixed-exterior/periodic convergence on local cylinders.
It may not substitute exact projective consistency of finite-volume chains or
infer an infinite process from finite nonexplosion alone.

## Seed-arity witness

Starting with the three named sites blank, define the cylinder event that all
three carry the specified `rho_f` at time `t`, regardless of outside Records.
A uniformly bounded one-site append generator needs three accepted target-site
jumps, so there is no constant, linear, or quadratic term. A declared compound
jump with finite `kappa_c(R)>0` has a nonzero linear coefficient. The
short-time orders therefore separate event arity without identifying the
three-site cylinder with the complete Block16 output state.

## Lumpability witness

At `y=c+2f`, the single seed `S_(c,f)` leaves `y` with no recorded neighbor,
so `p_y(f)=1/6` and both hazards equal `a`. The Block16 Record projection
`C_(c,f)` gives `y` one neighboring `rho_f`, so `p_y(f)=2/7`, while
`lambda_y^(1)=7a/6`. Hence

```text
q0(S,y:f)=a/6,   q0(C,y:f)=2a/7,
q1(S,y:f)=a/6,   q1(C,y:f)=a/3.
```

Any quotient identifying the two full states while retaining this append as a
common distinguishable coarse future cell fails strong lumpability under the
witness processes. A constant projection remains trivially lumpable. This
does not rule out a different process, a coarser quotient, or an explicit
compound event.

## Current/source witness

The oriented incidence matrix of a connected periodic graph has image equal
to the zero-sum vertex vectors and rank `L^3-1`. Every edge-current divergence
therefore sums to zero. A one-Record append changes raw occupancy by a vector
of total one; a Block16 compound append changes it by total three. Neither is
a source-free divergence.

Adding an explicit source `sigma=e_x`, a reservoir debit `-1`, open-boundary
flux, a neutral paired event, signed content, or a worldline transition evades
the boundary. A three-Record compound birth has source total `3` and requires
debit `-3`. The runner must prove the connected-graph incidence rank for every
`L>=3`; `L=3,4,5` are regressions only.

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

## Hard falsifiers

- a subnormalized `p` or a hidden no-event mark;
- a noncovariant or unbounded hazard;
- an external next-site scheduler;
- a global holding-time claim on the infinite blank lattice;
- a failed ancestor/coupling proof advertised as an infinite process;
- two generators separated only by one constant factor;
- `O(t)` three-Record creation from bounded one-site jumps;
- a failed lumpability row called a quotient;
- source-free conservation of positive Record-count births on a torus; or
- any axiom/TOE change inferred from one selected witness.
