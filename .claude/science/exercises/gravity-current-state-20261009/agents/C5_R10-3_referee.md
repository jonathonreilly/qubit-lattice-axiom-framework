# C5 R10-3 independent referee report

## VERDICT: NOT CONFIRMED

The worker found a valuable narrow no-go, but drew the wrong fixed reading from it. Its own model M_E has no locally finite stationary Gaussian record/metric at the light cone and explicitly fails one of the six pre-registered tests (`R10-3_report.md:42-50,229-232`). Calling that failure an optional price does not produce a model passing all tests. Under the fixed rule, T_E/M_E is therefore **EXCLUDED**, while broader emission-cancelled hybrids outside T_E remain **OPEN** (`TESTS.md:3984-3998`). Several supporting claims also need material qualifications: Q-prime establishes an effective negative-commutator sector, not fundamental negative energy; the closed-loop relation is a Kubo identity rather than a general equilibrium FDT; no tensor completion establishes gamma or a spin-2/spin-0 tower; and the proposed `1/mu <= 10 micrometres` bound is not obtained from the cited inverse-square-law fit.

## Scope and reproducibility

I read the worker report, both supplied checker files, the fixed R10-3 rule, the minimal axioms, and the available R4/R6/R8/R9 referee chain. I reran `python3 scripts/r103_checks.py`: it completed with the same nonfatal integration-subdivision warning and reproduced the supplied output. The script and output SHA-256 hashes begin `ca33798c` and `124448df`, exactly as reported (`R10-3_report.md:5-8`). I also wrote and ran an independent symbolic/high-precision checker: `scripts/r103_independent_checks.py` and `scripts/r103_independent_checks.out`. No fixed reading or pre-existing file was changed.

## 1. Lemma Q and Lemma Q-prime

**Lemma Q: confirmed under its stated spectral hypotheses, with one wording correction.** Stationarity plus `[J(x),J(y)]=0` makes the unsymmetrized record spectrum even. The ground-state spectrum condition puts the quantum two-point spectrum in the forward cone, so the even spectrum is supported only at zero momentum. Positivity of the joint `(B,J)` spectral matrix then kills the cross spectrum for `p != 0`, hence the linear gain commutator vanishes. The proof at `R10-3_report.md:144-150` is sound and does not need Lorentz invariance. "Informative" here means nonzero linear gain at nonzero four-momentum; the proof says nothing about a zero mode.

The phrase "even if commuting classical noise is added" is too compressed. Independent c-number noise cannot create an operator commutator or gain, so the conclusion survives, but the *total* noisy spectrum no longer obeys the quantum ground-state support condition used in step 2. The proof should be applied to the quantum meter part and the independent-noise observation stated separately.

**Lemma Q-prime: confirmed only in its declared free/generalized-free scope, with corrected interpretation.** For positive-energy free fields, the positive-frequency commutator weights in a fixed channel are nonnegative. A self-commuting combination with nonzero forward gain therefore needs an opposite commutator weight. That is an effective negative-frequency/negative-mass partner of the QMFS kind (`R10-3_report.md:153-154`), not necessarily a fundamental negative-energy field. Tsang and Caves explicitly use a positive-mass/negative-mass pair in the effective modulation-frame Hamiltonian, while the underlying laboratory system can remain positive-energy. Their construction supports the corrected statement, not the stronger prose at `R10-3_report.md:75-76,252`. Interacting, driven, and nonstationary meters remain outside the lemma.

Primary comparators: [Tsang--Caves, PRX 2, 031016](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.2.031016) and its [arXiv text](https://arxiv.org/html/1203.2317v2).

## 2. Closed-loop fluctuation--dissipation claim

**The algebraic identity is confirmed; its name and physical consequence are overstated.** With zero reverse gain, a self-commuting output, and the stated causal conventions, expanding `f=B+GJ` gives

`chi_ff = chi_BB + G F = R`,

and the cross commutator contributes `-2 Im(GF)`. The independent symbolic calculation gives `S_ff(abs)=|F|^2/P` and exactly that cross term (`scripts/r103_independent_checks.out:1-4`), confirming `R10-3_report.md:156-163` up to its conventions. With exact one-sided emission silence, the felt field satisfies zero-temperature detailed balance and is operationally indistinguishable, at Gaussian linear-response level, from a zero-temperature quantum bath.

This is not a general equilibrium fluctuation--dissipation theorem. Clerk et al. Eq. 90 is a stationary detector quantum-noise inequality; the review distinguishes that inequality from the equilibrium FDT. The appropriate description here is an exact closed-loop Kubo/commutator identity, promoted to a zero-temperature bath relation only after imposing emission silence. Wiseman--Milburn supports the general measurement-feedback drift-plus-diffusion architecture, not a covariant gravitational or record-metric realization. See [Clerk et al., arXiv:0810.4729](https://arxiv.org/html/0810.4729) and [Wiseman--Milburn, PRL 70, 548](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.70.548).

The scalar spectral argument does force positive absorptive continuum weight in every coupled channel for which the assumptions hold. It does **not** establish the claim that the theory is "linearized quantum gravity plus a massive spin-2/spin-0 continuum" (`R10-3_report.md:159-164`). No Barnes--Rivers decomposition, conserved stress-tensor coupling, gauge constraints, tensor positivity analysis, or tensor meter is supplied. At most, the work proves a scalar/channelwise quantum-bath response with a massless pole and positive continuum.

## 3. Lemma Z, Theorem P, and the growth table

**Lemma Z is correct after making its local measure assumptions explicit.** On a compact patch around a regular nonzero null point, use `s=p^2` as a transverse coordinate, with smooth nonzero Jacobian, `G ~ g/s`, `P>0` almost everywhere, and continuous `F` bounded away from zero. The inequality

`sigma |G|^2 P >= hbar^2 g^2 |F|^2/(2s^2)`

and Cauchy--Schwarz make simultaneous local integrability of `sigma` and `|G|^2P` impossible. The worker proof (`R10-3_report.md:171-176`) is concise but valid. The independent power-law classification confirms that `int ds/P` is finite only for `a<1`, whereas `int P ds/s^2` is finite only for `a>1`; both diverge logarithmically at `a=1` (`scripts/r103_independent_checks.out:6-12`).

**Theorem P is correct within T_E once two implicit assumptions are stated.** The response must admit the positive Kallen--Lehmann/Stieltjes representation used at `R10-3_report.md:184-187`, and a stationary Gaussian classical record must have a positive locally finite covariance measure. Emission silence supplies nonnegative `rho` with `rho >= const/P`; a finite spacelike response forces `int_0^delta rho(s) ds < infinity`, because the dispersion denominator is bounded and positive at fixed `s<0`; Lemma Z then forces `int |G|^2P ds = infinity`. Polynomial ultraviolet subtractions cannot cancel this positive infrared endpoint. Thus h is not the covariance of a stationary Gaussian random distribution near the cone. This is an inconsistency with T_E's declared stationary Gaussian record, not a finite model price (`R10-3_report.md:56-66,131-135,178-189`).

**Growth table: exponents confirmed, universal wording corrected.** The independent asymptotics are:

- `P~s^0`: `E(T)~T/2`;
- `P~s^(1/2)`: `E(T)~1.128379 sqrt(T)`;
- `P~s`: `(2/pi) log T + O(1)`;
- `P~s^2` with the worker's cutoff: time-averaged limit `78/pi=24.8282`.

These reproduce the worker's table at `R10-3_report.md:191-200` (`scripts/r103_independent_checks.out:14-19`). For a general irregular non-integrable spectrum, the robust conclusion is divergence of a long-time Cesaro mean and therefore `limsup E(T)=infinity`; pointwise monotone growth or a literal limit `E(T)->infinity` needs extra regularity. The `a=2` bounded row is not a counterexample because its absorptive/static integral diverges. The sentence "for any P, the record is not a stationary random field" (`R10-3_report.md:202`) is valid only within the complete V+N+continuity+positive-dispersion hypotheses.

The current no-go audit is recorded separately in `C5_R10-3_no_go_discipline.md`: the narrow theorem survives, but the worker packet itself lacks the present escape-ledger/certificate format.

## 4. The six tests and the reported numbers

1. **Newtonian limit -- not established for M_E.** Importing the R6-4 spacelike kernel gives its conservative linear window only conditionally. The worker never supplies and verifies the required bounded, causal, decaying form factor F (`R10-3_report.md:119-122,213-221,276`). The continuum-potential numbers do reproduce. At `r=38.6 micrometres`, `1/mu=1 micrometre` gives `delta V/V=4.255749e-4`, while `1/mu=10 micrometres` gives `3.356374e-2`. More relevant to an inverse-square-force experiment, the force corrections are `1.273372e-3` and `8.936996e-2` (`scripts/r103_independent_checks.out:21-29`). Lee et al. constrain a single Yukawa shape, whereas this continuum has a power tail. A one-point comparison to their `alpha=1` contour cannot yield `1/mu <= 10 micrometres`; an apparatus-level likelihood/geometry fit is required. The prior R6 referee likewise retained only a conservative demonstrated subwindow and rejected its own unsupported 10-micrometre endpoint (`C5_R6-4_referee_verdict.md:7`). See [Lee et al., arXiv:2002.11761](https://arxiv.org/abs/2002.11761).

2. **gamma and c_T -- c_T conditional; gamma not computed.** Keeping an unmodified massless retarded pole does give `c_T=1` for that pole (`R10-3_report.md:222-228`). There is no tensor completion from which gamma or the claimed massive-spin-2 trace factor can be calculated. The 1-AU continuum arithmetic is also parameter-specific: `2.844653e-35` for `1/mu=1 micrometre`, but `2.844653e-33` at the claimed 10-micrometre edge (`scripts/r103_independent_checks.out:30-31`). Both are negligible, but neither establishes gamma.

3. **Null-cone pumping -- FAIL, decisively.** Theorem P makes the record covariance non-locally finite (`R10-3_report.md:229-232`). This is the pre-registered record/metric test, not merely a matter-side diagnostic (`TESTS.md:3987-3993`).

4. **Vacuum excitation -- algebraically zero only at the advertised order.** The rank-one cancellation makes `S_ff(-p)=0` at timelike golden-rule order (`R10-3_report.md:110-140,233-235`). That check is correct. It does not rescue the nonexistent locally finite dilation, and nonlinear stability of the exact cancellation was not shown.

5. **Absorption -- spectral formula and proxy arithmetic confirmed; physical prediction incomplete.** `S_ff(p)=hbar^2|F|^2/P` is exact in the minimal construction. The quoted quadrupole proxies reproduce as `2.746680e-40 s^-1` at 10 eV and `2.746680e-30 s^-1` at 1 keV, with tower factors `2.49906` and `5.43068` for `1/mu=1 micrometre` (`scripts/r103_independent_checks.out:35-41`). But the matter matrix elements, tensor channels, and actual meter coupling are absent, and the CMB estimate assumes `sigma~l_P^2`; therefore "negligible absorption" remains a dimensional suggestion, as the worker itself partly acknowledges (`R10-3_report.md:236-241,275`).

6. **BMV -- zero only conditional on a completed classical spacelike channel.** Lemma N correctly gives a separable output for a c-number LOCC channel (`C5_R4-4_referee.md:43-49`), and the leakage number `4.392345e-24` reproduces (`scripts/r103_independent_checks.out:42`). Yet the worker merely suggests adding enough spacelike noise to cover the tower response and never embeds that repair in a full positive tensor model (`R10-3_report.md:213-216,242-247`). Thus "no entanglement" is the conditional prediction of the intended static sector, not a verified property of an explicit M_E.

The headline statement that M_E passes every matter-side test (`R10-3_report.md:35-40`) is narrower than the fixed rule and cannot support VIABLE. At least null-cone pumping fails, while Newton/gamma/absorption/BMV remain incomplete at model level.

## 5. Is conditional VIABLE coherent?

**No, not as a model in which records are the metric.** Merely leaving a legitimate record unread would not violate the one-way axiom "only records are readable." The deeper problem is that h has no positive locally finite covariance, so it is not a stationary classical random distribution capable of carrying local content at all. Record requires a record, when present, to lock one admissible local possibility and make readout content-determined (`MINIMAL_AXIOMS_2026-06-29.md:75-83`); the axioms do not supply a bridge that turns a singular formal variable into a metric/source/readout (`MINIMAL_AXIOMS_2026-06-29.md:85-95,173-190`). Declaring the divergent component forever unread, non-gravitating, and absent from all matter coupling leaves only the regular quantum bath f as physics. That is a coherent influence model, but it demotes h to auxiliary bookkeeping and abandons "records are the metric." Calling h the metric also invites its quadratic stress/self-coupling, which the worker explicitly does not calculate (`R10-3_report.md:229-232,249-263`). The proposed conditional VIABLE reading therefore changes the target rather than prices the stated model.

## 6. Fixed reading

The fixed alternatives say VIABLE requires an explicit model passing **all** six tests, while EXCLUDED requires a refereed inconsistency or bound violation for the model class (`TESTS.md:3995-3998`). T_E is the worker's expressly declared model class, and M_E is its proposed explicit member (`R10-3_report.md:56-66,108-140`). Theorem P, now checked, proves that no member satisfying finite vacuum rate and finite static response possesses the locally finite Gaussian record demanded by that class. The correct reading is therefore **EXCLUDED for T_E and for M_E as a record-metric CQ model**. This is not a set-A-wide theorem: non-Gaussian, interacting, nonstationary, reverse-gain, non-self-commuting-output, or modified-propagator theories are outside the proof, so the broader emission-cancelled route remains **OPEN** (`R10-3_report.md:204-209`).

## Strongest correct statement

For a translation- and Lorentz-invariant stationary Gaussian linear-meter CQ model with a self-commuting locally finite record, zero reverse gain, standard massless retarded propagation, continuous nonzero cone gain, positive spectral measures, finite vacuum excitation, and finite static response, exact emission cancellation makes the matter influence field obey zero-temperature quantum-bath detailed balance but necessarily makes the classical metric-record covariance non-locally finite at the light cone; correspondingly, finite-time on-shell record energy is unbounded at least in long-time Cesaro mean/limsup. Hence no record-metric realization exists in T_E, so M_E is EXCLUDED rather than conditionally VIABLE. The argument is channelwise and does not construct the claimed tensor gamma or spin-2/spin-0 tower, the 10-micrometre continuum bound is unsupported without a dedicated force-data fit, and emission-cancelled hybrids outside T_E remain OPEN.
