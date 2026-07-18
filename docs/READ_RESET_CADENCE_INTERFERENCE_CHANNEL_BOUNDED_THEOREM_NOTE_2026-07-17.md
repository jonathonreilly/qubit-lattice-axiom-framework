# Read/Reset Cadence and the Interference Channel — Bounded Theorem

**Date:** 2026-07-17

**Claim type:** bounded_theorem

**Status:** branch-local source note; audit unset

**Claim scope:** For a supplied finite-dimensional unitary, declared rank-one
instrument, squared-modulus transition weights, and read/reset schedule, this
note proves the exact cadence-defect identity and its all-time monomial closure
criterion. It then applies the identity to the conditional Cycle-222 candidate
blocks. It does not derive an instrument, Record, occurrence rule, clock, mass
law, or axiom content.

**Primary runner:**
[`scripts/read_reset_cadence_interference_channel_bounded_2026_07_18.py`](../scripts/read_reset_cadence_interference_channel_bounded_2026_07_18.py)

**Campaign and controls:**
[`LOCKING_CADENCE_RECORD_KERNEL_DISCRIMINATOR_CYCLE223_NOTE_2026-07-17.md`](work_history/repo/review_feedback/LOCKING_CADENCE_RECORD_KERNEL_DISCRIMINATOR_CYCLE223_NOTE_2026-07-17.md)
with its
[`historical application runner`](../scripts/locking_cadence_record_kernel_discriminator_cycle223_2026_07_17.py).

## Imported surface

Let `U` be a supplied unitary and let `{R_a}` be a declared complete rank-one
projector family. Supply the dephasing map

```text
D_B(X) = sum_a R_a X R_a
```

and the frame weights

```text
K_t[a,b] = |<a|U^t|b>|^2.
```

Interpreting `K_t` as a transition kernel additionally supplies selective
read/reset semantics: after an outcome, the system is represented by that
rank-one state before the next interval. None of this structure is derived
from Record or Admissibility.

## Exact cadence-defect identity

Suppose the `n`-update interval acts first and the `m`-update interval acts
second. On inputs diagonal in the declared frame, the difference between one
read after `m+n` updates and a read/reset after each interval is

```text
Delta_mn = K_(m+n) - K_m K_n.
```

It is the diagonal representation of the channel

```text
D_B Ad_(U^m) (I-D_B) Ad_(U^n) D_B.
```

Entry by entry, `Delta_mn` is exactly the sum of the interference cross terms
between distinct intermediate frame paths. Every `K_t` is entrywise
nonnegative and doubly stochastic; every `Delta_mn` has zero row and column
sum. The runner verifies the matrix/cross-term identity independently on the
candidate blocks and on a seeded Haar unitary whose induced `K_2` and `K_3`
kernels do not commute, fixing the interval order rather than relying on the
commuting special structure of the candidate kernels.

## All-time closure criterion

For every positive `m,n`,

```text
K_(m+n) = K_m K_n
```

if and only if `U` is monomial in the declared frame: a permutation matrix
with arbitrary phases.

The forward implication for a monomial unitary is immediate. Conversely,
all-time closure gives `K_t=K_1^t`. Finite-dimensional unitary recurrence has
a subsequence `U^(t_j)` converging to the identity, hence `K_1^(t_j)` converges
to the identity. Therefore `|det K_1|=1`. The Hadamard determinant bound and
the unit column sums of the doubly stochastic `K_1` can saturate only when
each column has one unit entry. Doubly stochasticity then makes `K_1` a
permutation, and `U` is monomial.

Closure for one fixed interval pair can occur by cancellation and does not
satisfy this criterion.

The cadence-defect identity is an elementary channel expansion. The all-time
monomial closure criterion is proved here from finite-unitary recurrence and
the Hadamard bound, but no claim of literature novelty is made for either
statement.

## Conditional Cycle-222 application

For each supplied Cycle-222 direction block, up to global phase,

```text
C_beta^t = P_scalar + (-1)^t P_even + exp(i t beta) P_vector.
```

Its declared-frame kernel is

```text
|C_beta^t|^2 = P_scalar + e_t P_even + v_t P_vector,

e_t = 1                         when t is even,
      1/3                       when t is odd,

v_t = cos(t beta)               when t is even,
      -cos(t beta)/3            when t is odd.
```

Two odd intervals therefore leave the nonzero term `8/9 P_even` in the
cadence defect. The runner checks the closed kernel and defect formulas through
twelve updates in all three blocks, with maximum residual below `7.3e-14`.

At total duration sixteen, schedules with interval lengths `1`, `2`, `4`, and
`8` differ from a final-only diagnostic in the declared direction frame. A
favorable fixed cadence can nearly coincide by cancellation, while the
all-time family still fails closure. In the supplied eigenframe the same
unitary has the identity kernel; monomial relabeling/rephasing and passive
co-transformation controls separate a changed instrument from changed
notation.

For the supplied diagonal kick, every-tick read/reset is exactly kick-blind:

```text
|D_left U D_right|^2 = |U|^2.
```

Longer coherent intervals can reveal the kick through interference. This is a
property of the declared candidate update, kick, frame, and schedule—not a
universal theorem about force or measurement.

## Pointer and archive control

In the tested binary-projector, equal-superposition controlled-write
construction, one and two coherent pointer copies induce the same reduced
dephasing channel. Reversing the first modeled write while leaving the second
pointer untouched leaves reduced-system purity `1/2`; reversing both modeled
writes restores fidelity one. Only a separately supplied nonselective
dephasing channel mixes the retained modeled history state. That control
establishes neither spatially disjoint independent witnesses nor global
irreversibility, outcome selection, or a physical Record.

## Dependencies

The application inherits every conditional input and wall from:

- [Cycle 219 common matter/field coin](work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md);
- [Cycle 220 generated beta-phase register](work_history/repo/review_feedback/GENERATED_BETA_PHASE_REGISTER_CYCLE220_NOTE_2026-07-16.md);
- [Cycle 221 operator-mass equivalence](work_history/repo/review_feedback/OPERATOR_MASS_EQUIVALENCE_CYCLE221_NOTE_2026-07-17.md); and
- [Cycle 222 conditional mass compiler](work_history/repo/review_feedback/CONDITIONAL_FLAVOR_MASS_OPERATOR_COMPILER_CYCLE222_NOTE_2026-07-17.md).

These are branch-local, unaudited support surfaces, not retained authority.

## Boundaries

- The unitary, frame, squared-modulus rule, reset/repreparation, schedule, and
  candidate force kick are supplied.
- A nonselective ensemble dephasing is not a selected realized trajectory.
- Abstract pointer tensor factors are not demonstrated independent physical
  witnesses.
- The result derives no Record formation, permanence under all lawful
  continuations, Born frequency, event trigger, rate, or clock normalization.
- It makes no mass-spectrum, gravity, measurement-solution, TOE, or no-go
  claim.
- It has no constitutional effect and supports no axiom conclusion.

## Primary comparisons

The instrument, unistochastic-kernel, process-history, and decoherent-walk
background is prior work; see Davies and Lewis,
<https://doi.org/10.1007/BF01647093>; Ozawa,
<https://doi.org/10.1063/1.526000>; Życzkowski, Kuś, Słomczyński, and Sommers,
<https://doi.org/10.1088/0305-4470/36/12/333>; Benoist, Cuneo, Jakšić, and
Pillet, whose rank-one von Neumann instruments give unistochastic Markov
outcome measures, <https://doi.org/10.1007/s10955-021-02725-1>; Pollock et al.
for the process-tensor framework and its operational Markov condition,
<https://doi.org/10.1103/PhysRevA.97.012127> and
<https://doi.org/10.1103/PhysRevLett.120.040405>; Kendon and Tregenna for
decohered walks, <https://doi.org/10.1103/PhysRevA.67.042315>; and
Chandrashekar for periodically measured quantum walks,
<https://doi.org/10.1103/PhysRevA.82.052108>. The finite application to the
conditional Cycle-222 candidate is not asserted to be globally novel.

## Reproduction

```bash
python3 scripts/read_reset_cadence_interference_channel_bounded_2026_07_18.py
```

Expected summary:

```text
TOTAL PASS=10 FAIL=0
```
