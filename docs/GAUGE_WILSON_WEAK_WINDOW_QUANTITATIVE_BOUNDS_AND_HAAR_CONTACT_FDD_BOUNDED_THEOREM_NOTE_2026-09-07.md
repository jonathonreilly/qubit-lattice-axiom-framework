---
claim_id: gauge_wilson_weak_window_quantitative_bounds_and_haar_contact_fdd_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/gauge_wilson_uniform_weak_scaling_controls_2026_09_07.py
upstream_dependencies: ["docs/GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md", "docs/GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md", "docs/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md", "docs/GAUGE_WILSON_SELECTED_INFINITE_STATIC_SOURCE_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-07.md"]
claim_scope: "Partial salvage: quantitative uniform-window estimates, actual Haar contact FDD, conditional gap/LR ratio and optional Haar moments. Original separated-field negative certification deferred under N1."
negative_certification_status: deferred
---

# Quantitative weak-window bounds and Haar contact FDD: partial salvage

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

This note retains the displayed quantitative clustering and weighted-smearing estimates, the actual positive Haar contact finite-dimensional distributions, and the conditional gap/Lieb–Robinson ratio. The optional third/fourth moments and finite-mesh skew formula are preserved in full below. These are conditional results for supplied model, norm, mesh and time choices.

**Deferred:** the original separated-field exclusion has not met the current N1 negative-certification requirement. Its mathematical argument is not disproved, but this partial salvage does not certify that classification or rename it as a positive theorem. The complete original exclusion proof is preserved exactly in the [recovery archive](work_history/review_loop/pr8030/README.md); its branch must remain available under the partial-salvage disposition.

## Actual mathematical inputs

- [compact Hamiltonian source](GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md).
- [volume-uniform gap source](GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md).
- [local-observable approximation and locality source](GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md).
- [selected infinite static-source sector source](GAUGE_WILSON_SELECTED_INFINITE_STATIC_SOURCE_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-07.md).

Use the same whole-range neutral state and the direct Yarotsky0411042 equation16 import stated below; no periodic-boundary identification is introduced. Original authorship, exposure, timing and independence statements in the recovery packet are historical.

## 1. One consistent supplied model and a uniform window

Take the compact SU3 cubic-link Hamiltonian already specified in the campaign, with a>0, v>=0, u=av, all fixed elementary plaquettes, and full link Hilbert spaces. The parameter a is a supplied kinetic/temporal-scaling parameter, not spatial spacing. Spatial spacing ell>0 is introduced independently as an embedding of the unchanged combinatorial lattice into Euclidean space. Parameters a_ell,v_ell may vary, but assume 0<=u_ell<=u_* in ONE sufficiently small fixed window.

Use the selected neutral ground state from the fixed whole-range finite restrictions of Yarotsky0411042 Theorem2. Section2 equation16 gives exponential connected correlations for this same state; its constants can be chosen uniformly by fixing the activity/decay parameter first and choosing u_* below the corresponding smallness threshold. In outgoing-cell scaled units the onsite operator h_z=(a/4)K_cell,z is independent of a, while the centered perturbation has norm at most3u/4. Hence arbitrary variation of a does not change this uniform ground-state bound. Explicit primary source: https://arxiv.org/pdf/math-ph/0411042 , equation16 and its Section2 convention that the decay parameter can be fixed by uniformly small perturbation norm.

Thus there are fixed C>=1 and mu>0 such that for bounded local operators supported on finite cell sets I,J,

 |omega_ell(AB)−omega_ell(A)omega_ell(B)|
 <= C^(|I|+|J|) ||A|| ||B|| exp(−mu dist(I,J)).       (1)

The distance is a fixed lattice metric, with fixed geometric conversion to Euclidean cell positions. For the usual nearest-neighbor metric it dominates Euclidean separation of cell centers. Any fixed-range metric changes mu by a constant only.

Independently, Yarotsky0412040 Theorem1(3)/Section2 supplies the analogous result for its periodic-selected ground state after the four-cell classical-block applicability map. https://arxiv.org/pdf/math-ph/0412040 . That is a separate version. No identification of two boundary-selected representations is required here: use0411042 directly when combining(1) with the reviewed gap/GNS model. Neither pointwise analyticity in u nor a family of nonuniform clustering estimates suffices for the theorem below.

## 2. Quantitative fixed-support estimate at positive physical separation

Let A_ell,B_ell have at most m_A,m_B cells of support, lying within fixed lattice radii D_A,D_B of cell centers x_ell,y_ell. Suppose their physical centers ell x_ell,ell y_ell approach different points at Euclidean separation r>0. For sufficiently small ell,

 dist(I_ell,J_ell)>= r/(2ell)−D_A−D_B.

If ||A_ell||<=K_A ell^(−p) and ||B_ell||<=K_B ell^(−q), with fixed finite p,q>=0, (1) implies

 |connected(A_ell,B_ell)| <= K ell^(−p−q) exp(−mu r/(2ell)).       (2)

For every fixed M>=0 the right side is o(ell^M). Indeed setting s=1/ell reduces the logarithm to (p+q+M)log s−(mu r/2)s, which tends to minus infinity. Multiplicative field renormalizations of polynomial growth are included in the norm hypothesis. Subtracting scalar counterterms does not affect the connected correlation; the hypothesis may instead be imposed on chosen representatives modulo scalars.

The estimate above is retained; certification of the original separated-field exclusion is deferred under N1. It does not bound truly unbounded local operators merely from their formal names or low-state moments. Operator-norm control, or a separate replacement theorem, is necessary.

## 3. Separated smearing sums

Let A_ell(f)=Σ_i alpha_(ell,i) A_(ell,i) and B_ell(g)=Σ_j beta_(ell,j) B_(ell,j), finite sums at every ell. Assume each constituent obeys the same uniform support-size/radius and polynomial norm bounds, and all physical centers in the first sum remain separated by r>0 from all centers in the second. Suppose Σ_i|alpha_(ell,i)|<=K_f ell^(−s) and Σ_j|beta_(ell,j)|<=K_g ell^(−t). Bilinearity and the triangle inequality give

 |connected(A_ell(f),B_ell(g))|
 <= K' ell^(−p−q−s−t) exp(−mu r/(2ell))=o(ell^M)

for every M. The number of summands need not be separately bounded: their total absolute weights are what is priced. Ordinary compact-support Riemann sums have polynomial counts and satisfy this condition. We do NOT apply C^(support volume) to the union of all smearing sites, which would discard the useful estimate.

The hypothesis requires two positively separated physical support regions. It says nothing about overlapping smearing regions, coincident-point singularities or distributions supported on the diagonal. More generally the same proof works if the logarithm of all norm/coefficient/support-prefactor costs is o(ell^−1) and the physical support radii shrink to zero; no such broader condition is silently assumed for macroscopic Wilson loops or volume-supported observables.

## 4. Actual Haar contact finite-dimensional distributions

At u=0 the neutral ground is product Haar. Choose N=n³ disjoint elementary xy plaquettes anchored at (2i,2j,2k), 0<=i,j,k<n, and set ell=1/(2n). Their physical anchors are(i/n,j/n,k/n) in the unit box. Their link sets are disjoint. Let J_k=ReTr(U_plaquette,k)/3. Haar orthogonality and fundamental center charge give omega(J_k)=0 and omega(J_k²)=1/18. The variables X_k=sqrt18 J_k are independent, centered, bounded by sqrt18, and have variance1.

For a real continuous test function f on the unit box put F_n(f)=n^(−3/2)Σ_k f(k/n)X_k. Its variance is n^(−3)Σ_k f(k/n)², tending to integral f²; for f=1 it is exactly1 at every n. The total coefficient l1 norm is at most n^(3/2)||f||_infinity, polynomial. Separated support regions have zero covariance already at finite n. There is therefore no contradiction with Sections2–3.

One can verify the full commuting Gaussian contact limit without a spectral fit: for coefficients a_(n,k)=n^(−3/2)f(k/n), boundedness and centering give omega(exp(it a X))=1−t²a²/2+O(|a|³), uniformly in k. Here max|a| tends to zero, Σa² tends to integral f² and Σ|a|³ tends to zero. Independence then gives the characteristic-function limit exp[−t² integral f²/2]. Applying the same argument to linear combinations of finitely many f gives the Gaussian white-noise finite-dimensional distributions with covariance integral fg. This is a commuting equal-time finite-dimensional distribution limit inside the actual u=0 model. No tightness or convergence in a topology of random distributions, relativistic quantum field theory, or dynamical limit is asserted.

The retained result here is the actual contact finite-dimensional distribution construction and its displayed bounds. The original separated-field negative classification is not certified by this partial salvage.

## 5. Independent gap and propagation-scale comparison

Use a common smaller weak window in which the reviewed uniform-gap bound and local-observable Lieb–Robinson estimate both apply. Introduce laboratory time tau=b_ell t, with arbitrary supplied b_ell>0. Its Hamiltonian is H_lab=H/b_ell. Write g_ell for its actual neutral excitation gap. The theorem gives only

 g_ell >= G_ell:=2/(a_ell b_ell).

It does not give an upper bound on g_ell. The local-observable source link metric joins links in one elementary plaquette; their midpoint Euclidean separation is at most ell. Consequently its exponential commutator estimate has a valid physical-velocity upper parameter

 V_ell:=32e ell v_ell/b_ell=32e ell u_ell/(a_ell b_ell).

This is a Lieb–Robinson UPPER parameter, not an observed group velocity or an actual speed equality. The ratio of this upper parameter to the gap lower bound is exactly

 V_ell/G_ell=16e ell u_ell <=16e u_* ell.          (3)

Two carefully conditional consequences follow. First, if the ACTUAL rescaled gap is additionally bounded above by a finite M, then G_ell<=M and V_ell<=16e u_* M ell tends to zero. For fixed physical separation and fixed finite laboratory time, the same polynomially norm-bounded local commutators consequently vanish faster than every power: their LR exponent is at most −r/(2ell)+O(1). This conclusion uses the extra upper bound on the actual gap; the uniform-gap lower bound alone does not supply it.

Second, for this LR upper parameter even to remain at least some fixed V_0>0, (3) forces G_ell>=V_0/(16e u_* ell), hence a diverging actual gap lower bound. The original propagation/bounded-gap noncoexistence certification is also explicitly deferred under N1. The preceding quantitative implication is retained with its stated hypotheses; it is not promoted here into a certified negative classification. We do not infer such a speed from the estimate itself. If a_ell b_ell stays bounded below, V_ell already tends to zero directly. If a_ell b_ell is of order ell, the LR upper parameter may stay finite while the gap lower diverges; no contradiction occurs.

No equation a_ell=ell has been introduced. Clock rescaling changes both quantities together and cannot change ratio(3). Energy shifts by the vacuum scalar do not alter the gap; more elaborate sector-dependent subtractions or changed dynamics are outside this simple rescaling statement.


## Full contact proof with explicit remainder constants

This proof is conditional on the supplied u=0 compact-link product Haar ground, spatial mesh and field normalization. Its original candidate-exposure and freeze narrative is historical provenance. No generic central limit theorem is imported.

At u=0 the neutral ground of the electric Hamiltonian is the product constant, so link variables under its expectation are independent normalized SU(3) Haar variables. For each k in Z3 take the positively oriented xy elementary plaquette based at fine-lattice vertex3k. Its four link variables are disjoint from those of every other chosen plaquette: projected unit-square coordinate intervals at distinct multiples of3 do not overlap in an edge, and different z layers also have distinct links. Its holonomy U_k is Haar, because a product of independent Haar matrices and their inverses is Haar. The holonomies are independent as functions of disjoint independent link sets.

Put J_k=ReTr(U_k)/3 and X_k=sqrt18 J_k. The fundamental Haar character chi satisfies integral chi=0, integral chi^2=0 and integral |chi|^2=1. The first follows from nontriviality, the second also follows from multiplication by the SU3 center, and the last is Schur orthogonality. Thus E J=0 and E J^2=(0+2+0)/36=1/18. Consequently E X=0, E X^2=1 and |X|<=B=sqrt18. These are actual plaquette multiplication observables in the electric ground, not abstract independent spins substituted for the model.

Give fine links mesh ell=h/3. The chosen plaquette anchors then have physical positions hk. For real f in C_c(R3), define the finite random variable

 Phi_h(f)=h^(3/2) sum_(k in Z3) f(hk) X_k.

Only finitely many terms are nonzero. They commute as multiplication observables. For any finite family f_1,...,f_m and real t_1,...,t_m set g=sum_j t_j f_j. The joint characteristic function equals the characteristic function of Phi_h(g).

## Explicit Taylor-product proof

Write phi(z)=E exp(i z X), z real. Taylor's integral remainder gives

 |phi(z)-1+z^2/2| <= B |z|^3/6,

because E|X|^3<=B E X^2=B. If |z|<=1/(2B), put w=phi(z)-1. Then |w|<=z^2(1/2+1/12)<=z^2<=1/72. The power-series logarithm about1 is therefore defined, with

 |log(1+w)-w| <= |w|^2/[2(1-|w|)] <= |w|^2 <= z^4.

It follows that

 |log phi(z)+z^2/2| <= (B/6+1/(2B))|z|^3 = (7B/36)|z|^3 <= (B/4)|z|^3.

For sufficiently small h, every z_k=h^(3/2)g(hk) satisfies the threshold. Independence gives an exact product, so summing these small-argument logarithms gives a logarithm of the product and

 |sum_k log phi(z_k) + (h^3/2)sum_k g(hk)^2|
 <= (B/4) h^(9/2) sum_k |g(hk)|^3 = O_g(h^(3/2)).

The last estimate uses a fixed compact box containing supp g: its number of mesh points is at most C_g h^-3 for0<h<=1, while ||g||_infinity is finite. The Riemann sum h^3 sum g(hk)^2 tends to integral g^2. Exponentiation therefore yields the joint limiting characteristic function

 exp[-(1/2) integral_(R3) (sum_j t_j f_j(x))^2 dx].

This is the finite-dimensional centered Gaussian white-noise characteristic functional. A degenerate covariance matrix is allowed if the test functions are linearly dependent. In particular

 Cov(Phi_h(f),Phi_h(g))=h^3 sum_k f(hk)g(hk) -> integral f g.

For disjoint test-function supports the finite covariance is already zero. This gives a nonzero contact/statistical limit while every separated-support connected covariance vanishes.

The O(h^(3/2)) bound is for the logarithmic product error relative to its discrete quadratic form. For arbitrary continuous compactly supported f no O(h^(3/2)) rate is asserted for the Riemann-sum-to-integral error. Only convergence of that latter error is needed. This distinction prevents a false quantitative CLT rate from being attached to arbitrary continuous test functions.

## Scope

The construction is at exactly u=0 with supplied ell=h/3, disjoint plaquette sampling and central-limit normalization. It is a rigorous finite-dimensional distribution limit, not a claim of convergence in a chosen random-distribution topology, a dynamical field, a propagating QFT, physical stochastic noise, or an interacting continuum limit. The Gaussian characteristic function does not supply a time evolution. The construction and its stated FDD scope are retained independently of the deferred negative-classification certification.

Disjoint links are a sufficient independence criterion. Distinct plaquettes alone do not justify applying that criterion; no converse dependence assertion about all overlapping plaquettes is made. Repeating the identical plaquette is an explicit adverse case: the two resulting X variables have covariance1 rather than0.

## Optional exact Haar moments and finite-mesh skew proof

## Actual independent variables

At u=av=0 with a>0, the ground state of the full infinite link model is product Haar. For k in Z3 choose the elementary xy plaquette whose anchor is3k. Distinct selected plaquettes have disjoint link sets, so their holonomies are independent and each is Haar-distributed in SU3. Assign a fine spatial mesh ell=h/3; the selected anchors then have physical positionshk.

Let chi=Tr(U) and X=sqrt18 ReTr(U)/3=(chi+bar chi)/sqrt2. Fundamental Haar orthogonality gives Echi=0, Echi²=0 and Echi bar chi=1, hence EX=0 and EX²=1. Also |X|<=3sqrt2=:M. All selected X_k therefore are identically distributed independent real bounded variables. The independence is exact and comes from actual disjoint links, not an assumed independence of adjacent plaquettes sharing links.

There is an exact non-Gaussian single-cell diagnostic. The SU3 invariant alternating tensor gives Echi³=Ebar chi³=1, and mixed cubic moments vanish by center charge. Thus EX³=1/sqrt2. Likewise3 tensor3=6 plus bar3 gives E|chi|^4=2, while the remaining fourth-order monomials vanish by center charge; consequently EX4=3. Only the first two moments and boundedness are required for the limit below. The determinant/tensor-product identities are analytical Haar inputs, not conclusions inferred from finite arithmetic checks.

## Smeared fields and covariance

For real continuous compactly supported f on R3 define the finite sum

 Phi_h(f)=h^(3/2) sum_(k in Z3) f(hk)X_k.

It has mean0 and covariance

 E[Phi_h(f)Phi_h(g)]=h³ sum_k f(hk)g(hk) -> integral_R3 f(x)g(x) dx,

by the Riemann-sum theorem. The sums are finite for everyh. In particular disjoint-support test functions have covariance exactly0 at every mesh, while a nonzero f has a positive limiting variance. The operator norm is bounded by M h^(3/2)sum|f(hk)|=O(h^(-3/2)), a polynomial budget consistent with the quantitative norm assumptions above. The FDD construction is retained without certifying the original negative classification.

## Direct characteristic-function proof

Let q be any fixed real continuous compactly supported function, including a real linear combination sum_j t_j f_j. Put b_k=h^(3/2)q(hk). For the one-site characteristic function phi(b)=E exp(i bX), Taylor's theorem with a bounded third moment gives

 phi(b)=1-b²/2+r(b), |r(b)|<=M³|b|³/6.

For sufficiently smallh every |b_k| is small uniformly. Using the analytic logarithm near1 and |log(1+z)-z|<=2|z|² for |z|<=1/2, one obtains a constantC_M such that

 log phi(b_k)=-b_k²/2+O(C_M|b_k|³).

There are O(h^(-3)) nonzero summands and q is bounded, so sum|b_k|³=O(h^(3/2)). Exact independence then gives

 log E exp(i Phi_h(q))
 =sum_k log phi(b_k)
 =-(h³/2)sum_k q(hk)²+O(h^(3/2))
 ->-(1/2) integral q(x)² dx.

Exponentiation proves convergence of every joint characteristic function of (Phi_h(f1),...,Phi_h(fn)) to the centered Gaussian characteristic function with covariance matrix integral fi fj. Thus the finite-dimensional distributions converge to Gaussian white-noise statistics. This is a finite-dimensional distribution statement; no topology of random distributions or dynamical field convergence is asserted.

Keeping the exact third moment gives the optional finite-mesh diagnostic

 sum_k log phi(b_k)=-(1/2)sum_k b_k² - i/(6sqrt2) sum_k b_k³ + O(sum_k|b_k|4).

The remainder is O(h³) for fixedq, while the cubic term is O(h^(3/2)); the mesh covariance is retained exactly rather than replacing its Riemann-sum error by an unjustified rate for arbitrary continuousq. This correction is analytical and not fitted from samples.


## No-Go Discipline Gate: DEFERRED N1–N8 applicability record

Both the separated-field exclusion certification and the propagation/bounded-gap noncoexistence certification remain **DEFERRED**. The following applicability record identifies existing mathematics and controls; it does not declare a negative-claim PASS or claim five independent failed in-domain routes.

| Item | Applicability and evidence boundary |
| --- | --- |
| N1 — alternative routes | DEFERRED: the required route coverage is not established. Uniform versus pointwise clustering, pairwise smearing versus applying a support-union prefactor, wrong exponential-series degree, clock direction, the extra actual-gap upper premise, and contact/repeated-plaquette/FDD scope are inference controls, not five failed in-domain mechanisms. |
| N2 — independence of the obstruction | DEFERRED: equation (1) explicitly imports a uniform clustering estimate for the selected state in one sufficiently small fixed window. No claim that this premise is independent of every proposed alternative mechanism is certified. |
| N3 — hidden assumptions | DEFERRED: support sizes, operator norms, positive separation, coefficient budgets, supplied mesh and clock, and the additional actual-gap upper bound are explicit hypotheses. Removing them has not been exhausted. |
| N4 — residual matching | DEFERRED: the positive contact FDD is retained, with overlapping/contact supports distinct from positively separated supports. It does not furnish a physical dynamical limit or certify the residual alternatives exhaustively. |
| N5 — resolution and execution | DEFERRED for negative certification. The scaling program specifies exact series-degree, weighted-budget and clock-ratio arithmetic and adverse checks; uniformity and support-union applicability are analytical checks in the proof. The contact program specifies moment normalization, 27 actual plaquette link sets, repeated-plaquette adversity, and Taylor/logarithm constants and mesh exponent. Its per-element, per-site, per-mode and per-block classes refer only to those finite fixtures; lattice-wide labels do not mean the clustering theorem or FDD limit was executed. These unchanged programs have historical evidence; no new capture has been performed for this draft. Scaling TOTAL18 includes one resource predicate; contact TOTAL13 has a separate resource guard. |
| N6 — partial closure | DEFERRED: the retained bounds and constructive Haar FDD require no new axiom. Changing norm/support assumptions, coupling window, dynamics or the supplied time/mesh relationship would require a separately justified statement, not a convention silently inserted here. |
| N7 — strongest alternative | DEFERRED: the actual contact FDD is a constructive alternative to conflating all statistical limits with separated-field dynamics. It does not exhaust alternatives involving changed hypotheses or interacting/dynamical limits. |
| N8 — prior-cycle consistency | DEFERRED: complete original arguments, controls and failures remain in the exact recovery archive. Their repetition or historical review does not establish the missing current route coverage. |

## Accepted scope and deferred certification

Retained: equations (1)–(3), the weighted pairwise smearing bound with every stated hypothesis, actual u=0 Haar contact FDD and its explicit logarithmic remainder, and the conditional gap/LR scale comparison. No tightness, dynamics, physical speed or coupling selection follows. The original separated-field and propagation/bounded-gap noncoexistence certifications remain procedurally deferred; the listed scope controls are not five independent failed in-domain mechanisms.

The two programs execute finite exact arithmetic and actual finite plaquette-disjointness controls. Analytical clustering, asymptotic estimates and FDD convergence are not numerical executions. Scaling TOTAL18 includes one resource predicate; contact TOTAL13 counts scientific controls, with a separate resource guard.

- [Program gauge_wilson_uniform_weak_scaling_controls_2026_09_07](../scripts/gauge_wilson_uniform_weak_scaling_controls_2026_09_07.py); [current cache](../logs/runner-cache/gauge_wilson_uniform_weak_scaling_controls_2026_09_07.txt).
- [Program gauge_wilson_haar_contact_fdd_controls_2026_09_07](../scripts/gauge_wilson_haar_contact_fdd_controls_2026_09_07.py); [current cache](../logs/runner-cache/gauge_wilson_haar_contact_fdd_controls_2026_09_07.txt).
