import numpy as np
from k1_function_space import O, rho
dirs=[tuple(v) for v in np.vstack([np.eye(3,dtype=int),-np.eye(3,dtype=int)])]
for kind in ['trivial','sign','axis','full']:
    ker=[g for g in O if np.allclose(rho(kind,g),np.eye(3))]
    orb=set()
    for d in dirs:
        orb.add(frozenset(tuple(g@np.array(d)) for g in ker))
    print(f'{kind:8s} |kernel|={len(ker):2d}  kernel orbits on the 6 bond directions: {len(orb)} sizes {sorted(len(o) for o in orb)}')
