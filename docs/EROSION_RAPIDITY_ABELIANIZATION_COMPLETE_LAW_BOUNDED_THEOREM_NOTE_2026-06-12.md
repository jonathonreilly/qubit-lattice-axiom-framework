# Erosion Rapidity Abelianization Complete Law (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** [scripts/frontier_erosion_rapidity_abelianization_2026_06_12.py](../scripts/frontier_erosion_rapidity_abelianization_2026_06_12.py)
**Runner cache:** [logs/runner-cache/frontier_erosion_rapidity_abelianization_2026_06_12.txt](../logs/runner-cache/frontier_erosion_rapidity_abelianization_2026_06_12.txt)
**Status authority:** independent audit lane only. This source note does not set,
predict, or change the audit status of any claim or dependency.

## Dependencies

- [EROSION_EXACT_RECURRENCE_PATH_PRODUCT_THRESHOLD_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-06-12.md](EROSION_EXACT_RECURRENCE_PATH_PRODUCT_THRESHOLD_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the landed recurrence and path-product model.
- [EROSION_MOBIUS_DERIVATIVE_CHAIN_RULE_LAW_BOUNDED_THEOREM_NOTE_2026-06-12.md](EROSION_MOBIUS_DERIVATIVE_CHAIN_RULE_LAW_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the derivative/matrix rate expression recovered here.
- [EROSION_GEOMETRIC_RATE_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-12.md](EROSION_GEOMETRIC_RATE_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the uniform-sign special case recovered here.

## Claim

In the landed erosion recurrence

\[
p_{j+1}=\frac{p_j+s_j\epsilon}{1+s_j\epsilon p_j},\qquad
\frac{c_{j+1}}{c_j}=\frac{1-\epsilon^2}{(1+s_j\epsilon p_j)^2},
\]

set \(\epsilon=\tanh\theta\), \(p_0=\tanh\phi_0\), and
\(S_j=\sum_{i<j}s_i\). The step map is exactly tanh addition:

\[
\frac{\tanh\phi+s\tanh\theta}{1+s\tanh\theta\tanh\phi}
=\tanh(\phi+s\theta).
\]

Therefore the path abelianizes in rapidity variables:

\[
p_j=\tanh(\phi_0+S_j\theta).
\]

The complete finite-word erosion law is

\[
\frac{c_n}{c_0}
=\frac{1-p_n^2}{1-p_0^2}
=\left(\frac{\operatorname{sech}(\phi_0+S_n\theta)}
{\operatorname{sech}\phi_0}\right)^2.
\]

Thus the final erosion factor depends on the word only through the net sign
imbalance \(S_n\), while intermediate \(p_j\) depends only on the running
imbalance \(S_j\).

## Periodic corollary

For a periodic word of length \(T\) with imbalance \(D=\sum_{j=1}^T s_j\),
the per-period asymptotic rate is

\[
\rho(\epsilon,w)=r(\epsilon)^{|D|},\qquad
r(\epsilon)=\frac{1-\epsilon}{1+\epsilon}.
\]

This reproduces the landed matrix expression
\(\det(M_w)/\lambda_{\max}(M_w)^2\). Uniform words have \(D=T\), hence rate
\(r(\epsilon)^T\). Alternating balanced words have \(D=0\), hence rate \(1\).

## Balanced random words

For zero-drift seeded random sign words, the standard simple-random-walk
scaling has \(S_n\) at \(\sqrt n\) scale. The exact law above gives

\[
\log(c_n/c_0)
=2\log\left(
\frac{\operatorname{sech}(\phi_0+S_n\theta)}{\operatorname{sech}\phi_0}
\right)
=-2\theta |S_n|+O(1),
\]

so balanced random words exhibit the stretched-decay reading
\(\exp(-2\theta O(\sqrt n))\). The runner gates the exact log identity on
three fixed seeded trajectories through \(n=4000\) and prints one trajectory
as an illustration; the asymptotic reading is the standard random-walk
corollary, not an additional framework-derived probability theorem.

## Scope

The scope is the landed recurrence model, \(|p_0|<1\), \(0<\epsilon<1\), and
finite-dimensional fixed-word verification. No claim is made for dynamics
outside that recurrence. The audit lane grades.
