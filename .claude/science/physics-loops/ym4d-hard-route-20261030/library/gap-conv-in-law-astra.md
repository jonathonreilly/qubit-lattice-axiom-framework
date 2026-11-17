# Repo search

The lead’s November 8 digest concerns row 531, not CONV. Row 1116 reports no matching CONV theorem on main. I checked main at `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`: `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145` is a different, noncompact covariance comparison; `docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md:79–94` concerns a finite-clock Villain law. PR 10114 at `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `MASS_GAP_LOCAL_BLOCK_ASTRA.md:1–35,106–149` in the soft-route folder, gives a strong-coupling endpoint and one-step witness, not CONV. I did not repeat the lead’s searches of PRs 10133, 10134 and 10141 or read unrelated RG hits. These are bounded source checks, not an exhaustive absence claim.

The existing uniform implications are row 691’s Theorem W (`gap-ds-gauge.md:79–101`) and row 1091’s FST-BD. Both are reused and credited below, not counted as new. Row 691 §2.1 already records the three collar failures of a central-core TV criterion; those failures are prior work, not this row’s stop certificate. Main’s `docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md:390–424,511–545` likewise gives a small-parameter uniform comparison domain and leaves its crossover supplier open.

The closest two-replica hit, found in the final targeted check, is **row 1099’s Proposition SW**, `gap-pinu-ev.md:208–214`, with the hand check in `gap-pinu-ev-check-opus.md:176–185`. It already bounds O(4) covariances by replica-swap connectivity, for pair interactions, fields and pins. The swap cancellation is therefore prior work, credited and reused, not this row’s contribution. Its guide run does not prove failure at the window couplings; the check corrects that overstatement. What those lines do not supply is the integrated compact-cell hyperedge construction (4.2)–(4.7), its quantitative joint-tail condition, or its infinite-state/measurable-observable statement. Those are the additional implication written here. Other replica hits checked in `gap-cuttyp-max.md:114–116,446–457`, `gap-unit-max.md:103–108` and `gap-brainstorm-max.md:399–404` concern planted overlaps or thermal purity, not that implication. No inspected source covers the original H-two/Rbar conversion, and no novelty claim is made for the underlying cluster-exchange method.

Model: this session’s configured Codex model; the runtime has not exposed an exact model identifier. The task requests gpt-6-astra at max effort; this file does not certify a runtime identity that has not been supplied.

Research text only. No audit status, no mass-gap claim, and no computer-assisted proof discharge.

## Plan

1. Read the target prior record first, then GOAL.md, the requested FINISH.md sections, operating rules, and ownership records; determine what remains uncovered.
2. Follow the outline and complete-account indices to the necessary source ranges; verify repository prior hits and record credited inputs.
3. Write and check the first-order coexistence test, including entrywise and two-sample responses in the model’s law.
4. Attempt a precise two-sample implication by coupling and counting bad cells in that law; record any failed proof step explicitly.
5. Analyze a measure-carrying, single-pin-connected restricted supremum and run all mandated hand tests.
6. State the exact proved implication or counterexample stop certificate, its covered limit states, remaining obligations, and one final RESULT line.

## Step 1 — source and ownership check

Step 1 result (reading). HEAD is 21596a191d115fe44f77fdca39c9b503f707b1a7, detached and otherwise clean before this output. The target prior digest is absent. GOAL.md and FINISH.md’s requested rules were read. The November 8 search concerns row 531’s RG suppliers, not CONV; row 1116 explicitly warns against treating it as a target-specific absence result. No CONV owner appears in open-registry.md, open-core.md or l17c.md under the target labels. FINISH assigns conversion to this row 1118 and response supply to row 1119. The latter is outside this attack.

Current main’s SCIENCE_WORKFLOW.md is a map to RULES.md, SETTINGS.md and PROCEDURES.md. Its research procedure supersedes physics-loop as entry point. This task’s explicit one-output/no-commit instructions control delivery. No audit, launch, status edit, separate worker or numerical job has been run. The planning branch was read only. Sources downloaded once into the new empty directory `/tmp/sa-gap-conv-in-law-astra.R3f4I0`: outline and CA-I, both at 31a47c543775.

The uncovered object is the conversion L3, not the response supplier L1/DEC/RESP-TR, and not Sussman–Alpoge’s continuum component decomposition. Continue with exact source checks before choosing a hypothesis.

## Step 2 — source contracts and prior methods

Step 2 result (reading). The requested sections of rows 1115 and 1018, row 1116, row 1091 and both checks, and the route/test tables were read. FST-BD’s hand proof is reusable with the measurable-metric correction. The checks also require periodic distance before taking limits, and do not derive FST-P from an unquantified neutral response. No association-based conversion is imported.

Index-first outline reads: README, chunk 01’s Theorem 0 and spectral-example rows, chunk 04’s G3 rows with neighbours, and obligations 16–30,1467–1482 lead to SA 114–130,580–600,4486–4539. These give component clustering, distinguish polynomial decay from a gap, and identify a polynomial approach to an invariant-field plateau. They do not state this finite-cell exponential criterion. CA-I 2700–2715 expressly excludes clustering and a mass gap from its stated clause. The 4.12–4.19 index was searched for the target/method labels; its RG stage results are different objects. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; credit Tadeusz Balaban for the ultraviolet method behind that account. No Balaban paper was needed or imported.

The candidate below uses a local two-replica *swap defect* and a joint bad-cell tail in the actual law. This is stronger data than the mean TV distance in H-two. It explicitly pays for recombining the rings, where the naive coupling changes law. The result is a conditional mixing theorem, not a verification for Wilson SU(2), nor a claim that Rbar implies it.

## Step 3 — coexistence and entrywise tests

The statement in row 1115 that a first-order point automatically makes its scale-normalized Rbar small needs a proof; phase coexistence alone does not provide that estimate.

### 3.1 The required first-order model — reading input, hand consequences

Take spins θ_x in S¹ on Z², normalized Lebesgue reference, and density with nearest-neighbour factors

```math
 w(\theta_x,\theta_y)=\exp\{\beta J[(1+\cos(\theta_x-\theta_y))/2]^p\}.
```

Aernout van Enter and Senya Shlosman, [Theorem 1, p. 3](https://arxiv.org/pdf/cond-mat/0205455), provide, for sufficiently large fixed p, a coexistence β_c and translation-invariant ordered-bond and disordered-bond Gibbs states μ_o, μ_d. For an ordered-bond indicator e in [0,1], their expectations satisfy m_o>κ(p), m_d<1−κ(p), with κ(p)→1. This existence theorem is a credited, unchecked literature input; it is not re-proved here. Nothing below assumes exponential mixing of either phase. Their paper expressly does not decide the low-temperature correlation-decay question. The smooth finite-p interaction is the test, not a hard constraint or a discrete replacement.

Fix p so κ(p)>3/4 and put Δ=m_o−m_d>1/2. Let μ_α=(1−α)μ_o+αμ_d, 0<α<1. For a finite region Λ_R containing the support of e, let F_R be its exterior sigma-field and K_R(η) its conditional law on a core A containing that support. By the Markov property K_R depends only on the ring. Write

```math
 g_R(\eta)=K_R(\eta)e,
 \quad d_R(\eta,\zeta)=\|K_R(\eta)-K_R(\zeta)\|_{\rm TV},
 \quad \|P-Q\|_{\rm TV}=\sup_E|P(E)-Q(E)|.
```

**Proved given the stated coexistence input:** for independent X,Y with law μ_α,

```math
 \mathbb E d_R(X,Y)\ \geq\ 2\alpha(1-\alpha)\Delta.                 \tag{3.1}
```

Indeed introduce the independent phase labels in the mixture representation. DLR gives E_{μ_o}g_R=m_o and E_{μ_d}g_R=m_d. On either cross-phase label event, Jensen gives E|g_R(X)−g_R(Y)|≥Δ. For e∈[0,1] this absolute difference is at most d_R. The two cross-phase events have total probability 2α(1−α). This proves (3.1), for every R and also for growing cores containing e. No claim that *each* cross-phase ring pair has distance one is needed.

In the balanced coexistence law the mean is >1/4 at every scale. Moreover, for 0<t<2α(1−α)Δ,

```math
 \mathbb P(d_R>t)\ \geq\frac{2\alpha(1-\alpha)\Delta-t}{1-t}.       \tag{3.2}
```

Use d_R≤t on the complement and d_R≤1 everywhere. Thus a small-mean two-sample test with threshold below 1/4 fails in the balanced law, as required.

**Proved:** μ_α does not cluster exponentially on all local observables. Let M_N be the average of translates of e over an N×N square. Conditional variance in the mixture gives

```math
 \operatorname{Var}_{\mu_\alpha}(M_N)
 \geq\alpha(1-\alpha)\Delta^2.                                  \tag{3.3}
```

Translation invariance makes its conditional means m_o,m_d for every N. If all translates of e had a uniform exponential covariance bound, summing that bound over the two square indices would give Var(M_N)≤C/N²→0. This contradicts (3.3). This argument does not need a pointwise limit of the phase covariances, or assert that periodic limits give equal phase weights. The class containing *all mixtures* must include μ_α; a torus-only theorem needs its own selection statement.

### 3.2 A precise entrywise form is false — hand argument

**H-ent-local(ε).** Fix a finite core A. For some large R, replace one ring spin y by an independent reference spin, leaving the entire remaining exterior fixed. Require

```math
 \sup_{y\in\partial\Lambda_R}
 \mathbb E_{\mu\otimes\lambda_y}
 \|K_R(X)-K_R(X^{y\leftarrow t})\|_{\rm TV}^{\,2}<\varepsilon.     \tag{3.4}
```

The same statement with a boundary-count-normalized sum follows. Hypothesis (3.4), even at every sufficiently large R for every fixed A, **does not imply exponential clustering**.

Here is the reason from first principles. It applies to every Gibbs state, including mixtures, for uniformly bounded finite-range continuous interactions with full-support product reference. Let T=∩_R F_R be the completed tail sigma-field. The conditional density of X_A given its full complement is k_A(a;X_{∂A}), with respect to the probability reference λ_A. It is bounded uniformly in both arguments by finite energy. By DLR and the tower identity the density given F_R is

```math
 h_R(a)=\mathbb E[k_A(a;X_{\partial A})\mid F_R].
```

For each a, these conditional expectations converge in L² to h_∞(a)=E[k_A(a;X_{∂A})|T]. One direct proof of this reverse-martingale fact: orthogonal projections onto the decreasing closed spaces L²(F_R) have decreasing squared norms; the squared distance between two projections is their squared-norm difference. They are Cauchy, and their limit lies in every space and has the defining inner products of projection onto their intersection. Boundedness and Fubini therefore give

```math
 u_R:=\int\mathbb E|h_R(a)-h_\infty(a)|^2\,\lambda_A(da)\longrightarrow0. \tag{3.5}
```

A finite change leaves every tail-measurable function unchanged, modulo a common null set. This assertion is legitimate for the resampling law: the law of X^{y←t} is absolutely continuous relative to μ, with density ≤C independent of y and R. To see the bound, condition on X_{y^c}; the one-site Gibbs density r_y relative to λ_y lies in [C^{-1},C] by the bounded number and size of incident interactions. Replacement changes r_y λ_y to λ_y, with density 1/r_y≤C.

Cauchy–Schwarz with λ_A(A)=1 and the triangle inequality now give

```math
 \mathbb E\|K_R(X)-K_R(X^{y\leftarrow t})\|_{\rm TV}^{\,2}
 \leq\tfrac12(1+C)u_R.                                        \tag{3.6}
```

For the two terms in the square difference, subtract h_∞; it is unchanged by the replacement. The changed configuration contributes at most C times the original integral. This proves (3.6), uniformly in y. No convergence rate has been assumed.

Apply (3.6) to the smooth finite-p first-order model of 3.1. Every ε>0 in (3.4) is attained, while (3.3) excludes mixing. The hand deduction is complete, conditional only on the explicitly identified published coexistence theorem. It does not assume either phase has a finite correlation length.

There is a differential version for fixed bounded f on A. On S¹ use the angular derivative D_y. Smoothness at fixed p and bounded degree give bounds, independent of R,y, on D_y g_R and D_y²g_R, by differentiating the normalized finite-cell integral. The one-site conditional density has bounded logarithmic derivative. With h=E[f|T], integration by parts in θ_y gives

```math
 \mathbb E|D_y g_R|^2
 =-\mathbb E[(g_R-h)(D_y^2g_R+(D_y\log r_y)D_yg_R)]
 \leq C_f\|g_R-h\|_2\longrightarrow0.                         \tag{3.7}
```

The tail function h is constant in this coordinate almost everywhere by the same absolute-continuity argument. This is a genuine mean squared single-pin response, and it also misses the phase label.

**Exact limit of this refutation.** Row 1018 defines a different quantity: l² times a sum over two growing faces of squared mixed derivatives of log Z_c. Its Neumann observables move with those faces. Neither (3.5) nor phase coexistence gives the rate needed to beat that growing sum. Thus the assertion in row 1115 §§3.4,5.2 that the first-order model already refutes *that particular* Rbar-to-mixing implication is unsupported. H-ent-local is refuted; H-ent interpreted literally as Rbar below its proposed universal threshold is OPEN here. Replacing that open estimate by “one pin does not move the phase” would be a false discharge.

Step 3 result: the first-order test is explicit; (3.1)–(3.3) prove its two-sample obstruction; (3.4)–(3.7) refute a precise entrywise-in-law criterion. The normalized growing-face criterion has not been decided.

## Step 4 — replica exchange with a local gluing cost

### 4.1 What the cited designs supply, and where the law changes

Credits and primary checks:

- J. van den Berg, [1997, Definition 1 and Theorem 1](https://ir.cwi.nl/pub/2166/2166D.pdf): the interaction is sampled first. The boundary maximum remains *inside* the disorder average. Independent local interactions supply the spatial independence; deterministic Gibbs rings do not inherit it.
- Guy Gielis and Christian Maes, [1995, pp. 831–834](https://fys.kuleuven.be/english/staff/christ/files/pdf/jspuniqueness.pdf): their local parameter maximizes conditional sensitivity before averaging over disorder. Their path proof discards alternate sites and uses independence there. Gibbs ring samples have no such independence. Their (13) bounds the expected **absolute covariance**, not the probability that covariance is nonzero, as row 1116 transcribed it. No numerical threshold from that reading is used here.
- Van den Berg and Maes, [1994, Theorem 1 and proof](https://ir.cwi.nl/pub/1472/1472D.pdf): the next conditional distribution is a mixture over environments determined by the revealed history. The worst-case bound on those environments survives the reveal; an average over the original Gibbs boundary law need not. The paper explicitly distinguishes its finite-spin construction from an extension to uncountable spins.
- Arka Adhikari and Sky Cao, [§3, Definition 3.1 and Lemma 3.2](https://arxiv.org/html/2202.10375v3#S3): two independent samples and a measure-preserving local exchange bound covariance by the exceptional-set probability. This cancellation is already their result. Their gauge construction and weak-coupling estimate use finite groups; neither is imported for SU(2). Below I supply a compact-spin local envelope that makes such an exchange exact, and state the extra law hypothesis it costs.
- Row 1099 (Claude Fable), Proposition SW, and its row 1100 check (Claude Opus): the continuous O(4) pair-interaction swap is already written in this repository. They credit Oliver Redner, Jonathan Machta and Lincoln Chayes for the two-replica cluster method. For a pair factor, the minimum in (4.3) reduces to their invariant closed-edge weight; the present construction extends that local mechanism to the many-ring-variable factors obtained by integrating a cell. No numerical observation from those rows is used as evidence here.

Thus the proof must pay for the *change of joint density*, not just couple two normalized cell laws successfully once.

Two elementary failures locate that cost. If a phase-discordance event B has probability q, then E1_B=q can be arbitrarily small, but P(B|B)=1 and E∏_{i=1}^n1_B=q, not q^n. Neither a history-conditioned success probability nor a path-tail bound follows from one-cell means. Also take two binary ring coordinates with probabilities (1−s)/2 on each of 00,11 and s/2 on each of 01,10. The partial swap (00,11)↔(01,10) changes the product density by the factor s²/(1−s)². Even with a strictly positive law, exchanging part of independently drawn rings does not preserve that law. This is a failure of the proposed swap step, not a counterexample to the theorem below. Row 691’s separate collar obstruction remains credited prior work.

### 4.2 The alternative hypothesis H-swap — definition

This criterion concerns uniformly bounded finite-range, strictly positive continuous interaction weights with compact metric one-site spaces and full-support product probability reference. Hard constraints require a separate zero-density treatment and are excluded. The stated Wilson, O(4), P4 and GH2 laws at finite parameters fit this regularity setting; no inequality below is asserted for them without its hypothesis.

Choose an integer cell length l at least the interaction range, enlarged by a fixed geometric factor when necessary. Use the cube cores and separating rings of row 1018, or a finite-range thickening. Partition the ring variables into disjoint compact blocks R_z, z∈Z^d, by their lattice anchors. Each R_z consists of variables anchored in ownership cube z of side l, and I_c is contained in ownership cube c. The reference on all ring variables remains a product over z. Cell c has a finite core I_c and ring arguments in a set S_c of ring-block indices. Choose the ownership so

```math
 S_c\subset c+\{-1,0,1\}^d,
 \quad |S_c|\le h_d:=3^d,
 \quad \#\{c:z\in S_c\}\le h_d.                              \tag{4.1}
```

A cell ring lies in its neighbouring ownership cubes, which proves these bounds. A site variable can include finitely many link orientations. Cells have no core-to-core interaction after conditioning on rings. Assign every interaction its prescribed cell weight, splitting ring-only interactions if needed. On finite tori, integration of all cores gives the exact ring density

```math
 \rho(d\omega)=Z^{-1}\prod_c Z_c(\omega_{S_c})\prod_z\lambda_z(d\omega_z),
 \qquad
 Z_c(\omega)=\int e^{-H_c(u,\omega)}\lambda_{I_c}(du)>0.         \tag{4.2}
```

These are the *unnormalized cell integrals*. Multiplication by a constant does not affect the definition below. Ring-only energy allocations are part of (4.2) and cannot be dropped. For an infinite DLR state its ring marginal has the same local specification: to condition finitely many ring blocks, include all cores of cells incident to them in the finite DLR volume and integrate those cores. No other core meets the changed rings. This proves the ring DLR assertion directly, including for mixtures.

Draw ω,η independently from this exact ring law. For T⊂S_c, exchange the two ring-block values at every index in T, and write the resulting arguments as ω^T,η^T. Define

```math
 A_c(\omega,\eta)=Z_c(\omega)Z_c(\eta),
 \quad m_c(\omega,\eta)=\min_{T\subset S_c}Z_c(\omega^T)Z_c(\eta^T),
 \quad p_c=1-m_c/A_c.                                         \tag{4.3}
```

The minimum has at most 2^{h_d} terms, independent of the number of spins in a cell. Its existence, not an enumeration, is used. It is invariant under every partial exchange on S_c. A_c is invariant under exchanging all of S_c. The local number p_c∈[0,1) measures how much the pair of cell weights can fall when these *two sampled rings* are recombined. It includes the finite response of the cell free energy F_c=−log Z_c. It is not a supremum over arbitrary pins, coupling fields, or tilted laws.

**H-swap(l;δ,b).** There are δ,b≥0 such that, with B_c={p_c>δ}, every finite set J of distinct cells obeys

```math
 (\rho\otimes\rho)\Big(\bigcap_{c\in J}B_c\Big)\le b^{|J|},
 \qquad \varepsilon:=\delta+b<\varepsilon_0(d):=\frac1{2\,5^d}. \tag{4.4}
```

The empty-set convention is one. This is a **joint** tail in the model’s own law. No independence of the B_c is assumed. A bound only on each P(B_c), or on their expected count, is insufficient. One may weaken (4.4) to subsets of self-avoiding chains in the cell-intersection graph; the proof uses nothing more.

An equivalent sufficient input for this proof, weaker than (4.4), is the path-moment bound

```math
 \mathbb E_{\rho\otimes\rho}\prod_{c\in\pi}p_c\le\varepsilon^{|\pi|}
 \quad\hbox{for every self-avoiding cell chain }\pi.             \tag{4.5}
```

Indeed p_c≤δ+1_{B_c}. Expand the finite product and apply (4.4) to each subset: the resulting sum is (δ+b)^{|π|}. This is the precise place where the bad-cell tail enters. It is not an assertion that the marks are independent in the Gibbs law.

### 4.3 Theorem CONV-swap — proved implication, not yet independently checked

Let d=2 or 4. For any DLR state μ of the specification in 4.2 whose ring marginal satisfies H-swap, all bounded measurable local observables f,g satisfy

```math
 |\operatorname{Cov}_\mu(f,g)|
 \le C_d\,\min(|A|,|B|)\,\|f\|_\infty\|g\|_\infty
        \exp\!\left[-\frac{\log2}{2l}\operatorname{dist}_\infty(A,B)\right],
 \qquad C_d=32(3^d)^2.                                        \tag{4.6}
```

Here A,B are nonempty finite supports of site variables (link anchors when applicable). The physical cell convention may enlarge l by its fixed finite-range factor; l in (4.6) is the resulting ownership-cube side. Constants do not depend on volume or the chosen state. The same statement holds in periodic distance on finite tori with side lengths divisible by l and at least 5l. Gauge invariance is not needed, so in particular gauge-invariant local observables are covered. There is no association or monotonicity premise.

**Proof, A: exact replica extension.** Given the two rings, mark cells independently, with mark ξ_c=1 of probability p_c. The *marginal* of the rings is still ρ⊗ρ. On a finite torus the joint density relative to paired ring reference and counting measure on marks is proportional to

```math
 \prod_c\begin{cases}
       m_c,&\xi_c=0,\\
       A_c-m_c,&\xi_c=1.
       \end{cases}                                            \tag{4.7}
```

This follows by multiplying A_c by (1−p_c) or p_c. No normalizer has been replaced by an expectation. For an infinite state the same statement holds locally: condition the ring blocks in a finite set and all marks incident to it. Its paired DLR factors A_c cancel the denominators in the mark probabilities, giving (4.7) for every factor that changes. The other marks depend only on the conditioned exterior.

**B: finite-cluster exchange preserves the law.** Join all vertices of S_c whenever ξ_c=1. A connected component is a component of this hypergraph on ring-block indices. Exchange ω_z and η_z for every vertex z of a finite union K of whole components. A marked factor touching K has S_c⊂K, so its A_c and m_c are unchanged. An unmarked factor is m_c, unchanged even if only part of S_c is exchanged. All remaining factors are unchanged. The paired product reference is also unchanged. Thus (4.7) and the local DLR equation prove measure preservation.

This includes an exchange chosen from the marks: let K be the union of the components touching a fixed finite vertex set U. Decompose the event {K finite} into its countably many possible finite K. For each choice, the event that these are exactly the components touching U depends on finitely many internal/incident marks and is unchanged by the exchange. Apply the preceding argument on each event and sum. This justifies the random choice of the exchange region; no independence from the rings is asserted.

**C: connection tails in the original law.** Two distinct factors can share a ring block only if their cell indices are at sup distance ≤2. The factor-intersection graph therefore has degree ≤5^d−1. At most h_d|U| factors meet U. There are at most h_d|U|(5^d)^{n−1} ordered self-avoiding factor paths of length n starting there: choose the first factor, then an adjacent one at each step. Distinctness only reduces this upper count. Conditional independence of marks and (4.5) give

```math
 \mathbb P(\xi_c=1\ \forall c\in\pi)
       =\mathbb E_{\rho\otimes\rho}\prod_{c\in\pi}p_c
       \le\varepsilon^n.                                      \tag{4.8}
```

Put q=5^d ε<1/2. A chain from U to V, at coarse sup distance L, needs at least ceil(L/2) factors: the first and last factor centres are within one of U,V, and each consecutive centre changes by at most two. Summing the path bounds gives, for L>0,

```math
 \mathbb P(U\leftrightarrow V)
 \le\frac{h_d|U|}{1-q}\,q^{\max(1,\lceil L/2\rceil)}
 \le2h_d|U|\,2^{-L/2}.                                       \tag{4.9}
```

For L=0 the trivial bound one is enough. The same estimate for paths of arbitrarily large length shows that every component meeting a fixed finite U is finite almost surely. A locally finite infinite connected component would contain self-avoiding paths of every length: grow the finite tree of finite paths and choose successively a branch with infinitely many descendants. This is the elementary finite-branching argument; no percolation threshold theorem is imported.

**D: covariance cancellation.** For bounded ring functions F,G on U,V, respectively, independence of the two replicas gives

```math
 2\operatorname{Cov}_\rho(F,G)
 =\mathbb E[(F(\omega)-F(\eta))(G(\omega)-G(\eta))].             \tag{4.10}
```

On {U not connected to V}, exchange all components touching U. Part B preserves the joint measure and that event. It negates the F difference and leaves the G difference fixed. Its integral on that event is therefore zero. On the complement the integrand is bounded by 4||F||∞||G||∞. Consequently

```math
 |\operatorname{Cov}_\rho(F,G)|
 \le2\|F\|_\infty\|G\|_\infty\mathbb P(U\leftrightarrow V).     \tag{4.11}
```

This reuses Adhikari–Cao’s exchange cancellation and row 1099’s continuous-spin mechanism. Parts A–B supply its extension to the integrated-cell hyperedges. The argument uses integration, not finite-spin counting.

**E: return from rings to all observables.** If no core is touched by both A and B, the cell-core independence gives E[fg|rings]=FG, where F=E[f|rings], G=E[g|rings]. Their norms do not increase. Each conditional expectation depends on the ring blocks containing its ring coordinates and the at most h_d ring blocks of each core it touches. Thus |U|≤h_d|A|, |V|≤h_d|B|. Their coarse distance obeys

```math
 L\ge\operatorname{dist}_\infty(A,B)/l-3.                      \tag{4.12}
```

The loss one comes from the ownership cubes, and the other two from the two ring neighbourhoods. Equations (4.9)–(4.12) give a prefactor at most 4·2^{3/2}h_d²|A|, smaller than C_d|A|. Exchange the roles of A,B for the minimum. If they touch the same core their distance is at most l by the ownership convention. The elementary bound |Cov(f,g)|≤2||f||∞||g||∞ then implies (4.6) with the chosen generous C_d. The same bound handles overlapping supports. This proves the theorem.

### 4.4 Which states and which hypothesis have actually been covered

The theorem applies **to each state satisfying H-swap**, whether or not extremality was assumed. A mixture cannot borrow the hypothesis from its components: its independent replicas include cross-phase pairs. By (3.3), any nontrivial coexistence mixture distinguished by a local observable fails (4.4) or (4.5). This is a conclusion about the hypothesis in that mixture, not about its individual phases. The theorem makes no uniqueness claim from a hypothesis checked in only one state.

If one specification satisfies the same H-swap uniformly on an exhausting family of periodic tori, every local weak limit satisfies (4.5) and (4.6). Each p_c is a bounded continuous local function: Z_c is positive continuous on a compact space and the minimum in (4.3) is finite. Hence each finite path moment passes to the limit under the product of two local weak limits. Local Gibbs identities pass for the same continuity reason. Apply the infinite-state theorem for bounded measurable tests; no unsupported passage from weak convergence to arbitrary measurable tests is needed. The bad-event version also passes using the open events {p_c>δ} and the lower bound in the open-set form of weak convergence. Arbitrary mixtures of those limits are covered only if they separately satisfy H-swap. Extremality alone supplies no positive rate.

Nonvacuity is elementary. If osc(log Z_c)≤a uniformly, then m_c/A_c≥e^{-2a}, so p_c≤1−e^{-2a}≤2a. For any fixed cell geometry with bounded interactions multiplied by β, this holds with a→0 as β→0, uniformly in volume. Take b=0 and 2a<ε_0(d). Thus the criterion is satisfied in a genuine open neighbourhood of the independent model, without a computed constant. It is not a hidden assumption of covariance decay.

**Price and scope.** H-swap uses the pair of cell *normalizers*, not just the normalized interior kernels. Equality of normalized kernels alone says nothing about a multiplicative ring weight. A ring-only factor can leave those kernels unchanged while changing the ring law. The assigned ring interactions in (4.2) are therefore essential. No inequality from the requested mean-TV H-two, or from row 1018’s Rbar, to (4.4) is proved. This alternative is a sufficient in-law criterion with explicit gluing cost and explicit bad-cell tails; it is not the missing supplier for the Wilson window, and it is not a claimed completion of L3 for Rbar.

Step 4 result: CONV-swap is a written implication with ε_0(d)=1/(2·5^d) and rate at least (log 2)/(2l), conditional on (4.4). The original mean-TV CONV-two remains OPEN without a law-stable gluing estimate. No calculation or simulation discharged a step.

## Step 5 — restricted supremum and mandatory tests

### 5.1 Relation to a boundary response, and the missing bridge

For F_c=−log Z_c define the finite response

```math
 D_c(\omega,\eta)=\max_{T\subset S_c}
 [F_c(\omega^T)+F_c(\eta^T)-F_c(\omega)-F_c(\eta)].
```

Then D_c≥0 and p_c=1−e^{−D_c}≤min(1,D_c). Thus H-swap is a hypothesis on full finite differences of a cell’s free energy, sampled in the ring law, with a joint tail. It sees a phase label that a derivative at one typical ring can miss.

For a smooth compact-group law, choose smooth paths connecting the sampled boundary data on T and on its complement, and write F(s,t) for the cell free energy on the resulting rectangle. The fundamental theorem of calculus gives exactly

```math
 F(1,0)+F(0,1)-F(0,0)-F(1,1)
       =-\int_0^1\!\int_0^1\partial_s\partial_tF(s,t)\,ds\,dt.  \tag{5.1}
```

This identifies the missing supplier precisely. A bound only at the original random endpoints does not bound this integral. Its intermediate pins are recombined and interpolated; their law is not the original ring law. Furthermore, row 1018’s K_c controls separated-face derivatives without a direct common-plaquette term. Equation (5.1) can include adjacent ring groups and all direct terms. Those terms and the change of law must be paid. Neither the charged engine, Rbar, nor H-two as originally worded supplies that payment here. No new name for that integral is treated as a proof.

### 5.2 H-sup on a measure-carrying single-pin-connected set

Let ν be the marginal law on a fixed finite ring. For the positive continuous finite-range specifications here, ν is equivalent to its full-support product reference λ, with a positive density bounded above and below. Suppose G is a measurable subset of the ring with ν(G)=1. Suppose a continuous single-pin response is bounded by a constant for every pair in G that differs only at that pin. This is **the same bound as the full boundary supremum**.

Here is the proof, including the issue of common coordinates. Write a ring configuration as (a,t), where t is the chosen pin and a comprises the others. Fubini gives a full-λ set of a for which G_a has full measure in the pin reference. Such a’s are dense, and each G_a is dense. Given arbitrary (a,t),(a,t′), choose these full-section a_n→a and t_n,t′_n in G_{a_n} approaching t,t′. The corresponding two configurations lie in G, have the same other pins, and converge to the desired pair. Pass the response inequality to the limit. Finite-cell positive continuous densities imply continuity in total variation, by uniform continuity on the compact configuration space and a positive lower bound for the normalizer. Thus the argument also applies to TV influence norms, not just smooth test functions. Continuous derivative/Hessian bounds pass in the same way when the interaction is smooth.

Single-pin connectedness adds no escape to this result. Also, independently sampling two continuous rings almost surely never gives a pair differing at exactly one pin; an “essential supremum” on that null relation is undefined unless its conditional reference is specified. Fubini’s common-coordinate formulation is the appropriate one.

If G has probability 1−r rather than one, the conclusion above need not hold. Connectedness alone still supplies neither a bound on the length of connecting single-pin paths nor a law bound for the pins along them. Heat-bath resampling or a history-selected path can enter G^c. Such a proposal needs an explicit closure/conditional-probability estimate. It is not supplied by the number r. H-swap avoids this issue by retaining the exact product law and charging all local recombinations in (4.3).

The restricted-supremum fallback therefore gives no new consumer here. With full measure it reduces to the appropriate existing uniform criterion (Theorem W or corrected FST-BD) if that criterion’s quantitative sum holds. With high probability only, its closure step is OPEN. This is not a claim that every uniform cube criterion is false: Proposition B′ has a particular response and strength-profile class, and CA-FAIL concerns a larger family of pinned volumes.

### 5.3 Mandatory hand tests and their exact scope

| Test | What happens to the proved implication or its hypothesis |
|---|---|
| The smooth first-order n-vector model | The balanced two-sample mean is >1/4 by (3.1), and the mixture violates clustering by (3.3). Hence H-swap must fail in that mixture. More specifically, the path connection bound (4.11) and (3.3) force the joint path moments in (4.5) to exceed the proposed subcritical bound for some paths; a joint bad-cell tail with δ+b<ε_0 cannot hold. No estimate is claimed for either extremal phase. |
| Compact U(1) at weak coupling | The theorem is group-blind. In a state with nonsummable bounded local field-strength correlations, (4.6) is impossible. Therefore its ring path moments cannot obey (4.5) at any finite l with ε<ε_0. This locates the failure in the **joint swap-defect tail**, not in compactness, the Markov property or the algebraic swap. The source input is Fröhlich–Spencer’s large-β Villain massless state, as scoped in prior/gap-lit-u1.md; their Wilson-cosine extension is stated with its derivation omitted. Those proofs were not rebuilt here. No theorem-grade assertion is made at the numerical Wilson transition near one. |
| A product with a massless factor | Test f,g on that factor alone. Their covariance in the product is unchanged. Thus exactly the same nonsummability contradiction applies to the full product’s H-swap. Checking a charged or massive factor alone is not the hypothesis: Z_c and ρ must include every variable. |
| Row 1077, example (16) | Reuse its exact calculation: at λ=1/N the diagonal Hamiltonian has all-plus and all-minus ground states; every mixed configuration has energy ≥1/N. In the balanced ground-state mixture, a core spin’s two conditional laws have distance one on the cross-phase event, of probability 1/2. Its mean two-sample test fails. The diagonal transfer kernel itself is not a strictly positive finite-temperature density, so it also lies outside (4.2). A gap and a perturbation norm imply neither (4.4) nor a uniform interval. No perturbative stability is asserted. |
| Proposition B′ | Its explicit boundary-only strength profile and closed twist refute the stated pin-uniform curl bound. H-swap assumes neither that curl bound nor all strength profiles. Its finite orbit uses the actual two sampled rings and the fixed cell action. A full-measure H-sup restriction would not remove a continuous failure at the same fixed parameters; varying the strength profile is a separate quantifier. |
| Theorem D2 | Its forced/pinned sheet gives a lower bound against the specified supremum over tilts, not against every cube-boundary law. H-swap makes no tilted-law assertion. If the proof conditions on such an interior sheet, it must verify (4.4) for the new law; the original law’s tail cannot be transferred silently. |
| Lemma SHEET | The frozen tube uses a spatial coupling field and makes the plaquette covariance grow with its length. No supremum over those fields occurs here. For SU(2) the triangular Haar change of variables in its proof is reused as a constraint; the source’s overly broad “every group” remark is not used (row 997’s correction requires an identity-maximizer condition). |
| Ordered slabs of CA-FAIL | Fixing spatial links between two slices creates a 3D O(4) magnet. Its ordered state obstructs mixing uniform over those pinned slabs, given the stated Fröhlich–Simon–Spencer input. CONV-swap is for the original cubic-cell law and its joint tail. It gives no preservation of that tail under slab conditioning and no all-shape complete analyticity. The law after conditioning must be tested anew. Thus it does not assert the conclusion CA-FAIL refutes. |

The U(1) check uses **nonsummability**, not an unverified pointwise power law. From (4.11), summability of the connection probabilities would imply summability of those fixed-support covariances. Equations (4.8)–(4.9) make the connection probabilities summable if the path hypothesis holds. This is the exact contradiction. It is about the same infinite-volume state, so it needs no fixed-boundary-to-torus bridge. A claim solely about periodic limits would require that bridge; none is inserted here.

These are consistency tests of a conditional theorem, not evidence that its hypothesis holds for SU(2). The first-order, U(1) and ordered-slab existence inputs remain credited literature inputs at the read status just stated. The implication (4.6), the one-pin lemma (3.6), and the full-measure argument in 5.2 do not depend on those literature inputs.

Step 5 result: H-sup with full measure does not avoid a continuous boundary supremum. H-swap passes the mandated logical tests at their stated state/parameter scope. In particular no all-state conclusion is inferred from one pure phase, and no all-boundary conclusion is inferred from an in-law tail.

## Step 6 — final checkpoint and disposition

The requested stop condition is the written implication **CONV-swap**, (4.1)–(4.6), proved in 4.3. It is an alternative H allowed by the brief. Its scope and additional price are explicit; it does not establish the original CONV-two or the Rbar consumer. This is a research proof by the author, not an independent check or a status grant.

| Mark | Result |
|---|---|
| proved | The conditional compact-spin replica-swap criterion, with ε_0(d)=1/(2·5^d), rate (log 2)/(2l), joint bad-cell tails in the actual ring law, and state scope in 4.4. |
| proved | Every bounded finite-range regular Gibbs law satisfies the vanishing fixed-core one-pin test (3.6); its differential version is (3.7). Full-measure single-pin suprema extend to all pins under the stated continuity hypotheses. |
| proved, given a reading input | The smooth first-order model refutes H-ent-local; its full balanced coexistence law fails a small mean two-sample test by (3.1). Its phase existence is van Enter–Shlosman’s unchecked input, not a new proof. |
| reading | The sources and earlier lane results listed in steps 1–2 and 4.1; their existing results are not counted again. The swap cancellation is Adhikari–Cao’s and row 1099’s; the latter credits Redner, Machta and Chayes. The path-count design is credited to van den Berg, Maes and Gielis. |
| open | CONV-two from normalized interior-law closeness with only the originally described bad-cell information; H-ent interpreted as row 1018’s scale-normalized Rbar; an estimate of (4.4) for any requested window-coupling model; the passage from endpoint/entrywise responses to (5.1) under recombined pins. |
| guide | None: no numerical job was run. |

Next decision: determine whether a supplier can control the finite-difference response D_c *and its joint tail* in one fixed cubic-cell law, including all ring-only terms. If it cannot, this criterion supplies no progress on the Wilson window. Do not report L3, RESP-TR, (SING), (W), a seed, or a physical mass gap as closed. Row 1119 still owns the O(4) response supplier.

Verification in this session consists of the displayed hand proofs and a final source/scope read. No Lean proof, independent reader, audit, numerical run, commit or push was performed. The only repository output is this file; downloads of the two requested SA sources remain in the fresh scratch directory recorded above. The local untracked output is the handoff. Exact model/effort identity beyond the requested configuration is not exposed by this runtime.

RESULT: PROVED by the displayed hand argument, not independently checked or formalized: CONV-swap, a sufficient compact-cell in-law mixing criterion with joint swap-defect tails, ε_0(d)=1/(2·5^d) and rate (log 2)/(2l), for exactly the states specified in §4.4; the replica-swap cancellation is credited prior work. H-ent-local is refuted given van Enter–Shlosman’s published coexistence input, and full-measure H-sup collapses to the corresponding continuous full supremum. The original CONV-two, the scale-normalized Rbar form of H-ent, and verification of H-swap at the requested model couplings remain OPEN. No mass gap or scientific status is claimed.
