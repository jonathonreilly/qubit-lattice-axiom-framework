"""R19-33 (a): O(kappa) and O(kappa^2) SITE reflection positivity of the coupled
matter + spatial-TT graviton + instantaneous constraint bridge on Euclidean Z^4 (xi = 1).

Setting (hypotheses):
 - free massive scalar, S_m = 1/2 sum[(Delta_mu phi)^2 + m^2 phi^2], spatial torus L^3, time Z;
 - spatial-TT graviton h^TT (K2's reduced form (s4^2+q^2)/4 per polarization), coupled by
   -kappa h^TT_ij T_ij with K2's exact stress; with h traceless the time-link part of T_ii
   (delta_ij x scalar) drops, so the coupling is SLICE-LOCAL (proved in report);
 - bridge (weight factor exp(+B), B = sum_t B_t, B_t instantaneous in slice t):
     GR bridge  B_t = lam [rho K rho + 2 rho K A + 4 Pperp K Pperp + PL K PL]   (r1933_c_decomp.out)
     Newton-only B_t = lam rho K rho
   rho = Minkowski energy density = -T_44, A = transverse trace of T_ij, P = T_4i (half-integer t,
   one-sided for site RP), K = (-Delta_3 + muK^2)^{-1} (screened; muK -> 0 checked), lam = kappa^2/4.
 - two lattice discretizations of the time-link part at slice 0 (a = phi_1 - phi_0, b = Theta a =
   phi_{-1} - phi_0):
     K2 : rho = 1/2 a.b + u      (K2's exactly conserved T_44; straddles slice 0)
     D2 : rho = -1/4 (a^2+b^2) + u   (symmetric link squares; differs by 1/4 (Delta_4^2 phi)^2, O(a^2))
   and in both A = -1/2 (a^2 + b^2) + A_s  (K2's T_ii link squares; transverse trace of delta_ij = 2).
   u = 1/4 sum_i[(D_i phi0)^2 + (D_i phi0(z-e_i))^2] + 1/2 m^2 phi0^2 >= 0, A_s = slice-local part.
Site RP test (exact, O(kappa^2)): given phi_0, the free measure is Markov, so on functions F with
E[F | phi_0] = 0 (the kernel of the O(1) RP matrix) the O(kappa^2) RP matrix is
   M2[i,j] = E_{a,b}[F_i(b) Bcross(b,a) F_j(a)],
with a, b independent copies of the conditional law of phi_1 - phi_0 (computed from the free
half-chain).  O(kappa): the coupling is slice-local and h-odd, so M1 restricted to ker M0 vanishes
and M1(ker, range) = 0 on h-independent F (proved in report).  TT exchange: positive type; on the
odd test functions used here at phi_0 = const it vanishes (parity; see report).
Test functions: F_i = z_i (linear, centred), z = a - E[a].
"""
import numpy as np, itertools, sys
np.set_printoptions(linewidth=140)

def lap3(L):
    N = L ** 3
    idx = np.arange(N).reshape(L, L, L)
    M = np.zeros((N, N))
    for ax in range(3):
        nb = np.roll(idx, -1, axis=ax).ravel()
        for i, j in zip(idx.ravel(), nb):
            M[i, i] += 2; M[i, j] -= 1; M[j, i] -= 1
    return M, idx

def half_chain(L, m, n=8):
    """conditional law of phi_1 given phi_0 for the free half chain (slices 1..n, open end):
    returns (R, C1): E[phi_1|phi_0] = R phi_0, Cov(phi_1) = C1."""
    Lap, idx = lap3(L); N = L ** 3
    Msp = Lap + m * m * np.eye(N)
    Q = np.zeros((n * N, n * N))
    for t in range(n):
        D = (2.0 if t < n - 1 else 1.0) * np.eye(N) + Msp
        Q[t * N:(t + 1) * N, t * N:(t + 1) * N] = D
        if t < n - 1:
            Q[t * N:(t + 1) * N, (t + 1) * N:(t + 2) * N] = -np.eye(N)
            Q[(t + 1) * N:(t + 2) * N, t * N:(t + 1) * N] = -np.eye(N)
    Ci = np.linalg.inv(Q)
    C1 = Ci[:N, :N]
    R = C1.copy()          # linear term phi_0 . phi_1 enters slice 1 with coefficient +1
    return R, C1, Lap, idx

def slice_quantities(phi0, L, m, idx):
    """u >= 0 (slice-local part of rho) and A_s (slice-local part of transverse trace of T_ij),
    with the transverse trace of the delta_ij parts taken as 2x (theta_ii = 2), off-diagonal and
    anisotropic parts projected exactly in momentum space (q=0: theta = 2/3 delta)."""
    p = phi0.reshape(L, L, L)
    D = [np.roll(p, -1, axis=i) - p for i in range(3)]
    Dm = [p - np.roll(p, 1, axis=i) for i in range(3)]
    u = 0.25 * sum(D[i] ** 2 + Dm[i] ** 2 for i in range(3)) + 0.5 * m * m * p ** 2
    # slice-local T_ij (spatial), K2 placement simplified to site-centred symmetric forms
    T = np.zeros((3, 3, L, L, L))
    for i in range(3):
        T[i, i] = 0.5 * D[i] * Dm[i] - 0.25 * sum(D[r] ** 2 + Dm[r] ** 2 for r in range(3) if r != i) - 0.5 * m * m * p ** 2
        for j in range(3):
            if j != i:
                T[i, j] = 0.25 * (D[i] + Dm[i]) * (D[j] + Dm[j])
    k = 2 * np.pi * np.fft.fftfreq(L)
    K = np.meshgrid(k, k, k, indexing='ij'); s = [2 * np.sin(kk / 2) for kk in K]
    s2 = sum(x ** 2 for x in s)
    Tq = np.fft.fftn(T, axes=(2, 3, 4))
    Aq = np.zeros((L, L, L), dtype=complex)
    with np.errstate(invalid='ignore', divide='ignore'):
        for i in range(3):
            for j in range(3):
                th = (1.0 if i == j else 0.0) - np.where(s2 > 0, s[i] * s[j] / np.where(s2 > 0, s2, 1), (1.0/3.0 if i == j else 0.0))
                Aq += th * Tq[i, j]
    A_s = np.fft.ifftn(Aq).real
    return u.ravel(), A_s.ravel()

def M2_linear(mu, C, Kmat, w, disc, bridge):
    """O(kappa^2) RP matrix (per lam) on centred linear test functions z_i."""
    N = len(mu)
    c = np.diag(C)
    M = np.zeros((N, N))
    if disc == 'K2':
        # term 1/4 sum K_xy (a_x a_y)(b_x b_y): E[z_i a_x a_y] = C_ix mu_y + C_iy mu_x
        # V_{i,(x,y)} ; quadratic form sum_xy K_xy V_i,xy V_j,xy
        # = sum_xy K_xy (C_ix mu_y + C_iy mu_x)(C_jx mu_y + C_jy mu_x)
        Kmu2 = Kmat * np.outer(mu, mu)
        T1 = C @ (Kmat * np.outer(mu, mu)) @ C.T * 0  # placeholder (computed below exactly)
        # expand: sum_xy K_xy [C_ix C_jx mu_y^2 + C_ix C_jy mu_y mu_x + C_iy C_jx mu_x mu_y + C_iy C_jy mu_x^2]
        Kmu_y2 = Kmat @ (mu ** 2)                       # sum_y K_xy mu_y^2
        T1 = 2 * (C * Kmu_y2[None, :]) @ C.T + 2 * C @ Kmu2 @ C.T
        M += 0.25 * T1
        # term sum_x w_x a_x b_x (w = K(u + A_s) for GR, K u for Newton)
        M += (C * w[None, :]) @ C.T
        if bridge == 'GR':
            # -1/2 sum K_xy [a_x a_y^2 b_x + a_x b_x b_y^2]
            # E[z_i a_x a_y^2] = 2 mu_x mu_y C_iy + mu_y^2 C_ix + C_ix C_yy + 2 C_iy C_xy
            # U_{i,x} := sum_y K_xy E[z_i a_x a_y^2]
            KmuC = Kmat * mu[None, :]                    # K_xy mu_y
            U = 2 * (C @ (Kmat * mu[None, :]).T) * mu[None, :]  # sum_y K_xy 2 mu_x mu_y C_iy
            U += C * (Kmat @ (mu ** 2 + c))[None, :]     # sum_y K_xy (mu_y^2 + C_yy) C_ix
            U += 2 * C @ (Kmat * C).T                    # sum_y K_xy 2 C_iy C_xy
            V = C                                        # E[z_j b_x] = C_jx
            M += -0.5 * (U @ V.T + V @ U.T)
    elif disc == 'D2':
        # cross = coef * sum K_xy a_x^2 b_y^2 ; E[z_i a_x^2] = 2 mu_x C_ix
        coef = 0.625 if bridge == 'GR' else 0.125
        G = 2 * C * mu[None, :]
        M += coef * G @ Kmat @ G.T
    return 0.5 * (M + M.T)

def run(L, m, muK, phi0_kind, rng):
    R, C1, Lap, idx = half_chain(L, m)
    N = L ** 3
    if phi0_kind == 'zero':
        phi0 = np.zeros(N)
    elif phi0_kind == 'const':
        phi0 = np.ones(N)
    else:
        phi0 = rng.normal(size=N)
    mu = R @ phi0 - phi0             # mean of a = phi_1 - phi_0
    Kmat = np.linalg.inv(Lap + muK ** 2 * np.eye(N))
    u, A_s = slice_quantities(phi0, L, m, idx)
    out = {}
    for disc in ('K2', 'D2'):
        for bridge in ('Newton', 'GR'):
            w = Kmat @ (u + A_s) if bridge == 'GR' else Kmat @ u
            M = M2_linear(mu, C1, Kmat, w, disc, bridge)
            ev = np.linalg.eigvalsh(M)
            out[(disc, bridge)] = (ev[0], ev[-1])
    return out, (Kmat.min() >= 0)

rng = np.random.default_rng(5)
print("O(kappa^2) site-RP matrix (per lam = kappa^2/4) on centred linear test functions of phi_1.")
print("columns: (min eig, max eig) for disc x bridge;  K entrywise >= 0 flag")
for phi0_kind in ('zero', 'const', 'random'):
    print("\n== phi_0 = %s ==" % phi0_kind)
    for L in (3, 4, 5, 6):
        for m in (1.0, 0.5, 0.25):
            for muK in (0.3, 0.1):
                out, kpos = run(L, m, muK, phi0_kind, rng)
                s = " | ".join("%s-%s %+.3e/%+.3e" % (d, b, v[0], v[1]) for (d, b), v in out.items())
                print("L=%d m=%.2f muK=%.1f Kpos=%s :: %s" % (L, m, muK, kpos, s))
        sys.stdout.flush()
