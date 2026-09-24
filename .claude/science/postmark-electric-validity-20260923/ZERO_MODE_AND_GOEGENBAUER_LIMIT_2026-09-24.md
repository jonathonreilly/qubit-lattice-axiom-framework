---
claim_id: postmark_electric_zero_mode_and_slow_form_2026_09_24
claim_type: bounded_theorem
claim_scope: "Conditional on the supplied six-site integer-spin one-vacancy hop map, M_S=A_S^*A_S has a unique exact zero mode. Its normalized electric-flux law converges on x=n/(5S) to (15/16)(1-x^2)^2 dx. After staggering and conjugating by the positive zero mode, the rescaled forms C M_S converge to the Gegenbauer form (1/25) integral (1-x^2)^3 |f'|^2 dx in L^2((15/16)(1-x^2)^2 dx), and each fixed-index eigenvalue C lambda_(S,j) converges to j(j+5)/25."
upstream_dependencies:
  - PR #8831 supplied one-vacancy hop map and integer-spin link factors
  - Conditional short-time and fixed-time campaign checkpoint in PR #8943
runner: .claude/science/postmark-electric-validity-20260923/zero_mode_profile.py
---

# Exact zero mode and the Gegenbauer slow-sector form

**Date:** 2026-09-24
**Type:** bounded_theorem

## Result up front

The supplied finite-spin hopping matrix has an exact one-dimensional kernel. After removing its alternating sign, its amplitude is parabolic across the macroscopic electric interval, so its probability law tends to the Gegenbauer weight \(\rho(x)dx=(15/16)(1-x^2)^2dx\) on \([-1,1]\). The rescaled forms converge, and each fixed-index eigenvalue obeys \(C\lambda_{S,j}\to j(j+5)/25\). This identifies a controlled slow spectral sector; it does not control the moving-index spectrum or the fixed-laboratory-time vacancy readout.

## Scope and imported model

The exact theorem is conditional on the supplied six-site one-vacancy path, its integer-spin link shift, and the actual first-mark output. The source is [PR #8831](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8831), at head `b6eb31bedb3134dfacd8f4ab83cb7d96fc6dc953`, based on open PR #8672 at `fe6dc2c5ef061fa1e0051063d49178f23b872c13`. Its source derivation is [`FAST_VACANCY_MOTION_AFTER_FORMATION.md`](../mobile-record-formation-20260920/campaign12h_third/post_birth_fast_motion_author/FAST_VACANCY_MOTION_AFTER_FORMATION.md), SHA-256 `76d7f2faf3a0b4635499ddff1d8a88868d691d58c035780af737129701e30eeb`. The prepared path state is `|0>` in that source's winding component. The link factor `-sqrt(1-m(m+a)/C)` and path/output identification are imported conditions; this note derives no Hamiltonian, transition rule, or new axiom from the four framework axioms.

The proof obligations are: (1) identify each legal one-hop intermediate row and its residue factors from the supplied 15-step path; (2) solve the exact bidiagonal kernel recurrence and telescope its block products; (3) pass from the zero-mode profile to its normalized macroscopic law; and (4) prove compactness, recovery, and lower semicontinuity for the transformed forms before applying min-max. The first two use the supplied graph plus the explicit link formula; the third is a Riemann-sum argument with endpoint control; the fourth is the analytic weighted-form argument below. The runner checks the hop incidence and residue table for `1<=S<=20` and provides numerical profile/eigenvalue diagnostics; those finite checks do not replace the all-S residue derivation or the compactness proof.

## Exact finite-spin zero mode

Let \(P\) be the supplied one-vacancy sector, \(\Pi_1\) the sector reached by one hop with one empty A site, and \(T_S\) the supplied Hermitian finite-spin hop map. Set

    A_S = Pi_1 T_S P,       M_S = -H_(2,S) = A_S^* A_S,
    C = S(S+1),              I_S = [-5S, 5S-4] intersect Z.

The one-vacancy path has \(N_S=10S-3\) vertices. Direct legal-hop enumeration gives exactly \(N_S-1\) intermediate states, one for each adjacent pair \(n,n+1\). Each intermediate row in \(A_S\) has precisely two nonzero entries:

    (A_S)_(r,n)   = -sqrt(1 - x_L/C),
    (A_S)_(r,n+1) = -sqrt(1 - x_R/C),
    x_L=m_L(m_L+1),       x_R=m_R(m_R+1).

The exact integer offsets are below. For \(n=15k+r\ge0\), use \(m_L=3k+L_r^+\), \(m_R=3k+R_r^+\). For \(n=-15K+r<0\), where \(K=\lceil -n/15\rceil\) and \(r=n+15K\), use \(m_L=3K+L_r^-\), \(m_R=3K+R_r^-\).

These are effective labels for the radicands: when a physical hop has shift `a=-1`, replace its source label `m` by `m-1`, so `m(m+a)` becomes `m_eff(m_eff+1)`. On the supplied finite path both effective labels lie in `[-S,S-1]`.

| \(r\) | \(L_r^+\) | \(R_r^+\) | \(L_r^-\) | \(R_r^-\) |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | -1 | -1 |
| 1 | 1 | 0 | -2 | -1 |
| 2 | 0 | 0 | -1 | -1 |
| 3 | 1 | 1 | -2 | -2 |
| 4 | 1 | 0 | -2 | -1 |
| 5 | 1 | 1 | -2 | -2 |
| 6 | 2 | 1 | -3 | -2 |
| 7 | 1 | 1 | -2 | -2 |
| 8 | 2 | 2 | -3 | -3 |
| 9 | 2 | 1 | -3 | -2 |
| 10 | 2 | 2 | -3 | -3 |
| 11 | 3 | 2 | -4 | -3 |
| 12 | 2 | 2 | -3 | -3 |
| 13 | 3 | 3 | -4 | -4 |
| 14 | 3 | 2 | -4 | -3 |

For \(1\le S\le20\), the runner rebuilds the finite-spin hop map and checks its row count, path incidence, and every in-domain entry of this table. The formulas follow exactly from the path's 15-step flux translation: the residue pattern is fixed and the electric field shifts affinely by three per block.

Write \(R_m=C-m(m+1)\). The null-vector row equation gives \(h_S(n+1)/h_S(n)=\sqrt{R_{m_L}/R_{m_R}}\) for an alternating vector \(\varphi_S(n)=(-1)^n h_S(n)\). Multiplying the fifteen residue ratios gives the exact rational identities

    product_(r=0..14) R_(3k+L_r^+)/R_(3k+R_r^+) = [R_(3k+3)/R_(3k)]^2,
    product_(r=0..14) R_(3K+L_r^-)/R_(3K+R_r^-) = [R_(3K-4)/R_(3K-1)]^2.

Since every in-domain \(R_m\) is positive, taking the positive square root and telescoping successive blocks gives, for every in-domain block index,

    h_S(15K)/h_S(0)  = R_(3K)/C,
    h_S(-15K)/h_S(0) = R_(3K-1)/C.

Each right coefficient is nonzero: its effective integer label lies in `[-S,S-1]`, so (R_m=(S-m)(S+m+1)>0). Restricting the bidiagonal \((N_S-1)\times N_S\) matrix to columns `n+1` gives a triangular square matrix with these nonzero coefficients on its diagonal. Thus \(A_S\) has full row rank and this is its unique kernel up to scale. Therefore \(M_S\varphi_S=0\), and also \(G_S\varphi_S=(M_S^2-CM_S)\varphi_S=0\) exactly.

## Macroscopic zero-mode law

Set \(x_n=n/(5S)\). The exact block formulas, together with at most 14 within-block ratios, imply uniformly on each compact subset of \((-1,1)\)

    h_S(n)/h_S(0) = 1 - x_n^2 + O_epsilon(S^-1).

The amplitude decreases moving out from the origin on both sides. This monotonicity controls the edge strips: a strip of width \(\epsilon\) in \(x\) has unnormalized mass at most \(O(\epsilon^3 S)\) relative to \(h_S(0)^2\). Interior Riemann sums then give

    sum_(n in I_S) [h_S(n)/h_S(0)]^2  ~  (16/3) S,
    |varphi_S(0)|^2  ~  3/(16S).

For each continuous \(F\) on \([-1,1]\),

    sum_n |varphi_S(n)|^2 F(x_n)
      -> (15/16) integral_(-1)^1 (1-x^2)^2 F(x) dx.

The unique exactly stationary component in the prepared vector has squared amplitude \(|\langle\varphi_S,0\rangle|^2\sim3/(16S)\). For any norm-one observable, removing that rank-one component changes its expectation by at most \(2|\langle\varphi_S,0\rangle|+|\langle\varphi_S,0\rangle|^2=O(S^{-1/2})\), uniformly in time. The stationary mode cannot by itself sustain an order-one fixed-time discrepancy.

## Rescaled slow-sector form

Let \(J|n\rangle=(-1)^n|n\rangle\), \(N_S=JM_SJ\), and let \(g_S(n)=|\varphi_S(n)|>0\) be the normalized positive zero mode of \(N_S\). With \(b_{S,n}=(M_S)_{n,n+1}\), the exact ground-state transform is

    <g_S f_S, N_S g_S f_S>
      = sum_(n,n+1 in I_S) b_(S,n) g_S(n)g_S(n+1)
          |f_S(n+1)-f_S(n)|^2.

On compact subsets of \((-1,1)\), the exact Jacobi factors give \(b_{S,n}\to1-x^2\), while \(g_S(n)^2\sim\rho(x_n)/(5S)\). Thus for each \(f\in C^1([-1,1])\), with \(f_S(n)=f(x_n)\),

    ||g_S f_S||^2 -> integral rho(x)|f(x)|^2 dx,
    C <g_S f_S,N_S g_S f_S>
      -> (1/25) integral rho(x)(1-x^2)|f'(x)|^2 dx.

The limiting weighted differential expression is

    L f = -[25 rho(x)]^-1 d/dx [(1-x^2) rho(x) f'(x)]
        = -(1/25)[(1-x^2)f''(x)-6x f'(x)].

Its polynomial eigenfunctions are the Gegenbauer polynomials \(C_j^{5/2}(x)\), with eigenvalues \(j(j+5)/25\). Convergence of the Gram and form matrices on the first \(j+1\) polynomial trial functions and min-max first give an upper bound.

    limsup_(S->infinity) C lambda_(S,j) <= j(j+5)/25,

where \(\lambda_{S,j}\) is the \(j\)-th eigenvalue of \(M_S\), starting at \(j=0\). A matching lower bound follows from compactness at the degenerate endpoints. Set \(\delta_S=(5S)^{-1}\), \(\pi_S(n)=g_S(n)^2\), and \(\kappa_S(n)=b_{S,n}g_S(n)g_S(n+1)\). The exact block products and link factors imply, with constants independent of S and n,

    pi_S(n)      comparable to delta_S (1-|x_n|+delta_S)^2,
    kappa_S(n)   comparable to delta_S (1-|x_(n+1/2)|+delta_S)^3.

The uniform comparison follows from

    R_m/C = ((S-m)/S) ((S+m+1)/(S+1)),       R_m=C-m(m+1).

The residue table has only fifteen entries, and each within-cell recurrence uses a fixed number of factors whose integer offsets differ by at most four. On `0 <= m <= S-1`, the first factor is the edge distance and the second is bounded above and below; on `-S <= m < 0`, the second factor is the edge distance and the first is bounded above and below. Thus `R_m/C` is comparable to `1-|m|/S+1/S`. The table places `|m|` within a fixed integer distance of `|n|/5`; adding `1/S` makes the comparison uniform even at a spin edge. The exact block products give the same comparison at cell endpoints. Hence, with constants independent of `S` and `n`,

    h_S(n)/h_S(0)        comparable to 1-|x_n|+delta,
    sum_n h_S(n)^2        comparable to delta^-1,
    pi_S(n)               comparable to delta(1-|x_n|+delta)^2.

The off-diagonal is `b_(S,n)=sqrt(R_(m_L)/C * R_(m_R)/C)` for the two hops shared by neighboring columns. The same finite-offset comparison yields `b_(S,n)` comparable to `1-|x_(n+1/2)|+delta`; multiplying by the adjacent zero-mode amplitudes gives the stated comparison for `kappa_S(n)`. On compact interior sets the exact products give the sharper local limits `pi_S(n)/delta -> rho(x_n)` and `kappa_S(n)/delta -> rho(x_(n+1/2))(1-x_(n+1/2)^2)`.

On a compact interior interval these bounds give ordinary discrete \(H^1\) compactness. At either endpoint, choose a node `a` in a fixed central interval with `|f_a|^2 <= K ||f||_(pi_S)^2`; it exists by averaging. Weighted Cauchy-Schwarz from `a` toward the endpoint and the resistance estimate

    sum_(j between a and n) 1/kappa_S(j) <= K delta_S^-2 (1-|x_n|+delta_S)^-2

give `|f_n|^2 <= 2|f_a|^2 + K q_S(f)/(1-|x_n|+delta_S)^2`; here `C delta_S^2` is bounded above and below uniformly. Since the strip mass is at most `K epsilon^3` and each product `pi_S(n) delta_S^-2 (1-|x_n|+delta_S)^-2` is at most `K delta_S`, summing over its at most `K epsilon/delta_S` sites gives the uniform tail bound

    sum_(|x_n|>=1-epsilon) pi_S(n)|f_n|^2
      <= K[epsilon^3 ||f||_(pi_S)^2 + epsilon q_S(f)],

for \(q_S(f)=C\sum_n\kappa_S(n)|f_{n+1}-f_n|^2\) and \(\delta_S\le\epsilon<1/4\). This is the range needed for compactness: fix epsilon, take S large enough that delta_S <= epsilon, then send epsilon to zero. More explicitly, linearly interpolate each grid vector between adjacent nodes. On compact interior intervals the local weight and conductance limits bound the interpolants in ordinary \(H^1\); Rellich compactness gives a strongly convergent subsequence there. The displayed endpoint estimate makes the omitted weighted norm uniformly small as the interval expands, so the discrete embedding is compact in the limit. For the continuum form, \(\rho(x)\asymp d(x)^2\) and \((1-x^2)\rho(x)\asymp d(x)^3\) at an endpoint, where \(d(x)=1-|x|\); the same resistance calculation gives the continuum tail estimate. Sampling a smooth function gives a recovery sequence; on each compact interior interval, coefficient convergence and weak lower semicontinuity give the form liminf, and increasing the interval to `(-1,1)` gives the global liminf. The limiting closed form is the closure of

    q(f) = (1/25) integral rho(x)(1-x^2)|f'(x)|^2 dx

on smooth functions, with no imposed endpoint values. Endpoint cutoffs of width `epsilon` cost `O(epsilon^2)` in this form because `(1-x^2)rho(x)=O(distance^3)`, so no endpoint trace condition survives the closure. Its associated operator has the displayed Gegenbauer polynomials as a complete orthogonal family of eigenfunctions; integration by parts has no endpoint term for these polynomials because `(1-x^2)rho(x)` vanishes cubically. The compact min-max argument therefore yields

    C lambda_(S,j) -> j(j+5)/25    for every fixed j=0,1,2,...

For each fixed j, the transformed normalized eigenfunction is locally \(H^1\)-bounded near \(x=0\), hence its value there is bounded. Since \(g_S(0)^2\sim3/(16S)\), its spectral weight in the prepared basis state obeys \(|\langle 0,u_{S,j}\rangle|^2=O_j(S^{-1})\). Any fixed finite set of these slow modes therefore has vanishing total initial weight and changes a norm-one readout by at most \(O_J(S^{-1/2})\), uniformly in time. The double-precision scan through \(S=1024\) agrees numerically through \(j=12\); it corroborates the theorem but is not used in its proof.

## Remaining fixed-time obligation

The entire fixed-index slow sector has vanishing initial weight, but this gives no uniform estimate when the mode index grows with S. The fixed-time signal still depends on that moving-index spectral tail and its off-diagonal phases under \(e^{itCM_S}\), with \(T=Ct\asymp S^2\). Candidate-domain selection, electric tails, and \(H_4\)/output corrections also remain open. No axiom or primitive is changed or derived.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: postmark_electric_zero_mode_and_slow_form_2026_09_24
target_blocker_text: "joint finite-spin electric limit"
source_of_blocker_text: handoff
reachability_to_target: supports
conditional_surface_status: conditional on the supplied six-site Hamiltonian, hop map, spin representation, and first-mark output
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The zero-mode and fixed-index spectral conclusions are conditional theorems on the supplied finite-spin hop map and prepared basis state; no axiom derivation or fixed-time readout limit is claimed."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: theorem
next_trace_action: "Control the growing-index off-diagonal spectral phases at fixed t, or certify a bounded-observable discrepancy; the exact stationary mode has vanishing initial weight and the slow-form result is only a fixed-profile statement."
```

The theorem is conditional on open parent PR [#8831](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8831). The source-relative campaign checkpoint is [#8943](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8943). Neither result derives the supplied Hamiltonian from the framework axioms or answers the fixed-laboratory-time comparison.

## Verification

`zero_mode_profile.py` rebuilds the intermediate-hop map from physical charge and electric-field states, checks the one-hop residue table and null-vector recurrence, and records block-product residuals. The analytic compactness and form-liminf argument above supplies the lower spectral bound; the runner does not implement that proof. Its zero-mode profile and low eigenvalues are evaluated in double precision and serve only as corroborating diagnostics. It establishes no fixed-time dephasing.
