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
