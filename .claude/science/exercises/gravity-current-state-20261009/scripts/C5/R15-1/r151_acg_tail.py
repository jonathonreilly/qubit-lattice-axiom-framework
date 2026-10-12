"""R15-1 (a): does coupling a cuscuton to an ordinary field transmit influence outside the light cone?
System: Afshordi-Chung-Geshnizjani hep-th/0609150 eq. (53)-(56) (flat space, 1+1 D here):
  dphi_k = -V_pp_psi/(k^2+V_phph) dpsi_k  (constraint),  psi'' = -(k^2 + V_psps) psi - V_phps dphi.
  => omega_k^2 = [k^4 + (Vphph+Vpsps)k^2 + Vphph Vpsps - Vphps^2]/(k^2+Vphph)  (their eq. 56; stable for the chosen V).
Source: initial velocity psi_t(0,x) = s(x), a C-infinity bump supported in |x| < w; psi(0,x) = 0.
Exact per-mode solution psi_k(t) = s_k sin(omega_k t)/omega_k; inverse FFT.
Control: Vphps = 0 (Klein-Gordon, retarded support inside |x| <= t + w).
Observable: max |psi(t,x)| for |x| > t + w + 0.25 (outside the source's future light cone).
Prediction (proved below in the report): the instantaneous term gives psi_tt(t,x) = Vphps^2 [G_Y * psi](x) outside the cone,
so the leak scales as Vphps^2 and decays like exp(-sqrt(Vphph)(|x| - t - w)).
"""
import numpy as np
L, Nx = 400.0, 2**16
x = (np.arange(Nx) - Nx//2)*(L/Nx)
k = 2*np.pi*np.fft.fftfreq(Nx, d=L/Nx)
w = 1.0
s = np.where(np.abs(x) < w, np.exp(-1.0/np.clip(1 - (x/w)**2, 1e-300, None)), 0.0)
sk = np.fft.fft(np.fft.ifftshift(s))
def evolve(t, Vpp, Vss, Vps):
    om2 = (k**4 + (Vpp + Vss)*k**2 + Vpp*Vss - Vps**2)/(k**2 + Vpp)
    om = np.sqrt(om2)
    psik = sk*np.sin(om*t)/om
    return np.fft.fftshift(np.real(np.fft.ifft(psik)))
for t in [2.0, 5.0, 10.0]:
    out = np.abs(x) > t + w + 0.25
    ctrl = evolve(t, 1.0, 1.0, 0.0)
    print(f"t = {t}: control (Vphps=0) max|psi| outside cone = {np.max(np.abs(ctrl[out])):.2e};  inside max = {np.max(np.abs(ctrl)):.2e}")
    for Vps in [0.1, 0.3, 0.5, 0.9]:
        p = evolve(t, 1.0, 1.0, Vps)
        leak = np.max(np.abs(p[out]))
        xr = t + w + 2.0; i = np.argmin(np.abs(x - xr))
        print(f"   Vphps = {Vps}: max|psi| outside cone = {leak:.3e}  (ratio to Vphps^2 = {leak/Vps**2:.3e});  psi at x = t+w+2: {p[i]:+.3e}, at t+w+6: {p[np.argmin(np.abs(x-(t+w+6)))]:+.3e}")
