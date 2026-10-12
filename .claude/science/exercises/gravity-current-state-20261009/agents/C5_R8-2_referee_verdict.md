# VERDICT: CONFIRMED WITH CORRECTIONS

The load-bearing free one-body mathematics survives independent derivation and the rerun. The principal corrections are that the Eötvös claim is not established for physical composite bodies, the R7-4 interacting obstruction is only conditional, the generic gap statement is an inequality rather than an equality, and option (c) overstates its microscopic Qubit cost. The registered reading is therefore **INCONCLUSIVE**, unless “Eötvös η” is explicitly weakened to a free-packet proxy.

1. **Conservation, Hermiticity, and first moment — confirmed.**

   The rerun completed in 236.9 s and reproduced the reported Ward, Hermiticity, forward-value, anomaly, doubler, and acceleration numbers ([r82_edge.out:37–74](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/scripts/r82_edge.out:37>)).

   Algebraically, for the dust kernel,
   \[
   F^{00}=\bar\epsilon,\quad F^{0i}=\bar\epsilon\Delta_i,\quad
   F^{ji}=\bar\epsilon\Delta_j\Delta_i,\qquad
   \sum_jD_j\Delta_j=\omega ,
   \]
   so both Ward components follow exactly. The continuum kernel obeys the same identity wherever \(D=q\), and scalar gluing preserves it ([R8-2_report.md:75–87](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/R8-2_report.md:75>), [r82_edge.py:141–170](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/scripts/r82_edge.py:141>)).

   Reversal of each divided difference gives Hermiticity precisely when
   \(D(q)^*=-D(-q)\). The proposed \(D=s_c+i\psi\), with \(s_c\) real odd and \(\psi\) real even, satisfies this condition ([R8-2_report.md:88](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/R8-2_report.md:88>), [r82_edge.py:120–127](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/scripts/r82_edge.py:120>)).

   Finally, real symmetry of \(F^{00}(k',k)\), together with \(F^{00}(k,k)=\epsilon(k)\), implies
   \(\partial_{k'}F^{00}|_{k'=k}=\frac12\nabla\epsilon\). Hence its dipole is exactly \(\frac12\{X,\epsilon\}\), with no diagonal improvement \(Y\), and it equals R7-1’s boost on box states ([R8-2_report.md:89–90](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/R8-2_report.md:89>)).

   Minor runner caveat: the gapped numerical profile uses `CubicSpline`, which is only piecewise \(C^2\); it is a surrogate for the report’s genuinely \(C^\infty\) exact integral and cannot itself certify asymptotic super-polynomial locality ([r82_edge.py:46–56](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/scripts/r82_edge.py:46>)).

2. **Lemma U — confirmed, with a physical-scope correction.**

   Continuity and a positive diagonal value guarantee a nonzero neighbourhood of \((k_0,k_0)\) at every box-boundary point, containing box-to-edge pairs. For a potentially complex kernel, the proof should say “nonzero” or “positive real part,” rather than simply \(F>0\) ([R8-2_report.md:109–112](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/R8-2_report.md:109>), [r82_edge.out:44–55](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/scripts/r82_edge.out:44>)).

   The statement that leakage “needs” momentum \(b/a\) is too broad. States already near the face couple across it with arbitrarily small \(q\); transfer of order \(b/a\) is needed only to take low-momentum matter near \(k=0\) directly to the edge. A nonzero vertex also does not by itself prove a real transition without appropriate gravitational Fourier support and energy conservation ([R8-2_report.md:113](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/R8-2_report.md:113>)).

3. **Theorem E — confirmed in its stated free, periodic-band scope.**

   The exact component identity is
   \[
   \dot P_i=-g_j\!\left[\delta_{ij}H+
   d\Gamma\!\left(\epsilon A_{ij}\right)\right],
   \qquad
   A=\operatorname{Hess}(\epsilon^2/2)-I .
   \]
   It follows directly from
   \([\,\frac12\{X_j,\epsilon\},p_i\,]
   =i\epsilon\,\partial_jp_i\), with \(p=\nabla(\epsilon^2/2)\)
   ([R8-2_report.md:115–124](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/R8-2_report.md:115>)).

   O2 Lemma F is the stationary-band-bottom, leading weak-field specialization. The arbitrary-\(k\) acceleration formula remains semiclassical—requiring a narrow isolated-band packet and slowly varying field—whereas the energy-current commutator above is the exact operator statement. It should not be described as an exact arbitrary-\(k\) position-acceleration theorem ([C5_O2_referee_full.md:91–104](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/C5_O2_referee_full.md:91>)).

   For one \(C^2\) periodic band, \(\int\operatorname{Hess}(\epsilon^2/2)=0\), so \(\langle A\rangle=-I\). I2 supplies the finite-multiband trace version, including crossings ([TESTS.md:1411–1416](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/TESTS.md:1411>)). Thus universal relativistic free fall for every state of a finite periodic band is impossible under this first-moment lapse coupling. The theorem does not cover nonperiodic towers, singular bands, nonadiabatic multiband/Berry dynamics, altered source bridges, or interacting composites.

4. **Doublers — confirmed. Option (b) needs one correction.**

   Periodicity and oddness imply \(s(\pi)=s(-\pi)=-s(\pi)\), hence \(s(\pi)=0\). Because the displayed profile is positive between \(0\) and \(\pi\), the \(2^d-1\) nonzero points of \(\{0,\pi\}^d\) are exactly the extra mass-\(m\) valleys ([R8-2_report.md:64–70](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/R8-2_report.md:64>), [r82_edge.out:30–34](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/scripts/r82_edge.out:30>)).

   Continuity proves only
   \[
   \inf_{k\notin B}\epsilon(k)\le \min_{\partial B}\epsilon
   =\sqrt{m^2+b^2},
   \]
   not equality for every extension—the literal profile itself has edge infimum \(m\). Equality holds for the specifically monotone gapped construction. The claimed **ceiling** is therefore correct, but the universal equality printed in the proof is false ([R8-2_report.md:145–148](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/R8-2_report.md:145>)).

5. **The fixed PASS criterion is not met for a physical Eötvös observable.**

   R7-1 accepted free matter because its earlier clause asked only for the box Poincaré algebra and leakage bound ([TESTS.md:3398–3407](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/TESTS.md:3398>)). R8-2 adds an Eötvös requirement ([TESTS.md:3455–3466](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/TESTS.md:3455>)).

   The report’s \(\eta\simeq|\Delta f_{\rm edge}\bar A_{\rm edge}|\) is explicitly imported as **SUGGESTED**, and neither interacting binding energy nor two compositionally different bound bodies have a universal stress constructed ([R8-2_report.md:30–35](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/R8-2_report.md:30>), [R8-2_report.md:170–185](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/R8-2_report.md:170>)). “Edge fraction equals zero because the chosen free sector contains no edge particles” proves a sector-selection statement, not a checked Ti/Pt-like Eötvös prediction.

   MICROSCOPE actually compared Pt- and Ti-alloy test masses and found \([-1.5\pm2.3_{\rm stat}\pm1.5_{\rm syst}]\times10^{-15}\), or \(2.7\times10^{-15}\) with errors combined ([arXiv 2209.15487](https://arxiv.org/abs/2209.15487), [arXiv 2209.15488](https://arxiv.org/abs/2209.15488)). A free stationary box packet does have the proxy value \(\eta=0\) at leading order, but accepting that as “Eötvös η” would require an explicit weakening of the fixed observable.

6. **Reliance on R7-4 — must be demoted to conditional.**

   R8-2’s statements that interacting matter “is blocked” and that the BT plateau interaction must vanish do not follow from the confirmed R7-4 result ([R8-2_report.md:161–168](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/R8-2_report.md:161>)).

   R7-4 established only the formal common-core relations \(i[H,D]=J\), \([H,J]=0\). Its S-matrix conclusion additionally needs essential self-adjointness and global exponentiation of \(D\), invariant domains, strong Møller intertwining, controlled clustering, and regular bands ([C5_R7-4_referee_verdict.md:35–55](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/C5_R7-4_referee_verdict.md:35>)). Under those extra assumptions, proper box-supported scattering is excluded; without them, the interacting universal stress and bound-body EP remain open ([C5_R7-4_referee_verdict.md:71–79](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/C5_R7-4_referee_verdict.md:71>)).

7. **Reading and option (c).**

   The correct registered reading is **INCONCLUSIVE**: option (a) is a valid universal free one-body \(O(h)\) Ward coupling, but the required physical Eötvös observable is not constructed; interacting matter remains open. The fixed FAIL is also unavailable because option (a) genuinely disproves a no-go against universal free coupling on box plus edge.

   Option (c) must be narrowed. I1 supports a complete unfolded reciprocal-lattice tower under integrated positive-energy Poincaré or suitable regular band-gluing assumptions; it establishes an infinite one-particle fibre in that class, not automatically an infinite microscopic on-site algebra ([C4_I1_referee_full.md:49–93](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/C4_I1_referee_full.md:49>)). Abstract finite-fibre realizations with position unbounded relative to lattice sites remain possible but are violently non-geometric ([C5_O2_referee_full.md:150–158](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-2/C5_O2_referee_full.md:150>)). The honest price is therefore “infinite one-particle tower or loss of uniformly site-tied geometry,” not unconditionally “violate the Qubit axiom.”

**Strongest correct statement:** R7-1’s literal periodic band has exactly \(2^d-1\) additional mass-\(m\) corner valleys, while a monotone edge extension can remove them but can place the edge threshold no higher than \(\sqrt{m^2+b^2}/a\). For free number-conserving matter there exists a smooth, quasi-local, symmetric and Hermitian box-plus-edge stress kernel satisfying the stated linear Ward identity exactly; its energy integral is the full Hamiltonian and its first energy moment is \(\frac12\{X,\epsilon\}\), hence R7-1’s boost on box states. Continuity forces this density to have box-edge matrix elements, and the associated uniform-lapse current obeys \(\dot P_i=-g_j[\delta_{ij}H+d\Gamma(\epsilon A_{ij})]\) with \(A=\operatorname{Hess}(\epsilon^2/2)-I\); the periodic-zone mean is \(-I\), so every finite periodic-band realization has non-universally falling states somewhere. Low-energy free packets confined to the relativistic box have the proxy value \(\eta=0\) at linear order, but no universally coupled interacting stress or composition-dependent bound-body Eötvös observable has been constructed, and R7-4 excludes box-supported scattering only after additional global exponentiation and scattering-domain assumptions. Consequently R8-2 is **INCONCLUSIVE** against its fixed physical PASS criterion, despite its confirmed free one-body construction.