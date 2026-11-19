---
claim_id: the_d4_spinor_register_keeps_the_spin12_far_wall_gap_and_the_cayley_term_as_w_f4_scalars_and_its_root_line_chain_stays_gapped_to_l_8_bounded_theorem_note_2026-10-26
claim_type: bounded_theorem
claim_scope: "(1) Exact: under the 1152 spinor lifts of W(F4), the proper lifts act on each chirality block with det 1, so the Spin(12) pair B_a = psi_-^T (M_a x eps) psi_- on the far-wall Weyl field is invariant; improper lifts swap chiralities (= wall swap). All lifts have det 1 and are unitary, so the Cayley 4-form on the 4 spinor modes is invariant (spinor image in SU(4) inside Spin(7)). W(F4)+ invariant counts Sym2, Sym4, Sym3 x V = 1, 1, 1 (SO(4) values). (2) Exact: the far-wall Weyl field of the 4-mode register is 16 x 2 modes with the Weyl spin as the two-16s flavour index; the Fock identity sum_a {B_a,B_a^+} = 2[144 - 2S(S+1) - C2_10 - J^2] holds with S the D4 Lorentz SU(2)_- on N = 0, 1 and the full N = 4 sector; with the cited spin10-two-flavour rep theory the unique Lorentz- and Spin(10)-singlet ground state (E0 = -144 g, gap 4 g, fermion gap 13 g) survives. (3) Finite: the root-line 1+1D reduction of the register with the Dirac hop is unitarily the cayley-mirror-gap proxy chain at even L; Cayley g = 0.25 gap 2.719, 2.702, 2.702 at L = 4, 6, 8 (OPEN); Re Omega at 0.25 INCONCLUSIVE; g = 0.125 not open."
upstream_dependencies:
  - the_spin10_pair_square_on_two_sixteens_is_a_spin12_casimir_with_a_unique_singlet_ground_state_and_gap_four_g_but_a_frozen_far_region_still_moves_the_mirror_bounded_theorem_note_2026-10-23
  - the_cayley_completion_of_the_charge_four_term_halves_the_gapping_coupling_of_the_eight_majorana_proxy_chain_but_both_forms_persist_at_strong_coupling_bounded_theorem_note_2026-10-24
  - the_3450_far_wall_term_keeps_a_unique_gapped_wall_mode_chain_state_to_l_18_but_its_gap_falls_from_six_to_eight_modes_per_flavour_bounded_theorem_note_2026-10-24
  - d4-zoom-chirality (PR #10099), d4-interacting-check (PR #10095), d4-sixteen-content / d4-spin-cell (PRs #10103, #10104)
runner: scripts/the_d4_spinor_register_keeps_the_spin12_far_wall_gap_and_the_cayley_term_as_w_f4_scalars_and_its_root_line_chain_stays_gapped_to_l_8_2026_10_26.py
---

# The D4 spinor register keeps the Spin(12) far-wall gap and the Cayley term as W(F4) scalars; its root-line chain stays gapped to L = 8

Runner: runner.py, TOTAL: PASS=14 FAIL=0, 22 s, 594 MB peak, 4.1 k characters, seeded, AUDIT_TIMEOUT_SEC = 120. Tested
under a unique filename (scratch/d4_far_wall_gapping_test_run.py). Laptop only, one thread, nice 10. Criteria fixed
in criteria_pre_run.txt before any run. Axioms unchanged; no CL edit; no rule adopted.
Labels: [T] exact, [F] finite diagnostic, [R] embedded earlier result.

## Question
Does the far-wall mirror gapping (Spin(12) Casimir on two 16s; Cayley completion of the charge-4 term) carry over to the
D4 zoom-fixed-point matter law with the 4-mode spinor register per event (the working candidate in
CANDIDATE_AXIOM_RULES.md), whose Borici slab keeps W(F4)?

## A. Symmetry [T]
- W(F4) (1152; 576 proper) is rebuilt with spinor lifts S (S g_mu S^-1 = R g, to 1e-15).
- Proper lifts commute with g5 and act on P- and on P+ with det 1, i.e. as SU(2)_- x SU(2)_+. The antisymmetric Weyl form
  eps is therefore invariant, and so is the pair B_a = psi_-^T (M_a x eps) psi_- and the Casimir term sum B B^+.
- Improper lifts anticommute with g5: they carry the far-wall (P-) term to the P+ term, which is the wall-swapped slab
  (as in d4-zoom-chirality 2c). The chiral slab already breaks these; the gapping adds no new breaking.
  The doubled term H_+ + H_- is invariant under all 1152 (B B^+ is phase-blind, |det| = 1 for the swap block).
- Every lift has det S = 1 and is unitary, so the spinor image lies in SU(4), inside the Cayley stabiliser Spin(7).
  The Fock lift commutes with the Cayley 4-form on the 4 spinor modes (2e-14).
- LIV argument. The gapping term is on-site and the same at every far-layer event. So it commutes with
  U(g) = (event permutation) x S(g) for every lifted rotation. It adds no tensor that W(F4)+ does not already allow.
  Under W(F4)+ the invariant counts are Sym2 = 1, Sym4 = 1, Sym3 x V = 1 (the SO(4) values). So no dimension-6 term arises for
  the bosons or for the fermion kinetic vector at any loop order. The dimension-8 counts (Sym6, Sym5 x V) are 2, 2, as known.
  So the gapping induces no LIV beyond the D4 law's own dim-8 term.

## B. On-site spectrum [T, F]
- M_a (the 10-channel matrix on the 16) is symmetric, so the flavour form must be antisymmetric. The only Lorentz-invariant
  antisymmetric form on a Weyl doublet is eps. So the "two 16s" of spin10-two-flavour are exactly the two Weyl spin
  components of the register's far-wall field. The six Spin(4) generators restricted to P- span su(2)_- (rank 3).
- The register changes nothing in the wall field's on-site Fock space: it is 16 x 2 = 32 modes, as before.
- Fock identity sum_a {B_a,B_a^+} = 2[144 - 2 S(S+1) - C2_10 - J^2], with S the D4 Lorentz SU(2)_-. It holds exactly on
  N = 0 (c0 = 160), on N = 1 (the one-body part) and on the full N = 4 sector (35960 states, sparse; deviation 0).
- Sparse Lanczos at N = 4: the lowest level is -108 = -(144 - 36). It is unique (next -88), with S = 0 and C2_10 = 0.
- Hence (citing spin10-two-flavour's rep theory, not rederived here) the unique Lorentz-, Spin(10)- and PH-singlet ground
  state E0 = -144 g at N = 16 survives, with gap 4 g and fermion gap 13 g.
- Full Dirac register on the far layer: H_+ + H_- has a unique product ground state, gap 4 g, invariant under all 1152.
  A P+/P- cross term (B = B_+ + B_-, 64 modes) is NOT analysed: support-function weight bounds do not fix its spectrum, and
  no equal-Casimir (Kostant) structure was found for so(12) + sp(4).

## C. Chain proxy (the 3450 risk) [T, F, R]
- The 1+1D root-line reduction keeps the 4 spinor modes per event, with hop i t psi_x^+ Gamma psi_{x+1} + h.c.,
  Gamma = i g(u_t) g(n), u_t = (1,1,0,0)/sqrt2, n = (0,0,1,1)/sqrt2. Gamma is Hermitian with Gamma^2 = 1 and eigenvalues
  (-1,-1,+1,+1). Rotating to its eigenbasis turns Omega into a phase times Omega and leaves omega^omega unchanged.
  Staggering the Gamma = -1 modes then maps the D4 chain exactly onto the cayley-mirror-gap proxy chain at even L.
  Gate: equal to 2e-13 in every sector at L = 4.
- So the D4 register supplies the 8-Majorana (FK / You-Xu) content natively, 4 complex modes per event, and the proxy is
  no longer an extra choice. The 3450 chain (single chirality per flavour window, gap falling at the n = 6 -> 8 step) is
  not the D4-relevant proxy.
- Gaps, twisted boundary. L = 4, 5 live; L = 6 live at g = 0.25; L = 8 embedded [R] (identical by the exact equivalence).

| model | g | L=4 | L=5 (D4 bc) | L=6 | L=8 [R] | rho | class |
|---|---|---|---|---|---|---|---|
| Cay | 0.25 | 2.719 | 2.708 | 2.702 | 2.702 | 0.994 | OPEN |
| Cay | 0.5 | 6.082 | 6.161 | 6.054 [R] | - | 0.995 | OPEN |
| ReO | 0.5 | 2.936 | 2.931 | 2.929 [R] | - | 0.998 | OPEN |
| ReO | 0.25 | 1.130 | 1.067 | 0.917 | 0.824 | 0.729 | INCONCLUSIVE |
| Cay | 0.125 | 0.993 | 0.943 | 0.791 [R] | 0.714 | 0.719 | INCONCLUSIVE |
| ReO | 0.125 | 0.803 | 0.686 | 0.550 [R] | 0.420 | 0.523 | CLOSING (free 0.510) |

- Trend (honest). At g >= 0.25 the Cayley gap is flat to 1% over L = 4..8, at the same five lattice rules. At weak coupling
  both forms fall with L. These are 4 even sizes and one mode number per flavour: a trend, not a limit.
  L = 7 on the D4 boundary was not computed (3.4e6-state sectors, > 1.5 GB).

## Verdict (pre-set criteria): PARTIAL
- What carries over: the symmetry is exact (both terms are W(F4)+ scalars, so no LIV is induced). The on-site Spin(12)
  state carries over unchanged, with the Weyl spin as the flavour. The D4 root-line proxy is exactly the Cayley chain, which
  is OPEN at g >= 0.25 to L = 8.
- What is not shown: the 3+1D far wall with the Spin(12) term (2^32 per event: beyond ED), the cross-chirality Dirac
  variant, and the frozen-far-region relocation risk of spin10-two-flavour E2, which the register does not touch.

## Proposed CL amendment (not adopted)
"On the D4 slab the far-wall gapping term is the on-site Spin(12) Casimir of the far-wall Weyl field, whose flavour index
is the event's Weyl spin; optionally completed per spinor register by the Cayley 4-form."
- Bent clause: the 4-mode spinor register (already the working candidate; Qubit axiom bend, owner-deferred).
- It removes the separately supplied "two-valued flavour" of spin10-two-flavour: that flavour is now forced by the Lorentz
  structure, since only eps is invariant and M_a symmetric needs an antisymmetric form.

## Smuggling gate
- (1) No fitted numbers. g is free; the classes hold for a coupling range. The Cayley weight 1/2 is fixed by the
  stabiliser.
- (2) Spin(10) and the 16 stay supplied, as before. Nothing new is named.
- (3) Untested prediction: no mirror-sector LIV at any order beyond the dim-8 J6 term. The mirror's composite spectrum is
  Lorentz-scalar (gap 4 g states are Spin(4) singlets).
- Supplied: the 16 content, the 10-channel pair and PH ordering, the 1+1D proxy class, the twisted boundary, g; and the
  cited rep theory for E0 and the gap at N = 16.
