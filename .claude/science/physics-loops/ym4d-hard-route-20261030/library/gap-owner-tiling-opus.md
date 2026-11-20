lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T02:14Z

# gap-owner-tiling-opus (FINISH row 1285): the owner's multi-direction idea, the tiling question

Row: 1285 of FINISH.md, branch claude/ym4d-hard-route pinned at ff38f286f. Worker: Claude Opus 5.5 (max), Mac mini
Claude worker 1. Labels: PROVED, ARGUED, GUIDE, OPEN as the row asks. Sibling row 1286 (gpt-6.2-astra, same question)
is `library/gap-owner-tiling-astra62.md`; it is read only after my own Section 3 is written, and cited where used.

## Status log

- 2026-11-20T14:14Z (date -u): file created; reading FINISH rules, `parts/gap.md`, rows 1273 and 1279.
- 2026-11-20T14:21Z (date -u): Section 1 written (inputs, registry grep, plan).
- 2026-11-20T14:39Z (date -u): Section 2 written (the tiling theorems on file; small-volume half decided by row 720).
- 2026-11-20T14:41Z (date -u): Section 3 written (axis versus angle; Proposition AX in the Gaussian model).
- 2026-11-20T14:44Z (date -u): numeric lock acquired 14:43:59Z (holder gap-owner-tiling-opus, memory 51 percent free); Section 4 criteria written before the Wilson runs.
- 2026-11-20T14:48Z (date -u): Section 5 written (attacks 2 and 3); Part 3 waiting for memory (41 percent free at 14:47Z).

## 1. Inputs, repo search, plan

Read at ff38f286f, before any attack: `FINISH.md` rule sections (L52-73, L320-350) and rows 1273, 1279, 1285;
`GOAL.md` in full; `parts/gap.md` L8-104 (state of attack, lead rules); `library/gap-mini-neutral-fable.md`
L30-60 (the exact (N-phys) statement, row 1161 / row 1179 wording); row 1273's file
`library/gap-owner-threeaxis-opus.md` in full; check 1279 `library/gap-threeaxis-check-astra.md` L55-123 (the
Hamiltonian, tiling and verdict sections). **Provenance of independence:** the sibling row 1286
(`library/gap-owner-tiling-astra62.md`, gpt-6.2-astra, same question, committed at my pin) was read at its outline
and its RESULT line (L209) only, before I chose my attacks, so that I do not repeat it. Its ground: reduced-model
arrays of N^3 periodic-block oscillators (independent, exactly constrained, finite and infinite spring stiffness,
tree sewing with dynamical frames giving a singlet gap asymptotic to kappa_r g^(2/3)/(N l), cyclic adjoint sewing
with at least 3N^3 soft neutral plaquette excitations), and a Wilson trace estimate (its (7)) for straight segment
transports, with the unselected links and the fine fluctuations left OPEN. Everything below is my own unless a
row is cited.

**Consumer (the "couplings the lane needs").** (N-phys) (row 1161 L146-148, wording of row 1179, quoted in
`gap-mini-neutral-fable.md` L39-49): one admissible physical side L and j_0 such that for every j >= j_0, with
n_j = L/a_j, 4 | n_j, some integer u_j in [3, n_j/K] gives s_j(u_j; n_j) <= 1/2, where s is the centre-neutral
excited thermal sum of the periodic cube in vacuum units and K = 512. GUIDE size (same file 2.4): m L of order
1.1 x 10^4. Equivalent and sufficient forms of the older wall (W) (z^-(L) > 256 D_0 + 30 at one L in the window)
are listed in `parts/gap.md` L13-35.

**Registry grep** (counts of files among `library/*.md`, `library/prior/*.md`, `parts/*.md` that contain the
term, case-insensitive, at ff38f286f): tiling 80, tiled 15, Knabe 33, "finite-size criterion" 37,
local-to-global 15, Garland 0, trickle 2, Yarotsky 1, Michalakis 13, Gosset 18, Stroock 42, Zegarlinski 25,
"block dynamics" 10, Martinelli 36, 4.1167 6, g^(2/3) 12, "2 pi/L" 7, "photon gap" 1, stiffness 128, spring 43,
Nedelko 1, "domain model" 2, Copenhagen 1, "intermediate volume" 0, sphaleron 2, Koller 18, "van Baal" 48.
So finite-size (local-to-global) criteria and the small-volume literature are heavily on file; each statement
below that touches them cites the hit it rests on (Section 2 lists the hits read).

**Plan (provisional; one step per response, appended at once).**
1. This section.
2. The tiling question as a carry statement: which carry theorems are on file (lane engine, (N-phys) consumer,
   Knabe / Martinelli / Dobrushin-Shlosman forms), what each needs from one block, and what a multi-direction
   block supplies (Lemma S: z = kappa g(l)^(2/3)). Read the registry hits first.
3. Value test (fact test with the free photon): is the single-block neutral gap of SU(2) selective at all?
   Lattice photon spectrum by hand.
4. Attack on the carry itself in the Wilson setting: the stiffness that the Wilson action puts between blocks,
   and what it does to the one-block mechanism.
5. A second, distinct attack on the first failing step of 4 (local-to-global criterion with a boundary-uniform
   block input).
6. Verdict and RESULT line.

## 2. The tiling question as a carry statement; the small-volume half is decided on file

Written 2026-11-20T14:39Z (date -u). Reading plus elementary remarks; no numeric run. Anchors taken with `grep -n -F`.

**2.1 Two readings of "carry".** Let a periodic block of side l have neutral gap m(l), z(l) = l m(l). Row 1273
Lemma S gives, in the reduced model, m(l) = kappa g(l)^(2/3)/l.
- (C-phys): the box of side N l has neutral gap at least c m(l) for every N. Since m(l) = kappa g(l)^(2/3)/l tends
  to infinity as l tends to 0 (g(l)^(2/3) falls only like a power of a logarithm), this fails at small l for any
  theory whose infinite-volume gap is finite in physical units. ARGUED, not a lattice theorem: the finiteness of the
  continuum gap is part of the open target. It is the reason the question can be asked only at one block size.
- (C-seed): one block supplies the input of a theorem whose conclusion is (N-phys), or the gap of all larger
  cubes. This is the reading of every tiling theorem on file (2.2).

**2.2 The tiling theorems on file take one block and a free-energy input (reading; PROVED on file).**
- Theorem D (a)-(b), row 697 (`gap-crux-restate.md` 3.1, L90-115): Z(..., j n_mu, ...) <= Z(..., n_mu, ...)^j in
  each direction (Lemma A (a), L37), the literal tiling of a torus by copies of one block, and the bound of the
  excited thermal sum of the doubled box by the doubling defect Phi(n) = 16 F(n^4) - F((2n)^4).
- Proposition R, same file 3.2 (L117-126): if the Casimir (excess) free energy Delta(n^4) is at most eps, every cube
  of side 2^k n with 8^k eps <= 1 has gap at least (1/n) log(1/(2 8^k eps)); "Positivity alone carries a seed over
  exponentially many scales. It does not carry it to infinite volume".
- Theorem S with Corollary S3' (row 697/699) and Theorem ZD-c (row 720): a seed gives all larger cubes, uniformly in
  the cutoff. Lemma FLOOR (row 988, `gap-unit-max.md` L174): a seed forces side times gap above 17.04 at threshold
  1/5041. Consumer of the newest chain: (N-phys) at one cube (`gap-mini-neutral-fable.md` L44-49).

**Reading for the owner (an exact paraphrase of Proposition R and Theorem D (c)).** In the only form in which a
tiling is a theorem here (reflection positivity, Lemma A), a tiling carries the block's free energy above the bulk
(Delta, Phi), not the block's gap. The block's gap enters only through the block's thermal sum, and a gap gives a
LOWER bound on the defect (Theorem D (c) read backwards = Lemma FLOOR), never an upper one. So "does a tiling carry
the single-block neutral gap" has, on file, one precise form: does some block have a small seed?

**2.3 Small multi-direction blocks have a large seed (on file: row 720).** `gap-phys-seed.md` L109: in a small
periodic box the seven excited flux sectors lie within exp(-12.46/g(L)) of the vacuum and add 7(1 - o(1)) to S;
each constant-mode level with eps_i g^(2/3) <= 1 adds about 1 in each of the eight sectors; so S(L/2; L^3) tends to
infinity as L tends to 0, and Delta(L^4) grows like a multiple of log(1/g(L)) (row 720's count on a fixed lattice
gives 3 log(1/g); "This count is not a proof"). The constant-mode levels eps_i g^(2/3)/L are exactly the
multi-direction spectrum whose singlet gap row 1273 proved (Lemma S, kappa = eps_1 - eps_0 in the singlet sector).

**Proposition SM (ARGUED from row 720's count and row 1273's Lemma S; the count rests on the small-volume
expansion, RECALLED there).** Below the band a periodic multi-direction block has a seed quantity S(l/2; l^3)
that grows without bound as g(l) falls, so it feeds no tiling theorem on file. In the Euclidean seed the
directional mechanism makes this worse, not better: it confines the constant modes only at the scale g^(2/3)/l,
so the number of levels below 1/l grows as g falls; and in four Euclidean dimensions the SU(2) constant-mode
integral sits at its threshold of convergence (W. Krauth and M. Staudacher; recalled on file at
`gap-uv-rigidity-max.md` L646 and `gap-mini-solve-h-fable.md` L61), which is the source of the log(1/g) growth.

**2.4 The value test (on file: rows 669, 988, 1274).** Row 1274 (`gap-owner-movingsites-opus.md` 4.3, L280-294):
the free photon has side times neutral gap 2 pi at every size; the small-box SU(2) value is of order g(L)^(2/3),
below it; the seed floor 17.04 is above both. Row 669 (`gap-skeleton-max.md` L194): "on a torus U(1) has a gap
2 pi/l as well". So a tiling theorem fed by the value of one block's neutral gap at z <= 2 pi is refuted by the
free photon; the value of Lemma S's gap is not selective. I do not repeat these.

**2.5 What is left of the question.** At the couplings the lane needs, (C-seed) asks for a seed at one block in the
band: that is (PHYS-SEED), (W), (N-phys) in another wording, not new. What row 1273 added, and check 1279 corrected,
is a directional statistic BETWEEN blocks ((TILE-dis): neighbouring blocks turn about different axes). A tiling
theorem on file reads no such statistic. So the part of the tiling question that is still the owner's own is:
**is "neighbouring blocks turn about different axes" a selective property at all, and at which couplings does it
hold?** Section 3 answers this in the weak-coupling (Gaussian) model by an exact computation.

## 3. Axis versus angle: "neighbouring blocks turn about different axes" already holds in the free limit

Written 2026-11-20T14:41Z (date -u). Hand computation; no numeric run in this section.

**Setting.** Two closed lattice loops B, C (for instance the boundaries of two b x b squares), based at x_B and x_C,
and a lattice path P from x_B to x_C. H_B, H_C are the based holonomies; H'_C = P H_C P^(-1). This is the
gauge-invariant comparison that check 1279 proposed (`gap-threeaxis-check-astra.md` L109: "the quantity
1 - (1/2) tr[H_B, P H_C P^(-1)] is gauge invariant and includes the sizes of the rotations"). Write a unit
quaternion as k = cos(theta/2) + sin(theta/2) n (rotation angle theta in [0, 2 pi], axis n in S^2) and
u(k) = Im k = sin(theta/2) n in R^3. Under a gauge transformation all of H_B, H'_C are conjugated by h_(x_B), so
u_B = u(H_B) and u'_C = u(H'_C) rotate together; |u_B|, |u'_C| and the angle phi between them are gauge invariant.

**Identity Q (PROVED; Lemma CC of row 1273 rewritten).** Q(B, C) := 1 - (1/2) tr [H_B, H'_C] satisfies

    Q(B, C) = 2 |u_B x u'_C|^2 = 2 sin^2(theta_B/2) sin^2(theta'_C/2) sin^2(phi).

*Proof.* Row 1273 Lemma CC (`gap-owner-threeaxis-opus.md` L126-142, HOLDS in check 1279) gives
(1/2) tr[k_1, k_2] = 1 - 2 |u x v|^2 with u, v the imaginary parts (its proof: <k_1 k_2, k_2 k_1> = 1 - 2 |u x v|^2),
and |u x v| = sin(theta_1/2) sin(theta_2/2) sin(phi). QED

So the statistic is a product of two **angle factors** sin^2(theta/2) (how far each block turns) and one **axis
factor** sin^2(phi) (how different the axes are). Row 1273's "role inversion" (L469-479) read a small Q at weak
coupling as alignment of axes; check 1279 refuted the deterministic step. The computation below shows that in the
weak-coupling (Gaussian) limit the axis factor is NOT small: Q is small only because the angles are.

**Model G (the Gaussian limit of weak coupling).** Three independent identically distributed copies a^1, a^2, a^3
of one centred Gaussian field on the links (any lattice free Maxwell field, in any gauge; only gauge-invariant
fluxes enter), and for each loop the R^3-valued flux Phi_B = (Phi_B^1, Phi_B^2, Phi_B^3), Phi_B^c = sum over the
links of B of the signed a^c_l (= the flux of da^c through any surface spanning B). At weak coupling g, with
U_l = exp(i g a_l . sigma / 2), u_B = (g/2) Phi_B + O(g^2) (Baker-Campbell-Hausdorff; the correction is of relative
order g times the square root of the number of links of B, so model G describes the regime g^2 |B| << 1). This
reduction is ARGUED (leading order); everything stated inside model G is PROVED.

Put s_B = Var(Phi_B^c), s_C = Var(Phi_C^c) (the same for c = 1, 2, 3), c_BC = Cov(Phi_B^c, Phi_C^c), and
rho = c_BC / (s_B s_C)^(1/2). Colour components are independent: Cov(Phi_B^c, Phi_C^d) = 0 for c != d.

**Proposition AX (PROVED in model G).**
(a) The axis n_B = Phi_B/|Phi_B| is uniform on S^2 and independent of |Phi_B|.
(b) E |Phi_B|^2 |Phi_C|^2 = s_B s_C (9 + 6 rho^2) and E (Phi_B . Phi_C)^2 = s_B s_C (3 + 12 rho^2), hence

    E |Phi_B x Phi_C|^2 = 6 s_B s_C (1 - rho^2).

(c) If the two axes were independent uniform directions, independent of the angles (same marginal laws of
Phi_B, Phi_C), E |Phi_B x Phi_C|^2 would be (2/3)(3 s_B)(3 s_C) = 6 s_B s_C. So in model G the axis alignment of B
and C is exactly rho^2: E|Phi_B x Phi_C|^2 = (1 - rho^2) times its value for independent axes. Equivalently the
weight-|Phi_B|^2|Phi_C|^2 mean of sin^2(phi) is (2/3)(1 - rho^2)/(1 + (2/3) rho^2), against 2/3 for independent
axes and 0 for aligned ones.
(d) It is positive unless Phi_B and Phi_C are almost surely proportional (|rho| = 1, Cauchy-Schwarz).

*Proof.* (a) Phi_B is a centred Gaussian vector in R^3 with covariance s_B I (independent identically distributed
components), so its law is rotation invariant; for such a law direction and norm are independent and the
direction is uniform. (b) For c != d the pairs (Phi_B^c, Phi_C^c) and (Phi_B^d, Phi_C^d) are independent. For a
centred bivariate normal (X, Y) with variances s_B, s_C and correlation rho, E X^2 Y^2 = s_B s_C (1 + 2 rho^2)
(Isserlis). Then E|Phi_B|^2|Phi_C|^2 = 3 s_B s_C (1 + 2 rho^2) + 6 s_B s_C and
E(Phi_B . Phi_C)^2 = sum over c, d of E[Phi_B^c Phi_C^c Phi_B^d Phi_C^d] = 3 s_B s_C (1 + 2 rho^2) + 6 c_BC^2.
Subtract, using |x x y|^2 = |x|^2 |y|^2 - (x . y)^2. (c) With independent uniform axes, E sin^2(phi) = 2/3 and
E|Phi|^2 = 3 s. (d) Cauchy-Schwarz. QED

**Corollary AX1 (PROVED in model G; the size of rho is GUIDE).** At leading order in g,
E Q(B, C) = (g^4/8) E|Phi_B x Phi_C|^2 = (3/4) g^4 s_B s_C (1 - rho^2). The commutator statistic is small at weak
coupling through the angle factors (g^2 s_B, g^2 s_C), not through the axes. For two equal coplanar b x b squares
sharing an edge, flux additivity gives 2 c_BC = Var(Phi_(B u C)) - s_B - s_C; with the leading perimeter law
(variance proportional to perimeter: 4b, 4b, 6b) this is rho = -1/4, so 1 - rho^2 = 15/16 and the weighted mean of
sin^2(phi) is about 0.60 against 2/3 (GUIDE: the perimeter law is the leading term only).

**Reading for the owner's picture.**
1. "Neighbouring pieces turn about different axes" holds already in the Gaussian limit, which is the free gluon:
   the axes of neighbouring blocks are nearly independent (alignment rho^2, about 1/16 for adjacent equal squares).
   The free limit is massless. So the axis part of the owner's picture is generic for pure SU(2) at weak coupling
   and carries no gap. This strengthens check 1279's refutation of row 1273's alignment step (L469-479) from a
   deterministic to a statistical statement: at weak coupling the axes are not aligned.
2. The commutator statistic is still selective against U(1)^3 (three free photons have the same fluxes, hence the
   same "axes", but commuting holonomies, so Q = 0 identically). Its selective content enters only through the
   angle factors, that is through how far the blocks turn.
3. How far the blocks turn. For raw block loops the angle variance g^2 s_B grows with the perimeter (UV noise), so
   large raw loops are randomized at every coupling, also in a Coulomb phase: raw angles are not selective either.
   For smeared block fluxes (smooth test surfaces at scale l) the tree-level variance is scale free in four
   dimensions and the scale dependence is the running coupling g(l)^2 (ARGUED, standard one-loop reading). So the
   only selective, scale-dependent part of "blocks turning" is that the turns become of order one when g(l) does,
   which is the band.
4. Adjoint-Higgs test (row 669 third test; row 1004 Lemma GG). In the Coulomb phase the block fluxes lie along the
   transported Higgs direction, so axes ARE aligned there (Q small through sin^2(phi)), while in pure SU(2) model G
   never aligns them. Axis alignment is thus a symptom of the massless Coulomb phase, but axis disorder is generic
   in pure SU(2) at every coupling: using it costs nothing and gives nothing selective against the free gluon.
   (This narrows check 1279's ruling on L506, which holds: the absence of axis order is not a usable premise.)

**Status of (TILE-dis) after Section 3.** Its axis half holds at weak coupling (model G) and is not selective; its
angle half is "smeared block turns of order one at the block scale", which is the band in another wording. Neither
half is an input of any tiling theorem on file (Section 2.2).

## 4. GUIDE run: the axis and angle factors in the free field and in the Wilson measure (not a proof step)

Written 2026-11-20T14:44Z (date -u). Script in a scratch folder outside the repository (plain numpy, `python3 -I`, `nice`, BLAS
threads 1, RSS guard 2 GB). A one-second self-test ran before the lock was taken (lock status was free); every
run below ran under `python3 scripts/lab_ops.py numeric-lock` (acquired 14:43:59Z, holder checked).

**Self-test (passed).** Quaternion product: associativity, norm and conjugation errors at most 3.3e-16; Identity Q
(1 - Re[a, b] = 2 |Im a x Im b|^2) on 1000 Haar pairs, error 8.9e-16; staple against a direct action change, equal
to 12 digits; heat-bath sampler mean of w_0 against the exact mean of sqrt(1 - w^2) e^(alpha w) at alpha = 0.3, 3,
20: within one standard error.

**Part 1, model G exactly (lattice free Maxwell field on the periodic 32^4 lattice, Feynman gauge; fluxes are
gauge invariant).** Flux variance s_B of a b x b square, correlation rho with the adjacent coplanar square, and
the axis factor A_G = (2/3)(1 - rho^2)/(1 + (2/3) rho^2) of Proposition AX (c); also for the square in a
perpendicular plane sharing one edge:

| b | s_B | rho (coplanar, shared edge) | A_G | rho (perpendicular planes, shared edge) | A_G |
|---|---|---|---|---|---|
| 1 | 0.50000 | -0.13775 | 0.6458 | +0.21556 | 0.6166 |
| 2 | 1.36930 | -0.18256 | 0.6304 | +0.23878 | 0.6056 |
| 3 | 2.30515 | -0.20120 | 0.6229 | +0.24442 | 0.6028 |
| 4 | 3.26136 | -0.21118 | 0.6185 | +0.24642 | 0.6018 |

(s_B = 1/2 at b = 1 is the exact equipartition value: three physical modes per site, six plaquettes per site.)
The coplanar rho tends to the perimeter-law value -1/4 of Corollary AX1 from above. In the free limit the axes of
neighbouring blocks are within 3 to 10 percent of independent (A_G against 2/3).

**Part 2 criteria, written before the Wilson runs.** Wilson SU(2) heat bath on the periodic 8^4 lattice, hot
start, beta in (2.3, 2.6, 4.0, 8.0), 200 thermalisation and 400 measurement sweeps, measurements every 4 sweeps,
adjacent coplanar b x b loops (b = 1, 2, 3) based at the shared corner, averaged over all sites and ordered planes.
- K1 (kill test of row 1273's "role inversion", L469-479: the commutator energy aligns the block axes at weak
  coupling): KILLED at GUIDE level if the axis factor A = E|u_B x u_C|^2 / E(|u_B|^2 |u_C|^2) is at least 0.5 at
  beta = 8 for b = 1, 2, 3. Alignment would give A well below 0.5.
- K2 (model G at weak coupling): at beta = 8, A within 0.03 of A_G (0.646, 0.630, 0.623) and
  rho_MC = E(u_B . u_C)/E|u_B|^2 within 0.03 of rho (-0.138, -0.183, -0.201).
- D (description, no pass or fail): the angle factor E|u_B|^2 against b and beta (Haar value 3/4).

**Part 2 results, beta = 8.0** (run 14:44:47Z-14:45:18Z, 49 ms per sweep, mean plaquette 0.90350; errors are
jackknife over 5 bins of 20 measurements, statistical only; appended 2026-11-20T14:45Z):

| b | angle factor E abs(u_B)^2 (Haar 0.75) | axis factor A (independent 0.6667) | rho_MC | E Q = 2 E abs(u_B x u_C)^2 |
|---|---|---|---|---|
| 1 | 0.1777 | 0.6522 +- 0.0002 | -0.1217 +- 0.0003 | 0.04156 |
| 2 | 0.3981 | 0.6498 +- 0.0002 | -0.1489 +- 0.0003 | 0.20805 |
| 3 | 0.5424 | 0.6532 +- 0.0001 | -0.1497 +- 0.0001 | 0.38726 |

- **K1: KILLED (GUIDE).** A is about 0.65 at beta = 8 for b = 1, 2, 3, far above 0.5: at weak coupling the axes of
  neighbouring block loops are nearly independent, as Proposition AX says. Row 1273's role inversion (L469-479)
  fails in the Wilson measure, not only as an inference (check 1279).
- **K2: passed for A at b = 1 (0.652 against 0.646) and b = 2 (0.650 against 0.630); failed marginally for A at
  b = 3 (difference 0.0303 against the pre-set 0.03) and for rho at b = 2, 3 (differences 0.034, 0.051).** The
  departure is in the direction of MORE axis disorder. Reason, which I should have written into the criterion: model
  G is the regime g^2 |B| << 1 of small angles (Section 3), and at beta = 8 the angle factor is already 0.40 and
  0.54 at b = 2, 3; also Part 1 used 32^4 while Part 2 uses 8^4. A cleaner check (model G on 8^4, and beta = 32,
  128) is queued as Part 3.
- **D:** at fixed beta = 8 the raw angle factor grows with b (0.18, 0.40, 0.54 toward the Haar value 0.75): raw
  block loops are randomized by perimeter (ultraviolet) noise already at weak coupling, as Section 3 point 3 says.

**Part 2 results, all four couplings** (8^4, same protocol; batch 14:44:47Z-14:45:55Z by `date -u`; appended 2026-11-20T14:46Z).
Errors (jackknife, 5 bins) are 0.0001-0.0010 on every A and rho_MC entry and are omitted here.

| beta | mean plaquette | b | angle factor E abs(u_B)^2 (Haar 0.75) | axis factor A (independent 0.6667) | rho_MC |
|---|---|---|---|---|---|
| 8.0 | 0.9035 | 1 / 2 / 3 | 0.178 / 0.398 / 0.542 | 0.652 / 0.650 / 0.653 | -0.122 / -0.149 / -0.150 |
| 4.0 | 0.7995 | 1 / 2 / 3 | 0.336 / 0.616 / 0.712 | 0.659 / 0.661 / 0.665 | -0.101 / -0.104 / -0.079 |
| 2.6 | 0.6701 | 1 / 2 / 3 | 0.486 / 0.721 / 0.748 | 0.664 / 0.666 / 0.667 | -0.067 / -0.045 / -0.016 |
| 2.3 | 0.6017 | 1 / 2 / 3 | 0.545 / 0.741 / 0.750 | 0.666 / 0.667 / 0.667 | -0.041 / -0.015 / -0.001 |

**Reading (GUIDE).** Over the whole range from weak coupling (beta = 8) to the window (2.3-2.6) the axis factor
stays between 0.650 and 0.667: in the Wilson measure neighbouring block loops ALWAYS turn about nearly independent
axes. Only the angle factor moves (0.18 to 0.75), with b and with beta. So the owner's picture, "neighbouring
pieces turn about different axes", is a property of the Wilson SU(2) measure at every coupling tried, including
weak coupling, where the free limit is massless; what distinguishes the window is how far the blocks turn. The
weak-coupling check of the mean plaquette against the leading-order value 1 - 3/(4 beta) (0.906 at beta = 8) is
0.9035. These are raw (unsmeared) loops, whose angles also grow by perimeter noise (Section 3, point 3); the runs
do not separate that noise from confinement and are not meant to.

Part 3 (model G on 8^4; beta = 32 and 128, where model G should hold for b = 1, 2) waits for 50 percent free
memory: at 14:46Z `memory_pressure` read 40 percent free.

## 5. Two further attacks on the tiling question

Written 2026-11-20T14:48Z (date -u).

### 5.1 Attack 2: a tiling theorem whose input is a junction statistic. Stops at the first step.

**Target.** A theorem of the form: if at one block scale l some statistic of block holonomies (axis factors, angle
factors, Q of Section 3, possibly uniform over the outside) is in a stated range, then (N-phys) holds at some
L = N l. No theorem on file has this form (Section 2.2: all read one block's free energy).

**Fact test (PROVED; this is row 998 Lemma PT and row 1003 Proposition NP in the form needed here, and check
1279's spectator remark made exact).** Take the Wilson SU(2) measure and, independently on the same lattice, the
free Gaussian photon; the product is a lattice gauge theory with group SU(2) x R. Every statistic of SU(2) block
holonomies has the same law in the product. The product's positive transfer operator is the tensor product, so
its excited neutral sum satisfies 1 + s >= 1 + s_photon. For the photon on the periodic cube n^3 the twelve
one-photon states with lattice momentum (2 pi/n) e_i (six momenta, two polarisations) have transfer energy
omega = 2 arcsinh(sin(pi/n)) <= 2 pi/n (the lane's formula, `gap-lsij-scale-opus.md` L106), so at u = n/512,
s_photon >= 12 exp(-2 pi/512) > 11, and (N-phys) fails for the product at every n. So no theorem whose input
reads only statistics of SU(2) block holonomies can conclude (N-phys): its hypotheses must also read a property
of the whole state space that the product lacks.

**Within pure SU(2) (ARGUED).** The rigorous links from Wilson-loop statistics to free energies that I know, and
that are on file (Tomboulis and Yaffe, CMP 100 (1985), read through rows 1025 and 1029, `gap-cr-tomboulis-max.md`),
run between large Wilson loops and twisted (centre-flux) free energies: they connect the ANGLE half of (TILE-dis)
to the flux half of (W), one way. No inequality on file, and none I know, bounds the neutral thermal sum by block
holonomy statistics. Section 3 and Part 2 of Section 4 show the AXIS half is present at every coupling, so it
cannot be the missing input either. **First failing step:** an upper bound on the centre-neutral thermal sum in
terms of block-holonomy statistics at one scale. It must fail for the photon product (above), so it would have to
use pure-gauge dynamics beyond the statistics: a (K-one) input at the band, the wall again.

### 5.2 Attack 3: where the directional mechanism does enter a tiling: the block's vacuum energy, not its gap

**Remark RT (PROVED; the long-time variant of Theorem D (a) and Proposition R of row 697, by Lemma A (a) in the
three spatial directions).** Write Z(u, n_1, n_2, n_3) for the periodic Wilson torus with time side u, E_0(n) =
-log lambda_0(n) for the periodic cube n^3, and X_full(u; n) = Z(u, n, n, n)/lambda_0(n)^u = sum over electric
sectors q of X_(0,q)(u; n). Then for integers N >= 1:
(i) Z(u, N l, N l, N l) <= Z(u, l, l, l)^(N^3);
(ii) E_0(N l) >= N^3 E_0(l), so e(n) := E_0(n)/n^3 increases along multiples and e(l) <= e_inf := lim e(n);
(iii) X_(0,0)(u; N l) <= X_full(u; l)^(N^3) exp(u [E_0(N l) - N^3 E_0(l)]) <= X_full(u; l)^(N^3) exp(u N^3 D_l / l),
     with the zero-temperature Casimir defect D_l := l (l^3 e_inf - E_0(l)) >= 0.
*Proof.* (i) Z(u, Nl, n_2, n_3) = Tr T_1^(Nl) <= (Tr T_1^l)^N = Z(u, l, n_2, n_3)^N (Lemma A (a), `gap-crux-restate.md`
L37, with the positive trace-class spatial transfer operator of (TM), L33), then directions 2 and 3. (ii) (i) at
u = U, take U-th roots and U to infinity (Lemma A (a): (Tr F^U)^(1/U) tends to lambda_0). (iii) X_(0,0) <= X_full
(all sector traces are non-negative); divide (i) by lambda_0(N l)^u; then (ii). QED

**Consequence (PROVED from RT and Perron-Frobenius).** Fix a block (l, beta). The full gauge-invariant transfer
operator of the block has a strictly positive kernel, so its top eigenvalue is simple and its full gap
Delta_full(l) > 0 (all electric sectors included). Hence at u = N l/K, N^3 log X_full(u; l) <=
N^3 exp(-(u - 3) Delta_full) (X_full(3; l) - 1) tends to 0 as N grows: in a long-time tiling every block's gap,
however small (a photon block's too), is carried for free. The binding factor is exp((N^4/K) D_l): a long-time
tiling needs a block whose zero-temperature vacuum energy is within about K log(3/2)/(N^4 l) of the bulk value,
that is D_l of order 10^(-13) at the size (N-phys) asks for (N l m about 10^4 with l m about 30). For a massive
theory D_l is exponentially small in l m (GUIDE); for any theory with a massless particle D_l stays of order one.

**Lemma E0 (PROVED in the reduced model of row 1273).** For n >= 2 colour vectors, the ground energy of
K_n = -(1/2) Delta + (1/2) sum over i < j of abs(y_i x y_j)^2 on L^2(R^(3n)) satisfies

    n e_A (4/27)^(1/3) s_n^(2/3) <= E_0(K_n) <= (9n/8) (n - 1)^(1/3),

with e_A = 2^(-1/3) abs(a_1) = 1.85576 (a_1 = -2.33811 the first zero of the Airy function) and
s_n = ((n - 1)/2)^(1/2). For n = 3: 2.946 <= E_0(K_3) <= 4.252; n = 2: 1.559 <= E_0 <= 2.250.
*Proof.* Lower: K_n >= -(1/2) Delta (V >= 0) and K_n >= s_n W, W = sum_i abs(y_i) (Lemma S_n, HOLDS in check 1279).
For t in [0, 1], K_n >= t(-(1/2) Delta) + (1 - t) s_n W = sum_i [-(t/2) Delta_(y_i) + c abs(y_i)], c = (1 - t) s_n,
a sum of operators in separate variables. With y = lambda z, lambda^3 = t/c, the operator -(t/2) Delta + c abs(y)
on R^3 equals t^(1/3) c^(2/3) (-(1/2) Delta_z + abs(z)), whose ground energy is e_A: the l = 0 radial equation
-(1/2) w'' + r w = E w, w(0) = 0, is solved by w = Ai(2^(1/3)(r - E)), so E = 2^(-1/3) abs(a_1); l >= 1 adds a
non-negative centrifugal term. Maximise t^(1/3)(1 - t)^(2/3) at t = 1/3. Upper: the trial state
exp(-a abs(y)^2/2) (colour invariant) gives kinetic energy 3na/4 and, with y_i independent N(0, I/(2a)),
E abs(y_i x y_j)^2 = 6 (2a)^(-2), so <K_n> = 3na/4 + 3n(n-1)/(8a^2); at a = (n-1)^(1/3) this is (9n/8)(n-1)^(1/3). QED

**Reading (GUIDE: tree level, small block; the Casimir constant is RECALLED).** For a massless scalar on a periodic
cube of side l the Casimir energy is -(1/(2 pi^2 l)) times the lattice sum over nonzero m in Z^3 of abs(m)^(-4)
(about 16.5323, RECALLED), that is -0.8375/l. The six nonzero-momentum gluon degrees of freedom of SU(2) give
-5.025/l, the same as three free photons (U(1)^3). The zero modes add +E_0(K_3) g(l)^(2/3)/l for SU(2) (Lemma E0:
coefficient in [2.95, 4.25]) and 0 for U(1)^3 (free rotors). So, at tree level,

    D_l(SU(2)) = 5.025 - eps_0 g(l)^(2/3) + ...,   D_l(U(1)^3) = 5.025 at every l,   eps_0 in [2.95, 4.25].

The directional zero-point energy is the selective term of the quantity a long-time tiling needs, and it has the
helpful sign: it pulls the block's vacuum energy toward the bulk value. Since D_l >= 0 is exact (RT (ii)), the
expansion must fail before g(l)^(2/3) reaches 5.025/eps_0, between 1.18 and 1.70 (g(l)^2 between 1.3 and 2.2).
This is where the owner's idea really meets a tiling: through the block's ground-state energy, at intermediate
block size. It is a pointer, not a route: RT needs D_l near 10^(-13), which no small-volume cancellation can give;
only the exponential decay of D_l in a massive phase reaches it. The Euclidean seed of the engine (symmetric
torus, temperature 1/l) sees the opposite sign: there the many low zero-mode levels make Delta grow like
log(1/g) (Section 2.3, row 720). Both statements are consistent; they are different quantities.
