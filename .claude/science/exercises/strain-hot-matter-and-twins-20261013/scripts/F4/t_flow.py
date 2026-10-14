import numpy as np, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f1_lib import *
F = Ferm(*ROOT, mflow=0.01)
x = np.linspace(0.01, 3.1, 156)
X = x[:, None, None]; Y = x[None, :, None]; Z = x[None, None, :20]
t0 = time.time()
Wz = F.W(Z)
fx, fy = flowF(F, X, Y, Wz, 0.003, 2)
a = F.s(fx); b = F.W(fx)
print('one flow + s,W on %d pts: %.2f s' % (fx.size, time.time() - t0))
