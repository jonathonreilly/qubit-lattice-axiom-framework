# Repo search

Codex, row 956 (requested gpt-6-astra xhigh), 2026-11-14; checkout `d8db8ac22c0981baf7d10e71df03323fe6b930e7`. Research check, not an audit; grants no status.

Searched `/Users/jonreilly/Projects/Physics` on `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, and `pr/10141`, using bounded `git grep -n -i -E ... -- '*.md' '*.tex' | head` commands. The completed exact-target search, `LSI-J|BR-J|two.slice.*Poincar|gap-lsij-scale|bridge.marginal`, returned no hits. Broader searches used `finite-cylinder`, `hypercontract`, `log.Sobolev`, `Poincar.{0,50}(vacuum|two.slice|Wilson)`, and `ground.state.transform`. These reached their caps; they are locators, not absence evidence.

Relevant hits, read at source:

| Ref and file | Exact statement relevant here | Closeness |
|---|---|---|
| `origin/main:research/mass-gap/library/gap-skeleton-max-b.md:232–239` | For the round unit S^3 metric, `Ric + beta Hess A >= 2-30 beta`; the stated Bakry–Emery consequence is a volume-uniform Wilson Poincare inequality for `beta<1/15`. | Full lattice law at strong coupling, not the two-slice vacuum law at 2.3 or 2.6. No duplicate of this check. |
| `origin/main:research/mass-gap/library/gap-form-exercise.md:91–99,108` | Reports Piazza–Shen's LSI uniform in L for 2D SU(N) Wilson at every beta, using exact block convolution; reports Shen–Zhu–Zhu's strong-coupling LSI range `abs(beta)<1/(16(d-1))` in their convention. | Existing literature record, not a supplier for this 4D two-slice test. No literature theorem is rederived here. |
| `pr/10114` and `pr/10133`, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` | A simple loop has Haar variance 1/4 for SU(2); the local convolution obeys `kbar_B >= (1+v_N/rho)^(-1) |F><F|`. The centered one-step correlation is `<uF,kbar uF>/<u,kbar u>`. | Earlier transfer/loop construction, not an upper bound on R_J or this numerical check. Credit this existing construction; do not redo it. |

Refs resolved to `827f55721da6d44f68339805649e7ca1da598b2e`, `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `89faef229ff6e6bde42baad15ed8270c2f4087d8`, `1e70c7211a2cdbc39001e619f1dd89db45e25851`, and `c73ad7b177d94f89ff37b77386936e3d52b48b05`, respectively. No fetch or remote mutation was used.

The prescribed target prior file is absent. `prior/repo-search-2026-11-08.md` was read whole; its thirteen targets concern earlier RG obligations. Its loop-witness pointer led to the source read above. No `LSI-J`, `BR-J`, `two.slice.*Poincar`, or `gap-lsij-scale` match occurs in `open-registry.md`. Row 947 owns the framework; row 954 owns the test; row 956 owns this check. This report does not attack another row's open inequality.

The outline index was consulted before source reads: README, chunk-01 rows around the scalar Poincare and mass-gap entries, chunk-02 rows around the transfer construction, and their obligations. Searches for `log.Sobolev|hypercontract|LSI-J|two.slice.*Poincar` found no matching statement in those index files. The CA full-read index likewise supplied no matching bridge/LSI entry. This is a bounded search result, not a theorem about every possible formulation in the account.

The cited outline passages actually read were SA 588–599, 687–707, 774–779, and 2315–2335. They give, respectively, the spectral-support requirement for a mass gap; a scalar block Neumann inequality; its explicit exclusion of a physical Hamiltonian gap; and the gauge-projected transfer operator with `Z_s=Tr L^s`. These are existing work by Ethan Sussman and Levent Alpoge, authored with Claude and Codex. None is the present two-slice LSI. The supplied source revision is `31a47c543775`; the on-disk `sa` directory has no Git metadata, so that revision is supplied provenance. No Balaban paper or additional literature theorem is imported.

# Scope and finding

Read `gap-lsij-scale-opus.md` lines 1–303 and all three saved Python files in `guide/lane954/` line by line. Definitions were matched to `gap-lsivac-max.md:80–91`, `gap-fc-max.md:76–101,128–184,489–584`, and check 943's caveat at `gap-lsivac-check-astra.md:154–164`. Existing check 949, `gap-fc-check-astra.md:100–103,188–199`, already checks BR-gap and Lemma J. Those implications are reused, not rechecked as a new research target.

**The free-photon formula and the conditional GAP-R argument hold. The saved SU(2) numbers do not refute a box-uniform LSI or the seed. The statements that the vacuum caveat is handled, that every reported number is a lower bound for R_J, and that the reported correlator floors are established fail as written.** The remaining evidence is a finite-slab GUIDE diagnostic with the limitations below.

# Verdicts per statement

Line numbers in this table refer to `gap-lsij-scale-opus.md` at the pinned checkout. Repeated conclusions in Section 8 and RESULT inherit these verdicts.

| Lines / statement | Verdict | Finding |
|---|---|---|
| 1–36, plan, provenance, chronology | HOLDS AFTER CORRECTION | Treat chronology and lock exclusivity as the author's record. The saved batch log confirms the interrupted shell invocation and completed L=14/L=16 runs. Historical lock acquisition and exclusivity are not independently recorded here. |
| 40–48, T_0, J, simultaneous gauge action, round metric, R_J | HOLDS | Normalize `integral Omega^2=1`. The transported second slice and intrinsic two-slice energy match rows 941/947. The variational bound refers to exact expectations under J. |
| 50–59, seed definition and table | HOLDS AFTER CORRECTION | The threshold formulas and quoted three-digit values agree with the stated approximate C_beta values. After extending to L=16, the smallest seed side is 45 times the largest measured side, not at least 60. |
| 61–63, finite-time marginal | HOLDS AFTER CORRECTION | The open-slab formula with `b=exp(-V/2)` is right. The actual periodic gauge theory needs its gauge projection at the closing seam; a bare `Tr T_0^N` includes nonphysical sectors. See defect 1. |
| 64, OB1 | HOLDS AFTER CORRECTION | The boundary vectors contain no centre-odd components. This removes odd states from the outer boundary propagation, not from J_K, its central kernel, or its winding correlations. |
| 65–66, OB2 and controlled vacuum approximation | HOLDS AFTER CORRECTION | Fixed-box spectral convergence holds with a norm, an overlap-dependent constant and an even-sector gap. These have not been bounded for the runs. C4 supplies position stability only. |
| 70, update algorithm and open-time sampler | HOLDS AFTER CORRECTION | The Python driver calls the asserted algorithm. The C sampler is absent, so its algorithm, staples, neighbour indexing and boundary exclusions remain unverified. |
| 72–82, observable list and symmetry sectors | HOLDS AFTER CORRECTION | The implemented observables are gauge invariant, but S0e has 36 entries; the fixed-base strip is not a pure zero-momentum observable. No swap-block decomposition is implemented. See defect 5. |
| 83, errors and bias correction | HOLDS AFTER CORRECTION | Twenty delete-block estimates and the stated jackknife formula are implemented. “Blocks long against the measured autocorrelation” has not been demonstrated. Configuration and block records are absent. |
| 86, C1 exact Haar ratios | HOLDS AFTER CORRECTION | The individual Casimir ratios hold. “Top of every span is 1/6” is false: the SU(2) winding-odd spans have top `1/(3L)`. The later calibration table gives the correct values. |
| 87, C2 and 102–116, free photon | HOLDS | On each nonzero transverse mode, the precision and `R=1/[beta(exp(omega)-1)]` are correct. Remove the free noncompact zero modes. Linear attainment is in the Gaussian Sobolev class; bounded truncations give the same supremum in the bounded test class. |
| 88,96, C3 with photon-sector amendment | HOLDS AFTER CORRECTION | The recorded photon growth test passes using the reported errors and L>=6. Its size pass is a marginal raw point-estimate pass, not a significant bound; full U1s and magnetic-only U1s-B fits were conflated. |
| 89, C4 criterion; 277, caveat “handled” | FAILS | Same-slab comparisons with unpaired errors do not control either boundary error or the vacuum limit. The 17/73 count and maximum quoted deviation reproduce. |
| 90,150, C5 independent implementation pass | FAILS as the stated like-for-like check | C5 prescribed the time-like plaquette-sum ratio. The report compares a 36-dimensional maximum with row 947's three-dimensional maximum. These are different statistics. The local means are consistent; the claimed ratio comparison was not reported. |
| 91–94, S1–S4 | HOLDS AFTER CORRECTION | They define descriptive finite-range criteria. Finite-range growth alone is not an unboundedness theorem. S3 tests a threshold on the measured law/box, not `(LSI-J-seed)_a` on another box. |
| 92,96, recalled deconfinement and rotor models | HOLDS AFTER CORRECTION | Useful disclosed hypotheses. The Gaussian holonomy kinetic action yields rotor energy about `1/(2 beta L)`; this is not an exact compact Wilson identity at beta 1.5. Recalled string tensions and masses are not measured inputs. |
| 97,120,131, gap estimator and saved artifacts | HOLDS AFTER CORRECTION | Per-slice data are computed in memory, but only final summaries are saved. They do not support reblocking, paired C4 errors or correlated plateau fits. The cited C source and shell runner are missing. |
| 98,120,133, analytic gradients and self-test | HOLDS | Prefix/suffix derivatives, Fourier phases, winding derivatives and tangent projection match the implemented functions. The test passes again; a deliberate doubled-gradient error is detected. This does not validate the missing sampler. |
| 122–124, Lemma GAP-R | HOLDS, conditional on BR-gap and variance Lemma J | Keep `E_1<=1`. These dependencies already have row 949's check; calling them still unchecked is stale. No SU(2) estimate is discharged. |
| 125–128, interpretation of the floor | HOLDS AFTER CORRECTION | Any genuine vacuum channel energy upper bound below one supplies a lower bound for the full R_J. An energy estimate is not automatically that bound; a floor does not identify which variational sector attains it. |
| 135–148, beta-zero calibration results | HOLDS AFTER CORRECTION | The displayed table and named ratios match the saved summaries within the stated tolerances. The exact count “70” has no itemized saved check record and is unverified. Upward raw maxima illustrate why sample maxima are not rigorous lower bounds. |
| 151,153, winding energies and rotor conclusion | HOLDS AFTER CORRECTION | The effective-energy values are transcribed correctly. Ground-state and error control are additional. The beta-8 holonomy instability, including the large bias correction, is correctly disclosed. |
| 153, C2 numerical comparison | HOLDS as GUIDE arithmetic | `0.08106` versus `0.077254` is +4.9%; the bias-corrected value is `0.07774`. This is a compact-U(1) weak-fluctuation check, not a direct Gaussian sampler test. |
| 155–167, timing, batch and interim numbers | HOLDS AFTER CORRECTION | Run parameters and completed counts match saved outputs. Restrict small memory figures to the corresponding timing runs; the main maximum is about 765 MB. C4 interpretations retain defect 1. |
| 171–175, three channels and seed-box interpretation | HOLDS AFTER CORRECTION | A heuristic list, not an exhaustive spectral decomposition. Flux states are expected to become heavy; they are not absent on the seed box. The finite data do not establish this extrapolation. |
| 176, seed needs `m_G>=K_a` | HOLDS, with the stated identification | If m_G is the lowest seed-box energy and `m_G<=1`, GAP-R gives this necessity. If `m_G>1`, it is automatic since `K_a<=1`. It is not a sufficient criterion for LSI. |
| 178–206, SU(2) beta 2.3 tables and S1/S3 | HOLDS AFTER CORRECTION | Saved variational numbers and fit arithmetic reproduce. The predeclared top-sector GROWTH criterion does not fire. The spectral-floor columns and “saturating” interpretation need defects 2,3,6. |
| 208–224, U(1) table and C3/C4 | HOLDS AFTER CORRECTION | Saved values reproduce. Correct the fit attribution, error interpretation and marginal size pass as in defect 4. Photon ratios increase in the measured range. |
| 226–252, SU(2) beta 2.6 table and S1–S3 | HOLDS AFTER CORRECTION | Saved variational values reproduce; top-sector GROWTH does not fire. The top fit is not a power law. The flux floors are conditional spectral interpretations, not certified lower bounds. |
| 256–269, no growth, scaling exponents, all numbers lower bounds | HOLDS AFTER CORRECTION | Say “the sampled top-sector criterion did not fire.” S1e at beta 2.3 does grow in the saved range. The slopes describe selected estimators, not the unknown optimal Poincare constant. Sample ratios are not deterministic lower bounds. |
| 271–275, seed comparison and smeared glueball floor | FAILS as a measured bound on m_G or seed-box R_J | The smeared effective energies are reproduced, but no plateau, controlled vacuum limit, channel identification or volume transfer is supplied. The conditional formula is valid; the claimed `m_G<=0.87` and floor `>=0.22` are not established. |
| 279–282, changed interpretation of row 947 | HOLDS AFTER CORRECTION | The larger winding span finds a much larger finite-slab ratio on L=4. This is useful. “Seed comparison decided by m_G” and “sharp form” overstate a necessary spectral condition. |
| 284–303, open items and no SU(2) refutation | HOLDS | No box-uniform SU(2) LSI or seed is proved or refuted here. Keep that conclusion while correcting the control, vacuum and floor claims above. |

# Defects that change the interpretation

## 1. Open boundaries do not finish the vacuum check

Multiplying the N_t-slice Wilson slab weight by halves gives

`Z=<b,T_0^(N_t-1)b>`, and `J_(K,K') ∝ (T_0^K b)(x) T_0(x,w) (T_0^K' b)(w)`.

This verifies the open-boundary formula by direct factor counting. Both outer vectors are gauge invariant and centre even. Odd flux eigenstates have zero overlap with b. They still propagate between two odd insertions. Even the vacuum law J has nonzero winding variance. Replace “no flux sector enters the measured law” with “no centre-odd state contributes to boundary contamination.”

For an actual periodic gauge cylinder, the transported-pair density instead contains

`T_0(x,w) (T_0^(N-1) Pi_G)(w,x) / Tr(T_0^N Pi_G)`.

This follows by retaining the residual temporal gauge average at the closing seam. The bare T_0 formula is appropriate to an unprojected chain, not that cylinder. This correction does not change the open-slab analysis.

In the main runs, `m=0`. For beta 2.3 and U(1), the pairs have depths `(10,10)` and `(6,14)` in the **same** 22-slice slab. At beta 2.6 they have depths `(12,12)` and `(8,16)` in the same 26-slice slab. A common bias can persist at both positions. Centre-even light states, including flux pairs, remain allowed.

The exact variance of the difference is `s_c^2+s_e^2-2 Cov(c,e)`. `analyze954.py:76–82` substitutes `s_c^2+s_e^2`. The covariance is unavailable. Thus the reported maximum 2.30038 is reproduced arithmetic, not a calibrated significance for the paired difference.

At fixed L the spectral statement can be written in norm as `T_0^K b/(lambda_0^K <Omega,b>)=Omega+O_L(exp(-E_even K))`. A usable expectation bound needs its constant and norm; signed expectations do not have a general relative-error estimate. Neither this bound nor a denominator error bound for the ratios is measured. C4 is a useful preliminary check only.

## 2. The elementary spectral floor is used beyond its hypothesis

GAP-R itself is sound. Write `rho=beta R_J` and `q=lambda(1-lambda)`. If `rho<1/2`, then `rho+(1-2rho)q<1/2`, hence `Xi(rho)>2`. BR-J would force `E_1>1`. Otherwise the denominator is at most rho, giving `2E_1>=1/rho` and the claimed floor.

The beta-2.3 plaquette proxies 1.16–1.73, and winding proxies 1.20 and 1.48, do **not** verify `E_1<=1`. They therefore do not license the displayed floors. Even a true vacuum effective-energy upper bound greater than one cannot supply the missing premise.

The restriction matters. In the same one-mode Gaussian model take `omega=log 4`. Then `R_J=1/(3 beta)`, whereas `1/(2 beta omega)>1/(3 beta)`. Indeed `log4<3/2`, since the first four positive terms of `exp(3/2)` already sum above 4. Thus removing the restriction makes the floor false. This is a hand counterexample to the unrestricted extension, not a counterexample to Wilson SU(2) or to GAP-R as stated.

A corrected use either supplies `E_1<=1`, or inverts the full decreasing function Xi: if a genuine upper bound `E_1<=Ebar` is available, retain `Xi(beta R_J)<=2Ebar`. No numerical floor is imported into a proof.

## 3. Slab correlators and their errors do not establish spectral floors

For a vacuum correlator, `C(t)=integral exp(-tE) dmu(E)` with positive mu gives `log(C(t)/C(t+1))>=inf supp(mu)`. A finite-slab correlator instead has outer vectors `T^t b` and `T^(N-1-t-tau)b`. Their spectral coefficients need not be positive coefficients of one fixed vacuum measure. The code also changes the average over source positions with tau. Subtracting the sample mean at each slice does not restore a vacuum spectral representation.

`rj954.py:519–555` uses slices only two steps from the ends. `glueball954.py:90–109` uses three. C4 tested deeper pair observables, not these correlators. It does not validate their energies.

`analyze954.py:13–23` averages tau=1,2,3 with inverse marginal variances and gives error `1/sqrt(sum 1/s_i^2)`. These energies share correlators and configurations. Their covariance is required. Nonpositive or nonfinite values are dropped adaptively. This is not a demonstrated plateau fit.

Both correlator routines use `nansum` for jackknife variances. If every leave-block logarithm is invalid, the code can emit zero error; saved logs contain `nan+-0.000`. In the glueball script the data are centered once with the full sample, before deleting blocks, rather than recomputing the mean per deletion. These errors cannot be repaired from the saved aggregate matrices.

The printed smeared numbers, `0.878±0.122` and `0.860±0.110` at tau=1, are correct transcriptions. The report correctly says no plateau is resolved. They do not establish `m_G<=0.87±0.11`. Even a vacuum 0++ correlator can couple to centre-even two-torelon states; it need not isolate a glueball. There is also no transfer from this L=14 box to side at least 720.

## 4. The U(1) control passes a narrower test than stated

The free-photon argument is verified directly: Gaussian integration yields `u+u^(-1)=2+|khat|^2`, with `u=(beta+c)/beta=exp(omega)`. The two precision eigenvalues are c and `2 beta+c`. Orthogonal Gaussian modes then give the asserted supremum and the large-L exponent one. The numerical table reproduces to its stated precision.

Saved-data fits give:

| Statistic and sizes | Slope ± nominal error | chi-square / degrees of freedom |
|---|---|---|
| U1s, L=6–12 | 0.71112 ± 0.03575 | 2.7873 / 2 |
| U1s, L=4–12 | 0.56630 ± 0.02371 | 32.0847 / 3 |
| U1s-B, L=4–12 | 0.842 ± 0.024 | 26.4 / 3 |
| U1s-B, L=6–12 | 0.711 ± 0.036 | 2.6 / 2 |

The report's all-size 0.84 and chi-square 2.6 belong to U1s-B, not the stated full U1s sector. The L>=6 growth criterion still passes using its nominal errors. Neither poor all-size fit is a measured asymptotic exponent.

At L=12, full U1s divided by the free value is `0.67070±0.01556`; its saved bias-corrected value gives `0.66459`. The factor-1.5 boundary is 2/3. The raw point estimate clears it by only about 0.26 nominal errors, and the bias-corrected estimate lies below it. Do not call this a robust size-control pass. The magnetic-only error is merely scaled from the full-sector error; it was not separately jackknifed.

The proposed incoherent-gradient explanation is plausible, not an established diagnosis. Local `sin(theta_p)` has derivative `cos(theta_p)`; a nonlinear local readout need not attain the Gaussian soft-mode optimum. That explains why the test can lose sensitivity, but does not exclude sampling or boundary error.

## 5. The actual span is useful but differs from its description

`rj954.py:260–300` contains 24 local fields plus four winding-even sums for each of three directions, hence 36 S0e entries. The reported `24+6×3` count is wrong. S0o contains the eight listed odd polynomials; S1e and S1o contain the stated Fourier fields. The 2×2 loops are larger unsmeared loops. APE smearing is used only in the separate energy run; no APE-smeared ratio or its derivative is measured.

The SU(2) strip uses a fixed base point on each line. Translating it along that line changes the relative holonomy. Its cross-section sum therefore includes longitudinal momenta. It remains gauge invariant and is an admissible variational observable, but S0e is not purely the claimed k=0 sector. The program averages selected direction copies and cosine/sine parts. It does not explicitly diagonalize swap parity or all cubic representations. Averaging ratios through summed covariance and energy still supplies a variational lower estimate for the common exact law; it can lose sensitivity.

The `1e-9` Gram cutoff is basis-dependent. At beta 2.6, L=16 it drops one of eight S0o directions. Diagonal rescaling retains eight and changes the saved top only from `0.02391899` to `0.02392035`. This is negligible here, but the literal claim to optimize the whole polynomial span needs the cutoff qualification.

The C5 scalar means agree with row 947. Its ratio comparison does not implement its own prescribed statistic. The C5 JSON has no C/G matrices, so the exact time-like sum or the matching three-variable maximum cannot be reconstructed from its diagonal entries. The main JSON files do contain C/G. Calling C5 an independent end-to-end implementation check also needs the missing C source.

## 6. Finite-range estimates are not bounds or scaling laws for the supremum

The saved main matrices reproduce every reported top eigenvalue to within `3.1e-15` in a separate Cholesky-based calculation. Independent weighted-sum regression reproduces the main slopes:

| Measured statistic | Slope ± nominal error | chi-square / degrees of freedom |
|---|---|---|
| SU(2), beta 2.3, top, L=6–12 | 0.16235 ± 0.07687 | 3.6932 / 2 |
| SU(2), beta 2.6, top, L=6–16 | -1.81327 ± 0.05218 | 306.4349 / 4 |
| SU(2), beta 2.6, S0e | 0.06824 ± 0.05250 | 3.8343 / 4 |
| SU(2), beta 2.6, S1e | 0.02401 ± 0.02231 | 7.7269 / 4 |

The beta-2.6 top fit is correctly labelled not a power law. Apply the same caution to winding fits: S0o has chi-square 52.9/2 at 2.3 and 28.2/4 at 2.6; S1o has 74.2/4 at 2.6. The statement that these sectors “fall like” the fitted powers is too strong.

At beta 2.3, S1e increases from 0.1342 to 0.1500, with fitted slope `0.14564±0.02876`. Thus “no measured lower bound grows” is literally false. Saturation as k_min approaches zero is a plausible reading, not a consequence of these four points. S0e is not an upper bound on the exact S1e or on R_J.

For exact C and G on one law, a restricted Rayleigh maximum is at most that law's optimum. Plug-in sample C/G do not preserve a deterministic inequality to the population optimum. C1 supplies an immediate illustration: the raw S0e estimate 0.17714 exceeds its exact 1/6. The main SU(2) bias corrections are small; this does not turn the raw numbers into certified lower bounds. The U(1) beta-8 winding correction is large: 10.362 to 6.065.

The block lengths are 40 or 60 measurements in the main runs. Only lag-one correlations of a sum of second-moment matrix entries are saved. That statistic is not the integrated autocorrelation of the optimized ratio. Errors on local means are ordinary standard deviations divided by sqrt(n), without autocorrelation correction. Neither systematic boundary error nor equilibration error is included in the reported bars.

Keep the useful conclusion: **the predeclared top-sector GROWTH criterion did not fire in these saved finite-slab estimates**. There is no upper bound on R_J. A finite list of growing lower estimates would also need further argument before refuting an all-volume bound.

## 7. Seed-threshold arithmetic is valid; the physical extrapolation is conditional

Using the source's approximate C_beta values, the raw `top-3 err` tests give exactly its listed exceedances: beta 2.3 only L=4 for a in {30,40,60}; beta 2.6 L=4 for all five listed a, L=6 for {30,40,60}, L=8 for {30}. These compare finite-slab estimators with threshold numbers. They do not refute an LSI for the vacuum law without a controlled passage, and never refute the seed on `(24a)^3`.

The statements about string tensions, deconfinement lengths and masses are disclosed recollections. Treat `E_flux≈sigma L` and `m_G≈0.49` as hypotheses for interpretation. They do not establish heavy flux at side 720, remove flux states from the spectrum, or prove that a local glueball is the only obstruction to LSI. LSI is stronger than its Poincare consequence. The necessary test `m_G>=K_a` does not decide the seed even if that mass were known exactly.

## 8. Missing executable provenance limits the code verdict

Only `rj954.py`, `analyze954.py`, and `glueball954.py` are present in `guide/lane954/`. The referenced `lgt_sweep.c`, `run954.sh`, and the compiled library are not supplied in the checkout. No matching C source or launcher was found by a bounded filename search inside `.claude/`.

The Python code reads plausible sampler output through ctypes. It cannot certify how that output was sampled. No Monte Carlo rerun was attempted, and no replacement sampler was invented. This is a missing verification step, not evidence that the original sampler was wrong. Preserve the useful numerical summaries while marking sampler correctness and historical resource/lock claims unverified.

# Checks performed and saved evidence

The source report and three Python implementations were read whole. The main JSON matrices, calibration summaries, relevant log records, and saved analysis were inspected. Aggregate data were recomputed; configuration samples and block matrices are unavailable.

Small deterministic checks ran under the repository's shared numeric lock, acquired for `gap-lsij-scale-check-astra-956` and released after completion. They used one BLAS thread and about 61 MB peak RSS. The requested `nice -n 10` invocation was attempted, but macOS returned `setpriority: Operation not permitted`; the sub-second checks still completed. No numerical result discharges a claim.

- Original directional-gradient self-test: all 13 reported tests pass again. A second seed gives maximum normalized error `1.88e-9`.
- A deliberate doubled local-gradient mutation produces nine failures. The supplied self-test prints FAIL but does not return a failing exit status; an automated runner must inspect it or change that behavior.
- Simultaneous random gauge transformation preserves values and gradient Gram matrices to about `1.2e-15` in the small test. A spatial translation preserves local sums but changes the fixed-base strip, confirming its momentum qualification.
- The main generalized eigenvalues, the 17 C4 points / 73 comparisons, and the main regression arithmetic reproduce. Main S0o rank/rescaling was checked separately.
- The saved photon table, approximate seed thresholds and displayed calibration arithmetic reproduce. C5's missing cross-covariances prevent its prescribed ratio comparison.

Full logs and scripts remain in `/tmp/ym4d-lane956-check/`: `selftest.log`, `check954.py`, `check954.log`, `span_rank.py`, `span_rank.log`, `analyze954.log`, and `source-manifest.json`. The manifest pins the five repository refs and hashes the report, its two row-947 references and all 53 lane954 artifacts. A first diagnostic attempt stopped on absent C/G in the calibration JSON; the corrected diagnostic records that absence and checks available matrices only. Reading `HEAD:scripts/lab_ops.py` in the sparse checkout failed because its promised blob required an unavailable network fetch; the lock helpers were read from the explicitly allowed full repository and copied to task scratch. No repository source, FINISH row, registry, ledger, audit file or remote was changed.

Checkpoint: the requested check is complete. Analytic implications survive on their stated domains. Saved finite-slab arithmetic is reproducible where matrices exist. Vacuum convergence, sampler validation, correlated errors and seed-box spectral identification remain unverified inputs, not newly assigned proof tasks. This report is the sole checkout output and is uncommitted/unpushed.

RESULT: HOLDS: the nonzero-mode free-photon formula and conditional GAP-R for E_1<=1. HOLDS AFTER CORRECTION: the saved variational code/controls, finite-range fits, threshold comparisons and the statement that no SU(2) refutation was obtained. FAILS as written: the claim that C4 handles the vacuum caveat, the C5 like-for-like ratio check, deterministic lower-bound language for sample estimates, and the reported spectral/glueball floors without their missing premises. No box-uniform SU(2) LSI or (LSI-J-seed) is proved or refuted; all runs remain GUIDE.
