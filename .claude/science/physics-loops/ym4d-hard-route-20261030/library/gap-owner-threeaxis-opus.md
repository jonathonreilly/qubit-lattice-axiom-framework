lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T00:27Z

# gap-owner-threeaxis-opus: multi-direction plaquette blocks and the SU(2) mass gap

Row 1273 of FINISH.md. Started 2026-11-20T12:27Z (date -u) at commit 49bbe938f on branch claude/ym4d-hard-route.
Worker: Claude Opus 5.5, max effort, Mac mini worker 2. Research-stage working state; no claim of status.

Labels: PROVED (written argument, checkable by hand), ARGUED (argument with a named gap), GUIDE (heuristic or numeric guide, never a proof step), OPEN.

## Step 0. Save protocol

File created first, per the row. Sections are appended one step at a time.

## Step 1. Repo search (rule 0a) and plan

Read for this step, at 49bbe938f: `GOAL.md` in full; `FINISH.md` L1-84, L299-351, row 1273 (this item) and the
RESULT parts of rows 930-934, 1011, 1141, 1188, 1200, 1201, 1228, 1249, 1256, 1260; `parts/gap.md` L1-104;
`library/gap-mini-neutral-fable.md` L55-135 ((N-phys) and what is on file about it).

Grep of `library/*.md`, `parts/*.md` and `FINISH.md` for the owner's idea and its neighbours (several wordings:
multi-direction, several directions, different axes, non-commuting rotation/twist, Fact T, three-axis, femto,
Luscher, van Baal, commutator potential, quartic valley). `library/open-core.md` has no line on rotations, twists
or commutators of blocks. Matches, each read at the cited lines:

| On file | Where | What it says | Bearing on this item |
|---|---|---|---|
| Fact T | `gap-crux-restate.md` L53; `gap-crux-exercise4-max.md` L210, L283 | -1 is the group commutator of i sigma_1 and i sigma_2; the single-plane central twist has classical cost zero for SU(2) | the commutator of two perpendicular half-turns is central: flux half only. Q_8 shares it (check of row 1003, L251-305), so it is not selective for the flux half |
| Crossed twists, torons | rows 930-938; row 1200 Lemma M (`gap-mini-solve-j-fable.md`) | minimum action in the crossed-twist sector; abelian family A_perp(L) = 2 L^4 (1 - cos(pi/L^2)) | a commutator held at a central value: flux half |
| OpenAI O(n) annulus engine | `gap-direction3-max.md` L190-197 (row 1007 B(2)) | "an additive gradient of non-commuting rotations is gauge equivalent to a commutator field"; commutators of plane waves on frequency shells add coherently to the twist while costs add incoherently | this is the owner's idea in 2D, for a twist (flux-type) quantity |
| Port of that engine | row 1046 Lemma TAN; row 1188 Lemma PC (`gap-mini-solve-a-fable.md`); row 1228 Prop P5 | identity holds on the pin space; cost of a commutator profile on a 3D slice is at least lambda^2 eta^2 N; plate twists squeeze under tiling | the commutator-as-twist mechanism has no 4D gain |
| Rigid symmetries | row 1016 Lemma CEN+ (`gap-pinned-cell-gauge-check-astra.md` L52-96 corrects CEN) | every trace-preserving family of single-link maps is a gauge transformation times a closed Z_2 field | block rotations that preserve the weight are gauge times central |
| Box symmetry group | row 1201 (`gap-mini-solve-k-fable.md`) | spatial rotations as a rigid non-abelian group; no stiffness | the spatial reading of the dream |
| Several directions kill association | `gap-face-stability.md` L308; `gap-face-exercise-fable.md` L934 | OpenAI's (3.6) and the Ginibre step fail for a sheet with pins of several directions | multi-direction pins are an obstruction for the neutral half by association |
| K_3 commutator frustration | row 1241 (`gap-mini-solve-y-opus.md`) | at Gaussian order K_3 is massless; the commutator frustration is cubic, not a decay mechanism | one neutral commutator route closed |
| Small-volume neutral gap | row 998 I33 (`gap-crux-exercise3-max.md` L218); row 1003 item 14; `gap-brainstorm-max.md` idea 36; `gap-council-rg-fable.md` L209; `gap-council-conf-fable.md` L159 | Luscher (1983), van Baal: in a small periodic box the zero-flux gap is about 4.1167 g^(2/3)/L; held as BELIEF; "z tends to 0 at small L" | the commutator potential of the constant modes is the neutral-half mechanism at small volume; it is on file only as a recalled belief, not as a lattice lemma |

Not found on file: (i) a literal multi-direction block with its gauge-invariant content worked out; (ii) the
question whether non-central commutators act inside the neutral sector; (iii) a hand proof that the commutator
potential of the constant modes, and not the twist, is what U(1) lacks in the neutral half.

**Plan (at most eight steps).**
1. This search (done).
2. Literal model: what a multi-direction block (MDB) is on the lattice; which of its data are gauge invariant
   (junction invariants). Elementary lemmas, PROVED or killed.
3. The commutator question as operators on the transfer-matrix space: do MDB operators and their commutators
   act inside the neutral sector, and how does that differ from the centre twists? PROVED or killed.
4. The commutator question as energy: the commutator (quartic) energy of an MDB, its dichotomy (central
   commutator = flux sector; non-central = curvature), its scaling with block size, and the fact tests (U(1),
   frozen Q_8 and 2T, products with a free photon).
5. The neutral mechanism at one block: a hand-provable reduced (Simon-type) lemma that the commutator potential
   gives a discrete spectrum and a gap on the neutral constant modes; what it does and does not give on the
   lattice.
6. Tiling: can a tiling of MDBs carry the one-block mechanism to the size that (N-phys) needs? Attack it as a
   real proof; name the first failing step.
7. Two further distinct attacks on that failing step, if the first fails.
8. Verdict and RESULT line.

**Moves (rule 0):** (N-phys), the neutral half of the gap clause (rows 1161, 1179, 1180). If the MDB commutators
give a selective neutral engine that crosses the band, (N-phys) moves; if they provably act only at small volume or
reduce to the block RG through the band, that closes the owner's idea as a route and says why.

## Step 2. The literal model: what a multi-direction block is, and what of it is gauge invariant

Written by 2026-11-20T12:40Z (date -u, taken after the step was appended). No numeric run.

**Setting.** A finite lattice Lambda (a torus or a box) in Z^d, d = 3 (a time slice) or 4. Oriented links l from
s(l) to t(l), U_l in SU(2), U_(l^-1) = U_l^-1. Plaquette holonomy U_p = U_1 U_2 U_3^-1 U_4^-1 from a base corner.
Wilson weight W(U) = exp(sum_p (beta/2) tr U_p). Gauge group G = SU(2)^(sites), (U^h)_l = h_(s(l)) U_l h_(t(l))^-1.
Every observable below is gauge invariant unless said otherwise. Quaternion notation: a unit quaternion
k = cos(theta/2) + sin(theta/2) n, n a unit pure quaternion (the axis), theta in [0, 2 pi] (the angle).

**Link-end rotation families.** Give each link l a pair (a_l, b_l) in SU(2) x SU(2) and put
(phi U)_l = a_l U_l b_l^-1. The element a_l sits at the link-end (l, s(l)), b_l at (l, t(l)); call it the germ of
that link-end. Write c_(x,e) for the germ at the link-end e at site x (2d link-ends per site). phi keeps the Haar
measure of every link. A gauge transformation h is the family with every germ at x equal to h_x.

**Three readings of "sub-block B_k turns about its axis n_k by the angle theta_k"** (g_k = cos(theta_k/2) +
sin(theta_k/2) n_k; the sub-blocks B_1, ..., B_m are disjoint sets of sites):

- (R1) site rotation: h_x = g_k for x in B_k, h_x = 1 elsewhere.
- (R2) internal rotation: U_l -> g_k U_l g_k^-1 for every link with both ends in B_k; every other link unchanged.
- (R3) direction-dependent rotation: the links of lattice direction mu turn about their own axis, a_l = g_mu on the
  links of direction mu in a region, b_l = 1. This is the reading in which "a cube turns about the axis towards the
  viewer, a second about the vertical, a third about the horizontal" can mean the three lattice directions.

### Lemma J (junction invariants). PROVED.

For gauge-invariant F, E_W[F o phi] depends on phi only through the following data, one per site: the
simultaneous conjugacy class of the tuple (k_(x,e))_(e != e_0), where k_(x,e) = c_(x,e_0)^-1 c_(x,e) are the
relative rotations of the link-ends at x (e_0 is any fixed link-end at x; another choice gives an equivalent tuple).

*Proof.* For gauge transformations h, h': (h o phi o h')_l (U) = h_(s) a_l h'_(s) U_l (h_(t) b_l h'_(t))^-1, with
s = s(l), t = t(l). So each germ at x changes as c_(x,e) -> h_x c_(x,e) h'_x, with one pair (h_x, h'_x) for all
link-ends at x, independently from site to site. Gauge invariance of F gives F o h = F; gauge invariance of W and
of Haar measure gives E[G o h'] = E[G] for every G. Hence E[F o (h o phi o h')] = E[F o phi]. The orbit of a germ
tuple under c_e -> h c_e h' is fixed by the conjugacy class, under k -> h'^-1 k h', of the tuple
k_e = c_(e_0)^-1 c_e: given two tuples with simultaneously conjugate k's, k'_e = r^-1 k_e r, take h' = r and
h = c'_(e_0) r^-1 c_(e_0)^-1; then h c_e h' = c'_(e_0) r^-1 k_e r = c'_(e_0) k'_e = c'_e. QED

Credit: the per-site structure is the corner graph of row 1013 Lemma WN (`gap-invent-selective-max.md` L136-166:
"vertices are link-ends, edges are corners ... a disjoint union of one copy ... per site"), there for one axis. Lemma
J is its several-axis form at the level of the full group, not of the Lie algebra.

### Lemma DR (the directions of a multi-direction block are pure gauge). PROVED.

In reading (R1) every relative rotation is 1, so E[F o phi] = E[F]. In reading (R2), for every gauge-invariant F,
E[F o R2(g_1, ..., g_m)] = E[F o R2(g'_1, ..., g'_m)] whenever each g'_k is conjugate to g_k. In particular the
axes n_k can all be replaced by one common axis, keeping the angles theta_k: every multi-direction block in reading
(R2) has the same expectations as a block in which all sub-blocks turn about the same axis, so all its rotations
commute.

*Proof.* (R1): phi = h is a gauge transformation. (R2): at a site x of B_k every germ is g_k (link-ends of links
inside B_k) or 1 (link-ends of links that leave B_k, including links to another sub-block). So every relative
rotation lies in {1, g_k, g_k^-1}, and the tuple's simultaneous class depends only on the class of g_k. Lemma J
ends the proof. Explicitly: with r_k g_k r_k^-1 = g'_k and the gauge transformation h_x = r_k on B_k,
h o R2(g) o h^-1 = R2(g'). QED

**Consequence.** Taken literally (pieces of the lattice, each turned about its own axis), the owner's block carries
no directional information: the commutators of its rotations are invisible to every gauge-invariant quantity. This
extends item 1 of row 1013 Proposition LOC ("Its commutators are gauge transformations ... No signal") from the
gauge group to the internal rotations (R2), which are not gauge transformations and do change the action, but whose
axes are gauge. Directional content needs a site at which two link-ends carry relative rotations that do not
commute: a junction.

### Lemma CC (which junctions are central). PROVED.

For unit quaternions k_i = cos(theta_i/2) + sin(theta_i/2) n_i (i = 1, 2) with angle phi between the axes,

  (1/2) tr [k_1, k_2] = 1 - 2 sin^2(theta_1/2) sin^2(theta_2/2) sin^2(phi),

where [k_1, k_2] = k_1 k_2 k_1^-1 k_2^-1. So [k_1, k_2] is central (+1 or -1) if and only if k_1 and k_2 commute, or
both are half-turns (theta_1 = theta_2 = pi) about perpendicular axes, in which case [k_1, k_2] = -1.

*Proof.* Write k_1 = a + u, k_2 = b + v with a, b real, u, v pure. The real part of a product of unit quaternions
is unchanged by cyclic order, so Re(k_1 k_2 k_1^-1 k_2^-1) = Re((k_1 k_2)(k_2 k_1)^-1) = <k_1 k_2, k_2 k_1>, the
Euclidean inner product in R^4 (for unit q, r: Re(q r^-1) = <q, r>). Now k_1 k_2 = ab - u.v + a v + b u + u x v and
k_2 k_1 = the same with -u x v. So <k_1 k_2, k_2 k_1> = |k_1 k_2|^2 - 2 |u x v|^2 = 1 - 2 |u x v|^2, and
|u x v| = sin(theta_1/2) sin(theta_2/2) sin(phi). The commutator is +1 iff u x v = 0 (commuting), and -1 iff
|u x v| = 1, that is sin(theta_1/2) = sin(theta_2/2) = sin(phi) = 1. Fricke's identity
tr[k_1, k_2] = x^2 + y^2 + z^2 - xyz - 2 (x = tr k_1, y = tr k_2, z = tr k_1 k_2) is the same fact in the
invariants of Lemma J. QED

**Corollary CC1 (the dream at half-turns is the flux half, on file).** In reading (R3) on a 3-torus, the constant
field U = i sigma_i on every link of direction i has every (i, j) plaquette equal to [i sigma_i, i sigma_j] = -1: in
the untwisted theory the constant three-axis half-turn field has the largest Wilson action there is. The flat form
puts each half-turn on one Dirac sheet: U = i sigma_i on the i-links of one slice x_i = 0, U = 1 on all other links
(the toron of `gap-council-geom-fable.md` L28, there for two directions). The cycle holonomies are i sigma_1,
i sigma_2, i sigma_3, pairwise anticommuting; every plaquette is +1 except the (i, j) plaquettes at
(x_i, x_j) = (0, 0), which are -1. With 't Hooft's twist in all three planes (those plaquettes enter the action
multiplied by -1) the field is flat: it is the flat connection of the twisted 3-torus with m = (1, 1, 1), isolated,
with no zero modes. This is Fact T (`gap-crux-restate.md` L53) in all three planes, and the twisted box of Route T
(rows 678-687, `gap-ac-lat.md`; row 1003 item 14: "in a twisted box no zero modes and a gap of order 1/L"). It
reaches the flux half only, and the frozen group Q_8 = {+-1, +-i sigma_k} has it too (check of row 1003,
`gap-crux-exercise4-check-opus.md` L251-305), so it is not selective for the flux half either.

**Corollary CC2 (every other non-commuting junction is curvature).** If the relative rotations at a junction do
not commute and are not perpendicular half-turns, their commutator is non-central. It is not a symmetry (row 1016
Lemma CEN+: weight-preserving single-link maps are gauge times a closed Z_2 field), and a plaquette whose corner
carries it has holonomy changed by a non-central factor. So outside the half-turn case the owner's directional
content is curvature with an energy, not a sector label.

**What Step 2 settles.** The owner's block, read literally, has three outcomes: pure gauge ((R1), and the axes in
(R2)); flux sectors (perpendicular half-turns at junctions, Corollary CC1, on file); curvature (all other junctions,
Corollary CC2). Only the third can be new, and only it can reach the neutral half. Steps 3-4 test it.

**Literature identification (RECALLED, not re-read; not on file by grep for Savvidy, Copenhagen, spaghetti,
domain model, Leutwyler, Nedelko).** A tiling of domains whose fields point along different colour axes is the
"Copenhagen" or "spaghetti" vacuum of Nielsen and Olesen (1979) and Ambjorn and Olesen (1980), built on Savvidy's
(1977) one-loop instability of a constant chromomagnetic field, and the domain model of Kalloniatis and Nedelko
(from 2001), with (anti-)self-dual covariantly constant fields of random colour axis in each domain, after
Leutwyler (1980-81). These are physics models, not proofs. The lane has the Nielsen-Olesen unstable mode only
(`gap-brainstorm-max.md` idea 11, L290; scored F: "no step from saddle to free energy", L533).

## Step 3. The commutator question as operators: what reaches the neutral sector

**Setting.** The time-slice space H = L^2(SU(2)^(links of a 3-torus)), the gauge action (V_h psi)(U) = psi(U^h), the
projection P = integral of V_h dh onto the gauge-invariant space H^G, and the electric-flux sectors
H^G = (+) over e in Z_2^3 of H_e (eigenvalues of the centre twists Omega_i below). For a family g = (g_l) on a link
set S put (L_g psi)(U) = psi(U') with U'_l = g_l^-1 U_l on S and U'_l = U_l off S (a left rotation at the start of
each link of S; right rotations at the end are the same with t(l) for s(l)). In the Peter-Weyl basis, L_g acts on
the start index of the spin-j_l matrix coefficient of U_l by D^(j_l)(g_l).

### Proposition PT (rotations at separate sites commute after projection). PROVED.

If the start sites s(l), l in S, are pairwise distinct, then on H^G

  P L_g P = prod over l in S of C_l(g_l),   C(g) = integral of L_(k^-1 g k) dk,

and C_l(g) acts on the spin-j part of the variable U_l as the number chi_j(g)/(2j + 1), chi_j the character. So
these operators are functions of the link Casimirs. They commute with each other for all choices of axes and angles,
with P, and with the electric factor of the transfer operator (also a function of the link Casimirs: the
convolution by the central weight exp((beta/2) tr g)). All axes and all commutators [g_l, g'_l] drop out.

*Proof.* For gauge-invariant psi: (g^-1 U^h)_l = g_l^-1 h_s U_l h_t^-1 = h_s (h_s^-1 g_l h_s)^-1 U_l h_t^-1, so
(L_g psi)(U^h) = psi(((g^h)^-1 U)^h) = (L_(g^h) psi)(U) with (g^h)_l = h_(s(l))^-1 g_l h_(s(l)). Hence
P L_g psi = integral of L_(g^h) psi dh. With distinct start sites, the h_(s(l)) are independent and Haar, so the
integral factors into prod_l C_l(g_l). C(g) is the convolution with the normalized measure on the conjugacy class of
g, a central measure; by Schur's lemma its Fourier coefficient on spin j is integral of D^j(k^-1 g^-1 k) dk =
(chi_j(g^-1)/(2j+1)) I = (chi_j(g)/(2j+1)) I (SU(2) characters are real). A central convolution commutes with left
and right translations, hence with V_h and P, and with every other function of the link Casimirs. QED

### Corollary PT1 (centre twists see the flux label only; other twists act inside the neutral sector, as in U(1)). PROVED.

(a) For g = -1 on the links that cross one plane x_i = const, C(-1) = (-1)^(2 j_l) exactly (no average is needed),
and Omega_i = prod over crossing l of (-1)^(2 j_l) is the 't Hooft electric-flux operator: on H_e it is the number
(-1)^(e_i). So a centre twist acts on each flux sector as a scalar; on the neutral sector H_0 it is the identity.
(b) For non-central g, prod_l chi_(j_l)(g)/(2 j_l + 1) is not a scalar on H_0 (it separates the spin content of the
crossing links). So non-central twists act inside the neutral half. (c) This is not selective. For compact U(1) the
same construction gives prod_l exp(i n_l theta_l) (n_l the electric charge of the link), which acts inside the U(1)
neutral sector in the same way.

*Proof.* (a) -1 is central, so L_(-1) = C(-1), and on the charge-j coefficient it multiplies by (-1)^(2j). The
operator Omega_i is the twisted gauge transformation that is 1 off the crossing links (the standard definition of
the electric-flux sectors). (b) Take two states in H_0 that differ only by the spin of one crossing link, j = 0
against j = 1 on a closed spin network; the multipliers are 1 and chi_1(g)/3 = (1 + 2 cos theta)/3, different
unless theta = 0. (c) Direct. QED

### Proposition PT2 (where the commutators survive: junctions, on intertwiners). PROVED.

Let several link-ends at one site x be rotated. On H^G the site factor of P L_g P is the compression of the
operator (x) over e at x of D^(j_e)(g_e) (g_e = 1 on ends not rotated) to the intertwiner space
Inv_x = Inv((x)_e V_(j_e)). (a) If all rotated ends at x carry the same germ g and the rotated set is A, the
operator is sum over J of (chi_J(g)/(2J + 1)) Pi_J^(A), with Pi_J^(A) the projection on total spin J of the ends in A:
a function of the coupled spin of A. (b) Rotations at one site on two different sets A, B do not commute in general,
even with one common axis. Example: four spin-1/2 ends at x, so dim Inv_x = 2, with basis vectors the pairings
(12)(34) and (13)(24); A = {1, 2}, B = {1, 3}, g non-central. The two operators are c_0 Q_A + c_1 (1 - Q_A) and
c_0 Q_B + c_1 (1 - Q_B), with Q_A, Q_B the rank-one projections on the two pairings and c_0 = 1 != c_1 =
chi_1(g)/3 (on Inv_x the A-pair has total spin 0 or 1); the two pairing vectors have overlap 1/2 in absolute
value, so Q_A Q_B != Q_B Q_A. (c) For compact U(1) every Inv_x is one-dimensional (charge conservation), so every
projected rotation at a site is a scalar and all of them commute.

*Proof.* The factorization over sites is the proof of PT with the joint average at x over one h_x. Compression of
the twirl to Inv_x equals compression of the operator itself, since the twirl is the average of conjugates by an
action that fixes Inv_x pointwise. (a) With one germ, (x)_(e in A) D^(j_e)(g) is the total-spin representation of
A at g; its twirl is sum_J (chi_J(g)/(2J+1)) Pi_J^(A) (Schur on each isotypic part). (b) On Inv_x of four spin-1/2
ends, total spin of {1, 2} is 0 on (12)(34) and 1 on its orthogonal complement in Inv_x; c_0 = chi_0/1 = 1 and
c_1 = chi_1(g)/3 = (1 + 2 cos theta)/3 < 1 for theta != 0. Two rank-one projections with overlap strictly between 0
and 1 do not commute. The overlap of the two pairing singlets is 1/2 in absolute value (standard recoupling: the
6j-symbol for four spins 1/2). (c) Direct. QED

**What Step 3 settles (PROVED, elementary).** After the gauge projection that defines the physical space:

1. Rotations whose rotated link-ends sit at distinct sites, with any axes, commute (PT). The owner's commutators
   vanish identically there.
2. Centre twists see only the flux label (PT1 (a)); non-central twists act inside the neutral half, but so do the
   U(1) phase twists (PT1 (c)). Acting inside H_0 is not selective.
3. The non-abelian residue lives on the intertwiner spaces at junction sites (PT2), which U(1) lacks. Several axes
   are not needed for it: one axis on two different groupings of link-ends already fails to commute (PT2 (b)).

So the precise form of "the commutators reach the neutral half" is: the projected rotations generate, at each
junction, non-commuting operators on the intertwiner space of the neutral sector. This is kinematics. It says where
a selective neutral engine would have to act (the recoupling degrees of freedom), not that one exists. Related on
file: the commutator kick with multiplier (2j+1)^(-2) and its U(1) failure (row 1132, `gap-council-op-astra.md`
L37, with rows 778-805 as "the commutator mechanism was already tried", L98); the spin-network form and squared-6j
matrix of row 1076 (`gap-descent-sign-2.md` L193). Credit: Kogut and Susskind (Hamiltonian lattice gauge theory);
spin networks and recoupling (Penrose; Baez 1996), RECALLED.

## Step 4. The commutator question as energy: a lower bound for every field, and the fact tests

Distance on SU(2): d(k, 1) = arccos((1/2) tr k) in [0, pi], the angle of k on S^3. It is bi-invariant, so
d(a b, 1) <= d(a, 1) + d(b, 1) and d(r a r^-1, 1) = d(a, 1); and 1 - (1/2) tr U = 1 - cos d(U, 1).

### Lemma CE (the commutator of slice holonomies bounds the Wilson action of every field). PROVED.

Let T be a periodic plane slice with L_1 x L_2 plaquettes, and h_1, h_2 the holonomies of the two straight cycles
through one site x_0. Put delta = d([h_1, h_2], 1). Then for every field on T

  sum over p in T of (1 - (1/2) tr U_p) >= (2/pi^2) delta^2 / (L_1 L_2).

On a 4-torus of side L, summing over the L^2 parallel slices of each of the six plane orientations,

  S_W(U) / beta >= (2/pi^2) (1/L^2) sum over slices s of delta_s^2,

so if every slice has delta_s >= delta, then S_W >= (12/pi^2) beta delta^2, independent of L.

*Proof.* Cut T along the two cycles through x_0 into the rectangle R = [0, L_1] x [0, L_2] of Z^2, with the link
variables of T. The boundary of R, read from x_0, is the word h_1 h_2 h_1^-1 h_2^-1. Lattice Stokes for a disc:
the boundary holonomy of R is an ordered product of the L_1 L_2 plaquette holonomies of R, each conjugated by the
holonomy of a path (a lasso) from x_0 (induction on the number of plaquettes, removing one boundary plaquette at a
time). With the bi-invariant triangle inequality, delta <= sum_p d_p, d_p = d(U_p, 1). On [0, pi],
1 - cos t >= 2 t^2 / pi^2 (the ratio (1 - cos t)/t^2 decreases on (0, pi], with value 2/pi^2 at pi). With
Cauchy-Schwarz, sum_p (1 - cos d_p) >= (2/pi^2) sum_p d_p^2 >= (2/pi^2) (sum_p d_p)^2 / (L_1 L_2). The 4D form sums
L^2 slices per orientation, six orientations. QED

**Not new (found in the final rule-0a grep).** Lemma CE is the untwisted case of the peeling identity and norm bound
checked in row 791 (`gap-ext-check-opus.md` L62-66: "its boundary word is [g_mu, g_nu] ... standard non-abelian
Stokes, lasso form"; ||[g_mu, g_nu] - (-1)^k I|| <= sum_j ||eta_j U_(p_j) - I||; ||I - V||^2 = 2(1 - tr V/2)), from
rows 783 and 788 (`gap-cf-check-opus.md` L18), after Balaban CMP 99 Lemma 1 (row 1038 Lemma LAD,
`gap-collapse-frame.md` 4.2). Their norm form gives the sharper constant: the slice action is at least
2 sin^2(delta/2) / (L_1 L_2), which is at least (2/pi^2) delta^2 / (L_1 L_2).

**Small angles (reading of Lemma CC with CE).** For slice holonomies turning by angles theta_1, theta_2 about axes
at angle phi, Lemma CC gives delta = arccos(1 - 2 s^2) >= 2 s with s = sin(theta_1/2) sin(theta_2/2) sin(phi)
(arccos(1 - 2s^2) = 2 arcsin s). So the cost is at least (8/pi^2) beta s^2 per slice orientation in 4D, about
(1/(2 pi^2)) beta theta_1^2 theta_2^2 sin^2(phi) for small angles (s about theta_1 theta_2 sin(phi)/4): quartic in the angles, zero when the axes agree. This is the lattice
form, valid for every field and not only constant ones, of the quartic zero-mode potential |[c_i, c_j]|^2 / g^2 of
Luscher's small-volume Hamiltonian. It is scale free in four dimensions (classical scale invariance).

### Lemma SS (the directional property is semisimplicity). PROVED, elementary.

For a compact connected Lie group with Lie algebra g, the following are equivalent: every non-zero X in g has a
partner Y with [X, Y] != 0; the centre of g is zero; the group is semisimple. For su(2) = (R^3, x) it holds in the
uniform form |[X, Y]| = |X| |Y| sin(angle): ad_X restricted to the plane orthogonal to X is |X| times a quarter turn.
*Proof.* The first two are the definition of the centre. Zero centre for a compact Lie algebra is semisimplicity.
For su(2), [X, Y] corresponds to the cross product. QED

The owner's "neighbouring pieces turn about different axes" holds for every axis exactly when this property holds.
The uniform form (every transverse direction turns with the same rate |X|) is what Step 5 uses.

### Fact tests for "commutator energy" as a neutral ingredient (each PROVED from CE, CC, SS, or cited)

| Comparison | What CE and the commutator energy give | Verdict |
|---|---|---|
| Free photon, compact U(1) | delta = 0 for every field (abelian holonomies commute); the commutator energy is identically zero | fails, as a neutral engine must |
| SU(2) x U(1), and any product with a massless factor | the U(1) generator commutes with everything (SS fails); the U(1) zero modes and photons pay nothing | a statement that reads only commutator energy is bound by the product (row 998 Lemma PT, row 1003 Proposition NP) |
| Frozen Q_8, 2T | no continuous rotations; flat connections are isolated; commutators of flat holonomies are central (commutator subgroup of Q_8 is {+1, -1}), so CE costs nothing in the twisted sectors and gives no lifting of the finite degeneracy of commuting flat connections | the commutator energy does not lift the frozen degeneracy, as it must not (frozen groups are tests of even-sector tools, check 884) |
| Half-turn junctions (Corollary CC1) | the commutator is -1: zero cost in the matching twisted sector (Fact T) | flux half only, shared with Q_8 |

So the commutator energy passes the selectivity tests for the neutral half (it vanishes for U(1) and on central
factors, and does not lift frozen degeneracies). It is a classical, scale-free lower bound. The question is whether
it produces a gap in the quantum theory, and at which size. Step 5 does one block; Step 6 the tiling.

## Step 5. One block: the three-axis zero modes have a discrete spectrum (Simon's mechanism). PROVED for the reduced model.

**Reduced model.** On a small periodic spatial box the constant modes are three colour vectors y_1, y_2, y_3 in
su(2) = R^3, one per spatial direction: "three cubes turning about three axes". Their Hamiltonian at leading order
in the box coupling g (Luscher 1983, RECALLED; the reduction from the lattice is not done here) is
H_g = g^2 (-(1/2) Delta_c) + (1/(2 g^2)) V(c), in units of 1/L, with V(y) = sum over i < j of |y_i x y_j|^2.
Physical states are invariant under simultaneous colour rotation of (y_1, y_2, y_3) (Gauss's law for constant
modes). V vanishes exactly on the valley where all y_i are parallel, a cone of infinite volume, so classically the
motion is not confined.

### Lemma S. PROVED (B. Simon's method, 1983, adapted to three colour vectors).

Let K = -(1/2) Delta + (1/2) V on L^2(R^9) (Friedrichs extension from C_c^infinity).

(a) K >= |y_1| + |y_2| + |y_3| as quadratic forms.
(b) K has compact resolvent: its spectrum is discrete, E_0 < E_1 <= E_2 <= ..., tending to infinity.
(c) E_0 is simple, its eigenvector is positive and invariant under colour rotations; so on the gauge-invariant
    (rotation-invariant) subspace the gap kappa = E_1^inv - E_0 is at least E_1 - E_0 > 0.
(d) H_g is unitarily equivalent to g^(2/3) K. So the neutral constant-mode gap is kappa g^(2/3) / L.
(e) For one colour (U(1)) the same construction gives y_i in R, V = 0, K = -(1/2) Delta on R^3: no gap (on the
    compact holonomy torus of the lattice the gap is of order g^2 / L instead, the free rotor).

*Proof.* (a) Write K as the sum over the six ordered pairs (i, j), i != j, of K_ij = -(1/4) Delta_(y_j) +
(1/4) |y_i x y_j|^2. Each -Delta_(y_j) occurs twice with weight 1/4 and each |y_i x y_j|^2 (i < j) twice with weight
1/4, so the sum is K. Fix all variables except y_j. Then |y_i x y_j|^2 = y_j^T M y_j with M = |y_i|^2 (I - n n^T),
n = y_i / |y_i|, whose eigenvalues are |y_i|^2, |y_i|^2, 0. The operator -(1/2) Delta + (1/2) y^T M y on R^3 is two
harmonic oscillators of frequency |y_i| and one free direction, so it is at least |y_i|; hence K_ij, which is half
of it, is at least |y_i|/2 as an operator in y_j. By Fubini the same holds as forms on L^2(R^9). Summing,
K >= sum over ordered pairs of |y_i|/2 = sum_i |y_i| (each i is the first index of two pairs).
(b) V >= 0 gives K >= -(1/2) Delta. With (a), 2K >= -(1/2) Delta + W, W = sum_i |y_i|, and W tends to infinity at
infinity. The form domain of -(1/2) Delta + W embeds compactly in L^2 (Rellich: the unit ball of that form is
bounded in H^1 and uniformly small outside large balls). By min-max the n-th eigenvalue of K is at least half the
n-th eigenvalue of -(1/2) Delta + W, which tends to infinity; so K has compact resolvent.
(c) V is a polynomial, locally bounded, so exp(-tK) is positivity improving (Feynman-Kac); by the Perron-Frobenius
theorem for such semigroups (Reed and Simon, volume IV, chapter XIII; RECALLED) E_0 is simple with a positive eigenvector. K commutes with the
simultaneous rotation of the y_i (Delta and V are invariant), so the unique ground state is invariant. On the
invariant subspace the next eigenvalue is at least E_1 > E_0.
(d) The dilation c = g^(2/3) y maps g^2 (-(1/2) Delta_c) to g^(2/3) (-(1/2) Delta_y) and (1/(2g^2)) V(c) to
g^(2/3) (1/2) V(y), since V is homogeneous of degree 4. (e) Direct. QED

**What Lemma S says about the owner's question.** In one small periodic block the commutators of the three axes
reach the neutral half: they turn a classically unconfined valley into a discrete spectrum with a gauge-invariant
gap kappa g^(2/3)/L, parametrically larger than U(1)'s g^2/L. The mechanism is exactly the uniform form of Lemma SS:
along the valley (all axes parallel to n, size |y|), every transverse direction oscillates with frequency |y|, and
its zero-point energy confines the motion along the valley. This is the precise sense in which "the commutators,
which have no U(1) analogue, reach the neutral half". Credit: B. Simon, "Some quantum operators with discrete
spectrum but classically continuous spectrum", Ann. Phys. 146 (1983) 209 (method; RECALLED, not re-read);
M. Luscher, Nucl. Phys. B219 (1983) 233, and P. van Baal and J. Koller (the small-volume effective Hamiltonian;
RECALLED). **On file as a recalled statement, not as a written proof** (found in the final rule-0a grep): row 669
(`gap-skeleton-max.md` L76 and lesson (c) L81: "valleys closed by zero-point energy"); row 670
(`gap-skeleton-max-b.md` L105-110, (K4): "The operator -Delta + sum_{i<j} |c_i x c_j|^2 on R^9 still has discrete
spectrum", with Simon listed as "FROM MEMORY ONLY", L397); row 1158 (`gap-paths-fable.md` L105); row 998 I33;
row 1003 item 14; the virial ratio of row 1128 (`gap-council-rg-fable.md` L208-209). New here: the written hand
proof, the explicit bound K >= sum_i |y_i|, and Lemma S_n below.

**What it does not give (PROVED from (d)).** The dimensionless gap is z = kappa g(L)^(2/3), which tends to 0 as
L tends to 0. (N-phys) needs m L of order 10^4 at a fixed large physical size (`gap-mini-neutral-fable.md` 2.4).
Lemma S lives where g(L) is small, that is below the band; it does not cross it. This is the lane's standing
remark "z tends to 0 at small L" (row 998 I33), now with the mechanism proved in the reduced model. The lattice
reduction (Born-Oppenheimer control of the non-constant modes) is not done here and stays RECALLED.

### Lemma S_n (any number n >= 2 of directions; the owner's "2 or 4, not just 3"). PROVED.

For y_1, ..., y_n in R^3 and K_n = -(1/2) Delta + (1/2) sum over i < j of |y_i x y_j|^2 on L^2(R^(3n)):
K_n >= sqrt((n - 1)/2) (|y_1| + ... + |y_n|), so (b)-(d) of Lemma S hold for every n >= 2, with the same exponent
g^(2/3). For n = 1 the potential is zero and there is no confinement. *Proof.* Split K_n into the n(n - 1) ordered
pairs, K_ij = (1/(n-1)) (-(1/2) Delta_(y_j)) + (1/4) |y_i x y_j|^2. The operator -(a/2) Delta + (b/2) y^T M y with
a = 1/(n-1), b = 1/2 has two oscillator directions of frequency sqrt(ab) |y_i| and one free direction, so it is at
least sqrt(ab) |y_i| = |y_i| / sqrt(2(n-1)). Each i is the first index of n - 1 pairs. QED (n = 3 gives Lemma S (a).)

So the directional statement is exact at one block: two non-commuting directions are enough to confine the
zero modes, one is not. The number of pieces only changes the constant.

## Step 6. Tiling: can combinations of blocks carry the one-block mechanism to the size (N-phys) needs?

**Target of the step (TILE).** Tile a periodic box of side L = N l (lattice units n = L/a) by N^3 spatial blocks
of side l. (N-phys) at L would follow if the neutral low-energy states of the big box were controlled block by
block by a lift of the Lemma S type, with a constant that does not depend on N or on the cutoff. I attack (TILE) in
four ways. Each stops; the stopping points agree.

### Way A: a block form of Simon's inequality. KILLED (Lemma GA, PROVED).

Lemma S rests on K >= sum_i |y_i|: the transverse frequency grows with the amplitude of the constant mode. In a
block that is not periodic the constant mode is not gauge invariant.

**Lemma GA.** Let B be a block (a contractible set of sites), n an axis and lambda any real function on the sites
of B. The abelian field U_l = exp((lambda(t(l)) - lambda(s(l))) n) on the links of B has amplitude as large as one
likes, and is a gauge transformation of U = 1 (h_x = exp(-lambda(x) n)). So every gauge-invariant quantity on B
(every Wilson loop, the action, the spectrum of the covariant fluctuation operator) takes its value at U = 1.
Hence no inequality "transverse frequency >= local amplitude" holds on a block. *Proof.* (1^h)_l =
h_(s(l)) h_(t(l))^-1 = exp((lambda(t(l)) - lambda(s(l))) n). QED

On a contractible block the gauge-invariant content of an abelian field is its field strength; only the holonomies
of non-contractible loops of the whole torus play the role of the y_i. So a block lift must act on field strength.

### Way B: lift through the field strength. FAILS at weak coupling (RECALLED, physics; ON FILE as row 1193).

On file: row 1193 (`gap-mini-solve-d-fable.md` L82) screened "zero-point closing of flat valleys (Simon's x^2 y^2,
Luscher's toron Hamiltonian) as a volume-uniform operator inequality": "it bounds H below, not E_1 - E_0; in a
background field the spin term reverses the sign". Way B is that entry; the paragraph below only spells it out.

The block version of Lemma S's zero-point energy is the one-loop energy of the transverse (charged) modes in a
constant abelian field strength B along n. Savvidy (1977) computed it: at small B it is negative relative to B = 0
(the logarithm has the asymptotic-freedom sign), and Nielsen and Olesen (1978) found the charged spin-aligned mode
of the lowest Landau level unstable (energy squared -gB + k^2). So the transverse zero-point energy does not lift
the abelian valley in the field-strength direction; it lowers it (colour paramagnetism: Nielsen 1981, Hughes 1981;
on file in `gap-council-conf-fable.md` L159-160 and row 1244 `gap-mini-solve-aa-opus.md` L74, which cites row 1011 L496 and row 1195 (HM)). The sign that makes
Lemma S work (an orbital zero-point energy of holonomy-massive modes) is overturned by the spin term once the
background is curvature. Not attempted as a proof: it is a one-loop statement and a lower bound needs the opposite
sign.

### Way C: the tiling as a block renormalization step. REDUCES to the band (ARGUED, on file).

The blocks' holonomies are coarse link variables, and "neighbouring blocks turning about different axes" is the
coarse plaquette (Lemma CE at the coarse scale). The law of the coarse links is, to leading order, Wilson's at the
block coupling g(l) (Balaban's block-spin construction; Sussman and Alpoge's account carries it across all
ultraviolet scales). So (TILE) at block size l is the original problem for the coarse theory at coupling g(l). It
gains only if g(l) is past the band, which is the lane's wall (W) and (N-phys) (rows 998, 1161, 1179), and the
standing finding that the frontier statement (S-V) is again an RG step through the band (row 1249).

### Way D: domain models (random axes per block). The neutral directions are reached only at junctions.

The physics models built literally from "neighbouring pieces turn about different axes" are the domain models
(Step 2, literature identification). One structural fact explains where their neutral mass comes from.

**Lemma DOM (one axis is U(1) in its parallel directions). PROVED.** Let the background be abelian along one axis
n on a region: U_l = exp(alpha_l n). Write a fluctuation as U_l = exp(alpha_l n) exp(eps_l n + eps_l^perp),
eps_l^perp orthogonal to n. Then the second-order expansion of the Wilson action is block diagonal: its parallel
block is the compact-U(1) Hessian (beta/2) sum_p cos((d alpha)_p) ((d eps)_p)^2, and its transverse block carries
all the non-abelian structure; there are no mixed terms. *Proof.* With eps^perp = 0 all factors commute and
(1/2) tr U_p = cos((d alpha)_p + (d eps)_p), whose second-order term is the stated one. A mixed term is a sum of
(1/2) tr(B_0 (a n) B_1 X B_2) with B_i in the one-parameter group of n and X orthogonal to n. Since n commutes with
the B_i and B X B^-1 is again orthogonal to n, it equals (a/2) tr(n X' e^(psi n)) with X' orthogonal to n. As
quaternions, n X' = n x X' is pure and orthogonal to n, so tr(n X' cos psi) = 0 and tr(n X' n sin psi) = 0 (the
real part of (n x X') n is -<n x X', n> = 0). The first-order term in eps^perp vanishes the same way. QED

The continuum form is the same two lines: [n, a_par n] = 0, so the axis-parallel fluctuation sees only partial
derivatives. **Reading:** inside one domain the commutators reach only the charged (transverse) directions; the
axis-parallel neutral directions are exactly those of U(1). They can be reached only where the axis changes, at
junctions between domains, and the change costs the scale-free energy of Lemma CE, about beta delta^2 per plane.
In the domain models of Kalloniatis and Nedelko the neutral mass comes from a boundary condition imposed at the
domain wall, and the domain size is fitted, not derived (RECALLED).

### The role inversion (ARGUED; the main finding of Step 6)

The commutator energy plays two opposite roles. (i) Inside one periodic block it is a confining potential for the
zero modes, and quantum fluctuation transverse to every axis lifts the valley (Lemma S, Lemma S_n): a neutral gap
kappa g(l)^(2/3)/l. (ii) Between blocks it is a junction cost that aligns axes. The proof of Lemma CE works for
any lattice rectangle R (a disc): if the holonomy around its boundary has angle delta, the plaquettes of R cost at
least (2/pi^2) beta delta^2 / |R|; a rectangle that crosses blocks turning about different axes has such a
boundary holonomy, and on a 4D block the cost summed over parallel rectangles is scale free. So at weak block
coupling (beta large) low-action fields keep one axis over long distances, and there (Lemma DOM) the axis-parallel
modes are U(1) photons. A neutral gap at large size needs axis changes to be frequent, that is fluctuation to beat the junction
cost: the coarse theory must be disordered, which is the strong-coupling side of the band. The owner's picture is
the right picture of the confined vacuum (it is the domain picture), but its directional ingredient, the
commutator, is by itself a force for order at weak coupling and a force for a gap only inside a periodic block.

**First failing step of the tiling route (OPEN, not new).** (TILE-dis): at some block size l along the trajectory,
the axes of neighbouring blocks are disordered with a margin uniform in the cutoff. This is a disorder statement for
the coarse theory at the band scale. It is the lane's wall in another form ((W), (N-phys); rows 998, 1161, 1179,
1249). Attacked four ways above: A killed by Lemma GA; B has the wrong sign (paramagnetism); C reduces to the
band; D puts the domain size in by hand.

## Step 7. A fact test for directional mechanisms, the GUIDE run, and the verdict

### Fact test GG (commutators present, axes ordered, neutral half fails). ON FILE: row 669 and row 1004 Lemma GG.

Found in the final rule-0a grep: this is the "third test" of row 669 (`gap-skeleton-max.md` L77-80: "SU(2) +
adjoint Higgs ... no gap, photon, the field selects a U(1)"; "a proof must fail when an adjoint Higgs field is
added"), and its end point at kappa = infinity is row 1004 Lemma GG (`gap-outside-box-max.md` 6.2, PROVED there,
checked by no one). The paragraph below restates it; the only addition is the reading through Lemma DOM.

Lattice SU(2) with a unit adjoint field phi_x in S^2 (in su(2)) and weight beta sum_p (1/2) tr U_p +
kappa sum_l <phi_(s(l)), Ad(U_l) phi_(t(l))>. In unitary gauge phi_x = n. At kappa = infinity the second term
forces Ad(U_l) n = n, that is U_l = exp(alpha_l n), and the model is exactly compact U(1) with action
beta sum_p (1 - cos (d alpha)_p) (PROVED, two lines: the stabilizer of n under Ad is the one-parameter group of n).
Compact U(1) has a Coulomb phase with a massless photon at large beta (Guth 1980; Frohlich and Spencer 1982;
RECALLED, the lane's standing U(1) test). At large finite kappa the model keeps the whole SU(2) group, every
commutator of Steps 2-5 and the transverse lift, and is believed to keep the massless photon (the Georgi-Glashow
Coulomb phase; on file as BELIEF in row 1017, `gap-compact-rigidity-max.md` L94). By Lemma DOM the photon is the
axis-parallel direction of the ordered axis. **Use:** a proof of the neutral half that uses the SU(2) commutators but
whose steps also hold when an adjoint field orders the axes is wrong. The directional idea must enter through the
absence of axis order, not through the commutator alone. Row 669 drew the same lesson ("the proof cannot use the
group alone; it must use the dynamics of the pure gauge measure").

### GUIDE run (not a proof step)

Run at 12:49Z-12:50Z under `python3 scripts/lab_ops.py numeric-lock` (acquired and released; free memory 50
percent by `memory_pressure`; one process, BLAS threads 1, peak RSS 33 MB; script in a scratch folder outside the
repository). Results: Lemma CC formula, maximum error 9.2e-16 over 20000 random pairs; Lemma CE, smallest ratio of
action to bound 1.11 over 3200 random fields on periodic planes 1x1, 2x2, 2x3, 4x4 at four field scales (the bound
holds in every sample); Lemma DOM, on a 2x2 periodic plane at a random abelian background, mixed
parallel-transverse Hessian entries and first-order transverse terms 0.0 by central differences. These agree with
the hand proofs and prove nothing.

### Verdict

**The owner's question, answered.** Do the commutators of multi-direction blocks reach the neutral half rather
than only the flux half?

1. Read literally (pieces of the lattice, each turned about its own axis), no: the axes are pure gauge (Lemma DR),
   and after the gauge projection rotations at distinct sites commute for all axes (Proposition PT). PROVED.
2. At half-turns about perpendicular axes, the commutator is central (Lemma CC): the three-axis dream at
   half-turns is 't Hooft's twisted box m = (1, 1, 1), Fact T in all three planes, the flux half, shared with Q_8
   (Corollary CC1). On file as Fact T and Route T.
3. Every other non-commuting junction is curvature (Corollary CC2). Its energy is the quartic, scale-free
   commutator energy, a lower bound for every lattice field (Lemma CE; on file as the untwisted case of the row 791
   peeling identity and norm bound). Kinematically it acts inside the neutral
   sector only through intertwiners at junction sites, which U(1) lacks; one axis on two groupings already fails to
   commute there (Proposition PT2). PROVED.
4. Dynamically, yes in one periodic block: two or more non-commuting directions confine the zero modes, and the
   gauge-invariant constant-mode spectrum is discrete with gap kappa g^(2/3)/L; one direction does not (Lemmas S,
   S_n, PROVED in the reduced model; the lattice reduction is Luscher's, RECALLED). This is the exact sense in
   which "the commutators, which have no U(1) analogue, reach the neutral half". It gives z = kappa g(L)^(2/3),
   which tends to 0 at small L, so it does not reach (N-phys).
5. In a tiling, the same commutator energy is a junction cost that aligns axes at weak coupling, and in an aligned
   region the axis-parallel modes are exactly U(1) at quadratic order (Lemma DOM, PROVED; Lemma GA kills the block
   form of Simon's inequality, PROVED). A neutral gap at large size needs disorder of block axes at the band scale,
   (TILE-dis), which is the wall (W)/(N-phys) in another form. Four ways stop there (Step 6). The adjoint-Higgs
   test (row 669 "third test", row 1004 Lemma GG; read here through Lemma DOM) says any directional proof must
   use the absence of axis order.

**Mass gap: NOT proved. Nothing disproved.** (N-phys), (W), the continuum datum and (TILE-dis) stay OPEN. No
statement of the T0 chain or of the gap chain changes status.

**New against the record (greps in Step 1 and a final grep before this verdict):** Lemma DR (the axes of turned
sub-blocks are gauge), Lemma J (several-axis form of row 1013's corner graph, at group level), Lemma CC with
Corollary CC2 (central only for perpendicular half-turns), Propositions PT, PT1, PT2 (projected rotations commute;
the residue sits on intertwiners at junctions), Lemma GA, the written proofs of Lemmas S and S_n (the statement for
three directions was on file only from memory), the lattice form of Lemma DOM (standard background-field splitting,
used at one loop in row 1244 L200-206), and the role inversion as a synthesis. All are elementary. Their value is to
close the owner's idea as a route with the reason, and to place the directional mechanism exactly: inside one
periodic block it works (Lemma S), across blocks it needs disorder.
**Not new:** Fact T and Route T (Corollary CC1); Lemma CE (row 791 peeling identity and norm bound, rows 783, 788);
the small-volume mechanism and its g^(2/3) value (rows 669, 670, 998, 1003, 1128, 1158); Way B (row 1193); the
adjoint-Higgs test (row 669 third test, row 1004 Lemma GG); the paramagnetic sign (row 1244 table); the RG reading
(row 1249); Lemma DOM's consequence for K_3 (row 1241: "at Gaussian order K_3 is massless", which Lemma DOM explains
in general: around a one-axis background, commutator effects start at third order).

**Suggested check (one reader of the other provider, line by line):** Lemmas J, DR, CC, PT, PT2 (b), CE, S (a)-(c),
S_n, GA, DOM; the GG reduction at kappa = infinity. Moves: (N-phys) only as a closed route; no consumer reads
these lemmas yet.

**Credits.** B. Simon (1983) for the method of Lemma S; M. Luscher (1983), P. van Baal and J. Koller for the
small-volume effective Hamiltonian; G. 't Hooft for twists and flux; G. K. Savvidy (1977), N. K. Nielsen and
P. Olesen (1978), J. Ambjorn and P. Olesen (1980), N. K. Nielsen (1981), R. J. Hughes (1981), H. Leutwyler
(1980-81), A. C. Kalloniatis and S. N. Nedelko (from 2001) for the physics of chromomagnetic domains (all
RECALLED, none re-read here); A. Guth (1980), J. Frohlich and T. Spencer (1982) for the U(1) Coulomb phase
(RECALLED); J. Kogut and L. Susskind for the Hamiltonian lattice form; R. Penrose and J. Baez for spin networks
(RECALLED); T. Balaban and Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text) for the
block renormalization that Way C refers to, cited and not used in any proof here; the lane's rows 998, 1003, 1013,
1016, 1017, 1046, 1128, 1132, 1161, 1179, 1188, 1194, 1200, 1201, 1228, 1241, 1244, 1249 as cited. The owner's
three-axis idea is the starting point of every step.

RESULT: Row 1273 (Claude Opus 5.5 max, Mac mini worker 2, 12:27Z-12:55Z by date -u; author only, checked by no one). Mass gap NOT proved, nothing disproved; (N-phys), (W), the continuum datum stay OPEN. The owner's multi-direction blocks, taken literally: PROVED by hand that the axes of turned sub-blocks are pure gauge (Lemma DR, via the several-axis junction invariants of Lemma J) and that gauge-projected rotations at distinct sites commute for all axes (Proposition PT); that a junction commutator is central only for perpendicular half-turns (Lemma CC), which gives 't Hooft's m = (1,1,1) twisted box, the flux half (on file: Fact T, Route T); that every other junction is curvature, whose action cost is the commutator bound already on file (rows 783/788/791 peeling identity), and which acts on the neutral sector only through intertwiners at junctions, which U(1) lacks, with one axis on two groupings already non-commuting (Proposition PT2); and a written proof (Simon's method) that in the reduced zero-mode model two or more non-commuting directions give a discrete spectrum and a neutral gap kappa g^(2/3)/L, one direction none (Lemmas S, S_n; the statement was on file only from memory, rows 669, 670). So the commutators reach the neutral half only inside one periodic block, with z -> 0 at small L. In a tiling the same commutator energy aligns axes at weak coupling and one-axis regions are U(1) in their parallel modes (Lemma DOM, lattice form of the background splitting; Lemma GA kills a block form of Simon's bound; the field-strength form fails by the spin sign, on file as row 1193); the route stops at (TILE-dis), disorder of block axes at the band scale, the wall in another form (four ways). The adjoint-Higgs test (row 669, row 1004 Lemma GG) binds any directional proof. Output library/gap-owner-threeaxis-opus.md.
