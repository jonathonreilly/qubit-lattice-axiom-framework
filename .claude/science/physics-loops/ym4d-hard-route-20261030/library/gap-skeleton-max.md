lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-11T09:11Z

# gap-skeleton-max (row 669): a plan for the mass gap of four-dimensional SU(2) Yang-Mills

State of this file: IN PROGRESS, started 2026-11-10T21:11Z at pinned commit 42e758764. Written section by section. The opening lines (chosen approach, crux lemma, how far the attack went, first proof item) are filled in last.

- **Chosen approach:** (not yet chosen; Part 1 is being written)
- **Crux lemma:** (pending)
- **How far the attack went:** (pending)
- **First proof item:** (pending)

Provenance: one author run, Claude Fable 5.2 at max effort, no subagents, not checked by any other model. Nothing here is a status claim. Not opened, per the row: `library/gap-skeleton.md`. Row 662 of `FINISH.md`: only its first 220 characters were seen, in a listing of row prefixes made before row 669 was read (they name the row and its model, no route); nothing more of it was read.

## Part 0. The object (facts only)

Source: `YM4_1400.tex` of Sussman and Alpoge (text written with Claude and Codex), commit `2bc0658f91d2`, 136,637 lines, fetched by URL into a scratch folder of this run. Line numbers below are lines of that file. Read: lines 137-200, 1560-1980, 2357-2490, 2862-2920, and the passages found by a search for "mass gap", "spectral gap", "clustering", "Wilson loop", "area law", "confine". Not read: the proofs.

**0.1 What exists, and under which condition.** The account is a conditional outline. Abstract, L143-146: "Under the stated uniform renormalization and short-distance hypotheses, we outline the continuum construction of the renormalized tr(F^2) observable in four-dimensional Wilson SU(2) theory at sufficiently small reference coupling." The hypotheses are the packages A-H of the dependency catalogue (L1913-3060). L2040 on: A1-A4 backgrounds, B1-B4 expansion and one-loop law, C1-C4 large-field histories, D1-D4 sources, E1-E4 flow, F1-F4 short distance, G1-G4 symmetries and phases, H1-H4 reconstruction. L3050-3051: "Actual verification of D1 and of the interacting short-distance law is not supplied here."

- *Measure.* L1650: Wilson's measure mu_{K,l,beta}(dU) = Z^{-1} exp(-beta sum_p a_p(U)) dU on the torus Lambda_{K,l} = a_K Z^4 / l Z^4, a_K = L^{-K}, G = SU(2), a_p(U) = 1 - (1/2) Re tr U_p.
- *Observable.* One scalar: O(f) = sum_p f(x(p)) a_p(U) (L1651), "the tr(F^2) observable" (L1655). No Wilson loop, no area law, no other field: a search of the file for "Wilson loop", "area law", "string tension", "glueball" finds only the reference to Wilson's paper (L136631).
- *Functions.* Connected functions S^T_n(f_1..f_n) for n >= 2 on tuples with pairwise disjoint supports (L1652-1657). The one-point function diverges and is subtracted (L1741-1746).
- *Unit of length.* The lattice with spacing a_K = L^{-K} is taken at a bare coupling beta such that the running coupling first reaches the window [g^{-2}, g^{-2} + B_sharp] after K steps (L1663-1670). So the unit of length is the scale where the running coupling equals the small reference coupling g. L1755: beta / log(1/a_K) -> 11 N^2 / (12 pi^2).
- *Volume.* Tori T_l with l in {2 L^m}, l >= l_*(g) (L1640-1647); limits on T_l and on R^4; "volume-first" limits take l -> infinity at fixed spacing first (L1690).
- *Limits.* Theorem "Continuum correlations" (L1748-1865), clause (a): subsequential limits exist on each torus and on R^4; along tuned couplings the whole sequence converges on a torus.
- *Axioms.* Clause (b): W_4 and translation invariance, reflection positivity at coordinate mirrors, symmetry, regularity, growth with (n!)^kappa. L1768-1773: a Hilbert space H(S) with "T_t = e^{-tH} ... H >= 0 and H Omega = 0", momenta P_j, and W_3.
- *Components.* Theorem "Canonical components" (L1884-1909): a volume-first limit S is O(4)-invariant, "satisfies H >= |P_j|" (L1894), and sigma_S = int sigma_xi lambda(d xi) over a compact space X. ker H is unitarily L^2(X, lambda) (L1895). Each component has "a unique vacuum, ker H_{sigma_xi} = C Omega" and "joint spectrum ... in the closed forward cone {E >= |q|}" (L1899). L1908: each sigma_xi satisfies every Osterwalder-Schrader axiom and gives "a single Hermitian scalar field ... unique vacuum ... local". The number of components is not determined.
- *Non-triviality.* Clause (c)(3)-(4), L1788-1797: the two-point function at short distance d equals (3(N^2-1)/pi^4) g(d)^4 K_free(f,h)(1+eps), K_free(f,h) = iint f(x) h(y) |x-y|^{-8}, with g(d)^{-2} ~ (11 N^2/(12 pi^2)) log(1/d).

**0.2 What is uniform in what.** L1724: "Apart from dependences that are displayed, the constants do not vary with K, beta, l or with positions ... Each constant ... may in addition depend on g". L1958-1962: "All uniform constants below must be independent of K, the torus, the history, the positions of the tests, and the relevant Gibbs state. Dependence on g, n, d, R must be displayed." The bound that carries this is clause (c)(2), L1781: |S^T_n| <= C^infty_n(d; R) prod ||f_i||_sharp for l >= C n (R+1), with (L1785) "C^infty_n(d;R) does not increase as d grows", valid also for every periodic Gibbs state at a first-passage datum. So: the bounds are uniform in the cutoff, in the volume and in the Gibbs state, at fixed small g. They are not uniform in g, and they contain no rate of decay in the separation d. All multiscale control is at scales below the unit of length, where the coupling is at most about g.

**0.3 What the account says about decay or a gap.** Three things.

1. The only decay statement is polynomial. L1900-1907: "|sigma_xi(X . tau_v Y) - sigma_xi(X) sigma_xi(Y)| <= C(X,Y) |v|^{-2} (|v| >= r(X,Y))". Its source is reflection positivity alone, the lattice "plateau law" (L2884-2893), valid for every translation-invariant Wilson Gibbs state at every beta, "with one numerical constant C independent of a, beta, nu, r, n, A, B". L126124-126127: "No spectral gap above the invariant subspace has been proved: the filter weight vanishes linearly near zero energy, and removing it is exactly what produces the inverse-square term."
2. The account says that it proves no gap. L556-563: "A polynomial cluster estimate likewise gives no positive mass gap ... If d mu_v(E) = E e^{-E} dE, the integral is (1+t)^{-2}. It decays, yet its spectral measure meets every interval (0, epsilon)." L3054-3056: "A mass-gap conclusion would require a new estimate, for example a bound yielding spectrum outside zero contained in [m, infinity) for some m > 0. None of the packages above supplies that estimate." Also L117539-117541 and L122948-122959.
3. A mass that does appear is not the gap. L2025 and L6615-6618: the mass of the constrained (gauge-fixed, block-averaged) fluctuation operator is "not a physical Yang-Mills mass gap". It is the ultraviolet regulator mass of one renormalization step.

**0.4 The exact statement of the gap for this object.** Let S be a volume-first limit at reference coupling g and sigma_xi a canonical component, with Hilbert space H(sigma_xi), vacuum Omega and Hamiltonian H_xi >= 0, ker H_xi = C Omega.

- **(GAP)** There is m = m(g) > 0 with spec(H_xi) contained in {0} union [m, infinity), for every component (or for lambda-almost every xi).
- **Equivalent Euclidean form.** For all F in a total set of C S({x_4 > 0}): sigma_xi(theta F-bar . tau_{t e_4} F) - |sigma_xi(F)|^2 <= C(F) e^{-m t} for all t >= 0. (If the spectral measure mu_F of F - <Omega,F> Omega has Laplace transform <= C e^{-mt} for all t, then mu_F((0,m)) = 0; a total set suffices because the range of the spectral projection of (0,m) is then orthogonal to a total set.) The set must contain products of fields: decay of the two-point function of the field alone gives the gap only on the one-field subspace.
- **Scale.** The unit of length is where the coupling is g. The expected size is m(g) ~ exp(-(12 pi^2/(11 N^2)) / g^2) up to a power of g, about exp(-2.69/g^2) for N = 2. So (GAP) is a statement about distances exp(+2.69/g^2) times larger than every scale the existence account controls. The existence account gives no small parameter there.

**0.5 Weaker statements that would still be new theorems** (to the author's knowledge at the time of Part 0; Part 2 checks them against the literature).

- **(W-lat)** At one fixed large beta (beyond the convergence radius of the strong-coupling expansion), the infinite-volume four-dimensional SU(2) Wilson lattice theory has exponential clustering: |nu(A tau_y B) - nu(A) nu(B)| <= C(A,B) e^{-m(beta)|y|}. No continuum limit is needed. This already separates SU(2) from U(1).
- **(W-unif)** (W-lat) for all beta, with m(beta) a_K^{-1} bounded below along the first-passage sequence. Together with the existence account this is (GAP).
- **(W-tor)** On a fixed torus T_l^3 x R of physical side l, the continuum limit has a gap m(l, g) > 0 uniformly in the cutoff. At finite cutoff the gap is trivial (strictly positive compact transfer operator); uniformity in the cutoff is the content. No infrared problem enters when l is of order one.
- **(W-rate)** Any decay of the connected functions in a component faster than the |v|^{-2} that reflection positivity gives; in particular faster than |v|^{-8}, the rate of tr(F^2) in a free Maxwell theory.
- **(W-cond)** (GAP) from one named infrared hypothesis that is itself a statement about the lattice measure at one scale.

## Part 1. Own thinking, before any digest or paper on the gap

(pending)

## Part 2. The literature, after Part 1

(pending)

## Part 3. The skeleton

(pending)

## Part 4. The queue

(pending)
