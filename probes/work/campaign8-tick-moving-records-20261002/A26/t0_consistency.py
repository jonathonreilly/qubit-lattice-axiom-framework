import os, signal
for _v in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS"): os.environ[_v]="1"
signal.alarm(58)
import numpy as np
from rs2d import Walk2D, bloch_batch, from_cells, packet, centroid
from walk2d import cycle
Lx, Ly = 16, 12
rng = np.random.default_rng(1)
cases = [dict(), dict(mu=0.07), dict(delta=0.03, mode='os'), dict(delta=0.03, mode='st', N=0.93, hxx=0.04),
         dict(beta=0.11), dict(imx=0.05, imy=-0.03), dict(mu=0.05, beta=-0.2, imx=0.02, imy=0.02, N=0.9, hxx=0.06, hyy=-0.02)]
worst = 0
for kw in cases:
    th0 = 0.37
    N = kw.get('N', 1.0); hxx = kw.get('hxx', 0.0); hyy = kw.get('hyy', 0.0)
    W = Walk2D(Lx, Ly, th0, N=N*np.ones((Lx,Ly)), hxx=hxx*np.ones((Lx,Ly)), hyy=hyy*np.ones((Lx,Ly)), mu=kw.get('mu',0.0),
               delta=kw.get('delta',0.0), mode=kw.get('mode','os'), rule='field',
               beta=None if 'beta' not in kw else kw['beta']*np.ones((Lx,Ly)), imx=kw.get('imx',0.0), imy=kw.get('imy',0.0))
    for trial in range(3):
        nx, ny = rng.integers(0, Lx//2), rng.integers(0, Ly//2)
        K = np.array([[2*np.pi*nx/(Lx//2), 2*np.pi*ny/(Ly//2)]])
        U = bloch_batch(K, th0, mu=kw.get('mu',0.0), delta=kw.get('delta',0.0), beta=kw.get('beta',0.0),
                        imx=kw.get('imx',0.0), imy=kw.get('imy',0.0), fx=1-hxx/2, fy=1-hyy/2, N=N, mode=kw.get('mode','os'))[0]
        w, V = np.linalg.eig(U)
        for k in range(4):
            cells = np.exp(1j*(K[0,0]*np.arange(Lx//2)[:,None] + K[0,1]*np.arange(Ly//2)[None,:]))[:,:,None]*V[:,k][None,None,:]
            psi = from_cells(cells)
            out = W.step(psi.copy())
            worst = max(worst, np.abs(out - w[k]*psi).max())
    # also compare to walk2d.cycle when it has the same parametrisation (N folded into angles)
print("max |step(psi) - lambda psi| over cases, K, bands: %.2e" % worst)
U1 = bloch_batch(np.array([[0.3, -1.1]]), 0.37, mu=0.05, beta=0.13, imx=0.02, imy=0.03)[0]
U2 = cycle(np.array([0.3,-1.1]), th=0.37, mu=0.05, beta=0.13, imx=0.02, imy=0.03)
print("bloch_batch vs walk2d.cycle: %.2e" % np.abs(U1-U2).max())
psi = packet(128, 96, (20, 24), (0.5, 0.0), 6.0, 0.4)
W = Walk2D(128, 96, 0.4)
xs=[]
for t in range(121):
    if t % 20 == 0: xs.append(centroid(psi))
    psi = W.step(psi)
xs = np.array(xs)
print("flat packet q0=(0.5,0): centroid x (sites) every 20 cycles:", np.round(xs[:,0],2), " y:", np.round(xs[:,1],3), " norm-1 %.1e" % (xs[-1,2]-1))
