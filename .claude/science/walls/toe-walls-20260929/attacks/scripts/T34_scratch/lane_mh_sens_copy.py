import sys, time
sys.path.insert(0,'.')
import numpy as np
import frontier_higgs_mass_full_3loop as H
PI=np.pi
g1,g2=0.464,0.648
g3=np.sqrt(4*PI*H.ALPHA_S_V_DERIVED)
t_v=np.log(H.V_DERIVED); t_pl=np.log(H.M_PL)
def mh(yt, g1=g1,g2=g2,g3=g3, lam_pl=0.0, loop=3):
    y0=[g1,g2,g3,yt,0.13]
    ypl,_=H.run_with_thresholds(y0,t_v,t_pl,loop_order=loop,apply_threshold_corrections=(loop>=2))
    y1=[ypl[0],ypl[1],ypl[2],ypl[3],lam_pl]
    yv,_=H.run_with_thresholds(y1,t_pl,t_v,loop_order=loop,apply_threshold_corrections=(loop>=2))
    lam=yv[4]
    return (np.sqrt(2*lam) if lam>0 else -np.sqrt(-2*lam))*H.V_DERIVED, ypl[3], lam
t0=time.time()
print("base yt", H.YT_V_DERIVED, mh(H.YT_V_DERIVED), time.time()-t0)
for yt in (0.85,0.9,0.9176,0.95,0.98,1.0):
    try: print(yt, mh(yt))
    except Exception as e: print(yt,'ERR',e)
