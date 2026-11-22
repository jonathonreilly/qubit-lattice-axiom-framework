# Check of library/gap-seed2-astra62.md (FINISH row 1372)

Checked by Claude Opus 5.5 (laptop Claude subagent), cross-provider check of a gpt-6.2-astra row; grants no status.

Target: library/gap-seed2-astra62.md (FINISH row 1371, by gpt-6.2-astra).
Method: line-by-line reading by hand. Positive claims first, then the rest.
Verdicts: HOLDS, HOLDS AFTER CORRECTION, FAILS. Each verdict names the line(s).

Status: complete. Verdict table and RESULT line at the end.

## Verdicts

Reading record. Lane head `7efcd0a54` (clone HEAD at the start of this check). Read in full: the target note (430 lines), row 1367 `gap-seed-astra62.md`, its check row 1369 `gap-seed-check-opus.md`, FINISH rows 1367, 1369, 1371, 1372. Cited sources were read at the cited equations; each is named at the verdict that uses it. `library/gap-seed3-astra62.md` was not opened.

Method. Every identity and inequality below was re-derived by hand. Where a step rests on an earlier row, I read that row at the cited place and say whether it says what the note claims. No computation was run.

### A. The one-box statement (L11, L13)

**S1 (L11, OPEN, the one-box question). HOLDS.** It restates row 1367 L11 and the FINISH brief of row 1371: one admissible L, n_j = L/a_j, 4 | n_j, beta_0 <= beta_j <= B_0 log n_j, test s(2 w_j) <= 4/21 at w_j = floor(n_j/1024). Each ratio lambda_a/lambda_0 lies in [0,1], so s is nonincreasing in time, and the largest allowed w is the right choice. "Zero electric flux" is the range of P_0 (row 1367 L11). Row 1367 also requires n_j >= 2^70; "every sufficiently large j" covers this. The row 1349 premises match row 1367 L13 and check S4 of row 1369. Restates rows 1367 and 1356.

S2 (L13, summary) is checked after S45-S52 below, since it summarizes them.

### B. Gaussian observations on the two cuts (L23-51)

**S3 (L23-27, the projected transfer F). HOLDS.** Gamma = (vertex gauges) x (eight centre elements) is a compact group, because a sheet flip multiplies links by the central element -1 and so commutes with vertex gauges. Left and right multiplication by unit quaternions are isometries of R^4, so Gamma acts orthogonally on R^d, d = 4m, m = 3n^3. Each spatial plaquette meets a sheet in 0 or 2 links, so M is invariant. The temporal factor is exp(-beta sum_e (1 - x_e . (g y)_e)) = e^{-beta m} e^{beta x . g y}. Averaging g over Gamma gives the gauge projection times the centre average P_0. This is the transfer of row 667 with the electric projection of row 1367.

**S4 (L29-33, H*H = F, K = HH*). HOLDS.** Re-derived: int H(z,x)H(z,y) d gamma_d(z) = e^{-beta m} M(x)M(y) int int e^{beta|gx + hy|^2/2} dg dh. Orthogonality gives |gx + hy|^2 = 2m + 2 x . g^{-1}h y, and g^{-1}h is Haar. So H*H = F. H is Hilbert-Schmidt: the integrand is at most sup M^2 e^{2 sqrt(beta m)|z|}, which is gamma-integrable. HH* and H*H share their nonzero spectrum with multiplicities. K has a nonnegative kernel. The construction is the Gaussian representation of an electric step of row 947 (B1) (`gap-fc-max.md` L132), as L17 says.

**S5 (L35-44, the two marked bonds and (1)). HOLDS.** At a marked bond, the likelihood e^{sqrt(beta) z.U - beta|U|^2/2} times the prior factor e^{beta a.b} (a = g^- x_0, b = g^+ x_1) equals e^{-beta m} e^{sqrt(beta) z.a} e^{sqrt(beta) z.b}. Integrating the two frames separately, with one half-weight each, gives H(z,x_0)H(z,x_1). The first arc then gives H F^{w-1} H* = (HH*)^w = K^w(z,z'), and the second gives K^w(z',z). So the joint density is proportional to K^w(z,z')^2, and its integral is Tr K^{2w} = Tr F^{2w}. The bound |U_e| <= 2 holds since U_e is a sum of two unit vectors. Remark: "spatial slices x_k with their half-weights" means each slice carries its full weight M(x_k)^2, one half from each adjacent bond; the formula is right.

**S6 (L46-51, inequality (2)). HOLDS.** Re-derived. Lower bound: B = K^w/sqrt(Tr F^{2w}) is positive and pointwise nonnegative, with top eigenvalue (1+s(2w))^{-1/2}, so the affinity <sqrt l, B sqrt l> is at most that, and Jensen gives I >= -2 log(affinity). Upper bound: K^w(x,y) = <F^{(w-1)/2} H*delta_x, F^{(w-1)/2} H*delta_y>, so K^w(x,y)^2 <= K^w(x,x)K^w(y,y), and int K^w(x,x) d gamma = Tr K^w = Tr F^w. Then B^2 <= b(x)b(y)(Tr F^w)^2/Tr F^{2w}, and D(P||b x b) = I + 2D(l||b) gives I <= 2 log(1+s(w)) - log(1+s(2w)). Restates row 1165 (3): I read `gap-solve11-astra62.md` L40-58, which proves exactly this two-sided bound, with the same diagonal reference m(x) = K^t(x,x)/Z_t, for the ordinary transfer. Here it is applied to the neutral Gaussian midpoint kernel, as the note says.

### C. The two-source response and its value at zero field (L55-101)

**S7 (L55-60, identity (3)). HOLDS.** With W the hidden circle, X_u - W - Y_v is a Markov chain. So I(X_u;Y_v) = I(X_u;W) - I(X_u;W | Y_v), and the I-MMSE formula of Guo, Shamai and Verdu gives 2 d_u I = E|E[U|X_u,Y_v]|^2 - E|E[U|X_u]|^2. The derivative in v of the first term is E||Cov(U,V | X_u,Y_v)||_F^2 (the Hessian form of the same identity). With I(u,0) = I(0,v) = 0, integration gives (3) with the factor 1/2. Scalar control: jointly Gaussian U,V with correlation rho give I ~ uv rho^2/2 for small u,v, which is (1/2) int int rho^2.

**S8 (L62-69, first derivative). HOLDS.** Re-derived: d_u p = -(2 sqrt u)^{-1} div(p E[U|y]), grad log p = -y + sqrt(u) E[U|y]. Then d_u h = (2 sqrt u)^{-1} E[E[U|y].y] - (1/2)E|E[U|y]|^2, and E[E[U|y].y] = E[U.y] = sqrt(u) E|U|^2. This gives the displayed formula, and the conditional version gives 2 d_u I. Bounded hidden vectors (|U| <= 2 sqrt m) justify the differentiations.

**S9 (L71-76, mixed derivative). HOLDS.** Re-derived: d_{y_j} a_i = sqrt(v)(D_ij - a_i b_j) and d_v(p a_i) = -(2 sqrt v)^{-1} sum_j d_{y_j}(p D_ij), also d_v p = -(2 sqrt v)^{-1} sum_j d_j(p b_j). Then d_v int |pa|^2/p = int [2a . d_v(pa) - |a|^2 d_v p] = (1/sqrt v) int p sum_ij (D_ij - a_i b_j) d_j a_i after integration by parts, and substitution gives E[||C||_F^2 | X_u]. The boundary values and continuity at the axes hold at finite volume.

**S10 (L78-82, posterior on a marked bond). HOLDS.** e^{sqrt(u) x.(a+b) - u|a+b|^2/2} = e^{-um} e^{sqrt(u) x.(a+b)} e^{-u a.b}, since |a|^2 = |b|^2 = m. With the prior e^{beta a.b} the residual coupling is beta - u. At u = beta the cut interaction is removed. Restates row 1290 (8), as L84 says.

**S11 (L84, GUIDE). HOLDS** as a pointer; not re-checked against row 1290 beyond its use in S10.

**S12 (L88-93, limit (4)). HOLDS.** |U_e|^2 = 2 + 2W_e since (g^-x_0)_e . (g^+x_1)_e is the framed temporal plaquette trace. Re-derived limit: the mixed covariance f(h,k) = d_h d_k log Z vanishes at h = 0 and at k = 0 (S13), so f(h,k) = int_0^1 int_0^1 kappa_4(sh,tk) h k ds dt. At zero source the only fourth cumulant left is kappa(U_ei,U_e'j,V_fa,V_f'b) = delta_ee' delta_ff' delta_ij delta_ab c_ef/16 with c_ef = Cov(|U_e|^2,|V_f|^2) = 4 Cov(W_e,W'_f). Hence C_{u,v} ~ sqrt(uv) c_ef X_ei Y_fa/16, and E||C||_F^2/(uv) -> sum c_ef^2 E|G_e|^2 E|G'_f|^2/256 = sum c_ef^2/16 = sum Cov(W_e,W'_f)^2. Then I = (1/2) int_0^u int_0^v u'v' S = u^2 v^2 S/8. Dominated convergence: |X_u| <= 2 sqrt(beta m) + |G| under the coupling (1).

**S13 (L95, gauge averages at each cut). HOLDS.** Left multiplication of both frames of one cut by a vertex gauge h preserves the Haar prior and the bond factor beta x_0 . (g^-)^{-1} g^+ x_1, and acts on U as a gauge transformation, leaving V fixed. Two distinct edges of the simple torus (n >= 4) have a vertex that belongs to only one of them; the Haar average of g_v U_e is zero. For one edge, SU(2) x SU(2) acts on R^4 as SO(4), so the average of U_e U_e^T is |U_e|^2 I/4.

**S14 (L97-101, the fourth-cumulant derivation). HOLDS.** At k = 0, the cut-2 gauge leaves e^{h.U - u|U|^2/2 - v|V|^2/2} invariant (|V_f|^2 is gauge invariant) and sends V to its gauge image, so E[V | U-data] = 0 and the mixed covariance vanishes; likewise at h = 0. The value of the cumulant is S12. The last two sentences correctly limit the claim to fixed volume.

### D. The cutoff-uniform partial bound (5) (L105-133)

**S15 (L105-109, statement (5)). HOLDS** by S16-S19. The extension "with the full opposite latent vector V" is what S19 proves; Y_beta is a noisy function of V, so data processing gives I(u,beta) <= I(X_u;V).

**S16 (L111-115, the plaquette moment). HOLDS.** Halving the coupling of edge e at the marked step replaces its normalized one-link convolution C_beta by C_{beta/2}. Row 1149 (16) proves that I_{j+1}(v)/I_j(v) increases in v and hence that normalized C_{beta/2} <= C_beta in positive-operator order (`gap-solve4-astra62.md` L214-221). The class-function convolutions commute with the gauge and centre actions, so the projected sandwich P M (.) M P keeps the order, and Tr(N' N^{2w-1}) <= Tr(N^{2w}) since N^{2w-1} >= 0. This gives E exp[beta(1-W_e)/2] <= J(beta/2)/J(beta). The radial integral J(b) = (2/pi) int e^{-b(1-cos t)} sin^2 t dt is of order (1+b)^{-3/2}. Then E(4-|U_e|^2)^2 = 4E(1-W_e)^2 <= min(16, 32C/beta^2) <= C/(1+beta)^2. This is the one-plaquette case of row 1334 (5) (`gap-solve43-astra62.md` L61-63, which uses the same ordering and trace argument), now on the neutral circle with frames.

**S17 (L117-123, random gauge on an observed face). HOLDS.** Re-derived. The edge marginal of g b is uniform on the sphere of radius r_e, so the marginal of P_b is q_{r_e}. The second moment of dP_b/dR_b is E_{g,g'} prod_e int p_c p_c'/q d gamma_4 = E prod_e (1 + H_e), because int p_c d gamma = int q d gamma = 1. Jensen gives q_r >= e^{-ur^2/2}, and ||p_c - 1||^2 = e^{u r^2} - 1, so |H_e| <= 4 e^{2u}(e^{4u} - 1) <= C_1 u on [0,1]. A leaf vertex v of the chosen edge set has a free frame g_v, and averaging it turns p_c into q, which kills the term. Leafless components have at least 4 edges (girth 4 for n >= 8). Connected sets of k edges number at most 2m 6^{2k} (closed walk on the doubled edges). The polymer bound gives exp(2m sum_{k>=4}(36 C_1 u)^k) <= exp(C m u^4), and Jensen gives D <= log of the second moment. The leaf cancellation is the device of row 1337 (`gap-solve44-astra62.md` L63), as credited.

**S18 (L125-131, the radial reference). HOLDS.** int q_r q_R d gamma_4 = E e^{u c.c'} = Phi(urR). So ||q_r - q_2||^2 = Phi(ur^2) - 2Phi(2ur) + Phi(4u) = sum_k phi_k u^{2k}(r^{2k} - 4^k)^2 with phi_k <= 1/(2k)!. With |r^{2k} - 4^k| <= k 4^{k-1}|r^2 - 4| the series is at most C u^2 (r^2-4)^2 for u <= 1. KL is at most chi-square, and q_2 >= e^{-2u}.

**S19 (L133, assembling (5) and the strips). HOLDS.** D(P_b || prod q_2) = D(P_b||R_b) + sum_e D(q_{r_e}||q_2), since the marginals of P_b are the q_{r_e}. The cut-1 gauge fixes V and preserves the law, so X_u given V is a mixture of the P_U. Convexity of KL, then I(X_u;V) = E_V D(L(X_u|V)||R) - D(L(X_u)||R) <= E_V D(L(X_u|V)||R), give I(X_u;V) <= C m u^4 + C u^2 sum_e E(4-|U_e|^2)^2 <= C m(u^4 + u^2/(1+beta)^2). Strips: with b_j = o((1+beta_j)/sqrt(m_j)) one has m b^2/(1+beta)^2 = o(1) and m b^4 = o((1+beta)^4/m) = o(1) in the logarithmic band, and b_j < u_0 eventually. Each strip is an I(b,beta)-type integral, so the union contributes o(1). The strip width is of order (log n)/n^{3/2}, a vanishing part of [0,beta]^2; the note does not claim more.

### E. Exact link readings returning to row 1367 (L137-178)

**S20 (L137-151, statement (6) and Z_+ >= Z/8). HOLDS.** Z_+ = int k_+^2 = (1/64) sum_{g,g'} int k(a,gb)k(a,g'b). All terms are nonnegative and each diagonal term equals Z by Haar invariance, so Z_+ >= 8Z/64 = Z/8. Equivalently Tr P_0 T^{2w} >= Tr T^{2w}/8, the positivity of the eight electric twists.

**S21 (L153-158, proof of (6)). HOLDS.** Re-derived. Given the endpoints the arcs are independent. Moving the centre average to the last bond replaces internal slices x by gx; a centre-invariant reading is unchanged. With the flip at the last bond, the arc is an ordinary bridge from a to gb with weight k(a,gb)/(8 k_+(a,b)). Convexity gives E_+ d_TV(L_+(D|a,b),R) <= (1/(8Z_+)) sum_g int k_+(a,b)k(a,gb)e(a,gb); the substitution b -> g^{-1}b and the invariance of k_+ give (1/Z_+) int k_+ k e. Cauchy-Schwarz gives sqrt((Z/Z_+) E_ord e^2) <= sqrt(8 E_ord e), using e <= 1. Conditional independence of D and Y given (a,b) gives the joint bound. The positive-insertion variant (used in S35 and S50) follows by the same computation with E_ord[f | a,b] in place of e.

**S22 (L160-165, (7)). HOLDS**, by S21, S23 and S24. Under k = o(b/log beta) every term of (8) tends to zero: k log(beta)/b -> 0, k b/n -> 0, and beta/b^8 = beta^{1-8 gamma} -> infinity. Time translation moves the face pair (0, w) to (t, t+w) with 1 <= t <= w-1, so D is strictly inside the first arc and Y strictly inside the second, as (6) requires. Plaquette angles are centre invariant. Replacing R by L_+(D) costs a factor two.

**S23 (L167-172, the inputs (8)). HOLDS.** I read row 1339 (`gap-solve45-astra62.md` L29-70) and its check `gap-solve45-check-opus.md` V4-V14 (all HOLD). Row 1339 (3) has exactly the right side of (8), with R = R_*^{k}, R_* = |N(0,I_3)|/sqrt 2, and D = sqrt(beta) times the plaquette angles. Its proof (L48, L70; check V9 and V14) bounds the shift average of the mean conditional variation given the cuts, before the opposite half is sampled. This is E_ord e(a,b) of (6). "Total variation with the endpoint marginal retained is exactly the mean conditional variation" is the identity d_TV(L(D,a,b), R x L(a,b)) = E d_TV(L(D|a,b),R).

**S24 (L174, change of aspect). HOLDS.** Row 1151 (24) (`gap-solve5-astra62.md` L301-311) is stated for rectangular tori with time T or 2T, with halves tiled separately and boxes at a cut discarded. Its b/n terms are boundary-strip fractions. At period 2w these become b/n + b/w, and b/w <= 2048 b/n at w = floor(n/1024). The shift count n^3(w-1) is about half of 2wn^3. Jensen over shifts is used correctly. I did not re-derive the row 1151 gluing comparison at this aspect; the note's bookkeeping is the natural one, and the explicit b/w term is kept in (12), where it matters at the short time of S47.

**S25 (L176, the unicyclic prefix). HOLDS.** Growing k disjoint squares by one new vertex and one edge at a time covers the connected torus, keeps k unicyclic components, and uses 4k + (n^3 - 4k) = n^3 edges. Given the first face, the law of the second face is invariant under its vertex gauges, components have independent gauges, and the orbit of a unicyclic component is the conjugacy class of its cycle holonomy. The unique invariant probability on each product of orbits gives a kernel from the k angles that does not depend on the first face. Data processing then transfers (7) (with the faces exchanged, J being symmetric). This is the orbit argument of row 1339 L19 (check V1), extended from isolated squares to unicyclic components.

**S26 (L178, the prefix sum). HOLDS.** The partial sum of the row 1367 (4) losses through the prefix is 1 minus the affinity of J and Q restricted to (x, prefix), which is at most their total variation. Clipping costs at most 2 sqrt(#terms) n^{-5/2} <= 2 sqrt(3) n^{-1} by row 1367 (5)-(6).

### F. The tree-first ordering with controlled chords, and its extension (L182-216)

**S27 (L182, GUIDE). HOLDS** for the parts I read: row 1145 (1)-(3) (`gap-solve2-astra62.md` L17-36) and row 1161 (23) (`gap-solve9-astra62.md` L347, the function eta). Rows 1227 (22) and 1272 (31) were not opened.

**S28 (L184-190, statement (9)). HOLDS** by S29-S32. K = (n^2/2) floor((n-1)/(r+1)) is of order n^3/(8(A+6)(1+6beta) log n), and r < n - 1 eventually since r = O((log n)^2) in the band. The bound does not use beta -> infinity.

**S29 (L192, the graph). HOLDS.** The trunks (even rows, i from 0 to n-1), the plane tree at i = 0 and the intervals [a, a+r], a = 1 + j(r+1), form a tree: the intervals are vertex disjoint, lie in 1 <= i <= n-1, and each hangs from its trunk by one left rung. Attaching further vertices one edge at a time keeps every path between covered vertices. Each right rung closes a 1 x r rectangle.

**S30 (L194, private selections). HOLDS.** The based path to a trunk vertex runs through the plane i = 0 and along even-row trunks, so it never enters an odd-row interval; each interval occurs once, in its own chord's based holonomy. Re-derived plaquette disjointness: two direction-1 links share a plaquette only if they are parallel and one step apart in direction 2, 3 or time. Selected links lie in one slice, odd rows are two apart (n even), and adjacent z rows carry opposite parities of i (also across the wrap since n is even). Each interval has at least floor(r/2) selected links.

**S31 (L196-200, the density bounds). HOLDS.** This is row 1145 (1)-(3): conditionally independent selected links with g_h laws, |h| <= 6 beta, multiplier I_d(s)/I_1(s) <= exp[-(d-1)/(1+6beta)] in dimension d, and the path density bound eta(m/(1+6beta)) with eta(x) = sum_{d>=2} d^2 e^{-(d-1)x}. Re-derived the arithmetic: floor(r/2)/(1+6beta) >= 2(A+6) log n - 1/2, so eta <= C n^{-2(A+6)} and K eta = O(n^{-2A-9}).

**S32 (L202, conditioning on the whole tree). HOLDS.** Root-fixed vertex gauges preserve every based holonomy and send the tree links to product Haar (fresh child frames, from root to leaves), independently of the based products and of the opposite face. Given the tree, chords are Haar translates of their based products. So the raw prefix density relative to product Haar lies in [(1-eta)^K, (1+eta)^K] given the opposite face, and also for the marginal. The likelihood ratio is 1 + O(K eta), so the variation distance is O_A(n^{-A}). This is the tree device of row 1367 L92, combined with S31.

**S33 (L206, statement: product Haar fails at positive chord density). HOLDS** by S34-S36. Row 1323 after (18) (`gap-solve39-astra62.md` L215) does use a box partition at fixed density, as credited.

**S34 (L208-212, a short cycle). HOLDS.** Re-derived. The 2-core keeps E - V = delta n^3 - 1 and degree <= 6. The non-backtracking walk has uniform stationary law on oriented edges and entropy rate sum_v deg(v) log(deg(v)-1)/(2E') >= (log 5)(E'-V')/(2E') >= c delta, by concavity of log(d-1) on [2,6]. Two distinct q-step continuations with the same end, or a repeated vertex, give a cycle of length at most 2q (non-backtracking walks), so girth > 2q+2 makes the end map injective into at most (2q+3)^3 sites. This contradicts c q delta > 3 log(2q+3) for q = ceil(C delta^{-1} log(2+delta^{-1})) with C large. A cycle of length h < n is contractible.

**S35 (L214, what the Wilson marginal sees). HOLDS.** Taking an axis of the plaquette plane as time, the ordinary half-tilt (row 1334 (5), proved for any orientation and period) gives E_ord e^{beta(1-W_p)/2} <= C, hence E_ord(1-W_p)^2 <= C/(1+beta)^2. The positive-insertion form of (6) (S21) with conditional Jensen gives E_+(1-W_p) <= sqrt(8 E_ord(1-W_p)^2) after a time shift into an arc interior. With |1-U|^2 = 2(1-W), E_+|1-U_p| <= C(1+beta)^{-1/2}.

**S36 (L216, filling and separation). HOLDS.** A loop of length h < n lifts to a closed lattice loop; at most h^2/2 adjacent transpositions sort its letters by axis, each inserting one conjugated plaquette, and each axis block then reduces freely. The chord norm is conjugation invariant and subadditive, so E_+|1-U_cycle| <= C h^2/sqrt(1+beta) = o(1) since h = o(beta^{1/4}). Markov's inequality puts Wilson mass 1 - o(1) in the ball of radius sqrt(eps), whose Haar mass is O(eps^{3/2}). The last two sentences correctly say this does not bear on the conditional-versus-marginal target.

### G. Short-loop patch estimates and the short-time Wilson example after (12) (L220-276)

**S37 (L220, GUIDE). HOLDS** as a pointer; row 1231 (37)-(40) was not re-read.

**S38 (L222-230, statement (10)). HOLDS** by S39-S44. With s = floor(beta^theta), s^5 log beta = beta^{5 theta} log beta = o(beta^gamma) exactly when 5 theta < gamma, and gamma < 1/12 forces theta < 1/60.

**S39 (L232, setup). HOLDS.** This is row 1339 (1) with Delta = (log beta)(1/b + b/n + b/w) (S24). A translate of the s-cube misses a single retained box for a fraction O(s/b + b/n + b/w) of shifts.

**S40 (L234-244, the projection bound (11)). HOLDS.** Re-derived. (i) Per colour LL* = (1-c_0/b)^{-1} P with P the projection onto the curl image (row 1339 L44, check V7); the image is the same in tree gauge and for the full curl, since gradients have zero curl. For a patch cochain a extended by zero, D*a = d_1* a, and D*(I-P) = 0 gives ||d_1* a|| <= ||D|| ||Pa|| with ||D||^2 <= 24. (ii) On the cubical complex of [0,s]^3, the 2-cochain Laplacian is the sum of the three one-dimensional Laplacians (Kunneth; mixed terms cancel by the Koszul sign). On a component of type (edge, edge, vertex) the two edge factors are Dirichlet path Laplacians D_1 D_1*, and the partial-sum argument gives ||phi||^2 <= s(s+1)||D_1* phi||^2, so D_1 D_1* >= (s+1)^{-2}. (The exact lowest value is 4 sin^2(pi/(2s+2)).) On (ker d_1*)-perp = im d_1 one has d_2 a = 0, so ||d_1* a||^2 >= (s+1)^{-2}||a||^2. (iii) Hence the positive spectrum of L_v L_v* is at least c(s+1)^{-2}, P_v <= C(s+1)^2 L_v* L_v, and with at most C(s+1)^3 shifts per face, sum_v P_v <= C(s+1)^5 I. (iv) Row 1339 (2) (Carlen and Cordero-Erausquin; check V6) then gives the average entropy C(s+1)^5 Delta, and Pinsker with Jensen gives C(s+1)^{5/2} sqrt(Delta). Circulations of patch loops are linear in the curls by Stokes on the filled cube.

**S41 (L246-250, Fisher bound). HOLDS.** A coordinate-ordered tree of the cube has root paths of length at most 3s, so fundamental loops have length at most 6s+1, and there are 3s(s+1)^2 - (s+1)^3 + 1 <= C(s+1)^3 chords. Given everything else, the chord density is exp of a sum of plaquette terms, each multilinear in the chords, so log f is linear in each H_c with coefficient norm at most 6 beta. Integration by parts on S^3 gives int |grad_c log f|^2 f = 3 E[h_c . H_c] <= 18 beta.

**S42 (L252, the channel S_tau). HOLDS.** x^{-1}G is again standard Gaussian, so S_tau(x) has the law of x S_tau(1) = x exp(d), with d isotropic (conjugation invariance), mean zero, E|d|^2 <= C tau^2 (angle <= C tau|G| when tau|G| <= 1/2, Chebyshev on the rest). Re-derived the smoothing cost: for fixed d, ||sqrt(f)(. exp d) - sqrt f||_2 <= ||sum_c d_c . grad_c sqrt f||_2 (left-invariant fields commute with right translation along their own one-parameter group); averaging over independent mean-zero isotropic d_c removes cross terms and gives C tau (sum_c int |grad_c log f|^2 f)^{1/2}/2 <= C tau sqrt(beta k). For deterministic inputs, Gaussian KL ||x-x'||^2/(2 tau^2), Pinsker and the radial map give ||x-x'||/(2 tau).

**S43 (L254-263, nonlinear error). HOLDS.** The chart of row 1151 has tree logarithms of norm at most b^{-7/2} (`gap-solve5-astra62.md` L274, L313-315). Re-derived the curve comparison: both t -> prod exp(tX_e) and t -> exp(t sum X_e) have equal value and first derivative at 0 and second derivatives bounded by C(sum |X_e|)^2. Row 1231 (8) (`gap-solve26-astra62.md` L88-92) gives b^{-7} sum |X_e|^2 <= C b^{-2} sum |(dX)_p|^2 <= C b^{-2} sum (1-W_p), that is sum |X_e|^2 <= C b^5 sum (1-W_p), as the note says. Multiplicity at most h per edge over translates, and beta E sum(1-W_p) <= CV, give beta sum_c |H_c - exp A_c|^2 <= C k h^4/b^2 per shift. The bad-box probability e^{-c beta/b^8} is row 1151 L315.

**S44 (L265-270, (12) and the proof of (10)). HOLDS.** Re-derived the chain at one shift: removing smoothing costs C tau sqrt(beta k) = C eps sqrt k; the replacement costs E||H - exp A||/(2 tau) <= C sqrt(k) h^2/(b eps) plus the bad-box probability; the Gaussian step costs C(s+1)^{5/2} sqrt(Delta) by S40 and contraction. With eps = h/sqrt(b), both eps sqrt(k) and sqrt(k) h^2/(b eps) are at most C(s+1)^{5/2} b^{-1/2}. This gives (12), and each term tends to zero under s^5 log beta = o(b). Contractible loops have centre-invariant orbits, so (6) applies at each shift; Jensen over shifts and the factor two for the reference are as in S22. The orbit determines the raw patch up to the patch vertex gauges, and the kernel from orbits to raw patches does not depend on Y.

**S45 (L272, contribution to the sum). HOLDS.** With root-fixed gauges the tree is product Haar and independent of the based chord array; the full gauge adds an independent Haar root conjugation to that array. So the prefix law given Y differs from its marginal by at most the orbit distance in (10), and the losses through the tree and all chords of Q sum to o(1). Clipping is paid by row 1367 (6).

**S46 (L274, combining the two prefixes). HOLDS.** The joined graph is a spanning tree that keeps the patch comb and every private interval. The patch based products and Y are functions of links outside the private selections, so S31 gives, conditionally on them, long based products within O(K' eta) of independent Haar. A common Haar root conjugation keeps independent Haar long products independent Haar. Re-counted K' = (n/2)(n-s-2) floor((n-1)/(r+1)).

**S47 (L276, the short-time Wilson example). HOLDS.** At w' = floor(sqrt(log n)) and b = ceil(beta^gamma) <= C(log n)^gamma with gamma < 1/12, one has b^2/w' -> 0. Then b/w' -> 0 and (s+1)^5 (log beta) b/w' = [(s+1)^5 log(beta)/b] (b^2/w') -> 0, so (12) still tends to zero; (9) does not depend on the time. Row 1161 (19), as checked in row 1369 S1, gives s(2w') >= c n^3 e^{-2C sqrt(log n)} = n^{3-o(1)} -> infinity. By row 1367 (3), A <= (1+s)^{-1/2} -> 0, so the total loss D -> 1 while the combined prefix pays o(1). This is a valid counterexample, in the Wilson law itself, to inferring a small total from patch-by-patch decoupling. The physical time a_j w'_j -> 0, as stated. It is not a counterexample to the seed.

### H. The midpoint-radius and one-site tests (L280-335)

**S48 (L280-285, statement (13)). HOLDS** by S49-S51. At u = beta^{1+alpha/2}/sqrt(m) and an exponent alpha' in (alpha, 1/12), m u^2 beta^{-2-alpha'} = beta^{alpha-alpha'} -> 0 and m u^4 -> 0.

**S49 (L287-292, the neutral comparison). HOLDS.** Seam plaquettes with action beta(1 - eta W) are nonnegative, so dropping every plaquette outside the internal boxes dominates each seam term; Z_+ >= Z/8 (S20) costs a factor 8. Hence the row 1339 (1) domination (check V4) holds with an extra log 8. Given the cuts and seams the arcs are independent. Writing each bond's frames as (common frame g^-, relative frame), the reweighting depends only on the relative frame, so the common frame stays independent Haar and absorbs the sheet-flip reparametrization.

**S50 (L294-302, the action coupling (14)). HOLDS.** Talagrand's inequality, in the triangular form of row 1339 (4) (check V17), gives E|Z - G'|^2 <= 2(C_1 V Delta + log 8) at every C. G' is independent of (C, opposite arc), hence so is B. Re-derived (14): min(r^2/2, M) is sqrt(2M)-Lipschitz; the good-box radius error sums to C V/b^2 (row 1151 L315); the curl map is bounded; the tail E(A - M)_+^2 <= C e^{-cM} uses the exponential moments (half-tilt for temporal squares, the positive insertion of S21 at half the parameter for spatial squares); omitted squares cost O(1/b + b/n + b/w); bad boxes cost M^2 times sqrt(8 P_ord(bad)). Dividing by about w anchors and m squares gives (14), including the M/(wn^3) term from log 8. With b = beta^gamma, gamma > alpha, M = C_2 log beta, every term is O(beta^{-alpha}).

**S51 (L304, from coupling to information). HOLDS.** r_e^2 = 4 - 2A_e/beta = |U_e|^2, and R_e^2 = 4 - 2B_e/beta lies in [0,4] once beta >= C_2 log beta. The radial argument of S18 with q_R >= e^{-2u} gives D(q_r||q_R) <= C u^2 (r^2 - R^2)^2. With the extra common gauge, D(P_U || prod q_{R_e}) <= C m u^4 + C u^2 sum (r_e^2 - R_e^2)^2 (S17, S19). The reference observation built from B is independent of V, so I(X_u;V) <= E D(L(X_u|V) || ref) <= C m u^4 + 4C u^2 beta^{-2} E sum |A_e - B_e|^2, which is (13).

**S52 (L308, GUIDE). HOLDS.** Row 1178 (`gap-solve18-astra62.md` L126-160) has the words of length at most 12, the Pearson identity (9) and the finite-precision bound (10)-(11). Row 1186 (`gap-solve19-astra62.md` L283) has the Gaussian family with vanishing total unconditioned correlations.

**S53 (L310-319, identity (15)). HOLDS.** Re-derived. Along the diagonal, d/du I(Z_u;Z'_u) = d_1 I + d_2 I, the two halves are equal by the symmetry J(x,y) = J(y,x), and 2 d_1 I = E|E[S|Z,Z']|^2 - E|E[S|Z]|^2 = E|E[S|Z,Z'] - E[S|Z]|^2 by orthogonality of nested conditional expectations. Spatial translation invariance of the neutral circle makes every site contribute equally, giving the factor n^3, and I = 0 at u = 0.

**S54 (L321-329, (16)). HOLDS.** A_0 <= A_U: the noise is a common product channel and the product of noisy marginals is the channel image of Q. For the upper bound I checked row 1178's bin lemma and exception bound (`gap-solve18-astra62.md` L148-157): with h = n^{-4} and delta = h^5 every smallness condition there holds, a cell containing a good slice has linkwise diameter at most C h^2 modulo gauge and flips (random offsets do not matter), and the exception has mass C n^3 (1+6beta) h = O(beta/n) in the endpoint marginal of the squared neutral kernel, which is l. The Lipschitz bound of row 1178 L159 gives oscillation O(beta n^3 h^2) = O(beta n^{-5}) for log J and log Q on good cell pairs. Binned affinity <= e^{O(beta n^{-5})} A_0 + sqrt(J(bad)Q(bad)). Decoding: n^3/(delta sqrt(U_n)) = n^{3+20-26} = n^{-3}, and a variation change e moves square roots by at most sqrt(2e). Data processing for the added offsets and decoding gives A_U <= decoded affinity.

**S55 (L331-335, (17) and its converse). HOLDS.** A_U >= exp(-T_n/2) by Jensen. A strict margin below log(25/21) gives liminf A_0 > sqrt(21)/5, hence D <= 1 - tau eventually and row 1367 (7) by (6), and also directly s(2w_j) <= 4/21 by row 1367 (3). Converse: T_n <= I_J(X;Y) by data processing, and I_J(X;Y) <= 2 log(1+s(w)) - log(1+s(2w)) by the diagonal Cauchy-Schwarz bound of row 1165 (3) applied to the positive kernel P_0 T^w. A small s at a fixed aspect on an enlarged side then follows from the propagation used for the converse of row 1367 (7) (checked in row 1369 S22). As stated, the converse may change the side.

### I. The first responding angular moment (L339-363)

**S56 (L339, statement). HOLDS** by S57-S61. The cycle space of the spatial graph has dimension 3n^3 - n^3 + 1 = 2n^3 + 1 and maps onto H_1(T^3; F_2) = F_2^3, so in any chord order exactly three chords enlarge the span of the earlier classes. The note correctly says that only a degree, not a uniform amplitude, is identified.

**S57 (L341-346, inequality (18)). HOLDS.** Injectivity: T_P = P M C M P with C a product of class-function convolutions with strictly positive multipliers I_{j+1}(beta)/I_1(beta) and M bounded above and below on the finite cube, so <f, T_P f> = <Mf, C Mf> > 0 for nonzero gauge-invariant f; P_0 commutes, and powers stay injective. B - sigma |Omega><Omega| >= 0 because B >= 0 has top eigenvector Omega. Continuous positive kernels give positive point matrices, so the Schur product (B - sigma Omega x Omega) o B is a positive kernel, and J = B o B >= sigma (Omega x Omega) o B gives (18). Strict positivity uses that Omega f is neutral and nonzero. Then E_J[f(X)f(Y)] > 0 rules out E_J[f(Y)|X] = 0. The injectivity is the one of row 1178 L137, as credited.

**S58 (L348, the tests F_i). HOLDS.** After the tree is revealed, H_i = A y_i^{+-1} B with A, B known, so t_i = Re H_i is linear in y_i with a unit coefficient. A sheet flip multiplies H_i by (-1)^{<g,a_i>}. A class in the span of earlier classes is the sum of at most three of them (a basis of the span has at most three elements), so F_i = t_i prod_{J_i} t_j is centre invariant; t_i^2 is centre invariant for a span-increasing chord. Each t_j vanishes only on a Haar-null set, and l is equivalent to Haar.

**S59 (L350, the contradiction). HOLDS.** Re-derived: b_i = E_l[F_i | Y_{<i}] is invariant up to null sets (substitution with the invariant l and F_i), so f_i is neutral; it is nonzero because F_i is a nonconstant function of y_i and the conditional density of y_i is positive. Under Q, E_Q[F_i | X, Y_{<i}] = b_i. Under J the conditional mean of F_i uses only the moments of y_i of degree at most 1 (span-preserving) or 2 (span-increasing). Equal moments would give E_J[f_i(Y) | X] = 0, which contradicts (18).

**S60 (L352, the three even laws). HOLDS.** Pick g in H^1(T^3;F_2) vanishing on the earlier classes and equal to 1 on a_i; a cocycle representative can be made trivial on the tree by vertex signs. It then equals +1 on every earlier chord and -1 on chord i. This sign map on Y alone is a symmetry of J and of Q (gauge and centre invariance on each face), fixes X and the prefix, and negates y_i; so both next-link laws are even.

**S61 (L354, almost every history, and clipping). HOLDS.** The kernel is an integral over compact groups of exponentials of polynomials in the ambient coordinates, so all prefix densities are restrictions of entire functions, and the moment ratios are real analytic with positive denominators. A real-analytic function on a connected product of spheres that is not identically zero has a null zero set. On a span-increasing chord the constant term agrees and odd terms vanish, so degree two responds. Clipping: Pi_d p has integral one and is positive on an open set U; equal positive parts would force Pi_d q = Pi_d p on U and hence everywhere. So each clipped Hellinger term is strictly positive.

**S62 (L356-361, inequality (19)). HOLDS.** |E_J[F_i | X,Y_{<i}] - b_i| <= ||p_i - q_i||_1 = 2 d_TV <= sqrt(2 KL) by Pinsker. With delta_i that difference, c_i = E_J[f_i(X) delta_i], and Cauchy-Schwarz with E_J f_i(X)^2 = v_i gives c_i^2 <= 2 v_i I_i. c_i > 0 by (18). The chain rule over all links (tree terms zero) gives the sum bound by I_J(X;Y).

**S63 (L363, every allowed degree). HOLDS.** chi_{d+1}(theta) = sin((d+1)theta)/sin(theta) satisfies |chi_{d+1}| <= d+1, has parity (-1)^d under H -> -H, and is a degree-d harmonic (eigenvalue -d(d+2)); the map y_i -> H_i is a sphere isometry and keeps the degree. Even d needs no multiplier; odd d on a span-preserving chord uses the same at most three earlier traces. The test is a pure degree-d function of y_i, so the argument of S59 shows that some degree-d coefficient responds, and S61 gives almost every history; a countable intersection over d follows.

### J. The log-trace decomposition (22)-(25) (L385-426)

**S64 (L385-397, identity (22)). HOLDS.** The vacuum pair law is lambda^{-w} Omega(x) F^w(x,y) Omega(y) dx dy = K d pi d pi, and int K(x,y) d pi(y) = 1 by F^w Omega = lambda^w Omega. int K^2 d pi^2 = Tr F^{2w}/lambda^{2w} = 1 + s(2w), the neutral form of row 1178 (9). L_i is the likelihood of the prefix, L_i = L_{i-1} p_i*/q_i*. Integrating y_i under q_i* gives H_i = E[L_{i-1}^2 int (p_i*)^2/q_i*] = H_{i-1}(1 + kappa_i) with nu_{i-1} = L_{i-1}^2 d pi^2/H_{i-1}. H_0 = 1 since L_0 = E[K|x] = 1, H_m = 1 + s(2w), and nu_m is proportional to K^2 d pi^2, which is J.

**S65 (L399, the vacuum one-link estimate). HOLDS.** lambda^{-M} F^M(x,y) - Omega(x)Omega(y) = lambda^{-2} <F(x,.), R_{M-2} F(.,y)> with ||R_{M-2}|| = (lambda_1/lambda)^{M-2}, which tends to zero uniformly at fixed volume. At finite M the slice y is interior to a positive Wilson torus, so its link conditionals are mixtures of g_h with |h| <= 6 beta; weak compactness of the mixing measures on the ball and joint continuity of g_h pass this to the limit. q* >= e^{-6 beta}/Z(h) >= e^{-12 beta}.

**S66 (L401-409, (23) and its O(n^{-5}) error). HOLDS.** Re-derived each constant. The Taylor error of row 1367 (5) is at most 2^{-(d+1)} <= e^{6beta} 2^{-(d+1)} once d+1 >= 24 e beta. ||Pi_d||_{2 -> inf} = sqrt(dim) because the reproducing kernel has constant diagonal with integral dim = sum_{k<=d}(k+1)^2 <= (d+1)^3. So ||p - Pi_d p||_inf <= (1 + (d+1)^{3/2}) e^{6beta} 2^{-(d+1)}, and with 2^{d+1} >= e^{30(1+beta)} n^{20} and d+1 = O(log n) in the band this is at most n^{-8} e^{-12 beta} for large n. Hence |q_{i,d}/q_i* - 1| <= n^{-8}. The numerator change moves sqrt(kappa_i) by at most 2 n^{-8} e^{-6beta} (triangle inequality in L^2(nu dv/q*)); x -> log(1+x^2) is 1-Lipschitz on x >= 0; the denominator change moves log(1+kappa) by at most -log(1-n^{-8}) <= 2n^{-8}. Over 3n^3 links the total is at most 12 n^{-5}. Both directions of the final remark follow, on the same side and time.

**S67 (L411, the paid prefix). HOLDS.** The (9) density bounds hold at each finite closing length M (the selected links stay interior with six incident plaquettes) and pass to the limit, for the conditional law given x and for the marginal. So the prefix likelihood is 1 + O_A(n^{-A}) uniformly, and H = 1 + E(L-1)^2 = 1 + O_A(n^{-2A}); by (22) the partial log trace is log H.

**S68 (L413-418, inequality (24)). HOLDS.** g_i = F_i - E_pi[F_i | Y_{<i}] are martingale differences, hence orthogonal in L^2(pi), neutral, of positive variance. Omega g_i/sqrt(v_i^pi) are orthonormal in L^2(dx) and orthogonal to Omega. For R = (F/lambda)^w on that space, sum_i |<e_i, R e_i>|^2 <= sum_i ||R e_i||^2 <= ||R P_perp||_HS^2 = s(2w), and <Omega g, R Omega g> = <g, P^w g>_pi. The disproof criterion is stated with the right quantifiers (every admissible side, a cofinal subsequence).

**S69 (L420-426, identity (25)). HOLDS.** D_{i-1} = E[K^2 | prefix] >= L_{i-1}^2 by conditional Jensen, and the thermal history density is D_{i-1}/H_m. Then E_{J_{<i}}[a_{i-1} chi_i^2] = E_{pi^2}[L_{i-1}^2 chi_i^2]/H_m = (H_i - H_{i-1})/H_m, which telescopes to s/(1+s). s <= 4/21 is s/(1+s) <= 4/25.

### K. Everything else

**S70 (L367-372, (20)). HOLDS.** By (15), the left side is I(Z_u;Z'_u) <= I(Z_u;Y). With S* independent of Y and coupled to S, I(Z_u;Y) <= E_Y D(L(Z_u|Y) || L(sqrt(u) S* + G)) <= u E|S - S*|^2/2 by joint convexity and the Gaussian translate formula. The coupling is that of S50 applied to beta(1 - S_{z,c}) with the reference min(|sum_p eps_p L_p G'|^2/2, M). Re-derived the two local facts: |W - 1|^2 = 2(1 - S) for a word W, and |1 - U_1U_2U_3| <= sum |1 - U_j| gives 1 - S <= 3 sum (1 - W_p). Per coordinate the error is O(beta^{-2-alpha}), so E|S - S*|^2 <= C n^3 beta^{-2-alpha}.

**S71 (L374-379, (21)). HOLDS.** For F = min(beta(1 - S_{0,c}), M), the gain E|E[F|O,Y] - E[F|O]|^2 equals E_P(F - phi(O))^2 - E_P(F - psi)^2 with phi optimal under the product law P' (where Y is independent of the patch). Since E_P(F - phi)^2 = E_{P'}(F - phi)^2 <= E_{P'}(F - psi)^2, the gain is at most M^2 d_TV(P,P') <= M^2 d_TV(L(D_Q,Y), L(D_Q) x L(Y)), which is o(1) by (10) and data processing through the kernel to O. The tail beyond M is small in L^2 uniformly by the exponential moment. The note correctly says (21) does not control (15), whose own-face observation leaves the patch.

**S72 (L381, OPEN). HOLDS.** T_n < log(25/21) is the per-site requirement sum_c int_0^{U_n} E|M_c|^2 < n^{-3} log(25/21). (20) is useless beyond u of order beta^{2+alpha}/n^3, far below U_n = n^{52}. Row 1153 (4) (`gap-solve6-astra62.md` L84) is J_T <= C N beta^{-3/16} l_beta^{9/8}, as quoted. Remark: row 1211's application of it at this aspect (`gap-solve22-astra62.md` L330) is labelled ARGUED there; the note does not lean on it.

**S73 (L428, OPEN). HOLDS.** In order (9) the paid part is O_A(n^{-2A}) by S67 and the rest is 2n^3 + 1 - K nonnegative terms; by S66 a strict limsup below log(25/21) for their sum would give the seed on that side.

**S74 (L430, RESULT). HOLDS.** It matches the statements above: the first responding degree (S56-S63), the paid partial sums (S28, S38, S46), the O(n^{-5}) log-trace formula (S66), and OPEN for the seed and the gap. Nowhere does the note claim the seed proved or disproved. The short-time example (S47) refutes an inference at a vanishing physical time, not the seed.

**S75 (L3, GUIDE). HOLDS at the spot check.** `library/prior/` has no `gap-seed2-astra62.md`; `library/open-registry.md` has no M-neutral or neutral-seed entry; `f9bf0dc29` is the commit that queued row 1371. A path-limited search of `research/mass-gap/*.md` on `8b11ae2bb95e` found none of the four phrases. I did not repeat the whole-tree search on the five refs.

**S76 (L5, GUIDE). HOLDS at the spot check.** Main's `research/mass-gap/library/prior/gap-crux-lit-2.md` L106 is the Chen-Eldan entry (spectral independence, discrete hypercube). PR 10133 at `89faef229ff6`, `ROTDEF.md` L681-696, leaves TQ = Cov(E_K[F_s], J_r), the coarse covariance with the far-shell angular-momentum flux, open. The `MASS_GAP_LOCAL_BLOCK_ASTRA.md` (11) quotation matches row 1369 S38.

**S77 (L7, GUIDE). HOLDS at the spot check.** PR 10114 at `f76f6c649cff`, `checks/review_crossover_import_criteria.md` L13, has "no plaquette meets two pivots". PR 10133, `NONLINEAR_READER_RETURN_ASTRA.md` L251-263, has the block-diagonal precision over disjoint field sets. The finite-clock perimeter bound and the Schur-complement hits were not re-read.

**S78 (L15, GUIDE). HOLDS** as a plan and status statement.

**S79 (L17, GUIDE). HOLDS.** The pointers match what I read: row 947 B1 (Gaussian electric kernel), row 1016 HS1 (positive plaquette identity, `gap-global-reform-max.md` L382), row 970 MM (`gap-direction2-max.md` L418), row 1165 (3), row 1290 (8), and the row 1369 credit corrections (its S11, S37).

**S80 (L19, GUIDE). HOLDS as GUIDE, index only.** The index lists GL3 at 2210-2213 and GL14 at 2475-2498 (chunk 02) and the measure with Laplace transform (1+t)^{-2} at 31871-31882 (chunk 29). Re-derived the multiplier: int e^{-beta(1-cos t)} chi_l (2/pi) sin^2 t dt = e^{-beta}(I_{2l} - I_{2l+2}) = 2(2l+1) e^{-beta} I_{2l+1}/beta, that is 2 e^{-beta} I_{2l+1}(beta)/beta per dimension. The CA-I range 2699-2713 is in the complete-account file, outside this index, and was not checked. `lit-balaban.md` L143 records CMP 102b Proposition 9, (189)-(190), as the background-minimizer response, as stated.

**S2 (L13, PROVED summary). HOLDS.** Each sentence matches a checked statement: three even chords and 2n^3 - 2 chords with responding linear moments (S56-S61), the distinction between response and uniform bounds (S62), (22)-(23) with error O(n^{-5}) (S64-S66), and the one-site test (15)-(17) (S53-S55).

## Restatements of earlier rows

- S1 restates row 1367 L11 and row 1356 (M1, M2), with attribution.
- S4: the Gaussian form of an electric step is row 947 (B1); S10 is row 1290 (8). Both are credited at L17 and L84.
- S6, inequality (2), is row 1165 (3) applied to the neutral Gaussian-midpoint kernel (credited).
- S16 is row 1334 (5) for one plaquette, using row 1149 (16) (credited). S17 uses the leaf cancellation of row 1337 (credited).
- S22-S24, (7)-(8), restate row 1339 (3) on the neutral circle at period 2w (credited, with its check V4-V14).
- S25 repeats the orbit kernel of row 1339 L19 and L72 for unicyclic components. L176 does not cite those lines; the cited (7) is row 1339 (3). Credit only; no verdict change.
- S31 is row 1145 (1)-(3) on a new graph (credited at L182 and L196). S32 is the tree device of row 1367 L92.
- S33 extends row 1323 after (18) (credited) to decreasing chord density.
- S40 uses row 1339 (2) and its projection bookkeeping (L44-46); S43 uses row 1231 (8) and the row 1151 chart (all credited).
- S47 uses row 1161 (19) and row 1367 (3); row 1337's vanishing-time test is credited.
- S49-S51 adapt row 1339 (1), (4), (5) to the neutral circle (credited).
- S53-S55 use row 1178 (9)-(11) and its bin lemma (credited); the converse of (17) is the propagation behind the converse of row 1367 (7).
- S57 uses the injectivity of row 1178 L137 (credited). S66 adapts row 1367 (5) (credited).
- S68, (24), is the orthonormal-family trace bound, the same device as row 1367 (2) and the orthonormal products of row 1149 (17). It is standard and not claimed as new.
- S72 quotes row 1153 (4) and row 1211 L330 (credited).

New as far as I found: the two-cut response identity (3) with its zero-field value (4); the strip bound (5); the neutral-to-ordinary bridge transfer (6); the rectangle graph of (9); the quantitative short-cycle separation; the patch bound (10)-(12) with the Hodge estimate (11); the short-time Wilson counterexample after (12); (13)-(14) on the neutral circle; the one-site test (15)-(17); (18)-(19) and the degree classification; (20)-(21); and the vacuum chi-square chain (22)-(25).

## Verdict table

| Id | Lines | Statement | Verdict |
|---|---|---|---|
| S1 | 11 | One-box question (OPEN) | HOLDS |
| S2 | 13 | Finite-volume summary | HOLDS |
| S3 | 23-27 | Projected transfer F | HOLDS |
| S4 | 29-33 | H*H = F, K = HH* | HOLDS |
| S5 | 35-44 | Two marked bonds, (1), density K^w(x,y)^2/Tr F^{2w} | HOLDS |
| S6 | 46-51 | (2) | HOLDS |
| S7 | 55-60 | (3) | HOLDS |
| S8 | 62-69 | First derivative | HOLDS |
| S9 | 71-76 | Mixed derivative | HOLDS |
| S10 | 78-82 | Posterior on a marked bond | HOLDS |
| S11 | 84 | GUIDE, row 1290 | HOLDS |
| S12 | 88-93 | (4) | HOLDS |
| S13 | 95 | Gauge averages at a cut | HOLDS |
| S14 | 97-101 | Fourth-cumulant derivation | HOLDS |
| S15 | 105-109 | (5) | HOLDS |
| S16 | 111-115 | Plaquette moment | HOLDS |
| S17 | 117-123 | Random gauge on a face | HOLDS |
| S18 | 125-131 | Radial reference | HOLDS |
| S19 | 133 | Assembly of (5), strips | HOLDS |
| S20 | 137-151 | (6), Z_+ >= Z/8 | HOLDS |
| S21 | 153-158 | Proof of (6) | HOLDS |
| S22 | 160-165 | (7) | HOLDS |
| S23 | 167-172 | (8) from row 1339 | HOLDS |
| S24 | 174 | Change of aspect | HOLDS |
| S25 | 176 | Unicyclic prefix | HOLDS |
| S26 | 178 | Prefix sum | HOLDS |
| S27 | 182 | GUIDE | HOLDS (partly read) |
| S28 | 184-190 | (9) | HOLDS |
| S29 | 192 | The graph | HOLDS |
| S30 | 194 | Private selections | HOLDS |
| S31 | 196-200 | Density bounds | HOLDS |
| S32 | 202 | Tree conditioning | HOLDS |
| S33 | 206 | Haar fails at chord density delta | HOLDS |
| S34 | 208-212 | Short cycle | HOLDS |
| S35 | 214 | What the marginal sees | HOLDS |
| S36 | 216 | Filling and separation | HOLDS |
| S37 | 220 | GUIDE | HOLDS (pointer) |
| S38 | 222-230 | (10) | HOLDS |
| S39 | 232 | Setup | HOLDS |
| S40 | 234-244 | (11) | HOLDS |
| S41 | 246-250 | Fisher bound | HOLDS |
| S42 | 252 | Channel S_tau | HOLDS |
| S43 | 254-263 | Nonlinear error | HOLDS |
| S44 | 265-270 | (12), proof of (10) | HOLDS |
| S45 | 272 | Contribution to the sum | HOLDS |
| S46 | 274 | Combined prefix | HOLDS |
| S47 | 276 | Short-time Wilson example | HOLDS |
| S48 | 280-285 | (13) | HOLDS |
| S49 | 287-292 | Neutral comparison | HOLDS |
| S50 | 294-302 | (14) | HOLDS |
| S51 | 304 | Coupling to information | HOLDS |
| S52 | 308 | GUIDE | HOLDS |
| S53 | 310-319 | (15) | HOLDS |
| S54 | 321-329 | (16) | HOLDS |
| S55 | 331-335 | (17) and converse | HOLDS |
| S56 | 339 | First responding degree | HOLDS |
| S57 | 341-346 | (18) | HOLDS |
| S58 | 348 | Tests F_i | HOLDS |
| S59 | 350 | Contradiction | HOLDS |
| S60 | 352 | Three even laws | HOLDS |
| S61 | 354 | Almost every history, clipping | HOLDS |
| S62 | 356-361 | (19) | HOLDS |
| S63 | 363 | Every allowed degree | HOLDS |
| S64 | 385-397 | (22) | HOLDS |
| S65 | 399 | Vacuum one-link estimate | HOLDS |
| S66 | 401-409 | (23), error O(n^{-5}) | HOLDS |
| S67 | 411 | Paid prefix | HOLDS |
| S68 | 413-418 | (24) | HOLDS |
| S69 | 420-426 | (25) | HOLDS |
| S70 | 367-372 | (20) | HOLDS |
| S71 | 374-379 | (21) | HOLDS |
| S72 | 381 | OPEN | HOLDS |
| S73 | 428 | OPEN | HOLDS |
| S74 | 430 | RESULT of the row | HOLDS |
| S75 | 3 | GUIDE, search record | HOLDS (spot check) |
| S76 | 5 | GUIDE, method hits | HOLDS (spot check) |
| S77 | 7 | GUIDE, method hits | HOLDS (spot check) |
| S78 | 15 | GUIDE, plan | HOLDS |
| S79 | 17 | GUIDE, lane pointers | HOLDS |
| S80 | 19 | GUIDE, published sources | HOLDS (index only) |

Counts: 80 statements (66 PROVED-labelled, 10 GUIDE, 3 OPEN, 1 RESULT); 80 HOLD; 0 HOLD AFTER CORRECTION; 0 FAIL. Remarks that change no verdict: S5 (wording of "half-weights"); S24 (the period-2w gluing comparison of row 1151 is used without re-derivation); S25 (missing credit to row 1339 L19); S72 (row 1211's use of row 1153 is ARGUED there); S80 (the CA-I range is not in the index and was not checked).

RESULT: Row 1371 checked by hand by Claude Opus 5.5 (FINISH row 1372, laptop Claude subagent; cross-provider; grants no status): 80 statements, 80 HOLD (10 GUIDE lines, four of them only spot-checked), 0 HOLD AFTER CORRECTION, 0 FAIL; main corrections: none to the mathematics, remarks only (L176 should also credit row 1339 L19 for the orbit kernel; L174 uses the row 1151 gluing comparison at period 2w without re-deriving it; row 1211's step quoted at L381 is ARGUED there); main findings: the two-cut identity (3) and its zero-field value (4), the strip bound (5), the bridge transfer (6), the exact-angle prefix (7)-(8) from row 1339 (3), the tree-first order (9) with K of order n^3/((1+beta) log n) paid chords and the failure of product Haar at any chord density, the patch bound (10)-(12), the short-time Wilson counterexample (patches decouple at w' = floor(sqrt(log n)) while the total loss tends to 1), (13)-(17), the degree classification with (18)-(19) (linear moments respond on 2n^3 - 2 chords, degree two on exactly three), and the exact chi-square chain (22)-(25) with the O(n^{-5}) projected form (23) all hold as stated; the note nowhere claims the seed proved or disproved; open: a cutoff-uniform bound below log(25/21) on the unpaid 2n^3 + 1 - K terms of (23) (or, as sufficient tests on the same side, a bound below log(25/21) on T_n in (17) or on the remaining square of (3)) at w = floor(n/1024) on one admissible side, hence the Wilson neutral seed and the mass gap.
