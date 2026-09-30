# T28 side check: what does the LITERAL reading (Wilson pure glue, a^-1 = M_Pl, beta = 6) give for Lambda_L?
import numpy as np
from scipy.optimize import brentq
b0=11/(16*np.pi**2); b1=102/(16*np.pi**2)**2
aL=lambda g2: (b0*g2)**(-b1/(2*b0**2))*np.exp(-1/(2*b0*g2))
MPl=1.221e19
print(f"a*Lambda_L at g^2=1 (beta=6): {aL(1.0):.3e}  -> Lambda_L = {aL(1.0)*MPl:.2e} GeV (a^-1 = M_Pl)")
target=0.2/MPl
g2=brentq(lambda x: np.log(aL(x))-np.log(target),0.05,1.0)
print(f"g^2 needed for Lambda_L = 0.2 GeV: {g2:.4f}, beta = 6/g^2 = {6/g2:.1f}")
