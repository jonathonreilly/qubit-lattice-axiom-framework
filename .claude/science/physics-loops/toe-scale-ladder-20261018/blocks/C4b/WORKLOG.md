# C4b worklog (2026-10-18)

- Read SCIENCE_WORKFLOW §2, no-go-discipline SKILL, C4 NOTE + REVIEW, 10-16 walk-freeze header.
- Plan: (1) index lemma via strip compactification + GNVW; (2) exact lemmas for on-site/diagonal
  and U(1) sectors; (3) Margolus partitions (symmetry check + magnon dynamics); (4) commuting
  covariant Pauli layers (non-Clifford family; Clifford point).
- c4b_01: GNVW index sanity via Choi mutual information (recalled RWW formula). 10/10.
- c4b_02: first run had 1 FAIL from a test-logic bug (the "entangling" test checked a commutator
  with s_n(e), which vanishes identically for a diagonal QCA). Replaced by a support test; the
  physics statement was unchanged. 8/8 after the fix. The bug is recorded in the script comment.
- c4b_03: Margolus stabiliser = 2Z^3 x| O_c, no O about a site; 5/5.
- c4b_04: first run had a bug: S^2 = (6-14) + matrix added a scalar to every entry. Fixed to
  (6-14)*I; verified S(S+1) spectra {20,12,6,2,0}. The first (buggy) run was killed, partly
  by an over-broad pkill that also killed its shell. 19/19 after the fix.
- c4b_05: Chamon/cuboctahedral strings: covariance with sign +, commuting translates,
  non-commuting cross pair; the composite at pi/4 has range 4 and nonconstant tau, and spreads
  ballistically (radius 4n). This was not predicted in advance: I expected a possible
  commuting/frozen outcome.
- c4b_06: k=3 clusters confined (120/120 closed). k=4: 9/40 not closed -> FAIL kept
  (falsifies "block c confines all clusters").
- c4b_07: declared prediction "flagged 4-clusters carry weight beyond |dCOM|>2" FAILED for both
  (weight <= 5e-8). Kept.
- c4b_08: second implementation of tau for E1 (Laurent ring), same result. Expected value
  disclosed as taken from c4b_05.
- Lemmas 1-5 written as proofs in NOTE.md; recalled facts marked (GNVW I2-I7, RWW formula,
  inverse-of-QCA-is-QCA, FH flow, HFH nontrivial 3D QCA).
- Resource use: one core, nice 10; the longest run was c4b_06 (5 min) and c4b_07 (~15 min).
- Not done: generic-theta dynamics (infeasible exactly in 3D); constructing a U(1) in-premise
  QCA with a nonflat pair walk; independent review.
