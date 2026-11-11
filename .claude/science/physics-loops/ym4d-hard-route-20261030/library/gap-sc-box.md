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

