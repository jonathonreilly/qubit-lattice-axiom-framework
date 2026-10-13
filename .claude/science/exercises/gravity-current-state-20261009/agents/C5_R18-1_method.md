# R18-1 method, fixed before any run (2026-10-13 ~02:00Z)

Ensemble (TESTS R18-1 setting): N0914 slots (diag n_jj at sites, face n_ij at x+(e_i+e_j)/2), labels n in {0,1},
mod-2 law (G n even on every edge, G = N0914 integer stencil, N0914:95-97), weight exp(-bU * sum_edges gamma^2),
gamma = (G n)/2 in {-1,0,1}. Moves: XOR of R17-1's minimal F2-invariant patterns (cube = 6 faces of a lattice cube;
mu8, 3 orientations), every translate; Metropolis. Sector = the coset of the move span containing n = 0.

(a) Exact: F2 ranks of G and of the move span at L = 2..6 (codimension = non-local sectors the moves cannot reach).
    Detailed balance: symmetric involutive proposals + Metropolis (proved); exact enumeration of the move-span coset
    at the smallest L where it is feasible, compared with the MC histogram of sum gamma^2 and with S(k) at the allowed k.
(b) Observables, fixed now: S_ab(k) = <|O_a(k)|^2>/V, O_eps(k) = sum_s e^{-ik.pos_s} c_s n_s with c = eps_jj on diagonal,
    2 eps_ij on face slots (R17-1 probe), for unit eps in the five traceless helicity channels relative to k-hat:
    TT (2), V (2), S (1); plus the trace. S_gamma(k) = <|gamma(k)|^2>/V (sum over the 3 components).
    Directions: axis (100), face (110), body (111); all lattice k = 2 pi m/L along them.
(c) Pinch diagnostic, fixed now: the longitudinal fraction along the axis, f_V(k) = S_V(k z) / S_TT(k z) and the
    direct-vs-transverse comparison S_xz,xz(k z) vs S_xz,xz(k y). Fit, at each (bU, L), the screened-Coulomb form
    S_V(k z) = A_V * kappa^2/(q^2 + kappa^2) + B_V with q^2 = 4 sin^2(k/2) [Identity V makes S_V = S_gamma/sin^2(k/2)];
    xi = 1/kappa. SCREENED if kappa(bU) converges in L (kappa*L grows with L) at every finite bU; PINCH-PRESENT if
    kappa ~ 1/L (kappa*L constant) at some finite bU with nonzero gamma density.
    Stillinger-Lovett-type check: S_gamma(k)/q^2 -> finite constant at small k (screened) versus -> 0 (pinch).
bU = infinity: sampled only if a move set that preserves gamma = 0 exactly and is checked ergodic is available;
otherwise reported as not sampled (ergodicity failure), with the reason.
(d) Analytic: attempt the extension of Theorem Z to k^0 f-sum + finite chi_TT; or exhibit the obstruction.
No result is extrapolated beyond the largest L run.
