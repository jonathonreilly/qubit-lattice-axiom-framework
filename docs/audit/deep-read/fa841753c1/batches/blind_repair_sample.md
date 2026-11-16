## Note 1683
- Path: `docs/RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md`
- Result: no fix
- Checked: `U_cc(θ)` factors as `P_0⊗exp(-iθσ_x)+P_1⊗exp(+iθσ_x)`; at `θ=π/4` the overlap is `<0|exp(iπ σ_x/2)|0>=cos(π/2)=0`; the calibrated blocks are `K_r=P_r`.
- Finding: The finite controlled-copy arithmetic is correct, and the note already confines the result to that model without claiming an audit verdict.
- Open: none

## Note 1684
- Path: `docs/P_LH_NCG_PRIMITIVE_UNDERDETERMINATION_BOUNDARY_NOTE_2026-06-18.md`
- Result: no fix
- Checked: `ρ_+` and `ρ_-` agree on bivectors and disagree in sign on `γ_1γ_2γ_3`; a 4-dimensional block is not a multiple of 3; both `J=K` and `J=SK` square to `+1`, and only `SK` anticommutes with chirality; `D=0` makes the order-one double commutator vanish.
- Finding: This is a correct no-go. The note says the baseline does not select the NCG packet, and it does not claim that packet is derived.
- Open: none

## Note 1685
- Path: `docs/POISSON_SELF_FIELD_SUPPLIED_BRANCH_CORE_BOUNDED_NOTE_2026-06-18.md`
- Result: no fix
- Checked: `eff_s = s/(|layer*H-x_src|+0.1)*H*H` is a supplied definition. The printed residual, `F~M`, and Born figures are runner reports with no further digit-to-digit derivation. `PASS=18` is not treated as an audit pass.
- Finding: The note keeps the Poisson data, readout, and gravity reading supplied or unclaimed. Nothing on the page is a false finite identity.
- Open: none

## Note 1696
- Path: `docs/GRAVITY_SIGN_IS_NOT_A_NEW_ADMISSION_REDUCES_TO_SHARED_ORIENTATION_DATUM_KCPT_CANNOT_SELECT_NARROW_THEOREM_NOTE_2026-06-18.md`
- Result: fix
- Checked: `e_4(e_1e_2e_3)e_4^{-1}=(-1)^3 e_1e_2e_3` and, for `ε∝e_1e_2e_3e_4`, `e_4 ε e_4^{-1}=-ε`. Grade of `ε` is 4. Also `σ_xσ_yσ_z=i I_2`, `dim su(3)=8` on a 3-dimensional space, and `A(3̄)=-A(3)`.
- Finding: The two conjugation identities are true, but the claim that `e_4`-conjugation fixes every even-grade blade is false. `ε` is even grade and the note’s own second identity sends it to `-ε`.
- Edit: Rewrite the §1 parenthetical. Spatial `k`-blades orthogonal to `e_4` pick up `(-1)^k`; that rule does not cover `ε`, because `e_4` lies in the blade. Keep both displayed identities.
- Open: the gravity-specific `χ_η` identification remains the cited bridge this note already does not derive.

## Note 1711
- Path: `docs/DM_LIVE_CONSTANTS_CANONICAL_EDGE_CERTIFICATE_NOTE_2026-06-18.md`
- Result: fix
- Checked: `0.5934^{1/4}`, `1/(4π)`, `α_bare/u_0`, and `α_bare/u_0^2` match the printed 15 digits after ordinary rounding. With the printed rationals, `0.268/((3.6515e-3*(6.12e-10/1e-10))/0.674^2)=454276/83385=5.44793428074593752…`, which rounds to `5.447934280745938`, not the printed `5.447934280745940`.
- Finding: The alpha edge matches. The eta/Omega ratio does not: the printed tail is the binary64 value of that expression, not the value of the printed rationals.
- Edit: Replace `5.447934280745940` with `5.447934280745938`, or print the exact fraction `454276/83385`.
- Open: none
