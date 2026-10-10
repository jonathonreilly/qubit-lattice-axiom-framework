# C3 lane X1: referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-10)

## VERDICT

**CONFIRMED WITH CORRECTIONS — bounded FAIL.**

The fixed X1 FAIL criterion is met for the preregistered finite-volume implementation. It is not an asymptotic no-go for random lattices.

## Findings

- **Direct estimator: confirmed.** The primary calculation uses nonzero reciprocal modes,
  \(S(q)=N^{-1}|\sum_i\kappa_i e^{-iqx_i}|^2\), with \(m\ge1\); it is not the old \(q=0\) box proxy ([work/x1_analyze.py:21](<work/x1_analyze.py:21>)). The stiffness density sums to the exact spectral Hessian ([work/x1_core.py:133](<work/x1_core.py:133>)). I reran the analytic/finite-difference validations successfully. The modulated-strain response independently agrees with the density spectrum at low \(q\), including K2 ([analysis_final.out:201](<work/out/analysis_final.out:201>)).

- **Levels and registered flatness: confirmed.** My independent reanalysis of the saved realizations reproduces:

  - K1 scalar: \(3.584\times10^{-3}\), \(p=-0.027\)
  - K2 scalar: \(2.073\times10^{-3}\), \(p=+0.180\)
  - K1 spinless sea: \(7.107\times10^{-2}\), \(p=-0.031\)
  - K2 spinless sea: \(3.754\times10^{-2}\), \(p=-0.202\)
  - K1 Dirac: \(1.441\times10^{-2}\), \(p=+0.131\)

  All meet the preregistered \(|p|\le0.3\) flatness route and exceed \(10^{-3}\) ([work/PREREG.md:50](<work/PREREG.md:50>)). K2 is the weakest leg: its high-statistics window contains only two modes and cannot exclude a mild eventual falloff ([C3_X1_report.md:127](<C3_X1_report.md:127>)).

- **Normalization: confirmed.** At fixed \(N\),
  \([\operatorname{sd}(E''/N)\sqrt N]^2=\operatorname{Var}(E'')/N\), exactly the centered \(q=0\) power normalization. My numerical identity agrees to machine precision. The power/amplitude ambiguity cannot change the verdict: the lowest result is \(2.07\times10^{-3}\), with amplitude \(0.0455\), both above \(10^{-3}\), and respectively 7.6 and 9.0 decades above \(5\times10^{-11}\). The independent checker is [referee_check.py:45](<referee_check.py:45>).

- **Fermions: literal reading satisfied.** F1 is a correctly differentiated, pilot-fixed grand potential for spinless fermions and was run with both kernels ([work/x1_core.py:44](<work/x1_core.py:44>), [work/x1_run.py:16](<work/x1_run.py:16>)). It is a \(4+1\)-Hamiltonian construction, not a four-dimensional Euclidean spinor. F2 is a valid massive naive-Dirac determinant for its stated discretization, but was run only on K1 and has no continuum/doubler analysis ([work/x1_dirac.py:1](<work/x1_dirac.py:1>)). The preregistration explicitly makes F1 the required fermion and F2 secondary, so this does not weaken the FAIL.

- **Two side claims must be narrowed.** “No realization is quiet” is too strong: the report itself gives K2 realization means down to \(4.1\times10^{-4}\), and a single pooled K2 point falls to \(9.6\times10^{-4}\) ([C3_X1_report.md:181](<C3_X1_report.md:181>)). The threshold is satisfied by ensemble-averaged spectra, not every realization or point.

- **The claimed absence of a zero-frequency atom is unsupported.** For F2, fixed-\(N\) and Poisson-\(N\) \(q=0\) powers are \(4.23\times10^{-2}\) and \(1.20\times10^{-2}\); I obtain variance ratio 3.54 and two-sided \(F\)-test \(p\simeq0.012\) ([C3_X1_report.md:197](<C3_X1_report.md:197>)). This is unresolved and does not affect the nonzero-\(q\) verdict.

- **Scope is finite-window only.** The rods enlarge \(L_z\) while retaining transverse widths \(4\)–\(5\), barely above twice the kernel ranges. There is no simultaneous four-dimensional thermodynamic limit and no proof that \(S(k)\) remains nonzero as \(k\to0\). The report’s exclusions of other graphs, relaxed/hyperuniform/dynamical substrates, interactions, and a physical graviton-noise map are necessary ([C3_X1_report.md:224](<C3_X1_report.md:224>)).

## Strongest correct statement

For the preregistered finite periodic Poisson ensembles, the two specified compact kernels, and the specified free scalar and fermion functionals, every **ensemble-averaged** measured nonzero-\(q\) TT stiffness spectrum is consistent with a constant over its registered window and has power \(S\ge2.07\times10^{-3}\). Therefore lane X1 is a **FAIL under the fixed reading**.

This does not establish a nonzero asymptotic \(k\to0\) limit in an uncompactified four-dimensional thermodynamic limit, nor exclude other random-lattice constructions, interactions, or protected cancellation mechanisms.