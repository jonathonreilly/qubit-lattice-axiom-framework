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

### 1.4 Attacks on two cruxes that die: (DEF) of A4 and (HESS) of A3

**Attack on (DEF).** Label: heuristic computation in the continuous-time (Kogut-Susskind) form; it is an obstruction to a proof, not a theorem.
Write H(g) = (g^2/2) K + (2/g^2) V at lattice spacing 1, with K = -sum_b Delta_b >= 0 (electric) and V = sum_p a_p >= 0 (magnetic). For an eigenvalue difference m = E_1 - E_0 in a finite volume, first-order perturbation theory gives, with <.>_{1-0} the difference of the expectations in the two states,
X + Y = m and X - Y = g^2 dm/dg^2, where X = (g^2/2)<K>_{1-0} and Y = (2/g^2)<V>_{1-0}.
If the mass scales as asymptotic freedom says, m = C exp(-1/(2 b_0 g^2)) (g^2)^{p} (1 + O(g^2)), then g^2 dm/dg^2 = m (1/(2 b_0 g^2) + p + O(g^2)). So X = (m/2)(1 + 1/(2 b_0 g^2) + ...) and Y = (m/2)(1 - 1/(2 b_0 g^2) - ...). At small g the magnetic part Y is negative and of size m/(4 b_0 g^2), far above m.
Consequences. (i) The natural operator comparison "|E^2 - B^2| <= E^2 + B^2", read as |X - Y| <= C (X + Y) with C independent of g, is false whenever the gap scales correctly: it would force a power law m = g^{2C}. (ii) What a proof needs is the one-sided bound Y >= -(m/(4 b_0 g^2))(1 + o(1)) with the exact constant 1/(4 b_0). A constant larger by any factor lets the physical mass tend to zero. An inequality with an exact constant comes only from an identity, and the identity here is the anomaly equation, which assumes the scaling it should prove. (iii) Positivity of a_p gives only Y >= -(volume of the excitation) x O(g^2), which is off by the factor (correlation length)^4.
Named point of failure: no inequality between the vacuum-subtracted electric and magnetic energies of a state is known that is sharp at order 1/g^2. K7 confirms that a non-sharp one cannot exist in a form that is stable under a small adjoint term.

**Attack on (HESS): the numbers.** This part is a proof.
Take SU(2) as the unit sphere S^3 in R^4, U = u_0 + i u.sigma, with the round metric. Then Ric = 2 on each link. For a plaquette U_p = U_1 U_2 U_3^{-1} U_4^{-1} and tangent vectors v_b, write the transported generators as y_b.sigma with |y_b| = |v_b|. Expanding the product of exponentials to second order gives
Hess a_p (v,v) = u_0 |sum_b y_b|^2 - 2 u . sum_{b<b'} (y_b x y_b'), where U_p = u_0 + i u.sigma.
(Proof: prod_b e^{i t y_b.sigma} = 1 + i t sum y_b.sigma - (t^2/2) sum |y_b|^2 - t^2 sum_{b<b'} (y_b.y_b' + i (y_b x y_b').sigma) + O(t^3), and (1/2) tr((u_0 + i u.sigma)(w_0 + i w.sigma)) = u_0 w_0 - u.w.)
Since |sum_b y_b|^2 <= 4 sum |y_b|^2 and |sum_{b<b'} y_b x y_b'| <= (3/2) sum |y_b|^2, and 4|u_0| + 3|u| <= 5 on the unit sphere, Hess a_p (v,v) >= -5 sum_{b in p} |v_b|^2. Each link lies in 6 plaquettes in four dimensions. So
Ric + beta Hess A >= (2 - 30 beta) on (S^3)^{links}, for every configuration and every volume.
So the Bakry-Emery criterion gives a Poincare inequality for the Wilson SU(2) measure, uniform in the volume, for beta < 1/15. (The constant 30 is crude. It is the order that matters.) For U(1) the same computation gives 0 - c beta < 0 for every beta > 0: the criterion never applies, as the U(1) test demands.
The other end: the existence estimates need g small at every step, so the last effective coupling they reach has beta_k = 4/g_k^2 large (above 40 if g_k^2 <= 0.1). The effective action there is beta_k sum a_p plus small terms, and its Hessian has negative directions of size beta_k on the set where a plaquette is far from 1. That set has small probability, but the criterion is pointwise.
Named point of failure: for effective couplings between about 1/15 and about 40 there is no one-sided Hessian bound and no other tool. The two-scale criterion does not help: it needs the same bound for the marginal at the coarse scale. A second failure, independent of the first: a Poincare inequality for the four-dimensional link-wise form with constant rho gives decay of correlations at rate proportional to rho (through finite speed of propagation of the Langevin dynamics), and rho must scale like (a m)^2. So even a perfect inequality loses the continuum limit unless a weighted estimate on 1-forms gives the rate sqrt(rho). That is a second open lemma.

### 1.5 Attack on (FE), the crux of A1

Setting. A finite lattice torus with sides n = (n_1,...,n_4), n_mu >= 3, Wilson SU(2) action, Z(n) its partition function, F(n) = log Z(n), |n| = n_1 n_2 n_3 n_4, f(n) = F(n)/|n|.

Input (TM), the transfer operator. For each direction mu and each choice of the other three sides there is a positive semi-definite trace-class operator T with Z(n) = Tr T^{n_mu}; its largest eigenvalue lambda_0 is simple with a strictly positive eigenfunction. This is the classical construction (recalled: Luescher; Osterwalder and Seiler). It is the object of FINISH row 667, whose file I did not open. I use it as an input. Write the eigenvalues as lambda_0 > lambda_1 >= lambda_2 >= ... >= 0, r_i = lambda_i / lambda_0, and S(k) = sum_{i >= 1} r_i^k.

**Lemma 1 (free energy bounds the spectrum). Proved here.**
(a) For A >= 0 trace class, k -> (Tr A^k)^{1/k} is non-increasing on k >= 1 and tends to lambda_0.
(b) S(k + k') <= S(k) S(k').
(c) f is non-increasing in each side. So f_inf := inf_n f(n) is the limit of f along every sequence with all sides tending to infinity, and Delta(n) := F(n) - |n| f_inf >= 0.
(d) With T the transfer operator in direction 1 for the box (n_2,n_3,n_4): 1 + S(n_1) <= exp(Delta(n)). In particular the gap m = log(lambda_0/lambda_1) of that box satisfies exp(-n_1 m) <= exp(Delta(n)) - 1 for every n_1.
Proof. (a) sum lambda_i^{k+1} <= lambda_0 sum lambda_i^k <= (sum lambda_i^k)^{1/k} sum lambda_i^k. The limit: lambda_0^k <= Tr A^k <= lambda_0^{k-1} Tr A. (b) sum r_i^{k+k'} <= max_j r_j^{k'} sum r_i^k <= S(k') S(k). (c) Apply (a) to T^{n_mu} in each direction; f is bounded below by -12 beta because Z >= exp(-2 beta 6 |n|). A function on a product of ordered sets that is non-increasing in each variable and bounded below has its infimum as the limit when all variables grow. (d) By (a), log lambda_0 = lim_{n_1} F(n)/n_1 = n_2 n_3 n_4 lim_{n_1} f(n) >= n_2 n_3 n_4 f_inf. So Z(n) = lambda_0^{n_1}(1 + S(n_1)) >= exp(|n| f_inf)(1 + S(n_1)). The last claim is r_1^{n_1} <= S(n_1). QED.

**Lemma 1' (zero electric flux). Proved here, given (TM).** Let Gamma = Z_2^3 act by the centre flips C_i (multiply by -1 every link in direction i that crosses the plane x_i = 0). Each C_i preserves Haar measure and the action, so it commutes with T, and Tr(T^{n_1} C^k) is the partition function Z_k(n) with twist k (recalled: 't Hooft). The positive ground state is invariant. So on the invariant subspace, with Z^(0) = (1/8) sum_k Z_k and Delta^(0) = log Z^(0) - |n| f_inf: 1 + S^(0)(n_1) <= exp(Delta^(0)(n)), and 0 <= Delta^(0) <= Delta. Functions of contractible loops preserve this subspace. Proof: the same as (d), with Tr over the invariant subspace.

**Lemma 2 (integral formula). Proved here.** For fixed n, F(n; beta) is smooth in beta, convex, with dF/dbeta = -6|n| abar(n; beta), where abar is the mean plaquette action. f_inf(beta) is an infimum and a limit of convex functions with f_inf(0) = 0, so it is convex, absolutely continuous, and differentiable for almost every beta; put abar_inf = -f_inf'/6 there. Then
Delta(n; beta) = 6 |n| int_0^beta (abar_inf(s) - abar(n; s)) ds >= 0.
Proof: F(n;0) = 0 = f_inf(0), and both functions are absolutely continuous. QED.
So, with Lemma 1: exp(-n_1 m(n_2,n_3,n_4; beta)) <= exp( 6|n| int_0^beta (abar_inf - abar_n) ds ) - 1. The gap of a box is bounded below by the integral, over all couplings up to beta, of the finite-size shift of one number, the plaquette expectation. That shift is the one-point function of the account's observable.

**Corollary (criterion).** If along first-passage data Delta_a(l,l,l,l) <= C exp(-m l) for l >= l_0, uniformly in a, then for C exp(-m l) <= 1 the gap of the l^3 box is at least m - log(2C)/l, uniformly in a. (Use e^x - 1 <= 2x on [0,1].) If only Delta_a(l) -> 0 uniformly, then l m_a(l) -> infinity: the spectrum of the box is not of the scale-invariant form z_i / l.

**Proposition 3 (finite volume: a uniform count of states). Proved here as an implication.** Assume the source hypothesis (ST5) of the account at W = 0 on symmetric tori: V - C_- l^4 <= log Z_{a,l} <= V + C_+ l^4 with V = V_{a,l}. Assume also (V-ext): V_{a,l'}/l'^4 >= V_{a,l}/l^4 - C_V for l' >= l in the family. (The account calls V "the source-independent vacuum number" and does not state this; lines 98405-98413.) Then Delta_a(l) <= (C_+ + C_- + C_V) l^4, and the number N_{a,l}(E) of eigenvalues of H_{a,l} = -(1/a) log T in [E_0, E_0 + E] satisfies
N_{a,l}(E) <= exp( l E + (C_+ + C_- + C_V) l^4 ), uniformly in the lattice spacing.
Proof. f_inf >= liminf_{l'} (V_{a,l'} - C_- l'^4)/l'^4 >= V_{a,l}/l^4 - C_V - C_-, so Delta <= V + C_+ l^4 - l^4 f_inf <= (C_+ + C_- + C_V) l^4. Then N(E) e^{-lE} <= 1 + S(l/a) <= e^{Delta} by Lemma 1(d). QED.
Meaning: weak limits of spectral measures with at most N atoms below E have at most N atoms below E. So a continuum limit on the cylinder l^3 x R, if it exists as a limit of these lattice theories, has a Hamiltonian with discrete spectrum, and so spec(H_l) lies in {0} union [m(l), infinity) with m(l) > 0. This is (W2). It uses nothing about the group. It holds for U(1) too, as it should (K4).

**Why (FE) does not follow from soft properties (a no-go, given K5).** U(1) Wilson theory has a positive transfer operator in every direction, the same lattice symmetries and locality. Lemmas 1, 1', 2 hold for it word for word. If (FE), or (FE-0), followed from those properties, U(1) at weak coupling would have l m(l) -> infinity, against K5 (the photon has energy 2 pi / l). So a proof of (FE) must use the group at a quantitative step.

**Where exactly the content sits.** Put phi(n) = F(n,n,n,n) - (1/16) F(2n,2n,2n,2n) >= 0. Then Delta(n) = sum_{k >= 0} 16^{-k} phi(2^k n). (FE-0) is the statement of near-supermultiplicativity: Z(2n) >= Z(n)^{16} exp(-eps(n)) with eps(n) = 16 phi(n) -> 0. The transfer structure gives only Z(2n) <= Z(n)^{16}. Three more exact facts, each checked by the same algebra as Lemma 1:
- Doubling one side: (1 + S(k))^{-2} <= Z(2k, box)/Z(k, box)^2 <= 1.
- The ratio 2 F(k, box) - F(2k, box) is the Renyi-2 entropy of the density matrix T^k / Tr T^k. It tends to zero exactly when that state tends to the vacuum projection.
- Crossing: for a box of sides (s, n_3, n_4) and time t, Z = lambda_0(s,n_3,n_4)^t (1 + S_t) = lambda_0(t,n_3,n_4)^s (1 + S_s). Letting t grow: the thermal free energy per unit length of the infinite tube at inverse temperature s equals the Casimir deficit, log lambda_0(s,n_3,n_4) - s lim_t (1/t) log lambda_0(t,n_3,n_4) >= 0.
I tried to close a recursion S(2n; (2n)^3) <= C S(n; n^3)^2 from these. The exact part is S(2n; (2n)^3) <= S(n; (2n)^3)^2. The missing part is the comparison of the thermal sum of the box (2n)^3 with that of the box n^3 at the same inverse temperature n, S(n; (2n)^3) <= C S(n; n^3). Through crossing this is a bound of the Casimir deficit of a doubled box by the thermal sum of the single box. Every inequality above that touches the deficit carries it on both sides and cancels (I wrote the chain out: it reduces to "l pi <= log(1+s) + l pi"). A decoupling by changed boundary conditions costs a surface term, which is of order l^3 at unit scale and is not small.

**Named point of failure of the attack on (FE).** Lemma NSM (near-supermultiplicativity): eps(n) = 16 F(n^4) - F((2n)^4) -> 0 as n a(beta) -> infinity, uniformly in the cutoff. Three ways failed: (1) transfer positivity in four directions (cancels, and holds for U(1)); (2) boundary-condition comparison (surface cost of order l^3); (3) the dilation identity, which gives l dDelta/dl = (6/c_a) n^4 (abar_n - abar_inf) with c_a = -d log a / d beta and so moves the question to the constant of integration Delta(infinity), which is the infrared Casimir amplitude and is zero only if the gap holds.

**Two side results of the same algebra.**
- An upper bound on the gap is free. For a positive-time vector, t -> <F, e^{-tH} F> - |<Omega,F>|^2 is a Laplace transform of a positive measure, so it is log-convex and its logarithmic derivative mu(t) decreases to the bottom of the support. The account's short-distance law gives mu(t) = (8/t)(1 + o(1)) in the window where the coupling is small. So the gap of the tr(F^2) sector is at most (8 + o(1))/r for every r in that window. The lower bound is the whole problem.
- Small torus: counting the modes with no quadratic action (4 flat directions, 6 transverse Gaussian ones, stabiliser of dimension 1) I get Delta(l) = 3 log(1/g(l)) + O(1) as l Lambda -> 0. Unchecked; the constant 3 is not used anywhere.

### 1.6 Verdict of Part 1

1. No approach among the twelve reaches the gap by hand with structures known to me. The reason is the same in each: the proof must control the theory at the scale where the running coupling is of order 1. The existence estimates stop before it (they need g small), every provable strong-coupling tool starts far behind it (beta below about 0.1), and the exact structures (positivity of transfer operators, reflection positivity, dilation identity, flux duality) are all consistent with a massless infrared limit, as U(1) shows.
2. The best conditional theorem is Lemma 1 with its corollary: (FE) implies a uniform gap on tori, for local observables through Lemma 1'. It has one hypothesis, and that hypothesis concerns numbers (partition functions of symmetric tori), which is the kind of object the existence proof bounds. Its differential form (Lemma 2) concerns the one-point function of the account's own observable.
3. The result short of the gap that is within reach is Proposition 3 and its consequence (W2): discrete spectrum of the continuum Hamiltonian in a finite box. Its inputs are the existence estimates, (V-ext), and the existence of the cylinder limit.
4. What would change the verdict: a proof of Lemma NSM at one scale beyond the crossing, or an inequality that bounds the Casimir deficit of a box by its thermal sum. I found neither.

### 1.7 A thirteenth approach, found while pushing the attack on (FE): analytic continuation in the bare coupling

This section was written after 1.6 and before any literature was opened. It changes the choice. I leave 1.3-1.6 as they stand.

**A13. Transport of the strong-coupling decay along a zero-free tube in the complex beta-plane (a different order of limits and a different inequality).**

Idea. At strong coupling the decay rate is as large as we like. A truncated correlation, and also the winding sum of a torus, is an analytic function of beta wherever the partition functions do not vanish. The logarithm of the modulus of an analytic function is subharmonic. So smallness on the strong-coupling circle and mere boundedness elsewhere give smallness inside, with an exponent equal to a harmonic measure. This is the mechanism of Lebowitz and Penrose for lattice gases (recalled; Part 2 checks it), used here in the temperature variable.

Notation. Z_n(beta) is the partition function of the symmetric torus n^4, entire in beta. E_n(beta) = Z_n(beta) exp(-n^4 f_inf(beta)) and Sigma_n = E_n - 1, defined where f_inf has an analytic continuation. On the real axis E_n = exp(Delta_n) >= 1 (Lemma 1).

**Theorem LP (two constants). Proved here; it is classical complex analysis.** Let D be a bounded domain, B a closed disc inside D, D' = D minus B, and omega the harmonic function on D' with boundary values 1 on the circle of B and 0 on the boundary of D. Let h be analytic on D' and continuous up to the boundary, with |h| <= eps on the circle and |h| <= M on the boundary of D, eps < M. Then |h(beta)| <= eps^{omega(beta)} M^{1 - omega(beta)} on D'.
Proof. log|h| is subharmonic on D'. The function v = omega log eps + (1 - omega) log M is harmonic and dominates log|h| on the boundary. The maximum principle gives log|h| <= v. QED.

**Lemma HM (the model domain). Proved here.** In the half-strip {x > 0, |y| < w} the bounded harmonic function with boundary values 1 on the side x = 0 and 0 on y = +-w is omega(x,y) = (4/pi) sum_{k odd} ((-1)^{(k-1)/2}/k) cos(k pi y / 2w) exp(-k pi x / 2w). On the axis omega(x,0) = (4/pi) arctan(exp(-pi x / 2w)) >= exp(-pi x / 2w). (The series is the Fourier series of the constant 1 on (-w,w); sum_{k odd} (-1)^{(k-1)/2} q^k / k = arctan q, and arctan q >= pi q / 4 on [0,1].) Harmonic measure of the circle increases when D is enlarged with B fixed (maximum principle). So if D contains a tube of half-width w along the real axis, omega decays no faster than exp(-pi x / 2w), up to a constant that depends on the shape near B.

**Corollary 4 (the conditional theorem of A13).** Assume:
- (SC) strong coupling for complex beta: |Sigma_n(beta)| <= C_0 n^4 exp(-kappa_0 n) on |beta| = r_0, for all n. (The convergent polymer expansion; winding polymers have at least 4n plaquettes; kappa_0 = 4 log(1/(c r_0)). To be rebuilt; I did not prove it here.)
- (BD) boundedness: f_inf is analytic in D and |E_n(beta)| <= M on D for all n >= n_0.
Then for real beta in D: Delta_n(beta) <= |Sigma_n(beta)| <= (M + 1) (C_0 n^4)^{omega(beta)} exp(-kappa_0 omega(beta) n). With Lemma 1 the gap of the box n^3 at coupling beta satisfies n m_n(beta) >= kappa_0 omega(beta) n - 4 omega(beta) log n - log(2 (M+1) C_0) when the right side of the bound on Sigma_n is at most 1. So the mass in lattice units is at least kappa_0 omega_D(beta) up to terms that vanish as n grows.
Proof. Theorem LP with h = Sigma_n on a truncation of D. QED given (SC).

**What the geometry says.** The lattice mass is bounded below by the harmonic measure of the strong-coupling circle.
- Sector. If D contains a sector of half-angle theta, omega decays like beta^{-pi/(2 theta)}. A half-plane gives 1/beta.
- Strip. If D contains a strip of half-width w, omega decays like exp(-pi beta / 2w).
- Asymptotic freedom. The lattice spacing is a(beta) = exp(-c_a beta (1 + o(1))) with c_a = 12 pi^2/(11 N^2) = 3 pi^2/11 for SU(2) (the account, line 1751, gives beta/log(1/a_K) -> 11 N^2/(12 pi^2)). The bound kappa_0 omega(beta) is a positive mass in physical units exactly when omega(beta) >= eps a(beta), that is when the tube has asymptotic half-width w_inf = pi/(2 c_a) = 11 N^2/(24 pi) = 11/(6 pi) = 0.584 for SU(2), with the next correction matching the two-loop term. In the variable 1/g^2 = beta/4 this is |Im (1/g^2)| < pi b_0. That is the line on which exp(-1/(b_0 g^2)), the square of the dynamical scale, becomes negative. So the width is not a coincidence: a complex shift of beta is a complex dilation, the mass turns by the angle c_a Im beta, and decay survives while the real part of the mass is positive. The two-constants bound is sharp for the true domain: if exp(-mu(beta)) is the ratio of the two largest transfer eigenvalues and mu maps the tube into the right half-plane with Re mu = 0 on the sides, then Re mu is itself a positive harmonic function that vanishes on the sides.

**Tests.**
- Two dimensions (exact). With the character coefficients c_j = 2(2j+1) I_{2j+1}(beta)/beta (a one-line integral with the Haar density (2/pi) sin^2), the torus of area A has Z = sum_j (2 I_{2j+1}(beta)/beta)^A up to exp(-beta A). So the ratios of transfer eigenvalues are I_k(beta)/I_1(beta), k = 2, 3, ..., and f_inf = log(2 I_1(beta)/beta) - beta, analytic in Re beta > 0 because I_1 has its zeros on the imaginary axis. A first draft of this bullet said that |I_k/I_1| <= 1 in the whole right half-plane. A small numerical check refuted that (scripts in my scratch folder, under the numeric lock, 57 percent memory free, guide only): the ratio exceeds 1 in a region next to the imaginary axis, of the form Re beta < x_c(Im beta), with x_c at most about log(1 + |Im beta|) on the samples (largest value 3.2 at Im beta = 80). The large-argument expansion agrees: I_2/I_1 = 1 - 3/(2 beta) +- 2i exp(-2 beta) + ..., so the modulus passes 1 where exp(-2 Re beta) is of order Re beta / |beta|^2. So the correct domain in two dimensions is D = {Re beta > log(1 + |Im beta|) + c} joined to the strong-coupling disc (the bound on that domain is numerical evidence and the asymptotic formula, not a proof). This D contains, for every theta < pi/2, a sector of half-angle theta with its vertex on the positive real axis. The theorem then gives a string tension of at least c beta^{-pi/(2 theta)}, that is beta^{-1-delta} for every delta > 0. The true value is -log(I_2/I_1) = 3/(2 beta) + O(beta^{-2}) (checked numerically at beta = 40, 80, 160: ratio to 3/(2 beta) is 1.013, 1.006, 1.003). The exponent is right. In two dimensions the coupling has a dimension, the mass is a power of 1/beta, and the zero-free domain is asymptotically a half-plane, not a strip.
- U(1) in four dimensions. The partition function has zeros that reach the real axis at the transition. (BD) fails for every D that crosses the transition. The argument stops at the right place and for the right reason.
- Finite groups. Z_2 in four dimensions has a transition. The argument stops there. The gap beyond it is real and comes from an anchor at beta = infinity, in a different domain.
- K6. On a lattice with a fixed short time side the zeros reach the real axis at the deconfinement coupling. The argument stops there, as it must.
- K7. A small adjoint term moves the zeros toward the real axis and at the end point they reach it. The hypothesis (BD) is a statement on the Wilson line only. No universality is claimed.
- Small torus. Not tested: the theorem concerns large n.

**The crux of A13.** (BD) on a domain D that contains the strong-coupling disc, a tube around the real axis, and the asymptotic strip. It has three parts of different kinds.
- (BD-uv) Re beta large, torus physically small. A perturbative statement at complex coupling. The complex part of 1/g^2 is not changed by the one-loop flow, so at every scale down to the size of the torus the coupling is nearly real. This is within the kind of estimate the existence proof makes (it already has complex sources of any fixed radius, at the price of a smaller g: lines 1744-1746).
- (BD-ir) Re beta large, torus physically large. The infrared theory under a complex dilation. If the real theory has a gap and scaling holds, this is true. Without the gap I have no proof. But it is needed only on one period of the renormalisation, and once the gap is known at one coupling in the scaling region, scaling alone carries it on.
- (BD-x) the tube between the strong-coupling disc and the first coupling beta_1 where the existence estimates apply. This is the statement that there is no phase transition on (r_0, beta_1), in the bounded-analytic sense. It is qualitative: the width of the tube there changes only the constant. It is specific to the Wilson action (K7).

**Attack on (BD) in this run, and where it stopped.**
1. I proved the transport (Theorem LP, Lemma HM, Corollary 4) and checked it on the exact two-dimensional theory.
2. (BD) from the trivial bounds fails. |Z_n(x + iy)| <= Z_n(x), and Re f_inf(x + iy) = f_inf(x) - (y^2/2) f_inf''(x) + ..., so the trivial bound is |E_n| <= exp(Delta_n(x) + c n^4 y^2). It is bounded only in a tube of width n^{-2}, and the harmonic measure of such a tube is useless. The true bound needs the cancellation between the modulus of the characteristic function of the total action and its infinite-volume rate: a local limit theorem for the action with an O(1) error in the exponent.
3. Zeros through the transfer operator. For a long torus over a fixed box the zeros of Tr T^n accumulate where the two largest eigenvalues have equal modulus (recalled: Beraha, Kahane and Weiss), that is where the real part of the complex gap vanishes. At real beta the gap is positive by Perron-Frobenius. A complex form of Perron-Frobenius (cones in complex spaces) gives a gap for kernels whose phases stay in a sector; here the phase of the kernel is Im beta times the action of a time slice, which grows with the box. So this gives a tube whose width shrinks like 1/volume. Failed.
4. A structural proof of non-vanishing (in the manner of Lee and Yang, or of Heilmann and Lieb) would need a positivity of the character expansion. For SU(2) in more than two dimensions the weights of the dual sum have signs. K7 shows that no argument that is stable under a small adjoint term can exist. Failed, with a reason.
Named point of failure: Lemma ZF-x (no zeros of Z_n(beta), uniformly in n, in a complex neighbourhood of a compact interval [r_0, beta_1] of the Wilson axis, with the bound |E_n| <= M). Three ways failed: trivial modulus bounds, complex Perron-Frobenius, positivity of the dual expansion.

### 1.8 Revised choice and verdict of Part 1

**Chosen approach: A13 joined to A1.** Prove (FE) by analytic transport from strong coupling (Corollary 4), then the gap by Lemma 1. Its crux is (BD). It is the only approach in the list in which the hypothesis is qualitative in the crossing region (a function does not vanish) and in which asymptotic freedom enters as the shape of a domain. It passes every known-answer test, the two-dimensional one with the correct exponent.

**Second approach, failing in a different way: A3** (multiscale functional inequality with Ric_G > 0). It fails by a threshold and a rate, not by a zero of a partition function.

**Plain judgement.** I do not have a proof and I do not see one by hand. (BD-x) is the statement that the Wilson SU(2) theory has no phase transition between strong coupling and the perturbative region. Simulations say so. No structure I know proves it, and K7 shows that it is false for a nearby action. What I do have is: an exact inequality from free energy to spectrum (Lemma 1, 1'), an exact formula for the excess free energy (Lemma 2), a uniform count of states in finite volume from the existence estimates (Proposition 3), and a conditional theorem with one hypothesis of analytic type (Corollary 4), whose sharp form explains the asymptotic-freedom rate. The best conditional theorem is: (SC) and (BD) imply (FE), hence a uniform gap on tori in physical units. The one hypothesis is (BD).

### 1.9 Sharpening of A13: zero-freeness alone is enough, and which partition function to use

Still before any literature. This section replaces the hypothesis (BD) of 1.7 by a weaker one and corrects the object.

**Theorem Z (no zeros implies the gap). Proved here, given (TM) and (SC).** Let D be a simply connected domain in {Re beta > -r_0}, symmetric under complex conjugation, that contains the disc |beta| <= r_0 and a real interval (0, X), and is bounded (cut at Re beta = X). Assume the shape condition (TUBE): for every beta = x + iy in D with x >= 0, the closed disc with centre x and radius |y| + d(beta)/2 lies in D, where d is the distance to the boundary of D. (A strip satisfies it. A tube whose width varies slowly satisfies it with d/2 replaced by a fixed fraction of d.) Let (n_j) be a doubling sequence, n_{j+1} = 2 n_j. Assume
(ZF) Z_{n_j}(beta) != 0 for all j and all beta in D.
Then for every real beta in D and every n in the sequence,
Delta_n(beta) <= C (1 + X) n^{5} exp( -kappa_0 omega_n(beta) n ),
where omega_n is the harmonic measure of the circle |beta| = r_0 in the domain {beta in D: dist(beta, boundary of D) > 1/n}, and C depends only on r_0, C_0 and the local shape of D. With Lemma 1, the transfer operator of the box n^3 has gap at least kappa_0 omega_n(beta) - (5 log n + log(2C(1+X)))/n in lattice units, as soon as the bound on Delta_n is at most log 2.
Proof.
1. f_n = n^{-4} log Z_n is analytic in D by (ZF), with the branch that is real on the real axis.
2. Upper bound. |Z_n(beta)| <= Z_n(Re beta) <= exp(12 n^4 max(0, -Re beta)), because 0 <= a_p <= 2 and there are 6 n^4 plaquettes. So Re f_n <= A := 12 r_0 on D.
3. Lower bound from the real axis. P = A - Re f_n is a positive harmonic function on D. At a real point x >= 0, f_n(x) >= -12 x, so P(x) <= A + 12 x. Harnack's inequality in the disc of (TUBE), with centre x, radius R = |y| + d/2, gives P(beta) <= ((R + |y|)/(R - |y|)) P(x) <= (4R/d)(A + 12 x). So Re f_n >= -C(1 + Re beta)/d on D, uniformly in n. The Borel-Caratheodory inequality in the same disc, |f(z)| <= (2r/(R-r)) sup Re f + ((R+r)/(R-r)) |f(x)| for |z - x| <= r < R, bounds |f_n| by the same form with another constant, because f_n(x) is real and |f_n(x)| <= A + 12 x.
4. Limit. The f_{n_j} are locally uniformly bounded and converge on the real interval (Lemma 1(c)). By Vitali's theorem they converge locally uniformly on D to an analytic f_inf, with the same bound. Put u_n = f_n - f_inf. Then |u_n| <= C(1 + Re beta)/d on D, and u_n = Delta_n / n^4 >= 0 on the real axis.
5. Anchor. By (SC), |u_n| <= 2 C_0 exp(-kappa_0 n) on |beta| = r_0.
6. Transport. Apply Theorem LP to h = u_n on the domain {d > 1/n} minus the disc, with eps = 2 C_0 exp(-kappa_0 n) and M = C (1 + X) n. This gives |u_n(beta)| <= C(1+X) n exp(-kappa_0 omega_n(beta) n). Multiply by n^4. QED.
(The same proof with v_n = f_n - f_{2n} in place of u_n avoids f_inf and uses (ZF) only for n and its doubles; then Delta_n = n^4 sum_k v_{2^k n}.)

Remarks.
- The hypothesis is one statement about explicit entire functions: the Laplace transforms Z_n(beta) = int exp(-beta A) dU of the Wilson action on symmetric tori have no zeros in D. No bound is assumed. The bounds come from positivity on the real axis and Harnack.
- The prefactor n^5 is harmless at a fixed coupling. In the continuum limit n = l/a, and the bound is small only for tori with l above a multiple of log(1/a). That is enough for volume-first limits (infinite volume at fixed spacing, then the spacing to zero), which are the main object of the account.
- Shrinking the domain by 1/n changes omega by a factor exp(-C beta / n), which tends to 1 because beta grows like log n at most.

**Which partition function.** In the confined theory the full Z_n contains the sectors with electric flux, whose energies grow like sigma l. On a torus of complex size l = |l| e^{-i theta} their weights exp(-sigma l^2) have modulus exp(-sigma |l|^2 cos 2 theta), which grows for |theta| > pi/4. So the zeros of the full Z_n accumulate on arg l = +-pi/4, that is on Im beta = +-pi/(4 c_a) = +-11/(12 pi). The zero-free strip of the full partition function has half the width, its harmonic measure decays like a(beta)^2, and transport from the strong-coupling anchor exp(-kappa n^2) of the planar windings gives exp(-kappa' sigma l^2): the area law. This is consistent, and it shows that the glueball gap needs the wider strip. So the object for the gap is the zero-flux partition function of Lemma 1',
Z^(0)_n(beta) = (1/8) sum_{k in Z_2^3} Z_{n,k}(beta),
the average over the three twists in the planes that contain the time direction. Its winding sum has only states of zero flux, and its expected zero-free strip has half-width 11/(6 pi). Theorem Z holds for it with the same proof (|Z_{n,k}(beta)| <= 1 for Re beta >= 0; the bulk free energy is the same).

**A caveat that fixes the form of the hypothesis.** Tori of physical size near 1/T_c feel the deconfinement crossover in all four directions (K6). I expect the universal function E(l) = lim Z^(0) exp(-l^4 f_inf) to have zeros at complex l of modulus near that size. In the beta-plane such zeros sit at Re beta = (1/c_a) log(n / |l_*|), Im beta = -arg(l_*)/c_a: they move to the right as n grows, at a fixed height that can be well inside the strip. So (ZF) cannot hold in the full strip for all n. It must be stated for tori that are physically large at the coupling in question:

**(ZF-L), the crux in its final form.** There are a domain D (the strong-coupling disc, a tube around the positive real axis, and for Re beta >= beta_1 the region between the curves on which the two-loop scale function a(beta) is imaginary), a size l_0, and n_0, such that Z^(0)_n(beta) != 0 whenever beta is in D and n |a(Re beta)| Lambda >= l_0 (for Re beta >= beta_1), respectively n >= n_0 (for Re beta < beta_1).
Theorem Z then applies on D cut at the coupling X_n where the torus n has size l_0. For real beta <= X_n - s the harmonic measure in the cut domain is at least eps a(beta)(1 - C e^{-c_a s}).

**Corollary 5 (the conditional theorem in final form).** (TM), (SC) and (ZF-L) imply: there are m > 0 and C such that, for every real beta >= beta_1 and every n in a doubling sequence with n a(beta) >= C log(1/a(beta)), the Hamiltonian of the box n^3 in the zero-flux sector has a simple lowest eigenvalue and no other spectrum below m in physical units. So every infinite-volume limit at fixed beta of these tori has exponential decay of the truncated functions of contractible-loop observables at rate m in physical units, uniformly in beta.

**The three parts of (ZF-L) and their kind.**
- (ZF-x): beta in the tube over [r_0, beta_1], all n >= n_0. No transition on the Wilson axis between strong coupling and the perturbative region. Non-perturbative, qualitative, specific to the Wilson action (K7). This is where the approach can die.
- (ZF-s): Re beta >= beta_1, torus physically large. By the exact renormalisation map this reduces to zero-freeness of the torus partition functions of the unit-scale effective actions over one period of the flow, inside the strip. True for a massive infrared theory and for a scale-invariant one alike. It is a regularity statement, not the gap.
- The small tori are not needed at all (they are cut away).

**Attack on (ZF-L) in this run: summary.** Proved: the transport theorem with zero-freeness as the only hypothesis. Not proved: any zero-free region beyond the strong-coupling disc. The three failed ways are those of 1.7 (trivial modulus bounds give width n^{-2}; complex Perron-Frobenius gives width 1/volume; no positivity in the dual expansion). A fourth: real cluster bounds give an analyticity radius of order (correlation length)^{-4}, and then the transport gives the differential inequality d(m^4)/d beta >= -C, which reaches zero at a finite beta. It is consistent with a transition and proves nothing. In the scaling region the true radius is of order 1 because an insertion of the total action is a dilation; that is an identity, not a bound, and it is not available in the crossing region.

**Final verdict of Part 1 (replaces the last paragraph of 1.8).** The chosen approach is A13 on the zero-flux partition function: (ZF-L), then Theorem Z, then Lemma 1'. I have no proof of (ZF-L), and I judge that no known structure gives (ZF-x) by hand. The conditional theorem is nevertheless a sharp one: its single hypothesis is that explicit entire functions have no zeros in an explicit region, it fails exactly where the known counterexamples fail, and it reproduces the scaling of the mass and of the string tension from the widths 11/(6 pi) and 11/(12 pi) of two strips.

## Part 2. The literature (read after Part 1 was written; Part 1 is not changed after this point)

### 2.0 Repo search and sources

Repo search (rule "repo first"). I read `library/prior/gap-prior.md` (row 655: seven branches of this repository and the main documentation), `library/prior/gap-lit.md` (row 656) and `library/prior/gap-lit-2.md` (row 661) in full, except the list of file names in gap-prior lines 31-94. I searched `library/open-core.md` and the FINISH rows (without rows 662 and 669) for: Fisher, zero-free, Lebowitz, two constants, harmonic measure, excess free energy, Perron, twist, strong coupling, mass gap. `open-core.md` has no hit. The FINISH hits that matter are row 667 (`gap-transfer`: the transfer operator, its positivity, trace class, Perron-Frobenius; this is my input (TM), I do not attack it) and row 668 (`gap-os-equiv`: decay against spectrum and the passage to a limit; I do not attack it). One repository note is close to A13: `docs/SU3_BETA6_GAP_BULK_CRITICALITY_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-09.md` on branch `claude/su3-beta6-gap-reduction-2026-06-09` (read: lines 36-110). It states: "If no second-order bulk critical point lies on the 4D SU(3) fundamental-Wilson axis in (0, 6], then the strong-coupling gap (R1) persists to beta = 6". Its argument is by definition of the correlation length ("m(6) = 0 requires xi -> infinity at some beta*"), with no analytic hypothesis and no rate, and it allows first-order transitions. Theorem Z is a different statement: its hypothesis is the absence of zeros in a complex region (this excludes first-order transitions too), and its conclusion has a rate.

Sources, each marked.
- READ (TeX source, abstract and lines 33-40, 76-96, 112-124, 146-166): A. Denbleyker, D. Du, Y. Liu, Y. Meurice, H. Zou, "Fisher's zeros as boundary of renormalization group flows in complex coupling spaces", arXiv:1005.1993.
- READ (abstract only): arXiv:1112.2734 (Denbleyker, Bazavov, Du, Liu, Meurice, Zou, "Fisher's zeros, complex RG flows and confinement in LGT models"); arXiv:1210.6969 (Meurice and others, "Fisher zeros and conformality in lattice models"); arXiv:0810.1792; arXiv:0708.0438; arXiv:2111.04809 (Regts, "Absence of zeros implies strong spatial mixing"); arXiv:1807.06577 (Liu, Sinclair, Srivastava, "Fisher zeros and correlation decay in the Ising model"); arXiv:2307.07619 (Bauerschmidt, Bodineau, Dagallier, "Stochastic dynamics and the Polchinski equation: an introduction"); arXiv:2204.12737 (Shen, Zhu, Zhu); arXiv:2202.10375 (Adhikari, Cao).
- READ (passages of the HTML that name Guth and Froehlich-Spencer): Chatterjee, "Yang-Mills for probabilists", arXiv:1803.01950.
- TITLE AND AUTHORS CONFIRMED BY CROSSREF, STATEMENT NOT READ: Froehlich and Spencer, Comm. Math. Phys. 83 (1982) 411-454, "Massless phases and symmetry restoration in abelian gauge theories and spin systems"; Lebowitz and Penrose, Comm. Math. Phys. 11 (1968) 99-124, "Analytic and clustering properties of thermodynamic functions and distribution functions for classical lattice and continuum systems"; Guth, Phys. Rev. D 21 (1980) 2291, "Existence proof of a nonconfining phase in four-dimensional U(1) lattice gauge theory"; Bhanot and Creutz, Phys. Rev. D 24 (1981) 3212, "Variant actions and phase structure in lattice gauge theory"; Luescher, Nucl. Phys. B 219 (1983) 233, "Some analytic results concerning the mass spectrum of Yang-Mills gauge theories on a torus". The Springer pages returned a bot check; I stopped there.
- NOT READ, FROM MEMORY ONLY: Osterwalder-Seiler; Luescher's transfer-matrix paper; 't Hooft's flux papers; Tomboulis-Yaffe; Mack-Petkova; Simon (discrete spectrum of -Delta + x^2 y^2); Singer; Dell'Antonio-Zwanziger; Beraha-Kahane-Weiss; Dobrushin-Shlosman; Lebowitz-Penrose 1974 and Guerra-Rosen-Simon (Lee-Yang zeros and the mass gap in a field); Rugh (complex cones); Svetitsky-Yaffe; Kupiainen (large N); Goepfert-Mack; Luescher-Weisz-Wolff; van Baal; Krauth-Staudacher; the results on the Kannan-Lovasz-Simonovits problem.

### 2.1 Corrections to Part 1

- **K5.** What I could confirm is weaker than what Part 1 uses. Chatterjee's survey (read) says: "Guth [53], who showed that four-dimensional U(1) lattice gauge theory fails to satisfy the area law at large beta. A fully rigorous proof of Guth's theorem was given by Froehlich and Spencer [44]." So the confirmed fact is: no area law at weak coupling. The stronger fact that Part 1 uses in the U(1) tests (a massless photon, energy 2 pi / l in a box, power-law decay of plaquette correlations) is what the title of Froehlich and Spencer announces; I did not read its statement. arXiv:1112.2734 (abstract, numerical) says for U(1) that "the zeros pinch the real axis near beta = 1.0113". The U(1) tests of A1 and A13 stand on these two unread or numerical items. Label: K5 in its massless form is recalled, not verified here.
- **K7.** Crossref confirms the Bhanot-Creutz paper by title. arXiv:1112.2734 (abstract) says "We discuss the effect of an adjoint term on these results." The end point itself stays recalled.
- **A13 is not new as a picture.** See 2.2. Part 1 said "the only approach in the list in which ... asymptotic freedom enters as the shape of a domain". The shape (a fixed height of the singular points, equal to pi/2 times the asymptotic-freedom coefficient) is already in arXiv:1005.1993 for the O(N) model at infinite N.
- **The Lebowitz-Penrose attribution** in 1.7 is from memory. Theorem LP as I state and prove it does not depend on it.
- **Shen-Zhu-Zhu.** The abstract (read) gives SU(N): |beta| < 1/(16(d-1)) with 't Hooft scaling N beta. For N = 2, d = 4 and my normalisation this is beta < 1/12. My own crude bound in 1.4 is beta < 1/15. Same mechanism (Bakry-Emery), theirs is sharper and comes with the infinite-volume statements.
- **The two-dimensional bound** |I_k/I_1| <= 1 was already corrected inside 1.7 by a numerical check before Part 2.

### 2.2 Each approach against the literature

- **A1 (excess free energy).** Lemma 1, 1', 2 and the criterion: not found in the sources read. The ingredients are standard (trace of powers of a positive operator; the integral of the plaquette over beta is the "integral method" of lattice thermodynamics, from memory). I did not search further than the three digests and two arXiv queries, so I do not say new.
- **A2 (exit domain).** Used: the standard programme. Where it stopped: the crossing region. `gap-prior.md` reports the same stop in this repository ("strong-coupling lattice contraction is separated from the weak-field construction by an unproved original-law crossover"). Tomboulis (arXiv:0707.2179) claimed to cross it with Migdal-Kadanoff bounds; Ito and Seiler (arXiv:0711.4930, both read in `gap-lit-2.md`, not by me) "say Tomboulis's argument relies on an unproved claim". My version does not pass that point.
- **A3 (functional inequalities).** Used at strong coupling by Shen, Zhu and Zhu. The multiscale criterion exists (Bauerschmidt, Bodineau, Dagallier; abstract read: "a renormalisation group perspective on log-Sobolev inequalities"). `gap-lit-2.md` section 10: "A theorem of that requested functional-inequality type: not found in the sources read" outside the strong-coupling range. My version does not pass the threshold.
- **A4 (transport in beta).** Not found in the sources read. It dies in Part 1.
- **A5 (step scaling).** Used numerically (from memory). `gap-lit-2.md` section 1: a rigorous small-torus gap theorem "not found in this search". My version adds nothing rigorous beyond Proposition 3.
- **A6 (flux duality).** Used by 't Hooft, Tomboulis-Yaffe, Borgs-Seiler (abstracts read in `gap-lit-2.md`; inequalities not recovered there). Chatterjee (arXiv:2006.16229, read in `gap-lit-2.md`): exponential decay under arbitrary boundary conditions implies the area law when the centre is non-trivial. That is the direction from the gap to confinement, with a stronger gap hypothesis than (GAP). My sector split in 1.9 (strip of half-width 11/(12 pi) for the flux sectors) is not found in the sources read.
- **A7, A8 (orbit space, Gribov region).** From memory only; no source read. No claim.
- **A9 (correlation inequalities).** For Z_2 the random-current method works (Forsstroem-Viklund, in `gap-lit.md`). For SU(2): not found.
- **A10 (dilation identity).** Standard in physics (from memory). No theorem found.
- **A11.** Three-dimensional U(1) only (from memory).
- **A12.** Refuted in Part 1 by the U(1) Gaussian computation. Not searched.
- **A13 (zeros in the complex coupling).** This has a clear precedent in physics. Denbleyker, Du, Liu, Meurice and Zou (arXiv:1005.1993, read): "We argue that the Fisher's zeros are located at the boundary of the complex basin of attraction of infra-red fixed points", and "We present numerical evidence that, as the volume increases, the Fisher's zeros of 4-dimensional pure gauge SU(2) lattice gauge theory with a Wilson action, stabilize at a distance larger than 0.15 from the real axis in the complex beta=4/g^2 plane. We discuss the implications for proofs of confinement". For the O(N) model at infinite N they find that "the imaginary part stabilizes at (pi/2)(1/(4 pi)) = 1/8 as can be inferred from" the asymptotic-freedom formula, and "This stabilization implies that the complex RG flows on the positive real axis and the neighboring complex flows can reach the strongly coupled fixed point without obstruction." Their sentence on the strategy: "If these RG flows end at the strongly coupled fixed point, the correlations among local observables decay exponentially with the separation (mass gap) and Wilson loops decay exponentially with their area (confinement). Showing rigorously that this statement correct is a possible strategy [Tomboulis] to prove confinement". arXiv:1112.2734 (abstract): "For SU(2), these zeros appear to move almost horizontally when the volume increases. They stay away from the real axis which indicates a confining theory at zero temperature." arXiv:1210.6969 (abstract): "a gap signals confinement".
 Where they stopped: numerical evidence on 4^4 and 6^4 lattices, and the heuristic that a gap in the zeros lets the flow reach strong coupling. In the passages I read there is no theorem from the absence of zeros to decay.
 Does my version pass that point? Yes, by one exact step: Theorem Z (subharmonicity of log|f_n - f_inf|, bounds from positivity on the real axis and Harnack, the strong-coupling anchor, the two-constants theorem), followed by Lemma 1'. It turns "no zeros in D" into a lower bound for the mass, equal to the harmonic measure of the strong-coupling circle. It does not prove the absence of zeros. Their numbers agree with the caveat of 1.9: the zeros of small symmetric lattices sit at height about 0.15 to 0.18, below both 11/(12 pi) = 0.29 and 11/(6 pi) = 0.58, and they move "almost horizontally" with the volume, as zeros of a universal function of the physical size must.
 The step from zeros to decay itself has rigorous precedents in other models: Lebowitz and Penrose (not read); Liu, Sinclair and Srivastava for the Ising model, in the other direction ("no Fisher zeros in a complex neighborhood of the entire region of parameters where the model exhibits correlation decay", abstract read); Regts ("absence of complex zeros of the partition function of the hard-core model ... implies ... strong spatial mixing", abstract read). For lattice gauge theory in the coupling variable: not found in the sources read.

### 2.3 Mechanisms in the literature that Part 1 lacks

- **A large number of components as the small parameter in the crossing** (Kopper, Magnen, Rivasseau for the Gross-Neveu model, abstract read in `gap-lit-2.md`: "for a large but finite number of fermion components ... the fermion two-point function decays exponentially"; Kupiainen for O(N), from memory). Tests: it needs N large; SU(2) has no such parameter. It is the only rigorous dynamical mass generation in an asymptotically free model that the digests report. U(1) test: not applicable. Known answers: correct where it applies.
- **Stability of a gap under local perturbations for frustration-free Hamiltonians** (Bravyi, Hastings, Michalakis; used by the repository's truncated strong-coupling note, `gap-prior.md` lines 97-110, status there: cited, rebuild open). Tests: works for U(1) as well; strong coupling only. It does not cross.
- **Random surfaces at every beta** (Cao, Park, Sheffield, in `gap-lit.md`): a representation, with signs, no decay.
- **Decay under arbitrary boundary conditions as the hypothesis** (Chatterjee's strong mass gap). It is the right hypothesis for stability arguments (complete analyticity). Theorem Z uses periodic tori only; a version for all boundary conditions is a later item.
- **Finite groups at weak coupling** (Adhikari, Cao: abstract read). The anchor is at beta = infinity. In the frame of A13 this is transport from the other end of the axis, in a domain that does not contain the transition.

### 2.4 A numerical guide run after the literature: the strip law in a hierarchical model

Purpose. The strip widths of 1.9 are heuristics. I tested the one for an area-law quantity in a model where everything can be iterated: the Migdal-Kadanoff recursion for SU(2) in four dimensions with scale factor 2 (bond moving F -> F^4, then decimation of the character coefficients a_k -> a_k^4), started from the Wilson weight at complex beta. In such a model the zeros of the partition function are the boundary of the basin of the strong-coupling fixed point (recalled; the picture of arXiv:1005.1993). The runs prove nothing. Scripts `mk4.py`, `mk4c.py`, `mk4d.py`, `mk4e.py`, `mk4f.py` are in my scratch folder, run under the numeric lock at 56 percent memory free, peak memory below 0.3 GB.

Results, with the criteria as I wrote them before each run.
1. Real flow. The effective coupling (defined by matching the first non-trivial coefficient to I_2/I_1) drops by D = 0.2515 per step at beta = 12, 16, 20, constant to three digits after two steps. So in this model a(beta) is proportional to 2^{-beta/D} and c_a = ln 2 / D = 2.756. (The true one-loop value is 2.692.)
2. Prediction. The string tension is proportional to a^2, so the strip law says: zeros first appear at height pi/(4 c_a) = pi D/(4 ln 2) = 0.2850.
3. First criterion (written first): "y_max(x), the first height at which the flow fails to reach strong coupling, tends to 0.285 within 15 percent". Outcome: FAIL as written. For Re beta = 6 to 16 the flow reached strong coupling for every sampled height up to 0.9. The observable was wrong: the set where the flow fails is thin, and a grid misses it.
4. Second criterion (written after seeing 3; so it is not blind): "over one period of Re beta the lowest failing height lies in [0.15, 0.40]". Outcome: 0.4375 at Re beta in [8, 8.25] with steps 0.0063 by 0.0125. Not in the window. Inconclusive for the same reason.
5. Third observable (chosen after 3 and 4; not blind): the number of steps the flow needs to reach strong coupling, on 500 values of Re beta over one period, at fixed heights. At heights 0.10, 0.20, 0.25, 0.26 the count is constant within one step and no point is delayed. At height 0.27 thirty points are delayed by 3 steps or more; at 0.28 and 0.29 some points do not converge at all. The same onset, between 0.26 and 0.27, appears at Re beta in [8, 8.25] and in [12, 12.25].
What this supports, and what it does not. The onset height 0.265 is 7 percent below the predicted 0.285, it does not depend on Re beta, and it is on the side that the transport theorem requires (a wider zero-free tube would give a lower bound above the true string tension). Thin vertical sets of zeros that reach down to height h make the effective width a little larger than h, which is the sign of the deviation. So the strip law, and the sharpness of the transport bound, are supported in a hierarchical asymptotically free model, at the level of a guide. It is not a test of the lattice theory: a hierarchical model has only discrete scale covariance, and it flows to strong coupling for every group, U(1) included.
A structural point that the run made clear and that holds for the lattice theory as well: where the renormalisation map is a translation of beta, the zero-free region is invariant under that translation. So in the scaling region it is a strip of constant width, and the width is fixed by one period. This is the reduction used in (ZF-s).

## Part 3. The skeleton

### 3.1 The chosen approach: zeros of the zero-flux torus partition function (A13 with A1)

Labels: PROVED (where, checked by whom), IN LITERATURE (reference, read or not read), IN REPO (row), OPEN, FALSE. "Proved here" means: written in this file by this author run, not checked by another model.

Object (Part 0): the Wilson SU(2) measures on tori at first-passage data (K, beta), their limits at fixed spacing as the torus grows (periodic Gibbs states), and the continuum limits of those (volume-first limits), under the existence estimates of the account.

| Node | Statement | Standing |
|---|---|---|
| N0 | The existence estimates of the account (packages A-F, in particular D1) | OPEN in the account ("Those estimates require proofs beyond the finite-dimensional and reference calculations given here", 1921-1925). Our T0 chain works on them. Not a gap node. |
| N1 (TM) | Transfer operator T of a box: positive, trace class, strictly positive kernel, Z = Tr T^n, simple top eigenvalue | IN REPO: FINISH row 667 (`library/gap-transfer.md`, not opened by me; its check is row 671). IN LITERATURE: Luescher; Osterwalder-Seiler (not read). |
| N2 | Twisted partition functions: Tr(T^n C^k) = Z_{n,k}; the centre flips C_i commute with T and fix the ground state; contractible-loop observables preserve the zero-flux subspace | IN LITERATURE ('t Hooft, not read). The three facts are one-line checks given N1. OPEN as a written proof (routine). |
| N3 | Lemma 1 and 1': 1 + S^(0)(n_1) <= exp(Delta^(0)); the gap of the box is at least (1/n_1) log(1/(exp(Delta^(0)) - 1)) | PROVED here (1.5), given N1, N2. Not checked. |
| N4 | Lemma 2: Delta(n; beta) = 6|n| int_0^beta (abar_inf - abar_n) | PROVED here (1.5). Not checked. Not used by the main line; it is the bridge to the account's observable. |
| N5 (SC) | For |beta| <= r_0, complex: |log(Z^(0)_n(beta) exp(-n^4 f_inf(beta)))| <= C_0 n^4 exp(-kappa_0 n), kappa_0 = 4 log(1/(c r_0)) | IN LITERATURE as a method (convergent strong-coupling expansion, Osterwalder-Seiler, not read). OPEN as a written proof with the winding count (routine to hard). |
| N6 | Theorem LP (two constants) and Lemma HM (half-strip) | PROVED here (1.7). Classical. Not checked. |
| N7 | Theorem Z: no zeros of Z^(0)_n in a tube D implies Delta^(0)_n(beta) <= C(1+X) n^5 exp(-kappa_0 omega_n(beta) n) on the real axis | PROVED here (1.9), given N1, N5, (TUBE). Not checked. |
| N8 (HM-AF) | For the domain bounded by the curves on which the scale function a(beta) of the account is imaginary: omega(beta) >= eps a(beta) on the real axis | OPEN (complex analysis: comparison of two positive harmonic functions that vanish on the sides; needs the two-loop form of a(beta) from the flow package of the account). Routine to hard. |
| N9 (ZF-x) | No zeros of Z^(0)_n(beta), n = 2^k n_0, in a complex neighbourhood of [r_0, beta_1] | OPEN. **This is the node where the approach dies if it dies.** Numerical evidence for the full Z on 4^4 and 6^4: arXiv:1005.1993 (read). False for U(1), for Z_2, at fixed short time side, and at the end point of the fundamental-adjoint action. Equivalent real form (CUM-x): the cumulants of the total action satisfy |kappa_k| <= 6 n^4 k! C^k uniformly in n and in beta in [r_0, beta_1]. |
| N10 (ZF-s) | For Re beta >= beta_1 and tori of physical size at least l_0: no zeros of Z^(0)_n in the asymptotic-freedom tube | OPEN. Reduces by the renormalisation map to one period. Needs N0 at complex coupling (the account has complex sources of fixed radius) and a regularity statement for the infrared theory under complex dilation. Supported by the hierarchical guide (2.4), by the O(N) computation of arXiv:1005.1993, not by any proof. |
| N11 | Corollary 5: uniform gap m > 0 in physical units for the zero-flux sector of boxes with n a(beta) >= C log(1/a(beta)) | Follows from N3, N7, N8, N9, N10. |
| N12 | Infinite volume at fixed spacing: every limit of these tori has truncated functions of positive-time observables bounded by ||[F]|| ||[G]|| exp(-m t), with the reflection-positivity norms | IN REPO as an interface: FINISH row 668 (`library/gap-os-equiv.md`, not opened). OPEN for the identification of the limits of tori with the periodic Gibbs states that the account uses for volume-first limits (the account takes "a limit point of the periodically extended torus measures", 1677-1680: same objects). |
| N13 | Continuum: the bound of N12 is uniform in the cutoff, the norms ||[F]|| are bounded by the account's (c)(2), so every volume-first limit satisfies (GAP-E) with rate m | Routine given N12 and N0 (limits of Laplace transforms of positive measures with support in {0} union [m, infinity)). OPEN as a written proof. |
| N14 | (GAP) for each canonical component, and the decomposition is trivial (W7) | Follows from N13: a state whose truncated functions tend to zero is ergodic. Routine. OPEN as a written proof. |

The node where the approach dies: N9. If the Wilson SU(2) theory had a transition on (r_0, beta_1), N9 would be false and the gap could still hold on the far side by scaling from another anchor; then this approach proves nothing. If N9 is true, I know no way to prove it by hand.

Results short of the full gap that would be new theorems, in the order of what they need:
1. N7 with N3 as a theorem on lattice gauge theory at a fixed coupling: "if the zero-flux partition functions of the symmetric tori have no zeros in a complex neighbourhood of [0, beta], the transfer operator has a gap at beta, with a rate given by a harmonic measure". Needs N1, N2, N5 only. Not found in the sources read.
2. Proposition 3 and (W2): the continuum Hamiltonian in a finite periodic box has discrete spectrum. Needs N0, (V-ext), and the cylinder limit.
3. The upper bound for the gap, (8 + o(1))/r for r in the window where the coupling is small (1.5). Needs N0 only.
4. Corollary 5 for a fixed beta_1 beyond the strong-coupling disc: any explicit complex zero-free neighbourhood of an interval [0, beta_1] with beta_1 above 1/12 would give a lattice gap at a coupling where none is proved.

### 3.2 The second approach, which fails in a different way: multiscale functional inequality (A3)

| Node | Statement | Standing |
|---|---|---|
| M1 | Ric + beta Hess A >= 2 - 30 beta on (S^3)^{links}; Poincare inequality uniform in the volume for beta < 1/15 | PROVED here (1.4). Not checked. Sharper and with more conclusions: Shen, Zhu, Zhu (abstract read). |
| M2 | A multiscale criterion: one-sided Hessian bounds on the renormalised actions give a log-Sobolev constant | IN LITERATURE (Bauerschmidt, Bodineau, Dagallier; abstract read). Not for gauge fields with hard block constraints: OPEN. |
| M3 (HESS) | The bounds of M2 along the flow, with a finite total negative part through the crossing and a positive end value | OPEN. **Dies here**: no bound for effective couplings between about 1/15 and about 40. |
| M4 | From the four-dimensional Poincare constant rho to decay at rate sqrt(rho), not rho | OPEN (a weighted estimate for the Witten Laplacian on 1-forms). Without it the continuum limit is lost even if M3 holds. |
| M5 | (GAP) | Would follow from M2-M4 and N12-N14. |

A3 dies by a threshold and a rate. A13 dies by a zero of an entire function. A proof of N9 would not help M3, and a proof of M3 would not give N9. That is the sense in which they fail differently.

### 3.3 If no approach has a real chance: the plain statement

I judge that neither tree can be closed by hand with known structures, because N9 and M3 are both statements about the Wilson theory at couplings of order 1, where no expansion has a small parameter and no exact structure is known that U(1) or the fundamental-adjoint action does not share. The best conditional theorem is Corollary 5. Its one hypothesis beyond the existence estimates and routine nodes is (ZF-L) = N9 with N10: the zero-flux partition functions of physically large symmetric tori have no zeros in the tube D.

## Part 4. The queue: the first six proof items

Each item is a text for a queue row. Paths are relative to the lane folder. "This file" is `library/gap-skeleton-max-b.md`. The account is `YM4_1400.tex` at commit 2bc0658f91d2 (Sussman and Alpoge, with Claude and Codex); credit it where it is used. Matches found by the duplicate check: the transfer operator is row 667 and the decay-spectrum-limit interface is row 668; no item below repeats them.

**Item 1, `gap-zf-x` (the crux; hard proof).**
Moves: node N9 of this file, the node where the chosen approach dies or lives.
Statement. Let Z_{n,k}(beta) be the partition function of Wilson SU(2) theory on the symmetric torus n^4 with centre twist k in Z_2^3 in the three planes that contain direction 1 (the sign of beta is reversed on one stack of plaquettes per twisted plane), and Z^(0)_n = (1/8) sum_k Z_{n,k}. Prove or refute: there are r_0 > 0, beta_1 > r_0, an open set U in the complex plane that contains [r_0, beta_1], and n_0, such that Z^(0)_n(beta) != 0 for all beta in U and all n = 2^j n_0. Equivalent real form to prove first (both directions, with constants): (CUM-x) the cumulants of the total twisted-averaged action obey |kappa_k| <= 6 n^4 k! C^k for all k, uniformly in n and in real beta in [r_0, beta_1].
Inputs. This file: Lemma 1' (1.5), Theorem Z steps 1-3 (1.9), the tests K5-K7 (1.1, 1.2), the Hessian bound of 1.4 (Ric + beta Hess A >= 2 - 30 beta). `library/gap-transfer.md` (row 667) for the transfer operator. arXiv:1005.1993 and arXiv:1112.2734 for the numerical picture (zeros of the full Z at height above 0.15 on 4^4 and 6^4, moving horizontally with the volume).
Order of attack. (a) Base: (CUM-x) on [0, beta_BE) with beta_BE = 1/15 from the uniform Poincare and log-Sobolev inequality, through tree bounds on truncated functions. (b) Continuation: from decay with length xi at a real coupling, a zero-free disc of radius c xi^{-4}; then Theorem Z on the tube with the real segment as part of the anchor; write the resulting differential inequality for the mass with its constant, and the largest coupling it reaches. (c) Search for an identity for the integrated action insertion in the crossing region that plays the part the dilation identity plays in the scaling region. Any beta_1 above 1/12 is a new lattice theorem.
Kind: hard proof. Stop rule: a proof with explicit U and beta_1; or a proof that zeros approach the real axis at some coupling in (r_0, beta_1] as n grows; or one named lemma that failed in three ways.
Follow-up for the likely stop (step (b) reaches zero mass at a finite coupling): `gap-zf-x-2`. Statement: for real beta in the range reached by (b), prove the bound sum over p of <F; a_p> <= C ||F|| with C independent of the correlation length for local F in the zero-flux algebra, or show by an explicit family that it fails. Inputs: step (b) of item 1; the Hellmann-Feynman computation of 1.4. Stop rule as above.

**Item 2, `gap-zf-s` (hard proof, with one named hypothesis allowed).**
Moves: nodes N10 and N8.
Statement. (i) Complex first passage: for bare coupling beta = x + i y with |y| <= rho (the source radius of the account), the flow of the account is defined, the scale function a(beta) and the unit-scale effective action are holomorphic in the strip, and the imaginary part of the running inverse coupling differs from y by at most C g^2 at every step down to the unit scale. (ii) Reduction: if the torus partition functions of the unit-scale effective theories with zero flux have no zeros for all complex couplings of one period of the flow inside the tube and all tori of at least l_0 unit cells, then Z^(0)_n(beta) != 0 for all beta in the tube with Re beta >= beta_1 and n |a(Re beta)| >= l_0. (iii) Harmonic measure: for the domain between the curves on which a(beta) is imaginary, omega(beta) >= eps a(beta) for real beta, including the cut at X_n as in 1.9.
Inputs. The account: first passage and the dilation identity (1658-1671), the constants and the source radius (1744-1746), fixed-torus uniqueness and the bi-Lipschitz map of couplings (1826-1833), the source hypothesis (98395-98440). This file: 1.9, 2.4 (translation invariance of the zero-free region). Kind: hard. Stop rule: proofs of (i)-(iii) with the hypothesis of (ii) stated exactly; or a counterexample to (ii); or a named lemma that failed in three ways.
Follow-up for the likely stop (the account's flow is written for real beta and fixes discrete choices by the coupling): `gap-zf-s-2`. Statement: the reference run with frozen choices (the run with theta_k = g^{-2} + c_0 (K-k) of the account, line 1667) is holomorphic in beta on |beta - beta_K| <= rho/4 with the bounds of (i). Inputs: the account, 1667 and clause (d).

**Item 3, `gap-zero-transport-check` (check and completion; routine to hard).**
Moves: nodes N2, N3, N6, N7 from "proved here, not checked" to checked.
Statement. Check line by line, by a model that did not write them: Lemma 1, Lemma 1', Lemma 2, Proposition 3 (1.5), the Hessian bound (1.4), Theorem LP and Lemma HM (1.7), Theorem Z and Corollary 5 (1.9). Write the three facts of N2 with proofs (the centre flips commute with T, the trace with a flip is the twisted partition function, contractible-loop observables preserve the zero-flux subspace). Verdict per statement.
Inputs: this file; `library/gap-transfer.md`. Stop rule: a verdict per statement, with each defect's explicit failure.
Follow-up for the likely stop (the shape condition (TUBE) and the cut at X_n): `gap-comb`. Statement: for a strip of half-width H with thin vertical slits {Re beta = x_j, |Im beta| >= h}, x_{j+1} - x_j = D, the harmonic measure of the left end at a real point x is at least c exp(-pi x / (2 (h + C D))). Inputs: Lemma HM; the hierarchical guide 2.4, where the zeros come in this form.

**Item 4, `gap-sc-complex` (routine to hard).**
Moves: node N5, the anchor.
Statement. There are r_0 > 0, c, C_0 such that for all complex beta with |beta| <= r_0 and all n >= 4: f_inf is analytic, and |log( Z^(0)_n(beta) exp(-n^4 f_inf(beta)) )| <= C_0 n^4 (c |beta|)^{4n}. For the sectors with flux: the same with n^2 in the exponent in place of 4n. Give r_0, c, C_0 explicitly.
Inputs: the polymer expansion (Osterwalder-Seiler, to be rebuilt; credited); this file 1.7 (the count: a winding closed surface has at least 4n plaquettes, a planar one n^2). Stop rule: a proof with explicit constants, or a counterexample to the count.

**Item 5, `gap-finite-volume` (routine to hard).**
Moves: result 2 of 3.1, the first unconditional-on-the-gap theorem: discrete spectrum in a finite box.
Statement. Under the source hypothesis of the account at W = 0 and (V-ext) of this file (to be derived from the account's flow package or from our chain), the number of eigenvalues of the lattice Hamiltonian of the box l^3 below E_0 + E is at most exp(l E + C l^4), uniformly in the cutoff (Proposition 3). Then: every continuum limit on the cylinder l^3 x R has a Hamiltonian with discrete spectrum. State what is needed for the cylinder limit to exist.
Inputs: this file 1.5; the account 98395-98413; `library/gap-os-equiv.md` (row 668) for the passage to limits. Stop rule: a proof, or the exact missing input.

**Item 6, `gap-limit-chain` (routine).**
Moves: nodes N12-N14.
Statement. From the conclusion of Corollary 5 (a gap m in physical units, in the zero-flux sector, for boxes with n a(beta) >= C log(1/a(beta))): (i) every limit at fixed spacing of these tori has truncated functions of positive-time contractible-loop observables bounded by the product of the reflection-positivity norms times exp(-m t); (ii) every volume-first limit of the account satisfies (GAP-E) of 0.4 with rate m; (iii) its canonical decomposition has one component.
Inputs: this file 0.4, 1.9; the account 1673-1680, 1777-1782, 1884-1908; `library/gap-os-equiv.md`. Stop rule: a proof, or the exact step where the periodic Gibbs states of the account differ from limits of the tori.

Guides, not proof items (a calculation may guide or refute). (G1) The two-dimensional theory as a complete known-answer check: prove by hand the bound on I_k/I_1 in the domain of 1.7 and run Theorem Z to the end; the answer must be a string tension of order 1/beta. (G2) Fisher zeros of Z^(0) against those of the full Z on small lattices from the density of states: the prediction of 1.9 is that the zeros of Z^(0) lie higher. (G3) The O(N) model at infinite N on a torus, where the gap is known: check that the transport bound is sharp.
