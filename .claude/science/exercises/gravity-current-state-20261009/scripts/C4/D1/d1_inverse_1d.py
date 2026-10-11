"""D1 check 3 (1D): the inverse problem and the smoothness of soft emission.

(i) Inverse problem.  For a target dressed band E = SLAC and a given gapless
    mediator (omega, w), the Dyson equation fixes the bare band uniquely:
        eps0 = E - Sigma_os[E].
    Lemma K predicts eps0 has a face kink of size 2 s (1+K) = 2 s / Z, i.e. its
    hopping tail is t_r ~ (-1)^r s(1+K)/(pi r^2): 1/Z times SLAC's own tail.
    So eps0 is never a trigonometric polynomial (never nearest-neighbour).
(ii) Soft emission is smooth in k at a smooth band: for an analytic subsonic
    band E (here 2 - cos k), Sigma_os[E](k) has exponentially decaying Fourier
    coefficients, also at marginal coupling (n=1): the soft-emission threshold
    is a singularity in the energy variable, not in k.
"""
import numpy as np
from scipy.integrate import quad

c, g = 2.0, 1.0


def setup(N):
    k = -np.pi + 2*np.pi*np.arange(N)/N
    q = 2*np.pi*np.arange(N)/N
    q = (q + np.pi) % (2*np.pi) - np.pi
    om = 2*c*np.abs(np.sin(q/2))
    return k, q, om


def wv(q, om, n):
    w = np.zeros_like(q)
    nz = q != 0
    w[nz] = g**2*(2*np.abs(np.sin(q[nz]/2)))**(2*n)/(2*om[nz])
    return w


def sigma_os(E, w, om):
    N = len(E)
    S = np.zeros(N)
    for l in range(1, N):
        S += w[l]/(E - np.roll(E, l) - om[l])
    return S/N


print("=== (i) inverse problem, n=2, target E = SLAC (m=beta=1) ===")
for N in (2048, 8192):
    k, q, om = setup(N)
    w = wv(q, om, 2)
    E = np.sqrt(1 + k**2)
    s = np.pi/np.sqrt(1+np.pi**2)
    eps0 = E - sigma_os(E, w, om)
    # K at the face (j=0): D = E[0] - E[-l] - om[l]
    idx = (-np.arange(1, N)) % N
    Kf = np.sum(w[1:]/(E[0] - E[idx] - om[1:])**2)/N
    tE = np.fft.fft(E)/N
    t0 = np.fft.fft(eps0)/N
    print(f"N={N}: K_face={Kf:.6f}  1+K={1+Kf:.6f}  (Z={1/(1+Kf):.6f})")
    print("   r    r^2(-1)^r t_r[SLAC]   r^2(-1)^r t_r[eps0]   ratio     prediction s/pi, s(1+K)/pi")
    for r in (8, 16, 32, 64, 128):
        a = (r**2*(-1)**r*tE[r]).real
        b = (r**2*(-1)**r*t0[r]).real
        print(f"  {r:4d}   {a:.6f}               {b:.6f}             {b/a:.5f}    {s/np.pi:.6f}, {s*(1+Kf)/np.pi:.6f}")

print("\n=== (ii) Sigma_os of an analytic subsonic band E = 2 - cos k is analytic in k ===")
Nk = 128
kk = -np.pi + 2*np.pi*np.arange(Nk)/Nk
Ean = lambda k: 2 - np.cos(k)
for n in (1, 2):
    vals = []
    for k0 in kk:
        f = lambda qq: (g**2*(2*abs(np.sin(qq/2)))**(2*n)/(2*2*c*abs(np.sin(qq/2))))/(Ean(k0) - Ean(k0-qq) - 2*c*abs(np.sin(qq/2))) if qq != 0 else 0.0
        v, _ = quad(f, -np.pi, np.pi, points=[0.0], limit=1000, epsabs=1e-15, epsrel=1e-14)
        vals.append(v/(2*np.pi))
    co = np.abs(np.fft.rfft(np.array(vals)))/Nk
    print(f"  n={n}: |Fourier coeff| r=1,3,5,9,13,17,25,33 (even r vanish by symmetry of this E): " + ", ".join(f"{co[r]:.2e}" for r in (1, 3, 5, 9, 13, 17, 25, 33)))
print("  (compare: a face kink would give a 1/r^2 tail, ~1e-3 at r=16)")
