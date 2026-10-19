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
