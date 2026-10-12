# Independent referee report: C5 / R4-3

## VERDICT: CONFIRMED WITH CORRECTIONS

The fixed reading **INCONCLUSIVE** is correct, and the arithmetic, the continuous form of Lemma Z, the forward-tube-zero criterion, the explicitly recomputed first instability, and the R3-1 correlation correction survive. The report nevertheless overstates (i) what `H_reg` alone proves for a massless branch, (ii) the massive-particle radiation kinematics, and (iii) the robustness and scope of the finite-shell instability survey.

## 1. Section 3.1 arithmetic

**Confirmed, with a scope qualification.** Rerunning `scripts/r43_obs_table.py` reproduces the Planck-spacing margins 44.18, 43.21, 38.82, 27.17, 32.51, and 30.66 decades (`scripts/r43_obs_table.py:20-44`; `scripts/r43_obs_table.out:3-12`). At `a = 10^-19 m`, the reciprocal-gap scale is `sqrt(|G^2|min) = 4.6862 TeV`; the UHECR-air and LHC entries are outside it by 4.41 and 0.93 decades (`scripts/r43_obs_table.out:14-23`). This verifies `R4-3_report.md:97-116`.

“Out of band” only removes the reciprocal-gap kinematic obstruction; it does not establish a nonzero transition or its rate, as the worker correctly says at `R4-3_report.md:116-117`. Likewise, exact in-band silence is established only for the ideal 1-to-1/0-to-2 setting, not every Bragg, virtual, finite-volume, or inelastic effect (`R2-2_referee.md:151-177`). “Every observed process” at `R4-3_report.md:110` should read “every listed process.”

## 2. Lemma Z and its dispersion consequence

### Null cone

**The continuous claim is correct, including scale.** On one time-oriented punctured null cone, `C+ = G/MN`. The missing dilation subgroup `A` is not in the stabilizer `MN`: it rescales the null vector. Thus `G/MN` retains both direction and scale. Minimality of the full horospherical `N` action on the compact quotient `Gamma_L\G`, followed by orbit duality and projection `G/N -> G/MN`, makes every `Gamma_L` orbit dense in the full punctured cone, not merely in its sphere of directions (`R4-3_report.md:120-131`). One route is unique `N`-ergodicity with full support plus amenability on the compact quotient; the underlying horospherical result is reviewed by [Schapira](https://www.numdam.org/articles/10.5802/cml.29/). The future and past cones are separate `SO+(1,3)` orbits; their two constants become equal only after continuity is combined with the adjacent spacelike shells. That gluing sentence is absent from the proof.

### Spacelike shells

**Correct despite exceptional closed orbits.** On each `p^2 = mu^2 > 0`, generic `Gamma_L` orbits are dense. The countably many closed exceptional orbits do not permit a different value of a continuous invariant: generic points approach every exceptional point, and continuity fixes the same constant (`R4-3_report.md:122-127`). In fact, Moore ergodicity plus full support already suffices for a continuous invariant. The measurable sentence needs qualification: it means constancy almost everywhere with respect to the invariant measure on each shell; it does not identify future- and past-null constants without an explicitly chosen measure/gluing hypothesis. With ambient four-dimensional Lebesgue measure the null cone is measure zero.

### Dispersion

**Narrow the consequence.** Lemma Z proves that a continuous scalar `Gamma_L` invariant on the stated spacelike-plus-null domain is `f(p^2)`. It therefore rules out anisotropy and positive-power `(a omega)^delta` corrections for an exactly null or spacelike regular scalar branch; it also rules out regular birefringence if the hypothesis applies separately to each polarization eigenvalue. This corrects the R3-3 suggestion at `C5_R3-3_report.md:167-174`.

But `H_reg` only requires a region containing the punctured null cone (`R4-3_report.md:66-72`), whereas Lemma Z is stated on all of `Omega` (`R4-3_report.md:120-127`). More importantly, the lemma deliberately leaves the timelike region free (`R4-3_report.md:140-143`). A branch asymptotic to the cone may still have a bounded automorphic timelike mass-like deformation. Hence “regular massless LV is exactly zero” and all of `Z1-Z3` being “proved given H_reg” (`R4-3_report.md:134-142,290-294`) are too broad. The proved statement is: **regular null/spacelike scalar dispersion is Lorentz invariant; bounded timelike mass-like dispersion and singular Bragg-cone physics remain open.**

## 3. Section 3.3 massive sector

**Partly confirmed.** If one additionally assumes a global continuous mass graph `m(v)` on compact `Gamma_L\H^3`, then its variation is bounded (`R4-3_report.md:145-148`). “Automorphic” is the precise term; “periodic in velocity” is only an analogy. For a smooth small deformation with bounded hyperbolic derivatives, the high-energy group-velocity correction is of order `epsilon m^2/E^2`, and ordinary mass thresholds receive only relative order-`epsilon` shifts (`R4-3_report.md:148-152`). This is conditional on the mass-graph ansatz, not a consequence of `H_reg` alone.

**The velocity-lowering-emission claim is false as stated.** For `p = m(v)v -> p' = m(v')v' + k`, `k^2 = 0` gives the exact condition

`d_H(v,v') = |log(m(v)/m(v'))|`.

The inequality `m(v') < m(v)` used at `R4-3_report.md:153-155` is necessary but not sufficient. If `|grad_H log m| < 1`—in particular for a sufficiently small smooth deformation with order-one derivatives—the mean-value theorem makes the equality impossible for distinct velocities. Therefore neither a generic thresholdless channel nor the quoted rate `alpha epsilon m/hbar` is established. Remove “proved kinematics” from `R4-3_report.md:292`.

**Clock mapping:** the nonrelativistic expansion does contain a traceless quadratic momentum tensor of order `epsilon partial_i partial_j psi`, so comparison with SME `c_jk` is reasonable, but the factor and species/projection mapping remain suggested, exactly as admitted at `R4-3_report.md:156-159,300-301`. The quoted comparator scales are externally consistent: the neutron comagnetometer paper reports sensitivity at `10^-29`, and the Yb+ clock paper at `10^-21` ([Smiciklas et al.](https://pubmed.ncbi.nlm.nih.gov/22107506/); [Sanner et al.](https://www.nature.com/articles/s41586-019-0972-2)). They are not bounds on `epsilon_s` without the omitted derivatives and projections.

## 4. Section 4.1 finite-shell instability

### Reproduction and criterion

**The fixed-kernel calculation reproduces.** I reran `r43_moment_lv2_analyse.py`, `r43_zero_robust.py`, and the direct-enumeration `r43_tube_zero.py`. For the empirical-density five-shell weights `[-1,-2,-3,-5,-7]`, the first roots are `0.49897, 0.50141, 0.48817, 0.45649`; the second roots are `0.17650, 0.18001, 0.17700, 0.16475` (`scripts/r43_tube_zero.py:9-40`; `scripts/r43_tube_zero.out:3-25`). The first e-folding times are 1.99-2.19 lattice times, while the second are 5.56-6.07, so “about 2” describes only the first family.

**The instability implication is correct.** Absolute convergence makes the retarded symbol real and continuous on `p = i kappa u` in the forward tube (`C5_R3-1_report.md:117-128`). A sign change therefore gives a zero by the intermediate value theorem. With signature `(-+++)`, `exp(i p.x) = exp(-kappa u.x)` grows along future timelike evolution, so this zero is a genuine exponentially growing homogeneous mode (`R4-3_report.md:195-198`; `scripts/r43_tube_zero.py:1-4`). This is the standard retarded nonlocal stability test; future-timelike imaginary zeros are likewise classified as unstable by [Aslanbeigi, Saravani, and Sorkin](https://arxiv.org/abs/1403.1622).

### Robustness and scope corrections

The first root of the displayed five-shell kernel is robust; the second is not established as robust. The worker's error bound preserves opposite signs at the wider first-root endpoints `kappa = 0.584, 0.438`, but it does not preserve the lower endpoint of the second-root bracket (`scripts/r43_zero_robust.out:1-5`). More fundamentally, the empirical densities differ from the counting estimates by as much as 0.7617%, not the unproved expected 0.03% (`scripts/r43_moment_lv2_analyse.out:1-13`). Re-solving the moment conditions with the counting densities preserves a direction-0 sign change between `kappa = 0.56` and `0.40` and gives sampled sign changes in all 32 directions, but removes the direction-0 second bracket (`r43_referee_checks.py:10-67`; `r43_referee_checks.out:1-5`). Thus the Planck-rate first instability is solid for this representative kernel; the `kappa about 0.17` zero is estimator-sensitive.

There is also data reuse: `nu_emp` is obtained from the directional mean at the smallest sampled `kappa`, then used to impose the moment conditions (`scripts/r43_moment_lv2_analyse.py:11-24`). Consequently the agreement `mean_u S_w = LI` in every table's `kappa = 0.035` row is exactly built in, not an independent asymptotic check (`scripts/r43_moment_lv2_analyse.out:15-29`). `r43_zero_robust.py` perturbs the LI subtraction while holding the empirical weights fixed (`scripts/r43_zero_robust.py:1-16`); it does not test kernels whose moment weights are re-solved after changing the density.

The broad reading at `R4-3_report.md:205-209` therefore needs narrowing. With count-density reconditioning, the four five-shell families and the min-norm family still show sampled zeros in all 32 directions, but the two optimized 12-shell families show none on the sampled grid (`r43_referee_checks.py:69-92`; `r43_referee_checks.out:6-12`). This does not prove stability—unsampled zeros may exist—but it defeats the stated robustness of “every tested moment-conditioned kernel.” Also, the relative LV is below one at several `kappa < 0.5` values for the optimized fits, directly contradicting “dominates at every `kappa lesssim 0.5`” (`scripts/r43_moment_lv2_analyse.out:95-125`). The `kappa^(-2.3...-3.2)` range applies to the four ordinary five-shell choices and min-norm choice, not both optimized choices, whose reported fitted slopes are `-0.55` and `-4.70` (`R4-3_report.md:179-191`). These are finite-window, oscillatory fits, not proved asymptotics.

Accordingly, the valid checked statement is instance-level: the explicitly fixed empirical five-shell kernels and min-norm kernel have large long-wavelength LV and sampled tube zeros; the first zero of the showcased kernel is robust to the available alternate density estimator. It is not a theorem about finite-shell kernels, and the optimized-weight universality claim is not robust.

## 5. R3-1 correlation correction

**Confirmed.** R3-1 says individual “pairwise pattern correlations are -0.01 to -0.04” (`C5_R3-1_report.md:195-197`), but its script actually prints the mean of all off-diagonal correlations (`R3-1_scripts/r31_multishell.py:29-33`). Direct recomputation gives 55 of 66 pairs with `|c| > 0.9` at `kappa = 0.1`, median `|c| = 0.97265`, and eight pairs remaining above 0.9 in magnitude at every sampled `kappa` (`scripts/r43_moment_lv2_analyse.out:141-205`; `r43_referee_checks.out:13-14`). The statement that cancellation, not independent-shell averaging, explains the small mean is justified on the sampled rapidity patch. The attribution to one low automorphic eigenfunction remains a suggestion, as the worker labels it at `R4-3_report.md:268-272`.

## 6. Reading and labels

**INCONCLUSIVE is the correct fixed reading.** PASS is not established because the massive amplitude, singular Bragg-cone response, and a stable effective law remain unbuilt; FAIL is not established because no existing stable law is shown to violate an observational bound at `a = l_P` (`TESTS.md:2822-2825`; `R4-3_report.md:51-62`). The current external scales quoted for GRB timing/polarization are also consistent with the literature ([LHAASO GRB 221009A](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.133.071501); [Götz et al.](https://arxiv.org/abs/1408.4121)), but they do not change that reading.

Relabel as follows: §3.1 remains **checked**; continuous Lemma Z is **proved mod recalled dynamics**, with the measurable and domain qualifications above; its dispersion consequence is **proved only for regular null/spacelike scalar branches**; §3.3 boundedness is **conditional**, emission kinematics is **not confirmed**, and clock mapping remains **suggested**; §4.1 fixed empirical-kernel roots and the instability criterion are **checked**, the representative first root is **robust**, the second root and all-optimized-kernel generalization are **not robust**, and §4.2 stays **suggested**; §5 is **checked**.

## Strongest correct statement

At Planck spacing, every listed process lies 27.2-44.2 decades below the invariant reciprocal-gap scale, while at `a = 10^-19 m` LHC and UHECR-air invariants exceed that scale, which opens but does not size umklapp channels. For cocompact `Gamma_L`, every orbit on each time-oriented punctured null cone is dense in direction and scale, and generic spacelike-shell orbits are dense; continuity therefore makes every scalar invariant on the spacelike-plus-null domain a function of `p^2`, excluding regular null/spacelike per-realization LV while leaving bounded timelike mass-like and singular Bragg-cone sectors open. Numerically, the specified empirical five-shell retarded kernel has a robust first forward-tube zero at `kappa = 0.456-0.501` (still bracketed by `0.40-0.56` after count-density reconditioning), hence a genuine growing mode with an e-folding time of about two lattice times; a second `kappa about 0.17` zero and the claim for every optimized moment-conditioned kernel are not robust. The shell patterns are indeed mostly strongly correlated on the sampled patch. Since no stable law supplies a computed Planck-spacing bound violation, the fixed reading remains **INCONCLUSIVE**.
