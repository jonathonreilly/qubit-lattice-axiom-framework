# Matter-Attachment Reduces to the Cross-Site Graded-Statistics Gate

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit.
**Primary runner:** [`scripts/frontier_koide_matter_attachment_graded_statistics_gate.py`](../scripts/frontier_koide_matter_attachment_graded_statistics_gate.py)

## Context

The companion note `KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02`
localized the charged-lepton faithfulness pin to a single matter-attachment
posit: the per-site `C^2` qubit STATE carrying the `j = 1/2` SPINOR rep of
the physical spatial rotation as its transformation LAW (action on the ket),
one level above the merger's OPERATOR-FRAME (adjoint) covariance
`U(R) sigma_i U(R)^dag = R_ij sigma_j`. Four independent levers were then
probed in parallel to FORCE that attachment from A1 (per-site qubit /
`Cl(3,0)`) + A2 (`Z^3` lattice + emergent time) + the retained inventory:
(1) audit the Kawamoto-Smit reconstruction; (2) derive a new state-level
rotation-covariance theorem; (3) the emergent-Lorentz boost lever; (4) a
selection principle privileging the genuine spin lift over the spin-blind
compensator.

## Claim

All four levers FAIL to force the matter-attachment, for a **common reason**,
and the pin REDUCES to a single cross-site **graded-statistics gate**: does
A1 + A2 force graded / CAR (fermionic) statistics over the native hard-core
boson? That gate is already a retained no-go
(`staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25`,
**retained_no_go**), and it coincides with the generation-identification
chirality question.

The common reason: the native first-order operator `D`'s spatial covariance
factors through `SO(3) ~ O` (the octahedral point group) and is **blind to
the `SU(2)` cover**. The genuine on-site `2 pi = -1` spinor sign DOES live
natively on the qubit `C^2`, but it is decoupled from everything `D`'s
spatial covariance can see. So no single-site rotation or boost covariance,
and no representation-closure argument, can select the spinorial-ket reading.
The discriminator is **graded (fermionic) locality** -- a cross-site
property -- not a single-site covariance.

### The four levers (all verified by the runner, non-circular)

**(4) Selection principle -- the sharpest, by direct octahedral-group
computation.** The spin-blind sign-field compensator `W(R)` that restores the
native single-component `D`'s lattice-rotation invariance closes into an
**honest, untwisted** representation of the octahedral group `O`:

```text
V(R) = P_R diag(s_R),   [V(R), D] = 0   for all 24 rotations,
V(R_1) V(R_2) = +V(R_1 R_2)   for all 576 pairs   (trivial Z_2 cocycle).
```

The genuine spin lift `U(R)` (the `SU(2)` double cover `2O`) is by contrast
**projective**: 208 of 576 pairs close with `-1` (the `2 pi = -1` sign).
Both `U(R)` and the spin-blind `V(R)` satisfy `D`-covariance, because `D`'s
covariance is the sign-blind adjoint `U sigma U^dag` (identical for `U` and
`-U`). So representation-closure does NOT force the spinor lift over the
spectator reading. (Route 4)

**(3) Boost lever.** A single-component (SCALAR) two-point function is
`SO(3,1)`-covariant -- `G(Lambda p) = G(p)` under random `SO(4)`
transformations -- with no spinor index. The retained
`lorentz_boost_covariance_3plus1d_theorem_note` (**retained_bounded**) already
realizes full boost covariance with a free scalar field. The spinor
transformation law applies only to an ALREADY-spinor field; boost covariance
does not create the index. The `2^4 = 4 x 4` spin-times-taste reindexing that
WOULD build a spinor is a `d = 4` / 16-corner structure the framework
(`d = 3+1`, 8 spatial corners `(Z_2)^3`) does not natively carry. (Route 3)

**(2) State-level theorem.** The adjoint -> fundamental upgrade is a genuine
**identification, not a theorem**. There are two spaces: Space 1, the qubit's
OWN `C^2` (where states carry the fundamental automatically by Schur), and
Space 2, the matter FIELD index (a separate Grassmann/Fock index).
`docs/MINIMAL_AXIOMS_2026-05-20.md` excludes particle sectors as primitives;
the matter realization is an OPEN GATE. The attachment is the identification
Space 2 = Space 1, supplied only by the open staggered-Dirac reconstruction.
(Route A)

**(1) Kawamoto-Smit audit.** The KS reconstruction
(`staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07`,
**unaudited**) is forcing only at the consistency level (the staggered phases
are the unique consistent spin-diagonalization GIVEN single-mode Grassmann
matter). Its antecedent BlockT1 ("matter = a single Grassmann mode, not a
two-component spinor") rides the statistics selection -- exactly the retained
no-go below -- plus a second `k = 1` multiplicity horn
(`staggered_dirac_substep1_u4_conditional_single_module_narrow_bounded_note_2026-05-17`,
**retained_bounded**: A1 + A2 do not force `k = 1`). (Route 1)

### The convergence

The native cross-site qubit ladders COMMUTE (hard-core boson), so the
fermionic / CAR frame is a Jordan-Wigner relabel = a frame CHOICE. The on-site
`2 pi = -1` spinor sign exists on the `C^2`
(`binary_octahedral_discrete_spinor_sign_narrow_theorem_note_2026-05-28`,
**retained_bounded**: `2O` acts as `-1` on the faithful 2-dim irrep), but it
is decoupled from the cross-site exchange operator
(`fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28`,
**retained_no_go**: the on-site sign and the two-site exchange are decoupled
on the discrete lattice; the rotation -> exchange Finkelstein-Rubinstein
bridge is continuum-only). So the four single-site levers all miss the same
cross-site target.

## Disposition

The matter-attachment is **admitted-not-forced** by every single-site
covariance or selection lever. It reduces to ONE cross-site gate -- graded
(CAR/fermionic) statistics over the native hard-core boson -- which is the
retained statistics no-go, the same gate as generation-identification
chirality, and (Route A) the open identification Space 2 = Space 1.

## Verified tiers (origin/main audit ledger)

| claim_id | effective status |
|---|---|
| `lorentz_boost_covariance_3plus1d_theorem_note` | retained_bounded |
| `binary_octahedral_discrete_spinor_sign_narrow_theorem_note_2026-05-28` | retained_bounded |
| `staggered_dirac_substep1_u4_conditional_single_module_narrow_bounded_note_2026-05-17` | retained_bounded |
| `pre_record_reference_state_tracial_derivation_note_2026-05-20` | retained |
| `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` | retained_no_go |
| `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28` | retained_no_go |
| `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | unaudited |
| `lorentz_boost_free_staggered_fermion_2point_so4_narrow_theorem_note_2026-05-29` | audited_conditional |
| `dirac_weyl_fermion_dof_from_lorentz_and_chirality_admission_bridge_note_2026-05-28` | audited_conditional |

The minimality/economy candidate is governed by
`docs/audit/AXIOM_MINIMALITY_POLICY.md` as support-tier, not a retained
derivation, so "identify Space 2 with the existing qubit" is not a forcing
principle. The records/pointer lane's tracial state is retained on the
ungraded operator algebra, but the pointer identification is itself a
separate open admission.

## Non-circularity

The forward checks are tier verification, prose verification, and direct
computation (the octahedral cocycle, the scalar boost-covariance, the
commuting ladders), none of which uses the faithful representation or
`Q = 2/3`. The reduction is a localization, not a forcing.

## Next paths this opens

- The discriminator that would privilege the spinorial-ket reading is
  **graded (fermionic) locality** -- odd operators anticommuting at disjoint
  separation -- which the retained ungraded Lieb-Robinson locality is not.
  Equivalently, a lattice-native discrete-homotopy / graph-braid `pi_1`
  coupling the on-site `2O` sign to a cross-site exchange. This is the sharp,
  correct-dimension version of the carrier question and sits on the same gate
  as generation-identification chirality.
- The hard-core-boson frame is a live physical alternative: characterize the
  spin/flavor carrier of the natively hard-core-bosonic matter WITHOUT the
  Jordan-Wigner dressing -- it may reach the spinor structure by a route other
  than Kawamoto-Smit.
- Re-derive the corner -> spinor content on the true `(Z_2)^3` 8-corner
  substrate (Hamming orbit `1 + 3 + 3 + 1`), where the `d = 4`
  `2^4 = 4 x 4` spin-times-taste factorization is not available -- the
  correct-dimension version of the staggered species reduction.

This is a localization of the matter-attachment pin to a single cross-site
gate, not an enumeration of routes.
