"""D1 check 2 (1D): self-consistent dressed bands  E = eps0 + Sigma_os[E].

Rainbow / SCBA-pole self-energy with the dressed band as intermediate state,
gapless boson omega(q) = 2c|sin(q/2)|, nearest-neighbour vertex of order n
(w ~ |q|^(2n-1)).  Grid k_j = -pi + 2 pi j/N (j = 0 is the face).

Cases
 (a) n=2 (Z>0), bare band WITH a face kink (non-local SLAC bare band,
     eps0 = sqrt(m0^2 + b0 k^2)): Lemma K predicts the dressed face slope
     s_E = Z * s_0 with Z = 1/(1+K[E]).  Dressing shrinks a kink; never makes one.
 (b) n=2, nearest-neighbour bare band eps0 = A - B cos k, iteration STARTED from
     the exact SLAC band: the kink must decay to zero at rate
     |1 - alpha(1+K)| per step (alpha = mixing) and the fixed point is smooth.
 (c) n=1 (marginal, Z=0), kinked bare band: the face slope is driven to zero
     like s_0/(1 + C' log(1/h)) as the grid spacing h -> 0 (kink erased).
"""
import numpy as np

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


def Kface(E, w, om):
    N = len(E)
    tot = 0.0
    for l in range(1, N):
        D = E[0] - E[(0 - l) % N] - om[l]
        tot += w[l]/D**2
    return tot/N


def stab(E, om):
    N = len(E)
    mx = -1e9
    for l in range(1, N):
        mx = max(mx, np.max(E - np.roll(E, l) - om[l]))
    return mx


def face_slope(E, k, M=6):
    """fit E(face + u) = E_f - s|u| + c2 u^2 + c3 |u|^3 on the interior side j=1..M"""
    h = k[1]-k[0]
    u = h*np.arange(1, M+1)
    y = E[1:M+1] - E[0]
    A = np.vstack([-u, u**2, u**3]).T
    sol = np.linalg.lstsq(A, y, rcond=None)[0]
    # other side check
    y2 = E[-1:-M-1:-1] - E[0]
    sol2 = np.linalg.lstsq(A, y2, rcond=None)[0]
    return sol[0], sol2[0]


def solve(eps0, Einit, w, om, alpha=0.5, tol=1e-12, itmax=400, track=False):
    E = Einit.copy()
    hist = []
    for it in range(itmax):
        Enew = eps0 + sigma_os(E, w, om)
        dE = np.max(np.abs(Enew - E))
        E = (1-alpha)*E + alpha*Enew
        if track:
            hist.append(E.copy())
        if dE < tol:
            break
    return E, it, dE, hist


print("=== (a) n=2, kinked (SLAC) bare band: dressed slope vs Z*s0 ===")
for N in (1024, 2048, 4096):
    k, q, om = setup(N)
    w = wv(q, om, 2)
    m0, b0 = 1.0, 1.0
    kr = k
    eps0 = np.sqrt(m0**2 + b0*kr**2)
    s0 = b0*np.pi/np.sqrt(m0**2 + b0*np.pi**2)
    E, it, dE, _ = solve(eps0, eps0, w, om)
    K = Kface(E, w, om)
    sE, sE2 = face_slope(E, k)
    Z = 1/(1+K)
    print(f"N={N}: iters={it} resid={dE:.1e}  stab max D={stab(E, om):.2e}  K_face={K:.6f} Z={Z:.6f}")
    print(f"       s0={s0:.6f}  dressed slope (two sides) = {sE:.6f}, {sE2:.6f}   Z*s0 = {Z*s0:.6f}   ratio sE/(Z s0) = {sE/(Z*s0):.5f}")

print("\n=== (b) n=2, nearest-neighbour bare band eps0 = A - B cos k, iteration started from exact SLAC ===")
N = 2048
k, q, om = setup(N)
w = wv(q, om, 2)
A_, B_ = 2.0, 1.0
eps0 = A_ - B_*np.cos(k)
Einit = np.sqrt(1 + k**2)
alpha = 0.5
E, it, dE, hist = solve(eps0, Einit, w, om, alpha=alpha, track=True, itmax=60, tol=1e-13)
Kf = Kface(E, w, om)
print(f"converged iters={it} resid={dE:.1e}; K_face(fixed point)={Kf:.6f}; predicted kink ratio per step 1-alpha(1+K) = {1-alpha*(1+Kf):+.5f}")
prev = None
for t in [0, 1, 2, 3, 5, 8, 12, 20, 30]:
    if t < len(hist):
        sl, _ = face_slope(hist[t], k)
        r = f"   ratio to previous listed: {(sl/prev[1])**(1/(t-prev[0])):+.5f}/step" if prev and abs(prev[1]) > 1e-14 else ""
        print(f"  iter {t:3d}: face slope s = {sl:+.3e}{r}")
        prev = (t, sl)
slF, _ = face_slope(E, k)
# smoothness of the fixed point: Fourier coefficients of E decay exponentially (no 1/r^2 kink tail)
co = np.fft.rfft(E)/N
print(f"  fixed point face slope = {slF:+.2e};  |Fourier coeff| r=1,5,10,20,40: " +
      ", ".join(f"{abs(co[r]):.2e}" for r in (1, 5, 10, 20, 40)))

print("\n=== (c) n=1 marginal (Z=0), kinked bare band: face slope vs grid spacing ===")
for N in (512, 1024, 2048, 4096, 8192):
    k, q, om = setup(N)
    w = wv(q, om, 1)
    eps0 = np.sqrt(1 + k**2)
    s0 = np.pi/np.sqrt(1 + np.pi**2)
    E, it, dE, _ = solve(eps0, eps0, w, om, alpha=0.5, tol=1e-11)
    sE, _ = face_slope(E, k)
    h = 2*np.pi/N
    # leading-log estimate: s_E (1 + Cp log(1/h)) ~ s0 with Cp = g^2/(2 pi c (c - s_E)^2)
    Cp = g**2/(2*np.pi*c*(c-sE)**2)
    print(f"N={N:5d} h={h:.2e}: iters={it}  dressed face slope = {sE:.5f}   s0/slope = {s0/sE:.4f}   1+C'log(1/h) = {1+Cp*np.log(1/h):.4f}")
