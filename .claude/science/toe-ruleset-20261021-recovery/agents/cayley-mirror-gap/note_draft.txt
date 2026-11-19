---
claim_id: the_cayley_completion_of_the_charge_four_term_halves_the_gapping_coupling_of_the_eight_majorana_proxy_chain_but_both_forms_persist_at_strong_coupling_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "(1) Exact on-site: on 8 Majoranas (4 complex modes) the 4-form Re Omega has so(8) stabiliser 15 (SU(4)) and operator spectrum -8 (1), 0 (14), +8 (1); (1/2) omega^omega has stabiliser 16 (U(4)) and spectrum -6 (2), 0 (8), +2 (6); their sum, the Cayley form, has stabiliser 21 (Spin(7)) and spectrum -14 (1), 0 (8, odd), +2 (7, even). The Cayley ground state is the Re Omega ground state, annihilated by all 21 commuting bilinears. (2) Finite diagnostics on a supplied 1+1D proxy: L sites with 4 complex modes each, SO(8)-invariant Majorana hopping (8 left + 8 right Majoranas), on-site g Phi^, flavour-twisted boundary (an SU(4) element), all momenta and the relative-charge sectors that can be lowest, L = 4..8 (L = 8 complete only for g <= 0.25). At g = 0.25 the Cayley gap is 2.719, 2.679, 2.702, 2.701, 2.702 (L = 4..8, OPEN) while Re Omega alone gives 1.130, 0.314, 0.917, 0.528, 0.824 (INCONCLUSIVE). At g = 0.5 and 1.0 both are OPEN and flat to 1%. At g = 0.125 Re Omega is free-like (Delta(8)/Delta(4) = 0.523 vs 0.510 free) and Cayley is not OPEN. At matched on-site gap (Re Omega at 0.5, Cayley at 0.25) both are OPEN. Pre-set outcome: PASS (Cayley advantage at g = 0.25), read as a lower gapping coupling, about a factor 2 consistent with the 7/4 on-site gap ratio, not a qualitative persistence difference. Not covered: the 3+1D 16, the slab with bulk and light wall, gauge fields, L > 8, a coupling scan finer than the grid."
upstream_dependencies:
  - the_3450_far_wall_term_keeps_a_unique_gapped_wall_mode_chain_state_to_l_18_but_its_gap_falls_from_six_to_eight_modes_per_flavour_bounded_theorem_note_2026-10-24
  - the_forced_far_wall_term_has_a_unique_gapped_three_site_cell_state_but_a_strong_coupling_cell_only_moves_the_mirror_and_the_one_orbital_sixteen_site_has_only_two_spin10_singlets_bounded_theorem_note_2026-10-23
  - the_spin10_pair_square_on_two_sixteens_is_a_spin12_casimir_with_a_unique_singlet_ground_state_and_gap_four_g_but_a_frozen_far_region_still_moves_the_mirror_bounded_theorem_note_2026-10-23
  - the_slab_mirror_sits_on_the_light_copy_so_the_turn_anomaly_allows_every_family_count_and_the_number_conserving_spin12_term_cannot_gap_the_mirror_bounded_theorem_note_2026-10-23
runner: scripts/the_cayley_completion_of_the_charge_four_term_halves_the_gapping_coupling_of_the_eight_majorana_proxy_chain_but_both_forms_persist_at_strong_coupling_2026_10_24.py
---

# The Cayley completion of the charge-4 term halves the gapping coupling of the 8-Majorana proxy chain, but both forms persist at strong coupling

Claim type: bounded_theorem. Exact statements are labelled [T], finite diagnostics [F], recorded mini results [R] and
readings [S]. Runner: runner.py, TOTAL: PASS=12 FAIL=0, 3.4 s, 53 MB peak, 2.8 k characters, seeded,
AUDIT_TIMEOUT_SEC = 120. It was tested under a unique filename (scratch/cayley_mirror_gap_test_run.py). The larger-L
results are an embedded literal copy of the mini summary. Axioms unchanged. No rule adopted.

## Question

The wizard panel's w2 proposed completing the far-wall charge-4 term Re Omega to the Cayley 4-form
Phi = Re Omega + (1/2) omega^omega. This adds no parameter (the weight 1/2 is fixed by the largest stabiliser) and raises
the symmetry from SU(4) to Spin(7). far-wall-L16 found the 3450 wall-mode chain's gap falling with L, but the 3450 chain
carries no Spin(7), so it may be the wrong proxy. Does the Cayley completion keep a chain gap open where Re Omega alone
does not, on a proxy that carries the structure?

## A. On-site [T] (reproduces w2)

| term | so(8) stabiliser | spectrum (multiplicity) | ground state | gap |
|---|---|---|---|---|
| Re Omega | 15 | -8 (1), 0 (14), +8 (1) | unique, even | 8 |
| (1/2) omega^omega | 16 | -6 (2), 0 (8), +2 (6) | 2-fold | 6 |
| Cayley | 21 | -14 (1), 0 (8, odd), +2 (7, even) | unique, Spin(7) singlet | 14 |

- w2's multiplicities for the omega^omega row were incomplete; they are 2, 8, 6.
- The Cayley ground state is the Re Omega ground state, since -8 - 6 = -14. The two Hamiltonians therefore differ by one
  added term at the same g.
- The operator commutant of the Cayley term among the 28 bilinears is exactly 21-dimensional, and it annihilates the
  ground state.

## B. Proxy [supplied] and engine

- The chain is the 1+1D 8-Majorana SO(7)/Spin(7) SMG chain class (Fidkowski-Kitaev; You-BenTov-Xu; BenTov 2015;
  supplied, not derived here).
  - Each site carries 4 complex modes.
  - The hopping is H_hop = sum (i t c+_{x,j} c_{x+1,j} + h.c.) = (i t / 2) sum_a g^a_x g^a_{x+1}, with t = 1. It is
    SO(8)-invariant, and its low-energy content is 8 left + 8 right Majoranas (k = 0 and k = pi).
  - The on-site term is g Phi^(x).
- This is the vector-like content FK/You-Xu need for an anomaly-free symmetric gapping.
  - The 3450-style single-chirality-per-flavour window (2 right + 2 left complex modes) would carry a U(1) anomaly under
    the SU(4) Cartan that Re Omega preserves. So the 3450 window cannot be used with this term.
  - The full lattice chain therefore plays the mirror (far-wall) sector on its own, with no light partner.
- Deviation from the task wording. I did not use the far-wall-L16 momentum-window reduction. With both chiralities per
  flavour that reduction costs 2^(8n) and caps at n = 4 modes per flavour, i.e. two mode numbers, the same confound that
  limited far-wall-L16. The real-space chain gives five sizes at fixed lattice rules.
- Boundary conditions.
  - Primary: the flavour twist (pi/2, pi/2, -pi/2, -pi/2). It is an SU(4) element inside Spin(7), and it leaves no free
    zero modes at any L.
  - Check: antiperiodic boundary at L = 4, 6. This is the fermion-parity element, so Spin(7) is exact.
- Conserved quantities: N_j - N_k, total N mod 4, and lattice momentum.
- Sectors: relative charge d in {0000, 1000, 0010, 1100, 0011, 1010, 1-100, 10-10, 001-1} (+ -1000, 00-10 at L <= 6).
  - Equivalences seen exactly at L = 6, 7: 0010 ~ 1000, 0011 ~ 1100, 001-1 ~ 1-100, and E(p) = E(L-p) in 0000 and 1010.
  - The adjoint sectors are never the lowest (they sit at >= 1.7 Delta).
  - At L = 8 the computed set was 0000 (p 0-4), 1000 (all p), 1100 (all p) and 1010 (p 0-4), at g = 0.125 and 0.25. For
    g = 0.5 and 1.0 only 0000 (all p) and 1000 (p = 0, 1) were computed, so those couplings are classified on L = 4..7, as
    the criteria pre-set.
- Gates [F]:
  - Momentum blocks over all sectors reproduce the full-Fock spectrum at L = 2 (runner) and at L = 3 (2^12, mini,
    deviation 2e-13).
  - g = 0 gives the free gap 2 sin(pi/2L).
  - The live L = 4 run matches the mini to 5e-6.
- Compute: Mac mini. L = 8 blocks have 4.5-5.6e6 states and about 1e8 nonzeros, with peak RSS about 6.8 GB.

## C. Results [R] (gap Delta = lowest excitation over all computed blocks; twisted chain)

| model | g | L=4 | L=5 | L=6 | L=7 | L=8 | rho = D(Lmax)/D(4) | class |
|---|---|---|---|---|---|---|---|---|
| Re Omega | 0.125 | 0.803 | 0.601 | 0.550 | 0.430 | 0.420 | 0.523 | CLOSING (free-like) |
| Re Omega | 0.25 | 1.130 | 0.314 | 0.917 | 0.528 | 0.824 | 0.729 | INCONCLUSIVE |
| Re Omega | 0.5 | 2.936 | 2.922 | 2.929 | 2.929 | (partial) | 0.998 | OPEN |
| Re Omega | 1.0 | 7.056 | 7.001 | 7.026 | 7.001 | (partial) | 0.992 | OPEN |
| Cayley | 0.125 | 0.993 | 0.071 | 0.791 | 0.274 | 0.714 | 0.720 | CLOSING (L = 5 quasi-degenerate) |
| Cayley | 0.25 | 2.719 | 2.679 | 2.702 | 2.701 | 2.702 | 0.993 | OPEN |
| Cayley | 0.5 | 6.082 | 6.031 | 6.054 | 6.031 | (partial) | 0.992 | OPEN |
| Cayley | 1.0 | 13.048 | 12.981 | 13.011 | 12.981 | (partial) | 0.995 | OPEN |

Free chain: 0.765, 0.618, 0.518, 0.445 (L = 4..7). The ground state is unique and in the neutral sector at p = 0 for
every OPEN entry.

- R1. In the strong-coupling window (g >= 0.5) both terms persist. At L = 8 the neutral gap matches L = 7 to 0.8%.
- R2. At g = 0.25 only the Cayley chain is gapped and L-flat. Its lowest excitations are the even pair/neutral level
  (2.70) and the fermion (2.78), the Spin(7) 7 and 8 split by the hopping. Re Omega alone at 0.25 is in a crossover.
  - Its even-L gaps 1.13, 0.92, 0.82 fall more slowly than 1/L (Delta*L grows from 4.5 to 6.6).
  - Its odd-L gaps dip (0.31, 0.53) in the pair sector.
- R3. The odd-L dips are a boundary-filling effect. At odd L the twisted free chain prefers N_12 != N_34 (its g = 0
  ground state is in d = 1100). They appear wherever the interaction is not yet dominant, for both terms at g = 0.125.
- R4. With the exact-Spin(7) antiperiodic boundary, Delta(4) -> Delta(6) is:
  - Cayley at 0.25: 2.70 -> 2.70.
  - Re Omega at 0.25: 1.55 -> 1.19, against the free 1.41 -> 1.00.
  This agrees with R2.
- R5. At matched on-site gap (Re Omega at 0.5, on-site 4.0; Cayley at 0.25, on-site 3.5) both are OPEN. The gapping
  coupling g_c lies in (0.125, 0.25] for Cayley and in (0.25, 0.5] for Re Omega. The ratio of about 2 is consistent with
  the on-site gap ratio 7/4.

## Pre-set criteria (criteria_pre_run.txt)

- The outcome is PASS (Cayley advantage). At g = 0.25 Cayley is OPEN and Re Omega is not, and at no g is Re Omega OPEN
  while Cayley is not.
- Disclosures:
  - The sector list was amended (adjoint classes added) after the L = 2, 3 engine tests and before any chain physics run.
  - "Unique ground state" was operationalised as: neutral p = 0 ground state at every L and gap > 0.1.
  - L = 8 is partial at g >= 0.5. Those couplings are classified on 4..7, as pre-set.

## Answer

- On a proxy that carries the Spin(7) structure, the Cayley completion gaps the chain at about half the coupling that
  Re Omega alone needs. It does so with an L-flat gap and a unique singlet.
- The gain is quantitative, not qualitative. Re Omega alone also gives a persistent, unique gap once g >= 0.5. At matched
  on-site gap the two behave alike.
- So w2's kill condition ("persistence no better than Re Omega alone") is NOT met at fixed coupling. It IS met at
  matched on-site gap.
- The result also says the far-wall-L16 decline is not generic to charge-4 terms. In a Spin(7)/SU(4)-carrying,
  anomaly-free proxy, Re Omega itself gaps at strong coupling. This supports w2's diagnostic remark that the 3450 trend
  may be a property of the proxy [S].

## Caveats

- This is a proxy. The 1+1D 8-Majorana chain is not the 3+1D 16 of Spin(10). It has no bulk and no light wall: the slab
  issue from smg-strong-coupling (a gapped far layer only moves the mirror inward) is untouched.
- Strong-coupling gaps (2.7 to 13) exceed the free bandwidth of 2 per mode, so the chain is then a cutoff theory.
- L <= 8 cannot see an exponentially small (marginal, BKT-like) 1+1D gap. Weak-coupling closure at g = 0.125 is
  therefore not evidence of a gapless limit.
- The twist breaks Spin(7) to its centraliser at O(1/L). The antiperiodic check at L = 4, 6 agrees.
- The anomaly-family-count requirement that the far-wall term break mode number is met by both terms (total N mod 4
  only). Whether the Z4 they keep is the right one for the 16 is not tested here.

## Smuggling review

- Supplied: the proxy chain class (literature), the hopping form, t, the g grid, the boundary twist and L.
- Forced, given the Cayley rule: the relative weight 1/2, fixed by the largest stabiliser (21), and the sign, fixed by a
  unique ground state.
- Nothing is fitted to measurement and no rule is adopted. The Cayley far-wall clause stays UNTESTED against measurement.
  Gate status if proposed:
  - (1) it chooses no measured number;
  - (2) Spin(7) is not an observed gauge group, but the 8-Majorana grouping is supplied structure (a design-principle
    risk: 8 modes on one site rather than a cluster);
  - (3) the prediction it was not built for is the lower gapping coupling found here;
  - (4) no axiom is bent.

Files: criteria_pre_run.txt, runner.py, out.txt, stems.txt. Engine and jobs: chain.py, chain2.py (threaded matvec,
identical physics), analyze.py, queue*.sh, mini_raw_jsonl.tgz (all per-block records). Scratch: scratch/.
