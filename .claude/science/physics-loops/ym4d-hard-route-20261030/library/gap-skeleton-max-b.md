lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-11T09:49Z

# gap-skeleton-max-b: author run for the plan of the mass gap (FINISH row 670)

Status: in progress. This file is written section by section. The summary lines required by the row (chosen approach, crux lemma, how far the attack went, first proof item) are filled in at the end and will stand here.

Provenance: Claude Fable 5.2, max effort, one session, no subagents, pinned at commit bf474ee1c. Research-stage working state. It grants no status. Nothing here is a public claim.

Disclosure on the "do not open" rule: I did not open `library/gap-skeleton.md`, `library/gap-skeleton-max.md`, `library/gap-transfer.md` or `library/gap-os-equiv.md`. When I located my own row with `grep -n 'gap-skeleton' FINISH.md | cut -c1-400`, the first 400 characters of rows 662, 667, 668 and 669 were printed. Those characters hold scheduling text and the object of row 667 (SU(2), a spatial torus, the Wilson action). They hold no list of routes and no crux. I read nothing more of rows 662 and 669.

## Part 0. The object (facts only)

Source: `YM4_1400.tex` of the Sussman-Alpoge repository (authors of the text: Ethan Sussman and Levent Alpoge, with Claude and Codex), commit 2bc0658f91d2d03ba44e20bf695067e0a56a2ed9, 136,637 lines, fetched by URL into my own scratch folder. Line numbers below are lines of that file. I read the abstract, Theorem 0, the setting (1647-1746), the three main theorems (1748-1846, 1884-1908, 122703-122720), catalogue packages D and G in part (2357-2420, 2792-2860), the source hypothesis (98387-98440), the plateau estimate (125584-125650), and every line that matches "mass gap" or "spectral gap" (22 lines). I did not read the proofs.

### 0.1 What exists, and under what hypotheses

The account is conditional. Abstract, 143-149: "Under the stated uniform renormalization and short-distance hypotheses, we outline the continuum construction of the renormalized tr(F^2) observable in four-dimensional Wilson SU(2) theory at sufficiently small reference coupling." Theorem 0, 156-164: "Assume the uniform renormalization and short-distance estimates stated below. For sufficiently small reference coupling, the correlations of tr(F^2) in four-dimensional Wilson SU(2) theory have nontrivial volume-first subsequential continuum limits. In every canonical component, the Schwinger functions satisfy the Osterwalder-Schrader axioms and reconstruct a local Hermitian scalar Wightman theory with positive energy and a unique vacuum."

- **Measure.** Wilson's measure on a torus, 1647-1653: mu_{K,l,beta}(dU) = Z^{-1} exp(-beta sum_p a_p(U)) dU, with a_p(U) = 1 - (1/2) Re tr U_p, G = SU(2), lattice spacing a_K = L^{-K}, torus side l in {2 L^m}.
- **Observable.** One scalar density, 1651-1655: O(f) = sum_p f(x(p)) a_p(U), "the tr(F^2) observable". The functions are the connected correlations S^T_n(f_1,...,f_n) = <O(f_1);...;O(f_n)> for n >= 2 on "tuples of real C_c^1 functions with pairwise disjoint supports". No Wilson loop, no other observable.
- **Unit of length.** 1658-1664: the unit is "the scale at which the flow reaches, for the first time, the reference window g^{-2} <= x <= g^{-2} + B_sharp". So the running coupling at distance 1 is about g, and g is small. Along the sequence, beta / log(1/a_K) tends to 11 N^2 / (12 pi^2) (1751).
- **Volume.** Three kinds of limit, 1673-1680: on a fixed torus T_l; on R^4 with l_j to infinity; and "volume-first": "each nu_j ... is a limit point of the periodically extended torus measures as l to infinity, with spacing and coupling held fixed. Thus the volume is removed first and the spacing only afterwards." All limits on R^4 are subsequential.
- **Axioms proved under the hypotheses.** Theorem `thm:continuum-main` (b), 1757-1773: invariance under the hypercubic group W_4 and translations; reflection positivity at coordinate mirrors; symmetry; regularity; the growth bound |S_n(phi)| <= c C^n (n!)^kappa |phi|_{kn}; a Hilbert space H(S) with T_t = e^{-tH}, "H >= 0 and H Omega = 0", momenta P_j. Theorem `thm:phase-main`, 1884-1908: a volume-first limit is O(4)-invariant, has H >= |P_j|, and has a canonical decomposition sigma_S = int sigma_xi lambda(d xi); each component sigma_xi satisfies "every Osterwalder-Schrader axiom ... growth, invariance under R^4 x O(4), reflection positivity, symmetry and clustering", has "a unique vacuum, ker H_{sigma_xi} = C Omega", joint spectrum in the closed forward cone, and gives a Wightman theory with "a single Hermitian scalar field".
- **Non-triviality.** (c)(3)-(4), 1784-1797: the two-point function of bumps of size d at separation about d equals 3(N^2-1)/pi^4 times g(d)^4 times K_free(f,h) times (1+eps), with (11 N^2 / 12 pi^2) g(d)^2 log(1/d) near 1. This is the free-field |x-y|^{-8} law with the asymptotic-freedom logarithm, at short distance only.
- **Hypotheses.** `thm:continuum-main` opens (1749-1753): "Assume the uniform background, interaction, history, flow and ordinary-source estimates of [the dependency catalogue]". The catalogue says (1921-1925): "The catalogue identifies where the principal multiscale estimates enter. Those estimates require proofs beyond the finite-dimensional and reference calculations given here." And 3050-3051: "Actual verification of D1 and of the interacting short-distance law is not supplied here." So the object exists conditionally on packages A-F (the ultraviolet multiscale estimates). Our T0 chain is the work of closing them.

### 0.2 What is uniform in what

- 1744: "Apart from dependences that are displayed, the constants do not vary with K, beta, l or with positions."
- (c)(2), 1777-1782: |S^T_n| <= C^infty_n(d;R) prod ||f_i||_sharp for l >= C n (R+1); "C^infty_n(d;R) does not increase as d grows. The bounds (2) also hold, with no condition on a volume, for S^T_n[nu], where nu is an arbitrary periodic Gibbs state". So the bound at separation d is uniform in the cutoff and in the volume, and it is monotone in d. No rate of decay in d is stated.
- The source hypothesis D1, 98395-98410: |Z_{a,l}(W)| <= exp[V + Re U(W) + Re sum_{s=0}^{K} sum_D e_{s,D}(W) + C_+ l^4] and Z_{a,l}(0) >= exp(V - C_- l^4), with local terms |e_{s,D}| <= A e^{-kappa m(D)} at every scale s from 0 to K. The scales s run from the cutoff up to the unit scale and stop there. The error terms C_+- l^4 are volume terms at unit scale: at distances above 1 the hypothesis gives no locality.
- Infinite volume comes from compactness and the chessboard estimate, not from an expansion (98350-98385).

### 0.3 What the account says about decay or a gap

- Clustering, 1900-1905: "|sigma_xi(X . tau_v Y) - sigma_xi(X) sigma_xi(Y)| <= C(X,Y) |v|^{-2} (|v| >= r(X,Y))". The rate is a power. It comes from the plateau estimate, 125588-125591: "a consequence of translation invariance and reflection positivity in coordinate and diagonal directions. No infrared bound, mass gap, or differentiability of a pressure is assumed."
- 126124-126127: "No spectral gap above the invariant subspace has been proved: the filter weight vanishes linearly near zero energy, and removing it is exactly what produces the inverse-square term."
- 556-563 and 122948-122959: "A polynomial cluster estimate likewise gives no positive mass gap ... If d mu_v(E) = E e^{-E} dE, the integral is (1+t)^{-2}. It decays, yet its spectral measure meets every interval (0, eps)."
- 3054-3056: "A mass-gap conclusion would require a new estimate, for example a bound yielding spectrum outside zero contained in [m, infinity) for some m > 0. None of the packages above supplies that estimate."
- 117539-117541: "The assertion concerns this scalar cyclic sector. Gauge-theory existence, full observable identification and a positive mass gap require separate arguments."
- 2025-2026, on the constrained fluctuation operator: "A mass for this constrained operator is not a mass gap for the physical continuum Hamiltonian."

So the account claims no decay beyond |v|^{-2}, and it says so. The number of components (the set X of xi) is not bounded: 1890-1892 allows ker H of infinite dimension for the mixture.

### 0.4 The exact statement of the gap for this object

Let sigma be a canonical component of a volume-first limit at reference coupling g, with Hilbert space H(sigma), vacuum Omega, and Hamiltonian H >= 0, ker H = C Omega (0.1).

**(GAP).** There is m > 0 with spec(H) contained in {0} union [m, infinity).

Equivalent forms on this object (the equivalence is the spectral theorem plus density of the vectors [F]; it is routine and I do not prove it here):

- **(GAP-E).** For all F, G in the positive-time test algebra, |sigma(theta F-bar . tau_{t e_4} G) - sigma(theta F-bar) sigma(G)| <= ||(1-P_Omega)[F]|| ||(1-P_Omega)[G]|| e^{-m t} for all t >= 0.
- **(GAP-2).** The same bound for each single vector: <[F], e^{-tH}[F]> - |<Omega,[F]>|^2 <= ||(1-P_Omega)[F]||^2 e^{-mt}.

Two points fix what "the gap" means here.

1. H(sigma) is the cyclic sector of one scalar field. So (GAP) is the gap in the scalar sector that tr(F^2) generates. A gap for the whole theory needs more observables (the account's F4), and a state with no overlap with tr(F^2) polynomials is invisible.
2. The unit of length is the scale where the running coupling is g. If the usual picture is right, m is of order exp(-12 pi^2 / (11 g^2)) up to a power of g (two-loop), which is far below 1. Between distance 1 and distance 1/m the coupling runs from g to order 1. No estimate of the account reaches those scales.

**The uniform lattice form that gives (GAP) in the limit.** There are m > 0 and, for all local F, G as above, a constant C(F,G), such that for all first-passage data (K, beta) and all periodic Gibbs states nu at (K, beta): |nu(theta F-bar . tau_{t e_4} G) - Pl_nu(F,G)| <= C(F,G) e^{-m t}, with m independent of K, beta, nu. Here Pl_nu is the invariant plateau of 125621-125627.

### 0.5 Weaker statements that would still be new theorems

I list them from the weakest. "New" here means: I know of no proof. Part 2 checks this against the sources.

- **(W1) Lattice, one coupling.** Exponential clustering of the infinite-volume Wilson SU(2) measure at one value of beta above the convergence radius of the strong-coupling expansion. No uniformity.
- **(W2) Fixed finite volume, continuum.** On the continuum limit over the torus T_l with l fixed and time unbounded: the Hamiltonian H_l has a gap m(l) > 0. At a fixed cutoff this is Perron-Frobenius on a compact space. The content is uniformity in the cutoff.
- **(W3) Small volume, quantitative.** m(l) >= c g(l)^{2/3} / l for l small. This is the rate of Luescher's small-volume expansion (recalled from memory; Part 2 checks it).
- **(W4) Volume-uniform.** inf over l >= l_0 of m(l) > 0. This is (GAP) for the torus limits and is the full difficulty.
- **(W5) Two-point decay only.** The limit two-point function of tr(F^2) decays exponentially. This gives a gap in the spectral measure of the one-field vectors, not on all of H(sigma).
- **(W6) A conditional theorem.** (GAP) from one named hypothesis on the effective measure at a scale where the coupling is of order 1, with every scale below it covered by the existence estimates.
- **(W7) Uniqueness.** The canonical decomposition is trivial (one component). The account does not claim it. It is implied by a volume-uniform gap, and it is weaker.
