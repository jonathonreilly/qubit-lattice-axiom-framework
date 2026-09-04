import numpy as np, math
from meas import report, fits
SV = [2,3,4,5,6,8,10,13,16,20,25]
for P,name in (((0,1,-1,0),"TRACELESS (0,1,-1,0)  [control]"), ((1,1,1,1),"CONFORMAL (1,1,1,1)")):
    r = report(32, P, name, eps=0.05, n=1, svals=SV)
    fits(r, 4, 16); fits(r, 5, 20); print()
