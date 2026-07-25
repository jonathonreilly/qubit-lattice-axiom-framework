# Worker B (Opus 4.8 max; workhorse substitution disclosed): block11 math — torus shells, d=3 assembly, envelope feed

> **SUPERSEDED SCAFFOLDING — historical record only.** This file was
> written before (a) the owner landed the rewritten blocks 03-10 on
> `origin/main` and (b) the review rounds that forced the alias lemma
> and the claim narrowing. Its quotations of "block10" are from the
> PRE-REWRITE stack drafts and do NOT appear in the landed
> corner-note; its "action-derived", "full-lane closure", "SAME
> constants", and "supplies both prerequisites" framings are all
> contradicted by the landed note. Read the landed note and
> `REVIEW_HISTORY_B11.md` for the actual claim boundary.

Do NOT read any repository files. Self-contained. Write INCREMENTALLY to:
.claude/science/physics-loops/microcausality-many-body-lightcone-20260718/worker_b11_math_analysis.md

Setup you may take as given: block07-style weighted quasilocal class with activity kappa = sup_x sum_{S ni x} ||h_S|| |S| e^{mu diam(S)} where diam uses A graph metric; the chain lemma (sum of diams >= d(X,Y)) and peeling (chain sums <= n_X^w kappa^{k-1}) hold for any finite graph metric (the supervisor will verify this claim separately — you USE it). The CT-style kernel bound ||k_xy|| <= K e^{-eta ||x-y||_inf} on Z^3; the block08 feed on Z^3: kappa <= K + 8K x(13+10x+x^2)/(1-x)^3, x = e^{-(eta-3mu)}, via l_inf shells 24r^2+2 and ||z||_1 <= 3||z||_inf.

Verify/derive with exact arithmetic, showing every step:
1. TORUS SHELL DOMINATION: for the d-dim discrete torus (Z/L)^d with the quotient graph metric, prove #{z : d_torus(0,z) = r} <= #{z in Z^d : ||z||_1 = r} for every r (covering/injection argument — give it cleanly), and compute exact torus sphere sizes for (Z/6)^3 at r = 1, 2, 3 vs the Z^3 values 6, 18, 38. State for which r <= floor(L/2)-type range equality holds and where it breaks.
2. Same for l_inf shells on the torus vs 24r^2+2 (needed for the kernel feed): exact counts on (Z/6)^3 and (Z/8)^3 at r = 1, 2, 3.
3. METRIC CONVERSION ON THE TORUS: does d^1_torus <= 3 d^inf_torus hold (quotient of the Z^3 inequality)? Prove or refute exactly.
4. CONSEQUENCE: the block08 envelope kappa <= K + 8K x(13+10x+x^2)/(1-x)^3 remains a VALID UPPER bound on the torus with the SAME constants (shell domination + conversion). State the exact chain of inequalities.
5. d = 3 PER-MODE ASSEMBLY: with per-reduced-mode kernels t_3(p) = e^{-2 E_3(p)}, E_3 = arcsinh(sqrt(m^2 + sum_{mu=1}^3 sin^2 p_mu)): verify E_3 >= arcsinh(m) > 0 for m > 0 (monotonicity), 0 < t_3 <= e^{-2 arcsinh(m)} < 1, and the discharge chain -log Gamma(t_3) = dGamma(-log t_3) = 2 a_tau dGamma(h_3) at a_tau = 1 (factor tracking as in the 1d case — flag ANY d-dependence in the factors; there should be none).
6. WRAP-TERM STATUS ON THE TORUS METRIC: in the torus graph metric the wrap term HAS diam 1 (not L-1), so the block10 open-boundary restriction is NOT needed once the class uses the torus metric. Confirm this resolves the 1d wrap blow-up too (the b10 exhibit used the AMBIENT metric on an open embedding). State exactly what changes.
7. LIMITS: anything assumed; what the supervisor must independently verify (especially any reliance on the metric-agnostic claim).
