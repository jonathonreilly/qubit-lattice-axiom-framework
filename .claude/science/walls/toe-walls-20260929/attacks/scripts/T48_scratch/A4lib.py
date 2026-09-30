"""A4: PMNS from the SAME universal seed R (multiplicative form), charged leptons from e,mu,tau masses, neutrinos with
normal ordering, m1 scanned.  Comparators: NuFIT-6.1 3-sigma box as quoted in the repo (T52 common.py BOX61)."""
import numpy as np, json
from common import *
BOX61 = {"s12": (0.2893, 0.3295), "s13": (0.02070, 0.02418), "s23": (0.435, 0.584)}
R_res = json.load(open("testA_results.json"))
D21, D31 = 7.42e-5, 2.515e-3   # eV^2 (comparators)
def obs(U):
    a=np.abs(U)**2; s13=a[0,2]; c13=1-s13
    return a[0,1]/c13, s13, a[1,2]/c13
def dist(o):
    d=0
    for v,k in zip(o,("s12","s13","s23")):
        lo,hi=BOX61[k]; d=max(d, (lo-v)/(hi-lo) if v<lo else (v-hi)/(hi-lo) if v>hi else 0)
    return d
