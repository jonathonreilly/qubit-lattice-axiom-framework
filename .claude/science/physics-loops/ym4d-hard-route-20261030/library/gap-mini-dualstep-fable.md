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
  (`gap-mini-solve-ab-opus.md` L52, `gap-brainstorm-max.md` L312).

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
induction, in the form that Theorem E of row 1354 uses).** In a model of the class (10*), with the sheet weights
W(S) = E[ prod_{p in S} beta_p prod_{p not in S} alpha_p ] of its expansion, every nonempty cycle S has

    | W(S) | <= 31^(-|S|) W(empty),      and W(empty) > 0.

Proof. Write alpha_p = 1 + h_p and c(S, X) = E[prod_S beta_p prod_X h_p] for X disjoint from S. Row 1351 proves
|c(S, X)| <= u^|S| eps^|X| (u = 1/40, eps = 1/4096), and c factors over sets that are not adjacent (adjacent:
a common link or a common three-cube; a closed neighbourhood has at most 41 plaquettes). Put
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
with the same local rules: N_kappa(f) <= kappa/32 (row 1353 5.1). For an image
rho(V) = E[ prod_E k_E(V_E | U) ] the windows are the cumulants, in the law of the fine field, of the local
factors k_E. So the content of the step is a mixing statement for the fine law, with a rate, uniform in
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
min(T, m) - 2 sites, with size(W) = the number of sites it meets, and the twist function of a window taken
from its bounding box: Step 2 uses only that a window has at most 4 size(W) links; Step 5 uses only that a
connected family of windows of total size k lies in one embedded box, and that the twist functions of two
boxes that contain a window differ on it by end signs (both have the same plaquette products on the
smaller box, and a box is simply connected). I use END-D in this form in 3.4.

