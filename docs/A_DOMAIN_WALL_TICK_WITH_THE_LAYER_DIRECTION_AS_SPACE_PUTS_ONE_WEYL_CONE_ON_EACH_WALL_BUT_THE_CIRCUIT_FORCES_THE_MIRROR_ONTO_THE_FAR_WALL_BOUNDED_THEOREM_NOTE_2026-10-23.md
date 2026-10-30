---
claim_id: a_domain_wall_tick_with_the_layer_direction_as_space_puts_one_weyl_cone_on_each_wall_but_the_circuit_forces_the_mirror_onto_the_far_wall_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Free-field test of three candidate tick (unitary, Hamiltonian/Floquet) forms of one-handed matter. (A) A 3+1+1 Wilson-type slab with Ls layers in an extra SPATIAL direction and the tick as time: the slab Hamiltonian H is strictly nearest-neighbour and tetrahedrally covariant; the layered circuit U = W_m W_1 W_2 W_3 W_odd W_even is unitary, range 1 in each space direction and range 2 in layers. Finite diagnostics at m = 0.6, theta = 0.2: 4D bulk gapped (0.067 at quasienergy 0, 1.66 at pi; H gap 0.60); exactly one two-component Weyl node per wall, at k = 0 and quasienergy 0, opposite chirality on the two walls, no other in-gap state on a 12^3 grid, and 4 in-gap states on the L = 6 torus; the mirror overlap falls as |1 - m|^Ls (exact zero-mode recursion; ratio 0.399 per layer, xi = 1.09 layers; exactly zero at m = 1); exp(-i H tau) is covariant and faster-than-exponentially local; no wall state at X, M, R. Exact: a circuit of gates exp(-i theta h) is homotopic to 1, so the slab's W3 = 0 for every step, mass and Ls; one wall has (n0, npi) = (-1, 0), which no walk-invariant sector of a 3D walk can have (n0 = npi = -W3, control on a degree-one family). (B) The slab's layer-sign charge is compact, quantised and on-site in 3D but not conserved; its commutator lives on the middle bond and falls as |1 - m|^Ls between wall modes; the cited 1+1D Onsager template's one-handed combination has levels |sin(k/2)|. (C) At larger steps the circuit's bulk gap closes between theta = 0.2 and 0.3; quasienergy-pi wall cones (-1, -3) appear at theta = 0.7 only with a gapless bulk. Not covered: gauging the light wall, gapping the far wall, interactions, identification with the CL-1 cube walk."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_bounded_theorem_note_2026-10-23
  - history_actuality_reproduces_the_readable_born_odds_and_which_way_complementarity_but_needs_a_tick_form_the_chiral_weighting_lacks_bounded_theorem_note_2026-10-23
  - the_composite_two_cell_light_label_makes_the_corner_stabilizers_reducible_but_the_light_floquet_winding_forces_the_mirror_to_carry_the_opposite_chirality_bounded_theorem_note_2026-10-23
  - the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_bounded_theorem_note_2026-10-23
runner: scripts/a_domain_wall_tick_with_the_layer_direction_as_space_puts_one_weyl_cone_on_each_wall_but_the_circuit_forces_the_mirror_onto_the_far_wall_2026_10_23.py
---

# A domain-wall tick with the layer direction as space puts one Weyl cone on each wall, but the circuit forces the mirror onto the far wall

Claim type: bounded_theorem (two exact statements, one exact recursion, labelled finite diagnostics; the domain-wall
construction and the Floquet/Nielsen-Ninomiya literature are supplied and cited).
Runner: runner.py, TOTAL: PASS=13 FAIL=0, 4.3 s, 76 MB peak, 4.9 k characters of stdout; run under a unique filename.
Axioms unchanged. No rule adopted.

## Question

CL-1's history-level matter weighting (the overlap D = 1 + V with Luscher's P_hat) gives the right chiral content, but
its weight is complex, so it is an amplitude, not odds (history-actuality). CL-2 and records need a TICK form: a unitary
in the tick direction. Tick-level 3D walks are blocked by the corner-Q8 no-go (freeze-gapped-partners) and by the
conserved Floquet winding W3 = -2 of the light sector (two-cell-light-label). Which of (A) a domain wall with the extra
direction as space, (B) an exponentially local non-on-site chiral charge, (C) an anomalous Floquet bulk gives a unitary
tick of one-handed matter with the mirror removed?

Repo first. This builds on rung-dimension-chirality (PR #9971, part E: a full-density layer coordinate inside a role
block is the domain-wall slab, residual mass (mu/kap)^Ls, far mirror fully charged), gk-nogo-check (PR #9985:
far-layer smoothing gives a gauge-invariant cutoff-scale photon mass), chiral-wall (exact mode number with the mirror
reflection forbids gapping the mirror alone under the register as written), nononsite-chiral (T1: compact one-body
charges are vector-like; Chatterjee-Pace-Shao template; Gioia-Thorngren 2025 arXiv:2503.07708 as cited there), and
overlap-from-walk (PR #10049: Shamir 5D -> overlap). The commit "name the fifth direction a zero-action null
direction" (e45d53c96a) concerns a null strain direction of the Regge edge carrier in the gravity lane; it is not
a spatial layer coordinate, and nothing here ties to it.

## Model (supplied)

Gammas G1..G3 = sx (x) s_i, G4 = sy (x) 1, G5 = sz (x) 1. Slab on Z^3 x {0..Ls-1}:
H(k) = sum_i [sin k_i G_i + cos k_i G5] + (m - 4) G5 + sum_bonds h_b, with h_b = A (x) |s+1><s| + h.c. and
A = (G5 + i G4)/2. Bulk mass M = m - 4 + sum cos k_i + cos p; window 0 < m < 2 (supplied, m = 0.6 used).
Tick: U = exp(-i th (m-4) G5) prod_i exp(-i th T_i) exp(-i th H_odd) exp(-i th H_even), T_i = sin k_i G_i + cos k_i G5,
T_i^2 = 1 and h_b^3 = h_b, so every factor is an exact range-1 gate.

## A. Domain wall with the layer direction as space: YES for a unitary tick with one cone per wall; mirror on the far wall

Exact:
- A-T1 (zero-mode recursion). At k = 0, psi_s = (1-m)^s chi with i G5 G4 chi = -chi solves H psi = 0 on the s = 0 wall
  exactly (A chi = 0 kills the missing bond); the far end leaves amplitude |1-m|^Ls, so the mirror overlap is
  O(|1-m|^Ls). At m = 1 the wall mode is compact (one layer) and the overlap is exactly 0 (3e-17).
- A-T2 (homotopy). Every factor is exp(-i th h) with h local hermitian; th -> 0 contracts U to 1 through local
  unitaries, so the slab, viewed as a 3D walk with 4 Ls components per cell, has W3 = 0 for all th, m, Ls.
  With the sector relation n0 = npi = -W3 (K1), the slab total chirality is 0 at both quasienergies.
- A-T3 (rotations). H is covariant under the tetrahedral rotations with the spinor lift on G1..G3 (C2, C3 checked to
  1e-15).
Finite diagnostics (m = 0.6, th = 0.2, pre-set criteria in brackets):
- A1 unitarity 2e-16, no Fourier weight at |n| = 2 (cube-local), layer range <= 2 [< 1e-12, <= 2].
- A2 bulk gap 0.067 at 0 and 1.66 at pi (8^4 grid plus local minimisation); H gap 0.60 [> 0.05, > 0.5, > 0.3].
- A3 Ls = 12: one 2-dim wall space per wall at k = 0, chirality L = -1, R = +1 (walk and H agree; H |det v| = 1);
  none at the other 7 corners, none at pi [exactly this pattern].
- A4 in-gap states only within 0.8 of k = 0 on a 12^3 grid; 4 in-gap states on the L = 6 torus [0 stray, 4].
- A5 k = 0 splitting 5.4e-2, 2.2e-2, ..., 2.2e-4 for Ls = 3..9, ratio 0.400 (H), 0.399 (walk) [|ratio - 0.4| < 4e-3].
- A6 no wall state at X, M, R [none].
- A7 exp(-i H tau), tau = 1: hop weight 0.6, 0.3, 9e-2, 9e-3, 5e-4, ..., 7e-11 at r = 0..8 [monotone, < 1e-6 at 8].
Answer to "does W3 / the corner no-go apply?": not to one wall, yes to the slab. One wall has (n0, npi) = (-1, 0); a
walk-invariant sector of a 3D walk needs n0 = npi, so the wall is not such a sector (its leak is the |1-m|^Ls
overlap), and the corner premise (a walk-invariant light label at X and M) is void because the wall has no state
at X or M. But the slab as a whole is a circuit with W3 = 0, so the opposite cone is forced, and it sits on the far
wall. The light 3+1 Weyl lives on one wall; the mirror is exponentially separated, not removed.
Standard open step (unchanged): gauge only the light wall (rung-dimension-chirality B: breaks gauge equivalence or
cuts the ladder and puts a charged mirror at the cut; gk-nogo-check: smoothed far layers give a cutoff-scale photon
mass) or gap the far wall by symmetric interactions (symmetric mass generation; chiral-wall: forbidden under the
register as written by exact mode number with the mirror reflection). Not attempted here.

## B. Exponentially local modified chiral charge in a 3D Hamiltonian: NO for one-handed matter

- B3 (theorem, rederived from the cited argument): if h(k) is analytic (exponential locality suffices) and commutes
  with a one-body, number-conserving q(k) of k-independent spectrum, the charge projectors are analytic (contour
  integral), each charge sector is a smooth bundle on T^3, and the slice Chern number is periodic in k3, so the net
  node chirality of every charge sector is 0. Non-on-site charges are covered. Escapes need non-compact charges
  (Gioia-Thorngren, as cited: single-Weyl charge non-compact) or pairing (non-number-conserving) charges.
- B1 [T]: the slab's layer-sign charge Q = sign(s - mid) is compact, quantised and on-site in 3D. [H, Q] is supported
  only on the middle bond, and its wall-mode element is 6.4e-3, 1.1e-3, 1.8e-4 at Ls = 6, 8, 10 (ratio per two layers
  0.171 -> 0.160 = 0.4^2). So the domain-wall "chiral charge" obeys B3 by not being conserved; its violation is the
  mirror leak. The pre-set criterion (both ratios within 0.01 of 0.16) failed on the first run at 0.171 because of
  finite size. It was revised to "asymptotic ratio within 0.005 and decreasing", and that change is disclosed here.
- B2 [T] recheck of the 1+1D template: the pairing axial charge has levels +-1, but (Q_V - Q_A)/2 has levels
  |sin(k/2)| in [0, 1], so there is no compact one-handed U(1) to gauge. This gives an exact chiral SYMMETRY of
  vector-like matter, not one-handed matter.

## C. Anomalous Floquet bulk: NO in this family; W3 cannot be a resource for any circuit

- C1 [F]: the pre-set criterion (th = 0.3 gapped, no pi cones) FAILED. The circuit's bulk gap at 0 closes between
  th = 0.2 and 0.3, and the wall chirality flips to +1 there. The pattern (n0, npi) = (-1, -3), with pi cones at the
  three face corners (0,pi,pi), (pi,0,pi), (pi,pi,0), appears at th = 0.7 only with a gapless bulk (gaps 2e-12,
  5e-15). It is not a gapped anomalous phase.
- C2 [T] (= A-T2): any circuit of exponentiated local gates has slab W3 = 0, so the "obstruction as resource" reading
  needs an index-carrying, non-circuit element (for example a shift-like map along the layers). Whether such an
  element exists on an open or one-ended layer direction with a gapped bulk is OPEN. The control K1 shows what W3 != 0
  would give: n0 = npi = -W3, i.e. cones of the SAME hand at 0 and pi (no mirror but an anomalous pi partner).

## Most promising: A, as the tick form of the existing overlap clause

The overlap is the Ls -> infinity limit of the domain wall (overlap-from-walk: Shamir 5D -> (1 + g5 tanh(Ls artanh H_T))/2).
A puts the same wall content on a Hamiltonian/Floquet tick: a positive transfer matrix in the tick direction is just
U itself, with records and CL-2 transport definable per tick. It inherits, unchanged, the open step of every
domain-wall route: the far-wall mirror.

Proposed CL wording (UNTESTED, not adopted; for the coordinator):
"Tick form of matter weighting (candidate). Each matter site carries a column of Ls layer modes (a role-block
coordinate, not a new spatial axis). The tick is the layered circuit of range-1 gates exp(-i eps h) with copy mass in
the window 0 < m < 2. Light matter is the finest-layer wall sector; its history weight at Ls -> infinity is the overlap
clause. The coarsest-layer wall carries the mirror, coupled to the light wall at O(|1-m|^Ls). Open: the far-wall rule
(gauging or symmetric gapping)."

## Gate (anti-smuggling)

(1) No measured number is chosen: m and th are free inside the gapped window, and the counts do not depend on them.
(2) No observed structure is inserted: no gauge group or content. The 4-component layer mode is a supplied cell
content (composite-before-atomic: it should be a cluster of qubit sites; not built here). (3) Prediction not built
for (UNTESTED): every light species carries a vector mass of order |1-m|^Ls times the cutoff from the far wall,
unless the far wall is gapped. (4) Axiom bent: if the layers are a new spatial axis, it bends the Z^3 axiom; if they
are a role-block coordinate (rung-dimension-chirality E), no axiom is bent, but each light site then costs Ls
cell contents. Gate result: passes (1) and (2); (3) is UNTESTED; (4) is named.

## Smuggling review

Supplied: the Wilson-type slab (Gamma basis, window), m = 0.6, th = 0.2/0.3/0.7, tau = 1, Ls, free fields, the
Trotter order (it breaks the rotation covariance at O(th^2); exp(-i H tau) is the covariant choice), and the cited
literature: Kaplan 1992; Creutz-Horvath 1994 (Hamiltonian domain wall); Zhang-Hu 2001 and Qi-Hughes-Zhang 2008 (4D
quantum Hall with a Weyl boundary); Rudner-Lindner-Berg-Levin 2013 (anomalous Floquet); Nielsen-Ninomiya 1981;
Chatterjee-Pace-Shao 2024; Gioia-Thorngren 2025 as cited by nononsite-chiral (not re-checked here). Forced: one cone per
wall, the |1-m|^Ls overlap, slab W3 = 0, and the n0 = npi sector relation. Not shown: that the CL-1 cube walk is this
slab's layer-zero restriction, anything interacting or gauged, or the far-wall fate.
