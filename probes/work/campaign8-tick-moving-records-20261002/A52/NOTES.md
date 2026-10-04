# A52 notes: record-conditioned fermionic hops for light's charges

## 0. Setting and plan (2026-10-04)
- Places: corners V (even coords), links E (one odd coord; field axis = odd coord), faces F, cubes C.
- Light: one qubit per link, field sigma^a; Gauss at corners; charges = Gauss defects.
- Hop on link l = v + delta (corners v, w = v + 2 delta): t = raise_out_v(l) x (field-type Z factors).
- Commutation-sign calculus (A45/A48): theta(i,j,k) = s_ij s_ik s_jk; all 20 triples at v equal -1
  iff s_ij = -1 * a_i a_j (gauge a), i.e. iff the decorations d(i,j) (hop i carries Z on leg j at v)
  satisfy d(i,j) + d(j,i) = 1 + y_i + y_j (A45's y variables are exactly this gauge freedom).
- Plan: (1) GF(2) census over stabilizers of record directions; (2) explicit tournament (BK-type)
  construction, record-conditioned, transported by the 24 turns; (3) symbolic Pauli checks on a coarse
  torus + dense/sparse checks on 6- and 12-qubit clusters; (4) Z2 single-cube spectra vs free fermions;
  (5) decorated vs bare ring in the charge-free sector; (6) bands; (7) controls.

## 1. Census (c1_census.py, 0.25 s, 37 MB) -- CHECKED (exact GF(2))
- A45 system, fermion-consistent: C3 (body diag), D3 (body-diag line), C2' (face diag), trivial: YES.
  O, T, C4 (axis), D4 (axis line), D2' (face-diag line, contains C2z), D2, C2z: NO (lemma F: any axis half-turn).
- Strict tournaments (every pair of the six hops anticommutes, no Gauss factors): 32 for C3, 0 for D3/C2'
  (those need y-gauge factors = Gauss-parity factors B_v on some hops), none transitive (C3 forces 3-cycles).
- Transport of each of the 32 C3 tournaments to the 8 body diagonals: 0 conflicts, covariant, fermionic (32/32).
  T_{-f} is the reverse tournament of T_f (all 15 pairs flipped).
- Control: BK total order (fermionic, not C3-invariant): 16 transport conflicts; Stab(f0) assigns it 3
  different tournaments, so its record family is ill defined.
- Lemma (EXACT, trivial): any tournament T gives s_ij = -1 for all 15 pairs at v (hop i has Z on j iff T[i][j]),
  so all 20 Levin-Wen triples are -1. Transitivity is not needed for the corner phases.

## 2. The construction (EXACT) and symbolic checks (c2_symbolic.py; L=3: 0.50 s, L=4: 2.6 s, 36 MB)
- Records: every corner place holds a record locking the state |f_v> with Bloch vector along a body diagonal
  f_v in {(+-1,+-1,+-1)}. Under a turn g the content transforms f -> R_g f (soldered action rotates the Bloch vector).
- Tournament family: T_{f0} = one of the 32 C3(111)-invariant tournaments; T_{g f0} := g.T_{f0} (well defined, c1).
- Hop on link l (corners v, w = v + 2 delta, legs i at v and i' = -delta at w):
    t_l[f_v, f_w] = raise_out_v(l) * prod_{j: T_{f_v}[i][j]=1} E_{v+j} * prod_{j: T_{f_w}[i'][j]=1} E_{w+j},
  E = field operator (sigma^axis) of that link. Reverse hop = adjoint (same decorations). Support: l plus the
  two corner stars (reach 2 from the link place); depends on the two corner records only.
- Checks on coarse tori L=3,4, all 32 tournaments, uniform f0 and random body-diagonal backgrounds:
  pair rule "anticommute iff the links share a corner": 0 violations; junctions: all 20 x every corner = -1
  (540/540, 1280/1280); Gauss: hop anticommutes with the Gauss parity exactly at its two ends (0 violations).
- Covariance as a function of the records: 24 turns about a corner, 24 about a cube centre, 3 translations:
  0 mismatches (9792 hop images at L=4). Control: records held fixed while turning: 4032/4608 mismatches.
- Loop products (Z2 version, exact phases): S_p = product of the 4 hops = (+-) X-loop x 6 off-loop field factors
  (uniform background; 4-8 on random backgrounds). S_p^2 = +1; S_p commutes with every hop, every Gauss parity,
  every other S_q. Cube relation (6 faces) = +1 for every cube; plane products on the torus = +1 (L=3,4).
- Bare ring (X-loop) anticommutes with 6 off-loop hops for EVERY plaquette (486/81 at L=3): the ring term must
  carry the same decoration (S_p) to commute with charges' hops on other links.
- Lemma R (EXACT, within star-supported field-factor decorations): if every bare ring term commutes with every
  off-loop hop, then for each hop i at v, d(i,.) is constant on the five other legs (perpendicularity graph on
  them is connected), i.e. hop i is dressed only by the Gauss parity; then theta = +1. So fermions force the
  ring term to be decorated.

## 3. Numeric checks with the true U(1) operators (c3_dense.py, 1.3 s, 37 MB) -- CHECKED
- Corner star (6 link qubits, dense 64-dim): U_g t_i[f] U_g^dag = c t_{gi}[gf], max residual 1.3e-15 over
  24 turns x 8 records x 6 hops; c in {+-1, +-i} (phases; fixable by transport, see 5). Gauss:
  ||[G_v, t_i] - t_i|| = 0. Junctions: 960/960 = -1 (8 records x 20 triples x 6 orderings), residual 0.
- Controls: no record (O-covariant decorations, 20 samples): every T and corner junction +1 (lemma F).
  BK order forced C3-covariant by summing its 3 images: 10/20 junctions not scalar (residual up to 4).
  BK order with one fixed tournament for every record (no transport): covariance residual 1.000.
- One coarse cube (12 link qubits, product-operator arithmetic): 24 turns about the cube centre with the 8
  corner records turned (uniform f0 + 3 random backgrounds): hops residual <= 1.1e-15, loop operators 3.1e-16;
  corner junctions 8/8 = -1; decorated loops commute with all 48 off-loop hops; bare ring loops anticommute
  with 12-14 of 48.

## 4. Exact free-fermion check, Z2 reduction, one cube (c3b_cube_spectrum.py) -- CHECKED
- H = sum_l (i/2) A_l (B_v - B_w) on 12 qubits; sectors N = 2 (896) and 4 (2240) charges.
  Spectrum = union over the 32 flux classes of free-fermion N-particle spectra: max|diff| 2.0e-14 (N=2),
  4.8e-14 (N=4) [first run, full complex diag, 7.95 s, 490 MB -- over the 300 MB guide]; lean rerun via
  eig(-M^2): 1.0e-7 / 1.3e-7 (sqrt near zero), 3.40 s, 232 MB. Versus hard-core bosons: 0.68 / 0.64 (differ).
- Control: bare hops X_l (1 - B_v B_w)/2 = hard-core bosons (2.7e-14, 3.6e-14), not fermions (0.68, 0.64).
- 4 tournaments x (8 uniform records + 3 random backgrounds): N=2 spectra identical to f0 (max diff 0.0).
- Zero-flux sector (all six S_p = +1, N=2, dim 28) = free fermions with all hoppings +1: 3.6e-15.

## 5. Records are invisible; the ring term in empty space (c4_ring_equiv.py, 41.7 s, 50 MB)
- Lemma V (EXACT): for two tournaments T, T' at a corner, q_jk = T[j][k] xor T'[j][k] is symmetric in (j,k)
  (since T[k][j] = 1 - T[j][k] for both). CZ_jk in the field basis maps raise_j -> raise_j E_k. So
  V = prod_{q_jk = 1} CZ_jk (star links of that corner) maps every hop (and every loop product) of T to that of T'.
  Any two record backgrounds and tournament choices give unitarily equivalent laws; V is diagonal in the
  field basis and commutes with every Gauss operator. CHECKED: torus L=4, six random pairs of backgrounds and
  tournaments: 0/1152 mismatches (456-528 CZ gates); dense star, f0 -> each record: residual 0.
- Consequence: the law on a uniform background H_f is exactly invariant under beta_g = V_{gT,T} o (soldered turn g),
  an exact group action (V's compose additively). So "records" buy exactly what a turn-plus-two-place-diagonal
  relabeling buys; A48's classification (on-site relabelings) does not cover it.
- Hop phases: covariance holds up to phases {+-1, +-i}; on-site link rotations exp(i phi E/2) multiply raise ops by
  exp(i phi) and the loop products consistently, so phases are removable (law defined by transport is exactly
  covariant; stabilizer of (oriented link, body-diagonal records) is trivial or one end-swapping half-turn).
- Ring term, charge-free (ice) sector, U(1) spin-1/2 links, BFS over states reachable by ring flips from a
  divergence-free start: decorated flips carry negative signs on ~half the edges, but there are 0 sign
  inconsistencies: tori 2x2x2 (864 states, complete), 2x2x3 (34080, complete), 2x2x4 (250000 capped), tournaments
  T0, T31, uniform and random records. So a diagonal sign function chi exists with chi L_p chi = W_p: in empty
  space the decorated ring law has the same spectrum and the same field-basis correlations as the bare ring law.
  chi cannot be a finite-depth local circuit if bosonic- and fermionic-charge Coulomb phases are distinct
  (COMPARATOR: Wang-Senthil E_bM_b vs E_fM_b); not tested here.

## 6. Axis records (c6_axis_search.py, adapted from A50 t2_search; <= 22 s, 79 MB each) -- CHECKED (search)
- C3 control: vlinks 12/12 and links-only 12/12 starts reach all 20 junctions = -1.
- C4z links-only (record on the corner): junctions scalar but 4 T-junctions stuck at +1 (best residual 5.29, 25 starts).
- C4z with a free corner qubit (record elsewhere): 0/25 scalar (best 4.52). D4z: 0/25 (best 5.66).

## 7. Explicit rule (c7_explicit.py, 0.18 s) -- EXACT, CHECKED
- T_f (record f a body diagonal; R_f = right-handed 120-degree turn about f): the hop along leg d carries the field
  factor of leg d' iff  f.d > 0 > f.d'  ("out-hops carry all three in-legs"), or f.d, f.d' have the same sign and
  d' = R_f d  ("within each triple, the next leg in the turn order"). Equals transported T0 for all 8 f; manifestly
  covariant (R_{gf} = g R_f g^-1); a tournament for every f. Example f0=(1,1,1): +x carries {-x,-y,-z,+y}; -x carries {-y}.
- Decorated ring at the xy plaquette (0,0,0)-(2,0,0)-(2,2,0)-(0,2,0), uniform f0: off-loop field factors on legs
  (0,0,0)+z; (2,0,0)+z,-z; (2,2,0)-z; (0,2,0)+y,-x. Reach sqrt5 from the face place (bare ring: 1).
- Lemma R, general local form (EXACT): if a hop's (finitely supported) field-factor set D has even overlap with every
  plaquette not containing its link, then dD is supported on the 4 plaquettes around the link and closed, so
  dD = 0 or d(1_link); compact-support cohomology of Z^3 vanishes in degrees 1, 2, so D = own link + Gauss
  parities -> boson. Fermionic link-decorated charges therefore always need a decorated ring term.

## 8. Bands (c5_bands.py, 7.3 s, 51 MB) and flux sectors (c3b) -- EXACT formulas, CHECKED
- Cube (Z2, N=2): S_p=+1 sector = free fermions at zero flux (3.6e-15); S_p=-1 sector = free fermions with pi
  through every face (2.5e-15). Single-particle levels: zero flux {-3,-1x3,1x3,3}; pi flux +-sqrt3 (4 each).
- Lattice, hopping t, coarse spacing a: zero flux: one band -2t sum cos k, no nodes, isotropic mass 1/(2ta^2) at the
  bottom. Pi flux: |E| = 2t sqrt(sum cos^2 k) (deviation 5.8e-15), two 4-fold nodes per magnetic zone at
  (pi/2,pi/2,+-pi/2), isotropic cone speed 2ta (same along 5 directions) = Kawamoto-Smit doubling (2 Dirac = 4 Weyl).
- Which flux: the sign of the decorated ring coupling (mean field, ARGUED). On the cubic lattice the ring sign is a
  diagonal gauge choice for light (period-2 sign pattern with delta h = 1 on every plaquette), so light is indifferent.
