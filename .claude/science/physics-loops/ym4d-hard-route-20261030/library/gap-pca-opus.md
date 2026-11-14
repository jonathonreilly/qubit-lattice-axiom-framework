lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T01:20Z

# Row 967, `gap-pca-opus`: plaquette cellular automata, PCA space-time Gibbs measures, and the gap crux

Started 2026-11-14T13:20Z on the Mac mini worker, at commit c8056a092 of `claude/ym4d-hard-route`.
Brainstorm-and-test item with literature. Owner's prompt (quoted in row 967): "i wonder if some wolfram style
approach to plaquetts could also be interesting here? cellular automata but with plaquetts? (left field brainstorm)".

Labels: PROVED (written argument, checkable by hand), CONDITIONAL (proved given a named input), GUIDE (a run; guides
or refutes only, never a step of the chain), ARGUED (heuristic, not a proof), OPEN.

## 0. Plan (at most eight steps; one step per response, appended before the next)

1. Read the inputs: row 962 (`library/gap-constraints-max.md`: constraint audit, idea table, ceilings), row 941
   Step 1 (the slice chain), row 947 (Theorem BR, (LSI-J-seed)), and grep the lane's idea inventories for PCA,
   cellular automata, Domany-Kinzel, Toom, Gacs, disagreement percolation, Bianchi, Batrouni-Halpern, Creutz,
   overrelaxation, Q2R. Write the crux in one paragraph and the list of prior matches.
2. Framing (a), the smallest case by hand: when is a (d+1)-dimensional Gibbs measure the space-time history of a
   d-dimensional PCA (site-factorised local updates)? State the exact criterion (a two-layer interaction with no
   intra-layer coupling in the update direction, plus the normalisation condition sum_{eta'} prod p = 1 that the
   PCA picture forces), and test it on Wilson SU(2) (and a Z_2 / U(1) lattice gauge toy) along the straight time
   axis and along diagonal / light-cone time directions. Prove or refute on the smallest case.
3. Literature check by URL (PCA/Gibbs correspondence: Goldstein-Kuik-Lebowitz-Maes, Lebowitz-Maes-Speer;
   Domany-Kinzel; Dobrushin-type PCA criteria; van den Berg-Maes disagreement percolation; Toom; Gacs), into a
   /tmp scratch folder, with what each actually gives.
4. Framing (b): which PCA ergodicity tools survive the outcome of Step 2; supremum versus averaged versions;
   comparison with the ceilings 2/3, 0.775, 4 G_3 = 1.0109; fact tests (U(1) photon, frozen groups, SMALL-BOX).
5. Framing (c): plaquette-level constraint systems (Bianchi on cubes, Batrouni-Halpern field-strength formulation,
   centre-vortex Z_2 surfaces, Creutz demons, overrelaxation, Q2R-type reversible rules): new input or reframing.
6. Optional GUIDE run (only if a step produces a falsifiable numeric claim, under the numeric lock).
7. Ranked list of what, if anything, deserves a proof lane.
8. RESULT line.

## 1. Inputs and prior matches (Step 1, READ at c8056a092)

**Read.** FINISH opening sections (How we work, Working efficiently, Rules), GOAL.md, rows 941, 947, 962, 963, 967
(lines 1018, 1024, 1039, 1040, 1044); `library/gap-lsivac-max.md` Steps 0-1 (L28-150, the slice chain);
`library/gap-constraints-max.md` Sections 1, 4 (A6) and 8 (L37-84, L205-215, L467-540); RESULT parts of rows 774,
821, 853; `library/gap-skeleton-max-b.md` L215-220 (idea A12) and L581-584. Row 963's output
`library/gap-rotgeom-opus.md` is not on disk at this commit.

**The crux in one paragraph (READ; nothing here is new).** The finish line (SEED-FP) needs one thermal sum of the
bare Wilson SU(2) transfer operator T_B on one periodic box to be small. By Lemma SPLIT (row 892) the SH seed on the
slab (a; (24a)^3) holds if the glue half S_ev <= 1/10 and the flux half Q_0 <= 1/20. Row 941 (Step 1, (A1)-(A7)):
the vacuum slice chain P = Omega^(-1) (T/lambda_0) Omega on L^2(nu) has one-step law
pi_x(dw) = e^(beta <x, w>) m(dw)/(lambda_0 phi_0(x)), an exponential family; log Omega = -V/2 + Lambda(beta x) - const
with Lambda convex; the two-slice law is J(dx, dw) = e^(beta <x, w>) m(dx) m(dw)/lambda_0. Row 947: Theorem BR (one
step is an ambient Brownian bridge of duration 1/beta) and Corollary BR-J: a log-Sobolev constant alpha_J of J gives
(HC-vac) with alpha >= min(alpha_J/(2 beta), 1). The smallest unproved inequality is (LSI-J-seed)_a:
alpha_J >= 2 beta K_a, K_a = (C_beta + 3 log a)/(a - 2), on (24a)^3 for one even a >= 30. Row 954: this needs
m_G >= K_a. Row 962: no relaxation of geometry, boundary, time direction or representation is a NEW INPUT; the seed
number is fixed by the measure and the scale, and a NEW INPUT can only be an order-one inequality for that number
or a comparison node between two measures.

**Fact tests that bind every idea here (row 962 1.4, READ).** FT-U1 (free photon and compact U(1) Coulomb fail the
seed); FT-FROZEN (frozen Q_8, 2T fail); K7 (mixed-action endpoint with no seed); SMALL-BOX (a fixed small box at
large beta has no gap in units of its side); FT-CEIL (worst-case single-link 1/3, single-site Dobrushin 2/3, vertex
blocks 0.775, background-uniform layer bounds false above 4 G_3 = 1.0109).

**Prior matches (rule 0a; grep of FINISH.md, `library/*.md`, `library/prior/*.md` at c8056a092).**

| Term | Where in the lane | What it says | Bearing on this row |
|---|---|---|---|
| Dobrushin, disagreement percolation | rows 690, 820-821, 853; `gap-brainstorm-max.md` L148; `gap-ds-gauge.md` L17-38; `prior/gap-lit-dp.md`; `prior/gap-lit-annealed.md` | GUIDE row 820: the single-link chord influence row sum has medians 2.13 (beta 0.5), 3.57 (1.0), 3.55 (2.3), 3.45 (2.5); every link is bad. Row 821: van den Berg-Maes and Gielis-Maes are finite-spin and quenched; no block or gauge-invariant influence bound for SU(2) is published. Row 853: annealed, space-time Peierls and PCA methods (Gielis-Maes-van de Velde for directed PCA; Swart-Szabo-Toninelli random Toom contours) exist for non-gauge, chiefly finite-spin systems; none usable for stationary Wilson SU(2) block dynamics. `gap-ds-gauge.md`: revealing in blocks fails for a cube with a collar | Framing (b) for supremum criteria is KNOWN dead at order-one beta; this row adds only what the PCA structure changes, if anything |
| coupling from the past | row 774 | WITHDRAWN before launch (certificate (16) reduced to a one-plaquette Wasserstein distance) | no prior attack on CFTP as a mixing tool |
| Gacs, Toom, eroders | `gap-brainstorm-max.md` L675 (Gacs hierarchical decoders, recalled); row 853 (Toom contours, literature) | named only, as literature | no prior analysis of non-ergodicity of a gauge PCA |
| plaquette variables, Bianchi | `gap-skeleton-max-b.md` A12 (L215-220) and L581-584; `gap-crux-restate.md`, `gap-sep-opus.md` | A12: in plaquette variables the Wilson measure is a Gaussian of variance 1/beta about 1 on each plaquette, restricted to the Bianchi variety; a Poincare inequality in the plaquette metric is FALSE as a route (it holds for U(1) with constant beta while the photon is massless). L581: one 3-cube partition function sum_k k^2 (2 I_k(beta)/beta)^6 has zeros in the right half-plane (GUIDE), so no Lee-Yang theorem | framing (c) Batrouni-Halpern is KNOWN in its magnetic-metric form and dead there |
| diagonal reflections, diagonal transfer | row 962 A6 (ARGUED, REFRAMING); row 963 item (3) (queued, Opus, not on disk) | reflection positivity across diagonal hyperplanes is row 963's question | NOT attacked here; this row asks only whether a diagonal time makes the update site-factorised (a different property) |
| cellular automata, PCA (probabilistic), Domany-Kinzel, light-cone time, Batrouni-Halpern, Q2R, microcanonical, Wolfram | only row 967 and this file (other "PCA" hits are principal component analysis in row 952) | none | NEW to the lane as terms |
| Creutz, overrelaxation | rows 944-957 GUIDE code | used only as samplers | no prior analysis of their invariant measures as a proof tool |

So framing (a) (a PCA structure of the Wilson measure) and the non-ergodicity side of (b) are new to the lane;
the supremum side of (b) and the magnetic-metric side of (c) are KNOWN dead. Steps 2-5 work on the new parts and
state, for the old ones, only what the PCA structure changes.

## 2. Framing (a): is the Wilson measure the space-time history of a PCA? (Step 2, by hand)

**Answer.** No, for D >= 3 and beta > 0, along the axis time and along the light-cone (body-diagonal, Domany-Kinzel)
time (PROVED, 2.2 and 2.3). Yes for D = 2, where it is the known independence of plaquettes. What is true instead in
both directions is a Feynman-Kac form: (electric PCA) x (magnetic potential) (Identity 2.6, Proposition 2.7). The
measure that IS a PCA history (the "gauge disorder variety", 2.4) drops the magnetic energy, so it is not Yang-Mills.

Credit. PCA <-> space-time Gibbs measures: Goldstein, Kuik, Lebowitz and Maes (1989); Lebowitz, Maes and Speer (1990).
Light-cone PCA and the Ising disorder line: Domany and Kinzel (1984); Rujan (1987); Georges and Le Doussal (1989). All
recalled here, to be read in Step 3. Slice chain: rows 931, 941 (transfer frame credited there to Ethan Sussman and
Levent Alpoge, with Claude and Codex as authors of their text). New here: Lemma 2.4, Proposition 2.5, Proposition 2.7.

### 2.1 Setting and the criterion

G = SU(2) as the unit sphere of R^4, <a, b> = (1/2) tr(a b^(-1)). Wilson factor f(V) = e^((beta/2) tr V) =
sum_n (n+1) b_n chi_n(V), b_n = 2 I_(n+1)(beta)/beta > 0 (check: b_n = (I_n - I_(n+2))/(n+1) by sin a sin b, then the
Bessel recurrence). A *layering* is a time function on vertices with finite slices S_t, and a partition of the link
variables into finite *sites*, each attached to one slice. The Wilson weight is *first order* if
prod_p f(U_p) = prod_t K(Y_t, Y_(t+1)), Y_t = the variables of the sites of S_t, K continuous and > 0 on a compact space.

Vacuum chain. By Jentzsch's theorem K has a simple top eigenvalue lambda with an eigenfunction phi > 0. The
bi-infinite Wilson measure is the stationary chain with kernel P(Y, dY') = K(Y, Y') phi(Y') dY'/(lambda phi(Y)).
**Definition.** The Wilson measure is the history of a PCA on these sites iff P(Y, .) is a product measure over the
sites of Y' for every Y. (A stationary path law fixes its Markov kernel almost everywhere, and P is continuous.)

**Lemma 2.1 (criterion, PROVED).** Let K(Y, Y') = prod_(s' in S_(t+1)) k_(s')(X'_(s'); Y) for every Y. Then P is a
PCA iff phi = prod_s e^(f_s(X_s)) for site functions f_s. Then the eigen-equation reads
prod_(s') integral k_(s')(X; Y) e^(f_(s')(X)) dX = lambda prod_s e^(f_s(X_s)) for all Y.
Proof. P(Y, dY') is proportional to prod k_(s')(X'_(s'); Y) phi(Y') dY'. If it equals prod q_(s')(X'_(s')) for one Y,
then phi = c prod (q_(s')/k_(s')) is a product (all factors positive). The converse is direct. QED

### 2.2 Axis time: the slice chain of row 941 is not a PCA

**Proposition 2.2 (AX, PROVED).** D >= 3, beta > 0, periodic spatial box of side >= 3, temporal gauge, sites = spatial
links. The vacuum slice chain P of row 941 is not a PCA.
Proof. By row 941 (A1), P(x, dw) is proportional to e^(beta <x, w>) e^(-V(w)) phi_0(w) dw with phi_0 = e^(V/2) Omega.
If it is a product over links for one x, then log phi_0(w) - V(w) = sum_l g_l(w_l) + c. V and phi_0 are gauge
invariant, so sum_l g_l is gauge invariant. A gauge transformation h at one vertex changes only the links at that
vertex, which are independent variables; so each g_l there changes by a constant c_l(h), each c_l is a continuous
homomorphism G -> R, hence 0 on the compact G. So each g_l is invariant under left (or right) multiplication, hence
constant. Then Omega is proportional to e^(V/2), and T_0 Omega(x) is proportional to
e^(-V(x)/2) integral e^(beta <x, w>) dw = e^(-V(x)/2) (2 I_1(beta)/beta)^(#links). This is proportional to
e^(V(x)/2) only if V is constant on M, which is false for beta > 0. QED
Reading (PROVED, an identity). K(x, w) = z_0^(#links) P_0(x, w) e^(-V(w)) with z_0 = 2 I_1(beta)/beta and
P_0(x, dw) = prod_l e^(beta <x_l, w_l>) dw_l / z_0: a trivial PCA (each link an independent heat-bath walk on G) times
the magnetic potential e^(-V). For D = 2 there is no spatial plaquette, V = 0, and P = P_0 is a PCA.

### 2.3 Light-cone time (the Domany-Kinzel geometry)

Lattice. Lambda_0 = {v in Z^D : sum v_mu = 0}; the light-cone cylinder C_(D,L) = Z^D/(L Lambda_0), L >= 2. The time
tau(n) = sum_mu n_mu is well defined; each slice S_t = {tau = t} has L^(D-1) vertices; every link (n, n + e_mu) runs
from S_t to S_(t+1). The site of a vertex m is X_m = (U(m - e_rho, rho))_(rho = 1..D) in G^D, the links with head m.
Each link lies in exactly one site.

**Lemma 2.3 (structure, PROVED).** (a) A plaquette p = (n; mu, nu) has the unique top vertex m = n + e_mu + e_nu. Its
links U_nu := U(m - e_nu, nu) and U_mu := U(m - e_mu, mu) lie in X_m; U(n, mu) lies in X_(m - e_nu) and U(n, nu) in
X_(m - e_mu). (b) U_p = U(n, mu) U_nu U_mu^(-1) U(n, nu)^(-1), so tr U_p = tr(U_mu^(-1) g_(mu nu) U_nu) with the wedge
transporter g_(mu nu) := U(n, nu)^(-1) U(n, mu). (c) Hence the Wilson weight is first order with
K(Y, Y') = prod_(m in S_(t+1)) w(X'_m; Y), w(X; Y) = prod_(mu < nu) f(U_mu^(-1) g_(mu nu) U_nu), a product over the
NEW sites for each fixed past. (d) The normaliser z(m; Y) := integral over G^D of w(X; Y) dX is the partition function
Z_D(g) of the principal chiral model on the complete graph K_D with background g. A change of variables
U_rho -> h_rho U_rho shows that it depends on g only through holonomies of cycles of K_D. The triangle (mu, nu, lambda)
holonomy is the zigzag hexagon through S_(t-1) and S_t around the equator of the 3-cube with top vertex m.
Proof. Read off the four vertices n, n + e_mu, n + e_nu, m at times tau, tau + 1, tau + 1, tau + 2. QED
Correction noted while writing: the two-sided conditional law of Y_t given Y_(t-1), Y_(t+1) is NOT a product, because
each plaquette with top vertex in S_(t+1) holds links of two different sites of S_t. Only the forward kernel K(Y, .)
is a product. This is the Domany-Kinzel shape (one child, its parents), with a three-site interaction.

**Lemma 2.4 (gauge forcing, PROVED).** The Jentzsch eigenfunction phi is invariant under (i) right multiplication of
all components of X_m by k_m, for each vertex m of its slice, and (ii) left multiplication of the components U(u, rho)
(in X_(u + e_rho)) by h_u, for each vertex u of the previous slice. If phi = prod_m e^(f_m(X_m)), each f_m is constant.
Proof. (ii): K(Y_t, Y_(t+1)) does not change when h_u acts on Y_t alone (it multiplies both lower links of each
plaquette on the left, and g_(mu nu) is unchanged); so K psi has the invariance for every psi, and phi = K phi/lambda.
(i): a gauge transformation at the vertices of S_t acts on Y_t (right) and on Y_(t+1) (left on components) and leaves
K unchanged; substitute Y' -> g Y' in K phi and use (ii) for phi on S_(t+1). Product form: (i) acts on X_m alone, so
f_m(X k) = f_m(X). Under (ii) one component of each of the D sites u + e_rho changes; these are independent variables,
so each f changes by a constant c_rho(h), and each c_rho is a continuous homomorphism G -> R, hence 0. Independent left
multiplications of the D components with one common right multiplication act transitively on G^D (take
h_rho = U_rho^(-1)). So f_m is constant. QED

**Proposition 2.5 (LC, PROVED).** On C_(D,L), L >= 2, beta > 0:
(i) D = 2: z(m; Y) = z_0 for all Y, phi = 1, and the vacuum chain is the PCA
P_*(Y, dY') = prod_m f(U_1^(-1) g_12 U_2) dX'_m / z_0. Each new plaquette has law f(V) dV/z_0, independent of the past.
(ii) D >= 3: the vacuum chain is not a PCA.
Proof. By Lemmas 2.1 and 2.4, P is a PCA iff phi is constant iff sum_(m in S_(t+1)) log z(m; Y) is constant in Y.
(i) K_2 has no cycle: substitute V = U_1^(-1) g_12 U_2. (ii) Take Y with all links 1 except one link
l = U(n_0, mu) = h. The link l is the mu-component of the site n_0 + e_mu, a parent of the D - 1 children
m_nu = n_0 + e_mu + e_nu (nu != mu). It enters z(m_nu; Y) only through the plaquette (mu, nu) at m_nu, where
g_(mu nu) = h^(+-1); all other g are 1 (L >= 2 keeps the base points m - e_kappa - e_lambda distinct, since a nonzero
vector with entries in {-1, 0, 1} is not in L Lambda_0). So sum_m log z = const + (D - 1) log zeta_D(h), with
zeta_D(h) := Z_D(g_12 = h, all other g = 1). By character orthogonality,
  integral zeta_D(h) chi_1(h) dh = b_1 integral 2 <U_1, U_2> prod_((mu,nu) != (1,2)) e^(beta <U_mu, U_nu>) dU.
Expand the exponentials: every term is a positive multiple of a moment integral prod <U_i, U_j>^(n_ij) dU, and each
such moment is >= 0 (expand the inner products in coordinates; a monomial moment on S^3 is >= 0). The term from the
path 1-3-2 is beta^2 integral 2 <U_1, U_2> <U_1, U_3> <U_3, U_2> dU = beta^2/8 > 0 (E[U U^T] = Id/4 on S^3, and
E <U_1, U_2>^2 = 1/4). So the chi_1-coefficient of zeta_D is at least b_1 beta^2/8 > 0, and zeta_D is not constant. QED
Smallest case, D = 3, by hand: one 3-cube below each vertex, and z(h) = (f * f * f)(h) = sum_n (n+1) b_n^3 chi_n(h), a
class function of the equator hexagon h. It is maximal at h = 1 and not constant for beta > 0. The same proof works
for U(1) (Fourier modes) and for finite groups with a non-trivial character in the weight: the obstruction is
group-blind.

### 2.4 The exact Feynman-Kac form, and the PCA representative

**Identity 2.6 (PROVED).** K(Y, Y') = Z(Y) P_*(Y, Y') with the site-factorised stochastic kernel
P_*(Y, dY') = prod_m w(X'_m; Y) dX'_m / z(m; Y) (a genuine PCA) and the potential Z(Y) = prod_m z(m; Y). On a torus
(Z/a) x (Z/b)^(D-1) with a | b the light-cone time tau mod a is defined (every link still goes from S_t to
S_(t+1)), and for a >= 3 the partition function is Tr((M_Z P_*)^a). This holds on the seed slab (a; (24a)^3).
**The PCA representative (the gauge disorder variety, PROVED as a definition).** The measure with weight
prod_p f(U_p) prod_m z(m; Y)^(-1) is the history of P_* (Lemma 2.1 with phi = 1). For D = 3 the extra factor is
prod over 3-cubes c of z(h_c)^(-1), a class function of the equator hexagon of each cube. This is the gauge analogue of
the Ising disorder line, where the PCA history carries the extra same-time coupling -(1/2) log cosh(2J) between the two
parents (direct check: log 2 cosh(J(s_1 + s_2)) = log 2 + ((1 + s_1 s_2)/2) log cosh 2J).

**Proposition 2.7 (the counterterm is the magnetic energy; exact in the Gaussian case, PROVED).** Non-compact U(1),
weight e^(-(beta/2) sum_p theta_p^2). At a vertex m let a in R^(edges of K_D) be the wedge fluxes and theta in R^D the
new links. Then sum over the plaquettes with top vertex m of theta_p^2 = ||a + delta theta||^2
= ||P_cyc a||^2 + ||P_cut a + delta theta||^2, with (delta theta)_(mu nu) = theta_nu - theta_mu and P_cyc, P_cut the
orthogonal projections on the cycle and cut spaces of K_D; and -log z(m; Y) = (beta/2) ||P_cyc a||^2 + const. So:
- the PCA representative has the action (beta/2) sum_m ||P_cut a_m + delta theta_m||^2 (the squared innovations), and
  the Wilson action exceeds it by exactly (beta/2) sum_m ||P_cyc a_m||^2;
- the cycle space of K_D is {F : sum_mu F_(mu nu) = 0 for every nu} = {F : i_v F = 0}, v = (1, ..., 1): the 2-forms
  with no component along the light-cone time. The cut space {x_nu - x_mu} = {v wedge x} is the electric part. For a
  constant field strength F one has P_cyc a = P_cyc F (a = F - delta theta). So the counterterm removes exactly the
  magnetic energy relative to the time direction v, and the PCA representative keeps only the electric energy.
Proof. Lemma 2.3 (a): each plaquette has one top vertex, and its flux is a_(mu nu) + theta_nu - theta_mu. Pythagoras,
since delta theta lies in the cut space; then the Gaussian integral over theta modulo constants. F is orthogonal to
all x_nu - x_mu iff sum_mu F_(mu nu) = 0 for every nu. QED
D = 3 explicitly (PROVED): with B(m) = (theta_23, theta_31, theta_12) of the three plaquettes with top vertex m and
n^ = (1, 1, 1)/3^(1/2), the PCA representative's action is EXACTLY (beta/2) sum_m |B(m)_perp|^2 (perp to n^), against
Wilson's (beta/2) sum_m |B(m)|^2. In Fourier, the lattice Bianchi identity reads sum_l (1 - e^(-i k_l)) B^_l(k) = 0, and
the least ratio |B_perp|^2/|B|^2 on that plane is |sum_l (1 - e^(-i k_l))|^2 / (3 sum_l |1 - e^(-i k_l)|^2), which is
|k|^2/12 + O(|k|^3) for k with sum k_l = 0. So for momenta transverse to the time diagonal one mode has stiffness of
order |k|^4 |A|^2 instead of |k|^2 |A|^2: the representative is an anisotropic, Lifshitz-type theory, not the photon.
SU(2) at weak coupling (ARGUED, Gaussian approximation): f is close to e^beta times the heat kernel at time 1/(2 beta),
so log z(h) = const - beta theta_h^2/6 + O(1), and the same split holds to leading order.

### 2.5 Verdict on framing (a), and the link to row 963

- (a) as stated: REFUTED for D >= 3 along the axis (Proposition 2.2) and the light-cone diagonal with vertex sites
  (Proposition 2.5); true only for D = 2. The obstruction is one function, the normaliser z, which is the magnetic
  free energy of the past seen from the new vertex.
- What survives (PROVED, Identity 2.6 and Reading 2.2): in BOTH directions the Wilson transfer operator is
  M_(potential) x (PCA), with the PCA carrying only electric (kinetic) energy and the potential carrying the magnetic
  energy. The light-cone frame moves the split; it does not remove the potential.
- The PCA representative is a different measure. Proposition 2.7 shows that at weak coupling it lacks the magnetic
  term, so no comparison node to the account's measure can exist for it. Row 962's finding applies: REFRAMING, no
  NEW INPUT.
- Link to row 963 (not attacked; row 963 owns reflection positivity across diagonal hyperplanes). The light-cone
  kernel K is not symmetric (parents and children play different roles), and the hyperplane reflection along
  v = (1,1,1,1) is not a symmetry of Z^4 (it maps e_1 to e_1 - v/2). The point reflection n -> -n gives only a
  symmetric kernel K R with R an involution, and no positivity (ARGUED). So Theorem S's engine, which needs a positive
  trace-class transfer operator in each direction, does not apply to the light-cone operator, although
  Z(a; (24a)^3) = Tr((M_Z P_*)^a) holds.
- Fact tests. Every statement here is group-blind (U(1), Z_2, Q_8, 2T, SU(2) alike), so the PCA part cannot pass
  FT-U1 or FT-FROZEN by itself: whatever separates SU(2) must sit in the potential Z.

### 2.6 Not proved here

- Sites larger than one vertex (blocks holding zigzag loops): Lemma 2.4 no longer forces phi constant. OPEN; ARGUED
  false at small beta, because the future partition function couples distant boundary blocks at finite order of the
  character expansion.
- Linear times c . n with all c_mu != 0 other than the body diagonal: the same K_D normaliser appears, but the chain
  has memory max c_mu. ARGUED, same conclusion.
- Single-link staggered orders: ARGUED impossible. Each plaquette needs a unique latest link, and a link that closes
  two plaquettes has a normaliser that depends on a six-link loop. D = 4 has 6 plaquettes and 4 links per vertex. In
  D = 3 a bijection would make all plaquettes independent, against the Bianchi identity.

## 3. Literature, checked by URL (Step 3)

Fetched into `/tmp/pca967/lit_*` (one empty folder per source; text read with PyMuPDF under `python3 -I`; nothing
committed). READ = the passages named were read; RECALLED = not opened.

| Source | Status | What it gives | Bearing |
|---|---|---|---|
| C. Maes, "Nonequilibrium physics aspects of probabilistic cellular automata", arXiv:1605.02876, pp. 2-4 | READ | Sites updated independently given the past; the formal (d+1)-dimensional Hamiltonian is H(sigma) = - sum_(i,n) log p_i(sigma_n(i) \| sigma_(n-1)) (citing Goldstein-Kuik-Lebowitz-Maes, CMP 125 (1989) 71-79, and Georges-Le Doussal, JSP 54 (1989) 1011-1064). A stationary +-1 PCA is time-reversible when h_i(eta) = tanh[lambda_i + sum_j J_ij eta_j] with J symmetric; then nu(eta) = C exp sum_i {lambda_i eta_i + log 2 cosh[lambda_i + sum_j J_ij eta_j]}, at least three-body. "PCA ... cannot produce any given Gibbs distribution as stationary"; "the standard Ising model cannot be obtained"; the alternative is bipartite lattices with alternate updating (Domany-Kinzel, PRL 53 (1984) 311) | Confirms the shape used in Section 2: the term -log(normaliser) is exactly what a PCA history adds to the action; for Ising it is log 2 cosh, for the gauge field it is log z(m; Y) |
| P.-Y. Louis, "Ergodicity of PCA: equivalence between spatial and temporal mixing conditions", ECP 9 (2004) 119-131, arXiv:1604.07707, abstract and Sections 1-3 | READ | Spin space S FINITE and totally ordered; for ATTRACTIVE PCA, exponential ergodicity in the uniform norm is equivalent to (A), exponential decay of boundary influence for the invariant measures on finite boxes. For reversible PCA on {-1, +1}^(Z^d) with Gibbs potential phi, the spatial weak mixing (WM) of phi gives (A). The constructive criteria are Dobrushin-Vasershtein and its space-time generalisation by Maes-Shlosman (CMP 135 (1991) 233-251) | For a PCA, time mixing is equivalent to SPATIAL mixing of its own Gibbs measure. So a PCA ergodicity theorem for a gauge PCA would be a spatial mixing (gap-type) statement in disguise. The hypotheses (finite ordered spins, attractiveness) fail for SU(2) links: no order, no FKG for non-abelian gauge fields |
| P. Arrighi, G. Di Molfetta, N. Eon, "Gauge-invariance in cellular automata", arXiv:2004.03656 (supersedes arXiv:1802.07644 and 1908.01229) | READ (abstract, Sections 1-2) | Gauge invariance and a gauging procedure for deterministic and quantum CA; "totally devoid of least action principle, or Lagrangian" | No Gibbs measure, no Wilson weight, no mixing statement. Not an input |
| Goldstein-Kuik-Lebowitz-Maes 1989; Lebowitz-Maes-Speer, JSP 59 (1990) 117-170; Georges-Le Doussal 1989; Domany-Kinzel 1984; Rujan, JSP 49 (1987) | RECALLED (Project Euclid and Rutgers links returned stubs or 404; APS and Springer paywalled; stopped there) | The PCA <-> (d+1)-Gibbs correspondence and the disorder-line equivalence, as quoted by Maes 2016 | Section 2 uses only the quoted form, re-derived there (Lemma 2.1 and the log 2 cosh check) |
| Maes-Shlosman 1991; Toom 1980 (eroders); Gacs 2001 (positive-rate non-ergodic 1D PCA); van den Berg-Maes 1994 | RECALLED here; the last is READ in the lane (row 821) | Constructive finite space-time criteria; stability of eroders under noise; non-ergodicity with positive rates | Step 4 states only what follows from their hypotheses, which are finite-spin |

**What the reading changes.** Nothing in Section 2. It adds one structural fact (READ, Louis 2004): for a PCA, temporal
ergodicity and spatial mixing of its stationary Gibbs measure are equivalent (attractive, finite-spin case). So even a
genuine PCA representation would turn the crux into the same spatial-mixing statement, now for the slice law.

