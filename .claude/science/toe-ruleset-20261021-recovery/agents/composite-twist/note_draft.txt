---
claim_id: the_cell_taste_doublet_is_a_geometric_tetrahedral_twist_giving_a_one_qubit_chiral_turn_charge_walk_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Free bands on CL-1's 2^3 cell (one fermion mode per site, face phase -1, Bloch over 2Z^3, 8 cell states) under the 12 tetrahedral rotations T kept by the copy mass. (A) CL-1's own Margolus tick is vector-like in turn charge: each chirality's taste E splits into w + wbar, T allows an L-R mass per character pair, the copy-mass light family has q_L = q_R and the T-invariant mass mu gaps it; the massless tick's exact internal symmetry algebra is dim 1 (not 8), so no twisted turn is a symmetry of it. (B) New exact member (composite TWIST): U(K) = f + i(h1 tau1 + h2 tau2 + tau3 g.sigma) with sigma = cell spin, tau = cell taste doublet, CL-1 chirality eta a spectator, and the atomic TWIST functions of the cell momentum. It is unitary, a pure nearest-cell hop, exactly T-covariant under the plain site permutations (the twist is the cell's own geometric taste action, nothing supplied), not O-covariant. Nodes exactly K = 0 (quasienergy 0) and the cell corner R (quasienergy pi), 8-fold each; Weyl chirality = tau3 at both; every L has q = 2, every R q = 1; no T-invariant on-cell L-R term exists; on-cell filter leak O(K^2). Light content 4 L + 4 R. Not covered: interactions, links, walks outside this Clifford form, a cube-local circuit decomposition."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_cube_tastes_are_two_doublets_and_no_symmetry_protects_a_family_triplet_bounded_theorem_note_2026-10-22
  - two_qubit_site_dirac_walk_is_vector_like_and_a_tetrahedral_twist_gives_a_chiral_turn_charge_with_a_pinned_pi_doubler_bounded_theorem_note_2026-10-22
  - no_tested_band_carries_both_the_light_turn_charge_and_the_momentum_separated_mirror_bounded_theorem_note_2026-10-22
runner: scripts/the_cell_taste_doublet_is_a_geometric_tetrahedral_twist_giving_a_one_qubit_chiral_turn_charge_walk_2026_10_23.py
---

# The cell's taste doublet is a geometric tetrahedral twist: a one-qubit chiral-turn-charge walk

Claim type: bounded_theorem (exact free-band statements). Runner: runner.py, TOTAL: PASS=15 FAIL=0, 0.9 s,
139 MB peak, stdout 4.0 k characters; run through scripts/runner_cache.execute_runner under a unique filename
(status ok, exit 0). Axioms unchanged; one mode per site.

## Question

two-qubit-cell found that TWIST (a flavour qubit carrying the Z3 character of the tetrahedral rotations) gives
light Weyls with a chiral turn charge (L: q = 2, R: q = 1), forbids every L-R mass, and has a pinned pi doubler
at R, but it puts a second qubit on each site. families-from-tastes found that the 2^3 cell's tastes are E + E,
and under T each E splits into w + wbar. Composite before atomic: can the taste doublet stand in for the flavour
qubit on one-qubit sites?

## A. CL-1's own tick is not composite TWIST (exact)

- A1. The cell is rebuilt, and all 24 cube-centred rotations are tick symmetries up to a +-1 site gauge. T is 12
  of them.
- A2. Correction to families-from-tastes A11. Over 8 momenta, the massless tick's commutant has dim 1. Three
  momenta give a spurious 8. Neither the chirality chi nor the taste doublet is conserved away from K = 0
  (||[chi, U(k)]|| >= 1.7).
- A3. Under T, L carries taste characters w and wbar, and so does R. The turn charges are vector-like:
  q in {1, 2} on each side.
- A4. K = 0 Dirac masses: T allows twice as many as O (dim 4 against 2), one per character pair. T never forbids
  an L-R mass on CL-1's cell.
- A5. The copy sign keeps T and breaks the 4-fold. Its light family has L and R of the same character, and the
  T-invariant mass mu gaps it. CL-1's one light family is therefore not turn-protected.
- A6. Multiplying the geometric turn by the taste phase that gives every L the same character is not a tick
  symmetry (residual 1.05). Relabelling CL-1 does not give TWIST.

## B. Composite TWIST (new, exact)

The rule tested, CTWIST, is a cell walk on the same 8 cell states with three ingredients:
- sigma: the cell spin, taken from CL-1's velocity matrices (sigma = 2S);
- tau: the cell taste doublet, with tau3 = (t - t^dag)/(i sqrt3), where t is the turn's taste factor;
- eta = chi: a spectator.

The walk is U(K) = f + i(h1 tau1 + h2 tau2 + tau3 g.sigma), with
f = (cos K1 + cos K2 + cos K3)/3, h1 - i h2 = (sqrt2/3)(cos K1 + wbar cos K2 + w cos K3), and g = sin K / sqrt3.
K is the cell momentum.

- B1. tau1, tau2 and tau3 sigma_i are 5 anticommuting involutions that commute with eta. tau+ has character
  wbar under the turn and 1 under the half-turns. **The twist is not supplied: it is how the plain cube-centred
  site permutation already acts on the cell's taste.** This is the one structural gain over atomic TWIST, which
  had to choose the nontrivial character.
- B2. U is unitary, with Clifford unitarity f^2 + |h|^2 + |g|^2 = 1 as in TWIST. It is exactly covariant under all
  12 T rotations through the same site permutations V that CL-1 uses. The opposite twist is not covariant. The
  4-fold sends tau3 to -tau3, so O fails, as in TWIST's B3.
- B3. Nodes on a 16^3 cell grid: exactly K = 0 (U = +1) and the cell corner R = pi(1,1,1) (U = -1, quasienergy pi),
  each 8-fold. R is site momentum (pi/2)(1,1,1).
- B4. Each node holds 4 Weyl blocks (tau3 x eta). The Weyl chirality is tau3 at both nodes, and eta is a
  spectator. The light content is 4 L + 4 R, which is TWIST's 2 + 2 doubled by eta.
- B5. Turn charges (det on a Weyl block = w^(2q)): every L has q = 2 and every R has q = 1, at both nodes. The
  turn acts as a chiral Z3.
- B6. Under T the cell is 2(E1/2 x w) + 2(E1/2 x wbar). By Schur, every T-invariant on-cell operator (dim 8) is
  tau3-diagonal, so no L-R mass exists at either node.
- B7. Neither the copy sign nor a random T-invariant on-cell term mixes L and R at the T-fixed nodes. Such terms
  only shift node energies or mix the two eta copies within a chirality.
- B8. The on-cell filter (1 + tau3)/2 leaks O(K^2) (the ratio for K -> K/2 is 4.000).
- B9. U is a pure nearest-cell hop: its Fourier support is the 6 neighbouring cells. In site units, a hop spans up
  to 3 lattice steps along an axis.

## Answers

(1) Structure. Composite TWIST reproduces TWIST on one-qubit sites:
- forced nodes at K = 0 and R, the R node at quasienergy pi;
- chiral turn charges;
- no T-invariant L-R mass.

CL-1's own tick does NOT reproduce it (A3-A6). Composite TWIST is a different cell update.

(2) Light content. 4 L (q = 2) + 4 R (q = 1): 2 L + 2 R at each node. This is twice TWIST's content per Brillouin
zone, from the spectator eta. Removing the eta doubling with a free T-keeping term is impossible by B6-B7, because
the two eta copies share chirality and character. Removing it needs a further rule or interactions.

(3) Clash.
- R10 (every light L carries the same q != 0): MET. Here it is forced by cell geometry, not by a chosen character.
  The vertex phase is w^(4 n_L N q) with n_L = 4 and q = 2, which is w^(32N) = w^(2N), so N = 0 mod 3 again.
- R11 (light and mirror at different momenta): NOT MET. Each node hosts L and R.
- The alternative is label separation. The mirror label tau3 is now a composite cell operator, built from site
  modes and fixed by the geometric turn. It is exact at the nodes, with an O(K^2) leak. A charge-4 mirror term
  built from (1 - tau3)/2 cell fields is therefore well-defined on one-qubit sites. Because w^(4q) != 1 per
  family, it must be multi-family. Whether such a term gaps only the mirror without breaking T is an interacting
  question (SMG) and is not computed. The clash is narrowed, not resolved: R11's momentum mechanism is replaced
  by a label mechanism that no longer bends Qubit.

(4) Gate (CTWIST).
1. Numbers: none. 1/3, sqrt2/3 and 1/sqrt3 are forced by unitarity of the nearest-cell member. Pass.
2. Observed structure: none. It uses only the cell's geometric taste character under the rotations the copy
   mass keeps. Pass.
3. Prediction not built for: a pinned pi-mode doubler at site momentum (pi/2)(1,1,1); a chiral Z3 with every L at
   q = 2; isotropic speed 1/sqrt3 per cell step; an eta-doubled light content. Untested against measurement, and
   the doubled content (8 Weyl per cell) is a liability. UNTESTED.
4. Axiom bent: not Qubit (one mode per site; no Qubit bend). It replaces CL-1's two cube-local layers with a
   nearest-CELL hop, whose site range is up to 3 steps. That bends nearest-neighbour admissibility unless the
   walk factors into cube-local layers, which is not shown. It also drops O to T (the 4-fold acts as a parity)
   and is incompatible with CL-1's O-covariant tick as the update.

Result: items 1, 2 and 4 pass on Qubit, with a possible nearest-neighbour bend flagged; item 3 is UNTESTED.
Composite TWIST is a bounded candidate, not adopted. It is better than atomic TWIST on composite-before-atomic
(no second qubit, no chosen character) and worse on light content (eta doubling).

## Smuggling review

- Supplied:
  - the Clifford ansatz on the cell;
  - the identification of Weyl chirality with tau3 instead of CL-1's chi (the one real choice);
  - the nearest-cell range;
  - the 12 rotations T (not O), justified only by the copy mass keeping T.
- Forced: the w + wbar split and the tau+ character (geometry); unitarity coefficients; the nodes at 0 and R; the
  chiralities and charges; the Schur selection rule (B6); the vector-likeness of CL-1's own tick (A3-A5).
- Not used: any measured number or named gauge group.
- Correction issued: families-from-tastes A11's "dim 8" internal algebra is a 3-momentum artifact. The true
  value is dim 1.

Next probe: a cube-local layer decomposition of CTWIST (does it keep nearest-neighbour admissibility?), and an
eta-lifting rule (for example, the copy sign's T-invariant eta mixing combined with a momentum-dependent term) to
reach 2 L + 2 R.
