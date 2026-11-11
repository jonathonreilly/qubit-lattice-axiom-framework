lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T16:15Z

# gap-sc-box: the winding bound (SC_B) on the strong-coupling disc (FINISH row 683, node Z2 / N2)

Provenance: one session, Claude Opus 5.5 (high), Mac mini worker 2, commit cecc90ccd. Not checked by another model. Written step by step; the status block at the end is the summary.

## 0. Repo search, duplicate check, sources

- Duplicate check. `library/open-core.md` has no hit for SC_B, sc-box or strong coupling. In the FINISH rows, (SC_B) is owned only by row 683 (this row). Other files only consume it as an input: `library/gap-zero-transport.md` (Section 6, line 88), `library/gap-zero-transport-check.md` (lines 76, 98, 214), `library/gap-zf-box-x.md` (lines 10, 142-151) and its check, and `library/gap-skeleton-final.md` (node Z2, line 106). No file proves it.
- Conventions taken from `library/gap-zf-box-x.md` Section 0, which match the brief: a_p = 1 - (1/2) Re tr U_p, A = sum_p a_p, Z(beta) = int exp(-beta A) dU, and N = |P| <= 6 k |B|.
- Sussman-Alpoge account: `library/sa-index/` has no strong-coupling expansion. Its "polymer expansion" hits (lines 179-184 and 19532-19538 of their text) are for the renormalised multiscale construction, not for a box at small bare coupling. Nothing of theirs is used below. Plan 2.5 also says that a box with free walls is outside their estimates.
- Literature. The brief names the convergent strong-coupling expansion of Osterwalder and Seiler (Ann. Phys. 110 (1978)) as the method. I recall it and did not read it. The proof below does not use it. It uses three elementary pieces, each written out in full here:
  (a) joint cumulants under Haar measure and a covering argument for the count "a winding set has at least 4k plaquettes" (Section 2);
  (b) Dobrushin's inductive criterion for a hard-core polymer gas to be zero-free, with a log bound. This is recalled from Dobrushin (1996) and from the Kotecky-Preiss line (CMP 103 (1986)). Neither was read. It is rebuilt in Section 3;
  (c) the Schwarz lemma (Section 4).
  No citation is load-bearing.

## 1. Statement proved

Object. B is a finite nonempty subset of Z^3, for example a box. The box has free walls: its spatial links are the pairs {x, x+e_i} with both ends in B, and its spatial plaquettes are the unit squares with all four corners in B. For k >= 3, the lattice Lambda_k = B x Z_k has spatial links at every time and time-like links (x,t)->(x,t+1). Its plaquettes are the spatial plaquettes at every time, plus the time-like plaquettes e x [t,t+1] over every spatial link e and every slab t. P_k is the set of plaquettes and N_k = |P_k|. U_p is the ordered product of link variables around p. Since every element of SU(2) has real trace, s_p := (1/2) tr U_p lies in [-1, 1] and a_p = 1 - s_p.
Z(k, B; beta) = int exp(-beta sum_{p in P_k} a_p) prod_links dU (Haar probability), entire in beta, with Z(k,B;0) = 1.

**Theorem SC.** Let R = 1/12800. For every finite B in Z^3, every k >= 3 and every q >= 1:
(i) Z(k, B; beta) != 0 for |beta| <= R. So log Z(k, B; .) is defined on that disc as the branch with log Z(k,B;0) = 0, and this branch is real on the real segment.
(ii) For |beta| < R:
|log Z(k, B; beta) - (1/q) log Z(qk, B; beta)| <= (|B| k / 100) (12800 |beta|)^{4k}.
So the brief's form holds with c = 12800 and C_0 = 1/100. Any r_0 with 2 r_0 < R is allowed. With r_0 = 1/51200 (2 r_0 = R/2), the form (SC_B) of Theorem ZB holds with C_0 = 1/100 and kappa_0 = 4 log 2: the bound is <= (|B| k/100) 2^{-4k} = C_0 |B| k exp(-kappa_0 k). More generally, with 2 r_0 = theta R and theta in (0,1), kappa_0 = 4 log(1/theta).

The theorem holds for all k >= 3, and the brief asks for k >= 4. Nothing is used about B beyond it being a finite subset of Z^3 with free walls.

Plan of proof. Write D(beta) = log Z(k) - (1/q) log Z(qk).
- Section 2: D has a zero of order >= 4k at beta = 0. This is the count in the brief, stated as an identity of cumulants.
- Section 3: |D| <= |B| k / 100 on |beta| < R, by a polymer representation and Dobrushin's criterion.
- Section 4: Schwarz lemma.

## 2. The count: D vanishes to order 4k at beta = 0

### 2.1 Joint cumulants (definitions and three facts)

For bounded real random variables Y_1, ..., Y_n on one probability space, put
kappa(Y_1, ..., Y_n) := d_{t_1} ... d_{t_n} log E exp(sum_r t_r Y_r) at t = 0, with t real. The moment generating function is smooth and positive, so the log is smooth near 0.
- (K1) kappa depends only on the joint law of (Y_1, ..., Y_n).
- (K2) Suppose {1..n} = I u J with I, J disjoint and nonempty, and the family (Y_i)_{i in I} is independent of (Y_j)_{j in J}. Then kappa(Y_1..Y_n) = 0. Proof: E exp(sum t_r Y_r) = E exp(sum_I t_i Y_i) E exp(sum_J t_j Y_j). So the log is f(t_I) + h(t_J), and a mixed derivative in one variable of I and one of J is zero.
- (K3) For a finite family (s_p)_{p in P} and S = sum_p s_p, let H(beta) = log E exp(beta S). Then H^{(n)}(0) = sum over (p_1..p_n) in P^n of kappa(s_{p_1}, ..., s_{p_n}). Proof: put G(u) = log E exp(sum_p u_p s_p) for u in R^P. Then H(beta) = G(beta, ..., beta), so by the chain rule H^{(n)}(0) = sum_{p_1..p_n} d_{u_{p_1}} ... d_{u_{p_n}} G(0). Also kappa(s_{p_1}, ..., s_{p_n}) is the derivative d_{t_1}..d_{t_n} of G(u(t)) with u_p(t) = sum_{r: p_r = p} t_r. By the chain rule d_{t_r} acts as d_{u_{p_r}}, so the two derivatives are equal. Write kappa_n(S) := H^{(n)}(0).

### 2.2 Independence under Haar measure

Fix m >= 3 and the lattice Lambda_m with product Haar measure on its links. For m >= 3 the four links of each plaquette are distinct. (The spatial links of a time-like plaquette over slab t sit at times t and t+1, which differ mod m. Its two time-like links sit at the two ends of a spatial link.)

**Lemma 2.1.** (a) Each s_p has the law of (1/2) tr V, with V Haar distributed on SU(2).
(b) If M_1, M_2 are sets of plaquettes with no common link, then (s_p)_{p in M_1} and (s_p)_{p in M_2} are independent.
(c) Let M be a set of plaquettes and p in M. Suppose p has a link l that lies in no other plaquette of M. Then s_p is independent of (s_{p'})_{p' in M, p' != p}.
Proof. (b): the two families are functions of disjoint sets of independent coordinates.
(a) and (c): by cyclicity of the trace, tr U_p = tr(U_l^eps V) with eps in {1, -1}. Here V is a product of the other three link variables of p or their inverses. Let W be the family of all link variables except U_l. U_l is Haar and independent of W, and V is a function of W. For fixed V in SU(2), the map U -> U^eps V preserves Haar measure, since inversion and right translation do. So for bounded measurable phi and psi:
E[phi(s_p) psi(W)] = E[psi(W)] E[phi((1/2) tr V_Haar)].
psi = 1 gives (a). Under (c), each s_{p'} with p' != p is a function of W. Taking psi a function of those s_{p'} then gives (c). QED.

### 2.3 Which tuples contribute

Let T = (p_1, ..., p_n) be a tuple of plaquettes and set(T) = {p_1, ..., p_n}. Two distinct plaquettes are adjacent if they share a link. A set M of plaquettes is connected if this adjacency graph on M is connected. M has property (C) (covered) if every link of every p in M lies in at least one other plaquette of M. T is good if |set(T)| >= 2, set(T) is connected and set(T) has (C). Write kappa(T) := kappa(s_{p_1}, ..., s_{p_n}).

**Lemma 2.2.** If set(T) = {p}, then kappa(T) = c_n, the n-th cumulant of (1/2) tr V_Haar, the same for all p. If |set(T)| >= 2 and T is not good, then kappa(T) = 0.
Proof. Singleton case: Lemma 2.1(a) and (K1).
Not connected: let M_1 be one component of set(T) and M_2 the rest. Both are nonempty, and they share no link. Put I = {r: p_r in M_1} and J = {r: p_r in M_2}. Lemma 2.1(b) and (K2) give kappa(T) = 0.
Connected but (C) fails at p and its link l: put I = {r: p_r = p} and J = the rest. J is nonempty since |set(T)| >= 2. The family (Y_r)_{r in I} is (s_p, ..., s_p), a function of s_p. Lemma 2.1(c) and (K2) give kappa(T) = 0. QED.

### 2.4 The count: a covered set that reaches a slab has 4 plaquettes there

**Lemma 2.3.** Let m >= 3 and let M be a set of plaquettes of Lambda_m with (C). Suppose M contains a time-like plaquette over slab t, meaning a plaquette e x [t, t+1]. Then M contains at least 4 time-like plaquettes over slab t. Consequently, if M contains time-like plaquettes over j distinct slabs, then |M| >= 4j.
Proof. Let G_t be the graph on vertex set B with an edge e = {x, y}, a spatial link of B, exactly when e x [t, t+1] is in M. Let e = {x, y} be an edge of G_t. The time-like link (x,t) -> (x,t+1) is a link of e x [t, t+1]. Which plaquettes contain this link? Spatial plaquettes contain only spatial links. A time-like plaquette e' x [t', t'+1] contains the time-like links of slab t' at the two ends of e'. So the link lies exactly in the plaquettes e' x [t, t+1] with x in e'. By (C), M contains a second such plaquette, so x has degree >= 2 in G_t, and so does y. Thus G_t is a finite simple graph with at least one edge, in which every vertex that meets an edge has degree >= 2.
Such a graph has a cycle. Take a longest path v_0, ..., v_L of distinct vertices along edges; L >= 1. Then v_L has a neighbour other than v_{L-1}. By maximality that neighbour is some v_i with i <= L-2, which closes a cycle of length L - i + 1 >= 3.
G_t is a subgraph of the nearest-neighbour graph of Z^3, which is bipartite by the parity of the coordinate sum. So the cycle has even length, hence length >= 4, and G_t has >= 4 edges. That is, M has >= 4 time-like plaquettes over slab t. Summing over the slabs gives the second claim. QED.

Remark. This is the only place where the free walls enter. In a spatial torus of side 3, a winding cycle of length 3 would break the bound. Any finite B in Z^3 is fine.

### 2.5 The covering argument

Let k >= 3 and q >= 1, and let pi: Lambda_{qk} -> Lambda_k be (x, t mod qk) -> (x, t mod k). It maps links to links and plaquettes to plaquettes of the same type and direction. It maps the ordered list of the four links of p~ to the ordered list of the links of pi(p~). For a set G of plaquettes, L(G) is the set of links of plaquettes in G.

Fix t_0 in {0, ..., k-1}. For j = 0, ..., q-1, let W_j = {t_0 + jk + 1, ..., t_0 + (j+1)k}, read mod qk. These are q disjoint windows of k consecutive times, and together they cover Z_{qk}. Put:
- G_j := the spatial plaquettes at times in W_j, together with the time-like plaquettes over slabs s with s and s+1 both in W_j;
- R(t_0) := P_k minus the time-like plaquettes over slab t_0 of Lambda_k.

(F1) pi restricted to G_j is a bijection onto R(t_0), and pi restricted to L(G_j) is a bijection onto L(R(t_0)).
Proof. pi on times is a bijection from W_j onto Z_k. So the spatial plaquettes at times in W_j go bijectively onto all spatial plaquettes of Lambda_k. The k-1 slabs s with s, s+1 in W_j go bijectively onto the slabs of Lambda_k other than t_0. Indeed, the excluded element t_0 + (j+1)k of W_j is the one congruent to t_0. So pi maps G_j bijectively onto R(t_0), and L(G_j) onto L(R(t_0)).
pi is injective on L(G_j) for these reasons. Spatial links of L(G_j) sit at times in W_j, which are distinct mod k. Time-like links of L(G_j) sit over the slabs above, which are distinct mod k. And pi preserves type and spatial position.
Consequence: for p~ in G_j and a link l~ in L(G_j), p~ contains l~ if and only if pi(p~) contains pi(l~). The forward direction holds because pi maps the links of p~ to the links of pi(p~). Conversely, if pi(l~) is a link of pi(p~), then pi(l~) = pi(l~') for a link l~' of p~, and injectivity on L(G_j) gives l~ = l~'. The same argument gives: U_{pi p~} is the same ordered word in the variables U_{pi l~} as U_{p~} is in the U_{l~}.

(F2) pi^{-1}(R(t_0)) is the disjoint union of G_0, ..., G_{q-1}, and L(G_j) and L(G_{j'}) are disjoint for j != j'.
Proof. Let p~ be a spatial plaquette at time a. Then a lies in exactly one W_j. Let p~ be a time-like plaquette over slab s with s not congruent to t_0 mod k. Then s lies in some W_j and is not its last element, so s+1 is in W_j. Conversely G_j lies in pi^{-1}(R(t_0)). Disjointness of the links: spatial links of L(G_j) sit at times in W_j, and time-like links sit over slabs inside W_j. These sets are disjoint for different j.

(F3) By (F2), a connected subset of pi^{-1}(R(t_0)) lies in a single G_j.

**Lemma 2.4.** Let 1 <= n < 4k.
(a) If T~ in P_{qk}^n is good, then pi(T~) := (pi p~_1, ..., pi p~_n) is good and kappa(pi T~) = kappa(T~).
(b) Every good T in P_k^n has exactly q good preimages T~ (with pi T~ = T).
Proof. (a) Let M~ = set(T~), so |M~| <= n < 4k. By Lemma 2.3 (m = qk), M~ has time-like plaquettes over fewer than k slabs of Lambda_{qk}. Their residues mod k are fewer than k, so some t_0 in {0..k-1} is not among them. Then M~ lies in pi^{-1}(R(t_0)), and by (F3) M~ lies in G_j for one j. By (F1), pi restricted to G_j and L(G_j) is an isomorphism of the plaquette-link incidence. It therefore preserves adjacency, connectedness and (C), and |pi(M~)| = |M~| >= 2. So pi(T~) is good.
By (F1), (s_{p~_r})_r = Phi((U_{l~})_{l~ in L(G_j)}) and (s_{pi p~_r})_r = Phi((U_{pi l~})_{l~ in L(G_j)}) for one function Phi. Both link families are Haar product families indexed bijectively. So the two tuples have the same joint law, and (K1) gives equal kappa.
(b) Let M = set(T), with |M| <= n < 4k. By Lemma 2.3 (m = k), some slab t_0 of Lambda_k carries no time-like plaquette of M, so M lies in R(t_0). For each j, T~_j := ((pi restricted to G_j)^{-1} p_r)_r is a preimage, and it is good by the isomorphism (F1). These q tuples are distinct, since they lie in disjoint G_j.
Conversely, let T~ be a good preimage. Then set(T~) lies in pi^{-1}(M), which lies in pi^{-1}(R(t_0)). Since set(T~) is connected, it lies in one G_j by (F3). Since pi is injective on G_j, T~ = T~_j. QED.

**Proposition 2.5.** For k >= 3, q >= 1 and 1 <= n < 4k: kappa_n(S_{qk}) = q kappa_n(S_k), where S_m = sum_{p in P_m} s_p under the Haar measure of Lambda_m.
Proof. By (K3) and Lemma 2.2, kappa_n(S_m) = N_m c_n + sum over good T in P_m^n of kappa(T). For the first term: N_m = m (P_s + L_s), where P_s is the number of spatial plaquettes of B and L_s the number of spatial links of B. So N_{qk} = q N_k. For the second term: by Lemma 2.4, T~ -> pi(T~) maps the good n-tuples of Lambda_{qk} onto the good n-tuples of Lambda_k, exactly q to 1, and preserves kappa. So the good sum for qk is q times the good sum for k. QED.

**Corollary 2.6.** Suppose Z(k), Z(qk) have no zero in a disc |beta| < rho. Take for log Z the branches with value 0 at beta = 0, and put D = log Z(k) - (1/q) log Z(qk). Then the Taylor coefficients of D at 0 of orders 0, 1, ..., 4k-1 vanish.
Proof. Z(m; beta) = exp(-beta N_m) E_m exp(beta S_m), since a_p = 1 - s_p. The branch log Z(m; .) and -beta N_m + H_m(beta) agree for small real beta, where H_m = log E_m exp(beta S_m) is real-analytic. Both are analytic near 0, so they agree near 0 by the identity theorem. So for n >= 1 the coefficient of beta^n in log Z(m; .) is kappa_n(S_m)/n! - N_m [n = 1]. In D:
- order 0: 0 - 0 = 0;
- order 1: (kappa_1(S_k) - N_k) - (1/q)(kappa_1(S_{qk}) - N_{qk}) = 0, by Proposition 2.5 with n = 1 and N_{qk} = q N_k;
- orders 2 to 4k-1: Proposition 2.5. QED.

What this section shows, in the brief's words. Only "winding" contributions survive in D. In the precise form: only good tuples whose plaquette set has time-like plaquettes over every slab, and by Lemma 2.3 such a set has at least 4k plaquettes. I did not show that the order 4k is attained, and nothing below needs it.

## 3. Zero-freeness and a volume bound on the disc |beta| <= R

Throughout this section, m >= 3, Lambda = Lambda_m, P = P_m and N = N_m.

**Lemma 3.1 (one plaquette).** Let |beta| <= 1/4 and c_0(beta) := E exp((beta/2) tr V) over Haar V; c_0 is entire. Then |c_0 - 1| <= (4/3)|beta| <= 1/3. The function g(U) := exp((beta/2) tr U)/c_0 - 1 satisfies |g| <= 4|beta| on SU(2), and g is analytic in beta for |beta| < 1/4.
Proof. For |z| <= y < 1: |e^z - 1| <= e^y - 1 <= y/(1 - y), since e^{-y} >= 1 - y. Take z = (beta/2) tr U, so |z| <= |beta| <= 1/4. Then |e^z - 1| <= (4/3)|beta|. Hence |c_0 - 1| = |E(e^z - 1)| <= (4/3)|beta| <= 1/3, and
|g| = |e^z - c_0|/|c_0| <= (|e^z - 1| + |c_0 - 1|)/(2/3) <= (8/3)|beta| (3/2) = 4|beta|. QED.

**Lemma 3.2 (polymer representation).** A polymer is a nonempty connected set X of plaquettes of Lambda (connected in the sense of 2.3). Two polymers are incompatible, written X ~/~ Y, if they share a link. This relation is reflexive and symmetric. Put w(X) := E prod_{p in X} g(U_p). For |beta| <= 1/4:
Z(m; beta) = exp(-beta N) c_0(beta)^N Xi(beta),
where Xi = sum over families F of pairwise compatible polymers (F empty allowed) of prod_{X in F} w(X). Also |w(X)| <= (4|beta|)^{|X|}, and each w(X) is analytic in |beta| < 1/4.
Proof. exp(beta s_p) = c_0 (1 + g(U_p)), so
Z = exp(-beta N) E prod_p exp(beta s_p) = exp(-beta N) c_0^N sum_{Q subset of P} E prod_{p in Q} g(U_p).
Split Q into its components (maximal connected subsets). Distinct components share no link, since a shared link would make them adjacent. So the factors depend on disjoint sets of independent link variables, and E prod_Q g = prod over components X of w(X).
The map Q -> {components of Q} is a bijection from subsets of P onto compatible families; its inverse is the union. To check this, let F be compatible and X in F. A plaquette of the union adjacent to X lies in some Y in F that shares a link with X, so Y = X. Hence X is a component of the union.
The bound holds since the integrand is bounded by (4|beta|)^{|X|}. Analyticity: the integrand is analytic in beta and jointly continuous, on a compact space. QED.

**Lemma 3.3 (counting).** (a) In Lambda_m (m >= 3) each link lies in at most 6 plaquettes, and each plaquette is adjacent to at most 20 others.
(b) For each plaquette p_0 and n >= 1, there are at most 400^{n-1} connected sets of n plaquettes that contain p_0.
Proof. (a) Take a spatial link in direction e_i at time t. It lies in at most 4 spatial plaquettes: two planes {i, j} with j != i, and two positions in each. It also lies in the time-like plaquettes over it in slabs t and t-1, which are distinct for m >= 2. That makes at most 6. A time-like link at (x, slab t) lies in the plaquettes e' x [t, t+1] with x in e', and there are at most 6 spatial links e' at x. Each plaquette has 4 links, each in at most 5 other plaquettes, so it has at most 20 neighbours.
(b) Let X be such a set, with a spanning tree of its adjacency graph. A depth-first traversal from p_0 crosses each tree edge twice. It is a walk of length 2(n-1) in the adjacency graph, starting at p_0, whose set of vertices is X. So X is determined by such a walk, and there are at most 20^{2(n-1)} = 400^{n-1} of them. QED.

**Lemma 3.4 (Dobrushin's criterion; recalled from Dobrushin 1996 and the Kotecky-Preiss line, rebuilt here).** Let Gamma be a finite set, ~/~ a reflexive symmetric relation on Gamma, and w: Gamma -> C. For S a subset of Gamma, let Xi_S be the sum over subsets F of S whose distinct elements are pairwise compatible of prod_{X in F} w(X), with Xi_empty = 1. Suppose c: Gamma -> [0, infinity) satisfies, for every X,
(D) |w(X)| <= (1 - e^{-c(X)}) exp(- sum_{Y ~/~ X, Y != X} c(Y)).
Then for every S: Xi_S != 0. For X in S, Xi_S / Xi_{S \ X} = 1 + u with
|u| <= |w(X)| exp(sum_{Y ~/~ X, Y != X} c(Y)) <= 1 - e^{-c(X)},
and in particular |Xi_{S \ X} / Xi_S| <= e^{c(X)}.
Proof. Induction on |S|. For S empty, Xi = 1 and there is nothing more to show. Let |S| = s >= 1, assume the claim for all sets of size < s, and fix X in S. Let N[X] = {Y : Y ~/~ X}, which contains X. Split the families by whether they contain X:
Xi_S = Xi_{S \ X} + w(X) Xi_{S \ N[X]}.
By induction Xi_{S \ X} != 0. Enumerate (N[X] \ {X}) intersected with S as Y_1, ..., Y_r. Put T_0 = S \ {X} and T_i = T_{i-1} \ {Y_i}, so T_r = S \ N[X]. Each T_{i-1} has size < s. So by induction Xi_{T_i} != 0 and |Xi_{T_i} / Xi_{T_{i-1}}| <= e^{c(Y_i)}. Multiplying, |Xi_{S \ N[X]} / Xi_{S \ X}| <= exp(sum_{Y ~/~ X, Y != X} c(Y)).
Put u = w(X) Xi_{S \ N[X]} / Xi_{S \ X}. By (D), |u| <= 1 - e^{-c(X)}. So |Xi_S / Xi_{S \ X}| = |1 + u| >= e^{-c(X)} > 0. QED.

**Corollary 3.5 (log bound).** Assume (D). Enumerate Gamma = {X_1, ..., X_K} and put Gamma_i = {X_1, ..., X_i}. Then Xi_Gamma = prod_i (1 + u_i) with u_i = Xi_{Gamma_i}/Xi_{Gamma_{i-1}} - 1 and |u_i| <= rho_i := |w(X_i)| exp(sum_{Y ~/~ X_i, Y != X_i} c(Y)) <= 1 - e^{-c(X_i)}. Put log Xi_Gamma := sum_i Log(1 + u_i), with the principal branch. Then
|log Xi_Gamma| <= sum_{X in Gamma} |w(X)| exp(sum_{Y ~/~ X} c(Y)),
where the inner sum now includes Y = X.
Suppose further that the w(X) are analytic in beta on an open set O and (D) holds at every beta in O with one fixed c. Then each u_i is analytic on O, since it is a ratio of polynomials in the w's with a nonvanishing denominator. So log Xi_Gamma is analytic on O and exp(log Xi_Gamma) = Xi_Gamma.
Proof. For |u| < 1: |Log(1+u)| <= sum_{n>=1} |u|^n/n = -log(1 - |u|) <= |u|/(1 - |u|). Here 1 - |u_i| >= e^{-c(X_i)}, so |Log(1 + u_i)| <= rho_i e^{c(X_i)}, which is the i-th term of the claimed sum. QED.

**Proposition 3.6.** Let R = 1/12800, m >= 3 and |beta| <= R. Then Z(m; beta) != 0. The function
log Z(m; beta) := -beta N + N Log c_0(beta) + log Xi(beta)
(Lemma 3.2 and Corollary 3.5) is analytic on |beta| < R, vanishes at 0, is real on the real segment and satisfies exp(log Z) = Z. Moreover |log Xi(beta)| <= (32/3)|beta| N.
Proof. Put x = 4|beta| <= 1/3200 and take Gamma = the polymers of Lambda, with w from Lemma 3.2, so |w(X)| <= x^{|X|}. Set c(X) := (4x)^{|X|}.
Step 1, sum over incompatible polymers. If Y ~/~ X, then Y contains a plaquette through some link of X. X has at most 4|X| links, each in at most 6 plaquettes (Lemma 3.3(a)), and Lemma 3.3(b) bounds the polymers through a given plaquette. Using 1600x <= 1/2:
sum_{Y ~/~ X} c(Y) <= 4|X| * 6 * sum_{n>=1} 400^{n-1} (4x)^n = 24|X| * 4x/(1 - 1600x) <= 192 x |X| <= 0.06 |X|.
Step 2, check (D). c(X) <= 4x <= 1/800 <= 1, so 1 - e^{-c} >= c - c^2/2 >= c/2. Hence the right side of (D) is at least
(1/2)(4x)^{|X|} e^{-0.06|X|} = (1/2)(4 e^{-0.06})^{|X|} x^{|X|} >= (1/2) 2^{|X|} x^{|X|} >= x^{|X|} >= |w(X)|.
This uses 4 e^{-0.06} >= 4(1 - 0.06) > 2.
Step 3, conclude. By Lemma 3.4, Xi != 0. By Lemma 3.1, c_0 != 0, so Z != 0. Corollary 3.5, with the sum over polymers bounded by summing over a plaquette and the polymers through it, gives
|log Xi| <= sum_X x^{|X|} e^{0.06|X|} <= N sum_{n>=1} 400^{n-1} (x e^{0.06})^n.
Since x e^{0.06} <= 2x <= 1/1600, the factor 400 x e^{0.06} is <= 1/4. So |log Xi| <= N (2x)/(1 - 1/4) = (8/3) x N = (32/3)|beta| N.
Analyticity: Lemma 3.2 and Corollary 3.5 on the open disc; Log c_0 is analytic since |c_0 - 1| <= 1/3. At beta = 0 we have c_0 = 1 and g = 0, so w = 0 and u_i = 0, and log Z = 0. For real beta, c_0 > 0 and all w(X) are real. Then each u_i is real with |u_i| < 1, so every term is real. QED.

Because the disc is simply connected and Z has no zero there, this log Z is the unique branch with value 0 at 0. So it is the branch named in Theorem SC(i) and Corollary 2.6, and the branch "real on the real axis" of Theorem ZB (`library/gap-zero-transport-check.md`, point (C)).

## 4. Assembly: proof of Theorem SC

(i) This is Proposition 3.6 with m = k.
(ii) Let k >= 3 and q >= 1, and put D = log Z(k) - (1/q) log Z(qk) on |beta| < R. By Proposition 3.6 and N_{qk} = q N_k (proof of Proposition 2.5), the terms -beta N + N Log c_0 cancel exactly:
D = log Xi_k - (1/q) log Xi_{qk}, so |D| <= (32/3)|beta| (N_k + N_{qk}/q) = (64/3)|beta| N_k.
Now N_k = k (P_s + L_s) <= 6 |B| k, since a site is the lower corner of at most 3 spatial plaquettes and at most 3 spatial links. So on |beta| < R,
|D| <= (64/3) R * 6 |B| k = 128 |B| k / 12800 = |B| k / 100 =: M.
D is analytic on |beta| < R, and its Taylor series at 0 converges there. By Corollary 2.6 its coefficients of order < 4k vanish. So D(beta) = beta^{4k} h(beta) with h analytic on the disc. For |beta| < r < R, the maximum principle gives |h(beta)| <= max_{|z| = r} |D(z)| / r^{4k} <= M / r^{4k}. Letting r -> R:
|D(beta)| <= (|B| k / 100) (|beta| / R)^{4k} = (|B| k / 100) (12800 |beta|)^{4k}.
The specializations stated in Section 1 follow by substituting |beta| <= theta R. QED.

Remark (what is uniform). The constants R, C_0 = 1/100 and c = 12800 do not depend on B, k or q. The theorem needs k >= 3; the brief's k >= 4 is covered. The proof never uses that the integrand of g has mean zero. All the cancellation is in Section 2, and Section 3 is a crude volume bound. The constants are far from optimal. Each step is a displayed inequality between explicit rationals, or the bound e^{-0.06} >= 0.94, so the whole proof is checkable by hand and has no computed step.

## 5. Status

Kind of result: a proof of a step the plan states as an input (node N2 / Z2). It is not a check of anyone's proof and not a correction. Stop rule (i) is met: a proof with explicit constants.

**Proved here (Claude Opus 5.5 high; not yet checked by another model):**
- Theorem SC. For every finite B in Z^3 with free walls, every k >= 3 and q >= 1, and |beta| < R = 1/12800:
  - Z(k, B; beta) has no zero (also for |beta| = R);
  - |log Z(k,B;beta) - (1/q) log Z(qk,B;beta)| <= (|B| k/100)(12800 |beta|)^{4k}.
  So (SC_B) holds as the brief states it, with c = 12800 and C_0 = 1/100, and in the form Theorem ZB reads with r_0 = 1/51200, C_0 = 1/100 and kappa_0 = 4 log 2.
- Supporting lemmas, each proved in full:
  - the cumulant identity kappa_n(S_{qk}) = q kappa_n(S_k) for n < 4k (Proposition 2.5, from Lemmas 2.1-2.4);
  - the count "a covered plaquette set meeting a slab has at least 4 time-like plaquettes there" (Lemma 2.3);
  - Dobrushin's zero-freeness criterion with a log bound (Lemma 3.4, Corollary 3.5);
  - the polymer representation and the counting (Lemmas 3.2, 3.3).

**What this moves.** Node N2 (Z2 in `library/gap-skeleton-final.md`) goes from OPEN to "proved, not checked". The consumers now have (SC_B) as a proved input rather than an assumption: Theorem ZB (`library/gap-zero-transport.md` Section 6, corrected in `library/gap-zero-transport-check.md` 3.6), and Theorem ZB-chain and Corollaries 3.2-3.3 of `library/gap-zf-box-x.md`. This file does not edit them; the lead forwards it.

**Open (not touched here):**
- (ZF_B) beyond the base region (nodes N6, N7);
- the harmonic-measure bound (N5);
- the limit nodes N9-N11.
Nothing of Theorem SC is open.

**Not done.** I did not read Osterwalder-Seiler, Dobrushin (1996) or Kotecky-Preiss. The attributions in Section 0 are from memory. The proof does not depend on them. No numerics were run. I did not commit or push (no push rights on this machine).

**Credits.** The idea of comparing log Z on a time circle and on its q-fold cover, where only winding contributions survive, is the plan's (`library/gap-skeleton-max-b.md` 2.5, Claude Fable 5.2, row 670). That plan's method of strong-coupling polymer expansions goes back to Osterwalder and Seiler. The zero-freeness criterion of Section 3 is Dobrushin's, rebuilt here. Conventions follow `library/gap-zf-box-x.md` (Claude Fable 5.2, row 677). Nothing is taken from the Sussman-Alpoge account, which does not treat this object.

**The one exact next statement.** A line-by-line check of Theorem SC (Sections 2-4 of this file) by a model that did not write it. Under the 2026-11-09 model rule, that is gpt-6-astra (max) for Opus-written steps. The check should give a verdict on:
- Lemma 2.3, the count;
- Lemma 2.4 with (F1)-(F3), the covering;
- Proposition 3.6, the arithmetic of (D);
- the Schwarz step.
