# dag55_3 — criteria (written 2026-10-28, BEFORE checks/dag55_3_tc.py exists). POST-HOC: designed after reading RLARGE §0's
# (TC) line and frozen Proposition CL while building the DAG; no dag55 output motivated it.

Question (RLARGE U3: "(TC) vs ε_loc … compatibility unchecked"): does (TC) ε_loc/2 ≥ (16N + 3)A_dη_q hold when ε_loc is
RLARGE's own ε_loc (frozen v1 Proposition CL: ε_loc := min{ε_1/4, (ε_1²/(4Nb_1))^{1/2}}, b_1 := n_P + 12κ(1 + A_d(L))²,
n_P := 6n_ℓ, n_ℓ := 4L³(L − 1), A_d(L) := (d − 1)L(L − 1)/2) and η_q is RS-lin's (η_q := min{ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d},
δ_0 := min{1/(640N), 2/N³})? Both sides are linear in ε_1 on the branch ε_1 ≤ 256Nδ_0 (δ_0 entry inactive) and
4·4Nb_1 ≥ … (ε_loc's square-root entry active), so the answer is a pure number.

Quantity: R(N, κ) := [(16N + 3)A_dη_q] / [ε_loc/2] at d = 4, L = 3 (ε_1 cancels). (TC) holds iff R ≤ 1.
Arithmetic: exact integers/Fractions; √(Nb_1) enclosed by integer square roots at scale 10^30 (rigorous lower/upper bounds); no floats
in any verdict (a float may be printed for reading only, labelled "display").

Pre-registered verdicts, per grid point (N, κ) ∈ {2, 3} × {1, 1/4}:
- FAILS if the LOWER bound of R exceeds 1; HOLDS if the UPPER bound of R is ≤ 1; else UNDECIDED.
- Branch gates (must PASS for the point to be reported): (B1) the δ_0/A_d entry of η_q is inactive at ε_1 ≤ 10⁻³⁰ (i.e.
  ε_1/(256NA_d) ≤ δ_0/A_d) and ε_1/(256NA_d) ≤ ε_1/(2L²); (B2) the square-root entry of ε_loc is active (1/(2√(Nb_1)) < 1/4).
Controls:
- C1 (sanity, must give exactly 1): R computed with ε_loc replaced by RLARGE's [hand] sufficient value (16N + 3)ε_1/(128N).
- C2 (designed to HOLD): R computed with ε_loc := ε_1/4 (the other entry of CL's min) — must be ≤ 1 at every grid point, else the
  verdict logic cannot output HOLDS and is reported as unable to decide.
Report also, per point, the factor 1/R by which a non-quiet threshold η ≤ η_q would have to be taken below η_q for (TC) to hold.
