# Robust Local Conserved Densities On The Forced Interaction Class Are Charges And Energy -- Classification, Controls, And The Source-Form Reduction

**Date:** 2026-07-08
**Type:** bounded_theorem (exact membership + exhaustive kernel
computation at declared bounded scope, with two structural controls and
a pool-bounded gauged spot)
**Claim type:** bounded_theorem
**Claim scope:** On the two-species matter sector of the
record-preservation-forced gauge-invariant-local interaction class in
`d = 1` (declared surface, links at trivial holonomy, plus one gauged
spot leg), this note classifies every translation-covariant local
conserved density of bounded support and bounded fermionic degree: for
generic couplings the complete list is the two species charges and the
total energy density -- exactly three, nothing else. Two controls locate
where the count comes from: the free theory has twenty, and mutually
decoupled species keep separate energies; only inter-species coupling
collapses the energy ledger to one shared total. The corollary reduces
the static gravitational-source form on this surface to one global
constant multiplying the energy density, conditional on the named
premises. Nothing here derives gravitational dynamics, the value of the
constant, or an audit status.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/noether_source_current_classification_2026_07_08.py`](../scripts/noether_source_current_classification_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/noether_source_current_classification_2026_07_08.txt`](../logs/runner-cache/noether_source_current_classification_2026_07_08.txt)

## Why This Note Exists

The mass campaign's source-reduction theorem left one supplied step: the
gravitational source had to be ASSUMED species-blind. Its banked
linear-F reduction says that a species-blind, additive,
composite-consistent source functional is forced to be linear with one
slope; the composite dichotomy falsifier says a charge-coupled source
breaks composite universality at order `E_B` while an energy-coupled
source preserves it. What was missing is the classification underneath
both: WHAT can a lawful static source couple to at all? This note
answers that question exhaustively at bounded scope. The answer is
short: charges and energy. Everything else fails to be conserved.

## Surface And Premises

- **Classification surface (declared import, comparator role):** two
  fermion species on the `d = 1` staggered chain with the forced class's
  matter skeleton at trivial holonomy: species hoppings `t_a, t_b`,
  staggered masses `m_a, m_b`, and gauge-invariant local density
  couplings `U` (on-site inter-species), `V_a, V_b` (intra-species
  nearest-neighbor), `W_ab` (inter-species nearest-neighbor). Every term
  is a member of the gauge-invariant-local class the dynamics-form
  theorem forces. Hamiltonian-kernel convention; the two-step transfer
  cousin split is inherited from the engine note unchanged.
- **P-STATIC-SOURCE (named premise):** a static source must couple to a
  conserved local density -- otherwise the sourced readout changes under
  the internal dynamics of the sourcing matter and the static limit is
  not self-consistent. This premise is used by the corollary only, not
  by the classification.
- **Genericity:** the exhaustiveness statement is for generic couplings
  (all eight sampled independently from `[0.3, 1.7]`); the controls show
  exactly which degeneracies (free, decoupled) enlarge the list.

## Statement

Let `rho` be the map `o -> sum_m [tau^m(h), o]` on translation-covariant
formal sums of anchored, Hermitian, per-species number-conserving
normal-ordered fermionic densities `o` with support window `<= W` sites
and fermionic degree `<= 4`, where `h` is the Hamiltonian cell density.
All computations below are exact symbolic operator algebra (no Hilbert
space truncation); the algebra engine is machine-validated against
dense many-body matrices (CHECK-00b, residual `0.0`), and the string
tables against an independent finite-ring construction (CHECK-00,
`2.8e-14`).

**T1 -- membership (exact).** `Q_a`, `Q_b`, and `h` lie in `ker(rho)`:
worst residual `3.0e-16`, span angle `2.5e-13`.

**T2 -- exhaustiveness at bounded scope (decisive).** For five
independent generic draws, at both `W = 4` and `W = 6`:

```text
    dim ker(rho) = 3   (all ten window x draw combinations),
```

with singular gap `4.2e14` between the kernel and the first non-kernel
direction, kernel span matching `span{Q_a, Q_b, h}` to principal angle
`2.5e-13`, and commutator overflow exactly `0` (every output monomial
was representable; nothing was dropped). There is no fourth conserved
local density at this scope. Because kernel dimension can only jump
upward on closed coupling subvarieties, interior witnesses with a
fourteen-order gap pin the generic count; the five draws are
independent witnesses.

**T3 -- free control.** Switching all interactions off (same hoppings
and masses) inflates the kernel to dimension `20` at `W = 6`, with the
per-species energies `H_a, H_b` identified inside it (angles
`<= 2.4e-12`). Free theories hoard conserved densities; the generic
count of three is an interaction effect, not an enumeration accident.

**T4 -- decoupled-species control (the mechanism exhibit).** With
intra-species interactions on but inter-species couplings off
(`U = W_ab = 0`, `V_a, V_b != 0`), the kernel has dimension exactly
`4`: the two charges plus `H_a` and `H_b` SEPARATELY. Only inter-species
coupling -- the mediator channel -- collapses the two energy ledgers
into one shared total. The interaction the Record axiom forces is
precisely what makes a single species-blind energy readout exist at
all.

**T5 -- gauged spot (pool-bounded).** On the `N = 8` Schwinger ring
(engine machinery, `W_MAX = 3`, one generic `(m, g)` draw), within a
declared 17-operator gauge-invariant pool (staggered densities,
electric field and its square, covariant-hop Hermitian pairs,
density-field products, plus `Q` and `H` explicitly), the traceless
commutant has dimension exactly `2 = span{Q, H}` at principal angle
`2.4e-14`. This is a pool-restricted confirmation on the gauged
comparator, not an exhaustive classification; the boundary is stated.

**T6 -- named absentees.** The staggered charge and the per-species
particle currents -- both inside the candidate basis -- have commutator
residual `>= 1.0` at every generic draw: the named non-conserved
candidates are demonstrably outside the kernel, not silently missing
from the enumeration.

## Corollary -- Source-Form Reduction

Under P-STATIC-SOURCE, a static source coupling on this surface must
read a density from `ker(rho)`; by T2 the general lawful form is

```text
    S = alpha_a Q_a + alpha_b Q_b + gamma H.
```

The banked composite dichotomy (source-reduction falsifier and the
static-comparator sum rule) excludes any charge admixture: a
charge-coupled source accelerates a bound composite at
`2g / (2m - E_B) != g / M_comp` and breaks the gated window
universality at order `E_B / E`. What survives is `gamma H` alone: the
energy density with ONE global constant. Combined with the banked
linear-F reduction (additive, composite-consistent, species-blind
source functionals are linear with one slope), the chain now reads:

- classification (this note): the source can only be charges or energy;
- dichotomy (banked): charges break composite universality;
- therefore the unique window-WEP-compatible static source form on the
  classified surface is the energy density, coefficient `gamma` free.

Species-blindness of the gravitational source is thereby DERIVED on the
declared surface, modulo the named premises and the single constant --
which is the same freedom every physical theory retains in Newton's
`G`. The axiom-trigger shape pre-registered for this campaign (a kernel
larger than the expected list, meaning the source selection would need
supplied structure) did NOT fire: the axioms' forced class supplies
exactly enough conservation structure, no more, no less.

## Boundaries

- `d = 1`; two species; the classification basis is bounded at
  fermionic degree `<= 4` and support window `<= 6` sites; five generic
  draws; floating-point kernel counts gated by a `1e6` singular-gap
  requirement (measured `4.2e14`).
- The gauged leg (T5) is pool-restricted; an exhaustive gauged
  classification is a named follow-up.
- P-STATIC-SOURCE is a premise, not derived. The EXISTENCE of the
  source coupling (that `gamma != 0`, i.e. that gravity exists) remains
  supplied; only its form is classified.
- No gravitational field dynamics is derived; nothing here says what
  generates the potential.
- Hamiltonian-kernel convention; the transfer-surface version of the
  classification is a named follow-up.
- This note sets no audit status. Independent audit is required.

## Dependencies

- [`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  -- the forced interaction class whose matter sector is classified.
- [`WEP_SOURCE_REDUCTION_FINITE_SPACING_BOUNDARY_SCALING_WINDOW_BOUNDED_NOTE_2026-07-08.md`](WEP_SOURCE_REDUCTION_FINITE_SPACING_BOUNDARY_SCALING_WINDOW_BOUNDED_NOTE_2026-07-08.md)
  -- the linear-F reduction and the coupling-form dichotomy falsifier
  the corollary cites.
- [`COMPOSITE_MASS_ENERGY_EQUIVALENCE_STATIC_COMPARATOR_NO_GO_NOTE_2026-07-08.md`](COMPOSITE_MASS_ENERGY_EQUIVALENCE_STATIC_COMPARATOR_NO_GO_NOTE_2026-07-08.md)
  -- the sum rule behind the dichotomy's energy branch.
- [`GAUGED_SCHWINGER_STAGGERED_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md`](GAUGED_SCHWINGER_STAGGERED_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md)
  -- machinery for the gauged spot leg.

## Runner And Cache

Primary runner:
[`scripts/noether_source_current_classification_2026_07_08.py`](../scripts/noether_source_current_classification_2026_07_08.py)

Runner cache:
[`logs/runner-cache/noether_source_current_classification_2026_07_08.txt`](../logs/runner-cache/noether_source_current_classification_2026_07_08.txt)

Supervisor-executed runner result:

```text
TOTAL KERNEL-EXACT-3 elapsed=11.06s notes=none
```

Load-bearing residuals: kernel dimensions `W4=[3,3,3,3,3]`
`W6=[3,3,3,3,3]` with minimum gap `4.2e14`, maximum span angle
`2.5e-13`, overflow `0.0`; free control dim `20`; decoupled control dim
`4`; gauged pool dim `2` at angle `2.4e-14`; absentee residuals
`>= 1.0`; algebra validations `2.8e-14` and `0.0`.

## Changelog

- **2026-07-08.** Initial note. The first runner draft's Pauli-string
  candidate basis was combinatorially infeasible at the required
  support (the worker correctly refused: 25.2M columns at three cells);
  the classification basis was redesigned to exact normal-ordered
  fermionic algebra with per-species number conservation and bounded
  degree, with the validated string machinery retained as CHECK-00/00b
  cross-checks. Supervisor-executed result `KERNEL-EXACT-3`.
