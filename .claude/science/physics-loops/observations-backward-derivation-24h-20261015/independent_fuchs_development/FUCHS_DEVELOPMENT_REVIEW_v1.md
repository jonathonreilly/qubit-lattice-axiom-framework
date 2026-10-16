# Focused Fuchs development check, v1

The selected-file parser and the scoped weak-regression calculation agree with the retained author evidence. No concrete implementation discrepancy was found on the checked inputs. The original v1 prose needed the two qualifications now present in v2: equation (4) has calibration force off, and full column rank does not establish consistency. This report confirms those narrow clarifications while preserving the v1 source bindings of the computations.

This is an independent data/implementation check, not a physical apparatus identification, empirical validation, formal audit or publication approval. Root retains authorship. Only the one selected development array was opened; none of the seven other arrays was opened, hashed or downloaded. The new complex-probe extension and plan were not read or tested.

## Exposure and scope

The six requested plan/receipt/schema/primary-review/math documents were read completely. Independent parsing and mathematical design were frozen at 2026-10-16T08:14:05.489869Z, before any raw-file access. The first 21 header lines and first five numeric rows then established the delimiter and explicit units before freezing the implementation. The complete independently produced source/results were frozen at 08:17:23.668315Z, before reading the author runner, helper, synthetic checker or results. The existing schema was known beforehand, so this is a distinct raw extraction, not blind discovery of the expected schema.

The independent run completed 44 controls with zero failures in 1.4942 seconds, with bytecode disabled and a 120-second cap. Source SHA-256: `0505f57367a8df2b3bb51667bcea78bb5ce951151c5c6685257135661fd966b2`; results SHA-256: `ce998478a74b2a5434dcfb9bd2395f80fa29a77c4c969d08ea1e125670745d6b`. All parsing metadata, raw-token and float-array digests, exact-model cases, window features and regression outputs are retained.

## Independent parsing and metadata

The selected trace has 21,579,572 bytes, MD5 `934a03d9632ba78e8d06f668717ec4fa` and SHA-256 `6caefb32f687e479d832a28ffa18a2125484acc3783ee12d42e602e15f1d9c67`, matching the acquisition receipt, access plan and deposited metadata. The local Zenodo metadata SHA-256 is `291a53a661e6fb08469de7056a01378ed7c373ce6bdc8111a7b036c90ea57620`; its selected file record and eight-entry inventory match the frozen plan. Reading that metadata did not open the seven other arrays. Plan and derivation cross-hashes were also checked.

A separate line parser retained the percent-comment headers and parsed all 678,861 two-column semicolon records without dropping rows or nonfinite values. Eight strict timestamp resets occur at data-row indices 75,429, 150,858, 226,287, 301,716, 377,145, 452,574, 528,003 and 603,432. They give nine streams of 75,429 samples. Stream boundaries were discovered from resets rather than imposed by reshaping.

Header order is three R streams, three Theta streams and three frequency streams. The headers explicitly specify seconds, volts, degrees and hertz. Each stream runs from -21467.8260005 to 0 seconds. Every timestamp token is identical across all nine streams, a stronger check than equality after floating conversion. Exact decimal increments range from 0.2846134 to 0.28461353 seconds and are strictly positive within streams. Every scalar statistic in the supplied intake matches the independent parser.

The recorded frequency fields are constant: demod1 is 15.8871013411 Hz, while demod2 and demod3 both contain 26.6992697817 Hz. This establishes correspondence of the archived fields, not receiver/source wiring, physical rotor phase, calibration, support motion or filter identity. R exp(i Theta*pi/180) respects the declared units; no phase unwrap or amplitude cut is used for the independent regression. The low source amplitude region remains included.

## Independent mathematics and one regression case

The two harmonic mechanical equations give Dq-m omega^2 X=m g_t+f and PX-Zq=M g_p+f_p-f. Eliminating X gives the stated numerator and determinant. The internal calibration coefficient is (P-m omega^2)/Delta, so the equivalent-force formula requires both the determinant and calibration numerator to be nonzero. Uniform free-support acceleration cancels the particular relative response; it does not remove homogeneous motion or establish the real support model.

Twice integrating by parts gives E-(gamma+2iOmega)D+(omega0^2-Omega^2+i gamma Omega)C=2iOmega bU. Division by 2iOmega yields R=aB+i nu C+bU with the displayed signs and factors. The compact endpoint conditions remove these boundary terms, not instrument transients or missing physical inputs. Rank four gives at most one consistent solution, or a unique least-squares estimate; it does not show that the model is consistent.

A distinct synthetic model used Omega=4, gamma=.12, nu=.08 and b=.8+.3i, three forced exponential components, and two different pairs of homogeneous amplitudes including both homogeneous roots. Adaptive quadrature over six independently selected windows gave weak residuals at most 2.51e-14 and parameter errors at most 5.40e-15. A monochromatic proportional-channel example independently demonstrated rank at most two. No experimental initial state was selected.

The independent real-record calculation was deliberately limited to the predeclared receiver2/source3, unit-phasor, 1200-second exact-model case. All 17 complete nominal windows were retained; 11 were used in the chronological fit and six evaluated with unchanged coefficients. The omitted final nominal duration is 1067.8260005 seconds; time after the last used sample is 1067.8697984 seconds. These are different bookkeeping quantities, both retained.

For each window, four-point Gauss-Legendre integration exactly integrates the piecewise-linear sampled envelope against the degree-six window polynomial, up to floating arithmetic. This is a separate interpolation/quadrature convention, not a certified description of the true between-sample signal. A separately computed trapezoidal version matches the frozen author convention. Its all-window coefficient vector (a,nu,Re b,Im b) is:

`[-7.582583004391661e-6, 1.0103362513708777e-5, -1.4587277973809897e-7, -1.2439104489886606e-7]`.

The largest difference from the author's coefficients is 1.15e-19; the chronological coefficient difference is at most 2.33e-19. All 68 complex window features agree within 1.73e-15 per real/imaginary component. Switching to exact piecewise-linear quadrature changes the all-window coefficients by at most 2.71e-13, and the chronological coefficients by at most 4.19e-13. These differences do not bound measurement or model error. The relative all-window RMS residual remains 0.757259; the later development ratio is 0.861485. Those substantial residuals are preserved, not converted into a calibrated rejection or erased by agreement between implementations.

## Post-exposure correspondence and limits

The complete author development runner, helper and synthetic checker were read. Their weak columns, real/imaginary stacking, normalization, temporal train indices and thinning endpoint handling implement the stated v1 plan. The author uses a closed nominal endpoint while the independent parser used a half-open endpoint; the actual selected indices are identical in the checked case. The records' inferred-mode and validation-named output fields remain conditional numerical/development outputs, not measured precision or an empirical holdout.

Unchanged author replays, each bytecode-disabled under 120 seconds, produced:

- Synthetic checker: 25 passed, 0 failed, exit 0 in 0.4432 seconds; full output byte-identical to SHA-256 `bdd95321cbfbc14450897fb8106ecf4db683a66c647f7f25f39a4204ea844668`.
- Development runner: all 24 frozen cases, exit 0 in 0.6967 seconds; full output byte-identical to SHA-256 `84c6481edd29c155eb07ab854bd4ff879a69c664b5a180b1e6435e9e6fda1351`.
- Narrow correspondence: 21 passed, 0 failed, source bytes unchanged and both stderr streams empty.

The full 24-case reproduction is not described as 24 independent implementations: independent numerical regression covered one exact-model case, plus the distinct synthetic model. Parser verification covered every selected-file sample and all nine streams. NumPy least-squares library independence is not claimed.

The exact v1-to-v2 note diff was inspected. V2 SHA-256 `87c88650707c10c204a106a86749a9fa42d037ee670e4d1093caa75895538d51` correctly adds f=0 to equation (4) and separates consistency from uniqueness; no numerical source changes accompany that clarification. Original computation hashes still correctly identify the v1 note. The new complex-probe route lies outside this review.

The author intake's NumPy-int64 serialization failure and primary-review PDF parser warning remain disclosed in their original receipts. The first display of the large synthetic output was truncated by the tool display budget; original bytes and exact replay remained complete. No independent scientific execution failed, and no tolerance was relaxed. Primary publication reading/rendering was not repeated here; its stated scope remains attributed to the author's receipt.

Final surviving premises include the physical wiring and force phase map, relative calibration and reaction path, carrier/envelope interpretation, lock-in filters and their initial histories, linear constant-coefficient applicability, support acceleration, unresolved modes and measurement covariance. Neither small quadrature changes nor normalized condition near unity supplies these premises. No force, scalar parameter, potential, action, physical channel identity or empirical validity is established by this focused check.
