"""C2c: exponent at eta0 = 0.9 (needs E*T >= ~12 for the band to hold 90% of a T-tap mode)."""
import numpy as np
from c2lib import pareto
for E in (0.1, 0.2, 0.4):
    lns = [np.log(pareto(int(round(ET / E)), E, 0.9)[0]) for ET in (12, 16, 20, 24)]
    print(f"eta0=0.9 E={E}: ln eps* at ET=12,16,20,24 = " + " ".join(f"{v:7.2f}" for v in lns)
          + f"; c(12->20) = {-(lns[2]-lns[0])/8:.2f}")
