"""V2 (b3'): scale of the O(lambda^3) cloud-scattering matrix element <T_4|V22|T_4> per cell (m = 1).
T = -(1/24) sum_x int dt (A+_{x,t})^4,  A+_{x,t} = N^-1/2 sum_k alpha e^{-t w} e^{-ikx} a+_k   (Kato/V1 dressing)
V22 = (6/24) sum_y (A+_{y,0})^2 (A_{y,0})^2.   Contractions <A_{x,s} A+_{y,t}> = G_{s+t}(x-y),
G_tau(r) = N^-1 sum_k e^{-tau w}/(2w) e^{ikr}.
  <T+ V22 T>/N = (6/24)(1/24^2) * 12 * 24 * int ds dt sum_w G_{s+t}(w)^2 (G_t^2 * G_s^2)(w)
  <T+ T>/N     = (1/24^2) * 24  * int ds dt sum_w G_{s+t}(w)^4
  <T+ H2 T>/N  = E2 of V1 (= sum E_n |S_n0|^2 = 6.9007e-6 at m=1)  [cross-check of normalisation via
                 <T+ T> with the energy weight: replace one Laplace pair by 1/(sum w)^2 * sum w]
This sets the natural size of the O(lambda^3) vacuum term that a split NOT referenced to Omega_h leaves:
  mu^(3) ~ 2 lambda^3 <T_4| X2 |T_4>, with X2 the O(eps^2) part of the split difference, an O(1)-weighted V22 on the
  (lattice-scale) cloud.  Labelled SUGGESTED: X2's weight is not computed here.
"""
import numpy as np, sys
m = 1.0
u, wu = np.polynomial.laguerre.laggauss(40)
beta = 3.0
tn, wn = u/beta, wu*np.exp(u)/beta   # int_0^inf dt F(t) ~ sum wn F(tn)
for L in [12, 16, 20]:
    k1 = 2*np.pi*np.fft.fftfreq(L); KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
    w = np.sqrt(m**2 + 4*np.sin(KX/2)**2 + 4*np.sin(KY/2)**2 + 4*np.sin(KZ/2)**2)
    N = L**3
    def G(tau): return np.fft.ifftn(np.exp(-tau*w)/(2*w)).real   # = N^-1 sum_k ... e^{ikr}
    Gs = [G(t) for t in tn]
    Gs2k = [np.fft.fftn(g**2) for g in Gs]
    I22 = 0.0; I0 = 0.0
    for i, s in enumerate(tn):
        for j, t in enumerate(tn):
            Gst = G(s + t)
            conv = np.fft.ifftn(Gs2k[i]*Gs2k[j]).real          # (G_s^2 * G_t^2)(w)
            I22 += wn[i]*wn[j]*np.sum(Gst**2*conv)
            I0 += wn[i]*wn[j]*np.sum(Gst**4)
    n22 = (6/24)*(1/24**2)*12*24*I22
    nTT = (1/24**2)*24*I0
    print(f'L={L}: <T+T>/cell = {nTT:.5e} | <T+ V22 T>/cell = {n22:+.5e} | ratio (typical 22 element on cloud) = {n22/nTT:+.4f}')
    sys.stdout.flush()
print('compare: V1 E2 = sum E_n|S_n0|^2 = 6.9007e-6 (lambda^2 units); O(lambda^2) Hessian pieces 1.42e-5 (E), 7.7e-7 (T2)')
