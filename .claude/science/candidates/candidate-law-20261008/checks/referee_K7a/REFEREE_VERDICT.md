# VERDICT: CONFIRMED WITH CORRECTIONS

I reran the symbol, fermion \(L=4\), and real-space \(L=3,4,5\) runners, tested the fermion runner adversarially at \(L=3\), and added an independent exact-arithmetic check: [independent_exact_checks.py](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_K7a/independent_exact_checks.py:1).

## Item-by-item findings

- **(a) \(W(B_4)\) invariance — confirmed.**  
  The symbol is actually \(O(4)\)-covariant as a polynomial in \(H\) and \(s\), so signed permutations are automatic. The three exact symbolic generators in [k7a_symbol.py:103](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_K7a/k7a_symbol.py:103) generate \(W(B_4)\). The “all 384” loop at lines 95–101 is numerical sampling, but the generator calculation supplies the exact proof. The real-space action and gauge map were also exhaustively checked under all 384 coordinate/tensor maps at each tested \(L\).

- **(b) Gauge invariance — confirmed.**  
  \(K(s)D(s)=0\) is an exact symbolic identity, independently reproduced. The \(L=3,4,5\) real-space reruns give exactly zero residual. The real-space matrices use floating storage, but their coefficients are dyadic and the symbolic identity removes any scientific ambiguity.

- **(c) Spectrum/no doubling — confirmed, with wording narrowed.**  
  Exact arithmetic gives
  \[
  \operatorname{spec}(K/s^2)=\{-1,\;0^{\times4},\;(1/2)^{\times5}\}.
  \]
  Because the formula is \(O(4)\)-covariant in \(s\), evaluation at \(s=(1,0,0,0)\) proves this for every \(s\neq0\), rather than merely the 2,000 random samples at [k7a_symbol.py:120](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_K7a/k7a_symbol.py:120). Since \(2\sin(k_\mu/2)=0\) only at \(k_\mu=0\) in the fundamental Brillouin zone, there are no additional zero-momentum branches, including at the 15 nonzero corners. The grid minimum and random scan at lines 147–149 and 249–261 are not proofs by themselves. Also, “no extra modes” should read **no extra zero modes/doublers**; physical two-polarization counting additionally uses the ADM constraints. The docstring’s “all 16 zone corners” at [k7a_symbol.py:14](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_K7a/k7a_symbol.py:14) is a typo: the origin has nullity 10, so the relevant number is 15.

- **(d) ADM split — confirmed, with a normalization correction.**  
  The spatial block, inverse temporal block with eigenweights \(2(-1/2,1,1)\), and lapse row \(-R/2\) are exact. For the shift,
  \[
  \left.\frac{\partial Q}{\partial h_{4i}}\right|_{h_{4\mu}=0}
  =-s_4s_j\bigl(h_{ij}-\delta_{ij}\operatorname{tr}_3h\bigr).
  \]
  The submitted row is taken in \(q_{4i}=\sqrt2\,h_{4i}\) coordinates, so it appears with \(-1/\sqrt2\); calling it directly \(dQ/dh_{4i}\) at [k7a_symbol.py:209](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_K7a/k7a_symbol.py:209) is imprecise. The ADM comparisons also import `stag2` through a hard-coded sibling path at [k7a_symbol.py:155](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_K7a/k7a_symbol.py:155) and [k7a_realspace.py:269](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_K7a/k7a_realspace.py:269). It currently hashes identically to the supplied `ref/stag2.py`, but this is a reproducibility defect.

- **Propagators — same denominator, not identical propagators.**  
  The photon propagator in Feynman gauge is \(\delta_{\mu\nu}/s^2\). For gravity,
  \[
  K_{\rm gf}=\frac12s^2A,\qquad
  A=I-\frac12tt^T,\qquad A^2=I,
  \]
  hence
  \[
  K_{\rm gf}^{-1}=\frac{2}{s^2}\left(I-\frac12tt^T\right).
  \]
  Thus both have the same \(1/s^2\) pole and tree-level dispersion, but not the same tensor numerator or normalization. [k7a_symbol.py:11](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_K7a/k7a_symbol.py:11) also says \(1/4\), whereas the actual exact result at lines 136–138 is \(1/2\).

- **Staggered fermions and Wilson \(U(1)\) — confirmed on \(\mathbb Z^4\), with an even-volume caveat.**  
  An exact parity-cocycle calculation finds site signs for all 384 signed permutations. Wilson-link orientation/conjugation then gives the interacting identity link by link, and the plaquette action is invariant. The submitted interacting test uses only one random link configuration at [k7a_fermion_gauge.py:121](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_K7a/k7a_fermion_gauge.py:121), although the underlying statement is exact. Periodic finite tori require even extents: at \(L=3\), only 1/384 transformations survives and the runner then crashes at [k7a_fermion_gauge.py:154](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_K7a/k7a_fermion_gauge.py:154). This does not contradict the infinite-\(\mathbb Z^4\) claim.

- **The 9/4/1 count — confirmed exactly, but only for the stated finite-dimensional ansatz.**  
  Exact monomial-orbit and rational-rank algebra gives:
  \[
  \dim \mathcal Q^{W(B_4)}=9,\qquad
  \dim \mathcal Q^{O(4)}=4,\qquad
  \dim\ker(\delta_\xi|\mathcal Q^{W(B_4)})=1.
  \]
  The submitted implementation used generic rotations and 40 random momenta at [k7a_symbol.py:291](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_K7a/k7a_symbol.py:291); the independent check removes that sampling gap. The count applies to homogeneous constant-coefficient symbols \(C_{IJab}h_Ih_Js_as_b\), equivalently onsite contractions of two half-step derivatives. It is not a count of all finite-range lattice kernels: gauge-invariant higher-derivative/form-factor terms such as \(f(s)K_{\rm EH}(s)\) remain possible. Therefore gauge symmetry protects the unique leading two-derivative graviton tensor structure and its single TT speed, not the complete finite-momentum dispersion against arbitrary lattice corrections. This is conditional, not circular: exact gauge symmetry with the chosen \(D(s)\) is an input.

- **Conformal mode and tick conditions.**  
  The \(L=4\) count of 255 negative directions is reproduced. It proves that the unreduced real Euclidean quadratic form is indefinite and lacks a positive Gaussian weight. It does **not by itself prove that no positive physical transfer matrix exists after constraints, gauge reduction, or a conformal contour prescription**; no transfer-matrix positivity test appears in the packet. The two-fine-edge tick is consistent bookkeeping. Leapfrog instability at \(\tau=a_s\) is exact: stability requires \(\tau^2\max s_{\rm spatial}^2\le4\), while \(\max s_{\rm spatial}^2=12\), hence \(\tau\le1/\sqrt3\).

## Prior literature

From memory, the closest established line is Roček–Williams linearized/quantum Regge calculus on subdivided hypercubic lattices, followed by Barrett’s linearized Regge theorem and Höhn’s canonical lattice-graviton analysis: [Roček–Williams (1981)](https://www.sciencedirect.com/science/article/abs/pii/0370269381908480), [Barrett (1987)](https://inspirehep.net/literature/250048), [Höhn (2015)](https://arxiv.org/abs/1411.5672). Those use simplicial edge-length variables and vertex-displacement symmetry; I do not know a published source for this exact 10-component half-shift \(h_{\mu\nu}\)/link-centered \(\xi_\mu\) stencil. That is not a novelty proof.

## Strongest correct statement

For the specified nearest-role, homogeneous two-half-step-difference discretization on \(\mathbb Z^4\), the quadratic linearized Einstein–Hilbert action is exactly \(W(B_4)\)-covariant and exactly invariant under the staggered linearized diffeomorphism, has only the four gauge zero directions at every nonzero Brillouin-zone momentum with spectrum \(s^2\{-1,0^{\times4},(1/2)^{\times5}\}\), and reduces algebraically to the stated ADM potential, DeWitt kinetic inverse, and Hamiltonian/momentum constraint rows. De Donder/Feynman gauge gives gravity and photon the same \(1/\sum_\mu4\sin^2(k_\mu/2)\) pole denominator, though different numerators. Within the constant-coefficient \(O(s^2)\) ansatz the exact invariant count is genuinely \(9/4/1\), so gauge symmetry removes all five hypercubic-but-non-\(O(4)\) leading graviton structures; this does not constrain higher-derivative lattice artifacts or prove transfer-matrix positivity.