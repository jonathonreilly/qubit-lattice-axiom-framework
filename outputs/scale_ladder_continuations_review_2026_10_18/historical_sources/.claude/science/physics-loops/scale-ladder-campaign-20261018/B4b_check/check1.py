import sys, time, numpy as np
from indep_bubble import *
sys.path.insert(0, '../B4b_induced_graviton_ward')
import stag_kernel as SK
rng = np.random.default_rng(7)
P = rng.uniform(-np.pi, np.pi, (50, 4)); K = rng.uniform(-np.pi, np.pi, 4); m = 0.7
Dm = D(P, m)
print("DD^dag=Delta err", np.abs(Dm @ np.conj(np.swapaxes(Dm,1,2)) - Delta(P,m)[:,None,None]*np.eye(16)).max())
print("gauge Ward err", np.abs(np.einsum('m,mnab->nab', khat(K), Vel(P+K/2)) - (D(P+K,m)-D(P,m))).max())
print("matches B4b D(P) exactly:", np.abs(Dm - SK.Dmat(P, m)).max())
# bubble cross-check vs B4b code
K = np.array([0.31, 0.17, -0.22, 0.09]); N = 8
t=time.time(); Tm = bubble(K, N, m); print("my bubble time", time.time()-t)
Tb = SK.Pi_tensor_fast(K, N, m, 'D')
print("my bubble vs B4b bubble max diff", np.abs(Tm - Tb).max(), " scale", np.abs(Tm).max())
# exact telescoping to one-propagator (tadpole-type) loops, K on grid
N = 8; K = 2*np.pi/N*np.array([1, 2, 0, -1])
lhs = ward(bubble(K, N, m), K); rhs = tadpole_contact(K, N, m)
print("khat.Pi_bubble == one-propagator contact loops (on-grid K): err %.2e, |lhs| %.3e" % (np.abs(lhs-rhs).max(), np.abs(lhs).max()))
K = np.array([0.31, 0.17, -0.22, 0.09]); N = 12
lhs = ward(bubble(K, N, m), K); rhs = tadpole_contact(K, N, m)
print("same, off-grid K, N=12: err %.2e, |lhs| %.3e" % (np.abs(lhs-rhs).max(), np.abs(lhs).max()))
