# VERDICT: CONFIRMED WITH CORRECTIONS

Full referee report: [R5-1_referee.md](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R5-1/R5-1_referee.md:1>).

1. **Lemma K — confirmed.** The stabilizer classification is correct (`R5-1_report.md:101-108`). The explicit off-axis matrix is integral Lorentz, fixes `(1,3,0,0)` and `e₃`, and has characteristic polynomial \((t-1)^2(t^2-30t+1)\), hence is loxodromic (`scripts/r51_stab_offaxis.py:17-25`; referee lines 7–21).

2. **Theorem W — confirmed with qualification.**
   - **(i)** Properness and pullback/change-of-variables are correct (`R5-1_report.md:119-129`). Sigma-finiteness needs the omitted a.e.-injectivity argument, but that repair is valid.
   - **(ii)** The Fourier-support argument works. Only the Haar-absolutely-continuous correlations are confined; the singular part is uncontrolled (`R5-1_report.md:121,130-134`).
   - **(iii)** Recurrence along one loxodromic kills both null-axis contractions. The remainder is spacelike, so positive energy forces zero (`R5-1_report.md:135-137`).

3. **Theorem Q — core theorem confirmed, consequences narrowed.**
   - Every \(\Gamma_x\) has infinite index because every nonzero orbit is infinite; the Neumann step is valid (`R5-1_report.md:154-158`).
   - Continuous equivariant event rules, including past-cone rules, are condition-independent.
   - A full DLR specification is therefore product. An arbitrary retarded kernel need not determine a product joint law: spacelike/common-source correlations remain possible without an additional generative assumption.
   - Q does not directly refute Admissibility as written. The axiom concerns `Z³`, finite nearest neighbors, and cubic symmetry, not `L₇` with full \(\Gamma\) covariance (`MINIMAL_AXIOMS_2026-06-29.md:35-61`). An explicit bridge is required; tail dependence would also cease to be literal nearest-neighbor dependence.

4. **Proposition L — confirmed conditionally.** The commutator/Fourier argument is correct (`R5-1_report.md:170-175`). Projected mass shells are Haar-null, and the positive/negative classes are mutually singular because their overlaps are countable unions of at-most-two-dimensional sections (`R5-1_report.md:176`). `(SC_m)` is a strong extra hypothesis not supplied by the axioms or ordinary positive energy; Bragg relifts with variable mass evade it (`R5-1_report.md:182`).

5. **Lemma H — confirmed.** No invariant probability exists on \(H^3\), and the equivariant-pushforward argument is valid (`R5-1_report.md:184-192`). The state/ensemble conclusion requires the stated measurable equivariant disintegration and does not cover branches defining no rest frame (`R5-1_report.md:196-198`).

6. **Example D — checks reproduced exactly.** All three scripts matched their saved outputs byte-for-byte. Covariance, decay, boosted-frame quadrature, and \(2/\pi\) one-particle weight reproduce (`scripts/r51_diamond_link.out:1-37`). Corrections:
   - the script tests the Gaussian, not the compact diamond profile;
   - its unequal-correlation test only shows \(g_1\) is not a stabilizer; stabilizer finiteness comes from Lemma K.
   
   The construction is sound but imports a continuum Fock space and mass shell; it is not an LRL-generated law (`R5-1_report.md:239-247`).

7. **Class statement — bounded FAIL is correct.** The fixed rubric expressly permits a no-go “in a stated class” (`TESTS.md:2870-2873`). Theorem W alone supplies a valid nontrivial class—qubit operators supported on points, spacelike lines, and spacelike planes (`R5-1_report.md:139-142`). The open finite-stabilizer timelike-link class prevents an exhaustive no-go but does not force INCONCLUSIVE under the fixed rubric.

**Strongest correct statement:** On \(L_7\), every finite-dimensional covariant operator family with infinite pointwise support stabilizer—including qubit operators supported on a point, spacelike line, or spacelike plane—has no standard massive or massless shell component; its Haar-a.c. correlations are confined to the stabilizer-fixed spacelike sublattice, and any decomposable covariant positive-energy four-charge vanishes on it. Continuous full-\(\Gamma\) event rules are condition-independent, full DLR versions are products, strict all-cell locality excludes fixed-mass content only under `(SC_m)`, and measurable frame-picking cannot be restored by invariant averaging. Continuum-smeared timelike links demonstrate consistency but import set A. Finite-stabilizer link cells with noncommuting timelike structure under a genuinely LRL-generated covariant law remain open; the correct recorded result is therefore **FAIL, bounded to the corrected stated classes**, not INCONCLUSIVE.