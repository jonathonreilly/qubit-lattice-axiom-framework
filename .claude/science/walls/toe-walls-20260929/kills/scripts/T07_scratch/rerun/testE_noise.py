"""Test E: price of forgetting -- add symmetric Metropolis noise gamma*min(1,P_y/P_x) (detailed balance with P_t,
so |psi|^2 stays exactly stationary-equivariant).  Scan gamma for the hardest starts of Test B."""
import os, sys, json
import numpy as np
import testB_protocol as B
cap = float(os.environ.get('RATE_CAP', '1e5'))
for m in B.models.values(): m.cap = cap
names = sys.argv[1].split(',') if len(sys.argv) > 1 else ['3 shifted by 2']
gammas = [0.0, 0.03, 0.1, 0.3, 1.0, 3.0]
out = []
# equivariance control with noise on
r = B.analyse('0 equilibrium', B.starts['0 equilibrium'], gamma=1.0, verbose=False)
print('control (equilibrium start, gamma=1): max|rho_8-P_8| = %.2e' % r['maxdiff_eq'], flush=True)
for nm in names:
    for g in gammas:
        r = B.analyse(nm, B.starts[nm], gamma=g)
        out.append(r)
json.dump(out, open('testE_results.json', 'w'), indent=1)
