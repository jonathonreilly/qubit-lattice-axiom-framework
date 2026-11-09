# Fix list

Pin: `fa841753c1a6296e5ad45518375660b0f1004769`

A row appears here only when the note is wrong or overclaims. One finding, one later repair. This file does not change claim status.

## Note 40

- Path: `docs/TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md`
- Defect: The Theorem 7 on-plane display has the wrong isotropic sextic numerator.
- Evidence: On the plane `b0=b1+2b2`, reversion of `cos ω=phi0^T G phi` gives `s^2(4s^4-5s^2+2)|k|^6/360`. The note prints `s^2(8s^4-5s^2+2)|k|^6/360`, which is larger by `s^6/90`. At `s^2=2/3` the series coefficient is `1/1215`; the printed numerator gives `1/243`. The same expansion reproduces the order-four term, the anisotropy `-(s^2/360)|k|^2 sum_a k_a^4`, and `z(b_iso)=sqrt(10)/9-16/45`. The Gram identities `v^T G v=1-s^2`, `w^T G w=s^2`, and `v^T G w=0` hold for the printed `G`.
- Edit: In the Theorem 7 display, replace `8 s^4` by `4 s^4`. Keep the anisotropy term and `z(b_iso)`.
- How this row was made: read on 2026-11-09. The series was recomputed from the printed Gram matrix. The runner was not executed.

## Note 46

- Path: `docs/SCALAR_KINETIC_RESPONSE_NOTE_2026-10-16.md`
- Defect: The eigenbasis disclaimer calls `n=11/10` a repeated root.
- Evidence: The note says “not a claim of a complete eigenbasis at repeated roots (n=97/98 or 11/10)”. The quadratic `(2n-1)m(2m+7)+6=0` has discriminant `(2n-1)[49(2n-1)-48]`. For `n>1/2` the only double root is `n=97/98`, at `m=-7/4`. At `n=11/10` the discriminant is `324/25` and the roots are the distinct values `m=-5/2` and `m=-1`. The mode `m=-5/2` is also one of the two common modes with `Xi=0`.
- Edit: Keep `n=97/98` as the repeated root. Describe `n=11/10` as the overlap of the root `m=-5/2` with that `Xi=0` mode. Leave the excluded denominator `m=-4` as it stands.
- How this row was made: read on 2026-11-09. The discriminant and both roots were recomputed from the printed quadratic. The runner was not executed.

## Note 61

- Path: `docs/INTERACTING_PREPARATION_CONTROL_WORK_BOUNDED_THEOREM_NOTE_2026-10-16.md`
- Defect: The ramp-integration sentence says the finest successive differences have observed ratios near four.
- Evidence: With 256, 512, and 1024 slices, the note prints those differences as `1.664×10^{-8}` and `4.371×10^{-8}`. Their ratio is `4371/1664 = 2.6268…`. Moving either printed mantissa by one in the last digit leaves the ratio near `2.63`.
- Edit: State that ratio, about `2.627`. Do not call it near four. Keep the next sentence, which already says these observations are not rigorous ODE enclosures.
- How this row was made: read on 2026-11-09. The ratio was divided from the printed digits. The runner was not executed.

## Note 65

- Path: `docs/COMMUTING_STATIC_EDGE_FIXED_TARGET_BOUNDED_THEOREM_NOTE_2026-10-16.md`
- Defect: The qualifications sentence joins two UTC stamps to an elapsed time they do not equal.
- Evidence: It says the attempt ran from `20:43:34.657018` to `20:43:34.842313` UTC, elapsed `0.18528820807114244` seconds. The stamps differ by `0.185295` seconds, which is `6.792` microseconds more than the printed elapsed time. That gap is larger than the microsecond resolution of the stamps. The earlier sentence that reports the same elapsed time is a timer reading and is not joined to the stamps.
- Edit: Do not present those stamps and that elapsed time as one interval. The stamps differ by `0.185295` seconds. Leave the earlier timer reading unless both values are recomputed from one clock.
- How this row was made: read on 2026-11-09. The stamp difference was subtracted from the printed digits. The runner was not executed.

## Note 1696

- Path: `docs/GRAVITY_SIGN_IS_NOT_A_NEW_ADMISSION_REDUCES_TO_SHARED_ORIENTATION_DATUM_KCPT_CANNOT_SELECT_NARROW_THEOREM_NOTE_2026-06-18.md`
- Defect: The note says `e₄`-conjugation fixes every even-grade blade. The chirality element `ε ∝ e₁e₂e₃e₄` has even grade, and the note's own identity is `e₄ ε e₄⁻¹ = −ε`.
- Evidence: Conjugation by a unit vector that lies inside a blade does not obey the orthogonal grade-parity rule. For `ε = e₁e₂e₃e₄` and `e₄⁻¹ = s e₄` with `s = e₄² = ±1`, the product is `−ε`. The two displayed identities can stand. The parenthetical cannot.
- Edit: Delete the claim that `e₄`-conjugation fixes every even-grade blade. Keep the two displayed identities.
- How this row was made: blind re-read on 2026-11-09. The prior card did not record this defect. It recorded a Type-label mismatch.

## Note 1711

- Path: `docs/DM_LIVE_CONSTANTS_CANONICAL_EDGE_CERTIFICATE_NOTE_2026-06-18.md`
- Defect: The printed quotient `5.447934280745940` is the binary64 value of the displayed expression. It is not the exact value of those printed decimals.
- Evidence: `0.268 / ((3.6515e-3 * 6.12) / 0.674^2) = 454276/83385 = 5.44793428074593752…`, which rounds to `5.447934280745938`. The same expression in binary64 prints `5.447934280745940`. The alpha-edge decimals in the same note do match binary64.
- Edit: Print the exact fraction `454276/83385`, or say the displayed quotient is the binary64 value.
- How this row was made: blind re-read on 2026-11-09. The prior card said the inputs give the printed quotient.

## Note 1716

- Path: `docs/ALPHA_S_SOMMER_STATIC_POTENTIAL_ROOT_KERNEL_THEOREM_NOTE_2026-06-18.md`
- Defect: The title names `alpha_s`. The proved object is the dimensionless Sommer root for a supplied Cornell potential and the supplied target 1.65.
- Evidence: The prior read checked the printed identity `F(r0) r0^2 = sigma (r0/a)^2 + e` against the printed `sigma`, `e`, and `r0/a`, and found it holds at binary rounding. The same read says the 0.5 fm anchor is not an input to `r0/a`, and the note does not derive the physical fm scale, QCD running, or `alpha_s(M_Z)`.
- Edit: Change the title and the claim so they do not present that dimensionless root as `alpha_s`.
- How this row was made: extracted from the prior card. The note was not re-read in this pass.

## Note 1737

- Path: `docs/QUARK_CP_SMALL_CORRECTION_BOUNDARY_NOTE_2026-06-17.md`
- Defect: The shipped complex 1-3 carriers are not a small correction to the Schur base. Caps at 1, 2, and 5 exclude the shipped fit.
- Evidence: On the printed digits, `|xi_u| / |c13_u(base)|` agrees with 101.908728437 and `|xi_d| / |c13_d(base)|` agrees with 6.643337509. Relative square error is below 1e-8. Both ratios sit above 5. Printed inputs: `xi_u = +0.340735147 - 0.063202935 i`, `xi_d = +0.078186196 + 0.108371050 i`, `c13_u(base) = 3.400565729750e-03`, `c13_d(base) = 2.011510840850e-02`.
- Edit: Stop calling the shipped fit a small correction inside those caps. State the ratios and that the caps exclude it.
- How this row was made: extracted from the prior read. The ratio check was repeated. The rest of the note was not re-read in this pass.
