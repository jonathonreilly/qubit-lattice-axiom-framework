# Flavor — J-hunt round 3: conditional finite-generation algebra for `U_gen=iI3`; no doublet `J` is supplied.

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** bounded finite-algebra support conditioned on the explicit input `U_gen=iI3`; no physical spinor-to-generation bridge is asserted here.
**Runner:** `scripts/flavor_find_J_round3_dirac_generation_blind_2026_06_02.py` (SCORECARD 4/4).
**Source:** workflow `wf_2d355f65` — 5 hunt routes + 3-lens verification + synthesis (6 agents), unanimous 5/5.

## The test
Round 2 sharpened the wall to **Dirac vs Majorana**. The original round-3 packet tested whether the
charged-lepton Dirac reality structure descends to the generation-doublet `J -> det_C -> r=1/2` lane.
The 2026-06-04 audit repair narrows that packet: this note does not derive how the physical Dirac
reality operator acts on generation space. It checks only the finite `C3`-circulant generation algebra
conditioned on the explicit input

```text
U_gen = i I3.
```

Under that input, the checked question is whether a central generation scalar or its `C`-eigenbasis
phase centralizer can rotate the doublet weight or force `det_C/r=1/2`.

## Round-3 verdict: dirac_generation_blind_no_J
On the restricted finite packet, `U_gen=iI3` is a *spectator* to the doublet:

- Conditional input `U_gen=iI3` leaves the finite `C3`-circulant Hermitian family
  `H = aI + bC + conjugate(b) C^2` fixed (verified R3-1). This is a finite matrix consequence, not a proof
  that physical charged-lepton charge conjugation acts as the identity on generation space.
- The continuous centralizer `diag(1,e^{i phi},e^{-i phi})` in the `C`-eigenbasis also leaves `H` fixed
  (verified R3-2). Within this packet it is a spectator to `r=|b|^2/a^2` and does not choose the `kappa`
  block count.
- The checked `b`-rotating route `C -> e^{i theta} C` violates `C^3=I` at generic phase; the exact runner
  displays `(e^{i pi/7} C)^3 = e^{3 i pi/7} I != I`, so only cube-root phases preserve the `C3` relation
  (verified R3-3).
- The checked Hermitian `C3`-circulant anticommutant route is empty: solving
  `{H,Gamma_chi}=0` for `H=aI+(x+iy)C+(x-iy)C^2` gives `a=x=y=0` exactly (verified R3-4). Any nonzero
  `Gamma_chi` anticommutant therefore lies outside this `C3`-circulant packet.

## Trajectory and the pivot
This note now supports a narrower round-3 conclusion. Conditional on `U_gen=iI3`, a central
generation-space Dirac block does not supply the doublet complex structure, does not rotate `b`, and does
not force `det_C/r=1/2`. The finite obstruction evidence still points the lane toward the discrete
`kappa` block-count measure attacked in round 4, but the physical Dirac/Majorana generation-action bridge
remains open.

Not claimed here:

- a retained derivation that charged-lepton charge conjugation acts as `I3` on generation space;
- an exhaustive theorem that all continuous levers are closed;
- a physical charged-vs-neutral lane assignment from Dirac/Majorana reality alone.

## Provenance (verified 2026-06-02)
- Conditional `U_gen=iI3` invariance, centralizer invariance, `C3`-break under generic rephasing, and the
  exact no-circulant-anticommutant solve are verified directly (runner 4/4).
- Anchors: `koide_c3_generator_rephasing_obstruction` (retained), `koide_z3_equivariant_anticommuting_no_go` (retained_bounded), `koide_anticommuting_operator_derivation` (retained), `dm_neutrino_dirac_bridge` (retained).
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.

## Remaining bridge

The audit-quoted missing step is still a real open bridge if one wants the stronger physical statement:

```text
derive the charged-lepton Dirac reality operator's action on generation space.
```

This repair removes that bridge from the load-bearing claim rather than pretending it is established.
