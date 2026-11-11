lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-11T11:45Z

# gap-skeleton-max (row 669): a plan for the mass gap of four-dimensional SU(2) Yang-Mills

State of this file: IN PROGRESS. Second run, under the restart rule of row 669, started 2026-11-10T23:45Z at pinned commit 037414f03. Part 0 is the text of the first run (2026-11-10T21:11Z, commit 42e758764), kept. Written step by step; each step is appended before the next one starts. The opening lines (chosen approach, crux lemma, how far the attack went, first proof item) are filled in last.

- **Chosen approach:** (not yet chosen; Part 1 is being written)
- **Crux lemma:** (pending)
- **How far the attack went:** (pending)
- **First proof item:** (pending)

Provenance: one author, Claude Fable 5.2 at max effort, no subagents, not checked by any other model. Nothing here is a status claim. Not opened, per the row: `library/gap-skeleton.md`, and `library/gap-skeleton-max-b.md` (the independent second author run of row 670). Row 662 of `FINISH.md`: only its first 300 characters were seen, in two listings of row prefixes (they name the row, its model and "attack first the node where it can die"; no route); nothing more of it was read. Rows 667, 668 and 670: only their first 300 characters were seen in the same listing, before Part 1; they are read in full only at the duplicate check before the attacks (Section 1.C).

Check of Part 0 by the second run (three citations, as the restart rule asks): L1785 ("does not increase as d grows"), L1899-1907 (unique vacuum, forward cone, the |v|^{-2} cluster bound), L3054-3056 and L126124-126127 (no gap proved) were re-read in the source and agree with the quotations below.

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

Written before any digest or paper on the gap was opened. Facts quoted from memory are marked (memory); Part 2 confirms or corrects them. Part 1 is not edited after Part 2 starts; corrections go under it.

### 1.A The question itself: why is there a gap, as mathematics?

**A.1 One reduction, and one constraint on every mechanism.** The existence account controls all scales below the unit of length, where the coupling is g. So it can deliver, uniformly in the cutoff K, an effective lattice measure on the unit lattice: Wilson's weight at beta_* ~ 1/g^2 plus corrections that are small in a polymer norm, plus rare large-field regions. Hence

- (GAP) follows from the account plus **(W-lat, robust form): exponential clustering, with one rate, for every lattice gauge measure in a small neighbourhood of Wilson's measure at one large beta_*.** The neighbourhood is in a norm of exponentially decaying gauge-invariant polymer activities. The transport of the observable tr(F^2) to the unit lattice is a second, routine-looking, input.
- The expected rate is m ~ exp(-c beta_*) in lattice units. So **a mechanism that gives a gap of size a power of 1/beta at the unit scale is wrong**: it would prove too much. A correct mechanism must be able to produce a number as small as exp(-c beta). This removes every argument that uses a local curvature or a local convexity bound of size O(1) or O(beta^{-p}).

**A.2 The known answers that every idea must reproduce** (memory; Part 2 confirms).

| Case | Answer | Mechanism |
|---|---|---|
| Any compact G, any d, small beta | gap | independence of links; convergent expansion |
| d = 2, any G | gap, range zero in axial gauge | plaquette variables are independent |
| U(1), d = 4, large beta | no gap, free photon | the flux is conserved; monopole loops are dilute |
| U(1), d = 4, small beta | gap | monopole loops condense |
| U(1), d = 3, all beta | gap ~ exp(-c beta) | point monopoles, Debye screening |
| Finite G, d = 4, large beta | gap, no confinement | discreteness: every excitation costs a fixed energy |
| SU(2), small 3-torus of side l | gap ~ g(l)^{2/3} / l | constant modes: quartic potential |tr [c_i, c_j]^2|, valleys closed by zero-point energy |
| SU(2) + adjoint Higgs, d = 4, Higgs region | no gap, photon | the field selects a U(1) |
| SU(2) + fundamental Higgs | gap everywhere expected | no residual U(1) |

Three lessons. (a) An abelian theory can have a gap (rows 4, 5), and a gap needs no confinement (row 6). So "non-commutative" is neither necessary nor sufficient; the proof must use what SU(2) has and the U(1) Coulomb phase lacks. (b) Row 8 is a **third test**, not in the row's list: a proof must fail when an adjoint Higgs field is added. So the proof cannot use the group alone; it must use the dynamics of the pure gauge measure. (c) Row 7 is the one place where a gap is computed at weak coupling. Its mechanism is exact mathematics: on constant fields the potential |c_i x c_j|^2 vanishes on the abelian valleys c_i parallel, and the zero-point energy of the two charged components, of frequency |c|, closes the valley with an effective potential that grows linearly.

**A.3 Where the group SU(2) can enter a proof.** Five places; each approach below must use one.

1. *Curvature.* Ric(SU(2)) > 0 and Ric(U(1)) = 0. The quotient of the configuration space by the gauge group does not lower sectional curvature (O'Neill's formula).
2. *Flux is not conserved.* pi_1(SU(2)) = 0, pi_1(SO(3)) = Z_2, pi_1(U(1)) = Z. A U(1) flux through a 2-torus is an integer and costs a classical energy Phi^2/(2e^2) per symmetric 4-torus, the same at every size: exactly marginal. An SU(2) centre flux is carried by a commutator, Omega_1 Omega_2 = -Omega_2 Omega_1 with Omega_1 = i sigma_1, Omega_2 = i sigma_2, with zero classical action. Its free energy on a torus of side l comes from fluctuations only. Count of flat directions: f_m(l) = -log(Z_twisted/Z) ~ 4 log(1/g(l)) + const at small l, which decreases as l grows, at a rate fixed by the beta function. In U(1) the same quantity is constant in l.
3. *No continuous flux symmetry.* The photon of U(1) is tied to the conserved integer flux (in modern words, a broken continuous 1-form symmetry). SU(2) has only the Z_2 centre. A discrete symmetry forces no massless mode.
4. *The sign of the one-loop coefficient.* b_0 > 0 makes the Gaussian point unstable in the infrared. In U(1) the coupling does not run. The sign comes from the spin coupling of the charged components to an abelian background (lowest Landau level below zero).
5. *The gauge-fixed region is bounded.* The Faddeev-Popov operator -d.D(A) is linear in A, so the region where it is positive is convex and bounded in every direction; the bound on a mode of wave number k is of order k/g. In U(1) the operator does not depend on A.

**A.4 The wall.** Places 2, 4 and 5 act when g(l) is of order one. Between the unit of length and the scale exp(c/g^2) there is a finite number of scales, about c/(g^2 log L), and on the last of them there is no small parameter. Every approach must say how it crosses them. I see three ways, and Part 1 is organised by them:

- **(I) an exact inequality that holds at every coupling**: monotonicity, convexity, positivity, a comparison;
- **(II) a finite-size criterion that is already satisfied in the perturbative regime**: a statement "if a quantity Q of a finite box passes a threshold, then exponential decay", for which the free theory sits exactly at the threshold and the one-loop term, whose sign is the sign of b_0, tips it;
- **(III) an analytic continuation with uniform bounds**: decay is known at one end of a path in a parameter, the functions are bounded and analytic along the path, and the two-constants theorem carries the decay along.

A fourth way, a renormalization group that reaches strong coupling by expansion, has no small parameter. I list it and give it no weight.

### 1.B The approaches

Notation. Lambda is a finite periodic lattice in d = 4, X = SU(2)^{links}, A(U) = sum_p a_p(U), mu_b = Z^{-1} e^{-b A} dU, and gamma(b) is the spectral gap of the Langevin generator L_b = -Delta + b <grad A, grad .> on gauge-invariant functions in L^2(mu_b). A lower bound gamma(b) >= gamma_0 > 0 that is uniform in Lambda gives exponential clustering at rate >= c sqrt(gamma_0) (finite range and compact fibres; routine). c_AF = 3 pi^2/11 is the expected rate, m ~ exp(-c_AF b) with b = 4/g^2.

Each approach has: the mechanism; the CRUX; why it could be true; the U(1) test; the known-answer test; how it dies.

**B1. Transport along the coupling (way I). The measure at b is the image of the measure at b_0 under a map that is Lipschitz with constant exp(c(b - b_0)).**

- *Mechanism.* Let phi_b solve the Poisson equation L_b phi_b = A - mu_b(A) and put Z_b = -grad phi_b. Then div Z_b - b <grad A, Z_b> = A - mu_b(A), so the flow of Z_b carries mu_{b_0} to mu_b. If the symmetric part of grad Z_b is at most c, the flow map is exp(c(b-b_0))-Lipschitz, and a Poincare inequality is carried along a Lipschitz map: gamma(b) >= gamma(b_0) exp(-2c(b - b_0)). This is the asymptotic-freedom law, obtained from one bounded quantity. In finite volume phi_b exists and is smooth for every b; only the uniform bound is at stake.
- **CRUX (T).** There is c < infinity, independent of Lambda and of b >= b_0, such that Hess phi_b(U) >= -c for all U, where L_b phi_b = A - mu_b(A). It is a one-sided bound on the solution of an elliptic equation. A weaker form that may be the true one: the bound holds on a set of U that the flow does not leave, of mu_b-measure close to one.
- *Why it could be true.* (i) Gaussian model, mu_b = exp(-(b/2)(A, K A)): phi = (A, P A)/(4b) with P the projection on the range of K, Hess phi = P/(2b) >= 0, and the flow is the rescaling A -> A sqrt(b_0/b), a contraction. The bound holds although gamma = 0. So (T) does not need a gap as input. (ii) Spherical (N = infinity) sigma model in d = 2: mu_b is Gaussian with covariance b^{-1}(-Delta + m_b^2)^{-1} and m_b^2 = 32 exp(-4 pi b). The transport map is linear, with multiplier M_k^2 = (b/b')(k^2 + m_b^2)/(k^2 + m_{b'}^2). Its logarithmic derivative in b' is at most 2 pi - 1/(2b) at k = 0 and negative for k >> m_b. So (T) holds with c = 2 pi, and integrating it gives back m_b = m_{b_0} exp(-2 pi (b - b_0)). Short waves contract at rate 1/(2b); waves longer than the correlation length dilate at the rate of the beta function.
- *U(1) test.* Compact U(1) in d = 4 has a gap at small b and none at large b, so (T) must fail there. It fails at the transition near b = 1, where no continuous transport exists. The proof of (T) must therefore contain a step that excludes a transition; the group enters in that step and nowhere else. For non-compact U(1) the Gaussian formula holds and gamma = 0 on both sides: no contradiction.
- *Known answers.* d = 2: the plaquette variables are independent and the map acts on each by a monotone rearrangement of the class angle; its derivative is bounded for all b. U(1) in d = 3: m ~ exp(-c b), the same form, so (T) should hold; this is a case where (T) can be tested on a theorem (Gopfert-Mack, memory). Finite groups: no smooth structure; not applicable. Small torus: true with c depending on the volume.
- *How it dies.* The second derivative of the Poisson equation is (L_b + b Hess A (x) 1 + 1 (x) b Hess A + Ric) Hess phi = Hess A - b (grad^3 A)(grad phi). The source b grad^3 A . grad phi is the cubic vertex contracted with the field; it has no sign, and the inverse on the left is infrared-singular. On a field that is constant of size |A| over a region of side R the correction is of order R |A| / b, which is not bounded over all U. So (T) with a supremum over all U is probably false, and the typical-U form needs a transport theory with exceptional sets, in infinite dimension. That is the same large-field problem as in the existence proof, moved to the infrared.

**B2. A strip in the complex coupling plane, and the two-constants theorem (way III).**

- *Mechanism.* Let F(b) be a truncated correlation of two local observables at distance R on Lambda. It is a ratio of entire functions of b. Suppose that it is analytic and bounded by M, uniformly in Lambda and R, in the strip D = {|Im b| < w}. For |b| <= b_0 the strong-coupling expansion converges also at complex b and gives |F| <= M exp(-m_0 R). The two-constants theorem gives |F(b)| <= M exp(-m_0 R omega(b)) in D, where omega is the harmonic measure of the disc |b| <= b_0 seen from b. In a strip of half-width w, omega(b) = C exp(-pi b/(2w)) (1 + o(1)) on the real axis. So m(b) >= C m_0 exp(-pi b/(2w)).
- *The law of asymptotic freedom comes out of the geometry of the strip.* The rate pi/(2w) equals c_AF when w = pi/(2 c_AF) = 11/(6 pi) = 0.58. The same w comes from the other side: if m(b) = C exp(-c_AF b) continues to complex b, then m(b + i theta) has argument -c_AF theta, and the decay exp(-m R) is lost when c_AF |theta| = pi/2.
- **CRUX (S).** There are w > 0 and M such that for every torus Lambda, every b with |Im b| < w, and local observables F, G with |F|, |G| <= 1: Z_Lambda(b) is not zero and |mu_b(F G) - mu_b(F) mu_b(G)| <= M. A weaker form with a horn, |Im b| < w(Re b) with w decreasing, still gives (W-lat) at each fixed b, with a rate below exp(-c b).
- *Why it could be true.* In the spherical sigma model in d = 2 it is true and sharp: m_b^2 = 32 exp(-4 pi b) is entire, the propagator 1/(k^2 + m_b^2) is singular only when m_b^2 is real and negative, that is at |Im b| = 1/4, and pi/(2w) = 2 pi is the exact rate. In d = 2 gauge theory Z = (2 I_1(b)/b)^{|P|}, whose zeros are on the imaginary axis. In the continuum, a change of b is a change of scale, and analyticity under complex dilations x -> e^{i phi} x, |phi| < pi/2, follows from the spectral condition for the two-point function.
- *U(1) test.* Compact U(1) in d = 4 has a transition at real b near 1: zeros of Z_Lambda approach the real axis and cut the strip. A proof of (S) must show that no zeros come near the real axis. No line is known where the group enters.
- *Known answers.* For the heat-kernel weight the natural domain is the half-plane Re t > 0, t = g^2. If the functions were bounded there, the harmonic measure would give m >= c t, a power of g. By A.1 this is false. So zeros must enter the half-plane and leave only a horn |Im t| < w |t|^2, which is the strip in b = 1/t. The test confirms the shape and shows that the strip cannot be widened to a sector.
- *How it dies.* At complex b the weight is not positive, reflection positivity is lost, and no lower bound on |Z_Lambda(b)| is known except by a convergent expansion. Lee-Yang theorems exist for a complex field, not for a complex temperature, and not for a four-link interaction. Perturbation of the transfer operator in theta is extensive in the spatial volume. The stability theory of gapped systems gives a neighbourhood of the real axis only where the gap is already known, and its width shrinks with the gap. So (S) has the same content as the gap and no handle of its own. Its value is as a target shape: it says that the right object is analytic in b in a strip of width fixed by b_0, and it gives a test for any other approach.

**B3. Centre flux (way I, with a hope of way II). The free energy of a twist on a torus of side l is a running quantity that is constant for U(1) and decreases for SU(2).**

- *Mechanism.* Z_n(l) is the partition function on the 4-torus of side l with 't Hooft twist n_{34} = 1, f_m(l) = -log(Z_n/Z_0) >= 0, and e^{-f_e} = (Z_0 - Z_n)/(Z_0 + Z_n) = tanh(f_m/2). Three views of the same number: Z_n = Tr(V e^{-l H}) with V the centre operator (time along 3 or 4), Z_n = Tr e^{-l H^m} on the space with magnetic flux (time along 1 or 2). Confinement of a loop of area A follows from f_e (Tomboulis and Yaffe, memory): <W(C)> <= 2 (e^{-f_e})^{A/(l_3 l_4)} roughly, from chessboard estimates. So an area law follows from f_m(l) <= C exp(-sigma l^2).
- **CRUX (F).** A recursion from an exact inequality: there are eps_0 > 0 and a function Phi with Phi(x) <= x^2/eps_0, such that f_m(2l) <= Phi(f_m(l)) for every l. Then f_m(l_0) < eps_0 at one scale gives f_m(2^k l_0) <= eps_0 (f_m(l_0)/eps_0)^{2^k}. This is not yet the area law (it needs 4^k), and a gap needs one more step; it is the first statement to aim at.
- *Why it could be true.* At small l the twisted sector has no flat directions (the twist-eating pair i sigma_1, i sigma_2 is isolated), and the untwisted sector has four. Each flat direction gives a factor 1/g. So f_m(l) = 4 log(1/g(l)) + O(1), which decreases as l grows, at the rate -4 b_0 g(l)^2 per unit of log l. For U(1), f_m = 2 pi^2/e^2 at every l. So the direction of the flow of f_m is the sign of b_0, and a proof that f_m keeps decreasing uses the group at this place.
- *U(1) test.* f_m is constant in the Coulomb phase; (F) is consistent only if eps_0 < 2 pi^2/e_c^2. The recursion cannot be an identity of reflection positivity alone, because every such identity holds for U(1) with f_m constant; this fixes the shape Phi(x) = o(x) at 0 and forbids Phi(x) <= x - delta.
- *Known answers.* d = 2: Z_n/Z_0 is explicit and tends to 1 exponentially in the area. Strong coupling: f_m ~ exp(-sigma l^2) (Munster, memory). Z_2 at large b: f_m ~ b l^2 grows; there is a gap and no confinement. So (F) is a route to confinement, and the gap needs a separate argument that the confined phase has no massless mode.
- *How it dies.* The exact tools give only one direction. log Z_0 and log Z_n are convex in each side length (traces of powers of a positive operator), so the flux energies are concave in the length: at most linear growth. Chessboard estimates bound a part of a twist sheet by the whole sheet on the same torus, not a large torus by a small one. No inequality in the needed direction is known; the attempt of Tomboulis (2007, memory) put a Migdal-Kadanoff recursion in this place and its key inequality was not proved. And the criterion f_m < eps_0 is not reached in the perturbative regime: f_m ~ 4 log(1/g) is large there.

**B4. Curvature after renormalization: a multiscale Bakry-Emery criterion (way I).**

- *Mechanism.* A single-scale curvature bound Ric + b Hess A >= K > 0 holds only at small b: the plaquette is not an affine function of the links, and its Hessian has an indefinite part of size b theta_p, about sqrt(b) on typical fields, against Ric = O(1). The multiscale form asks for convexity only of the renormalized potential V_s at scale s, measured in the metric of the fluctuation covariance of that scale: if Hess V_s >= lambda'(s) in that metric, the log-Sobolev constant is at most int_0^infinity exp(-2 lambda(s)) ds (the Polchinski-flow criterion, memory). The deficit lambda' may be negative on a bounded range of scales.
- **CRUX (C).** For the Wilson measure there is a scale decomposition (block averaging on the lattice, gauge covariant) such that the renormalized action V_s on gauge orbits has Hess V_s >= lambda'(s) with int exp(-2 lambda(s)) ds < infinity uniformly in the volume. In words: beyond the correlation length the effective action is uniformly convex in block variables.
- *Why it could be true.* It is what strong coupling at the block scale means: nearly independent block variables on a space of positive curvature. The criterion needs lower bounds only, no expansion.
- *U(1) test.* For the massless Gaussian lambda' -> 0 and the integral diverges. The proof must produce lambda' >= const > 0 at large scales; for SU(2) this can only come from Ric > 0 on the orbit space of block variables together with disorder of the block field.
- *Known answers.* Strong coupling: s = 0 suffices. d = 2: block variables independent. Finite groups: not applicable. The constraint A.1 is met, because the perturbative scales contribute exp(+2c int g_s^2 ds) and the number of such scales is of order b.
- *How it dies.* The Hessian of V_s obeys a Riccati inequality whose quadratic term makes negative curvature more negative: a bound Hess >= -K survives only while the integrated covariance is below 1/K. So semi-convexity of the bare action is lost before the scales where convexity is needed, and V_s at coupling one is not known in any form.

**B5. The ground-state measure (way I; a different object).**

- *Mechanism.* Take the Hamiltonian limit in the time direction: H = (g^2/2) sum_l E_l^2 + (1/g^2) sum_p a_p on L^2 of the spatial links. Its ground state Omega is positive. In the representation L^2(Omega^2 dU) the operator H - E_0 is the Dirichlet form (g^2/2) int |grad f|^2 d mu_0 with mu_0 = Omega^2 dU. So the mass gap is exactly (g^2/2) times the Poincare constant of the three-dimensional measure mu_0. The gap becomes a statement of three-dimensional statistical mechanics.
- **CRUX (G).** W = -log Omega^2 is uniformly convex on gauge orbits in the Bakry-Emery sense, Hess W + Ric >= 2m/g^2, or, weaker, mu_0 has a Poincare inequality uniform in the volume. The equation for W is a stationary Hamilton-Jacobi equation with viscosity g^2, and convexity estimates for it come from a maximum principle (Brascamp-Lieb; the proofs of the fundamental gap conjecture, memory).
- *Why it could be true.* Free massive field: W = (phi, sqrt(-Delta + m^2) phi), Hess W >= m, and the criterion is sharp.
- *U(1) test.* Free photon: Hess W = sqrt(-Delta) on transverse fields, lowest value 2 pi/l on a torus of side l, which tends to zero. For SU(2) the gain must come from the quartic part of the potential and from Ric > 0.
- *Known answers.* Small torus: the constant modes have V = |c_i x c_j|^2, which is not convex; the ground state behaves like exp(-|x| y^2/2) along a valley, and its Hessian is indefinite of size |y| there. So pointwise convexity of W is already false in the one case where the gap is known. Only a Poincare inequality by a Lyapunov argument survives, and that is not uniform in the dimension.
- *How it dies.* W is non-local, with kernel sqrt(-Delta) at short distance, and it is known only through Omega. A maximum principle in infinitely many variables with a non-convex potential gives nothing. By A.1 the convexity constant is exp(-c/g^2), which no local estimate produces.

**B6. A finite-size criterion on the unit lattice, and the conditional theorem (way II).**

- *Mechanism.* A lattice gauge measure is a Markov field with compact fibres and range one. For such fields there is a constructive criterion (Dobrushin and Shlosman, memory): if, in one cube Q of side R, the law of the inner half of Q depends on the boundary condition by at most delta in total variation, uniformly in the boundary condition, and delta is below a constant of the dimension, then the Gibbs state is unique and clusters exponentially at rate c/R. Gauge invariance costs nothing: two boundary conditions that differ by a gauge transformation give the same law on the inner half, because the transformation extends by the identity.
- **CRUX (D).** For the effective measures of A.1 at beta_*, there is R with delta(R) < delta_4. The conditional theorem is: the account, plus (D) at one R, give (GAP).
- *Why it could be true.* If the gap is true with strong mixing in cubes, (D) holds for R of order xi log xi. It is a statement about finitely many integrals over SU(2).
- *U(1) test.* In the Coulomb phase the centre of a cube feels the boundary through the harmonic extension; delta(R) does not tend to zero. The criterion fails, as it must.
- *Known answers.* Strong coupling: R = 1. Z_2 at large b: true, R of order one. Small torus: not applicable.
- *How it dies.* Two places. (i) R must exceed xi ~ exp(c beta_*), where nothing is small; (D) is the gap in finite form, not a reduction of difficulty. (ii) The supremum over all boundary conditions includes rough ones, on which no weak-coupling method works; a form with typical boundary conditions needs a new criterion with rare bad cubes.

**B7. A local-gap threshold for a frustration-free generator (way II), and a rule that every criterion of way II must obey.**

- *Mechanism.* The heat-bath generator of the four-dimensional measure, H = sum_l (1 - E_l) with E_l the conditional expectation at link l, is a sum of projections of range one that all annihilate the constants: it is frustration-free. For such sums there are finite-size theorems (Knabe; later sharper forms, memory): if the gap of the sum over one box of side n, on the full space, exceeds a threshold t(n) of order n^{-2}, the infinite sum has a gap. The box gap on the full space is the worst case over boundary conditions. A gap of H gives exponential clustering.
- **CRUX (K).** The sharp threshold equals the value of the massless Gaussian field, t(n) = 1 - cos(pi/(n+1)), and the box gap of the SU(2) measure at large b exceeds that value at some n.
- *U(1) test.* The massless Gaussian field has no gap and its box gap is exactly the Gaussian value, so the sharp threshold cannot be lower. Equality is the first half of (K). The second half is where the group would enter, as the sign of a one-loop correction.
- *How it dies: by A.1.* If the criterion held at a perturbative n with margin delta, the known proofs would give a gap of order delta n^{-2}, a power of 1/b. The truth is exp(-c b). So (K) is false for SU(2): the worst boundary condition keeps the box gap at or below the Gaussian value. The quantum form, with H the Hamiltonian of B5, dies earlier: the Dirichlet form is frustration-free but not of finite range (kernel sqrt(-Delta)), and a gapless frustration-free sum of finite range has box gap O(n^{-2}), while a relativistic box gap is of order 1/n.
- **A rule for way II.** A finite-size criterion that is satisfied at a perturbative scale with margin delta ~ g^2 is consistent with A.1 only if its conclusion is a gap of order exp(-C/delta). So its proof must be an induction over scales in which a dimensionless quantity moves by an amount of order delta^2 per doubling. The only possible form of way II is therefore **(RGI): an exact inequality q(2l) >= q(l) + c q(l)^2 for a non-perturbative running coupling q(l), valid while q <= q_c, together with a criterion "q(l) >= q_c gives the gap".** For the flux quantity of B3, q = exp(-f_m/2) is proportional to g(l)^2 at small l and is constant for U(1). An exact proof of (RGI) would be the first proof that the infrared flow leaves weak coupling. No inequality of this kind is known to me.

**B8. Comparison with a model of lower dimension (way I).**

- *Mechanism.* Durhuus and Frohlich (1980, memory): a gauge theory in d dimensions is at most as ordered as the sigma model with values in G in d - 1 dimensions. The picture: freeze U_mu = 1 for mu >= 2; the links U_1 in each hyperplane x_1 = const then form a sigma model, the hyperplanes decouple, and a Wilson loop of size L x T is a product of L two-point functions at distance T. A mass m of the sigma model gives the area law with sigma >= m. So d = 3 gauge theory confines if the d = 2 sigma model has a gap. In d = 4 the comparison model is three-dimensional and orders at large b.
- **CRUX (DF2).** A comparison across two dimensions: for a model M_b in d = 2 with values in SU(2) = S^3 (the O(4) model, or a model built from it), <W(C)>_{4, b} <= C exp(-c m_2(b)^2 Area(C)). The Migdal-Kadanoff recursion of the d = 4 gauge theory is the recursion of the d = 2 sigma model, which is the reason to look for it.
- *Why it could be true.* The exponents allow it: sigma_4 ~ exp(-2 c_AF b) = exp(-5.38 b), and for O(4) at the same b, m_2^2 ~ exp(-2 pi b) = exp(-6.28 b), which is smaller.
- *U(1) test.* Passed without any use of the group: d = 4 U(1) against the d = 2 rotator, which has the Kosterlitz-Thouless phase at large b. Z_2: d = 4 Z_2 gauge theory against the d = 2 Ising model, ordered at large b. The comparison is true in every known case.
- *How it dies.* (i) Freezing raises order, so it can remove one dimension at the price of comparing with a more ordered model; nothing lowers the dimension by two. With two directions frozen the model has plaquette interactions in the mixed planes only and a symmetry on each plane, and the exponents then go the wrong way. (ii) The gap of the d = 2 O(4) model is open as well. So (DF2) would reduce one open problem to another; it would still be a new theorem.

**B9. Homotopy in a field with a Lee-Yang property (way III).**

- *Mechanism.* Add a Higgs field in the fundamental representation of fixed length. In the unitary gauge the weight is exp(-b A(U) + kappa sum_l (1/2) tr U_l): a field kappa coupled to the first component of the unit 4-vector on each link. At large kappa every link is pinned and the theory has a gap. If Z_Lambda(kappa) had no zero in Re kappa > 0 (a Lee-Yang property), the two-constants theorem would give exponential clustering for every kappa > 0 and every b.
- **CRUX (LY).** Z_Lambda(b, kappa) is not zero for Re kappa > 0, for every b >= 0 and every Lambda. On one link it is true: int exp(kappa s_0) d sigma(s) over S^3 is 2 I_1(kappa)/kappa, whose zeros are imaginary.
- *U(1) test.* For U(1) with a charge-one Higgs field the same statement would give a gap for all kappa > 0, which is the expected truth there too. The limit kappa -> 0 is where U(1) and SU(2) part: the rate from the harmonic measure tends to zero, as it must for U(1).
- *How it dies.* The Lee-Yang theorems for vector spins need pair interactions that are ferromagnetic, and at most three components (memory); the plaquette is a four-body term and S^3 has four components. And the result would stop at kappa > 0: the pure theory is on the boundary of the half-plane. The result short of the gap would be new: a gap in the whole Higgs-confinement region.

**B10. A small circle with the centre kept symmetric: the gap by the monopole mechanism, then continuity in the size (another order of limits).**

- *Mechanism.* On R^3 x S^1 of length l much below the confinement scale the coupling g(l) is small. If the centre symmetry is kept (by twisted boundary conditions or by a term in the Polyakov loop), the holonomy around the circle acts as an adjoint Higgs field with a non-degenerate value, SU(2) breaks to U(1), the charged components have mass pi/l, and the long-distance theory is compact U(1) in three dimensions with a dilute gas of monopole-instantons of action 4 pi^2/g^2. Row 5 of the table in A.2 then gives a gap m ~ l^{-1} exp(-2 pi^2/g(l)^2), by screening in a Coulomb gas. Every step has a rigorous precedent (ultraviolet stability, the Higgs mechanism on a lattice, the three-dimensional Coulomb gas).
- **CRUX (AC).** The gap m(l) of the centre-symmetric theory on R^3 x S^1_l stays positive as l grows to infinity, and the stabilizing term can be removed at large l. This is continuity in l through the region where g(l) is of order one.
- *U(1) test.* For U(1) on R^3 x S^1 there are no monopole-instantons made by the holonomy, and the photon stays massless. The group enters as pi_2(SU(2)/U(1)) = Z, the existence of the monopole.
- *Known answers.* It reproduces row 5 (the gap of compact U(1) in d = 3) and row 8 (no gap with an adjoint Higgs field in d = 4, where the monopoles are particles, not instantons).
- *How it dies.* (AC) is the wall. Without the stabilizing term the small circle is the high-temperature phase, the centre is broken, and the spatial gap needs the gap of three-dimensional Yang-Mills theory, which is open. The result short of the gap: a mass gap, by a controlled mechanism, in a four-dimensional non-abelian gauge theory at weak coupling on R^3 x S^1.

**B11. The small torus: hypercontractivity (the result short of the gap that is closest).**

- *Mechanism.* On T^3_l x R the transfer semigroup in the ground-state representation is positivity preserving. A semigroup that is hypercontractive and positivity improving has an isolated simple lowest eigenvalue (Gross; Simon and Hoegh-Krohn; a quantitative form by Aida, memory). The physical reason for the gap is row 7 of A.2.
- **CRUX (HC).** A defective logarithmic Sobolev inequality for the lattice Hamiltonian on T^3_l in its ground-state representation, with constants uniform in the lattice spacing, and a uniform positivity-improving bound. Then (W-tor): m(l) > 0 uniformly in the cutoff.
- *U(1) test.* Not a test: on a torus U(1) has a gap 2 pi/l as well. The approach says nothing about l -> infinity; it is listed because it is the nearest new theorem.
- *How it dies.* The time-zero fields of a four-dimensional gauge theory are too singular for a time-zero measure in the continuum; the inequality must be formulated on slabs, and its uniformity is a problem of the size of the existence proof.

**B12. The renormalization group continued to strong coupling (the specialist's first item; no weight).** CRUX: one block step at effective coupling of order one maps a neighbourhood of the effective actions into itself and increases the effective coupling. U(1) test: the sign of b_0. It dies because nothing is small: no norm is known in which the map is controlled between the last perturbative scale and the first scale where a strong-coupling expansion converges. B4 and (RGI) of B7 are its two inequality forms.

**B13. Loop equations with positivity (way I).** The Schwinger-Dyson equations of the Wilson loops and reflection positivity define a convex set that contains every invariant Gibbs state at b. CRUX: every point of this set satisfies an area-law bound. At small b the loop equation is a contraction and gives it. U(1) test: the abelian loop equations have the Coulomb solution, so the non-abelian trace identities of SU(2) must be used. It dies because decay is not a closed convex condition and the equations are not contractive at large b.

**Summary of 1.B.** Thirteen mechanisms. Each of them, except B11, ends at the same place: uniform control of the measure on the compact interval of couplings between the strong-coupling region and the region of the existence account, or equivalently on the finite range of scales between the unit and exp(c/g^2). They differ in the form of the statement that is needed there: a one-sided Hessian bound (B1, B4, B5), a zero-free strip (B2, B9), a recursion for one number (B3, B7), one finite-volume inequality (B6), a comparison (B8, B13), a continuity statement (B10).

### 1.C The choice, and the duplicate check

**Judgement.** No approach in 1.B has a step that crosses the wall of A.4 by a known method. I say this plainly. The choice below is therefore a choice of the form in which the wall is attacked, and it is made by four tests: the crux is a one-sided inequality and not a smallness condition; the rest of the chain is exact; the crux is true in the solvable cases; the approach can produce exp(-c b).

1. **Chosen: B1, transport along the coupling, crux (T).** It is the only approach whose crux is a one-sided bound on one explicit function, the solution phi_b of a Poisson equation, in finite volume, on a compact interval of couplings [b_0, beta_*]. It gives the law exp(-c b) from a bounded quantity. It holds in the Gaussian model without a gap and in the spherical model with the exact rate. Its failure has a meaning: a point of the coupling axis where no Lipschitz transport exists is a phase transition.
2. **Second, failing in a different way: B3 with the rule of B7, crux (RGI).** One number per scale, the centre-flux free energy, and a recursion. It fails for lack of an inequality in the right direction, not for lack of control of a function on the whole configuration space.
3. **Third, attacked if the first two leave room: B2, crux (S).** It shares the path in the coupling with B1 and fails by loss of positivity.

Not attacked: B6 (its crux is the gap in finite form; it enters the skeleton of Part 3 as the conditional theorem), B11 (see the duplicate check), B10 (its own first theorem is a construction of the size of the existence proof).

**Duplicate check (rule 0a), made before the attacks.** Searched for: transport, trivializ, Poisson, twist, vortex, flux, strip, two-constants, Fisher, Lee-Yang, Dobrushin, Knabe, hypercontract, Tomboulis, Durhuus, weak mixing, Hellmann, log-Sobolev, Bakry, Polchinski, mass gap, spectral gap, transfer, in `FINISH.md` (row numbers only) and `library/open-core.md`.

- `library/open-core.md`: no entry on the gap (one unrelated use of the word).
- Rows 667 `gap-transfer` and 668 `gap-os-equiv` are proof items. By their first lines, 667 is the transfer operator on a fixed finite lattice and 668 is the interface between decay and spectrum with the passage to the limit. They match B11's base and the Euclidean form of Part 0.4. **Neither is attacked here.** Rows 671 and 672 are their checks.
- Rows 655, 656, 661 are reading rows; their digests are the input of Part 2 and were not opened before this point. Row 662 is closed to this run. Row 670 is the independent second author; its row and its file were not opened.
- No row and no entry covers (T), (RGI) or (S). The attacks go ahead.

### 1.D Attack on the crux (T)

**D.1 The exact frame (proved here; these are not the crux).** X is a compact Riemannian manifold, A is smooth, mu_b = Z_b^{-1} e^{-bA} vol, L_b = -Delta + b <grad A, grad .>, so int f L_b g d mu_b = int <grad f, grad g> d mu_b. gamma(b) is the lowest non-zero eigenvalue, f_b an eigenfunction with mu_b(f_b) = 0, and phi_b the solution of L_b phi_b = A - mu_b(A) with mean zero.

*Lemma 1 (transport).* Let Z_t = -grad phi_t and let Phi_{s,t} be its flow. Then (Phi_{s,t})_* mu_s = mu_t. If Hess phi_t >= -c on X for s <= t <= b, then gamma(b) >= gamma(s) exp(-2c(b - s)).
Proof. For smooth f, d/dt mu_t(f) = -Cov_t(f, A) = -int f L_t phi_t d mu_t = int <grad f, Z_t> d mu_t. The image measure satisfies the same continuity equation with the same initial value, and the solution is unique for a smooth field on a compact manifold. For a tangent vector v carried by the flow, d/dt |v|^2 = 2 <grad_v Z_t, v> = -2 Hess phi_t(v, v) <= 2c |v|^2, so |D Phi_{s,b}| <= e^{c(b-s)}. Then Var_b(f) = Var_s(f o Phi) <= gamma(s)^{-1} int |grad (f o Phi)|^2 d mu_s <= gamma(s)^{-1} e^{2c(b-s)} int |grad f|^2 d mu_b. The same holds on gauge-invariant functions, because phi_t is invariant and the flow commutes with the gauge group. QED

*Lemma 2 (four forms of the derivative of the gap).* At every b where gamma is differentiable (almost every b; gamma is a minimum of smooth Rayleigh quotients), with f = f_b and < . > = mu_b:

- (HF1) gamma' = 2 <Hess phi_b(grad f, grad f)> / <f^2>.
- (HF2) gamma' = (1/2) <f^2 L_b A> / <f^2>, where L_b A = b |grad A|^2 - Delta A has mean zero.
- (HF3) gamma' = <f <grad f, grad A>> / <f^2> = -(1/2) (d/dt)|_{t=0} <(f o W_t)^2> / <f^2>, where W_t is the gradient flow of A (the Wilson flow).
- (HF4) b gamma' = gamma - <f (-Delta) f> / <f^2>.

Proof. The derivative of the Rayleigh quotient at fixed f is [-Cov(|grad f|^2, A) + gamma Cov(f^2, A)] / <f^2>. With Cov(g, A) = <grad g, grad phi>, the bracket is -2 <Hess f(grad f, grad phi)> + 2 gamma <f <grad f, grad phi>>, and gamma <f <grad f, grad phi>> = <L f <grad f, grad phi>> = <Hess f(grad f, grad phi)> + <Hess phi(grad f, grad f)>. This is (HF1). For (HF2) use |grad f|^2 = gamma f^2 - (1/2) L(f^2), so <|grad f|^2 A> = gamma <f^2 A> - (1/2) <f^2 L A>, and <|grad f|^2> = gamma <f^2>. (HF3): <f^2 L A> = <grad f^2, grad A>, and d/dt (f o W_t) = -<grad f, grad A> at t = 0. (HF4): integrate (HF3) by parts against vol: <grad f^2, grad A> = (1/b) <Delta f^2> = (2/b)(<|grad f|^2> + <f Delta f>). QED

Check on the Gaussian model: f is linear, Delta f = 0, and (HF4) gives b gamma' = gamma, which is right (gamma = b lambda).

*Corollary (the exact content of the crux).* gamma(b) >= gamma(b_0) e^{-2c(b-b_0)} on an interval if and only if, for almost every b in it,

**(T-avg)** <Hess phi_b(grad f_b, grad f_b)> >= -c <|grad f_b|^2>; equivalently (d/dt)|_{t=0} <(f_b o W_t)^2> <= 4c <|grad f_b|^2>; equivalently <f_b (-Delta) f_b> <= (1 + 2cb) <|grad f_b|^2>.

In words: the L^2(mu_b) norm of the gap mode may grow under the Wilson flow at most at the rate 4c times its Dirichlet energy. For the Wilson action Delta A = 3 sum_p (1 - a_p) and |grad_l A|^2 = (rho_l^2 sin^2 theta_l)/4, where the staple sum at l times U_l is rho_l (cos theta_l + i sin theta_l n.sigma); so (HF2) is explicit.

**D.2 Tests of (T).** (i) Gaussian: Hess phi = P/(2b) >= 0 (1.B). (ii) Spherical model: holds with c = 2 pi (1.B). (iii) One plaquette, class angle alpha: psi = phi' = (4/rho) int_alpha^pi rho (A - <A>), rho = sin^2 alpha e^{b cos alpha}; near alpha = 0, Hess phi = 1/(2b); near the antipode alpha = pi all eigenvalues tend to -(2 - <A>)/3. So (T) holds with c about 2/3, and the negative part sits at the cut locus U_p = -1. (iv) A remark on the object. gamma is a stronger object than the mass. For compact U(1) in d = 2 the correlation length is zero, but the trial function f = sum_p chi(p) h(F_p), with chi a bump of width n and h(F) = F away from the cut F = pi, has Rayleigh quotient at most C b (n^{-2} + e^{-2b}): the flux through a region changes only through its boundary or through a plaquette that passes -1. So gamma <= C b e^{-2b} there. For SU(2) in d = 2 there is no additive gauge-invariant flux beyond area b, and no such mode. A lower bound on gamma is sufficient for clustering and far from necessary.

**D.3 The pointwise form of (T) fails for the product transport in a solvable model.** Model: sites x = 0..L, theta in R^{L+1}, increments eta_x = theta_{x+1} - theta_x, A = sum_x W(eta_x), W even and smooth. It has the structure of a gauge theory in d = 2: the invariant functions are the functions of eta = d theta, and the eta_x are independent. The natural transport from b to b' acts on each increment by the monotone map T that carries the one-increment law at b to that at b', and theta'_x = theta_0 + sum_{y<x} T(eta_y).

*Lemma 3.* Put t_y = T'(eta_y) and d_y = t_y - t_{y-1}. For the tangent vector v with v_y = d_y for 1 <= y <= R and v_y = 0 otherwise, (D Theta v)_x = t_{x-1} d_x - sum_{y<x} d_y^2 for x <= R and (D Theta v)_x = -S_R for x > R, with S_R = sum_{y<=R} d_y^2. Hence, modulo constants, |D Theta v|^2 >= sum_{x<=R} (S_R - S_x - |t d_x|)^2 while |v|^2 = S_R. For independent eta_y and non-affine T, S_x = delta^2 x (1 + o(1)) with delta^2 = 2 Var T'(eta) > 0, so |D Theta| >= c delta R, which is unbounded as R <= L grows.
Proof. Summation by parts: sum_{y<x} t_y (v_{y+1} - v_y) = t_{x-1} v_x - sum_{1<=y<x} (t_y - t_{y-1}) v_y. QED

So the Lipschitz constant of this transport grows like L delta on typical fields: a rough multiplier does not commute with the inverse of d. In the metric of the increments the same map is Lipschitz with constant sup T'. The loss is the passage from the field strength to the potential. For W = 1 - cos at large b, delta is of order 1/b.

*The maximum principle also fails.* Let u = Hess phi(v, v) be minimal at (x_0, v_0), with value lambda. Differentiating the Poisson equation twice and using Delta u >= 0, grad u = 0 at the minimum gives 2 b lambda Hess A(v_0, v_0) >= Hess A(v_0, v_0) - b (grad^3 A)(grad phi, v_0, v_0) + (curvature terms). This bounds lambda from below only if Hess A(v_0, v_0) is positive and not small. On long waves Hess A is of order k^2, on gauge directions it is zero, and on fields away from the minimum it has no sign. The inequality gives nothing there.

**D.4 Verdict on (T).** (a) The frame is exact: Lemma 1, Lemma 2. (b) The pointwise form of (T) is refuted for the product transport in the solvable model (Lemma 3), and no argument gives it for the gradient transport; the maximum principle fails at the soft directions. I do not claim a counterexample for the gradient transport. (c) The form that is necessary and sufficient is (T-avg). It involves the gap mode f_b itself. It is true in the solvable model with c of order 1/b (there gamma_L(b) is the diffusion constant 1/Var_b(eta) times (2 pi/L)^2). It says that the long-wave mode sees only an average of Hess phi; a proof would be a homogenization statement for the pair (phi_b, f_b), and no method gives that on the interval of couplings where it is needed. (d) So the attack ends with a sharper statement and not with a handle: **(T-avg) is the statement "the gap does not close faster than exponentially in b" in differential form.** Its use is as an a priori estimate in a continuity argument: the set of b with a uniform gap is open, and (T-avg) with a constant that does not depend on the gap would close it. What is missing is any bound of <f (-Delta) f> by b <|grad f|^2> that does not use the size of gamma.

### 1.E Attack on the crux (RGI)

**E.1 The exact frame.** Torus of sides (l_1, l_2; l_3, l_4), twist n_{34} = 1, Z_0 and Z_n the two partition functions, f_m = -log(Z_n/Z_0), r = (Z_0 - Z_n)/(Z_0 + Z_n) = tanh(f_m/2) = e^{-F_e}. Two representations, both from the transfer operator of the lattice theory, which is positive and self-adjoint:

- time along 1 (or 2): Z_0 = Tr T^{l_1} on the periodic space of the slice (2,3,4), Z_n = Tr T_m^{l_1} on the slice space with the twist in (3,4);
- time along 3 (or 4): Z_0 +- Z_n = 2 Tr_{even/odd} T^{l_3} on the slice (1,2,4), where even and odd refer to the centre operator V_4, which commutes with T.

For a positive trace-class operator S put R(S, l) = log((Tr S^l)^2 / Tr S^{2l}) >= 0, the Renyi entropy of order two of the state S^l / Tr S^l. It is zero if and only if S^l has rank one, and it is small when l times the gap of -log S is large.

*Lemma 4 (doubling identities).* (D-sheet) f_m(2 l_1) = 2 f_m(l_1) + R(T_m, l_1) - R(T, l_1). (D-plane) r(2 l_3) = r(l_3)^2 exp(R(T_even, l_3) - R(T_odd, l_3)). The same with 2 in place of 1 and 4 in place of 3.
Proof. Tr S^{2l} = (Tr S^l)^2 e^{-R(S,l)} for each of the four operators. QED

Consequences, all exact. (i) r(2 l_3) <= r(l_3)^2 e^{R(T_even, l_3)}: the electric flux free energy F_e is superadditive in the directions of its world sheet, up to an entropy. This is a recursion of the shape asked for in (F), f_m(2 l_3) <= (1/2) f_m(l_3)^2 e^{R} for small f_m. (ii) f_m(2 l_1) <= 2 f_m(l_1) + R(T_m, l_1): the magnetic free energy is subadditive in the directions of the vortex sheet, up to an entropy. (iii) For U(1) with the Gaussian (Villain) weight the classical parts satisfy both with equality and zero entropy difference: f = 2 pi^2 b n^2 l_1 l_2/(l_3 l_4).

**E.2 Symmetric doubling.** Double l_3, l_4, l_1, l_2 in turn. With r small, f = 2 artanh r is about 2r, and

f_m(2l) <= 4 f' + 2 R(T_m, l_1) + R(T_m', l_2), f' <= 2 r(l)^4 exp(2 R(T_even, l_3) + R(T_even', l_4)) (1 + o(1)),

where the primes mean the operators on the tori already doubled. So f_m(2l) <= 8 r(l)^4 e^{entropies} + (three entropies of twisted sectors). **If all the entropies were below a constant times f_m(l)^2, the recursion f_m(2l) <= C f_m(l)^2 would hold, and with it, by Tomboulis-Yaffe, the area law.** The entropies are small exactly when, on each torus of the chain, the side being doubled is long against the inverse gap of the transfer operator across it.

**E.3 Where it fails.** In the scaling region below the correlation length the gap of every slice operator is of order 1/l, the entropies are of order one (the Stefan-Boltzmann value for free gluons is about 1.2 for a cubic slice), and the additive entropies in (ii) alone keep the bound on f_m(2l) of order one. The recursion closes only on tori that are already larger than the correlation length in every direction. Below it the identities are bookkeeping: all the dynamics is in the finite-size terms C = log Z + f_infinity |Lambda| of the tori, and reflection positivity gives only C(2 l_i) <= 2 C(l_i) and convexity in each l_i. For U(1) these terms are scale invariant and never small. So (RGI) is not obtained: the missing statement is an upper bound for R(T_m, l) - R(T, l), the change of the entropy of a slab of thickness l caused by a twist in two of its long directions, in terms of f_m at the same scale. In a phase with screening this difference is exponentially small; proving it is the gap again.

**E.4 What the attack found: thin tori.** The entropies can be made small without the gap by making tori thin. Take l_1 = l_2 = s with g(s) small, and l_3, l_4 long. Then the slice operators along 3 and 4 act on a system with two short directions, the reduced theory is two-dimensional, and a two-dimensional gauge theory confines by the Coulomb law. So on T^2_s x T^2_l the flux free energy has an area law with a tension of order g(s)^2/s^2 at tree level (in the untwisted case the light adjoint scalars made of the two holonomies do not screen a fundamental charge, but they make the reduced theory strongly coupled; the twisted case B14 has no light field). The step from two short directions to one short direction is the infrared problem of the three-dimensional theory (magnetic screening), and the step to none is the problem of this file. The cleanest member of the family has a twist in the short torus; it is added as B14.

**Verdict on (RGI).** Exact doubling identities (Lemma 4) give the recursion in the directions of the sheet and reduce everything to entropies of slabs. No inequality bounds these entropies below the correlation length, and U(1) shows that none can follow from positivity alone. The attack fails at one named place: an upper bound on R(T_m, l) - R(T, l).

**B14 (added to 1.B during the attack; own thinking, the physics is recalled from memory). The thin torus with a twist: a family in which every member is gapped at tree level at one end.**

- *Mechanism.* Put the theory on R^2 x T^2_s with 't Hooft twist n_{12} = 1 in the small torus. The transition functions i sigma_1, i sigma_2 leave no constant mode: every component of the gauge field is antiperiodic in at least one short direction. All modes have mass at least pi/s at tree level. The gauge symmetry is broken to the centre by the boundary condition, and no Higgs field is used. When g(s) is small the theory is a weakly coupled massive theory in two dimensions with a Z_2 gauge symmetry. Its Wilson loops in R^2 have an area law from a dilute gas of centre vortices (fractional instantons of action 4 pi^2/g^2), with sigma ~ s^{-2} exp(-4 pi^2/g(s)^2). The gap is m(s) >= c/s.
- **CRUX (AC').** inf over s of m(s) is positive, where m(s) is the gap on R^2 x T^2_s with the twist. For s below the unit of length the gap is a weak-coupling theorem to prove, (W-twist); for s large it is (GAP) up to finite-size terms; the content is the range of s where g(s) is of order one.
- *U(1) test.* Passed at the first line: a pair of non-commuting transition functions does not exist in U(1). There the twist is a constant flux, the photon is neutral and stays massless.
- *Known answers.* It is the small-torus row of A.2 without its defect: there are no flat valleys, so the gap is c/s and not g^{2/3}/s, and two directions are infinite. Adjoint Higgs test: the twist gives the same masses with the field present; the test applies only at large s, where the crux is.
- *How it dies.* At (AC'), the wall. But (W-twist) is a theorem within reach of the method of the existence account plus a cluster expansion for a massive field and a dilute gas: a mass gap and an area law, at weak coupling, with two infinite directions, uniformly in the cutoff.

### 1.F Attack on the crux (AC') of B14

Setting: T_s is the theory on R^2 x T^2_s with the twist, at a fixed lattice spacing or in the continuum; m(s) is its gap and sigma(s) its string tension for loops in R^2. For each s it is a two-dimensional reflection-positive system whose "spin" at a point of R^2 is the field on the fibre T^2_s.

**F.1 What is exact.**

*Lemma 5 (in this family a gap gives the area law).* The twist operator tau(x), which inserts the twist n_{34} at a point x of R^2, is a positive local observable with e^{-2 b |S|} <= tau <= e^{2 b |S|}, |S| the number of plaquettes of the fibre. Hence f_m(L_3, L_4; s) = -log <tau> <= 2 b |S| for all L_3, L_4, and F_e = -log tanh(f_m/2) >= F_0(b, s) > 0, uniformly in the size of the large torus. With (D-plane) of Lemma 4: F_e(2 L_3) >= 2 F_e(L_3) - R(T_even, L_3). If the slice operator on T^2_s x S^1_{L_4} has a gap m in its even sector, uniformly in L_4, then R(T_even, L_3) <= C L_4 e^{-m L_3}, and iterating from L_0 = C' m^{-1} log(1/F_0) in both directions gives F_e >= sigma L_3 L_4 with sigma >= c F_0 / L_0^2. By the Tomboulis-Yaffe inequality this is the area law. So in the family, confinement is not a second problem: it follows from the gap by positivity. (The hypothesis "uniformly in L_4" is a finite-size statement that a constructive proof of the gap gives; it is not automatic.)

*The untwisted family must have a transition.* Without the twist the centre symmetry of the short cycles is broken at small s (the holonomies sit at +-1) and unbroken at large s. So the untwisted thin torus has a critical point at s of the order of the correlation length, and no statement like (AC') holds for it. With the twist the holonomies are frozen at i sigma_1, i sigma_2, where tr P = 0: the centre symmetry is unbroken at both ends. This is the reason to choose the twist.

*Small s (memory of the one-loop law).* sigma(s) ~ s^{-2} exp(-4 pi^2/g(s)^2) = Lambda^2 (s Lambda)^{5/3}, because 4 pi^2/g(s)^2 = (11/3) log(1/(s Lambda)) for N = 2. So sigma increases with s from zero and, extended to s ~ 1/Lambda, is of order Lambda^2; m(s) decreases from pi/s.

**F.2 What was tried for the continuity itself.**

1. *Monotonicity of m(s) or of s m(s).* Reflection positivity gives concavity of ground-state energies in a side length (1.B, B3), not monotonicity of a gap. For periodic or twisted boundary conditions there is no domain monotonicity.
2. *The c-theorem in two dimensions.* For fixed s the c-function is monotone in the distance r. It relates nothing at different s, and its ultraviolet value is infinite (the theory is four-dimensional at r << s).
3. *Derivative in s.* By dimensional analysis d log(s m)/d log s is the derivative in the coupling, which by (HF) of 1.D is a one-particle matrix element of the action density. No sign, no bound.
4. *Doubling s.* A field on T^2_s with the twist is a field on T^2_{2s} without twist that is invariant under the half-translations combined with the colour rotations by i sigma_1, i sigma_2. So T_s is a symmetric sector of the untwisted theory at 2s. Positivity gives no inequality between a sector and the whole.
5. *A general theorem for two-dimensional systems with compact fibre and range one.* Uniqueness holds at high temperature only. A continuous symmetry gives power-law bounds, not a gap.

**Verdict on (AC').** One exact gain: in the family the area law follows from the gap (Lemma 5), so there is one crux and not two. The continuity itself is not touched by any exact tool. It fails at the same place as (T) and (RGI): the range of s where g(s) is of order one.

### 1.G The choice after the attacks

The attacks changed the order of 1.C.

- (T), pointwise, is false for the product transport in a solvable model, and (T-avg) is the conclusion in differential form. B1 keeps its exact identities and loses its handle.
- (RGI) is reduced by exact identities to entropies of slabs, and these are small only beyond the correlation length, or on thin tori.
- The thin torus with a twist, B14, came out of that reduction. It is the only approach in this file whose first node is a theorem that looks provable now, by a mechanism that uses the group at its first line, and whose family contains the target as a limit without a change of phase at either end.

**Final choice: B14.** Crux (AC'). Second approach, failing in a different way: B1 on the unit lattice, crux (T-avg), which fails for lack of an a priori estimate in the coupling and has no gapped member at weak coupling. The conditional theorem of B6 is kept as the fall-back form of the crux in finite volume. My judgement of 1.C stands: no approach here has a real chance at the crux with known methods; what the run gives is the exact form of the crux in three languages, the reductions that are exact, and one new theorem to prove short of the gap, (W-twist).

<!-- PART1-END -->

## Part 2. The literature, after Part 1

(pending)

## Part 3. The skeleton

(pending)

## Part 4. The queue

(pending)
