# Wilson Generator-Rescaling Beta Bookkeeping - Bounded Algebraic Lemma

**Date:** 2026-06-17
**Claim type:** bounded_theorem
**Type:** bounded algebraic support / convention bookkeeping
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome, does not retag any ledger row, and does not
promote any `g_bare` claim.
**Primary runner:**
[`scripts/wilson_generator_rescaling_beta_bookkeeping_2026_06_17.py`](../scripts/wilson_generator_rescaling_beta_bookkeeping_2026_06_17.py)

## Purpose

The audited conditional row
[`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md)
names a missing bridge: if one wants to route generator rescaling into a
Wilson action coefficient, the source must state which quantity is held fixed
and derive the corresponding `beta_new / beta_old` law.

This note supplies only that bookkeeping theorem. It does not derive the
Wilson action surface from the framework, does not select `beta = 6`, and does
not prove `g_bare = 1`.

## Setup

Let `T_a` be a finite `SU(N)` generator basis with trace metric

```text
    Tr(T_a T_b) = kappa delta_ab.
```

For the usual canonical fundamental normalization used elsewhere in the repo,
`kappa = 1/2`. The small-plaquette quadratic part of the Wilson plaquette
action has, up to common geometric factors, coefficient

```text
    Q(beta, g, kappa) = beta g^2 kappa / N.
```

Matching this quadratic coefficient to the same continuum normalization gives
the standard relation in the more general trace metric convention

```text
    beta = N / (kappa g^2),
```

which reduces to `beta = 2N/g^2` when `kappa = 1/2`.

Now rescale the generator basis by a real nonzero scalar

```text
    T'_a = c T_a.
```

Then the trace metric changes as

```text
    kappa' = c^2 kappa.
```

## Lemma

There is no single convention-free `beta_new / beta_old` law unless the
held-fixed surface is named. The two useful exact bookkeeping maps are:

1. **Fixed component coupling and field coordinates.** If `g` and the
   component field coordinates are held fixed while `T_a -> c T_a`, then the
   Wilson quadratic coefficient scales by `c^2`. To keep the same continuum
   quadratic normalization,

   ```text
   beta_new / beta_old = 1 / c^2.
   ```

2. **Fixed group element / exponent bookkeeping.** If the Lie-algebra exponent
   is held fixed by simultaneously changing the coupling coordinate to
   `g_new = g_old / c`, then

   ```text
   g_new^2 kappa_new = g_old^2 kappa_old
   ```

   and the Wilson quadratic coefficient is unchanged at the same `beta`.
   If one then reports the reparameterized coupling in a re-canonicalized
   `kappa = 1/2` coordinate, the canonical formula
   `beta = 2N/g^2` gives the coordinate relation

   ```text
   beta_canonical(g_new) / beta_canonical(g_old) = c^2.
   ```

These are convention maps, not physical selections. They explain why beta
routing cannot be inferred from the Gram-scaling lemma alone.

## What This Closes

This note closes the narrow algebraic bridge:

```text
T_a -> c T_a
  + named held-fixed convention
  => exact beta bookkeeping law.
```

It can serve as bounded support for rows that need to state the Wilson
generator-rescaling convention explicitly before discussing `beta` or
`g_bare` coordinate changes.

## Non-Claims

This note does not:

- derive the Wilson plaquette action from the three framework axioms;
- select the physical local Wilson action surface;
- derive or audit `beta = 6`;
- derive `g_bare = 1`;
- remove all continuum rescaling freedom as a physical theorem;
- identify the algebraic `SU(3)` carrier with physical QCD color;
- edit or predict audit status.

## Runner Certificate

The paired runner checks exact rational instances of:

- `kappa -> c^2 kappa`;
- fixed-component matching `beta_new / beta_old = 1/c^2`;
- fixed-exponent matching at unchanged `beta`;
- re-canonicalized coupling-coordinate reporting
  `beta_canonical(g/c) / beta_canonical(g) = c^2`;
- source-boundary text forbidding `g_bare = 1`, `beta = 6`, or audit-status
  promotion.

Expected output:

```text
SUMMARY: PASS=29 FAIL=0
```

## Status Certificate

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: "Wilson beta bookkeeping under explicitly named generator-rescaling conventions"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The note supplies exact bookkeeping for a supplied Wilson quadratic surface; it does not derive the Wilson action surface, beta=6, or g_bare=1."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
