---
claim_id: the_d4_far_wall_cayley_term_on_two_plus_one_d_patches_keeps_a_unique_gapped_state_above_a_sharp_transition_near_g_0_25_bounded_theorem_note_2026-10-26
claim_type: bounded_theorem
claim_scope: "(1) Exact: the D4 points orthogonal to the time root u_t form a cubic lattice of three orthogonal roots; the
in-plane hops Gamma_k = i g(u_t) g(n_k) are, in a unitary frame, sz x 1 and sx x 1 (Gamma_3 = -sy x tz, g5 = -(1 x tz)), so the
wall hop conserves the far-wall-chirality number n_A and n_B separately and the Cayley Omega moves both by 2. (2) Finite: with
the 4-mode register, the Cayley term and the Z4-twisted Dirac hop, the 1x4/1x6 code reproduces the chain gaps 2.719/2.702;
on 2x2 and 2x3 patches the ground state is unique in (Q, n_A mod 2) = (0, 0) at every g tested; the GS-sector gap has a minimum
that sharpens from 0.877 (2x2, g = 0.255) to <= 0.017 (2x3, g = 0.2435); at g = 0.25 the gap is 0.886 -> 0.290 (CLOSING by the
pre-set rule, because g = 0.25 sits on the 2D transition), while at g = 0.35 and 0.5 it is 2.557 -> 3.182 and 5.639 -> 5.599
(OPEN-LIKE). Two width-2 patches only; no thermodynamic claim."
upstream_dependencies:
  - the_d4_spinor_register_keeps_the_spin12_far_wall_gap_and_the_cayley_term_as_w_f4_scalars_and_its_root_line_chain_stays_gapped_to_l_8_bounded_theorem_note_2026-10-26
  - the_cayley_completion_of_the_charge_four_term_halves_the_gapping_coupling_of_the_eight_majorana_proxy_chain_but_both_forms_persist_at_strong_coupling_bounded_theorem_note_2026-10-24
runner: scripts/the_d4_far_wall_cayley_term_on_two_plus_one_d_patches_keeps_a_unique_gapped_state_above_a_sharp_transition_near_g_0_25_2026_10_26.py
---

# The D4 far-wall Cayley term on 2+1D patches keeps a unique gapped state above a sharp transition near g = 0.25

Runner: runner.py, TOTAL: PASS=11 FAIL=0, 14 s, 665 MB peak, 4.1 k characters, seeded, AUDIT_TIMEOUT_SEC = 120. Tested
under a unique filename (scratch/d4_far_wall_2plus1_test_run.py). Laptop only, one thread, nice 10, load < 5, free memory
>= 48%. Criteria and sizes fixed in criteria_pre_run.txt before any run. Axioms unchanged; no CL edit; no rule adopted.
Labels: [T] exact, [F] finite diagnostic, [R] embedded result (same code, scratch/drive.py + scratch/results.jsonl).

## Question
The root-line (1+1D) reduction of the D4 far wall with the Cayley 4-form on the 4-mode spinor register is the Cayley chain,
gapped at g = 0.25 (2.719, 2.702, 2.702 at L = 4, 6, 8). Does the gap survive when the wall has two transverse directions?

## A. Geometry and structure [T]
- Time root u_t = (1,1,0,0)/sqrt2. The D4 roots orthogonal to it are +-n1, +-n2, +-n3 with n1 = (0,0,1,1)/sqrt2,
  n2 = (0,0,1,-1)/sqrt2, n3 = (1,-1,0,0)/sqrt2, mutually orthogonal. The spatial wall slice is a cubic lattice; the 2D patch
  is its (n1, n2) square sublattice, with hop i psi_x^+ Gamma_k psi_{x+n_k} + h.c., Gamma_k = i g(u_t) g(n_k) (the chain rule).
- The Gamma_k anticommute, are Hermitian and square to 1. In a unitary frame U: Gamma_1 = sz x 1, Gamma_2 = sx x 1,
  Gamma_3 = -sy x tz, g5 = -(1 x tz). The second factor is chirality: A = g5 -1 (the far-wall Weyl), B = g5 +1.
- So the wall hop (in-plane, and also the full 3D one) conserves n_A and n_B. Omega = c_A c_A c_B c_B moves both by 2; the
  omega^omega part depends only on site occupation. Sectors: (Q = n_A - n_B, n_A mod 2). H = h_A x 1 + 1 x h_B + on-site
  couplings, applied as a Kronecker matvec (no dense Fock space). The Omega phase from det U is removed by an A-phase.
- Twist: psi -> i psi on every wrap (Z4 element, det 1, commutes with all Gamma). It removes the free zero modes.

## B. Gate [F, R]
- 1x4 with the earlier chain twist: Cayley 2.7194, Re Omega 1.1299, free 2 sin(pi/8) (live). 1x6: 2.7024 [R].
  The new code is the old chain on a line.

## C, D. Patches [F, R]
- Free baseline: patch gap = min|eps|, eps = 2 sqrt(sin^2 k1 + sin^2 k2): 2.000 (2x2), 1.732 (2x3). The dispersion has nodes
  at k in {0, pi}^2: 4 two-component cones per chirality, 8 in all (16 Majorana cones). Gapless as L -> inf; the patches are
  finite-size gapped only.
- Ground state unique in sector (0, 0) in every run. At 2x2 all sectors Q = -8..8 were scanned and the lowest excitation is
  always in |Q| <= 1, so 2x3 used |Q| <= 2.

| g | gap 2x2 | gap 2x3 | ratio | 2x3/free | E0/site 2x2, 2x3 | class (pre-set) |
|---|---|---|---|---|---|---|
| 0.125 | 1.946 | 1.666 | 0.856 | 0.96 | -4.030, -3.975 | CLOSING (free-like; free ratio 0.866) |
| 0.25 | 0.886 | 0.290 | 0.327 | 0.17 | -4.216, -4.188 | CLOSING (on the transition) |
| 0.35 | 2.557 | 3.182 | 1.244 | 1.84 | -5.315, -5.340 | OPEN-LIKE |
| 0.5 | 5.639 | 5.599 | 0.993 | 3.23 | -7.287, -7.296 | OPEN-LIKE |

- GS-sector gap scan at 2x3: 0.69 (0.225), 0.126 (0.24), 0.024 (0.2425), 0.017 (0.2435), 0.058 (0.2445), 0.29 (0.25),
  0.72 (0.26), 2.18 (0.3). At 2x2 the minimum is 0.877 at g = 0.255 (avoided crossing). The 1x4 chain's minimum is
  1.24 near g ~ 0.11, i.e. the chain at g = 0.25 is already deep in the strong-coupling state.
- The minimum drops by a factor ~50 from 4 to 6 sites: a sharp ground-state transition at g_x ~ 0.24-0.26 between the
  free-like (semimetal) state and the on-site Cayley state. Whether it is a true level crossing (different patch quantum
  numbers), first order, or a continuous SMG point is not resolved at these sizes.
- Strong side: 2x3 at g = 0.5 has gap 5.599 against 6.054 for the 1x6 chain [R] (-8%), with no low tower in any sector
  (no sign of symmetry breaking). Re Omega alone at 2x2: 1.839 (0.25), 1.751 (0.5), 6.595 (1.0); its crossover lies above
  g = 0.5 (2x3 Re Omega not run).

## Verdict (pre-set criteria)
- At g = 0.25: CLOSES at these sizes. The reason is that g = 0.25 is where the 2D patches change ground state; the second
  direction doubles the kinetic energy and moves the crossover from g ~ 0.11 (chain) to g ~ 0.25.
- For g >= 0.35: SURVIVES at these sizes. The ground state is unique and symmetric, the gap is flat or growing with patch size,
  and it is >= 1.8 times the free finite-size gap. The Cayley mechanism carries over; its coupling threshold roughly doubles.
- Honest limit: two width-2 patches (quasi-ladders). This is a trend, not a limit. The 1D numbers are not a guide to the
  2D threshold.

## What would decide
- 2x4 (3.0e8 states per sector; 3.8e7 per momentum sector with the two-species translations, ~0.6 GB per complex vector,
  ~3 GB Lanczos matrix-free): fits the Mac mini 6 GB single-worker cap; hours of runtime. It gives a third size for the
  minimum-gap scaling and g_x drift.
- 3x3 (4.5e9 states; ~5e8 per momentum sector, ~8 GB per vector): beyond the cap; it needs DMRG or sign-free QMC. In the
  literature, 2+1D SU(4)-type bilayer models (Slagle-You-Xu 2015; He-Wu-You-Xu-Meng 2016) are sign-free and show a direct
  symmetric mass-generation transition at finite coupling. That is context only, not used.
- The 3D wall (cubic, Gamma_3 = -sy x tz, same A/B split) is beyond ED at any non-trivial size.

## Smuggling review
- Supplied: the 4-mode register (owner-deferred Qubit bend), the Cayley form and weight 1/2 (fixed by the stabiliser, as
  before), the naive hop with t = 1 (no Wilson term; doublers kept), the Z4 twist, the patch shapes, g (scanned; nothing fitted).
- Forced: the cubic slice, the Gamma frame, the n_A/n_B conservation (from Clifford structure), the sector labels.
- No CL text: the 2D result is not decisive. It does say that any far-wall CL text must state the coupling as "above the
  2D/3D threshold", not the chain value.
