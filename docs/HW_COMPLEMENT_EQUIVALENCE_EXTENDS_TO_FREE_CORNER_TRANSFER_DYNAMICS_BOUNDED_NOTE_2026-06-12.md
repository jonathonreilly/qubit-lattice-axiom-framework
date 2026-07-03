# hw-complement Registration-Equivalence Extends to Free Corner-Transfer Dynamics -- Bounded Note

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** source-side bounded theorem on the supplied free corner-transfer
surface only. No audit status is asserted here.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit any audit-lane-owned registry,
ledger, queue, or publication-status surface.
**Primary runner:** `scripts/frontier_hw_equivalence_free_transfer_dynamics_2026_06_12.py`

## Boundary

This note proves M1-M4 below only on the supplied free corner-axis surface. The
surface is finite and explicit: the corner cube `{0,1}^3`, the rotation
`R(x,y,z) = (z,x,y)`, coordinatewise complementation `b -> 1-b`, the supplied
three-channel Hermitian circulant, and the retained-bounded free two-step
transfer recipe applied per channel.

This note is firewall-limited:

- it does not select a physical species reading;
- it treats the free (U = 1) case only;
- it does not prove full-dynamics equivariance, and the interacting/gauge level
  is the named open that remains after this bounded result;
- it does not fix r or set any value of r;
- it leaves the occupancy binary untouched and does not alter the occupancy
  binary;
- it adds no axiom, primitive, physical comparator, species-selection rule,
  gauge extension, probability rule, or audit verdict.

Thus `hw=1` versus `hw=2` remains frame/convention data at this level. The
physical species identification, if used downstream, rides with the
`AC_phi_lambda` admission rather than with any result proved here.

## The Supplied Surface

The supplied corner cube is `{0,1}^3`. The frame rotation is
`R(x,y,z) = (z,x,y)`. Complementation is the coordinatewise map
`b -> 1-b`. The `hw=1` triplet is
`{(1,0,0), (0,1,0), (0,0,1)}` and the `hw=2` triplet is
`{(0,1,1), (1,0,1), (1,1,0)}`. Complementation maps the first triplet
bijectively to the second and commutes with `R` on all eight corners.

The supplied channel class is the Hermitian circulant

```text
H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T,
```

on the positivity domain `a > 2B > 0`, with unordered channel-mass spectrum

```text
lambda_k(delta) = a + 2B cos(delta + 2 pi k/3),    k = 0,1,2.
```

The transfer object is the retained-bounded free two-step construction applied
per channel. For each channel mass `lambda_k` and spatial momentum `p` at
`L_s = 2`, the one-channel two-step kernel is

```text
t_k(p) = exp(-2 E(lambda_k, p)),
E(lambda_k, p) = asinh(sqrt(lambda_k^2 + sin(p)^2)).
```

The full transfer object is the fermionic tensor-Fock second quantization of
these six one-particle mode kernels. Its finite Fock dimension is `2^6 = 64`.

## The Theorem

> **Theorem.** On the supplied free corner-axis surface just stated, the
> hw-complement registration-equivalence extends from the finite slot model to
> the free corner-transfer dynamics. The complement reading induces the same
> unordered channel-mass spectrum, the two readings' free two-step transfer
> structures are unitarily equivalent by the induced channel relabeling, all
> registrable free-transfer readouts coincide, and including this free dynamics
> does not make the hw choice registrable.

**M1 -- same channel content (runner checks M1a-M1c).** Complementation maps
the `hw=1` triplet bijectively to the `hw=2` triplet and commutes with
`R` on all eight corners. The orientation-reversal equation fails on a named
corner: for `(1,0,0)`, complement-after-rotation gives `(1,0,1)`, whereas
inverse-rotation-after-complement gives `(1,1,0)`. Thus the complement reading
preserves the supplied orientation rather than reversing it. Both readings
carry the same supplied circulant class, and the unordered spectrum
`{lambda_k(delta)}` is identical. The runner reproves the slot-level facts
from scratch and checks positivity at the supplied parameter points.

**M2 -- unitarily equivalent transfer structures (runner checks M2a-M2b).**
Let `Pi` be the channel permutation induced by complementation, lifted to the
six-mode tensor Fock space by permuting each channel's `L_s = 2` spatial modes.
Then, on the 64-dimensional Fock space,

```text
T^2(hw=2) = Pi T^2(hw=1) Pi^dag.
```

The equality is checked numerically at the supplied parameter points by
building the second-quantized diagonal transfer matrices and measuring the
matrix residual.

**M3 -- all registrable transfer data coincide (runner checks M3a-M3d).** For
both readings and for `N = 1,2,3`, the Fock traces
`Tr Gamma(t)^N` are equal. The dispersion multisets are equal. The
trace-correspondence normalization is identical: the canonical Berezin
normalization `lambda = 1` gives the same trace equality for both readings, and
a `lambda = 2` rescale breaks it in the same way for both readings. The runner
uses an explicit one-pair Grassmann expansion for the Berezin side rather than
replacing the check by a determinant shortcut. Consequently every registrable
readout of the free transfer object in the cited class -- additive and
K/CPT-orbit-constant, hence channel-symmetric by M2 -- takes the same value on
the two readings. A concrete witness is `log Tr Gamma(t)`, which is additive in
the transfer spectrum and constant on the relevant K/CPT orbit of the positive
free data.

**M4 -- consequence (runner check M4).** M1, M2, and M3 assemble to the bounded
conclusion: the hw-complement registration-equivalence already established on
the finite slot model extends to the free corner-transfer dynamics. The next
path is the interacting/gauge level; that level remains the named open.

## Consequence

Adding the supplied free transfer dynamics does not make the hw choice
registrable. The free transfer object registers the same unordered masses, the
same dispersions, the same Fock traces, and the same canonical Berezin
trace-correspondence data for the two complement readings.

The named open is now located at the interacting/gauge level. This note opens
that next path; it does not supply it.

## What This Note Does NOT Claim

- It does not select matter-as-`hw=1` or matter-as-`hw=2` as the physical
  species reading.
- It does not state that the two readings are physically identical in an
  interacting theory.
- It does not supply a gauge-background, gauge-integrated, or interacting
  transfer equivalence.
- It does not prove full-dynamics equivariance.
- It does not fix r, force `r = 1/2`, or change any r-admission boundary.
- It does not touch, reinterpret, or revise the occupancy binary.
- It does not derive `delta`, a charged-lepton value, or any downstream
  physical species identification.
- It does not promote, demote, retire, or edit any dependency.

## Dependencies

- [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
  -- the retained-bounded per-channel free two-step transfer engine reused
  here.
- [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
  -- the canonical pair measure used for M3's Berezin side.
- [`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)
  -- the additive and K/CPT-orbit-constant registrable class used in M3.

## Context

The following companions are context only; all facts used above are reproven in
the runner:

- `ACPHILAMBDA_HW_COMPLEMENT_READING_REGISTRATION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-06-12.md`
  (in review).
- `corner-extension note` (in review).
- `trace-correspondence note` (in review).
- `ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09.md`
  (`open_gate`).
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status
authority.
