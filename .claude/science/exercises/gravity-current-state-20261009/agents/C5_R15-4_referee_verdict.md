# VERDICT: CONFIRMED WITH CORRECTIONS

The bounded **FAIL** is supported. The construction and main no-go are sound, but several scope, numerical, and reproducibility qualifications are required.

1. **Constant annihilation and \(\kappa E=2S\): confirmed with a notation correction.**  
   Since the reader uses \(E=-d\rho/du\), an additive constant is exactly annihilated, and both designs satisfy \(G(0)=0,\ G(3)=G(4)=1\). In the lumpy case the exact identity is
   \[
   -\frac{d\mathcal E}{du}=2S,
   \]
   or \(\kappa E_{\mathcal E}=2S\); it is not generally \(\kappa(-d\rho_{\rm tot}/du)=2S\) pointwise. Those coincide homogeneously. “No new non-locality” means no additional slice average beyond R14-5’s already-global elliptic CMC clock; it does not make the model causal or fundamentally local. [R15-4_report.md:151](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R15-4/R15-4_report.md:151>), [R15-4_report.md:221](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R15-4/R15-4_report.md:221>).

2. **Lemma P2: confirmed.**  
   The two-register expression for \(H(t)\) is correct, and \(H\ge0\) plus the layer-cake representation proves \(\widehat\rho\ge0\) when \(Ee^{4u}\) is nondecreasing. Two harmless algebraic slips should be corrected: the layer-cake formula at line 165 has an extraneous factor \(4\), and for a release into rate \(x_s\), line 345’s derivative contains \(x_s\,{\rm release}\), not universally \(4\,{\rm release}\). Both terms retain the needed nonnegative sign. [R15-4_report.md:163](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R15-4/R15-4_report.md:163>), `scripts/r154_p2_random.out:1-4`.

3. **(a), transitions and numbers: confirmed with BBN qualifications.**  
   The convolution argument gives the width-independent bounds
   \[
   -\alpha_r\le\epsilon\le0.8\alpha_r\quad({\rm D1}),\qquad
   -\alpha_r\le\epsilon\le2.4803\alpha_r\quad({\rm R*}),
   \]
   and the R14-5/R13-3 transition numbers reproduce. The EW \(7.97\times10^{-13}\) and QCD \(8.89\times10^{-5}\) residuals also reproduce. [R15-4_report.md:158](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R15-4/R15-4_report.md:158>), `scripts/r154_reader.out:28-45,311-319`.

   The \(e^\pm\) calculation reproduces \(+0.431\) for D1 and a maximum \(+0.156\) for R*; at the tabulated \(0.070\) MeV point R* is \(+0.130\), so “\(+0.16\) at \(0.07\) MeV” is only approximate. These are equivalent energy-density shifts under instantaneous neutrino decoupling, not BBN-network predictions. **RECALLED:** the \(\Delta N_{\rm eff}\sim0.3\) observational scale, EW/QCD transition temperatures and released fractions, and the radiation-era comparator. [R15-4_report.md:200](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R15-4/R15-4_report.md:200>), `scripts/r154_bbn.out:6-15,66-75`.

   Seven of nine supplied scripts reproduced exactly. The two BBN outputs are stale relative to their current sources: `r154_bbn.py:55-61` now emits R* twice, while `r154_bbn_diag.py:7-8` uses a no-longer-present split sentinel and executes the whole BBN runner. The quoted values nevertheless reproduce.

4. **(b), identities and lapse positivity: algebra confirmed, physical scope narrowed.**  
   A1–A4, including
   \[
   \widetilde Q=\mathcal E_{\rm nc}+\sigma^2+\frac{\kappa}{2}(\rho+3p)_{\rm nc},
   \]
   are exact. Thus a reader of uniform \(\mathcal E\) avoids an additional density average. Positivity follows on an already-existing compact CMC slice if \(\mathcal E_{\rm nc}>0\) and the remaining pointwise term is nonnegative; “no recollapse” alone does not prove \(\mathcal E_{\rm nc}>0\). Global CMC existence remains assumed. The \(10^{-8}\)–\(10^{-7}\Lambda_{\rm obs}\) residuals reproduce only for the recalled linear BBKS inputs and suggested normalization; they are not a nonlinear-halo result. [R15-4_report.md:221](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R15-4/R15-4_report.md:221>), `scripts/r154_lumpy.py:71-106`.

5. **Lemmas N+ and N0: confirmed after tightening scope.**  
   N+ is correct for kernels with the required finite exponential moment: reheating positivity is equivalent to \(H(t)\ge0\), and integration by parts gives
   \[
   G(x)\le \frac{x(4-x)}3\quad(0<x<3),\qquad G(x)\le0\quad(x<0).
   \]
   To apply this to an evolving CPL curve, “it is phantom somewhere” is not by itself sufficient. The repair is that each fitted CPL history has the high-redshift asymptote \(x=3(1+w_0+w_a)<0\); hence a regular LTI reader asymptotically returns \(G(x)\rho_{\rm DE}\le0\), not the positive CPL density. The no-go therefore holds for the full CPL histories, not necessarily for an arbitrary finite observed-redshift interval. [R15-4_report.md:250](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R15-4/R15-4_report.md:250>).

   N0 correctly proves a dead band for readers continuous at zero input in the stated finite-window sup norm. Its quantitative bound additionally assumes local Lipschitz continuity. It does not exclude every infinite-memory or discontinuous nonlinear reader. [R15-4_report.md:245](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R15-4/R15-4_report.md:245>).

   \(\mathcal R^+\) is physically motivated by dust exactness and \(H^2\ge0\) after reheating, but linearity and \(u\)-translation invariance are model choices; `AX:94-95` does not itself imply LTI evolution. Thus it is a natural restricted signal-processing class, not the general reader class.

   The four quoted \((w_0,w_a)\) pairs exactly match [DESI DR2 v3, Table 5](https://arxiv.org/html/2503.14738v3), and DESI itself describes the crossing near \(z\simeq0.4\). The exact crossings of the four central fits are \(z=0.496,0.354,0.440,0.405\). The worker fixed \(\Omega_m=0.31\) for every fit (`scripts/r154_desi.py:24-28`), rather than using Table 5’s fitted values. With the latter, peak \(|\delta H/H|\) becomes 29.9–42.7% for D1 and 21.8–26.0% for R*, instead of the stated overall 24–43%. The failure remains overwhelming.

6. **The escape and present \(g\): confirmed at background level.**  
   The inverse system produces \(E_{\rm true}\ge0\); integrating it and adding an arbitrary invisible constant constructs a positive, non-phantom true DE density whose reader output is the target CPL background. The finite-start residual is at most \(4.4\times10^{-7}\Omega_{\rm DE}\). For R*, using the corresponding Table-5 \(\Omega_m\) values gives
   \[
   g_0/H_0^2=(-0.289,-1.085,-0.746,-0.913),
   \]
   confirming the reported \(-0.3\) to \(-1.1\) range. This is only a background escape: perturbations, ISW, lensing, and the constraint-sector response are uncomputed. [R15-4_report.md:274](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R15-4/R15-4_report.md:274>), `scripts/r154_desi.out:56-100`.

7. **Fixed FAIL clause: met, boundedly.**  
   With the regular-kernel hypothesis stated explicitly and the CPL-asymptote step supplied, N+ proves that no reader in the stated causal linear LTI positive-reheating class can both annihilate constants and track the full DESI-like CPL content. That satisfies the literal fixed clause at `TESTS.md:4985-4988`. It is not a universal no-go: nonlinear/state-dependent readers and readers allowed to become negative remain open.

8. **Relation to R15-1 and R15-6.**  
   R15-6’s Theorem L is correct for this linear fading-memory class: exactness on both dust and radiation forces \(g>0\) somewhere after a sufficiently fast release. More decisively, R15-1’s refereed result says **any** \(g\ne0\), of either sign, enables superluminal signalling. Therefore the regular reader repairs Prony’s singular/negative-density failure but does not repair the underlying model: \(g\ne0\) during transitions, and the DESI escape leaves \(g=O(H_0^2)\) today. [C5_R15-6_report.md:203](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R15-4/C5_R15-6_report.md:203>), [C5_R15-1_referee_verdict.md:17](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R15-4/C5_R15-1_referee_verdict.md:17>).

**Strongest correct statement:** Within the smooth R14-5 CMC model and an assumed existing positive-lapse foliation, D1 and R* are causal finite-state linear readers that exactly ignore additive constants, exactly read constant-\(w\) dust and radiation, remain nonnegative on \(\mathcal H_4\), and replace Prony’s phase-transition singularities by bounded transients; the lumpy identities are exact, while the quoted backreaction residual is only a recalled-input linear estimate. For regular causal LTI readers exact on dust and nonnegative after radiation reheating, positivity forces \(G(x)\le x(4-x)/3\) for \(0<x<3\) and \(G(x)\le0\) for \(x<0\), so no reader in that stated class tracks the full DESI DR2 CPL histories, whose early-time asymptotes are phantom. A non-phantom true DE can reproduce the same background through inverse reading, but it leaves \(g/H_0^2=O(1)\) today; since R15-1 establishes superluminal signalling whenever \(g\ne0\), this escape and the transition reader do not rehabilitate the underlying CMC model. Thus R15-4 is a bounded **FAIL** in \(\mathcal R^+\), consistent with—and operationally subordinate to—the broader causality FAIL already established by R15-1.