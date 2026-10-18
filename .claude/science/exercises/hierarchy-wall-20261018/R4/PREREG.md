# R4 pre-registration (written before any run), 2026-10-18

Tradition: dynamical systems / RG. Target budget L* = ln(M_Pl/v) = 38.4
(M_Pl = 1.22e19 GeV, v = 246 GeV); 36.8 with the reduced Planck mass.

## Route A: integer selected by a self-consistency balance

Lemma A (to prove): if N* is a real zero of F(N) = sum_j c_j N^{p_j} exp(-k_j N),
J terms, |c_j| in [1/R, R], rate gap Delta = k_2 - k_1 > 0 (k_1 smallest), then
N* <= [ln((J-1) R^2) + p_max ln N*] / Delta  (pure exponentials: p_max = 0).
Consequence: k_1 N* <= (k_1/Delta) ln((J-1)R^2) (+ log terms).

Test a1 (checked): random exponential sums, verify bound, record max k_1 N*.
Test a2 (checked): 1D Wilson-Dirac kink/antikink ring. Measure the rate of the
zero-mode splitting m(N) and of the sea energy E(N); report their ratio.
Reading rules: A-KILL if every O(1) instance (R <= 10, Delta/k >= 0.2) has
k_1 N* < 38.4 and the physical rates come in integer ratios (no near-degeneracy
without a tuned parameter). A-OPEN if a physical instance shows an intrinsic
rate near-degeneracy Delta/k < 0.1 at O(1) inputs.

## Route B: slow passage near a fixed point (essential-singularity tool)

Lemma B (to prove in 1D): T = int du/|beta|. With O(1) start and end,
T >= L* needs one of (i) a near zero met as a hyperbolic fixed point (tuning
e^{-y L*}); (ii) a ghost (non-degenerate interior minimum m of |beta|, curvature k):
m <= 2 pi^2/(k L*^2); (iii) |beta| <= range/L* on the whole path (weak coupling).
A small linear eigenvalue alone (transcritical, pitchfork, weak focus) does not
help: T <= 1/(b u0) for every y >= 0.

Test b1 (checked): normal forms, numeric vs exact.
Test b2 (checked): random 1D and 2D polynomial flows with O(1) coefficients and
O(1) starts; for every trajectory with T >= 38.4 record min |beta| on the path
and distance to the nearest fixed point. B-KILL of the "near-marginal exponent
suffices" reading if no trajectory with T >= 38.4 has min|beta| > 0.05.
Test b3 (comparator): 2D Potts merger family, T(q) = pi^2/sqrt(q-4) - ln(8 sqrt2);
integers q >= 5 vs the needed q.
