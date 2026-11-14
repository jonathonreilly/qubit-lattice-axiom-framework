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

## 4. Framing (b): which PCA ergodicity tools survive (Step 4)

**Answer.** None gives a NEW INPUT. After Section 2, a PCA tool can act only on the PCA part (P_0 in axis time, P_* in
light-cone time), never on the Wilson chain itself, which is M_Z P_* and not a PCA. The PCA part is the electric
(kinetic) theory. It mixes for every compact group, compact U(1) included, so it cannot carry the U(1)/SU(2)
separation. All the difficulty sits in the potential, which the tools do not see.

### 4.1 The tools, one by one

| Tool (PCA form) | Hypothesis | What it would give here | Supremum or averaged | Verdict |
|---|---|---|---|---|
| Dobrushin-Vasershtein: sup_k sum_j sup over parents differing at j of the TV distance of the child laws < 1 | uniform over all parent configurations | ergodicity of P_* (or P_0), at small beta only: for SU(2) the child law at beta 2.3 moves by O(1) when one parent site moves, so each term is near 1 and the sum is near D (the single-link GUIDE of row 820 gives row sums 3.4-3.6 at beta 2.3-2.5 for the related link chord influence) | supremum | capped; FT-CEIL (single-site 2/3) applies in its PCA form |
| Maes-Shlosman 1991 (finite space-time volumes) | uniform over boundary conditions; finite spins | the same object, with a better constant | supremum | capped; finite-spin |
| Synchronous coupling, coupling from the past (Doeblin form) | each child density >= epsilon x reference, uniformly in parents | for P_*: epsilon >= e^(-2 beta C(D,2)) = e^(-12 beta) at D = 4, about 1e-12 at beta 2.3; forgetting events are far below any oriented percolation threshold | supremum | dead at beta 2.3 |
| Disagreement percolation (van den Berg-Maes), PCA form | per-site disagreement probability below the threshold of ORIENTED percolation | the one gain of the PCA frame: disagreements propagate only forward, so the oriented threshold replaces the unoriented one. But the per-site disagreement probability is a supremum over parent pairs and is near 1 at beta 2.3 (row 820) | supremum | capped; gain is a constant factor in the threshold only |
| Wasserstein / coarse-Ricci contraction (Dobrushin with a metric) | contraction for all pairs of parent states | linearised P_* transports the magnetic part P_cyc a unchanged (Proposition 2.7: the new plaquette fluxes are P_cyc a_m plus electric noise), so the contraction constant along magnetic directions is 1 at weak coupling, for U(1) and SU(2) alike | supremum | fails at the linear level, group-blind |
| Annealed criteria for random environments (Gielis-Maes 1995; Gielis-Maes-van de Velde 1999, READ in row 853) | environment i.i.d. and independent of the process | the "environment" here is the process's own past | averaged | not applicable (row 821) |
| Spatial weak mixing <-> time ergodicity (Louis 2004, READ in Section 3) | finite ordered spins, attractive PCA | turns time mixing into spatial mixing of the stationary law | uniform | circular: it is the gap statement again |

Where an averaged version exists, it needs independent disorder (Gielis-Maes) or is the gap statement itself (Louis).
The lane's averaged forms ((LSI-J-seed), row 947) are not supplied by any PCA theorem known to me or to rows 821, 853.

### 4.2 Why the PCA part cannot carry the separation (ARGUED from PROVED identities, plus hand arithmetic)

- The PCA parts are explicit. Axis: P_0 = independent heat-bath walks on each link, spectral gap 1 - b_1/b_0 =
  1 - I_2(beta)/I_1(beta) on spin-1/2 functions (convolution by f/b_0 has eigenvalue b_n/b_0 on spin n/2). This is
  0.52 at beta 2.3 and 0.48 at 2.6 (hand arithmetic from four series terms: I_1(2.3) = 2.098, I_2(2.3) = 1.005). The
  same kind of number holds for compact U(1) (1 - I_1/I_0). Light-cone: P_* is the electric-only theory
  (Proposition 2.7). Neither has a phase transition in beta that distinguishes U(1) from SU(2).
- FT-U1 kills every route that uses only the PCA part (ARGUED): compact U(1) at large beta has a mixing PCA part of the
  same order and no seed. So an implication "mixing of P_* gives the seed" must be false, or must use the potential
  in a U(1)-sensitive way, at a named step.
- SMALL-BOX kills it too (ARGUED): P_*-based bounds are local, in lattice units, and do not see the box size; but a small
  box at large beta has a gap small in units of its side.
- Size of the potential (hand arithmetic, GUIDE weight). D = 3, beta 2.3: z(h) = sum_n (n+1) b_n^3 chi_n(h) gives
  z(1) = 9.00 and z(-1) = 3.64, so log z varies by 0.91 per vertex; at beta 2.6 by 1.18. The axis potential varies by
  2 beta = 4.6 per spatial plaquette. The light-cone potential is smoother, but it is extensive and of order one per
  vertex, so no perturbation around the PCA reaches beta 2.3. At small beta it is O(beta^3) per vertex (the first
  g-dependent term of z is (beta/2)^3 tr(h)/4), which reproduces the known strong-coupling range only.

### 4.3 Toom, Gacs and the frozen groups

- What they prove: positive-rate PCA can be non-ergodic (Toom's eroders are stable under small noise; Gacs builds a
  one-dimensional example). In the PCA frame the frozen-group failure is a non-ergodicity of M_Z P_*, not of P_*: for
  a finite group, P_* on a finite cylinder has a strictly positive kernel on a finite state space and mixes; the
  potential pins the magnetic flux to flat connections at large beta, and the flat sectors are separated by vortex
  sheets whose cost grows with their area.
- A Toom-type space-time contour argument for that stability is the standard Peierls argument for finite-group gauge
  theories at large beta. It explains WHY the seed fails for Q_8 and 2T (FT-FROZEN), as the lane already records; it
  gives no input for SU(2), where flux is not quantised in the link variables and thin vortices can be thickened.
  REFRAMING; a fact-test explanation, not a tool.

### 4.4 Verdict on framing (b)

REFRAMING. The supremum tools are capped as before (FT-CEIL), now in their PCA form; the averaged tools need
independent disorder; time mixing of a PCA is spatial mixing of its law (Louis 2004), so nothing is gained even in
principle. The one structural gain (oriented instead of unoriented percolation thresholds) is a constant factor in a
threshold that a near-one disagreement probability does not meet. New, as a filter for later ideas (proposed for the
fact-test list, ARGUED): **FT-FK** - an argument that acts only on the PCA (kinetic) part of a Feynman-Kac
representation fails FT-U1 and SMALL-BOX; it must use the magnetic potential, at a named step, in a way U(1) fails.

## 5. Framing (c): plaquette-level constraint systems (Step 5)

**Answer.** REFRAMING throughout. Bianchi and Batrouni-Halpern are KNOWN dead in the magnetic metric (row A12); in
light-cone time they become causal, and then they are exactly the PCA part of Section 2. Centre vortices are the
flux half, KNOWN in the lane. Reversible energy-conserving rules preserve the Wilson measure at every beta at once, so
they carry no beta-dependent inequality.

### 5.1 Bianchi on cubes, Batrouni-Halpern, and the obstruction count

- KNOWN (`gap-skeleton-max-b.md` A12, L215-220): in plaquette variables the Wilson measure is a product of plaquette
  weights restricted to the Bianchi variety, with a Jacobian. A Poincare inequality in the plaquette (magnetic)
  metric holds for U(1) with constant beta while the photon is massless, so that metric is the wrong one. One 3-cube's
  partition function has zeros in the right half-plane (L581-584), so no Lee-Yang route.
- NEW here, a reading of Section 2 (PROVED there): in light-cone time each cube's Bianchi identity ties its three top
  faces (new, at the top vertex m) to its three bottom faces (old). So the Bianchi system is solved forward, vertex by
  vertex: at m, D(D-1)/2 new plaquettes satisfy C(D,3) cube constraints of rank (D-1)(D-2)/2 (the cycle rank of K_D),
  leaving D - 1 free plaquette degrees of freedom per vertex, which matches D links minus one gauge degree. This is
  the causal Batrouni-Halpern system, and it is the PCA P_*.
- The obstruction count (PROVED, from Proposition 2.7): the normaliser depends on the past through the cycle space of
  K_D, of dimension C(D-1, 2). That is exactly the number of magnetic components of F relative to the time direction.
  So the Wilson measure is a PCA history iff there is no magnetic component, iff D = 2. The plaquette CA fails for
  the same reason the field has magnetic energy.
- Non-abelian locality (ARGUED): for SU(2) each cube constraint involves parallel transport by link variables, so a
  CA on plaquette variables alone is not local; it must carry the links (a local frame). The abelian plaquette CA is
  local. Nothing here separates SU(2) from U(1).

### 5.2 Centre vortices as Z_2 plaquette surfaces

- KNOWN in the lane: the flux half Q_0 of the split seed is a twist-sector (vortex free energy) statement; the
  order-one vortex free-energy area law ((14) of the brainstorm notes) is 't Hooft-Tomboulis-Yaffe confinement and is
  not supplied by any known method; Tomboulis 2007 was diagnosed in rows 797/799 (Ito-Seiler's critique); see
  `gap-brainstorm-max.md`, `gap-crux-exercise-r858-max.md`, `gap-flux-exercise.md`.
- The PCA frame adds one reading (ARGUED): sigma_p = sign tr U_p is transported forward by P_*, and the Z_2 Bianchi
  closure fails exactly at SO(3) monopoles (the product of sigma over a cube's faces is the cube's monopole charge).
  The twist sectors are topological invariants of the torus configuration, conserved by any local rule; their
  relative weights are set by the potential. No new input.

### 5.3 Reversible energy-conserving rules (Creutz demons, overrelaxation, Q2R)

**Lemma 5.1 (a deterministic reversible gauge CA, PROVED).** For a link l with staple quaternion S != 0 put
V = S/|S| and R_l(U_l) = 2 <U_l, V> V - U_l (for S = 0, R_l = id). R_l is an isometry of S^3 (a reflection through the
line R V), so it preserves Haar measure and <U_l, S>, hence the Wilson action given the other links. The links
{(n, mu) : sum over nu != mu of n_nu even} share no plaquette (two links (n, mu), (n', mu) lie in one plaquette only
if n' - n = +-e_nu, nu != mu, which changes that parity). So on a torus with even sides the 2D sublattice updates are
parallel products of commuting reflections, and their composition Phi is an invertible, Haar-preserving map with
S_W o Phi = S_W.
Consequence (PROVED): Phi preserves g(S_W) dU for every g, hence the Wilson measure at every beta at once. For Z_2 the
same construction flips a link iff its staple sum is 0: the exact gauge analogue of Q2R (Vichniac; Pomeau, recalled).
- Why it is not an input (ARGUED): Phi carries no beta, so it cannot produce a beta-dependent bound. A deterministic
  measure-preserving map has a unitary Koopman operator, with no spectral gap to transfer; its orbits stay on level
  sets of S_W and of any further invariant. Creutz's demons (PRL 50 (1983) 1411, recalled) only extend the measure by
  demon variables whose marginal is canonical. Overrelaxation (Adler 1981; Creutz 1987; Brown-Woch 1987, recalled)
  speeds samplers; the Poincare or log-Sobolev constant of the measure for a fixed Dirichlet form does not change
  when measure-preserving moves are added to a sampler. (LSI-J-seed) is a statement about the measure and its gradient
  form, so these rules do not touch it.
- Fact tests: group-blind (U(1), Z_2, SU(2) alike); FT-U1 fails as for every rule that does not use the potential.

### 5.4 Verdict on framing (c)

REFRAMING or KNOWN. The one exact new fact is the count in 5.1: the PCA obstruction is the magnetic field itself
(cycle rank of K_D = C(D-1, 2) magnetic components). Lemma 5.1 is a correct but idle construction.

## 6. GUIDE run: bookkeeping check of the exact identities (Step 6; a run can refute, it proves nothing)

Script `/tmp/pca967/scripts/guide6.py` (scratch, not in the repository), run under `lab_ops.py numeric-lock`, nice,
BLAS threads 1, self-stop above 2 GB. Criteria written before the run:
- A1. Z_2 gauge theory, D = 3, torus (Z/2)^3 (24 links, 24 plaquettes). Brute-force Z(beta) over 2^24
  configurations must equal Tr(K_01 K_10) built from the light-cone kernels of Lemma 2.3 (every plaquette assigned to
  its top vertex), to relative error below 1e-10 at beta 0.3 and 0.7. FAIL = a bookkeeping error in Lemma 2.3 or
  Identity 2.6.
- A2. Lemma 2.3(a) structure check on that torus: each plaquette has exactly two links into its top vertex and two
  links in the previous slice.
- A3. Row sums of K_01 (the normaliser Z(Y) of Identity 2.6) must take only values z+^j z-^(4-j) with the Z_2 hexagon
  normalisers z+ = 2(e^(3 beta) + 3 e^(-beta)), z- = 2(3 e^beta + e^(-3 beta)), and must not be constant (Proposition
  2.5 (ii) in its Z_2 form). On a side-2 torus the parents of different vertices overlap, so only the value set is
  tested, not the count of each value.
- A4. The Perron vector of K_01 K_10 must be non-constant, and its logarithm on slice 1 must not be a sum of site
  functions (residual of the best fit by site functions clearly above rounding). This is the GUIDE form of "the
  vacuum chain is not a PCA".
- B1. Proposition 2.7: min over theta of ||a + delta theta||^2 = ||P_cyc a||^2 to 1e-10 for random a (D = 3, 4); the
  cycle space has dimension C(D-1, 2) and equals ker i_v.
- B2. D = 3: ||P_cut F||^2 = |B|^2 - (B . 1)^2/3 with B = (F_12, -F_02, F_01); the soft-mode formula
  |sum (1 - e^(-i k_l))|^2/(3 sum |1 - e^(-i k_l)|^2) equals the least eigenvalue computed numerically; it is close to
  |k|^2/12 for small k with sum k_l = 0.
- B3. The Ising disorder-line identity of 2.4 holds to rounding.

Status: job started in the background at 13:49Z (date -u); another lane held the lock (row 965, "seconds"), so it retried
after 60 s. Lock acquired 13:50:45Z with 73 percent memory free; job ended 13:50:49Z; peak RSS 0.84 GB.
Process slip, recorded: the release in the script's exit trap ran from /tmp and failed ("can't open file
scripts/lab_ops.py"); I released the lock by hand from the repository root at 13:51:00Z, 11 s after the job ended.

**Results (GUIDE; all criteria met; nothing here is a step of a proof).**

| Check | Result |
|---|---|
| A1 brute force vs light-cone trace | beta 0.3: Z = 5.1282529536e7 both ways, relative difference 6.0e-14; beta 0.7: Z = 2.4908746390e10 both ways, 4.3e-15. PASS |
| A2 Lemma 2.3(a) structure | every plaquette: two links into its top vertex, two in the previous slice. PASS |
| A3 normaliser values | row sums of K_01 take 3 values, all of the form z+^j z-^(4-j); max/min 1.219 (beta 0.3) and 6.023 (beta 0.7), so not constant. PASS |
| A4 not a PCA (GUIDE form) | Perron vector max/min 1.224 (beta 0.3) and 11.58 (beta 0.7); log phi minus its best fit by site functions has max residual 0.10 of a range 0.20 (beta 0.3) and 1.38 of 2.45 (beta 0.7). PASS |
| B1 Proposition 2.7 | min over theta of norm squared minus norm of P_cyc a squared: at most 3.6e-15 (D = 3, 4); cycle space dimension 1 and 3 = C(D-1, 2); equals ker i_v. PASS |
| B2 D = 3 forms | P_cut identity to 1.8e-15; soft-mode formula equals the numerical least eigenvalue to 1.1e-15 at 200 random k; at k = s(1, -1, 0), s = 0.2, 0.1, 0.05: ratio 6.644e-3, 1.665e-3, 4.166e-4 against s^2/6 = 6.667e-3, 1.667e-3, 4.167e-4 (that is, abs(k)^2/12). PASS |
| B3 Ising disorder-line identity | exact to rounding. PASS |

What the run can and cannot establish: it found no bookkeeping error in Lemma 2.3, Identity 2.6 or Proposition 2.7 on
the smallest torus, and it shows the Z_2 analogue of Proposition 2.5 (ii) on that torus. It says nothing about D = 4,
SU(2), or any box size; those statements rest on the hand proofs of Section 2 only.

## 7. Ranked list: what, if anything, deserves a proof lane (Step 7)

Plain answer to the owner's question. A "cellular automaton with plaquettes" exists exactly: in light-cone time the
Bianchi identities are solved forward, vertex by vertex, and this is a genuine PCA (P_*). But it is only the electric
part of Yang-Mills. The Wilson measure is that PCA weighted by the magnetic energy (Identity 2.6, Proposition 2.7),
and in four dimensions no time direction and no vertex grouping removes the weight (Propositions 2.2, 2.5). The mass
gap lives in the weight. So the CA view moves the hard part; it does not remove it.

No item below moves an item of the (SEED-FP) chain. By rule 0 ("Is it worth doing?") the lead may rightly launch none.

1. **FT-FK as a fact test (no lane; one line in the lane's fact-test list).** Statement: an argument that acts only on
   the kinetic (PCA) part of a Feynman-Kac representation of the transfer operator (P_0 in axis time, P_* in
   light-cone time; Doeblin, coupling, coupling from the past, disagreement percolation, Dobrushin-Vasershtein,
   Wasserstein contraction of the free part) fails FT-U1 and SMALL-BOX; it must use the magnetic potential, at a named
   step, in a way that compact U(1) fails. Moves: saves later brainstorm lanes (rule 0, waste avoided). Cost: none.
2. **Optional: one cross-provider check of Lemma 2.4, Propositions 2.2, 2.5, 2.7 and Lemma 5.1** (about 2 pages), only
   if the lead wants to record "the Wilson measure is not a PCA history in D >= 3" as a checked negative result, for
   instance in an answer to the owner. REFRAMING for the seed. First step: redo Lemma 2.4's transitivity argument and
   the chi_1-coefficient positivity in Proposition 2.5. Fact test: the statements are group-blind by design. Moves:
   nothing on the chain. Chance the check passes: about 85 percent (ARGUED; the arguments are short).
3. **Not worth a lane, with the reason.** (a) A small-beta gap from the light-cone potential of size O(beta^3): known
   range only (strong coupling). (b) Block-site PCA (Section 2.6): ARGUED false at small beta; even if true, the
   magnetic content would move into the block eigenfunction. (c) The PCA representative as a model: it lacks the
   magnetic term (Proposition 2.7), so it has no node to the account. (d) Toom/Gacs for the frozen groups: the
   standard Peierls argument for finite groups; explains FT-FROZEN, gives nothing for SU(2). (e) Reversible gauge CA
   (Lemma 5.1): measure-preserving at every beta, no inequality. (f) Centre vortices: the flux half, KNOWN (rows
   797/799 and the vortex free-energy notes).

## 8. Result (Step 8)

Steps done: 1-8 of the plan, in order; each was appended before the next. Wall clock 13:20Z-13:55Z.

| Statement | Label |
|---|---|
| Lemma 2.1 (a first-order chain with a product forward kernel is a PCA iff its Perron vector is a product of site functions) | PROVED |
| Proposition 2.2: the axis-time vacuum slice chain of row 941 is not a PCA (D >= 3, beta > 0); its kernel is (independent link walks) x e^(-V) | PROVED |
| Lemma 2.3: light-cone structure (unique top vertex, forward kernel a product over new vertex sites, normaliser = principal chiral model on K_D, triangle holonomy = equator hexagon) | PROVED; GUIDE bookkeeping check passed (Section 6) |
| Lemma 2.4: gauge invariance forces a product Perron vector on vertex sites to be constant | PROVED |
| Proposition 2.5: the light-cone vacuum chain is a PCA iff D = 2 (or beta = 0); for D >= 3 the chi_1-coefficient of the one-edge normaliser is >= b_1 beta^2/8 > 0 | PROVED (group-blind) |
| Identity 2.6: K = M_Z P_* (genuine PCA times a potential), Z = Tr((M_Z P_*)^a) on tori (Z/a) x (Z/b)^(D-1), a \| b, a >= 3, including the seed slab | PROVED |
| Proposition 2.7: the PCA counterterm is exactly the magnetic energy relative to the light-cone time (Gaussian case); cycle space of K_D = ker i_v, dimension C(D-1, 2); D = 3 representative action (beta/2) sum abs(B_perp)^2 with a soft mode of relative stiffness abs(k)^2/12 | PROVED (Gaussian); SU(2) weak-coupling form ARGUED |
| Two-sided conditionals in light-cone time are a product | FALSE (corrected in 2.3) |
| Block sites, other diagonal times, single-link staggered orders | ARGUED (no PCA); OPEN for blocks |
| No hyperplane reflection reverses light-cone time in D = 4; the light-cone transfer operator gets no positivity from reflection positivity | PROVED for the first part; ARGUED for the second (row 963 owns diagonal reflection positivity) |
| PCA tools (Dobrushin-Vasershtein, Maes-Shlosman, coupling and CFTP, oriented disagreement percolation, Wasserstein contraction, annealed criteria) give no input at beta 2.3-2.6 | ARGUED from the PROVED identities, READ sources and the lane's GUIDE (row 820) |
| FT-FK (proposed fact test): an argument acting only on the kinetic part of a Feynman-Kac representation fails FT-U1 and SMALL-BOX | ARGUED |
| Toom/Gacs: explain FT-FROZEN through the finite-group Peierls argument; no SU(2) input | ARGUED; KNOWN physics |
| Lemma 5.1: a deterministic reversible gauge CA (parallel overrelaxation; Q2R for Z_2) preserves the Wilson measure at every beta | PROVED; not an input |
| Light-cone normaliser at beta 2.3 / 2.6 (D = 3): log z varies by 0.91 / 1.18 per vertex; axis potential by 2 beta per plaquette | hand arithmetic (four series terms), GUIDE weight |
| (LSI-J-seed), (SEED-FP), (UNIV-K), (VAC-SUB) | OPEN, unchanged; not attacked (owned by their rows) |

**Limits.** One author; no check by another model. D = 4 and SU(2) statements rest on the hand proofs only; the
GUIDE run covers only Z_2 on (Z/2)^3 and linear algebra. GKLM 1989, Lebowitz-Maes-Speer 1990, Georges-Le Doussal 1989,
Domany-Kinzel 1984, Maes-Shlosman 1991, Toom, Gacs, Batrouni-Halpern, Creutz, Adler, Brown-Woch, Vichniac and Pomeau
were not opened here (paywall, stub or 404, or not needed); what is attributed to them is as quoted by Maes 2016 or
recalled, and no step of Section 2 uses them. Row 963's diagonal reflection positivity question was not attacked. No
cross-branch search was run (this clone holds only `claude/ym4d-hard-route`). Nothing here is a seed, a mass gap or a
public claim.

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the account that
fixes the measure (isotropic Wilson SU(2), periodic tori) and for the transfer frame used through rows 931 and 941.
Rows 820, 821, 853 (Dobrushin and disagreement percolation numbers and readings), row A12 of `gap-skeleton-max-b.md`
(plaquette variables), rows 797/799 (Tomboulis), 941 (slice chain), 947 (Theorem BR, (LSI-J-seed)), 962 (constraint
audit). Literature: Goldstein, Kuik, Lebowitz and Maes; Lebowitz, Maes and Speer; Georges and Le Doussal; Domany and
Kinzel; Rujan; C. Maes (arXiv:1605.02876, read); P.-Y. Louis (arXiv:1604.07707, read); Arrighi, Di Molfetta and Eon
(arXiv:2004.03656, read); Maes and Shlosman; Dobrushin and Vasershtein; Toom; Gacs; van den Berg and Maes; Gielis,
Maes and van de Velde; Batrouni and Halpern; Creutz; Adler; Brown and Woch; Vichniac; Pomeau.

RESULT: Row 967 (Claude Opus 5.5 max, author, unchecked). Framing (a) REFUTED for D >= 3, PROVED by hand: the Wilson measure is not the space-time history of a site-factorised PCA along the axis time (Proposition 2.2) or along the light-cone (Domany-Kinzel) time with vertex sites (Proposition 2.5); the obstruction is one normaliser, the principal chiral model on K_D, a non-constant class function of the equator hexagons of the 3-cubes below each vertex; it is a PCA only for D = 2 (independent plaquettes). PROVED instead: in both directions the Wilson transfer operator is exactly (electric PCA) x (magnetic potential) (Identity 2.6), and the counterterm that would make it a PCA is exactly the magnetic energy relative to the time direction (Proposition 2.7: cycle space of K_D = ker i_v, dimension C(D-1, 2)); the PCA representative ("gauge disorder variety") drops the magnetic term (D = 3 Gaussian: (beta/2) sum |B_perp|^2, Lifshitz-type soft mode |k|^2/12), so it has no node to the account. Framing (b) REFRAMING: every PCA ergodicity tool acts only on the electric PCA part, which mixes for compact U(1) too; the supremum tools are capped (Doeblin constant e^(-12 beta), about 1e-12 at beta 2.3; oriented disagreement percolation gains only a threshold constant), the averaged ones need independent disorder, and PCA time mixing is spatial mixing (Louis 2004); Toom/Gacs explain FT-FROZEN only. Framing (c) REFRAMING or KNOWN: Bianchi/Batrouni-Halpern solved forward in light-cone time is the PCA part; centre vortices are the flux half; a reversible gauge CA (Lemma 5.1, parallel overrelaxation, Q2R for Z_2) preserves the Wilson measure at every beta and gives no inequality. GUIDE: brute-force check on Z_2 (Z/2)^3 and of the Proposition 2.7 algebra, all passed. Ranked: 1. adopt FT-FK as a fact test (no lane); 2. optional cross-provider check of Section 2; nothing else deserves a lane. NO NEW INPUT for the crux; (LSI-J-seed), (SEED-FP), block-site PCA (ARGUED false at small beta) stay OPEN.
