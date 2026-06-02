# Koide Q=2/3 as Real-Wedderburn Block Count; Trace/Dimension Gives Q=1

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Claim boundary:** bounded equivalence/localization for the `Z_3` generation carrier. It
compares two allowed measure conventions and does not choose the physical convention.
**Primary runner:**
`scripts/frontier_koide_q23_k0_real_block_equivalence_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_q23_k0_real_block_equivalence_2026_05_30.txt`.

## Result (one sentence)

For the `Z_3` generation carrier, equal real-Wedderburn-block weighting gives `Q=2/3`,
complex-dimension/trace weighting gives `Q=1`, and the `Cl(3)` central pseudoscalar
`i` is forced only on the one-qubit factor and acts on the generation index as a scalar,
so it does not decide the measure convention.

## The fork is `K0`-real vs `K0`-complex (Frobenius-Schur)

`Z_3` has Frobenius-Schur indicators `(+1, 0, 0)` (F1): the **real** group algebra
`R[Z_3] = R (+) C` has **two** real-irreducible blocks (`K0`-real `= Z^2`) — the
complex-type doublet `(omega, omega-bar)` is **one** real block of real-dimension 2 —
while the complexified `C[Z_3] = C^3` has **three** blocks (`K0`-complex `= Z^3`). With
`Q = (1+2r)/3`, `r = |b|^2/a^2`, and block energies `E_+ = 3a^2`, `E_perp = 6|b|^2`:
counting **each real block once** (equal block energy) gives `3a^2 = 6|b|^2 -> r=1/2 ->
Q=2/3` (verified end-to-end on the real circulant: `sum lambda = 3`, `sum lambda^2 = 6`,
`Q = 2/3`); counting by **dimension** (doublet weighted by 2) gives `r=1 -> Q=1` (F4).

## The qubit `i` is a generation scalar — it does not fix the choice

The `Cl(3)` central pseudoscalar `omega_Cl = sigma_1 sigma_2 sigma_3 = i*I_2` is forced
on the per-site **qubit** factor (F2.1). But on the **generation** triplet it acts as
the **scalar** `i*I_3` (eigenvalues `+i` on all three isotype modes, including the
singlet) — **not** the traceless doublet complex structure `diag(0, +i, -i)` (the
spectrum of `Jcs`) that the per-block `det_C` count requires (F2.2). The generation
carrier is built from the **real** `Z^3` lattice + real `hw=1` orbit + real `C_3`
permutation; the framework baseline does not by itself complexify **it**. So the forced qubit complexification
does **not** propagate to the generation factor: the doublet measure is a **free
convention slot** in this bounded comparison.

## Coherent-state reading supplies the per-block candidate

A qubit `C^2` is the space of Bloch coherent states: the spin-1/2 `SU(2)` coherent
states resolve the identity, `(2/4pi) integral |n><n| dOmega = I_2` (F3). Reading
"qubit-per-site" through a **coherent-state / Bargmann amplitude** convention gives a
concrete reason to consider the per-block measure, under which each block is counted
once and `Q=2/3`. This supplies a candidate convention; it is not a forcing principle by
itself.

## Correction: `C^3=I` does not make `Q=1` the forced default

`C^3=I` forbids a continuous `U(1)_b` **symmetry** (`(e^{i a}C)^3 = I` only at
`a in {0, 2pi/3, 4pi/3}`, F5.1). But the **Schur** complex structure
`Jcs in End_R(doublet) = C` **exists** (forced by FS=0, `Jcs^2 = -P_doublet`), so the
`det_C` per-block **measure** is available even though `U(1)_b`-as-symmetry is not
(F5.2). `C^3=I` bites the **symmetry**, not the **measure** — so the claim that it makes
`det_R / Q=1` the unique default is **over-stated**. Neither measure is forced.

## Boundary

This is an **equivalence-characterization**, not a forced derivation of `Q=2/3`. It uses
no new substrate: the carrier is the real `R[Z_3]`, with the same real/block and
trace/dimension readings compared by the runner. The framework baseline also admits the
trace-default `Q=1`, so neither reading is uniquely forced here. Choosing one as the
physical generation measure remains a separate convention/admission question.

**What this reveals:** the equal-slot `Q=2/3` rule is exactly the `K0`-real
real-Wedderburn-block count of the same real `Z_3` generation structure (singlet + one
complex-type doublet block, one slot each, equal-slot `= r=1/2 = Q=2/3`). `Q=1` is the
complex-dimension/trace reading. The forced qubit `i` is irrelevant to this split because
it acts as a scalar on generations rather than as the doublet Schur complex structure.
This sharpens the frontier left by `koide_q23_block_weight_frontier` without closing the
physical measure slot.

**The open prize (both directions, not a no-go):** can a future source result select the
real-block/per-block measure, or force the trace/`K0`-complex reading? Either would close
the slot.

## Load-bearing authorities

[CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md)
[CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md)
[KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md)
[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
[STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17.md)
[KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)

Non-load-bearing companion context: `KOIDE_IMPORT_TWO_BIT_DECOMPOSITION_NOTE`,
`KOIDE_KAHLER_DIRAC_SILENT_ON_MEASURE_NOTE`,
`KOIDE_REALITY_TYPE_PERMITTED_NOT_FORCED_NOTE`.
