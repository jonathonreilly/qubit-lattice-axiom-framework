# Criteria, written before any run. Commit 73b09692a. Runs can refute or guide; they discharge nothing.

## T1 `t1_tree_reflection.py` (Sections 3, 4)
Tiling (3.1) with b = 8 * 64 in lattice units; random cubes of radius b/64; every tree of at most 4 nodes with
decreasing distinct coordinates and every nonempty proper leaf set S; random half-odd active sites.
PASS needs all of: tree has at most 4 nodes, distinct coordinates, at most 5 leaves; max score attained exactly in the selected leaf;
R^2 = Id; F(Rx) = -F(x); neighbour |R x - R x'|_inf <= 80; pi(x) in S; neighbour image l1 <= 328;
preimage count <= nu; the path of Section 4 has every edge inside Omega.
FAIL on any violation.

## T2 `t2_opt_extension.py` (Sections 2, 5: does the OPTIMAL exact extension grow with L?)
d = 3, balanced pattern f, leaves 1 and 4, box of 4 x 4 x 4 parents, Neumann outer faces, walls on parent faces.
Quantity: A(L) := sup over u on Omega with zero parent means of
min{ ||w||_1^2 : w = u on Omega, zero parent means on Y } / ||u||_{1,Omega}^2.
Controls: flat wall (leaves z<0 only) must be finite; literal condition r^(k)w = 0 on Y at L = 2,4,8 must grow about like L.
PASS: A(16)/A(8) <= 1.25 and A(8)/A(4) <= 1.25 and literal control ratio >= 1.5 per doubling.
FAIL: A grows by more than 1.25 per doubling at the top two sizes. Then find the mode.

## T3 `t3_dcoer_2d.py` (Section 7: does C_0 hide L or depth?)
d = 2, bricks of side 2 parents shifted by 1, torus of 4 parents, Omega = one brick, then a two-brick union.
Quantity: C_0 := max ||H||^2 / (||dH||^2 + ||P_N D*H||^2) on ker bC.
(L, M) with M = h/eta: (4,1), (8,1), (16,1), (4,2), (4,4), (8,2).
PASS: C_0(16,1)/C_0(8,1) <= 1.25 and C_0(4,4)/C_0(4,2) <= 1.25.
FAIL otherwise. Then find the mode.
d = 2 has no balanced fan; this tests bookkeeping of L and depth only.

Memory: start only at 50 percent free or more. Scripts stop themselves above 2 GB RSS. One job at a time, under the numeric lock.

## Amendment to T2, made during the run, before any L = 16 value existed
The run at 4^3 parents, L = 16, reached 1.94 GB RSS inside the sparse LU and was killed under the 2 GB rule. Values already seen: fan A = 1.7395, 2.1788, 2.7180 at L = 2, 4, 8; flat A = 1.6607, 1.7032, 2.1303. So A(8)/A(4) = 1.2475 had been seen, just under the 1.25 written.
New geometry: 2^3 parents, Neumann outer faces, same walls, L = 4, 8, 12, 16, 24, with a watchdog at 2 GB. Same pass rule per doubling (A(16)/A(8), A(8)/A(4) <= 1.25), plus A(24)/A(16) <= 1.25 reported. A rising value that flattens is what an extension domain predicts, since data at zero parent mean are suppressed at small L. A run cannot show a limit either way.
