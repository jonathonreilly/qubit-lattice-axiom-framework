# T75 results against PREREG.md (all same-family checks by Claude Sonnet 5.5)

| Test | Registered reading | Observed | Verdict |
|---|---|---|---|
| A wedge, stopped-site zero w_j = a j, M = 1500 (A_kinematic_kms.py, out_A.txt) | beta a/pi in [0.97, 1.03], resid < 0.05, beta > 0 | beta a/pi = 0.7749 for a = 0.02, 0.05, 0.1; resid 0.0099; beta > 0 | MISSED the registered band (magnitude off 23%; sign and shape right) |
| A controls (same script) | C1 on-site resid > 0.5; C2 local beta varies > 5x | C1 resid 0.80-1.28 (as predicted); C2 not run as registered (resid 0.04 with beta pushed to the scan edge, uninformative) | C1 ok; C2 replaced (see A4) |
| Diagnosis of the miss (A2_exact_bonds.py, mpmath) | none | exact entanglement-Hamiltonian bonds are 0.66-0.84 of pi (j+1/2): lattice-scale offset (rate zero on a site vs the cut between sites) plus a far-end mismatch (linear profile to M vs the segment's own second horizon) | explains the miss |
| Post hoc protocol (NOT pre-registered): exact segment of N sites, Slepian's commuting tridiagonal T (A3), Planck plot of eps_l vs <l|H_w|l> (A4) | beta/pi = 1 | N = 100, 200, 400, 800: beta/pi = 1.0063, 1.0047, 1.0039, 1.0033; R^2 >= 0.99996; max deviation 0.16 -> 0.12. Site-zero variant 0.930 -> 0.958. | checked, post hoc |
| A4 controls | no single T; no thermal law | double zero: beta/pi = 2.14, 2.48, 2.81, 3.15 (drifts with N), max deviation 1.5 -> 1.2 (10x larger); on-site ramp R^2 = 0.000 | as predicted |
| B1 stopped ball, simplest energy (B1_stopped_ball.py, B1b_shell_exponent.py) | ledger reproduces 192.32; axis exponent p in [1.8, 2.2] | ledger 192.32 (exact match). Axis p12 = 1.2-1.45, shell fits p = 1.1-1.5 for R <= 22 | validation ok; exponent band MISSED: dominated by curvature 1/(R+n) and the staircase surface, uninformative. The double-zero claim rests on B3 and the Hopf lemma |
| B2 second bond energy F2, point body, 41^3 (B2_second_bond_energy.py, L = 21 and 41) | w0 < 1e-3 with m within 1% of 18; (18-m)/w0 within 5% of 8 sum(1/w_y) | m(w0) monotone, no fold; m = 17.925 at w0 = 1e-3; (18-m)/w0 = 74.63 vs 74.81 (0.2%), 74.8064 vs 74.8065 at w0 = 1e-6; neighbours at 0.6417 | PASS: finite-mass stop at m* = 18/gamma. Ledger saturates at 4.81 (F1 single-site bound 8.02) |
| B3 1D stopped half-space, weight-one energies (B3_exponent_1d.py) | p(20) >= 1.7 for all | p(20) = 1.998 (F1), 1.896 (F2), 2.146 (F3); p(80) = 2.000, 1.972, 2.035. Weight-two energy: p = 1.000 | PASS |

Formal-asymptotics lemma behind B3 (not a referee-grade proof): for a bond energy sqrt(w_x w_y) f(u_x - u_y), f even, smooth, f_2 > 0, a power-law profile u = p ln n obeys, from the second-order expansion in block 55 T4 (sum_y [d_y - d_y^2/4] = 0), p/n^2 - p^2/(2 n^2) = 0, so p = 2 independent of f_2. p = 1 is inconsistent at leading order.
Generic scale-covariance-breaking family F_s = sum (w_x^s - w_y^s)^2: psi = w^s is exactly harmonic, so w ~ n^(1/s); s = 1/2 (weight one) gives p = 2, s = 1 (weight two) gives p = 1.
Finite-mass stop criterion (F1, F2, F3): a stop at finite m needs dF/dw_x finite at w_x = 0. F1: -(w_y/w_x)^(1/2) diverges (w_0 ~ m^-2). F2: -3 per bond (m* = 18/gamma). F3: diverges (w_0 ~ m^(-2/3)).

## File key for the report's block references (all under main_wt/docs/)
- block 53: ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md (:4 claim scope, :50 absolute pin fails covariance)
- block 55: ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md (:26 H_w = phi H phi, :54 T4 weight one, :62 second-order expansion)
- block 56: ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md (:64 T1, :80 T3, :96 T5, :129 N1 route 1)
- Hawking note: AXIOM_FIRST_HAWKING_TEMPERATURE_THEOREM_NOTE_2026-05-01.md (:42-95)
- Half-line/Hegerfeldt note: NATIVE_HALFLINE_CLOCK_COMPLETION_FINITE_HORIZONS_AND_PERMANENCE_BOUNDED_THEOREM_NOTE_2026-09-14.md (:16-22): capture obstruction concerns permanent capture by a closed semibounded unitary; the clocked-walker horizon here is zero hopping (slowing), so no absorber is involved.
- Literature (memory, unverified): Bisognano-Wichmann J. Math. Phys. 16, 985 (1975); Corley-Jacobson PRD 54, 1568 (1996); Visser CQG 15, 1767 (1998); Slepian Bell Syst. Tech. J. 57, 1371 (1978) for the commuting tridiagonal; Shapiro-Teukolsky PRD 47, 1529 (1993).
