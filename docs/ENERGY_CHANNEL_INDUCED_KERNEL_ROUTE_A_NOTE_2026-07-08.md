# The Lapse Channel Is Exactly Massless -- Matter-Induced Kernels For The Energy Sector, Conservation-Protected Shift Symmetry, And The Route A Result

**Date:** 2026-07-08
**Type:** bounded_theorem (exact identities + exact linear-response
computations on the declared surfaces; one interacting confirmation leg)
**Claim type:** bounded_theorem
**Claim scope:** On the framework's matter surface, the matter-induced
quadratic kernel for local coupling modulations is computed exactly in
three channels. Bond and site channels are MASSIVE at every nonzero
mass (induced range tied to the pair threshold, verified). The LAPSE
channel -- local modulation of the full energy density, whose uniform
mode is the registered global time-unit convention -- is EXACTLY
massless at every mass: its `k = 0` kernel vanishes identically
(machine zero), because a uniform lapse rescales the Hamiltonian
without moving any eigenstate, and its small-`k` kernel is
`A(m) k^2 + O(k^4)` with strictly positive stiffness, the masslessness
enforced by energy conservation through the continuity equation
(identity verified at `1e-12`). The induced lapse dynamics is therefore
of the classified shift-symmetric Poisson class, sourced by energy
density by construction. What this note does NOT do: promote the lapse
to a dynamical variable -- that promotion is the supplied step the
campaign's synthesis note surfaces to the owner. No audit status set.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/energy_channel_induced_kernel_2026_07_08.py`](../scripts/energy_channel_induced_kernel_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/energy_channel_induced_kernel_2026_07_08.txt`](../logs/runner-cache/energy_channel_induced_kernel_2026_07_08.txt)

## Why This Note Exists

The source-law classification pinned what an energy-sourced field must
look like (shift-symmetric, subtracted, Poisson-class). This is Route A
of the derivation campaign: does the matter sector INDUCE such dynamics
for any background field, Sakharov-style? The generic expectation was
no -- induced scalars are massive. The generic expectation holds for
the generic channels and fails, exactly and for a structural reason,
for precisely the one channel whose global mode the framework already
treats as a convention.

## Results

**T1 -- generic channels are massive (exact linear response, free
surface, `N = 256`).** Bond-modulation and staggered-site channels:
`chi(0) > 0` at every `m > 0` (bond: `0.69 / 6.35 / 19.7` at
`m = 0.05 / 0.2 / 0.5`; site channel massive at every mass including
`m = 0`), with the real-space induced kernel decaying at the pair
threshold `2m` (fitted rates `0.105 / 0.4005 / 0.964` against
`0.1 / 0.4 / 1.0`). Internal consistency: the Lehmann `chi(0)` agrees
with the independent finite-difference ground-energy curvature to
`1e-6` relative at every point. At `m = 0` the bond channel is the
special case of T2 (at zero mass the uniform bond operator IS the
Hamiltonian).

**T2 -- the lapse channel is exactly massless at every mass
(decisive).** For `O_L(n)` = the full local energy density (bond plus
half of each endpoint site term):

```text
    chi_LL(0) = 0   exactly (machine zero, ~1e-28), m in {0, 0.05, 0.2, 0.5},
```

with the redundancy exhibited independently: the ground energy under
`H -> (1 + eps) H` is linear in `eps` to `1.4e-15` -- a uniform lapse
shift rescales every eigenvalue and moves no eigenstate. This is
protection by redundancy, the same kind (not the same group) as the
protection that keeps the charge sector's field long-range: the mode's
global component is not a physical direction. The framework already
registers the global time-unit as a convention (the mass lane's I-TIME
import); the lapse field is its local version.

**T3 -- positive stiffness, Poisson-class form.** Small-`k` fit
`chi_LL(k) = A k^2 + B k^4`:

```text
    A(m) = 7.67 / 1.46 / 0.0334 / 0.00149   at m = 0 / 0.05 / 0.2 / 0.5,
```

all strictly positive (fit residuals `<= 2.9e-2`). The induced
quadratic action for a promoted lapse field is therefore of the
classified stable shift-symmetric class -- the unique class member
whose static law is Poisson -- with computable, mass-dependent
stiffness.

**T4 -- conservation protection (the identity that ties Route A to
Route B).** The lattice continuity equation forces every matrix
element `(eps_j - eps_i) <j|h(q)|i> = f(q) <j|j_E(q)|i>` with
`f(q) = 1 - e^{-iq}` and `j_E` built from the commutators of adjacent
energy densities -- the SAME operator content that obstructs Route B's
abelian gauging. Verified pairwise to `5.2e-12` and at kernel level to
`1.3e-13`: `chi_LL(q) = |f(q)|^2 * (current spectral sum)`, so the
`q^2` vanishing is energy conservation itself, not tuning. The
obstruction operator of Route B is the protection operator of Route A.

**T5 -- interacting confirmation and contrast legs.** The gauged
comparator (`N = 12`, `m = 0.3`): the lapse redundancy holds exactly in
the interacting theory (ground-energy linearity under uniform
rescaling, `1e-10`). The direct matter-mediated energy-energy
interaction is short-ranged with rate equal to the meson mass to `1%`
(`0.961` vs `0.969` at `g = 0.6`; `1.329` vs `1.328` at `g = 1.0`) --
gapped matter alone provides no long-range energy force; the long
range, if realized, lives in the induced lapse dynamics. The charge
sector's constraint-protected potential grows linearly alongside
(slope `0.152` at `g = 0.6`), the measured constrained-vs-unconstrained
contrast.

## Boundaries

- Free-surface legs are exact one-body linear response at `N = 256`,
  `d = 1`; the interacting legs are the declared comparator at
  `N = 12`. The stiffness values are surface-specific numbers, not
  universal constants.
- The lapse field here is a BACKGROUND modulation; nothing in this
  note makes it dynamical. Whether the axioms should promote it is the
  owner conversation, not a claim.
- Sign conventions: `chi = -d^2 E_0 / d eps^2` per channel; stability
  statements are in the convention documented in the runner.
- This note sets no audit status. Independent audit is required.

## Dependencies

- [`SOURCE_FIELD_STATIC_LAW_CLASSIFICATION_BOUNDED_NOTE_2026-07-08.md`](SOURCE_FIELD_STATIC_LAW_CLASSIFICATION_BOUNDED_NOTE_2026-07-08.md)
  -- the classified target law the induced lapse kernel lands in.
- [`ENERGY_GAUSS_CONSTRAINT_OBSTRUCTION_ROUTE_B_NOTE_2026-07-08.md`](ENERGY_GAUSS_CONSTRAINT_OBSTRUCTION_ROUTE_B_NOTE_2026-07-08.md)
  -- the sibling route whose obstruction operator is T4's protector.
- [`GAUGED_SCHWINGER_STAGGERED_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md`](GAUGED_SCHWINGER_STAGGERED_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md)
  -- machinery for the interacting legs.

## Runner And Cache

Supervisor-executed result:

```text
TOTAL INDUCED-LONGRANGE(LAPSE-CHANNEL; bond/site massive as before) elapsed=6.14s
```

Load-bearing residuals: lapse `chi(0)` machine-zero at all four masses
with rescaling linearity `1.4e-15`; stiffness positive with fit
residuals `<= 2.9e-2`; continuity identity `5.2e-12` pairwise,
`1.3e-13` kernel-level; bond/site massive with threshold-matched
ranges; gauged energy-response range = meson mass to `1%`; charge
contrast gated.

## Changelog

- **2026-07-08.** Initial note. Run 1 established the massive generic
  channels and flagged the `m = 0` bond shift symmetry; the supervisor
  identified its mechanism (the `q = 0` bond operator is `H` at
  `m = 0`) and its generalization to the lapse channel at all masses;
  run 2 added the lapse channel, the stiffness extraction, and the
  continuity-protection identity, all supervisor-executed.
