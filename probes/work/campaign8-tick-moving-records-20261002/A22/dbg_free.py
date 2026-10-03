import numpy as np
from tb import Rel, bands, PI
M, m = 4096, 0.3
te, to = PI/2, PI/2 - m
R = Rel(M, te, to, 0.0, geom="ladder", V=None)
q = 2*PI*np.fft.fftfreq(M); k = (q + PI) % (2*PI) - PI
g = np.where(k > 0, np.exp(-0.03/np.maximum(k,1e-12) - (k/0.5)**2), 0.0)
EA, vA, uA = bands(q, te, to)[0]; EB, vB, uB = bands(-q, te, to)[0]
# check eigen-equation of bands
from tb import bloch
U = bloch(q, te, to)
res = np.abs(np.einsum('qij,qj->qi', U, uA) - np.exp(-1j*EA)[:,None]*uA).max()
print("band eigvec residual", res, " |u| range", np.linalg.norm(uA,axis=1).min(), np.linalg.norm(uA,axis=1).max())
chi = np.fft.ifft((g*np.exp(-1j*q*(-150)))[:,None,None]*uA[:,:,None]*uB[:,None,:], axis=0)*np.sqrt(M)
n0 = np.sum(np.abs(chi)**2); chi /= np.sqrt(n0)
for t in range(200):
    chi = R.tick(chi)
qq, W = R.project(chi)
w0 = W[0,0]
for kk in (0.05, 0.1, 0.2, 0.4):
    i = np.argmin(np.abs(k-kk))
    print(kk, w0[i], g[i]**2/n0, w0[i]/(g[i]**2/n0), "other bands", W[0,1,i]+W[1,0,i]+W[1,1,i])
print("sum W", W.sum(), "sum W00", W[0,0].sum())
