"""D1 check 5 (1D): lane RC B2's remaining corner -- a band that TOUCHES a gapped
continuum exactly at the face (B2 showed exact SLAC needs such contact).

Band: exact SLAC E = sqrt(1 + k^2) (m = beta = 1), max E_f at the face k = pi.
Mediator: gapped, omega(q) = Om + A (1 + cos q), minimum Om at q = pi, tuned to
Om = E_f - m, so the one-boson threshold min_q[E(k-q) + omega(q)] equals E_f
exactly at the face (via k - q = 0, q = pi) and lies above the band elsewhere.
Vertex w_b(q) = g^2 (1 + cos q)^b, vanishing like (q - pi)^(2b) at the
touching configuration (b = 1 nearest-neighbour; b = 2 range two).
Lemma K: if K = int w/D0^2 < inf (here b >= 2), the on-shell self-energy carries
the V-kink Sigma'(0+) = s K (opposite to E's), so SLAC is not self-consistent.
If K = inf (b = 1): Z -> 0 at the face and Sigma_os ~ +C sqrt(delta) (wrong form).
"""
import numpy as np
from scipy.integrate import quad

m, beta, A, g = 1.0, 1.0, 1.0, 1.0
Ef = np.sqrt(m**2 + beta*np.pi**2)
s = beta*np.pi/Ef
Om = Ef - m


def red(k):
    return (k + np.pi) % (2*np.pi) - np.pi


def E(k):
    return np.sqrt(m**2 + beta*red(k)**2)


def om(q):
    return Om + A*(1 + np.cos(q))


def D(k, q):
    return E(k) - E(k - q) - om(q)


kk = np.linspace(-np.pi, np.pi, 1201)
qq = np.linspace(-np.pi, np.pi, 2401)
print(f"E_f={Ef:.6f} s={s:.6f} Om=E_f-m={Om:.6f}")
print(f"stability: max_(k,q) D = {max(np.max(D(k, qq)) for k in kk):.3e} (0 only at k=pi, q=pi)")
for k0 in (np.pi - 0.1, np.pi - 0.01):
    print(f"  gap to threshold at k=pi-{np.pi-k0:.2f}: {-max(D(k0, qq)):.4e}")


def sig(k, b):
    kink = float(red(k - np.pi))
    pts = sorted(set([kink, 0.0] + [x for x in (np.pi - (np.pi - red(k))/2, -np.pi + (np.pi + red(k))/2) if -np.pi < x < np.pi]))
    f = lambda q: g**2*(1 + np.cos(q))**b/D(k, q)
    v, _ = quad(f, -np.pi, np.pi, points=pts, limit=4000, epsabs=1e-15, epsrel=1e-13)
    return v/(2*np.pi)


def Kface(b, cut=0.0):
    f = lambda q: g**2*(1 + np.cos(q))**b/D(np.pi, q)**2
    v, _ = quad(f, -np.pi + cut, np.pi - cut, points=[0.0], limit=4000, epsabs=1e-15, epsrel=1e-12)
    return v/(2*np.pi)


for b in (2, 3):
    K = Kface(b)
    S0 = sig(np.pi, b)
    print(f"\nb={b}: K_face={K:.8f} Z={1/(1+K):.6f}; predicted Sigma'(0+) = sK = {s*K:.8f}")
    for dl in (1e-2, 1e-3, 1e-4, 1e-5):
        sl = (sig(np.pi - dl, b) - S0)/dl
        print(f"   delta={dl:.0e}: slope = {sl:.8f}   slope/(sK) = {sl/(s*K):.6f}")

b = 1
print("\nb=1 (nearest-neighbour vertex): K_face with |q|<pi-cut grows like 1/cut  ->  Z = 0 at the face")
for cut in (1e-1, 1e-2, 1e-3):
    print(f"   cut={cut:.0e}: K={Kface(1, cut):.4f}")
S0 = sig(np.pi, 1)
print("   Sigma_os(pi-delta) - Sigma_os(pi)  vs  sqrt(delta):")
for dl in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
    dS = sig(np.pi - dl, 1) - S0
    print(f"   delta={dl:.0e}: dS = {dS:+.6e}   dS/sqrt(delta) = {dS/np.sqrt(dl):+.5f}")
