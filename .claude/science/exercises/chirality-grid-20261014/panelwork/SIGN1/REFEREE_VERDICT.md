# VERDICT: CONFIRMED WITH CORRECTIONS

The core result is valid for a stated ungauged subfamily, but several implementation and presentation claims require correction.

1. Positivity theorem — confirmed after correcting the remainder.

- `T1²=T2²=-1` and `{T1,T2}=0` hold exactly (`scripts/kramers_fams.py:7-11`).
- All 1,024 HS channels have the required parity under both antiunitaries and commute with \(U(1)_c\); the three walker directions and any real, flavour-blind filter preserve the same symmetries.
- Thus every HS slice satisfies the Kramers criterion, which makes the number-conserving \(d\)-frame determinant nonnegative. This is precisely the Wu–Zhang theorem and the Li–Jiang–Yao Kramers class. [Wu–Zhang](https://arxiv.org/html/cond-mat/0407272v3), [Li–Jiang–Yao](https://arxiv.org/html/1601.05780v3)
- `REPORT.md:72` omits part of the full trace: in Majorana notation it is proportional to
  \[
  \frac{\det(1+M_d)}{\sqrt{\det M_d}},
  \]
  as correctly used in `scripts/p4c_stable.py:88-90`. The denominator is positive.
- The filtered remainder in `scripts/p4_cluster_weights.py:44-47` and `scripts/p4c_stable.py:44-46,69-70` is wrong for \(\lambda_1\ne0\). If \(F_xF_x^T=\rho I\), it must be
  \[
  K_{R,F}=\rho F_x^T K_R F_x,
  \]
  with the scalar remainder multiplied by \(\rho^2\). For the four-site filter, \(\rho=3/8\). This correction preserves Kramers symmetry; at \(\lambda_1=0\), \(R=0\).

2. Decomposition — quartic identity confirmed, worker’s exactness argument corrected.

- Exhausting all \(\binom{64}{4}=635{,}376\) components gave relative residuals \(4.24\times10^{-16}\) at \(230^\circ\) and \(2.96\times10^{-16}\) for the \(270^\circ\) Fierz identity.
- The four-form image has rank 12, not 11 as claimed at `REPORT.md:64` and `scripts/p5_exact_margin.out:1`. The worker’s sample missed one supported direction, so its minimal-norm correction alone did not establish an exact identity.
- A rank-12 correction remains strictly inside the cone at \(230^\circ\), with margin \(0.317862823\).
- At \(270^\circ\), the worker’s minimal correction actually has negative margin \(-4.276\times10^{-7}\) (`scripts/p5_exact_margin.out:23`). The separate exact Fierz solution \((-34,+2,-2,+2)\) repairs this with margin 2 (`scripts/p6_fierz_lambda1_zero.out:10`).
- `REPORT.md:90-97` is not a complete written decomposition: it omits the four nonzero 2×2 density blocks shown at `scripts/p5_exact_margin.out:18-21` and does not specify \(R\).

3. Cluster weights — reproduced with the corrected faithful Hamiltonian.

At \(230^\circ\), on four sites and three configurations each:

- \(W=0.5,\ dt=0.05,\ L_\tau=4\): maximum phase \(1.13\times10^{-14}\).
- \(W=8,\ dt=0.05,\ L_\tau=10\): maximum stabilized phase \(2.09\times10^{-12}\).
- \(|\arg\det M_d|<8.2\times10^{-16}\) when computed from exact traces.

The bounded reproduction is in [REFEREE_CHECKS.py](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_SIGN1/REFEREE_CHECKS.py:1>).

4. Boundaries and gauging.

- An exhaustive \(190^\circ\) check gives residual \(2.25\times10^{-16}\) and margin \(0.0155744\). Convexity with the exact \(270^\circ\) point certifies
  \[
  \lambda_1\le0,\qquad |\lambda_2/\lambda_1|\ge\tan 10^\circ=0.17632698.
  \]
  The quoted \(0.15\)–\(0.18\) is only a boundary bracket, not a proved sharp threshold.
- \(\lambda_1>0\) is correctly OPEN: `REPORT.md:101` lists untested MTR pairs, and the known classifications are sufficient criteria rather than automatic decompositions. [Wei et al.](https://arxiv.org/html/1601.01994v5)
- The real \(10\) does branch under \(G_{\rm SM}\) as \(6_{\mathbb R}\oplus4_{\mathbb R}\), with no invariant real two-plane. This kills the proposed fixed \(U(1)_c\) construction for arbitrary dynamical links, but not every conceivable Kramers/Majorana/reflection-positive construction.
- The exhaustive P1 classification is underproved: `scripts/p1_p2_p3_lp.py:54-70` constructs representatives for \(k=1,3,5\), but does not classify every admissible \(V\) or accidental Fierz symmetry.

5. Fixed SIGN-1 reading.

Yes, narrowly. `TESTS.md:98-102` explicitly permits the walker plus filtered global-Spin(10) quartic as a faithful reduction. Since X2 leaves the couplings free (`PREREG.md:10-15`), the exact \(\lambda_1=0,\lambda_2\ne0\) member—with its four-family Fierz decomposition—meets SIGN-FREE. This does not establish sign-freeness for every allowed X2 coupling or for the dynamical gauged theory.

Strongest correct statement: The ungauged X2 matter Hamiltonian with a real flavour-blind filter is rigorously Kramers-class sign-free at \(\lambda_1=0,\lambda_2\ne0\), and is numerically certified with strict cone margin throughout the conservative region \(\lambda_1\le0,\ |\lambda_2/\lambda_1|\ge0.17632698\), provided the filtered lower-grade remainder is corrected as above; \(\lambda_1>0\) and the dynamical \(G_{\rm SM}\)-gauged theory remain open.

Full details: [REFEREE_REPORT.md](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_SIGN1/REFEREE_REPORT.md:1>).