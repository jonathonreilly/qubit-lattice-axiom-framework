"""F2 cross-check: brute-force 4x4 Dirac algebra + numerical k0 quadrature for the fermion self-energy
of lattice QED on Z^3 with continuous time, in covariant gauge xi (xi=1 Feynman, xi=0 Landau-type).
Checks (i) the semi-analytic Feynman-gauge formulas of f2_qed_speeds.py, (ii) gauge-parameter independence
of dc_f = a1 - a0 (the physical speed shift), at small L.
Gamma(p) = S0^{-1}(p) + T(p) - Sigma_sun(p),
  Sigma_sun(p) = sum_{mu,nu} int_k V_mu(p<-q) S0(q) V_nu(q<-p) D_mu,nu(k),  q = p - k,
  V_0 = i e g0,  V_j = i e g_j cos((p_j+q_j)/2),  D = [delta - (1-xi) khat khat/K^2]/K^2 (K^2 = k0^2+khat^2+lam^2),
  T(p) = -(e^2/2) sum_j <A_j^2> i g_j sin p_j.
"""
import numpy as np, sys
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
Z = np.zeros((2, 2)); I2 = np.eye(2)
g = [np.block([[Z, I2], [I2, Z]])] + [np.block([[Z, -1j * s], [1j * s, Z]]) for s in (s1, s2, s3)]
for a in range(4):
    for b in range(4):
        assert np.allclose(g[a] @ g[b] + g[b] @ g[a], 2 * (a == b) * np.eye(4))

def gamma_of_p(p, L, m, lam, xi, nk0=120):
    k = (np.arange(L) + 0.5) * 2 * np.pi / L - np.pi
    KX, KY, KZ = [x.ravel() for x in np.meshgrid(k, k, k, indexing="ij")]
    t, wt = np.polynomial.legendre.leggauss(nk0)
    sc = 1.0
    k0 = sc * np.tan(np.pi * t / 2); dk0 = wt * sc * (np.pi / 2) / np.cos(np.pi * t / 2) ** 2
    kv = np.stack([KX, KY, KZ])
    khat = 2 * np.sin(kv / 2)
    khat2 = (khat ** 2).sum(0)
    tot = np.zeros((4, 4), complex)
    # tadpole <A_j^2> = int [1 - (1-xi) khat_j^2/K^2]/K^2  (k0 integral numerically for consistency)
    A2 = np.zeros(3)
    for i0 in range(nk0):
        K2 = k0[i0] ** 2 + khat2 + lam ** 2
        q0 = p[0] - k0[i0]
        q = p[1:, None] - kv
        sq = np.sin(q)
        den = q0 ** 2 + (sq ** 2).sum(0) + m ** 2
        # S0(q) = (-i g0 q0 - i g_j s_j + m)/den
        cvec = np.cos((p[1:, None] + q) / 2)  # c_j
        khat_mu = np.vstack([np.full(KX.shape, k0[i0]), khat])
        cmu = np.vstack([np.ones(KX.shape), cvec])
        # coefficient arrays of S0: S0 = sum_a Sa * g_a + m/den * 1
        Sa = np.vstack([-1j * q0 * np.ones(KX.shape), -1j * sq]) / den
        Sm = m / den
        for mu in range(4):
            for nu in range(4):
                Dmn = ((mu == nu) - (1 - xi) * khat_mu[mu] * khat_mu[nu] / K2) / K2
                w = cmu[mu] * cmu[nu] * Dmn
                if np.allclose(w, 0):
                    continue
                # (ie)^2 g_mu S0 g_nu, e=1
                acc = np.zeros((4, 4), complex)
                for a in range(4):
                    acc += np.mean(Sa[a] * w) * (g[mu] @ g[a] @ g[nu])
                acc += np.mean(Sm * w) * (g[mu] @ g[nu])
                tot += -1.0 * acc * dk0[i0] / (2 * np.pi)
        for j in range(3):
            A2[j] += np.mean((1 - (1 - xi) * khat[j] ** 2 / K2) / K2) * dk0[i0] / (2 * np.pi)
    Sigma = tot
    T = sum(-0.5 * A2[j] * 1j * g[j + 1] * np.sin(p[j + 1]) for j in range(3))
    return T - Sigma, A2

def coeffs(L, m, lam, xi, h=1e-3):
    def c0(p0):
        G, _ = gamma_of_p(np.array([p0, 0, 0, 0.]), L, m, lam, xi)
        return np.trace(g[0] @ G) / (4j)
    def c1(px):
        G, _ = gamma_of_p(np.array([0, px, 0, 0.]), L, m, lam, xi)
        return np.trace(g[1] @ G) / (4j)
    a0 = ((c0(h) - c0(-h)) / (2 * h)).real
    a1 = ((c1(h) - c1(-h)) / (2 * h)).real  # sin p ~ p
    return a0, a1

if __name__ == "__main__":
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    m = float(sys.argv[2]) if len(sys.argv) > 2 else 0.1; lam = float(sys.argv[3]) if len(sys.argv) > 3 else 0.2
    u = 16 * np.pi ** 2
    sys.path.insert(0, __file__.rsplit("/", 1)[0])
    from f2_qed_speeds import fermion_coeffs
    r = fermion_coeffs(L, m, lam)
    print(f"semi-analytic Feynman L={L}: a0*16pi^2={u*r['a0']:+.5f} a1*16pi^2={u*r['a1']:+.5f} dc_f*16pi^2={u*r['dcf']:+.5f}")
    for xi in (1.0, 0.0, 3.0):
        a0, a1 = coeffs(L, m, lam, xi)
        print(f"brute force xi={xi}: a0*16pi^2={u*a0:+.5f} a1*16pi^2={u*a1:+.5f} dc_f*16pi^2={u*(a1-a0):+.5f}", flush=True)
