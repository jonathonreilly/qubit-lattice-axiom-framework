# C3 lane M-B: referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-10)

# VERDICT: CONFIRMED WITH CORRECTIONS

The lane verdict is correctly **INCONCLUSIVE**, but several no-go and swerve statements require narrower scope.

## Findings

1. **Theorem A is correct under A1–A3.** The invariant nonnegative weight \(n(y,x)\), Palm/Mecke construction, and Lorentz-invariant-measure lemma correctly force \(W(y,x)=0\) for \(y\neq x\). This covers finite-dimensional event fibers with a positive event-local norm and single-event isometry, including jointly Lorentz-invariant-in-law auxiliary randomness. [C3_M-B_report.md:65–83](<C3_M-B_report.md:65>)

   Correction: it proves **no nontrivial off-event propagation**, not literally “no unitary rule.” A diagonal stay/internal unitary remains possible. Infinite-dimensional event fibers, nonlocal norms, supplied frames/slices, and isometry restricted to an extended-state subspace are outside the theorem. [C3_M-B_report.md:73](<C3_M-B_report.md:73>) [C3_M-B_report.md:98–102](<C3_M-B_report.md:98>)

2. **Theorem B is confirmed, but only as a slice-selection theorem.** A stationary Poisson sprinkling cannot equivariantly select a nonempty antichain of its events; the column-count argument is sound. It does not forbid covariant dynamics defined for supplied slices or slice pairs. “A supplied slice carries a frame” is not proved in the required generality. [C3_M-B_report.md:106–110](<C3_M-B_report.md:106>) [C3_M-B_report.md:319–323](<C3_M-B_report.md:319>)

3. **C1 is not a class-S no-go.** The divergent expected number of arbitrarily long past links supports the statement that event amplitudes on a finite-depth cut are not Cauchy data for an all-link recursion. The almost-sure upgrade is argued, not proved here. It does not obstruct independent antichain-to-antichain walks or the correct crossing-link data. [C3_M-B_report.md:112–115](<C3_M-B_report.md:112>)

4. **C2’s dimension identity is exact but narrow.** For a finite frontier updated by one naturally labelled element, \(\Delta\dim=1-k\); hence an isometry fails when \(k\ge2\), and an onto unitary requires \(k=1\). The numerical frequencies reproduce this bookkeeping. It does not cover infinite antichains, nonlocal slice maps, skipped/grouped updates, other labellings, ancillary degrees of freedom, or Fock-space evolution. [C3_M-B_report.md:117–131](<C3_M-B_report.md:117>) [s3_frontier_merge.py:1–6](<work/scripts/s3_frontier_merge.py:1>)

5. **The rapid swerve result is confirmed only for the greedy nearest-continuation chain.** Every permutation coin has the exact nearest-out-link kick lower bound, with measured mean \(0.465\), but that alone does not force outward drift. The greedy chain has the exact i.i.d.-isotropic law and asymptotic \(0.0805\) rapidity drift per link; it is not a bijection and therefore is not itself a unitary permutation coin. [C3_M-B_report.md:162–178](<C3_M-B_report.md:162>) [C3_M-B_report.md:332–336](<C3_M-B_report.md:332>)

   Re-extracting the stored trajectories gives first \(\gamma\ge2\) at median 7 links, mean 8.3 links; cumulative segment proper time is median \(9.75\,\ell_P\), mean \(11.4\,\ell_P\). Thus “roughly 7–10 links/about \(9.5\,\ell_P\)” is a sound typical value, not a universal 20-Planck-time bound. [C3_M-B_report.md:327–330](<C3_M-B_report.md:327>) [s2 output:1–3](<work/out/s2_greedy_chain_swerve_3p1.out:1>)

6. **Arc states are not excluded, but neither are they constructed.** “Survive” should mean only that Theorem A does not apply. No measurable equivariant unitary arc coin, massive one-cone mean, or controlled kilometre-scale detector coherence law is supplied. The fixed-profile mismatch tests cover only particular compact ball/Gaussian profiles and are not general decoherence theorems. [C3_M-B_report.md:140–145](<C3_M-B_report.md:140>) [C3_M-B_report.md:186–220](<C3_M-B_report.md:186>)

The fixed reading therefore gives INCONCLUSIVE: no construction earns PASS, while arc states and general supplied-slice dynamics prevent a comprehensive FAIL. [TESTS.md:489–497](<TESTS.md:489>) [PREREG.md:37–40](<work/PREREG.md:37>)

## Strongest correct statement

On an infinite homogeneous Poisson sprinkling, no jointly Poincaré-equivariant isometry with finite-dimensional event fibers and a positive event-local norm can propagate a basis state to another event: all off-diagonal amplitudes vanish. The sprinkling also cannot intrinsically select a nonempty antichain. These results do not exclude dynamics on supplied slices or on the infinite-dimensional space of causal links. For link states, the greedy nearest-continuation chain rapidly swerves toward the light cone, but arbitrary unitary permutation coins and spreading arc coins remain unclosed. Consequently, definability of a suitable arc-unitary, a massive one-cone mean, and controlled packet coherence over 1 km are all still open.