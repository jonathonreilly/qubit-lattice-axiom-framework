"""T4 -- headline measurement at L=64, n=1, eps=0.05.  Traceless control + conformal."""
import numpy as np
from meas import report, fits
SV = [4,6,8,10,13,16,20,25,32,40,50,64]
for P,name in (((0,1,-1,0),"TRACELESS (0,1,-1,0)  [CONTROL, immune to the c error]"),
               ((1,1,1,1),"CONFORMAL (1,1,1,1)")):
    r = report(64, P, name, eps=0.05, n=1, svals=SV, chunk=1024, verbose=True)
    fits(r, 6, 32); fits(r, 8, 50); fits(r, 10, 64); print(flush=True)
