# Area law below beta_W = 2/3 from (AS-bg)? (FINISH row 825), by Claude Opus 5.5 (max effort), author

- Clone: `/Users/jonreilly/ym4d-lead/clone`, commit `da92c56e26bcd657a0fb53ae27ce7b782c74e7ba`
  (`git pull --ff-only` said "Already up to date"). During the run the clone advanced to
  `b9dabda264dd5a026c5c3b163fc69d7d30942a40` (rows 823-827, surface classes). `git diff --stat` shows the
  four library files read here unchanged between the two commits, and the new `gap-rtail-astra.md` has
  no hit for area law, Wilson loop, Durhuus or AS-bg.
- Lane directory D = `.claude/science/physics-loops/ym4d-hard-route-20261030`.
- Read in full: `D/library/gap-vmf-lip.md` (609 lines; Codex gpt-6-astra, row 785),
  `D/library/gap-vmf-lip-check-opus.md` (153 lines; Claude Opus 5.5, row 790),
  `D/library/gap-novelty-opus.md` (389 lines; Claude Opus 5.5, row 819).
  Read: `D/library/gap-crux-fp.md` lines 300-460 (Claude Fable 5.2, row 712), which hold
  Section 4.2 in full, with 4.1, 4.2b and 4.3.
- Downloads. Each PDF was fetched once with `curl -sSfL https://arxiv.org/pdf/<id>`, each into its
  own new empty directory made by `mktemp -d` under `.../scratchpad/arealaw-dl/`:
  - arXiv:2509.04688v2 (8 pages, dated 28 Sep 2025): `.../arealaw-dl/cns2509.trR2te/cns-2509.04688.pdf`,
    sha256 `b74d2ca0555260cf218fe15bb105f34faeaa6674fcbe87215d597a83c3a373f5`.
  - arXiv:2505.16585v3 (35 pages, dated 26 Sep 2025): `.../arealaw-dl/cns2505.3xhoOB/cns-2505.16585.pdf`,
    sha256 `d89d819ad27ccbdce3c92626a8ceb687b589d08ab3cf045871ce1dc21bc2177d`.
  - Here `...` is `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad`.
  - The Read tool could not render PDF pages (pdftoppm is not installed). I compiled a PDFKit text
    extractor in a separate directory (`.../scratchpad/arealaw-tools/`), passed each PDF path as an
    argument, and read the text: 2509.04688 all 8 pages, 2505.16585 pages 1-10.
- For Section 6 I searched, without new downloads, the texts that row 819 fetched and extracted:
  `.../scratchpad/novelty-tools/{ceiling,hex-v4,hex-v7pdf,ax-2611.11534,ax-2606.19362}.txt` and the
  archive `.../scratchpad/novelty-dl/zen24117822.nfT8eM/4Y-M-v4.47.1.zip` (read with `unzip -p`;
  nothing was executed).
- All downloaded content was treated as data. No sign-in page and no refusal occurred.
- No repository file was edited. No numerical run was made.
- Marks. PROVED: proved here by me. READ: read in the named source, with page or line. ARGUED: an
  argument is given but not written to proof standard. GUIDE: a heuristic or a recalled number; it
  decides nothing. OPEN: not settled.
- Credits. `gap-vmf-lip.md` (Theorem V, Corollary V1, Lemma DC and Lemma INF in chord form, R-a and
  (AS-bg) for beta < 2/3): Codex gpt-6-astra. `gap-crux-fp.md` (the layer model, Identity L,
  Proposition TW, the statement (AS-bg)): Claude Fable 5.2. Line-by-line check of `gap-vmf-lip.md`:
  Claude Opus 5.5 (row 790). Comparison and conventions: Claude Opus 5.5 (row 819). The slab
  reduction is due to B. Durhuus and J. Frohlich (1980), as stated by S. Cao, R. Nissim and
  S. Sheffield. The comparison method is Dobrushin's.

## 0. Answer in brief

1. The statement (AS-bg) bounds a twist free energy. The hypothesis of CNS Theorem 2.3 is a
   covariance bound. The first does not give the second by itself (ARGUED, Section 3.6).
2. The two lemmas that prove (AS-bg), Lemma INF (12) and Lemma DC of `gap-vmf-lip.md`, give the
   covariance bound in one step (Lemma SC). So the CNS hypothesis holds for 4D SU(2) for every
   beta_W < 2/3, with C1 = 8/(1 - q), C2 = log(1/q), q = 3 beta_W/2 (Corollary H). PROVED, given the
   checked inputs.
3. I prove the slab reduction for SU(2) directly (Lemma R). It needs no expansion into matrix
   entries and no perimeter law. The result, Theorem A: on every periodic torus with sides at least 3,
   for 0 <= beta_W < 2/3 and every R x T rectangle with R, T at most half the torus sides,
   `|<W>| <= (2/(1 - q))^min(R,T) q^(RT)`. PROVED, given the checked inputs.
4. The same bound holds in every infinite-volume Gibbs measure and in free-boundary boxes
   (Corollary A3). PROVED.
5. The range beta_W < 2/3 is four times the 1/6 of Cao-Nissim-Sheffield. I found no source,
   refereed or not, that states an area law for 4D SU(2) at any beta_W >= 1/6 (Section 6).

## 1. Conventions and exact conversions

**Lane coupling (READ `gap-novelty-opus.md` lines 38-49).** The Wilson weight is
`exp(beta_W x_p)` per plaquette, with `x_p = (1/2) tr U_p = Re U_p`. The action is
`beta_W sum_p (1 - x_p)`. This is the physics coupling `beta_W = 4/g^2` for SU(2).

**Quaternions.** I identify SU(2) with the unit quaternions, that is with the unit sphere S^3 of R^4.
Haar probability is the uniform law sigma on S^3. For quaternions put `<a, b> = Re(a conj(b))`. This
is the Euclidean inner product of R^4. Left and right multiplication by a unit quaternion are
orthogonal maps; conjugation is the inverse on S^3. Three identities are used (PROVED, one line each
from `Re(ab) = Re(ba)` and `conj(ab) = conj(b) conj(a)`):
`Re(ab) = Re(ba)`, `<a c, b> = <a, b conj(c)>`, `<c a, b> = <a, conj(c) b>`.
The chord metric on S^3 is `|h - h'|` in R^4.

**The layer model (READ `gap-crux-fp.md` line 371; `gap-vmf-lip.md` lines 315-338).** On a periodic
box B, a site carries `h_x` in S^3. A bond b = (x, y) carries `y_b = h_x . O_b h_y` with `O_b` an
orthogonal 4 x 4 matrix fixed by the background, and a coefficient `J_b` in [-1, 1]. The law is
`mu(dh) proportional to prod_b exp(beta J_b y_b) prod_x sigma(dh_x)`. With `J = 1` and
`y_b = (1/2) tr(h(x) v_b h(x + e_i)^(-1) u_b^(-1))` this is the normalized integrand of `I(u, v)`.

**CNS normalization (READ arXiv:2509.04688v2 p. 2, (1.1)-(1.2), Definition 1.3).** The weight is
`exp(N beta sum_p Re Tr Q_p)` on the torus `Lambda_L = Z^d / L Z^d`, with product Haar measure.
The Wilson loop is `W_l = tr(Q_l)` with `tr = (1/N) Tr`.

**Conversion (PROVED).** For SU(2), N = 2 and `Re Tr Q_p = 2 x_p`. So
`N beta_CNS Re Tr Q_p = 4 beta_CNS x_p`, and

    beta_W = 4 beta_CNS.

The CNS slab action (READ p. 3, Definition 2.1) is `N beta_CNS sum_e Re Tr(Q_x A_e Q_y^(-1) B_e^(-1))`.
For SU(2) fields, `(1/2) Re Tr(Q_x A Q_y^(-1) B^(-1)) = Re(q_x a conj(q_y) conj(b))
= <q_x, b q_y conj(a)> = q_x . O q_y` with `O = L_b R_conj(a)` orthogonal. So the CNS slab law at
`beta_CNS` is the lane's layer law at `beta = 4 beta_CNS = beta_W`, with `J = 1`. This agrees with
row 819 (READ `gap-novelty-opus.md` lines 61-64).

**Thresholds (PROVED from READ statements).** CNS: `beta*_SU(N) = 1/(8(d - 1))` (READ p. 2,
Definition 1.4; it matches their Bakry-Emery constant `K = (N + 2)/2 - 1 - 4 N beta (d - 1)`, p. 5).
For d = 4 this is `beta_CNS < 1/24`, that is `beta_W < 1/6`. Lane: Lemma INF (12) gives the row sum
`alpha <= 3 beta_W/2`; `alpha < 1` is `beta_W < 2/3`, that is `beta_CNS < 1/6`. The ratio is 4.

## 2. What the Cao-Nissim-Sheffield reduction needs and gives

Source: S. Cao, R. Nissim, S. Sheffield, "Dynamical approach to area law for lattice Yang-Mills",
arXiv:2509.04688v2 (28 Sep 2025). Its publication status was not checked. Page numbers are the
paper's own. Everything in this section is READ unless marked.

**2.1 The slab law (p. 3, Definition 2.1).** G is a compact subgroup of U(N). Boundary fields
`A = (A_e)`, `B = (B_e)` take values in U(N) on the positively oriented edges of the
(d-1)-dimensional slice `Lambda^(d-1)`. The action is `S_A,B(Q) = N beta sum_(e = (x,y)) Re Tr(Q_x A_e Q_y^(-1) B_e^(-1))`,
and `d mu_A,B(Q) = exp(S_A,B(Q)) dQ / Z_A,B` with product Haar measure over the vertices. Remark 2.2
says that U(N)-valued fields are needed only for the U(N) case.

**2.2 Where it comes from (p. 3, opening of Section 2).** Fix an integer k. Condition on the edges in
the planes `x_d = k` (values `A_e`) and `x_d = k + 1` (values `B_e`). The vertical edges between the
two planes, identified by their base points, then have the law `mu_A,B` on the slice.

**2.3 The hypothesis (p. 3-4, Theorem 2.3, which CNS label as Theorems 1.2 and 1.3 of DF80).**
- G has a nontrivial scalar centre element: some `z` in U(1), `z != 1`, with `z I` in G.
- `d >= 2`, `beta >= 0`.
- `f^(ij)_x(Q) = (Q_x)_ij` and `g^(ij)_x(Q) = (Q_x^(-1))_ij` (matrix entries).
- There are constants C1, C2 "only depending on G,d,β (and in particular not on A,B)" such that,
  for all x, y in the slice and all indices,
  `|Cov_A,B(f^(i1 j1)_x, g^(i2 j2)_y)| <= C1 exp(-C2 d(x, y))`, the covariance under `mu_A,B`.

So the estimate is a **conditional two-point covariance** of matrix entries, in the law of one
height-1 slab given its two faces. It must be **uniform over all face fields A, B**, over all pairs
x, y, and (since the constants depend only on G, d, beta) over the side L of the torus. The slab is
a periodic (d-1)-torus of side L. `d(x, y)` is not defined in the text; I read it as the graph
distance of the slice (any of the usual distances is at most this one). The coupling is the
't Hooft beta of (1.2): `beta_W = 4 beta_CNS` for SU(2).

**2.4 The conclusion (p. 4, (2.2)).** There are C1, C2 depending only on G, d, beta such that for
every rectangular loop l in `Lambda_L` with side lengths at most L/2,
`|<W_l>_(Lambda,beta)| <= C1 exp(-C2 area(l))`. The state is the periodic torus measure (1.1);
Remark 1.2 (p. 2) says free boundary conditions on a cube change nothing and that all estimates are
uniform in L. The constants are not explicit.

**2.5 Their proof (p. 4, a sketch with a pointer to DF80).** Condition on all edges orthogonal to
the side of length T. Expand `tr(Q_l)` into `N^|l|` products of matrix entries. Each product
factors into T two-point functions `E_A,B[f_x g_y]` with `d(x, y) = R`, one per slab. The centre
gives `E_A,B[f_x] = z E_A,B[f_x]`, so `E[f_x] = 0` and each factor is a covariance. This gives
(2.3), `<tr Q_l> <= C1 N^|l| exp(-C2 area)`. A perimeter law ([Cha21, Lemma 12.3]) absorbs the
factor `N^|l|` when the area is not large against the perimeter.
- Note (ARGUED). The product of T factors, each at most `C1 exp(-C2 R)`, is `C1^T exp(-C2 RT)`.
  The printed (2.3) has `C1` for `C1^T`. The factor `C1^T` is of perimeter type and the same last
  step absorbs it, so the conclusion stands.

**2.6 Their verification of the hypothesis (p. 4-6, Proposition 3.2).** For SU(N) they prove the
Hessian bound `|Hess S_A,B(v, v)| <= 4 (d - 1) N beta |v|^2` (3.1), uniformly in A, B. Bakry-Emery
then holds with `K = (N + 2)/2 - 1 - 4 N beta (d - 1)` (p. 5), and decay follows as in
[SZZ23, Corollary 4.11] (p. 6). For SU(2), d = 4: `K = 1 - 24 beta_CNS > 0` iff `beta_W < 1/6`.
Theorem 1.6 (p. 2) is the combination: area law for `beta < beta*_G`.

**2.7 The companion paper (arXiv:2505.16585v3, 26 Sep 2025).** Theorem 1.2 (p. 2) treats U(N)
only, with `beta <= beta0(d)`; the weight is `exp(2 beta Re Tr U_p)` (p. 6, Definition 2.3); the
proof assumes N very large (p. 7, (2.1)), and Remark 1.3(1) (p. 2) sends bounded N to
Osterwalder-Seiler. It has no SU(2) statement. Page 1 says that, to the authors' knowledge,
Osterwalder-Seiler was the only earlier area-law result in four dimensions for any range of beta,
and that DF80 and Chatterjee 2021 give sufficient conditions in terms of mass-gap assumptions. Page 3 (Figure 1 caption) describes
the Osterwalder-Seiler range as `beta <= c(d)/N` for a small unspecified dimensional constant.

**2.8 Not read.** Durhuus-Frohlich, CMP 75 (1980) 103-151, and Chatterjee, CMP 385 (2021). Their
content enters here only through the CNS statements above. Section 4 does not use them: Lemma R
proves the reduction for SU(2) from scratch.

## 3. Does (AS-bg) supply that hypothesis? Step by step

### 3.1 The inputs from the lane (READ, with their checks)

- **Theorem V and Corollary V1** (`gap-vmf-lip.md` lines 59-220; check row 790, Sections 1-2, HOLDS).
  For `mu_F` proportional to `exp(F . h) sigma(dh)` on S^3: `d_Lip(mu_F, mu_F') <= |F - F'|/4` in the
  chord metric, for all F, F' in R^4.
- **Lemma DC, chord form** (`gap-vmf-lip.md` lines 222-313; check Section 3, HOLDS). For kernels
  `gamma_i` with `d_Lip(gamma_i(.|w), gamma_i(.|w')) <= C_ij |w_j - w'_j|` and
  `max_i sum_j C_ij <= alpha < 1`, if `gamma_i` are the conditional laws of mu at every site and of
  mu~ at every site outside D, then
  `|mu~(f) - mu(f)| <= 2 sum_i delta_i(f) sum_(j in D) (sum_(n >= 0) C^n)_ij <= 2 Delta(f) alpha^d/(1 - alpha)`,
  d the influence-graph distance from the support of f to D.
- **Lemma INF (12), chord form** (`gap-vmf-lip.md` lines 315-338; check Section 4, HOLDS). In the
  layer model at coupling `beta >= 0`, on a periodic box with sides at least 3, with arbitrary fixed
  orthogonal backgrounds and coefficients in [-1, 1]: `C_xy <= beta/4` for neighbours, 0 otherwise,
  and `alpha <= 3 beta/2`.
- **(AS-bg)** (`gap-vmf-lip.md` lines 352-417; check Section 5, HOLDS; the statement is
  `gap-crux-fp.md` line 412). For `0 <= beta <= beta_1 < 2/3`, every background, every box with
  sides at least 3 and every direction nu:
  `|log(I(u, c_nu v)/I(u, v))| <= C (|B|/b_nu) exp(-m b_nu)`.
  Its proof is Lemma DC with D = two planes of sites, applied to the bond functions `y_b` on the bonds
  that cross a third plane.

### 3.2 Lemma S (the slab law of 4D SU(2) is a layer law; PROVED)

Let `Lambda = prod_(mu=1..4) Z/L_mu Z` with all `L_mu >= 3`. Fix a direction nu ("vertical") and put
`Lambda' = prod_(rho != nu) Z/L_rho Z` (the horizontal torus). For z in `Lambda'` and k in `Z/L_nu Z`
let `q_(z,k)` be the variable of the edge from (z, k) to (z, k+1), and `a^k_(z,rho)` that of the edge
from (z, k) to (z + e_rho, k). Let H be the sigma-algebra of all edges not in direction nu.

(i) A plaquette in a plane (rho, rho') with rho, rho' != nu is H-measurable.
(ii) The plaquette of the plane (rho, nu) with lower corner (z, k) has
`x_p = q_(z,k) . O^k_(z,rho) q_(z+e_rho,k)`, with `O^k_(z,rho) = L_a R_conj(a')` orthogonal,
`a = a^k_(z,rho)`, `a' = a^(k+1)_(z,rho)`.
(iii) Given H, the vertical families `(q_(z,k))_z`, k in `Z/L_nu Z`, are independent. A regular
conditional law of slab k is the layer law `mu_k` on `Lambda'` at coupling `beta_W`, with `J = 1` and
`O_b = O^k_(z,rho)` on the bond (z, z + e_rho).

Proof. (ii) Going round p: `U_p = a q' conj(a') conj(q)` with `q = q_(z,k)`, `q' = q_(z+e_rho,k)`. By the
identities of Section 1, `Re U_p = Re(conj(q) a q' conj(a')) = <conj(q) a q', a'> = <a q', q a'>
= <a q' conj(a'), q> = q . (L_a R_conj(a') q')`. The other orientation gives the same real part.
(iii) The density of all edges with respect to product Haar measure is `Z^(-1) prod_p exp(beta_W x_p)`.
Every plaquette that is not of type (i) contains exactly two vertical edges, and both lie in the same
slab. So, given H, the density of the vertical edges is a constant times
`prod_k prod_(z,rho) exp(beta_W q_(z,k) . O^k_(z,rho) q_(z+e_rho,k))`, a product of functions of single
slabs. Under the reference measure the vertical edges are Haar and independent of H, so this product,
normalized slab by slab, is a regular conditional law. QED

This is the CNS slab law of 2.1 with `beta_W = 4 beta_CNS` (Section 1).

### 3.3 Lemma SC (background-uniform slab covariance; PROVED from Lemma INF (12) and Lemma DC)

Let B be a periodic box `prod_(i=1..3) Z/b_i Z` with all `b_i >= 3`. Let mu be a layer law on
`(S^3)^B` at coupling `0 <= beta < 2/3`, with any orthogonal `O_b` and any `J_b` in [-1, 1]. Put
`q = 3 beta/2` and `G = sum_(n >= 0) C^n`, with C the influence matrix of Lemma INF. Let `x != y` in B,
and let d(x, y) be the periodic graph distance. For xi in S^3 let `mu^xi` be mu conditioned on
`h_y = xi` (defined by its explicit density, Step 2). Then:

(a) `|mu^xi(h_x) - mu(h_x)| <= 2 G_xy <= 2 q^d(x,y)/(1 - q)` for every xi (Euclidean norm of the mean
    vector in R^4);
(b) `|mu(h_x . M h_y) - mu(h_x) . M mu(h_y)| <= 2 G_xy` for every real 4 x 4 matrix M with `||M|| <= 1`;
(c) mu is invariant under `h -> -h` at all sites. So `mu(h_x) = 0` and
    `|mu(h_x . M h_y)| <= 2 q^d(x,y)/(1 - q)`.

Proof.
Step 1 (kernels). The conditional law of `h_z` given the rest is `mu_(F_z)`, with
`F_z = beta sum_(b ni z) J_b O_b^(z) h_(z_b)`; here `z_b` is the other end of b, and `O_b^(z)` is `O_b`
or its transpose. These kernels are versions of mu's conditional laws, since the density is
continuous and positive. Lemma INF (12) gives `C_zw <= beta/4` for neighbours, `C_zw = 0` otherwise,
and row sums at most `q < 1`.
Step 2 (the conditioned law). Let `mu^xi` put `h_y = xi` and give the other sites the density
proportional to `prod_b exp(beta J_b y_b(h))` at `h_y = xi`, with respect to `prod_(z != y) sigma(dh_z)`.
For `z != y` its conditional law at z is again proportional to `exp(F_z . h_z)`, that is `gamma_z`.
So `mu^xi` has the kernels of mu at every site outside `D = {y}`. The y-marginal of mu has a continuous
positive density `rho_y`, and Fubini gives `mu = integral mu^xi rho_y(xi) sigma(d xi)`.
Step 3 (Lemma DC). Fix a unit vector e and put `f(h) = h_x . e`. Then `delta_x(f) = 1` and
`delta_z(f) = 0` for `z != x`. Lemma DC with mu, `mu~ = mu^xi` and D = {y} gives
`|mu^xi(f) - mu(f)| <= 2 G_xy`. The supremum over e gives the first inequality of (a). Since
`C_zw > 0` only for neighbours, `(C^n)_xy = 0` for `n < d(x, y)`; and `(C^n)_xy <= sum_w (C^n)_xw <= q^n`.
So `G_xy <= sum_(n >= d) q^n = q^d/(1 - q)`.
Step 4 (b). By Step 2, `mu(h_x . M h_y) - mu(h_x) . M mu(h_y) = integral (mu^xi(h_x) - mu(h_x)) . M xi rho_y(xi) sigma(d xi)`.
Its modulus is at most `sup_xi |mu^xi(h_x) - mu(h_x)| sup_xi |M xi| <= 2 G_xy`.
Step 5 (c). The map `h -> -h` at every site keeps `sigma^B` and every `y_b`, which is bilinear. So it
keeps mu, and `mu(h_x) = -mu(h_x) = 0`. Then (b) and (a) give (c). QED

At beta = 0 the sites are independent and G_xy = 0 for x != y, as it must be.

### 3.4 Corollary H (the CNS hypothesis for 4D SU(2) up to beta_W = 2/3; PROVED)

Let G = SU(2), d = 4 and `0 <= beta_CNS < 1/6`, that is `0 <= beta_W < 2/3`; put
`q = 3 beta_W/2 = 6 beta_CNS`. For every `L >= 3`, all fields `A, B` in `U(2)^(E+)`, all x, y in the
slice and all indices,

    |Cov_A,B(f^(i1 j1)_x, g^(i2 j2)_y)| <= (8/(1 - q)) q^d(x,y).

So the hypothesis of CNS Theorem 2.3 holds with `C1 = 8/(1 - q)` and `C2 = log(1/q)`, which depend
on beta only.

Proof. (1) Write `A_e = e^(i theta_e) A'_e` with `A'_e` in SU(2) (choose `e^(2 i theta_e) = det A_e`), and
`B_e = e^(i phi_e) B'_e` in the same way. The trace of an SU(2) matrix is real. So
`Re Tr(Q_x A_e Q_y^(-1) B_e^(-1)) = cos(theta_e - phi_e) Tr(Q_x A'_e Q_y^(-1) B'_e^(-1)) = 2 cos(theta_e - phi_e) q_x . O_e q_y`.
Thus `mu_A,B` is a layer law at coupling `4 beta_CNS = beta_W` with `J_e = cos(theta_e - phi_e)` in
[-1, 1] (`J = 1` for SU(2) fields), on the 3-torus of side `L >= 3`. Lemma SC applies.
(2) Write `Q = [[h1 + i h2, h3 + i h4], [-h3 + i h4, h1 - i h2]]` for h in S^3. Every entry of Q and of
`Q^(-1) = Q*` is `h . a + i h . b` with a, b among the signed standard basis vectors.
(3) The covariance `E[fg] - E[f] E[g]` is bilinear. It splits into four real covariances
`Cov(h_x . a, h_y . c)` with unit a, c and coefficients of modulus 1. Each one equals
`mu(h_x . M h_y) - mu(h_x) . M mu(h_y)` with `M = a c^T`, `||M|| = 1`. For `x != y`, Lemma SC (b) and (a)
bound each by `2 q^d/(1 - q)`; the sum is at most `8 q^d/(1 - q)`. For x = y, `|Cov| <= 2 < 8/(1 - q)`.
QED

For L <= 2 the CNS conclusion is empty or trivial: a loop with sides at most L/2 <= 1 is one
plaquette, and `|W| <= 1`. (PROVED; for L = 2 the slice has double bonds, and I did not re-check
Lemma INF there.)

### 3.5 The check, step by step

| Step | CNS Theorem 2.3 needs | What the lane gives | Status |
|---|---|---|---|
| 1 | the slab law `mu_A,B` of SU(2) at `beta_CNS` | the layer law at `beta = beta_W = 4 beta_CNS`, `J = 1`; `J = cos(theta - phi)` for U(2) fields | PROVED (Lemma S, Corollary H (1)) |
| 2 | uniformity in A, B | Lemma INF (12) holds for every orthogonal background and every J in [-1, 1] | READ (lines 315-338), check HOLDS |
| 3 | uniformity in L and in x, y | Lemma INF needs sides >= 3; nothing else depends on L, x, y | PROVED |
| 4 | a contraction | `alpha <= 3 beta_W/2 < 1` iff `beta_W < 2/3` | READ (12), Theorem V |
| 5 | a two-point covariance of matrix entries | (AS-bg) is a twist free energy, not a covariance; Lemma DC with D = {y} gives the covariance | PROVED here (Lemma SC) |
| 6 | constants depending only on (G, d, beta) | `C1 = 8/(1 - q)`, `C2 = log(1/q)` | PROVED (Corollary H) |
| 7 | a nontrivial scalar centre element | `z = -1`, `-I` in SU(2) | PROVED |
| 8 | the distance d(x, y) | the periodic graph distance of the slice | PROVED (path count, Step 3) |

So the gap between (AS-bg) and the CNS hypothesis is one application of the same Lemma DC that
proves (AS-bg). Both (AS-bg) and Lemma SC are consequences of the background-uniform contraction
(12); neither is derived from the other.

### 3.6 Why the statement (AS-bg) alone does not give the hypothesis (ARGUED)

- By (15)-(16) of `gap-vmf-lip.md`, (AS-bg) bounds `-2 beta sum_(b in Sigma_0) integral_0^1 E_(J^theta) y_b d theta`:
  bond means summed over one plane, in interpolated models. It is one number per background. The CNS
  hypothesis is a function of two sites at every distance. I know no inequality that bounds the
  second by the first. (ARGUED)
- (AS-bg) is the kind of input of flux or vortex criteria for confinement, not of DF80. Through
  Identity L (`gap-crux-fp.md` line 379) it bounds `1 - Z[k]/Z` uniformly in the time extent t.
  In a confining theory the electric-flux free energy grows like the area `b_nu t` (GUIDE: the
  standard picture, not used). A bound that does not decay in t cannot supply that growth.
  (ARGUED)

## 4. The area-law theorem for 4D SU(2)

### 4.1 Statement

**Theorem A (area law below beta_W = 2/3; PROVED, given Theorem V, Lemma DC and Lemma INF (12) of
`gap-vmf-lip.md`, all checked HOLDS in row 790).**
- State: `Lambda = prod_(mu=1..4) Z/L_mu Z` with all `L_mu >= 3` (periodic boundary conditions, sides
  may differ). `<.>` is the expectation of the Wilson measure
  `Z^(-1) prod_p exp(beta_W x_p) prod_e dU_e`, one factor per unoriented plaquette, Haar probability
  on each edge.
- Range: `0 <= beta_W < 2/3`. Put `q = 3 beta_W/2`.
- Loops: l is the boundary of a rectangle in a coordinate plane (mu, nu), `mu != nu`, with `R >= 1`
  edges in direction mu and `T >= 1` edges in direction nu, `R <= L_mu/2`, `T <= L_nu/2`; any
  position, base point and orientation.

Then

    |<W_l>| <= (2 q^R/(1 - q))^T   and   |<W_l>| <= (2 q^T/(1 - q))^R,

hence

    |<W_l>| <= (2/(1 - q))^min(R,T) q^(RT) = exp( -log(1/q) RT + log(2/(1 - q)) min(R, T) ).

The bound does not depend on the sides `L_mu`.

### 4.2 Lemma R (the slab reduction for SU(2); PROVED from Lemma S)

Take the setting of Lemma S with vertical direction nu. Let l be as in Theorem A, except that
`T <= L_nu - 1` replaces `T <= L_nu/2`; so its vertical edges on each side lie in T distinct slabs
`k0, ..., k0 + T - 1`.
Let x and `y = x + R e_mu` in `Lambda'` be the horizontal positions of its two vertical sides. Then,
almost surely,

    |E[W_l | H]| <= prod_(k = k0 .. k0+T-1) sup_(O in O(4)) |E_(mu_k)[q_(x,k) . O q_(y,k)]|.

Proof. `W_l = Re(Q_l)` does not depend on the base point or the orientation, since `Re(ab) = Re(ba)`
and `Re conj(U) = Re U`. Start at (x, k0) and go first in direction mu. Then
`Q_l = H_b V_y conj(H_t) conj(V_x)`. Here `H_b` (resp. `H_t`) is the product of the R horizontal edges
from x to y at level k0 (resp. k0 + T); `V_y = q_(y,k0) q_(y,k0+1) ... q_(y,k0+T-1)`; `V_x` is the same
at x. `H_b` and `H_t` are H-measurable unit quaternions. By the identities of Section 1,

    W_l = Re(conj(V_x) H_b V_y conj(H_t)) = <conj(V_x) H_b V_y, H_t> = <T_(k0+T-1) ... T_(k0) (H_b), H_t>,

where `T_k` is the random linear map `X -> conj(q_(x,k)) X q_(y,k)` of R^4, a function of slab k only.
By Lemma S (iii) the maps `T_k` are independent given H, with laws given by `mu_k`. The expectation
of a product of independent random matrices is the product of the expectations. So
`E[W_l | H] = <E_(mu_(k0+T-1))[T_(k0+T-1)] ... E_(mu_(k0))[T_(k0)] H_b, H_t>`, and, since `|H_b| = |H_t| = 1`,
`|E[W_l | H]| <= prod_k ||E_(mu_k)[T_k]||`. For unit X, Y in R^4,
`<Y, conj(q) X q'> = <q Y, X q'> = q . (R_Y^T L_X q')`, and `R_Y^T L_X` is orthogonal. So
`||E_(mu_k)[T_k]|| = sup_(X,Y) |E_(mu_k)[q_(x,k) . R_Y^T L_X q_(y,k)]| <= sup_O |E_(mu_k)[q_(x,k) . O q_(y,k)]|`. QED

This replaces the CNS sketch of 2.5. It needs no expansion into the `N^|l|` matrix entries, and so no
perimeter law.

### 4.3 Proof of Theorem A (PROVED)

First bound. Take nu as the vertical direction in Lemmas S and R. The horizontal torus `Lambda'` has
sides `L_rho >= 3`, rho != nu. Since `T <= L_nu/2 < L_nu`, Lemma R applies. In `Lambda'` the positions
x and `x + R e_mu` have periodic graph distance `min(R, L_mu - R) = R`, because `R <= L_mu/2`. Each
`mu_k` is a layer law on `Lambda'` at coupling `beta_W < 2/3` with `J = 1` (Lemma S (iii)). Lemma SC (c)
gives `sup_O |E_(mu_k)[q_(x,k) . O q_(y,k)]| <= 2 q^R/(1 - q)`, for every k and every value of the
horizontal edges. Lemma R then gives `|E[W_l | H]| <= (2 q^R/(1 - q))^T` almost surely. Take the
expectation.

Second bound. Repeat with mu as the vertical direction. Now `T <= L_nu/2` gives the distance T, and
`R <= L_mu/2 < L_mu` gives R distinct slabs.

Since `2/(1 - q) >= 2 > 1`, the smaller of the two bounds is the one with exponent `min(R, T)`. QED

The three inputs enter as follows: Theorem V gives the per-neighbour constant 1/4 (through
Corollary V1 and Lemma INF); Lemma INF gives the background-uniform row sum `3 beta_W/2`; Lemma DC
turns it into the covariance bound of Lemma SC. The Durhuus-Frohlich idea enters as Lemma S and
Lemma R.

### 4.4 Corollaries

**Corollary A1 (the CNS form, with constants; PROVED).** Put `s0 = log(1/q)` and `c0 = log(2/(1 - q))`.
- (i) `|<W_l>| <= exp(-s0 area(l) + (c0/4) |l|)`, with `|l| = 2(R + T)` the perimeter.
- (ii) `|<W_l>| <= C exp(-c area(l))` with `c = s0/2` and `C = exp(2 c0^2/s0)`.
- (iii) `-log|<W_l>|/(RT) >= s0 - c0/max(R, T)`, uniformly in the torus. So every lattice string
  tension defined from these loops is at least `log(2/(3 beta_W))`.

Proof. (i) `min(R, T) <= (R + T)/2 = |l|/4`. (ii) Put `s = min(R, T)`, `t = max(R, T)`. It suffices that
`s (c0 - (s0/2) t) <= log C`. If `t >= 2 c0/s0` the left side is at most 0. Otherwise `s <= t < 2 c0/s0`,
and the left side is less than `2 c0^2/s0`. (iii) Divide the exponent of Theorem A by `RT = st`. QED

Example (PROVED arithmetic). At `beta_W = 1/2`, three times the CNS threshold, `q = 3/4` and
`|<W_l>| <= 8^min(R,T) (3/4)^(RT)`. For a 20 x 20 loop this is
`exp(20 log 8 - 400 log(4/3)) < exp(41.6 - 115.0) < e^(-73)`.

**Corollary A2 (limit points; PROVED).** Let tori `Lambda_n` with `min_mu L_mu(n) -> infinity` be centred
at the origin of `Z^4`, and let mu be a probability measure on `SU(2)^(E(Z^4))` whose finite-dimensional
laws are limits of those of the torus measures. Then mu satisfies the bounds of Theorem A for every
rectangle. Proof. For n large the rectangle fits with sides at most `L_mu(n)/2`, and `W_l` is a
bounded continuous function of finitely many edges. QED

**Corollary A3 (free boundary, every boundary condition, every Gibbs measure; PROVED).** Let
`Lambda_n = {-n, ..., n}^4` and let `E_n` be the edges with both ends in `Lambda_n`.
- (a) Free boundary: `Z^(-1) prod_(p in E_n) exp(beta_W x_p) prod_(e in E_n) dU_e`. Every rectangle in
  `Lambda_n` satisfies the bounds of Theorem A.
- (b) Boundary condition omega on the edges outside `E_n`: `mu_(n,omega)` proportional to
  `prod_(p meets E_n) exp(beta_W x_p) prod_(e in E_n) dU_e`. If the rectangle lies in
  `{-n+m, ..., n-m}^4`, then `|mu_(n,omega)(W_l)| <= (2 q^R/(1 - q) + 4 q^(2m)/(1 - q)^2)^T`, and the
  same with R and T exchanged.
- (c) Every infinite-volume Gibbs measure mu of the Wilson specification on `Z^4` (the DLR equations
  for the kernels of (b)) satisfies `|mu(W_l)| <= (2/(1 - q))^min(R,T) q^(RT)` for every rectangle.

Proof. Lemma S holds in the box with the same proof. Given the horizontal edges in `E_n` and omega,
the vertical edges of slab k form a layer model on the cube `K = {-n, ..., n}^3`, without periodicity.
In case (b), a site z on the boundary of K also receives external terms `beta_W q_(z,k) . w` with w a
fixed unit vector, one for each plaquette whose other vertical edge lies outside `E_n`.
*Lemma INF' (PROVED; the proof of (12) word for word).* In this model `C_zw <= beta/4` for neighbours
in K and 0 otherwise, and all row sums are at most `6 beta/4 = q`. The external terms depend on no
site variable, and two distinct sites of K share at most one bond.
Lemma DC needs no periodicity, so Lemma SC (a) and (b) hold with d the graph distance of K, and Lemma R
holds unchanged. In case (a) there are no external terms, the law is invariant under `h -> -h`, and
Lemma SC (c) gives the factor `2 q^R/(1 - q)`. In case (b), Lemma SC (b) gives
`|mu_k(q_x . O q_y)| <= 2 q^R/(1 - q) + |mu_k(q_x)| |mu_k(q_y)|`. Let `mu_k^0` be the model with the
external terms deleted. It has row sums at most q and is invariant under `h -> -h`, so
`mu_k^0(q_x) = 0`. `mu_k` has the kernels of `mu_k^0` at every site off the boundary of K. Lemma DC with
`mu = mu_k^0`, `mu~ = mu_k` and `f = q_x . e` gives `|mu_k(q_x . e)| <= 2 q^m/(1 - q)`, because the graph
distance from x to the boundary of K is at least m. This proves (b). For (c), the DLR equations give
`mu(W_l) = integral mu_(n,omega)(W_l) mu(d omega)` once `E_n` contains l. Apply (b) with
`m = n - max |coordinate on l|` and let n tend to infinity. QED

So the area law holds in every Gibbs state for `beta_W < 2/3`, whether or not the Gibbs state is
unique. Uniqueness is known in the lane only for `beta_W < 2/9`.

### 4.5 Remarks

**Remark A4 (a sharper rate; PROVED).** In Lemma SC, `C <= (beta/4) A` entrywise, with A the adjacency
matrix of the slab. On the torus put `phi(z)` = periodic distance from `z_mu` to `x_mu`. Then
`(D^(-1) A D)_zw = A_zw e^(theta (phi(w) - phi(z)))` with `D = diag(e^(theta phi))` has row sums at most
`2 e^theta + 4`, and `(A^n)_xy = e^(-theta R) ((D^(-1) A D)^n)_xy <= e^(-theta R) (2 e^theta + 4)^n` for
`y = x + R e_mu`. So `G_xy <= e^(-theta R)/(1 - beta (2 + e^theta)/2)` for `0 <= theta < log(2/beta - 2)`, and

    |<W_l>| <= (2/(1 - beta_W (2 + e^theta)/2))^min(R,T) e^(-theta RT)   for every such theta.

The string-tension bound becomes `log(2 (1 - beta_W)/beta_W)`, against `log(2/(3 beta_W))`; both vanish
exactly at `beta_W = 2/3`. In free boxes and for Gibbs measures (Corollary A3) a linear phi gives row
sums `2 cosh(theta) + 4`, so there any rate below `arccosh(2/beta_W - 2)` is allowed (PROVED, same
lines).

**Remark A5 (other dimensions; PROVED by the same proofs).** In dimension `d >= 2` the slab torus is
(d-1)-dimensional with `2(d - 1)` distinct neighbours (sides at least 3). The proof of Lemma INF gives
`alpha <= (d - 1) beta/2`. Lemmas S, SC, R and Theorem A then hold with `q = (d - 1) beta_W/2`: an area
law for `beta_W < 2/(d - 1)`. The CNS range is `beta_W < 1/(2(d - 1))`. The factor 4 holds in every
dimension.

**Remark A6 (strong-coupling consistency; ARGUED, with one RECALLED fact).** At small beta, Remark A4
in a box gives a string-tension bound `arccosh(2/beta_W - 2) = log(4/beta_W) - O(beta_W)`. The
strong-coupling (character) expansion of SU(2) gives `<W> = u^(RT) (1 + ...)` with
`u = I_2(beta)/I_1(beta) = beta/4 + O(beta^3)` (RECALLED), that is a string tension
`log(4/beta) + O(beta^2)`. So the bound has the correct leading term and lies below the true value, as
it must. This is a check of the constants, not a proof of sharpness.

**Remark A7 (the black-box route; PROVED given READ).** Corollary H with CNS Theorem 2.3 (READ, p. 3-4)
also gives an area law for 4D SU(2) on tori for `beta_W < 2/3`, with unspecified constants. That route
rests on DF80 as stated by CNS. Theorem A does not.

## 5. Scope and limits

- **Strong coupling only.** `2/3` is far below the crossover. BB's Table I lists the open fixed-coupling
  range as about `2/9 <= beta_W <~ 2.2` (READ BB 18 Oct 2026, p. 20, in row 819's extracted text);
  `gap-crux-fp.md` line 458 puts it from 1/18 to about 2.
  Theorem A gives no mass gap and no uniqueness of the 4D Gibbs state for `beta_W >= 2/9`. Corollary A3
  holds in every Gibbs state, so it does not need uniqueness. (PROVED / READ)
- **Beyond every claimed gap range.** The claimed uniqueness or gap ranges stop at `2/9` (lane, BB
  Theorem E), `1/3` (BB forest gauge), `0.345-0.348` (Hexagon plaquette blocks), and `0.354` for a
  conditional three-link functional (Mihajlovic abstract, p. 1) (READ row 819 Sections 0 and 1; READ
  Mihajlovic p. 1). So for `0.354 <= beta_W < 2/3` the area law is proved where no gap claim exists, by
  the sources read.
- **No continuum statement.** (PHYS-SEED) of `gap-crux-fp.md` 4.3 is untouched. That section says such
  strong-coupling improvements move a lattice theorem but not (GAP) (READ line 458). This
  result moves no item on the mass-gap critical path. It is a side result on confinement.
- **SU(2) only.** Theorem V is a statement on S^3, and Lemma R uses the quaternion structure. For
  SU(N), N >= 3, this route needs a single-site Kantorovich bound on SU(N) and a replacement for
  Lemma R. OPEN.
- **The ceiling of the uniform slab route.** The hypothesis must hold for the flat background, where
  the slab is the 3D O(4) model. That model orders above a critical coupling near 0.94 (GUIDE:
  `gap-crux-fp.md` line 416; recalled value about 0.936). So no background-uniform slab bound passes
  about 0.94 for 4D SU(2). Between 2/3 and that value the uniform hypothesis is OPEN; Dobrushin's
  method stops at the mean-field value 2/3.
- **Verification boundary.** Lemmas S, SC, R, INF', Corollary H, Theorem A and its corollaries are my
  author proofs. They rest on Theorem V, Lemma DC and Lemma INF (12) of `gap-vmf-lip.md` (Codex
  gpt-6-astra), checked line by line by Claude Opus 5.5 in row 790. Nothing in this note has had an
  independent reading. The steps that most need one: Step 2 of Lemma SC (the conditioned law has the
  kernels off y), the quaternion identity and the independence step in Lemma R, and the mean
  comparison in Corollary A3 (b).

## 6. What is new

All competing sources are dated before 2026-11-12. "Found no" means a bounded search of the texts
named here; it is not an absence theorem.

**6.1 Refereed or published work (as framed by the row).**
- **Cao-Nissim-Sheffield, arXiv:2509.04688v2** (publication status not checked). Area law for
  `beta_W < 1/6` on tori and free boxes, constants not explicit (READ p. 2, Theorem 1.6, Definition 1.4,
  Remark 1.2). Their slab hypothesis is proved for `beta_W < 1/6` by Bakry-Emery (READ p. 4-6).
  Theorem A: the range `beta_W < 2/3` is **NEW** (four times). Corollary H (the slab hypothesis up to 2/3),
  the explicit constants (Corollary A1) and the every-Gibbs-state form (Corollary A3) are **NEW**.
- **Cao-Nissim-Sheffield, arXiv:2505.16585v3.** U(N) at large N; no SU(2) statement (READ p. 2, p. 7).
  Not comparable.
- **Osterwalder-Seiler 1978.** Not read. CNS describe its range as `beta <= c(d)/N` with a small
  unspecified c(d) (READ arXiv:2505.16585 p. 3) and as the only earlier 4D area-law regime (p. 1).
  An explicit range of `2/3` is **NEW** relative to that description.
- **Shen-Zhu-Zhu 2023.** No area law: CNS write that SZZ left the area-law question open (READ
  arXiv:2509.04688 p. 1). Their decay range is `beta_W < 1/12` (READ row 819, Section 1 table).
  **NEW** relative to it.
- **Durhuus-Frohlich 1980; Chatterjee 2021.** Not read. CNS describe both as sufficient conditions in
  terms of mass-gap assumptions (READ arXiv:2505.16585 p. 1). They are the reductions, not competing
  ranges. Lemma R re-proves the Durhuus-Frohlich reduction for SU(2); it is **EQUAL** in idea and
  self-contained here.
- **The single-site input against refereed work.** Row 819 found no refereed source for the uniform
  quarter; the best refereed Dobrushin constants for O(4) are weaker (Royer 1986: `J_c >= 2` for N = 4)
  (READ `gap-novelty-opus.md` Section 2.1). So relative to refereed work alone, the input is also new.

**6.2 Unrefereed preprints listed in row 819.**
- **Bhattacharjee-Bhattacharya, "Mass Gap of Lattice Yang-Mills Theory up to the Dobrushin Ceiling"
  (Zenodo, dated 18 Oct 2026).** The abstract (p. 1) states the uniform quarter for von Mises-Fisher
  laws; this is the key input of Lemma INF, **EQUAL** in its uniform form. Theorem E (p. 2): 4D
  uniqueness and decay for `beta_W < 2/9`. Theorem G and Proposition 18 (p. 3, p. 15): a box-hereditary
  total-variation finite-box condition HGDS implies boundary-uniform decay and, by Chatterjee's
  Theorem 2.4, the area law. The condition is verified only for 2D SU(2) (Proposition 21, p. 15). I found
  no 4D SU(2) area-law range, and no slab or Durhuus-Frohlich route (searches for area law, Durhuus,
  slab, sigma model). Theorem A's range is **NEW** relative to it.
- **Bhattacharjee et al., v4.47.1 (Zenodo 24117822, 10 Nov 2026).** The same conditional proposition
  (`strong-coupling/paper/main.tex`, label `prop:hgds`). `detailed/sec/10_massgen.tex` (near line 441)
  mentions a decay hypothesis close to Chatterjee's. No 4D SU(2) area-law range found. **NEW** relative
  to it.
- **Hexagon 2610.00341, v4 (30 Oct) and v7 (6 Nov 2026).** Both cite CNS for the area law (extracted v4
  text line 112, v7 line 93). No own area-law statement, no Durhuus, no sigma-model route found.
  **NEW** relative to it.
- **Mihajlovic, arXiv:2611.11534v1 (8 Nov 2026; "Version 5", 5 Nov).** Theorem 78.1 (p. 355) gives
  boundary-uniform covariance decay by total-variation Dobrushin for `q = 18 beta < 1`. Page 356 says
  that Chatterjee's theorem then gives a Wilson area law in this strong-coupling region. His
  proof uses oscillation `4 beta` per shared plaquette, the lane's old total-variation normalization
  with `beta = beta_W`, and his Wilson coupling is `2N/g0^2` (p. 356). So his range is `beta_W < 1/18`
  (ARGUED conversion). Page 383 takes a strong-coupling area law as an external input. Theorem A's
  range is **NEW** relative to it (twelve times).
- **Faizal-Shabir, arXiv:2606.19362v1 (9 Jun 2026).** Theorem 3.2 (p. 26) and Theorem B.4 (p. 171): a
  strong-coupling area law for `beta <= beta1` or `beta(N)`, existential, by character and polymer
  expansions. No explicit SU(2) threshold found. Hexagon v7's reference list gives a Fortschr. Phys. 74
  (2026) e70097 version; I did not check it. **NEW** relative to it.

**6.3 Verdict.** The area law for 4D SU(2) for `1/6 <= beta_W < 2/3` is **NEW** relative to every source
read, refereed or not. It is a short consequence of public ingredients: the uniform quarter
(Bhattacharjee-Bhattacharya Theorem 7, unrefereed, 18 Oct 2026; independently the lane's Theorem V,
which also gives the field-dependent constant), Dobrushin's comparison theorem, and the
Durhuus-Frohlich reduction as stated by Cao-Nissim-Sheffield. Anyone who combined the first and the
last could have found it. I found no source that does. The explicit constants and the every-Gibbs-state
form are **NEW** relative to CNS. The mechanism of the gain is also plain: in the slab each vertical
edge has 6 neighbours, against 18 in the 4D measure, and the sharp constant 1/4 per neighbour reaches
the mean-field value `6 beta_W/4 = 1`.

## 7. Marks

| Statement | Mark | Where |
|---|---|---|
| Conversion `beta_W = 4 beta_CNS`; CNS slab law = lane layer law at `beta_W` | PROVED | Section 1 |
| CNS Theorem 2.3 hypothesis and conclusion, Theorem 1.6, Proposition 3.2 | READ (arXiv:2509.04688v2 p. 2-6) | Section 2 |
| Missing `C1^T` in CNS (2.3); harmless | ARGUED | 2.5 |
| Theorem V, Corollary V1, Lemma DC, Lemma INF (12), (AS-bg) | READ (`gap-vmf-lip.md`; check row 790 HOLDS) | 3.1 |
| Lemma S (slab law of 4D SU(2)) | PROVED | 3.2 |
| Lemma SC (background-uniform slab covariance `<= 2 q^d/(1 - q)`) | PROVED | 3.3 |
| Corollary H (CNS hypothesis for `beta_W < 2/3`, `C1 = 8/(1 - q)`, `C2 = log(1/q)`) | PROVED | 3.4 |
| (AS-bg) alone does not give the hypothesis | ARGUED | 3.6 |
| Lemma R (slab reduction for SU(2)) | PROVED | 4.2 |
| Theorem A (`|<W>| <= (2/(1 - q))^min(R,T) q^(RT)`, tori, `beta_W < 2/3`) | PROVED | 4.1-4.3 |
| Corollaries A1, A2, A3 (constants; limit points; free boxes, all boundary conditions, all Gibbs states) | PROVED | 4.4 |
| Remark A4 (rates `log(2(1 - beta_W)/beta_W)` on tori, `arccosh(2/beta_W - 2)` in boxes) | PROVED | 4.5 |
| Remark A5 (dimension d: `beta_W < 2/(d - 1)`) | PROVED (same proofs) | 4.5 |
| Remark A6 (leading strong-coupling term matches) | ARGUED; `u = beta/4 + O(beta^3)` RECALLED | 4.5 |
| Uniform slab hypothesis for `2/3 <= beta_W <~ 0.94` | OPEN | 5 |
| No uniform slab bound beyond about 0.94 (flat background orders) | GUIDE | 5 |
| SU(N), N >= 3, by this route | OPEN | 5 |
| Novelty verdicts | READ (sources and pages in Section 6); bounded search | 6 |
| Independent reading of this note | OPEN (not done) | 5 |

RESULT: Yes, with one added step: (AS-bg) itself is a twist bound and does not supply the Cao-Nissim-Sheffield (Durhuus-Frohlich) hypothesis, but its two inputs (Lemma INF (12) and Lemma DC of gap-vmf-lip.md) give it by one more application of Lemma DC (Lemma SC: background-uniform slab covariance at most 2q^d/(1-q), q = 3beta_W/2), so CNS Theorem 2.3's hypothesis holds for 4D SU(2) for all beta_W < 2/3 (C1 = 8/(1-q), C2 = log(1/q)); with a self-contained SU(2) slab reduction (Lemma R) this proves Theorem A: on every periodic torus with sides at least 3, in free boxes and in every infinite-volume Gibbs state, every R x T rectangular Wilson loop (sides at most half the torus) obeys |<W>| <= (2/(1-q))^min(R,T) q^(RT), an area law with string tension at least log(2/(3beta_W)) for 0 <= beta_W < 2/3, four times the CNS range 1/6; PROVED given the row-790-checked Theorem V, Lemma DC and Lemma INF, not yet independently read, and NEW against every refereed and unrefereed source read (closest: CNS 1/6; Mihajlovic 1/18, unrefereed; Bhattacharjee-Bhattacharya give only a conditional criterion), though it is a short corollary of public ingredients (their sharp quarter, Dobrushin, DF80); strong coupling only: no mass gap, nothing for SU(N >= 3) or the continuum, and the uniform slab route cannot pass about beta_W = 0.94.
