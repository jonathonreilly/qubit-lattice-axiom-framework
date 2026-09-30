"""KILL CHECK 3: the attack's 'pairing passes (1.020)' has no saved script.  Recompute sqrt(8/9)*K*r_run with the lane runner.
r_run = y_t(mu)/y_t(v) at mu = 173 (fixed) and at the self-consistent mu* (m(mu*)=mu*)."""
import numpy as np
from common import *
g0=gauge_at_v(0)
tgt=np.sqrt(4*PI*ALPHA_LM)/np.sqrt(6)
for loop in (2,3):
    yraw=ward_yt_v(tgt,g0,loop=loop)
    for lab,y in (("raw (no projection)",yraw),("physical (x sqrt(8/9))",yraw*np.sqrt(8/9))):
        for mu in (172.57,173.0):
            r=run_yt_from_v(y,g0,mu,loop=loop)[3]/y
            print(f"loop {loop} {lab}: y_t(v)={y:.4f}  r_run(v->{mu})={r:.4f}   sqrt(8/9)*K*r_run={np.sqrt(8/9)*K_SERIES*r:.4f}  K*r_run={K_SERIES*r:.4f}")
    mu,m=msbar_mass_scale(yraw*np.sqrt(8/9),g0,loop=loop)
    r=run_yt_from_v(yraw*np.sqrt(8/9),g0,mu,loop=loop)[3]/(yraw*np.sqrt(8/9))
    print(f"   self-consistent mu*={mu:.1f}: r_run={r:.4f}; pole={K_SERIES*m:.2f}; pole/(yraw v/sqrt2)= {K_SERIES*m/(yraw*V/np.sqrt(2)):.4f}; note's 172.57/169.4 = {172.57/169.4:.4f}")
print("attack quoted r_run=1.019 = repo compression script POLE_FACTOR (hard-coded 1.019)")
