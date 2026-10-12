"""D1 check 4 (2D): the face-kink relation in d = 2.

Exact SLAC band E = sqrt(m^2 + beta |k|^2) on the lifted square, periodic;
gapless boson omega(q) = c sqrt(4 sin^2(qx/2) + 4 sin^2(qy/2)); nearest-neighbour
gradient vertex w = g^2 (4 sin^2(qx/2) + 4 sin^2(qy/2)) / (2 omega)  ~ |q|  (a = 1/2,
d + 2a = 3 > 2, so Z > 0).  On-shell rainbow self-energy with the dressed band:
   Sigma_os(k) = int d^2q/(2pi)^2  w / (E(k) - E(k-q) - omega(q)).
At the face point k = (pi - delta, ky0), Lemma K predicts the one-sided normal
slope  dSigma/ddelta(0+) = + s K,  s = beta pi / E_f(ky0),  K = int w / D0^2 = 1/Z - 1,
i.e. the self-energy carries a V-kink 2 s K opposite to the band's Lambda-kink 2 s.
Corrections are O(delta log delta) (soft piece |delta|^(d+2a-1) = delta^2 log).
Midpoint grid, N x N.
"""
import numpy as np

m, beta, c, g = 1.0, 1.0, 2.0, 1.0
ky0 = 0.7


def red(x):
    return (x + np.pi) % (2*np.pi) - np.pi


def E(kx, ky):
    return np.sqrt(m**2 + beta*(red(kx)**2 + red(ky)**2))


rng = np.random.default_rng(1)
K1 = rng.uniform(-np.pi, np.pi, (200000, 2))
Q1 = rng.uniform(-np.pi, np.pi, (200000, 2))
om1 = c*np.sqrt(4*np.sin(Q1[:, 0]/2)**2 + 4*np.sin(Q1[:, 1]/2)**2)
Dm = E(K1[:, 0], K1[:, 1]) - E(K1[:, 0]-Q1[:, 0], K1[:, 1]-Q1[:, 1]) - om1
print(f"stability sample: max D over 2e5 random (k,q) = {Dm.max():.3e} (<0 needed)")

Ef = np.sqrt(m**2 + beta*(np.pi**2 + ky0**2))
s = beta*np.pi/Ef
print(f"face point (pi, {ky0}): E_f={Ef:.6f}, s = beta*pi/E_f = {s:.6f}")

for N in (1024, 2048):
    h = 2*np.pi/N
    qv = -np.pi + (np.arange(N) + 0.5)*h
    QX, QY = np.meshgrid(qv, qv, indexing='ij')
    S2 = 4*np.sin(QX/2)**2 + 4*np.sin(QY/2)**2
    om = c*np.sqrt(S2)
    w = g**2*S2/(2*om)
    Ekq0 = E(np.pi - QX, ky0 - QY)
    D0 = Ef - Ekq0 - om
    K = np.sum(w/D0**2)/N**2
    S0 = np.sum(w/D0)/N**2
    print(f"\nN={N} (h={h:.2e}): K_face={K:.6f} (Z={1/(1+K):.5f})  predicted slope sK = {s*K:.6f}")
    print("   delta      slope=[S(d)-S(0)]/d    slope/(sK)    even-check")
    for j in (2, 4, 8, 16, 32, 64):
        dl = j*h
        Ek = E(np.pi - dl, ky0)
        Dp = Ek - E(np.pi - dl - QX, ky0 - QY) - om
        Sp = np.sum(w/Dp)/N**2
        Ekm = E(np.pi + dl, ky0)
        Dmn = Ekm - E(np.pi + dl - QX, ky0 - QY) - om
        Sm = np.sum(w/Dmn)/N**2
        sl = (Sp - S0)/dl
        print(f"   {dl:.4f}    {sl:.6f}              {sl/(s*K):.5f}       {Sm-Sp:+.1e}")
