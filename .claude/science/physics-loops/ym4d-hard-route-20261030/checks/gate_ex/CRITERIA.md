# gate_ex: registered criteria (written before any run), pin 7c12c6981

Target: Lemma EX and Lemma EX2, `library/sector-values.md` 3A, 3B. SU(2), d = 4.

Conventions. q = exp(t) = cos|t| + sin|t| t/|t|, as in `checks/hard-core--mapped_lift_su2.py`; theta_p = log of the
plaquette. S := sum_p 2(1 - Re q_p) (= |theta|^2 + O(theta^4)). Parent V' on a torus N'^4, fine torus N = L N'.
Block map: Balaban's log-average of comb paths, library/composite-adjoint.md Lemma AD1, fixed axis order, L odd, centred blocks.
f := max |theta'|. E := sum_{x,p} |theta'|^2. I := sum_{x,p,e>0} |Ad(V'_e(x)) theta'_p(x+e) - theta'_p(x)|^2.
e := S(U*) - S(V'), U* the true constrained Wilson minimiser. Composite: minimiser of S with Q^k U = V; e_j := S(V_j) - S(V_{j+1}).
c_e(L) := the Fourier value (1/9)(1 - L^-2) at large L; c_1 := c_e/2 (Lemma EX Step 3).
C_eff(V') := (c_1 I - e)/(f E). W-form: C_W := (c_1 I(W) - e(W))/((f + nu) E(W)).

What a run can show: a family with unbounded C_eff is a counterexample in trend. A bounded C_eff proves nothing.

Validity (all must hold or the run is void).
 V1. Q covariance under a random fine gauge transformation: residual <= 1e-9.
 V2. Solves used: constraint residual <= 1e-9 (max norm), KKT gradient residual <= 1e-6 x (max |grad S|) or <= 1e-8.
 V3. Abelian control: V' a U(1) wave of small amplitude: e/E within 2 percent of the Fourier value (g - 1).
 V4. Minimiser check: random feasible perturbations of U* do not lower S (20 tries, tangent, tolerance 1e-10).

Lemma EX.
 X1 (f scaling). For each family, sup C_eff at fixed shape as f falls by 2.5 twice. FAIL if C_eff(f/2.5) > 1.5 C_eff(f) + 0.5,
    i.e. if the defect is not of order f E.
 X2 (size). Same search budget at N' = 2, 3 (and 4 for a final family). FAIL if sup C_eff grows by more than 2 per step.
 X3 (block side). Constant non-commuting links, N' = 1, L = 3, 5, 7, 9. Reported: e/I and C_eff(L). C(L) may depend on L. FAIL only if
    e/I at fixed f L^2 has no limit (changes by more than 2 between the last two L).
 X4 (levels). Reduction to test, at k = 1, 2, 3 on N' = 1 and k = 1, 2 on N' = 2: e_(top) >= e^(1) (one-level excess of the same parent),
    tolerance 1e-9 E. FAIL if violated. Also sup C_W at level k-1 against level 0 for k = 2: FAIL if the ratio exceeds 2.
 X5 (weight). W = exp(nu phi), phi 1-Lipschitz, nu in {0.4, 0.2, 0.1, 0.05}. FAIL if C_W grows as nu falls at fixed f.
 X6 (symbol). c_e by an optimiser over all P, polarisations, not a grid, L = 3, 5, 7. FAIL if min (g - 1)/|P-hat|^2 < 0.95 (1/9)(1 - L^-2).

Lemma EX2.
 Y1 (identity). d^2/dt^2 Y_k(V(t)) = sum_j d^2/dt^2 e_j(V_{j+1}(t)) to 1 percent by finite differences.
 Y2 (coercivity along the chain). With b_j := sum over level-j+1 cells |grad delta theta|^2 at the chain: d^2/dt^2 e_j >= (c_e/2) b_{j+1} - err,
    and err/(f_{j+1} ||delta theta||^2) bounded. FAIL if err is not of that order: err/(f_(j+1) ||delta theta_(j+1)||^2) above 3 times its value at the smallest f,
    with the f_(j+1) of that level.
 Y3 (sum). b_m(V)/b_m(1) at m = 0, 1, 2 (k = 2), SU(2), non-flat V, adversarial bond and colour. FAIL if b_2(V)/b_2(1) exceeds 2 at f <= 0.05
    or if b_2(V) >= b_1(V) at any f tested, since the sum then has no geometric fall.
 Y4 (L^2 size). ||delta theta||^2_{l^2} at each level: FAIL if it rises with m by more than 1.5 per level (Prop AN3, (i)).

A FAIL is reported as found; it is then checked for artefacts before any verdict.
Limits fixed in advance: torus sizes reach N' = 4 at one level, N = 27 at most; f in numerics cannot be as small as a_* <= c L^-2 in all runs; k <= 3.
