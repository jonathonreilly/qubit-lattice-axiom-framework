lead: anthropic/claude-fable-5-2 laptop subagent

Started 2026-11-28 13:31:30Z, pinned at commit 44550e2f4. Author only, checked by no one.

# Gap purity: strategy mining (FINISH row 1682)

## Plan

1. Read the crux card and the Lean files it cites. Nothing else in Phase 1.
2. Part 1: twenty or more hard problems that fell; the transferable move of each.
3. Part 2: at most twelve strategy types; the (PUR-io) analogue of each.
4. Part 3 (Phase 2): compare with the registry and the section 3 files.
5. Part 4: rank five; first buildable component for the top three; reading list.
6. RESULT line.

Labels: PROVED (written in full here), CITED (exact reference), ARGUED (my judgement), GUESSED. A reference marked UNVERIFIED comes from memory and I did not check it. Phase 1 (sections 0 to 2) used only `library/gap-purity-crux-card.md` and the Lean files it cites (`Purity.lean`, `PurIo.lean`, `Stage0.lean`, `Transfer.lean`, statement of `Offset.lean` L701).

## 0. The target as I read it (Phase 1, closed folder)

Notation. n = `Γ.side` = ℓ L^k. u = n/512. T = `Γ.transfer μt β` on the spatial cube n³. T is positive, compact, Hilbert-Schmidt, and its kernel is strictly positive (`Transfer.lean` L679, L684, L693, L719). λ_0 = ‖T‖. P₀ = `neutralProj`. The neutral eigenvalues are λ_0 ≥ λ_1 ≥ ... ≥ 0. D(u) = tr(P₀ T^u)/λ_0^u = Σ_i (λ_i/λ_0)^u ≥ 1. This D − 1 is the quantity of `NeutralTailLE` (`Stage0.lean` L86).

**F1 (PROVED).** 1/D(u)² ≤ purity ≤ 1/D(u). Proof: Σ λ_i^{2u} ≥ λ_0^{2u} gives the left side. Σ λ_i^{2u} ≤ λ_0^u Σ λ_i^u gives the right side. So D(u) ≤ 25/√457 = 1.1694 implies the test 457/625, and the test implies D(u) ≤ 625/457 = 1.3676. (The vacuum is neutral: `F.vacuum` in `Purity.lean` L82. ARGUED from Jentzsch's theorem and the positive kernel.)

**F2 (PROVED).** With K = P₀ T^u on the neutral sector, 1 − purity = 2 tr(Λ²K)/(tr K)². Proof: tr Λ²K = Σ_{i<j} κ_i κ_j = ((tr K)² − tr K²)/2. So the test says: the antisymmetric two-replica trace is at most 0.1344 of the product trace.

**F3 (PROVED for the full trace; the neutral case is the same on the quotient by the centre shifts).** Let ψ_0 > 0 be the top eigenvector and π = ψ_0² dHaar. The operator P f = (λ_0 ψ_0)^{-1} T(ψ_0 f) is a self-adjoint Markov operator on L²(π). Its kernel density is p_t(U,U')/π(U') = Σ_i (λ_i/λ_0)^t φ_i(U) φ_i(U') with φ_i = ψ_i/ψ_0. Hence ∫π(dU) χ²(P^t(U,·) ‖ π) = Σ_{i≥1} (λ_i/λ_0)^{2t}. With t = u/2: D(u) − 1 is the mean chi-square distance from equilibrium, at lattice time u/2, of the time-slice chain started at a π-typical point.

**F4 (ARGUED; the same estimate as the card's "m ℓ of about 12,000").** For one particle of mass m in the box, D − 1 ≈ (ℓ³)(mT/2π)^{3/2} e^{−m/T} at T = 512/ℓ. This is 0.1 at mℓ/512 ≈ 23. In thermal words: the test asks p(T)/T⁴ ≤ about 10⁻⁹ at one temperature T = 512/ℓ, in a box of side 512/T. The Stefan-Boltzmann value for three gluon colours is π²/15 ≈ 0.66. For free photons it is π²/45 at every T. This is the U(1) failure in one line.

**Structural remark (ARGUED).** The physical mass in lattice units is of order exp(−c β). So no estimate that is algebraic in g at the cutoff scale can prove the test. Every candidate must act at the physical scale, on the Wilson law or on a law that the account carries to it exactly. I use this remark as the first death test below.

## 1. Part 1. How hard problems fell (closed folder)

Each entry: what made it hard; the decisive move as a pattern; the new object; one idea or a chain; the reference. Fields outside mathematical physics come first (A1 to A23). Then four from mathematical physics (B1 to B4).

**A1. Fermat's Last Theorem (number theory).** Hard: the equation has no structure of its own. Move: carry the counterexample to another category (Frey curve, Galois representation) where a rigidity statement (modularity) can be false only in a controlled way. Then prove an isomorphism R = T by a numerical criterion at minimal level and extend it with auxiliary primes. Pattern: *transfer, then prove equality of a "possible" object and an "actual" object by counting at one level and patching over an auxiliary family*. New object: Taylor-Wiles systems. Chain of many tools. CITED: A. Wiles, "Modular elliptic curves and Fermat's Last Theorem", Ann. of Math. 141 (1995) 443-551; R. Taylor, A. Wiles, Ann. of Math. 141 (1995) 553-572.

**A2. Poincaré conjecture (geometry).** Hard: Ricci flow develops singularities and nothing stopped collapse. Move: *find a quantity that is monotone along the flow and whose monotonicity forbids the bad scenario at every scale* (entropy W, reduced volume; no local collapsing). New object: the W-functional. One decisive idea inside a long chain (surgery). CITED: G. Perelman, "The entropy formula for the Ricci flow and its geometric applications", arXiv:math/0211159.

**A3. Riemann hypothesis over finite fields (arithmetic geometry).** Hard: no positivity was available. Move: *prove a weak bound that holds for every tensor power, then take roots* (Rankin's trick), fed by monodromy of a family (Lefschetz pencil). New object: weights and big monodromy. Short chain. CITED: P. Deligne, "La conjecture de Weil. I", Publ. Math. IHÉS 43 (1974) 273-307.

**A4. Bounded gaps between primes (analytic number theory).** Hard: the needed distribution estimate (Elliott-Halberstam) was out of reach. Move: *weaken the hypothesis to a structured subfamily that can be proved* (smooth moduli), and later *optimise the test weight* so that the classical input suffices. New object: Zhang's smooth-modulus estimate; Maynard's multidimensional sieve weight. Chain (Zhang); one idea (Maynard). CITED: Y. Zhang, Ann. of Math. 179 (2014) 1121-1174; J. Maynard, "Small gaps between primes", Ann. of Math. 181 (2015) 383-413.

**A5. Progressions in the primes (additive combinatorics).** Hard: the primes have density zero. Move: *transference*: embed the sparse set in a pseudorandom majorant, and show that a known dense theorem transfers. New object: the dense model theorem. Chain of three tools. CITED: B. Green, T. Tao, Ann. of Math. 167 (2008) 481-547.

**A6. Kadison-Singer (operator algebras).** Hard: random choices fail with positive probability at the needed scale. Move: *replace the random object by its expected characteristic polynomial; real-rootedness of an interlacing family gives one realisation at least as good as the average*. New object: interlacing families, mixed characteristic polynomial, barrier function. Chain of three new tools. CITED: A. Marcus, D. Spielman, N. Srivastava, "Interlacing families II", Ann. of Math. 182 (2015) 327-350.

**A7. Sensitivity conjecture (theoretical computer science).** Hard: thirty years of combinatorial attacks. Move: *choose signs on the edges (a Z_2 gauge field) so that the signed operator satisfies an exact algebraic identity A² = n; then interlacing does the rest*. New object: the signed hypercube matrix. One idea. CITED: H. Huang, Ann. of Math. 190 (2019) 949-955.

**A8. Sphere packing in dimension 8 (geometry, number theory).** Hard: the linear-programming bound needed one function that nobody could build. Move: *a dual certificate: one explicit auxiliary function with sign conditions on it and on its transform proves optimality*. New object: the magic function from quasimodular forms. One idea on top of a known duality. CITED: M. Viazovska, Ann. of Math. 185 (2017) 991-1015; H. Cohn, N. Elkies, Ann. of Math. 157 (2003) 689-714.

**A9. Kepler conjecture; four colours (discrete geometry, combinatorics).** Hard: an infinite configuration space. Move: *reduce to a finite list by a local inequality (discharging, local density), then check the list by machine, then check the checker*. New object: the local scoring function; the formal proof. Chain. CITED: T. Hales, Ann. of Math. 162 (2005) 1065-1185; T. Hales et al., Forum Math. Pi 5 (2017) e2.

**A10. Bieberbach conjecture (complex analysis).** Hard: coefficient problems are non-linear. Move: *embed in a flow (Loewner), find a Lyapunov functional with free weights, and reduce the sign of its derivative to a classical positivity of special functions* (Askey-Gasper). New object: the weight system. One idea plus one imported inequality. CITED: L. de Branges, Acta Math. 154 (1985) 137-152.

**A11. PCP by gap amplification; SL = L (theoretical computer science).** Hard: a gap of size 1/n had to become a constant without a blow-up in size. Move: *iterate a step that multiplies the gap by a fixed factor while it is below a constant (powering), and repair the side cost of each step (alphabet or degree reduction)*. New object: the powered constraint graph; the zig-zag product. Chain of two alternating tools. CITED: I. Dinur, J. ACM 54 (2007) Art. 12; O. Reingold, J. ACM 55 (2008) Art. 17.

**A12. Expansion in SL_2(F_p) (group theory, number theory).** Hard: no automorphic input for general generators. Move: *spectral gap from multiplicity times trace*: every non-trivial eigenvalue has high multiplicity because the group has no small representations (quasirandomness), and a return-probability bound (from product growth) bounds the trace. New object: the Bourgain-Gamburd machine. Chain of three tools. CITED: J. Bourgain, A. Gamburd, Ann. of Math. 167 (2008) 625-642; H. Helfgott, Ann. of Math. 167 (2008) 601-623; P. Sarnak, X. Xue, Duke Math. J. 64 (1991) 207-227.

**A13. Property (T) for Aut(F_n) (operator algebras, group theory).** Hard: no geometric model. Move: *a spectral gap is equivalent to an operator inequality Δ² − λΔ ≥ 0 with a finite sum-of-squares witness; find the witness by semidefinite programming with rigorous rounding at one small n; then symmetrise it to all larger n by a structural decomposition*. New object: Ozawa's criterion; the Sq/Adj/Op decomposition. Chain: algebra, numerics, induction. CITED: N. Ozawa, J. Inst. Math. Jussieu 15 (2016) 85-90; M. Kaluba, P. Nowak, N. Ozawa, Math. Ann. 375 (2019) 1169-1191; M. Kaluba, D. Kielak, P. Nowak, Ann. of Math. 193 (2021) 539-562.

**A14. Mihail-Vazirani conjecture; mixing at the uniqueness threshold (TCS, probability).** Hard: canonical-path and coupling methods did not reach the conjectured range. Move: *local to global*: a spectral bound on all local conditional walks (links) forces the global gap; the local bound comes from an algebraic property (log-concave polynomials) or from bounded total influence under every pinning (spectral independence). New object: high-dimensional expanders, trickle-down, spectral independence. Chain. CITED: N. Anari, K. Liu, S. Oveis Gharan, C. Vinzant, "Log-concave polynomials II", Ann. of Math. 199 (2024) 259-299 (pages UNVERIFIED); I. Oppenheim, Discrete Comput. Geom. 59 (2018) 293-330; N. Anari, K. Liu, S. Oveis Gharan, "Spectral independence in high-dimensional expanders and applications to the hardcore model", FOCS 2020.

**A15. Sharpness of the phase transition for random-cluster models (probability).** Hard: earlier proofs used independence or special structure. Move: *import an inequality from another field (OSSS, decision trees) to get a differential inequality in the parameter, θ_n' ≥ c (n/Σ_{k<n} θ_k) θ_n; integrate it to a dichotomy*. New object: the randomised exploration algorithm as a proof device. One idea plus one import. CITED: H. Duminil-Copin, A. Raoufi, V. Tassion, Ann. of Math. 189 (2019) 75-99.

**A16. Conformal invariance of percolation; the connective constant (probability, combinatorics).** Hard: no handle on the scaling limit. Move: *find an observable that obeys exact local linear relations (discrete holomorphicity) on the lattice; sum the relations over a domain; boundary terms give the answer*. New object: the parafermionic observable. One idea. CITED: S. Smirnov, C. R. Acad. Sci. Paris 333 (2001) 239-244; H. Duminil-Copin, S. Smirnov, Ann. of Math. 175 (2012) 1653-1665.

**A17. Energy-critical dispersive equations (analysis, PDE).** Hard: no small parameter at the critical scaling. Move: *compactness plus rigidity*: if the theorem fails, a minimal counterexample exists and is compact modulo symmetries; a rigidity identity (virial) excludes it. New object: the critical element (profile decomposition). Two tools. CITED: C. Kenig, F. Merle, Invent. Math. 166 (2006) 645-675.

**A18. Aldous' spectral gap conjecture; Kac's master equation (probability).** Hard: the gap of a large non-commutative walk had to equal the gap of a small one. Move: *induction that removes one site by an exact reduction (network reduction, conditional expectation), plus one new operator inequality that makes the reduction monotone* (octopus inequality; the K-operator of Carlen-Carvalho-Loss). New object: that inequality. Short chain. CITED: P. Caputo, T. Liggett, T. Richthammer, J. Amer. Math. Soc. 23 (2010) 831-851; E. Carlen, M. Carvalho, M. Loss, Acta Math. 191 (2003) 1-54.

**A19. Hyperboundedness implies a spectral gap (functional analysis).** Hard: the Høegh-Krohn-Simon conjecture stood for forty years. Move: *replace the spectral statement by an L^p to L^q mapping property and use a geometric (Cheeger-type) argument on level sets*. New object: higher-order Cheeger inequalities for Markov operators. Short chain. CITED: L. Miclo, "On hyperboundedness and spectrum of Markov operators", Invent. Math. 200 (2015) 311-343.

**A20. Marton's conjecture (additive combinatorics).** Hard: combinatorial doubling loses constants at every step. Move: *replace the combinatorial quantity by an entropic one that has an exact calculus (submodularity), then run a descent: if the object is not yet structured, build a new one with strictly smaller entropic doubling*. New object: the entropic Ruzsa distance and the "fibring" identity. One idea with a careful descent. CITED: W. T. Gowers, B. Green, F. Manners, T. Tao, "On a conjecture of Marton", arXiv:2311.05762.

**A21. Universality of local eigenvalue statistics (probability).** Hard: no formula outside the Gaussian case. Move: *three steps: a rigidity estimate at the local scale; a flow that relaxes the local statistic fast; a comparison that removes the small perturbation the flow introduced*. New object: local relaxation flow; four-moment comparison. Chain. CITED: L. Erdős, B. Schlein, H.-T. Yau, Invent. Math. 185 (2011) 75-119; T. Tao, V. Vu, Acta Math. 206 (2011) 127-204.

**A22. Fundamental gap conjecture (analysis, geometry).** Hard: the gap of a Schrödinger operator on a convex domain with convex potential had no sharp lower bound. Move: *a two-point maximum principle gives a modulus of log-concavity of the ground state that is better than plain log-concavity; the gap follows by comparison with a one-dimensional model*. New object: the modulus of concavity. One idea. CITED: B. Andrews, J. Clutterbuck, J. Amer. Math. Soc. 24 (2011) 899-916.

**A23. Near-optimal spectral gaps by strong convergence (spectral geometry, random matrices).** Hard: the edge of the spectrum of a random cover or a random matrix polynomial is not a trace statistic. Move: *the expected trace of a test function is a rational function of 1/N; soft information at N = ∞ extends to finite N by polynomial (Markov) inequalities; a gap follows with no hard analysis*. New object: the "polynomial method" for strong convergence. Two tools. CITED: W. Hide, M. Magee, Ann. of Math. 198 (2023) 791-824 (pages UNVERIFIED); C.-F. Chen, J. Garza-Vargas, J. Tropp, R. van Handel, "A new approach to strong convergence", arXiv:2405.16026.

**B1. The AKLT gap, one and two dimensions (mathematical physics).** Hard: no perturbative parameter. Move: *a finite-size criterion: if the gap of a finite piece exceeds an explicit threshold, the gap is uniform in the volume; in two dimensions the finite piece is checked by a rigorous computation*. New object: Knabe's inequality. Two tools. CITED: I. Affleck, T. Kennedy, E. Lieb, H. Tasaki, Comm. Math. Phys. 115 (1988) 477-528; S. Knabe, J. Stat. Phys. 52 (1988) 627-638; M. Lemm, A. Sandvik, L. Wang, Phys. Rev. Lett. 124 (2020) 177204; N. Pomata, T.-C. Wei, Phys. Rev. Lett. 124 (2020) 177203.

**B2. Confinement and mass in three-dimensional compact U(1) (mathematical physics).** Hard: weak coupling, no cluster expansion in the gauge variables. Move: *an exact duality carries the model to a gas in which the mass is a screening effect with a small activity; a renormalisation group for the gas proves screening*. New object: the monopole gas with a multi-scale Debye screening proof. Chain. It reads the dimension and the compactness of the group. CITED: M. Göpfert, G. Mack, Comm. Math. Phys. 82 (1982) 545-606.

**B3. Marginal triviality of φ⁴ in four dimensions (mathematical physics).** Hard: the critical dimension; a logarithm had to be won. Move: *an exact geometric representation (random currents) turns the non-Gaussian quantity into an intersection probability, and a multi-scale argument wins the logarithm*. New object: the multi-scale intersection estimate. Chain. CITED: M. Aizenman, H. Duminil-Copin, Ann. of Math. 194 (2021) 163-235.

**B4. Log-Sobolev inequalities by renormalisation (mathematical physics, probability).** Hard: the Bakry-Émery criterion fails for non-convex actions. Move: *apply the convexity criterion scale by scale along an exact renormalisation flow (Polchinski); only semi-convexity of the renormalised potential at each scale is needed, and the constants multiply*. New object: the multi-scale Bakry-Émery criterion. One idea on top of a known flow. CITED: R. Bauerschmidt, T. Bodineau, J. Funct. Anal. 276 (2019) 2582-2588; R. Bauerschmidt, T. Bodineau, Comm. Pure Appl. Math. 74 (2021) 2064-2113.

Observation (ARGUED). Of the 27 entries, 8 are one idea (A7, A8, A10, A16, A20, A22, and in part A2, A4-Maynard). The other 19 are chains of two to four tools from different fields, and in most chains one link is a new exact identity or a new object, not a harder estimate. Gaps in particular (A11, A12, A13, A14, A18, A19, A23, B1) fell to one of four mechanisms: amplification, multiplicity times trace, a finite certificate with a stabilisation argument, or local to global. No gap in this list fell to a direct estimate of the spectrum.

## 2. Part 2. Twelve strategy types and their (PUR-io) analogues (closed folder)

### 2.0 Two tool packs that several types use

**Pack E: the excess free energy on tori.** Let N = (N_1,...,N_4), all N_j ≥ 3, and Z(N) the periodic Wilson partition function at β with Haar probability and weight exp(−β Σ(1 − halfTrace)). Hypothesis (H): for each direction j and each choice of the other three sides there are reals μ_0 ≥ μ_1 ≥ ... ≥ 0 with Z(N) = Σ_i μ_i^{N_j} for all N_j ≥ 3. (This is the trace formula of the rectangular transfer in direction j: `Transfer.lean` L679 and L758-L761, with the lattice symmetry that permutes the axes. I did not check that the Lean files state the trace formula for every direction; ARGUED.) Write 2_jN for N with N_j doubled, |N| for the number of sites, f(N) = log Z(N)/|N|.

- **E1 (PROVED).** Z(2_jN) ≤ Z(N)². Proof: Σ μ_i^{2m} ≤ (Σ μ_i^m)². So R_j(N) := Z(2_jN)/Z(N)² lies in (0,1]. R_4 at N = (n,n,n,u) is the untwisted purity.
- **E2 (PROVED).** N_j ↦ log Z(N) is convex. Proof: Cauchy-Schwarz on Σ μ_i^{m−h} μ_i^{m+h}.
- **E3 (PROVED).** f(2_jN) ≤ f(N) by E1. Since 0 ≥ f ≥ −12β, f_∞ := inf of f over all tori obtained from N by doublings is finite, and it is the same for every torus in that family (two tori of the family have a common doubling, and f decreases). Define the excess e(N) := log Z(N) − |N| f_∞ ≥ 0. Then e(2_jN) ≤ 2 e(N), and −log R_j(N) = 2 e(N) − e(2_jN) for each of the four directions.
- **E4 (PROVED).** purity ≥ exp(−2 e(n,n,n,u)) for the neutral purity of `Purity.lean`. Proof: purity ≥ D^{−2} by F1. D ≤ D_full := Z(N)/λ_0^u because P₀ is a projection that commutes with T ≥ 0. u log λ_0 = lim_r 2^{−r} log Z(n,n,n,2^r u) ≥ |N| f_∞. So log D_full ≤ e(N). Consequence: **e(N_k; β_k) ≤ ½ log(625/457) = 0.1565 implies the test at cutoff k.** With E3 applied 27 times: e(u,u,u,u) ≤ 0.1565/2^27 = 1.17 × 10⁻⁹ on the hypercube of side u = n/512 also implies it.
- **E5 (PROVED).** Channel identity. Let Λ(a,b,w) = log of the top eigenvalue of the transfer on the slice a × b × w. Then log D_full(n³; u) = n Λ(n,n,u) − u Λ(n,n,n) + log D′, where D′ = Z(N)/exp(n Λ(n,n,u)) ≥ 1 is the same ratio in the channel where a spatial axis is time. Proof: both sides equal log Z(N) − u Λ(n,n,n).
- **E6 (PROVED).** Fix (a,b). The function w ↦ Λ(a,b,w) is convex (limit of t^{−1} log Z(t,a,b,w), each convex by E2). Its increments increase to a finite limit ρ (finite because −12β a b w ≤ Λ ≤ 0). So κ(w) := Λ(a,b,w) − ρ w is convex and non-increasing. E1 gives κ(2w) ≤ 2κ(w), and κ(w)/w → 0; together these exclude κ → −∞, so κ ≥ lim κ ≥ 0. With (a,b) = (n,n) the term ρ cancels in E5: **log D_full(n³;u) = n κ(u) − u κ(n) + log D′ ≤ n κ(u) + log D′.** In words: the thermal trace of the cube equals the Casimir excess of the slab n × n × u, times n, up to the slab's own tail. The monotone, convex κ is the lattice form of "the Casimir force between periodic images is attractive" (CITED for the continuum statement: O. Kenneth, I. Klich, Phys. Rev. Lett. 97 (2006) 160401; C. Bachas, J. Phys. A 40 (2007) 9089).
- **E7 (PROVED up to almost-everywhere differentiation of a convex function).** e(N; β) = ∫_0^β (A_∞(b) − A_N(b)) db, where A_N(b) = ⟨Σ_p (1 − halfTrace U_p)⟩ on the torus N at coupling b, and A_∞(b) = −|N| f_∞′(b). Proof: d log Z/db = −A_N; f_∞ is a limit of convex functions of b; Z = 1 at b = 0. So the excess is the integrated action deficit of the torus against the infinite lattice. This is the "integral method" of lattice thermodynamics (CITED, UNVERIFIED pages: J. Engels, J. Fingberg, F. Karsch, D. Miller, M. Weber, Phys. Lett. B 252 (1990) 625).
- **E8 (PROVED from E7).** Dilation on the trajectory. N_{k+1} = L N_k as lattices. So "physical side Lℓ at cutoff k" and "physical side ℓ at cutoff k+1" are the same lattice at two couplings: e(N_{k+1}; β_k) − e(N_{k+1}; β_{k+1}) = −∫_{β_k}^{β_{k+1}} ∂_b e(N_{k+1}; b) db. The width of the window is positive on average only because the trajectory is asymptotically free: β_k/(k log L) → 11/(3π²) (`PurIo.lean` L172, L348).

**Pack K: block conditional expectations.** Let ν be a Gibbs state of the Wilson action (a torus state, or an infinite-volume limit `ν j`). For a finite set B of links let E_B be the conditional expectation given the links outside B. E_B is an orthogonal projection on L²(ν), it maps gauge-invariant functions to gauge-invariant functions, and E_B E_{B′} = E_{B′} E_B when no plaquette meets both B and B′ (Markov property of a plaquette action; PROVED in one line: given the rest, the two blocks are independent).

**Lemma K (PROVED here modulo one CITED lemma).** Let (E_x)_{x∈X} be finitely many orthogonal projections on a Hilbert space H, Π the projection on their common fixed space. Suppose each E_x commutes with all but at most g of the others, X has a colouring with χ colours such that projections of one colour commute, and Σ_x (1 − E_x) ≥ γ (1 − Π) with γ > 0. Let A be the product over the colours of the products of the E_x of that colour. Let F, G ∈ H and m ≥ 0 be such that ⟨F, (A*A)^k G⟩ = ⟨F, G⟩ for all 0 ≤ k ≤ m. Then

  |⟨F, (1 − Π) G⟩| ≤ 2 ‖F‖ ‖G‖ exp(−2m √(γ/(γ + g²))).

Proof. The detectability lemma gives ‖A(1 − Π)‖² ≤ δ² := g²/(g² + γ) (CITED: A. Anshu, I. Arad, T. Vidick, Phys. Rev. B 93 (2016) 205142, Lemma 2; lemma number UNVERIFIED). AΠ = Π = ΠA, so A*A commutes with Π and has spectrum in [0, δ²] on the range of 1 − Π. Let q(x) = T_m(2x/δ² − 1)/T_m(2/δ² − 1) with T_m the Chebyshev polynomial. Then q(1) = 1 and |q| ≤ 1/T_m(1 + 2γ/g²) on [0, δ²]. The hypothesis on F, G and q(1) = 1 give ⟨F, q(A*A) G⟩ = ⟨F, G⟩. Also q(A*A) = Π + q(A*A)(1 − Π). Subtract: ⟨F, (1 − Π)G⟩ = ⟨F, q(A*A)(1 − Π)G⟩. Finally T_m(cosh θ) = cosh mθ ≥ e^{mθ}/2 with θ = 2 arcsinh √(γ/g²) ≥ 2 √(γ/(γ + g²)). ∎

The locality hypothesis holds for conditional expectations (PROVED): if G depends only on links in a set S, then E_x G = G unless the block of x meets S, and then E_x G depends on S and the block with its boundary. If F does not depend on the links of the block of x, then E_x F = F, and E_x is self-adjoint. So every E_x in the word (A*A)^k acts either as the identity on the right factor or can be moved to F, as long as the grown support of G has not reached the support of F. The method is that of D. Gosset and Y. Huang for quantum spin systems (CITED: Phys. Rev. Lett. 116 (2016) 097202); the classical form above is my transcription.

### 2.1 The types

**S1. A monotone quantity along a flow (A2, A10, A15).**
Object: the excess e(N; β) of Pack E. Flow: dilation of the box at a fixed cutoff, read through E8 as a change of β on a fixed lattice.
Statement to prove: (ACT) for the lattice N_{k+1} and every b in [β_k, β_{k+1}]: ∂_b e(N_{k+1}; b) ≥ G(e), with G > 0 while e > 0.1565. Then e falls under each dilation by L until the test E4 holds.
First estimate (written out): E8 and E7 give e_k(Lℓ) = e_{k+1}(ℓ) − ∫_{β_k}^{β_{k+1}} (A_∞(b) − A_{N_{k+1}}(b)) db. In spectral form (ARGUED, Hellmann-Feynman on the eigenvalues E_i = −log λ_i of the cube): ∂_b log D_full = −u Σ_i p_i ∂_b(E_i − E_0), with p_i the thermal weights. So the sign statement is "the thermal mean of the lattice excitation energies does not increase with β". In two dimensions this holds exactly: Z = Σ_j (I_{2j+1}(β)/I_1(β))^{area}, and each Bessel ratio increases with β (ARGUED; the monotonicity of I_{ν+1}/I_ν is classical, reference UNVERIFIED).
Where it reads the group and the dimension: the window [β_k, β_{k+1}] has positive width because of the one-loop coefficient 11/(3π²), a four-dimensional logarithm of a non-abelian group. For weak compact U(1) there is no running: the window is empty and the statement is void.
Where it dies: at the size, not the sign. No inequality bounds the action deficit below by a function of the excess outside perturbation theory. The sign alone is a Ginibre-type correlation inequality, which is not known for SU(2).
Chain: reflection positivity (Pack E) → integral method (E7) → a correlation inequality or a decision-tree inequality in the style of A15 for the size.

**S2. A finite certificate with a stabilisation argument (A8, A9, A13, B1).**
Object: the family of block conditional expectations E_x of Pack K, with blocks of fixed physical side b, on gauge-invariant L²(ν_j).
Statement to prove: (BL) there are b and c > 0 such that for infinitely many j and every gauge-invariant local f: Σ_x ‖f − E_x f‖² ≥ c ‖f − ν_j(f)‖². By Lemma K this gives exponential clustering of gauge-invariant local observables at a physical rate, the form that `ExpClusters` (`Stage0.lean` L228) consumes. It does not go through the cube.
First estimate: Lemma K with blocks of side 2b centred on the grid bZ⁴: g = 5⁴ − 1 = 624, χ = 81, support growth at most 2b + 2 per colour layer, so m = ⌊d/(162(2b + 2))⌋ for supports at sup-distance d. The rate per lattice unit is √(c/(c + 624²))/(162(b + 1)). With b a = b_phys fixed this is a physical rate. For single links (g = 18, χ = 8) the same lemma needs a gap ≥ (144 m a)², and I expect that to fail on tori because the topological charge freezes under local updates (GUESSED). Blocks of physical size do not have this problem.
A finite-size criterion in the style of B1 exists for sums of projections (Knabe; CITED UNVERIFIED for higher dimensions: M. Lemm, E. Mozgunov, J. Math. Phys. 60 (2019) 051901; A. Anshu, Phys. Rev. B 101 (2020) 165104). It needs the gap of a finite block for every boundary condition.
Where it reads the group and the dimension: nowhere in Lemma K. (BL) is false for weak 4D U(1): the infinite-volume block dynamics of a massless Gaussian field has no gap. A proof of (BL) must read SU(2) in the conditional laws.
Where it dies: (BL) is at the level of the mass gap itself. The finite-size criterion dies on worst-case boundary conditions. (BL) is an L²(ν) statement, so it needs typical boundary conditions only; this is its one advantage.
Chain: detectability lemma (quantum Hamiltonian complexity) → Lemma K → a supplier of approximate tensorisation of variance (S5, S9, S11).

**S3. Amplification by iteration; tensor powers (A3, A11).**
Object: the Rényi family p_k = tr ρ^k = Z̃(ku)/Z̃(u)^k and the doubling maps N ↦ 2_jN.
Result (PROVED): p_2 ≥ p_k for all k ≥ 2, because p_k = E[X^{k−1}] for a random variable X in [0,1] with E[X] = p_2. So higher replica numbers give lower bounds on the purity only through quantities that are harder than the purity. The tensor-power trick gives nothing.
Result (PROVED, E3): the only free amplification is e(2_jN) ≤ 2e(N). It is extensive, not contractive.
A Dinur-style scheme needs: (i) a contraction e(2N) ≤ C e(N)² below a threshold (this is what a seed consumer does); (ii) a definite decrease per step above the threshold. (ii) is S1. So S3 is not a separate candidate. For U(1), (ii) fails as in S1.

**S4. Change of category (A1, A5, B2).**
Four exact dictionaries are available: the time-slice Markov chain (F3), the two-replica swap (F2), the Casimir energy of a slab (E5, E6), the thermal pressure (F4). Each makes a different toolbox legal.
Candidate (renormalised disagreement percolation). Object: single-block conditional laws of a carried law at the physical scale. Statement: if the total-variation oscillation q of the conditional law of one block, over the configurations of the neighbouring blocks, is below the site-percolation threshold of the block graph, the Gibbs state is unique and clusters exponentially (CITED: J. van den Berg, C. Maes, Ann. Probab. 22 (1994) 749-763). First estimate: for the Wilson law itself q → 1 as β → ∞, because two different staples give link laws concentrated at two different points (PROVED in that sense; this is the structural remark of section 0). So the statement can only be used after a carry.
U(1): q does not fall under coarse-graining; the criterion never holds.
Where it dies: at the definition of block variables for a gauge field whose conditional laws are known at coupling of order one.

**S5. Local to global (A14, A18).**
Object: two overlapping half-boxes A, B of the spatial cube (or of the four-dimensional block), with E_A, E_B.
Statement: Var(f) ≤ (1 − ε)^{-1} ν(Var_A f + Var_B f) with ε = ‖E_A E_B − Π‖ on mean-zero functions. First estimate (PROVED, standard): E_A E_B − Π has norm ε, so 1 − (E_A + E_B)/2 ≥ (1 − ε)/2 on mean-zero functions. Iterating over scales gives gap(2^r ℓ) ≥ Π_s (1 − ε_s) · gap(ℓ) up to the usual averaging loss (CITED UNVERIFIED: F. Martinelli, "Lectures on Glauber dynamics for discrete spin models", Lecture Notes in Math. 1717 (1999)).
U(1): ε_s does not tend to zero (scale invariance), so the product is zero. Void as a gap proof.
Where it reads the group: only in the size of ε at one physical scale. Where it dies: the first ε.
Use: S5 is the stabilisation half of S2. It turns (BL) at one block size into (BL) at all larger sizes.

**S6. Multiplicity times trace (A12).**
Void (ARGUED). The symmetries of the neutral gauge-invariant sector are the translations (abelian), the cubic point group (irreducible dimensions at most 3) and the centre shifts. The local gauge group has large representations, but the transfer kernel contains the gauge average (`Transfer.lean` L547), so states that are not invariant have eigenvalue zero. No eigenvalue below λ_0 is forced to have high multiplicity.

**S7. Sign choices and interlacing (A6, A7).**
The twist sums are already the lane's objects (`twistedPartition`, `kappaWeight`, `Stage0.lean` L97-L116). A signing with an exact identity in the style of A7 would need an operator whose square is the transfer; reflection positivity gives T = Q*Q, and QQ* has the same non-zero spectrum, so nothing is gained (PROVED: isospectral). Void as a new route. On file by the Lean files themselves.

**S8. Exact identities plus positivity (A8, A16).**
Object: the function N ↦ Z(N) on all tori, as the unknown of a linear programme. Constraints: symmetry under permutation of the axes; a Stieltjes moment sequence in each variable (hypothesis H); the consequences E1 to E6; data in the range of the account.
Statement wanted: an upper bound on e(N) at a large torus from data at small tori.
First estimate: E5 and E6. Assessment (ARGUED): the linear constraints alone cannot give it, because the free massless family satisfies all of them with a scale-invariant excess. The missing input must be non-linear in the measure: the loop (Schwinger-Dyson) equations, which read SU(2) through the Casimir term and the dimension through the 2(d − 1) staples of a link. Rigorous two-sided bounds from loop equations plus positivity exist for small loops (CITED UNVERIFIED: V. Kazakov, Z. Zheng, "Bootstrap for lattice Yang-Mills theory", Phys. Rev. D 107 (2023) L051501; P. Anderson, M. Kruczenski, Nucl. Phys. B 921 (2017) 702).
U(1): the loop equations differ; the abelian ones admit the massless solution.
Where it dies: the needed precision is 10⁻⁹ on a torus of 512 correlation lengths; the truncations in use reach a few lattice spacings.

**S9. From spectrum to L^p and entropy (A19, A20, B4).**
Object: the Markov operator P of F3 on L²(π).
**Lemma HC (PROVED).** If P^s is a contraction from L²(π) to L⁴(π), then ‖P^s f‖_2 ≤ 3^{−1/2} ‖f‖_2 for every f with π(f) = 0; that is, (λ_1/λ_0)^s ≤ 3^{−1/2}. Proof: for bounded real f with π(f) = 0, expand ‖1 + ε P^s f‖_4⁴ = 1 + 6ε²‖P^s f‖_2² + O(ε³) and ‖1 + εf‖_2⁴ = 1 + 2ε²‖f‖_2² + O(ε⁴); the hypothesis and ε → 0 give 6‖P^s f‖_2² ≤ 2‖f‖_2². ∎
Also (PROVED): D_full(2s) ≤ ‖P^s‖²_{L²(π)→L^∞(π)}, and D(u) − 1 ≤ (λ_1/λ_0)^{u−2s} (D(2s) − 1) for 2s ≤ u.
Statement to prove: (HB) P^s is an L² → L⁴ contraction at s = n/c for one fixed c > 12, at infinitely many cutoffs. By Lemma HC this gives the finite-volume gap bound (λ_1/λ_0)^{n/c} ≤ 3^{−1/2}.
U(1): for a free field the transfer is a second quantisation Γ(e^{−sω}), and Γ(r) is an L² → L⁴ contraction exactly when r ≤ 3^{−1/2} (CITED: E. Nelson, J. Funct. Anal. 12 (1973) 211-227). The lowest photon in the box has ω = 2π/n, so (HB) holds only for s ≥ n log 3/(4π) = 0.0874 n. For c > 11.5 it is false. So (HB) with c > 12 is false for weak U(1), has a sign and a size, and does not imply the seed (it gives no count of states).
Where it reads the group: in the proof only. Where it dies: (HB) is stronger than the gap bound it implies, and no supplier of a log-Sobolev inequality for π is known at the physical scale. Hypercontractivity tensorises and passes through mixtures; this is the property that S11 would use.

**S10. Compactness and rigidity (A17).**
Object: a sequence of failing cutoffs.
First estimate (PROVED from E4): if (PUR-io) fails for a side ℓ, then e(N_k(ℓ); β_k) > 0.1565 for all large k. If it fails for every ℓ, the excess at aspect 512 is bounded below at every physical scale.
Statement wanted: no limit of the calibrated trajectory has a thermal excess bounded below at all scales.
U(1): the hypothesis holds and nothing contradicts it. So the rigidity step must use asymptotic freedom, and the only cutoff-uniform non-abelian datum in the cited Lean files is the slope 11/(3π²).
Where it dies: there is no rigidity theorem. The release gives a continuum limit of fixed observables, not of thermal traces. I rank this last.

**S11. Geometry of the configuration space (A22, B4).**
Object: SU(2)^links with the product of bi-invariant metrics, and the heat flow on it.
First estimate: with the metric −2 tr(XY), SU(2) is a 3-sphere of radius 2 and Ric = ½ (PROVED by that identification). The Bakry-Émery criterion gives a Poincaré inequality for the Langevin dynamics when ½ exceeds the largest negative Hessian of the action, which is of order 6β. So it holds only for β below a small constant (CITED UNVERIFIED: H. Shen, R. Zhu, X. Zhu, "A stochastic analysis approach to lattice Yang-Mills at strong coupling", Comm. Math. Phys. 400 (2023) 805-851). For U(1) the curvature is zero and the criterion is void at every coupling: this is a clean non-abelian reading, but at the wrong coupling.
Candidate (stochastic localisation on the group). Decompose ν = ∫ ν_y ρ_t(dy), where y is the configuration after an independent Brownian step of time t on every link, and ν_y ∝ exp(−S(U)) Π_l p_t(U_l^{-1} y_l) is the posterior. The posterior has a mass term of size 1/t on every link. Statement: a Poincaré constant for ν from Poincaré constants of the posteriors and of the smoothed law, in the manner of B4 and of localisation schemes (CITED UNVERIFIED: Y. Chen, R. Eldan, "Localization schemes: a framework for proving mixing bounds for Markov chains", FOCS 2022, arXiv:2203.04163).
Where it dies: by the structural remark, at the cutoff scale the semi-convexity constants are algebraic in β and cannot see the mass. The scheme would have to run on blocks of physical size (the E_x of S2), where the posterior is not explicit.
The Gribov-region route (the fundamental domain is bounded in every direction for a non-abelian group, so a fundamental-gap theorem like A22 would apply) dies on the dimension of the domain: Payne-Weinberger and A22 bounds depend on the diameter, which is infinite in the limit (ARGUED).

**S12. Weaken the input; perturb and compare (A4, A21, A23).**
For (PUR-io) itself there is no slack: one ℓ, infinitely many k, fixed constants. Two remarks for the consumer side only (not candidates for the target):
- The aspect ratio 512 costs a factor of about 500 in the box size. With aspect 4 the same count as F4 gives mℓ ≈ 24 in place of 11,500 (ARGUED).
- A projection on zero spatial momentum (the average of the traces with a spatial shift) removes the factor ℓ³ from the one-particle count.
The polynomial method of A23 needs an integer parameter in which the traces are polynomial. At fixed gauge group SU(2) I found none. Void (ARGUED).

### 2.2 Candidates carried to Phase 2

C1 (S1): excess calculus with the action-deficit inequality (ACT) on the dilation window. C2 (S2 with S5): block-dynamics gap (BL) at physical block size, fed to `ExpClusters` by Lemma K. C3 (S9): vacuum-relative hypercontractivity (HB). C4 (S8): torus linear programme with loop equations. C5 (S11): stochastic localisation on the group with pinned posteriors. C6 (S4): renormalised disagreement percolation. C7 (S10): compactness and rigidity. C8 (S12): consumer-side threshold remarks. Void or folded: S3, S6, S7.

## 3. Part 3 (Phase 2). Comparison with the registry and the section 3 files

Method and limits. I opened `library/open-registry.md` (header, section list, the rows added 2026-11-25 and 2026-11-27) and `gap-direction9-fable.md` section 4. For every candidate I ran keyword searches over `library/` and `parts/` and read the matching passages with a few hundred characters of context. I did not read the brainstorm files in full. A candidate marked "on file" has a quoted match. A candidate marked "no hit" means only that my keywords found nothing; it does not prove absence.

| Candidate | Nearest file and a phrase from it | Verdict |
|---|---|---|
| C1, excess calculus and (ACT) | `gap-afield-a-max.md` L85: "its Casimir free energy D (free energy minus the bulk part)"; L816: "The monotones that Lemma A gives are E(x)/x_i"; `gap-afield-b-max.md` L99: "(MONO-Delta): D(n; beta) non-decreasing in beta is the positivity of the interaction measure on the symmetric torus"; registry row VIR-DOWN: "t a_0 - A_t bounded below by kappa t Ebar_t ... by a method that fails for the free photon"; `gap-mini-solve-au-opus.md` L121: "l -> zeta(l; b,c) is nonincreasing" | ON FILE. Pack E (E1 to E8) restates Lemma A, the Casimir free energy D, (MONO-Delta) and (VIR-down). (ACT) is (VIR-down). Nothing differs in substance. |
| C2, block gap (BL) and Lemma K | `gap-brainstorm-max.md` L202: "Theorem AG: the exact annealed condition (AN) ... implies a block gap kappa/2, a Langevin gap and exponential clustering ... with no independence and no uniformity over exteriors"; `gap-solve-fresh-astra62.md` L21: "the square-root correlation-length estimate of Gosset and Huang for frustration-free systems. The comparison here is on the four-dimensional Euclidean probability space"; `gap-afield-b-max.md` L48: "Theorem S is already a finite-size criterion in the sense of Knabe" | ON FILE. The classical transcription of Gosset-Huang, the typical-exterior form and the block form are there. My explicit constants (g = 624, χ = 81) are the only difference, and they move nothing. |
| C3, hypercontractivity (HB) | `gap-hcphys-max.md` L30: "(HC-phys): there is M_H > 0, free of iota, with (HC-traj) ... at ... a fixed physical time"; `gap-direction-max.md` L353: "Open lemma (E-to-HC), group-blind" | ON FILE as a class and as a named open item. Lemma HC and the Nelson threshold 0.0874 n are a short form of it. |
| C4, torus linear programme with loop equations | `gap-brainstorm-max.md` L69: "768 (no winding-loop positivity bootstrap for SU(2))"; `gap-outside-box-max.md` L142: "First reading: blind (every model of the class satisfies the identities)" | ON FILE, with the same verdict I reached (the linear constraints are blind). |
| C5, stochastic localisation, Polchinski, Bakry-Émery | `gap-afield-a-max.md` L365-366: "Shen, Zhu and Zhu ... on file (row 821: 1/12 in the lane's units); a ceiling" and "log-Sobolev inequalities by the Polchinski equation; links to stochastic localisation ... on file (row 968)" | ON FILE. |
| C6, renormalised disagreement percolation | `gap-afield-a-max.md` L342: "F8: Dobrushin, disagreement percolation, coupling from the past, information percolation" | ON FILE. |
| C7, compactness and rigidity | `gap-compact-rigidity-max.md` L499: "The compactness half of the Kenig-Merle architecture is PROVED by hand"; `gap-afield-a-max.md` L193: "soft rigidity FAILS (Proposition NR); (LIOU) open" | ON FILE, and further than I took it. |
| C8, zero momentum and aspect | `gap-outside-box-max.md` L142: "Sums over shifts project on momentum. Consumer: a possible engine with momentum-resolved thermal sums (a smaller seed box)" | ON FILE. |
| F3, chi-square reading; S3, Rényi family | `gap-afield-a-max.md` L342: "F7: The seed as a chi-square mutual information of two slices; Renyi-2 form of the doubling defect"; registry row WMIX-SLICE: "Every bounded whole-slice two-sample criterion (TV, beta-mixing, Hellinger ...) ... is equivalent to (PUR-io)" | ON FILE. |
| S6, multiplicity times trace | `gap-brainstorm-max.md` L291: "Non-amenability ... (Lubotzky-Phillips-Sarnak; Bourgain-Gamburd)" | ON FILE as an idea in another form; my reading (void, because the gauge average removes the large representations) agrees with no row I saw and contradicts none. |
| S7, twist sums | the Lean file `Stage0.lean` L97-L116 | ON FILE. |
| Diagonal reflection positivity (considered in Phase 2 as a replacement) | `gap-pca-opus.md` L69: "reflection positivity across diagonal hyperplanes is row 963's question" | ON FILE. |
| Wilson weight as a mixture of heat kernels (considered in Phase 2) | `gap-sepinput-max.md` L208: "B8, Hartman-Watson mixture: FOUND for the Villain form ... The SU(2) form (heat kernels on S^3, Levy semigroup) is not there; I found no consumer" | ON FILE as an idea. The SU(2) statement and a consumer are not on file (see 4.3). |

**Verdict of Phase 2 (ARGUED from the searches above).** All eight candidates of section 2.2 are on file as method classes. The natural analogue of nearly every pattern of Part 1 has been written down by an earlier row, usually with the same death point. Six pattern classes of Part 1 gave no hit under my keywords: the sum-of-squares certificate with rounding and symmetrisation (A13: "Kaluba", "Ozawa"), the entropic descent (A20: "Marton", "doubling constant"), transference by a dense model (A5: "dense model", "transference"), an exact local observable (A16: "parafermion", "discrete holomorph"), a signing with an exact identity and interlacing families (A7, A6: "signed adjacency", "interlacing famil"), and the dual certificate by a special function (A8: "magic function", "linear programming bound"). Section 4 treats these.

## 4. Part 4. Ranking, first components, reading list

### 4.1 The honest count

New candidates with a live first link toward an instance of the gate: **none**. I do not rank a restatement as a candidate. What follows is the best I can do with the six unfiled pattern classes and one unfiled statement. For each I wrote the analogue, and then tried to kill it.

### 4.2 Five items, ranked by the chance that a first link gives a gate instance

1. **HW-SU2: the Wilson weight as a random-time heat kernel, used as an operator inequality (pattern B3 and A10: an exact representation plus a classical positivity).** Chance: low. The identity is blind to the group (it holds for U(1) with Bessel order 0), so it cannot be a gate instance by itself. It is ranked first because it is exact for the Wilson law at every β, it has a statement that is not on file, and the lane recorded "no consumer" for it; 4.3 gives two consumers to test.
2. **Certificate with rounding (A13).** Chance: low. A sum-of-squares certificate for a block gap at one order-one coupling on one small torus can be made rigorous from floating-point output by Lemma OU of 4.3. This does not touch the carry in K. It serves the tool lane only. U(1): the certificate does not exist at weak coupling in infinite volume (no gap).
3. **Entropic descent with a fibring identity (A20).** Chance: very low. The exact identity available is the commutation of doublings: S_i(2_jN) + 2S_j(N) = S_j(2_iN) + 2S_i(N), with S_j = −log R_j (PROVED from E3: both sides equal 4e(N) − e(2_i 2_jN)). So the defect δ_ij := S_i(2_jN) − 2S_i(N) is symmetric in (i,j). A descent would need a sign for δ_ij. I found none (ARGUED): in terms of the excess, δ_ij = 2e(2_iN) + 2e(2_jN) − 4e(N) − e(2_i 2_jN). For a free massless field on a thermal torus the leading (extensive) terms cancel exactly, for two long axes and for one short and one long axis, so the sign sits in subleading terms that I did not compute. The identity is on file in the form Φ = 8d_1 + 4d_2 + 2d_3 + d_4 (`gap-afield-a-max.md` L342). Closed unless a new inequality on δ_ij appears.
4. **Transference by a dense model (A5).** Void (PROVED, Lemma NC of 4.3): the class of clustering laws is not convex, so the min-max step has no model class. The convex relaxation (all states that satisfy reflection positivity and the loop equations at one coupling) is the bootstrap class, which is on file and blind.
5. **Signing, interlacing, exact observable, magic function (A7, A6, A16, A8).** Void (ARGUED). Signing: T = Q*Q and QQ* are isospectral; the only sign patterns that are not gauge changes are the twists, which are on file. Interlacing: the natural positive decomposition of the transfer, Σ_J c_J e^{−V/2} P_J e^{−V/2} over spin labels J, is not a sum of independent rank-one terms, and I found no common interlacing. Exact observable: the only exact local relations I know are the loop equations and the 't Hooft commutation, both on file. Magic function: the two channels of a torus give positivity in both, but the crossed-channel vacuum energy (the Casimir term κ) is an unknown of the theory, not an anomaly coefficient as in two dimensions; this is the on-file verdict "blind".

### 4.3 First buildable components for the top three

**Component 1 (for item 1). Lemma HW-SU2.**
Statement. For every β > 0 there is a probability measure η_β on [0, ∞) such that for all j in {0, 1/2, 1, ...}:

  c_j(β) := I_{2j+1}(β)/I_1(β) = ∫ exp(−4j(j+1) s) η_β(ds).

Here I_ν is the modified Bessel function, and c_j(β) is the eigenvalue, relative to the trivial representation, of convolution by exp(β halfTrace) on the spin-j matrix coefficients of SU(2). Source to check: the function λ ↦ I_{√(ν²+λ)}(r)/I_ν(r) is completely monotone for ν ≥ 0 (CITED, UNVERIFIED as to the exact theorem and its range of ν: P. Hartman, G. Watson, Ann. Probab. 2 (1974) 593-607; J. Kent, Proc. London Math. Soc. 35 (1977) 359-384). The case needed is ν = 1 and λ = (2j+1)² − 1 = 4j(j+1), the eigenvalues of the Laplacian of the 3-sphere.
Consequences to prove in the same row (each is one line given the statement):
(a) The kinetic factor of the Wilson transfer on a link is k_β = ∫ exp(s Δ) η_β(ds), with Δ the bi-invariant Laplacian of eigenvalue −4j(j+1) on spin j.
(b) With s̄(β) = ∫ s η_β(ds): c_j(β) ≥ exp(−4j(j+1) s̄(β)) for all j (Jensen). Hence, in operator order on the slice space, T_Wilson(β) ≥ T_HK(s̄(β); β), the transfer with the heat kernel at time s̄ on temporal plaquettes and the Wilson weight on spatial ones. Hence λ_i(T_Wilson) ≥ λ_i(T_HK) for every ordered eigenvalue.
(c) (GUESSED; the lane must check the hypotheses.) By the Araki-Lieb-Thirring inequality, tr (e^{−V/2} e^{−sC} e^{−V/2})^u ≥ tr (e^{−V/2m} e^{−sC/m} e^{−V/2m})^{mu} for every integer m ≥ 1, and the right side tends to tr e^{−u(V+sC)} as m → ∞ (Trotter). So heat-kernel torus traces dominate the traces of a continuous-time Kogut-Susskind semigroup, monotonically in the time refinement.
Quantifiers and constants: all β > 0, all j; no constant. Why it is not equivalent to the seed: it is an identity for the one-plaquette weight and holds for every β and every lattice. What it must deliver to the next link: a two-sided comparison of D(u) between the Wilson transfer and a transfer with a semigroup in the time direction. (b) and (c) give one side each. Where I expect it to die: the comparison is in operator order, and D(u) is a ratio; one-sided order does not control it.

**Component 2 (for item 2). Lemma OU (the sum of the projections is an order unit).**
Statement. Let Q_1, ..., Q_r be orthogonal projections on a Hilbert space and H = Σ_x Q_x. Let γ > 0, let S ≥ 0 be a bounded operator, and let (r_xy) be a real symmetric matrix with zero diagonal such that

  H² − γ H = S + Σ_{x<y} r_xy (Q_x Q_y + Q_y Q_x).

Put ρ = max_x Σ_y |r_xy|. Then H² ≥ (γ − ρ) H. In particular, if γ > ρ, the spectrum of H does not meet (0, γ − ρ).
Proof (PROVED). For projections P, Q: (P − Q)² ≥ 0 and (P + Q)² ≥ 0 give −(P + Q) ≤ PQ + QP ≤ P + Q. So Σ_{x<y} r_xy (Q_x Q_y + Q_y Q_x) ≥ −Σ_{x<y} |r_xy| (Q_x + Q_y) ≥ −ρ H. ∎
Use: Q_x = 1 − E_x for the block conditional expectations of Pack K on gauge-invariant L². A numerical sum-of-squares decomposition of H² − γH with a small residual in the span of the anticommutators becomes a proof of a block-dynamics gap γ − ρ. It is the analogue of the order-unit lemma of A13. Why it is not equivalent to the seed: it is operator algebra, true for any projections. Limit: it certifies one law on one finite lattice. It does not carry in K.

**Component 3 (for items 3 and 4). Two closure lemmas, so that later rows do not reopen these classes.**
Lemma REP (PROVED). Let K ≥ 0 be trace class, K ≠ 0, and p_k = tr K^k/(tr K)^k. Then p_2^{k−1} ≤ p_k ≤ p_2 for all integers k ≥ 2. Proof: let X take the value q_i = κ_i/tr K with probability q_i. Then p_k = E[X^{k−1}], 0 ≤ X ≤ 1, and Jensen gives the left side. ∎ So every replica number carries the information of k = 2, up to a power. The tensor-power pattern (A3) gives nothing for (PUR-io).
Lemma NC (PROVED). Let ν_1, ν_2 be two translation-invariant states that cluster (the covariance of F and its translate by t tends to zero as t → ∞, for every bounded local F), and let F be bounded and local with ν_1(F) ≠ ν_2(F). Then ν = (ν_1 + ν_2)/2 has lim_t Cov_ν(F, τ_t F) = (ν_1(F) − ν_2(F))²/4 > 0. Proof: Cov_ν = ½(Cov_1 + Cov_2) + ¼(ν_1(F) − ν_2(F))(ν_1(τ_tF) − ν_2(τ_tF)), and translation invariance gives ν_i(τ_tF) = ν_i(F). ∎ So the clustering laws are not a convex class, and the dense-model pattern (A5) has no model class.
Why these are not equivalent to the seed: they are negatives about method classes. They are not gate instances and I do not claim them as progress on the target.

### 4.4 Reading list (12 papers; the question each full read must answer)

1. P. Hartman, G. Watson, "'Normal' distribution functions on spheres and the modified Bessel functions", Ann. Probab. 2 (1974) 593-607. Question: is λ ↦ I_{√(1+λ)}(β)/I_1(β) a Laplace transform of a probability measure for every β > 0? What are its mean and its support?
2. J. Kent, "The infinite divisibility of the von Mises-Fisher distribution for all values of the parameter in all dimensions", Proc. London Math. Soc. 35 (1977) 359-384 (UNVERIFIED pages). Question: does infinite divisibility hold on the 3-sphere in the sense of convolution on SU(2), so that the Wilson weights at different β are ordered by convolution?
3. H. Araki, "On an inequality of Lieb and Thirring", Lett. Math. Phys. 19 (1990) 167-170 (UNVERIFIED pages). Question: does the inequality apply to the transfer with its gauge projection, and does it give the monotone chain of Component 1 (c)?
4. N. Ozawa, "Noncommutative real algebraic geometry of Kazhdan's property (T)", J. Inst. Math. Jussieu 15 (2016) 85-90. Question: what exactly makes the Laplacian an order unit, and does Lemma OU capture all of it for block projections?
5. M. Kaluba, D. Kielak, P. Nowak, "On property (T) for Aut(F_n) and SL_n(Z)", Ann. of Math. 193 (2021) 539-562. Question: does the passage from n = 5 to all n use only commutation of generators with disjoint supports (then it is Knabe's method, on file), or a relation that is special to the group?
6. W. T. Gowers, B. Green, F. Manners, T. Tao, "On a conjecture of Marton", arXiv:2311.05762. Question: what is the exact fibring identity, and which inequality turns it into a strict descent? Is there an analogue for the symmetric defect δ_ij of item 3?
7. O. Reingold, L. Trevisan, M. Tulsiani, S. Vadhan, "Dense subsets of pseudorandom sets", FOCS 2008. Question: does any form of the dense model theorem work with a model class that is not convex? (If not, Lemma NC closes the class for good.)
8. A. Marcus, D. Spielman, N. Srivastava, "Interlacing families II: mixed characteristic polynomials and the Kadison-Singer problem", Ann. of Math. 182 (2015) 327-350. Question: is there a mixed characteristic polynomial for a sum of positive operators of large rank with a fixed sandwich e^{−V/2} · e^{−V/2}, and a root bound for it?
9. C.-F. Chen, J. Garza-Vargas, J. Tropp, R. van Handel, "A new approach to strong convergence", arXiv:2405.16026. Question: which structure in the parameter does the method need (polynomial, rational, a bound on the degree)? Does the character expansion in the variables c_j(β) have it at a fixed lattice size?
10. T. Hartman, D. Mazáč, L. Rastelli, "Sphere packing and quantum gravity", JHEP 12 (2019) 048, arXiv:1905.01319. Question: do the linear functionals ever give a lower bound on a gap, or an upper bound on a density of states, without a protected vacuum energy in the crossed channel?
11. M. Göpfert, G. Mack, "Proof of confinement of static quarks in 3-dimensional U(1) lattice gauge theory for all values of the coupling constant", Comm. Math. Phys. 82 (1982) 545-606. Question: the proof works because many defects sit in one screening volume. Which step uses abelian duality only, and is there a defect variable for SU(2) (for example the plaquettes with a large clock s in Lemma HW-SU2) with the same counting?
12. B. Andrews, J. Clutterbuck, "Proof of the fundamental gap conjecture", J. Amer. Math. Soc. 24 (2011) 899-916. Question: does the two-point maximum principle have a form that does not depend on the diameter or the dimension, so that it survives infinitely many modes?

### 4.5 Labels and limits

- PROVED here: F1, F2, F3, E1 to E8 (E7 up to differentiation almost everywhere), Lemma K modulo the cited detectability lemma, Lemma HC, Lemma OU, Lemma REP, Lemma NC, the cocycle identity of item 3. All are by hand, by one author, and checked by no one. No Lean and no numeric run supports them. By the lane's rule on written proofs, none of them may land as a proof note in this state.
- Most of the PROVED items of sections 0 and 2 turned out to be on file in Phase 2. I kept them because the brief asked for the first estimates written out.
- Every reference comes from memory. The ones marked UNVERIFIED are the ones where I am not sure of a page, a year or a theorem number. I opened no paper.
- Phase 2 was done by keyword search with bounded context. I read none of the brainstorm files in full.
- I did not run the hypothesis (H) of Pack E against the Lean files for all four directions.

RESULT: Row 1682 (Claude Fable 5.2, laptop; author only, checked by no one; no numeric run). 27 solved problems mined, 12 strategy types mapped to (PUR-io). Phase 2: all eight candidates are on file; no new candidate has a live gate link. Least-covered three: (1) Wilson weight as a random-time heat kernel on SU(2), component Lemma HW-SU2 with the order bound T_Wilson ≥ T_HK; (2) sum-of-squares block-gap certificates, component Lemma OU (order-unit rounding); (3) entropic descent and dense-model transference, closed by Lemmas REP and NC and a symmetric doubling defect with no sign. Reading list: 12 papers.
