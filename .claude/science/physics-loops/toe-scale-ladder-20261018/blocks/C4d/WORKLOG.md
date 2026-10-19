# C4d WORKLOG

## 2026-10-19 start
- Read C4, C4b, C4c (NOTE+REVIEW), SCIENCE_WORKFLOW s2.
- Key new idea (derived, to be checked): **spectator lemma**. If singles are frozen
  (alpha(s+_w)|Omega> = e^{i phi}|w>) and dist(w, C) > r, then U|C u {w}> = e^{i phi} (U|C>) (x) |w>.
  Proof: alpha(s+_C) is supported in N_r(C), which does not contain w.
  Consequence: the 3-magnon images of (pair + far spectator) are fixed by the pair walk W alone,
  so isometry of U (and U^dagger) on these states gives W-only bilinear constraints.
- Plan: (1) sanity check the lemma on a non-TI-symmetric toy; (2) range-1: classify monomial T-covariant
  pair maps + numerical search for general W; (3) range 2: glider at 3-magnon level; (4) emptiness-shell
  commuting-gate no-go (vertex argument, classical/monomial version).
Resume: scripts in scripts/, logs in logs/. Each script standalone, < 20 min.

## ~1h in
- c4d_01 (1D toy, spectator lemma) PASS=7.
- c4d_02 range-1 monomial exhaustive: T has 6 equivariant bijective maps (2 move = the face-diagonal
  gliders of Obs. M); only identity survives the 3-magnon spectator test. O: 2 maps, identity survives.
- c4d_04 numerics (T, r=1): cost ~0.14 mu^2 for prescribed moving weight mu -> rigid.
- **Exact**: single-term deduction (unitarity + spectator isometries for U, U^dag) forces all 59
  non-stay amplitudes to zero at r=1 under T => W diagonal. c4d_05 re-verifies each deduction with an
  independent evaluator (own keying/enumeration). Running T and O (log c4d_05_*).
- c4d_03 (brute crosscheck) was too memory-hungry -> superseded by c4d_05's per-witness re-verification.
  WARNING: never `pkill -f c4d_...` in the same shell command line (kills own shell).
Next: c4d_06 range-2 glider at 3-magnon level; C1 (no symmetry) range-1 run; NOTE.

## ~2h in
- c4d_05 T and O: exact, every deduction re-verified independently: W (pairs, r=1) diagonal. PASS 5+5.
- c4d_06 range 2: v=1 face glider passes exact 3-magnon test (2 of 4 moving maps) -> method is r=1-specific.
- c4d_07 general k-clique code; k=2 regression reproduces 59 zeros. k=3: single-term deduction leaves
  159 non-stay unknowns (FAIL kept: prediction 'W_3 diagonal by single-term deduction' fails).
- c4d_08 numeric probe for k=3 running (log c4d_08_clique_numeric_k3.txt).
- c4d_09 Prop. E (emptiness-shell pattern gates, vertex argument) instance checks PASS=2.
- c4d_04 has a FAIL from a mis-set threshold (cost ~0.14 mu^2 < 1e-4 at mu=0.02); kept & disclosed.
Resume: write NOTE.md; if time, k=3 exact attempt.

## ~3h in
- c4d_08 (k=3 numerics): W_3-only system admits off-diagonal (cost 2e-18) and COM-moving (cost 5e-12..5e-14)
  solutions -> k=3 NOT rigid at W-only level.
- c4d_10: extracted moving solution (mu=0.2, cost 1.4e-12): band variation ~3e-3 rad on 6^3 grid (small).
  Long run (4000 nfev) in background -> logs/c4d_10_clique3_solution_long.txt.
- NOTE.md drafted; needs k=3 numerics section + reproduction + SUMMARY log.
Resume: after long run, finish NOTE "k = 3 numerics", write logs/SUMMARY.txt (concatenate TOTAL lines).

## ~3h40 — wrap-up
- C1 (no symmetry) probe: deduction proves 174/679 zeros only -> T is load-bearing for P1 (FAILs kept).
- NOTE.md complete; logs/SUMMARY.txt TOTAL: PASS=37 FAIL=4 (all FAILs explained in NOTE).
- Open for a follow-up: exact k=3 clique-walk system (164 unknowns); range-2 glider extension to a full QCA;
  independent review of Theorem P1 certificate (suggest blind Groebner/elimination route).
