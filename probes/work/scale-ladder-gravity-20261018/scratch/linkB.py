"""B: law-level odds as a Gaussian field with nearest-neighbour conditions on Z^3 (precision -Delta + m^2).
Distance from correlation decay; isotropy; and how far conditioning one site (a record) changes distances."""
import numpy as np
L = 96
k = 2*np.pi*np.fft.fftfreq(L); KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
ph = 4*(np.sin(KX/2)**2 + np.sin(KY/2)**2 + np.sin(KZ/2)**2)
def corr(m):
    return np.real(np.fft.ifftn(1.0/(ph + m*m)))
def C_at(Cr, v): return Cr[v[0] % L, v[1] % L, v[2] % L]
for m in (1.0, 0.3, 0.1):
    Cr = corr(m)
    # B1: long-range decay rate per unit length along axis / face / body (log-derivative between r1 and r2)
    rates = {}
    for nm, d in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1)}.items():
        d = np.array(d); n1, n2 = int(round(12/np.linalg.norm(d))), int(round(24/np.linalg.norm(d)))
        r1, r2 = n1*np.linalg.norm(d), n2*np.linalg.norm(d)
        c1, c2 = C_at(Cr, n1*d), C_at(Cr, n2*d)
        rates[nm] = (np.log(c1*r1) - np.log(c2*r2))/(r2 - r1)       # remove the 1/r prefactor
    print(f"m={m}: correlation decay rate (inverse correlation length) axis {rates['axis']:.4f}, face {rates['face']:.4f}, body {rates['body']:.4f}; anisotropy (axis/body - 1) {rates['axis']/rates['body']-1:+.4f}")
    # B2: a record at the origin (condition the field there); nearest-neighbour pair (x, x+e_x) at distance r along y
    C0 = C_at(Cr, (0, 0, 0)); out = []
    for r in (2, 4, 8, 12, 16):
        x, y = np.array([0, r, 0]), np.array([1, r, 0])
        cxy = C_at(Cr, y - x); cxs, cys = C_at(Cr, x), C_at(Cr, y)
        cxy_c = cxy - cxs*cys/C0
        cxx_c = C0 - cxs**2/C0; cyy_c = C0 - cys**2/C0
        rho0 = cxy/C0; rho1 = cxy_c/np.sqrt(cxx_c*cyy_c)
        out.append((r, -np.log(rho1) + np.log(rho0)))              # change in the correlation distance (log-correlation units)
    print(f"      record at origin: change of the NN pair's correlation distance at r = " + ", ".join(f"{r}: {v:.2e}" for r, v in out)
          + f";  falloff ratio r=8->16: {out[2][1]/out[4][1]:.1f}")
