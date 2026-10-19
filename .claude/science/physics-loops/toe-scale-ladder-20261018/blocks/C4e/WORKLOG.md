# C4e WORKLOG
Started 2026-10-19. Worker: Claude (Opus 5.5) subagent. Writes only in blocks/C4e/.
## Plan
1. 1D SAT probe: does a reversible number-conserving CA with frozen singles and moving pairs exist (intuition for collisions).
2. 3D: glider = L2∘L1 (square crossing then B-tetra opposite-edge) — design/predicate search.
## Log
- t0: read C4d NOTE/REVIEW, C4c, C4b L2/L3. pysat installed (pip python-sat).
- ~1h: 1D SAT probe (c4e_01): reversible CA, frozen singles + moving '11' pair: UNSAT r<=3 (with or without
  number conservation); with only <=4-magnon windows SAT (pair passes single by "absorbing it and re-emitting
  its back magnon"). Two-type (11 right, 101 left) UNSAT even at <=3-magnon windows. Intuition only.
- Key reduction found: for MONOMIAL QCAs (permutation part is a reversible CA radius 2), the 3-magnon sector
  given W is an equivariant bipartite MATCHING problem (connected 3-configs -> targets, edges = F-locality +
  G-locality + equal stabilisers). Writing c4e_02_k3_matching.py.
- Constructive idea (not yet realised): glider = L2∘L1, L1 = face-square crossing, L2 = B-tetra opposite edge
  (each face pair lies in exactly one square and exactly one B-tetra). Layers need consistent predicates (Prop E).
- c4e_02 DONE: k=3 monomial equivariant extension EXISTS (478 source orbits, perfect matching 478/478). log logs/c4e_02_k3_matching_s-1.txt PASS=4.
- Candidate construction "cube inversion" (c4e_03): every unit cube K has A-tetra = sites with parity of K's lower corner.
  Candidate K: |c ∩ A(K)| >= 2. Active: candidate & no other candidate cube shares a site. F inverts active cubes
  through their centres (full 8-site permutation). Inverse candidate G = I F I (I = point inversion, swaps A/B).
  F has range 2 by construction. Testing G∘F = id on small sectors.
- cube-inversion v1/v2 FAIL already at k=3 (14-16 failing orbits; e.g. A-triangle has F-move but G-conflict). Abandoned.
- NEW (proved on paper, implementing c4e_04): U = L2∘L1, each Li an INVOLUTION over "units" (two-state swaps):
  L1 units = unit squares (crossing D<->D'), L2 units = (B-tetra, opposite-edge pair) (edge <-> opposite edge).
  Unit active iff (a) content = D or D' exactly; (b) for both states of u, no other unit sharing a site is a candidate;
  (c) no candidate among units in N2(u)\N1(u). Lemma: Q1,Q2 active => Q1 active after crossing Q2 => active set
  invariant => L∘L = id on ALL configurations. Range(Li) <= 3, range(U) <= 6 (not 2!). Glider: L2 L1 P = P+e.
- c4e_04 (main verification) running/done -> logs/c4e_04_verify_construction.txt; c4e_05 clusters PASS=4
  (478 connected triples: 403 static, 6 periodic, 69 split, 0 rigid movers; pair hitting single head-on is
  REFLECTED with orientation rotated (1,1,0)->(1,-1,0); head-on pairs pass with shift 0..2).
- c4e_06 independent flat-index torus implementation: agrees, involutions hold (L=8,10).
- c4e_07 stress test (packed face pairs) running.
- RESUME: if container restarts, rerun scripts 04,06,07 (each < 20 min) and write NOTE.md.
- c4e_04 first run: 1 FAIL (false prediction: hole pairs static; actually U C = C U). Transcribed to
  logs/c4e_04_first_run_FAIL.txt; script corrected and re-running.
- NOTE.md drafted. Remaining: c4e_07 result, c4e_04 rerun result, logs/SUMMARY.txt.
- FINAL: all scripts re-run; logs/SUMMARY.txt TOTAL: PASS=25 FAIL=0 (plus 1 kept FAIL from superseded run).
  NOTE.md complete. Status: unreviewed. Block done.
