# VERDICT: CONFIRMED WITH CORRECTIONS

The central price lemma is correct. The report overstates its physical corollaries, the general-background index claim, and the continuous-time reduction.

## 1. Lemma R — confirmed

The proof at [ROUTE_REPORT.md:54–62](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/ROUTE_REPORT.md:54) works.

- After clearing negative Laurent powers, \(U=(\mathbb C^\*)^d\setminus V(g)\) is the principal open \(D(z_1\cdots z_d g)\subset\mathbb A^d\).
- \(T^d\) is Zariski-dense: a Laurent polynomial vanishing there has all Fourier coefficients zero. Thus \(P^2=P\) on \(T^d\) implies the algebraic identity on \(U\).
- An idempotent over \(\mathcal O(U)\) gives a finite projective module and hence an algebraic vector bundle.
- The disputed step 5 is correct. Localization makes \(CH^k(\mathbb A^d)\to CH^k(U)\) surjective, while \(CH^k(\mathbb A^d)=0\) for \(k>0\); see the [Stacks localization sequence](https://stacks.math.columbia.edu/tag/0B5Z).
- For smooth complex \(U\), the cycle map is compatible with vector-bundle Chern classes, including for nonproper \(U\), using Borel–Moore homology and Poincaré duality; this is Fulton, Proposition 19.1.2, not merely a projective-variety assertion.

Correction: “regular on \(T^d\)” must mean “admits a common Laurent-polynomial denominator nonzero on \(T^d\),” equivalently regular on a complex Zariski-open neighbourhood of \(T^d\). Merely assigning finite values at real-torus indeterminacy points would not suffice.

## 2. Lemma 0 — confirmed algebraically, not physically in full generality

The two implications at [ROUTE_REPORT.md:48–52](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/ROUTE_REPORT.md:48) are correct for unconstrained translation-invariant Gaussian block operators:

\[
N/g=0-N(-gI)^{-1}I .
\]

This uses finitely many auxiliary components and finite-range Laurent-polynomial blocks; invertibility on compact \(T^d\) gives a uniform singular-value gap.

The converse construction does not by itself preserve Hermiticity, \(\gamma_5\)-Hermiticity, reflection positivity, gauge covariance, or a Hamiltonian interpretation. Therefore “same thing” is correct as a Schur-complement/algebraic statement, not as an equivalence of every physically constrained auxiliary realization.

## 3. Theorem F2-R

### Part (a) — confirmed with explicit hypotheses

The calculation at [ROUTE_REPORT.md:70–72](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/ROUTE_REPORT.md:70) is correct in four dimensions for canonical \(R=\tfrac12\), a \(\gamma_5\)-Hermitian scalar-plus-vector symbol
\[
D=a+i\gamma_\mu b_\mu,
\]
and isolated regular massless zeros. GW gives
\[
2a=a^2+b^2,\qquad n=(a-1,b)\in S^4.
\]
The projector is the pullback of the Bott projector, so \(C_2(\widehat P)=\pm\deg n\); the local degree at \(D=0\) is the zero’s chirality. Lemma R therefore forces the sum of local chiral indices to vanish.

Correction: “always carries a doubler” is too literal. A massive operator carries no massless modes, and nongeneric/nonisolated zeros need not look like a conventional doubler. The exact conclusion is: a rational pole-free operator cannot have one isolated simple chiral zero; any nonzero local chirality must have compensating total local index.

### Part (b) — not established

[ROUTE_REPORT.md:73–75](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/ROUTE_REPORT.md:73) correctly labels the 4D link a comparator, but the heading calls the theorem proved. T1 cannot establish it for general \(R\), taste structure, or gauging.

A valid theorem needs additional hypotheses: a specified gauge-covariant extension, admissibility, uniform locality and smoothness over gauge-field space, and a universality theorem relating its index to the free topological coefficient. In general rank the relevant coefficient is the top Chern character/anomaly coefficient, not automatically one Chern class. Exact GW alone is insufficient: known GW examples can reproduce the perturbative anomaly yet have no topological zero modes in nontrivial sectors ([Chiu](https://arxiv.org/abs/hep-lat/0110083)).

## 4. Corollaries — narrow core confirmed; trichotomy not confirmed

- Confirmed: nonzero free GW Chern number requires leaving the rational, pole-free class. This follows from Lemma R.
- Confirmed: matrix size does not change Lemma R. Thus \(M_2(\mathbb C)\to M_4(\mathbb C)\) cannot help within the finite-band, translation-invariant rational-projector class; see [ROUTE_REPORT.md:77–83](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/ROUTE_REPORT.md:77).
- Not confirmed: the three-way list at [ROUTE_REPORT.md:147–155](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/ROUTE_REPORT.md:147) is not exhaustive. The theorem only says “non-rational or singular on the torus,” not that every escape must take exactly one of those three representations.
- The sign kernel, infinite-domain-wall realization, and Fermi-sea projector are overlapping representations of similar functional calculus, not three exclusive mathematical alternatives.
- Treating a spectral projector as physically selecting or “privileging” a realized vacuum does not follow from the axiom at [MINIMAL_AXIOMS_2026-06-29.md:92–95](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/MINIMAL_AXIOMS_2026-06-29.md:92). A ground-state projector may be used purely as an operator construction.

## 5. Tests

All requested scripts were rerun serially. Peak RSS was 21–103 MB.

- **T1: confirmed as a 2D finite test.** It reproduced all 96 relations in [t1_index_vs_chern_2d.out:1–19](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/scripts/t1_index_vs_chern_2d.out:1). The independent FHS calculation is at [t1_index_vs_chern_2d.py:66–83](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/scripts/t1_index_vs_chern_2d.py:66). It tests Wilson overlap in 2D only, as the preregistration already admits at [PREREG.md:3–10](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/PREREG.md:3).

- **T3b/T3c: numerically reproduced, with a normalization correction.** The code computes \(\|1-r\|_\infty\), explicitly at [t3b_zolotarev_direct.py:33–36](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/scripts/t3b_zolotarev_direct.py:33), whereas the stated GW defect is \(\|1-r^2\|_\infty\), approximately twice as large. The pole-count conclusions survive: at \(M=1\), \(n=28\) gives a GW-defect upper estimate \(10^{-35.814}\), and \(n=70\) gives \(10^{-89.923}\). T3c has only an output file, [t3c_zolotarev_direct_targets.out:1–5](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/scripts/t3c_zolotarev_direct_targets.out:1); I reproduced it by calling the T3b function. The sampled dense-grid maximum is a strong numerical check, not a rigorous supremum certificate.

- **T4b: confirmed.** The corrected candidate selection and commutator test are at [t4b_staggered_adams_overlap_2d.py:44–68](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/scripts/t4b_staggered_adams_overlap_2d.py:44); all 24 flux cases reproduce index \(=-n\), [t4b_staggered_adams_overlap_2d.out:9–18](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/scripts/t4b_staggered_adams_overlap_2d.out:9). It demonstrates a one-component-per-site overlap carrier, not an evasion of Lemma R.

- **T5b: reproducibly passes its preregistered proxy.** The output at [t5b_u1_background_gap_4d_L4.out:1–3](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/scripts/t5b_u1_background_gap_4d_L4.out:1) is reproduced. It is only 24 fixed-seed Gaussian noncompact-U(1) samples on \(4^4\); the generator and dense diagonalization are at [t5b_u1_background_gap_4d_L4.py:16–25](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/scripts/t5b_u1_background_gap_4d_L4.py:16) and [line 51](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/scripts/t5b_u1_background_gap_4d_L4.py:51). It supports no nonabelian, equilibrium, thermodynamic-limit, or interacting claim.

## 6. F2-T reduction — core balance lemma confirmed; SMG collapse not confirmed

The Stokes argument at [ROUTE_REPORT.md:124–137](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_F2R/ROUTE_REPORT.md:124) correctly gives zero net Berry-monopole charge in each continuous integer-charge eigenbundle. For simple Weyl nodes this gives equal numbers of the two chiralities; generally it gives algebraic charge balance, not equal raw counts.

It does not prove that continuous time “collapses onto SMG.” It only excludes the specified free finite-band Hamiltonian class. Interactions/SMG are one remaining route, but extra dimensions, noncompact symmetry, non-locality/discontinuity, enlarged/infinite local Hilbert spaces, or other anomalous-boundary mechanisms have not been reduced to SMG. The cited Gioia–Thorngren construction explicitly uses a noncompact not-on-site symmetry ([paper](https://arxiv.org/abs/2503.07708)); Fidkowski–Xu address shallow-depth/locality-preserving implementations, not every conceivable non-on-site action ([paper](https://arxiv.org/abs/2306.10105)).

## Strongest correct statement

For a four-dimensional, translation-invariant, \(\gamma_5\)-Hermitian scalar-plus-vector free Dirac symbol satisfying canonical GW with \(R=\tfrac12\), if the symbol is rational in \(z=e^{ik}\) and admits a common denominator nonzero on \(T^4\)—equivalently, algebraically, it is a Schur complement of a finite-range system with finitely many auxiliaries and an invertible auxiliary block—then its GW projector extends to an algebraic idempotent on a principal open \(U\subset\mathbb A^4\); localization gives \(CH^{>0}(U)=0\), hence every Chern class of its restriction to \(T^4\) vanishes, and consequently the sum of local chiral indices of its isolated regular massless zeros is zero. Thus that class cannot realize a lone simple chiral species, regardless of finite fibre dimension; what is not proved is an exhaustive three-option physical price, the general-\(R\) gauge-background index formula, or the identification of every continuous-time escape with SMG.