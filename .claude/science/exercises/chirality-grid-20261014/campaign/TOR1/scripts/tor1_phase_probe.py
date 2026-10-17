"""TOR-1 descriptive: the chiral measure's phase over the kernel nodes of single entries (level (2,8)): spread, pieces
(toron S-phase, measure-term kbb phase, transported-det phase), and |sum w rho| / sum w |rho|.  usage: python3 tor1_phase_probe.py"""
import numpy as np, time
from tor1_geom import *
S = Torus(4, 4); z = np.load('pool_TOR1_srch_Lt4_k6_s3201.npz'); U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]
M = TorusMeasure(S, '11112', Ns=4, sk=-1, ntor=96, nloop=1024); M.ntor1 = 24; M.use_spline(); t0 = time.time()
for (a, b) in ((0, 0), (0, 3), (2, 5)):
    A, w = entry_fields(S, U[a], U[b], 2, 8); Ws = []; Sp = []; Kp = []; ww = []
    for c in range(0, len(A), 128):
        W, r = M.logrho(A[c:c+128], parts=True); Ws.append(W); Sp.append(r['Sph'].imag); Kp.append(-np.sum(r['AT'] * r['kbb'], 1)); ww.append(r['w'])
    W = np.concatenate(Ws); Sp = np.concatenate(Sp); Kp = np.concatenate(Kp); wv = np.concatenate(ww)
    ph = np.angle(np.exp(1j * (W.imag - W.imag[np.argmax(W.real)])))
    rho = np.exp(W - W.real.max()); wt = w * np.abs(rho)
    print(f"entry ({a},{b}): phase spread over nodes {np.ptp(ph):.3e} rad (weighted rms {np.sqrt(np.sum(wt*ph**2)/wt.sum()):.2e}); S-phase range [{Sp.min():+.2e},{Sp.max():+.2e}]; "
          f"kbb-phase range [{Kp.min():+.2e},{Kp.max():+.2e}]; w_x range [{wv[:,0].min():+.3f},{wv[:,0].max():+.3f}], w_t range [{wv[:,1].min():+.3f},{wv[:,1].max():+.3f}]; "
          f"|sum w rho|/sum w|rho| = {abs(np.sum(w*rho))/np.sum(wt):.10f}; arg sum w rho {np.angle(np.sum(w*rho)):+.2e} [{time.time()-t0:.0f}s]", flush=True)
