# VERDICT: NOT CONFIRMED

All four runners reproduce their supplied outputs. The narrow Bianchi identity, conditional maximum-principle result, and \(g=0\) GR limit are sound. The central **VIABLE** reading is not: CMC existence/no-caustic behavior is assumed rather than demonstrated, the stated positivity bound drops inhomogeneous curvature terms, the tested Prony law becomes nonphysical during several vacuum transitions, and causality/Hamiltonian stability of the globally driven “cuscuton-type” sector remains unproved. Under the FIXED readings, the result is **OPEN**, not EXCLUDED.

## 1. Lemma C

The core computation is correct. From
\[
E_{\mu\nu}=\lambda n_\mu n_\nu+p_Eh_{\mu\nu},
\]
conservation gives
\[
D_i p_E+(\lambda+p_E)D_i\ln N=0,\qquad
\frac{\dot\lambda}{N}+(\lambda+p_E)\theta_n=0.
\]
Since \(\lambda\) is spatially uniform,
\[
N(\lambda+p_E)=g(t),\qquad \dot\lambda=-g\theta_n .
\]
The symbolic rerun returns zero residuals exactly ([r145_bianchi.py:38](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/scripts/r145_bianchi.py:38>), [r145_bianchi.out:1](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/scripts/r145_bianchi.out:1>)).

Two corrections are necessary:

- At a single instant \(g=0\) implies only \(\dot\lambda=0\) at that instant. “\(\lambda\) is constant” and “exact GR” require \(g\equiv0\) on an interval ([report:186–190](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:186>)).
- CMC follows wherever \(g\neq0\). A smooth vacuum adjustment with \(\dot\lambda\neq0\) therefore forces CMC during that adjustment, but not automatically between transitions. Choosing CMC for all time is an additional clock law. The claimed exclusion of every finite-speed clock is valid only inside H-imp/H-T with isotropic \(E\), uniform \(\lambda\), and exact constraint preservation—not as a general theorem ([report:190–192](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:190>)).

## 2. Is the vacuum genuinely untuned?

There is a real, narrow vacuum-shift symmetry in the ideal homogeneous equations. Under
\[
\rho_v\mapsto\rho_v+C,\qquad \lambda\mapsto\lambda-\kappa C,
\]
the geometry and \(\widetilde\Lambda=\lambda+\kappa\rho_v\) are unchanged. If the algebraic expansion law \(3H^2=\kappa\widehat\rho_{\rm nc}\) is fundamental, \(\lambda\) is a slice multiplier fixed by the constraint, not an initially tuned integration constant.

This is **not standard unimodular gravity with a dynamically adjusted \(\Lambda\)**. Standard unimodular gravity is the \(g\equiv0\), constant-\(\lambda\) branch and retains the usual vacuum-shift problem. The \(g\neq0\) branch adds a globally driven constraint stress with \(p_E=g/N-\lambda\). The vacuum’s gravitational effect is transferred into \(\lambda\); during transitions it reappears transiently in \(g\), the elliptic pressure response, and reader error ([report:231–257](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:231>)).

The homogeneous runner does not demonstrate dynamical self-adjustment independently:

- It analytically constructs the density derivatives, defines \(H^2=\widehat\rho/3\), and then computes \(\lambda=3H^2-\rho_{\rm tot}\) algebraically ([r145_homog.py:23–50](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/scripts/r145_homog.py:23>)). Thus the endpoint equality \(\lambda=-\rho_v\) is chiefly a check of the imposed zero-frequency projector.
- The \(10^{-16}\) endpoint residual is floating-point closure after the history has again become an exact rank-two exponential mixture, not evidence of robust relaxation.
- More seriously, \(\widehat\rho/\rho_{\rm nc}\) reaches \(-3.43\), \(-482\), and \(-34.3\) in three advertised runs ([r145_homog.out:9–30](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/scripts/r145_homog.out:9>)). Then the law gives \(H^2<0\). `np.clip` is used only when computing \(H\) for diagnostic \(g\), not in the stated expansion law ([r145_homog.py:45–47](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/scripts/r145_homog.py:45>)).
- The proposed \(c=\max(0,\cdot)\) clamp is neither specified nor tested; it would produce \(H=0\), conflicting with the claimed \(H>0\)-forever arrow. A regularized reader remains unbuilt ([report:251–255](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:251>), [report:299–302](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:299>)).

Thus there is no hidden tuning of the *value* of the initial \(\lambda\) in the ideal homogeneous law, but the exact global projector is an added nonlocal mechanism, and the supplied transition model is not a complete real-valued evolution. Moreover, the report itself finds \(\widetilde\Lambda=\tfrac12\langle R\rangle-\tfrac12\langle\sigma^2\rangle\), not zero, in the inhomogeneous model ([report:257](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:257>)).

## 3. Lapse positivity, CMC existence, and caustics

The lapse equation and maximum-principle statement are correct conditionally:
\[
-D^2N+\widetilde QN=S(t),\qquad
\widetilde Q=K_{ij}K^{ij}+\frac{\kappa}{2}(\rho+3p)_{\rm nc}-\widetilde\Lambda.
\]
On a compact connected slice, \(\widetilde Q\ge0\), not identically zero, indeed gives a unique positive normalized lapse ([report:200–202](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:200>)).

But the asserted sufficient bound is incomplete. Combining the averaged Hamiltonian constraint with \(K_{ij}K^{ij}=\theta^2/3+\sigma^2\) gives
\[
\widetilde Q
=\kappa\bar\rho_{\rm nc}
+\frac{\kappa}{2}(\rho+3p)_{\rm nc}
+\sigma^2-\frac12\langle R\rangle+\frac12\langle\sigma^2\rangle .
\]
The report drops the final curvature/shear terms at [report:203–206](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:203>) even though it restores them at line 257. Consequently, positivity for arbitrary lumpy dust/radiation data is not proved. The numerical box simply sets \(Q=3+1.5\rho/\bar\rho\) on a flat fixed metric, so it cannot test this missing self-consistent term ([r145_lapse.py:22–28](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/scripts/r145_lapse.py:22>)).

CMC existence is explicitly assumed at [report:102](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:102>). Gerhardt’s theorem requires compact Cauchy surfaces, global big-bang/big-crunch barriers, and timelike convergence; it does not establish a CMC foliation for this eternally expanding, modified-gravity model ([Gerhardt 1983](https://www.math.uni-heidelberg.de/studinfo/gerhardt/1103922929.pdf)). There are even Einstein-dust spacetimes possessing a CMC slice but not covered by a CMC foliation ([Isenberg–Rendall](https://arxiv.org/abs/gr-qc/9710053)).

Given an already-existing smooth CMC foliation with finite uniform \(\theta>0\) and bounded \(N>0\), a normal-volume caustic is indeed excluded. But that is conditional almost to the point of circularity. The weak-field boxes, static top hats, and flat-metric lapse-collapse toy do not evolve a collapsing spacetime or prove global continuation ([report:208–226](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:208>)). Therefore test (a) is not passed.

## 4. Linear growth

The displayed synchronous-gauge equations are consistent, and the \(g=0\) statement is correct: on an interval with \(g=0\), \(E_{\mu\nu}=-\lambda g_{\mu\nu}\) with constant \(\lambda\), so the local equations are exactly GR with constant \(\widetilde\Lambda\) ([report:261–272](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:261>)).

The claimed correction needs qualification:
\[
\frac{\Delta{\cal G}}{\cal G}
=O\!\left[\left(\frac{g}{H^2}+\frac{\dot g}{H^3}\right)
\left(\frac{aH}{k}\right)^2\right],
\]
with further rapid-background terms. Reducing this to \(O[(g/H^2)(aH/k)^2]\) assumes \(\dot g=O(Hg)\). The runner hard-codes precisely the special case \(g=2X,\ \dot g=-2Hg\) ([r145_growth.py:16–26](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/scripts/r145_growth.py:16>)); it does not test the singular, rapidly varying Prony-transition \(g\), nor the suggested backreaction \(g\). Several tabulated modes are also horizon-scale or superhorizon during part of the integration, so that table is not an observational CMB/growth calculation.

Hence the stationary \(g=0\) GR limit is confirmed, but the general \(g\neq0\) growth claim and test (c) for the actual transition model are only conditional.

## 5. Conservation, causality, and stability

Energy conservation closes algebraically if conserved total matter stress, exact CMC, and the imposed field equations are granted: Lemma C is precisely the conservation condition. What is missing is a local action or complete Hamiltonian/constraint-algebra demonstration for the arbitrary global functionals \(\lambda[\bar\rho]\) and \(g[\bar\rho]\).

Causality is unresolved by the report’s own admission ([report:294–297](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:294>), [report:314–315](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:314>)). For \(g\neq0\), a local change of \(Q\) alters \(N\) everywhere through an elliptic Green function and produces the physical stress response \(\delta p_E=-g\,\delta N\). Merely naming this instantaneous influence as a price does not establish no-signalling.

The original cuscuton’s no-information argument applies to its particular degenerate scalar action, not automatically to an arbitrary globally driven stress tensor ([Afshordi–Chung–Geshnizjani](https://arxiv.org/abs/hep-th/0609150)). Later analyses explicitly identify a preferred foliation and a nonperturbative instantaneous elliptic mode, with ghosts or an unbounded Hamiltonian outside that foliation ([Bhattacharyya et al.](https://arxiv.org/abs/1612.01824)). Gomes–Guariento find regular homogeneous behavior only when the field is imposed a priori as a single global degree of freedom in CMC slicing, with additional conditions for nonvanishing lapse ([Gomes–Guariento](https://arxiv.org/abs/1703.08226)). The model resembles that special sector, but its arbitrary Prony-driven \((\lambda,g)\), its passage through \(g=0\), and its constraint rank/bounded Hamiltonian were not analyzed. The “two local degrees plus one global pair” statement is explicitly only suggested ([report:307–313](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/R14-5_report.md:307>)).

## 6. Reading

The FIXED VIABLE criterion requires an explicit model passing (a)–(c), with untuned \(\Lambda_{\rm eff}=0\) and prices named ([TESTS.md:4882–4890](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R14-5/TESTS.md:4882>)). Prices are named, and the homogeneous constant-vacuum cancellation is a legitimate conditional mechanism. But (a) rests on assumed global CMC existence and an incomplete positivity bound; the tested transition law produces \(H^2<0\) without a built regularization; the inhomogeneous \(\widetilde\Lambda\) is not zero; and \(g\neq0\) causality and Hamiltonian stability remain open. **VIABLE is therefore unjustified even inside the stated \(\mathcal Z\) packet. The correct reading is OPEN.**

## Strongest correct statement

Within a smooth continuum theory that imposes \(E_{ni}=0\), \(E^{\rm TL}_{ij}=0\), spatially uniform \(E_{nn}=\lambda(t)\), conserved total stress, and an independently supplied global zero-frequency expansion law, Bianchi conservation exactly implies \(N(\lambda+p_E)=g(t)\) and \(\dot\lambda=-g\theta_n\); hence any smooth interval of active vacuum compensation forces CMC slicing, while \(g\equiv0\) reduces locally to GR with a constant effective cosmological term. An exact finite-rank Prony reader can algebraically remove a constant \(w=-1\) vacuum from a homogeneous constant-\(w\) mixture without tuning the value of \(\lambda\), but the supplied construction does not establish a globally existing positive-lapse CMC foliation through collapse, a real and regular evolution through the tested phase transitions, exact \(\widetilde\Lambda=0\) in the lumpy universe, or causal and Hamiltonian-stable \(g\neq0\) dynamics. Thus R14-5 supplies a credible conditional zero-mode degravitation mechanism and a correct CMC necessity lemma, but not an explicit model meeting the FIXED VIABLE criterion; the strongest reading is **OPEN**.