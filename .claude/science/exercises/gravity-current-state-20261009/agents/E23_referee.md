# E2/E3 and Lemma P: referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-09)

Paths below point to the referee's scratch copy; the same files are in `scripts/E23/` and `agents/`.

## Verdicts

- **E2: CONFIRMED WITH CORRECTIONS.** “FAIL (bounded)” is justified for the tested scalar models and densities. It is not an exhaustive no-go for every \(p\), coupling, or stress functional.
- **E3: CONFIRMED WITH CORRECTIONS.** All three tested routes fail the fixed joint criterion, but the quasicrystal \(S(0)\) claim and universal frozen-substrate language are too strong.
- **Lemma P: CONFIRMED WITH CORRECTIONS.** Its SL/AN second-moment obstruction is sound after narrowing “ergodic,” adding the AN singular-orbit argument, and distinguishing white continuous spectrum from a possible zero-frequency atom.

## 1. Validation

The implementation is correct. The TT matrices are Frobenius-orthonormal and split as \(E_g\oplus T_{2g}\) in [e23_core.py:23](e23_core.py:23). For
\[
s(t)=D^Te^{th}D,
\quad s'=D^ThD,\quad s''=D^Th^2D,
\]
the code constructs the correct \(L'\), \(L''\), and divided-difference spectral Hessian, including degenerate eigenspaces, in [e23_core.py:107](e23_core.py:107).

My rerun reproduced:

- pd crystal: \(E_g=0.0473827,\ T_{2g}=0.0140046\);
- small-\(p\) pd slopes: \(+0.032934p,\ +0.038466p\);
- small-\(p\) nn slopes: \(+0.192450p,\ -0.288675p\);
- all displayed finite differences to the printed precision.

See [E2_0_validate.out:1](E2_0_validate.out:1), [E2_0_validate.out:5](E2_0_validate.out:5), and [E2_0_validate.out:11](E2_0_validate.out:11).

There is also a useful analytic strengthening for nn: in every off-diagonal \(T_{2g}\) direction, axis bonds have \(s'=0\) and \(w's''<0\). Thus \(L'=0\), \(L''\preceq0\), and the bosonic stiffness is strictly negative whenever affected occupied bonds exist. Hence the nn \(T_{2g}\) mean is negative for every \(p>0\), not merely at sampled \(p\).

## 2. E2 means and noise

The mean table is faithfully generated and shows no simultaneous two-channel zero at any sampled \(p\); the light pd boson crosses only in \(E_g\), while \(T_{2g}\) stays positive. See [E2_4_table.out:10](E2_4_table.out:10) and [E2_4_table.out:28](E2_4_table.out:28).

All 24 extended bosonic fits lie between \(-0.596\) and \(-0.375\), within approximately \(2\) quoted SE of \(-1/2\), as reported in [E2_3_pooled_fits.out:1](E2_3_pooled_fits.out:1). But these cover only \(p=0.1,0.3116,0.5\), not every \(p<1\). Some three-box fits outside that set fail the preregistered “within 2 SE” white criterion—for example nn \(p=0.9\), \(q\simeq-0.234\pm0.113\), in [E2_1_nn.out:99](E2_1_nn.out:99). This is finite-size inconclusiveness, not evidence for suppression.

The fixed-\(N\), whole-periodic-box estimator is **not generally a lower bound on \(S(k\to0)\)**. Conditioning reduces the corresponding grand-canonical zero-mode variance on average, but there is no general ordering between the canonical \(k=0\) mode and the nonzero-\(k\) limit. The code measures \(\sqrt{\langle N\rangle}\,\mathrm{sd}(K/N)\), effectively a compensated total \(K-\bar\kappa N\), not a spatial spectrum directly; see [E2_1_frozen_dilution.py:51](E2_1_frozen_dilution.py:51). The observed \(N^{-1/2}\) scaling is strong evidence for extensive fluctuations, but calling it a rigorous \(S(0)\) bound requires locality/mixing assumptions or direct nonzero-\(k\)/window measurements.

## 3. Growing dilution

Theorem A is applied correctly: independent activation times give Bernoulli occupation with
\[
p(t)=1-e^{-\lambda t}
\]
at every fixed time; see [record note:64](RECORD_ACTIVATION_CRITICALITY_AND_CONDITIONED_PLANAR_MODELS_BOUNDED_THEOREM_NOTE_2026-10-08.md:64) and the implementation at [E2_2_growing.py:31](E2_2_growing.py:31). The stage means accordingly reproduce frozen Bernoulli means.

The instantaneous, adiabatic ground-state reading is a fair equilibrium interpretation of the requested vacuum energy. It does **not** test actual state preparation, excitations from adding degrees of freedom, temporal averaging, or any dynamical cancellation. Thus growing dilution adds memory between stages but no new instantaneous protection.

## 4. Quasicrystal

The construction is correct. The stacked physical/internal projectors are orthogonal to \(1.1\times10^{-16}\), with determinant \(-1\); the spherical window has volume exactly one, so the regular model set has density one. See [E3_a_core.py:16](E3_a_core.py:16).

Quadratic TT isotropy is exact for the thermodynamic hull mean: the five-dimensional traceless-symmetric representation is irreducible under the icosahedral group. It is not exact for an arbitrary finite, generically shifted patch. The symmetric-centre patch demonstrates the exact finite symmetry at [E3_a1_symmetric_centre_patch.out:1](E3_a1_symmetric_centre_patch.out:1).

The full-functional values reproduce as:

- \(R=1.8:\ -0.0002046\pm0.0000750\);
- \(R=2.2:\ +0.0454185\pm0.0000885\).

The quoted errors are finite phason-patch scatter, not controlled thermodynamic errors. Changing the interior buffer moves the \(R=1.8\) estimate by its quoted uncertainty and the \(R=2.2\) estimate by about \(10^{-3}\). Thus “\(R=1.8\) is the crossing” is too precise, but the near-zero is plainly not range-protected.

An independent thermodynamic pair-frequency calculation using the spherical-window covariogram gives equal values in all five channels:
\[
R=1.2:-0.06704484,\quad
1.8:+0.00263459,\quad
2.2:+0.19767328,\quad
3.0:-0.09153786,
\]
confirming the scan in [E3_a5_pair_level_scan.out:1](E3_a5_pair_level_scan.out:1). Zeros occur only after choosing the range.

Full-functional \(S(0)=0\) is **not established**. Its window study reaches only radius \(3\) and \(k=0.5\), on one large patch, in [E3_a2_patch_noise.out:1](E3_a2_patch_noise.out:1). The stronger 35-fold suppression is for the pair functional, not the spectral square-root functional; the largest windows also have only four or one independent centres in [E3_a7_pair_level_Sk.out:2](E3_a7_pair_level_Sk.out:2).

A polyhedral Ammann–Kramer window would preserve icosahedral quadratic isotropy but change all pair frequencies and the full spectrum. It is untested and does not inherit the spherical-window numbers.

## 5. Hyperuniform substrates

The stealth optimization is genuinely extremely converged, but the literal “every realization has \(\Phi/N<10^{-26}\)” is not documented. Logs report \(1.2\times10^{-26}\) and \(1.9\times10^{-26}\), and the extension records only its last realization; see [E3_b3.out:3](E3_b3.out:3). These residuals are nevertheless negligible. An independent seed reached \(4.3\times10^{-28}\).

The \(m^2=1\) mean near \(+0.024\) is real and robust through \(L=12\). Direction-centred refits give
\[
q_{E_g}=-0.405\pm0.077,\qquad
q_{T_{2g}}=-0.504\pm0.077,
\]
agreeing with [E3_b4_stealth_pooled.out:1](E3_b4_stealth_pooled.out:1). This is convincing finite-size evidence that density stealthiness does not transfer to this stiffness functional, subject to the fixed-\(N\) spectral caveat above.

The perturbed-\(Z^3\) mean at \(s=1.2,1.6\) is unresolved relative to the iid control, as [E3_b2.out:9](E3_b2.out:9) shows. This does not affect E3’s verdict: those cases retain iid-scale stiffness fluctuations, and the independently tested stealthy construction already fails both practically relevant conditions.

## 6. Lemma P

The corrected theorem is:

> For a stationary simple point process in \(\mathbb R^d\), \(d\ge2\), with \(0<\rho<\infty\) and finite local second moments, SL(d)—or AN—invariance implies that the reduced factorial second-moment measure is \(\rho c\,dx\), \(c\ge1\). Hence  
> \[
> \operatorname{Var}N(W)=\rho|W|+\rho^2(c-1)|W|^2.
> \]
> Moreover, \(c=1\) iff density averages converge to \(\rho\) in \(L^2\). Translation ergodicity is sufficient, not necessary.

Specific corrections:

- The homogeneous-space measure argument and removal of the zero atom by simplicity are sound; [supervisor_thread.md:67](supervisor_thread.md:67).
- “\(c=1\) iff ergodic” is valid only if “mean-ergodic” means density self-averaging. A Haar-random affine unimodular lattice has \(c=1\) but retains a translation-invariant random lattice shape, so it is not fully translation-ergodic. Its Poisson first and factorial second moments are given in [Marklof’s lecture notes](https://mathweb.tifr.res.in/conferences/Jens-Marklof/TATA_LectureONE.pdf).
- For \(c>1\), the spectrum is white for \(k\ne0\) **plus a zero-frequency atom**:
  \[
  S=1+(2\pi)^d\rho(c-1)\delta_0.
  \]
  Thus [supervisor_thread.md:65](supervisor_thread.md:65) excludes ensemble hyperuniformity but should not simply call every case “white.”
- The AN conclusion is correct but its proof is incomplete. The two open half-spaces do not exclude singular mass on \(x_d=0\). That mass vanishes because
  \[
  \operatorname{diag}(t,\ldots,t,t^{-(d-1)})
  \]
  contracts this hyperplane, while invariance, local finiteness, and no atom at zero force its measure to be zero. Pair-exchange symmetry—not assumed parity invariance—then equates the two half-space constants. “AN already suffices” is justified; “smallest group” is not.
- The narrow corollary is correct: SL/AN law-symmetry protection and **ensemble density hyperuniformity** are incompatible. The broader statements at [supervisor_thread.md:73](supervisor_thread.md:73) and [supervisor_thread.md:75](supervisor_thread.md:75) are too strong: density noise does not imply stiffness noise, and lack of symmetry protection does not prove nonzero response.
- The coboundary caveat at [supervisor_thread.md:78](supervisor_thread.md:78) is essential. A divergence can give \(S_\tau(k)\sim k^2\); a double-curl construction can give \(k^4\), despite white density.
- In spacetime, Lorentz-invariant pair measures are constant on Lorentz orbits, but those include timelike/spacelike hyperboloids and null cones, with possible singular orbit measures. The simplified \(g_2(x)=G(x^2)\) statement requires an absolutely continuous density.

Relative to R3, Lemma P removes smooth pair-density assumptions and derives an exact count-variance obstruction directly from affine law invariance. R3 instead needs the response to vanish for every admissible pair kernel before its ODE forces \(\rho_2=a\); a zero for one kernel does not. See [R3_price.md:34](R3_price.md:34).

## 7. Final reading and strongest statement

Under the fixed readings, the bounded E2 and E3 FAIL verdicts stand: the tested diluted lattices never achieve both channel means zero and quiet stiffness; the spherical-window quasicrystal’s small response is range-dependent; stealthy density order leaves a positive mean and extensive stiffness fluctuations; and growing Poisson retains white fluctuations. The universal sentence “no frozen spatial pattern escapes” does not stand.

**Strongest correct statement:** Giving up the repeating pattern, or merely leaving some lattice sites absent, is insufficient in every tested free-field construction: iid dilution preserves cubic shear response and extensive disorder fluctuations; icosahedral order enforces equality of the five TT directions but not their vanishing; density hyperuniformity does not automatically hyperuniformize a nonlinear stiffness functional; and Poisson law symmetry protects only the ensemble mean. More generally, a frozen spatial law whose shape-blind mean is protected solely by SL(d), or already AN, symmetry cannot also have hyperuniform ensemble density fluctuations under Lemma P’s moment hypotheses. This is not a theorem that all frozen substrates fail or that sites must move: an exact realization-wise coboundary/conservation identity, another structural cancellation, a quenched/nonergodic mechanism, or a spacetime construction remains open. The defensible instruction is therefore to give up **ensemble-symmetry-only protection on a frozen spatial substrate**, not merely “the fixed repeating pattern” or “all sites present.”