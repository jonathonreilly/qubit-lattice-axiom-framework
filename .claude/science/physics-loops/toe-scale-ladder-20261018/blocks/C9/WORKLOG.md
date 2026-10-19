# C9 WORKLOG

## 2026-10-19 start
- Read C4b NOTE (Lemma 2: U(1) + full action => SU(2)), C4f NOTE (S^- monomial argument), C4d context.
- Key idea found analytically (before any code): a rigidity theorem.
  THEOREM (candidate): every Z^d-TI one-qubit QCA commuting with global SU(2) is a translation tau_c.
  Proof chain: (B) SU(2)-invariant ops overlapping in ONE site commute iff one has zero vector
  channel there; (C) lexmax-lexmin translate overlaps in exactly one site => non-commuting;
  (D) applied to alpha(P_{0,e}) => support is a NN bond => alpha(P_{0,e}) = P_{p,p+e};
  (F) commutation pattern => same shift c for all three directions; (G) tau_{-c} alpha fixes all
  swaps => fixes sigma_x (support-elimination) => identity.
  Consequence: full action + U(1) + O-covariance => alpha = id. Nothing moves.
- Plan: scripts/c9_01_lemmas.py (numerical checks of B,C,D,F,G ingredients),
  scripts/c9_02_sector.py (step (1): S^- sector analysis, 6-cycle ker S^- glider at sector level,
  showing the S^- argument alone does NOT forbid motion), scripts/c9_03_search1d.py (independent
  numerical route: search SU(2)-inv self-adjoint unitaries in a 4-site window with commuting
  translates; expect only NN swaps).
- Resume: rerun scripts; logs go to NEW files logs/<name>_runN.txt (never overwrite).
- dry runs of c9_01 in scratchpad (one FAIL in dry run was a sign-convention bug R[j,k]->R[k,j] in the G check's equation, fixed before official run). Official: logs/c9_01_lemmas_run1.txt
- 07:55 launched c9_03_search.py 100 starts -> logs/c9_03_search_run1.txt (~15 min). Dry run (10 starts, scratch) had 2 FAILs 'each expected bond found' just from too few starts. If container restarts: rerun to logs/c9_03_search_run2.txt
- 07:57 NOTE.md drafted (Theorem 1 + Cor 2 + sector witnesses + gate). Corollary 2 corrected: needs H irreducible on R^3 (D2 counter-case). Remaining: wait c9_03, write logs/SUMMARY.txt, fill c9_03 result in NOTE table.
- 08:19 c9_03 run1 produced only header lines then python was gone (likely killed by its 1150 s timeout: some starts very slow at max_nfev=4000). Kept as logs/c9_03_search_run1_INCOMPLETE_killed.txt (renamed, content unchanged). Relaunch run2 with max_nfev=800, 60 starts, progress lines.
- 08:39 c9_03 run2 also killed by its 1150 s timeout during 1D window (machine load ~2; starts far slower than dry run). Renamed to logs/c9_03_search_run2_INCOMPLETE_timeout.txt. Restructuring: per-window runs, per-start log lines, wall-clock budget.
- 09:00 c9_03 run3 1D: PASS=4 FAIL=0 (62 starts, 16 converged, all NN swaps). 2D running.
- 09:03 DONE. c9_03 2D PASS=4. logs/SUMMARY.txt TOTAL PASS=49 FAIL=0. Block complete; needs independent review (load-bearing: Lemma B, Step D, Step G).
- 09:18 Applied REVIEW.md corrections to NOTE.md (Step D argument, generic=injective, c_1 attribution, i.e., brickwork, novelty, status, dispositions). No logs touched.
