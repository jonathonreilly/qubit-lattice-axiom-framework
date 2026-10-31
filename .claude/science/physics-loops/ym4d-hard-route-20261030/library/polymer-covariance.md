# Covariance of a rare polymer gas with general interactions

Producer: `parts/hard-core--mapped.md`, Text 5. Status: proved here. Not reviewed.

Credit. The contraction of oscillations under single-site updates is Dobrushin's uniqueness method; the covariance estimate is Föllmer's (1982). The derivation below through the continuous-time update semigroup is written out so that nothing is load-bearing. The application to polymers with only first-difference bounds is mine, and it replaces the Kirkwood-Salsburg route I had planned, which needed mixed differences of all orders.

Consumers: `Rare cells` in the real one-step theorem.

## Setting

I is a finite index set (polymers). Each i has a state space X_i with a distinguished state 0 (absent) and a reference measure nu_i with nu_i({0}) = 1. A probability measure mu on prod_i X_i has conditional laws pi_i(. | sigma_{-i}). Define

- v_i := sup_sigma pi_i(sigma_i != 0 | sigma_{-i}),
- C_{ji} := sup { TV( pi_j(.|sigma), pi_j(.|sigma') ) : sigma, sigma' differ only at i }, for i != j, with C_{ii} = 0,
- osc_i(f) := sup { |f(sigma) - f(sigma')| : sigma, sigma' differ only at i }.

Assume there are weights w_i > 0 with

    (D)  sup_j (1/w_j) sum_k C_{kj} w_k =: theta < 1.

## Lemma 1

For bounded f, g,

    |cov_mu(f,g)| <= 2 sum_j v_j osc_j(g) sum_i G_{ji} osc_i(f),     G := sum_{n >= 0} (C^T)^n,  (C^T)_{jk} = C_{kj}.

*Proof.* Let Pi_i f(sigma) := integral pi_i(d sigma_i | sigma_{-i}) f(sigma), L := sum_i (Pi_i - 1), P_t := e^{tL}. Each Pi_i is self-adjoint in L^2(mu), so P_t is reversible.

*Oscillations.* osc_j(Pi_j g) = 0. For k != j, comparing the two integrals against pi_k given sigma and sigma' that differ at j: osc_j(Pi_k g) <= osc_j(g) + C_{kj} osc_k(g). So osc_j((1 + dt L) g) <= (1 - dt) osc_j(g) + dt sum_k C_{kj} osc_k(g) + o(dt). With a_j(t) := osc_j(P_t f) this reads d a_j/dt <= -a_j + sum_k C_{kj} a_k. Since the off-diagonal part is non-negative, a(t) <= e^{-t(1 - C^T)} a(0) entrywise. By (D), C^T has norm at most theta in the sup norm weighted by w, so e^{-t(1-C^T)} decays exponentially and

    integral_0^infty a_j(t) dt <= sum_i G_{ji} osc_i(f).

*Convergence.* Each coordinate oscillation of P_t f tends to 0, so P_t f tends to a constant, which is mu(f).

*The identity.* cov(f,g) = - integral_0^infty d/dt mu(P_t f . g) dt = - integral_0^infty mu(L P_t f . g) dt = integral_0^infty sum_j mu( (1 - Pi_j) P_t f . g ) dt, and mu((1 - Pi_j) h . g) = mu( cov_{pi_j}(h, g) ), the conditional covariance at site j. Under pi_j, the state 0 has mass at least 1 - v_j. Subtracting the values at sigma_j = 0, |cov_{pi_j}(h,g)| <= (v_j + v_j^2) osc_j(h) osc_j(g) <= 2 v_j osc_j(h) osc_j(g). Insert and integrate. QED

## Lemma 2 (polymers)

Let the index set consist of polymers gamma: finite connected sets of cells at range d_0 in a metric space with uniform growth. Let the states of gamma be 0 or hole data. Let mu be given by a weight W >= 0 on compatible families, where gamma, delta are compatible if their distance is at least d_0, normalised by W(empty) = 1. Assume, for hole data held fixed:

- (A1) Absolute rarity: for gamma compatible with a family F, integral over the data of gamma of W(F u gamma)/W(F) is at most z^{|gamma|}, uniformly in F and its data.
- (A2) First differences: for gamma compatible with F and with delta, and delta compatible with F, |log [ W(F u gamma u delta) W(F) / ( W(F u gamma) W(F u delta) ) ]| <= kappa(gamma, delta) := kappa_0 |gamma| |delta| e^{-mu_1 d(gamma, delta)}.

Let c_a be the lattice-animal growth at range d_0, so that the number of polymers of m cells containing a given cell is at most c_a^m. If z c_a e^{2a} <= 1/32 for an a >= 1, and z c_a e^{2a} kappa_0 G(mu_1/2) <= 1/32 and sup_m m C(d_0) e^{-a m} <= 1 for the neighbourhood count C(d_0), then with nu := min(mu_1/2, a/(2 d_0)):

(i) v_gamma <= z^{|gamma|}, and C_{gamma delta} <= 2 z^{|gamma|} min(1, 2 kappa(gamma,delta)) for compatible pairs, C_{gamma delta} <= z^{|gamma|} for incompatible ones.

(ii) (D) holds with weights w_gamma := e^{a |gamma|} e^{-nu d(gamma, y)} for each point y, with theta <= 1/2.

(iii) For bounded f, g with osc_gamma(f) <= A_f (1 + |gamma|) e^{-mu_1 d(gamma, y_f)}, and the same for g at y_g,

    |cov_mu(f,g)| <= C z A_f A_g e^{-nu d(y_f, y_g)}.

*Proof.* (i) pi_gamma(sigma_gamma != 0 | rest) is a ratio at most the integrated W(F u gamma)/W(F), so (A1) gives v. If an incompatible delta is present, pi_gamma is the point mass at 0, so the variation against the other conditional is at most z^{|gamma|}. If delta is compatible, the two conditional odds, as densities on the data of gamma, differ by a factor e^{u}, |u| <= kappa, by (A2) applied pointwise in the data of gamma. So the variation is at most 2 z^{|gamma|} (e^{kappa} - 1), and also at most v + v' <= 2 z^{|gamma|}, by (A1) with and without delta.

(ii) Fix delta and sum over gamma the quantity C_{gamma delta} w_gamma/w_delta. With q the point of gamma nearest y, d(delta,y) - d(gamma,y) <= d(gamma,delta) + diam gamma, so w_gamma/w_delta <= e^{a|gamma| - a|delta|} e^{nu (d(gamma,delta) + diam gamma)}, and diam gamma <= d_0 |gamma|, so e^{nu diam gamma} <= e^{a|gamma|/2}. Incompatible gamma: d(gamma,delta) < d_0 and e^{nu d_0} <= e^{a/2}. The count of gamma of m cells within d_0 of delta is at most C(d_0) |delta| c_a^m, so the sum is at most C(d_0) |delta| e^{-a|delta|} e^{a/2} sum_m (z c_a e^{3a/2})^m <= 2 e^{a/2} z c_a e^{3a/2} <= 1/16. Compatible gamma: e^{nu d} min(1, 2 kappa) <= 2 kappa_0 |gamma| |delta| e^{-(mu_1/2) d}. Summing over positions with G(mu_1/2), using |gamma| e^{-a|gamma|/2} bounded, and including the factor 2 from (i), the same assumptions give at most 1/4. So theta <= 1/2.

(iii) Apply Lemma 1. By (ii), G has weighted sup-norm at most 2. Take the weight at y = y_f: the vector osc(f) is at most C A_f w_gamma, because nu <= mu_1/2 and the factor (1+|gamma|) e^{-a|gamma|} is bounded. So sum_i G_{ji} osc_i(f) <= 2 C A_f e^{a|j|} e^{-nu d(j, y_f)}. Then sum_j v_j osc_j(g) e^{a|j|} e^{-nu d(j,y_f)} <= C A_g sum_j z^{|j|} e^{a|j|} (1+|j|) e^{-mu_1 d(j,y_g)} e^{-nu d(j,y_f)}, and summing over j, with d(j,y_f) + d(j,y_g) >= d(y_f,y_g) and growth, gives C z A_g e^{-nu d(y_f,y_g)}. QED

## Why this suffices, and what failed

The covariance of two local functions needs no bound on mixed differences of the weights of order greater than one. Only first differences enter, through single-site updates, and these are exactly what the convex propagator supplies: conditional odds of a polymer change by at most the mutual information across the exterior, which is a pair bound uniform in all other holes.

Tried and dropped, in this order.

1. *Dobrushin on cell statuses.* Fails at adjacency: given a wild neighbour, a cell's non-class state can be as likely as its class state, so the influence is not small. Polymers as the sites repair this, since the state of a polymer is a whole connected set, and (A1) is absolute.
2. *Separating shells.* A polymer-free shell around y_1 has probability near 1 only below a radius z^{-1/6}, so it gives a small constant but no decay beyond that radius.
3. *Chain order adapted to the derivative points.* It gives the first derivative at once: order cells by decreasing distance from y, so that no polymer lies nearer to y than the current cell. At two points it leaves the correlation between polymers near y_1 and near y_2.
4. *Kirkwood-Salsburg with many-body weights.* Its kernel is a Möbius sum of the conditional energies, and first-difference bounds give only 2^{|S|} times the smallest interaction, which does not sum over large sets. Product bounds would need the tree structure of all orders, with constants from the Laplace lemma that I do not control in the number of perturbations.
5. *Langevin coupling on the exact non-convex measure.* The Hessian is bounded below in the B variables, so contraction fails only in rare regions, but a metastable hole has an exponentially long residence, and exponential moments of the time spent there are not under control.
