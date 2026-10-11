# Lane RC, probe C1: reduction and emergent SLAC bands. Report

**Provenance.** Worker: Claude Opus 5.5 (same model family as the supervisor). Ran 15:43Z to about 16:10Z on 2026-10-11. Not refereed. No repository files were edited.

**Scratch folder:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/laneRC/C1/`

| Script | Output | What it does |
|---|---|---|
| `c1_checks.py` | `c1_checks.out` | Koszul lemma; Lemma R null space |
| `c1_harmonic.py` | `c1_harmonic.out` | The singular-improvement loophole |
| `c1_approx.py` | `c1_approx.out` | Whole-zone best-uniform LP. Its window rows are unreliable below about 1e-7, the LP tolerance. |
| `c1_approx2.py` | `c1_approx2.out` | Window rates, bounded band, 1-band E, filtered Fourier |
| `c1_twoband.py` | `c1_twoband.out` | Two-band network with the face kink built in |

## Reading against the FIXED lines

**PASS is not met.** No finite network gives an exact SLAC band. Theorem B1 proves this impossible for the stated class.

**FAIL (bounded) is supported, pending the codex sol referee.**
- **The reduction holds** (Theorem A, proved under hypotheses H1–H5, listed in §a.1). Exactness plus closure forces E² = m² + c²|k|² on the lifted cube. It also forces the law to be umklapp-free; that is a consequence, not an assumption.
- **Impossibility, proved for these classes:**
  - (i) finite-component one-body (quadratic) networks whose Bloch matrix has real-analytic periodic entries. That covers any finite range, exponentially decaying hopping, any depth, gapped or gapless, Hermitian, Bogoliubov or non-Hermitian, and Schur complements over finite mediator networks;
  - (ii) dressed bands where the band is a simple root of a secular function that is analytic at the zone face. This includes a single band with a Herglotz self-energy whose continuum is gapped above the band at some face point.
- **Named and not closed:**
  - dressed bands with gapless mediators, where the emission threshold touches the band at every k;
  - non-transfer-regular (dipolar-tailed) divergence-free improvements;
  - laws whose normal scattering vanishes on open sets;
  - d = 1.

**Q1 has a new feature.**
- The whole-zone limit depends on the number of bands.
  - A single smooth band: O(1/n) error, and the closure residual never drops below πc².
  - A two-band network whose bands touch exactly at the face: both fall faster than any power of n on the whole zone (checked in 1D).
- Windowed errors are exponential, at the Bernstein–Walsh rate ρ(κ).

## (a) The reduction

### a.1 Setting and hypotheses

- Translation-covariant local H on Z^d, finitely many fields per site, with energy density h(x) whose total is H.
- J_E is the local energy current: ḣ = −div J_E, with backward-difference divergence.
- Closure (G3 and the RN L3 referee) gives div P_shift = div J_E. Write w := P_shift − J_E, so div w = 0.

**Hypotheses.**
- **H1 (transfer-regular improvement).** w is finite-range, or more generally each n-body kernel of w is ℓ¹. For the total-level lemma it is enough that w's form factor be continuous at transfer q = 0.
- **H2 (regular one-particle states).** The asymptotic species are isolated bands E_α(k). Form factors of local densities between one-particle states are continuous on the diagonal, and t(k,k) = E(k) after vacuum subtraction.
- **H3 (exact conservation with clustering).** ΣP_shift is exactly conserved and acts additively on asymptotic states (the RN L2 referee's premise).
- **H4 (scattering).** The total 2↔2 amplitude T ≠ 0 almost everywhere on the normal on-shell set of the lifted cube U = (−π,π)^d. Normal means lifted momentum is conserved with no 2π.
- **H5 (dispersion).**
  - d ≥ 2.
  - E ∈ C¹(U∖S), where S is closed and U∖S is connected (this allows a cone at k = 0).
  - E² ∈ C²(U∖S).
  - E is not constant and is covariant under proper cubic rotations (C4 for d = 2, O for d = 3).

### a.2 Lemma C, cohomology (two versions)

**C-alg (PROVED, finite range).** On Z^d, let w be a finite-range, translation-covariant, divergence-free edge field of local operators. Then w = curl A + c·1, where A is a finite-range, translation-covariant antisymmetric 2-form and c ∈ C^d.

*Proof.*
1. Densities are fixed by their seeds in the local algebra 𝔄_loc. div is the Koszul map with u_j = 1 − τ_{−e_j} over R = C[t_1^{±1}, …, t_d^{±1}].
2. 𝔄_loc = C·1 ⊕ 𝔄⁰, where 𝔄⁰ is spanned by Pauli strings (or Majorana or normal-ordered monomials) with nonempty finite support.
3. Translations act freely on such strings, since no finite nonempty set is translation-invariant. So 𝔄⁰ is a free R-module.
4. (u_1, …, u_d) is a regular sequence in R: modulo u_1, …, u_{j−1}, the remaining ring is C[t_j^{±1}, …], and in it u_j is not a zero divisor.
5. So the Koszul complex on 𝔄⁰ is acyclic in positive degree, H_1 = 0, and every divergence-free w is a curl.
6. On C·1, u_j acts as 0, so H_1 = C^d. These are the constants.
7. Hermiticity is kept by taking hermitian parts.
8. **H_0 statement:** a degree-0 density with zero total is a divergence. This is the translation-covariant, finite-range local Noether statement, so J_E exists and has finite range. ∎

*Checks:*
- **CHECKED** (`c1_checks.out` K): every divergence-free W in boxes [−2,2]², [−3,3]² and [−1,1]³ (16, 36 and 28 dimensions) is a curl from a box one site larger, with residual ≤ 9e-16.
- **Quasi-local, exponentially decaying densities: ARGUED.** The same Koszul argument works over functions holomorphic on a polyannulus, by Hadamard division at t_j = 1.

**C-tot (PROVED, weaker hypothesis).** Let w be divergence-free, and let each n-body form factor W_j(k′;k), with transfer q = Σk′ − Σk, be continuous at q = 0. Then Σ_x w_j(x) vanishes in every sector with at least one leg. Only the c-number part survives.

*Proof.*
1. div w = 0 means Σ_j (1 − e^{−iq_j}) W_j(k′;k) = 0 for all q ≠ 0.
2. Approach a q = 0 point along q = εe_j, divide by ε, and take ε → 0. This gives W_j = 0 on the q = 0 hyperplane. ∎
3. ℓ¹ kernels satisfy the continuity hypothesis.
4. So does the SLAC current itself: it is not ℓ¹, but its form factor is continuous at q = 0 for k off the face.

**Answer to the RN L3 caveat.** "Divergence-free = local curl + constant" is proved for finite range. For the totals, only C-tot is needed. **Consequence:** ΣP_shift = ΣJ_E + c·N, as derivations (exactly, for the finite-range form).

**The precise loophole (CHECKED that it exists).** Let w have the symbol Π_jl(q)c_l(k), with Π_jl = δ_jl − ū_j u_l/|u|² and u_j = 1 − e^{−iq_j}.
- It is divergence-free: |div| ≤ 1e-15.
- Its limit at q = 0 depends on direction, so its total can be set to anything, for example the sawtooth on top of nearest-neighbour Klein–Gordon.
- Its kernel is about R^{−d}: slope −1.97 for d = 2. The ℓ¹ sums grow by 0.44 per doubling (`c1_harmonic.out`).
- **SUGGESTED:** its momentum-continuity completion needs a stress singular as 1/q. The longitudinal limit of P at small q is still that of J_E. So this is a formal loophole, carrying power-law non-locality of SLAC's order.

### a.3 Lemma D, the energy-current symbol (PROVED; G3 re-derived with continuity stated)

Energy continuity between one-particle states gives

i(E(k+q) − E(k)) t(k+q,k) = −Σ_j (1 − e^{iq_j}) j_j(k+q,k).

Take q = εn and let ε → 0. Using H2, and continuity of j (C-alg, J_E finite-range): n·j(k,k) = E n·∇E for every n.
- So the one-particle action of ΣJ_E is E∇E.
- **Degenerate (taste) blocks.** With a smooth band frame the same limit gives E∇E·1. The symbol is forced to be **taste-universal** (a multiple of the identity).

### a.4 Lemma R, collision invariants of the normal set (PROVED; cleaner than L2-A, with no second derivatives of F)

**Statement.** Let d ≥ 2 and U′ = U∖S be connected. Let E ∈ C¹(U′), with ∇E(U′) not contained in any affine line. Suppose F ∈ C¹(U′) satisfies F(k1)+F(k2) = F(k3)+F(k4) whenever all k_i ∈ U′, k1+k2 = k3+k4 and E(k1)+E(k2) = E(k3)+E(k4). Then F = λE + b·k + c on U′.

*Proof.*
1. **Fix a pair.** Take a, b with ∇E(a) ≠ ∇E(b), and set K = a+b. On the open set V = U′ ∩ (K−U′), the functions g = F(q)+F(K−q) and Ω = E(q)+E(K−q) are C¹, and ∇Ω(a) ≠ 0.
2. **g is constant on the level set.** Every q ∈ V with Ω(q) = Ω(a) is a normal collision partner, so g(q) = g(a). Near a, the set {Ω = Ω(a)} is a C¹ hypersurface of dimension d−1 ≥ 1. Hence ∇g(a) ∥ ∇Ω(a):

   ∇F(a) − ∇F(b) = λ_ab (∇E(a) − ∇E(b)).   (*)
3. **λ is constant.**
   - If u = ∇E(a)−∇E(b) and v = ∇E(b)−∇E(c) are independent, adding (*) for (a,b) and (b,c) and comparing with (a,c) gives λ_ab = λ_bc = λ_ac.
   - Because the gradient image is not contained in a line, a chain of at most two such triangles links any two pairs. (Case analysis: use a third point off the line, then whichever of a, b is off line(x,c).)
   - So λ ≡ λ0.
4. **Integrate.** ∇(F − λ0E) is constant. Points with equal gradients are handled through a third point. Connectedness of U′ finishes the proof. ∎

**Check (`c1_checks.out` R).** d = 2, m = 1, 600 normal collisions in the open cube, 17-column basis. The null space is {k_x, k_y, E} plus one basis dependency (E² is affine in the basis), for both nearest-neighbour Klein–Gordon and SLAC. The collision defect of f = E∇E on the normal set:
- Klein–Gordon (f = sin k): 2.44 max, so it fails;
- SLAC (f = k): exactly 0.

### a.5 Theorem A, the reduction (PROVED, same-family, unrefereed)

**Statement.** Under H1–H5, the following are forced:
- E² = m² + c²|k|² on U (exact SLAC on the lifted cube);
- T = 0 a.e. on every umklapp configuration, so the law must be umklapp-free.

*Proof.*
1. C-alg or C-tot, with D: the one-particle symbol of ΣP_shift is f = E∇E.
2. H3 and H4: each component f_j satisfies the hypotheses of Lemma R. f_j ∈ C¹ because E² ∈ C².
3. Lemma R gives E∇E = aE + Bk + c, with a, c ∈ R^d and B ∈ R^{d×d}.
4. f = ∇(E²/2) has a symmetric Jacobian, so a⊗∇E − ∇E⊗a is constant. If a ≠ 0, this confines ∇E to an affine line. So a = 0 and B is symmetric.
5. Integrate: E² = k·Bk + 2c·k + e.
6. Cubic covariance gives B = c²·I and c = 0. (The symmetric commutant of C4 or O is the scalars.)
7. A cubic-covariant nonconstant E cannot have its gradient image in a line, so H5's line condition holds automatically.
8. Then f = c²k jumps by 2πc²m on umklapp configurations, so T must vanish there. ∎

**Oddness is not needed:** it follows from the theorem.

**Matrix bands and tastes (PROVED per band; one item ARGUED).**
- ΣP commutes with h(k), so its one-particle action is block-diagonal on eigenspaces. Each nondegenerate band, and each degenerate taste block, carries f_α = E_α∇E_α (times 1).
- **Each band with intraband normal scattering a.e.** is forced to E_α² = m_α² + c_α²|k|² on its lifted zone. For staggered matter that is the open reduced cube of period π.
- **Two species that each self-scatter and also scatter elastically off each other,** with a nondegenerate AB collision set, must share c_α = c_β (PROVED). The masses may differ.
- **Interspecies-only scattering** (Compton with no self-scattering): **ARGUED**, not proved.
- **This subsumes G3's "network-carried current" option (ii).** J_E is the total current of the full nearest-neighbour system, so every asymptotic species that scatters, mediators included, must be exactly SLAC with the common c.

**Outside the theorem (named):**
- the dipolar-tail improvements of §a.2;
- laws with T = 0 on open parts of the normal set (the conclusion is then only local);
- species that never scatter, which are free;
- d = 1;
- modified gravity completions (C3's business).

## (b) Emergent SLAC

### Theorem B1 (PROVED, rigorous, any d ≥ 1)

**Statement.** Let h(k) be an n×n matrix whose entries are real-analytic and 2π-periodic on R^d. Equivalently, its hopping decays exponentially (Paley–Wiener). Then no eigenvalue of h equals G(k) = √(m² + c²|k|²), with c ≠ 0, on any nonempty open set V. The same holds for E² = G² on V.

*Proof.*
1. Let χ(λ,k) = det(λ − h(k)), and put Ψ(k) = χ(√G², k)·χ(−√G², k). This is a polynomial in G² = m² + c²|k|² with coefficients analytic on R^d, so Ψ is real-analytic on all of R^d.
2. Ψ vanishes on V, so by the identity theorem it vanishes on all of R^d.
3. Hence ±G(k) is an eigenvalue of h(k mod 2π) for every k ∈ R^d.
4. But eigenvalues are bounded by sup_T ‖h‖ < ∞, while G is unbounded. Contradiction. ∎

**Rigor notes.**
- Branch points and the global structure of the bands never enter. The identity theorem is applied to Ψ, which is analytic everywhere. The even-product trick also removes the m = 0 cone, so the proof holds for d = 1 too.
- **Equivalent transcendence form.** On a generic line through V, a nonzero polynomial relation P(t², e^{it}) = 0 on an interval contradicts the linear independence of t^a e^{ibt}. This is also rigorous, and equivalent to the boundedness argument.
- **Coverage:** gapless networks, Bogoliubov frequencies (ω² is an eigenvalue of a trigonometric-polynomial dynamical matrix), and integrated-out finite mediator networks (clearing the rational denominators gives a polynomial).
- **SLAC escapes** only because h = k is analytic on the open cube alone (1/r hopping).

### Proposition B2, dressed bands (PROVED under the stated hypotheses)

**Kink condition.** Let E be a simple root of F(λ,k) = det(λ − h(k) − Σ(k,λ)). If F is analytic near (E(k_f), k_f), the analytic implicit function theorem makes E analytic near k_f. So it cannot have SLAC's Λ-kink there.

**Necessary condition for an exact SLAC dressed band:** every face point lies either in the non-analytic set of F (a wall) or on a band touching.

**Single band with Herglotz Σ and a gapped continuum.**
- Σ = ∫ρ/(λ−ω) with ρ ≥ 0, so ∂_λF ≥ 1, and Σ is jointly analytic below the threshold λ_th(k).
- **Rigidity:** if the band is SLAC on an open set and stable on the open cube, it is SLAC on the whole open cube.
- **Face condition:** E(k_f) = λ_th(k_f) on the entire face. The band must merge with the continuum along the whole zone face.
- If the continuum is strictly gapped above the band at any face point, exact SLAC is impossible.

**Gapless mediators: OPEN.** A subsonic quasiparticle always sits at its soft-emission threshold, λ_th(k) = E(k) for all k. So B2 is silent.

**SUGGESTED, by power counting.** A self-sustained first-order face kink would need the soft-emission integral to produce a term linear in the distance δ from the face. With vertex |g|² ~ |q|^{2a}, the soft part scales as δ^{d+2a−1} (possibly with logarithms). A term linear in δ therefore needs d + 2a = 2. That is marginal infrared coupling (QED-like in d = 3), where charged particles become infraparticles with no sharp band.

**Fermi seas: ARGUED, standard.** A moving particle can always emit soft particle–hole pairs, so the band has nonzero width away from its minimum. There is no exact band, so no exact SLAC band.

**Exact band touchings are a real mechanism for kinks** (CHECKED; see (c)). A two-band network with d(k) = (1 + e^{ik})a(k) has an exact Λ-kink at the face in its lower band. B1 still forbids exact SLAC, because the continuation of the SLAC branch past the face is unbounded.

## (c) Readout Q1 (units c = 1, per axis; the d-dimensional SLAC E² is separable)

| Construction (n = range, i.e. trigonometric degree) | Error on the whole zone | Closure residual sup\|E∇E − c²k\| |
|---|---|---|
| 1 band, E² = m² + p_n, best uniform | **1.760/n** (fit exponent −0.9997, n = 16–192). Order 1/n is optimal (Bernstein inverse theorem) | **= π on the zone for every n.** **PROVED** lower bound πc² for any band with E² ∈ C¹, since E∇E is then continuous and c²k jumps by 2πc². Still about 0.88 on \|k\| ≤ π/2: the best-uniform approximant does not converge in C¹ |
| 1 band, smooth-filtered Fourier exp(−36η⁸) | 6.82/n | π on the zone. On \|k\| ≤ π/2: 8e-9 (n = 64), 4e-15 (n = 128). On \|k\| ≤ 3π/4: 1.3e-4 (n = 64), 8e-9 (n = 128) |
| 1 band, window \|k\| ≤ κ, near-best | ≈ A n^{−3/2} e^{−ρ(κ)n}, with ρ(κ) = arccosh((3+cos κ)/(1−cos κ)) = 3.23, 1.76, 0.81 for κ = π/4, π/2, 3π/4. Fitted 3.11, 1.72, 0.79 | Window residual local rates 3.1, 1.7, 0.78. The approximants stay bounded on the zone, max\|p\| ≤ 9.3, so the stability constraint 0 ≤ p ≤ π² is not binding (LP agrees to its 1e-8 to 1e-10 floor) |
| 1 band, approximating E itself (fermion-like) | Window rate is capped by the branch point k = ±im/c: ρ_m = arccosh((2cosh(m/c) − 1 − cos κ)/(1 − cos κ)) = 0.14 (m = 0.1) and 0.42 (m = 0.3). Fitted local rates 0.16 and 0.45 (pre-asymptotic) | — |
| **2 bands, exact touching at the face** (`c1_twoband.out`, m = c = 1) | 3.2e-4 (n = 8), 2.0e-8 (64), 3.2e-11 (128), 4.8e-14 (192) | **On the whole zone:** 8.3e-3, 4.1e-6, 1.3e-8, 3.1e-11. Faster than any power of n; the rate is set by the C^∞ gluing window, so no exponential rate is claimed |

**Does approximate SLAC suffice for closure? (G3's defect formula)**
- The one-particle defect is δ = E_n∇E_n − c²k = ½∇(E_n² − c²k² − m²). That is the gradient of the E² error, so closure is a C¹ approximation problem, not a C⁰ one.
- This holds whether the defect sits in (E), with P_shift = sawtooth, or in the conservation of ΣJ_E, with P_shift = J_E: there δ(k1)+δ(k2)−δ(k3)−δ(k4) per normal collision. The two routes are equivalent.
- **A single smooth band:** the residual is exponentially small for content confined to |k| ≤ κ, and of order 1 (at least πc²) at the face for every n.
- **Two bands touching at the face:** the face residual can be made small on the whole zone. **But** the partner band is degenerate with the matter band on the face and is not SLAC (it has a V-kink). Interband scattering at lattice-scale momenta then breaks the collision invariant there. **SUGGESTED:** the band projector is non-analytic at the touching, so analytic vertices cannot exclude this exactly, an umklapp-like obstruction moved to the face. Not computed.

**n\*** (READING, conditional; G3's design-A assumption that the response is quadratic in the defect, with B ≈ 5.7e-99): n\* ≈ ½ln(1/B)/rate = 113/rate.
- **1 band, window-confined content:** about 36, 66 and 145 range steps for κ = π/4, π/2 and 3π/4. Double these for a linear law.
- **1 band, face content (vacuum, lattice-scale momenta):** no finite n\* unless the face is removed separately, the same structure as G3's floor.
- **2 bands:** n\* is not determined. The rate has not been optimised, and it depends on the partner-band issue.

## Against the supervisor expectation

| Expectation | Outcome |
|---|---|
| Reduction holds | Confirmed, under H1–H5. Oddness is a consequence, not an input. Umklapp-freeness is forced. Taste-universality of the symbol is forced. |
| Transcendence obstruction | Confirmed, and made rigorous by an elementary boundedness and identity-theorem proof. It extends to every exponentially local finite-component network. |
| Error exponential in depth | **Only on sub-windows,** at rate ρ(κ). On the whole zone, a smooth single band gives 1/n, and its closure residual never drops below πc². Not foreseen: exact band touchings remove the whole-zone 1/n and πc² limits (faster than any power), but they move the face problem into a degenerate partner band. |

## Labels and strong words

**PROVED (same-family, unrefereed):**
- C-alg (finite range), and the H_0 local-Noether statement;
- C-tot;
- Lemma D;
- Lemma R;
- Theorem A, with per-band and common-c corollaries;
- B1;
- B2 and its Herglotz corollary;
- the πc² lower bound for C¹ bands.

**CHECKED:**
- Koszul boxes;
- the Lemma R null space;
- the dipolar loophole kernel;
- the 1.760/n law;
- the window rates;
- the filtered-series residuals;
- the two-band whole-zone convergence (1D, m = 1 only).

**ARGUED:**
- quasi-local Koszul;
- interspecies-only common c;
- Fermi-sea damping.

**SUGGESTED:**
- the loophole's 1/q stress;
- infrared power counting for gapless dressing;
- partner-band interband obstruction;
- extending the two-band construction to d = 2 and 3 with 2^d bands (tensor blocks for the edge cross terms |δ_x||δ_y|).

**OPEN:**
- gapless-mediator dressed bands;
- the optimal two-band rate;
- n\* for two bands.

**READING:** the n\* values.

**COMPARATORS:**
- Bernstein–Walsh;
- Jackson and Bernstein inverse theorems;
- Paley–Wiener;
- the Koszul complex of a regular sequence (standard commutative algebra);
- Fejér–Riesz.

**Scope of strong words.**
- "Exact" is used only for algebraic identities and for the theorem conclusions.
- "Impossible" is bounded to B1's and B2's hypotheses.
- "Every n" in the πc² bound applies only to bands with E² ∈ C¹, i.e. one smooth band.
