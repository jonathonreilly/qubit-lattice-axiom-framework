"""t7b: pure-band wavepackets near K* (built in Bloch space, inverse FFT), centroid velocity vs direction."""
import numpy as np
from vcyc import layers_U, plain6, strang9
from t7_real import run   # real-space layer code (checked against Bloch in t7)

pi = np.pi
N = 32; L = 2 * N
m = np.arange(N); Kg = 2 * pi * m / N
KK = np.array(np.meshgrid(Kg, Kg, Kg, indexing="ij")).reshape(3, -1).T
Xc, Yc, Zc = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")

def packet_velocity(lay, signed, nhat, q0=0.45, sK=0.09, T=8, which="upper"):
    Ks = np.array([pi, pi, pi])
    U0 = layers_U(Ks[None], lay, signed)[0]
    ref = np.exp(1j * np.angle(np.linalg.eigvals(U0)[0]))
    U = layers_U(KK, lay, signed)
    w, v = np.linalg.eig(U)
    ph = np.angle(w * np.conj(ref))                       # (N^3, 8)
    K0 = Ks + q0 * nhat
    dK = ((KK - K0 + pi) % (2 * pi)) - pi
    g = np.exp(-(dK ** 2).sum(1) / (2 * sK ** 2))
    phi0 = np.ones(8) / np.sqrt(8)
    if which == "upper":
        sel = ph > 0            # upper cone (positive relative phase) near K*
    else:                       # top sheet only
        sel = ph >= ph.max(1, keepdims=True) - 1e-9
    coef = np.einsum("nij,ni->nj", np.conj(v), np.broadcast_to(phi0, (KK.shape[0], 8)))  # v^dagger phi0 (v not unitary -> use pinv below)
    vinv = np.linalg.inv(v)
    coef = np.einsum("nji,i->nj", vinv, phi0)
    coef = coef * sel
    phiK = np.einsum("nij,nj->ni", v, coef) * g[:, None]   # (N^3, 8)
    phiK = phiK.reshape(N, N, N, 8)
    psi = np.zeros((L, L, L), complex)
    for p in range(8):
        px, py, pz = p & 1, (p >> 1) & 1, (p >> 2) & 1
        psi[px::2, py::2, pz::2] = np.fft.ifftn(phiK[..., p]) * N ** 1.5
    psi /= np.linalg.norm(psi)
    def cent(psi):
        P = np.abs(psi) ** 2
        # unwrap around the initial centroid: use circular mean per axis
        out = []
        for C in (Xc, Yc, Zc):
            ang = 2 * pi * C / L
            out.append(np.angle((P * np.exp(1j * ang)).sum()) * L / (2 * pi))
        return np.array(out)
    r0 = cent(psi)
    psi_t = psi
    for t in range(T):
        psi_t = run(psi_t, lay, signed)
    d = cent(psi_t) - r0
    d = ((d + L / 2) % L) - L / 2
    return d / T

th = 0.6
for name, lay, signed, which in [("plain-6 top sheet", plain6(th), False, "top"),
                                 ("strang-9 signed upper cone", strang9(th), True, "upper")]:
    for nhat in [np.array([1., 0, 0]), np.array([1., 1, 0]) / np.sqrt(2), np.array([1., 1, 1]) / np.sqrt(3),
                 np.array([0.3, -0.5, 0.81]) / np.linalg.norm([0.3, -0.5, 0.81])]:
        v = packet_velocity(lay, signed, nhat, which=which)
        cosang = abs(v @ nhat) / np.linalg.norm(v)
        print(f"{name}: n={np.round(nhat, 3)} v={np.round(v, 3)} |v|={np.linalg.norm(v):.3f} "
              f"|cos(v,n)|={cosang:.4f}  (2 sin th={2*np.sin(th):.3f}, 2 sqrt3 sin th={2*np.sqrt(3)*np.sin(th):.3f})")
