# Flavor — J-hunt round 3: charged-lepton Dirac reality structure is generation-blind (J_spin ⊗ I_gen); it does not supply the doublet J. det_C/r=1/2 not forced; wall pivots to the κ block-count measure.

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** bounded negative (round 3) + a lane reframing.
**Runner:** `scripts/flavor_find_J_round3_dirac_generation_blind_2026_06_02.py` (SCORECARD 4/4).
**Source:** workflow `wf_2d355f65` — 5 hunt routes + 3-lens verification + synthesis (6 agents), unanimous 5/5.

## The test
Round 2 sharpened the wall to **Dirac vs Majorana**. Round 3's lever: charged leptons *are* Dirac
(e⁻≠e⁺, from electric charge) — a *physical* reality structure, **not** the C³=I-forbidden continuous
U(1)_b. Does it descend to the generation-doublet J → det_C → r=1/2, and predict the lane (charged=Dirac;
neutral=Majorana)?

## Round-3 verdict: dirac_generation_blind_no_J
The Dirac reality structure **factorizes as J_spin ⊗ I_generation** and is a *spectator* to the doublet:
- Charge conjugation acts as the **identity on the generation index** (it neither permutes nor mixes
  e,μ,τ); U(1)_em charges all three generations identically. So on the generation factor the Dirac "i" is
  the central scalar `i·I₃` (verified R3-1: `U=i·I₃` leaves `H` fixed).
- The continuous centralizer `diag(1,e^{iφ},e^{-iφ})` also leaves `H` fixed (verified R3-2) — a uniform
  ambient complexification multiplies the singlet and doublet weights **equally** and **cancels in the
  ratio r**. So Dirac-ness does **not** touch `κ` (the isotype block-count) and does **not** force det_C.
- The maps that *would* set `κ=2` (r=1/2) are exactly the two blocked objects: a continuous doublet
  rotation `b→e^{iθ}b` = the rephasing `C→e^{iθ}C` (breaks C³=I except at the 3 cube roots, verified R3-3),
  or a Hermitian generation operator anticommuting with `Γ_χ` — which is **non-circulant /
  C₃-equivariance-breaking** (verified R3-4: no circulant anticommutes with `Γ_χ`).

## Trajectory and the pivot
Three genuinely-distinct levers — static `J_cs` (round 1), the fermionic Berezin frame (round 2), the
Dirac/charge reality structure (round 3) — all land **det_R-default**. The common root: **every
*continuous* lever leaves `b` fixed and cancels in `r`**, because they all act on the same complex `b`
without adjudicating `κ`. The wall is robust but **not closed**: the gap relocates cleanly to the **`κ`
block-count *measure*** — a discrete/counting question ("count the doublet as one block or two real
modes?"), decoupled from symmetry generators — which round 4 attacks. The Dirac/Majorana datum remains a
physically-meaningful per-sector reality label, so the **lane assignment is reframed** (pending a
spinor-reality-to-generation coupling), not closed.

## Provenance (verified 2026-06-02)
- Generation-blindness, centralizer, C³=I-break, no-circulant-anticommutant: verified directly (runner 4/4).
- Anchors: `koide_c3_generator_rephasing_obstruction` (retained), `koide_z3_equivariant_anticommuting_no_go` (retained_bounded), `koide_anticommuting_operator_derivation` (retained), `dm_neutrino_dirac_bridge` (retained).
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
