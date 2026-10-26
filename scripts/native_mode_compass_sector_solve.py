"""Stationary finite open-grid selected-sector benchmark, full native H."""
import json,time,sys,os
from pathlib import Path
import numpy as np
from numba import njit,prange,set_num_threads
P=Path(__file__).resolve().parent
set_num_threads(min(4,os.cpu_count() or 1))
@njit(parallel=True)
def apply(v,flips,zs,coefs):
 out=np.empty_like(v)
 for i in prange(len(v)):
  value=0.
  for t in range(len(flips)):
   j=i^flips[t];w=j&zs[t]
   w^=w>>32;w^=w>>16;w^=w>>8;w^=w>>4
   odd=(0x6996>>(w&15))&1
   value+=coefs[t]*(1-2*odd)*v[j]
  out[i]=value
 return out

# Receipt metadata; execution is bounded by the calling primary runner.
AUDIT_TIMEOUT_SEC = 1800
