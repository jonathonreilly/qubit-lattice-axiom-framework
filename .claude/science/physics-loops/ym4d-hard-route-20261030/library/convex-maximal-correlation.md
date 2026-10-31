# Maximal correlation of a uniformly log-concave law

Written for `parts/upper-chain.md`, Text 21. Proved here. The quantity is Gebelein's maximal correlation. The inequalities used are the Poincare inequality of Bakry and Emery, and the marginal convexity of Prekopa and of Brascamp and Lieb; the last two are classical, and they are the only citations. The bound on the spectrum by a contraction of gradients for a reversible kernel is an old argument; the use here is short enough to write in full.

## Statement

Let K_x, K_y be convex sets in Euclidean spaces, and let p(x, y) := exp(-S(x, y)) / N on K_x x K_y, with S of class C^2. Let A_x, A_y be positive definite constant matrices with

    S_xx >= A_x,   S_yy >= A_y,   || A_x^{-1/2} S_xy A_y^{-1/2} || <= r < 1

at every point. Then for all F(x), G(y) in L^2(p),

    | Cov(F, G) | <= r ||F - E F||_2 ||G - E G||_2.

For a Gaussian the bound is an equality, for r the largest singular value of the matrix above. **It has no factor of the volume, and it does not change when S is multiplied by a constant,** since the blocks scale together. F and G need no derivative and no bound.

## Proof

Change variables linearly, so A_x = 1, A_y = 1, and the conditions read S_xx >= 1, S_yy >= 1, ||S_xy|| <= r.

*Step 1.* Let U be uniformly convex on a convex set, Hess U >= 1. Then Var(f) <= E |grad f|^2 for the law exp(-U), by Bakry and Emery, or by Brascamp and Lieb. So |Cov(f, g)| <= ||grad f||_2 ||grad g||_2.

*Step 2.* Let G be Lipschitz on K_y and g(x) := E[G | x]. The domain of y does not depend on x, so for a unit vector e, d_e g(x) = -Cov_(y | x)(G, d_e S). By Step 1, applied to the conditional law, which has Hess_y S >= 1,

    | d_e g(x) | <= ||grad G||_(L^2(. | x)) || grad_y d_e S ||_(L^2(. | x)) <= r ||grad G||_(L^2(. | x)).

So ||grad g||_(L^2(p_x)) <= r ||grad G||_(L^2(p_y)). The same holds with x and y exchanged.

*Step 3.* Let P G := E[G | x], and P^* g := E[g | y]. T := P^* P is self-adjoint and non-negative on L^2_0(p_y), of norm at most 1, and by Step 2, ||grad T G||_2 <= r^2 ||grad G||_2.

*Step 4.* -log p_y has Hessian at least S_yy - S_yx S_xx^{-1} S_xy >= 1 - r^2, by Prekopa, Brascamp and Lieb, on the convex set K_y. So for h of mean zero, ||h||_2^2 <= (1 - r^2)^{-1} ||grad h||_2^2.

*Step 5.* For G Lipschitz of mean zero, ||T^n G||_2^2 <= (1 - r^2)^{-1} ||grad T^n G||_2^2 <= (1 - r^2)^{-1} r^(4 n) ||grad G||_2^2. With mu_G the spectral measure of G for T, integral lambda^(2 n) d mu_G <= C r^(4 n) for all n, so mu_G lives on [0, r^2]. Lipschitz functions are dense, so ||T|| <= r^2.

*Step 6.* ||P G||_2^2 = <G, T G> <= r^2 ||G||_2^2 for G of mean zero, and Cov(F, G) = <F - E F, P (G - E G)>. []

## Use with a middle variable

Let exp(-S(x, z, y)) be uniformly log-concave on a product of convex sets, with Hess S >= A, and let S-tilde(x, y) := -log integral dz exp(-S). Then Hess S-tilde is at least the Schur complement of A on (x, y), by the same marginal inequality, and

    S-tilde_xy = E_z[ S_xy ] - Cov_z( S_x, S_y ).

The covariance is the Helffer-Sjostrand form E_z < grad_z S_x, L^-1 grad_z S_y >, with L := (Witten Laplacian) + Hess_z S on one-forms in z. Let the indices of z carry a distance d, and let H := Hess_z S obey H >= kappa, ||H|| <= H_max, with the second moment sup_(z, i) sum_j |H_ij(z)| d(i, j)^2 exp(mu_0 d(i, j)) <= C H_max R^2, R the range of H, mu_0 > 0.

*Combes-Thomas on L.* Let phi be a function of the index, |phi(i) - phi(j)| <= mu' d(i, j), mu' <= mu_0. The Witten part acts on each component and commutes with multiplication by exp(phi), so exp(phi) L exp(-phi) = (Witten) + exp(phi) H exp(-phi). At each z the real matrix H is symmetric, so the term of first order in phi is antisymmetric, and it vanishes in the real part of a quadratic form. Therefore Re < v, exp(phi) L exp(-phi) v > >= (kappa - C H_max R^2 mu'^2) ||v||^2. For mu' := min(mu_0, (kappa / (2 C H_max R^2))^(1/2)) this is at least (kappa / 2) ||v||^2, and by Lax-Milgram, ||exp(phi) L^-1 exp(-phi)|| <= 2 / kappa. **The rate is the square root of the ratio kappa / H_max, not the ratio itself**, which is what gives the rate c / L per level-j cell when kappa / H_max is of order L^-2. On a box as domain, the normal components of a one-form vanish on the faces, and the Bochner term has the right sign, as for any convex domain.

*The mixed block.* Take phi := mu' d(., block x). If H_(z x) and H_(z y) have range R and tails faster than mu', then || exp(phi) grad_z S_(e_x) ||_2 <= C H_max, and || exp(-phi) grad_z S_(e_y) ||_2 <= C H_max exp(-mu' D), for unit vectors e_x, e_y, D the distance between the blocks. So, by the bound on L^-1, ||S-tilde_xy|| <= C (H_max^2 / kappa) exp(-mu' D), plus the direct tail of E_z[S_xy], which is smaller. Divided by the gap,

    rho(x; y) <= C (H_max / kappa)^2 exp(-mu' D),

**with no factor of the scale of S and no factor of the area of the blocks.**

## What it does not do

It says nothing about a law with several wells, or about functions correlated through rare sets: a rare event of probability p that is perfectly correlated across the distance gives maximal correlation near 1. So it applies at fixed data of the rare sets, and these need a separate argument.
