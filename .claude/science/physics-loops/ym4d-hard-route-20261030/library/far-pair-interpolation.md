# Orders 3 and 4 from orders 2 and 5, by a far pair

Status: proved here, 2026-11-01, by the closure gate, `gates/closure-bad958abb.md`. Not reviewed. Elementary calculus; no source needed. Replaces the interpolation *Orders 3, 4* of `library/sector-values.md`, Section 3B, and Step B' of `library/one-step-closure.md`, Section 10. It reads no (Loc^c), no sum over levels at order 3, and no field far from the tuple.

## Setting

D^+ is the class flux <= (1 + c_0) T_2 and D the class flux <= T_2. Put t := c_0 T_2 / 8. Then e^{s r + s' r'} V is in D^+ for V in D, |s|, |s'| <= t, r, r' unit directions at bonds. For V in D let u(xi) := Z(e^{xi} V), a smooth function of a bond field xi near 0, so that D^n Z(V)[a_1, ..., a_n] = d^n u(0)[a_1, ..., a_n], which is symmetric.

Hypotheses, for directions a_i at bonds, d the distance between bonds and tree the shortest tree on the tuple:

- (a) |D^2 Z(V)[p, q]| <= B_2 Phi(d(p, q)/2) on D^+;
- (b) in the coordinates xi at V in D, |d^5 u(xi)[a_1, ..., a_5]| <= B'_5 Phi(tree/2) for xi in the steps above.

(b) is ||Z||_5 <= B_5 on D^+ up to a change of coordinates, which acts only when two directions share a bond: B'_5 <= C (B_5 + sum_{j < 5} B_j), with the B_j read on the larger domain, up to D^+. The terms with j = 3, 4 are removed by iterating the conclusion on a ladder of domains between D and D^+, with steps t_i := t 2^-i: B(rho) <= A t^-2 + C t B(rho + t) iterates to B(rho) <= C' A t^-2 for C t small, the remainder tending to 0 since B is finite (Z is smooth on a compact set of a finite lattice, and no bound on that finite value is used). This is the standard absorption; I have not displayed the sum.

## Lemma FP

*For V in D, n = 3, 4, a tuple a_1, ..., a_n, and Delta := max_{i, j} d(a_i, a_j):*

    |D^3 Z(V)[a_1, a_2, a_3]| <= (2/t) B_2 Phi(Delta/2) + t^2 B'_5 Phi(tree/2),
    |D^4 Z(V)[a_1, ..., a_4]| <= (8/t^2) B_2 Phi(Delta/2) + 4 t B'_5 Phi(tree/2).

*Since tree <= (n - 1) Delta, and with norms read at the rates shown, for C = C(mu) absolute if mu is:*

    ||Z||_3 at rate mu/4 <= C ( T_2^-1 B_2 + T_2^2 B'_5 ),    ||Z||_4 at rate mu/6 <= C ( T_2^-2 B_2 + T_2 B'_5 ),

*on D.*

*Proof.* If Delta = 0 all directions share a bond; take p, q among them and the bound below holds with the constant 2 B_2 replaced by C (B_1 + B_2), which changes nothing for the norms. Otherwise, by symmetry, let p, q be a pair realising Delta. They lie on different bonds, so in xi coordinates, at any xi supported off them or on them alike, d_p d_q u(xi) is D^2 Z(e^{xi} V)[p, q] up to the Jacobian of the coordinate change on the bonds of p and q, of size 1 + C t: no term with a first derivative appears, as the bonds differ. So |d_p d_q u(xi)| <= (1 + C t) B_2 Phi(Delta/2) on the steps above, by (a).

n = 3, with r the third direction. Let g(s) := d_p d_q u(s r). Central difference: g'(0) = (g(t) - g(-t))/(2 t) + O(t^2 sup |g'''|)/6, and g''' is a fifth derivative of u on the tuple (p, q, r, r, r), whose tree is that of the tuple. So (b) gives the first display.

n = 4, with r, r' the other two. If they differ, let g(s, s') := d_p d_q u(s r + s' r'). Then g(t, t) - g(t, 0) - g(0, t) + g(0, 0) = int_0^t int_0^t d_s d_s' g, which is t^2 d_s d_s' g(0) up to t^3 times the sup of the third derivatives of g, fifth derivatives of u on the tuple. If r = r' use g(t) - 2 g(0) + g(-t) = t^2 g''(0) + O(t^3 sup |g'''|). So (b) gives the second display.

Norms. Pointwise, for the first tier, Phi(Delta/2) <= Phi(tree/(2 (n - 1))), so |D^3| is at most e^{-mu tree/4} times the bracket, and |D^4| at most e^{-mu tree/6} times the bracket. Dividing by the norm's weight at the rate shown leaves e^{-mu tree/8}, e^{-mu tree/12}, which sum over the free bonds to C mu^-8, C mu^-12. The second tier: as in `library/one-step-closure.md`, Section 1, split the sum at tree length y_*. QED

## What it changes

1. (Loc^c) is not read, at any order. Four failures of the old step go with it: the system for B_3, B_4 with one step size, whose coefficient is exactly 1; order 3 locality, which has no sum over levels; the rate mu_c(L) of (Loc^c), which is not recovered by a factor L; and steps that leave the class.
2. Rates are mu/4, mu/6, not mu/2, mu/4. "A lift multiplies a rate by L" needs L >= 6 for this.
3. B_1 is read only when all directions share a bond.
4. (Loc^c_k) is then a separate clause, and the recursion of `library/sector-values.md`, Section 5, with D_n proportional to B_{n+1}, proves it with no circle, as B_3, B_4 no longer read it.
5. D^+ is the domain of orders 1, 2 and 5, 6; orders 3, 4 hold on D. This is the existing enlargement of T_2 by a fixed factor, once more. Orders 3, 4 are read at V^*(V') and at Phi(xi), of flux at most C_r L^-1 (1 + c_0) T_2 + tau, so inside D.
