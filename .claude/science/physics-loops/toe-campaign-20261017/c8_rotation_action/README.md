> Landing review scope correction (2026-10-17): Historical exploration. The final paragraph records the invalid restricted-rotation test, superseded by the canonical bare-permutation note. Current supported data are finite pair eigenvalues; D3/single-C2 class inference has its stated localization premise, and D2 localization remains open.
> Exact original: `.claude/science/physics-loops/toe-campaign-20261017/landing_history/8b534c8e0d6aac10ea590d456a349a022bdb364cfd8b0b69de9c1027f6efc6cc.md.txt`.

# C8: rotation action on the BKSF fermion codes (spin question)

Exploration scripts (scratch originals; the runner is
`scripts/bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17.py`):

- `spin.py`, `spin_run.py`: for one D3 code at L = 4, solve for a Pauli sign correction F with
  U = F P_R, form W = U^n and test it against fermion legs from the rotation centre. Result:
  F = 1, W = 1 for C3^3 and C2^2 in sector (0,0,0).
- `all_signs.py`: all 60 codes x 8 sign sectors x every stabilizing rotation: does the bare permutation
  preserve the signed group? Yes exactly in sectors (0,0,0), (1,1,1); mixed sectors need corrections
  for some rotations (44 of 60 codes per mixed sector).
- `flux.py`: hop product around a plaquette vs signed generator: flux 0 in (0,0,0), pi in (1,1,1).

Conclusion (note): eta_f(C2, C2) = +1; the fermion is not spinorial under lattice rotations; the
pi-flux sector (staggered-fermion hopping) is rotation-symmetric.
