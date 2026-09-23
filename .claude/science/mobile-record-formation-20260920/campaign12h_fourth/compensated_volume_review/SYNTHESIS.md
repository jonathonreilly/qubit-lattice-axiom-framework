# Consistent local dynamics as the lattice grows

The supplied compensated rotor target has a local infinite-volume dynamics
on Z^d, d>=2, at fixed electric, magnetic and formation couplings. A bounded
observable in a fixed region has a limit in operator norm as the surrounding
finite graph grows, uniformly on every compact time interval. Local formation
and transport remain part of that dynamics. The result takes the already
checked target first, then its spatial limit; it does not exchange a microscopic
or large-spin limit with volume or select the compensated interaction physically.

Read the frozen author note together with
[the topology clarification](../compensated_volume_author/ROOT_TIME_TOPOLOGY_CLARIFICATION.md).
The independent comparison found and resolved that narrow wording issue;
the original note and all mathematical/control evidence remain unchanged.

## Why unbounded electric fields do not invalidate the construction

The electric Hamiltonian is a sum of mutually commuting diagonal local
operators. Conjugating a bounded local observable by that evolution enlarges
its support by one fixed neighborhood, regardless of field amplitude or time.
The remaining Hamiltonian and formation maps are bounded local operators.
In the electric interaction picture, their norms remain bounded and their
support diameters are at most12 and8 in the incidence-graph metric. Constants
depend on lattice degree and the fixed bounded couplings, not volume or
the magnitude of the electric energy.

The interaction-picture coefficients are generally strongly continuous
rather than norm continuous. The root proof approximates them in time on
trace class, proves the bounded local propagation estimates for the sampled
generators, and passes those estimates through the ultraweak dual limit.
The independent proof instead caps each commuting electric term, applies
the bounded estimates, and removes the caps at fixed volume. Both routes
justify the extra topology step rather than importing a theorem with an
unmet norm-continuity hypothesis. The support-path machinery is standard;
the checked application, uncapped passage and model consequences are the
new conditional construction here.

Boundary comparison gives an exponentially decreasing distance tail with a
polynomial shell factor. It applies to the actual induced-graph target, whose
incomplete stars differ only near the boundary, and to the stated uniformly
bounded local boundary perturbations. The result is uniform over each fixed
local observable unit ball, and remains valid with finite matrix ancillary
factors. It does not make arbitrarily strong or bulk-reaching boundary driving
irrelevant, or identify states chosen by different boundary flux conditions.

## What the limit does and does not mean

The limiting maps form a unital completely positive semigroup on the norm
completion of the full finite local B(H) algebras. All-A occupancy is built
into the local effective spaces, so no infinite P projection is used. Locally
normal initial states remain locally normal, their local expectations vary
continuously with time, and all local Gauss constraints are preserved. No
uniform electric moment or spatial correlation assumption is needed for these
bounded-observable statements.

Operator-norm continuity in time on this whole algebra is false. A physical
plaquette shift has norm difference2 at electric times tending to zero as
the initial circulation grows. Fixed bounded local interactions change its
free evolution by at most C times time, so they cannot remove the obstruction.
A locally normal representation supplies strong/weak statewise continuity;
it does not restore norm continuity on the same algebra. A smaller invariant
regular algebra would need a separate construction and check.

The independent packet also supplies a separated-plaquette product example
showing that local normality does not ensure a global density in a preselected
infinite tensor-product representation. That is a separate attributed
counterexample. Neither proof introduces a global finite particle count,
finite total formation rate or first-event clock on the infinite lattice.

## A checked local physical diagnostic

Starting with all A sites plus, all B empty and zero electric field, a
resolved edge mark has z-1 orthogonal old-record destinations, z=2d. Its
coherent two-sign channel has the same total initial edge rate,
`2 kappa(z-1)`, but a different post-event state. Occupation of a fixed B
site initially increases at `4 kappa z(z-1)`, half from the newborn and half
from the transferred old record. Mean record number per vertex initially
increases at `2 kappa z(z-1)`: 24 kappa on the square lattice and 60 kappa
on the cubic lattice. These are initial derivatives, not a finite-time
exponential clock or closed equation for density.

A finite collection of local detector registers fits the locality argument
when its bounded jump extension preserves the original channel on discarding
the register. Finite-dimensional registers store finite outcomes or saturated
counts; exact unlimited counts require countable registers with bounded
shifts. No duplicate formation channel or autonomous detector is inferred.

## Evidence and review scope

Root author seal:
`5da6ab8a81e7f6442a3c63ece190e9119b3c2cdd00c9960465bc01cc963d1f7f`.
The root analytic draft was sealed before independent assignment. Independent
PRE:
`6e8bae143d8ee1e0c77c57461c8025143b660709ff89e42c5c072a38d2164d0f`;
FINAL:
`ad9aa6598563aabe3db38e0ae4bb421aef602782aa9c718daf479056402f8c89`.
Root read the complete arguments, scientific scripts and new comparison,
and authenticated 55 FINAL occurrences, 52 distinct identities. The independent
wording correction is separately acknowledged and bound to the original.

Root exact controls cover five square/cubic boxes, the necessary external
electric shell, the Wilson-loop countercontrol and local formation factors.
The independent implementation checks support and rate factors in d=2,3,4,
rebuilds the new external phase for both newborn signs, tests off-diagonal
field Grams and reproduces two selected overlap counts. The other three
finite overlap counts were source-reviewed and authenticated, not independently
rerun. The volume proof does not rest on numerical extrapolation or on the
number of passing finite checks. Versioned primary-source citations and read
receipts are included; full third-party papers remain outside publication.

This is a regular conditional research milestone. It confers no formal
retained status, microscopic error uniform in volume, field phase, photon
dispersion, autonomous source, empirical prediction or theory of everything.
