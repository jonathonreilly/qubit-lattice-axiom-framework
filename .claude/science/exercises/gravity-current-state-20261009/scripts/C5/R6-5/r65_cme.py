"""R6-5 (a),(b): explicit law, its b0, its one-loop mixing, and the induced (k_AF)_0.

Law: Z^3 x R, one 4-component fermion per site, NN Peierls-coupled hopping (Wilson-Dirac) plus on-site b*gamma5.
  h(k) = sum_j alpha_j sin k_j + beta*(m + r*sum_j(1-cos k_j)) + b*gamma5        (a = t = e = 1)
Covariant under translations and the 24 proper cubic rotations (r65_symmetry.out); P-odd, T-even, C-even.

Computes
  A. low-energy check: the dispersion near k=0 is E = sqrt(m_eff^2 + (|p| +- b)^2) (SME b0 form); the doublers are gapped.
  B. one-loop (Hartree) mixing: chi5 = d<psi^+ gamma5 psi>/db per site for the filled Dirac sea.
  C. calibration of the Kubo code: anomalous Hall conductivity of the spatial-b (b.Sigma) Weyl semimetal
     against Delta_k/(4 pi^2).
  D. the CS coefficient k(omega, q) defined by j = 2k B, i.e. k = i(Pi^xy - Pi^yx)/(4q) for q || z,
     for the gapped b0 law: static limit (omega=0, q->0) and its omega dependence below the gap;
     compared with the 'anomaly' value b/(4 pi^2) (j = (e^2/2pi^2) b B).
"""
import sys
import numpy as np

s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
Z2 = np.zeros((2, 2))
beta = np.block([[s0, Z2], [Z2, -s0]]).astype(complex)
alpha = [np.block([[Z2, s], [s, Z2]]) for s in (sx, sy, sz)]
g5 = np.block([[Z2, s0], [s0, Z2]]).astype(complex)
SigZ = np.block([[sz, Z2], [Z2, sz]])


def grid(N):
    k = 2 * np.pi * np.arange(N) / N - np.pi
    K1, K2, K3 = np.meshgrid(k, k, k, indexing='ij')
    return K1, K2, K3


def ham(K, m, r, b, bz=0.0):
    K1, K2, K3 = K
    H = (np.sin(K1)[..., None, None] * alpha[0] + np.sin(K2)[..., None, None] * alpha[1] + np.sin(K3)[..., None, None] * alpha[2]
         + (m + r * (3 - np.cos(K1) - np.cos(K2) - np.cos(K3)))[..., None, None] * beta + b * g5 + bz * SigZ)
    vx = np.cos(K1)[..., None, None] * alpha[0] + (r * np.sin(K1))[..., None, None] * beta
    vy = np.cos(K2)[..., None, None] * alpha[1] + (r * np.sin(K2))[..., None, None] * beta
    return H, vx, vy


def kubo_anti(N, m, r, b, bz, mq, omegas, imag=False):
    """returns D(omega) = Pi^xy - Pi^yx at q = 2 pi mq/N zhat, T=0, Fermi level 0."""
    K = grid(N)
    H, vx, vy = ham(K, m, r, b, bz)
    E, U = np.linalg.eigh(H)
    Uq = np.roll(U, -mq, axis=2); Eq = np.roll(E, -mq, axis=2)   # states at k+q
    f = (E < 0).astype(float); fq = (Eq < 0).astype(float)
    Ud = np.conj(np.swapaxes(U, -1, -2)); Uqd = np.conj(np.swapaxes(Uq, -1, -2))
    Ax = Ud @ vx @ Uq; Ay = Ud @ vy @ Uq        # <n,k| v |m,k+q>
    By = Uqd @ vy @ U; Bx = Uqd @ vx @ U        # <m,k+q| v |n,k>
    df = f[..., :, None] - fq[..., None, :]
    dE = E[..., :, None] - Eq[..., None, :]
    num_xy = Ax * np.swapaxes(By, -1, -2)
    num_yx = Ay * np.swapaxes(Bx, -1, -2)
    out = []
    for w in omegas:
        ww = 1j * w if imag else w
        den = ww + dE
        mask = np.abs(df) > 0
        pxy = np.sum(np.where(mask, df * num_xy / np.where(mask, den, 1.0), 0.0)) / N ** 3
        pyx = np.sum(np.where(mask, df * num_yx / np.where(mask, den, 1.0), 0.0)) / N ** 3
        out.append(pxy - pyx)
    return np.array(out), E


m, r = 0.3, 1.0
print("=== A. low-energy content of the explicit law (m=%.2f, r=%.1f)" % (m, r))
for b in (0.0, 0.1, 0.2):
    ps = np.linspace(0.0, 0.4, 9)
    Es = []
    for p in ps:
        H, _, _ = ham((np.array(0.0), np.array(0.0), np.array(p)), m, r, b)
        Es.append(np.sort(np.linalg.eigvalsh(H))[2:])   # two positive branches
    Es = np.array(Es)
    # continuum SME form with lattice p -> sin p, mass m + r(1-cos p)
    pred = np.array([[np.sqrt((m + r * (1 - np.cos(p))) ** 2 + (np.sin(p) - b) ** 2), np.sqrt((m + r * (1 - np.cos(p))) ** 2 + (np.sin(p) + b) ** 2)] for p in ps])
    print("  b=%.2f  max|E_lattice - sqrt(M(p)^2+(sin p -+ b)^2)| = %.1e ; positive-branch minimum %.4f at p=%.3f"
          % (b, np.abs(np.sort(Es, axis=1) - np.sort(pred, axis=1)).max(), Es.min(), ps[np.argmin(Es.min(axis=1))]))
corners = [(0, 0, 0), (np.pi, 0, 0), (np.pi, np.pi, 0), (np.pi, np.pi, np.pi)]
print("  doubler gaps (min |E| at corners with 0,1,2,3 pi components, b=0.2):", ["%.2f" % np.abs(np.linalg.eigvalsh(ham(tuple(np.array(x) for x in C), m, r, 0.2)[0])).min() for C in corners])

print("=== B. one-loop (Hartree) mixing chi5 = d<psi^+ g5 psi>/db (per site, filled sea)")
for N in (24, 40):
    vals = []
    for b in (-0.01, 0.01):
        H, _, _ = ham(grid(N), m, r, b)
        E, U = np.linalg.eigh(H)
        occ = U[..., :, :2]
        n5 = np.real(np.einsum('...in,ij,...jn', occ.conj(), g5, occ).sum()) / N ** 3
        vals.append(n5)
    print("  N=%d  chi5 = %.5f  (lattice units a^-2 per unit b)" % (N, (vals[1] - vals[0]) / 0.02))

print("=== C. calibration: AHE of the spatial-b Weyl semimetal (m=0, r=1, b.Sigma_z = 0.2), imaginary frequency")
for N in (32, 48):
    bz = 0.2
    D, _ = kubo_anti(N, 0.0, 1.0, 0.0, bz, 0, [0.02, 0.01], imag=True)
    sig = D / (2j * 1j * np.array([0.02, 0.01]))
    dk = 4 * np.arcsin(bz / 2)
    print("  N=%d  sigma_xy(i eta=0.02,0.01) = %s ; |Delta_k|/(4 pi^2) = %.5f" % (N, np.round(sig.real, 5), dk / (4 * np.pi ** 2)))

print("=== D. CS coefficient k = i(Pi^xy - Pi^yx)/(4q), q || z, gapped b0 law (m=%.2f, r=%.1f)" % (m, r))
for b in (0.0, 0.1, 0.2):
    for N in (32, 48, 64):
        omegas = [0.0, 0.05, 0.1, 0.15, 0.2]
        rows = []
        for mq in (1, 2, 3):
            q = 2 * np.pi * mq / N
            D, E = kubo_anti(N, m, r, b, 0.0, mq, omegas)
            rows.append(1j * D / (4 * q))
        rows = np.array(rows).real   # (mq, omega)
        qs = 2 * np.pi * np.array([1, 2, 3]) / N
        # extrapolate q->0 with k(q) = k0 + k2 q^2 using the two smallest q
        k0 = (rows[0] * qs[1] ** 2 - rows[1] * qs[0] ** 2) / (qs[1] ** 2 - qs[0] ** 2)
        gap = np.abs(E).min()
        print("  b=%.2f N=%d gap=%.3f  k(q->0, omega) for omega=%s : %s ;  anomaly b/(4pi^2)=%.5f"
              % (b, N, gap, omegas, np.array2string(k0, precision=6), b / (4 * np.pi ** 2)))
        if N == 64 and b > 0:
            w = np.array(omegas)
            A = np.vstack([np.ones_like(w), w ** 2, w ** 4]).T
            c = np.linalg.lstsq(A, k0, rcond=None)[0]
            print("      fit k(omega) = %.2e + %.5f omega^2 + %.4f omega^4  (lattice units, e=1)" % tuple(c))
sys.stdout.flush()
