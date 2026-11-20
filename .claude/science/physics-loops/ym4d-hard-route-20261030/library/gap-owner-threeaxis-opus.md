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

**Corollary CC1 (the dream at half-turns is the flux half, on file).** In reading (R3) on a 3-torus, take the
links of direction i equal to i sigma_i (half-turns about three perpendicular axes; with U = 1 elsewhere this needs
a cut, as in the toron of `gap-council-geom-fable.md` L28). Every plaquette of the (i, j) plane has holonomy
[i sigma_i, i sigma_j] = -1. Up to a central field this is the flat connection of 't Hooft's twisted 3-torus with
twist in all three planes, m = (1, 1, 1): the three holonomies pairwise anticommute, the flat connection is
isolated, with no zero modes. This is Fact T (`gap-crux-restate.md` L53) in all three planes, and the twisted box of
Route T (rows 678-687, `gap-ac-lat.md`; row 1003 item 14: "in a twisted box no zero modes and a gap of order 1/L").
It reaches the flux half only, and the frozen group Q_8 = {+-1, +-i sigma_k} has it too (check of row 1003,
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
