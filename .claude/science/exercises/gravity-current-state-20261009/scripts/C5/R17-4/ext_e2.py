"""R17-4: extension dependence of the off-axis U rows. E2 (product) vertex V = sum e_ij [f(k1_i) f(k2_j) + f(k2_i) f(k1_j)]/2,
k1 = k + q/2, k2 = -(k - q/2) (pair created at total momentum q), against E1 (relative-momentum) V = e:f(k)f(k). Direct 3D grid,
Pi(0,q) Richardson in s and beta at q = 0 (the vertex at q = 0 is the same in E1 and E2 up to sign). NN band, m = 1 and 0.5."""
import numpy as np, sys; sys.path.insert(0, '.')
from offaxis import POLS
def eps(K, m): return np.sqrt(m*m + sum(4*np.sin(k/2)**2 for k in K))
def fU(k): return np.sin(k)
def run(m, name, ext, N=64, hs=(0.08, 0.04, 0.02)):
    n, e = POLS[name]; n = np.array(n, float)
    k1d = 2*np.pi*(np.arange(N)+0.5)/N - np.pi; K = np.meshgrid(k1d, k1d, k1d, indexing='ij')
    def V(q):
        if ext == 'E1': fa = [fU(k) for k in K]; return sum(e[i, j]*fa[i]*fa[j] for i in range(3) for j in range(3))
        ka = [K[i] + q[i]/2 for i in range(3)]; kb = [-(K[i] - q[i]/2) for i in range(3)]
        A = [fU(k) for k in ka]; B = [fU(k) for k in kb]
        return -sum(e[i, j]*(A[i]*B[j] + B[i]*A[j])/2 for i in range(3) for j in range(3))
    ep = eps(K, m); W0 = V(np.zeros(3))**2; P0 = -0.25*np.mean(W0/(2*ep**3))
    a = []
    for h in hs:
        q = h*n; e1 = eps([K[i] + q[i]/2 for i in range(3)], m); e2 = eps([K[i] - q[i]/2 for i in range(3)], m)
        a.append((-0.25*np.mean(V(q)**2/(e1*e2*(e1+e2))) - P0)/h**2)
    a = np.array(a); r1 = (4*a[1:] - a[:-1])/3; alpha = (16*r1[1] - r1[0])/15
    return alpha - np.mean(W0/ep**5)/32
for m in [1.0, 0.5]:
    for name in ['Eg', 'T2g', 'face1', 'face2', 'body']:
        x1 = run(m, name, 'E1'); x2 = run(m, name, 'E2')
        print('NN m=%.1f U %-5s: E1 %+.6e  E2 %+.6e  (E2-E1 %+.2e)' % (m, name, x1, x2, x2-x1), flush=True)
