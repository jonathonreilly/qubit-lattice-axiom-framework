# Tree-Level Gluon Masslessness on a Bounded SU(3) Yang-Mills Surface

**Date:** 2026-05-02; scope repair 2026-05-27
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** `scripts/gluon_tree_level_massless_check.py`
**Log:** `outputs/gluon_tree_level_massless_check_2026-05-02.txt`

## Source Boundary

This row proves only the standard tree-level Yang-Mills algebra on a supplied
local Lorentz-covariant `SU(3)` field surface. It does not derive that field
surface from graph-first structural `su(3)`, does not add a new framework
axiom, and does not close nonperturbative or phenomenological QCD claims.

## Scope Repair

The previous version mixed two different claims:

1. a standard tree-level Yang-Mills algebra theorem for a local
   Lorentz-covariant `SU(3)` connection, action, and propagator; and
2. a framework-closure claim that the graph-first structural `su(3)` surface
   by itself constructs that local Yang-Mills field surface.

This repair keeps the algebraic theorem on the repo's bounded
Wilson/Yang-Mills surface and removes the unconditional framework-closure
wording.

No new axiom or new bridge theorem is introduced.

## Cited Surfaces

- [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md) supplies the
  native nonabelian structural gauge surface.
- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  supplies the graph-first structural `su(3)` closure.
- [`G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`](G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md)
  supplies the bounded Wilson plaquette action / continuum kinetic-matching
  context under its own bounded-surface boundary.

The last item is load-bearing for this repaired row. Therefore this row is a
bounded theorem, not an unbounded framework theorem from graph-first `su(3)`
alone.

## Claim

Assume a local Lorentz-covariant `SU(3)` Yang-Mills surface with connection
`A_mu^a`, standard infinitesimal nonabelian gauge transformation

```text
delta A_mu^a = (1/g) partial_mu omega^a + f^{abc} A_mu^b omega^c,
```

and kinetic action

```text
L_kin = -(1/4) F^a_{mu nu} F^{a mu nu}.
```

Then, at tree level:

1. the quadratic color-singlet candidate

   ```text
   L_mass = (1/2) m^2 A_mu^a A^{a mu}
   ```

   is gauge invariant only on the `m = 0` branch;
2. `F^a_{mu nu} F^{a mu nu}` is the gauge-invariant quadratic kinetic
   operator, up to total derivative and conventional normalization; and
3. in covariant Lorenz gauge, the transverse propagator has pole at `p^2 = 0`.

This is the tree-level masslessness theorem on the bounded Yang-Mills surface.

## Proof

Under the infinitesimal gauge transformation,

```text
delta L_mass
  = m^2 A_mu^a delta A^{a mu}
  = (m^2/g) A_mu^a partial^mu omega^a
    + m^2 f^{abc} A_mu^a A^{b mu} omega^c.
```

The second term vanishes pointwise because `f^{abc}` is antisymmetric in
`a,b` while `A_mu^a A^{b mu}` is symmetric in `a,b`. The first term integrates
by parts to

```text
-(m^2/g) (partial_mu A^{mu a}) omega^a
```

up to a boundary term. It is not zero for arbitrary local `omega^a` on the
unconstrained action surface unless `m = 0`. Thus a quadratic gluon mass term
is incompatible with local `SU(3)` gauge invariance.

For the kinetic term, the curvature transforms covariantly:

```text
delta F^a_{mu nu} = f^{abc} F^b_{mu nu} omega^c.
```

Therefore

```text
delta(F^a_{mu nu} F^{a mu nu})
  = 2 f^{abc} F^a_{mu nu} F^{b mu nu} omega^c
  = 0
```

again by antisymmetry against the symmetric color contraction.

The quadratic kinetic operator in covariant Lorenz gauge has the standard
inverse-propagator form

```text
Gamma^{(2)}_{mu nu,ab}(p)
  = i delta_ab ( -p^2 g_{mu nu} + (1 - 1/xi) p_mu p_nu ).
```

The transverse propagator is proportional to `1/p^2`, so the tree-level pole
is at `p^2 = 0`. A nonzero `m^2 g_{mu nu}` shift would move the pole, but the
mass operator is excluded by the previous calculation.

## What This Claims

- A bounded tree-level algebra theorem on the supplied local `SU(3)`
  Yang-Mills surface.
- Compatibility with the graph-first structural `su(3)` input only after the
  bounded Wilson/Yang-Mills surface is supplied.
- No observed values, fitted masses, or Standard Model phenomenology.

## What This Does Not Claim

- It does not derive the local Lorentz-covariant Yang-Mills connection from
  graph-first structural `su(3)` alone.
- It does not derive the Wilson plaquette action, continuum kinetic matching,
  or propagator surface from the minimal axioms.
- It does not prove nonperturbative QCD mass-gap, confinement, glueball, or
  dynamical-mass statements.

## Remaining Bridge

To use this beyond bounded theorem scope, a later row must construct a bridge
from the graph-first structural `su(3)` surface to a local Lorentz-covariant
Yang-Mills connection, gauge action, and propagator.

Until then, this row is only the tree-level masslessness algebra on the bounded
Yang-Mills surface.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/gluon_tree_level_massless_check.py
```

Expected:

```text
OVERALL: PASS
```

The runner checks:

- nonzero generic gauge variation of `A_mu^a A^{a mu}`;
- antisymmetry cancellation of the `f^{abc} A^a A^b` and `f^{abc} F^a F^b`
  terms;
- `1/p^2` tree-level propagator scaling; and
- nonabelian `SU(3)` structure constants.
