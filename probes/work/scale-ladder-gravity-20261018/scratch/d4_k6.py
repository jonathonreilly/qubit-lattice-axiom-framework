import sys, numpy as np
sys.path.insert(0, '.')
from d4_maxwell import maxwell
from d4e import on_shell
from d4f import golden
def svn(k):
    s = np.sort(np.linalg.svd(maxwell(k), compute_uv=False)); return s/s[-1]
print(" dir    |k|   scalar beta   photon beta (nullity at root)   [omega^2 = k^2(1 + alpha k^2 + beta k^4)]")
for name, n in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1), 'gen': (3,1,2)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n)
    for km in (0.3, 0.2):
        ks = km*n
        kS, _, _ = on_shell(ks, 1j*km); bs = (abs(kS[3])**2/km**2 - 1)/km**4
        oms = km*np.linspace(0.97, 1.03, 241); f = [svn(np.array([*ks, 1j*o]))[8] for o in oms]; i = int(np.argmin(f))
        w = golden(lambda o: svn(np.array([*ks, 1j*o]))[8], oms[max(i-1,0)], oms[min(i+1,240)])
        nul = int((svn(np.array([*ks, 1j*w])) < 1e-9).sum()); bp = (w*w/km**2 - 1)/km**4
        print(f" {name:5s} {km:.1f}   {bs:+.5f}      {bp:+.5f} ({nul})")
