"""R17-4 validation of offaxis.py:
 (1) axis rows equal R16-3's zz.xi_all (NN at m=1 vs R9-9's table; G(1.0), Z1 at m=0.3);
 (2) direct 3D-grid check of the off-axis closed form, independent of the IBP: alpha = d/ds^2 Pi(0, s n) by
     Richardson on Pi(0,q) = -1/4 <W(k)/(e+ e- (e+ + e-))>, e+- = eps(k +- q/2); beta = -(1/32)<W/eps^5>;
 (3) the O_h relation body = (8 face1 + 4 face2 - 3 Eg)/9 on computed values."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import ZLaw, xi_all, Mix
from laws import G, Z1
from offaxis import xi_off, POLS, relation
T0 = time.time()
class NN:
    def __init__(self, nf=1 << 18):
        self.k = np.linspace(0, np.pi, nf+1); self.sig = 2*np.sin(self.k/2); self.sp = np.cos(self.k/2); self.name = 'NN'
if __name__ == "__main__":
    nn = NN()
    for law, m in [(nn, 1.0), (G(1.0), 0.3), (Z1(), 0.3)]:
        g, f = (law.samples(1 << 14) if hasattr(law, 'samples') else (None, None))
        if g is None:
            kk = 2*np.pi*(np.arange(1 << 14)+0.5)/(1 << 14) - np.pi; g = 4*np.sin(kk/2)**2; f = 2*np.sin(kk/2)*np.cos(kk/2)
        ref = xi_all(g, f, m, nu=1500)
        for vtx in ['M', 'U']:
            X, _ = xi_off(law, m, vtx)
            print('%-14s m=%.1f %s: axis Eg %+.9e (zz %+.9e)  T2g %+.9e (zz %+.9e) | face1 %+.6e face2 %+.6e body %+.6e | O_h relation resid %.1e'
                  % (law.name, m, vtx, X['Eg'], ref[vtx+',Eg'], X['T2g'], ref[vtx+',T2g'], X['face1'], X['face2'], X['body'], relation(X)), flush=True)

    # (2) direct 3D grid, NN band (analytic), m = 1 and 0.5, E1 vertex
    def eps_nn(kx, ky, kz, m): return np.sqrt(m*m + 4*(np.sin(kx/2)**2 + np.sin(ky/2)**2 + np.sin(kz/2)**2))
    def V_nn(kx, ky, kz, e, vtx):
        s = [2*np.sin(kx/2), 2*np.sin(ky/2), 2*np.sin(kz/2)]
        if vtx == 'U': s = [x*np.cos(k/2) for x, k in zip(s, [kx, ky, kz])]
        return sum(e[i, j]*s[i]*s[j] for i in range(3) for j in range(3))
    def direct(m, name, vtx, N=96, hs=(0.08, 0.04, 0.02)):
        n, e = POLS[name]; n = np.array(n, float)
        k1 = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
        KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
        W = V_nn(KX, KY, KZ, e, vtx)**2; ep = eps_nn(KX, KY, KZ, m)
        P0 = -0.25*np.mean(W/(2*ep**3))
        a = []
        for h in hs:
            q = h*n; e1 = eps_nn(KX+q[0]/2, KY+q[1]/2, KZ+q[2]/2, m); e2 = eps_nn(KX-q[0]/2, KY-q[1]/2, KZ-q[2]/2, m)
            a.append((-0.25*np.mean(W/(e1*e2*(e1+e2))) - P0)/h**2)
        a = np.array(a); r1 = (4*a[1:] - a[:-1])/3; alpha = (16*r1[1] - r1[0])/15
        beta = -np.mean(W/ep**5)/32
        return alpha + beta
    for m in [1.0, 0.5]:
        for vtx in ['M', 'U']:
            X, _ = xi_off(nn, m, vtx)
            for name in ['Eg', 'T2g', 'face1', 'face2', 'body']:
                d96 = direct(m, name, vtx, N=96); d64 = direct(m, name, vtx, N=64)
                print('direct NN m=%.1f %s %-5s: grid N=64 %+.9e N=96 %+.9e | closed form %+.9e | rel diff %.1e' % (m, vtx, name, d64, d96, X[name], abs(d96-X[name])/abs(X[name])), flush=True)
    print('runtime %.1fs' % (time.time()-T0))
