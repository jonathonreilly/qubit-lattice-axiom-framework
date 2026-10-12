# C3 lane M-A: referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-10)

# VERDICT: CONFIRMED WITH CORRECTIONS

**Correct M-reading: M-INCONCLUSIVE.** The worker’s M-PASS is not confirmed. The checker’s conclusion is substantially correct, but its \(R\simeq1.5\times10^{-60}\), slow-proton, and decoherence numbers remain conditional predictions of an unproved renewal closure—not established values of the observable.

## Findings

1. **Exact tools versus the claimed growth law**

   - The add-one resolvent identity is algebraically exact, including added and killed links, and the brute-force insertion test supports its implementation: [C3_M-A_report.md:72–82](C3_M-A_report.md:72).
   - The first-chaos lower bound
     \[
     \rho\int |\mathbb E D_zF|^2dz\leq\operatorname{Var}F
     \]
     and Poisson Poincaré upper bound are exact for square-integrable \(F\). But no controlled physical-parameter Poincaré upper bound was produced. The accessible Monte Carlo even gives two statistically problematic rows with \(\mathrm{Var}/FC<1\), so it is not a reliable extrapolating sandwich: [C3_M-A_report.md:154–173](C3_M-A_report.md:154), [work/out/sandwich_boot_CV16.out:3–8](work/out/sandwich_boot_CV16.out:3).
   - The shared-common-vertex decomposition is a valid formal renewal organization: consecutive stretches occupy disjoint Alexandrov intervals, and direct-link/indirect-path stretches are indeed incompatible. However, the exact kernel is \(S_{\rm true}=a^2P_1+E_2\), with \(E_2\) unevaluated: [C3_M-A_report.md:111–128](C3_M-A_report.md:111).
   - The number \(k_0=(2\pi\sqrt6)^{-1/2}=0.25490\) is established as the continuum-limit exponent of the **pure shared-link subkernel**. It is not established as the exponent of the full second moment or variance. The pair-path expansion has signed cross terms, so selecting the positive shared-link sector does not furnish a variance lower bound. Likewise, the asserted \(k_{\rm chaos}=0.2143\) is not derived as a lower bound for the complete first-chaos norm.
   - Therefore, **the \(0.2549\,m^2\ell\) growth remains a model for this observable**, albeit one with an exact pure-chain component. The simulations only reach the pre-exponential regime and do not test the physical \(M\tau\gtrsim1\) regime.

2. **The \(P_{\rm tr}\) correction is correct within the worker’s packet approximation**

   For normalized free Gaussian packets,
   \[
   |\bar F|^2\propto |\langle\psi_d|U(T)\psi_s\rangle|^2=P_{\rm tr},
   \]
   whereas the chain numerator contains endpoint packet norms. Thus the quoted chain ratio must be divided by \(P_{\rm tr}\). This is exact for the same paraxial, minimum-uncertainty Gaussian approximation used to derive the worker’s packet formula—not an exact finite-density Johnston result.

   My rerun reproduces:

   - \(P_{\rm tr}=8.33\times10^{-24}\) for the 1 MeV/c proton with \(1\) nm/\(1\) nm packets;
   - nominal \(C=1,\ k=k_0\): \(R_{\rm chain}=1.45\times10^{-60}\);
   - \(k_{\rm crit}/k_0=2.55\), ranging from \(2.49\) to \(2.58\) over the worker’s \(C\) scan;
   - several mismatched-width corners give \(k_{\rm crit}/k_0=2.65\)–\(2.97\).

   These reproduce the checker’s calculations: [work/verify/kcrit_overlap.py:18–42](work/verify/kcrit_overlap.py:18), [C3_M-A_report.md:310–320](C3_M-A_report.md:310).

   Consequently the 1 MeV/c proton fails the preregistered requirement that the conclusion survive every \(k\leq3k_0\): [work/PREREG.md:18–23](work/PREREG.md:18).

   Correction to the checker: \(1.45\times10^{-60}\) is the **nominal corrected-model value**, not a controlled value of the true \(R\).

3. **The two ARGUED steps remain load-bearing**

   - **\(E_2\):** The continuum estimate \(\int K_{\ge2}^2d^3x=m^2t/(8\pi)\) controls an overlap-free approximation, not the actual joint probability of two vertex-disjoint link paths. The claimed side-by-side phase-space suppression \(\ell/R\) is not supplied with a uniform bound, and shared empty-interval correlations can be exponentially enhanced. Thus
     \[
     M_{\rm true}=k_0m^2\ell[1+O((m\ell)^2)+O(M\ell)]
     \]
     is not controlled: [C3_M-A_report.md:124–128](C3_M-A_report.md:124).
   - **End factor \(C\):** Neither non-vanishing nor \(O(1)\) uniformity in packet width, propagation time, and overlap was derived. Scanning \(1/16\leq C\leq100\) is sensitivity analysis, not a bound. The missing \(P_{\rm tr}\) demonstrates that endpoint structure can carry very large factors: [C3_M-A_report.md:130–140](C3_M-A_report.md:130).

4. **Momentum scope and the M reading**

   The Campaign C3 instruction says to evaluate “the electron and the proton at laboratory momenta”; it does not impose a 1 MeV/c proton floor: [TESTS.md:479–487](TESTS.md:479). The preregistered grid therefore materially narrowed the fixed reading: [work/PREREG.md:16–24](work/PREREG.md:16).

   Conditional on \(k=k_0,\ C=1\) and the Gaussian-overlap closure, I find \(R=1\) by 1 km below approximately:

   - \(0.391\) MeV/c for 1 nm/1 nm;
   - \(0.330\) MeV/c for 1 µm/1 µm;
   - \(0.312\) MeV/c for 1 mm/1 mm.

   Those are ordinary laboratory proton momenta. They defeat an unrestricted M-PASS. They **do not trigger M-FAIL**, because Campaign C3 requires an exact or controlled law and the exponential rate and end factors are not controlled. The original E1′ PASS wording also required bounded noise, which the worker’s own exponential model violates: [TESTS.md:340–343](TESTS.md:340).

5. **Experimental comparison**

   - Ordinary perfect-crystal neutron interferometry has a typical transit time around \(25\,\mu\mathrm{s}\), far shorter than the conditional 10 ms neutron threshold, so it does not by itself exclude that number ([NIST review](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nbsspecialpublication711.pdf)).
   - qBounce Ramsey spectroscopy coherently evolves ultracold-neutron gravitational-state superpositions for \(T\simeq42.5\) ms between interactions, with approximately 19 ms interaction sections. That is conditionally in tension with a universal 10 ms elementary-neutron decoherence time ([qBounce experiment](https://arxiv.org/abs/2301.08583)).
   - Spatial \(^{87}\mathrm{Rb}\) atom interferometry has operated for 2.3 s, over six orders of magnitude beyond the claimed 1.2 µs full-mass prediction ([Rb-87 experiment](https://arxiv.org/abs/1305.1700)); atom interferometers have also maintained spatial coherence for up to 70 s ([Nature Physics](https://www.nature.com/articles/s41567-024-02518-9)).

   These are not direct exclusions of an **elementary Johnston scalar**. Neutrons, protons, and atoms are composite; neutrons and protons are also spin-\(\tfrac12\), not scalars. Moreover, the calculation gives ensemble variance of a single source-detector amplitude, whereas interferometric visibility depends on the covariance between two arms. The experiments would decisively exclude applying the chain law to a composite’s centre of mass using its total mass, but that mapping has not been derived.

## Strongest correct statement

For the smeared Johnston observable, the add-one identity and the general Poisson chaos and Poincaré inequalities are exact. Pair paths admit a legitimate shared-vertex renewal decomposition, and its pure shared-link sector has a continuum tachyonic exponent \(k_0m^2\ell\), \(k_0=0.25490\). The full variance exponent is not established because the vertex-disjoint kernel \(E_2\), signed cross-term cancellations, and packet end factors are uncontrolled, and the simulations never enter the exponential regime.

Within that unproved closure, the checker’s \(1/P_{\rm tr}\) correction is required and changes the nominal 1 MeV/c proton corner to \(R\simeq1.45\times10^{-60}\) and \(k_{\rm crit}\simeq2.5\)–\(3.0\,k_0\), invalidating the preregistered controlled-PASS margin. The same model predicts failure for sufficiently slow protons and severe conditional tension with neutron and atom interferometry if applied to composite centre-of-mass propagation. Neither PASS nor FAIL is supported by an exact or controlled law. **The correct reading is M-INCONCLUSIVE.**