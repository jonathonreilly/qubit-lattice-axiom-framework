lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T18:38Z

# Row 1358, gap-mini-dualstep-fable: the step into the dual end class

Started 2026-11-21T06:38Z (date -u) at commit 6c42642f5 on branch claude/ym4d-hard-route. Research-stage working state. It grants no status, and nothing here is a public claim.

Labels: PROVED, ARGUED, GUIDE, OPEN, as the queue row asks.

## Step 0. Orientation (written 2026-11-21T06:51Z, date -u)

Read, statements only unless a proof is named:

- `GOAL.md` (whole); `FINISH.md` L1-84, L299-360, and the rows 1326, 1331, 1332, 1335, 1340-1358.
- `parts/gap.md` L1-104 and L213-322 (state of attack, route registry, test table, the exact price).
- `library/gap-mini-nphys-fable.md` (row 1354, whole; an earlier row of this worker).
- `library/gap-blockstep2-astra62.md` (row 1345, whole): the centre-sign block map (1)-(3), the bounds (4)-(10),
  the end class (11)-(12), the failure (14).
- `library/gap-blockstep4-astra62.md` (row 1351) L1-150: the neutral end class (10)-(11) and its proof.
- `library/gap-shrink-box-fable.md` (row 1332) Sections 1 and 6: Proposition CH.
- This worker's notes on the route-screening tables (rows 1189, 1194, 1199, 1200, 1237, 1241, 1273), on the
  prior-identity list and on row 1354.

The item, as the queue row states it: carry the Wilson trajectory, uniformly in the cutoff and through
mass-preserving block steps, from a coupling above the hand range into an end class with a strict margin that a
confining theory can reach. Row 1354 proposed the class (10*) of its Theorem E.

Not on disk at this pin: the outputs of rows 1356 and 1357 (running). The checks 1352 and 1355 are read in their
RESULT lines only.

**Repo search.** This checkout has the branch claude/ym4d-hard-route only; origin/main and the open PR
branches are not refs here, so the search is this folder. Searched with `grep -l -i` over `library/*.md` and
`parts/*.md`, then read at the hits named in each step: "sheet" (270 files), "monopole" (51), "Mack" (84),
"Tomboulis" (85), "Chatterjee" (87), "'t Hooft loop" or "disorder operator" (15), "polymer" (197),
"Kotecky" (38), "decimat" (54), "Simon-Yaffe" or "Doeblin" (about 40 lines), "perimeter law" (27),
"exactly one link" and "plaquette cover" (Lemma LF of `gap-seed23-opus.md`, used by row 1341), "0.3609" and
"1.0109" (the hand ceilings, rows 836 and 839). Four objects that I was about to rebuild were found on file
and are cited, not rebuilt: the end class for block links (Theorem END-D, row 1353), the plaquette cover and
its exact integration (row 1341), the near-Haar law of straight transports (row 1145), and the single-link
Doeblin bound (rows 859 and 1248).

## Step 1. How best to attack it (written 2026-11-21T07:03Z, date -u)

Also read for this step: `library/gap-mini-neutral-step-fable.md` (row 1353) Sections 2, 3, 5 and 6; the RESULT
line of its check (row 1355).

**1.1 What is on file for each leg (READ; rule 0a).**

- End classes. Coherent centre weights with a product reference: row 1345 (11)-(12) (periodic mass), row 1351
  (10)-(11) and (23)-(24) (neutral mass; an alternative-II class by row 1354). The Fourier-dual class (10*): row
  1354 Theorem E. Block links with a nearly Haar law and windows of any range: row 1353 Theorem END-D. END-D
  gives the two-period bound for each of the eight twisted masses, so it is an alternative-I class, and it is
  the natural home of (10*): a plaquette weight with a small odd part and a nearly constant even part is one
  window. Dobrushin ends: row 785 Theorem DOB, row 1340 Lemma END-RAY.
- Exact maps. The 2^4 cube map (row 1341), the centre-sign map (row 1345), the gluing and the strip elimination
  (row 1351), noise steps with pins (rows 861, 1340). Row 1353 2.2: Proposition CH is vacuous without maps that
  are local and explicit; row 1353 2.3: no class is carried by any map on file.
- The step. Open in every row. Row 1354 6.1 states it as (BS*). The single-link Doeblin bound (Simon and
  Yaffe) gives a perimeter law at every coupling and for every compact group; it is not selective
  (row 1248, `gap-mini-solve-ab-opus.md` L52; row 859, `gap-brainstorm-max.md` L312).

**1.2 The plan.** The queue row names a target class, (10*). Before any step is attacked, one question decides
which map can have that target: what are the electric sheet weights of the Wilson image under the maps on file?
Row 1354 left this open. Its 4.4 said that the sheets "can be rare only after the angular environment is
integrated, by cancellation of the signs", and its 6.2 item 1 read the cost of a coarse centre monopole as a
thick-monopole free energy of order beta. Step 2 answers the question with a proof. The answer changes the
target, so it comes first.

After that the plan is: (Step 3) say which coarse variable has rare sheets and what the step then is, as one
statement in the law of the fine model; (Step 4 on) attack that statement.

**1.3 What I do not expect (GUIDE).** A proof of the step at a coupling of order one. Every row since 998 ends
at the same place, and the tools on file that reach order one are blind to the group. I state this before the
work so that the labels below are read against it.

## Step 2. The centre-sign maps on file cannot land in (10*): their coarse sheets are free (written 2026-11-21T07:12Z, date -u)

**Rule 0a.** Searched before writing: `grep -i` for "sheet", "Fourier", "monopole", "'t Hooft loop",
"topological" in `library/gap-blockstep2-astra62.md`, `gap-blockstep2-check-opus.md`,
`gap-blockstep4-astra62.md`, `gap-mini-nphys-fable.md`, `gap-mini-neutral-step-fable.md`; `library/open-core.md`
has no line on sheet weights. On file: the Fourier formula for the coarse sheet weight (row 1354 6.2 item 1,
PROVED there, elementary) and the bound (9) of row 1345 on the mass of sign arrays that violate a cube
constraint. Neither row draws the conclusion below. Row 1354 4.4 and 6.1 state the opposite hope. Credit:
gpt-6.2-astra for row 1345 (the map, (7), (8), (9)), checked by Claude Opus 5.5 in row 1347; G. Mack and
V. Petkova for the centre split; G. 't Hooft for the loop operator that appears in 2.4.

**2.1 Setting (row 1345 (1)-(3), L73-103; READ, not re-derived).** A periodic fine lattice, tiled by blocks of
side B; the coarse torus has v sites, 4v links, 6v plaquettes and 4v three-cubes. Each coarse plaquette P has
its packet S_B(P) of B^2 fine plaquettes. For a sign array tau on the coarse plaquettes, Z_tau is the Wilson
mass in which q_p is replaced by tau_P q_p on every packet. Facts used:

- (F1) Z_tau > 0, and Z_tau <= Z_0 for the array tau = 1 (row 1345 (7) with no deletion).
- (F2) Z_(tau d sigma) = Z_tau for every sign array sigma on the coarse links (row 1345 L89: flip the bundle).
- (F3) Z_tau = integral of a_B(dy) E_t exp(sum_P J_P(y) tau_P (dt)_P), with fair coarse link signs t (row 1345
  (1)-(3); the sign tau_P multiplies the whole packet sum).
- (F4) If 6 sqrt(u_beta) < 1 and d tau = -1 on k coarse three-cubes, then Z_tau <= q_B^k Z_0, with
  u_beta = e^((17/18) beta)/A(beta) and q_B = (6 sqrt(u_beta))^(B/19) (row 1345 (8)).

Write C for the group of coboundaries d sigma, H^2 for the 64 classes of closed arrays, and Z_h for the common
value of Z_tau on the class h. For a set S of coarse plaquettes put

    W(S) = 2^(-6v) sum over all 2^(6v) arrays tau of ( prod_{P in S} tau_P ) Z_tau .

**2.2 Lemma SW (the sheet weights are the Fourier coefficients; PROVED; (a), (b) are row 1354 6.2 item 1).**

- (a) W(S) = 0 unless S is a cycle (every coarse link lies in an even number of plaquettes of S).
- (b) For a cycle S, W(S) = integral of a_B(dy) prod_{P in S} sinh J_P prod_{P not in S} cosh J_P. For every
  array tau, Z_tau = sum over cycles S of W(S) prod_{P in S} tau_P. So the W(S) are the sheet weights of the
  coarse representation: the numbers that Theorem E of row 1354 expands and bounds in the class (10*).
- (c) Let mu be the probability law mu(tau) = Z_tau / sum_tau' Z_tau' on sign arrays. Then
  W(S)/W(empty) = E_mu[ prod_{P in S} tau_P ]. If S is the boundary mod 2 of a set V of coarse three-cubes,
  then W(S)/W(empty) = E_mu[ prod_{c in V} (d tau)_c ].

Proof. (a) By (F2), W(S) = W(S) prod_{P in S} (d sigma)_P = W(S) prod_E sigma_E^(n_E), with n_E the number of
plaquettes of S that contain E. If some n_E is odd, take sigma = -1 on that link only. (b) By (F3),
e^(J x) = cosh J + x sinh J for x = 1 or -1, and E_t prod_{P in S} (dt)_P = 1 if S is a cycle and 0 if not. This
gives the expansion of Z_tau; Fourier inversion on the group of sign arrays gives the formula for W(S). (c) The
first claim is the definition. For the second, a plaquette lies in an odd number of the cubes of V exactly when
it is in the boundary of V. QED

**2.3 Proposition THIN (PROVED GIVEN (F1)-(F4)).** Assume 6 sqrt(u_beta) < 1 and put
eta = 64 [ (1 + q_B)^(4v) - 1 ]. Then:

- (a) mu(d tau is not 1) <= eta.
- (b) For every set V of coarse three-cubes, W(boundary of V) >= (1 - 2 eta) W(empty).
- (c) For every cycle S, the number W(S)/W(empty) differs by at most 2 eta from
  sum_h chi_S(h) Z_h / sum_h Z_h, where chi_S(h) is the pairing of the class of S with the class h.
- (d) On the first-passage tail, with either choice of B in row 1345 (B = L^K, or B = L^j fixed with
  B lambda_sharp/1368 > 4 log L), eta tends to zero uniformly, on both tori.

Proof. (a) is row 1345 (9) in the present notation: a syndrome d tau with k odd cubes has exactly 64 |C|
arrays above it, there are at most binom(4v, k) such syndromes, and (F4) bounds each array by q_B^k Z_0; the
arrays in C alone have the mass |C| Z_0. (b) By Lemma SW (c), W(boundary of V)/W(empty) is the mean of a
function that is 1 on closed arrays and has modulus 1. (c) On a closed array, prod_{P in S} tau_P = chi_S of
its class, and the closed arrays of the class h have the mass |C| Z_h; a mean under mu and the mean under mu
conditioned on closed arrays differ by at most 2 mu(not closed) for a function of modulus at most 1. (d) is
row 1345 L103. QED

Instance (arithmetic only, with I_1(beta) = e^beta (2 pi beta)^(-1/2) (1 - 3/(8 beta) + ...)): at beta = 300,
u_beta = 3.8 x 10^(-4) and 6 sqrt(u_beta) = 0.116; with B = 190, q_B = 4.6 x 10^(-10); on a coarse torus 16^4
(v = 65536), eta = 0.0077. So the hypothesis is not empty, and it needs a large bare coupling: 6 sqrt(u_beta)
is below 1 only for beta above about 215.

**2.4 Reading (the identities are PROVED above; the physics words are GUIDE).** An array tau with
d tau = -1 on a coarse cube puts a line of B frustrated fine cubes on the triple crossing of that cube. So
Z_tau/Z_0 is the expectation of a thin Z_2 monopole loop, the 't Hooft loop, drawn along the coarse dual
lattice. (F4) is a perimeter law for it: the cost grows like B times the length. Row 1354 6.2 item 1 read this
cost as a thick-monopole free energy of order beta that does not depend on B. That reading was wrong for this
map. By Lemma SW (c) a coarse sheet that bounds has the weight E_mu[(-1)^(number of monopole lines through V)].
Monopoles are suppressed, so the weight is near W(empty): the sheets that bound are free. By (c) the sheets
that do not bound carry the Fourier transform of the 64 twisted masses. For a confining theory (all Z_h nearly
equal) their weight is near zero. So the image of a confining theory under the centre-sign map is a
topological sheet gas: the weight of a sheet depends on its homology class only, up to 2 eta.

**2.5 Lemma RS (in the class (10*) every sheet is rare; PROVED GIVEN row 1351's bound (12) and deletion
induction, in the form that Theorem E of row 1354 uses; the proof uses the moment bound and the factorization
only, so it holds for the moment form of row 1354 4.4 as well).** In a model of the class (10*), with the sheet weights
W(S) = E[ prod_{p in S} beta_p prod_{p not in S} alpha_p ] of its expansion, every nonempty cycle S has

    | W(S) | <= 31^(-|S|) W(empty),      and W(empty) > 0.

Proof. Write alpha_p = 1 + h_p and c(S, X) = E[prod_S beta_p prod_X h_p] for X disjoint from S. The Hoelder
step of row 1351 L124, as the proof of Theorem E uses it, gives |c(S, X)| <= u^|S| eps^|X| (u = 1/40,
eps = 1/4096), and c factors over sets that are not adjacent (adjacent: a common link or a common
three-cube; a closed neighbourhood has at most 41 plaquettes). Put
Xi_D = sum over X in D of c(empty, X), so W(empty) = Xi for D = all plaquettes. The deletion induction of row
1351 L134, run with no surfaces, gives Xi_D > 0 and Xi_(D minus p)/Xi_D <= e^(1/256). Now fix S. For X disjoint
from S let X_1 be the part of X in the components of S union X that meet S, and X_2 the rest. Then
c(S, X) = c(S, X_1) c(empty, X_2), and X_2 runs over the subsets of the set D(X_1) of plaquettes that are not in
and not adjacent to S union X_1. So W(S) = sum over X_1 of c(S, X_1) Xi_(D(X_1)), and
Xi_(D(X_1))/Xi <= e^(41 (|S| + |X_1|)/256). Each component of X_1 (components taken inside X_1) has a plaquette
adjacent to S; there are at most 41 |S| such anchor plaquettes. The sum over the connected sets X through
one anchor of (eps e^(41/256))^|X| is at most 1/512: it is part of the rooted sum that row 1351 bounds by
(12) with x = 2 e^(41/256). Hence
|W(S)|/Xi <= (u e^(41/256))^|S| (1 + 1/512)^(41 |S|) <= (e^(123/512)/40)^|S| < 31^(-|S|) (e^(123/512) < 1.272).
QED

**2.6 Corollary (what THIN excludes; PROVED GIVEN 2.3 and 2.5).** Call a change of representation
sign-pointwise if it changes or integrates environment variables at each fixed array of coarse centre signs,
so that it keeps Z_tau for every tau. Integration of angular variables is of this kind; so is the gluing (2)-(3)
of row 1351 (READ at L26-45; the strip elimination was not read in detail).

- (a) Sign-pointwise changes keep every W(S). So no chain of them carries the image of row 1345's map into
  the class (10*) on the tail: by 2.3 (b) the elementary coarse cube has W >= (1 - 2 eta) W(empty), and by 2.5
  a model of (10*) has W <= 31^(-6) W(empty) there.
- (b) A further centre-sign step with a larger block side has the same property (2.3 with the larger B).
- (c) The hope of row 1354 4.4 fails on the tail: W(S) is the weight after the whole environment is
  integrated, and it is not small. No cancellation of the signs of sinh J_P occurs for sheets that bound.

What this does not exclude: a map that is exact only for the eight temporal twists and changes the other
Z_tau; a different coarse centre variable (Step 3). It is a statement on the tail (large bare beta). At
small beta the opposite holds for B = 1 (Wilson is in (10*) for beta <= 1/46, row 1354 3.2). At a fixed small
beta and a growing block side the image leaves the class again (ARGUED: the coarse cube collects the B fine
cubes of its triple crossing, so W(cube)/W(empty) grows like B times the weight of a fine cube until it
saturates; I did not write the bounds).

**2.7 Consequence for the target (ARGUED from 2.3 to 2.6).** For the centre-sign maps the landing class of a
confining theory is not (10*). It is a class with locked local signs and free classes: row 1345 (11), whose
reference has free plaquette signs with one cube constraint each. In that picture everything that the seed
needs is in two places: the 64 twisted masses (the classes), and the mass W_B = 2^(3v) integral of
a_B prod cosh J_P of row 1345 (9), which is a local positive product. When the 64 classes weigh the same on
both tori, W_B is 8 Z_0 up to the factor 1 + eta, so its cover defect is that of Z_0 plus 3 (m - 1) log 2 (the
term that row 1345 (6) says must cancel). Both are integrals over the angular field. By row 1345
(5) the remaining integral is the Wilson integral itself on an event of probability 1 - p_T. So the centre-sign
maps do the centre sums exactly and uniformly on the tail, and they leave the angular problem unchanged. The
class (10*) is the class of a different variable: the centre sign of an SU(2)-valued block link, whose two
values have nearly equal weight (row 1353 Section 5, Theorem END-D).

## Step 3. Which coarse variable has rare sheets, and what the step then is (written 2026-11-21T07:26Z, date -u)

Also read for this step: `library/gap-finishline-opus.md` (row 837) 1.1 to 1.6 (the account's density at first
passage, READ there from Sussman and Alpoge); `library/gap-solve2-astra62.md` (row 1145) Section 1, statements
only; `library/gap-blockstep-astra62.md` (row 1341) L19-40.

**3.1 Block-link kernels (definition; the lemma is PROVED, elementary).** Keep the tiling of row 1345 and its
bundles: b(E) is the set of fine links that cross the face of the coarse link E. For a sign array sigma on
the coarse links, U^sigma is U with the bundle b(E) multiplied by sigma_E, and V^sigma is the coarse field
with V_E multiplied by sigma_E. A block-link kernel is a probability density k(V | U) for a coarse field V
in SU(2)^(coarse links), with respect to Haar measure, measurable in the fine field U, with

- (K1) the integral of k(V | U) dV is 1 for every U;
- (K2) k(V | U^sigma) = k(V^sigma | U) for every sigma (centre covariance).

Examples: V_E = the straight transport along one line (row 1145); V_E = a normalized average of transports
that cross the face once (the averaging of Balaban that the account uses); either one with a heat-kernel
factor in place of the delta function (the pins of rows 861 and 1340, moved to block links).

**Lemma KER.** Put rho^tau(V) = integral of k(V | U) w_tau(U) dU, with w_tau the Wilson weight with the packet
signs tau. Then: (a) the integral of rho^tau(V) dV is Z_tau, for every tau; so the map is mass-preserving and
exact for every twist. (b) rho^(tau d sigma)(V) = rho^tau(V^sigma). (c) For tau = 1: rho(V^sigma)/rho(V) is the
conditional mean, given V, of exp(-2 sum of X_P over the coarse plaquettes with (d sigma)_P = -1), where
X_P = beta times the sum of q_p over the packet. In particular the unconditional mean of
exp(-2 sum_{P containing E} X_P) under the Wilson law is exactly 1.

Proof. (a) Fubini and (K1). (b) w_(tau d sigma)(U) = w_tau(U^sigma) pointwise (this is (F2) before
integration); substitute U -> U^sigma, which preserves Haar measure, and use (K2). (c) is (b) written with
the joint law k(V | U) w(U) dU dV / Z; the last claim is (F2) for tau = d sigma. QED

So the centre sign of a block link has the coupling of (c): the conditional cost of the thin flip, given
the coarse field. In the centre-sign map of row 1345 the whole fine environment is kept, the cost is
pointwise, and it is of order B^2 beta (row 1345 L34). In a block-link image the cost is averaged over the
fine field given V. The class (10*), and Theorem END-D of row 1353, are classes for this second variable.

**3.2 Free signs are cheap, and they are not the content (READ and ARGUED).** For straight transports the
sign is free at every coupling and for every compact group: given all links off the lines, the links of a
line are independent, and the transport of h steps converges in density to Haar (row 1145 Section 1, PROVED
there; the mechanism is the perimeter law of Simon and Yaffe). Row 1145 also records what fails: the
straight grid keeps no spectral information (its L51), because the field off the lines carries the
correlations. So a block-link image with small windows of one link is available for the asking. What a
landing in END-D needs beyond that is the decay of the windows with their size, at one rate, on both tori
with the same local rules: N_kappa(f) <= kappa/32 (row 1353 5.1). For a product kernel the image is
rho(V) = Z E[ prod_E k_E(V_E | U) ], with the mean in the Wilson law of U, and the windows are the cumulants,
in that law, of the local factors k_E. So the content of the step is a mixing statement for the fine law, with a rate, uniform in
the cutoff, at one physical mesh. A product with a massless factor, and compact U(1) at large coupling,
have free straight signs and no such decay.

**3.3 The account's block field is on the locked side (READ in row 837 1.2 and 1.3; not re-read in the
account).** At first passage the account gives the density rho_K of its block field V_K on the unit
lattice: the Wilson action of a background field at the coupling x_K >= gamma^(-2), local terms, and
large-field regions with weight e^(-c p_0(g)) per component. This is a block-link image in the sense of 3.1
(K2 holds for an average of transports; I did not check the account's exact averaging against (K2)). Its
signs are locked: a flip of one block link leaves the small-field region. So a block-link chain from the
account's class to END-D is the continuation of the account's own renormalization through the range where
its hypothesis g_k <= gamma fails (row 837 1.1, from the account's citation of Balaban's stability theorem),
down to couplings where the block field is nearly Haar. Row 1332 6.3 and 6.4 say this in the words "one
block step at an effective coupling of order one", and count the steps.

**3.4 The step, corrected (OPEN).** (BS-BL) There are a block-link kernel that reads a bounded neighbourhood
and one physical coarse mesh such that, for every late datum, the images on the two tori have the form
c^v prod_W (1 + f_W) with the same local rules and N_kappa(f) <= kappa/32. By Lemma KER and Theorem END-D this
gives the neutral and the periodic two-period bounds and alternative I. It replaces (BS*) of row 1354 6.1,
whose natural reading (the centre-sign map into (10*)) is excluded on the tail by Step 2. I do not claim
that (BS-BL) is necessary for (N-phys): the consumer needs the two masses only (row 1353 6.1), and a
landing in a class with decaying windows is a stronger statement than a gap of the periodic transfer
operators (ARGUED: it gives the tree decay of all cumulants of the coarse field, for supports that no
hyperplane separates as well).

**3.5 Remark on END-D (PROVED by inspection of row 1353's proof; small).** Theorem END-D is stated for
windows that are boxes, with size = the number of sites of the box. Cumulants of a block-link image decay
in the tree length of their support, not in the volume of its bounding box (three coarse plaquettes at
mutual distance r have tree length about 2r and a bounding box with about r^2 sites or more). The proof
of END-D holds word for word when a window is any connected set of links that meets at most
min(T, m) - 2 sites, with size(W) = the number of sites it meets. Such a set projects to an arc in each
coordinate, so it has a smallest box, and the twist function of the window is taken from that box. Step 2
uses only that a window has at most 4 size(W) links. Step 5 uses only that a connected family of windows of
total size k lies in one embedded box, and that the twist function of that box differs from the twist
function of the smallest box of each window by end signs on the window (the two have the same plaquette
products on the smaller box, and a box is simply connected). I use END-D in this form in 3.4.

## Step 4. The step attacked three ways, and where each stops (written 2026-11-21T07:28Z, date -u)

The statement is (BS-BL) of 3.4, or any landing of the trajectory in an end class that a confining theory
can reach. Each way below is a pairing of a coarse variable with an end class.

**Way 1: centre signs of thin packets (the maps of rows 1345 and 1351), into (10*).** Refuted on the tail
by Step 2: the sheets that bound are free (Proposition THIN), every model of (10*) has rare sheets (Lemma
RS), and sign-pointwise changes keep the sheet weights (Corollary 2.6). Into the class with locked signs
and free classes, row 1345 (11): the centre sums are exact and uniform on the tail (row 1345 (5), (10)),
and what is left is the Wilson integral on an event of probability 1 - p_T. Stops at: the angular integral,
unchanged. (New here: the exclusion of (10*); the rest is rows 1345 and 1354.)

**Way 2: straight block links, into END-D.** By Lemma KER the map is exact for every twist. The norm half
of the landing holds at every coupling and for every compact group: given the rest, a transport of h steps
is nearly Haar (row 1145 Section 1). The decay half fails without an input: the windows of the image are
cumulants of functions of the field off the lines (3.2), and the straight grid keeps no spectral
information (row 1145 L51). The same construction applies to compact U(1) at large coupling and to a
product with a massless factor, where no landing in END-D exists, because END-D gives the periodic seed
(row 1353 5.2, 5.3) and those models have none (`parts/gap.md` test table). Stops at: the mixing of the
fine field at the physical mesh, with a rate. (READ and ARGUED; nothing here is new except the statement
through Lemma KER.)

**Way 3: averaged block links, one more step past first passage; or one exact step on the plaquette
cover.** The account's block field at first passage is an averaged block link on the locked side (3.3).
Its step theorem has the hypothesis g_k <= gamma (row 837 1.1); the number of further steps to a coupling
of order one is at least 7 e-folds of length (row 1332 6.4), each at a coupling above the ceiling. The one
exact step on file that removes every raw plaquette is the integration on the plaquette cover (row 1341
L19-31, with Lemma LF of the Opus lane): it leaves six-staple factors A(beta |v_1 + ... + v_6|)/A(beta)^6 on
the other links, it does not lower the coupling (the factor is of the order e^(beta |sum of staples|)), and
row 1341 finds that its residual is not in a class closed under a next step (its L31, and the obstructions
(24), (27)). Stops at: a class with bounds on both sides of one step at a coupling of order one. This is
row 1332 6.5 and row 1340's first failing step; the finite statement of one such step is far above 10^15
exact operations by every sizing on file (rows 1326, 1340, 1353 3.3).

**4.1 The first failing step, as one statement (OPEN; not new).** For the Wilson trajectory at one
physical mesh: the law of the fine field mixes with one exponential rate, uniformly in the late cutoffs, in
the form that an end class reads (decaying windows of a block-link image; or the two masses of a cell with
its surroundings in law). In the block-link form it is (BS-BL). On file it is the open hypothesis (DS-W) of
row 691 in its in-law forms, the step of row 1332 6.5, and (M-neutral) of row 1353 6.3 when only the two
masses are asked. I found no way to it that is not on file, and no finite statement of it inside the
budget. I prove no impossibility.

**4.2 Why the centre does not help above the monopole scale (GUIDE, with the identities of Step 2).** At
B = 1 the law mu of 2.2 (c) is the law of independent plaquette signs with the fields beta q_p(U), where U
is drawn from the model with the even weights cosh(beta q_p). Lemma SW (c) then reads: the weight of a
sheet that bounds a volume V is the mean parity of the thin Z_2 monopoles in V. For small beta the
monopoles are dense and nearly independent, the parities are unbiased, the sheets are rare, and Wilson is
in (10*) (row 1354 3.2, beta <= 1/46 by proof). On the tail the monopoles are suppressed (F4), and the
sheets that bound are free at every block side. Between the two regimes the even model is believed to
have a bulk transition where its Z_2 monopoles condense (recalled from the physics literature on SO(3)
and mixed actions, Bhanot and Creutz, Halliday and Schwimmer; not checked, no proof step). So an exact
reformulation through central variables alone can show rare sheets only on the strong-coupling side of
that transition. Above it the central variables are locked, the 64 class weights carry the whole content
of confinement, and they are properties of the angular field at the physical scale. First-passage data
are on that side.

## Step 5. Corrections to row 1354, and notes for the lead (written 2026-11-21T07:32Z, date -u)

Row 1354 (`library/gap-mini-nphys-fable.md`) is an earlier row of this worker. Three of its statements need
a correction. Its PROVED statements (Lemma B0, Proposition B, Corollaries B1 and B2, Theorem E, Lemmas SST0
and SST1) are not affected; their check is row 1357.

1. **6.2 item 1 (reading).** It called the cost of a coarse centre monopole "a thick-monopole free energy"
   that "classically ... is of order beta and does not depend on B". For the map of row 1345 the monopole
   is thin: a line of B frustrated fine cubes. Its cost grows like B times the length on the tail (row
   1345 (8)). The formula of that item (the sheet weight is a Fourier coefficient of the signed-packet
   masses) is right and is Lemma SW here.
2. **4.4 and 6.1 (target).** They proposed that the sheets of row 1345's representation can be rare after
   the angular environment is integrated, and stated the step (BS*) with (10*) or its moment form as the
   end class. Proposition THIN and Corollary 2.6 exclude this on the tail for the centre-sign maps. The
   class (10*) is a class for the sign of a block link (Step 3), and the step is (BS-BL).
3. **6.2 item 2 (ARGUED there; withdrawn).** It said that the chessboard norms of sinh(beta q) and
   cosh(beta q) are 2 I_2(beta)/beta and 2 I_1(beta)/beta, that a sheet therefore "costs at most
   t(beta) = I_2/I_1 per plaquette, for every beta", and that the expansion converges for beta below about
   0.8. The first step is not valid. The product over all plaquettes of ONE orientation is a product of
   two-dimensional sums, with those leading coefficients. But no chessboard estimate bounds a product over
   all six orientations by these norms. Test with the empty sheet (ARGUED; small beta, where the
   strong-coupling expansion converges): the bound would give W(empty) <= A(beta)^(6v) (1 + o(1))^(6v), with
   A = 2 I_1(beta)/beta, on large tori; but W(empty) = A^(6v) exp(36 v x_1^6 + ...), x_1 = I_3/I_1 > 0, because a
   cube with its six faces in the spin-one representation has the positive weight 9 x_1^6 and there are 4v
   cubes. What Hoelder's inequality over the six orientations gives is a bound with sixth-moment norms,
   |W(S)| <= norm_6(sinh(beta q))^|S| norm_6(cosh(beta q))^(6v - |S|) up to the two-dimensional corrections,
   which is the form of (10*) and has no factorization. What holds pointwise at B = 1 is
   |W(S)| <= (tanh beta)^|S| W(empty) (PROVED: W(S)/W(empty) is the mean of prod_{p in S} tanh(beta q_p) in
   the even model, and |tanh(beta q_p)| <= tanh beta); with it the centre sum converges uniformly in the
   angular field only for tanh beta below about 1/5, beta below about 0.2 (the comparison of Mack and
   Petkova; ARGUED here, not written out). The ceiling 0.8 has no proof on file.

**For the lead (proposals; no file other than this one was edited).**

1. A landing of the centre-sign maps in (10*) should not be queued: it is excluded on the tail (Step 2).
   The check of Step 2 needs row 1345 L73-103 with its check (row 1347 L148-170) and row 1351 L124-134:
   Lemma SW, Proposition THIN, Lemma RS, Corollary 2.6. Step 3 adds Lemma KER (five lines) and the remark
   3.5 on END-D.
2. The four pairings of a coarse variable with an end class are now each on file with their first failing
   step: thin signs into the coherent class (10) (alternative II; row 1354); thin signs into (10*)
   (excluded on the tail; this row); thin signs into the class with free classes, row 1345 (11) (the
   Wilson integral itself is left; rows 1345 and 1353); block links into END-D or (10*) (a mixing
   statement with a rate; rows 1145, 1353 and Step 3). In each one the centre part is done exactly or is
   group-blind, and the open part is the same integral over the angular field at the physical scale. So
   the chain of Proposition CH is sound and does not shrink the problem: no pairing on file turns the
   seed into a smaller statement. I would reopen this line only for a block map that comes with a named
   mechanism of contraction at a coupling of order one, which is the reopen condition of route RA in
   `parts/gap.md`.
3. The remark 4.2 may be useful as a filter: a row that works with central variables alone (signs,
   packets, classes) can reach rare sheets only where thin Z_2 monopoles are dense; on the trajectory
   they are suppressed, and the centre is locked at every block side.

## Step 6. Summary (written 2026-11-21T07:32Z, date -u)

**Solved?** No. The carry of the trajectory into an end class is not proved. (N-phys) and the mass gap are
not proved. No finite computation is specified. No step of the chain is disproved, and no impossibility of
the mass gap route is proved.

**PROVED here (by hand; author only; given the named statements of rows 1345 and 1351, both checked by
Claude Opus 5.5 in rows 1347 and 1352, and the proof structure of Theorem E of row 1354, whose check is row
1357).**

- Lemma SW: the sheet weights of the coarse centre representation are the Fourier coefficients of the
  signed-packet masses; for a sheet that bounds a volume V the relative weight is the mean of the product
  of (d tau)_c over the cubes of V in the positive law mu(tau) = Z_tau / sum Z ((a), (b) are row 1354 6.2
  item 1).
- Proposition THIN: on the tail (6 sqrt(u_beta) < 1, eta = 64[(1 + q_B)^(4v) - 1] small) every sheet that
  bounds has weight at least (1 - 2 eta) W(empty), and the weight of every cycle is the Fourier transform of
  the 64 twisted masses up to 2 eta. Instance: beta = 300, B = 190, a coarse torus 16^4, eta = 0.0077.
- Lemma RS: in the class (10*), and in its moment form, every nonempty cycle has |W(S)| <= 31^(-|S|) W(empty).
- Corollary 2.6: no chain of sign-pointwise changes carries the image of the centre-sign map of row 1345
  into (10*) on the tail; a larger block side does not help.
- Lemma KER: a centre-covariant block-link kernel gives a map that keeps every signed-packet mass; the
  coupling of a block-link sign is the conditional thin-flip cost given the coarse field; the unconditional
  mean of exp(-2 sum_{P containing E} X_P) is 1.
- Remark 3.5: Theorem END-D of row 1353 holds with windows that are connected sets (by inspection of its
  proof).
- Step 5 item 3: at B = 1, |W(S)| <= (tanh beta)^|S| W(empty) for every beta.

**ARGUED here.** 2.7 and 3.2 to 3.4: for the centre-sign maps the confining landing class is row 1345 (11)
and the open part is the Wilson integral itself; (10*) and END-D are classes of block-link signs; free
signs are available for every compact group, and the content of a landing is a mixing statement with a
rate; the account's block field at first passage is on the locked side, so the block-link chain is the
continuation of its renormalization past the ceiling. Step 5 item 2 for the lead: no pairing on file
shrinks the seed.

**GUIDE.** 2.4 (the thin 't Hooft loop reading; the image of a confining theory is a topological sheet
gas), 4.2 (the monopole condensation of the even model as the limit of central methods; recalled physics,
not checked), the arithmetic instance of 2.3.

**OPEN.** (BS-BL) of 3.4 at any coupling above the hand range (0.3609 by row 836); equivalently in kind
the in-law mixing statement of 4.1, (DS-W) of row 691, (M-neutral) of row 1353; its form uniform in the
cutoff; a perimeter law for the thin Z_2 monopole loop at every coupling (it would extend Proposition THIN
from the tail to every beta at large B; not needed for the trajectory; ARGUED: the map tau -> Z_tau is
reflection positive at planes through sites, so by the chessboard estimate the law follows from the strict
positivity of the pressure deficits of finitely many periodic frustrated sign patterns, which I did not
prove at intermediate beta); (N-phys); the mass gap.

**Not done.** I did not read the outputs of rows 1356 and 1357 (not on disk at this pin). I did not re-read
the account of Sussman and Alpoge; statements about it come from rows 837 and 1345. I did not re-derive the
constants of rows 1345 and 1351. I did not search origin/main or the open PR branches (this checkout has no
such refs). I ran no numeric job. I read no published paper in this row; the published results named
(Mack and Petkova, Simon and Yaffe, 't Hooft, Bhanot and Creutz, Halliday and Schwimmer) are recalled.


RESULT: Row 1358 (Claude Fable 5.2 max, Mac mini worker 2; author only, checked by no one; no numeric job, arithmetic only). NOT solved: the carry of the Wilson trajectory into an end class is not proved, (N-phys) and the mass gap are not proved, no finite computation is specified, and no impossibility is proved. Main finding, PROVED GIVEN row 1345 (7)-(9) and row 1351 (12) (both checked, rows 1347 and 1352): the centre-sign block maps on file cannot land in the Fourier-dual class (10*) on the cutoff tail. Lemma SW: the coarse sheet weights are the Fourier coefficients of the signed-packet masses, and a sheet that bounds a volume V has relative weight E_mu[prod over the cubes of V of (d tau)_c] in the positive law mu(tau) = Z_tau/sum Z. Proposition THIN: for 6 sqrt(u_beta) below 1 and eta = 64[(1 + q_B)^(4v) - 1], every sheet that bounds has weight at least (1 - 2 eta) W(empty), and every cycle carries the Fourier transform of the 64 twisted masses up to 2 eta (instance beta 300, B 190, coarse torus 16^4: eta 0.0077; eta tends to 0 uniformly on the tail). Lemma RS: in (10*) and in its moment form every nonempty cycle has weight at most 31^(-area) W(empty). Corollary 2.6: sign-pointwise changes of the environment keep all sheet weights, so no chain of them, and no larger block side, brings the image of row 1345's map into (10*). So the image of a confining theory under these maps is a topological sheet gas (sheets that bound are free; the classes carry everything), its landing class is row 1345 (11), and what stays is the Wilson integral itself. Also PROVED: Lemma KER (a centre-covariant block-link kernel keeps every signed-packet mass; the coupling of a block-link sign is the conditional thin-flip cost; the mean of exp(-2 sum over the packets around one coarse link) is exactly 1); Theorem END-D of row 1353 holds for windows that are connected sets (by inspection); at B = 1 every sheet weight is at most (tanh beta)^area W(empty). ARGUED: (10*) and END-D are classes of block-link signs; free signs hold for every compact group (straight transports, row 1145), and the content of a landing is a mixing statement with a rate at one physical mesh, the corrected step (BS-BL); the account's block field at first passage is on the locked side, so the block-link chain is the continuation of its renormalization past the ceiling; none of the four pairings of a coarse variable with an end class now on file turns the seed into a smaller statement. Corrections to row 1354 (same worker): its reading of the monopole cost in 6.2 item 1 was wrong for this map, its target (BS*) with (10*) is excluded on the tail, and its 6.2 item 2 (the chessboard cost I_2/I_1 per plaquette and the ceiling 0.8) is withdrawn. First failing step, three ways (Step 4): the in-law mixing of the fine field at the physical scale, on file as (DS-W) of row 691, the step of row 1332 6.5 and (M-neutral) of row 1353. OPEN: (BS-BL) at any coupling above the hand range 0.3609, its form uniform in the cutoff, a perimeter law for the thin Z_2 monopole loop at every coupling, (N-phys), the mass gap. Output library/gap-mini-dualstep-fable.md.
