lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T15:10Z

# gap-transport-check (FINISH row 682; item P5 of `library/gap-skeleton-max.md`)

Provenance: Claude Opus 5.5 at high effort, one session, no subagents, started 2026-11-11T03:10Z at pinned commit b1671559b. This is a line-by-line check by a model that did not write the proofs (the author of `gap-skeleton-max.md` is Claude Fable 5.2). It is not an audit and grants no status. Written section by section; a section that ends with "STOPPED HERE" was cut by the output limit.

Scope (row 682): Lemmas 1, 2, 3 of 1.D (lines 224-250), Lemma 7 of 3.6 (line 524), Lemma 6 of 3.5 (line 515), Facts 1, 2, 3 of 3.4 (lines 501-505); then the question of P5: in the chain model of D.3, is Hess phi_b bounded below uniformly in L?

## Repo search

- `library/open-core.md`: no entry contains "transport", "chain model", "Hess phi" or "T-avg". FINISH: only rows 669 (the author run) and 682 (this item) mention the chain model or Hess phi. So no other row covers the chain-model question.
- `library/gap-skeleton-final.md` (row 676, laptop lead) lists the same statements in its section 6 with this item as their check (lines 155-162), and its own run-2 statements go to a different item, `gap-zero-transport-check`. No proof of the chain-model question there.
- The Sussman-Alpoge account does not treat transport in the coupling or the gap (it proves no gap; `gap-skeleton-max.md` Part 0.3, re-quoted from YM4_1400.tex L3054-3056). Nothing in it to port for this item; it enters only through Lemma 6, whose input is its clause (c)(3)-(4), quoted in the skeleton.

## 1. Lemma 1 (transport), skeleton line 224

Setting checked first (D.1). For f, g smooth, int f (-Delta g) e^{-bA} dvol = int <grad f, grad g> e^{-bA} - b int f <grad A, grad g> e^{-bA}, so int f L_b g d mu_b = int <grad f, grad g> d mu_b with L_b = -Delta + b <grad A, grad .>. Correct. phi_b exists, is smooth and is unique up to a constant, because A - mu_b(A) has mean zero and L_b is elliptic with kernel the constants on a connected compact X (connectedness is used and not stated; SU(2)^links is connected).

Line by line.

1. d/dt mu_t(f) = -Cov_t(f, A): derivative of int f e^{-tA} / Z_t. Correct.
2. Cov_t(f, A) = int f (A - mu_t A) d mu_t = int f L_t phi_t d mu_t = int <grad f, grad phi_t> d mu_t. Correct. Hence d/dt mu_t(f) = int <grad f, Z_t> d mu_t, the weak continuity equation.
3. "The image measure satisfies the same equation ... and the solution is unique for a smooth field on a compact manifold." The uniqueness is cited, not proved. GOAL.md forbids "standard" as a step, so here is the line that replaces it (a direct proof, no comparison of two solutions needed). Z_t is smooth in (t, x): phi_t = L_t^{-1}(A - mu_t A) on mean-zero functions, and t -> L_t is a smooth family of elliptic operators with a uniform gap on mean-zero functions on any compact t-interval (the gap is positive for every t and continuous in t by Lemma 2's Lipschitz bound below), so the resolvent is smooth in t and elliptic regularity gives joint smoothness. Fix g smooth and b; put u(t, x) = g(Phi_{t,b}(x)). Then u is smooth, d/dt u = -<grad u, Z_t>, and d/dt int u(t) d mu_t = int (d/dt u) d mu_t + int <grad u(t), Z_t> d mu_t = 0 (the second term is line 2 applied to f = u(t); the product rule holds because u is jointly C^1 and t -> mu_t has a C^1 density). So mu_b(g) = mu_s(g o Phi_{s,b}). This is the claim.
4. For v carried by the flow, D_t v = grad_v Z_t (covariant derivative along the trajectory), so d/dt |v|^2 = 2 <grad_v Z_t, v> = -2 Hess phi_t(v, v) <= 2c |v|^2, and |D Phi_{s,b}| <= e^{c(b-s)}. Correct.
5. Var_b(f) = Var_s(f o Phi_{s,b}) by 3; Poincare at s; grad (f o Phi) = (D Phi)^T (grad f o Phi), so |grad (f o Phi)|^2 <= e^{2c(b-s)} |grad f|^2 o Phi, and int |grad f|^2 o Phi d mu_s = int |grad f|^2 d mu_b by 3. So Var_b(f) <= gamma(s)^{-1} e^{2c(b-s)} int |grad f|^2 d mu_b for every f, which is gamma(b) >= gamma(s) e^{-2c(b-s)}. Correct.
6. Gauge-invariant version: if a compact group acts by isometries preserving A, phi_t is invariant (uniqueness of the mean-zero solution), Z_t is equivariant, Phi commutes with the action, and f o Phi is invariant when f is. Then 5 runs inside the invariant functions with gamma replaced by the invariant gap. Correct.

**Verdict: HOLDS.** The only gap is the cited uniqueness in line 3; the duality line above closes it. No change to the statement.

## 2. Lemma 2 (four forms of the derivative of the gap), skeleton line 227, and its Corollary (T-avg)

Line by line.

1. "Differentiable almost every b; gamma is a minimum of smooth Rayleigh quotients." A minimum of smooth functions need not be differentiable a.e.; what is needed is a Lipschitz bound uniform in f. It holds: for g >= 0, |Cov_b(g, A)| <= osc(A) mu_b(g). The numerator N_b(f) = mu_b(|grad f|^2) has N' = -Cov(|grad f|^2, A); the denominator V_b(f) = Var_b(f) has V' = -Cov((f - mu_b f)^2, A) (the derivative in the centring constant vanishes at c = mu_b f). So |d/db log R_b(f)| <= 2 osc(A) for every f, log gamma is 2 osc(A)-Lipschitz, and Rademacher gives differentiability a.e. Supplied; the statement is unchanged.
2. At a differentiable b, R_{b'}(f_b) - gamma(b') >= 0 with equality at b' = b, so gamma'(b) = d/db' R_{b'}(f_b) at b' = b, for every eigenfunction f_b of the eigenvalue gamma(b) (degeneracy is harmless). With mu_b(f) = 0: gamma' = [-Cov(|grad f|^2, A) + gamma Cov(f^2, A)] / <f^2>. Correct.
3. Cov(g, A) = <grad g, grad phi> gives the bracket -2 <Hess f(grad f, grad phi)> + 2 gamma <f <grad f, grad phi>>. Correct (grad |grad f|^2 = 2 Hess f(grad f, .)).
4. gamma <f <grad f, grad phi>> = <(L f) <grad f, grad phi>> = <grad f, grad <grad f, grad phi>> = <Hess f(grad f, grad phi)> + <Hess phi(grad f, grad f)>. Correct. Hence (HF1): gamma' = 2 <Hess phi(grad f, grad f)> / <f^2>.
5. (HF2): L(f^2) = 2 f L f - 2 |grad f|^2 = 2 gamma f^2 - 2 |grad f|^2. So |grad f|^2 = gamma f^2 - (1/2) L(f^2), the bracket equals (1/2) Cov(L(f^2), A) = (1/2) <L(f^2) A> = (1/2) <f^2 L A>. L A = b |grad A|^2 - Delta A, mean zero. Correct.
6. (HF3): <f^2 L A> = <grad f^2, grad A> = 2 <f <grad f, grad A>>; with dW/dt = -grad A, d/dt (f o W_t) at 0 = -<grad f, grad A>, so d/dt <(f o W_t)^2> at 0 = -2 <f <grad f, grad A>>. Correct.
7. (HF4): <grad f^2, grad A> = -(1/b) int <grad f^2, grad e^{-bA}> dvol / Z = (1/b) <Delta f^2> = (2/b)(<|grad f|^2> + <f Delta f>). With <|grad f|^2> = gamma <f^2>: b gamma' = gamma - <f(-Delta) f>/<f^2>. Correct.

Independent check on the Gaussian (a different data path: direct computation, not the lemma's algebra). One dimension, A = x^2/2 on R, mu_b = N(0, 1/b), f = x, gamma = b, phi_b = x^2/(4b) (L phi = -1/(2b) + x^2/2 = A - mu_b A), Hess phi = 1/(2b). (HF1): 2 (1/(2b)) (1)/(1/b) = 1. (HF2): L A = b x^2 - 1, <x^2 (b x^2 - 1)> = 3/b - 1/b = 2/b, (1/2)(2/b)/(1/b) = 1. (HF3): <x . x> / <x^2> = 1. (HF4): b gamma' = b - 0. All give gamma' = 1. Agrees.

Constants of the Wilson formulas (line 245, not a lemma, checked because P5 inputs use them): with \|X\|^2 = -2 tr X^2 (the norm of 3.4), SU(2) is the round 3-sphere of radius 2, the fundamental character is an eigenfunction of -Delta with eigenvalue 3/4 in each link variable, and each plaquette has four links, so Delta A = 4 (3/4) sum_p (1 - a_p) = 3 sum_p (1 - a_p). For the link term -(1/2) Re tr(U_l S) with U_l S = rho (cos theta + i sin theta n.sigma), the derivative along X = (i/2) t m.sigma (\|X\| = \|t\|) is (1/2) rho sin theta (m.n), so \|grad_l A\|^2 = rho^2 sin^2 theta / 4. Both agree with the skeleton, in that normalisation (the skeleton states the norm only in 3.4).

**Corollary (T-avg).** By (HF1) and <|grad f|^2> = gamma <f^2>, (T-avg) at b is exactly (log gamma)'(b) >= -2c, and the two other forms are (HF3) and (HF4) rewritten. All three equivalences are correct. The "if and only if" with the bound gamma(b) >= gamma(b_0) e^{-2c(b - b_0)} is correct only when that bound is asked for every pair b_0 <= b in the interval: a bound from one base point b_0 does not control the derivative at interior points.

**Verdict, Lemma 2: HOLDS** (a.e. differentiability supplied by the Lipschitz bound of item 1). **Corollary: HOLDS AFTER CORRECTION.** Corrected statement: on an interval I, gamma(b) >= gamma(b_0) e^{-2c(b - b_0)} for all b_0 <= b in I if and only if (T-avg) holds at almost every b in I. Proof: log gamma is Lipschitz, hence absolutely continuous, so the pairwise bound is equivalent to (log gamma)' >= -2c a.e., which is (T-avg) by (HF1).

