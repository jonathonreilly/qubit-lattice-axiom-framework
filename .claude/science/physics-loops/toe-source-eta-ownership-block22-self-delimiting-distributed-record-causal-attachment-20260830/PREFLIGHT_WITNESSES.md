# Preflight witnesses

No Block22 target runner, cache, or target mutation has been created or
executed.  These desk witnesses must be independently rederived after the
preregistration commit.

## Exact POVM witness

Expanding Block09's trace-free tensor gives the Stage-A coefficients directly.
For a fixed effect, different-site Pauli terms commute.  The axis coefficient
norm sum is `1/36`, so its extreme eigenvalues are `1/12+-1/36`, namely
`1/18` and `1/9`.  Every corner has six coefficient vectors of norm
`sqrt(2)/256`; its extremes are `(8+-3 sqrt(2))/128`.

Axis linear terms cancel across the three duplicate-sign pairs.  Corner terms
cancel by sign parity.  The constants give `6/12+8/16=1`.  This witnesses a
strictly positive complete effect family on the whole 64-dimensional Hilbert
space, not merely product-state positivity.

## Why the first computational-pointer draft was rejected

The first draft used computational one-hot pointer bits.  Block09 covariance
rotates each live qubit's Bloch axes nontrivially, while a scalar computational
bit would need a trivial onsite action.  Since translated templates let one
primitive site play different roles, that is not one global representation.

Its translated locked-word guard could also overlap an arbitrary live qubit
and thereby change the nominally isolated POVM effect.  A large boundary
marker can repair that later guard only after a common pointer representation
exists; it does not fix the representation or Record/live typing.  The
rejected draft never executed and carries no result.

## Radial-code witness

At every pointer site the logical basis is the pair of antipodal pure states
along the site's relative radius.  The Bloch-sphere identity

```text
u_g (I+-n_r dot sigma) u_g^dagger
  = I+-n_(g r) dot sigma
```

proves projector covariance under the same onsite spin action used by the
live effects.  Antipodal projectors at a fixed site multiply to zero.  Product
words that differ in status, front, or outcome are therefore orthogonal.

The relative radii `1,2,3,4` and the radius-two corners are disjoint geometric
orbits.  Rotations permute each set and carry its radial basis with it.  Thus
the complete code, not merely the label list, has a common-action covariance
witness.

The equality `P_0(r)=P_1(-r)` defeats a site-local scalar-bit reading.  For the
locked compound packet, however, the 26 recorded positions have zero relative
sum and hence centroid equal to the selected anchor.  Once that centroid is
recovered, every displacement and radial bit is fixed.  This is the exact
anchored-packet semantics to test; it is not an autonomous overlapping-template
semantics.

A quarter turn about an axis can multiply one `|Locked><Ready|` representative
by `+-i`.  The phase cancels in `K X K^dagger`; branch Choi operators and CP
maps still transform exactly.  A checker must reject physical noncovariance,
but must not reject a pure Kraus-gauge phase.

## CP/TP and permanence witness

For a fixed Ready front,

```text
sum_b K_(f,b)^dagger K_(f,b)
 = I_live tensor |Ready_f><Ready_f|.
```

Summing over the six orthogonal Ready fronts gives `I_live tensor P_ready`.
The STOP projector completes the identity.  Orthogonal pointer support makes
every branch CP on arbitrary reference-entangled inputs.

After a branch, all six status bits flip and the pointer is Locked, hence
orthogonal to every Ready word.  All formation branches vanish and STOP is
identity.  This proves permanence for the output 26-site Record packet inside
the isolated instrument.  It does not prove compatibility of overlapping
translated instruments.

## Record/live information boundary

If a nonselective channel is the identity on every six-qubit state, its Choi
matrix is rank one.  A sum of positive branch Choi matrices equaling that
rank-one operator forces every branch to share its support.  Each branch is a
nonnegative scalar multiple of the identity channel and has an effect
proportional to `I`.

The Stage-A effects are nonconstant.  Their Lueders instrument must disturb
some inputs.  Calling those inputs consumable live conditions is consistent;
calling them arbitrary permanent `M_2` Records whose full state is unchanged
is not.

## Principal risks

1. Product-state positivity masquerades as full-Hilbert effect positivity.
2. Duplicate axis signs are merged or falsely treated as input information.
3. Computational pointer bits receive a hidden trivial onsite action.
4. Radial projectors rotate only as labels, not as physical qubit states.
5. A Kraus phase is mistaken for failure or used to hide CP-map noncovariance.
6. An abstract dilation replaces the explicit effect square roots.
7. The live poststate is silently copied, restored, or called a permanent
   input Record.
8. Isolated STOP/lock behavior is overstated as mixed-front arbitration.
9. Radius-four atomic locality is called nearest-neighbor dynamics.
10. A supplied Ready packet or compound formation event is called an
    axiom-selected law.
