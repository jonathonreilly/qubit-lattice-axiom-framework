"""R17-4 (c),(d): LV tadpole rho + p in the supplied zero-point vacuum (R11-3 Lemma Tad: rho = <eps>/2, p_U = <sum f^2/eps>/6,
p_M = <sum g/eps>/6) on the axis-zero laws; whole-zone v_max; raw tails |eps_r| of eps_1D = sqrt(0.09 + g) (nothing subtracted)."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import ZLaw, Mix
from floor_scan import Zz
T0 = time.time()
def tad(g, f, m, nu=3000):
    u = np.linspace(-30, np.log(80/min(m*m, 1)) + 2, nu); t = np.exp(u); du = u[1]-u[0]
    E0 = np.empty(nu); G1 = np.empty(nu); F2 = np.empty(nu)
    for i0 in range(0, nu, 200):
        W = np.exp(-np.outer(t[i0:i0+200], g)); E0[i0:i0+200] = W.mean(1); G1[i0:i0+200] = W @ g/len(g); F2[i0:i0+200] = W @ (f*f)/len(g)
    w = t*du*t**-0.5*np.exp(-t*m*m)/np.sqrt(np.pi)
    inv = np.sum(w*E0**3); gx = np.sum(w*G1*E0**2); fx = np.sum(w*F2*E0**2)
    rho = 0.5*(m*m*inv + 3*gx); pU = 3*fx/6; pM = 3*gx/6
    return rho, pU, pM
# NN control against R11-3's table (m = 1: rho 1.3000, p_U 0.0991, w_M 0.282)
kk = 2*np.pi*(np.arange(1 << 14)+0.5)/(1 << 14) - np.pi
rho, pU, pM = tad(4*np.sin(kk/2)**2, np.sin(kk), 1.0)
print('NN m=1 control: rho %.4f p_U %.4f w_U %.3f w_M %.3f (R11-3: 1.3000, 0.0991, 0.076, 0.282)' % (rho, pU, pU/rho, pM/rho))
NF = 1 << 19
A = ZLaw([1.0, 0.0], [1.0 + (np.pi-1.0)/2], np.pi-1.0, 'G(1.0)', nf=NF)
def ZzN(b, V, P, wt):
    L = Zz(b, V, P, wt); return ZLaw(L.vals, L.bks, wt, L.name, nf=NF)
C2 = ZzN(1.0, 0.35, 0.47, 0.03); C = ZzN(1.0, 0.35, 0.43, 0.03)
zeros = {'M zero m=0.1 (A,C2,C) (0.955978,0.024523)': (0.955977637884, 0.024523462318),
         'U zero m=0.1 (A,C2,C) (this run)': (0.964879, 0.007410)}
import re
try:
    txt = open('evalzeros.out').read(); mm = re.search(r'm=0.10 \(u,v\)=\(([0-9.]+),([0-9.]+)\)', txt)
    zeros['U zero m=0.1 (A,C2,C) (this run)'] = (float(mm.group(1)), float(mm.group(2)))
except Exception: pass
for nm, (u, v) in zeros.items():
    L = Mix([A, C2, C], [1-u-v, u, v])
    g, f = L.samples(1 << 14)
    for m in [0.1, 0.01]:
        rho, pU, pM = tad(g, f, m)
        print('%s m=%.2f: rho %.5f  p_U %.5f  p_M %.5f  rho+p_U %.5f  rho+p_M %.5f  (w_U %.3f, w_M %.3f)' % (nm, m, rho, pU, pM, rho+pU, rho+pM, pU/rho, pM/rho))
    # tails: exact grid 2^20 on the circle
    n = 1 << 20; k = 2*np.pi*np.arange(n)/n; a = np.where(k <= np.pi, k, 2*np.pi - k)
    idx = np.rint(a/np.pi*NF).astype(int); gg = L.sig[idx]**2
    c = np.abs(np.fft.rfft(np.sqrt(0.09 + gg)))/n
    print('   raw tails |eps_r| (m=0.3, nothing subtracted): r=128 %.2e r=256 %.2e r=512 %.2e r=1024 %.2e | v_max(0.1) %.6f v_max(0.01) %.6f'
          % (c[128], c[256], c[512], c[1024], L.vmax(0.1), L.vmax(0.01)), flush=True)
print('runtime %.1fs' % (time.time()-T0))
