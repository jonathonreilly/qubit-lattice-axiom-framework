# Certified collective binding for six native column ends

**Status:** bounded-support.
**Primary runner:** [scripts/native_six_endpoint_binding.py](../scripts/native_six_endpoint_binding.py)

The native endpoint mechanism extends beyond the exactly solved four-column
example. Six neighboring ends on a 2x3 cross section have a bound relative-height
state below every asymptotic breakup channel in the specified first-order
coefficient sector. No new interaction or chosen collective potential is used.

## Separate genuine binding from a finite-box eigenvalue

Use the previously derived native height moves and the flat-connected component
at total longitudinal momentum zero. Exact layer parity forces every height
to occur an even number of times. Widely separated ends must therefore split
as 2+4 or 2+2+2.

For every induced four-column subset, a seven-state core plus independent
half-line tails represents the full even-parity sector, including components
unreachable from its own flat state. Interval LDL certificates on a momentum
grid, together with an explicit derivative bound between grid points, prove
that all these operators are bounded below by -5. Every two-column cluster
is bounded below by -2.

A discrete localization argument then gives an essential-spectrum lower bound
of -7 for the six-column relative operator. This is a lower bound, not a claim
that the exact continuum threshold equals -7.

An independently checkable integer trial vector supported on 1,459 configurations
satisfies exactly

    10 q^T H q + 71 q^T q = -3080607397277827 < 0.

It therefore has Rayleigh quotient below -7.1. Combining the exact upper bound
with the certified breakup lower bound proves at least one discrete eigenvalue
below -7.1. This establishes binding in the coefficient model; it does not rely
on extrapolating a sequence of finite-box eigenvalues.

## Coupling to the original readout

The original longitudinal distance-two Fourier readout is still the same
physical bond operator. In this height sector its unnormalized upper-interface excess has vertex
-4cos(p/2)exp(ip/2) times the sum of six endpoint phases. Projected between the
isolated bound-state clusters at nearby momenta, this tends to -24 times the
bound projection as p tends to zero. Finite-rank continuity therefore gives
a nonzero vertex for sufficiently small finite momentum, without supplying
a coupling constant.

A finite interval also has a lower-interface contribution; its full zero-momentum
excess is -48 for six intervals of length at least two.

The uniform projection is constant and produces no internal inelastic
transition. The argument allows a degenerate bound cluster; it does not prove
a unique species, nonflat dispersion, vacuum creation or experimental visibility.

## Scope and evidence

The [root proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIX_ENDPOINT_BINDING_PROOF.md)
records the full interval certificate, exact integer trial, cluster argument
and readout limit. Independent checks cover the four-column reduction,
interval replay, breakup threshold and source projection.

The supplied sector contains six same-orientation walls with infinite ordered
columns and uniform exterior. Its physical first-order energy is
12Jz+Jz lambda times the dimensionless coefficient eigenvalue. Finite paired
endpoints and higher native orders remain separate problems. This is progress
toward collective large features, not a full-H particle theorem, fermion,
universal gravitational scalar or cosmological identification. No empirical
calibration or independent observation is claimed.
