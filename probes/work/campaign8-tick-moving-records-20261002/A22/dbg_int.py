import numpy as np
from tb import Rel, bands, PI
M, m = 8192, 0.3
te, to = PI/2, PI/2 - m
R = Rel(M, te, to, 0.0, geom="ladder", V=[(0,"all",0.8)])
q = 2*PI*np.fft.fftfreq(M); k = (q + PI) % (2*PI) - PI
g = np.where(k > 0, np.exp(-0.03/np.maximum(k,1e-12) - (k/0.2)**2), 0.0)
EA, vA, uA = bands(q, te, to)[0]; EB, vB, uB = bands(-q, te, to)[0]
chi = np.fft.ifft((g*np.exp(-1j*q*(-150)))[:,None,None]*uA[:,:,None]*uB[:,None,:], axis=0)*np.sqrt(M)
n0 = np.sum(np.abs(chi)**2); chi /= np.sqrt(n0)
for T in (1500, 3000):
    c = chi.copy()
    for t in range(T):
        c = R.tick(c)
    left = c.copy(); left[R.r > -60] = 0; right = c.copy(); right[R.r < 60] = 0
    _, WL = R.project(left); _, WR = R.project(right)
    half = M//2
    print("T", T, "mid", 1 - np.sum(np.abs(left)**2) - np.sum(np.abs(right)**2))
    for kk in (0.03, 0.05, 0.08, 0.1, 0.15, 0.2):
        i = np.argmin(np.abs(k-kk)); j = (-i) % M
        To, Td, Ro, Rd = WR[0,0,i], WR[1,1,(i+half)%M], WL[0,0,j], WL[1,1,(j+half)%M]
        s = To+Td+Ro+Rd
        print(f"  k={kk}: To {To/ (g[i]**2/n0):.4f} Td {Td/(g[i]**2/n0):.4f} Ro {Ro/(g[i]**2/n0):.4f} Rd {Rd/(g[i]**2/n0):.4f}  sum {s/(g[i]**2/n0):.4f}  vrel {abs(vA[i]-vB[i]):.3f}")
