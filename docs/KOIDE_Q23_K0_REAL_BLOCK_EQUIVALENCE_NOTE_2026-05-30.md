# Koide: Q=2/3 is the K0-real (real-Wedderburn-block) reading of A1+A2; the qubit `i` does not fix it

**Date:** 2026-05-30
**Claim type:** equivalence-characterization / bounded structural localization (positive)
**Status:** structural result. Approves no axiom and no import; sets no audit verdict.
The audit lane sets status and the per-block-vs-per-dimension convention tier.
**Primary runner:**
`scripts/frontier_koide_q23_k0_real_block_equivalence_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_q23_k0_real_block_equivalence_2026_05_30.txt`.

## Result (one sentence)

The charged-lepton Koide value is a single **reality-structure bit** on the generation
matter measure: `Q=2/3` **iff** the **real-Wedderburn-block** (`K0`-real, count each
block once / coherent-state) quantization of the A1+A2 generation carrier, and `Q=1`
**iff** the **complex-dimension** (`K0`-complex / trace-default) quantization — and the
`Cl(3)` central pseudoscalar `i`, which would push `Q=1`, is **forced only on the qubit
factor** and acts on the generation index as a **scalar**, so it does **not** fix the
choice.

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
permutation; nothing in A1+A2 complexifies **it**. So the forced qubit complexification
does **not** propagate to the generation factor: the doublet measure is a **free
convention slot** within A1+A2.

## A qubit is natively a coherent-state object — so the per-block reading is the faithful one

A qubit `C^2` is the space of Bloch coherent states: the spin-1/2 `SU(2)` coherent
states resolve the identity, `(2/4pi) integral |n><n| dOmega = I_2` (F3). Reading
"qubit-per-site" as a **coherent-state / Bargmann amplitude** is the **holomorphic**
quantization, which counts each complex mode (each block) **once** — the per-block
measure `-> Q=2/3`. This is arguably the **more faithful** bare reading of A1 than the
trace-default that yields `Q=1`.

## Correction: `C^3=I` does not make `Q=1` the forced default

`C^3=I` forbids a continuous `U(1)_b` **symmetry** (`(e^{i a}C)^3 = I` only at
`a in {0, 2pi/3, 4pi/3}`, F5.1). But the **Schur** complex structure
`Jcs in End_R(doublet) = C` **exists** (forced by FS=0, `Jcs^2 = -P_doublet`), so the
`det_C` per-block **measure** is available even though `U(1)_b`-as-symmetry is not
(F5.2). `C^3=I` bites the **symmetry**, not the **measure** — so the claim that it makes
`det_R / Q=1` the unique default is **over-stated**. Neither measure is forced.

## Boundary

This is an **equivalence-characterization**, not a forced derivation of `Q=2/3`. `Q=2/3`
is a native **convention-derivation**: it uses **no new axiom and no different
substrate** — the generation carrier is the real `R[Z_3]`, a qubit is a coherent-state
object, and the support for the real/block reading is already retained
(`cpt_exact_real_anti_hermitian_d`; `staggered_dirac_substep1` is statistics-agnostic).
But A1+A2 **also** admit the trace-default `Q=1`, so neither is **uniquely forced**.
Committing to `det_C` as **the** measure is the single user-approval **import**, to be
adopted (if at all) via the unit-convention precedent (source-note + paired-runner +
independent audit), not self-set.

**What this reveals:** the observed `2/3` is the canonical **idempotent / K-theoretic
count** of the same real `Z_3` generation structure `A2` supplies for free (singlet +
one complex-type doublet block, one slot each, equal-slot `= r=1/2 = Q=2/3`). It is not
a coincidence and not a tune; `Q=1` is the complex-dimension/trace reading that the
central `i` pushes only on the unrelated qubit factor. This sharpens
`koide_q23_block_weight_frontier` (retained_bounded) from "the equal-block selection is
unproved" to "the selection is exactly the `K0`-real-vs-`K0`-complex reality-structure
bit of the generation matter measure, with the forced qubit-`i` proven irrelevant."

**The open prize (both directions, not a no-go):** does any **retained** structure act
as a `C_3`-equivariant complex structure / measure-`J` on the doublet measure (selecting
`K0`-real) — given `C^3=I` bites only the symmetry, not the measure — or, dually, does a
retained structure force the trace/`K0`-complex reading? Either would close the slot.

## Anchors (live-ledger tiers)

retained / retained_bounded / retained_no_go: `cl3_complexification_split`,
`cpt_exact_real_anti_hermitian_d`, `koide_q23_block_weight_frontier` (retained_bounded),
`koide_circulant_q_two_thirds_algebraic`,
`staggered_dirac_substep1_u4_conditional_single_module` (retained_bounded),
`koide_z3_equivariant_anticommuting_no_go` (retained_bounded). Complements
`KOIDE_IMPORT_TWO_BIT_DECOMPOSITION_NOTE`, `KOIDE_KAHLER_DIRAC_SILENT_ON_MEASURE_NOTE`,
`KOIDE_REALITY_TYPE_PERMITTED_NOT_FORCED_NOTE`.
