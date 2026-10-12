# VERDICT: NOT CONFIRMED

The worker’s algebraic core is sound, but its scoped **PASS** is not. The construction is GR with a cosmological counterterm fixed to cancel the late vacuum; the packet neither derives nor dynamically enforces that cancellation. Under the requested adjudication, the campaign reading is therefore **INCONCLUSIVE**, not FAIL: a tuned \(g\equiv0\) counterexample defeats the universal FAIL clause, but does not constitute an untuned removal of \(\Lambda\).

1. Algebra of IE and Theorem Z — confirmed with qualifications.

   From \(3H^2=\kappa R\), total conservation \(\rho'_{\rm tot}=-3h\), and \(g=-2\dot H-\kappa h\),

   \[
   g=-\frac{\kappa}{3}(R'+3h)
     =\frac{\kappa}{3}(\rho_{\rm tot}-R)'.
   \]

   Hence, on a connected expanding interval, \(g\equiv0\) iff \(R'=-3h\) iff \(R=\rho_{\rm tot}-C\). Adding \(\widetilde\Lambda_{\rm late}=0\) fixes \(C=\rho_{v,\rm late}\). Theorem Z is therefore correct, although part (iii) is largely the definition of \(\widetilde\Lambda_{\rm late}\) plus conservation. See [R16-6_report.md:132–141](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/R16-6_report.md:132>) and [r166_identity.py:18–29](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/scripts/r166_identity.py:18>).

   IE guarantees \(g\equiv0\) for any homogeneous conserved history, but guarantees \(\widetilde\Lambda_{\rm late}=0\) only when its integration constant is initialized exactly to the late-vacuum-subtracted density. Those are distinct claims. Moreover, the inflation runner does not initialize IE from an equilibrium EoS: it directly sets \(R(t_0)=\rho_{\rm inflaton}(t_0)\), an exact state read [r166_inflation.py:18–27](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/scripts/r166_inflation.py:18>). Thus the inflation run tests an enlarged “one exact state read, then integrate” reader, not IE as defined at [R16-6_report.md:90–95](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/R16-6_report.md:90>). G0 remains an algebraically valid state-reader example.

2. Decisive tuning judgment — P-r166a is Lemma PT again as presently supplied.

   The literal PASS line does omit the words “without tuning”; it asks for removal, checks, and named prices [TESTS.md:5241–5244](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/TESTS.md:5241>). But the worker itself proves that \(g\equiv0\) leaves exact GR with a fixed cosmological term and admits that its rule is a stipulated c-number reference rather than adjustment [R16-6_report.md:40–49](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/R16-6_report.md:40>). On any fixed law,

   \[
   \lambda=-\kappa\rho_{v,\rm late}
   \]

   is physically the same relation as adding a counterterm \(-V_{\rm late}\). Calling it the EoS convention \(p(0)=0\) does not explain why gravity honors that matter-sector convention. No symmetry, local action, constraint, or renormalization theorem is supplied that forces the relation or makes it radiatively stable. Indeed, source/action identification is explicitly outside the axioms [MINIMAL_AXIOMS_2026-06-29.md:173–190](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/MINIMAL_AXIOMS_2026-06-29.md:173>), while Lemma PT identifies precisely this c-number cancellation problem [TESTS.md:2985–2988](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/TESTS.md:2985>).

   P-r166d is an additional exact-boundary cancellation for IE. An initialization error \(\delta\) remains forever as \(\widetilde\Lambda=\kappa\delta\) [R16-6_report.md:243–246](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/R16-6_report.md:243>). For a Planck-density start this requires roughly \(10^{-120}\)–\(10^{-123}\) relative accuracy, depending on reduced versus unreduced Planck convention. It would cease to be a numerical tuning only if an independently derived exact law identity enforced it; the scripts merely impose the value. G0 removes this integration constant but retains the same exact ground-state counterterm premise.

3. FAIL clause, bookkeeping, and inflation — universal FAIL refuted only conditionally.

   The report correctly distinguishes two statements:

   \[
   \widetilde\Lambda_{\rm inst}=0,\ g=0
   \quad\Rightarrow\quad
   \rho_{v,\rm inst}=\text{constant},
   \]

   whereas

   \[
   \widetilde\Lambda_{\rm late}=0,\ g=0
   \quad\Rightarrow\quad
   R=\rho_{\rm tot}-\rho_{v,\rm late}.
   \]

   Thus an earlier false vacuum, bag term, or inflaton potential can gravitate as energy above the final reference while \(g=0\). This is a valid counterexample to the broad claim that every out-of-equilibrium drop mathematically forces \(g\ne0\), but only after adopting the fixed late-vacuum subtraction. It does not refute Lemma PT; it accepts its tuned branch. The worker’s unqualified phrase “the FAIL text is false” at [R16-6_report.md:52–55](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/R16-6_report.md:52>) should therefore read “false given the late-vacuum counterterm premise.”

   The inflation argument itself is correct within \(3H^2=\kappa R\): subtracting the scalar potential as an instantaneous vacuum leaves kinetic/radiation-like stress and destroys potential-driven acceleration. What must gravitate is the potential above the fixed late reference—not necessarily something ontologically “non-vacuum.” See [R16-6_report.md:143–158](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/R16-6_report.md:143>).

4. Theorem NA — correct narrowly; landscape language too broad.

   The causal-indistinguishability proof is valid: if two histories and all reader inputs agree through \(u_1\), a common causal reader must choose the same constant \(C\), so it cannot equal two unequal final vacuum energies. See [R16-6_report.md:191–198](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/R16-6_report.md:191>). It does not exclude landscape laws generally: it excludes branches that are causally indistinguishable up to the branch event, use the same reader law, and end at unequal vacuum energies while demanding exact cancellation on both. An early branch label, law-supplied endpoint record, equal-energy vacua, noncausal input, or acceptance of a residual lies outside the theorem. Accordingly, “excludes landscape-type laws” at lines 58 and 245 should be narrowed.

5. Numerics — reproduced; they validate consistency, not the normalization premise.

   All five supplied runners reproduced their stored outputs byte-for-byte. An independent fixed-step RK4 implementation gave \(N_{\rm total}=68.1509\), \(N_{\rm accel}=65.2000\), and reheated fraction \(0.999999972\), agreeing with [r166_inflation.out:2–3](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/scripts/r166_inflation.out:2>). The bag-model values \(B/\rho_r=(0.355637,3.73333,28.8066,2333.33)\) also reproduce [r166_supercool.out:7–24](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/scripts/r166_supercool.out:7>). The EW estimate independently gives \(V_{\rm EW}^{1/4}=104.27\) GeV and \(V_{\rm EW}/\rho_{\rm rad}(160\,{\rm GeV})=0.00514\), matching the report. The \(e^\pm\), QCD, and DESI outputs also reproduce [r166_sm.out:1–13](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/scripts/r166_sm.out:1>) and [r166_desi.out:1–3](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-6/scripts/r166_desi.out:1>). However, IE’s \(g=0\) is imposed through its ODE and exact seed, so these runs cannot distinguish an enforced identity from the contested fine-tuned boundary condition. The QCD run is explicitly only a recalled parametrization and finite-difference check.

6. Prices.

   P-r166a is a new, unproved source/action bridge and the decisive counterterm tuning; P-r166b is a genuine conditional requirement, not established for the SM; P-r166c is justified only in Theorem NA’s narrow causal-branching class; P-r166d is an exact integration-constant condition of roughly 120–123 decimal orders for a Planck-era start. Naming these prices is honest, but does not convert them into an untuned solution.

Strongest correct statement: In the homogeneous R14-5 equations with conserved total stress and \(R>0\), \(g=(\kappa/3)(\rho_{\rm tot}-R)'\), so \(g\equiv0\) exactly characterizes ordinary GR with one constant subtraction, \(R=\rho_{\rm tot}-C\); choosing \(C=\rho_{v,\rm late}\) lets all earlier phase energy—including a false vacuum and the inflaton potential—gravitate and therefore avoids R15-1 signalling while reproducing the checked histories. A causal common reader cannot make this choice on two initially indistinguishable branches with unequal final vacuum energies. But the packet obtains \(C=\rho_{v,\rm late}\) only by stipulating the law’s \(T=0\) gravitational zero, and IE additionally imposes its integration constant exactly; without a derived symmetry, constraint, or source/action mechanism these are the same late-vacuum counterterm and precision cancellation identified by Lemma PT. Thus the broad signalling FAIL is not proved, but neither is untuned removal of \(\Lambda\): the strongest campaign reading is **INCONCLUSIVE**.