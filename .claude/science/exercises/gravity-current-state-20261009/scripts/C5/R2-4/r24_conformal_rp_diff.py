"""G3c: Frobenius difference of the OS matrices of model A (positive 4D-TT Gaussian) and B (linearised GR), q = e1."""
import numpy as np
s = open('r24_conformal_rp.py').read()
head, tail = s.split("ts = np.arange")
exec(head)
ts = np.arange(0.25, 3.01, 0.25)
Ms = {}
for name, Ch in (("B", CB), ("A", CA)):
    Cf = Ctau(Ch); n = len(comps); N = n*len(ts)
    M = np.zeros((N, N))
    for a in range(n):
        for b in range(n):
            for i, t in enumerate(ts):
                for j, tp in enumerate(ts):
                    M[a*len(ts)+i, b*len(ts)+j] = rsign[a]*complex(Cf[a][b](t+tp)).real
    Ms[name] = M
d = Ms["A"] - Ms["B"]
print("q = e1: ||M_A - M_B||_F / ||M_B||_F =", np.linalg.norm(d)/np.linalg.norm(Ms["B"]), "; max |entry diff| =", np.abs(d).max())
n = len(comps); per = [np.abs(d[a*len(ts):(a+1)*len(ts), :]).max() for a in range(n)]
order = np.argsort(per)[::-1][:5]
print("components with largest difference:", [(comps[k], round(per[k], 5)) for k in order])
