lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T00:34Z

# gap-owner-movingsites-opus: moving sites, sliding blocks and the mass gap

Queue row 1274 of `FINISH.md`, run on the Mac mini Claude worker 3 at commit fa2cf667b,
started 2026-11-20T12:34Z (date -u). Claude Opus 5.5, max effort.

Status of this file: complete (13:04Z). Sections were appended as each step finished.
Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## 0. Task as read

The problem (row 1274): prove that four-dimensional SU(2) Yang-Mills theory has a mass gap
in the sense of Jaffe and Witten. The owner's hint (2026-11-20): "anything to the sites
themselves moving between lattice nodes in some interesting way?" Forms named in the row:
sliding or sheared blocks, shifted or translation-twisted boundary conditions, lattice
dislocations, comparisons with moved or random lattices. The record has only lattice
translations as a symmetry group (row 1201, no stiffness).


## 1. Repo search (12:34Z-12:46Z, date -u)

Read: `GOAL.md`; `FINISH.md` L1-84, L299-356 and rows 1201, 1218, 1258-1260, 1264-1275 (RESULT lines);
`parts/gap.md` L1-105; `library/gap-crux-restate.md` Sections 1-3.4 (setting, C1-C5, Theorem D, Theorem S);
`library/gap-mini-solve-k-fable.md` (row 1201, all); `library/gap-constraints-max.md` A4 (L185-198) and 7.4
(L411-440) (row 962); `library/gap-solve9-astra62.md` L42-75 (row 1161, fractional momentum);
`library/gap-mini-neutral2-fable.md` L60-80, L160-175 (the statement of (N-phys)).
Grepped `library/`, `library/prior/`, `parts/gap.md`, `FINISH.md` for each moving form.

The crux as I use it below (cited, not re-derived). Engine: Theorem S (row 697, checked rows 698-699): on
periodic tori one seed S(n; (2n)^3) < 1/5041 gives a uniform gap on all larger cubes, for every group. Open
content: the neutral premise (N-phys) (row 1161 L146-148; row 1184 L66-70): a physical side L and, at every fine
cutoff, a time u <= n/K with neutral excited trace s(u; n^3) <= 1/2. Row 1184 reads it as "the neutral gap of one
physical cube, in units of its inverse side, passes a threshold" between about K log 2 and 2K log(2 S_0); a free
massless field has the value 2 pi at every size. Row 1258 gives the one-coupling forms (SL)/(RR). The flux half (BS)
is a separate item.

### 1.1 Moving forms against the record

| Form | On file | What is there | Verdict on file |
|---|---|---|---|
| Sheared tori, translation-twisted periodic conditions, Tr(T^a tau_v) | row 962 A4 and 7.4 (`gap-constraints-max.md` L185-198, L411-440): Lemma SHIFT, projected doubling, projected crossing identity; row 1066 Lemma FR and I9 (`gap-outside-box-max.md` L113-120, L172, L190) | exact identities | blind; "changes a constant, not the crux" |
| Rotated and diagonal tori, boxes rotating in time | row 963 (`gap-rotgeom-opus.md` Lemmas R2, R3, D2) | diagonal tori are sheared axis tori | buy nothing for the seed |
| The symmetry group of the box (translations and signed permutations) as a rigid group | row 1201 Lemma G1 (`gap-mini-solve-k-fable.md` L64-91) | invariant and charged sums as group averages of twisted traces | no stiffness: a uniform displacement is removed by pulling back the field; reduces to routes RA and RB |
| Translations with a centre twist (compensated translations, fractional momentum) | row 1161 (`gap-solve9-astra62.md` L42-75); check `gap-channel-check-opus.md` L48 | D_i^(n_i) = -I in sectors with Mq != 0; even multiplicities; 42 sectors bounded | flux half only; the neutral sector q = 0, m = 0 is untouched |
| Twist weights under changes of basis (the modular group on twists) | row 1161 (same file, after L64) | near invariance of f_Q(B) under rank-preserving changes | flux half |
| Bond moving (Migdal-Kadanoff, Tomboulis decimation) | row 876 item 16; `gap-cr-tomboulis-max.md` 7.2 (Proposition SIGN) | bond moving bounds Z, not the twist ratio | no sign on the twist quotient (PROVED there for Z_2) |
| Dislocations (sliding blocks with a mismatch) | not as a moving form; "lattice dislocations" occur only as small-action instanton lumps (row 1013 K8, `gap-invent-selective-max.md` L258; row 1200, `gap-mini-solve-j-fable.md` L184-185) | - | NEW as a moving form |
| Moved lattices (offset against the continuum) and random lattices (Christ, Friedberg and Lee) | no hit for "random lattice", "Voronoi", "moved lattice" outside this item | - | NEW |
| Rotation of sites about a codimension-2 axis (corner transfer matrix; branched covers are its powers Tr A^(4k)) | row 962 A7 (`gap-constraints-max.md` L139, L215-218); row 1066 (`gap-afield-b-max.md` L91); no hit for "disclination", "branched cover" in this sense | spectrum of a half-space entanglement Hamiltonian, level spacing about 1/log(xi) in solvable 2D models | dead: "no seed can be read from it" |
| A positively curved slice (S^3 in place of the 3-torus) | row 962 A9 (`gap-constraints-max.md` L224-) | no axis exchange, no crossed-channel trace | dead |
| Translations traded for colour (twist eaters, Eguchi-Kawai reduction) | twist eaters in 20 files (Fact T, C5, rows 930-938, 1200); Eguchi-Kawai in 6 files (`gap-lit-xvol.md` and others) | small-volume and large-N statements | flux half and small volume |

`library/open-core.md` holds the existence chain; grep for "dislocation", "shear", "random lattice", "branched"
there: no hit (checked: 0 matches for each, and for "disclination", "corner transfer", "Eguchi", "translation").
So the new forms for this row are two: dislocations (sliding blocks with a mismatch) and moved or random lattices.
Rotation of sites about an axis is row 962 A7 and is not redone.

### 1.2 What a moving form must do to matter (GUIDE; a reading of the record)

The record fixes two tests (parts/gap.md L36-50, row 998 6b; row 1201 Section 2.1):

- (SEL) The input must be selective. It must be false for compact U(1) at weak coupling (a massless photon,
  Guth; Frohlich and Spencer), for the free Maxwell field, for products with a massless factor, and for frozen
  groups in the periodic form. A statement that every compact group satisfies cannot give the seed.
- (NEU) The open premise (N-phys) is about the centre-neutral, periodic sector (m, q) = (0, 0); row 1161 bounds
  the 42 sectors with Mq != 0 and the rest given (N-phys). Inside the neutral sector, a lattice symmetry can only
  split the trace into its invariant part and twist costs (row 1201 Lemma G1). The part no symmetry move can see
  is the zero-momentum scalar part: states of a one-dimensional representation of the box symmetry group (row 1201
  Section 3.2).

A moving form can matter in two ways only: as a selective input that reaches the neutral sector, or as an engine
that lowers the seed threshold to a size where a provable input (asymptotic freedom at small coupling) holds.
Sections 2-4 test each new form against both.

## 2. Sliding blocks and dislocations (12:46Z-12:53Z; corrected 13:02Z)

Setting. Q = Z^4/Gamma, Gamma = diag(n_1, ..., n_4) Z^4, all n_mu >= 4. Wilson SU(2) action with class-function
plaquette weights; any compact group G is allowed in 2.1-2.3, because nothing there reads G. "Regluing a cut by a
shift v" means: for each bond that crosses the cut, keep its tail and move its head by v. A shift is always a lattice
vector, so a lattice never slides by a fraction of a spacing.

### 2.1 Lemma SLIDE (PROVED)

(a) Slabs. Cut Q along the hyperplanes x_1 = c_k + 1/2, k = 1, ..., r, and reglue the k-th cut by a shift
v_k in span(e_2, e_3, e_4). The result is a lattice torus with square plaquettes, isomorphic to Z^4/Gamma', where
Gamma' is generated by (n_1, -V) with V = v_1 + ... + v_r and by n_2 e_2, n_3 e_3, n_4 e_4. So its partition function
is the sheared-torus trace Tr(T_1^(n_1) tau_V) of row 962 (Lemma SHIFT) and row 1201 (Lemma G1).

Proof. Every site keeps one bond in each of the eight directions. A (1, j)-plaquette across cut k closes:
(c_k, y) -> (c_k + 1, y + v_k) -> (c_k + 1, y + v_k + e_j) -> (c_k, y + e_j) -> (c_k, y), because the bond from
(c_k, y + e_j) is moved by the same v_k. Put W(x_1) = sum of v_k over the k with c_k < x_1, for 0 <= x_1 < n_1, and
phi(x_1, y) = (x_1, y - W(x_1)). A moved bond (c_k, y) -> (c_k + 1, y + v_k) goes to (c_k, y - W(c_k)) ->
(c_k + 1, y - W(c_k)), a standard bond. Inside a slab W is constant. The bond that closes the period x_1 = n_1 - 1 ->
0 goes to (n_1 - 1, y - V) -> (0, y), which is a standard bond of Z^4/Gamma' because (n_1, -V) is in Gamma'. phi is a
bijection of sites that maps bonds to bonds and plaquettes to plaquettes. QED

(b) A grid of blocks, screw type. Cut Q along x_1 = c_k + 1/2 (k = 1..r) and x_2 = d_l + 1/2 (l = 1..s). The cuts
divide the (x_1, x_2) torus into r s rectangles, so Q into r s blocks B_kl. Reglue each face between two neighbouring
blocks by its own shift, every shift in span(e_3, e_4). At the line where four blocks meet, the (1, 2) cycle that
starts at (c_k, d_l, z) and follows the four moved bonds ends at (c_k, d_l, z + beta_kl), with

beta_kl = a + b' - a' - b,

a, a' the shifts of the two x_1-faces below and above the line, b, b' those of the two x_2-faces left and right of
it. If every beta_kl = 0, the result is a lattice torus with square plaquettes, isomorphic to Z^4/Gamma'', Gamma''
generated by (n_1, 0, -H_1), (0, n_2, -H_2), n_3 e_3, n_4 e_4, where H_1, H_2 in Z^2 are the sums of the shifts
along one closed row and one closed column of blocks.

Proof. The shifts are a 1-cochain with values in Z^2 on the dual grid of the (x_1, x_2) torus (blocks are vertices,
faces are edges). beta_kl is its coboundary on the dual square around line (k, l), by the computation above. If the
coboundary is zero, the cochain is a cocycle on a torus, so it is a coboundary plus the class fixed by its two sums
H_1, H_2 along a closed row and a closed column (these sums do not depend on the row or column chosen, because the
cocycle condition makes them homologous). Translate each block by the value of the 0-cochain whose coboundary
removes the exact part. What is left is part (a) applied in direction 1 with total shift H_1 and in direction 2 with
total shift H_2. QED

(c) Mismatch. If beta_kl is not zero, the line (k, l) carries a screw dislocation: the elementary cycles that cross
it close only after |beta_kl|_1 further steps in directions 3 and 4, so the plaquettes there are replaced by longer
cycles. The sum of all beta_kl is zero (the coboundary of a 1-cochain sums to zero over the closed dual torus). So
on a torus dislocations come in sets with total Burgers vector zero, and a sliding-block lattice is a sheared torus
(the class (H_1, H_2)) plus such a set.

Remarks. (1) A shift with a component normal to another family of cuts leaves sites without a partner across that
cut: the core then also carries an extra or missing half-hyperplane (edge type). I do not need that case below; the
statements of 2.2 hold for it with the same proofs once a core action is fixed (ARGUED). (2) On the dislocated
lattice the weight of each long core cycle is a free choice of a local core action. Any class function of its
holonomy gives a positive measure invariant under gauge transformations. (3) Every centre flip still exists on
the reglued lattice, with one change: C_nu flips each bond whose two ends lie on opposite sides of the hypersurface
x_nu = c + 1/2, and a moved bond can cross a plane x_3 = c + 1/2 or x_4 = c + 1/2. (The naive flip of the e_3-bonds
alone is NOT a symmetry once b has a 3-component: the (1, 3)-square in the strip, (0, x_2, c) -> (1, x_2, c + 1) ->
(1, x_2, c + 2) -> (0, x_2, c + 1) -> (0, x_2, c), would carry one flipped bond.) Every 2-cell, square or core
cycle, is a closed loop of integer points, so the sign of x_nu - c - 1/2 changes an even number of times around it,
and the flip leaves every weight unchanged. Flips preserve Haar measure. So a dislocation is centre-neutral.

### 2.2 Lemma DIP: a dislocation dipole is a localized shear, and its tension is the shear deficit (PROVED given (TM) for the two slice lattices)

Take one cut piece: the bonds of direction 1 from (0, x_2, z) to (1, x_2, z), z = (x_3, x_4), with 0 <= x_2 < m,
reglued by a shift b in span(e_3, e_4), b != 0. By 2.1 (c) this is a dislocation dipole: cores at x_2 = -1/2 and
x_2 = m - 1/2 (2-planes in the directions 3 and 4) with Burgers vectors b and -b. For b = e_3 the core cycle is the
pentagon (0, -1, z) -> (1, -1, z) -> (1, 0, z) -> (0, 0, z - e_3) -> (0, 0, z) -> (0, -1, z) (the third step runs
backward along the moved bond from (0, 0, z - e_3)); it crosses x_1 = 1/2 twice. Its mirror image under
x_2 -> m - 1 - x_2 is the core cycle at x_2 = m - 1/2. Write Z_dip(m) for its partition function with a fixed core action.

(a) Z_dip(0) = Z(Q) and Z_dip(n_2) = Z(Q with the period (n_1, 0, -b)) = Tr(T_1^(n_1) tau_b) (part (a) of 2.1, no core).
So the dipole interpolates between the periodic torus and the sheared torus, as a 't Hooft loop interpolates between
the periodic and the twisted torus.

(b) Channel 2 (direction 2 as time). Slices with 0 <= x_2 < m are the 3-torus Q_b = Z^3/<(n_1, -b), n_3 e_3,
n_4 e_4> (by 2.1 (a) in three dimensions); the other slices are the rectangular Q_0. With T_0, T_b the positive
transfer operators of Q_0 and Q_b in direction 2 ((TM) on each slice lattice: the proof of `gap-transfer.md` reads
only that the slice is a lattice with square plaquettes, as row 962 A4 notes) and K_+, K_- the one-step kernels at
the two cores,

Z_dip(m) = Tr( T_0^(n_2 - m - 1) K_- T_b^(m - 1) K_+ ),   1 <= m <= n_2 - 1.

Count: the slices x_2 = 0, ..., m - 1 are Q_b and x_2 = m, ..., n_2 - 1 are Q_0; there are m - 1 steps inside the
strip, n_2 - m - 1 outside, and two interface steps, K_- from slice m - 1 to m and K_+ from slice n_2 - 1 to 0, which
carry the core cycles; m - 1 + n_2 - m - 1 + 2 = n_2. All other plaquettes between two slices are standard squares.

(c) The shear deficit Delta_b := log lambda_0(T_0) - log lambda_0(T_b) is >= 0. Proof: the 4-torus with period
(n_1, 0, -b) has Tr(T_b^(n_2)) = Tr(T_1^(n_1) tau_b) <= Tr(T_1^(n_1)) = Tr(T_0^(n_2)) for every n_2 (row 1201
Lemma G1 (d): |Tr(T^t U)| <= Tr(T^t) for a unitary U commuting with T >= 0); take the n_2-th root and let n_2 grow.

(d) Upper bound, for 1 <= m <= n_2 - 2 (so that the power of T_0 is at least 1). Since |Tr(AB)| <= ||A||_1 ||B||,
Z_dip(m) <= ||K_-|| ||K_+|| lambda_0(T_b)^(m-1) Tr(T_0^(n_2-m-1)), so with Z(Q) >= lambda_0(T_0)^(n_2):

-log( Z_dip(m)/Z(Q) ) >= (m - 1) Delta_b - log( ||K_-|| ||K_+|| / lambda_0(T_0)^2 ) - log(1 + S_0(n_2 - m - 1)),

with S_0 the excited thermal sum of T_0. The dipole pays at least the shear deficit per unit of width.

(e) Lower bound. The reflection x_2 -> m - 1 - x_2 (mod n_2) maps the dipole lattice onto itself and exchanges the
two interface steps, so K_+ = K_-^* (reason at the end of (e)). T_0 and T_b are self-adjoint and >= 0 ((TM)), with
eigenvectors psi_i and phi_j. So every term of the spectral sum
Z_dip(m) = sum over i, j of lambda_i(T_0)^(n_2-m-1) lambda_j(T_b)^(m-1) |<psi_i, K_- phi_j>|^2 is >= 0, so
Z_dip(m) >= lambda_0(T_0)^(n_2-m-1) lambda_0(T_b)^(m-1) |<psi_0, K_- phi_0>|^2. The overlap is > 0: the kernel
of K_- is a product of the strictly positive weights exp(beta (1/2) tr U) of its plaquettes and core cycles,
integrated over the bonds between the two slices, so it is a strictly positive function; psi_0 and phi_0 are
strictly positive by (TM). K_+ = K_-^*: the reflection sends the strip [0, m) to itself, leaves b unchanged,
sends slice n_2 - 1 to slice m and slice 0 to slice m - 1, and exchanges the two core cycles (see the pentagon
above). So the kernel of K_+ is the kernel of K_- with its two arguments exchanged, and both kernels are real.

Reading (PROVED from (d) and (e)): for all widths 1 <= m <= n_2 - 2,
-log(Z_dip(m)/Z(Q)) = (m - 1) Delta_b + R(m), with R(m) between -log(||K_-|| ||K_+|| / lambda_0(T_0)^2) -
log(1 + S_0(n_2 - m - 1)) and -log(|<psi_0, K_- phi_0>|^2 / lambda_0(T_0)^2) + log(1 + S_0(n_2)): bounded by
core and thermal terms, uniformly in m. So **the tension of a dislocation strip is exactly the shear deficit of the slice**,
the object of row 962's crossing identity and of
route RA. The cores add a local core free energy and a core-core interaction. The interaction is a correlation of
two centre-neutral defect operators across the strip; in channel 2 its m-dependence is set by the neutral
excited spectra of T_0 and T_b (ARGUED: K_- commutes with the centre flips, Remark (3)).

### 2.3 Verdict on dislocations (ARGUED; the identities are PROVED above)

- (SEL) fails. Lemmas SLIDE and DIP use only the lattice, Haar invariance and positivity, and hold for every
  compact group. For a free massless field (and compact U(1) at weak coupling) Delta_b is the change of the Casimir
  energy of the slice under the shear: about (|b|/n)^2/n for a small shear and of order 1/n when |b| is of order n
  (GUIDE: the Casimir energy of a 3-torus of side n is of order 1/n, and it is a smooth function of the shape, even
  in the shear). So a dipole of width n_2/2 that slides the strip by half the box costs order one. A gapped theory
  has Delta_b exponentially small in the slice size (ARGUED), so its dipole cost saturates at the core terms. That
  dichotomy is the gap itself, read through a localized shear; it is not an input.
- (NEU) fails as a lever. The core interaction is a neutral correlation, so a bound on it is a neutral clustering
  statement of the kind (N-phys) asks for. A dislocation does not see zero-momentum scalars any better than a
  plaquette does.
- First failing step: the strip is invisible because a lattice translation is a symmetry; what is left is the
  shear deficit (route RA, row 962 7.4: "only the full sum bounds it") and a local core (a neutral observable).
  Nothing in either reads SU(2).

What is new here: dislocations as localized shears with an exact tension (Lemma DIP), and the sliding-block
reduction (Lemma SLIDE). Neither has a consumer in the chain.

## 3. Moved and random lattices (12:53Z-12:54Z)

### 3.1 Lemma GRAPH (PROVED, elementary)

The Wilson partition function, and the law of every gauge-invariant lattice observable, depend on the lattice
only through its cell complex (sites, oriented bonds, the cycles that carry a weight) and the weights. They do not
depend on where the sites sit in R^4.

Proof. The measure is the product of Haar measures over bonds times the product of the cycle weights, and each
weight is a class function of the holonomy of its cycle. Neither reads a coordinate. QED

So a move of sites changes something at a fixed cutoff in one of two ways only:

- (i) it changes the complex: Section 2 (a dislocation or another defect), or a different lattice model;
- (ii) it changes the weights with the geometry, as in the random-lattice actions of Christ, Friedberg and Lee
  (RECALLED: weights that depend on the volumes of dual cells). That is an inhomogeneous coupling field.

Positions enter only when lattice observables are matched with continuum test functions, that is, in the
continuum datum of the T0 chain and its Euclidean clauses.

### 3.2 Verdicts (ARGUED)

- A moved lattice a Z^4 + v is the same model as a Z^4 at each cutoff (Lemma GRAPH). As a -> 0 the comparison of
  offsets is the translation clause of the continuum limit. That is a T0 clause, not the gap. Rotated lattices
  are row 963.
- A random lattice is a different model. Its gap is as open as the hypercubic one, and a comparison with Z^4 needs
  a universality theorem that I do not know for four-dimensional gauge theories (RECALLED; no source opened). If
  its weights follow the geometry, they are a coupling field, and a hypothesis uniform over coupling fields is
  false (Lemma SHEET, row 996, cited in `parts/gap.md` L29). Averaging over random lattices gives exact
  statistical Euclidean invariance of the random-lattice model; that is a tool for the O(4) clause (RO1), not for
  the gap (GUIDE).
- Annealed dilution of sites or bonds (vacancies that hop between nodes) changes the plaquette weight by a
  mixture: Identity MIX of row 996 (K7 as Wilson with annealed Gaussian couplings). Quenched dilution is a coupling
  field (Lemma SHEET). Both on file.
- (SEL): none of these reads the group; the free Maxwell field does not see the lattice at all, so it passes
  every comparison between lattices.

## 4. Does any moving form read SU(2)? (12:54Z-12:57Z; corrected 13:02Z)

### 4.1 The only place where a translation meets the group (PROVED on file; my reading of it)

A lattice translation reads the gauge group in one way only: through the centre, when a twist is present. Row 1161
(`gap-solve9-astra62.md` L42-64, credit 't Hooft): in a magnetic sector m != 0 the translation has to be
compensated by centre flips to move the twist stack back, and the compensated translation D_i satisfies
D_i^(n_i) = product of C_j^(m_ij). In the sectors with Mq != 0 this is -I, so every eigenvalue has even
multiplicity. In the periodic neutral sector (m, q) = (0, 0) no compensation is needed: D_i is the plain
translation tau_i, tau_i^(n_i) = 1, the momentum is an integer multiple of 2 pi / n_i, and the zero-momentum
scalars are fixed by every symmetry move (row 1201 Lemma G1). So the one group-reading combination of moving sites
and gauge structure acts on the flux half, which row 1161 has already used, and does nothing in the sector that
(N-phys) is about.

Statement (PROVED, elementary): every symmetry move of Sections 1.1 and 2.1 (a translation, a signed permutation,
and by Lemma SLIDE (a), (b) every sheared or reglued torus without core) gives a twisted trace Tr(T^t U_g) with g in
the box symmetry group GG of row 1201. Restricted to the periodic neutral sector H_(0,0), the trivial-representation
part of T (the GG-invariant states: the vacuum and every zero-momentum scalar) enters each such trace with the
coefficient chi_triv(g) = 1. Proof: row 1201 Lemma G1 (c) with the decomposition
restricted to H_(0,0). Every U_g preserves H_(0,0): a translation or reflection maps the flip C_nu at the plane
x_nu = c + 1/2 to the flip at another plane x_nu = c' + 1/2, which acts in the same way on gauge-invariant
functions (the two differ by the gauge transformation -1 on the slab between the planes); a permutation sigma of the
axes maps C_nu to C_sigma(nu). So U_g permutes the centre flips and keeps their joint +1 eigenspace. QED. So no family of symmetry moves separates the zero-momentum
scalar part from the vacuum: every such trace contains it with weight one.

### 4.2 Non-symmetry moves (dislocations, junctions of sliding blocks): what they add (ARGUED, from 2.2)

A move that is not a symmetry is a defect. By Lemmas SLIDE and DIP its far field is a symmetry move (invisible, or
a shear when it wraps the torus), and what is left is a core: a centre-neutral local modification of the complex.
Its free energy is a local quantity at the cutoff scale, and its interaction with a second core is a neutral
correlation. Both are read off the same measure as a plaquette correlation; neither brings a new inequality.

### 4.3 Moving forms as engines (on file; GIVEN the free-photon facts)

A moving form could still matter as an engine that lowers the seed threshold to a size where asymptotic freedom
gives a provable input (Section 1.2). It cannot, for the reason the record already states for every blind engine:
Lemma FLOOR (row 988, `library/gap-unit-max.md` L174, check 991: HOLDS) says a seed forces side times gap above
17.04 at threshold 1/5041, and row 998 lists "a seed below the massless floor (twisted or small boxes)" as set aside
(`gap-crux-exercise3-max.md` L506). The free photon has side times neutral gap 2 pi at every size, and (N-phys) is
selective only because K is large (row 1219, `gap-mini-solve-o-fable.md` L47). At small physical size the periodic
neutral sector of SU(2) has a lowest level of order g(L)^(2/3)/L (Luscher, RECALLED, rows 1143, 1008), below the
photon's 2 pi/L. On a twisted torus the single gluons have half-integer momenta and so sit in electric sectors
q != 0 (fractional momentum, row 1161); the neutral twisted levels start at about two gluons, about 2 pi/L (GUIDE,
tree level), no better than the photon. A moving form changes the geometry, not these numbers. So no moving form
gives an engine that small-volume information can seed (ARGUED: it assumes the engine's seed gets harder with more
or lighter states, as every seed on file does). That is the first failing step on this side.

### 4.4 Answer to the owner's question (ARGUED; the lemmas it rests on are PROVED above or on file)

"Anything to the sites themselves moving between lattice nodes?" Not for the gap, in any of the forms named in
row 1274. The reasons, form by form:

| Form | What it is on the lattice | First failing step |
|---|---|---|
| Sheared or shifted blocks, translation-twisted periodic conditions | a sheared torus, Tr(T^t tau_v) (Lemma SLIDE (a), (b); row 962 Lemma SHIFT) | blind identity; its cost is the shear deficit, route RA; row 962 7.4: the deficit is small for all shears only if the full thermal sum is small |
| Sliding blocks with a mismatch, lattice dislocations | a sheared torus plus cores with total Burgers vector 0 (Lemma SLIDE (c)); a dipole has tension exactly the shear deficit (Lemma DIP) | strip invisible (translation is a symmetry); core is a local neutral observable; (SEL) fails |
| Moved lattices | the same model at each cutoff (Lemma GRAPH) | T0's translation clause, not the gap |
| Random lattices, diluted lattices | a different model, or a coupling field, or an annealed mixture | universality open; Lemma SHEET (row 996) and Identity MIX (row 996) |
| Rotated or diagonal lattices, rotation about an axis | rows 963 and 962 A7 | on file: blind, or the entanglement spectrum, not the mass |
| Translations compensated by centre flips | row 1161 | reads the group, but only on the flux half; in (m, q) = (0, 0) it is the plain translation (4.1) |

The common reason: a lattice moves sites only by its own symmetries, and a symmetry move cannot tell SU(2) from
U(1). Away from symmetry moves a move is a defect, and a defect is a local neutral observable. The free Maxwell
field (and compact U(1) at weak coupling) passes every moving-site identity, so none of them can be the selective
step; and the zero-momentum scalars, which (N-phys) has to bound, are fixed by every symmetry move.

What would reopen the question (a reopen condition, not a claim): a move of sites whose cost cannot be removed by a
lattice symmetry and whose cost differs between SU(2) and U(1) at order-one coupling. The only candidates I can
see move colour together with the sites (a translation composed with a non-central colour rotation that varies
across the box). That is the non-abelian block idea of the parallel row 1273 (`gap-owner-threeaxis-opus`), so I do
not attack it here (rule 0a). GUIDE: in such a composite the site part is still removable away from the cores (Lemma
SLIDE), so its cost is the colour part, a twist on the block boundary, which is row 1273's object; I do not expect
the translation to add a mechanism.

## 5. Status, conditions, credits (12:58Z-13:04Z)

| Statement | Label |
|---|---|
| Four-dimensional SU(2) Yang-Mills has a mass gap in the sense of Jaffe and Witten | OPEN. Not proved, not disproved |
| (N-phys), (SL)/(RR), (BS), (W), the continuum datum | OPEN, unchanged |
| Lemma SLIDE (a) slabs reglued by transverse shifts give the sheared torus Z^4/Gamma'; (b) a grid of blocks with screw-type shifts and zero Burgers vectors gives a doubly sheared torus; (c) a mismatch is a screw dislocation, total Burgers vector zero | PROVED here, elementary, any compact group |
| Lemma DIP (a) a dislocation dipole interpolates between the periodic and the sheared torus; (b) transfer form in the channel normal to the strip; (c) shear deficit Delta_b >= 0; (d), (e) -log(Z_dip(m)/Z) = (m - 1) Delta_b + R(m) with R bounded by core and thermal terms | PROVED here given (TM) for the two slice lattices (row 962 A4: same proof as `gap-transfer.md`) |
| Lemma GRAPH: the lattice measure reads only the cell complex and the weights, not the positions of the sites | PROVED here, elementary |
| 4.1: in the periodic neutral sector every symmetry move acts through the box symmetry group, and the zero-momentum scalar part enters each twisted trace with weight one | PROVED here as a corollary of row 1201 Lemma G1 |
| Verdicts: sheared and sliding blocks reduce to the shear deficit (route RA); dislocation cores are local neutral observables; moved lattices are identities, random lattices another model; moving forms give only blind engines (Lemma FLOOR, row 988) | ARGUED, each against (SEL) and (NEU), with the free Maxwell field and compact U(1) at weak coupling as comparison cases (GIVEN the photon facts on file) |
| Neutral twisted levels start at about 2 pi/L (two gluons) | GUIDE, tree level, recalled |
| Reopen condition: a move of sites whose cost no lattice symmetry removes and which differs between SU(2) and U(1) at order-one coupling; the candidates I see move colour with the sites, which is row 1273's idea | OPEN, not attacked here (rule 0a) |

Answer to the owner, in one paragraph. Moving sites do not give the gap in any form named in row 1274. A lattice
can move its sites only by its own symmetries, and a symmetry move cannot tell SU(2) from U(1); its only cost is the
shear deficit, the shape dependence of the torus free energy that route RA already holds. A move that is not a
symmetry is a defect: Lemma DIP shows that a dislocation dipole is a localized shear whose tension is exactly that
shear deficit, plus two cores that are ordinary neutral local observables. Translations read SU(2) only through the
centre, when a twist is present (row 1161's compensated translations); that acts on the flux half, and in the
periodic neutral sector, which is where the proof is stuck, the zero-momentum scalars are fixed by every move. A
side remark, GUIDE only: sliding a block grid at random (the random dyadic grids of Nazarov, Treil and Volberg,
RECALLED) is a standard way to remove the boundary effects of a fixed grid; it bears on the block geometry of the
existence chain, not on the gap, and I did not examine it.

What I would not queue from this row: a check of Lemmas SLIDE, DIP or GRAPH on their own (no consumer), or another
row on sheared, sliding or dislocated lattices for the gap.

Conditions of the run. One session, Claude Opus 5.5, max effort, Mac mini worker 3, pinned at fa2cf667b,
12:34Z to 13:04Z (date -u). No subagent. No numeric run (none was needed; Lemma DIP is a spectral statement with a
hand proof). No outside search; no source outside this checkout was opened. Literature marked RECALLED was not
re-read. Checked by no one.

Credit. Jaffe and Witten (the problem). Balaban; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text (the account the lane builds on; nothing of theirs is used in a step here). 't Hooft (twists,
fractional momentum, as used in row 1161); Luscher (small volume); Guth, and Frohlich and Spencer (the Coulomb
phase of compact U(1)); Osterwalder and Seiler (reflection positivity of the Wilson action); Christ, Friedberg and
Lee (random lattices); Volterra (the cut-and-reglue construction of dislocations); Nazarov, Treil and Volberg (random
dyadic grids); all RECALLED. The lane's rows cited above: 962 (Lemma SHIFT, sheared tori), 963 (rotated tori), 988
(Lemma FLOOR), 996 (Lemma SHEET, Identity MIX), 1161 (fractional momentum), 1184 and 1219 (readings of (N-phys)), 1201
(Lemma G1), and the owner's hint of 2026-11-20.

RESULT: Row 1274 gap-owner-movingsites-opus (Claude Opus 5.5 max, Mac mini worker 3, 12:34Z-13:04Z; author only, checked by no one; no numeric run, no outside search). The mass gap is NOT proved and nothing is disproved. Verdict on the owner's moving-sites idea (ARGUED, each form tested against selectivity with the free Maxwell field and compact U(1) at weak coupling as comparison cases): it does not reach the open premise (N-phys) in any form named. Sheared, shifted and translation-twisted blocks are on file (rows 962, 963, 1201) and cost only the shear deficit (route RA); translations read SU(2) only through the centre on twisted tori (row 1161, flux half); moving forms give only blind engines, which small-volume data cannot seed (Lemma FLOOR, row 988). NEW and PROVED by hand, no consumer: Lemma SLIDE (sliding blocks give a sheared torus plus screw dislocations with total Burgers vector zero); Lemma DIP, given (TM) for the two slice lattices (a dislocation dipole interpolates between the periodic and the sheared torus, and -log(Z_dip(m)/Z) = (m - 1) Delta_b + R(m) with R bounded by core and thermal terms, so the strip's tension is exactly the shear deficit Delta_b >= 0 of the slice); Lemma GRAPH (the lattice measure reads only the cell complex and the weights, so moved lattices are identities and random lattices another model); and, as a corollary of row 1201 Lemma G1, every symmetry move puts the vacuum and the zero-momentum scalars of the periodic neutral sector into each twisted trace with weight one, so no such move separates them. Dislocations are centre-neutral once the centre flips count moved bonds (Remark 3, corrected in this run). OPEN, unchanged: (N-phys), (SL)/(RR), (BS), the continuum datum. Reopen condition: a move whose cost no lattice symmetry removes and that differs between SU(2) and U(1) at order-one coupling; only colour-with-site moves qualify, and their cost is a colour boundary twist (row 1273's object). Output library/gap-owner-movingsites-opus.md.
