"""T09 - rebuild check: does the machinery reproduce the recorded L-trend
B/B_pred = 0.009 / 0.111 / 0.502 / 0.772 at tau0=8 (plain operator)?"""
import numpy as np, sys, time; sys.path.insert(0,".")
from bridge_fit import *
AL=[0.0,1.0,-1.0,0.0]     # transverse-traceless, k along x0
print("T09  plain Delta, m=0, TT perturbation amp=0.03,  tau0=8"); print(HDR)
for L in (6,8,12,16):
    for nk in (1,2):
        for d in run(L,0.03,nk,AL,[(8.0,0.0,False)]): print(line(d), flush=True)
