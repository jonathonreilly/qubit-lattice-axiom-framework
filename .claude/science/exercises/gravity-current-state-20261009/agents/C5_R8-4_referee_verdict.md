# VERDICT: CONFIRMED WITH CORRECTIONS

The worker’s overall **INCONCLUSIVE** reading is correct. The one-loop construction and toy-N non-closure are real, but several scope statements require tightening.

## Findings

1. **Fermion sign and second-order identity — confirmed.**

   The CAR implementation applies monomials right-to-left with the standard parity sign, and constructs the Hermitian conjugate in reversed operator order (`scripts/r84_fock.py:40-70`). For an external \(X_p\), the decay intermediate contributes \(|K_X|^2/(E_p-W)\). Vacuum diagrams not containing \(X_p\) cancel between the one-particle and vacuum energies; the diagram containing \(X_p\) is Pauli-blocked only in the one-particle state, leaving \(+|K_0|^2/(E_p+W)\). Thus the reported fermionic sign is correct.

   The rerun reproduces the closed form to \(1.1\times10^{-16}\) (`scripts/r84_fock_part1.out:3-19`). My independent bit-set CAR implementation also reproduces toy N’s fermionic mixed coefficient to \(8.7\times10^{-17}\) ([r84_referee_checks.py:44](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-4/r84_referee_checks.py:44), [r84_referee_checks.out:3](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-4/r84_referee_checks.out:3)). The code’s use of `amp**2` rather than \(|amp|^2\) is valid only because every submitted amplitude is real.

2. **The \(h\) identity — confirmed, with an important classification correction.**

   Directly,
   \[
   \frac{h}{E-W}+\frac1{E+W}
   =\frac{2CW}{E^2-W^2},\qquad
   h=\frac{W(1+2C)-E}{W+E}.
   \]
   With \(h=1\),
   \[
   \frac1{E-W}+\frac1{E+W}
   =\frac{2E}{E^2-W^2}.
   \]
   Combining this with the spectral phase-space factor \(1/(2W)\) leaves the claimed \(E_p/W\) factor and hence momentum dependence. Independent random checks close both identities at \(1.1\)–\(1.8\times10^{-14}\) (`r84_referee_checks.out:1-2`).

   However, \(h(E_p,W)\) is frame-dependent, not a function solely of invariant masses. Therefore model S has compact invariant-mass plateau factors **plus a tuned non-scalar kinematic factor**; it is not literally a Hamiltonian whose complete vertices are only invariant-mass functions. This narrows the claims at `R8-4_report.md:28-34,109-117`.

3. **Spectator bound and rapidity budget — essentially confirmed, but the stated budget is only a sufficient approximation.**

   For equal masses and the mirrored vacuum cluster,
   \[
   s_{XY}=2m^2+2(E_pE_Y+\mathbf p\!\cdot\!\mathbf k_Y)
   \le 2m^2+2E_Y(E_p+|\mathbf p|).
   \]
   If \(E_Y\le E_{\max}\) uniformly and \(E_p+|p|=me^y\), a sufficient strict plateau condition is
   \[
   y\le
   \log\!\frac{\Lambda_1^2-2m^2}{2mE_{\max}},
   \]
   intersected with every leg, total-momentum and spectator cutoff. The report’s logarithm drops the \(2m^2\) term and should be labeled an asymptotic estimate (`R8-4_report.md:160-164`).

   Also, \(p=0.30\) is already outside the strict spectator plateau: the stored maxima are \(1.122\) for \(m=0.05\) and \(1.156\) for \(m=0.15\), both exceeding \(\Lambda_1=1\) (`scripts/r84_d3_oneloop_m0.05.out:22`, `scripts/r84_d3_oneloop_m0.15.out:22`). Thus the exact numerical plateau check is established through \(p=0.20\), not all rows before \(p=0.45\). The large \(p=0.45\) violation and its disappearance when spectator factors are removed are real.

4. **Toy N — closed form and failure confirmed; no class-wide no-go follows.**

   Both requested reruns reproduce the stored fermionic and bosonic results (`scripts/r84_toyN_fock_F.out:4-15`, `scripts/r84_toyN_fock_B.out:4-15`). The closed form at `scripts/r84_toyN_fock.py:58-76` follows from the forward insertion denominator
   \[
   \frac{|i|^2}{\alpha^2(\alpha-c)}
   \]
   and the four vacuum-relative orderings
   \[
   \pm |i_v|^2\frac{\alpha-b}{\alpha^2b^2}.
   \]
   A separate genuine bosonic occupation-number engine confirms the bosonic coefficient to \(1.9\times10^{-15}\) (`r84_referee_checks.out:6-8`). This matters because the worker’s generic boson path can over-enumerate annihilator subtuples when repeated occupations occur (`scripts/r84_fock.py:29-37,72-79`), although that latent defect does not change this mixed coefficient.

   An independent joint 4-D Sobol integral, avoiding the worker’s nested trapezoid route, finds relative drift at \(p=0.1\) of \(-0.0601\pm0.0031\) for fermions and \(-0.00598\pm0.00035\) for bosons ([r84_referee_qmc.out:1](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-4/r84_referee_qmc.out:1)). The failure is therefore real for toy N.

   The worker’s mass-scaling script did not keep \(p/m\) fixed (`scripts/r84_toyN_scaling.py:22-28`). Repeating it at \(p/m_X=1/3\) still gives fermionic coefficients \(-0.558,-0.460,-0.393\) and bosonic coefficients \(-0.0538,-0.0499,-0.0490\) as masses fall fourfold ([r84_referee_fixed_rapidity.out:1](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R8-4/r84_referee_fixed_rapidity.out:1)). Persistence over that window is confirmed; the \(m/\Lambda\to0\) limit remains open.

   I did not add the missing crossings because the submitted invariant-mass prescription does not define their vertex functions. Any such addition would introduce a new arbitrary model. They could restore covariance: a complete local bosonic crossing set recombines old-fashioned time orderings into the covariant diagram. Therefore the omitted \(2\leftrightarrow2\) and reverse-decay terms (`R8-4_report.md:225-228`) are a concrete unclosed restoration route.

5. **Bounded-below proof — confirmed with numerical and infinite-volume corrections.**

   At finite volume, each CAR monomial has norm at most one, \(H_0\ge0\), and translation invariance gives
   \[
   \|V_j\|\le |\Lambda|\,\|\kappa_j\|_1,
   \qquad
   H_\Lambda\ge-2|g||\Lambda|
   \left(\|\kappa_0\|_1+\sum_X\|\kappa_X\|_1\right).
   \]
   Smooth periodic kernels have super-polynomial Fourier decay and finite \(\ell^1\) norm, so a volume-uniform finite constant exists (`R8-4_report.md:120-130`).

   The quoted \(-105g|\Lambda|\) is not a rigorous bound: the \(L=192\) numbers give \(105.254623|g||\Lambda|\), and the sampled norms are still increasing with \(L\) (`scripts/r84_tails.out:1-6`). The rigorous statement is \(H_\Lambda\ge-C|g||\Lambda|\) for some finite \(C\); the \(d=1\) numerical estimate is about \(105.3\), not safely \(105\).

   Bru–de Siqueira Pedra’s theorem does support a \(C_0\)-group of CAR-algebra automorphisms for finite-\(\mathcal W\)-norm interactions, with polynomial decay functions explicitly allowed, but it does not itself produce one global infinite-volume Fock-space Hamiltonian [Bru–de Siqueira Pedra, Theorem 4.8](https://arxiv.org/html/1702.08869). The four-mode, dimension-16 site is also supplied block structure, not the axiom’s literal one-site \(M_2(\mathbb C)\) domain (`MINIMAL_AXIOMS_2026-06-29.md:43-50`; `R8-4_report.md:273-277`).

   Finally, the literature supports only the narrower BT statements: Polyzou restricts particle production to bounded bare-particle degrees of freedom, while Keister–Polyzou confirms BT’s cluster-separability failure for three or more particles and Sokolov restoration. Neither source establishes the report’s additional “not quasi-local” claim [Polyzou](https://arxiv.org/abs/nucl-th/0302023), [Keister–Polyzou](https://arxiv.org/abs/1109.6575).

6. **Reading — INCONCLUSIVE confirmed.**

   The fixed PASS explicitly requires “two-loop closure in a stated toy” (`TESTS.md:3523-3525`); toy N demonstrably does not close. Model S also omits \(2\leftrightarrow2\) orderings and uses the non-invariant \(h\) factor, so it should not be called a literal complete realization of the preregistered all-orderings INV class.

   The toy-N result is a **robust counterexample to radiative closure for this specified ordering-truncated Hamiltonian and tested parameter family**, not a bounded class no-go. Missing crossings, reverse decays, alternative crossing kernels and order-by-order vertex completion remain live routes. Conversely, the registered FAIL is not earned because no incompatibility theorem was proved; indeed, the CAR norm argument shows that adding any finite family of summable even crossing monomials preserves extensive boundedness. Thus neither fixed PASS nor fixed FAIL is met.

## Strongest correct statement

Conditional on a supplied four-CAR-mode block per lattice site, model S is an explicit finite-volume Hermitian, extensively stable and super-polynomially quasi-local quartic Hamiltonian whose on-shell \(O(g^2)\) dispersion is Lorentz-invariant within the strict spectator and cutoff plateau after imposing the frame-dependent fermionic factor \(h=(3W-E)/(W+E)\); the CAR sign, spectral identity and finite-Fock second-order formula are correct. For the precisely defined ordering-truncated toy N, the \(O(g_o^2g_i^2)\) correction is genuinely momentum-dependent—about \(-6.2\%\) for fermions and \(-0.60\%\) for bosons already at \(p=m_X/3\)—and this survives independent Fock, quadrature, Sobol and fixed-rapidity scaling checks. That establishes failure of radiative closure for toy N, but not for invariant-mass Hamiltonians with a completed crossing set, whose missing vertex prescription remains an open restoration route; consequently the fixed two-loop PASS is not met, the fixed incompatibility FAIL is not proved, and the correct campaign reading is **INCONCLUSIVE**.