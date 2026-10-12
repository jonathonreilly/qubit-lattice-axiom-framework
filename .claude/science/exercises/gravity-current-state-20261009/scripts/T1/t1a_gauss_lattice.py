r"""T1 part (a): one-loop speed split on fixed Z^3, continuous time, Gaussian proper-distance kernel
(R2 Route 3 form, scripts/R2_c1_kernel_tt_modulus.py 'gauss', at g = identity).

  w(n)   = 2/((2pi)^{3/2} s^5) exp(-|n|^2/(2 s^2)),  n in Z^3 \ {0}
  K(q)   = sum_n w(n) (1 - cos q.n)                   (= q^2 + O(q^4))
  scalar : w2(q) = m^2 + K(q)                          (exactly R2's kernel)
  fermion: S_b(q) = 1/2 d_b K = 1/2 sum_n w(n) n_b sin(q.n)   (= q_b + O(q^3); same weights)
           M(q)   = (r s/2) K(q)                       (Wilson term from the same kernel; r=1 default)
  IR regulator: equal masses m; fermion mass is TWISTED (-i g5 m), so E^2 = S^2 + M^2 + m^2 (no 2mM cross term).
Tree speeds: both exactly 1 at q -> 0.  IR masses m for both species, then m -> 0.
Also: nearest-neighbour Hamiltonian control (Z^3, continuous time):
  S_b = sin q_b,  M = r sum_b (1 - cos q_b) (+ twisted m),  w2 = m^2 + sum_b 4 sin^2(q_b/2).
Usage: python t1a_gauss_lattice.py L s m [r [f]]   (f: variant a2, Collins-form Gaussian propagator weight, width s)   or   python t1a_gauss_lattice.py L nn m [r]
"""
import sys, time
import numpy as np
from t1_loop import coeffs


def arrays_gauss(L, s, m, r):
    n1 = np.fft.fftfreq(L, d=1.0 / L)
    q1 = 2 * np.pi * np.fft.fftfreq(L)
    N = np.meshgrid(n1, n1, n1, indexing="ij")
    r2 = N[0] ** 2 + N[1] ** 2 + N[2] ** 2
    w = 2.0 / ((2 * np.pi) ** 1.5 * s ** 5) * np.exp(-r2 / (2 * s * s))
    w[0, 0, 0] = 0.0
    del r2
    W0 = w.sum()
    ft = lambda a: np.fft.fftn(a)
    K = W0 - ft(w).real
    # S_b = 1/2 sum w n_b sin = -1/2 Im fft(w n_b)
    S = np.stack([-0.5 * ft(w * N[b]).imag for b in range(3)])
    # d_x S_b = 1/2 sum w n_x n_b cos = 1/2 Re fft(w n_x n_b)
    dS = np.stack([0.5 * ft(w * N[0] * N[b]).real for b in range(3)])
    # d_x^2 S_b = -1/2 sum w n_x^2 n_b sin = 1/2 Im fft(w n_x^2 n_b)
    d2S = np.stack([0.5 * ft(w * N[0] ** 2 * N[b]).imag for b in range(3)])
    del N, w
    M = 0.5 * r * s * K          # IR mass enters as twisted mass mt (see t1_loop.coeffs)
    dM = r * s * S[0]          # (r s/2) d_x K = r s S_x
    d2M = r * s * dS[0]        # (r s/2) d_x^2 K = r s d_x S_x
    one = np.ones_like(K); zero = np.zeros_like(K)
    F = dict(S=S, M=M, dS=dS, d2S=d2S, dM=dM, d2M=d2M, fF=one, dfF=zero, d2fF=zero)
    B = dict(w2=m * m + K, dw2=2 * S[0], fB=one, dfB=zero)
    Q = np.meshgrid(q1, q1, q1, indexing="ij")
    qn = np.sqrt(Q[0] ** 2 + Q[1] ** 2 + Q[2] ** 2)
    return F, B, qn, K


def add_collins_factor(F, B, L, sf):
    """Variant (a2): multiply both free propagators by f(q) = sum_n v(|n|) e^{i q.n},
    v = (2 pi sf^2)^{-3/2} exp(-|n|^2/(2 sf^2)) normalised so f(0) = 1 (Gaussian proper-distance kernel).
    The dispersion (w2, S, M) is unchanged, so R2's vacuum-energy/stiffness check is unchanged."""
    n1 = np.fft.fftfreq(L, d=1.0 / L)
    N = np.meshgrid(n1, n1, n1, indexing="ij")
    v = np.exp(-(N[0] ** 2 + N[1] ** 2 + N[2] ** 2) / (2 * sf * sf)); v /= v.sum()
    f = np.fft.fftn(v).real
    df = np.fft.fftn(v * N[0]).imag          # -sum v n_x sin
    d2f = -np.fft.fftn(v * N[0] ** 2).real   # -sum v n_x^2 cos
    F.update(fF=f, dfF=df, d2fF=d2f); B.update(fB=f, dfB=df)
    return f


def arrays_nn(L, m, r):
    q1 = 2 * np.pi * np.fft.fftfreq(L)
    Q = np.meshgrid(q1, q1, q1, indexing="ij")
    S = np.stack([np.sin(Q[b]) for b in range(3)])
    dS = np.stack([np.cos(Q[0]), np.zeros_like(Q[0]), np.zeros_like(Q[0])])
    d2S = np.stack([-np.sin(Q[0]), np.zeros_like(Q[0]), np.zeros_like(Q[0])])
    M = r * sum(1 - np.cos(Q[b]) for b in range(3))
    dM = r * np.sin(Q[0]); d2M = r * np.cos(Q[0])
    K = sum(4 * np.sin(Q[b] / 2) ** 2 for b in range(3))
    one = np.ones_like(K); zero = np.zeros_like(K)
    F = dict(S=S, M=M, dS=dS, d2S=d2S, dM=dM, d2M=d2M, fF=one, dfF=zero, d2fF=zero)
    B = dict(w2=m * m + K, dw2=2 * np.sin(Q[0]), fB=one, dfB=zero)
    qn = np.sqrt(Q[0] ** 2 + Q[1] ** 2 + Q[2] ** 2)
    return F, B, qn, K


if __name__ == "__main__":
    L = int(sys.argv[1]); kind = sys.argv[2]; m = float(sys.argv[3])
    r = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
    t0 = time.time()
    if kind == "nn":
        F, B, qn, K = arrays_nn(L, m, r); s = 1.0
    else:
        s = float(kind); F, B, qn, K = arrays_gauss(L, s, m, r)
        if len(sys.argv) > 5 and sys.argv[5] == "f":
            fmin = add_collins_factor(F, B, L, s).min(); kind = kind + "+f"
    o = coeffs(np.full(qn.shape, 1.0 / L ** 3), F, B, h=min(1e-3, 0.02 * m), mt=m)
    k = 16 * np.pi ** 2
    # region split: inner ball |q| < 2.5/s (where the kernel disperses) vs outer zone (flat band)
    inner = qn < 2.5 / s
    ip, iph = o["_ipsi"], o["_iphi"]
    print(f"{kind:>4s} L={L} m={m:.4g} r={r:g} | 16pi^2: A={k*o['A']:.4f} B={k*o['B']:.4f} a={k*o['a']:.4f} b={k*o['b']:.4f} | "
          f"dc_psi={k*o['dc_psi']:+.5f} dc_phi={k*o['dc_phi']:+.5f} Delta={o['Delta']:+.5f} | "
          f"inner/outer Delta: {k*(ip[inner].sum()-iph[inner].sum()):+.4f} / {k*(ip[~inner].sum()-iph[~inner].sum()):+.4f} "
          f"| Kmax={K.max():.4f} [{time.time()-t0:.0f}s]", flush=True)
