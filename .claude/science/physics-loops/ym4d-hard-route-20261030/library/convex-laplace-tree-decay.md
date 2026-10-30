# Convex Laplace step: tree decay of all derivatives, free of the volume

Producer: `parts/hard-core--mapped.md`, Text 5. Status: proved here. Not reviewed.

Credit. The idea of controlling correlations of a uniformly convex measure through the first-order operator is Helffer and Sjöstrand's; the contraction estimate is Bakry and Émery's. Using the renormalised potential's convexity in place of polymers is in the spirit of Bauerschmidt, Bodineau and Dagallier for scalar models. Nothing is cited as load-bearing: the proof below is complete and uses synchronous coupling of Langevin dynamics, which I have written out so that no cumulant combinatorics is needed.

Consumers: the real one-step theorem of Text 5 (all derivatives of the integrated fluctuation), hence the M-freeness item of the account, which does not arise here, since no block size appears.

## Setting

X is a finite metric space with distance d and uniform growth: sup_x sum_y e^{-kappa d(x,y)} =: G(kappa) < infinity for each kappa > 0, the bound being the only thing used of X. E = product of R^{m_x} over x in a subset X_B of X, with m_x <= m. P is an open subset of a product of R^{m_y} over y in a subset X_v of X. S: E x P -> R is smooth.

**Tree length.** For a finite multiset Z in X, tau(Z) is the least total length of a tree whose vertices lie in X and contain Z. Then tau is monotone, tau(Z) <= tau(Z u {y}); it is subadditive, tau(Z u Z') <= tau(Z) + tau(Z') + d(z,z') for z in Z, z' in Z'; and tau(Z) >= d(z,z') for z, z' in Z. Consequently, for 0 < mu' < mu,

    (T)  sum_{y} e^{-mu tau(y, Z)} e^{-mu tau(y, Z')} <= G((mu-mu')/2)  e^{-mu' tau(Z u Z')}   for Z, Z' non-empty.

Proof of (T): tau(y,Z) + tau(y,Z') >= tau(Z u Z') by joining the trees at y, and tau(y,Z) + tau(y,Z') >= d(y,z) for z in Z fixed. Use (mu - mu') of the exponent for the second bound, with a factor 2 lost in the first summand, and sum over y. QED

Multi-indices alpha in X_B and beta in X_v are written as lists of points; D_B^alpha, D_v^beta are the corresponding derivatives (tensors in the components, with any fixed norm).

## Hypotheses

Constants gamma, mu > 0 and C_{a,b} for a, b >= 0. For all (B,v):

- (H1) D_B^2 S >= gamma.
- (H2) For a >= 2 and any beta: |D_B^alpha D_v^beta S(B;v)| <= C_{a,b} e^{-mu tau(alpha, beta)}, a = |alpha|, b = |beta|. No dependence on B.
- (H3) At B = 0, for any beta: |D_B^x D_v^beta S(0;v)| <= C_{1,b} e^{-mu tau(x,beta)}, and for b >= 1, |D_v^beta S(0;v)| <= C_{0,b} e^{-mu tau(beta)}.

(H3) does not ask for the gradient to vanish. In the application it vanishes at b = 0 up to a term of order g, and the point of (H2), (H3) is that no factor of the large inverse coupling appears in them.

## Theorem

G(v) := -log integral_E e^{-S(B;v)} dB is smooth on P. For each b >= 1 there are C'_b, mu'_b > 0, depending only on gamma, mu, m, the function G(.) and the C_{a,c} with a + c <= b + 2, such that

    |D_v^beta G(v)| <= C'_b e^{-mu'_b tau(beta)},   |beta| = b,

for all v in P and all X. In particular, the bound does not involve the size of X.

## Proof

Fix v. Let mu_v be the probability measure proportional to e^{-S}, and B_t = B_t(v) the strong solution of dB = -D_B S(B;v) dt + sqrt2 dW, B_0 = 0, on a fixed probability space. The drift is globally Lipschitz by (H2) with a = 2, and smooth in v, so v -> B_t(v) is smooth with the same noise. By (H1) two solutions contract: |B_t - B'_t| <= e^{-gamma t} |B_0 - B'_0| pathwise, hence B_t -> mu_v in law, with E f(B_t) -> <f>_v for f of polynomial growth.

*Step 1. Local moments.* Let w_x = e^{-kappa d(x,x_0)}, phi = sum_x w_x |B(x)|^2. Writing D_B S(B)(x) = D_B S(0)(x) + sum_y Hbar_{xy}(B) B(y), with Hbar an average of the Hessian, and conjugating with w^{1/2}: for kappa <= kappa_0(gamma,mu,C_{2,0},G), sum_{x,y} w_x B(x) Hbar_{xy} B(y) >= (3 gamma/4) phi. With Young's inequality on the gradient at 0 and (H3), Ito gives d E phi/dt <= -gamma E phi + C. For p >= 2, Ito on phi^p, with d<phi> <= 8 phi dt because w <= 1, gives d E phi^p/dt <= -p gamma E phi^p + C_p E phi^{p-1}. Hence

    (M)  sup_{t,x_0} E |B_t(x_0)|^{2p} <= C_p,

with C_p depending only on the listed constants. Let Omega_t(y) := 1 + sum_z e^{-kappa d(y,z)} |B_t(z)|; by Minkowski, sup_{t,y} ||Omega_t(y)||_{L^p} is finite for every p.

*Step 2. Pathwise decay of the propagator.* Let H_t = D_B^2 S(B_t;v), J_{t,s} the solution of d_t J_{t,s} = -H_t J_{t,s}, J_{s,s} = 1. Let f be a bounded 1-Lipschitz function on X and H^f = e^{delta f} H e^{-delta f}. By Schur's test and (H2), ||H^f - H|| <= sup_x sum_y C_{2,0} e^{-mu d(x,y)} delta d(x,y) e^{delta d(x,y)} <= gamma/2 for delta <= delta_0(gamma,mu,C_{2,0},G). So the symmetric part of H^f_t is at least gamma/2 and ||e^{delta f} J_{t,s} e^{-delta f}|| <= e^{-(gamma/2)(t-s)}. Taking f = min(d(.,y), d(x,y)):

    (J)  |J_{t,s}(x,y)| <= e^{-(gamma/2)(t-s)} e^{-delta_0 d(x,y)},  for every path.

*Step 3. Derivatives of the path.* For beta of length n >= 1, Z^beta_t := D_v^beta B_t solves d_t Z^beta = -H_t Z^beta - Phi^beta_t, Z^beta_0 = 0, where Phi^beta_t(y) is the Faà di Bruno sum over splittings of beta into a list b_0 and blocks beta_1, ..., beta_a, a >= 0, of the terms D_B^{1+a} D_v^{b_0} S(B_t;v)(y, y_1, ..., y_a; b_0) prod_i Z^{beta_i}_t(y_i), summed over y_1, ..., y_a, excluding the term a = 1, b_0 empty. Thus

    Z^beta_t(x) = - integral_0^t ds sum_y J_{t,s}(x,y) Phi^beta_s(y).

Claim: there are delta_n > 0 and random variables Xi^beta_t(x) >= 0, with sup_{t,x,beta} ||Xi^beta_t(x)||_{L^p} <= C_{n,p} for all p, such that |Z^beta_t(x)| <= Xi^beta_t(x) e^{-delta_n tau(x,beta)}.

Induct on n. A term with a = 0 has b_0 = beta and coefficient D_B D_v^beta S(B_s;v)(y). By the Taylor formula in B, (H3), (H2) and tau(y,z,beta) >= (tau(y,beta) + d(y,z))/2, it is bounded by C e^{-(mu/2) tau(y,beta)} Omega_s(y), with kappa <= mu/4 in Omega. A term with a >= 1 has 1 + a >= 2, so its coefficient is bounded by C e^{-mu tau(y,y_1,...,y_a,b_0)}, and each Z^{beta_i} has length < n. Apply (T) repeatedly in the variables y_i: the sum over y_i of e^{-mu tau(y, y_1, ..., b_0)} prod e^{-delta_{n_i} tau(y_i, beta_i)} Xi(y_i) is at most e^{-delta' tau(y,beta)} times a weighted sum of products of the Xi, with weights summable uniformly. Hölder and Minkowski give all moments. Insert in the integral with (J) and apply (T) once more, in y. For the time integral, Minkowski gives ||integral_0^t e^{-(gamma/2)(t-s)} Y_s ds||_p <= (2/gamma) sup_s ||Y_s||_p. So the claim holds for n, with delta_n := min over the finitely many terms of the rates obtained. No constant depends on t or on the size of X. QED for the claim.

*Step 4. The conclusion.* Integrating by parts, D_v G(y) = <D_v^y S(.;v)>_v. By (H2), (H3), |D_v^y S(B;v)| <= C (1 + Omega(y)^2), so with (M) and the limit t -> infinity this is bounded. For |beta| = b >= 2 write beta = (y, beta') and f := D_v^y S. Then D_v^{beta'} E f(B_t(v);v) is the Faà di Bruno sum of E[ D_B^a D_v^{b_0} f(B_t;v)(y_1,...,y_a) prod_i Z^{beta_i}_t(y_i) ] over splittings of beta'. For a = 0 use the Taylor formula as above, for a >= 1 the coefficient is bounded by (H2) or by (H3) plus the Taylor formula, with a factor Omega_t(y). By Step 3, (T) and Hölder, each term is at most C e^{-mu' tau(y,beta')}, uniformly in t. The functions v -> E f(B_t(v);v) have derivatives of all orders bounded uniformly in t on P, and converge pointwise to <f>_v, so the derivatives converge. QED

## Remarks

1. The constants depend on the hypotheses only through the listed quantities; if the C_{a,b} are small for a >= 3, nothing improves here, and the smallness needed in the application is only that of (H1).
2. Polynomial growth is in Omega only through (M), which is why (H2) must hold uniformly in B for a >= 2. This is the reason for the convex extension in Text 5.
3. No Gaussian comparison, no polymer and no partition of unity is used. A corollary: the marginal law of any block of variables is again log-concave with gap gamma, by Prékopa and Brascamp-Lieb; I do not use it.
