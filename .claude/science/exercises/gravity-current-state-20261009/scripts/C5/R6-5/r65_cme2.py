"""R6-5 (b) follow-up.
 1. static CS coefficient k(omega=0, q->0) with a three-point q-extrapolation, for two different P-odd terms:
      on-site b*gamma5, and P-odd hopping c5*gamma5*sum_j cos k_j (b_eff at k=0 is b + 3 c5);
 2. separation of the omega^2 and q^2 terms of k(omega, q) and the ON-SHELL (omega = |q|) coefficient,
      k(omega,q) ~ k_w omega^2 + k_q q^2 ;  on-shell d=5 birefringence coefficient = k_w + k_q.
      In a Lorentz-covariant continuum the odd form factor depends on p^2 = omega^2 - q^2 only, so k_q = -k_w and the
      on-shell term vanishes; on the lattice it survives as a lattice (Lorentz-violating) artefact. Scan m -> 0 at fixed b/m.
 3. tighter AHE calibration (N=64, eta=0.005).
"""
import numpy as np

s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
Z2 = np.zeros((2, 2))
beta = np.block([[s0, Z2], [Z2, -s0]]).astype(complex)
alpha = [np.block([[Z2, s], [s, Z2]]) for s in (sx, sy, sz)]
g5 = np.block([[Z2, s0], [s0, Z2]]).astype(complex)
SigZ = np.block([[sz, Z2], [Z2, sz]])


def grid(N):
    k = 2 * np.pi * np.arange(N) / N - np.pi
    return np.meshgrid(k, k, k, indexing='ij')


def ham(K, m, r, b, c5=0.0, bz=0.0):
    K1, K2, K3 = K
    H = (np.sin(K1)[..., None, None] * alpha[0] + np.sin(K2)[..., None, None] * alpha[1] + np.sin(K3)[..., None, None] * alpha[2]
         + (m + r * (3 - np.cos(K1) - np.cos(K2) - np.cos(K3)))[..., None, None] * beta
         + (b + c5 * (np.cos(K1) + np.cos(K2) + np.cos(K3)))[..., None, None] * g5 + bz * SigZ)
    vx = np.cos(K1)[..., None, None] * alpha[0] + (r * np.sin(K1))[..., None, None] * beta - (c5 * np.sin(K1))[..., None, None] * g5
    vy = np.cos(K2)[..., None, None] * alpha[1] + (r * np.sin(K2))[..., None, None] * beta - (c5 * np.sin(K2))[..., None, None] * g5
    return H, vx, vy


def kubo_anti(N, q, omegas, imag=False, **hp):
    """Pi^xy - Pi^yx at arbitrary q || z (states at k+q diagonalised separately; the integrand is smooth when gapped)."""
    K = grid(N)
    H, vx, vy = ham(K, **hp)
    Hq, _, _ = ham((K[0], K[1], K[2] + q), **hp)
    E, U = np.linalg.eigh(H)
    Eq, Uq = np.linalg.eigh(Hq)
    f = (E < 0).astype(float); fq = (Eq < 0).astype(float)
    Ud = np.conj(np.swapaxes(U, -1, -2)); Uqd = np.conj(np.swapaxes(Uq, -1, -2))
    num_xy = (Ud @ vx @ Uq) * np.swapaxes(Uqd @ vy @ U, -1, -2)
    num_yx = (Ud @ vy @ Uq) * np.swapaxes(Uqd @ vx @ U, -1, -2)
    df = f[..., :, None] - fq[..., None, :]
    dE = E[..., :, None] - Eq[..., None, :]
    mask = np.abs(df) > 0
    out = []
    for w in omegas:
        den = np.where(mask, (1j * w if imag else w) + dE, 1.0)
        out.append((np.sum(np.where(mask, df * num_xy / den, 0)) - np.sum(np.where(mask, df * num_yx / den, 0))) / N ** 3)
    return np.array(out), np.abs(E).min()


def kcs(N, q, omegas, **hp):
    D, gap = kubo_anti(N, q, omegas, **hp)
    return (1j * D / (4 * q)).real, gap


print("=== 1. static k(0, q->0), three-point extrapolation k0 + k2 q^2 + k4 q^4 (q = 0.02, 0.04, 0.06)")
for label, hp in [("on-site b=0.1", dict(m=0.3, r=1.0, b=0.1)),
                  ("P-odd hopping c5=0.1 (b=0)", dict(m=0.3, r=1.0, b=0.0, c5=0.1)),
                  ("both b=0.1, c5=-0.05", dict(m=0.3, r=1.0, b=0.1, c5=-0.05))]:
    for N in (32, 48):
        qs = np.array([0.02, 0.04, 0.06])
        ks = np.array([kcs(N, q, [0.0], **hp)[0][0] for q in qs])
        A = np.vstack([np.ones(3), qs ** 2, qs ** 4]).T
        c = np.linalg.solve(A, ks)
        beff = hp.get('b', 0) + 3 * hp.get('c5', 0)
        print("  %-28s N=%d  k_static(q->0) = %+.2e   (anomaly-value b_eff/4pi^2 = %.2e ; ratio %.1e)"
              % (label, N, c[0], beff / (4 * np.pi ** 2), c[0] / (beff / (4 * np.pi ** 2))))

print("=== 2. omega^2 vs q^2 terms and the on-shell coefficient (b/m = 1/3, r = 1); N=48, q,omega = x*m")
for m in (0.4, 0.3, 0.2, 0.15):
    b = m / 3
    N = 48
    x1, x2 = 0.1, 0.2
    q1, q2 = x1 * m, x2 * m
    st1 = kcs(N, q1, [0.0], m=m, r=1.0, b=b)[0][0]; st2 = kcs(N, q2, [0.0], m=m, r=1.0, b=b)[0][0]
    kq = (st2 - st1) / (q2 ** 2 - q1 ** 2)
    dyn = kcs(N, q1, [0.0, q2], m=m, r=1.0, b=b)[0]
    kw = (dyn[1] - dyn[0]) / q2 ** 2
    on1 = kcs(N, q1, [q1], m=m, r=1.0, b=b)[0][0] / q1 ** 2
    on2 = kcs(N, q2, [q2], m=m, r=1.0, b=b)[0][0] / q2 ** 2
    print("  m=%.2f b=%.3f : k_w=%+.5f  k_q=%+.5f  (k_w+k_q)/k_w=%+.4f ; on-shell k/q^2 at q=%.3f,%.3f: %+.3e, %+.3e ; k_w*m^2/b=%.4f"
          % (m, b, kw, kq, (kw + kq) / kw, q1, q2, on1, on2, kw * m ** 2 / b))

print("=== 3. AHE calibration, N=64, eta=0.005 (spatial b.Sigma_z=0.2, m=0)")
D, _ = kubo_anti(64, 0.0, [0.005], imag=True, m=0.0, r=1.0, b=0.0, bz=0.2)
print("  sigma_xy = %.5f ; Delta_k/(4pi^2) = %.5f" % ((D / (2j * 1j * 0.005)).real[0], 4 * np.arcsin(0.1) / (4 * np.pi ** 2)))
