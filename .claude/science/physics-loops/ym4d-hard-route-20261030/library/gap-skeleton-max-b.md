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

## Part 1. My own thinking (written before any digest or paper on the gap was opened)

Everything in Part 1 is from my own reasoning and from memory. Where I recall a published result, I say "recalled". Part 2 checks the recalls. Nothing recalled is used as a proof step.

### 1.1 The cases where the answer is known

**(K1) Two dimensions, any compact group, U(1) included: gap.**
Exact reason: on a planar lattice the map from links (modulo gauge) to plaquette holonomies sends the Wilson measure to a product measure, prod_p w_beta(U_p) dU_p. Disjoint sets of plaquettes are independent, so the truncated correlations of local gauge-invariant functions vanish at separation above their size. In the Hamiltonian picture on a circle of length l, the state space is the class functions of one holonomy and H = (g^2 l / 2) C_2, with spectrum on the characters. The gap is g^2 l C_2(fundamental)/2.
What the reason uses: there is no Bianchi constraint in two dimensions, and the group is compact (the dual is discrete). It does not use non-commutativity: U(1) has the gap too.
What survives in four dimensions: only compactness of the group, as a gap of the one-link kinetic operator (g^2/2a)(-Delta_G). What is lost: independence of plaquettes. In four dimensions the plaquette variables are a product measure conditioned on the Bianchi identity on every 3-cube, and for U(1) that conditioning alone creates the photon (the projection onto exact 2-forms has a kernel that decays like a power). So the replacement must be a statement on how a nonlinear constraint differs from a linear one.

**(K2) Strong coupling, any compact group, U(1) included: gap.**
Exact reason: for beta below a threshold beta_0(d,G), the Gibbs measure is a small perturbation of product Haar measure, for which the links are independent. Either the polymer expansion of log Z converges with weights that decay in the size of the polymer (recalled: Osterwalder and Seiler), or the single-link conditional laws depend on the neighbours with total influence below 1 (Dobrushin), or the Bakry-Emery tensor Ric_G + beta Hess(A) is positive (this last one needs Ric_G > 0 and is false for U(1)). The rate is about -4 log beta per lattice unit.
What survives at weak coupling: nothing directly, because U(1) has a transition to a massless phase at finite beta. What could survive: the statement at a coarse scale. If the effective action at the scale where the running coupling is of order 1 were in a convergence domain of this kind, the gap would follow. What must be supplied: control of the effective action across the region where the coupling is of order 1. There the weak-coupling expansion has no small parameter, and the strong-coupling thresholds that can be proved by hand are far away (beta_0 is of order 0.01 to 0.1 for SU(2), while the Wilson theory looks strongly coupled, with correlation length below one lattice unit, already at beta about 2: recalled from simulations, not an input).

**(K3) Finite groups in four dimensions: gap at weak coupling too.**
Exact reason: for a finite group the single-plaquette action has an isolated minimum: a_p(U) >= delta > 0 unless U_p = 1. At large beta the excited plaquettes form closed surfaces on the dual lattice with weight at most exp(-beta delta |surface|), and the Peierls sum converges. So the measure is a small perturbation of the frozen (pure gauge) configuration, and the truncated correlations of local gauge-invariant functions decay at rate about 6 beta delta. (Recalled: low-temperature expansions for Z_N; more recent work on finite groups by Chatterjee, by Cao, and by Adhikari and Cao.)
What it uses: discreteness of the group, which makes the Hessian of the action at the vacuum irrelevant (there are no small fluctuations).
What survives for SU(2): only the centre Z_2, a finite group. The continuous directions have a Hessian at the vacuum equal to the lattice Maxwell operator, which has spectrum down to (2 pi / l)^2. So the gap of SU(2) cannot come from the quadratic approximation at the vacuum. It must come from the terms beyond it.

**(K4) A small torus: gap of order g(l)^{2/3}/l for SU(2), of order 1/l for U(1).**
Exact reason, SU(2) (recalled: Luescher's small-volume expansion): at l small against 1/Lambda the modes with non-zero momentum have energy at least 2 pi / l and can be integrated out; the constant modes c_i in su(2), i = 1,2,3, have the Hamiltonian -(g^2/2l) Delta_c + (l/2g^2) sum_{i<j} |[c_i,c_j]|^2 plus small terms. The potential vanishes on commuting triples (the valleys), which are non-compact in the leading approximation. The operator -Delta + sum_{i<j} |c_i x c_j|^2 on R^9 still has discrete spectrum, because the transverse oscillators have frequency proportional to the distance along the valley and their zero-point energy grows linearly (recalled: Simon's theorem on -Delta + x^2 y^2). Scaling c -> (g^2/l^2)^{1/3} c gives the rate g^{2/3}/l.
Exact reason, U(1): the constant modes have no potential at all. They live on the compact torus of holonomies, and -Delta on a compact torus has discrete spectrum; the photons have energy 2 pi / l. The gap is of order 1/l and tends to zero as l grows.
What it uses: finite volume. Non-commutativity enters only the rate: the product z(l) = l m(l) is constant for U(1), and it grows with l for SU(2) because g(l) grows.
What survives: the function z(l) = l m(l) is defined for every l, and (GAP) for the torus limits says z(l) >= m l. At small l the existence estimates can in principle prove z(l) = c g(l)^{2/3}(1 + o(1)). What must be supplied: an argument that z does not stop growing. A point l* with z stationary under l -> 2l for all larger l would be a massless theory.

**(K5) U(1) in four dimensions: no gap at weak coupling.**
Exact reason (recalled: Guth; Froehlich and Spencer): the theory is a free photon dressed by a gas of closed monopole loops. In four dimensions the loops have action proportional to beta times their length, so at large beta they are short and dilute. They renormalise the charge by a finite factor and leave the photon massless. The plaquette two-point function decays like |x|^{-4}.
A second exact statement of the same fact: U(1) theory has a continuous 1-form symmetry (the electric flux through a closed surface is conserved). In the Coulomb phase it is broken and the photon is its Goldstone particle. A third: the U(1) coupling does not run at weak coupling; the Gaussian fixed point is stable in the infrared.
For SU(2) each of these changes: (a) the Gaussian fixed point is unstable in the infrared, because the one-loop coefficient is proportional to the Casimir of the adjoint representation, which is zero exactly for abelian groups; (b) the 1-form symmetry is the centre Z_2, a discrete group, and a broken discrete symmetry forces no massless particle; (c) the group manifold has Ric > 0, which is true exactly when the Lie algebra has no centre.
None of (a), (b), (c) is a proof of a gap. (a) says the massless free theory is left behind. It does not say where the flow ends. (b) says nothing protects a massless particle. (c) is a statement at the lattice scale.

**(K6) A test the row does not list, which I add because it is also a fact: SU(2) at the deconfinement temperature.** On a slab with one periodic direction of length 1/T_c and the other three infinite, the SU(2) theory is critical (recalled: second-order transition in the universality class of the three-dimensional Ising model). The transfer operator along an infinite direction has no gap there, also on tr(F^2) observables, which couple to the energy operator of the Ising model. So an argument that proves decay on every periodic geometry is wrong. An argument must use that all four directions are large, or it must work on symmetric tori only.

### 1.2 The question itself: why is there a gap, as mathematics?

I separate what is forced from what is not.

**What is equivalent to the gap (exact reformulations).** Let T be the transfer operator on a finite spatial lattice, H = -(1/a) log T, Psi_0 > 0 its ground state (Perron-Frobenius on a compact space with a strictly positive kernel), nu = Psi_0^2 dU.

- (R1) Coercivity: m = inf over psi orthogonal to Omega of <psi, (H - E_0) psi> / <psi, psi>. In the ground-state representation this is a Poincare inequality for nu with the Dirichlet form of H (the electric, link-wise form), uniform in the volume, with a constant that scales like a m.
- (R2) Decay: exponential decay in time of <F, e^{-tH} G> - <F,Omega><Omega,G> on a dense set, with one rate.
- (R3) Free energy, new in this note as far as my own thinking goes (Section 1.5, Lemma 1): for every torus, sum_{i >= 1} exp(-l_1 (E_i - E_0)) <= exp(Delta) - 1, where Delta = log Z(torus) - Vol f_infinity >= 0 is the excess free energy of the torus. So a gap on tori follows if the torus partition function equals its bulk term up to an exponentially small error.

**What is not a reason.** Compactness of the group gives a gap in finite volume and nothing more (U(1) is compact). Positivity of the transfer kernel gives uniqueness of the vacuum in finite volume and nothing more. Reflection positivity and Euclidean invariance are satisfied by massless theories. Asymptotic freedom says the massless Gaussian theory is not the infrared limit. It does not say what the limit is.

**What I believe the true reason is, stated so that it can be false.** The family of finite-volume continuum theories on symmetric tori has one parameter, l Lambda. Let Delta(l) be the excess free energy of the symmetric torus (restricted to zero electric flux if one wants only local observables). At small l the existence estimates give Delta(l) = kappa log(1/g(l)) + O(1) with kappa > 0 from the count of constant modes (this is K4 in another form: many states lie below 1/l). The gap, with confinement, is the statement Delta(l) -> 0 exponentially. A massless infrared phase is the statement Delta(l) -> Delta_* > 0. For U(1), Delta is constant in l at weak coupling: nothing moves. So the gap is the statement that the flow of one number, which asymptotic freedom starts, does not stop before zero. In mathematics this is the absence of a second scale-invariant theory on the way. I know no property of the measure, of the transfer operator, of the configuration space or of the group that forces this without a quantitative estimate at the scale where the coupling is of order 1. The three structural facts that separate SU(2) from U(1) are (a) b_0 proportional to the adjoint Casimir, (b) Ric_G > 0, (c) the 1-form symmetry is discrete. (a) acts only where the coupling is small. (b) acts only where the lattice coupling beta is below about 0.1. (c) forbids nothing. Between the reach of (a) and the reach of (b) lies the whole difficulty, and Section 1.4 shows that two candidate bridges fail there.

**A warning that sharpens the tests (K7, recalled from simulations, not rigorous).** The SU(2) lattice theory with a fundamental plus adjoint plaquette action has a first-order line that ends at a critical point close to the Wilson axis (recalled: Bhanot and Creutz). At that end point the scalar channel is massless at a finite lattice coupling. That theory has the same group, gauge invariance, locality and reflection positivity (for a non-negative adjoint coupling) as the Wilson theory. So a proof of a lattice gap at all couplings that uses only those properties is wrong. A proof must use the continuum limit (where the adjoint term is irrelevant) or the exact Wilson form.

### 1.3 Approaches

Each approach has: mechanism; CRUX; why it could be true; U(1) test (the line where the non-commutative group is used); known-answer test (2D, strong coupling, finite group, small torus, and K6/K7 where they bite); how it dies.

**A1. Excess free energy of symmetric tori (a different object to bound).**
Mechanism: bound numbers, not correlations. By Lemma 1 the gap on tori follows from an upper bound on Delta(l) = log Z(l^4) - l^4 f_infinity.
CRUX (FE): there are m > 0 and C such that Delta_a(l) <= C exp(-m l) for all l >= l_0, uniformly in the lattice spacing a along first-passage data. Weaker crux (FE-0): Delta(l) -> 0.
Why it could be true: Delta is a sum over excitations that wind around the torus; with a gap and a string tension they cost exp(-m l) and exp(-sigma l^2).
U(1) test: Delta tends to the Casimir amplitude of the photon plus the flux sums, a positive constant. The non-commutative group must enter the proof that no constant survives. Passes the test in the sense that the statement is false for U(1).
Known answers: 2D: Z = sum_lambda (c_lambda)^{Area}, Delta = log(1 + sum_{lambda != 0} (c_lambda / c_0)^{Area}), exponentially small in the area: correct. Strong coupling: only winding polymers contribute: correct. Finite group at weak coupling: Delta -> log(number of flux sectors) > 0 although local correlations decay. So (FE) is stronger than the local gap: it is the gap plus no vacuum degeneracy on the torus. With the projection to zero electric flux the constant disappears. Small torus: Delta = kappa log(1/g) + O(1), large: correct (many low states).
How it dies: (FE) is equivalent in strength to the gap with confinement. Soft inequalities (positivity of transfer operators in all four directions) do not give it: Section 1.5 shows they are satisfied with Delta constant.

**A2. Renormalisation group to an exit domain (the specialist's route).**
Mechanism: continue the block renormalisation past the unit scale until the effective coupling is large, then use a convergent expansion.
CRUX (EXIT): there is an explicit set D of effective lattice gauge actions such that every action in D has uniform exponential clustering, and the trajectory started at weak coupling enters D.
Why it could be true: simulations show no transition; the Migdal-Kadanoff recursion flows to strong coupling in four dimensions.
U(1) test: the U(1) coupling does not run, so the trajectory never moves. The group enters through b_0 > 0. But the Migdal-Kadanoff recursion also flows to strong coupling for U(1) in four dimensions, which is wrong (K5). So that recursion is not evidence.
Known answers: 2D and 3D: the coupling has a dimension and the flow reaches strong coupling, but in 3D the crossing is as hard as in 4D and the 3D gap is also open. K7: the fundamental-adjoint end point shows that D cannot be reached by every trajectory of every nearby action.
How it dies: in the crossing region the weak-coupling analysis has no small parameter and the provable strong-coupling domain is two to three orders of magnitude away in g^2.

**A3. Multiscale functional inequality (turn the control at every scale into decay).**
Mechanism: a Poincare or log-Sobolev inequality for the composite measure from one-sided Hessian bounds on the renormalised action at each scale (the Polchinski-flow criterion, or the two-scale criterion), plus Ric_G > 0 at the end.
CRUX (HESS): along the renormalisation flow the effective actions satisfy Ric + Hess S_k >= -mu_k with sum_k mu_k finite uniformly in the cutoff through the crossing region, and >= rho > 0 after it.
Why it could be true: the criterion needs only one-sided bounds, and it tolerates a bounded total negative part.
U(1) test: Ric_{U(1)} = 0, and the fluctuation Hessians are the same as for SU(2) at one loop, so the positive end value rho must come from Ric_G > 0 at strong effective coupling. That is the line. But U(1) at strong coupling has a gap with Ric = 0, so the mechanism does not explain K2 for U(1): it is sufficient, not the reason.
Known answers: strong coupling: gives the gap for beta below about 0.1 (SU(2)), nothing for U(1). 2D: works in plaquette variables. Finite groups: not applicable (no Riemannian structure).
How it dies: the bound Ric + beta_k Hess A >= rho holds only for beta_k below about 0.1; at the last scale that the existence estimates reach, beta_k is large. Section 1.4 gives the numbers. A Poincare inequality for the four-dimensional Langevin form also loses the rate: it gives decay at rate rho, not sqrt(rho), unless a weighted estimate on 1-forms is proved.

**A4. Transport in the coupling (a differential inequality for the mass).**
Mechanism: d/d beta of any expectation is an insertion of the total action, which is the account's observable with f = 1. Prove -d log m / d beta <= c_AF + integrable error, and integrate from strong coupling.
CRUX (DEF): in the first excited state the magnetic energy is lower than in the vacuum by at most (c/4) m (1 + o(1)) with the sharp one-loop constant c; equivalently the Hessian of the solution h of the Poisson equation L h = A - <A> is bounded uniformly in beta.
Why it could be true: it is the trace-anomaly mass formula m = <1| theta |1> read as an inequality.
U(1) test: at the U(1) transition the transport map cannot be Lipschitz, so the bound must fail there. For SU(2) I see no line where the group would enter a proof. Fails the test in this sense: no mechanism.
Known answers: K7 kills every version with a non-sharp constant, because the mass vanishes at the end point of a nearby action.
How it dies: Section 1.4: the natural operator inequality |E^2 - B^2| <= E^2 + B^2 is off by the factor 1/g^2 after vacuum subtraction, and only an identity can give the sharp constant.

**A5. Finite-size scaling with a monotone coupling.**
Mechanism: base at small l (K4), then a step from l to 2l.
CRUX (STEP): there is a finite-volume coupling u(l) with u(2l) >= sigma(u(l)), sigma(u) > u on (0, u_*), and u >= u_* implies a gap of order 1/l in all larger volumes.
Why it could be true: for every coupling defined so far the step function is positive in simulations.
U(1) test: u is constant for U(1); the group enters through sigma(u) - u = b_0 u^2 at small u. Beyond small u there is no line.
Known answers: K6: on a slab the step function has a fixed point at 1/T_c. So the coupling must be defined on symmetric tori.
How it dies: strict monotonicity is not enough; u can converge to a finite limit below u_*.

**A6. Centre flux duality ('t Hooft; exact Z_2 Fourier transform).**
Mechanism: on a symmetric torus exp(-F_e) = tanh(F_m / 2) exactly, where exp(-F_m) = Z_twisted / Z. Show F_m(l) -> 0.
CRUX (VORT): 1 - Z_twisted(l)/Z(l) <= C exp(-sigma l^2).
Why it could be true: thick vortices cost no action at large size.
U(1) test: for U(1) with a Z_N twist the ratio does not tend to 1. No line in a proof is known to me.
Known answers: Z_2 at weak coupling: ratio tends to 0, no confinement, yet a local gap. So (VORT) is confinement, a different statement from (GAP), and neither implies the other without more.
How it dies: it bounds a different object; the link to tr(F^2) decay is a second open theorem.

**A7. Geometry of the orbit space (Bakry-Emery for the ground-state measure).**
Mechanism: gap(H) is the Poincare constant of nu = Psi_0^2. The orbit space has sectional curvature (3/4)|[X,Y]^vert|^2 >= 0 (O'Neill), zero for U(1).
CRUX (BE-0): Ric + Hess(2W) >= rho > 0 on the orbit space for Psi_0 = e^{-W}, with rho of order a m / g^2, uniformly in the volume.
U(1) test: curvature zero: passes at the first line.
Known answers: on the lattice, log-concavity of Psi_0 with Ric_G > 0 would give a gap of order g^2/a, which is false at weak coupling (the true gap is far smaller). So Hess W has negative directions that cancel Ric almost exactly.
How it dies: the needed rho is exponentially small in 1/g^2; a pointwise curvature bound cannot produce it without a multiscale step, and then it is A3.

**A8. Gribov region and log-concavity.**
Mechanism: in Landau gauge the Faddeev-Popov operator M(A) is linear in A, the region {M >= 0} is convex, and det M is log-concave on it (log det of a positive operator that depends linearly on a parameter is concave). For a log-concave measure a bounded covariance gives a Poincare inequality up to the constant of the Kannan-Lovasz-Simonovits problem.
CRUX (LC): the gauge-fixed measure is a bounded perturbation, uniformly per degree of freedom in a way that the Poincare constant survives, of a log-concave measure whose covariance has no pole at zero momentum.
U(1) test: det M is constant for U(1). Passes at the first line.
How it dies: the Yang-Mills action is not convex in A: its Hessian has the term 2<F_A, [B,B]>, which is the same paramagnetic term that gives asymptotic freedom. Also the restriction to one Gribov copy is not known to be the right measure.

**A9. Correlation inequalities and sharpness.**
Mechanism: an inequality of Simon-Lieb type would give a finite-size criterion with no boundary conditions.
CRUX (SL): <a_p; a_q> <= sum over r in a surface separating p from q of <a_p; a_r>_inside <a_r; a_q>.
U(1) test: for U(1) Ginibre inequalities exist and the criterion fails at weak coupling, as it must.
How it dies: the dual (spin-network) weights of SU(2) have signs; I know no inequality of this type. On one 3-cube the covariance of two plaquette characters is non-negative by a positive dual measure (checked by hand in my notes), but that does not extend. K7 forbids a criterion that holds for all actions and is met at all couplings.

**A10. Dilation identity (trace anomaly).**
Mechanism: l d/dl of log Z on a torus is the integrated one-point function of tr(F^2). So l dDelta/dl = l^4 (theta(l) - theta(infinity)), the finite-size shift of the condensate.
CRUX (SHIFT): l^4 |theta(l) - theta(infinity)| <= C exp(-m l), and the constant of integration Delta(infinity) is zero.
U(1) test: the shift is zero for a scale-invariant theory, and Delta(infinity) is the photon amplitude. The second clause is the line.
How it dies: the constant of integration is the whole question.

**A11. Monopole plasma (Polyakov's mechanism).** CRUX: the monopole loops of an abelian projection condense. U(1) test: in 4D they do not at weak coupling (K5). Dies at once in four dimensions: loops, not points.

**A12. Plaquette variables (the Wilson measure as a Gaussian restricted to the Bianchi variety).**
Mechanism: for SU(2) = S^3 in R^4, beta a_p = (beta/2)|U_p - 1|^2. So the Wilson measure in plaquette variables is the Gaussian of variance 1/beta centred at the point (1,...,1), restricted to the variety of plaquette fields that satisfy the Bianchi identity, with a Jacobian.
CRUX: a Poincare inequality in the plaquette metric.
Verdict: FALSE as a route. For U(1) at weak coupling the covariance of the plaquette field is (1/beta) times a projection, so the Poincare inequality in the plaquette metric holds with constant beta although the photon is massless. A bounded covariance in the magnetic metric says nothing about decay. The Dirichlet form must be the link-wise (electric) one.

**Choice.** I choose A1 (with A10 as its differential form) as the frame, because its entry is an exact inequality with no loss, its object is the one the existence estimates control, and it turns the gap into the behaviour of one number per scale. I take A3 as the second approach because it fails in a different way (a rate and a threshold, not a constant of integration). I attack three cruxes below: (FE) of A1, (DEF) of A4, and (HESS) of A3. My plain judgement, argued in 1.4-1.6: none of the twelve closes by hand with structures I know; the reason is one and the same, and I state the best conditional theorem.
