"""RL1 (I): physical translation of the noise law for the best readout (inverse of a stable local layer operator, smeared at l_k).
Diagonal-ladder variance rate (RL1_F5): z*_var = k_var * l^2/l_k^3 with k_var = sqrt(4 pi I1) = 2.8446 (RL1_F5 member 0; 3.33 for member 5) (eps = (l/l_k)^4 <= 0.1);
sd e-fold length lambda_N = 2/z*_var = (2/k_var) l_k^3/l^2.  Mean-instability of plain/smeared BD: e-fold l_k/0.3756."""
import numpy as np
lP = 1.616255e-35; kvar = 2.8446; Gpc = 3.0857e25
lam = lambda lk: (2/kvar)*lk**3/lP**2
for lk in [1e-30, 1e-25, 1e-23, 1e-21, 1e-19]:
    print("l_k = %.0e m: sd e-fold length %.2e m ; e-folds over 1 Gpc = %.2e ; BD mean e-folds over 1 Gpc = %.2e" % (lk, lam(lk), Gpc/lam(lk), 0.3756*Gpc/lk))
for D, lab in [(1.0, "1 m"), (1.496e11, "1 AU"), (Gpc, "1 Gpc")]:
    print("noise e-folds <= 1 over %-6s needs l_k >= %.2e m  (repo locality bar l_k <= 1e-19 m)" % (lab, (D*lP**2*kvar/2)**(1/3)))
