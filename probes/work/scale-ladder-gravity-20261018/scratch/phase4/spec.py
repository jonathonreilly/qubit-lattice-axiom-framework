from common import *
for nm, d in {'axis': [0,1,0,0], 'body': [1,1,1,1], 'generic': [0.3,-0.5,0.6,0.55]}.items():
    d = np.array(d, float); d /= np.linalg.norm(d)
    for s in (0.08, 0.04, 0.02):
        Q = Dc.Q(s*d); w = np.sort(np.abs(np.linalg.eigvalsh(0.5*(Q+Q.conj().T))))
        print(nm, s, ' '.join(f"{x:.1e}" for x in w[30:44]), ' max', f"{w[-1]:.1f}")
