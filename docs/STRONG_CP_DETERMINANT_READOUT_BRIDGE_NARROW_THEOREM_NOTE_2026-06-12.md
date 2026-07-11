# Strong-CP Determinant-Readout Bridge - Narrow Bounded Theorem

**Date:** 2026-06-12
**Current premise authority (2026-07-11):** every Tier-A/admission/registry
reference below is superseded historical context. It supplies no premise and
makes no dependency ready; the scientific conditions remain conditional/open.
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit any audit-owned registry.
**Primary runner:** [`scripts/frontier_strong_cp_determinant_readout_bridge_2026_06_12.py`](../scripts/frontier_strong_cp_determinant_readout_bridge_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/frontier_strong_cp_determinant_readout_bridge_2026_06_12.txt`](../logs/runner-cache/frontier_strong_cp_determinant_readout_bridge_2026_06_12.txt)

## Boundary

This note supplies the determinant-readout bridge named open by
`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`
for the **mass-determinant channel only**.

It proves a narrow theorem:

1. If the mass-side strong-CP readout is a supplied determinant-channel record
   readout, so independent mass blocks compose by determinant multiplication,
   then the phase part of any continuous block-multiplicative phase readout is
   a circle character `exp(i k arg det M)`.
2. K/CPT orbit registration sends `det M -> conj(det M)` and requires equal
   registered value on the orbit. Therefore the only K/CPT-invariant
   determinant phase character is `k = 0`.
3. K-even but nonmultiplicative phase probes, for example `cos(arg det M)`,
   are not admitted determinant-channel readouts because they violate the
   independent-block composition law.

This is not a gauge-theta theorem. It does not set `theta_gauge = 0`, does
not derive the real-positive Wilson action surface, does not eliminate
multi-plaquette or large-winding gauge data, and does not prove that every
possible action-level observable in the full theory factors through the mass
determinant. It only closes the mass determinant-channel bridge under the
stated Record/readout interface.

## Supplied Interface

The theorem is stated on a supplied finite mass-sector readout interface:

- each independent mass block has an invertible complex determinant
  `z = det M in C*`;
- direct sums of independent blocks compose by
  `det(M1 direct_sum M2) = det(M1) det(M2)`;
- a record scalar for this channel is finite-additive over independent record
  blocks, so its exponentiated phase character is multiplicative over the
  determinant product;
- K/CPT orbit registration identifies `z` and `conj(z)` as the same realized
  determinant-channel outcome;
- no within-block phase datum outside `det M` is supplied to this channel.

The Record axiom supplies the orbit/additivity discipline only after this
readout interface is supplied. It does not supply the determinant channel by
itself.

Theta(b)'s mass-side residual shares the K-real counting structure with
AC_phi_lambda(i). That physical grain is now the explicit
[AC orbit-occupancy statistical-grain derivation obligation](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md).
It carries zero premise weight. Consequently the mass-side physical reading is
conditional/pending until that obligation is retained-derived; the algebraic
character result below does not itself close the physical grain.

## Theorem

Let the phase part of a determinant-channel readout be a continuous
multiplicative map on the determinant phase circle:

```text
f(e^{i phi_1} e^{i phi_2}) = f(e^{i phi_1}) f(e^{i phi_2}),
f(1) = 1.
```

For completeness, the continuous characters of `U(1)` are

```text
f_k(e^{i phi}) = exp(i k phi),   k in Z.
```

Indeed, lifting a continuous multiplicative circle map through the universal
cover gives a continuous additive phase map `F(phi + psi) = F(phi) + F(psi)`
modulo `2 pi`; continuity gives `F(phi) = k phi`, and single-valuedness on
`phi ~ phi + 2 pi` forces `k in Z`.

K/CPT orbit registration sends `phi -> -phi`, so an admissible scalar for one
realized orbit must obey

```text
f_k(e^{i phi}) = f_k(e^{-i phi})   for all phi.
```

Thus `exp(i k phi) = exp(-i k phi)` for all `phi`, equivalently
`sin(k phi) = 0` for all `phi`; hence `k = 0`. The determinant phase is erased
inside this determinant-channel readout class.

## Hostile Guard

K/CPT evenness alone is weaker than this theorem. The function

```text
g(e^{i phi}) = cos(phi)
```

is K-even, since `cos(-phi) = cos(phi)`, and it is phase-sensitive. But it is
not a determinant-channel block readout:

```text
cos(phi + psi) != cos(phi) cos(psi)
```

for generic independent phases. It therefore violates the multiplicative
determinant/block-composition law required by the supplied interface.

Similarly, any action-level observable that does not factor through the
mass-determinant channel is outside this theorem. The gauge-side theta residual
remains separately open.

## Consequence For The Theta P2/K-CPT Row

Composed with
`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`,
this bridge supplies the missing determinant-readout interface for the
mass-determinant component:

```text
physical mass determinant-channel readout
  + independent-block determinant multiplication
  + K/CPT orbit registration
  -> no registered phase character from arg det(M_u M_d).
```

The statement is deliberately conditional on the supplied mass determinant
channel. It does not promote the strong-CP parent, does not touch the Tier-A
registry, and does not claim the gauge/action theta residual is discharged.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) for the Record additivity/orbit boundary once
  a readout context is supplied.
- [`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)
  for the broader Record-registrable additive-plus-orbit bridge already cited
  by the theta P2/K-CPT row; this note is only the mass-determinant-channel
  specialization.
- [`STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md) as the strong-CP selected-surface parent whose
  mass-side determinant readout is the target; this note does not promote it.

Context target, not a dependency edge: this bridge is intended to feed
`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_strong_cp_determinant_readout_bridge_2026_06_12.py
```

Expected:

```text
TOTAL: PASS=19 FAIL=0
```
