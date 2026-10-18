"""F5-T1: dissipative Wilson walker on Z^3 (quasi-free Lindblad), pre-registered in PREREG_T1.md.

Single-particle density matrix rho(k) (2x2) obeys
    d rho/dt = -i[h, rho] - 1/2 {M + N, rho} + N,
M = sum_loss v v^dag (loss symbols), N = sum_gain g g^dag (gain symbols),
h_eff = h - (i/2)(M + N).  h(k) = sum_j sin k_j sigma_j (the framework walker comparator).

Measures: W3[h_eff - E_ref] (point-gap winding), doubler damping, steady-state mixedness,
steady-state jump rate per site r, sea error near the light node, parity relation.
Small: < 50 MB.  Run with OMP_NUM_THREADS=2.
"""
import numpy as np

rng_master = np.random.default_rng(20261014)
s0 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
SIG = [sx, sy, sz]
OFFS = np.array([(a, b, c) for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1)])


def grid(N, shift=0.0):
    k1 = 2 * np.pi * (np.arange(N) + shift) / N
    K = np.stack(np.meshgrid(k1, k1, k1, indexing="ij"), axis=-1)  # (N,N,N,3)
    return K


def h_walker(K):
    out = np.zeros(K.shape[:-1] + (2, 2), dtype=complex)
    for j in range(3):
        out += np.sin(K[..., j])[..., None, None] * SIG[j]
    return out


def ffun(K):
    return (1 - np.cos(K)).sum(-1)


def random_symbols(n_ops, scale, rng):
    """Random range-1 trig-polynomial 2-vectors: coefficient arrays (n_ops, 27, 2)."""
    return scale * (rng.normal(size=(n_ops, 27, 2)) + 1j * rng.normal(size=(n_ops, 27, 2))) / np.sqrt(54)


def eval_symbols(C, K, m):
    """v_mu(k) = f(k)^m * sum_r c_{mu,r} e^{i k.r}; returns (..., n_ops, 2)."""
    ph = np.exp(1j * np.tensordot(K, OFFS.T, axes=([-1], [0])))  # (..., 27)
    v = np.einsum("...r,orc->...oc", ph, C)
    return v * (ffun(K) ** m)[..., None, None]


def gram(v):
    return np.einsum("...oc,...od->...cd", v, v.conj())


def W3(A, N):
    """Winding of A: T^3 -> GL(2,C) on an N^3 periodic grid, spectral derivatives (A is a trig poly)."""
    kf = np.fft.fftfreq(N, d=1.0 / N)  # integer frequencies
    Ainv = np.linalg.inv(A)
    B = []
    for ax in range(3):
        F = np.fft.fft(A, axis=ax)
        shape = [1, 1, 1, 1, 1]
        shape[ax] = N
        dA = np.fft.ifft(F * (1j * kf).reshape(shape), axis=ax)
        B.append(Ainv @ dA)
    comm = B[1] @ B[2] - B[2] @ B[1]
    integrand = 3 * np.trace(B[0] @ comm, axis1=-2, axis2=-1)
    return (integrand.sum() * (2 * np.pi / N) ** 3 / (24 * np.pi ** 2))


def steady_state(H, Mtot, Ngain):
    """Solve -i(Heff rho - rho Heff^dag) + N = 0 per k (batched, column-stacked vec)."""
    Heff = H - 0.5j * Mtot
    I2 = np.eye(2)
    # build explicitly: vec(A X B) = (B^T kron A) vec X, column stacking
    sh = H.shape[:-2]
    K1 = np.zeros(sh + (4, 4), dtype=complex)
    K2 = np.zeros(sh + (4, 4), dtype=complex)
    # (I kron Heff): block diag
    K1[..., 0:2, 0:2] = Heff
    K1[..., 2:4, 2:4] = Heff
    # (Heff^* kron I)
    Hc = Heff.conj()
    for a in range(2):
        for b in range(2):
            K2[..., 2 * a:2 * a + 2, 2 * b:2 * b + 2] = Hc[..., a, b][..., None, None] * I2
    L = -1j * K1 + 1j * K2
    rhs = -np.stack([Ngain[..., 0, 0], Ngain[..., 1, 0], Ngain[..., 0, 1], Ngain[..., 1, 1]], -1)
    x = np.linalg.solve(L, rhs[..., None])[..., 0]
    rho = np.stack([np.stack([x[..., 0], x[..., 2]], -1), np.stack([x[..., 1], x[..., 3]], -1)], -2)
    return 0.5 * (rho + np.conj(np.swapaxes(rho, -1, -2)))


def mixedness(rho):
    lam = np.linalg.eigvalsh(rho)
    return (lam * (1 - lam)).sum(-1), lam


def jump_rate(rho, Mloss, Ngain):
    t1 = np.trace(Mloss @ rho, axis1=-2, axis2=-1).real
    t2 = np.trace(Ngain @ (np.eye(2) - rho), axis1=-2, axis2=-1).real
    return (t1 + t2).mean()


def fib_sphere(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], -1)


def sea_test(Mfun, Nfun, qs, ndir=200):
    """Occupations of the walker's bands near k = 0 in the steady state."""
    D = fib_sphere(ndir)
    out = []
    for q in qs:
        Kp = q * D
        Km = -q * D
        res = {}
        for tag, KK in (("p", Kp), ("m", Km)):
            H = h_walker(KK)
            Ml, Ng = Mfun(KK), Nfun(KK)
            rho = steady_state(H, Ml + Ng, Ng)
            d = np.sin(KK)
            dh = d / np.linalg.norm(d, axis=-1, keepdims=True)
            Pp = 0.5 * (np.eye(2) + np.einsum("nj,jab->nab", dh, np.array(SIG)))
            Pm = np.eye(2) - Pp
            res[tag] = (np.trace(Pp @ rho, axis1=-2, axis2=-1).real, np.trace(Pm @ rho, axis1=-2, axis2=-1).real)
        npl, nmi = res["p"]
        npl_m, nmi_m = res["m"]
        e_sea = np.mean(npl + 1 - nmi)
        parity_dev = np.max(np.abs(npl - nmi_m))  # n_+(qhat) vs n_-(-qhat)
        out.append((q, e_sea, parity_dev, npl.min(), npl.max(), nmi.min(), nmi.max()))
    return out


def main():
    N = 40
    K = grid(N)            # includes k = 0 (for W3; A invertible there because E_ref != 0)
    Ks = grid(24, 0.5)     # shifted grid avoiding k = 0 (for steady states)
    H, Hs = h_walker(K), h_walker(Ks)
    f, fs = ffun(K), ffun(Ks)
    print("=== 0. W3 normalisation check: A = sin k . sigma + i (m - sum cos k) ===")
    for mm in (2.0, 4.0):
        A = H + 1j * (mm - np.cos(K).sum(-1))[..., None, None] * s0
        print(f"  m={mm}: W3 = {W3(A, N).real:+.6f}   (expect +-1 for 1<m<3, 0 for m>3)")

    print("=== 1. Scalar dissipative Wilson walker: Gamma = kappa f^p ===")
    kappa = 1.0
    for p in (1, 2, 4):
        G = kappa * f ** p
        Heff = H - 0.5j * G[..., None, None] * s0
        for gref_frac in (0.25, 1.0):
            Eref = -0.5j * kappa * gref_frac  # between node damping 0 and doubler damping >= kappa 2^p
            A = Heff - Eref * s0
            mins = np.linalg.svd(A, compute_uv=False).min()
            print(f"  p={p} E_ref=-i*{0.5*kappa*gref_frac:.3f}: W3 = {W3(A, N).real:+.6f}  (min sing. value {mins:.3e})")
        corners = [(a, b, c) for a in (0, np.pi) for b in (0, np.pi) for c in (0, np.pi)]
        dmp = [kappa * ffun(np.array(cn)) ** p for cn in corners]
        print(f"   damping rate at the 8 corners: {sorted(np.round(dmp, 3))}")
    A = H - (-0.5j) * s0  # Hermitian control
    print(f"  Hermitian control (Gamma = 0, E_ref = -0.5i): W3 = {W3(A, N).real:+.6f}")

    print("=== 2. Scalar families: steady state, mixedness, jump rate, sea error ===")
    for p in (1, 2):
        for gainfrac in (0.0, 0.5, 0.9):
            Gs = kappa * fs ** p
            Ml = (1 - gainfrac) * Gs[..., None, None] * s0
            Ng = gainfrac * Gs[..., None, None] * s0
            rho = steady_state(Hs, Ml + Ng, Ng)
            mx, lam = mixedness(rho)
            r = jump_rate(rho, Ml, Ng)
            Mf = lambda KK, p=p, gf=gainfrac: (1 - gf) * kappa * (ffun(KK) ** p)[..., None, None] * s0
            Nf = lambda KK, p=p, gf=gainfrac: gf * kappa * (ffun(KK) ** p)[..., None, None] * s0
            st = sea_test(Mf, Nf, (0.3, 0.1, 0.03))
            print(f"  p={p} gain fraction={gainfrac}: <mixedness>={mx.mean():.4f}, r={r:.4f} jumps/site/time, "
                  f"e_sea(q=.3,.1,.03)={[round(s[1],4) for s in st]}")

    print("=== 3. Random local jump families (3 loss + 2 gain, range-1 symbols x f^m) ===")
    summary = []
    for m in (1, 2):
        for seed in range(6):
            rng = np.random.default_rng(1000 * m + seed)
            CL = random_symbols(3, 1.0, rng)
            CG = random_symbols(2, 1.0, rng)
            Mfun = lambda KK, CL=CL, m=m: gram(eval_symbols(CL, KK, m))
            Nfun = lambda KK, CG=CG, m=m: gram(eval_symbols(CG, KK, m))
            Ml, Ng = Mfun(K), Nfun(K)
            Heff = H - 0.5j * (Ml + Ng)
            # doubler damping: smallest decay rate (-2 Im lambda) at the 7 doubler corners
            corners = np.array([(a, b, c) for a in (0, np.pi) for b in (0, np.pi) for c in (0, np.pi)])[1:]
            Mc, Nc = Mfun(corners), Nfun(corners)
            Hc = h_walker(corners) - 0.5j * (Mc + Nc)
            dec = -2 * np.linalg.eigvals(Hc).imag
            dmin_corner = dec.min()
            # point-gap reference: half of the smallest corner decay rate
            w = []
            for frac in (0.25, 0.5):
                Eref = -0.5j * frac * dmin_corner
                A = Heff - Eref * s0
                mins = np.linalg.svd(A, compute_uv=False).min()
                w.append((W3(A, N).real, mins))
            # steady state on the shifted grid
            Mls, Ngs = Mfun(Ks), Nfun(Ks)
            Hes = Hs - 0.5j * (Mls + Ngs)
            dec_all = -2 * np.linalg.eigvals(Hes).imag
            rho = steady_state(Hs, Mls + Ngs, Ngs)
            mx, lam = mixedness(rho)
            r = jump_rate(rho, Mls, Ngs)
            st = sea_test(Mfun, Nfun, (0.3, 0.1, 0.03) if m == 1 else (0.5, 0.3, 0.1))
            summary.append((m, seed, w, dmin_corner, dec_all.min(), mx.mean(), mx.min(), r, st))
            print(f"  m={m} seed={seed}: W3={w[0][0]:+.4f}/{w[1][0]:+.4f} (minsv {min(w[0][1], w[1][1]):.2e}); "
                  f"min corner decay={dmin_corner:.3f}; min decay on shifted grid={dec_all.min():.2e}; "
                  f"<mix>={mx.mean():.4f} (min {mx.min():.2e}); r={r:.4e}")
            for s in st:
                print(f"      q={s[0]:.2f}: e_sea={s[1]:.4f}, max|n+(q)-n-(-q)|={s[2]:.4f}, "
                      f"n+ in [{s[3]:.3f},{s[4]:.3f}], n- in [{s[5]:.3f},{s[6]:.3f}]")

    print("=== 4. Control: gapped trivial insulator with an on-site dark state ===")
    Hc = (2.0 + np.cos(Ks).sum(-1))[..., None, None] * sz
    vl = np.zeros(Ks.shape[:-1] + (1, 2), dtype=complex); vl[..., 0, 0] = 1.0  # spin-up loss
    vg = np.zeros(Ks.shape[:-1] + (1, 2), dtype=complex); vg[..., 0, 1] = 1.0  # spin-down gain
    Ml, Ng = gram(vl), gram(vg)
    rho = steady_state(Hc, Ml + Ng, Ng)
    mx, lam = mixedness(rho)
    print(f"  <mixedness>={mx.mean():.2e}, r={jump_rate(rho, Ml, Ng):.2e}  (expect 0, 0)")

    print("=== 5. Loss-only transient from the filled Dirac sea: records written per site ===")
    # loss-only scalar Gamma = kappa f^p: each mode decays at rate Gamma(k); jumps per site by time t
    # = fraction of the (one-per-site) sea removed = mean_k [1 - exp(-Gamma(k) t)]  (lower band filled at t=0)
    Kfine = grid(64, 0.5)
    ff = ffun(Kfine)
    for p in (1, 2, 4):
        for t in (1e1, 1e3, 1e6, 8e60):
            n_rec = np.mean(1 - np.exp(-kappa * ff ** p * t))
            print(f"  p={p} t={t:.0e} (lattice units): records written per site = {n_rec:.6f}")
    # relaxed-shell scale q* where kappa (q^2/2)^p t_age = 1, t_age = 8e60 Planck times
    t_age, MPl = 8.0e60, 1.22e19
    for p in (1, 2, 4, 8, 16, 31):
        qs = np.sqrt(2.0) * (1.0 / (kappa * t_age)) ** (1.0 / (2 * p))
        print(f"  p={p}: q* a = {qs:.3e}  ->  q* = {qs*MPl:.3e} GeV  (modes above q* have relaxed)")


if __name__ == "__main__":
    main()
