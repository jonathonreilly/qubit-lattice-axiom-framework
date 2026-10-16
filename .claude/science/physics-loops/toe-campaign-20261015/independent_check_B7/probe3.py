import numpy as np
from walks import *
from quat import x56, x62, x60
D = class_D(3)
for nm, M in [("K",x56),("S1",x62),("S2",x60)]:
    print(nm, "commutes with all D:", all(np.allclose(d@M, M@d) for d in D.values()), "M^2=", np.unique(M@M), "antisym", np.allclose(M.T,-M))
print("anticommute KS1,KS2,S1S2:", np.allclose(x56@x62+x62@x56,0), np.allclose(x56@x60+x60@x56,0), np.allclose(x62@x60+x60@x62,0))
print("K S1 = -S2:", np.allclose(x56@x62, -x60))
