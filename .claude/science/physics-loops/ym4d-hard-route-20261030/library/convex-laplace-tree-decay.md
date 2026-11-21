# Convex Laplace step: tree decay of all derivatives, free of the volume

Producer: `parts/hard-core--mapped.md`, Text 5. Status: proved here. Not reviewed.

Credit. The covariance representation through the first-order operator is Helffer and Sjöstrand's; the contraction estimate is Bakry and Émery's. Using the renormalised potential's convexity in place of polymers is in the spirit of Bauerschmidt, Bodineau and Dagallier for scalar models. Nothing is cited as load-bearing: the proof below is complete.

Consumers: the real one-step theorem of Text 5; the exterior comparison and the interaction bound in `library/polymer-covariance.md`.

Version 2. The first version differentiated the Langevin path to every order, which needs third and higher derivatives of the action bounded uniformly on the support. That fails with a compact log-concave cut, whose derivatives blow up at its wall. This version uses only the first-order propagator, moments, and an algebraic splitting of cumulants, so a cut is allowed. The price is a decay rate that degrades like 1/(n-1) with the order n; the first version gave better rates without a cut, and they are not needed.

## Setting

X is a finite metric space with uniform growth: sup_x sum_y e^{-kappa d(x,y)} =: G(kappa) < infinity for each kappa > 0. The variables xi = (xi_c) are indexed by a family of cells c, a partition of the coordinates into blocks of at most m coordinates and diameter at most D_c in X. E is their product. P is an open subset of a product of R^{m'} over points of X.

S: E x P -> R is smooth on K x P, where K = prod_c K_c. Each K_c is an open convex neighbourhood of 0 in the variables of c, and it does not depend on v in P. Psi_c is smooth and convex on K_c, with Psi_c -> infinity at the wall of K_c and xi_c . grad Psi_c(xi_c) >= 0. It is allowed that K_c is the whole space and Psi_c = 0. Psi := sum_c Psi_c.

**Tree length.** For a finite multiset Z in X, tau(Z) is the least total length of a tree with vertices in X containing Z. It is monotone in Z, subadditive when two trees are joined, and tau(Z) >= d(z,z').

## Hypotheses

Constants gamma, mu > 0, C_{a,b}. For (xi, v) in K x P:

- (H1) D_xi^2 S >= gamma.
- (H2) For a >= 2 and any beta: |D_xi^alpha D_v^beta S| <= C_{a,b} e^{-mu tau(alpha, beta)}.
- (H3) At xi = 0, for any beta: |D_xi^x D_v^beta S(0;v)| <= C_{1,b} e^{-mu tau(x,beta)}, and for b >= 1, |D_v^beta S(0;v)| <= C_{0,b} e^{-mu tau(beta)}.

(H3) does not ask the gradient to vanish. The hypotheses carry no factor of the large inverse coupling in the application, because x_k g_k^2 = 1 and the reference is critical.

## Theorem

Let G(v) := -log integral_K e^{-S(xi;v) - Psi(xi)} d xi. For each b >= 1 there are C'_b, mu'_b > 0, depending only on gamma, mu, m, sup D_c, the function G(.) and the C_{a,c} with a + c <= b + 2, such that for all v in P and all X,

    |D_v^beta G(v)| <= C'_b e^{-mu'_b tau(beta)},   |beta| = b.

## Proof

Write mu_v for the probability measure proportional to e^{-S-Psi} on K, <.> its expectation, and L the generator Delta - grad(S + Psi). grad. The diffusion stays in K because Psi blows up at the wall. Let B_t be the diffusion and J_{t,s} its first variation along a path.

**Step 1. Local moments.** Let w_x = e^{-kappa d(x,x_0)}, phi = sum_x w_x |xi(x)|^2. Write D_xi S(xi)(x) = D_xi S(0)(x) + sum_y Hbar_{xy}(xi) xi(y) with Hbar an average of the Hessian. Conjugating with w^{1/2} gives, for kappa <= kappa_0, sum_{x,y} w_x xi(x) Hbar_{xy} xi(y) >= (3 gamma/4) phi. The cut contributes with a good sign when w is constant on each cell, which I take: then sum_c w_c xi_c . grad Psi_c >= 0. Ito, with Young on the gradient at 0 and d<phi> <= 8 phi dt, gives d E phi^p/dt <= -p gamma E phi^p + C_p E phi^{p-1}. Hence, in the stationary law,

    (M)  sup_{x_0} <|xi(x_0)|^{2p}> <= C_p.

Let Omega(y) := 1 + sum_z e^{-kappa d(y,z)} |xi(z)|. Then sup_y ||Omega(y)||_{L^p} is finite for every p. By the Taylor formula and (H2), (H3), every function f = D_v^beta S obeys

    (F)  |f| <= C e^{-(mu/2) tau(beta)} Omega_beta^2,   |D_xi^x f| <= C e^{-(mu/2) tau(x,beta)} Omega(x),

with Omega_beta the maximum of Omega over beta. For the second bound use tau(x,z,beta) >= (tau(x,beta) + d(x,z))/2. Since the L^p norms of Omega are bounded uniformly, which point it is taken at does not matter below.

**Step 2. Pathwise decay of the propagator.** d_t J_{t,s} = -(H_t + P_t) J_{t,s}, with H_t = D_xi^2 S(B_t) and P_t = D_xi^2 Psi(B_t) >= 0, block diagonal over the cells. Let f be a bounded Lipschitz function on X, constant on each cell, and conjugate by e^{delta f}. P_t commutes with it, with no cost however large P_t is. By Schur's test and (H2) with a = 2, ||e^{delta f} H_t e^{-delta f} - H_t|| <= gamma/2 for delta <= delta_0(gamma, mu, C_{2,0}, G, sup D_c). So

    (J)  |J_{t,s}(x,y)| <= C e^{-(gamma/2)(t-s)} e^{-delta_0 d(x,y)},  for every path,

where C accounts for the cell diameter in passing to the cell-constant f.

**Step 3. Covariance with decay.** For F, H in L^2(mu_v), smooth with square-integrable gradients,

    cov(F,H) = integral_0^infty < grad P_t F . grad H > dt,    grad P_t F(xi) = E_xi[ J_{t,0}^T grad F(B_t) ].

The first identity is integration by parts with reversibility and the gap gamma. The second is the chain rule on the flow. So by (J), Cauchy-Schwarz and stationarity,

    (C)  |cov(F,H)| <= C sum_{x,y} e^{-delta_0 d(x,y)} ||D_x F||_{L^2} ||D_y H||_{L^2}.

**Step 4. Splitting a cumulant at a large gap.** Let X_1, ..., X_m be random variables with all moments, and A, B a partition of {1,...,m} into non-empty parts. The cumulant is the sum over partitions s of {1,...,m} of (-1)^{|s|-1} (|s|-1)! prod_{b in s} E[prod_{i in b} X_i]. If in each factor E[X_b] is replaced by E[X_{b cap A}] E[X_{b cap B}], the sum is the cumulant of two independent families, which is 0. Telescoping,

    (S)  |cum(X_1,...,X_m)| <= C_m max_{b} |cov(X_{b cap A}, X_{b cap B})| prod_{i not in b} ||X_i||_{L^{m}},

where X_I := prod_{i in I} X_i, the maximum runs over sets b meeting both parts, and a product of the norms of the X_i in b is included in the covariance.

**Step 5. The conclusion.** The law and the cut do not depend on v, except through S. So for |beta| = b, D_v^beta G is the sum over partitions pi of beta of (-1)^{|pi|-1} cum( D^{pi_1} S, ..., D^{pi_m} S ). For m = 1 the term is <D^beta S>, and (F) with (M) bounds it by C e^{-(mu/2) tau(beta)}. For m >= 2 take a minimal spanning tree on the blocks pi_i with edge lengths the distances between blocks. Then the sum of its edge lengths plus sum_i tau(pi_i) is at least tau(beta). So its largest edge has length l >= (tau(beta) - sum_i tau(pi_i))/(m-1). Removing that edge splits the blocks into A and B at distance exactly l, by the cut property of minimal spanning trees. Apply (S), then (C) with F, H products over the sets of blocks, and D_x of a product by Leibniz with (F) and Hoelder with (M). The double sum over x, y, with decay delta_0 between them and mu/2 to the two supports, gives e^{-delta' l} with delta' = min(delta_0, mu/2)/2, times C prod_i e^{-(mu/4) tau(pi_i)}. Altogether, each term is at most C exp( -min(delta'/(m-1), mu/4) tau(beta) ). No constant depends on the size of X. QED

## Remarks

1. The cut must be independent of v. In the application the variables are coordinates on a fixed space, and v enters through the chart.
2. Polynomial growth of f enters only through (M). (H2) is asked on K, not beyond it: this is why no convex extension of the action is needed if the cut lies inside the class.
3. (C) is what the rare-cell estimates use with hole data fixed.
