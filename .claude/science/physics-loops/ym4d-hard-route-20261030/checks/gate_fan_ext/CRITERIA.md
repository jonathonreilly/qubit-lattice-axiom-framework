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

## Second amendment, T2 and T3
T2's first runs, at both 4^3 and 2^3 parents, gave flat A above 2 at L = 8 and 16. That is impossible: reflection across a flat wall is a competitor with total energy exactly twice the Omega energy, so A <= 2. An exact dense solve gave 1.4577 and 1.6698 at L = 4, 8, against the Lanczos values 1.8128 and 2.3083. Cause: rounding left a component off ker C_O that Lanczos amplified by about 13 per step. All those values are void, including the ones quoted in the first amendment. Fix: reproject each Lanczos vector onto ker C_O. New control: flat A <= 2 at every L, and Lanczos must match the dense value at L = 4, 8. L = 24 exceeded 2 GB, so the sizes are L = 4, 8, 12, 16, 20. The pass rule is unchanged.
T3's dense QR exceeded 2 GB at N = 64. It is rewritten as a sparse saddle solve with eigsh, and (32,1), (4,8) are added if memory allows. Values (4,1) = 0.1064 and (8,1) = 0.1062 had been seen. New control: the sparse code reproduces those two values.

## T2 outcome by the written rule, and diagnostics registered before running them
With the fix, T2 gave flat A = 1.4577, 1.6698, 1.7660, 1.8189 (below 2, matching the dense values) and fan A = 1.9253, 2.4551, 2.7543, 2.9589 at L = 4, 8, 12, 16. A(8)/A(4) = 1.275 > 1.25, so T2 FAILS the written rule; L = 20 hit the watchdog and the literal control was not reached.
The fan values are close to linear in log L, about 0.52 per doubling. Hypothesis, not proved: this is the slow approach to a spectral edge from scale-invariant modes on the wall edges. On a line where Omega has opening 3 pi/2 and Y has pi/2, odd data with Mellin variable s have Y/Omega energy ratio coth(s pi/4)/coth(3 s pi/4), which tends to 3 as s -> 0. So A would tend to 4 from below, with s of order pi / log L available on the lattice. That is bounded, unlike L or log L growth.
T5 `t5_corner_2d.py`: d = 2, 2 x 2 parents, Omega = three quarters, L = 4 to 256. PASS: A <= 4.5 at every L, and A(256) - A(128) < A(16) - A(8). FAIL means the hypothesis is wrong: stop and report growth.
T6 `t6_edge_vs_fan.py`: d = 3, L = 4, 8, 12, 16. Edge pattern Omega = {z<0, x<0} or {z>0}. Literal control on the fan at L = 2, 4, 8. Top mode of the fan at L = 16: share of its Y energy near the vertex and near the wall edges.
PASS: fan minus edge varies by at most 0.5 over L = 4 to 16, and literal ratio >= 1.5 per doubling. FAIL: the fan grows by something the edge does not explain.
Neither test can bound the fan's A in the limit. The hand proof (5.3) is the only bound.

## Third amendment, T5 and T6, and T7
T5 hit the watchdog at L = 256, so A(256) does not exist; the nearest clause is A(128) - A(64) < A(16) - A(8).
T6's peak-RSS guard stopped it at the L = 16 edge run. The edge pattern equals the d = 2 corner exactly at L = 4, 8 (1.5208, 1.8269), so T5's value 2.0892 is used for L = 16; L = 12 is 1.9695 from T6 itself. Fan minus edge is then 0.4045, 0.6282, 0.7848, 0.8697: range 0.465, inside the 0.5 written, but it is still rising about 0.23 per doubling, so the edge explains only half of the fan's slope.
T6b `t6b_control.py`: the literal control and the top fan mode, each in a fresh process.
T7 `t7_energy_factor.py`, guide only: for every pattern, on each linear piece of the map R, kappa = ||DR||^2 / |det DR| in the Euclidean norm. Then u o R gives the continuum Dirichlet bound A <= 1 + kappa before mean corrections, a number to set against the rise in T2. No pass rule: it only says how far any log rise could go.
