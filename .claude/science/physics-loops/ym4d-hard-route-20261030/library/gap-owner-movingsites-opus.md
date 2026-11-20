lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T00:34Z

# gap-owner-movingsites-opus: moving sites, sliding blocks and the mass gap

Queue row 1274 of `FINISH.md`, run on the Mac mini Claude worker 3 at commit fa2cf667b,
started 2026-11-20T12:34Z (date -u). Claude Opus 5.5, max effort.

Status of this file: in progress. Each section is appended as a step finishes.
Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## 0. Task as read

The problem (row 1274): prove that four-dimensional SU(2) Yang-Mills theory has a mass gap
in the sense of Jaffe and Witten. The owner's hint (2026-11-20): "anything to the sites
themselves moving between lattice nodes in some interesting way?" Forms named in the row:
sliding or sheared blocks, shifted or translation-twisted boundary conditions, lattice
dislocations, comparisons with moved or random lattices. The record has only lattice
translations as a symmetry group (row 1201, no stiffness).


## 1. Repo search (12:34Z-13:05Z)

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
Sections 2-5 test each new form against both.

## 2. Sliding blocks and dislocations (13:05Z-13:40Z)

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
holonomy gives a positive measure invariant under gauge transformations. (3) Every centre flip C_nu of the torus is
still a symmetry: each closed cycle of the dislocated lattice crosses the hypersurface x_nu = c + 1/2 an even number
of times (checked for the core cycle of 2.2 below). So a dislocation is centre-neutral.

### 2.2 Lemma DIP: a dislocation dipole is a localized shear, and its tension is the shear deficit (PROVED given (TM) and RP for the slice lattices; ARGUED for the core overlap)

Take one cut piece: the bonds of direction 1 from (0, x_2, z) to (1, x_2, z), z = (x_3, x_4), with 0 <= x_2 < m,
reglued by a shift b in span(e_3, e_4), b != 0. By 2.1 (c) this is a dislocation dipole: cores at x_2 = -1/2 and
x_2 = m - 1/2 (2-planes in the directions 3 and 4) with Burgers vectors b and -b. For b = e_3 the core cycle is the
pentagon (0, -1, z) -> (1, -1, z) -> (1, 0, z) -> (0, 0, z - e_3)... closed by one step in direction 3; it crosses
x_1 = 1/2 twice. Write Z_dip(m) for its partition function with a fixed core action.

(a) Z_dip(0) = Z(Q) and Z_dip(n_2) = Z(Q with the period (n_1, 0, -b)) = Tr(T_1^(n_1) tau_b) (part (a) of 2.1, no core).
So the dipole interpolates between the periodic torus and the sheared torus, as a 't Hooft loop interpolates between
the periodic and the twisted torus.

(b) Channel 2 (direction 2 as time). Slices with 0 <= x_2 < m are the 3-torus Q_b = Z^3/<(n_1, -b), n_3 e_3,
n_4 e_4> (by 2.1 (a) in three dimensions); the other slices are the rectangular Q_0. With T_0, T_b the positive
transfer operators of Q_0 and Q_b in direction 2 ((TM) on each slice lattice: the proof of `gap-transfer.md` reads
only that the slice is a lattice with square plaquettes, as row 962 A4 notes) and K_+, K_- the one-step kernels at
the two cores,

Z_dip(m) = Tr( T_0^(n_2 - m - 1) K_- T_b^(m - 1) K_+ ),   1 <= m <= n_2 - 1.

(c) The shear deficit Delta_b := log lambda_0(T_0) - log lambda_0(T_b) is >= 0. Proof: the 4-torus with period
(n_1, 0, -b) has Tr(T_b^(n_2)) = Tr(T_1^(n_1) tau_b) <= Tr(T_1^(n_1)) = Tr(T_0^(n_2)) for every n_2 (row 1201
Lemma G1 (d): |Tr(T^t U)| <= Tr(T^t) for a unitary U commuting with T >= 0); take the n_2-th root and let n_2 grow.

(d) Upper bound. Since |Tr(AB)| <= ||A||_1 ||B||,
Z_dip(m) <= ||K_-|| ||K_+|| lambda_0(T_b)^(m-1) Tr(T_0^(n_2-m-1)), so with Z(Q) >= lambda_0(T_0)^(n_2):

-log( Z_dip(m)/Z(Q) ) >= (m - 1) Delta_b - log( ||K_-|| ||K_+|| / lambda_0(T_0)^2 ) - log(1 + S_0(n_2 - m - 1)),

with S_0 the excited thermal sum of T_0. The dipole pays at least the shear deficit per unit of width.

(e) Lower bound, when the dipole is reflection symmetric (reflection of direction 2 through x_2 = (m - 1)/2, which
swaps the cores; then K_+ = K_-^* by the Osterwalder-Seiler argument, which reads only the bonds and plaquettes next
to the reflection plane, and those are standard squares): every term of the spectral sum
Z_dip(m) = sum over i, j of lambda_i(T_0)^(n_2-m-1) lambda_j(T_b)^(m-1) |<psi_i, K_- phi_j>|^2 is >= 0, so
Z_dip(m) >= lambda_0(T_0)^(n_2-m-1) lambda_0(T_b)^(m-1) |<psi_0, K_- phi_0>|^2. The overlap is > 0 if K_- has a
positive kernel and the top eigenvectors are positive (Perron-Frobenius, (TM)). ARGUED, not written out: that the
core kernel K_- is positive for the Wilson weight of the core cycle (it is a product of positive functions of the
link variables, so I expect the standard proof to apply).

Reading (PROVED from (d) and (e) up to the core overlap): for widths m with m and n_2 - m both large,
-log(Z_dip(m)/Z(Q)) = m Delta_b + O(1), the O(1) set by the cores and the thermal sums. So **the tension of a
dislocation strip is exactly the shear deficit of the slice**, the object of row 962's crossing identity and of
route RA. The cores add a local core free energy and a core-core interaction. The interaction is a correlation of
two centre-neutral defect operators across the strip: in channel 2 it decays at the rate of the neutral gap of T_0
(and of T_b), and not faster.

### 2.3 Verdict on dislocations (ARGUED; the identities are PROVED above)

- (SEL) fails. Lemmas SLIDE and DIP use only the lattice, Haar invariance and positivity. Compact U(1) at weak
  coupling satisfies them with Delta_b of the order of the Casimir shape term, of order 1/n per unit width
  (GIVEN the photon facts on file: test table of `parts/gap.md`, row 1184's value 2 pi), so a dipole of width
  n_2/2 costs order one. A gapped theory has Delta_b exponentially small in the slice size, so the dipole cost
  saturates at the core terms. That dichotomy is the gap itself, read through a localized shear; it is not an input.
- (NEU) fails as a lever. The core interaction is a neutral correlation, so a bound on it is a neutral clustering
  statement of the kind (N-phys) asks for. A dislocation does not see zero-momentum scalars any better than a
  plaquette does.
- First failing step: the strip is invisible because a lattice translation is a symmetry; what is left is the
  shear deficit (route RA, row 962 7.4: "only the full sum bounds it") and a local core (a neutral observable).
  Nothing in either reads SU(2).

What is new here: dislocations as localized shears with an exact tension (Lemma DIP), and the sliding-block
reduction (Lemma SLIDE). Neither has a consumer in the chain.
