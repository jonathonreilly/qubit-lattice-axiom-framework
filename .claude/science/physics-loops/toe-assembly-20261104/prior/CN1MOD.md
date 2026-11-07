## **Searches run.**

Initial terms: `R1-MOD`, `CN1MOD`, `H-CONV`, `velocity.*attract`, `multi-cone`, `metric attraction`, `star flow`, `scale integration`, `reduced QED`, `marginal.*drag`, `Peierls`.

Directories: `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104/`. Follow-ups covered `massless photon`, `Giuliani`, `Mastropietro`, `Gram.*bound`, `fermionic.*expansion`, `QED`, `anisotrop`, and `O(4)`. Searches included TOE drafts, referee reports, prior digests, and `LIT_*.md`.

Read `ref/README.md` first. Its corpus description is “origin/main docs/ at clone time”; consolidation PRs contain “changed files at branch head” (`ref/README.md:2–3`). Findings below concern these supplied snapshots.

Path abbreviations:

- **T** = `repo/.claude/science/physics-loops/toe-assembly-20261104/`
- **M** = `ref/main/docs/`
- **A** = `ref/main/docs/audit/data/ledger/`
- **Y** = `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/`
- **S** = `M/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md`
- **K** = `M/WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md`
- **Q** = `M/SUPPLIED_QUARTET_LINEAR_METRIC_FLOW_BOUNDED_THEOREM_NOTE_2026-09-15.md`
- **W** = `M/NATIVE_INTERACTING_WEYL_PROTECTED_PATHS_BOUNDED_THEOREM_NOTE_2026-09-13.md`

## **Already in the repo.**

- **The precise model obligation is already stated.** R1-MOD requires exact lattice scale integration, interpolated `(OL+ρ)` coefficients, uniform remainder bounds, initial smallness, and exponential forcing. The text says “uniformly at all scales” and “Both are open,” distinguishing R1-MOD from R1-OBS (`T/CN1.md:52`). The assembly target is interacting species whose “speed differences … flow to zero” (`T/TOE_ASSEMBLY.md:730`).

- **CN1 supplies the conditional ODE endpoint.** Theorem 1 gives global positive-speed consensus. Theorem 2 gives equal-charge pair exponent `2q²/W`. Theorem 3 covers the specified small remainders and smallness conditions. Exact quotes: “All speeds converge to one positive limit,” “the exponent is `2q²/W`,” and “Under the same hypothesis on `f` and (R-iii)” (`T/CN1.md:87,99,123`). Under merely integrable forcing, the referee closure gives convergence but “no rate is claimed” (`T/CN1.md:133`). Status: frozen; the report is “not audited status” (`T/CN1.md:5,7`).

- **The Peierls carrier already supplies one-loop lattice matching.** It derives vertices, Ward cancellation, fermion/photon logarithms, and infrared remainder estimates for a supplied noncompact, continuous-time carrier. The remainder “integrates to a finite `O(rho_0)` value”; its constants concern “fixed microscopic parameters” and separated nodes (`S:269,279–280`). These are coefficients of a local two-point action: “They are not exact charged-particle pole speeds” (`S:40–43`). Source status is “conditional-support” (`S:7`). Ledger: `"audit_status": "unaudited"` and `"claim_type": "bounded_theorem"` (`A/sp/spatial_lattice_gauge_fermion_logarithms_and_metric_attraction_limits_bounded_theorem_note_2026-09-14.json:6,17`).

- **Several attraction calculations precede CN1MOD.** The Peierls note has a linear tensor star flow whose “unique zero direction is a common metric,” and a nonlinear shared-fermion-speed flow converging “to a positive common value” (`S:455,487`). Its limit is explicit: “a theorem of the displayed truncated ODE” (`S:487–488`). Its decaying-forcing calculation changes the finite matching constant, conditional on decay; “a permanent marginal source … is a different problem” (`S:507–517`).

- **The quartet note retains modes that a scalar-speed ansatz misses.** It counts each Weyl cone with `n_i=1/2`, gives node-resolved metric flow, and finds slower inter-node contrasts. Exact quotes: “There is no extra factor of the total node count” and “Inter-node contrasts decay more slowly” (`Q:111–112,166–167`). It also computes a quadratic photon-polarization source from metric variance. The formulas solve “the truncated equations”; uniform omitted-order control “is not asserted” (`Q:216–218`). Ledger: `"effective_status": "unaudited"` (`A/su/supplied_quartet_linear_metric_flow_bounded_theorem_note_2026-09-15.json:30`).

- **The exchange criterion and rate distinction are available.** The constant-coefficient theorem gives difference eigenvalue `−(a+b)` under assumed positive mutual drag. It “does not derive the physical one-loop coefficients” (`M/EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md:21,68–76`). Current ledger status is `"unaudited"` (`A/em/emergent_lorentz_velocity_rg_exchange_matrix_exact_support_note_2026-06-18.json:6`). Frozen LZ1I extends this to scale-dependent drag: convergence requires that “the integral diverges.” Its marginal example is not a positive momentum-power rate (`T/LZ1I.md:5,184,188`).

- **An exact fermionic polymer construction exists, with different hypotheses.** K controls the exact retained gauge–Grassmann logarithm in a “simultaneous all-degree connected polymer norm,” in an “explicit high-mass, small-coupling region” (`K:11–13`). It uses the retained positive body `det D_II`, with `m>4` (`K:21–23,34`). It is one-step closure and “does not prove an invariant RG neighborhood” (`K:85–88`). Ledger: `"effective_status": "unaudited"` (`A/wi/wilson_staggered_retained_grassmann_two_layer_kp_polymer_norm_bounded_theorem_note_2026-07-12.json:30`).

- **A short-range interacting Weyl correlation input is already packaged.** W imports an analytic counterterm and renormalized two-point theorem for a “symmetric finite-range class.” The limit takes “volume first, then inverse temperature”; “The counterterm is indispensable” (`W:93–100`). This is an imported theorem for the specified density-interaction model, not a dynamical-photon construction (`W:108–115`). Ledger: `"effective_status": "unaudited"` (`A/na/native_interacting_weyl_protected_paths_bounded_theorem_note_2026-09-13.json:30`).

- **A massive-photon tick calculation is logged.** The gauge-register consolidation records #9943’s exact dressed-hop Ward identity and one-loop vertex calculation with a Stueckelberg photon mass. Its scope is a supplied Gaussian, small-step model; “the cone (step) counterterm” is excluded (`ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md:1191`). Status is `logged`; the consolidation calls its contents “author statements for review” (`same:11,1191`).

## **Failed attempts on file.**

- **Port the all-orders reduced-QED expansion.** The missing step is “the sum over `N`.” Orderwise bounds do not supply the required order-summable remainder bound. The source also distinguishes planar fermions from M1’s spatial fermions (`T/CN1_OUTLINE.md:295`).

- **Integrate out the Gaussian photon, then use a convergent fermionic expansion.** The missing step is “scale-summability of the kernel.” The massless current kernel lacks the needed extra decay across a scale gap (`T/CN1_OUTLINE.md:296`).

- **Replace size estimates with Ward identities and exchange symmetry.** The missing step is “the size estimate.” The identities constrain charge renormalization while leaving the spatial/temporal coefficient ratio free (`T/CN1_OUTLINE.md:297`). The frozen formulation requires a “uniform `O(G²)` Lipschitz bound”; “symmetry alone does not give the bound” (`T/CN1.md:117`).

- **Use large `N`.** At leading order the fermion speeds remain fixed; drag appears at `1/N`. The recorded failure is that “the `1/N` series is not known to converge” (`T/CN1_OUTLINE.md:298`). The referee characterizes these attacks as plans: “none is carried to a written partial result” (`T/CN1_REFEREE.md:250`).

- **Allow an unrestricted marginal source.** Proposition 4 gives a permanent offset. The explicit full-flow construction has `Δ ≠ 0` and an `O(G)` source that “violates (R-i)” (`T/CN1.md:135,141`). This is a counterexample within the displayed flow, not evidence that a framework tick generates that source (`T/CN1.md:139`).

- **Use denominator proxies as physical drag evidence.** The earlier note withdraws “physical log-flow corroboration and power-divergent `f0` route no-go.” Its denominators are “not full tensor propagators or self-energy integrands” (`M/VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md:22–27`).

## **Overlap with this lane's results.**

not run

## **Missed inputs.**

- **Use the corrected frozen remainder specification.** Start from initial `(Sm)`, exponential forcing for the rate, and the derivative bound needed for exchange symmetry. The referee explicitly requires “state both in R1-MOD” (`T/CN1_REFEREE.md:160`). This replaces the outline’s broader robustness summary with the actual model obligation (`T/CN1_REFEREE.md:216`).

- **Use the Peierls action and remainder calculation as the starting carrier.** This would concentrate new work on repeated exact integration and uniform higher-order control. The existing note already isolates the remaining issue: “Higher-loop control remains open” (`S:503`).

- **Use K and W as bounded constructive inputs.** K provides an exact joint norm and the correct retained determinant body, but its next task is to extract marginal coordinates and establish an invariant rescaled neighborhood (`K:21–23,371–376`). W provides a finite-range Weyl correlation comparison with an indispensable counterterm (`W:95–100`). Neither removes the recorded massless-kernel scale-gap obligation (`T/CN1_OUTLINE.md:296`).

- **Include full tensor and photon-content checks when selecting the model.** Q shows that a shared-metric simplification erases slow contrasts (`Q:166–168`). The two-node Hall example instead produces a photon “quadratic along the node-separation axis,” so Maxwell-only infrared extrapolation requires an additional cancellation condition (`M/NATIVE_WEYL_GAUGE_HALL_AND_CONE_FLOW_BOUNDED_THEOREM_NOTE_2026-09-13.md:18–28`). That source’s ledger is `"unaudited"` (`A/na/native_weyl_gauge_hall_and_cone_flow_bounded_theorem_note_2026-09-13.json:6`).

- **Separate finite matching from persistent forcing.** #9913’s supplied tick calculation reports that “kappa is a finite lattice constant”; its logarithms cancel at matched tree cones (`ref/pr10125/docs/LORENTZ_DISPERSION_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md:112`). This supplies a matching obligation. CN1 distinguishes an initial offset from “a source at every scale” (`T/CN1.md:54`).

## **Consumers.**

- **CN1’s rung-1 convergence result.** Its weakest model input is exact scale evolution satisfying the smallness and integrable-forcing hypotheses. The existing closure then gives consensus with “no rate” (`T/CN1.md:133`). The sharper pair-rate consumer additionally needs the weighted pair remainder conditions and decay hypotheses (`T/CN1.md:114,123`).

- **R1″-MOD, the photon-mass intermediate problem.** It needs bounds uniform in the number of marginal scales. The frozen text also requires “uniform initial data, smallness and constants in Theorem 3” (`T/CN1.md:58`). A fixed-mass construction alone would not meet that handoff.

- **CN1-T and R1-OBS.** R1-MOD supplies action coefficients. The next consumer needs invariant spectral thresholds near each coefficient, with “a constant independent of `κ`,” plus access and denominator conditions (`T/CN1.md:44,52`). The free-current result alone “does not establish R1-OBS at nonzero coupling or on a tick” (`T/CN1.md:153`).

- **Framework rung R2 and LZ1.** R2 additionally needs tick-loop coefficients, threshold transfer, and decaying cell-scale forcing (`T/CN1.md:54`). LZ1 needs all stated species and `p≥2`, “beyond the logarithmic pair result” (`T/CN1.md:195`). Neutral sectors and gravitons require “separate bridges” (`T/CN1.md:56`).

- **YM branch and its TOE bridges.** No direct pure-YM consumer of R1-MOD was found. YM’s stated observable scope is the “`tr(F^2)` sector of Wilson SU(2)” (`Y/GOAL.md:22`). Related downstream needs belong to Y3’s anisotropy-removal bridge and Y4’s matter extension: “T0 is pure gauge,” while the TOE needs RG with chiral fermions “outside T0’s statement” (`T/TOE_ASSEMBLY.md:615–616`).