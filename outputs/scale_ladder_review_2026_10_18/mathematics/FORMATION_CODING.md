> Live corrected supporting argument. Historical run results are in a separate retrieval file and are not proof. This is not a new standalone audited claim.


# iid-priority formation is a finitary factor of iid noise with a factorial coding-radius tail


## Result up front

A formation field in which every site draws its Record at an iid random time, from a local rule applied to its already-formed neighbours, is a finitary factor of iid noise. This holds for a rule in Definition 1. Jointly iid site pairs are required for the stationary factor statement; independent pairs and iid atomless activation times suffice for the ancestry bounds. The coding radius has a factorial tail, P(R > r) ≤ 6·5^(r−1)/(r+1)! on Z³. Every covariance of local observables is bounded by an explicit quantity that decays like exp(−d ln d + (1+ln 10)d) in the separation d. The rule can be order-sensitive, can read clocks, can have zeros and can emit holes.

From an empty start with a covariant rule and jointly iid site noise, the connected covariance decays factorially and its connected structure factor is entire. A zero order parameter additionally requires the label symmetry in §5. A constant all-plus rule is allowed and has nonzero unconnected long-range correlations. Terminal physical/exclusion promotions are separated below; the quantitative estimates remain the mathematical result.

A deterministic start slice is forgotten at the same factorial rate. Every evasion route needs one of the following: a random correlated start slice, correlated or deterministic clocks (sweep, light-cone or monotone orders), global conditioning (for example on hole-free completion), resampling or repair dynamics, unbounded range, or a different reading altogether (static Gibbs, Hamiltonian).

## 1. The formation class (Definition 1)

The setup generalises exactly the construction of the [2026-09-07 priority-formation note](../../../../../docs/NATIVE_RECORD_SUPPORT_PRESERVING_PRIORITY_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md).

- **Graph.** G = (V, E) is countable with maximum degree D < ∞. N(y) is the neighbour set and N[y] = N(y) ∪ {y}. Distances d are graph distances in G. A rule of finite range ρ on Z³ is covered by taking G to be the graph joining sites at distance ≤ ρ, so that D = |{z ≠ 0 : |z| ≤ ρ}|. Nearest-neighbour Z³ has D = 6. Finite tori are covered too.
- **Start slice.** B ⊂ V is a deterministic set with fixed Records b_z, z ∈ B. These are never resampled. The empty start is B = ∅.
- **Noise.** ω_y = (T_y, U_y) for y ∈ V∖B, independent across sites.
  - The T_y are iid with an atomless law; Exp(λ) and U(0,1) are the repo's choices.
  - U_y is a mark in any standard Borel space, for example the race marks (E_{y,s})_s.
  - T_y and U_y may be dependent within a site. Whenever stationarity, translation-equivariant iid-factor status or a single translation-independent probability is used, the full pairs (T_y,U_y) must be jointly identically distributed as well as independent across sites. Separately iid marginals do not suffice if the within-site copula varies with the site.
- **Rule.** Measurable maps F_y. A site y ∉ B *forms* at time T_y. Its Record is

  X_y = F_y( ω|_{N[y]∖B} , ( X_z, T_z )_{z ∈ N(y)∖B, T_z < T_y} , ( b_z )_{z ∈ N(y)∩B} ),

  and X_y = b_y for y ∈ B. The rule may depend on y, so translation covariance is not assumed until §5.

**The repo's construction is an instance.** Take U_y = (E_{y,s})_{s∈M} iid Exp(1) and F_y = argmin_s E_{y,s}/r_y(s | η). Here η is the labelled configuration of formed neighbours, including the B-neighbours. This is the race of the 2026-09-07 note. The class also contains the following without change:

- the six-label product rules (native (3,1,2), ferro (20,1,1));
- order-blind soldered rules;
- the copy-when-unanimous rule, which has zeros and is order-sensitive;
- clock-reading rules (the clock-and-rate notes);
- hole-emitting rules, where the hole is an output symbol that later neighbours may read or ignore.

**Not in the class:**

- deterministic or correlated orders (row/column sweeps, light-cone layers, monotone linear extensions);
- conditioning on any global event (a completion event, a realised order);
- resampling or repair of formed Records;
- rules of unbounded range;
- random start slices. These are handled only by the remark in §7.

## 2. Decreasing paths (Lemma 1)

Orient y → z when z ∈ N(y)∖B and T_z < T_y. Let A_y be the set of sites reachable from y, with y ∈ A_y, and let L_y be the length of the longest directed path from y. Write c_n for the number of n-step self-avoiding paths from a vertex. Then c_0 = 1, c_n ≤ D(D−1)^(n−1), and on Z³ c_n is OEIS A001412.

**Lemma 1.** For every y and n ≥ 1:

(a) E[#directed paths of length n from y] ≤ c_n/(n+1)!, with equality when no path of length n meets B.

(b) P(L_y ≥ n) ≤ c_n/(n+1)! ≤ D(D−1)^(n−1)/(n+1)!. On Z³: 6·5^(n−1)/(n+1)!.

(c) Almost surely all times are distinct, every A_y is finite, and there is no infinite directed path.

(d) Lower bound: if y has an infinite self-avoiding path avoiding B, which holds on Z³ with B = ∅, then P(L_y ≥ n) ≥ 1/(n+1)!. Hence log P(L_y ≥ n) = −n ln n + O(n), so the factorial rate is sharp.

*Proof.* A directed path has strictly decreasing times, so it is self-avoiding. For a fixed self-avoiding path of n+1 distinct sites, the iid atomless times are exchangeable and a.s. distinct, so the probability of the one decreasing ordering is 1/(n+1)!. Summing over the at most c_n paths gives (a). (b) follows because {L_y ≥ n} implies at least one directed path of length n, so the indicator is at most the path count. Ties have probability zero (countably many pairs, atomless law). The bound in (b) tends to 0, so a.s. L_y < ∞ for every y, and V is countable.

If A_y were infinite, the reachable subgraph would be infinite, connected from y and locally finite. König's lemma would then give an infinite directed path, which forces L_y = ∞. So A_y is finite. (d) holds because one fixed path of length n is decreasing with probability 1/(n+1)!; the upper bound uses c_n ≤ D^n. ∎

Lemma 1 is classical. The factorial decreasing-path argument is Harris's graphical-construction percolation argument, used for deposition processes by Penrose–Sudbury (cited in the parent note) and in "random-ranking" local algorithms. It is restated here to fix constants.

## 3. Determining sets and the coding radius (Lemma 2, Theorem 1)

Let Ω₀ be the full-measure event of Lemma 1(c). For y ∉ B put K_y := A_y ∪ N(A_y). For y ∈ B put K_y := ∅.

**Lemma 2 (stopping-set locality).** On Ω₀:

(i) X_y is well defined, by recursion along increasing T on the finite set A_y.

(ii) {K_y = k} ∈ σ(ω|_{k∖B}) for every finite k.

(iii) If ω̂ ∈ Ω₀ agrees with ω on K_y, then K_y(ω̂) = K_y(ω) and X_y(ω̂) = X_y(ω).

*Proof.* (i) The rule at a ∈ A_y reads ω on N[a] ⊂ K_y and the Records and times of earlier neighbours, which lie in A_y, or of B-neighbours, which are fixed. Recursion on the finite acyclic order gives a unique value. Shared ancestors use the same noise, so the outputs are consistent; this is the parent note's uniqueness argument.

(iii) Let a ∈ A_y(ω) and let a → z be an edge for ω̂. Then z ∈ N(a) ⊂ K_y, and T̂ = T on {a, z}, so the edge is also an ω-edge and z ∈ A_y(ω). Induction along paths gives A_y(ω̂) ⊂ A_y(ω). Conversely, every ω-path inside A_y(ω) uses only sites where ω̂ = ω, so A_y(ω̂) = A_y(ω) and therefore K_y(ω̂) = K_y(ω). The recursion in (i) then reads identical inputs.

(ii) Whether A_y = A for a given finite A is decided by the times on A ∪ N(A): A must be closed under decreasing edges and reachable from y. ∎

Define the coding radius in the sense of Holroyd–Schramm–Wilson:

R_y := min{ r : X_y(ω̂) = X_y(ω) for all ω̂ ∈ Ω₀ with ω̂ = ω on the ball B(y, r) }.

**Theorem 1 (finitary coding, factorial tail).** On Ω₀, R_y ≤ L_y + 1. For every r ≥ 1,

  P(R_y > r) ≤ P(L_y ≥ r) ≤ c_r/(r+1)! ≤ D(D−1)^(r−1)/(r+1)!.

On nearest-neighbour Z³ this is 6·5^(r−1)/(r+1)!. If B = ∅, G = Z³ (or Z^d with finite range) the full pairs (T_y,U_y) are jointly iid, and F_{y+v}(θ_v ·) = F_y(·) for all translations θ_v, then X = Φ(ω) with Φ translation-equivariant and R finite a.s.: X is a finitary factor of iid (ffiid).

*Proof.* A directed path of length k from y stays in the ball B(y, k), so K_y ⊂ B(y, L_y + 1). Apply Lemma 2(iii) and then Lemma 1(b). Note that {R > r} ⊂ {L + 1 > r} = {L ≥ r}. Equivariance follows because the construction commutes with shifts. ∎

On Z³ the tail is P(R > 10) ≤ 0.29 and P(R > 20) ≤ 2.2·10⁻⁶ (crude constants). The exact-count bound and the empirical tail are in §8.

## 4. Covariance bounds (Lemma 3, Theorem 2)

**Lemma 3 (resampling outside a stopping set).** Let K be a.s. finite with {K = k} ∈ σ(ω|_k) for all finite k, and let ω′ be an independent copy of ω. Then ω̂ := (ω on K, ω′ off K) has the same law as ω.

*Proof.* Take bounded measurable h. Then

  E h(ω̂) = Σ_k E[1{K=k} h(ω_k, ω′_{k^c})] = Σ_k E[1{K=k} H_k(ω_k)],

where H_k(a) = E h(a, ω′_{k^c}) = E h(a, ω_{k^c}). This uses that ω′_{k^c} and ω_{k^c} are each independent of ω_k with the same law, and that 1{K=k} is a function of ω_k. The right side equals Σ_k E[1{K=k} h(ω)] = E h(ω). ∎

A finite union of the sets K_y is again such a stopping set. The event {∪K_y = k} is a countable union of intersections of events {K_y = k_y} with k_y ⊂ k.

**Theorem 2 (two-copy covariance bound).** Let f be a bounded function of X_S and g of X_{S′}, with S and S′ finite. Write osc f = sup f − inf f. Then

  |Cov(f, g)| ≤ (osc f · osc g / 2) · P( K_S(ω) ∩ K_{S′}(ω′) ≠ ∅ ),   with ω, ω′ independent,   (1)

  P( K_S(ω) ∩ K_{S′}(ω′) ≠ ∅ ) ≤ Σ_{y∈S, y′∈S′} Γ(d(y, y′)),   Γ(d) := Σ_{j+j′ ≥ d−2} c_j c_{j′} / ((j+1)!(j′+1)!).   (2)

With c_j ≤ κ ν^j, where κ = D/(D−1) and ν = D−1,

  Γ(d) ≤ κ² Σ_{N ≥ (d−2)⁺} ν^N (2^{N+2} − 2)/(N+2)!.

On Z³ (D = 6):

  Γ(d) ≤ (144/25) Σ_{N≥d−2} 10^N/(N+2)! ≤ (144/25) · 10^{d−2}/d! · (d+1)/(d−9)   for d ≥ 10.

So |Cov| ≤ C_{f,g} exp(−d ln d + (1+ln 10) d + O(ln d)).

*Proof of (1).* Put ω̂ = ω on K_S(ω) and ω′ elsewhere. By Lemma 3, ω̂ has the law of ω, so ω̂ ∈ Ω₀ a.s. By Lemma 2(iii), f(ω̂) = f(ω). Therefore

  E[f(ω̂) g(ω̂)] = E[f g],   and   E[f(ω) g(ω′)] = E f · E g.

Suppose K_{S′}(ω′) ∩ K_S(ω) = ∅. Then ω̂ = ω′ on K_{S′}(ω′), so Lemma 2(iii), applied to ω′, gives g(ω̂) = g(ω′). Hence

  Cov(f, g) = E[f(ω)(g(ω̂) − g(ω′))].

Shift f so that |f| ≤ osc f / 2. Then |g(ω̂) − g(ω′)| ≤ osc g · 1{intersection}, which gives (1).

*Proof of (2).* An intersection means some y ∈ S, y′ ∈ S′, a ∈ A_y(ω) and a′ ∈ A_{y′}(ω′) satisfy d(a, a′) ≤ 2. Apply the union bound and independence:

  P ≤ Σ_{a, a′ : d(a,a′)≤2} P(a ∈ A_y) P(a′ ∈ A′_{y′}).

Each factor satisfies P(a ∈ A_y) ≤ Σ_j c_j(y→a)/(j+1)!, a sum over self-avoiding paths ending at a. Summing over a, a′ and dropping the constraint d(a, a′) ≤ 2 leaves at most c_j c_{j′}. Only j + j′ ≥ d(y, y′) − 2 can contribute. For the closed form,

  Σ_{j+j′=N} 1/((j+1)!(j′+1)!) = (2^{N+2} − 2)/(N+2)!,

and the terms with j = 0 use c_0 = 1 ≤ κ. The tail sum is geometric with ratio at most 10/(d+1). ∎

**Theorem 2′ (ball coupling: the "P(R ≥ |x|/2)" form).** Let m ≥ 1 with 2m < d(S, S′). Then

  |Cov(f, g)| ≤ (osc f · osc g / 2) (|S| + |S′|) · c_m/(m+1)!.

*Proof.* Put V = ∪_{y∈S} B(y, m) and W = ∪_{y′∈S′} B(y′, m); these are disjoint. Define F_m = f(ω on V, ω′ off V) and G_m = g(ω on W, ω″ off W) with ω′ and ω″ independent copies. Then F_m and G_m are independent, they have the laws of f and g, and they equal f and g on {max_S R ≤ m} and {max_{S′} R ≤ m} respectively. Expand FG − F_mG_m with centred f and g, and use Theorem 1. ∎

For single-site observables on Z³ take the minimum of the two forms. Theorem 2′ is the stronger one at moderate d: it drops below 1/4 from d = 21. Theorem 2 has the better rate, d ln d instead of (d/2) ln(d/2). Both are rigorous but loose: the empirical intersection probability is below 10⁻⁴ by d = 12 (§8).

## 5. Corollaries for an empty start (B = ∅, translation-covariant rule on Z³)

**C1. Mixing and symmetry-qualified order parameters.**

- By Theorem 2, Cov(f(X_S), g(X_{S′+x})) → 0 factorially, so the field is mixing and hence ergodic.
- For any local h, block averages satisfy Var((1/|Λ|) Σ_Λ h(X_x)) ≤ χ_h/|Λ|, where χ_h = Σ_z |C_h(z)| < ∞ is explicitly bounded by Theorem 2. They converge a.s. by the ergodic theorem.
- Suppose a label symmetry σ commutes with the rule and preserves the full joint site-noise law of (T,U), with σ acting on U and leaving T fixed. Invariance of the mark marginal alone is insufficient when T and U are dependent. Label-indexed iid race marks suffice when their joint law with the activation clock is permutation invariant, for example when the marks are independent of that clock. Then E[h∘σ] = E[h]. For a vector observable, its mean lies in the invariant subspace of the full preserved symmetry group. Its mean is zero, and box magnetisations tend to zero almost surely, only when that representation has no invariant vector; a single symmetry need not imply this.
- Hence the field is not a mixture of symmetry-broken phases, and lim_{|x|→∞} C(x) = 0.

**C2. Entire structure factors.** For local f and g,

  Σ_x |Cov(f(X_S), g(X_{S′+x}))| e^{s|x|₁} < ∞   for every s,

because the number of x at ℓ¹ distance d is at most 4d² + 2. So S_{fg}(q) = Σ_x Cov(·) e^{−iq·x} extends to an entire function of q ∈ C³. In particular:

- no pinch points: S is continuous, while a pinch point is a direction-dependent limit at some q₀;
- no power-law decay;
- no dipolar r^{−3} correlations.

This proves an entire connected structure factor for this class. A terminal exclusion of a physical phase requires the specified observable/phase bridge and its separate promotion discipline. For comparison, the 2026-10-16 note shows that order-blind positive rules give *1-dependent* fields; C2 is the weaker but rule-independent statement for the whole class.

The terminal colouring and recalled Ising implications are retained separately in `FORMATION_DEFERRED_PROMOTIONS.md`; they are not additional premises of this proof.

## 6. Start-slice forgetting (Theorem 3) and graded clocks (Proposition 4)

**Theorem 3.** Couple the B-process and the B = ∅ process with the same ω. On {K^∅_S ∩ B = ∅} they agree on S. Hence for local f on S,

  |E_B f − E_∅ f| ≤ osc f · P(K^∅_S ∩ B ≠ ∅) ≤ osc f Σ_{y∈S} c_{n_y}/(n_y+1)!,   n_y = d(y, B) − 1.

*Proof.* If K^∅_y avoids B, then no site of A^∅_y has a B-neighbour. The B-process explores the same edges and reads the same inputs, so A^B_y = A^∅_y and the outputs agree. Reaching N[B] requires a directed path of length at least d(y, B) − 1. ∎

So a deterministic start slice, for example an ordered planted slab, imprints only within a factorially thin layer. Theorem 2 also holds verbatim for B ≠ ∅, since translation invariance was never used.

**Proposition 4 (independent exponential clocks with bounded rate ratio).** Let T_y ~ Exp(λ_y) be independent with λ_y ∈ [λ₋, λ₊]. The probability that a fixed path v₀ … v_n is decreasing is

  Π_k λ_{v_k}/(λ_{v_0} + … + λ_{v_k}) ≤ (λ₊/λ₋)^{n+1}/(n+1)!.

All the bounds above then hold with c_n replaced by c_n (λ₊/λ₋)^{n+1}. This covers deterministic, bounded clock-rate fields.

## 7. What is excluded and what is not (caveats)

The quantitative conclusion is factorial connected-covariance decay, and under jointly iid covariant empty-start conditions, mixing and an entire connected structure factor. Symmetry-qualified order parameters require the symmetry premises in C1. Broader phase and colouring promotions are separately deferred. State-dependent resampling/reset clocks are outside this one-shot priority class.

**Not excluded**, with the reasons:

1. **Heavy-tailed finitary codings.** These are ffiids outside the class, such as resampling, repair or "retry" dynamics, CFTP-type constructions, and adaptive orders that read Records. The HSW 3-colouring has power-law tails. The theorem says nothing about codings that are not iid-priority formation.
2. **Random correlated start slices.** Condition on the complete start data (B,b). Theorems 2 and 3 hold conditionally only if the remaining site noises still satisfy the independent-site assumptions with iid continuous activation clocks required by those theorems. An independent random start is sufficient; an arbitrary start correlated with the clocks is not covered. Writing B below as shorthand for the complete start data, unconditionally,

   Cov(f, g) = E[Cov(f, g | B)] + Cov(E[f|B], E[g|B]).

   The second term carries the slice's own correlations, attenuated only within a factorial layer. These bounds do not assert that every ordered or critical initial condition remains ordered or critical throughout the bulk; they bound its influence by the start-slice coupling probability under the stated conditional assumptions.
3. **Correlated, deterministic or atomic clocks.** Examples are monotone, row or sweep orders (2026-09-07 monotone note), light-cone layered formation (2026-09-23 note: ordered above β ≈ 0.5905), and conditioning on the realised order.
   - Infinite ancestry is then possible, and Lemma 1 fails.
   - Dependent clocks with short range, and clocks with atoms (simultaneous formation), are *not proved* here.
   - Non-identical clocks are covered only by Proposition 4.
4. **Global conditioning.** Conditioning on hole-free completion turns rejection rules into static pair measures (2026-09-22 holes note, with staggered completed Records). Such measures may order. They are not in the class.
5. **Readings other than formation.** The static Gibbs reading of the same rule can order (probe F1: ferro (20,1,1) static χ₈ ≈ 512 against formation χ₈ ≈ 9). The Hamiltonian rung is untouched.
6. **Unbounded range or degree.** Here D = ∞ and the counting fails.
7. **Constants.** All bounds are upper bounds. They do not say that correlations are nonzero, and they are numerically loose at moderate d.
