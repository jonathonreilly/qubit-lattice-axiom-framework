# R19-1 method, fixed before any run (2026-10-13 ~04:00Z)

Setting (TESTS:7157-7161): R18-1's ensemble (N0914 slots, mod-2 law, weight pi ~ exp(-bU sum gamma^2),
moves = XOR of cube + 3 mu8 patterns, every translate; trivial coset of the move span).
RK Hamiltonian (fixed now): H = sum_m t [ -X^{p_m} + exp(-bU Delta_m(C)/2) ], Delta_m(C) = E(C xor p_m) - E(C),
E = sum gamma^2. Each term is t*2cosh(bU Delta/2) times a rank-1 projector annihilating psi0 = sqrt(pi).
So H is frustration-free and H = D^{1/2}(-Lgen)D^{-1/2}, Lgen the Markov generator with rates t*exp(-bU Delta/2).

(a) f-sum, exact classical expression (derived before running):
    f(k,eps) = (1/2)<[O^dag,[H,O]]> = (t/2V) sum_m < exp(-bU Delta_m/2) |sum_{s in p_m} e^{-ik.pos_s} c_s sigma_s|^2 >_pi,
    sigma_s = 1 - 2 n_s, c = eps_jj (diag), 2 eps_ij (face) as in R18-1. Units t = 1.
    Measured by MC as a 6x6 slot-type matrix per k; S(k) as R18-1's 6x6 matrix; same component, same normalization.
(b) omega_SMA(k) = f/S for TT1, TT2, V1, V2, S along axis, face, body (all lattice k, all cubic copies), L = 6, 8.
    bU in {0, 0.5, 1, 2, 3, 3.5}.
    Checks fixed now: bU = 0 exact solution (characters: slot-linear observables decay at 2t N_type exactly,
    N_type = number of moves containing a slot), so omega_SMA must equal 2tN at every k (to MC error).
    Equilibration criterion (fixed now): single-temperature Metropolis (R18-1 mc.py), hot start (bU=0 equilibrium),
    >= 2000 equilibration sweeps (L=6) / 2000 (L=8), then 20 bins. A (bU,L) point is ACCEPTED only if
    (i) E/edge agrees with R18-1's s5b table within 2%, and (ii) two seeds agree on f and S at k_min (axis) within 3 sigma.
    Otherwise it is reported NOT EQUILIBRATED and not used. Nothing above bU = 3.5 is claimed.
(c) ED: L = 2 coset (1024 states): full spectrum of H at bU in {0,1,2,3,4}; TT-channel spectral measure at k = (0,0,pi);
    ground-state degeneracy; spectral gap. Momentum resolution at L = 2 is k in {0,pi}^3 only (no dispersion claim).
(d) Analytic: RK/Markov identity; bU = 0 exact solution; positivity of f_TT(0) at finite bU; parity/analyticity of
    f and S => form of omega_SMA along rays; Rellich-type argument for analytic Rayleigh-Ritz branches.
Readings as registered (TESTS:7174-7178).
