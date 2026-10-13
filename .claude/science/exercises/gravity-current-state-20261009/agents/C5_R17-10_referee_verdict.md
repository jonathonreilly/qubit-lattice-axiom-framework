# VERDICT: CONFIRMED WITH CORRECTIONS

Theorem F is mathematically sound on its conditioned fast face. The corrections concern its scope and the breadth of the μ_E no-certificate remark. The fixed campaign readings remain **K₆: OPEN**, **μ_E: OPEN**, and **JOINT: not met**.

## Per-item findings

1. **Five-moment forms, integrations by parts, and boundaries — confirmed.**

   The substitutions \(a_6=c_7\!\int z\,d\lambda\), \(a_{42}=c_7\!\int xy\,d\lambda\), \(a_{222}=c_7\!\int x^3d\lambda\), and \(b_4,b_{22}=(5/2)c_7\!\int(y,x^2)d\lambda\) reproduce all four polynomial rows exactly. My independent symbolic assertions are at [referee_checks.py:74](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/referee_checks.py:74>), confirming [R17-10_report.md:116](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/R17-10_report.md:116>).

   Both IBPs give the reported Eg and face1 cubics exactly; independent expansions are at [referee_checks.py:89](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/referee_checks.py:89>). The two actual boundary terms are \(wV\) and \(wG\), with \(w=t^{1/2}e^{-m^2t}\Phi^3\) and \(G=(45/2)x^2-(35/2)x+sx\). At zero, \(x=O(t)\), \(V=O(t^2)\), so these are \(O(t^{5/2})\) and \(O(t^{3/2})\); at infinity the \(m>0\) exponential dominates. The brief explanation at [R17-10_report.md:186](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/R17-10_report.md:186>) mentions only \(t^{1/2}x\), but the fuller checklist correctly mentions \(V\) at [R17-10_report.md:305](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/R17-10_report.md:305>). This is an exposition gap, not a proof failure. Reruns reproduced five-moment/IBP differences no larger than \(5.5\times10^{-12}\), consistent with [scripts/fastcert.out:4](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/scripts/fastcert.out:4>).

2. **Exact certificate, trajectory bound, and \(R(z)\) enclosure — confirmed.**

   Exact recomputation gives
   \[
   (c_2,c_1,c_0)=(-451/32000,-353/64000,-261/64000),
   \]
   \(k_1=89/4000\), \(k_2=2087/32000\), \(x_*=712/2087\), \(\alpha=536/625\), \(\beta=-16/125\), and Region-1 margin \(-117/1600000\). See [referee_checks.py:51](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/referee_checks.py:51>) and the worker result at [scripts/fastcert_exact.out:1](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/scripts/fastcert_exact.out:1>).

   The bound
   \[
   x\ge\min(x_{\rm box},\,t s_{\min}^2)
   \]
   is valid because \(x\) is a convex combination of the box mean and an edge mean whose every state has \(W\ge ts_{\min}^2\). The monotonicity argument for \(R(z)\) above \(1/\sqrt2\) is also valid. In addition to rerunning `mpmath.iv`, I used independent exact rational alternating-series bounds for both \(e^{-z^2}\) and \(\int_0^z e^{-v^2}dv\); they prove \(R(1.27)<0.307939153<0.3079868\) and \(x_{\rm box}>x_*\), at [referee_checks.py:111](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/referee_checks.py:111>). The safe rounded thresholds \(b/m\ge2.9935\) and \(s_{\min}/m\ge1.3768\) follow.

3. **Status of \(\mathcal F\) and the fixed reading — correction required.**

   \(\mathcal F\) is a legitimate face of the relaxation, but it is not a subclass of the physical class \(\mathcal S\). With the edge floor, \(C^2\) regularity forces \(\sigma'(\pi)=0\), hence a non-fast neighborhood of the endpoint; the report correctly states \(\mathcal F\cap\mathcal S=\varnothing\) at [R17-10_report.md:229](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/R17-10_report.md:229>). Moreover, Theorem F covers only the portion satisfying its \(b,s_{\min}\) thresholds, not the entire fast face.

   “Sharp-turn limit” is accurate for realizable finite zigzag skeletons, but too broad if applied to every arbitrary positive edge-level measure in \(\mathcal F\), since the theorem deliberately omits total-mass and path/reachability constraints [R17-10_report.md:217](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/R17-10_report.md:217>).

   Most importantly, the fixed clause requires incompatibility “on the relaxation superset,” meaning the whole stated superset, not an arbitrary contained face [TESTS.md:6223](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/TESTS.md:6223>). Thus the uppercase campaign label **CERTIFIED-CONFLICT** is not earned even with the qualifier “on \(\mathcal F\).” The proper description is a *referee-confirmed exact conflict theorem on the conditioned fast face*. The campaign reading is **OPEN**, as the report ultimately records at [R17-10_report.md:269](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/R17-10_report.md:269>).

4. **Continuity into \(\mathcal S\) — locally provable, not class-wide.**

   For fixed \(m>0\), the original five moments are continuous under smoothings with \(\sigma_n\to\sigma\) uniformly and \(\sigma_n'\to\sigma'\) almost everywhere or in \(L^p\), because \(|\sigma'|\le1\), the zone is compact, and \(\epsilon\ge m\). Therefore the strict Lagrangian inequality persists in some neighborhood of each fixed *realizable* fast skeleton. This gives a genuine local continuity corollary: sufficiently close smooth turnings cannot acquire an axis-zero point with \(K_6\le0\).

   It does not supply a uniform neighborhood of the whole fast face, prove that an exact-axis-zero branch remains near it, or cover slow climbs/terraces. The reported \(u\ge1/2\) search is non-certified [R17-10_report.md:242](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/R17-10_report.md:242>), while the same Lagrangian becomes positive on flat-heavy relaxation states [R17-10_report.md:238](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/R17-10_report.md:238>). No extension adequate to certify \(\mathcal S\) is presently proved.

5. **\(\mu_E\) remark — confirmed narrowly; broader wording must be avoided.**

   In the displayed fast-density representation,
   \[
   \frac{x}{t}(5x-\tfrac12+s)\longrightarrow-\tfrac12\langle g\rangle_0<0
   \]
   as \(t\to0\), whereas every fixed constant multiple of the displayed Eg and T2g densities vanishes there. Hence no finite constant multipliers can produce a pointwise nonnegative Lagrangian from those three displayed densities. The formula and numerical cross-check are at [R17-10_report.md:250](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/R17-10_report.md:250>) and [scripts/mufast_check.out:1](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R17-10/scripts/mufast_check.out:1>).

   This does not exclude an integral certificate using \(t\)-dependent multipliers, added exact derivatives/alternative IBP forms, or quantitative trajectory/path constraints. Accordingly it supports **OPEN**, not a general certificate no-go.

## Strongest correct statement

For the scalar U vertex with extension E1 and the supplied zero-point prescription, the five-moment \((x,y,z)\) formulation and its Hausdorff extension are correct, and on the conditioned fast relaxation face \(u=1\), with \(b\ge2.9935m\) and \(s_{\min}\ge1.3768m\), the exact certificate \(\Xi_{\rm face1}-(536/625)\Xi_{Eg}+(16/125)\Xi_{T2g}=c_7\int d\lambda\,xP(x,m^2t)<0\) is valid; hence the two axis zeros force \(\langle K_6/\epsilon^7\rangle>0\) there, and the result persists locally around each fixed realizable sharp-turn skeleton. This does not satisfy the fixed **CERTIFIED-CONFLICT** clause because it neither covers the full relaxation superset nor any class-wide portion of \(\mathcal S\); the available general-relaxation results remain local numerical searches. The \(\mu_E\) asymptotic rules out only the displayed constant-multiplier pointwise construction, not trajectory-based certificates. Therefore **K₆ is OPEN, \(\mu_E\) is OPEN, and JOINT is not met**.