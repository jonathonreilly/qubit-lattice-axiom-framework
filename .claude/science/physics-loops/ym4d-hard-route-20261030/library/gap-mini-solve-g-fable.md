lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T14:01Z

# gap-mini-solve-g-fable (FINISH row 1197): the mass gap of 4D SU(2) Yang-Mills, plain brief

Research-stage working state. Nothing here is a public claim. Every statement carries one of the labels
PROVED (a written argument in this file or a cited checked row), ARGUED (an argument with a named gap),
GUIDE (numeric or heuristic evidence, never a proof step), OPEN.

## 0. Status log

- 2026-11-20T02:01Z start. Pinned commit 35f40c473. Read GOAL.md, FINISH.md L1-84 and row 1197 (L1278). File created.
- 2026-11-20T02:28Z Section 1 written (record and first screening). Attack not yet chosen; Section 2 will state it.
- 2026-11-20T02:48Z arXiv probe done (four abstract queries, newest first; newest relevant record 2026-11-15): no posted weak-coupling gap or confinement result for a non-abelian lattice gauge theory in four dimensions. Attack chosen: port of the Ding-Huang-Yang mechanism (Section 2).

## 1. Repo search and where the record stands (GUIDE: statements about the record, not evidence)

Read in this session: `GOAL.md` in full; `FINISH.md` L1-84, L320-350, row 1197 and the RESULT lines of rows
1185-1210; `parts/gap.md` L1-104 and L223-322 (state of attack, route registry, test table, price);
`gap-crux-restate.md` L20-125 (definitions, Theorem D, candidates C1-C5); `gap-solve9-astra62.md` L1-160
(row 1161: the Pfaffian seed (7), the one-cube theorem (8)-(10), the finite-aspect statement and its
consumer); `prior/gap-2don-proofs-read-opus.md` L30-125 (digest of Ding, Huang and Yang and of OpenAI);
the head of `gap-solve21-astra62.md` (row 1204, the relativistic test (1)-(2)); the plans of the sibling
files i and k (both in progress, no attack named yet).

1. **The open lattice statement.** (N-phys) of row 1161 (gpt-6.2-astra; checked by row 1162): on one periodic
   cube n^3 of fixed physical side, uniformly in the cutoff, the centre-neutral excited trace s(u) at a time
   u at most n/K is at most 1/2. Row 1179 (Theorem BP) says the Jaffe-Witten gap clause needs this and the
   continuum datum of the T0 chain, and not the branch selection (BS). Row 1184: (N-phys) is the crux lemma
   (GLUE-FP) of rows 895 and 920 with other constants. All OPEN.
2. **The wall in one sentence** (`parts/gap.md` L321-322): one selective inequality at every scale between
   first passage and the seed size is missing; selective means false for a massless factor.
3. **What a tool must fail on** (test table, `parts/gap.md` L268-309): compact U(1) at weak coupling, the free
   photon, a product with a massless factor, Theorem D2 (supremum over tilts), Lemma SHEET (uniform over
   coupling fields), Proposition V (peaked weights at a first-order point), and non-local weights from
   integrated matter (so a tool must use the Markov property of the Wilson weight or first-passage data).
4. **The two posted 2D O(N) proofs** are the only all-coupling proofs of a gap in an asymptotically free
   model. The lane ported OpenAI's bracket step (rows 1009-1016, 1076-1086, 1188, 1193, 1195: fails in the
   class of all pins, the conditional abelian model is frustrated, no global non-abelian symmetry on the
   integration variables). For Ding, Huang and Yang the digest marks every key input "NONE" in 4D
   (`prior/gap-2don-proofs-read-opus.md` L96-110).

**Registry grep before choosing** (count of files among `library/gap-*.md`, `library/prior/gap-*.md`,
`parts/gap.md` that contain the term; done with one `grep -l -i` loop). Zero hits: "mass inequalit",
"colour-flavour", "induced QCD", "Savvidy", "shifted bound", "Parisi-Wu", "reflection coupling", "Eberle",
"Fredenhagen-Marcu", "holonomy flow", "Hardy", "Born-Oppenheimer", "Dirichlet-Neumann". Present (so not new by
name): Vafa 2, Zirnbauer 2, paramagnet 10, Nielsen 11, Singer 21, O'Neill 12, orbit space 24, Karabali 3,
Feynman 39, trace anomaly 17, Cheeger 6, Ollivier 5, Wasserstein 17, path coupling 2, Lieb-Robinson 3,
instanton 30, abelian projection 10, Witten Laplacian 13, Brascamp 31, van Baal 37, Zwanziger 15, Gribov 24,
Simon-Lieb 12, hypercontract 37, Knabe 23, martingale 47, Luscher 48, step scaling 19, tunnel 43,
adiabatic 13, semiclassical 18, min-max 34, variational 86.

**First screening (GUIDE; each line is a route I derived blind in this session and then found on the map).**

| Route derived blind | Where it already sits |
|---|---|
| Fixed-coupling form: a seed at one coupling of the window plus a carrier to finer cutoffs | `parts/gap.md` L26-28; set-aside method 23 (row 978) |
| Gronwall in beta: d log m / d beta bounded below; equivalent to "no zero of the lattice beta function"; action sum rule | (NOCRIT), (VIR-log) `gap-mid-max.md` L172, L207; row 859 G8 |
| Thermal form: (N-phys) is "pressure over T^4 below 3e-9 at one temperature"; coupling integration | route RB; row 934; Theorem D (f) |
| Uniform Poincare inequality of the 4D Gibbs measure gives the gap | route RF; rows 957, 968, 982 |
| One-sided renormalization inequality on tori (contraction of D under doubling) | (CAS), route RA |
| Stiffness under a twist needs a global symmetry; SU(2) has only the centre | rows 1011, 1013, 1016 (Lemma CEN+) |
| Time-independent gauge rotations in temporal gauge as the global group | rows 944-952; row 1190's list |
| The layer of time-like links as an O(4) model in an SO(4) background; Durhuus-Frohlich | rows 712, 825-834, 1139 |
| Wilson weight as a Gaussian in two-link transporters; quaternion auxiliary field | `gap-brainstorm-max.md` L329; row 996 Identity MIX; row 1194 D1 |
| Signs of real coordinates as coupled Ising gauge fields; SO(3) matrix-entry expansion | method 35 (rows 1127-1133); row 1190 |
| SO(3) x Z_2 split, Z_2 monopoles as the frustration of the conditional Ising gauge theory | rows 1155-1175 (adjoint-only forms); Mack and Petkova in row 1025 |
| Tomboulis decimation needs a sign for bond moving on the ratio | rows 1025, 1029; row 876 item 16 |
| Thin twisted torus, fractional instanton gas, adiabatic continuity | Route T, (AC'), row 842; C5 of row 697 |
| Rotation-twisted tori (non-abelian point group characters) | rows 960-965 (vargeom, rotgeom) |
| Massless photon is not protected by a symmetry in SU(2), but an adjoint-Higgs Coulomb phase shows that "only a Z_2 one-form symmetry" does not give a gap | test table last row (non-local weights); row 1017 |

So a seventh screening finds the map again. The next section picks one mechanism and works on it.

## 2. The attack: port the Ding-Huang-Yang mechanism (the posted mechanism that the lane has tabulated but not ported)

**Why this one.** OpenAI's bracket step has six port rows. For Ding, Huang and Yang (arXiv:2611.04908; all credit for
the mechanism is theirs) the lane holds a digest in loop language with the verdict "NONE" for each key input
(`prior/gap-2don-proofs-read-opus.md` L96-110), and no port row. The registry grep for the spin-language
objects used below ("block orientation", "solid angle", "good box" outside that digest) returned no file.
So I first rewrite their mechanism in spin language, then try each gauge translation.

### 2.1 The mechanism in spin language (ARGUED: my reading of their Sections 1 and 5 through the digest; I did not re-read the paper)

Write an O(3) spin as sigma = (rho e^(i theta), zeta), rho = (1 - zeta^2)^(1/2). The energy is
- beta sum over bonds of [zeta_u zeta_v + rho_u rho_v cos(theta_u - theta_v)]. Given the field rho, the angles
theta form an XY model with non-negative couplings J_uv = beta rho_u rho_v. Their z-copy of the loop soup is
the field zeta^2 in this language (Lupu's isomorphism, their (1.6)).

**Lemma G1 (PROVED, elementary).** For a real function alpha on the sites put
(R_alpha sigma)_u = (rho_u e^(i(theta_u + alpha_u)), zeta_u). Then R_alpha keeps the product measure, and

E(R_alpha sigma) - E(sigma) = - beta sum over bonds of rho_u rho_v [cos(theta_u - theta_v + alpha_u - alpha_v) - cos(theta_u - theta_v)].

So the cost of a twist is carried by the bonds with rho_u rho_v > 0 only, and R_alpha fixes the spin at every
site with rho_u = 0. Proof: the term zeta_u zeta_v does not change, and the other term is the display. QED

The three structural inputs of their proof, in this language:

- (S1) **A rigid twist with fixed points.** The twist group U(1)_z is a subgroup of the global symmetry group, and
  it has fixed points on the fibre S^2 (the poles). For N = 2 the fibre is S^1 and the action is free: no
  fixed point, no mechanism. This is the one place where N > 2 enters (digest L71-74).
- (S2) **A free collective coordinate.** Below the correlation length a block has an orientation n in S^2. By
  the global symmetry its law is uniform, at every scale and under free or symmetric boundary conditions. So
  with a probability fixed by a solid angle (a power of 1/beta, not exp(-c beta)) the block points so close
  to a pole that the conditional XY couplings across it are of order one instead of order beta. That is a
  "good box" (their Definition 5.4), and its probability does not depend on the scale.
- (S3) **A conditional abelian model with positive couplings**, so that spin-wave bounds (McBryan and Spencer)
  and positive association hold for it under every boundary condition.

Many scales then give every point a good box at some scale (their Lemma 5.7), a spin wave pays only outside
good boxes (their Section 5.2), and one coarse-graining step gives the decay.

### 2.2 Gauge translation 1: the twist with fixed points exists, and it is a zero-form twist

**Lemma G2 (PROVED, elementary; the structure is the corner formalism of row 1013, `gap-invent-selective-max.md`
L101-204, found after the derivation).** For SU(2) link variables V_l and a real function alpha on the links put
C_alpha(V)_l = r_l V_l r_l^(-1) with r_l = exp(i alpha_l sigma_3 / 2). Write V = [[z, w], [-conj(w), conj(z)]].

- (a) C_alpha keeps Haar measure, and it acts by (z_l, w_l) -> (z_l, e^(i alpha_l) w_l). Its fixed points on one
  link are the diagonal elements (w_l = 0).
- (b) For a plaquette with links 1, 2, 3, 4 in cyclic order,
  tr C_alpha(V)_p = tr(V_1 r_12 V_2 r_23 V_3^(-1) r_34 V_4^(-1) r_41), with r_ij = r_i^(-1) r_j.
  So the change of the action depends on the differences of alpha between consecutive links around each
  plaquette only. It is zero when alpha is constant on the plaquette, and zero for every alpha when the four
  links are diagonal.
- (c) In the monomial expansion
  (1/2) tr V_p = Re[z_1 z_2 conj(z_3 z_4) - z_1 z_2 w_3 conj(w_4) - w_1 conj(w_2) conj(z_3 z_4) + w_1 conj(w_2) w_3 conj(w_4)
  + z_1 w_2 conj(w_3) conj(z_4) + z_1 w_2 z_3 conj(w_4) + w_1 conj(z_2) conj(w_3) conj(z_4) + w_1 conj(z_2) z_3 conj(w_4)],
  the map shifts the phase of each monomial by the signed sum of the alpha_l over its w-factors.

Proof. (a) Conjugation keeps Haar measure, and the matrix product gives the stated action. (b) Insert
r_l^(-1) r_l between the factors and use the cyclic trace. If the four links are diagonal they commute with
every r_ij, and r_12 r_23 r_34 r_41 = 1. (c) With A = V_1 V_2 and B = V_4 V_3, (1/2) tr(A B^(-1)) =
Re[A_11 conj(B_11) + A_12 conj(B_12)], A_11 = z_1 z_2 - w_1 conj(w_2), A_12 = z_1 w_2 + w_1 conj(z_2), and the
same for B with (4, 3) in place of (1, 2). Expanding gives the eight monomials. QED

**Reading (ARGUED).** C_alpha is the exact analogue of R_alpha. The off-diagonal part w_l plays the part of
rho e^(i theta), and a smooth weak-coupling block in a smooth gauge sits at the fixed point (w small), as an O(3)
block at the pole. So input (S1) has a gauge form. It fails as a mechanism for three reasons, all on file:

1. The cost is a Dirichlet form of a zero-form (differences of alpha between neighbouring links). In four
   dimensions a twist across a shell of scale M costs of order M^2 times the coupling, not a constant. This is
   the dimension count of rows 1013 and 1016 and Lemma PC of row 1188 (cost at least lambda^2 eta^2 N).
2. Its charged observables are gauge-variant (the phases of w). Under the gauge-invariant measure the frame at
   each site is Haar distributed, so C_alpha is a rotation about a lab axis: Lemma WN of row 1013 (free
   lab-frame moves do nothing, the others cost a fixed amount per site).
3. The conditional model of the phases of w is frustrated on one plaquette: the two minus signs in (c) cannot
   be removed (Lemma HF of row 1188; row 1190). So (S3) fails for it.

### 2.3 Gauge translation 2: the one-form twist has no fixed point structure and no rigid form

The twist whose cost is scale invariant in four dimensions is a one-form twist: shift the diagonal phase,
(z_l, w_l) -> (e^(i alpha_l) z_l, w_l). By Lemma G2 (c) its cost is beta prod cos(a_l) [1 - cos(d alpha)_p] from
the first monomial, plus six terms in which alpha enters through sums over two links, not through d alpha.
Those terms are a mass form with coefficient of order beta |w|^2, which is of order one in a smooth gauge
at every beta (ARGUED: |w|^2 is of order 1/beta per link). This is the frame defect of row 1011 (Lemma FR)
and the covariant-Laplacian gap of row 1141. The mass form is removed only when the off-diagonal field
re-adjusts at all finer scales, which is a renormalization statement and not a map. A rigid form (a twist
that is a symmetry of the cell) exists for the centre only: Lemma CEN+ of row 1016. So (S1) holds for Z_2 and
for nothing continuous. The conditional Z_2 model given the SO(3) data has couplings (beta/2) |tr U_p| of order
beta, so it is rigid at weak coupling, and thick vortices live in the SO(3) data (rows 1155-1175).

### 2.4 Gauge translation 3: the free collective coordinate is missing, and this is the first failing step

**Statement (ARGUED, the point of this section).** In the O(3) model a good box has probability a power of
1/beta at every scale, because the block orientation is a free coordinate (S2). In the pure gauge theory a
block that is a ball has no free coordinate: its classical vacuum is one point modulo gauge. Every
deformation of a block at scale L that decouples something across it (a thick vortex through it, a lump, a
large-field cell in Balaban's sense) has classical action of order 1/g^2(L). So its probability is of order
exp(-c/g^2(L)) = (L/xi)^(c') in the scaling region, small at every scale below the correlation length xi, and
of order one only at L of order xi, where no expansion holds. The multi-scale step (every point in a good
box at some scale) therefore has no input: summed over scales the good-box probabilities converge and are
dominated by the last scale. This is the first failing step of the port, and it is the wall again: a
statement at order-one coupling at one scale.

Two remarks that qualify the statement.

- On periodic tori free coordinates do exist: the torons and the twist sectors. Their weights are powers of
  beta, not exponentials (row 1143: D_beta(n) = (3/2) log beta + log log beta + constant; the doubling defect
  (45/2) log beta). A twisted sector is the gauge form of a good box: with twist eaters every gluon mode has
  energy at least pi/L, so the sector is massive at its own scale. But a twist sector is a boundary condition
  of the whole torus, not a local event of a cell, and reflection positivity relates cells to tori of the same
  size only. At the lane's aspect ratio (time n, space 2n) the twisted free gluons alone give an excited sum
  of about 8 e^(-pi/2) = 1.66, far above every blind threshold. So this gives no seed (GUIDE: one-line
  arithmetic, two colours with momentum pi/L in one direction, two polarizations, two signs).
- Even a lower bound exp(-c/g^2(L)) on the probability of a smooth deformation at scale L is not on record:
  superposing a smooth field on a rough one costs the frame defect of 2.3 at every link of the core (row 1177
  (33)-(35), the obstruction to spreading a twist). Only defects whose far field is a gauge function are
  cheap, and then the cost sits on the singular set of that function: points for pi_3 (lattice-scale lumps,
  cost of order beta), sheets for the centre (thin vortices, cost of order beta per plaquette).

**What the port would need (OPEN, stated as one requirement).** A family of events G_L, one per cell of scale L,
with (i) probability bounded below uniformly in L between first passage and xi, under the Wilson law with
arbitrary outside data or in the chessboard sense, and (ii) a neutral consequence: given G_L, the influence of
the outside on the inside of the cell is reduced by a fixed factor. For O(3), (i) is the solid angle and (ii)
is Lemma G1. For the gauge theory I found no candidate for (i) that is not exponentially small in 1/g^2(L).
