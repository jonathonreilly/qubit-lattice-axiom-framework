# C3 lane X2: referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-10)

## VERDICT

**CONFIRMED WITH CORRECTIONS — bounded FAIL.** The decisive result survives independently; it is not a general no-go for classical record substrates.

## Findings

1. **Lemma A is correct, but “shape-blind statistics” is too broad.** M1’s symmetric bond rates and M2’s balanced streaming plus doubly-stochastic collisions share a metric-independent stationary one-time law, conditional on the conserved closed class. Consequently, any metric-independent state-function stress has \(G_T(\omega)\equiv0\) when initialized stationarily. Two-time correlations and relaxation rates can still depend on the metric, so the broader wording at [C3_X2_report.md:255](C3_X2_report.md:255) should be narrowed to the statement proved at [C3_X2_report.md:121](C3_X2_report.md:121).

2. **The zero-frequency-noise argument is sound.** On a finite mixing closed class,
   \[
   S_T(0)=2\langle T,(-Q)^{-1}T\rangle_\pi
   =\sum_{\eta,\eta'}\pi_\eta k_{\eta\eta'}(u_{\eta'}-u_\eta)^2>0
   \]
   for a nonconstant state observable; reversibility is unnecessary. The exact small generators reproduce the positive results in [work/x2_exact_small.out:3](work/x2_exact_small.out:3), while the long runs give \(S(0)\simeq0.0068\) for M1 and \(0.50\) for M2 at [work/x2_long.out:11](work/x2_long.out:11) and [work/x2_long.out:27](work/x2_long.out:27). Thus \(n_S=0\).

   Minor qualification: \(0.006684\) is the grand-canonical/thermodynamic-limit value identified in [work/x2_ssep_exact_S0.py:3](work/x2_ssep_exact_S0.py:3). For the actual fixed-\(N\), \(L=16\) simulation the corresponding canonical value is about \(0.006690\), an immaterial 0.1% correction.

3. **The response calculations are correct for the coded observables, except for one preregistration mismatch.** The linear contact responses are \(-0.0700236\) for M1 and \(-0.1000163\) for M2’s attempted-stream count, matching [C3_X2_report.md:134](C3_X2_report.md:134). However, the preregistration defines an M2 hop as a **configuration-changing** stream event at [work/PREREG.md:24](work/PREREG.md:24), while the simulator increments `K` even when equal contents are exchanged and the state is unchanged at [work/x2gas.c:103](work/x2gas.c:103). Under the literal preregistered definition, the M2 contact value is approximately **−0.0950**, not −0.1000. It remains decisively nonzero.

4. **The M3 response is confirmed.** Independent momentum-space differentiation and finite-difference convergence reproduce the crystal values and new dilution masks reproduce the stated \(+0.09\)–\(+0.19\) range; see [work/x2_m3_frozen_dilution.out:2](work/x2_m3_frozen_dilution.out:2). M3 therefore fails on \(\operatorname{Re}G_T(0)\ne0\).

5. **The reading needs no “common exponent.”** The preregistration explicitly distinguishes \(n_S\) and \(n_G\) at [work/PREREG.md:36](work/PREREG.md:36). An identically zero \(\operatorname{Im}G_T\) satisfies any required vanishing order; the gas fails solely because \(S(\omega)\to S(0)>0\), hence \(n_S=0\). The “common exponent/minimum” language at [C3_X2_report.md:311](C3_X2_report.md:311) is unnecessary.

6. **The FDT conclusion is correct; its temperature gloss is not.** M1 is reversible but the perturbation is purely kinetic and leaves forward/reverse ratios unchanged; M2 is nonreversible. Thus the equilibrium potential-coupling FDT does not connect their noise and response, as correctly tabulated at [C3_X2_report.md:155](C3_X2_report.md:155). Calling this an “infinite effective temperature” at line 162 is unjustified precisely because FDT fails.

7. **M3’s quenched spread is not per-realization temporal noise.** The connected spectrum is defined per realization at [work/PREREG.md:34](work/PREREG.md:34). Therefore the realization-to-realization static-stress spread at [C3_X2_report.md:233](C3_X2_report.md:233) should not be called an \(\omega=0\) atom in that spectrum. M3 already fails on its static response, so this does not affect the verdict.

## Strongest correct statement

Under the preregistered T-3 metric coupling, at \(k=0\), on finite tori and for the tested stresses, the FR3 gases have a common metric-independent stationary one-time law. Their configurational stresses therefore have \(G_T(\omega)\equiv0\), but nonzero white stress noise gives \(n_S=0\). Their activity stresses additionally have nonzero instantaneous contact responses. The tested frozen-dilution scalar has positive static shear response. Hence **every preregistered model fails the fixed X2 reading**. This establishes a bounded model failure—not a theorem excluding other classical gases, couplings, stress definitions, nonzero momenta, or formation dynamics.