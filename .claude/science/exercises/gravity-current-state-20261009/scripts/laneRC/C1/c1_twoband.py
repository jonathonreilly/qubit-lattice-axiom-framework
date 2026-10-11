"""Two-band network with the zone-face kink built in exactly.
h(k) = D0(k) 1 + Re d sigma_x + Im d sigma_y,  d(k) = (1 + e^{ik}) a(k),  lower band E = D0 - |d| = D0 - 2|cos(k/2)| |a|.
The simple zero of d at k = pi gives an exact Lambda-kink. Choose |a| = alpha with alpha = alpha_loc near the face, where
alpha_loc(delta) = -G_odd(delta)/(2 sin(delta/2)),  G_odd(x) = [Gh(x)-Gh(-x)]/2,  Gh(x) = sqrt(m^2 + c^2 (pi-x)^2),  delta = k - pi,
so that D0 = G + 2|cos(k/2)| alpha is C-infinity (alpha glued to a constant away from the face by a C-infinity window).
Then truncate D0 and alpha^2 to Fourier degree n (range-n hopping; a from alpha^2 by Fejer-Riesz) and measure
sup|E_n - G| and the closure residual sup|E_n E_n' - c^2 saw(k)| over the WHOLE zone. Compare: 1-band E^2 (1.76/n, residual >= pi).
"""
import numpy as np
m, c = 1.0, 1.0
N = 2**14
k = 2*np.pi*np.arange(N)/N - np.pi           # [-pi, pi)
saw = k.copy()
G = np.sqrt(m**2 + c**2*k**2)
delta = np.where(k >= 0, k - np.pi, k + np.pi)  # distance to the face, in (-pi, pi]
def Gh(x): return np.sqrt(m**2 + c**2*(np.pi - x)**2)
def alpha_loc(dl):
    s = np.sin(dl/2); out = np.empty_like(dl)
    small = np.abs(dl) < 1e-6
    out[~small] = -(Gh(dl[~small]) - Gh(-dl[~small]))/2/(2*s[~small])
    # limit: -Gh'(0) ... G_odd(x) ~ Gh'(0) x, sin(x/2) ~ x/2  -> alpha = -Gh'(0)/1
    out[small] = c**2*np.pi/np.sqrt(m**2 + c**2*np.pi**2)
    return out
def smoothstep(x):  # C-infinity 0->1 on [0,1]
    f = lambda t: np.where(t > 0, np.exp(-1/np.maximum(t, 1e-300)), 0.0)
    return f(x)/(f(x) + f(1-x))
r0, r1 = 1.0, 2.6
w = 1 - smoothstep((np.abs(delta) - r0)/(r1 - r0))
aL = alpha_loc(delta)
alpha = w*aL + (1-w)*aL[np.argmin(np.abs(np.abs(delta) - r0))]
D0 = G + 2*np.abs(np.cos(k/2))*alpha
A2 = alpha**2
def trunc(f, n):
    F = np.fft.fft(f); fr = np.fft.fftfreq(N, 1/N)
    F[np.abs(fr) > n] = 0
    return np.fft.ifft(F).real
def deriv(f):
    F = np.fft.fft(f); fr = np.fft.fftfreq(N, 1/N)
    return np.fft.ifft(1j*fr*F).real
out = []
P = lambda s: (print(s), out.append(s))
P(f"m={m}, c={c}; D0 smoothness check: Fourier tail |F_j| at j=200,400: "
  f"{np.abs(np.fft.fft(D0))[200]/N:.2e}, {np.abs(np.fft.fft(D0))[400]/N:.2e}")
P("n    sup|E_n-G| zone   sup|E E' - c^2 saw| zone (|delta|>2pi/N)   min alpha_n^2   [1-band E^2 best: 1.76/n, residual >= pi]")
mask = np.abs(delta) > 4*np.pi/N
for n in [8, 16, 32, 64, 96, 128, 192, 256]:
    D0n = trunc(D0, n); A2n = trunc(A2, n)
    En = D0n - 2*np.abs(np.cos(k/2))*np.sqrt(np.maximum(A2n, 0))
    # derivative of E_n: smooth parts by spectral derivative, kink factor analytically
    dD0 = deriv(D0n); aN = np.sqrt(np.maximum(A2n, 1e-300)); daN = deriv(A2n)/(2*aN)
    cosf = np.abs(np.cos(k/2)); dcosf = -0.5*np.sin(k/2)*np.sign(np.cos(k/2))
    dE = dD0 - 2*(dcosf*aN + cosf*daN)
    res = np.abs(En*dE - c**2*saw)[mask].max()
    P(f"{n:4d}  {np.abs(En-G).max():.3e}   {res:.3e}   {A2n.min():.3e}")
open('c1_twoband.out','w').write('\n'.join(out)+'\n')
