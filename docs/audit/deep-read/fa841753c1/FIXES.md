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

## Note 1634

- Path: `docs/QUARK_ROUTE2_RHOE_FLOOR_FAMILY_SIZE_PARAMETRIZED_LADDER_NOTE_2026-07-02.md`
- Defect: Section 6 still offers a derivation of why the size-15 smooth floor value is the physically selected one. The note's own corrigendum says that selection path was wrong.
- Evidence: The 2026-09-30 corrigendum says section 6 offers that path, and that a size-15 selection argument would have no centre-minus-shell value to explain. Section 6 still ends by opening "an independent derivation of why the size-15 smooth floor value is the physically selected one." The spline account in the corrigendum is already the note's correction. This row is only the leftover sentence.
- Edit: Drop that selection path from section 6. Keep the corrigendum and the runner-output tables.
- How this row was made: parent check on 2026-11-09 of the same leftover pattern as note 1635. This note was not in the five-card draw. The runner was not executed.

## Note 1635

- Path: `docs/QUARK_ROUTE2_HONEST_GRAVITY_METRIC_RHOE_CHARACTERIZATION_NOTE_2026-07-02.md`
- Defect: Section 7 still calls `rho_E(15) = +5.257476782081e+00` the sharpened target. The note's own corrigendum says that value is not a target.
- Evidence: The 2026-09-30 corrigendum says section 7's sharpened-target sentence was wrong, and the corrected statement is that `rho_E(15) = 5.2575` is not a target. Section 7 still prints that the value "remains the sharpened target for any future E-center derivation path." The 2026-10-04 quantifier limits the all-site identity and the phrase "does not converge." It does not withdraw the target sentence. The ladder quotients were recomputed from the printed gammas and match the displayed cells to display rounding.
- Edit: Rewrite section 7 so it does not call that value the sharpened target. Keep the corrigendum.
- How this row was made: blind re-read on 2026-11-09, then a parent check. The reader treated the corrigendum as enough. The parent filed the sentence that is still printed. The runner was not executed.

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

## Note 1737

- Path: `docs/QUARK_CP_SMALL_CORRECTION_BOUNDARY_NOTE_2026-06-17.md`
- Defect: The note calls `|xi_u| / |c13_u(base)| = 101.908728437` and `|xi_d| / |c13_d(base)| = 6.643337509` the exact ratios of the printed components. Those equalities are false for the printed digits.
- Evidence: With `xi_u = +0.340735147 - 0.063202935 i` and `c13_u(base) = 3.400565729750e-03`, the modulus ratio is `101.908728360781…`. With `xi_d = +0.078186196 + 0.108371050 i` and `c13_d(base) = 2.011510840850e-02`, the modulus ratio is `6.643337541498…`. The completed-slot shares do match the printed `0.990442514` and `0.913327261`. The small-correction no-go is the note's own claim: the body already says the shipped fit is outside caps `R <= 1` and `R <= 5`. That claim is not this repair.
- Edit: Do not present the printed components and those two ratio decimals as one exact equality. Print the ratio of the printed components, or say the displayed ratios come from a finer runner state. Leave the negative small-correction claim in place.
- How this row was made: blind re-read on 2026-11-09. The reader saw the gap and did not file it. The parent recomputed the moduli from the printed components. The runner was not executed. An earlier row that told a later editor to stop calling the fit a small correction was removed, because the note already says that.

## Note 2322

- Path: `docs/PMNS_TM2_MAGIC_RESIDUAL_DYNAMICAL_GENERATOR_NARROW_THEOREM_NOTE_2026-06-05.md`
- Defect: Theorem item 4 still says a `V_4`-invariant `M_nu` leaves `theta_13` free because the `C_3`-doublet block is unconstrained. The note's own corrigendum says that sentence is false.
- Evidence: The 2026-09-30 corrigendum says item 4 keeps the trimaximal column and maximal atmospheric mixing, and also forces `theta_13 = 0`. Item 4 still prints `theta_13` free and the doublet unconstrained. The later restatement `(4)` says the same: the doublet block is unconstrained, so its eigenvectors carry a free `theta_13`.
- Edit: Replace both statements with the corrigendum's item 4. Keep the corrigendum.
- How this row was made: corrigendum scan on 2026-11-10. The rest of the note was not read. The runner was not executed.

## Note 3494

- Path: `docs/QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md`
- Defect: Section 3 still says the `+0.20%` mixed-scale match "is real bounded support." The note's own corrigendum withdraws that phrase.
- Evidence: The 2026-09-30 corrigendum says the `+0.20%` is a convention coincidence and withdraws "real bounded support" in Section 3. Section 3 still ends with that sentence after printing `R_pred/R_self - 1 = +0.20%`.
- Edit: Delete that sentence. Keep the corrigendum's common-scale miss.
- How this row was made: corrigendum scan on 2026-11-10. The rest of the note was not read. The runner was not executed.

## Note 3548

- Path: `docs/QUARK_MASS_RATIOS_TASTE_STAIRCASE_SUPPORT_NOTE_2026-04-25.md`
- Defect: Section 4 still reports `m_s/m_b` at `+0.20%` and `m_d/m_b` at `+3.51%` as the reproduced match. The note's own corrigendum withdraws those entries as agreement.
- Evidence: The 2026-09-30 corrigendum says those two mixed-scale entries are a convention coincidence. The Section 4 table still prints them as the deviations, and the following sentence says the mass-ratio comparators are reproduced to `+3.3%` and `+0.2%` on the threshold-local convention.
- Edit: Do not present those two rows as agreement. Keep `m_d/m_s` at `+3.30%`, which the corrigendum says still stands.
- How this row was made: corrigendum scan on 2026-11-10. The rest of the note was not read. The runner was not executed.

## Note 3821

- Path: `docs/YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md`
- Defect: Section 5.4 still says the CKM-dual `m_s/m_b` prediction matches the threshold-local ratio to `+0.2%`. The note's own corrigendum says that is not a success.
- Evidence: The 2026-09-30 corrigendum names that sentence and says the common-scale comparison misses by `+18.6% ± 1.2%`. Section 5.4 still prints the `+0.2%` match.
- Edit: Delete the `+0.2%` success sentence from Section 5.4. Keep the statement that the dual note does not close the absolute `m_b` scale.
- How this row was made: corrigendum scan on 2026-11-10. The rest of the note was not read. The runner was not executed.

## Note 4204

- Path: `docs/UP_TYPE_MASS_RATIO_CKM_INVERSION_NOTE.md`
- Defect: The observation-comparator section still prints `f_23 = 0.9983` and says the Phase 1 bridge saturates `|V_cb|^2` to within `0.2%`. The note's own corrigendum withdraws both.
- Evidence: The 2026-09-30 corrigendum says the common-scale partition is `f_23 = 0.867`, not `0.9983`, and that the saturation is an artefact of the mixed comparator. Both sentences are still printed as the current numerical reading.
- Edit: Remove `0.9983` and the `0.2%` saturation from the current reading. Keep `f_12 = 0.9839`, which the corrigendum says is unchanged.
- How this row was made: corrigendum scan on 2026-11-10. The rest of the note was not read. The runner was not executed.

## Note 4321

- Path: `docs/STRONG_CP_THETA_ZERO_NOTE.md`
- Defect: The combined runner paragraph still concludes that the runner finds no CKM-to-`theta_eff` leakage. The note's own corrigendum says that conclusion does not follow from `|det V_CKM| = 1`.
- Evidence: The 2026-09-30 corrigendum says `|det V|^2 = 1` for every unitary matrix, so the check cannot see a CKM phase. The paragraph still prints the leakage conclusion. A later pointer says the sentence does not follow. The conclusion is still on the page.
- Edit: Delete the leakage conclusion. Keep the statement that `|det V_CKM| = 1` is a unitarity check.
- How this row was made: corrigendum scan on 2026-11-10. The rest of the note was not read. The runner was not executed.

## Note 4609

- Path: `docs/MASS_SPECTRUM_DERIVED_NOTE.md`
- Defect: The "Retained vs bounded vs conditional" list still calls the down-type chain sub-percent and still lists `m_s/m_b` at `+0.13%` and `m_d/m_b` at `+3.6%` as retained. The note's own corrigendum withdraws those entries and that phrase.
- Evidence: The 2026-09-30 corrigendum says the `+0.13%` uses `m_s(2 GeV)/m_b(m_b)` and withdraws those two entries from the retained list. The list still prints them under "RETAINED (zero-free-parameter, sub-percent or few-percent to observation)."
- Edit: Remove those two entries and the sub-percent wording. Keep `m_d/m_s` at `+3.3%`, which the corrigendum says still stands.
- How this row was made: corrigendum scan on 2026-11-10. The rest of the note was not read. The runner was not executed.

## Note 4836

- Path: `docs/DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md`
- Defect: The scale-qualifier section still says the live comparison surface is the threshold-local self-scale comparator. The note's own corrigendum withdraws that sentence, and it withdraws the `+0.2%` and `+3.5%` rows as agreement.
- Evidence: The 2026-09-30 corrigendum names that sentence and withdraws it. The table above it still prints `m_s/m_b` at `+0.2%` and `m_d/m_b` at `+3.5%`, and the next section still calls that comparator the live surface.
- Edit: Delete the live-surface sentence. Do not present those two deviations as agreement. Keep the `+3.3%` on `m_d/m_s`.
- How this row was made: corrigendum scan on 2026-11-10. The rest of the note was not read. The runner was not executed.

## Note 4887

- Path: `docs/COMPLETE_PREDICTION_CHAIN_2026_04_15.md`
- Defect: Section 11.3 still says the `5/6` bridge gives `V_cb = (m_s/m_b)^{5/6}` to `0.23%` on the threshold-local comparator. The note's own corrigendum says that figure is not evidence for the bridge.
- Evidence: The 2026-09-30 corrigendum names that clause and says the common-scale comparison misses by `+18.6% ± 1.2%`. Section 11.3 still prints the `0.23%` bullet.
- Edit: Replace that bullet with the corrigendum's corrected statement. Leave the clause that full bridge closure remains open.
- How this row was made: corrigendum scan on 2026-11-10. The rest of the note was not read. The runner was not executed.

## Note 4898

- Path: `docs/CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md`
- Defect: The note still calls `+0.20%` the live miss of the `m_s/m_b` bridge, and the scale statement still names the threshold-local comparator as the live comparison surface. The note's own corrigendum says that figure is not a scale-consistent test.
- Evidence: The 2026-09-30 corrigendum says the `+0.20%` compares `m_s(2 GeV)` with `m_b(m_b)`. The body still prints "the bounded bridge misses by only `+0.20%`" and "the live `m_s/m_b` prediction lands at `+0.20%`." The scale statement then lists the threshold-local comparator as the live surface.
- Edit: Do not call `+0.20%` the live miss. State the common-scale comparison from the corrigendum.
- How this row was made: corrigendum scan on 2026-11-10. The rest of the note was not read. The runner was not executed.

## Note 3741

- Path: `docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`
- Defect: The safe statement, section 2, section 3, and the honest endpoint still present the triple `(-1, -2, 21/4)`, the ratio chain `{5/6, -2, -8/9}`, and the section 3 live readout as the theorem target. The note's own corrigendum says those two centre-minus-shell entries are not a property of the field.
- Evidence: The 2026-09-30 corrigendum says the triple, the ratio chain, and the "live endpoint-fixed readout" of section 3 are size-15 cubic-spline outputs, and that a local interpolation gives both centre-minus-shell ratios `0`. The safe statement still says the stack does not derive that triple. Section 2 calls it "the key compression of the theorem target." Section 3 still prints the live endpoint-fixed readout and says those ratios would have to be proved. The honest endpoint still says the missing map entry is `beta_E / alpha_E = 21/4` and that this is the right theorem endpoint.
- Edit: Stop presenting that triple, that chain, and the section 3 live readout as the theorem target. Keep the statement that `rho_E = 0` and `rho_E = 21/4` are both admissible maps on the restricted class, and that a local readout gives `rho_E = 0`.
- How this row was made: corrigendum scan on 2026-11-10. The withdrawn sentences and their later restatements were checked. The runner was not executed.

## Note 3748

- Path: `docs/QUARK_ENDPOINT_READOUT_CONSTRAINTS_NOTE_2026-04-19.md`
- Defect: The safe statement and the "Bounded live relations" section still list `b_T / a_T ~ -1`, `b_E / a_E ~ 5.2575`, and `|b_E / b_T| ~ 2.6216` as live constraints, and the close still calls that pattern stable. The note's own corrigendum says those three numbers are spline artefacts, not constraints on a coefficient law.
- Evidence: The 2026-09-30 corrigendum withdraws those three relations and says a local interpolation gives `b_E = b_T = 0`. The safe statement still prints them under "bounded live relations." The later section calls them useful live constraints, says the `T` channel is already `1 - delta_A1`, and names `r_E` as the unresolved primitive. "What this closes" still says the live ratios show a stable bounded pattern.
- Edit: Remove those three relations from the current endpoint. Do not call the spline pattern a coefficient constraint. Keep `a_T / a_E` only as the corrigendum states it: a shell-only ratio that is not stable. Keep the exact endpoint-fixation algebra and the no-go against an exact coefficient theorem.
- How this row was made: corrigendum scan on 2026-11-10. The withdrawn sentences and their later restatements were checked. The runner was not executed.

## Note 4422

- Path: `docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`
- Defect: The status block and the bottom line still name the readout-map endpoint triple `(-1, -2, 21/4)` as the single open theorem target. The note's own corrigendum withdraws that sentence.
- Evidence: The 2026-09-30 corrigendum says the two centre-minus-shell entries are not a field value to derive, and withdraws the sentence that names the missing triple as the next theorem target. The purpose block still says the coupling theorem is not closed because that triple is not yet derived. The authority role still names it as the single open theorem target. The bottom line still says "The next theorem target is the missing readout-map endpoint triple." The body repeats the same triple as the inherited no-go.
- Edit: Delete those target sentences. Keep the conditional coupling family and the inherited non-uniqueness of `P_R`, including that `rho_E = 0` and `rho_E = 21/4` are both admissible. Do not present `(-1, -2, 21/4)` as a field value still to be derived. The middle entry `alpha_T / alpha_E` stays undecided, as the corrigendum says.
- How this row was made: corrigendum scan on 2026-11-10. The header, the cited-authority block, and the bottom line were checked. The runner was not executed.

## Note 4937

- Path: `docs/BH_ENTROPY_DERIVED_NOTE.md`
- Defect: "Reproduced Finite Results" still says the two-dimensional `1/L` intercept being close to `1/4` is evidence against declaring the finite data inconsistent with `1/4`. The note's own corrigendum says that intercept is not evidence for `1/4`.
- Evidence: The 2026-09-30 corrigendum says the mixed-state intercept `0.2492` is not evidence for the coefficient `1/4`, and that a pure half-filled state does not reach `1/4` under either printed fit. The results section still prints the evidence sentence, then points back at the corrigendum.
- Edit: Delete the sentence that calls closeness to `1/4` evidence against inconsistency. Keep the printed intercept `0.2492` as a runner number, and keep the corrigendum.
- How this row was made: corrigendum scan on 2026-11-10. The corrigendum and the results section were checked. The runner was not executed.
