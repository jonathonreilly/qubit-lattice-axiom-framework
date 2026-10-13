# VERDICT: CONFIRMED WITH CORRECTIONS

All five R17-7 runners reproduced their stored outputs byte-for-byte; all twelve inherited recheck artifacts also match. The worker’s final **OPEN** reading survives, but three claims require material narrowing: dark energy above \(e_0\) need not be temporary, the “one tuning per order” statement is proved only through \(m^4\), and Bianchi does not exclude \((S'_{\rm current})\) in every conceivable local covariant completion.

## Per-item findings

1. **Late universe — algebra confirmed; “temporary” corrected.**  
   Provided \(V_{\rm late}\) means the total vacuum-state energy density of the same Hamiltonian used to define \(e_0\), the variational inequality gives
   \[
   \widetilde\Lambda_{\rm late}=\kappa(V_{\rm late}-e_0)\ge0,
   \]
   and P93 gives equality. This does not imply temporary acceleration or eventual deceleration. The report’s own exponential fit has \(\lambda=0.639\); its scalar-dominated attractor has \(w=-1+\lambda^2/3=-0.864\) and \(a(t)\propto t^{2/\lambda^2}\simeq t^{4.90}\), hence eternal power-law acceleration while \(H\to0\). Thus the general claims at [R17-7_report.md:155–166](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/R17-7_report.md:155>) must be restricted; the PNGB example can be temporary, but “content above \(e_0\)” need not be.

   The proxy arithmetic is correct: \(1-0.241/0.529=54.4\%\) and \(1-0.200/0.529=62.2\%\), matching [r177_late_universe.out:2–10](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/scripts/r177_late_universe.out:2>). Its scope is exactly as disclosed: synthetic distances from one recalled CPL curve, diagonal approximate errors, no covariance/CMB/SNe, and a fitted amplitude—not a likelihood or evidence ratio ([R17-7_report.md:168–178](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/R17-7_report.md:168>)). “The phantom side is not reproducible” is valid only for canonical scalars with \(w\ge-1\), not for all content allowed by (S). The official DESI result supports the favored \(w_0>-1,w_a<0\) quadrant, but not these 54–62% numbers ([DESI DR2 Results II](https://arxiv.org/abs/2503.14738)).

2. **Grid zero-point — substantially confirmed.**  
   If \(H\) is the full law Hamiltonian, \(E_0[H]\) includes its zero-point contribution definitionally. Subtracting the scalar \(e_0\) leaves
   \[
   (\rho_{\rm res},p_{\rm res})=(0,\rho_0+p_0),
   \]
   and the reported \(1.2\)–\(1.8\times10^{123}\rho_\Lambda\) per real scalar at \(a=\ell_P\) reproduces ([r177_gridvac_sector_cov.out:7–14](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/scripts/r177_gridvac_sector_cov.out:7>)).

   Under the stipulated (d-i) bridge, the pressure is algebraically invisible in Lemma V’s homogeneous source equations; this is a bridge-specific result, not a generic consequence of GR or (S). Under (d-ii), separate site-frame conservation indeed requires \(\rho_v+p_v=0\), also locally in a nonconstant lapse ([C5_R15-1_referee_verdict.md:15](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/C5_R15-1_referee_verdict.md:15>)).

   The expansion
   \[
   E(m^2)=E_0+c_2m^2+c_4m^4+\cdots,\qquad
   c_4=\left\langle\frac{\operatorname{tr}A}{48\epsilon^3}\right\rangle
   \]
   is correct. Independent grids converge to \(t_*=0.00117\) and \(c_4=0.03880\), matching [r177_enthalpy_orders.out:1–10](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/scripts/r177_enthalpy_orders.out:1>). This proves that one \(c_2\) tuning is insufficient. “One tuning per order per species” is only a generic extrapolation beyond \(m^4\), not a theorem; symmetries, cross-species cancellations, or correlated coefficients could reduce the count.

   The full-stress conclusion is correct for the defined \((S\!-\!T)\): subtracting one fixed late-ground-state tensor does not conserve an arbitrary preferred-frame \((\rho_0,p_0)\) tensor through expansion or phase changes, so it does not remove the need for exchange. A dynamical conserved compensator would be a new bridge, not this \((S\!-\!T)\) ([R17-7_report.md:208–213](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/R17-7_report.md:208>)).

3. **Metastability — numbers confirmed; universal Bianchi no-go rejected.**  
   The recalled arithmetic is correct:
   \[
   \frac{0.015(10^{17}\,\mathrm{GeV})^4/4}{\rho_\Lambda}=1.49\times10^{112},\qquad
   \frac{0.013M_P^4/4}{\rho_\Lambda}=2.87\times10^{120}.
   \]
   These are conditional SM-extrapolation/cutoff estimates, not measured vacuum energies; without a UV cutoff the negative-quartic approximation has no finite \(E_0\). The qualitative metastability premise is supported by the cited NNLO SM studies ([Buttazzo et al.](https://arxiv.org/abs/1307.3536), [Degrassi et al.](https://arxiv.org/abs/1205.6497)). Preserving (S) and the observed small \(\Lambda\) therefore requires our vacuum to be the true minimum to extraordinary accuracy—through stabilization, UV/lattice lifting, or different SM inputs ([R17-7_report.md:215–221](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/R17-7_report.md:215>)).

   \((S'_{\rm start})\) is a causal constant-reference alternative, but it is not a rescue of (S) itself: it adds basin structure, a first reading, loss of positivity, and P94′ ([R17-7_report.md:236–247](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/R17-7_report.md:236>)).

   For \((S'_{\rm current})\), Bianchi proves only:
   \[
   G_{\mu\nu}=\kappa\!\left(T_{\mu\nu}-C(x)g_{\mu\nu}\right),\quad
   \nabla^\mu T_{\mu\nu}=0
   \;\Longrightarrow\; \partial_\nu C=0 .
   \]
   Thus a varying algebraic \(C(x)g_{\mu\nu}\) with separately conserved \(T\) is excluded. “Every local covariant form” is too strong: a local scalar/gradient, wall, four-form, or other exchange sector can carry \(\partial_\nu C\) while the total stress remains conserved. R15-1’s \(g\ne0\) signalling theorem is specific to its elliptic CMC constraint-fluid model, not all local covariant exchange theories ([C5_R15-1_referee_verdict.md:17–19](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/C5_R15-1_referee_verdict.md:17>)). Exact causal current-basin cancellation remains unconstructed and open, not universally no-go.

4. **Covariant form — confirmed conditionally.**  
   The sign is correct:
   \[
   G_{\mu\nu}+\Lambda_*g_{\mu\nu}=\kappa T_{\mu\nu},
   \qquad \Lambda_*=-\kappa e_0 .
   \]
   Once \(e_0\) is stipulated as a fixed scalar law parameter, this Einstein equation is local, covariant, and non-signalling. What is not local or manifestly covariant is the selection map \(H\mapsto\lim_VE_0(H_V)/V\), especially for a preferred-time lattice Hamiltonian. Thus the equation is a covariant embedding of the principle, not a derivation of \(e_0\) from local covariant data; the grid enthalpy bridge remains an additional condition ([R17-7_report.md:249–262](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/R17-7_report.md:249>)).

5. **Lemma X and records — confirmed with scope.**  
   Pinching satisfies
   \[
   \operatorname{Tr}[H\,\mathcal D(\rho_0)]-E_0=-\langle H_{\rm off}\rangle_0\ge0.
   \]
   Equality means the pinched state is supported entirely in the ground subspace; for a unique ground state, that state must be a record-basis vector. The KS numbers—dense excess \(1.1938/a^4\) and first-record mean cost \(2.38/a\)—reproduce ([r177_records.out:1–14](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/scripts/r177_records.out:1>)).

   The \(1.05\times10^{123}\rho_\Lambda\) statement is an energy density per staggered field, conditional on the KS law, nonselective R-proj pinching, and \(a=\ell_P\). The \(2.4/a\) value is the first isolated-record average and is not additive through dense recording. R-proj and R-label are explicitly alternative downstream readings, not Record-axiom content ([R17-7_report.md:99–102](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/R17-7_report.md:99>); [MINIMAL_AXIOMS_2026-06-29.md:75–90](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/MINIMAL_AXIOMS_2026-06-29.md:75>)). Therefore projections instantiate P4 heating; inert labels cost nothing.

6. **Reading — OPEN is correct.**  
   EXCLUDED-PRINCIPLE is not met because fixed-\(e_0\) GR supplies a non-signalling covariant form and no observation presently contradicts every completion. VIABLE-PRINCIPLE is not yet met in the fixed “checked” sense: the needed stabilization/P93, (d-i) or pairing, and R-label bridge are unresolved rather than demonstrated. There is a conditionally viable branch, but it remains conditional on precisely those open source/action and record identifications. This matches the fixed fallback at [TESTS.md:6040–6047](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-7/TESTS.md:6040>).

## Strongest correct statement

If \(e_0\) is a well-defined total ground-state energy density and the source/action rule \(C=e_0\) is stipulated, it enters Einstein’s equation as a fixed, non-signalling constant and makes the residual vacuum energy \(\kappa(\rho_v-e_0)\) nonnegative, vanishing when our vacuum is the true ground state; present acceleration must then be supplied by content above that state, but it need not be temporary. The tested canonical thawing models recover 54–62% of one synthetic CPL-versus-\(\Lambda\)CDM BAO-distance gap and cannot realize \(w<-1\), which is only a proxy-level statement. On the preferred grid, scalar subtraction leaves a Planck-sized enthalpy unless the (d-i) exchange bridge or structural cancellations are supplied; the \(m^4\) coefficient \(+0.0388\) proves one \(m^2\) tuning insufficient but not a universal tuning count. SM extrapolation makes P93 a severe stabilization condition, while R-proj records produce the existing P4 heating cost and R-label records do not. A varying current-basin subtraction violates Bianchi only without a local carrier, not in every possible covariant completion. Therefore the principle is not excluded and has conditionally viable realizations, but the registered result remains **OPEN**.