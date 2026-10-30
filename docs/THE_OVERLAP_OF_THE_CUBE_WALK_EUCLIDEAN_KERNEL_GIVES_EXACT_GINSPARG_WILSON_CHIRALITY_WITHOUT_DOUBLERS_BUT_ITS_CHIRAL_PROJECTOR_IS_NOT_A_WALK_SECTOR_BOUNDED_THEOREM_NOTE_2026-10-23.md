---
claim_id: the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Free and fixed-U(1)-background lattice Dirac operators built from the Euclidean (space x tick) form of the Wilson-type copy-mass cube walk, X = D_W - m0 on Z^4. Exact: for any g5-hermitian kernel, V = g5 sign(g5 X) is unitary and D = 1 + V obeys the Ginsparg-Wilson relation g5 D + D g5 = D g5 D; conversely GW plus g5-hermiticity forces V unitary. The 3+1 tick unitary U(K) itself is not such a V (g5 commutes with its hop). Finite diagnostics: on the 12^4 zone D vanishes only at k = 0 for 0 < m0 < 2 (one Dirac field; 15 doubler corners at |D| = 2; also with tick weight 0.5, m0 = 0.6); the count is 1, 5, 11, 15 for m0 = 1, 3, 5, 7; position-space decay rate 0.72 per taxicab step (free), 0.91 in a Q = 1 2D background; the Chebyshev form X P_n(X^+X) has strict range 2n+1 and error falling at rate >= ln rho = 0.29 per step; the Shamir domain-wall 5D operator (strictly nearest-neighbour) gives (1 + g5 tanh(Ls artanh H_T))/2 to 1e-15 with GW defect falling from 1e-2 (Ls = 4) to 3e-9 (Ls = 16). In U(1) backgrounds (2D 10^2, 4D 4^4) GW holds to 1e-14, zero modes are exactly chiral, |index| = |Q|; Luscher's P_hat = (1 - g5_hat)/2 has rank 100 at Q = 0 and 101 at Q = 1; the 2D 3-4-5-0 indices are -e and the anomaly sums to zero. Exact arithmetic: the 16 has sum Y = sum Y^3 = SU(3)^2 Y = SU(2)^2 Y = 0. Not covered: a chiral walk (tick) realisation, reflection positivity of the chiral theory, non-abelian chiral existence (open in the literature), the composite-cell turn charges inside the overlap, interacting dynamics."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_composite_two_cell_light_label_makes_the_corner_stabilizers_reducible_but_the_light_floquet_winding_forces_the_mirror_to_carry_the_opposite_chirality_bounded_theorem_note_2026-10-23
  - the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_bounded_theorem_note_2026-10-23
  - the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_bounded_theorem_note_2026-10-23
runner: scripts/the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_2026_10_23.py
---

# The overlap of the cube walk's Euclidean kernel gives exact Ginsparg-Wilson chirality without doublers, but its chiral projector is not a walk sector

Claim type: bounded_theorem (exact algebra plus labelled finite diagnostics; literature results cited as supplied).
Runner: runner.py, TOTAL: PASS=19 FAIL=0, 2.2 s, 225 MB peak, 3.0 k characters of stdout; run through
scripts/runner_cache.execute_runner under a unique filename (status ok, exit 0). Axioms unchanged.

## Question

Does the campaign's walk supply an overlap (Ginsparg-Wilson) Dirac operator with exact lattice chirality and
no doublers, is it local in the owner's sense (influence passed site to site), and does it get past the
FREEZE obstructions (corner Q8 Schur no-go; light Floquet winding W3(light) = -2)?

## Repo check

- On main: ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28 (GW is sufficient, not necessary, for
  a lattice index; this note does not contradict it) and AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26
  (staggered trace identity, no overlap construction). No overlap construction from the walk exists on main.
- Open PRs used: #9971 (rung ladder as a domain-wall direction, exact inflow, charged tower), #9985
  (Grabowska-Kaplan far layers: Nielsen-Ninomiya count passes, cutoff-scale photon mass), #10025
  (rung-separated mirror). This note supplies the vector-like overlap underneath them and does not touch
  their chiral-gauging verdicts.

## Which form, and why

4D Euclidean on space x tick. The GW relation, the index and the anomaly are properties of the Euclidean
fermion action over histories, and the tick is a lattice direction like space. The walk enters through its
Euclidean kernel: the Wilson form D_W - m0, whose copy mass is the walk's Wilson-type copy mass. This
identification (and isotropy between tick and space) is SUPPLIED; A2 shows the result survives tick weight 0.5.

## A. Construction and zone count

- A1 (exact). For any g5-hermitian kernel X, V = g5 sign(g5 X) = X (X^+X)^(-1/2) is unitary with
  g5 V g5 = V^+, and D = 1 + V obeys GW exactly. Conversely GW for D = 1 + V means V g5 V = g5, which together
  with g5-hermiticity says V is unitary. So "an overlap operator" is the same thing as "a g5-hermitian unitary".
- A0 (exact). The 3+1 Wilson-Dirac tick U = exp(-i eps H) is not such a V: g5 commutes with the hop
  alpha.sin K, so g5 H g5 != -H (residual 0.99 at eps = pi/4). V must come from the Euclidean history kernel.
- A2-A5 (finite diagnostics, 12^4 zone). For 0 < m0 < 2, D vanishes only at k = 0; the 15 doubler corners
  have D = 2 (lifted to the cutoff); GW holds to 9e-16 at all momenta; near k = 0, D = i kslash/m0 + O(k^2).
  The light-corner count is the number of corners with 2n < m0: 1, 5, 11, 15 for m0 = 1, 3, 5, 7. So one
  light species needs the copy-mass window 0 < m0 < 2 (with tick weight c_t: 0 < m0 < 2 c_t).

## B, C. Locality and the site-to-site reading

- B1. The free kernel decays as exp(-0.72 d) in taxicab distance d (12^4 and 10^4 agree to 0.01).
- C1 (exact structure, numerical rate). X^+X has taxicab range 2. A degree-n Chebyshev polynomial
  V_n = X P_n(X^+X) is therefore a sum of products of at most n neighbourhood steps, range 2n+1, and its error
  falls as rho^(-n), rho = (sqrt b + sqrt a)/(sqrt b - sqrt a) from the spectral range [a,b] of X^+X (measured
  rate 0.32 >= ln rho = 0.29). Hence |D(x)| <= C rho^(-d/2) (C2: bound 0.14 <= measured 0.72). This is the
  Hernandez-Jansen-Luscher locality mechanism (supplied for gauge fields; here checked free and in a background).
- C3 (exact match). The Shamir domain-wall operator (Kaplan 1992) is strictly nearest-neighbour in five
  dimensions. With the Pauli-Villars ratio, the boundary operator equals (1 + g5 tanh(Ls artanh H_T))/2,
  H_T = g5 D_W (2 + D_W)^(-1), to 6e-16. Its GW defect falls 1.2e-2, 7.8e-5, 3.0e-9 at Ls = 4, 8, 16: the
  overlap (Shamir kernel) is the Ls -> infinity limit.
- Reading for the owner's wording. Both realisations pass influence site to site: the polynomial form is n
  neighbourhood steps with weight falling geometrically in n, and the domain-wall form is a strict
  neighbour rule in a fifth direction whose bulk modes are gapped. The 4D tail comes from integrating out that
  gapped bulk, as a Yukawa tail comes from a massive field. No instantaneous long-range coupling enters.
  Whether the fifth direction is the zoom-rung ladder of #9971 is open; #9971 finds that bounded speed makes
  the coarse rungs a charged tower, which is a separate cost.

## D. Exact chirality, index, Luscher projector, anomaly sums

- D1, D6. U(1) backgrounds with uniform flux: 2D 10^2 with Q = 1, and 4D 4^4 with fluxes (1,1) in the (12)
  and (34) planes, Q = 1. GW holds in the background to 5e-15 and 2e-14. Each has one zero mode with g5 = -1
  exactly, so |index| = |Q| (Hasenfratz-Laliena-Niedermayer 1998 index theorem, supplied and observed).
- D2 (exact integers). Luscher's g5_hat = g5(1 - D) squares to 1, and P_hat_L = (1 - g5_hat)/2 has rank 100
  at Q = 0 but 101 at Q = 1 (Tr g5_hat = 2 x index). The chiral split depends on the gauge field and changes
  rank between topological sectors.
- D3. Exponential locality persists in the Q = 1 background (rate 0.91).
- D4 (doubler control). With m0 = 3 in 2D, the two one-pi corners come back light with opposite chirality and
  the index becomes -1 + 2 = +1, so the doublers are exactly what the index counts.
- D5 (2D chiral U(1), 3-4-5-0). The measured indices for U^e are -e for e = 3, 4, 5. The left-minus-right
  sum of e x index is 0, and the anomaly density sum_f s_f e_f tr g5 D_f(x,x) sums to 0 to 2e-13. Pointwise it
  leaves a zero-sum remainder of 1e-3, which is the divergence term in Luscher's cohomology result (supplied).
- D7 (exact fractions). The 16 of one family, taken as left-handed Weyl fields, has sum Y = 0 and sum Y^3 = 0
  (Luscher 1999's abelian condition for an exactly gauge-invariant chiral measure on the lattice), and its
  SU(3)^2 Y and SU(2)^2 Y sums are also 0. So U(1)_Y is anomaly-free for the 16, and an abelian Luscher theory
  exists for it. Non-abelian nonperturbative existence is NOT claimed; it is open in the literature.
- D8 (arithmetic flag). FREEZE's light content per node is L with q = 2 and R with q = 1. As left-handed Z3
  labels that is {2, 2}, with sum q = sum q^3 = 1 mod 3 per family. This matters only if the turn were gauged;
  it is a global lattice rotation, and its 't Hooft anomaly is allowed. It cancels for N_fam = 0 mod 3. The plain
  Z^4 overlap does not carry these composite-cell turn charges (its light Weyl transforms spinorially under the
  3-fold turn), so combining the overlap with the composite cell is open.

## Verdict

- YES, for a vector-like theory. The Euclidean form of the copy-mass cube walk gives an overlap operator with
  exact GW chirality, one light Dirac field and no doublers (for 0 < m0 < 2), and exponential locality. It is
  realised site to site, either as n neighbourhood steps or as the Ls -> infinity limit of a strictly
  nearest-neighbour fifth direction. Nielsen-Ninomiya (1981) is evaded in the standard way (Luscher 1998): the
  exact chiral symmetry is the GW-deformed one, not an on-site g5.
- CHIRAL: only as a Euclidean (history) theory. One left-handed Weyl per field with no mirror is obtained by
  restricting the field space to the range of P_hat (Luscher 1998/99), and this is consistent for anomaly-free
  U(1) content; the 16's U(1)_Y passes. This MEETS the measured comparator (one left-handed Weyl per field, no
  mirror at low energy) in the Euclidean sense for abelian gauge fields.
- It does not evade the walk obstructions; it steps outside their hypotheses. W3 and the corner Q8 theorem
  apply to walk-invariant sectors of a 3+1 tick with on-site rotation action. P_hat is not such a sector: it is
  a projector on histories, built from D (which contains the tick direction), and its rank changes with gauge
  topology (D2). A walk-invariant sector has a fixed rank. No 3+1 tick (positive transfer matrix) is known for
  the chiral overlap theory, and none is supplied here.
- Effect on the chirality wall. The wall MOVES from "no local lattice chirality" to a precise price. The light
  Weyl content is obtained if (i) the rule may be exponentially local (the owner's neighbourhood-of-influence
  reading, realised site to site) and (ii) the chiral selection may be a history-level, gauge-field-dependent
  projection rather than a sector of the tick. Item (ii) bends the update reading of the axioms (the rule is no
  longer only a tick), and that is an owner decision. The tick-level wall (W3, corner Q8) is unchanged.

## Anti-smuggling gate (candidate rule: "matter histories are weighted by the overlap of the cube walk's
## Euclidean kernel; chiral fields are the range of P_hat")

1. No measured number: PASS. m0 is chosen in a window (0, 2), not at a value; one species is the comparator,
   so the window choice is labelled SUPPLIED.
2. No observed structure by name: PASS for the vector-like rule. For the chiral rule it is INCOMPLETE: which
   fields are left-handed and their U(1) charges are inputs; the rule supplies only the consistency condition
   (anomaly freedom).
3. Prediction not built in: the overlap gives the exact integer index and an anomaly coefficient equal to the
   continuum one (D1/D5/D6). That fixes the pi0 -> 2 gamma coefficient (a measured process), but the runner does
   not compute that rate, so this is UNTESTED here. It also predicts that the chiral content must be anomaly-free
   (the 16 passes; this is a postdiction).
4. Axioms bent: nearest-neighbour admissibility becomes neighbourhood influence with an exponential tail (owner
   intent 2026-10-23); and for the chiral part, the update axiom becomes a history-level rule. Not proposed as
   an AX entry here; it is logged as a candidate for the owner.

## Supplied (cited, not derived)

Neuberger 1998 (overlap operator); Luscher 1998 (exact lattice chiral symmetry from GW), Luscher 1999 (abelian
chiral gauge theories with anomaly-free charges); Kaplan 1992 (domain-wall fermions); Nielsen-Ninomiya 1981;
Hernandez-Jansen-Luscher 1999 (locality for smooth fields); Hasenfratz-Laliena-Niedermayer 1998 (index).

## Not covered

A chiral tick or Hamiltonian realisation; reflection positivity of the chiral theory; non-abelian chiral
existence; the composite-cell turn charges inside the overlap; admissibility bounds for rough fields;
interacting dynamics; whether the zoom-rung ladder can serve as the fifth direction without #9971's tower.
