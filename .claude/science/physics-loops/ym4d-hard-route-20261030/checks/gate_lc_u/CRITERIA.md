# Criteria, written before the first run

Kill test of `library/lc-u.md` Section 5, SU(2), d = 4, L = 3, actual log-average block map with axis-ordered combs, on fine tori of side N = 9 (depth 2) and N = 27 (depth 3). Units: the whole torus is the leaf, sigma = 1, eps = 1/N, a := E_0/eps. L = 3 is far below the file's L >= 2^124. No run proves a bound; constants b_L, d_L are not computed, so only trends can kill.

Field families, each rescaled to target a = 0.02 and 0.01: `smooth` (random low modes), `tube` (a straight tube along axis 3, radius 1 fine cell, plus a second one along axis 2 with another colour, crossing the paths used), `noise` (independent random links).

- **K1, (5.5).** FAIL if max_j E_j/(s_j a) > 1.25 at a = 0.01. At small a the file gives E_(j+1) <= L E_j + b_L E_j^2, so the ratio should stay near or below 1.
- **K2, (5.8) linearity.** T := sup over all x, for 6 base sites z, of the quaternion distance between the hierarchical transport C(x) and hol(root to z) J_z(x). FAIL if T/a differs by more than 25 percent between a = 0.02 and a = 0.01 in any family at N = 27.
- **K3, (5.8) depth.** FAIL if T/a at N = 27 exceeds 2 times T/a at N = 9 for `smooth` or `noise`, or if for `tube` T/a at N = 27 exceeds 2 times its value at N = 9. The tube's radius is one fine cell at each N, so the file's exponent predicts a value falling or flat with depth.
- **K4, level sum.** With err_j the distance between hol_j(root to z_j to x_j) and hol_(j+1)(root to z_(j+1) to x_(j+1)) Gamma_(x_(j+1), x_j)(V_j): FAIL if err_j exceeds 2^12 L^2 times the sum over level-(j+1) cells along the path of the largest level-j angle in the two-block patch. FAIL if sum_j err_j < T_path, which would mean the telescoping identity was coded wrong.
- **K5, (3.3).** Smallest eigenvalue of G = avg_x (A(x) A(x)^T), with A(x) the single hierarchical adjoint transport, is 1 here exactly, since one contour order makes A orthogonal. So the test uses two contour orders, A = (A_1 + A_2)/2: FAIL if the smallest eigenvalue of G is below (1 - 2 T_12)^2 where T_12 is the sup over x of the operator norm of A_1 A_2^T - 1 over two. That inequality is elementary; it checks the code, not the theorem.

Memory: start only at 50 percent free or more; the script stops above 2 GB RSS.
