---
claim_id: the_fewest_change_symmetric_far_wall_term_is_forced_and_gaps_the_3450_mirror_in_a_wall_mode_chain_while_the_flux_pump_separates_anomalous_content_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "1+1D proxy of the domain-wall tick's open step: a 2D Wilson slab (m = 1, four flavours) whose near wall carries the 3-4-5-0 content L(3,4) R(5,0) and whose far wall carries its mirror, with U(1)_A x U(1)_B charges (3,4,5,0), (2,1,2,-1). Exact: the neutral occupation-change lattice is Z l1 + Z l2 with l1 = (1,-2,1,2), l2 = (2,1,-2,1); it is K-null (a gapping lattice); its fewest-change elements are exactly +-l1, +-l2 (six fermion operators), which need one nearest-neighbour bond; both coupling phases rotate away and a free-wall symmetry swaps the two terms, so one coupling g is forced. The bulk Chern number is 1 per flavour, so a flux quantum pumps s_f q_f particles per flavour onto the far wall; for 3450 both pumps lie in the neutral lattice, for 3451 the pump carries Q51 = -1, and no symmetric gapping set exists. Finite diagnostics on the far-wall chain (wall modes |k| < pi/2, bulk dropped, antiperiodic L = 8, 12): at L = 12, g = 200 a unique neutral P = 0 ground state, neutral gap 4.03 and single-particle gap 4.84 (free 0.52, 0.26), flat lowest branch; a level crossing near g = 40; L = 8 is mode-capped (quasi-doublet), so no finite-size trend is extracted. The near-wall flavour-3 level moves by 4e-5, 3e-7, 1e-9 at Ls = 2, 3, 4 (scaling as its own leak squared). The same chain also gaps 3451 with its fewest-change symmetric terms, so the chain regulator cannot see the anomaly; the flux pump separates the two. Not covered: a local (bulk-included) interacting computation, sizes beyond L = 14, 3+1D, gauging."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - a_domain_wall_tick_with_the_layer_direction_as_space_puts_one_weyl_cone_on_each_wall_but_the_circuit_forces_the_mirror_onto_the_far_wall_bounded_theorem_note_2026-10-23
  - the_label_selective_charge_four_mirror_term_on_the_freeze_walk_first_exists_at_four_families_and_frees_the_light_partners_bounded_theorem_note_2026-10-23
runner: scripts/the_fewest_change_symmetric_far_wall_term_is_forced_and_gaps_the_3450_mirror_in_a_wall_mode_chain_while_the_flux_pump_separates_anomalous_content_2026_10_23.py
---

# The fewest-change symmetric far-wall term is forced and gaps the 3450 mirror in a wall-mode chain, while the flux pump separates anomalous content

Claim type: bounded_theorem (exact lattice statements; labelled finite diagnostics on a supplied regulator; the
3+1D target and the local 1+1D SMG are literature inputs, not computed).
Runner: runner.py, TOTAL: PASS=16 FAIL=0, 19 s, 300 MB peak, 5.0 k characters of stdout; run under a unique filename.
Axioms unchanged. No rule adopted.

## Question

The working tick form (chiral-tick-form) puts one Weyl cone on each wall of a domain-wall slab and forces the
mirror onto the far wall. Can a symmetric local interaction confined to the far wall gap the mirror there,
leave the near-wall chiral modes massless for anomaly-free content, and fail for anomalous content? The laptop
proxy is 1+1D: a 2D slab whose wall theory is the 3-4-5-0 model (Wang-Wen 2013, 2018; Tong 2021).

Content convention. In the slab each species has one chirality per wall. Flavours 3 and 4 are left movers on the near
wall and right movers on the far wall; flavours 5 and 0 are the reverse. So the near wall carries the whole 3-4-5-0
theory L(3,4) R(5,0), and the far wall carries its mirror R(3,4) L(5,0). Both are anomaly-free
(3^2 + 4^2 = 5^2 + 0^2 and the same for U(1)_B and the mixed anomaly). This is the 1+1D image of "one family on the light
wall, its mirror on the far wall".

Repo first. This builds on smg-3450 (agents/smg-3450, not a PR: Wilson two-leg ladder, L = 3, inconclusive E5),
filtered-smg-1d (agents/filtered-smg-1d: L = 3, 4, 5, quasi-doublets, no size trend), tpf-circuit (PR #9927: one-mode
sites carry no exact 3450 charge; the rotor-matter disentangler), and the smg-literature lens (agents/smg-literature).
It also builds on chiral-tick-form and freeze-mirror-smg (the Z16 bookkeeping). What is new here:
- the far wall is treated as a genuinely one-handed chain of wall modes, not as a vector-like ladder leg;
- the fewest-change derivation of the term;
- the near-wall leak computation;
- the flux-pump discriminator.

## A. Which far-wall term (exact)

- A1. 3450 has AA = BB = AB = 0 with K = diag(1,1,-1,-1). 3451 has AA = -1.
- A2. The occupation-change vectors of all U(1)_A x U(1)_B-neutral fermion products form exactly Z l1 + Z l2
  (the minors have gcd 1). Every such vector is K-null. So the symmetric terms are precisely the gapping (Lagrangian)
  lattice: nothing symmetric is left over, and no symmetric fermion bilinear exists.
- A3. Fewest occupation changes: the minimal elements are exactly +-l1 and +-l2, with l1-norm 6. The next have
  norm 8. Since max |l_f| = 2, Pauli forces two sites per flavour, so the least local form is one nearest-neighbour bond:
  O1 = psi3(b) psi4^+_x psi4^+_x+1 psi5(b) psi0_x psi0_x+1 and O2 likewise, with psi(b) = (psi_x + psi_x+1)/2 the bond
  average. The average is the reflection-symmetric replacement for choosing a site.
- A4. One coupling. rank[l1; l2] = 2, so the free wall's U(1)^4 rotates both phases away. The free-wall symmetry
  M = (3 <-> 4, 5 <-> 0, particle-hole c_k -> c_-k^+ on flavours 3 and 5) maps l1 -> l2 and l2 -> -l1, so g1 = g2 is
  the only M-invariant choice.
- A5. For 3451, a charge kept by a Lagrangian set obeys q^T K q = 0, so no symmetric gapping set exists (brute force:
  8 single null vectors, no mutually null pair). The 3450 terms carry Q51 = 2 and 1, so they break U(1)_51 explicitly.

## B. Free slab (exact and finite)

Model: h_s(k) = sin k sx + (1 - cos k) sz, with layer bond T = -(sz + i sy)/2.
- B1. For |k| < pi/2, the far wall has E = +sin k with spinor (1,1)/sqrt2, and the near wall has E = -sin k with
  spinor (1,-1)/sqrt2. The decay per layer is r(k) = 1 - cos k, and the far-layer amplitude is a(k) = sqrt(1 - r^2).
  The k = 0 mode is compact.
- B2. The bulk gap is 1 and the Chern number is +1 per flavour layer Hamiltonian (Fukui-Hatsugai, 40^2). So one flux
  quantum of a U(1) pumps s_f q_f particles of flavour f onto the far wall.
  - 3450: the U(1)_A pump (3,4,-5,0) = -l1 + 2 l2 and the U(1)_B pump (2,1,-2,1) = l2 both lie in the neutral lattice.
  - 3451: its pump (3,4,-5,-1) carries Q51 = -1.
- B3. The near-wall mode's component along the far spinor at the far layer is its coupling to any far-layer term. It
  falls by exactly r(k) per layer (ratio/r = 1.000, 0.998). At Ls = 6 it is 3e-9, 4e-4 and 3e-2 at k = pi/12, pi/4
  and 5pi/12. Modes near the window edge delocalise, which is standard.

## C. Far-wall chain with the forced term (finite diagnostics)

The chain keeps only the far-wall modes (|k| < pi/2), with their exact dispersion and far-layer amplitudes. The bulk is
dropped. Boundary conditions are antiperiodic. Sectors are (Q_A, Q_B, P). The Hamiltonian is
H = sum s_f sin k (n - 1/2) + g sum_x (O1 + O2 + h.c.).

| L | n (modes per flavour) | g | neutral gap | single-particle gap | E(P1), E(P2) |
|---|---|---|---|---|---|
| 8 | 4 | 0 | 0.765 | 0.383 | 0.77, 1.31 |
| 8 | 4 | 40 | 0.085 | 0.945 | 1.61, 2.20 |
| 8 | 4 | 200 | 0.183 | 1.531 | 5.28, 7.60 |
| 12 | 6 | 0 | 0.518 | 0.259 | 0.52, 0.97 |
| 12 | 6 | 40 | 0.079 | 0.656 | 0.88, 1.08 |
| 12 | 6 | 200 | 4.031 | 4.838 | 4.03, 4.10 |

- C1 [T]. g = 0 reproduces the free mirror: gaps 2 sin(pi/L) and sin(pi/L).
- C2 [F]. L = 12, g = 200:
  - the ground state is unique, neutral and at P = 0;
  - the neutral gap is 4.03 and the single-particle gap is 4.84;
  - the lowest branch is flat, E(2 dk)/E(dk) = 1.02 (a linear gapless mode gives 2).
  In 1+1D a continuous U(1) cannot break, so a unique gapped ground state in a definite charge sector is the symmetric
  gapped outcome at this size.
- C3 [F]. Near g = 40 the neutral gap dips (0.085 and 0.079). This is a level crossing in the P = 0 sector between the
  free-like and the strong-coupling ground state. It is consistent with a transition, but its order and its BKT
  character (Zeng et al.) cannot be resolved here.
- C4 [F, recorded result]. L = 8 has 4 modes per flavour, and one lattice step +-l1 or +-l2 already fills the window.
  So at strong coupling it has a quasi-doublet (gap 0.18 at g = 200, 0.88 at g = 1000), not a gap. n = 8 (L = 16) has
  neutral sectors of 2.3e6 states, beyond the budget.
  So NO finite-size trend is extracted, and question (1)'s "stays open as L grows" is INCONCLUSIVE.
  - Scratch only (not in the runner): L = 14 (n = 6, window |k| <= 5pi/14) gives a unique ground state with neutral gap
    3.36 and single-particle gap 4.31 at g = 200; 16.8 and 23.2 at g = 1000; lowest branch 3.79 and 3.36 (flat).
  - The L = 12 -> 14 decrease (0.83) sits near 12/14, but the window also shrinks. With fixed n this is not a
    size trend either way.
- Validity [supplied]. Dropping the bulk is consistent while the interaction scales stay below the bulk gap of 1.
  The strong-coupling gaps (4 to 20) exceed it, so there the chain is a cutoff wall theory, not the slab.

## D. Near wall stays free (finite diagnostic)

The near-wall flavour-3 modes are added to the L = 8 chain at g = 200. They couple only through their exact leak
eps(k, Ls) from B3.
- With eps = 0, the near left mover at k = -pi/8 keeps its free level sin(pi/8) to 8e-14.
- With the exact leak, the shift is -4.4e-5, -2.5e-7 and -1.5e-9 at Ls = 2, 3 and 4. The ratio per layer is
  ~1/172 = r(pi/8)^2.
- So the shift is second order in that mode's own leak. That is forced: the first-order term needs the expectation of a
  fermion-odd far operator, which vanishes.

Answer to (2): the near-wall low-energy modes stay free chiral fermions up to O(g^2 eps(k)^2 / gap), with
eps ~ (k^2/2)^Ls near k = 0. Their charges (3,4) on the left and (5,0) on the right are untouched.

## E. Anomalous control (exact plus finite)

- E1. The fewest-change symmetric bond terms for 3451 (|l_f| <= 2) are (2,0,-1,-1), (1,0,-1,2) and (1,-2,1,0). They
  have l1-norm 4 and rank 3, and none is K-null.
- E2 [F, recorded result]. The same chain gives 3451 a unique neutral ground state, with charge gaps of 32.6 at
  g = 1000 and L = 8. Scratch: at L = 12 the neutral sectors also have a unique ground state, with gap 9.6 at g = 1000 (charged sectors were not computed). So the gapped strong-coupling spectra of the
  wall-mode chain do NOT discriminate between anomaly-free and anomalous content. The chain is a non-local
  (momentum-window) regulator in which every charge acts mode by mode, so the anomaly lives in the dropped bulk.
- E3 [T + F]. The discriminator is the Laughlin pump. One U(1)_51 flux quantum delivers charge -1 to the far wall (B2),
  whose lowest Q51 = -1 state is 32.6 above the ground state. An adiabatic flux quantum returns a unique gapped ground
  state to itself, so a symmetric gapped far wall cannot exist for 3451: the gap must close or the state must be
  degenerate along the flux path. For 3450 both pumps land in the ground-state sector, so no such obstruction arises.
  Intermediate-flux spectra are not computed.

Answer to (3): anomalous content fails by the exact pump plus A5. It does not fail by any chain spectrum, which is a
property of the regulator.

## Answers

1. Gap at strong coupling: yes, at L = 12 (and L = 14 in scratch): unique, neutral, flat-branch gapped ground state.
   Persistence as L grows is inconclusive at these sizes (C4). No symmetry breaking is seen.
2. Near wall: free to O(eps^2), and exact at eps = 0.
3. Anomalous content: no symmetric gapping set (A5), and the flux pump forbids a symmetric gapped far wall (E3). The
   chain's own spectrum cannot show this (E2).
Literature (supplied, not computed): Zeng-Zhu-Wang-You 2022 (arXiv:2202.12355) find BKT-type symmetric gapping of
3-4-5-0 on exactly this geometry (a Chern-strip boundary, DMRG). Zakharov-Ueda-Verstraete-Beenakker 2026
(arXiv:2606.24713, as summarised by the smg-literature lens) need a Luttinger helper interaction for the 6-fermion terms
to become relevant. The target is 3+1D SMG of one family plus nu_R (the 16, Z16 anomaly-free). It is supported in the
literature:
- by Razamat-Tong (2020) and Tong 2021;
- by lattice numerics (Butt-Catterall-Hasenfratz 2024, PRL 134 031602; Hasenfratz 2022), which are vector-like gauge
  theories;
- by 4D four-fermion work (Catterall-Schaich, Butt-Catterall-Schaich), where the direct transition is not established
  generically (smg-literature lens).
None of this is computed here.

## Mapping to the rules (UNTESTED proposal, not adopted)

Candidate far-wall clause: "On the coarsest-layer wall, the update adds every minimal occupation-change product of
neighbouring wall modes that is neutral under all charges acting on the light wall, with one shared coupling."

Why this is a rule and not a fit:
- the term set is FORCED by the light-wall charges (A2, A3): fewest changes is CL-2's fewest-occupation-change ordering
  applied to terms;
- nearest-neighbour support is forced by Pauli plus the admissibility axiom;
- the phases are removable and g1 = g2 is forced by M (A4);
- only g is free, and it must exceed a crossover value (C3);
- on anomalous content the same clause produces terms (E1) that cannot gap symmetrically (E3), so the clause itself
  carries the anomaly test.

For the 16 in 3+1D, the analogous clause would pick the minimal Spin(10)- or SM-neutral multi-fermion term on the far
wall. Which term that is (a four-fermion term for the 16 x 16 x 16 x 16 singlet, or a six-fermion one) is not derived.

Gate:
1. no measured number is chosen (g is free);
2. no observed structure is inserted, because the charges are whatever acts on the light wall;
3. prediction not built for: UNTESTED in 3+1D. In 1+1D, the threshold coupling and the absence of any bilinear
   condensate are internal statements only;
4. axiom bent: none beyond the tick form's role-block layer coordinate.

Gate result: passes 1, 2 and 4; 3 is UNTESTED.

## Smuggling review

Supplied:
- the 2D Wilson slab and m = 1;
- the 3450 charges (the textbook anomaly-free test content);
- the projection onto wall modes (bulk dropped);
- the bond-average and point-split forms;
- g, L, Ls;
- the Laughlin adiabatic argument and the 1+1D literature.

Forced:
- the neutral lattice and its K-nullity;
- the fewest-change term pair and its nearest-neighbour support;
- the single coupling;
- the Chern number and the pump vectors;
- the near-wall leak and its second-order effect.

Not shown:
- a local interacting computation with the bulk included (smg-3450 and filtered-smg-1d tried the ladder at L <= 5,
  inconclusive);
- a size trend;
- anything in 3+1D or gauged.

Criteria disclosure. Scratch exploration (ex*.py, scan*.py, anom*.py in this folder) preceded the runner, so the C, D
and E thresholds were fixed after seeing scratch values. They are reported as diagnostics, not as blind tests. D1's
first run failed because of a code error: it used the wrong ground-state momentum, since the one-handed near Fermi sea
carries momentum. It was fixed and is disclosed here.
