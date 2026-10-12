# Independent reconstruction of the public Sun estimator

The independently written second-stage port reproduces the published rounded numerals **0.66 +/- 0.61**. It does not establish a dimensionally valid acceleration measurement from the public script. In that script, `m` starts as a mass in kg, is overwritten by a nearest-time residual in days, and is then used in the acceleration and Eotvos normalization. A known injected Sun-template acceleration is also attenuated by the data processing. Neither replacing `m` nor dividing by an injection gain supplies a corrected experimental result: the native MATLAB execution, original first-stage state, raw data, and an adequate uncertainty model remain unverified.

This is an independent source reconstruction, not an audit-status change or a claim of new physics. No composition-worker numerical results were read until the local code/results freeze at 2026-10-12T17:31:04Z. The paper summary was known. While locating inputs, a grep of the composition worker's script exposed qualitative comments about `m`, percentile conventions, and endpoint alignment. The present work therefore does not claim blindness to those possible issues. The complete original MATLAB source was then read and the mapping below derived before loading the fit arrays. The protocol is [FROZEN_RECONSTRUCTION.md](FROZEN_RECONSTRUCTION.md); the before-comparison hashes are in [V1_INDEPENDENT_RESULTS_FREEZE.json](V1_INDEPENDENT_RESULTS_FREEZE.json).

## Exact source and data scope

The upstream source is [EotWash/EP-Analysis-Sun, commit 1e103b78b5c3f2d948a30da4f1e7301c6b6f83f5](https://github.com/EotWash/EP-Analysis-Sun/tree/1e103b78b5c3f2d948a30da4f1e7301c6b6f83f5). The paper is [Ross et al., arXiv:2602.02815v1](https://arxiv.org/abs/2602.02815v1), not an unspecified current revision.

| Input | SHA256 |
|---|---|
| `NewWashMultiRunSun.m` | `e37298004871bb9849cd6c188bea060a29e00e1fa8595560ae0b6b4080a33fd3` |
| `Fits/NewWashAnalysis.m` | `dc0422a74dcb044c0adda1335eafaaefa4a13abba09aeeba533b9440df3d16cd` |
| `Basis Functions/sunVect.py` | `6efb8fafc2ddaa7c060269745516950ed51e4b3aec64af6896fb639d9aeb4f61` |
| `Basis Functions/sunVectMin.out` | `064184d2215c5983967f4c8385319f68b1f989638e14245a0441f046443160bc` |
| paper PDF v1 | `3bbd4d70dc39b2b28ebd64fdbde7537c034fd9783bfec0252625b2d68480ca84` |

The 25 fit arrays are used in exactly the order declared on source lines 41–47, from run6891 to run6964. Their individual SHA256 checks, git blob identifiers, URLs, and local paths are included in runtime `independent_results.json`. Every used upstream file was hashed against the input manifest. The extra run6984–6987 arrays were not substituted. The archived solar basis is used without regenerating it: its Astropy version and the local timezone used by `datetime.fromtimestamp` are not pinned by the generator.

The archived fit values are processed torque observations, not independently recovered raw measurements. Calibration constants and the Sun basis are imported. The original cuts select the estimator's input; they were not optimized for a scalar-force model. The known paper result is a reproduction target, not a blind prediction. Synthetic injections test specified response maps, not the truth of a new force or the false-positive rate of a discovery statistic.

## What the code estimates

Let `v=C+iS` denote the archived cosine/sine amplitudes after the thermal cut. The first-stage source constructs a torque series as `kappa*lsim(filt,theta,tim)` (line 63), then fits real sine/cosine columns to that series (lines 113–152). Its saved `C`, `S`, and residual `U` consequently have torque units, N m, conditional on that stage's calibration and time conventions. The second-stage `thetaCalib` variable is declared but never applied to the saved amplitudes.

Per run, the second-stage code retains `U/thermAmp < 3.77`, where `thermAmp = sqrt(4 k_B T kappa/Q) = 1.0023215469e-17 N m`. The comment calls this a chi-squared cut; the implemented quantity is a residual standard-deviation ratio. Each run's surviving C and S vectors is detrended against **sample index**, separately. The joint strict 5th/95th percentile cuts on both components follow. Neither the literal ratio nor the two simultaneous 90% marginal intervals should be silently replaced by a textbook chi-squared or 95% confidence procedure.

The source's tropical-year modulo, flip schedule, inferred sample rate, and daylight-saving expression are kept. All four daylight-saving comparisons act on the same old time array. The corrected complex torque is

\[
 z_j=\frac{e^{i53.69\pi/180}}{0.9958}P_jv_j.
\]

In a selected two-day block B, define the column Sun template `x = inSun + i*outSun`, and the centered data column `y=M_B z`, with `M_B=I-11^T/n_B`. The actual MATLAB `y` variable is a row. Thus the apostrophe in `y'` **conjugates** it. Source line 175 computes

\[
 \hat a_B=\frac{x_B^\dagger\overline{y_B}}{x_B^\dagger x_B},
 \qquad \widehat y_B=\overline{\hat a_Bx_B}.
\]

This is a well-defined two-real-parameter least-squares fit to `y ≈ conjugate(a*x)`. It is not a fit to `y ≈ a*x`. The real design columns are `[Re x; -Im x]` and `[-Im x; -Re x]`. An independent real least-squares evaluation agrees with every complex coefficient to the script's numerical check tolerance. Conjugation itself is not established here to be a physical sign error: the basis/turntable orientation can support this convention. Absolute encoder phase and dipole orientation require the original calibration.

The final torque estimator and its displayed statistical uncertainty are

\[
 \bar a_R=\frac1{N_B}\sum_B\Re\hat a_B,
 \quad s_R=\frac{\operatorname{std}_{N_B-1}(\Re\hat a_B)}{\sqrt{N_B}}.
\]

The residual-derived `uSun` is not used to weight the mean. The expression is an unweighted block SEM. It alone does not quantify calibration error, covariance across blocks, template timing error, processing gain uncertainty, or effects of selection.

## The overwritten normalization

Source line 12 sets `m = 38.72e-3/2`, i.e. `m_phys = 0.01936 kg`; line 13 sets `r = 0.01885 m`. Inside every accepted block, line 160 executes

```matlab
[m,minI] = min(abs(timSun-cutSun/24/3600));
```

The time residual is in days. There is no restoration of the physical mass before `ampSun/(r*m)` and `ampSun/(r*m*aSun)` on lines 212–218. This reassignment is a source-level fact independent of the floating-point decimator details. After at least one eligible block, the printed quantity has dimensions `torque/(length*time)` if the overwritten variable's dimensions are respected; it is not an acceleration. Merely attaching `fm/s^2` in a display string does not fix the dimensions. The eta expression similarly is not dimensionless. No conversion from days to kg exists.

The baseline port finishes with a residual numeral **0.0241700709903 days**. Its numerical closeness to the physical mass numeral **0.01936 kg** helps the resulting display look plausible, but is not a unit conversion.

## Reproduction and filter conditions

The port uses Python 3.12.8, NumPy 2.4.1 and SciPy 1.17.0 as recorded in its results. There is no MATLAB or Octave executable on PATH. This is therefore not a native MATLAB replay.

The [MathWorks decimate documentation](https://www.mathworks.com/help/signal/ref/decimate.html), read at R2026b, specifies an initial order-eight Chebyshev-I IIR filter, .05 dB ripple, cutoff .8/q, forward/reverse filtering, endpoint-aligned downsampling, and an automatic order reduction based on cutoff response error. The default [percentile convention](https://www.mathworks.com/help/matlab/ref/prctile.html) uses midpoint plotting positions. These documented algorithms were implemented independently. The exact release used for the paper is unknown.

There are 3,060 archived points, 2,240 after the thermal cut, 1,845 after the amplitude cuts, and 1,837 in the 90 accepted blocks. Sampling from retained points four and five gives 4373.3305974 s, q=72, and a minimum block length of 4.75 samples (hence at least five). The adaptive polynomial-coefficient port rejects orders 8, 7 and 6 under the documented 1e-6 criterion and uses order 5. At order 6 the computed error is 1.6594e-6; numerical platform/implementation details therefore matter.

| Baseline result | In phase | Quadrature |
|---|---:|---:|
| Mean coefficient, N m | 3.0266691185e-19 | 5.4170972737e-20 |
| Block SEM, N m | 2.7966166069e-19 | 2.6988932334e-19 |
| Literal display numeral | 0.6643174571 | 0.1188987677 |
| Literal display SEM numeral | 0.6138236986 | 0.5923745939 |
| **Physical-mass-only diagnostic**, fm/s² | 0.8293698398 | 0.1484396517 |
| Same diagnostic SEM, fm/s² | 0.7663307010 | 0.7395524786 |

The literal first two in-phase display numerals round to the paper's **0.66 +/- 0.61**. This is a successful numerical reproduction at the paper's quoted precision under the stated port. The physical-mass-only line is a diagnostic of one normalization substitution, **not a corrected measurement or a confidence bound**. The paper's good-day accounting and 95% bound construction have not been independently reconstructed here.

Prespecified numerical controls are revealing. Stable second-order sections at order 5 give physical-mass diagnostics 0.8293698594 +/- 0.7663307167 and literal numerals 0.6645820034 +/- 0.6140681353. Changing only first/last alignment gives 0.645522 +/- 0.596193 in literal numerals. Stable even orders 6 and 8 give strongly different coefficients. An even-order .05 dB Chebyshev filter has nonunit DC gain, and the forward/reverse gain is `10^(-.05/10)=.9885530947`; applying it to the **absolute time coordinate** scales the time axis. At several hundred days this is a multi-day change. The controls were not selected to improve agreement. They establish why the actual MATLAB filter path and time-array outputs are needed before empirical reuse.

After the independent results were frozen, the composition worker reported its own frozen SOS5 values. They agree with this worker's SOS5 control and fixed-selection injection to the shown precision. Both ports use SciPy, so this is independent implementation agreement, not an independent native-library validation.

## Known-signal transfer

For a declared Sun-directed differential acceleration A in the source's own orientation/calibration convention, the midpoint amplitude map is

\[
 z_j^{\rm signal}=r m_{\rm phys} A\,\overline{x_j},
 \qquad
 \delta v_j=\frac{r m_{\rm phys} A\,\overline{x_j}}
 {e^{i53.69\pi/180}P_j/0.9958}.
\]

The first equation is the source's explicit model with a real Sun coefficient, expressed in torque units. It is not an independently demonstrated map from the unavailable raw TDMS channels. The source basis geometry is `x=-cos(alt)[sin(az+theta_d)+i cos(az+theta_d)]`, `theta_d=-23 degrees`; the physical phase assignment remains conditional on the apparatus convention.

If only the block centering is applied, a perfect matched signal returns

\[
 \hat a_B=r m_{\rm phys}A\,g_B,
 \quad g_B=\frac{x_B^\dagger M_Bx_B}{x_B^\dagger x_B}
 =1-\frac{n_B|\bar x_B|^2}{\sum_j|x_j|^2}\in[0,1].
\]

This exact projection identity explains attenuation without a noise assumption. The numerical mean g is **0.8374374978**, ranging from **0.1594283142 to 0.9996991823** over accepted blocks. The uncentered denominator retains an offset that was removed from the data. Centering both model and data would define another estimator; it is not silently substituted here.

For the full second-stage probe, A=+/-1e-15 m/s² is injected into each archived C+iS amplitude before run detrending. Misfit values are held fixed; the original cuts, flip/phase calibration, block centering and fits follow. With nominal selection/rate/basis/block definitions fixed, both signs return the same linear response:

| Injection map / selection | Response in physical-mass diagnostic units per 1 fm/s², real + i imag |
|---|---:|
| Matched decimated template, fixed selection | 0.8299200071 + i 0.0005261075 |
| Archived minute template, fixed selection | 0.8313458946 - i 0.0066258991 |
| Matched template, amplitude cuts rerun, + injection | 0.5951938795 - i 0.0401515525 |
| Matched template, amplitude cuts rerun, - injection | 0.6956818812 + i 0.0289541076 |

For the negative injection the table is `(output(-A)-output(0))/(-A)`, so the signs are comparable. Dynamic recuts change ten and seven selection entries respectively; 90 blocks remain. The first sampled interval and q remain unchanged, as explicitly checked. These are finite-injection responses in this particular archived noise realization. Their asymmetry is not an uncertainty estimate or a universal small-signal transfer function.

The original literal display responds by only **0.6647581359** to the fixed-selection matched 1 fm/s² injection, because it subsequently uses the time-residual numeral in place of the physical mass. Its dynamic-cut responses are 0.4767447109 and 0.5572346571. These are display numerals, not valid recovered accelerations. No single response division repairs the complete estimator: selection is nonlinear, the signal template/first-stage map is conditional, and noise/systematic propagation has not been supplied.

## Limits and the next decisive check

The archived first-stage script currently names run6987/FitsN, while the second stage consumes older Fits files. It also has a different torsional frequency/Q, an earlier calibration value, and a commented turntable-frequency change. The exact executed first-stage revisions for the 25 inputs are not archived as per-run provenance here. The apparent `tim=(startIndex:endIndex)*sampF` assignment needs its actual sample-rate context; it is not corrected or asserted to invalidate the archived inputs. The external helper functions, raw TDMS channels, encoder phase, and original environment are not reconstructed. An amplitude-level injection cannot determine which raw-time residuals would pass the first-stage quality cut.

The next decisive action is a **native replay of the pinned source in the paper's exact MATLAB/Signal Processing Toolbox release**, recording `version`, toolbox versions, `sampF`, q, the decimated time/basis arrays, coefficient vectors, and `m` immediately before lines 212–218. A known real Sun-template injection should then be propagated both at the archived-amplitude level and, once the original raw data/calibration are available, before the first-stage filtering and fits. Run both fixed-selection and fully repeated-selection variants. The physical-mass variable must be tracked separately from the time residual, and any revised estimator's calibration, transfer, covariance, systematics and confidence procedure documented. Only that additional evidence can support a corrected experimental inference. This note supplies neither a new constraint nor an allegation about unpublished processing.

## Reproduction

From the campaign worktree, with the archived input paths present:

```bash
python3 .claude/science/physics-loops/observations-to-toe-24h-20261012/agents/neutrino/ross_independent/reconstruct_sun.py
```

The runner uses one numerical thread, checks stop/deadline markers, verifies hashes, and writes only to runtime `neutrino/ross_independent/`. Its run took about 1.1 s for computation on this machine. `independent_results.json` contains receipts and all controls; `baseline_blocks.csv` exposes every fitted coefficient and projection gain; `run.log` records the checks. It verifies complex/real least-squares equivalence, the exact matched-signal projection, exhaustive nearest-index agreement, and positive/negative fixed-selection linearity. Frozen result files should be copied to a new version before another deliberate run if preserving this receipt is required.
