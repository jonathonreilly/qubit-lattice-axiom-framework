import sys, numpy as np
sys.path.insert(0, '.')
from d4h import roots
for n in [(1,2,0), (1,1,2), (2,3,6), (3,1,2)]:
    n = np.array(n, float); n /= np.linalg.norm(n); km = 0.05
    r = roots(km*n, km, 0.9985, 1.0015, 400)
    al = sorted(set(round((w*w-1)/km**2, 4) for w, nu, sh in r))
    n2 = n**2; S2 = n2[0]*n2[1] + n2[0]*n2[2] + n2[1]*n2[2]; T = n2.prod()
    pred = np.sqrt(max((1-S2)**2 - 12*T, 0))/12
    print(f"n={np.round(n,3)}: measured alphas {al}; predicted +-{pred:.4f}")
