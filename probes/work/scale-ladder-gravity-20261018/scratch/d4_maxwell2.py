import sys, numpy as np
sys.path.insert(0, '.')
from d4_maxwell import maxwell, C, gauge, lmap
from d4f import golden
kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd); ev = []
for s in (0.02, 0.01):
    Q = maxwell(s*kd); ev.append(np.sort(np.abs(np.linalg.eigvalsh(0.5*(Q+Q.conj().T)))))
print("massless (ratio 4) beyond gauge:", sum(abs(ev[0][i]/ev[1][i]-4) < 0.05 for i in range(8, 30)), "; first massive", ev[1][8:14].round(4))
def svn(k):
    s = np.sort(np.linalg.svd(maxwell(k), compute_uv=False)); return s/s[-1]
for name, n in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1), 'gen': (3,1,2)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n); km = 0.05; ks = km*n
    oms = km*np.linspace(0.998, 1.002, 201); f = np.array([svn(np.array([*ks, 1j*o]))[8:11] for o in oms])
    res = []
    for j in range(3):
        for i in range(1, 200):
            if f[i, j] < f[i-1, j] and f[i, j] < f[i+1, j] and f[i, j] < 1e-7:
                w = golden(lambda o: svn(np.array([*ks, 1j*o]))[8+j], oms[i-1], oms[i+1]); res.append(round((w*w/km**2-1)/km**2, 4))
    print(f"{name}: on-shell alphas (one per added null direction) {sorted(set(res))}")
