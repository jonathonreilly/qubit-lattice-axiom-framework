# Retarded cubic mass field — Cycle 213

**Date:** 2026-07-16

**Authority:** none

**Status:** conditional retarded proper-cubic source/response construction

**Constitutional effect:** none

**Audit:** unset

**Packaging:** draft parking branch and draft PR only

Companion runner:

```text
scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py
```

## Question

Cycle 211 generated a cubic Green field from the Cycle-210 object, but did so
with a dissipative relaxation rule.  That supplied a quasi-static answer at
every tick rather than a reversible field carrier with a causal propagation
history.

Can the same bound-object scalar source and respond to a strictly local,
retarded proper-cubic field with a one-edge causal cone, exact local energy
transport, and source/response reciprocity?  Can the old Green field then be
recovered as a sector of this dynamics rather than remaining a separate
solver?

## Candidate local law

At every cubic site keep two consecutive real field values.  The next value is

```text
phi_(n+1)(x) - 2 phi_n(x) + phi_(n-1)(x)
  = -dt^2 L phi_n(x) + dt^2 rho_n(x),
```

where `L` is the positive six-neighbour graph Laplacian and `dt=0.45`.  The
coefficient obeys the exact cubic CFL bound `dt^2 lambda_max < 4` with
`lambda_max=12`.  The update reads only the current six neighbours and the
same site's preceding value.

The matter/field interface is one supplied local bilinear interaction,

```text
V_int(x) = -g Q(x) phi(x).
```

Varying the same term with respect to `phi` supplies the source `g Q`;
varying it with respect to matter position supplies the response
`g Q grad(phi)`.  This ties the two couplings together.  It does not derive
the interaction term.

## Which scalar is `Q`?

`Q` is the principal vacuum-relative phase of the composite's scalar sector,
not a raw phase coordinate and not a record count.  On the bounded low-energy
branch used here it is

```text
Q = Arg(lambda_scalar / lambda_vacuum).
```

This distinction removes a representation bug that a literal numeric
`rest_phase` would have had.  A `2 pi` phase lift leaves the coin and `Q`
unchanged.  Arbitrary coin-basis changes and all 24 proper-cubic frame changes
also leave it unchanged.  The vacuum reference and principal low-energy
branch remain explicit conditions.

On the tuned Cycle-210 family, this vacuum-relative rest generator equals the
independently obtained dispersion/forced-inertia mass for all three tested
species.  A held-out two-object scalar sector adds `Q` before phase wrapping.
Shifting the allowed cubic coin family away from that alignment preserves
unitarity, locality, and cubic covariance while destroying universal
response.  The equality is therefore still a load-bearing supplied
condition, not a consequence of cubic symmetry alone.

## Result up front

The retarded field bridge succeeds conditionally.

- A point impulse remains inside an exact one-edge-per-tick Manhattan cone.
  A detector four edges away has exactly zero field gradient until the causal
  front reaches it.
- The update is uniquely reversible.  Frozen-predecessor site evaluation in
  forward, reverse, and random order gives the same next slice.
- The full source/update process commutes with every one of the 24
  proper-cubic rotations and with translations.
- Each site satisfies an exact local energy identity:

  ```text
  change in field energy = source work - outward one-edge flux.
  ```

  The edge flux is antisymmetric, so the global field-energy change equals
  source-port work.  After the source is turned off the field conserves its
  energy without relaxation; including a local source reservoir gives exact
  total-energy balance.
- For the zero-mode-subtracted periodic boundary experiment, the reversible
  retarded field's time-averaged Green field converges to the Cycle-211 Green
  field.  A
  separately evaluated finite modal sum agrees with the literal 6,000-tick
  history.
- The generated field drives the actual Cycle-210 molecular wavepacket.  The
  three tuned species exhibit species-independent response within the
  existing finite packet error while remaining in the scalar molecular band.
- For a simultaneously activated stationary pair, one bilinear interaction
  gives equal-and-opposite forces and the same pair interaction energy
  whichever object is named the source.  This is not a claim that matter
  forces alone balance for arbitrary moving retarded sources; field momentum
  must then be included.
- Source composition is linear; source deletion and coupling deletion remove
  their respective effects; redundant spectator records do not duplicate
  mass or source charge.

Reference diagnostics are emitted by the runner.  The central exact checks
are the sitewise continuity residual, source-work residual, 24-frame
covariance residual, causal-cone exterior amplitude, post-source energy
spread, and literal/modal time-average residual.

## Bare-metal reading

This candidate now supports the conditional chain

```text
local contact continuation law
  -> persistent proper-cubic composite
  -> vacuum-relative rest generator
  = dispersion and forced-inertia mass       [tuned condition]
  -> one local bilinear matter/field port
  -> retarded one-edge field propagation
  -> reciprocal molecular response
  -> exact local energy/work/flux accounting.
```

The important advance over Cycle 211 is structural.  The Green profile is no
longer the output of a dissipative potential solver only; it appears as the
time-averaged sector of a reversible causal field history.  Source and
response are no longer two independently chosen coefficients; both are the
two sides of one candidate interaction term.

## Conditions and remaining gap

The following physics is still supplied:

- two real field values per site and an unbounded continuous field alphabet;
- the centered wave law, its coefficient, and the global synchronous slice;
- the vacuum-relative charge map and its principal low-energy branch;
- the one bilinear matter/field interaction and coupling strength;
- the source history, including when a body is coupled to the field;
- the periodic uniform-background convention used only for the stationary
  time-average comparison; and
- the weak semiclassical reading of the field in the molecular response test.

The source history remains supplied.  The source reservoir used in the energy
ledger is an accounting port, not a derived finite-alphabet microscopic
degree of freedom.  The matter walk does not yet recoil self-consistently
while emitting the field, and the field has not been quantized or compiled
into the finite coin alphabet.  There is no tensor geometry, nonlinear
self-coupling, stress-energy source, equivalence beyond this scalar branch,
continuum limit, Lorentz-covariant field theorem, or empirical prediction.
This is not general relativity.

It also does not derive occurrence, record formation, a clock rate, Born
frequencies, or an axiom update.  The field state is coherent working state;
records may archive a detector outcome later, but are not the mass or the
field carrier.  There is no axiom conclusion.

## Attribution and scope

The proper-cubic composite and its operational mass contract are internal
Cycles 210 and 212.  The Green-field comparison is internal Cycle 211.  The
centered finite-difference wave equation and its discrete energy identity are
standard numerical-analysis structures; no novelty is claimed for them.

The one-dimensional Thirring-QCA molecule used in Cycles 205–209 is published
prior work of Bisio, D'Ariano, Mosco, Perinotti, and Tosini:

<https://arxiv.org/abs/1804.08508>

Cycle 213 claims only the bounded conditional composition and diagnostics
described here.  Global novelty has not been established.

This work remains on the draft parking branch.  It changes no foundation,
axiom, primitive, registry, policy, queue, or audit surface.

## Verification

```text
python3 scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py
```
