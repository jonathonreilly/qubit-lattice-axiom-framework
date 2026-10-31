# sp55_seam — criteria (pre-registered before the script; SPHERE55.md §1.2-§1.3, §2)

Written 2026-10-29 03:32 UTC (file mtime), before `sp55_seam.py` exists; C2 wording cleaned at 03:34 UTC, still before the script.

Object. Grid vertices a(Z^4 + h), h = (1/2,1/2,1/2,1/2), a = 1; cubes are the unit cubes centred at Z^4.
D_R := union of closed unit cubes contained in the closed ball |x| <= R. dD := union of the 3-faces lying in exactly
one cube of D_R. Prism complex P_R := D_R u (dD x [0,1]) u theta(D_R). Cube-based Wilson weights: every 4-cell Q
(cube of D_R, of theta(D_R), or prism cell c x [0,1] for a 3-cube c of dD) gives weight 1/4 (in units of the local
beta) to each of its 24 two-faces. Radii tested: R in {2.3, 3.7, 4.5, 5.2, 6.1} (non-degenerate: no vertex with
|x| = R exactly is checked and reported).

Items:
- S1  D_R is invariant under all 384 signed permutations, and is coordinatewise down-closed: if the cube centred at k
      is in D_R and |k'_mu| <= |k_mu| for all mu, then the cube centred at k' is in D_R.
- S2  chi(D_R) = 1 (alternating count of vertices, edges, squares, 3-faces, 4-cubes of D_R).
- S3  dD is a closed 3-pseudomanifold: every square of dD lies in exactly 2 three-cubes of dD; chi(dD) = 0.
- S4  Every vertex link in dD has Euler characteristic 2 (#edges - #squares + #3-cubes of dD at that vertex = 2), and
      every edge of dD lies in k_e >= 3 three-cubes of dD.
- S5  chi(P_R) = 2 (computed from the cell counts of the glued complex, not from the formula 2 - chi(dD)).
- S6  Seam weights: every crossing plaquette e x [0,1] has weight k_e/4 >= 3/4 > 0; report the distribution of k_e.
      Every square sigma of dD has total weight (m_sigma^D + 2)/4 where m_sigma^D = number of cubes of D_R containing
      sigma; report the distribution; every plaquette of the glued complex has strictly positive weight.
- S7  Bulk agreement on flat terraces: for every boundary edge e with k_e = 4, the crossing plaquette weight equals the
      bulk value 1; for every square sigma of dD with m_sigma^D = 2, the total weight equals the bulk value 1.
      (Reported counts; PASS iff these implications hold — they are algebraic consequences of the counts.)
- S8  Report (no verdict): fraction of seam vertices whose valence in P_R equals the bulk value 8.

Controls that MUST fire:
- C1  Removing the central cube from D_R makes S1 (down-closure) fail.
- C2  The two-cube complex {cube centred at (0,0,0,0), cube centred at (1,1,1,1)}, which share only a vertex: its
      boundary fails S4 (the shared vertex's link in the boundary is two disjoint 2-spheres, chi = 4).
- C3  A single cube: chi(D) = 1, chi(dD) = 0 must PASS (positive control that the counting is right).

Verdict rule: PASS iff S1-S7 hold for every tested R, C1 and C2 fire, and C3 passes. Exact integer arithmetic only
(geometry tests use integer squared norms: a cube centred at k is in D_R iff sum_mu (|k_mu| + 1/2)^2 <= R^2, tested as
sum (2|k_mu|+1)^2 <= 4R^2 with R^2 rational).
