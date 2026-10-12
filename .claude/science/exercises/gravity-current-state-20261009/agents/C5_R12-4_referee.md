# Independent referee report: C5 probe R12-4

## VERDICT

**CONFIRMED WITH CORRECTIONS.** The fixed reading is **DERIVED**: the report proves a genuine unified cone no-go in its explicitly restricted class \(\mathcal U\), and that class contains \(T_E\), \(T_u\), and the refereed R8-3 additive/common-scalar or GR-normalized spin-2 subclass. Lemma K is state-independent and therefore does extend beyond Gaussian states. Theorem U is correct, and its logarithmic divergence is coordinate/frame independent at every regular nonzero null point. The corrections are substantive but do not overturn that fixed reading: Corollary \(U_L\) is only a regulator-specific log-squared bound, not the one exact formula written for every cut; E2 is a finite stationary spectral ansatz with a causal damped propagator, not an exhibited stationary CQ dilation; the observational comparison uses \(\beta=\gamma/c\), not the amplitude coefficient \(\beta/2\); and “a preferred frame plus one cone regulator” is an example price within the investigated constructions, not a proved minimal price for all record-metric CQ theories.

## Scope and reproducibility

I read the worker report, its runner and output, the fixed R12-4 rule, the R8-3/R9-4/R10-3/R11-5 reports and referee records, and the supplied axioms. I reran `python3 scripts/r124_checks.py`; its output is byte-identical to `scripts/r124_checks.out`, with SHA-256 `7a57b113359f71df890f7076c870964c8b160e17e40e8170dd4d4f2b20862909`. The script hash is the reported `5f0252c1d220a7f7d9d6158833f4c090864aab6fcf03bb56f5d143cb252c91c4`.

Independent checks are in `scripts/r124_referee_checks.py` and `scripts/r124_referee_checks.out`. They use fresh random positive spectral matrices, a separate three-million-point cone Monte Carlo, analytic regulated integrals, and an independent conversion of \(H_0\) to inverse megaparsecs.

## 1. Lemma K

**Confirmed, with two scope clarifications.** For Hermitian \(f,J\), stationarity and spatial homogeneity make each unsymmetrized spectral matrix \(S(p)\) positive semidefinite in any state, not merely a Gaussian state. With

\[
C_{fJ}(p)=S_{fJ}(p)-S_{Jf}(-p),\qquad
\bar\sigma={S_{ff}(p)+S_{ff}(-p)\over2},\qquad
\bar P={S_{JJ}(p)+S_{JJ}(-p)\over2},
\]

spectral Cauchy--Schwarz followed by ordinary two-component Cauchy--Schwarz gives

\[
|C_{fJ}|\leq
\sqrt{S_{ff}(p)S_{JJ}(p)}+
\sqrt{S_{ff}(-p)S_{JJ}(-p)}
\leq2\sqrt{\bar\sigma\bar P}.
\]

This part does not use Gaussianity and in fact does not need self-commutation. Self-commutation is used to make the record classical and to remove the \(\widetilde GJ\) term from \(C_{fJ}\). If \(B\) is the operator conjugate to the matter source, zero reverse gain makes the full \(J\)-\(B\) commutator retarded, so the Kubo identity gives \(|C_{fJ}|=\hbar|F|\). Thus \(\bar\sigma\bar P\geq\hbar^2|F|^2/4\), with no Gaussian-state premise. The independent random check found no violation in 250,000 pairs (`scripts/r124_referee_checks.out:1-4`).

The first clarification is that “stationary” must include the translation structure needed for the pointwise \(p\)-space statement, as class \(\mathcal U\) does (`R12-4_report.md:68-75`). The second is that Belavkin nondemolition is past-output compatibility with **all** later system observables, together with self-commuting outputs; the report imposes that condition only for the load-bearing operator \(B\). That is sufficient for Lemma K, but it is not by itself the full definition of a classical record. Belavkin's formulation explicitly requires future system operators to commute with past pointer outputs and separately requires output self-nondemolition ([Belavkin, Eq. 2.1 and surrounding discussion](https://www.maths.nottingham.ac.uk/plp/vpb/publications/ndp-fph-ams.pdf)).

The measure version is also sound provided the joint spectra are locally finite positive matrix-valued measures and the gain commutator has the stated absolutely continuous density. Apply the same inequality to Borel sets, take the Lebesgue decompositions, and differentiate the absolutely continuous parts. A singular diagonal component cannot cancel the nonzero absolutely continuous commutator density; it can only add positive spectral weight. Those hypotheses should be stated rather than compressed into “singular parts only add” (`R12-4_report.md:96-99`).

## 2. Theorem U and the frame-tied Monte Carlo

**Confirmed.** From \(M=|G_R|^2\bar P\), (H-T\(_f\)), \(|G_R|^2=g^2/s^2\), and \(|F|\geq f_0\),

\[
\bar\sigma M\geq{\kappa g^2f_0^2\over s^2}.
\]

If both nonnegative measures were finite on a cone patch, Cauchy--Schwarz would make \(\int\sqrt{\bar\sigma M}\) finite. The displayed bound instead makes it at least a constant times \(\int |s|^{-1}d^4p\). At every \(p_0\ne0\) with \(s(p_0)=0\), \(ds=(2\omega,-2\mathbf k)\ne0\); the regular-level-set/coarea theorem therefore supplies local coordinates \((s,y_1,y_2,y_3)\) with a smooth positive Jacobian, and \(\int ds/|s|\) diverges. This survives every smooth nonsingular change of inertial or preferred-frame coordinates. It does not mean that a singular reparametrization or a different physical propagator is covered.

The supplied Monte Carlo reproduces, and the independent run gives `fraction/(2x) = 2.452, 2.460, 2.478` as \(x\) decreases and `0.04838` for the cut integral versus `0.04927` from the local-shell estimate (`scripts/r124_referee_checks.out:6-11`). The Monte Carlo is illustrative; the coarea argument is the proof. The one-sided lower bound must hold on a patch of nonzero tangential measure. In a general frame-tied theory Newton's static limit alone does not establish that hypothesis at every radiative cone point; it is correctly an explicit part of \(\mathcal U\) (`R12-4_report.md:73-77`).

## 3. Corollary U_L

**The log-squared scaling is confirmed; the exact universal formula is not.** The general regulated statement is

\[
\left(\int_B\bar\sigma\,d\mu\right)
\left(\int_BM\,d\mu\right)
\geq\kappa f_0^2
\left(\int_B |G_{\rm reg}(p)|\,d\mu\right)^2.
\]

For a unit-normalized transverse slice and a **two-sided damped** band \(|s|<\delta\), \(|G|=g/\sqrt{s^2+s_*^2}\) gives \(2g\,\operatorname{asinh}(\delta/s_*)\). For a **two-sided hard cut** \(s_*<|s|<\delta\) with the undamped pole it gives \(2g\ln(\delta/s_*)\), not the same exact expression. One-sided bands divide those logarithmic integrals by two, and a four-dimensional band brings its coarea/Jacobian-weighted tangential measure. The independent values differ by \(2\ln2\) asymptotically (`scripts/r124_referee_checks.out:13-18`). A finite observation window is not literally a hard spectral deletion either; it gives the same logarithmic scaling with window-dependent constants.

Accordingly, `R12-4_report.md:116-120` should be retained as an asymptotic \(\propto L^2\) trade after the regulator, sidedness, and band normalization are specified. It is not one exact coefficient “under any cut.” The worker runner itself uses a one-sided hard-cut normalization in section [4] and a two-sided damped normalization in section [6] (`scripts/r124_checks.py:109-126,144-155`), so it does not validate the single merged formula.

## 4. Containment

**Confirmed, with a precision correction about R8-3.**

- In \(T_u\), the additive kernel and \(P_JD'_0\geq1/4\) imply \(K P_J\geq |F|^2/4\); the standard pole and nonzero continuous cone gain then give the referee-corrected Lemma C. This is exactly the required \(\mathcal U\) mechanism (`C5_R11-5_report.md:86-111`; `C5_R11-5_referee_verdict.md:5-6`).
- In \(T_E\), the defining self-commuting output, zero reverse gain, standard pole, and continuous cone gain meet Lemma K directly (`C5_R10-3_report.md:56-66`). Theorem U first gives the dichotomy that felt-field noise and metric-record covariance cannot both be locally finite. Emission silence plus the positive Källén--Lehmann/Stieltjes representation and a finite spacelike response make the felt-field spectral density locally integrable; R10-3's refereed dispersion step then selects the other horn, forcing the metric-record covariance to be non-locally finite (`C5_R10-3_referee.md:33-41`). Thus Theorem P is reproduced. The dispersion step is not needed for containment or for the dichotomy; it is needed to identify which member of the pair diverges.
- The R8-3 retained subclass explicitly assumes the pointwise product trade-off, additivity, the standard pole, and a common scalar or GR-normalized spin-2 cone coupling (`C5_R8-3_referee.md:246-252`), so it is contained. R8-3's boost-orbit vacuum-rate obstruction is a different residual, not an unqualified stronger version of Theorem U: within that narrower Lorentz-invariant subclass it excludes more than cone-local record finiteness, but it uses additional vacuum and matter-spectrum hypotheses (`C5_R8-3_referee.md:26-49,125-160`).

## 5. E2: damped TT propagation

**Algebraically consistent and observationally allowed at the quoted scale; not an explicit CQ model.** With

\[
G={g\over s+i\gamma\omega},\qquad
\bar P=a\sqrt{s^2+\gamma^2\omega^2},\qquad
\bar\sigma={\kappa\over a\sqrt{s^2+\gamma^2\omega^2}},
\]

both near-cone integrals are finite for every \(\gamma>0\), and their logarithm is the damped \(\operatorname{asinh}\) expression. These are positive stationary spectra. The differential operator \(\partial_t^2+\gamma\partial_t-\nabla^2\) is causal because its principal part is the ordinary wave operator; its retarded Green function has front speed \(c\). At real frequency,

\[
k={\omega\over c}\sqrt{1+i\gamma/\omega}
= {\omega\over c}\left(1+{i\gamma\over2\omega}+{\gamma^2\over8\omega^2}+\cdots\right),
\]

so the amplitude decays as \(e^{-\gamma D/(2c)}\), while phase/group-speed corrections are of order \(\gamma^2/(8\omega^2)\). At \(\gamma=H_0\) and 100 Hz this is \(1.53\times10^{-42}\), far below GW170817's multimessenger interval of roughly \(-3\times10^{-15}< (v_{GW}-c)/c <7\times10^{-16}\) ([LIGO/Virgo/Fermi/INTEGRAL](https://arxiv.org/abs/1710.05834)).

The convention correction is important. arXiv:1803.11397 defines \(\beta=16\pi G\eta\) and writes the **amplitude** factor as \(e^{-\beta D/2}\); its combined 95% upper bound is \(\beta<6.75\times10^{-4}\,\mathrm{Mpc}^{-1}\) ([paper, Eqs. 5 and the combined fit](https://arxiv.org/html/1803.11397v1)). The E2 equation maps to \(\beta=\gamma/c\), not \(\gamma/(2c)\). For \(\gamma=H_0=2.2\times10^{-18}\,\mathrm{s}^{-1}\), \(\beta=2.264\times10^{-4}\,\mathrm{Mpc}^{-1}\), so E2 is still below the quoted bound by a factor about 2.98. The worker's amplitude-loss numbers are correct because they used \(e^{-\beta D/2}\) (`scripts/r124_referee_checks.out:20-27`).

What is missing is the physical realization. The energy identity is

\[
{dE_h\over dt}=\int J\dot h\,d^3x-\gamma\int\dot h^2\,d^3x,
\]

so a conservative dilation requires sink degrees of freedom. A stationary quantum or stochastic bath that produces the absorptive term also carries fluctuation noise; a full proposal must include that noise in \(M\) and the matter kernel, preserve the nondemolition/CP structure, and show that a TT-only friction term is compatible with source conservation/Bianchi constraints and an acceptable local preferred-frame completion. None is built (`R12-4_report.md:154,163,198-210`). Thus E2 is a plausible causal stationary **spectral escape** from U2, not the claimed explicit stationary CQ model. Its existence is not needed for the DERIVED no-go reading.

## 6. Minimal price

**Not confirmed as a universal minimality statement.** Theorem U proves only that a locally finite model cannot retain all of U1--U6. One may abandon stationarity/eternal duration, the undamped pole, the nonzero cone gain, the linear record-to-metric map, second-order treatment, spatial homogeneity, or the stationary nondemolition/Kubo realization. The report itself lists several of these open routes (`R12-4_report.md:158-168`). Earlier referees explicitly leave general CP histories without the stationary meter structure and non-Gaussian/jump/mediator constructions open (`C5_R9-4_referee.md:17-33,83-92`; `C5_R8-3_referee.md:158-161,268-270`). Therefore prior results do not force a preferred frame across all record-metric CQ theories.

Even for E1, a finite start time supplies a temporal boundary or arrow; it does not literally privilege a spatial lattice site. The Lattice axiom's “No site is privileged” is spatial (`MINIMAL_AXIOMS_2026-06-29.md:35-41`), while time, arrow, and record-production dynamics are open downstream gates (`MINIMAL_AXIOMS_2026-06-29.md:173-187`). The honest statement is that, among the constructions actually analyzed while preserving linear record gravity and nonzero GW coupling, a finite start or damped propagation are two economical cone regulators, and the latter selects a frame/sink. “Preferred frame plus exactly one regulator” is not a proved exhaustive or minimal price.

## 7. No-go stress test and fixed reading

The narrow theorem survives the no-go stress test. Distinct routes were checked: correlated/sub-floor spectra; non-Gaussian two-point states; singular spectral measures; alternative homogeneous solutions/Green prescriptions; a vanishing or jumping gain; a modified/damped pole; finite-start histories; and histories lacking a stationary nondemolition dilation. The first five fail inside \(\mathcal U\); the last three are honest exits rather than counterexamples. The walls—stationarity/homogeneity, a nondemolition product bound, a standard undamped pole, and nonzero cone gain—must remain explicit and are not a unique “minimal price.” R10-3 and R11-5 attack the same cone-local residual; R8-3's boost-orbit residual is different and should not be counted as a duplicate proof. The strongest steelman is the unclosed general CP-history route without a stationary nondemolition dilation; because it is outside \(\mathcal U\), it narrows but does not refute Theorem U.

The fixed `DERIVED` alternative requires a unified no-go in a stated class containing \(T_E\), \(T_u\), and R8-3's retained subclass (`TESTS.md:4447-4461`). That requirement is met. The fixed reading is therefore **DERIVED**, with E2 and the minimal-price discussion downgraded as above.

## Strongest correct statement

For any translation-stationary, spatially homogeneous, linearized record-metric CQ theory at second order whose record admits the stated nondemolition Kubo realization (or the stated additive product trade-off), whose retarded metric response has an undamped massless \(1/s\) pole, and whose gain is bounded away from zero on a one-sided patch of a regular nonzero light cone, state-independent spectral positivity gives \(\bar\sigma\bar P\geq\hbar^2|F|^2/4\) (up to the declared normalization), hence \(\bar\sigma M\geq\kappa g^2f_0^2/s^2\); the coarea theorem then forbids simultaneous local finiteness of matter noise and classical metric-record covariance in every nonsingular frame. This class contains \(T_u\), \(T_E\), and R8-3's retained additive/common-scalar or GR-normalized spin-2 subclass, with R10-3's positive-dispersion step selecting metric-record divergence in \(T_E\). A specified finite-time or damped regulator yields a regulator- and band-normalization-dependent log-squared trade, but E2 is presently only a causal, observationally allowed stationary spectral ansatz—\(H_0/c=2.26\times10^{-4}\,\mathrm{Mpc}^{-1}<6.75\times10^{-4}\,\mathrm{Mpc}^{-1}\)—until its sink, fluctuation noise, conservation laws, and nondemolition CQ dilation are constructed; no universal preferred-frame-plus-one-regulator minimal price follows outside \(\mathcal U\).
